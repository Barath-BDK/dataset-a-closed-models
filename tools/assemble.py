#!/usr/bin/env python3
"""Turns the model replies of one package into the 30-column file.

    python tools/assemble.py P05_gemini_python --generator "Gemini 2.5 Pro" [--prompt-id P1-t0.7]

Reads   submissions/<package>.txt   (ONE file: every reply pasted under a line '=== 001', '=== 002' ...)
        or submissions/<package>/replies/001.json, 002.json ...   (the model's JSON reply for row 1, 2 ...; code fences and text around the JSON are ignored)
Writes  submissions/<package>/<package>.xlsx and .jsonl         rows that passed the QA checks, all 30 columns, label_source / label_confidence still empty
        submissions/<package>/qa_report.md                       what is missing, which rows must be generated again and why
Nothing is taken from the model except the content keys; weakness, language, case type, label, input source, pattern, fix type and group come from the brief.
"""
import argparse, collections, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import qa
import spec as S


def load_briefs(package):
    rows = [json.loads(l) for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8") if l.strip()]
    rows = [r for r in rows if r["package"] == package]
    if not rows:
        sys.exit(f"unknown package {package!r}; see the folder names in packages/")
    return {r["row_no"]: r for r in rows}


def read_json(path):
    return parse_text(open(path, encoding="utf-8", errors="replace").read())


def split_single_file(path):
    """submissions/<package>.txt: replies pasted under lines like '=== 001'. Returns {row_no: text}."""
    import re
    out, cur = {}, None
    for line in open(path, encoding="utf-8", errors="replace").read().splitlines():
        m = re.match(r"^\s*===\s*(\d+)", line)
        if m:
            cur = int(m.group(1))
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return {k: chr(10).join(v) for k, v in out.items()}


def parse_text(text):
    dec = json.JSONDecoder()
    i = 0
    while True:
        i = text.find("{", i)
        if i < 0:
            return None
        try:
            obj, _ = dec.raw_decode(text, i)
        except ValueError:
            i += 1
            continue
        if isinstance(obj, dict) and "code" in obj:
            return obj
        i += 1


def norm_lines(v):
    if v in (None, "", []):
        return ""
    if isinstance(v, str):
        import re
        v = [int(t) for t in re.findall(r"\d+", v)]
    if isinstance(v, int):
        v = [v]
    return json.dumps([int(x) for x in v])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package")
    ap.add_argument("--generator", required=True, help="exact model name and version, for example 'Gemini 2.5 Pro'")
    ap.add_argument("--prompt-id", default="P1-t0.7")
    a = ap.parse_args()
    briefs = load_briefs(a.package)
    base = os.path.join(ROOT, "submissions", a.package)
    rep_dir = os.path.join(base, "replies")
    os.makedirs(rep_dir, exist_ok=True)
    rows, report = [], []
    missing, unreadable = [], []
    single = os.path.join(ROOT, "submissions", a.package + ".txt")
    texts = split_single_file(single) if os.path.exists(single) else {}
    for no, b in sorted(briefs.items()):
        path = os.path.join(rep_dir, f"{no:03d}.json")
        if os.path.exists(path):
            o = read_json(path)
        elif no in texts and texts[no].strip() and not texts[no].strip().upper().startswith("SKIP"):
            o = parse_text(texts[no])
        else:
            missing.append(no)
            continue
        if o is None:
            unreadable.append(no)
            continue
        hard, soft, notes = qa.check(o, b)
        report.append((no, b, hard, soft, notes))
        if hard:
            continue
        vuln = b["case_type"] in S.VULNERABLE_CASES
        note = ["draft: labels not verified yet"] + ([o["_note"]] if o.get("_note") else []) + [x for x in notes if x.startswith("length")]
        row = {c: "" for c in S.ALL_COLUMNS}
        n = len(o["code"].rstrip().splitlines())
        row.update(sample_id=b["sample_id"], language=b["language"], cwe=b["cwe"], case_type=b["case_type"], label=1 if vuln else 0,
                   task_description=(o.get("task_description") or b["task"]).strip(), cwe_detail=(o.get("cwe_detail") or "none") if b["case_type"] != "no_code" else "none",
                   n_lines=n, band=S.band_of(n), build_style=(o.get("build_style") or "none") if b["case_type"] != "no_code" else "none", source=b["source"],
                   fix_type=b.get("fix_type", "") if vuln else "", code=o["code"].rstrip(), fixed_code=(o.get("fixed_code") or "").rstrip() if vuln else "",
                   vulnerable_lines=norm_lines(o.get("vulnerable_lines")) if vuln else "", sink=(o.get("sink") or "") if b["case_type"] != "no_code" else "",
                   pattern=b["pattern"], group_id=b["group_id"], origin="synthetic", suggested_split="train", generator=a.generator, prompt_id=a.prompt_id,
                   notes="; ".join(note))
        rows.append(row)
    jl = os.path.join(base, f"{a.package}.jsonl")
    with open(jl, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    import openpyxl
    from openpyxl.styles import Font
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "rows"
    ws.append(S.ALL_COLUMNS)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in rows:
        ws.append([r[c] for c in S.ALL_COLUMNS])
    wb.save(os.path.join(base, f"{a.package}.xlsx"))
    lines = [f"# QA report: {a.package}", "", f"- replies read: {len(report) + len(unreadable)} of {len(briefs)} rows; **written to the file: {len(rows)}**",
             f"- rows without a reply yet: {len(missing)}" + (f" ({', '.join(f'{m:03d}' for m in missing[:20])}{' ...' if len(missing) > 20 else ''})" if missing else ""),
             f"- replies that contain no readable JSON: {', '.join(f'{m:03d}' for m in unreadable) if unreadable else 'none'}", ""]
    held = [r for r in report if r[2]]
    lines.append(f"## Rows to generate again ({len(held)})\n")
    lines.append("Generate each one again in a NEW chat (master prompt first, then that row's prompt from `packages/" + a.package + "/batch_NN.md`), save the reply over the same file, and run this script again.\n")
    for no, b, hard, soft, notes in held:
        lines.append(f"- **{no:03d}** `{b['sample_id']}` ({b['case_type']}): " + "; ".join(hard))
    lines += ["", "## Notes (rows were kept)", ""]
    for no, b, hard, soft, notes in report:
        if not hard and (soft or notes):
            lines.append(f"- {no:03d} `{b['sample_id']}`: " + "; ".join(soft + notes))
    open(os.path.join(base, "qa_report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{len(rows)} rows written, {len(held)} to generate again, {len(missing)} without a reply, {len(unreadable)} unreadable")
    print("see", os.path.join("submissions", a.package, "qa_report.md"))


if __name__ == "__main__":
    main()
