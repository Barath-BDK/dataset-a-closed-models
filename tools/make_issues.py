#!/usr/bin/env python3
"""Builds the issue texts: for P01-P11 a warm-up issue (rows 001-005) and a main issue (rows 006-100); P12a-d stay as they are.
Writes issues/<package>.md (main), issues/<package>_warmup.md, issues/titles.csv (number, title, file, labels, assignee).
Issue numbers on GitHub: 1-15 are the main issues in the order of assignments_filled.csv, 16-26 are the warm-ups of P01-P11.
"""
import csv, json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/"
MODEL = {"chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude"}
LANG = {"python": "Python", "c": "C", "cpp": "C++", "go": "Go"}


def main():
    assign = list(csv.DictReader(open(os.path.join(ROOT, "assignments_filled.csv"), encoding="utf-8-sig")))
    user_of = {a["package"]: a["github_username"] for a in assign}
    number_of = {a["package"]: i + 1 for i, a in enumerate(assign)}
    briefs = collections.defaultdict(list)
    for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            briefs[r["package"]].append(r)
    mine = collections.defaultdict(list)
    for a in assign:
        mine[a["github_username"]].append(a["package"])
    out = []
    for pkg, rs in briefs.items():
        user = user_of[pkg]
        plist = mine[user]
        n_steps = len(plist) + (1 if plist[0].startswith("P") and len(briefs[plist[0]]) == 100 else 0)
        m, lang = MODEL[rs[0]["model"]], LANG[rs[0]["language"]]
        pid = pkg.split("_")[0]
        hand = f"{URL}submissions/{pkg}.txt"
        mp = f"{URL}MY_PROMPTS/{pkg}.md"
        links = ["| | |", "|---|---|",
                 f"| **Your prompts (one file)** | [`MY_PROMPTS/{pkg}.md`]({mp}) |",
                 f"| **Your hand-in file (the only file you hand in)** | [`submissions/{pkg}.txt`]({hand}) |",
                 f"| **How to do it** | [`README.md`]({URL}README.md) |",
                 f"| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`]({URL}prompts/CLAUDE_CHECK_PROMPT.md) |", ""]
        if len(rs) == 100:
            warm, rest = rs[:5], rs[5:]
            wnum = 15 + int(pid[1:])
            # warm-up issue
            step_of_main = 2
            W = [f"## 🟩 STEP 1 of {n_steps}: THIS IS YOUR FIRST ISSUE. RESOLVE IT FIRST", "",
                 f"**Assigned to: {user}.** This is the **first issue you must resolve**, before any other issue. It is only **5 prompts** (rows 001 to 005 of {m} × {lang}). **These 5 rows are real rows: they count towards your 100** and are part of the final dataset. They are first so that the lead can check your format after 5 rows and you learn the routine before the big job.", "",
                 *links,
                 "### What to do", "",
                 f"1. Read the `README.md` (set-up, personal branch).",
                 f"2. Open [`MY_PROMPTS/{pkg}.md`]({mp}) and find the green block **STEP 1: FIRST ISSUE (rows 001 to 005)**.",
                 f"3. New chat with **{m}** (free base model) → paste the **MASTER PROMPT** → wait for `ready` → paste ROW 001 → paste the answer into `submissions/{pkg}.txt` under `=== 001` → same for rows 002 to 005.",
                 "4. Check the 5 answers with Claude (README section 4, Check A and Check B).",
                 f"5. Make the issue branch `issue/<this issue number>-first`, commit `submissions/{pkg}.txt` with rows 001 to 005 filled, open a pull request into your personal branch `dev/{user}`, write the exact model name in it, and ask the lead for review.",
                 f"6. **Wait for the lead's reply**, then start Step 2 (issue #{number_of[pkg]}). Rows 006 to 100 go in the same file.", "",
                 "- [ ] Master prompt pasted, answered `ready`", "- [ ] Rows 001 to 005 pasted under their lines", "- [ ] Check A and B done", "- [ ] Pull request opened, lead's OK received (only then start Step 2)", ""]
            wtitle = f"[{user} · Step 1 of {n_steps} · FIRST ISSUE, DO THIS FIRST] {pid} {m} x {lang}: rows 001-005 (5 rows)"
            open(os.path.join(ROOT, "issues", f"{pkg}_warmup.md"), "w", encoding="utf-8").write("\n".join(W))
            out.append([wnum, wtitle, f"{pkg}_warmup.md", f"first-issue,model:{rs[0]['model']},lang:{rs[0]['language']}", user])
            body_rows, first, last = rest, 6, 100
            title = f"[{user} · Step 2 of {n_steps}] {pid} {m} x {lang}: rows 006-100 (95 rows)"
            head = [f"## 🟦 STEP 2 of {n_steps}", "", f"**Assigned to: {user}.** Do this **after** your first issue (#{wnum}) is approved. Rows **006 to 100** ({m} × {lang}).", ""]
        else:
            body_rows, first, last = rs, 1, len(rs)
            step = n_steps
            title = f"[{user} · Step {step} of {n_steps}] {pid} {m} x {lang} x {rs[0]['cwe']}: {len(rs)} rows"
            head = [f"## 🟦 STEP {step} of {n_steps}: extra package", "", f"**Assigned to: {user}.** Do this after your other steps. All {len(rs)} rows ({m} × {lang} × {rs[0]['cwe']}).", ""]
        cnt = collections.Counter(r["case_type"] for r in body_rows)
        B = head + links + [
            "### Steps (tick them in your pull request)", "",
            f"- [ ] Issue branch `issue/<this issue number>-{pkg}` made from your personal branch `dev/{user}` (after the earlier steps are merged)",
            f"- [ ] Prompts for rows {first:03d}-{last:03d} pasted into {m} (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/{pkg}.txt`",
            "- [ ] Check A done with Claude (rules); every REDO row generated again",
            "- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)",
            f"- [ ] Pull request from the issue branch into `dev/{user}` with **only** `submissions/{pkg}.txt`; the exact model name in the description",
            f"- [ ] After approval: merged into `dev/{user}`; when all your steps are merged, one last pull request `dev/{user}` into `main`", "",
            "Mix of rows: " + ", ".join(f"{k} {v}" for k, v in cnt.items()) + ".", "",
            "<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>", "",
            "| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in body_rows:
            B.append(f"| {r['row_no']:03d} | `{r['sample_id']}` | {r['cwe']} | {r['case_type']} | `{r['pattern']}` | {r['api']} | {r['band']} | {r['shape'].split(' (')[0]} | {r['source']} | {r['names']} | {r['comments']} | "
                     f"{r.get('flaw', '-')} | {r.get('fix_type', '-')} | {r['task']} |")
        B += ["", "</details>", ""]
        open(os.path.join(ROOT, "issues", f"{pkg}.md"), "w", encoding="utf-8").write("\n".join(B))
        out.append([number_of[pkg], title, f"{pkg}.md", f"package,model:{rs[0]['model']},lang:{rs[0]['language']}", user])
    out.sort(key=lambda x: x[0])
    with open(os.path.join(ROOT, "issues", "titles.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["number", "title", "file", "labels", "assignee"])
        w.writerows(out)
    print(len(out), "issues")


if __name__ == "__main__":
    main()
