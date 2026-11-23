#!/usr/bin/env python3
"""Builds, for every package, the two files a person works with:

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
             "",
             "**Order:** first do the **STEP 1 first issue (rows 001 to 005, five prompts, they count towards your 100)** and hand it in, so the lead can tell you if you are doing it right. Only then do the rest (STEP 2)." if n == 100 else "",
             "6. When you finish, check your answers with Claude (see the README, step 5) and hand in the one file.", "",
             "Do not change the model's answer. Do not leave out rows. If a row goes wrong, ask the same row again in a new chat and replace the answer.", "",
             "---", "",
             "## MASTER PROMPT (paste this first in every new chat)", "",
             "````text", mp, "````", "", "---", ""]
        warm = n == 100
        groups = ([rs[:5]] if warm else []) + [rs[i:i + 10] for i in range(5 if warm else 0, n, 10)]
        for gi, chunk in enumerate(groups, 1):
            a, z = chunk[0]["row_no"], chunk[-1]["row_no"]
            if warm and gi == 1:
                L += [f"# 🟩 STEP 1: YOUR FIRST ISSUE. DO THIS FIRST (rows {a:03d} to {z:03d}, only 5 prompts, they count towards your 100)", "",
                      "**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → paste these 5 rows one by one → paste each answer into your hand-in file.** "
                      "Then hand in these 5 rows with a pull request (README, section 3) and wait for the lead's reply before you continue with CHAT 2.", ""]
            else:
                k = gi - 1 if warm else gi
                tot = len(groups) - 1 if warm else len(groups)
                L += [f"# 🟦 STEP 2: CHAT {k} of {tot}: rows {a:03d} to {z:03d}" if warm else f"# 🟦 CHAT {k} of {tot}: rows {a:03d} to {z:03d}", "",
                      "**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**", ""]
            for r in chunk:
                L += [f"### ▶ ROW {r['row_no']:03d} &nbsp;·&nbsp; {r['cwe']} &nbsp;·&nbsp; {r['case_type']}",
                      f"Save the answer under `=== {r['row_no']:03d}`", "", "```text", r["prompt"], "```", ""]
            L += ["---", ""]
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
