#!/usr/bin/env python3
"""Builds the issue texts.

P01-P11: a Step 1 issue (rows 001-005, the prompts are in the issue text) and a Step 2 issue (rows 006-100, the prompts are posted as comments, 10 per comment = one chat).
P12a-d: one issue each (25 rows, the prompts are posted as comments, 10 per comment).
Writes issues/<package>.md (Step 2 or P12), issues/<package>_first.md (Step 1), issues/comments/<package>/NN.md and issues/titles.csv.
GitHub issue numbers: 1-15 are Step 2 / P12 issues in the order of assignments_filled.csv, 16-26 are the Step 1 issues of P01-P11.
"""
import csv, json, os, re, shutil, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/"
MODEL = {"chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude"}
LANG = {"python": "Python", "c": "C", "cpp": "C++", "go": "Go"}


def master_prompt():
    t = open(os.path.join(ROOT, "prompts", "MASTER_PROMPT.md"), encoding="utf-8").read()
    return re.search(r"````text\n(.*?)\n````", t, re.S).group(1)


def prompt_block(r):
    return [f"### ▶ ROW {r['row_no']:03d} &nbsp;·&nbsp; {r['cwe']} &nbsp;·&nbsp; {r['case_type']}",
            f"Paste the answer under `=== {r['row_no']:03d}` in your hand-in file.", "", "```text", r["prompt"], "```", ""]


