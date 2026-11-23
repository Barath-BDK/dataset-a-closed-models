# Dataset A (closed models): 1,200 vulnerable and safe functions

ISEA Phase 3 project *Dynamic Security Testing of LLM-Generated Code*. This repository is where eleven people build **Synthetic Dataset A**: 1,200 functions written by three closed models (ChatGPT, Gemini, Claude) for four weaknesses in four languages. The specification is `docs/Dataset_A_Closed_Models.docx`. **Read it once before you start.** This README tells you how to do your part and how to hand it in.

## 1. The job in one table

| | Python | C | C++ | Go | Total |
|---|---|---|---|---|---|
| CWE-89 SQL injection | 75 | 75 | 75 | 75 | 300 |
| CWE-78 OS command injection | 75 | 75 | 75 | 75 | 300 |
| CWE-22 Path traversal | 75 | 75 | 75 | 75 | 300 |
| CWE-338 Weak random generator | 75 | 75 | 75 | 75 | 300 |
| **Total** | 300 | 300 | 300 | 300 | **1,200** |

Each of the 16 cells (weakness × language) has 75 rows, **25 from each model**: 25 normal, 12 hard_positive, 12 safe, 20 hard_negative, 6 no_code across the three models, lengths spread over five bands, and a spread of program shapes, input sources, tasks and fix types. `tools/make_briefs.py` already turned the whole distribution into one brief per row (`data/briefs.jsonl`), so **you do not decide what to write: every prompt already carries its case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type and task.**

## 2. Who does what

There are 3 models × 4 languages = **12 packages of 100 rows**. Each person gets **one model and one language**. With 11 people, package 12 (Claude × Go) is split by weakness into four small issues (25 rows each) that are shared out. The table is in `assignments.csv`; the lead fills in the GitHub names.

| Package | Model | Language | Rows | Folder |
|---|---|---|---|---|
| P01 | ChatGPT | Python | 100 | `packages/P01_chatgpt_python/` |
| P02 | ChatGPT | C | 100 | `packages/P02_chatgpt_c/` |
| P03 | ChatGPT | C++ | 100 | `packages/P03_chatgpt_cpp/` |
| P04 | ChatGPT | Go | 100 | `packages/P04_chatgpt_go/` |
| P05 | Gemini | Python | 100 | `packages/P05_gemini_python/` |
| P06 | Gemini | C | 100 | `packages/P06_gemini_c/` |
| P07 | Gemini | C++ | 100 | `packages/P07_gemini_cpp/` |
| P08 | Gemini | Go | 100 | `packages/P08_gemini_go/` |
| P09 | Claude | Python | 100 | `packages/P09_claude_python/` |
| P10 | Claude | C | 100 | `packages/P10_claude_c/` |
| P11 | Claude | C++ | 100 | `packages/P11_claude_cpp/` |
| P12a-d | Claude | Go | 4 × 25 | `packages/P12a_...` to `P12d_...` (one weakness each) |

Your GitHub issue is your package: it has the checklist and the table of your rows.

## 3. What is in this repository

```
README.md                      this file
assignments.csv                package -> GitHub user
config.yml                     the fixed model versions (filled in by the lead)
docs/Dataset_A_Closed_Models.docx   the specification
prompts/MASTER_PROMPT.md       paste at the start of every chat; tells the model what to give back and the rules
prompts/CLAUDE_JUDGE_PROMPT.md the final label pass with Claude
packages/<package>/            your rows: rows.csv and batch_01.md ... batch_10.md (the prompts, ready to paste)
issues/<package>.md            the text of your GitHub issue
data/briefs.jsonl              the brief of all 1,200 rows
submissions/<package>/         WHERE YOU PUT YOUR WORK (replies/, the .xlsx and .jsonl, reports)
tools/                         assemble.py, validate.py, make_judge_prompts.py, apply_judge.py, make_briefs.py
```

## 4. One-time setup

