## Assignment

Write **25 rows** with **Claude** in **Go** (CWE-89). Package folder: `packages/P12a_claude_go_sqli/`. Your files go to `submissions/P12a_claude_go_sqli/`.

Read `README.md` first (setup, branches, pull request) and `docs/Dataset_A_Closed_Models.docx` (the specification).

### Settings

- Model: **Claude**, the newest version your account offers. Use one fixed version for all rows and write its exact name in the `generator` column.
- Web chat or API. API: temperature 0.7.
- **A new chat for every 10 rows.** Paste `prompts/MASTER_PROMPT.md` at the start of each chat and wait for `ready`.
- One row per prompt. Do not ask the model to repair another model's rows.

### What you will produce

Case types in this package: normal 8, hard_positive 4, safe 4, hard_negative 7, no_code 2. Lengths: 1-5: 4, 6-10: 7, 11-20: 6, 21-40: 5, 41-100: 3.

The full list of rows (case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type, task) is in `packages/P12a_claude_go_sqli/rows.csv` and in the table below. The ready-to-paste prompts are in `packages/P12a_claude_go_sqli/batch_01.md` ... `batch_03.md`.

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

- [ ] Batch 01: rows 001-010 generated and saved as replies (`packages/P12a_claude_go_sqli/batch_01.md`)
- [ ] Batch 02: rows 011-020 generated and saved as replies (`packages/P12a_claude_go_sqli/batch_02.md`)
- [ ] Batch 03: rows 021-025 generated and saved as replies (`packages/P12a_claude_go_sqli/batch_03.md`)
- [ ] `python tools/assemble.py P12a_claude_go_sqli --generator "<exact model name>"` runs; every row passes the QA report or was regenerated
- [ ] Labels checked (section 8 of the specification): run the code with a harmless attack where possible, two reviewers otherwise; `label_source` set for every row
- [ ] Final Claude pass done (`prompts/CLAUDE_JUDGE_PROMPT.md`, `tools/make_judge_prompts.py`, `tools/apply_judge.py`); `label_confidence` set
- [ ] `python tools/validate.py P12a_claude_go_sqli` shows no errors
- [ ] Pull request from your issue branch into your personal branch, with `submissions/P12a_claude_go_sqli/P12a_claude_go_sqli.xlsx`, `submissions/P12a_claude_go_sqli/P12a_claude_go_sqli.jsonl` and the QA and validation reports

