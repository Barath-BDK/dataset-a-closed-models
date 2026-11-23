#!/usr/bin/env python3
"""Builds, for every package, the two files a person works with:

    MY_PROMPTS/<package>.md       all prompts of the package in ONE file (master prompt on top, then chat 1 ... chat 10)
    submissions/<package>.txt     the ONE file the person hands in: an empty form with a line '=== 001' ... for every row

Run from the repository root after tools/make_briefs.py. Never overwrites a submission file that already has content.
"""
import json, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = {"chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude"}
LANG = {"python": "Python", "c": "C", "cpp": "C++", "go": "Go"}


def master_prompt():
    t = open(os.path.join(ROOT, "prompts", "MASTER_PROMPT.md"), encoding="utf-8").read()
    m = re.search(r"````text\n(.*?)\n````", t, re.S)
    return m.group(1)


def main():
    rows = [json.loads(l) for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8") if l.strip()]
    pk = collections.OrderedDict()
    for r in rows:
        pk.setdefault(r["package"], []).append(r)
    mp = master_prompt()
    os.makedirs(os.path.join(ROOT, "MY_PROMPTS"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "submissions"), exist_ok=True)
    for pkg, rs in pk.items():
        m, lang = MODEL[rs[0]["model"]], LANG[rs[0]["language"]]
        n = len(rs)
        nb = max(r["batch"] for r in rs)
        L = [f"# {pkg.split('_')[0]} · {m} · {lang} · {n} prompts", "",
             "> **This one file has everything you need to paste.** Your answers go into ONE other file: "
             f"[`submissions/{pkg}.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/{pkg}.txt).", "",
             "## What to do (the short version)", "",
             f"1. Open **{m}** (the free base model). Start a **new chat**.",
             "2. Copy the **MASTER PROMPT** below (the copy button is in the top right corner of the box) and paste it into the chat. Wait until the model answers `ready`.",
             "3. Copy **ROW 001**, paste it into the chat. The model answers with a block of JSON.",
             f"4. Copy the whole answer and paste it into `submissions/{pkg}.txt` **under the line `=== 001`**.",
             "5. Do the same for the next rows. **After 10 rows, start a new chat** and paste the MASTER PROMPT again (the file tells you where).",
             "6. When you finish, check your answers with Claude (see the README, step 5) and hand in the one file.", "",
             "Do not change the model's answer. Do not leave out rows. If a row goes wrong, ask the same row again in a new chat and replace the answer.", "",
             "---", "",
             "## MASTER PROMPT (paste this first in every new chat)", "",
             "````text", mp, "````", "", "---", ""]
        for b in range(1, nb + 1):
            chunk = [r for r in rs if r["batch"] == b]
            a, z = chunk[0]["row_no"], chunk[-1]["row_no"]
            L += [f"# 🟦 CHAT {b} of {nb}: rows {a:03d} to {z:03d}", "",
                  f"**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**", ""]
            for r in chunk:
                L += [f"### ▶ ROW {r['row_no']:03d} &nbsp;·&nbsp; {r['cwe']} &nbsp;·&nbsp; {r['case_type']}",
                      f"Save the answer under `=== {r['row_no']:03d}`", "", "```text", r["prompt"], "```", ""]
            L += ["---", ""]
        open(os.path.join(ROOT, "MY_PROMPTS", f"{pkg}.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))
        sub = os.path.join(ROOT, "submissions", f"{pkg}.txt")
        if not os.path.exists(sub) or not open(sub, encoding="utf-8").read().strip():
            S = [f"HAND-IN FILE FOR {pkg}  ({m}, {lang}, {n} rows)",
                 "Paste the model's answer for each row under its line. Do not delete the '=== NNN' lines. Keep the answers exactly as the model wrote them.",
                 "If a row could not be made, write SKIP and the reason under its line.", ""]
            for r in rs:
                S += [f"=== {r['row_no']:03d}", "", ""]
            open(sub, "w", encoding="utf-8", newline="\n").write("\n".join(S))
    print(len(pk), "packages")


if __name__ == "__main__":
    main()
