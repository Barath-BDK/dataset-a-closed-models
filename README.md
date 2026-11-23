# Dataset A: 1,200 code examples written by AI models

ISEA Phase 3 project *Dynamic Security Testing of LLM-Generated Code*. Eleven people build a dataset of **1,200 small functions** (some safe, some with a security weakness) using three AI chat models: ChatGPT, Gemini and Claude. Each person gets **one model and one programming language**.

**You do three things: paste prompts into an AI chat, paste the answers into one file, hand that one file in.** You do not need to write code and you do not need the command line (a few Git commands are shown, with a no-Git alternative).

---

## 1. Find your job

1. Open the **Issues** tab of this repository. Your issue is the one **assigned to you** (it names your model and language, for example `[P05] Gemini x Python: 100 rows`). Note your package name, for example `P05_gemini_python`.
2. Your **prompts** are in one file: **`MY_PROMPTS/<your package>.md`** (for example `MY_PROMPTS/P05_gemini_python.md`).
3. Your **hand-in file** is one file: **`submissions/<your package>.txt`** (for example `submissions/P05_gemini_python.txt`). It already exists and is empty; you fill it in.

That is all you work with: **one prompts file, one hand-in file.**

### Your issues come in steps: do them in this order
Each person has numbered issues, named `[your-github-name · Step 1 of N] ...`:
- **Step 1: warm-up (DO THIS FIRST).** Only **5 prompts** (rows 001 to 005) to learn the routine. Hand them in with a pull request and wait for the lead's OK.
- **Step 2:** the rest of your package (rows 006 to 100).
- **Step 3** (only four people): an extra small package of 25 rows.

All steps use the same two files. The warm-up rows are the first rows of the same hand-in file, so nothing is wasted.

| Package | Model | Language | Rows |
|---|---|---|---|
| P01 – P04 | ChatGPT | Python, C, C++, Go | 100 each |
| P05 – P08 | Gemini | Python, C, C++, Go | 100 each |
| P09 – P11 | Claude | Python, C, C++ | 100 each |
| P12a – P12d | Claude | Go (one weakness each) | 25 each |

Use the **free base model** of your service. Write its exact name (as the chat window shows it) in your pull request, so we can record it.

---

## 2. One-time setup (Git)

You need a GitHub account (you have one) and either Git on your computer or just the GitHub website (see section 6).

```bash
git clone https://github.com/Barath-BDK/dataset-a-closed-models.git
cd dataset-a-closed-models
git checkout main
git pull
git checkout -b dev/<your-github-username>
git push -u origin dev/<your-github-username>
```

This makes your **personal branch** `dev/<your-github-username>` (a copy of `main` that is only yours). Never work on `main` directly: it is locked and only accepts pull requests.

---

## 3. Do the work: step by step, for every issue assigned to you (start with Step 1)

**Make a branch for the issue, starting from your personal branch** (`<number>` is the issue number, `<package>` your package name):

```bash
git checkout dev/<your-github-username>
git pull
git checkout -b issue/<number>-<package>
```

Now open `MY_PROMPTS/<package>.md`. It is built like this:

1. **A short how-to** at the top. The green block **STEP 1: WARM-UP** (5 prompts) comes first; the blue blocks are Step 2.
2. **The MASTER PROMPT** in a grey box. It tells the AI what to answer and which rules to follow. Copy it with the copy button in the corner of the box.
3. **CHAT 1, CHAT 2 ... CHAT 10**: ten blocks of 10 prompts each (the 25-row packages have 3). Every prompt is in its own grey box with a **▶ ROW 001** heading.

For each CHAT block:

1. Open a **new chat** with your model.
2. Paste the **MASTER PROMPT**. The AI answers `ready`.
3. Paste **ROW 001**. The AI answers with a block of JSON (text with curly brackets).
4. Copy the **whole answer** and paste it into your hand-in file `submissions/<package>.txt`, on the empty lines under `=== 001`.
5. Do the same for ROW 002, 003, ... until the block ends. Then start a **new chat** for the next block (back to step 1).

What the hand-in file looks like after a few rows:

```
=== 001
{"code": "def get_user(...)", "fixed_code": "", "vulnerable_lines": [], ...}

=== 002
{"code": "...", ...}
```

Tips:
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

## 5. Hand in: ONE file

You hand in exactly one file: **`submissions/<package>.txt`**, with every row filled in (or marked `SKIP: reason`). Do not add other files.

```bash
git add submissions/<package>.txt
git commit -m "<package>: all rows pasted and checked"
git push -u origin issue/<number>-<package>
```

Then on GitHub: **Pull requests → New pull request**. Set **base = `dev/<your-github-username>`** (not `main`) and **compare = `issue/<number>-<package>`**. Title: the issue title. In the description write `Closes #<number>` and the exact model name you used. Create the pull request and ask the lead for review. When it is approved, merge it into your personal branch.

When all your issues are merged into your personal branch, open **one last pull request: `dev/<your-github-username>` → `main`**. The lead merges it.

### No Git on your computer?
You can do everything on the website: open `submissions/<package>.txt` on GitHub, click the pencil icon, paste your answers, then **Commit changes → "Create a new branch for this commit and start a pull request"**. Name the branch `issue/<number>-<package>` and choose the right base branch in the pull request.

---

## 6. For the lead (after everyone has handed in)

The checking of the labels with scripts is done once by the lead, not by each person:

```bash
python tools/assemble.py <package> --generator "<exact model name>"   # builds the 30-column file + qa_report.md from the .txt
python tools/make_judge_prompts.py <package>                          # Claude label pass prompts (see prompts/CLAUDE_JUDGE_PROMPT.md)
python tools/apply_judge.py <package> --judge-version "<claude version>"
python tools/validate.py <package>                                    # counts and format check
```

Also: fill `config.yml`; the packages merge into one Excel or JSON Lines file per model (see section 10 of the specification: pilot of 48 rows, then batches of about 200, then the final files and count table). Where possible the labels should also be tested by running the code with a harmless attack (section 8 of the specification).

## Where is what

```
MY_PROMPTS/<package>.md        your prompts, all in one file (start here)
submissions/<package>.txt      your hand-in file (the only file you hand in)
prompts/MASTER_PROMPT.md       the master prompt (also copied at the top of your prompts file)
prompts/CLAUDE_CHECK_PROMPT.md the two checks to do in the browser with Claude
docs/Dataset_A_Closed_Models.docx   the full specification (read it once if you like)
packages/, data/, issues/, tools/    material of the lead; you can ignore these
```

## Rules of a good row (the master prompt already tells the AI these)

One complete function. No second function. No helper that is not defined. No words like "vulnerable" or "safe" in comments or names. Vulnerable rows have a fix of at most 10 lines. Safe rows have no fix. Length close to what the prompt asks, no padding.

## Questions
Ask in your issue or in your pull request. If a prompt looks impossible, write it in the issue, use the closest sensible choice, and add a `NOTE:` under the answer.