### Rows

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_sqli_go_0019` | CWE-89 | normal | `plain` | gorm Raw | 41-100 | helper called by another function | web_request | descriptive | without | early | query_builder | Look up a city by postal code. |
| 002 | `cla_sqli_go_0001` | CWE-89 | normal | `plain` | database/sql QueryRow | 1-5 | method on a struct | database_value | terse | with | middle | bound_parameters | Insert a new product review. |
| 003 | `cla_sqli_go_0015` | CWE-89 | normal | `plain` | database/sql Exec | 6-10 | goroutine or callback | web_request | terse | with | late | allow_list | Find books by author name. |
| 004 | `cla_sqli_go_0011` | CWE-89 | hard_positive | `bound_but_input_identifier` | database/sql Query | 6-10 | method on a struct | network_message | descriptive | without | late | type_conversion | Get the loyalty points of a customer. |
| 005 | `cla_sqli_go_0023` | CWE-89 | hard_positive | `handwritten_escaping` | gorm Raw | 21-40 | helper called by another function | network_message | descriptive | with | middle | query_builder | Count signups per day for a date range. |
| 006 | `cla_sqli_go_0004` | CWE-89 | hard_positive | `bound_but_input_identifier` | database/sql QueryRow | 6-10 | method on a struct | command_line | descriptive | with | late | type_conversion | Mark a notification as read for a user. |
| 007 | `cla_sqli_go_0018` | CWE-89 | hard_negative | `integer_forced` | database/sql QueryRow | 6-10 | command line tool function | command_line | descriptive | without | - | - | Delete expired sessions older than a number of days. |
| 008 | `cla_sqli_go_0016` | CWE-89 | no_code | `plain` | none | 11-20 | HTTP handler | not_applicable | descriptive | with | - | - | Merge two lists without duplicates. |
| 009 | `cla_sqli_go_0013` | CWE-89 | normal | `plain` | sqlx | 11-20 | HTTP handler | web_request | descriptive | with | early | type_conversion | Find a customer record by email address. |
| 010 | `cla_sqli_go_0008` | CWE-89 | normal | `plain` | sqlx | 6-10 | command line tool function | command_line | descriptive | with | middle | bound_parameters | Find a vehicle by its registration number. |
| 011 | `cla_sqli_go_0017` | CWE-89 | normal | `plain` | sqlx | 1-5 | plain function | web_request | terse | without | early | type_conversion | Return the stock quantity for a product code. |
| 012 | `cla_sqli_go_0022` | CWE-89 | hard_negative | `bound_via_builder` | sqlx | 6-10 | helper called by another function | web_request | terse | without | - | - | List recent transactions for an account sorted by amount or date. |
| 013 | `cla_sqli_go_0009` | CWE-89 | normal | `plain` | gorm Raw | 11-20 | method on a struct | web_request | terse | with | early | query_builder | Find all accounts created through an affiliate code. |
| 014 | `cla_sqli_go_0020` | CWE-89 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | terse | without | - | - | Format an order total with tax and currency. |
| 015 | `cla_sqli_go_0002` | CWE-89 | safe | `plain` | gorm Raw | 21-40 | plain function | function_argument | terse | with | - | - | Check a username and password hash for a login. |
| 016 | `cla_sqli_go_0014` | CWE-89 | hard_negative | `placeholder_list_for_in` | database/sql Query | 21-40 | helper called by another function | file | terse | without | - | - | Find all accounts created through an affiliate code. |
| 017 | `cla_sqli_go_0010` | CWE-89 | hard_negative | `placeholders_only_format` | database/sql Query | 6-10 | plain function | command_line | terse | with | - | - | Find articles that carry a given tag. |
| 018 | `cla_sqli_go_0012` | CWE-89 | normal | `plain` | sqlx | 1-5 | plain function | command_line | descriptive | without | early | query_builder | Find events happening in a given city. |
| 019 | `cla_sqli_go_0005` | CWE-89 | hard_negative | `placeholder_list_for_in` | sqlx | 21-40 | plain function | function_argument | terse | with | - | - | List the most recent log entries of a service. |
| 020 | `cla_sqli_go_0025` | CWE-89 | hard_negative | `bound_via_builder` | database/sql Exec | 41-100 | method on a struct | command_line | descriptive | without | - | - | Export the orders of a given month. |
| 021 | `cla_sqli_go_0021` | CWE-89 | hard_negative | `constant_fragments_only` | database/sql Exec | 11-20 | helper called by another function | function_argument | terse | with | - | - | Find patients by surname. |
| 022 | `cla_sqli_go_0003` | CWE-89 | safe | `plain` | sqlx | 11-20 | command line tool function | command_line | terse | without | - | - | List the employees of a department. |
| 023 | `cla_sqli_go_0007` | CWE-89 | safe | `plain` | sqlx | 41-100 | goroutine or callback | network_message | terse | with | - | - | Find articles that carry a given tag. |
| 024 | `cla_sqli_go_0006` | CWE-89 | hard_positive | `one_branch_bound` | database/sql Query | 21-40 | command line tool function | command_line | terse | without | middle | allow_list | List recent transactions for an account sorted by amount or date. |
| 025 | `cla_sqli_go_0024` | CWE-89 | safe | `plain` | database/sql QueryRow | 11-20 | HTTP handler | web_request | terse | without | - | - | Search a phone book by name prefix. |