def main():
    assign = list(csv.DictReader(open(os.path.join(ROOT, "assignments_filled.csv"), encoding="utf-8-sig")))
    user_of = {a["package"]: a["github_username"] for a in assign}
    number_of = {a["package"]: i + 1 for i, a in enumerate(assign)}
    mine = collections.defaultdict(list)
    for a in assign:
        mine[a["github_username"]].append(a["package"])
    briefs = collections.defaultdict(list)
    for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            briefs[r["package"]].append(r)
    mp = master_prompt()
    cdir = os.path.join(ROOT, "issues", "comments")
    shutil.rmtree(cdir, ignore_errors=True)
    out = []
    for pkg, rs in briefs.items():
        user = user_of[pkg]
        m, lang = MODEL[rs[0]["model"]], LANG[rs[0]["language"]]
        pid = pkg.split("_")[0]
        full = len(rs) == 100
        n_steps = len(mine[user]) + (1 if len(briefs[mine[user][0]]) == 100 else 0)
        hand = f"{URL}submissions/{pkg}.txt"
        links = ["| | |", "|---|---|",
                 f"| **Your hand-in file (the only file you hand in)** | [`submissions/{pkg}.txt`]({hand}) |",
                 f"| **How to do it** | [`README.md`]({URL}README.md) |",
                 f"| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`]({URL}prompts/CLAUDE_CHECK_PROMPT.md) |", ""]
        master = ["## 1. The MASTER PROMPT (paste this first in every new chat)", "",
                  "Copy it with the copy button in the corner of the box. The AI must answer `ready`.", "", "````text", mp, "````", ""]
        branch = lambda tag: f"`issue/<this issue number>-{tag}`"
        if full:
            first, rest = rs[:5], rs[5:]
            wnum = 15 + int(pid[1:])
            W = [f"## 🟩 STEP 1 of {n_steps}: THIS IS YOUR FIRST ISSUE. RESOLVE IT FIRST", "",
                 f"**Assigned to: {user}.** This is the **first issue you must resolve**, before any other issue. It is only **5 prompts** (rows 001 to 005 of {m} × {lang}). "
                 "**These 5 rows are real rows: they count towards your 100** and are part of the final dataset. They come first so that the lead can check your format after 5 rows and you learn the routine before the big job.", "",
                 *links,
                 "## What to do", "",
                 "1. Read the `README.md` (set-up, personal branch) and make your issue branch from your personal branch.",
                 f"2. Open a **new chat** with **{m}** (the free base model).",
                 "3. Paste the **MASTER PROMPT** (section 1 below). Wait for the answer `ready`.",
                 "4. Paste **ROW 001** (section 2 below). Copy the whole answer into your hand-in file under `=== 001`. Then ROW 002, and so on to ROW 005.",
                 "5. Check the 5 answers with Claude (README section 4, Check A and Check B).",
                 f"6. Commit `submissions/{pkg}.txt` with rows 001 to 005 filled, open a pull request into your personal branch `dev/{user}`, write the exact model name in it, and ask the lead for review. Branch name: {branch('first')}.",
                 f"7. **Wait for the lead's OK**, then start Step 2 (issue #{number_of[pkg]}). Rows 006 to 100 go in the same file.", "",
                 "- [ ] Master prompt pasted, answered `ready`", "- [ ] Rows 001 to 005 pasted under their lines", "- [ ] Check A and B done", "- [ ] Pull request opened, lead's OK received (only then start Step 2)", "",
                 "---", ""] + master + ["---", "", "## 2. Your 5 prompts", ""]
            for r in first:
                W += prompt_block(r)
            open(os.path.join(ROOT, "issues", f"{pkg}_first.md"), "w", encoding="utf-8").write("\n".join(W))
            out.append([wnum, f"[{user} · Step 1 of {n_steps} · FIRST ISSUE, DO THIS FIRST] {pid} {m} x {lang}: rows 001-005 (5 rows)", f"{pkg}_first.md",
                        f"first-issue,model:{rs[0]['model']},lang:{rs[0]['language']}", user])
            body_rows = rest
            title = f"[{user} · Step 2 of {n_steps}] {pid} {m} x {lang}: rows 006-100 (95 rows)"
            head = [f"## 🟦 STEP 2 of {n_steps}", "", f"**Assigned to: {user}.** Do this **after** your first issue (#{wnum}) is approved. Rows **006 to 100** ({m} × {lang}).", ""]
        else:
            body_rows = rs
            title = f"[{user} · Step {n_steps} of {n_steps}] {pid} {m} x {lang} x {rs[0]['cwe']}: {len(rs)} rows"
            head = [f"## 🟦 STEP {n_steps} of {n_steps}: extra package", "", f"**Assigned to: {user}.** Do this after your other steps. All {len(rs)} rows ({m} × {lang} × {rs[0]['cwe']}).", ""]
        chunks = [body_rows[i:i + 10] for i in range(0, len(body_rows), 10)]
        first_no, last_no = body_rows[0]["row_no"], body_rows[-1]["row_no"]
        B = head + links + [
            "## What to do", "",
            f"1. Make your issue branch {branch(pkg)} from your personal branch `dev/{user}` (after the earlier steps are merged).",
            "2. The prompts are in the **comments below this text**, **10 prompts per comment = one chat**. Do the comments in order: CHAT 1, CHAT 2, ...",
            "3. For each comment: open a **new chat**, paste the **MASTER PROMPT** (section 1 below), wait for `ready`, then paste the 10 prompts one by one. After each prompt, paste the whole answer into your hand-in file under its `=== NNN` line.",
            "4. Check every 10 answers with Claude (README section 4, Check A and Check B).",
            f"5. When all rows are done: pull request from your issue branch into `dev/{user}` with **only** `submissions/{pkg}.txt`, the exact model name in the description. After approval merge it; when all your steps are merged, open one last pull request `dev/{user}` into `main`.", "",
            f"- [ ] Rows {first_no:03d} to {last_no:03d} done ({len(chunks)} chats), every answer pasted under its `=== NNN` line",
            "- [ ] Check A done (rules); every REDO row generated again", "- [ ] Check B done (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)",
            "- [ ] Pull request opened with only the hand-in file", "- [ ] Merged into your personal branch", "",
            "---", ""] + master + ["---", "", f"## 2. Your prompts are in the comments below ({len(chunks)} comments, 10 prompts each, one chat each)", ""]
        open(os.path.join(ROOT, "issues", f"{pkg}.md"), "w", encoding="utf-8").write("\n".join(B))
        os.makedirs(os.path.join(cdir, pkg), exist_ok=True)
        for ci, ch in enumerate(chunks, 1):
            C = [f"# 🟦 CHAT {ci} of {len(chunks)}: rows {ch[0]['row_no']:03d} to {ch[-1]['row_no']:03d}", "",
                 "**New chat → paste the MASTER PROMPT (top of this issue) → wait for `ready` → paste the prompts below one by one.**", ""]
            for r in ch:
                C += prompt_block(r)
            open(os.path.join(cdir, pkg, f"{ci:02d}.md"), "w", encoding="utf-8").write("\n".join(C))
        out.append([number_of[pkg], title, f"{pkg}.md", f"package,model:{rs[0]['model']},lang:{rs[0]['language']}", user])
    out.sort(key=lambda x: x[0])
    with open(os.path.join(ROOT, "issues", "titles.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["number", "title", "file", "labels", "assignee"])
        w.writerows(out)
    print(len(out), "issues,", sum(len(os.listdir(os.path.join(cdir, p))) for p in os.listdir(cdir)), "comments")


if __name__ == "__main__":
    main()
