## Assignment

Write **100 rows** with **Claude** in **C** (CWE-22, CWE-338, CWE-78, CWE-89). Package folder: `packages/P10_claude_c/`. Your files go to `submissions/P10_claude_c/`.

Read `README.md` first (setup, branches, pull request) and `docs/Dataset_A_Closed_Models.docx` (the specification).

### Settings

- Model: **Claude**, the newest version your account offers. Use one fixed version for all rows and write its exact name in the `generator` column.
- Web chat or API. API: temperature 0.7.
- **A new chat for every 10 rows.** Paste `prompts/MASTER_PROMPT.md` at the start of each chat and wait for `ready`.
- One row per prompt. Do not ask the model to repair another model's rows.

### What you will produce

Case types in this package: normal 33, hard_positive 16, safe 16, hard_negative 27, no_code 8. Lengths: 1-5: 6, 6-10: 28, 11-20: 33, 21-40: 23, 41-100: 10.

The full list of rows (case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type, task) is in `packages/P10_claude_c/rows.csv` and in the table below. The ready-to-paste prompts are in `packages/P10_claude_c/batch_01.md` ... `batch_10.md`.

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

- [ ] Batch 01: rows 001-010 generated and saved as replies (`packages/P10_claude_c/batch_01.md`)
- [ ] Batch 02: rows 011-020 generated and saved as replies (`packages/P10_claude_c/batch_02.md`)
- [ ] Batch 03: rows 021-030 generated and saved as replies (`packages/P10_claude_c/batch_03.md`)
- [ ] Batch 04: rows 031-040 generated and saved as replies (`packages/P10_claude_c/batch_04.md`)
- [ ] Batch 05: rows 041-050 generated and saved as replies (`packages/P10_claude_c/batch_05.md`)
- [ ] Batch 06: rows 051-060 generated and saved as replies (`packages/P10_claude_c/batch_06.md`)
- [ ] Batch 07: rows 061-070 generated and saved as replies (`packages/P10_claude_c/batch_07.md`)
- [ ] Batch 08: rows 071-080 generated and saved as replies (`packages/P10_claude_c/batch_08.md`)
- [ ] Batch 09: rows 081-090 generated and saved as replies (`packages/P10_claude_c/batch_09.md`)
- [ ] Batch 10: rows 091-100 generated and saved as replies (`packages/P10_claude_c/batch_10.md`)
- [ ] `python tools/assemble.py P10_claude_c --generator "<exact model name>"` runs; every row passes the QA report or was regenerated
- [ ] Labels checked (section 8 of the specification): run the code with a harmless attack where possible, two reviewers otherwise; `label_source` set for every row
- [ ] Final Claude pass done (`prompts/CLAUDE_JUDGE_PROMPT.md`, `tools/make_judge_prompts.py`, `tools/apply_judge.py`); `label_confidence` set
- [ ] `python tools/validate.py P10_claude_c` shows no errors
- [ ] Pull request from your issue branch into your personal branch, with `submissions/P10_claude_c/P10_claude_c.xlsx`, `submissions/P10_claude_c/P10_claude_c.jsonl` and the QA and validation reports

