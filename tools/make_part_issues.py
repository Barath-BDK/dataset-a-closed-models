#!/usr/bin/env python3
"""Builds one GitHub issue per part (one part = one chat = at most 10 prompts, the prompts are inside the issue text).

Part 1 of every full package (P01-P11) = rows 001-005 (the first issue, "do this first").
Then rows 006-015, 016-025, ... 086-095 and 096-100 (5 rows). P12a-d (25 rows): 001-010, 011-020, 021-025.
A person with an extra P12 package continues the part numbers after the main package.

Writes issues/parts/<NNN>.md and issues/parts.csv (one row per issue: key, part, total, package, rows, title, labels, assignee, file).
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


def chunks_of(rs):
    if len(rs) == 100:
        return [rs[:5]] + [rs[i:i + 10] for i in range(5, 100, 10)]
    return [rs[i:i + 10] for i in range(0, len(rs), 10)]


def main():
    assign = list(csv.DictReader(open(os.path.join(ROOT, "assignments_filled.csv"), encoding="utf-8-sig")))
    user_of = {a["package"]: a["github_username"] for a in assign}
    order = [a["package"] for a in assign]
    briefs = collections.defaultdict(list)
    for l in open(os.path.join(ROOT, "data", "briefs.jsonl"), encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            briefs[r["package"]].append(r)
    mine = collections.defaultdict(list)
    for p in order:
        mine[user_of[p]].append(p)
    total = {u: sum(len(chunks_of(briefs[p])) for p in ps) for u, ps in mine.items()}
    done_parts = collections.defaultdict(int)
    mp = master_prompt()
    pdir = os.path.join(ROOT, "issues", "parts")
    shutil.rmtree(pdir, ignore_errors=True)
    os.makedirs(pdir)
    out = []
    for pkg in order:
        user, rs = user_of[pkg], briefs[pkg]
        m, lang = MODEL[rs[0]["model"]], LANG[rs[0]["language"]]
        pid = pkg.split("_")[0]
        extra = " × " + rs[0]["cwe"] if len(rs) < 100 else ""
        hand = f"{URL}submissions/{pkg}.txt"
        links = ["| | |", "|---|---|",
                 f"| **Your hand-in file (the only file you change)** | [`submissions/{pkg}.txt`]({hand}) |",
                 f"| **How to do it** | [`README.md`]({URL}README.md) |",
                 f"| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`]({URL}prompts/CLAUDE_CHECK_PROMPT.md) |", ""]
        master = ["## 1. The MASTER PROMPT (paste this first in the new chat)", "",
                  "Copy it with the copy button in the corner of the box. The AI must answer `ready`.", "", "````text", mp, "````", ""]
        for ci, ch in enumerate(chunks_of(rs)):
            done_parts[user] += 1
            k, N = done_parts[user], total[user]
            a, z = ch[0]["row_no"], ch[-1]["row_no"]
            first = len(rs) == 100 and ci == 0
            n = len(ch)
            if first:
                title = f"[{user} · Part {k} of {N} · DO THIS FIRST] {pid} {m} x {lang}: rows {a:03d}-{z:03d} ({n} rows)"
                head = [f"## 🟩 PART {k} of {N}: THIS IS YOUR FIRST ISSUE. RESOLVE IT FIRST", "",
                        f"**Assigned to: {user}.** Only **{n} prompts** (rows {a:03d} to {z:03d} of {m} × {lang}). **These {n} rows are real rows: they count towards your 100.** "
                        "They come first so that the lead can check your format and you learn the routine before the big job.", ""]
                todo = [f"6. Commit and push to your personal branch `dev/{user}`, then open **one pull request**: base = `main`, compare = `dev/{user}`. Write the exact model name in it. "
                        "This pull request stays open: every later part you push to the same branch appears in it automatically.",
                        "7. **Close this issue** (button at the bottom of the page) and wait for the lead's OK in the pull request before you start Part 2."]
            else:
                title = f"[{user} · Part {k} of {N}] {pid} {m} x {lang}{extra}: rows {a:03d}-{z:03d} ({n} rows)"
                head = [f"## 🟦 PART {k} of {N}: rows {a:03d} to {z:03d}", "",
                        f"**Assigned to: {user}.** {m} × {lang}{extra}. Do the parts in order: start this one when your previous part is pushed"
                        + (" and the lead has said OK to Part 1." if k == 2 else "."), ""]
                todo = [f"6. Commit and push to your personal branch `dev/{user}` (your open pull request updates itself).",
                        "7. **Close this issue** (button at the bottom of the page). That is how the lead sees that this part is done. Then start the next part."]
            body = head + links + [
                "## What to do", "",
                f"1. Open a **new chat** with **{m}** (the free base model).",
                "2. Paste the **MASTER PROMPT** (section 1 below). Wait for the answer `ready`.",
                f"3. Paste **ROW {a:03d}** (section 2 below). Copy the **whole answer** (use the copy button of the answer's code box) and paste it into `submissions/{pkg}.txt` under the line `=== {a:03d}`. Then ROW {a + 1:03d}, and so on to ROW {z:03d}.".replace("ROW 001 ", "ROW 001 "),
                "4. Check the answers with Claude (README section 4: Check A and Check B). Generate every REDO row again.",
                f"5. Rows {a:03d} to {z:03d} only: do not change any other row.",
                *todo, "",
                f"- [ ] Master prompt pasted, answered `ready`", f"- [ ] Rows {a:03d} to {z:03d} pasted under their `=== NNN` lines",
                "- [ ] Check A and Check B done", f"- [ ] Pushed to `dev/{user}`", "- [ ] Issue closed", "",
                "---", ""] + master + ["---", "", f"## 2. Your {n} prompts (one chat)", ""]
            for r in ch:
                body += prompt_block(r)
            key = f"{pkg}:{a:03d}"
            fn = f"{len(out) + 1:03d}.md"
            open(os.path.join(pdir, fn), "w", encoding="utf-8").write("\n".join(body))
            labels = f"first-issue,model:{rs[0]['model']},lang:{rs[0]['language']}" if first else f"package,model:{rs[0]['model']},lang:{rs[0]['language']}"
            out.append([key, k, N, pkg, a, z, title, labels, user, fn])
    with open(os.path.join(ROOT, "issues", "parts.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["key", "part", "total", "package", "row_from", "row_to", "title", "labels", "assignee", "file"])
        w.writerows(out)
    big = max(os.path.getsize(os.path.join(pdir, f)) for f in os.listdir(pdir))
    print(len(out), "issues; largest body", big, "bytes")


if __name__ == "__main__":
    main()
