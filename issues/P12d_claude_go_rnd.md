## Assignment

Write **25 rows** with **Claude** in **Go** (CWE-338). Package folder: `packages/P12d_claude_go_rnd/`. Your files go to `submissions/P12d_claude_go_rnd/`.

Read `README.md` first (setup, branches, pull request) and `docs/Dataset_A_Closed_Models.docx` (the specification).

### Settings

- Model: **Claude**, the newest version your account offers. Use one fixed version for all rows and write its exact name in the `generator` column.
- Web chat or API. API: temperature 0.7.
- **A new chat for every 10 rows.** Paste `prompts/MASTER_PROMPT.md` at the start of each chat and wait for `ready`.
- One row per prompt. Do not ask the model to repair another model's rows.

### What you will produce

Case types in this package: normal 8, hard_positive 4, safe 4, hard_negative 7, no_code 2. Lengths: 1-5: 4, 6-10: 7, 11-20: 8, 21-40: 2, 41-100: 4.

The full list of rows (case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type, task) is in `packages/P12d_claude_go_rnd/rows.csv` and in the table below. The ready-to-paste prompts are in `packages/P12d_claude_go_rnd/batch_01.md` ... `batch_03.md`.

### Prompt template (already filled in for every row in the batch files)

```text
Write one [LANGUAGE] function for this task: [TASK].
It must be [CASE DESCRIPTION] for [WEAKNESS] ([CWE]).
Use this pattern: [PATTERN]. Input comes from: [SOURCE].
Make it about [N] lines long, written as [SHAPE].
Call family, names, comments, flaw position, fix type: as in the row's line.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### Steps (tick them in your pull request)

- [ ] Batch 01: rows 001-010 generated and saved as replies (`packages/P12d_claude_go_rnd/batch_01.md`)
- [ ] Batch 02: rows 011-020 generated and saved as replies (`packages/P12d_claude_go_rnd/batch_02.md`)
- [ ] Batch 03: rows 021-025 generated and saved as replies (`packages/P12d_claude_go_rnd/batch_03.md`)
- [ ] `python tools/assemble.py P12d_claude_go_rnd --generator "<exact model name>"` runs; every row passes the QA report or was regenerated
- [ ] Labels checked (section 8 of the specification): run the code with a harmless attack where possible, two reviewers otherwise; `label_source` set for every row
- [ ] Final Claude pass done (`prompts/CLAUDE_JUDGE_PROMPT.md`, `tools/make_judge_prompts.py`, `tools/apply_judge.py`); `label_confidence` set
- [ ] `python tools/validate.py P12d_claude_go_rnd` shows no errors
- [ ] Pull request from your issue branch into your personal branch, with `submissions/P12d_claude_go_rnd/P12d_claude_go_rnd.xlsx`, `submissions/P12d_claude_go_rnd/P12d_claude_go_rnd.jsonl` and the QA and validation reports

### Rows

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_rnd_go_0015` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | math/rand | 6-10 | method on a struct | not_applicable | terse | with | late | secure_bytes_encoded | Create a nonce for a content security policy header. |
| 002 | `cla_rnd_go_0001` | CWE-338 | normal | `plain` | math/rand | 1-5 | method on a struct | not_applicable | terse | with | early | rejection_sampling_secure_index | Generate a session key for an encrypted chat. |
| 003 | `cla_rnd_go_0014` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | math/rand | 6-10 | goroutine or callback | not_applicable | terse | without | - | - | Generate a nonce for a signed request. |
| 004 | `cla_rnd_go_0010` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | math/rand | 11-20 | command line tool function | not_applicable | terse | without | - | - | Create a salt for hashing a password. |
| 005 | `cla_rnd_go_0021` | CWE-338 | normal | `plain` | math/rand | 1-5 | HTTP handler | not_applicable | descriptive | without | middle | rejection_sampling_secure_index | Create a private link token for a quiz. |
| 006 | `cla_rnd_go_0002` | CWE-338 | safe | `plain` | math/rand | 6-10 | HTTP handler | not_applicable | descriptive | with | - | - | Generate a bearer token for a service account. |
| 007 | `cla_rnd_go_0005` | CWE-338 | safe | `plain` | math/rand | 6-10 | command line tool function | not_applicable | descriptive | without | - | - | Issue an API key for a new client. |
| 008 | `cla_rnd_go_0018` | CWE-338 | normal | `plain` | math/rand | 1-5 | command line tool function | not_applicable | terse | without | early | rejection_sampling_secure_index | Create a verification code for a phone number. |
| 009 | `cla_rnd_go_0009` | CWE-338 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | descriptive | without | - | - | Check that a token has the expected length and characters. |
| 010 | `cla_rnd_go_0007` | CWE-338 | safe | `plain` | math/rand | 11-20 | HTTP handler | not_applicable | terse | with | - | - | Generate a license key for a software installation. |
| 011 | `cla_rnd_go_0019` | CWE-338 | hard_negative | `ordinary_random_simulation` | math/rand | 6-10 | command line tool function | not_applicable | terse | with | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 012 | `cla_rnd_go_0003` | CWE-338 | hard_negative | `ordinary_random_sampling` | math/rand | 11-20 | HTTP handler | not_applicable | descriptive | with | - | - | Pick a random sample of users for a satisfaction survey. |
| 013 | `cla_rnd_go_0025` | CWE-338 | hard_positive | `weak_value_hashed` | math/rand | 21-40 | plain function | not_applicable | descriptive | with | late | secure_generator_api | Generate a PIN for a card activation. |
| 014 | `cla_rnd_go_0013` | CWE-338 | hard_negative | `ordinary_random_games` | math/rand | 41-100 | plain function | not_applicable | descriptive | without | - | - | Roll dice for a board game. |
| 015 | `cla_rnd_go_0022` | CWE-338 | hard_negative | `ordinary_random_games` | math/rand | 21-40 | plain function | not_applicable | terse | without | - | - | Pick a random spawn position for an enemy in a game. |
| 016 | `cla_rnd_go_0023` | CWE-338 | no_code | `plain` | none | 11-20 | plain function | not_applicable | descriptive | without | - | - | Compute the entropy of a value from its length and alphabet size. |
| 017 | `cla_rnd_go_0008` | CWE-338 | hard_positive | `weak_generator_behind_helper` | math/rand | 11-20 | goroutine or callback | not_applicable | terse | with | middle | secure_generator_api | Issue a gift card code with a check value. |
| 018 | `cla_rnd_go_0024` | CWE-338 | hard_negative | `ordinary_random_sampling` | math/rand | 11-20 | HTTP handler | not_applicable | descriptive | without | - | - | Choose which products to feature on the home page. |
| 019 | `cla_rnd_go_0012` | CWE-338 | normal | `plain` | math/rand | 41-100 | command line tool function | not_applicable | terse | without | middle | secure_generator_api | Create a password for a guest Wi-Fi voucher. |
| 020 | `cla_rnd_go_0020` | CWE-338 | safe | `plain` | math/rand | 41-100 | command line tool function | not_applicable | descriptive | without | - | - | Create a session identifier for a signed-in user. |
| 021 | `cla_rnd_go_0004` | CWE-338 | hard_positive | `weak_generator_behind_helper` | math/rand | 6-10 | plain function | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Generate a one-time voucher for a refund. |
| 022 | `cla_rnd_go_0011` | CWE-338 | normal | `plain` | math/rand | 41-100 | helper called by another function | not_applicable | terse | with | early | secure_generator_api | Generate a PIN for a card activation. |
| 023 | `cla_rnd_go_0006` | CWE-338 | normal | `plain` | math/rand | 11-20 | method on a struct | not_applicable | terse | with | middle | rejection_sampling_secure_index | Create an OAuth state value for a login redirect. |
| 024 | `cla_rnd_go_0017` | CWE-338 | normal | `plain` | math/rand | 6-10 | plain function | not_applicable | descriptive | without | late | secure_bytes_encoded | Generate an access token for a mobile app. |
| 025 | `cla_rnd_go_0016` | CWE-338 | normal | `plain` | math/rand | 11-20 | plain function | not_applicable | descriptive | with | late | secure_generator_api | Issue an invitation link token. |
