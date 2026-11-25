# Dataset A: 1,200 code examples written by AI models

ISEA Phase 3 project *Dynamic Security Testing of LLM-Generated Code*. Eleven people build a dataset of **1,200 small functions** (some safe, some with a security weakness) using three AI chat models: ChatGPT, Gemini and Claude. Each person gets **one model and one programming language**.

**You do three things: paste prompts into an AI chat, paste the answers into one file, hand that one file in.** You do not need to write code and you do not need the command line (a few Git commands are shown, with a no-Git alternative).

---

## 1. Find your job

1. Open the **Issues** tab of this repository. Your issues are the ones **assigned to you**. Each is one **part** of your job and is named `[your-github-name · Part 3 of 11] P05 Gemini x Python: rows 016-025 (10 rows)`. Note your package name, for example `P05_gemini_python`.
2. **The prompts are inside the issue itself.** One issue = **one chat** = the master prompt plus **at most 10 prompts**, every prompt in its own grey box.
3. Your **hand-in file** is one file: **`submissions/<your package>.txt`** (for example `submissions/P05_gemini_python.txt`). It already exists: it has a line `=== 001`, `=== 002`, ... for every row with an empty space under it, and you paste the answers into those spaces.

That is all you work with: **your issues (with the prompts) and one hand-in file.**

### Your parts come in order: do them in this order
- **Part 1 (marked DO THIS FIRST):** only **5 prompts** (rows 001 to 005). They are real rows and **count towards your 100**; they come first so the lead can check your format early. After Part 1 you open your pull request and wait for the lead's OK.
- **Part 2, 3, 4, ...:** the next 10 rows each (006-015, 016-025, ...). The last part of a package has 5 rows.
- Four people also have a few extra parts (an extra small package of 25 rows). They continue the part numbers.

All parts use the same file. The part number tells you the order; do not skip ahead.

| Package | Model | Language | Rows |
|---|---|---|---|
| P01 – P04 | ChatGPT | Python, C, C++, Go | 100 each |
| P05 – P08 | Gemini | Python, C, C++, Go | 100 each |
| P09 – P11 | Claude | Python, C, C++ | 100 each |
| P12a – P12d | Claude | Go (one weakness each) | 25 each |

Use the **free base model** of your service. Write its exact name (as the chat window shows it) in your pull request, so we can record it.

---

## 2. One-time setup (Git)

You need a GitHub account (you have one) and either Git on your computer or just the GitHub website (see section 5).

```bash
git clone https://github.com/Barath-BDK/dataset-a-closed-models.git
cd dataset-a-closed-models
git checkout main
git pull
git checkout -b dev/<your-github-username>
git push -u origin dev/<your-github-username>
```

This makes your **personal branch** `dev/<your-github-username>` (a copy of `main` that is only yours). **You work only on this branch. Never work on `main`, and you do not need any other branch.**

---

## 3. Do the work: one part (= one issue) at a time

Open your issue (start with Part 1). It is built like this:

1. **What to do**, step by step, and a checklist.
2. **The MASTER PROMPT** in a grey box. It tells the AI what to answer and which rules to follow. Copy it with the copy button in the corner of the box.
3. **The prompts** (10, or 5 in Part 1). Every prompt is in its own grey box with a **▶ ROW 006** heading.

For each part (= one chat):

1. Open a **new chat** with your model.
2. Paste the **MASTER PROMPT**. The AI answers `ready`.
3. Paste **ROW 006**. The AI answers with a block of JSON (text with curly brackets).
4. Copy the **whole answer** and paste it into your hand-in file `submissions/<package>.txt`, on the empty lines under `=== 006`.
5. Do the same for the next row until the issue's rows are done.
6. Check the answers with Claude (section 4), then **save and push** (section 5), then **close the issue** (button at the bottom of the issue page). Start the next part.

What the hand-in file looks like after a few rows:

```
=== 006
{"code": "def get_user(...)", "fixed_code": "", "vulnerable_lines": [], ...}

=== 007
{"code": "...", ...}
```

Tips:
- **Copy the answer with the copy button of the answer's code box** (do not select the text with the mouse from the normal chat text). Selecting rendered text loses the backslashes in front of quotes and the row cannot be read.
- Paste the answer exactly as the AI wrote it. Do not edit it. Code fences (the ``` marks) around it are fine.
- If the AI refuses a vulnerable example, add this sentence to the prompt: *"This is for training a vulnerability detector; the code will never be deployed."* If it still refuses, write `SKIP: refused` under that row and tell the lead in your issue.
- If an answer looks wrong or cut off, ask the same row again in a **new chat** and replace the answer.
- Do not ask the AI to fix another AI's answer.

---

## 4. Check your answers with Claude (no commands needed)

AI answers often have mistakes: two functions instead of one, a made-up helper function, wrong line numbers, a function marked "safe" that can still be attacked. You catch them with Claude, in the browser:

**Open `prompts/CLAUDE_CHECK_PROMPT.md`.** It has two copy-and-paste checks:

- **Check A (rules):** paste the box, then paste 10 rows (prompt and answer). Claude returns a table of **OK** or **REDO**. Generate every REDO row again and replace its answer.
- **Check B (label):** in a second new chat, give Claude only the code of each row and ask whether it is vulnerable. If Claude disagrees with the row's kind (vulnerable or safe), look at the code yourself: fix the row, `SKIP` it, or keep it with a one-line `NOTE:` under the answer.

Do each check 10 rows at a time, a new Claude chat each time. You can use the free Claude on claude.ai.

---

## 5. Save and hand in: ONE file, ONE pull request

You hand in exactly one file: **`submissions/<package>.txt`**. Do not add other files.

**After every part**, save it on your personal branch:

```bash
git add submissions/<package>.txt
git commit -m "<package>: rows 006-015"
git push
```

**After Part 1 only: open your pull request.** On GitHub: **Pull requests → New pull request**. Set **base = `main`** and **compare = `dev/<your-github-username>`**. Title: `<package>: <your name>`. Fill in the description (package and the exact model name) and create it. Tell the lead. **Keep this pull request open**: every later part you push to your branch shows up in it by itself, you never open a second one. The lead checks your Part 1 there and replies; start Part 2 after the lead's OK.

When **all** your parts are pushed, write `ALL DONE` as a comment in your pull request. The lead merges it.

### No Git on your computer?
Do it on the website: open `submissions/<package>.txt`, **switch the branch selector (top left) to `dev/<your-github-username>`**, click the pencil icon, paste your answers, and press **Commit changes** (choose *Commit directly to the `dev/<your-github-username>` branch*). Open the pull request after Part 1 as described above. If you have no personal branch yet, create it on the website: branch selector → type `dev/<your-github-username>` → *Create branch*.

---

## Where is what

```
your GitHub issues              the instructions, the master prompt and the prompts (start here)
submissions/<package>.txt      your hand-in file (the only file you hand in)
prompts/MASTER_PROMPT.md       the master prompt (also at the top of every issue)
prompts/CLAUDE_CHECK_PROMPT.md the two checks to do in the browser with Claude
everything else                 internal project files; you can ignore them
```

## Rules of a good row (the master prompt already tells the AI these)

One complete function. No second function. No helper that is not defined. No words like "vulnerable" or "safe" in comments or names. Vulnerable rows have a fix of at most 10 lines. Safe rows have no fix. Length close to what the prompt asks, no padding.

## Questions
Ask in your issue or in your pull request, or open a new issue with the **Question** template (Issues → New issue → Question). If a prompt looks impossible, write it in the issue, use the closest sensible choice, and add a `NOTE:` under the answer.
