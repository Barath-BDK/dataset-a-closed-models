## Assignment

Write **100 rows** with **Gemini** in **C** (CWE-22, CWE-338, CWE-78, CWE-89). Package folder: `packages/P06_gemini_c/`. Your files go to `submissions/P06_gemini_c/`.

Read `README.md` first (setup, branches, pull request) and `docs/Dataset_A_Closed_Models.docx` (the specification).

### Settings

- Model: **Gemini**, the newest version your account offers. Use one fixed version for all rows and write its exact name in the `generator` column.
- Web chat or API. API: temperature 0.7.
- **A new chat for every 10 rows.** Paste `prompts/MASTER_PROMPT.md` at the start of each chat and wait for `ready`.
- One row per prompt. Do not ask the model to repair another model's rows.

### What you will produce

Case types in this package: normal 34, hard_positive 16, safe 16, hard_negative 26, no_code 8. Lengths: 1-5: 12, 6-10: 26, 11-20: 25, 21-40: 26, 41-100: 11.

The full list of rows (case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type, task) is in `packages/P06_gemini_c/rows.csv` and in the table below. The ready-to-paste prompts are in `packages/P06_gemini_c/batch_01.md` ... `batch_10.md`.

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

- [ ] Batch 01: rows 001-010 generated and saved as replies (`packages/P06_gemini_c/batch_01.md`)
- [ ] Batch 02: rows 011-020 generated and saved as replies (`packages/P06_gemini_c/batch_02.md`)
- [ ] Batch 03: rows 021-030 generated and saved as replies (`packages/P06_gemini_c/batch_03.md`)
- [ ] Batch 04: rows 031-040 generated and saved as replies (`packages/P06_gemini_c/batch_04.md`)
- [ ] Batch 05: rows 041-050 generated and saved as replies (`packages/P06_gemini_c/batch_05.md`)
- [ ] Batch 06: rows 051-060 generated and saved as replies (`packages/P06_gemini_c/batch_06.md`)
- [ ] Batch 07: rows 061-070 generated and saved as replies (`packages/P06_gemini_c/batch_07.md`)
- [ ] Batch 08: rows 071-080 generated and saved as replies (`packages/P06_gemini_c/batch_08.md`)
- [ ] Batch 09: rows 081-090 generated and saved as replies (`packages/P06_gemini_c/batch_09.md`)
- [ ] Batch 10: rows 091-100 generated and saved as replies (`packages/P06_gemini_c/batch_10.md`)
- [ ] `python tools/assemble.py P06_gemini_c --generator "<exact model name>"` runs; every row passes the QA report or was regenerated
- [ ] Labels checked (section 8 of the specification): run the code with a harmless attack where possible, two reviewers otherwise; `label_source` set for every row
- [ ] Final Claude pass done (`prompts/CLAUDE_JUDGE_PROMPT.md`, `tools/make_judge_prompts.py`, `tools/apply_judge.py`); `label_confidence` set
- [ ] `python tools/validate.py P06_gemini_c` shows no errors
- [ ] Pull request from your issue branch into your personal branch, with `submissions/P06_gemini_c/P06_gemini_c.xlsx`, `submissions/P06_gemini_c/P06_gemini_c.jsonl` and the QA and validation reports

