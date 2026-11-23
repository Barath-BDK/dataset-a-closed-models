#!/usr/bin/env python3
"""Applies the final Claude verdicts (section 8.1) to the package file.

    python tools/apply_judge.py P05_gemini_python --judge-version "claude-<version>"

Reads   submissions/<package>/<package>.jsonl and submissions/<package>/judge/replies/<row_no>.json
Writes  the same .jsonl and .xlsx with `notes` (judge: claude-<version> agrees / disagrees ...) and `label_confidence` set:
          label_source dynamic_exploit and Claude agrees  -> high
          label_source two_reviewers or by_design and Claude agrees -> medium
          Claude disagrees -> label_confidence stays empty and the row is listed: a person re-checks it (keep as medium with a note, fix the label, or drop the row)
        Rows written by Claude itself that were not checked by running the code are listed for a person to re-check even when Claude agrees.
Claude's verdict alone never sets high. If Claude's vulnerable_lines differ from the row's, a person decides which lines are right.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import spec as S


def read_json(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    dec, i = json.JSONDecoder(), 0
    while True:
        i = text.find("{", i)
        if i < 0:
            return None
        try:
            obj, _ = dec.raw_decode(text, i)
        except ValueError:
            i += 1
            continue
        if isinstance(obj, dict) and "verdict" in obj:
            return obj
        i += 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package")
    ap.add_argument("--judge-version", required=True)
    a = ap.parse_args()
    base = os.path.join(ROOT, "submissions", a.package)
    rows = [json.loads(l) for l in open(os.path.join(base, f"{a.package}.jsonl"), encoding="utf-8") if l.strip()]
    briefs = {r["sample_id"]: r for r in (json.loads(l) for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8")) if r["package"] == a.package}
    disagree, recheck, nolabel, nojudge, linediff = [], [], [], [], []
    for r in rows:
        b = briefs[r["sample_id"]]
        o = read_json(os.path.join(base, "judge", "replies", f"{b['row_no']:03d}.json"))
        if o is None:
            nojudge.append(r["sample_id"])
            continue
        verdict_vuln = str(o.get("verdict", "")).lower().startswith("vuln")
        agrees = verdict_vuln == (r["label"] == 1)
        ls = r.get("label_source") or ""
        notes = re.sub(r"judge:[^;]*;?\s*", "", str(r.get("notes") or "")).strip("; ")
        tag = f"judge: {a.judge_version} {'agrees' if agrees else 'DISAGREES'} ({o.get('verdict')})"
        if o.get("reason"):
            tag += f" - {str(o['reason'])[:160]}"
        jl = o.get("vulnerable_lines") or []
        if agrees and r["label"] == 1:
            mine = json.loads(r["vulnerable_lines"]) if r.get("vulnerable_lines") else []
            if sorted(jl) != sorted(mine):
                tag += f"; judge lines {jl} differ from {mine}: a person decides"
                linediff.append(r["sample_id"])
        r["notes"] = (notes + "; " if notes else "") + tag
        if not ls:
            nolabel.append(r["sample_id"])
        if agrees:
            r["label_confidence"] = "high" if ls == "dynamic_exploit" else ("medium" if ls else "")
            if b["model"] == "claude" and ls != "dynamic_exploit":
                recheck.append(r["sample_id"])
        else:
            r["label_confidence"] = ""
            disagree.append(r["sample_id"])
    with open(os.path.join(base, f"{a.package}.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
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
        ws.append([r.get(c, "") for c in S.ALL_COLUMNS])
    wb.save(os.path.join(base, f"{a.package}.xlsx"))
    print(f"{len(rows)} rows; judge replies missing for {len(nojudge)}")
    print(f"- Claude disagrees ({len(disagree)}): a person re-checks: {', '.join(disagree[:10])}")
    print(f"- Claude's own rows that agree but were not run ({len(recheck)}): a person re-checks every one: {', '.join(recheck[:10])}")
    print(f"- vulnerable_lines differ ({len(linediff)}): a person decides: {', '.join(linediff[:10])}")
    if nolabel:
        print(f"- label_source is still empty for {len(nolabel)} rows (set it first, section 8): {', '.join(nolabel[:10])}")


if __name__ == "__main__":
    main()
