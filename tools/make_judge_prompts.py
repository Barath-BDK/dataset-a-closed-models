#!/usr/bin/env python3
"""Final label pass with Claude (section 8.1): writes the judge prompts, 10 rows per chat.

    python tools/make_judge_prompts.py P05_gemini_python

Reads   submissions/<package>/<package>.jsonl
Writes  submissions/<package>/judge/batch_NN.md   (ten prompts per file: open a NEW Claude chat for each file)
Each prompt shows only the language, the weakness and the numbered code. It does not show the label, the model that wrote the row, or fixed_code.
Save each Claude reply as submissions/<package>/judge/replies/<row_no>.json (the number is in the heading of the prompt), then run tools/apply_judge.py.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import qa
import spec as S

NAME = {"CWE-89": "SQL injection", "CWE-78": "OS command injection", "CWE-22": "Path traversal", "CWE-338": "Weak random generator"}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pkg = sys.argv[1]
    base = os.path.join(ROOT, "submissions", pkg)
    rows = [json.loads(l) for l in open(os.path.join(base, f"{pkg}.jsonl"), encoding="utf-8") if l.strip()]
    briefs = {r["sample_id"]: r for r in (json.loads(l) for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8")) if r["package"] == pkg}
    out = os.path.join(base, "judge")
    os.makedirs(os.path.join(out, "replies"), exist_ok=True)
    rows.sort(key=lambda r: briefs[r["sample_id"]]["row_no"])
    for b in range(0, len(rows), 10):
        chunk = rows[b:b + 10]
        parts = [f"# Final pass, batch {b // 10 + 1}", "", "Open a NEW Claude chat (use the Claude version written in `config.yml`). Paste the prompts below one at a time. "
                 "Save each reply as `replies/<row_no>.json`.", ""]
        for r in chunk:
            no = briefs[r["sample_id"]]["row_no"]
            parts += [f"## Row {no:03d} · `{r['sample_id']}`", "", "```text",
                      f"Here is a {S.LANG_TITLE[r['language']]} function. Lines are numbered.",
                      qa.numbered(r["code"]),
                      f"Question: is this function vulnerable to {NAME[r['cwe']]} ({r['cwe']})?",
                      "Reply with JSON only:",
                      '{"verdict": "vulnerable" or "safe",', ' "vulnerable_lines": [line numbers, empty if safe],', ' "reason": "one sentence"}', "```", ""]
        open(os.path.join(out, f"batch_{b // 10 + 1:02d}.md"), "w", encoding="utf-8").write("\n".join(parts))
    print(f"{len(rows)} judge prompts in {(len(rows) + 9) // 10} files: {os.path.join('submissions', pkg, 'judge')}")


if __name__ == "__main__":
    main()