### Rows

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `gem_cmdi_c_0013` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | popen | 11-20 | callback passed as a function pointer | file | descriptive | without | - | - | Run a unit conversion script on a value. |
| 002 | `gem_cmdi_c_0010` | CWE-78 | normal | `plain` | execl through sh -c | 1-5 | command line tool function | command_line | descriptive | without | middle | allow_list | Show the mount information of a device. |
| 003 | `gem_sqli_c_0016` | CWE-89 | hard_positive | `handwritten_escaping` | PQexec | 11-20 | request handler that receives a struct or buffer | web_request | terse | with | middle | allow_list | Count signups per day for a date range. |
| 004 | `gem_pt_c_0013` | CWE-22 | hard_positive | `check_before_normalising` | rename | 6-10 | helper called by another function | network_message | descriptive | with | late | path_containment_check | Serve a PDF from the document library. |
| 005 | `gem_cmdi_c_0009` | CWE-78 | normal | `plain` | execvp | 11-20 | small embedded or library utility | network_message | descriptive | without | late | argv_no_shell | Compress a log file after rotation. |
| 006 | `gem_rnd_c_0002` | CWE-338 | normal | `plain` | random | 11-20 | request handler that receives a struct or buffer | not_applicable | terse | without | middle | secure_bytes_encoded | Pick the words of a recovery phrase for a wallet. |
| 007 | `gem_sqli_c_0007` | CWE-89 | normal | `plain` | mysql_query | 1-5 | command line tool function | command_line | descriptive | without | late | type_conversion | Find the members of a team by role. |
| 008 | `gem_cmdi_c_0006` | CWE-78 | safe | `plain` | execl through sh -c | 41-100 | callback passed as a function pointer | file | descriptive | with | - | - | Restart a named system service. |
| 009 | `gem_sqli_c_0010` | CWE-89 | normal | `plain` | mysql_query | 6-10 | callback passed as a function pointer | environment | terse | with | middle | allow_list | Insert a new product review. |
| 010 | `gem_pt_c_0015` | CWE-22 | hard_positive | `relative_check_misses_absolute` | rename | 41-100 | command line tool function | command_line | descriptive | with | late | base_name_only | Move a processed file to an archive folder. |
| 011 | `gem_rnd_c_0021` | CWE-338 | no_code | `plain` | none | 11-20 | helper called by another function | not_applicable | descriptive | with | - | - | Check that a token has the expected length and characters. |
| 012 | `gem_cmdi_c_0017` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | execvp | 6-10 | command line tool function | command_line | terse | without | - | - | Scan an uploaded file with a command line scanner. |
| 013 | `gem_cmdi_c_0014` | CWE-78 | normal | `plain` | execvp | 1-5 | callback passed as a function pointer | database_value | terse | without | early | quoting | Show the owner and permissions of a file. |
| 014 | `gem_cmdi_c_0007` | CWE-78 | normal | `plain` | system | 6-10 | helper called by another function | network_message | terse | with | late | quoting | Read the expiry date of a certificate file. |
| 015 | `gem_cmdi_c_0011` | CWE-78 | hard_negative | `constant_shell_command` | execvp | 21-40 | plain function | file | descriptive | with | - | - | Search a log file for lines containing a term. |
| 016 | `gem_cmdi_c_0008` | CWE-78 | normal | `plain` | execvp | 21-40 | small embedded or library utility | environment | descriptive | with | middle | argv_no_shell | Compute the checksum of a file. |
| 017 | `gem_pt_c_0020` | CWE-22 | hard_negative | `id_mapped_to_known_file` | unlink | 11-20 | helper called by another function | database_value | descriptive | without | - | - | Count the lines of a stored text file. |
| 018 | `gem_cmdi_c_0003` | CWE-78 | normal | `plain` | execl through sh -c | 21-40 | helper called by another function | file | terse | with | middle | quoting | Start a background job from a script name. |
| 019 | `gem_sqli_c_0020` | CWE-89 | hard_positive | `bound_but_input_identifier` | sqlite3_exec | 6-10 | plain function | environment | terse | without | middle | type_conversion | Search support tickets by keyword and priority. |
| 020 | `gem_rnd_c_0011` | CWE-338 | safe | `plain` | random | 6-10 | small embedded or library utility | not_applicable | descriptive | without | - | - | Issue a gift card code with a check value. |
| 021 | `gem_sqli_c_0006` | CWE-89 | safe | `plain` | sqlite3_exec | 6-10 | small embedded or library utility | function_argument | descriptive | with | - | - | Search a phone book by name prefix. |
| 022 | `gem_rnd_c_0023` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | random | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | without | - | - | Create a share link secret for a document. |
| 023 | `gem_pt_c_0012` | CWE-22 | safe | `plain` | open | 6-10 | command line tool function | command_line | descriptive | with | - | - | Report the size of a stored file. |
| 024 | `gem_sqli_c_0002` | CWE-89 | no_code | `plain` | none | 1-5 | helper called by another function | not_applicable | descriptive | without | - | - | Check the shape of an email address. |
| 025 | `gem_pt_c_0023` | CWE-22 | normal | `plain` | fopen | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | without | middle | path_containment_check | Read a log file of a named service. |
| 026 | `gem_cmdi_c_0022` | CWE-78 | hard_negative | `command_from_fixed_map` | popen | 41-100 | callback passed as a function pointer | function_argument | terse | without | - | - | Run a database backup tool for one schema. |
| 027 | `gem_cmdi_c_0015` | CWE-78 | hard_negative | `user_data_after_end_of_options` | system | 6-10 | request handler that receives a struct or buffer | web_request | terse | with | - | - | Sync a folder to a remote host over ssh. |
| 028 | `gem_pt_c_0024` | CWE-22 | safe | `plain` | rename | 41-100 | callback passed as a function pointer | function_argument | terse | without | - | - | Save a note under a given name. |
| 029 | `gem_rnd_c_0008` | CWE-338 | safe | `plain` | srand | 41-100 | plain function | not_applicable | terse | with | - | - | Create a deletion confirmation token. |
| 030 | `gem_sqli_c_0008` | CWE-89 | normal | `plain` | mysql_query | 21-40 | callback passed as a function pointer | web_request | terse | with | early | type_conversion | Find articles that carry a given tag. |
| 031 | `gem_sqli_c_0001` | CWE-89 | no_code | `plain` | none | 11-20 | small embedded or library utility | not_applicable | descriptive | with | - | - | Compute a discount tier from an amount. |
| 032 | `gem_pt_c_0014` | CWE-22 | normal | `plain` | unlink | 1-5 | command line tool function | command_line | descriptive | without | middle | base_name_only | Read a language pack for a game. |
| 033 | `gem_cmdi_c_0021` | CWE-78 | normal | `plain` | popen | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | with | late | strict_validation | Unpack an uploaded archive into a working folder. |
| 034 | `gem_rnd_c_0016` | CWE-338 | normal | `plain` | rand | 1-5 | callback passed as a function pointer | not_applicable | descriptive | without | middle | secure_generator_api | Issue a temporary access code for a visitor badge. |
| 035 | `gem_pt_c_0006` | CWE-22 | hard_negative | `library_confined_access` | fopen | 11-20 | plain function | command_line | descriptive | without | - | - | Open a video file for streaming. |
| 036 | `gem_rnd_c_0006` | CWE-338 | normal | `plain` | random | 21-40 | command line tool function | not_applicable | terse | without | middle | secure_bytes_encoded | Create a share link secret for a document. |
| 037 | `gem_pt_c_0002` | CWE-22 | hard_negative | `base_name_only` | rename | 6-10 | small embedded or library utility | function_argument | terse | without | - | - | List the files in a sub folder of the storage area. |
| 038 | `gem_pt_c_0018` | CWE-22 | hard_negative | `library_confined_access` | open | 11-20 | plain function | network_message | terse | with | - | - | Fetch a user's uploaded resume. |
| 039 | `gem_rnd_c_0007` | CWE-338 | normal | `plain` | random | 1-5 | command line tool function | not_applicable | terse | without | late | rejection_sampling_secure_index | Generate a PIN for a card activation. |
| 040 | `gem_pt_c_0021` | CWE-22 | safe | `plain` | rename | 6-10 | plain function | command_line | terse | with | - | - | Extract the entries of an uploaded archive into a folder. |
| 041 | `gem_pt_c_0009` | CWE-22 | hard_negative | `library_confined_access` | rename | 11-20 | callback passed as a function pointer | database_value | descriptive | with | - | - | Read a log file of a named service. |
| 042 | `gem_pt_c_0001` | CWE-22 | no_code | `plain` | none | 6-10 | callback passed as a function pointer | not_applicable | descriptive | without | - | - | Count the segments of a path string. |
| 043 | `gem_sqli_c_0004` | CWE-89 | normal | `plain` | sqlite3_exec | 1-5 | plain function | database_value | terse | without | late | allow_list | Transfer a balance between two accounts inside a transaction. |
| 044 | `gem_cmdi_c_0004` | CWE-78 | normal | `plain` | popen | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | without | middle | strict_validation | Pack an installer from a folder with a packaging tool. |
| 045 | `gem_cmdi_c_0018` | CWE-78 | no_code | `plain` | none | 6-10 | plain function | not_applicable | terse | with | - | - | Check the shape of a host name string. |
| 046 | `gem_sqli_c_0021` | CWE-89 | normal | `plain` | sqlite3_exec | 1-5 | request handler that receives a struct or buffer | network_message | descriptive | without | middle | allow_list | Return a page of articles sorted by a column chosen by the caller. |
| 047 | `gem_sqli_c_0013` | CWE-89 | hard_negative | `identifier_allowlist` | sqlite3_exec | 21-40 | plain function | command_line | terse | with | - | - | Look up a city by postal code. |
| 048 | `gem_sqli_c_0014` | CWE-89 | hard_negative | `placeholder_list_for_in` | mysql_query | 6-10 | small embedded or library utility | web_request | descriptive | without | - | - | Find all accounts created through an affiliate code. |
| 049 | `gem_pt_c_0003` | CWE-22 | hard_positive | `single_pass_parent_removal` | open | 21-40 | callback passed as a function pointer | web_request | terse | without | late | path_containment_check | Extract the entries of an uploaded archive into a folder. |
| 050 | `gem_rnd_c_0014` | CWE-338 | normal | `plain` | rand | 6-10 | command line tool function | not_applicable | descriptive | without | late | secure_generator_api | Create a webhook signing secret. |
| 051 | `gem_pt_c_0007` | CWE-22 | hard_negative | `id_mapped_to_known_file` | open | 41-100 | small embedded or library utility | environment | descriptive | without | - | - | Read a plugin manifest from a plugin folder. |
| 052 | `gem_pt_c_0025` | CWE-22 | normal | `plain` | rename | 21-40 | small embedded or library utility | environment | descriptive | with | early | allow_list_mapping | Read the lines of a CSV import file. |
| 053 | `gem_sqli_c_0017` | CWE-89 | safe | `plain` | sqlite3_exec | 6-10 | command line tool function | command_line | terse | with | - | - | Search a phone book by name prefix. |
| 054 | `gem_rnd_c_0013` | CWE-338 | normal | `plain` | srand | 1-5 | helper called by another function | not_applicable | descriptive | without | early | secure_bytes_encoded | Create a salt for hashing a password. |
| 055 | `gem_sqli_c_0025` | CWE-89 | normal | `plain` | sqlite3_exec | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | without | early | prepared_statement_bind | Look up a coupon by its code. |
| 056 | `gem_cmdi_c_0024` | CWE-78 | hard_positive | `partial_shell_character_filter` | system | 41-100 | plain function | function_argument | descriptive | with | early | quoting | Mount a network share with given options. |
| 057 | `gem_pt_c_0011` | CWE-22 | normal | `plain` | fopen | 21-40 | callback passed as a function pointer | environment | descriptive | with | middle | allow_list_mapping | Read a data file for a selected report. |
| 058 | `gem_pt_c_0004` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | open | 21-40 | small embedded or library utility | database_value | terse | without | - | - | Read the first line of a stored file. |
| 059 | `gem_cmdi_c_0002` | CWE-78 | hard_positive | `quoting_in_wrong_context` | execl through sh -c | 11-20 | small embedded or library utility | file | descriptive | with | late | argv_no_shell | Compare two files and show the differences. |
| 060 | `gem_rnd_c_0019` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | srand | 21-40 | plain function | not_applicable | terse | without | early | rejection_sampling_secure_index | Generate a shared secret for a time-based one-time password setup. |
| 061 | `gem_pt_c_0005` | CWE-22 | normal | `plain` | open | 21-40 | helper called by another function | file | descriptive | without | late | allow_list_mapping | Load a configuration file for a named profile. |
| 062 | `gem_pt_c_0019` | CWE-22 | normal | `plain` | open | 21-40 | command line tool function | command_line | terse | with | late | base_name_only | Return the contents of a help page file. |
| 063 | `gem_sqli_c_0015` | CWE-89 | safe | `plain` | mysql_query | 41-100 | callback passed as a function pointer | command_line | descriptive | without | - | - | Find all accounts created through an affiliate code. |
| 064 | `gem_cmdi_c_0019` | CWE-78 | hard_positive | `quoting_in_wrong_context` | popen | 11-20 | plain function | database_value | descriptive | with | early | strict_validation | Show the commit history of a repository for one author. |
| 065 | `gem_cmdi_c_0005` | CWE-78 | safe | `plain` | execl through sh -c | 21-40 | small embedded or library utility | web_request | terse | with | - | - | Stop a process by name. |
| 066 | `gem_cmdi_c_0020` | CWE-78 | hard_negative | `command_from_fixed_map` | popen | 21-40 | small embedded or library utility | network_message | terse | without | - | - | Download a web page with a command line client. |
| 067 | `gem_cmdi_c_0023` | CWE-78 | hard_positive | `validation_of_other_variable` | system | 6-10 | request handler that receives a struct or buffer | network_message | descriptive | without | early | quoting | Read the last lines of a log file. |
| 068 | `gem_rnd_c_0003` | CWE-338 | safe | `plain` | srand | 11-20 | command line tool function | not_applicable | descriptive | with | - | - | Create a nonce for a content security policy header. |
| 069 | `gem_sqli_c_0023` | CWE-89 | hard_negative | `placeholders_only_format` | sqlite3_exec | 11-20 | helper called by another function | file | terse | with | - | - | Find a customer record by email address. |
| 070 | `gem_rnd_c_0010` | CWE-338 | hard_negative | `fixed_seed_reproducible` | random | 11-20 | plain function | not_applicable | terse | with | - | - | Generate reproducible synthetic data for a unit test. |
| 071 | `gem_rnd_c_0001` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | random | 21-40 | helper called by another function | not_applicable | descriptive | without | - | - | Generate a nonce for a signed request. |
| 072 | `gem_pt_c_0016` | CWE-22 | safe | `plain` | open | 6-10 | command line tool function | command_line | terse | without | - | - | Write a user's settings file. |
| 073 | `gem_rnd_c_0017` | CWE-338 | normal | `plain` | random | 6-10 | small embedded or library utility | not_applicable | terse | without | late | rejection_sampling_secure_index | Create an invite code for a team. |
| 074 | `gem_sqli_c_0024` | CWE-89 | hard_positive | `one_branch_bound` | sqlite3_exec | 11-20 | request handler that receives a struct or buffer | web_request | descriptive | with | early | prepared_statement_bind | Update the email address of a user profile. |
| 075 | `gem_pt_c_0010` | CWE-22 | normal | `plain` | fopen | 21-40 | helper called by another function | environment | descriptive | with | middle | path_containment_check | Return the modification time of a stored file. |
| 076 | `gem_rnd_c_0015` | CWE-338 | normal | `plain` | srand | 6-10 | helper called by another function | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Generate a one-time voucher for a refund. |
| 077 | `gem_rnd_c_0012` | CWE-338 | hard_negative | `ordinary_random_games` | random | 41-100 | plain function | not_applicable | terse | without | - | - | Roll dice for a board game. |
| 078 | `gem_sqli_c_0009` | CWE-89 | hard_negative | `constant_fragments_only` | mysql_query | 6-10 | command line tool function | command_line | descriptive | without | - | - | Find the members of a team by role. |
| 079 | `gem_cmdi_c_0016` | CWE-78 | hard_negative | `command_from_fixed_map` | execvp | 11-20 | callback passed as a function pointer | command_line | terse | with | - | - | Add a user to a group with the system tool. |
| 080 | `gem_sqli_c_0005` | CWE-89 | normal | `plain` | PQexec | 21-40 | command line tool function | command_line | terse | without | middle | prepared_statement_bind | List reservations for a room between two dates. |
| 081 | `gem_cmdi_c_0012` | CWE-78 | no_code | `plain` | none | 11-20 | request handler that receives a struct or buffer | not_applicable | terse | without | - | - | Join a list of words into a title. |
| 082 | `gem_pt_c_0008` | CWE-22 | hard_positive | `relative_check_misses_absolute` | fopen | 11-20 | callback passed as a function pointer | database_value | descriptive | without | early | allow_list_mapping | Write a user's settings file. |
| 083 | `gem_rnd_c_0004` | CWE-338 | no_code | `plain` | none | 1-5 | plain function | not_applicable | descriptive | with | - | - | Convert a token to uppercase for display. |
| 084 | `gem_rnd_c_0009` | CWE-338 | hard_negative | `ordinary_random_simulation` | rand | 21-40 | command line tool function | not_applicable | terse | without | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 085 | `gem_rnd_c_0025` | CWE-338 | hard_negative | `ordinary_random_sampling` | srand | 11-20 | callback passed as a function pointer | not_applicable | terse | without | - | - | Pick a random sample of users for a satisfaction survey. |
| 086 | `gem_pt_c_0022` | CWE-22 | normal | `plain` | unlink | 11-20 | command line tool function | command_line | terse | with | late | allow_list_mapping | Delete a user's attachment. |
| 087 | `gem_sqli_c_0019` | CWE-89 | hard_positive | `handwritten_escaping` | PQexec | 21-40 | helper called by another function | network_message | terse | without | middle | prepared_statement_bind | Delete expired sessions older than a number of days. |
| 088 | `gem_rnd_c_0005` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | srand | 11-20 | helper called by another function | not_applicable | descriptive | with | early | secure_generator_api | Create an unguessable id for a private upload. |
| 089 | `gem_pt_c_0017` | CWE-22 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | descriptive | with | - | - | Build a numbered report name from a prefix. |
| 090 | `gem_rnd_c_0024` | CWE-338 | safe | `plain` | srand | 6-10 | small embedded or library utility | not_applicable | descriptive | with | - | - | Issue a ticket secret for a QR code. |
| 091 | `gem_rnd_c_0020` | CWE-338 | normal | `plain` | rand | 6-10 | helper called by another function | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Generate a secret for a shared team calendar link. |
| 092 | `gem_sqli_c_0003` | CWE-89 | normal | `plain` | PQexec | 1-5 | command line tool function | command_line | descriptive | with | early | prepared_statement_bind | List recent transactions for an account sorted by amount or date. |
| 093 | `gem_sqli_c_0022` | CWE-89 | hard_negative | `identifier_allowlist` | sqlite3_exec | 41-100 | small embedded or library utility | web_request | descriptive | without | - | - | Export the orders of a given month. |
| 094 | `gem_sqli_c_0011` | CWE-89 | safe | `plain` | sqlite3_exec | 11-20 | callback passed as a function pointer | function_argument | descriptive | with | - | - | Mark a notification as read for a user. |
| 095 | `gem_cmdi_c_0001` | CWE-78 | safe | `plain` | execl through sh -c | 11-20 | small embedded or library utility | database_value | descriptive | with | - | - | Query the status of a container by name. |
| 096 | `gem_sqli_c_0012` | CWE-89 | normal | `plain` | PQexec | 21-40 | small embedded or library utility | network_message | descriptive | without | middle | prepared_statement_bind | Get the loyalty points of a customer. |
| 097 | `gem_rnd_c_0022` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random | 21-40 | plain function | not_applicable | terse | with | early | rejection_sampling_secure_index | Issue an email confirmation token. |
| 098 | `gem_cmdi_c_0025` | CWE-78 | safe | `plain` | execl through sh -c | 11-20 | command line tool function | command_line | terse | with | - | - | Trace the network route to a host. |
| 099 | `gem_sqli_c_0018` | CWE-89 | hard_negative | `placeholders_only_format` | mysql_query | 6-10 | plain function | function_argument | terse | with | - | - | List a user's orders with a given status. |
| 100 | `gem_rnd_c_0018` | CWE-338 | hard_positive | `weak_generator_behind_helper` | rand | 41-100 | small embedded or library utility | not_applicable | terse | with | middle | rejection_sampling_secure_index | Generate a pairing code for a device. |