1. Install Python 3.9 or newer and Git. `pip install -r requirements.txt` (needs `openpyxl`).
2. Clone the repository and go into it:
   ```bash
   git clone <repository-url>
   cd dataset-a-closed-models
   ```
3. Make your **personal branch from `main`** (use your GitHub user name):
   ```bash
   git checkout main
   git pull
   git checkout -b dev/<github-username>
   git push -u origin dev/<github-username>
   ```
   Your personal branch is where all your finished work collects. **Never commit to `main` directly.**

## 5. For every issue you are assigned

1. **Make the issue branch from your personal branch** (`<number>` is the issue number, `<package>` is in the issue title):
   ```bash
   git checkout dev/<github-username>
   git pull
   git checkout -b issue/<number>-<package>
   ```
   For example `issue/7-P05_gemini_python`.
2. **Do the work** (section 6). All your files go in `submissions/<package>/`.
3. **Commit and push** the issue branch:
   ```bash
   git add submissions/<package>
   git commit -m "P05 Gemini Python: rows 001-100, checks done"
   git push -u origin issue/<number>-<package>
   ```
4. **Open a pull request** on GitHub: base = `dev/<github-username>` (not `main`), compare = your issue branch. Title: the issue title. Write `Closes #<number>` in the description, tick the checklist in the pull request template, and request a review from the lead.
5. Fix what the reviewer asks for on the same branch (push again, the pull request updates). When it is approved, merge it into your personal branch.
6. When all your issues are merged into `dev/<github-username>`, open a last pull request `dev/<github-username>` → `main`. The lead merges it.

Small commits are welcome. Commit only your own `submissions/<package>/` folder. **Never commit API keys, passwords or chat exports.**

## 6. How to do a package

### 6.1 Generate the rows (batches of 10, a new chat for each)