### Rows

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_cmdi_c_0021` | CWE-78 | normal | `plain` | system | 6-10 | request handler that receives a struct or buffer | network_message | terse | without | early | strict_validation | Report the disk usage of a folder. |
| 002 | `cla_rnd_c_0008` | CWE-338 | hard_negative | `ordinary_random_test_data` | rand | 21-40 | request handler that receives a struct or buffer | not_applicable | descriptive | with | - | - | Generate random names for test fixtures. |
| 003 | `cla_cmdi_c_0009` | CWE-78 | safe | `plain` | execl through sh -c | 6-10 | helper called by another function | database_value | descriptive | without | - | - | Rotate the logs of one application. |
| 004 | `cla_rnd_c_0025` | CWE-338 | hard_negative | `ordinary_random_shuffling` | random | 11-20 | small embedded or library utility | not_applicable | descriptive | with | - | - | Deal a shuffled deck of cards to four players. |
| 005 | `cla_sqli_c_0014` | CWE-89 | hard_negative | `integer_forced` | mysql_query | 21-40 | small embedded or library utility | database_value | descriptive | with | - | - | List the most recent log entries of a service. |
| 006 | `cla_sqli_c_0021` | CWE-89 | normal | `plain` | sqlite3_exec | 21-40 | request handler that receives a struct or buffer | database_value | terse | without | late | allow_list | Record an audit entry for an administrator action. |
| 007 | `cla_pt_c_0011` | CWE-22 | hard_negative | `base_name_only` | unlink | 11-20 | plain function | function_argument | terse | with | - | - | Store a user's avatar image. |
| 008 | `cla_cmdi_c_0012` | CWE-78 | normal | `plain` | execl through sh -c | 21-40 | request handler that receives a struct or buffer | database_value | descriptive | without | middle | allow_list | Create a snapshot of a virtual machine by name. |
| 009 | `cla_cmdi_c_0001` | CWE-78 | safe | `plain` | execvp | 6-10 | plain function | web_request | descriptive | with | - | - | Sync a folder to a remote host over ssh. |
| 010 | `cla_cmdi_c_0016` | CWE-78 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | descriptive | without | - | - | Pick the larger of two version strings. |
| 011 | `cla_sqli_c_0015` | CWE-89 | hard_positive | `bound_but_input_identifier` | mysql_query | 11-20 | helper called by another function | network_message | descriptive | with | early | allow_list | Fetch an invoice by its number. |
| 012 | `cla_pt_c_0010` | CWE-22 | hard_negative | `base_name_only` | unlink | 41-100 | request handler that receives a struct or buffer | web_request | descriptive | with | - | - | Delete temporary files that match a name. |
| 013 | `cla_cmdi_c_0022` | CWE-78 | safe | `plain` | execl through sh -c | 11-20 | small embedded or library utility | database_value | descriptive | with | - | - | Check whether a host answers a network ping. |
| 014 | `cla_pt_c_0009` | CWE-22 | normal | `plain` | open | 1-5 | helper called by another function | web_request | terse | with | early | allow_list_mapping | Load the translation file for a locale. |
| 015 | `cla_rnd_c_0005` | CWE-338 | hard_negative | `ordinary_random_games` | rand | 21-40 | request handler that receives a struct or buffer | not_applicable | descriptive | without | - | - | Pick a random spawn position for an enemy in a game. |
| 016 | `cla_cmdi_c_0007` | CWE-78 | normal | `plain` | execl through sh -c | 6-10 | helper called by another function | network_message | terse | with | middle | strict_validation | Count the lines of a file with a standard tool. |
| 017 | `cla_cmdi_c_0011` | CWE-78 | hard_negative | `command_from_fixed_map` | popen | 11-20 | plain function | function_argument | terse | with | - | - | Run a unit conversion script on a value. |
| 018 | `cla_pt_c_0024` | CWE-22 | safe | `plain` | rename | 6-10 | plain function | command_line | terse | without | - | - | Delete temporary files that match a name. |
| 019 | `cla_cmdi_c_0017` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | execl through sh -c | 11-20 | small embedded or library utility | function_argument | terse | with | - | - | Run a spell checker on a text file. |
| 020 | `cla_rnd_c_0007` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | rand | 11-20 | small embedded or library utility | not_applicable | terse | with | - | - | Choose a polling interval spread between workers. |
| 021 | `cla_sqli_c_0009` | CWE-89 | hard_negative | `bound_via_builder` | PQexec | 6-10 | request handler that receives a struct or buffer | web_request | descriptive | with | - | - | List the employees of a department. |
| 022 | `cla_pt_c_0014` | CWE-22 | no_code | `plain` | none | 11-20 | helper called by another function | not_applicable | terse | without | - | - | Return the parent part of a path string. |
| 023 | `cla_sqli_c_0012` | CWE-89 | hard_negative | `placeholder_list_for_in` | PQexec | 21-40 | callback passed as a function pointer | database_value | descriptive | with | - | - | Search products whose name contains a keyword. |
| 024 | `cla_sqli_c_0002` | CWE-89 | normal | `plain` | mysql_query | 6-10 | command line tool function | command_line | terse | without | middle | prepared_statement_bind | Look up the shipping address of an order. |
| 025 | `cla_pt_c_0019` | CWE-22 | normal | `plain` | unlink | 41-100 | plain function | network_message | terse | without | late | path_containment_check | Check whether a named file exists in the storage area. |
| 026 | `cla_rnd_c_0016` | CWE-338 | no_code | `plain` | none | 1-5 | plain function | not_applicable | terse | with | - | - | Mask a token for display in a log line. |
| 027 | `cla_pt_c_0013` | CWE-22 | hard_positive | `single_pass_parent_removal` | rename | 11-20 | callback passed as a function pointer | file | terse | with | late | base_name_only | Restore a document from a version folder. |
| 028 | `cla_sqli_c_0019` | CWE-89 | normal | `plain` | PQexec | 41-100 | helper called by another function | environment | descriptive | with | early | allow_list | List recent transactions for an account sorted by amount or date. |
| 029 | `cla_rnd_c_0006` | CWE-338 | normal | `plain` | rand | 21-40 | command line tool function | not_applicable | terse | with | middle | secure_generator_api | Generate an access token for a mobile app. |
| 030 | `cla_sqli_c_0022` | CWE-89 | no_code | `plain` | none | 6-10 | command line tool function | not_applicable | terse | without | - | - | Compute the average rating from a list. |
| 031 | `cla_rnd_c_0012` | CWE-338 | hard_positive | `weak_generator_behind_helper` | random | 11-20 | helper called by another function | not_applicable | terse | without | middle | secure_generator_api | Create an OAuth state value for a login redirect. |
| 032 | `cla_pt_c_0012` | CWE-22 | normal | `plain` | unlink | 11-20 | command line tool function | command_line | terse | without | early | path_containment_check | List the files in a sub folder of the storage area. |
| 033 | `cla_pt_c_0007` | CWE-22 | hard_positive | `relative_check_misses_absolute` | fopen | 6-10 | callback passed as a function pointer | function_argument | descriptive | with | late | path_containment_check | Fetch a user's uploaded resume. |
| 034 | `cla_sqli_c_0024` | CWE-89 | hard_negative | `placeholders_only_format` | PQexec | 11-20 | request handler that receives a struct or buffer | web_request | terse | with | - | - | Find a customer record by email address. |
| 035 | `cla_pt_c_0002` | CWE-22 | hard_negative | `id_mapped_to_known_file` | open | 21-40 | callback passed as a function pointer | file | terse | without | - | - | Unzip a theme package into the themes folder. |
| 036 | `cla_cmdi_c_0008` | CWE-78 | hard_positive | `partial_shell_character_filter` | system | 11-20 | command line tool function | command_line | descriptive | with | middle | allow_list | Mount a network share with given options. |
| 037 | `cla_pt_c_0025` | CWE-22 | safe | `plain` | fopen | 11-20 | command line tool function | command_line | terse | with | - | - | Remove an old export file. |
| 038 | `cla_sqli_c_0017` | CWE-89 | hard_positive | `keyword_blocklist` | mysql_query | 11-20 | command line tool function | command_line | terse | without | early | prepared_statement_bind | Search a product catalogue with optional filters for price and brand. |
| 039 | `cla_sqli_c_0006` | CWE-89 | normal | `plain` | mysql_query | 11-20 | helper called by another function | database_value | terse | with | middle | prepared_statement_bind | Delete a user's saved bookmarks that match a title. |
| 040 | `cla_pt_c_0005` | CWE-22 | safe | `plain` | rename | 11-20 | request handler that receives a struct or buffer | web_request | terse | with | - | - | Return the text of an uploaded file. |
| 041 | `cla_rnd_c_0009` | CWE-338 | normal | `plain` | random | 6-10 | request handler that receives a struct or buffer | not_applicable | terse | without | early | secure_generator_api | Generate a password reset token to email to a user. |
| 042 | `cla_pt_c_0006` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | rename | 41-100 | small embedded or library utility | network_message | terse | with | - | - | Create a backup copy of a document. |
| 043 | `cla_sqli_c_0004` | CWE-89 | safe | `plain` | sqlite3_exec | 11-20 | command line tool function | command_line | descriptive | without | - | - | Count the unread messages of a user. |
| 044 | `cla_pt_c_0016` | CWE-22 | normal | `plain` | unlink | 6-10 | helper called by another function | function_argument | descriptive | without | middle | path_containment_check | Save a note under a given name. |
| 045 | `cla_cmdi_c_0024` | CWE-78 | normal | `plain` | system | 21-40 | callback passed as a function pointer | file | descriptive | with | late | allow_list | Query the status of a container by name. |
| 046 | `cla_cmdi_c_0020` | CWE-78 | hard_positive | `dash_argument_injection` | popen | 21-40 | request handler that receives a struct or buffer | web_request | terse | with | middle | quoting | Start a background job from a script name. |
| 047 | `cla_rnd_c_0001` | CWE-338 | hard_negative | `ordinary_random_simulation` | rand | 11-20 | callback passed as a function pointer | not_applicable | descriptive | without | - | - | Estimate pi with a Monte Carlo simulation. |
| 048 | `cla_pt_c_0004` | CWE-22 | hard_positive | `check_before_normalising` | fopen | 6-10 | helper called by another function | web_request | descriptive | with | middle | allow_list_mapping | Append a line to a user's activity log. |
| 049 | `cla_pt_c_0020` | CWE-22 | normal | `plain` | fopen | 1-5 | request handler that receives a struct or buffer | database_value | descriptive | with | early | base_name_only | Append a line to a user's activity log. |
| 050 | `cla_rnd_c_0024` | CWE-338 | hard_positive | `weak_generator_behind_helper` | random | 21-40 | callback passed as a function pointer | not_applicable | terse | without | late | secure_bytes_encoded | Create a verification code for a phone number. |
| 051 | `cla_rnd_c_0022` | CWE-338 | safe | `plain` | rand | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | without | - | - | Create a password for a guest Wi-Fi voucher. |
| 052 | `cla_rnd_c_0021` | CWE-338 | normal | `plain` | rand | 21-40 | helper called by another function | not_applicable | terse | with | late | rejection_sampling_secure_index | Create a key for a private download link. |
| 053 | `cla_pt_c_0017` | CWE-22 | safe | `plain` | open | 6-10 | small embedded or library utility | web_request | descriptive | without | - | - | Truncate a log file chosen by name. |
| 054 | `cla_sqli_c_0010` | CWE-89 | hard_positive | `one_branch_bound` | PQexec | 21-40 | request handler that receives a struct or buffer | web_request | terse | without | late | allow_list | Update the status of a support ticket. |
| 055 | `cla_sqli_c_0008` | CWE-89 | no_code | `plain` | none | 1-5 | small embedded or library utility | not_applicable | descriptive | with | - | - | Merge two lists without duplicates. |
| 056 | `cla_cmdi_c_0003` | CWE-78 | normal | `plain` | popen | 21-40 | callback passed as a function pointer | command_line | descriptive | with | middle | quoting | Report the disk usage of a folder. |
| 057 | `cla_sqli_c_0018` | CWE-89 | safe | `plain` | sqlite3_exec | 11-20 | callback passed as a function pointer | command_line | terse | with | - | - | Find patients by surname. |
| 058 | `cla_sqli_c_0011` | CWE-89 | hard_negative | `constant_fragments_only` | mysql_query | 6-10 | small embedded or library utility | file | descriptive | with | - | - | Fetch the configuration value for a given key and environment. |
| 059 | `cla_rnd_c_0019` | CWE-338 | safe | `plain` | rand | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | with | - | - | Generate a PIN for a card activation. |
| 060 | `cla_rnd_c_0014` | CWE-338 | normal | `plain` | rand | 11-20 | callback passed as a function pointer | not_applicable | descriptive | with | late | rejection_sampling_secure_index | Create a one-time code for two-factor sign in. |
| 061 | `cla_rnd_c_0002` | CWE-338 | normal | `plain` | srand | 6-10 | callback passed as a function pointer | not_applicable | terse | with | early | rejection_sampling_secure_index | Issue an API key for a new client. |
| 062 | `cla_rnd_c_0017` | CWE-338 | normal | `plain` | srand | 6-10 | small embedded or library utility | not_applicable | terse | without | early | rejection_sampling_secure_index | Issue a short-lived upload key. |
| 063 | `cla_pt_c_0001` | CWE-22 | hard_negative | `id_mapped_to_known_file` | open | 21-40 | small embedded or library utility | network_message | descriptive | with | - | - | Let a user download a generated report by name. |
| 064 | `cla_rnd_c_0011` | CWE-338 | hard_negative | `ordinary_random_games` | srand | 41-100 | request handler that receives a struct or buffer | not_applicable | descriptive | with | - | - | Roll dice for a board game. |
| 065 | `cla_cmdi_c_0006` | CWE-78 | normal | `plain` | execl through sh -c | 21-40 | small embedded or library utility | network_message | descriptive | without | late | argv_no_shell | Run a spell checker on a text file. |
| 066 | `cla_sqli_c_0007` | CWE-89 | normal | `plain` | sqlite3_exec | 41-100 | callback passed as a function pointer | network_message | terse | without | late | type_conversion | List the files shared with a user. |
| 067 | `cla_cmdi_c_0015` | CWE-78 | normal | `plain` | execvp | 1-5 | command line tool function | command_line | terse | without | early | argv_no_shell | Extract a thumbnail frame from a video file. |
| 068 | `cla_cmdi_c_0002` | CWE-78 | hard_positive | `validator_accepts_too_much` | execvp | 41-100 | command line tool function | command_line | descriptive | without | middle | strict_validation | Look up the DNS records of a host name. |
| 069 | `cla_cmdi_c_0013` | CWE-78 | safe | `plain` | system | 11-20 | request handler that receives a struct or buffer | database_value | terse | without | - | - | Execute a report generator with a chosen template. |
| 070 | `cla_pt_c_0021` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | fopen | 21-40 | plain function | command_line | descriptive | without | - | - | Return a preview of a stored image. |
| 071 | `cla_rnd_c_0023` | CWE-338 | no_code | `plain` | none | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | with | - | - | Compute the entropy of a value from its length and alphabet size. |
| 072 | `cla_sqli_c_0001` | CWE-89 | normal | `plain` | mysql_query | 21-40 | helper called by another function | function_argument | terse | with | late | prepared_statement_bind | Report order totals grouped by a chosen category. |
| 073 | `cla_cmdi_c_0023` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | system | 6-10 | helper called by another function | file | terse | without | - | - | Convert an audio file to another bitrate. |
| 074 | `cla_cmdi_c_0018` | CWE-78 | normal | `plain` | execl through sh -c | 21-40 | command line tool function | command_line | terse | without | early | allow_list | Print the version of a tool chosen from a list. |
| 075 | `cla_cmdi_c_0004` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | system | 6-10 | request handler that receives a struct or buffer | web_request | descriptive | with | - | - | Run a code formatter on a source file. |
| 076 | `cla_rnd_c_0003` | CWE-338 | hard_positive | `weak_value_hashed` | rand | 6-10 | command line tool function | not_applicable | terse | without | middle | rejection_sampling_secure_index | Generate a booking confirmation code. |
| 077 | `cla_pt_c_0022` | CWE-22 | hard_positive | `prefix_test_without_separator` | unlink | 11-20 | request handler that receives a struct or buffer | web_request | terse | without | late | base_name_only | Read a font file requested by a stylesheet. |
| 078 | `cla_sqli_c_0013` | CWE-89 | safe | `plain` | sqlite3_exec | 11-20 | helper called by another function | file | terse | with | - | - | Search a product catalogue with optional filters for price and brand. |
| 079 | `cla_sqli_c_0023` | CWE-89 | hard_negative | `identifier_allowlist` | sqlite3_exec | 11-20 | request handler that receives a struct or buffer | database_value | descriptive | with | - | - | Export the orders of a given month. |
| 080 | `cla_pt_c_0003` | CWE-22 | normal | `plain` | fopen | 11-20 | plain function | function_argument | descriptive | with | middle | allow_list_mapping | Open a certificate file by name. |
| 081 | `cla_rnd_c_0010` | CWE-338 | hard_negative | `ordinary_random_shuffling` | srand | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | without | - | - | Shuffle a playlist before playing it. |
| 082 | `cla_pt_c_0023` | CWE-22 | normal | `plain` | fopen | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | without | middle | path_containment_check | Restore a document from a version folder. |
| 083 | `cla_rnd_c_0004` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | srand | 21-40 | callback passed as a function pointer | not_applicable | terse | without | early | secure_bytes_encoded | Issue a ticket secret for a QR code. |
| 084 | `cla_pt_c_0008` | CWE-22 | normal | `plain` | unlink | 11-20 | plain function | command_line | terse | without | early | path_containment_check | Read a font file requested by a stylesheet. |
| 085 | `cla_rnd_c_0015` | CWE-338 | safe | `plain` | random | 11-20 | helper called by another function | not_applicable | terse | without | - | - | Generate a license key for a software installation. |
| 086 | `cla_cmdi_c_0010` | CWE-78 | hard_negative | `constant_shell_command` | execvp | 11-20 | request handler that receives a struct or buffer | web_request | descriptive | with | - | - | Convert a document to another format with a converter. |
| 087 | `cla_sqli_c_0016` | CWE-89 | hard_negative | `placeholder_list_for_in` | mysql_query | 6-10 | plain function | file | descriptive | with | - | - | List a user's orders with a given status. |
| 088 | `cla_cmdi_c_0019` | CWE-78 | hard_negative | `argument_list_with_user_data` | system | 11-20 | plain function | function_argument | descriptive | with | - | - | Show the owner and permissions of a file. |
| 089 | `cla_cmdi_c_0014` | CWE-78 | no_code | `plain` | none | 11-20 | helper called by another function | not_applicable | terse | without | - | - | Turn a byte count into a short size label. |
| 090 | `cla_cmdi_c_0005` | CWE-78 | hard_positive | `dash_argument_injection` | popen | 41-100 | small embedded or library utility | command_line | terse | with | late | allow_list | Back up a directory to another location with a sync tool. |
| 091 | `cla_sqli_c_0005` | CWE-89 | normal | `plain` | mysql_query | 6-10 | plain function | web_request | terse | without | middle | type_conversion | Count the unread messages of a user. |
| 092 | `cla_rnd_c_0020` | CWE-338 | normal | `plain` | rand | 11-20 | command line tool function | not_applicable | descriptive | with | late | secure_generator_api | Pick the words of a recovery phrase for a wallet. |
| 093 | `cla_sqli_c_0020` | CWE-89 | normal | `plain` | PQexec | 6-10 | helper called by another function | environment | terse | without | middle | prepared_statement_bind | Return the top sellers for a given region. |
| 094 | `cla_rnd_c_0013` | CWE-338 | safe | `plain` | srand | 41-100 | small embedded or library utility | not_applicable | descriptive | with | - | - | Generate an unlock code for a smart lock. |
| 095 | `cla_rnd_c_0018` | CWE-338 | normal | `plain` | random | 11-20 | plain function | not_applicable | terse | without | late | secure_bytes_encoded | Issue an invitation link token. |
| 096 | `cla_pt_c_0018` | CWE-22 | no_code | `plain` | none | 1-5 | small embedded or library utility | not_applicable | terse | with | - | - | Split a path string into its parts. |
| 097 | `cla_pt_c_0015` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | unlink | 6-10 | small embedded or library utility | network_message | descriptive | with | - | - | Write an exported spreadsheet under a requested name. |
| 098 | `cla_cmdi_c_0025` | CWE-78 | normal | `plain` | execl through sh -c | 41-100 | callback passed as a function pointer | file | terse | with | early | quoting | Zip the contents of a folder into a named archive. |
| 099 | `cla_sqli_c_0003` | CWE-89 | hard_positive | `one_branch_bound` | PQexec | 21-40 | plain function | file | terse | without | middle | type_conversion | Return the top sellers for a given region. |
| 100 | `cla_sqli_c_0025` | CWE-89 | safe | `plain` | mysql_query | 21-40 | plain function | environment | terse | with | - | - | Return the latest comments on a post. |
