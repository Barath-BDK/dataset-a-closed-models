#!/usr/bin/env python3
"""Validates the file of one package against the specification and its brief (section 11 checklist).

    python tools/validate.py P05_gemini_python [--draft]

--draft   rows are not verified yet: label_source, label_confidence and the final-pass note may still be empty.
Reads  submissions/<package>/<package>.jsonl  (or .xlsx).  Prints a count table and the problems; exit code 1 if there is any error.
"""
import argparse, ast, collections, json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import qa
import spec as S


def load(path):
    if path.endswith(".jsonl"):
        return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    import openpyxl
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)["rows"]
    it = ws.iter_rows(values_only=True)
    head = [h for h in next(it)]
    return [{h: ("" if v is None else v) for h, v in zip(head, vals)} for vals in it if any(v not in (None, "") for v in vals)]


def parse_lines(v):
    if v in ("", None):
        return None
    try:
        x = json.loads(v) if isinstance(v, str) else v
    except Exception:
        return "bad"
    if isinstance(x, int):
        return [x]
    return x if isinstance(x, list) and all(isinstance(i, int) for i in x) else "bad"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package")
    ap.add_argument("--draft", action="store_true")
    a = ap.parse_args()
    briefs = {r["sample_id"]: r for r in (json.loads(l) for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8")) if r["package"] == a.package}
    if not briefs:
        sys.exit(f"unknown package {a.package!r}")
    base = os.path.join(ROOT, "submissions", a.package)
    path = os.path.join(base, f"{a.package}.jsonl")
    if not os.path.exists(path):
        path = os.path.join(base, f"{a.package}.xlsx")
    rows = load(path)
    errs, warns = [], []
    E = lambda rid, m: errs.append((rid, m))
    W = lambda rid, m: warns.append((rid, m))
    seen = collections.Counter(r.get("sample_id") for r in rows)
    keys = {}
    expected_model = next(iter(briefs.values()))["model"]
    for r in rows:
        rid = r.get("sample_id") or "(no id)"
        b = briefs.get(rid)
        if seen[rid] > 1:
            E(rid, "sample_id used more than once")
        if not b:
            E(rid, "sample_id is not in this package's brief")
            continue
        for k in S.ALL_COLUMNS:
            if k not in r:
                E(rid, f"column {k} missing")
        if list(r.keys())[:len(S.ALL_COLUMNS)] != S.ALL_COLUMNS:
            E(rid, "columns are not the 30 required columns in the required order")
        for k in ("language", "cwe", "case_type", "pattern", "group_id"):
            exp = b[k if k != "group_id" else "group_id"]
            if r.get(k) != exp:
                E(rid, f"{k} is {r.get(k)!r}; the brief says {exp!r}")
        vuln = r.get("case_type") in S.VULNERABLE_CASES
        if r.get("label") != (1 if vuln else 0):
            E(rid, "label does not match case_type")
        code = r.get("code") or ""
        n = len(code.splitlines())
        if r.get("n_lines") != n:
            E(rid, f"n_lines {r.get('n_lines')} but the code has {n} lines")
        if r.get("band") != S.band_of(n):
            E(rid, f"band {r.get('band')} but {n} lines is band {S.band_of(n)}")
        if r.get("n_tokens") not in ("", None):
            W(rid, "n_tokens should be empty")
        if r.get("origin") != "synthetic":
            E(rid, "origin must be synthetic")
        if r.get("suggested_split") != "train":
            E(rid, "suggested_split must be train")
        gen = str(r.get("generator") or "")
        if not gen:
            E(rid, "generator is empty (write the exact model name)")
        elif S.MODEL_TITLE[expected_model].lower() not in gen.lower():
            W(rid, f"generator {gen!r} does not look like {S.MODEL_TITLE[expected_model]}")
        if not r.get("prompt_id"):
            E(rid, "prompt_id is empty")
        if S.band_of(n) != b["band"]:
            W(rid, f"band {S.band_of(n)} differs from the brief's {b['band']}")
        if vuln:
            fixed = r.get("fixed_code") or ""
            if not fixed.strip():
                E(rid, "vulnerable row has no fixed_code")
            elif qa.changed_lines(code, fixed) > S.MAX_FIX_LINES:
                E(rid, f"fixed_code changes more than {S.MAX_FIX_LINES} lines")
            vl = parse_lines(r.get("vulnerable_lines"))
            if vl is None or vl == "bad" or not vl:
                E(rid, "vulnerable_lines must be a list like [2, 3, 5]")
            elif any(x < 1 or x > n for x in vl):
                E(rid, f"vulnerable_lines {vl} outside 1..{n}")
            if not r.get("fix_type"):
                E(rid, "vulnerable row has no fix_type")
        else:
            for k in ("fixed_code", "vulnerable_lines", "fix_type"):
                if r.get(k) not in ("", None):
                    E(rid, f"safe row must leave {k} empty")
        if r.get("case_type") == "no_code" and r.get("sink"):
            E(rid, "no_code row must leave sink empty")
        ls, lc = r.get("label_source") or "", r.get("label_confidence") or ""
        if not a.draft:
            if ls not in S.LABEL_SOURCES:
                E(rid, f"label_source must be one of {S.LABEL_SOURCES}")
            if lc not in S.CONFIDENCE:
                E(rid, "label_confidence must be high or medium (set by the final Claude pass)")
            if "judge:" not in str(r.get("notes") or ""):
                E(rid, "notes has no final-pass verdict (judge: claude-<version> ...)")
        if ls == "dynamic_exploit":
            if r.get("cwe") == "CWE-338":
                E(rid, "CWE-338 cannot be dynamic_exploit")
            if r.get("runnable") != 1:
                E(rid, "dynamic_exploit needs runnable = 1")
            if vuln and (r.get("exploit_confirmed") != 1 or r.get("fix_resists_exploit") != 1):
                E(rid, "dynamic_exploit on a vulnerable row needs exploit_confirmed = 1 and fix_resists_exploit = 1")
            if not vuln and r.get("exploit_confirmed") != 0:
                E(rid, "dynamic_exploit on a safe row needs exploit_confirmed = 0")
        if r.get("case_type") != "no_code" and r.get("sink") and qa.sink_token(r["sink"]) not in code:
            W(rid, f"sink {r['sink']!r} does not appear in the code")
        if qa.LEAK.search(code) or qa.LEAK.search(str(r.get("task_description") or "")):
            W(rid, "a word that hints at the label appears in the code or the task sentence")
        if r.get("language") == "python":
            for name, c in (("code", code), ("fixed_code", r.get("fixed_code") or "")):
                if c.strip():
                    try:
                        ast.parse(textwrap.dedent(c))
                    except SyntaxError as e:
                        E(rid, f"{name} is not valid Python: {e.msg}")
        k = (r.get("language"), re.sub(r"\s+", "", code))
        if k in keys and keys[k] != rid:
            E(rid, f"exact duplicate of {keys[k]}")
        keys[k] = rid
    # duplicates against the other packages already in the repository
    others = {}
    sub = os.path.join(ROOT, "submissions")
    for d in sorted(os.listdir(sub)):
        f = os.path.join(sub, d, f"{d}.jsonl")
        if d != a.package and os.path.exists(f):
            for line in open(f, encoding="utf-8"):
                if line.strip():
                    o = json.loads(line)
                    others[(o["language"], re.sub(r"\s+", "", o.get("code") or ""))] = o["sample_id"]
    for r in rows:
        k = (r.get("language"), re.sub(r"\s+", "", r.get("code") or ""))
        if k in others:
            E(r.get("sample_id"), f"exact duplicate of {others[k]} in another package")
    missing = [i for i in briefs if i not in {r.get("sample_id") for r in rows}]
    cnt = collections.Counter
    print(f"# Validation: {a.package}  ({len(rows)} of {len(briefs)} rows delivered{', draft mode' if a.draft else ''})\n")
    print("rows per weakness and case type (delivered / brief):")
    exp = cnt((b["cwe"], b["case_type"]) for b in briefs.values())
    got = cnt((r.get("cwe"), r.get("case_type")) for r in rows)
    print("  " + " ".join(f"{c:14s}" for c in ["weakness"] + S.CASE_TYPES))
    for w in S.CWES:
        if any(exp[(w, c)] for c in S.CASE_TYPES):
            print("  " + " ".join(f"{x:14s}" for x in [w] + [f"{got[(w, c)]}/{exp[(w, c)]}" for c in S.CASE_TYPES]))
    print("length bands:", dict(cnt(r.get("band") for r in rows)), "(brief:", dict(cnt(b["band"] for b in briefs.values())), ")")
    print("label sources:", dict(cnt(r.get("label_source") or "(empty)" for r in rows)))
    for w in ("CWE-89", "CWE-78", "CWE-22"):
        rs = [r for r in rows if r.get("cwe") == w]
        if rs:
            share = sum(1 for r in rs if r.get("label_source") == "dynamic_exploit") / len(rs)
            print(f"  {w}: {share:.0%} dynamic_exploit (target at least 60%)")
    if missing:
        print(f"\nrows not in the file: {len(missing)}  e.g. {', '.join(missing[:6])}")
    print(f"\nERRORS ({len(errs)})")
    grouped = collections.defaultdict(list)
    for rid, m in errs:
        grouped[re.sub(r"\d+", "#", m)[:90]].append((rid, m))
    for k, items in grouped.items():
        print(f"- {items[0][1]}  ({len(items)} rows: {', '.join(i[0] for i in items[:6])}{' ...' if len(items) > 6 else ''})")
    print(f"\nWARNINGS ({len(warns)})")
    grouped = collections.defaultdict(list)
    for rid, m in warns:
        grouped[re.sub(r"\d+", "#", m)[:90]].append((rid, m))
    for k, items in grouped.items():
        print(f"- {items[0][1]}  ({len(items)} rows)")
    sys.exit(1 if errs or missing else 0)


if __name__ == "__main__":
    main()