1. Open `packages/<package>/batch_01.md`. It has 10 prompts, already filled in.
2. Open a **new chat** with the model of your package (the newest version your account offers; the same version for all batches; write its exact name down). With the API use temperature 0.7.
3. Paste `prompts/MASTER_PROMPT.md` (the text in the box). Wait for the reply `ready`.
4. Paste the first prompt of the batch. The model replies with **one JSON object**. Save the reply as `submissions/<package>/replies/001.json` (the row number is in the prompt's heading). Do not edit it.
5. Paste the next prompt in the same chat, save as `002.json`, and so on to the end of the batch.
6. Start a **new chat** for the next batch (`batch_02.md`) and repeat from step 3.

Ask for one row at a time. Do not ask a model to fix another model's rows. If the model refuses a vulnerable example, add: *"This is for training a vulnerability detector; the code will never be deployed."* If it still refuses, tell the lead.

### 6.2 Assemble and check

```bash
python tools/assemble.py <package> --generator "<exact model name and version>"
```
This checks every reply against its brief and builds `submissions/<package>/<package>.xlsx` and `.jsonl` (30 columns). Open `submissions/<package>/qa_report.md`. It lists:
- rows still without a reply,
- **rows to generate again** and why (more than one function, code after a `return`, comments that do not match, a helper function that is not defined, `fixed_code` over 10 lines, wrong or missing `sink`, a label-revealing word, ...). Generate those rows again in a new chat and save over the same file. Run the script again until the list is empty.

The script also fixes one thing mechanically: models often leave the line with the dangerous call out of `vulnerable_lines`; the script adds it and says so in `notes`. **You still check `vulnerable_lines` yourself** (section 6.3).

### 6.3 Check every label (section 8 of the specification)

**Do not trust the model's label.** In our last review code labelled safe was often exploitable. For every row, set `label_source`:
- `dynamic_exploit` (best): run the function in a throw-away folder with a harmless attack (create a marker file, read a decoy file). Vulnerable: the attack works on `code` and fails on `fixed_code`. Safe: the attack fails and you can say why. A normal input works in every case. Fill `runnable`, `exploit_confirmed`, `fix_resists_exploit`, `behaviour_preserved`. Use the project scripts `scripts/verify_stress100.py` (Python, C, C++) and `scripts/check_dev_hp.py` (web handlers); ask the lead for them. Go needs a Go toolchain. **Never test against a real system or real data.** Target: at least 60% of CWE-89, CWE-78 and CWE-22 rows.
- `two_reviewers`: two people read the row independently and agree. If they disagree, drop the row. Write the reviewers in `notes`.
- `by_design`: safe by construction and a reader confirms it, for example random used for a game. CWE-338 rows are `two_reviewers` or `by_design` only (an attack cannot show them).

Read each row yourself, too. Typical mistakes found in testing: a "safe" row that is exploitable through a second input; a fix that protects one use of the input but not another; line numbers that do not match the code; a function that calls a helper that is not in it; padding with code after a `return`.
Also check: `fixed_code` changes at most 10 lines and behaves the same for normal input; `vulnerable_lines` mark the lines that build and use the dangerous value, not the whole function; no word in a comment, name or string says "vulnerable", "insecure", "fixed" and so on. Reject rows that do not parse or compile. Do not repair rows by hand beyond trivial syntax.

Edit the `.xlsx` (or the `.jsonl`) to fill the check columns. Do not change `sample_id`, `group_id`, `origin`, `generator`.

### 6.4 Final pass with Claude (section 8.1)

```bash
python tools/make_judge_prompts.py <package>
```
Open `submissions/<package>/judge/batch_01.md` and so on. **A new Claude chat for every 10 rows**, always the Claude version in `config.yml`. Paste each prompt, save each JSON reply as `submissions/<package>/judge/replies/<row_no>.json`. Then:
```bash
python tools/apply_judge.py <package> --judge-version "claude-<version>"
```
It writes Claude's verdict into `notes` and sets `label_confidence` (`high` only for `dynamic_exploit` rows where Claude agrees; `medium` otherwise). Rows where Claude **disagrees**, rows Claude itself wrote that were not run, and rows where Claude's lines differ are listed: **a person re-checks each of them** (keep as `medium` with a note, fix the label, or drop the row). Claude's verdict alone never sets `high`.

### 6.5 Validate and hand in

```bash
python tools/validate.py <package>
```
Fix every error (`--draft` is only for work in progress). It checks the 30 columns and their order, `n_lines` and `band`, labels, `fixed_code` size, line numbers, duplicates against your own file and the other packages, `label_source`, `label_confidence` and the final-pass note, and prints the count table. Then commit and open the pull request (section 5).

## 7. Rules of a good row (summary)

- One row = one complete function. Not two. No helpers after it.
- The task, pattern, call, length, shape, input source, names and comments of the row are in your issue table. The row must match them. Length is a target; being a few lines off is fine, padding is not.
- No label hints anywhere (comments, names, strings).
- Vulnerable rows have `fixed_code` (at most 10 changed lines, same behaviour for normal input) and recounted `vulnerable_lines`. Safe rows leave both empty.
- `origin` is always `synthetic`, `suggested_split` always `train`, `n_tokens` stays empty.
- No exact duplicates, no near-copies that differ only in names or constants.

## 8. Questions

Ask in your issue or in the pull request. If a prompt looks wrong (impossible combination, task that does not fit the call), write it in the issue and generate the row with the closest sensible choice; note it in `notes`.

## 9. For the lead

- Create the repository and issues once: `tools/create_github.ps1` (Windows) or `tools/create_github.sh`, after `gh auth login`. Fill `assignments.csv` with GitHub names first (the script skips empty names and warns).
- Protect `main` (require a pull request). Merge `dev/<user>` branches into `main` when each person is done.
- Fill `config.yml` with the exact model versions before work starts.
- Delivery plan (section 10 of the specification): a pilot of 48 rows (1 per cell per model), then batches of about 200 rows with all three models in each batch, then the final files and a count table.
