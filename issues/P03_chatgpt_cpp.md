## Assignment

Write **100 rows** with **ChatGPT** in **C++** (CWE-22, CWE-338, CWE-78, CWE-89). Package folder: `packages/P03_chatgpt_cpp/`. Your files go to `submissions/P03_chatgpt_cpp/`.

Read `README.md` first (setup, branches, pull request) and `docs/Dataset_A_Closed_Models.docx` (the specification).

### Settings

- Model: **ChatGPT**, the newest version your account offers. Use one fixed version for all rows and write its exact name in the `generator` column.
- Web chat or API. API: temperature 0.7.
- **A new chat for every 10 rows.** Paste `prompts/MASTER_PROMPT.md` at the start of each chat and wait for `ready`.
- One row per prompt. Do not ask the model to repair another model's rows.

### What you will produce

Case types in this package: normal 33, hard_positive 16, safe 16, hard_negative 27, no_code 8. Lengths: 1-5: 9, 6-10: 26, 11-20: 31, 21-40: 22, 41-100: 12.

The full list of rows (case type, pattern, call, length, shape, input source, names, comments, flaw position, fix type, task) is in `packages/P03_chatgpt_cpp/rows.csv` and in the table below. The ready-to-paste prompts are in `packages/P03_chatgpt_cpp/batch_01.md` ... `batch_10.md`.

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

- [ ] Batch 01: rows 001-010 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_01.md`)
- [ ] Batch 02: rows 011-020 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_02.md`)
- [ ] Batch 03: rows 021-030 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_03.md`)
- [ ] Batch 04: rows 031-040 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_04.md`)
- [ ] Batch 05: rows 041-050 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_05.md`)
- [ ] Batch 06: rows 051-060 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_06.md`)
- [ ] Batch 07: rows 061-070 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_07.md`)
- [ ] Batch 08: rows 071-080 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_08.md`)
- [ ] Batch 09: rows 081-090 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_09.md`)
- [ ] Batch 10: rows 091-100 generated and saved as replies (`packages/P03_chatgpt_cpp/batch_10.md`)
- [ ] `python tools/assemble.py P03_chatgpt_cpp --generator "<exact model name>"` runs; every row passes the QA report or was regenerated
- [ ] Labels checked (section 8 of the specification): run the code with a harmless attack where possible, two reviewers otherwise; `label_source` set for every row
- [ ] Final Claude pass done (`prompts/CLAUDE_JUDGE_PROMPT.md`, `tools/make_judge_prompts.py`, `tools/apply_judge.py`); `label_confidence` set
- [ ] `python tools/validate.py P03_chatgpt_cpp` shows no errors
- [ ] Pull request from your issue branch into your personal branch, with `submissions/P03_chatgpt_cpp/P03_chatgpt_cpp.xlsx`, `submissions/P03_chatgpt_cpp/P03_chatgpt_cpp.jsonl` and the QA and validation reports

### Rows

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `gpt_sqli_cpp_0012` | CWE-89 | safe | `plain` | Qt QSqlQuery | 21-40 | web or network handler that receives a request object | database_value | terse | without | - | - | Find a vehicle by its registration number. |
| 002 | `gpt_sqli_cpp_0018` | CWE-89 | hard_negative | `identifier_allowlist` | Qt QSqlQuery | 6-10 | helper called by another function | network_message | descriptive | with | - | - | List the most recent log entries of a service. |
| 003 | `gpt_sqli_cpp_0015` | CWE-89 | hard_negative | `bound_via_builder` | PQexec | 6-10 | helper called by another function | command_line | descriptive | without | - | - | Update the status of a support ticket. |
| 004 | `gpt_sqli_cpp_0010` | CWE-89 | safe | `plain` | mysql_query | 6-10 | callback, lambda or asynchronous task | environment | terse | without | - | - | Find all students enrolled in a course. |
| 005 | `gpt_pt_cpp_0001` | CWE-22 | hard_positive | `check_before_normalising` | std::remove | 11-20 | class method | function_argument | descriptive | with | early | allow_list_mapping | Fetch a user's uploaded resume. |
| 006 | `gpt_sqli_cpp_0016` | CWE-89 | hard_positive | `one_branch_bound` | sqlite3 C API | 11-20 | helper called by another function | environment | terse | with | middle | query_builder_bind | Return the stock quantity for a product code. |
| 007 | `gpt_pt_cpp_0019` | CWE-22 | normal | `plain` | ifstream or ofstream | 21-40 | helper called by another function | environment | descriptive | with | middle | base_name_only | Read a user's saved draft. |
| 008 | `gpt_sqli_cpp_0006` | CWE-89 | normal | `plain` | PQexec | 11-20 | web or network handler that receives a request object | web_request | descriptive | with | middle | allow_list | List the files shared with a user. |
| 009 | `gpt_sqli_cpp_0019` | CWE-89 | hard_negative | `identifier_allowlist` | mysql_query | 41-100 | callback, lambda or asynchronous task | environment | terse | with | - | - | Find events happening in a given city. |
| 010 | `gpt_pt_cpp_0025` | CWE-22 | hard_positive | `relative_check_misses_absolute` | std::filesystem | 6-10 | helper called by another function | environment | terse | without | late | allow_list_mapping | Read the first line of a stored file. |
| 011 | `gpt_pt_cpp_0022` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | fopen | 6-10 | command line tool function | command_line | descriptive | without | - | - | Let a user download a generated report by name. |
| 012 | `gpt_pt_cpp_0003` | CWE-22 | normal | `plain` | std::filesystem | 21-40 | web or network handler that receives a request object | web_request | terse | with | late | base_name_only | Return the text of an uploaded file. |
| 013 | `gpt_rnd_cpp_0007` | CWE-338 | safe | `plain` | rand | 41-100 | plain function | not_applicable | descriptive | without | - | - | Create a webhook signing secret. |
| 014 | `gpt_sqli_cpp_0017` | CWE-89 | normal | `plain` | mysql_query | 1-5 | plain function | file | descriptive | without | late | type_conversion | Find a customer record by email address. |
| 015 | `gpt_cmdi_cpp_0017` | CWE-78 | normal | `plain` | QProcess | 1-5 | web or network handler that receives a request object | network_message | terse | with | middle | allow_list | Rotate the logs of one application. |
| 016 | `gpt_rnd_cpp_0025` | CWE-338 | normal | `plain` | std::default_random_engine | 21-40 | helper called by another function | not_applicable | terse | without | early | secure_bytes_encoded | Create a nonce for a content security policy header. |
| 017 | `gpt_rnd_cpp_0018` | CWE-338 | normal | `plain` | rand | 11-20 | web or network handler that receives a request object | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Pick the words of a recovery phrase for a wallet. |
| 018 | `gpt_sqli_cpp_0011` | CWE-89 | normal | `plain` | mysql_query | 41-100 | command line tool function | command_line | terse | without | early | allow_list | Delete a user's saved bookmarks that match a title. |
| 019 | `gpt_cmdi_cpp_0025` | CWE-78 | hard_negative | `command_from_fixed_map` | QProcess | 21-40 | web or network handler that receives a request object | web_request | descriptive | with | - | - | Start a background job from a script name. |
| 020 | `gpt_sqli_cpp_0005` | CWE-89 | hard_positive | `bound_but_input_identifier` | Qt QSqlQuery | 41-100 | plain function | database_value | terse | without | late | prepared_statement_bind | Delete a user's saved bookmarks that match a title. |
| 021 | `gpt_pt_cpp_0010` | CWE-22 | safe | `plain` | fopen | 41-100 | helper called by another function | function_argument | descriptive | with | - | - | Return the contents of a shared snippet file. |
| 022 | `gpt_cmdi_cpp_0003` | CWE-78 | normal | `plain` | Boost.Process | 6-10 | callback, lambda or asynchronous task | network_message | descriptive | with | middle | allow_list | Download a web page with a command line client. |
| 023 | `gpt_rnd_cpp_0015` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | std::mt19937 | 11-20 | callback, lambda or asynchronous task | not_applicable | terse | without | - | - | Create an OAuth state value for a login redirect. |
| 024 | `gpt_pt_cpp_0008` | CWE-22 | hard_negative | `base_name_only` | ifstream or ofstream | 41-100 | command line tool function | command_line | descriptive | without | - | - | Unzip a theme package into the themes folder. |
| 025 | `gpt_sqli_cpp_0013` | CWE-89 | hard_negative | `integer_forced` | sqlite3 C API | 6-10 | helper called by another function | command_line | terse | with | - | - | Remove a product from a wishlist. |
| 026 | `gpt_rnd_cpp_0009` | CWE-338 | hard_negative | `fixed_seed_reproducible` | std::mt19937 | 11-20 | class method | not_applicable | descriptive | with | - | - | Generate reproducible synthetic data for a unit test. |
| 027 | `gpt_cmdi_cpp_0018` | CWE-78 | hard_negative | `argument_list_with_user_data` | system | 21-40 | helper called by another function | function_argument | descriptive | with | - | - | Look up the registration data of a domain. |
| 028 | `gpt_pt_cpp_0002` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | std::remove | 6-10 | helper called by another function | command_line | descriptive | without | - | - | Count the lines of a stored text file. |
| 029 | `gpt_rnd_cpp_0021` | CWE-338 | no_code | `plain` | none | 11-20 | plain function | not_applicable | terse | with | - | - | Mask a token for display in a log line. |
| 030 | `gpt_pt_cpp_0016` | CWE-22 | hard_negative | `id_mapped_to_known_file` | fopen | 21-40 | command line tool function | command_line | terse | with | - | - | Delete a user's attachment. |
| 031 | `gpt_rnd_cpp_0020` | CWE-338 | normal | `plain` | std::mt19937 | 21-40 | command line tool function | not_applicable | terse | with | early | secure_bytes_encoded | Generate a bearer token for a service account. |
| 032 | `gpt_rnd_cpp_0010` | CWE-338 | hard_negative | `fixed_seed_reproducible` | rand | 21-40 | helper called by another function | not_applicable | terse | without | - | - | Draw the same sample every run for a reproducible experiment. |
| 033 | `gpt_cmdi_cpp_0022` | CWE-78 | normal | `plain` | QProcess | 11-20 | plain function | function_argument | terse | with | early | strict_validation | Check whether a port is open on a host. |
| 034 | `gpt_cmdi_cpp_0010` | CWE-78 | hard_negative | `constant_shell_command` | Boost.Process | 41-100 | callback, lambda or asynchronous task | web_request | terse | with | - | - | Query a package manager for the version of a package. |
| 035 | `gpt_pt_cpp_0023` | CWE-22 | normal | `plain` | ifstream or ofstream | 1-5 | helper called by another function | database_value | terse | without | middle | allow_list_mapping | Serve a PDF from the document library. |
| 036 | `gpt_rnd_cpp_0024` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | std::mt19937 | 6-10 | helper called by another function | not_applicable | descriptive | without | early | secure_bytes_encoded | Generate a secret for a shared team calendar link. |
| 037 | `gpt_rnd_cpp_0022` | CWE-338 | normal | `plain` | std::default_random_engine | 6-10 | helper called by another function | not_applicable | terse | without | early | secure_bytes_encoded | Generate a license key for a software installation. |
| 038 | `gpt_cmdi_cpp_0015` | CWE-78 | hard_negative | `command_from_fixed_map` | Boost.Process | 11-20 | command line tool function | command_line | descriptive | with | - | - | Mount a network share with given options. |
| 039 | `gpt_pt_cpp_0013` | CWE-22 | hard_positive | `prefix_test_without_separator` | std::filesystem | 11-20 | class method | web_request | terse | with | early | base_name_only | Remove an old export file. |
| 040 | `gpt_sqli_cpp_0025` | CWE-89 | normal | `plain` | Qt QSqlQuery | 11-20 | command line tool function | command_line | descriptive | without | middle | prepared_statement_bind | Count signups per day for a date range. |
| 041 | `gpt_cmdi_cpp_0012` | CWE-78 | safe | `plain` | QProcess | 21-40 | plain function | command_line | descriptive | with | - | - | Show the fingerprint of an ssh key file. |
| 042 | `gpt_cmdi_cpp_0019` | CWE-78 | normal | `plain` | popen | 41-100 | callback, lambda or asynchronous task | command_line | descriptive | without | middle | allow_list | Show the owner and permissions of a file. |
| 043 | `gpt_cmdi_cpp_0007` | CWE-78 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | terse | without | - | - | Format a duration in seconds as hours and minutes. |
| 044 | `gpt_cmdi_cpp_0013` | CWE-78 | safe | `plain` | Boost.Process | 21-40 | web or network handler that receives a request object | database_value | descriptive | with | - | - | Show the commit history of a repository for one author. |
| 045 | `gpt_cmdi_cpp_0009` | CWE-78 | normal | `plain` | popen | 6-10 | class method | network_message | descriptive | without | late | argv_no_shell | Look up the DNS records of a host name. |
| 046 | `gpt_sqli_cpp_0022` | CWE-89 | normal | `plain` | sqlite3 C API | 11-20 | web or network handler that receives a request object | web_request | descriptive | with | late | prepared_statement_bind | Record an audit entry for an administrator action. |
| 047 | `gpt_rnd_cpp_0006` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | std::default_random_engine | 11-20 | command line tool function | not_applicable | descriptive | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 048 | `gpt_cmdi_cpp_0021` | CWE-78 | hard_positive | `dash_argument_injection` | QProcess | 21-40 | helper called by another function | environment | descriptive | without | early | argv_no_shell | Query the status of a container by name. |
| 049 | `gpt_sqli_cpp_0001` | CWE-89 | no_code | `plain` | none | 6-10 | command line tool function | not_applicable | terse | without | - | - | Format an order total with tax and currency. |
| 050 | `gpt_sqli_cpp_0024` | CWE-89 | hard_negative | `integer_forced` | sqlite3 C API | 11-20 | helper called by another function | function_argument | descriptive | with | - | - | Check a username and password hash for a login. |
| 051 | `gpt_cmdi_cpp_0016` | CWE-78 | safe | `plain` | popen | 11-20 | helper called by another function | file | descriptive | without | - | - | Rotate the logs of one application. |
| 052 | `gpt_cmdi_cpp_0002` | CWE-78 | hard_positive | `quoting_in_wrong_context` | QProcess | 6-10 | plain function | function_argument | terse | without | early | quoting | Convert a document to another format with a converter. |
| 053 | `gpt_pt_cpp_0015` | CWE-22 | normal | `plain` | fopen | 11-20 | plain function | database_value | terse | without | late | path_containment_check | Create a backup copy of a document. |
| 054 | `gpt_pt_cpp_0014` | CWE-22 | safe | `plain` | std::filesystem | 11-20 | callback, lambda or asynchronous task | web_request | terse | without | - | - | Copy a template file into a user's workspace. |
| 055 | `gpt_cmdi_cpp_0011` | CWE-78 | normal | `plain` | popen | 11-20 | class method | command_line | descriptive | with | middle | quoting | Count the lines of a file with a standard tool. |
| 056 | `gpt_sqli_cpp_0004` | CWE-89 | hard_positive | `one_branch_bound` | MySQL Connector/C++ | 41-100 | helper called by another function | environment | descriptive | with | middle | query_builder_bind | Count signups per day for a date range. |
| 057 | `gpt_rnd_cpp_0014` | CWE-338 | hard_negative | `ordinary_random_shuffling` | std::default_random_engine | 11-20 | plain function | not_applicable | descriptive | with | - | - | Shuffle a playlist before playing it. |
| 058 | `gpt_pt_cpp_0009` | CWE-22 | no_code | `plain` | none | 1-5 | callback, lambda or asynchronous task | not_applicable | terse | without | - | - | Compute a human readable size label. |
| 059 | `gpt_pt_cpp_0007` | CWE-22 | normal | `plain` | ifstream or ofstream | 1-5 | class method | web_request | descriptive | without | middle | base_name_only | Read a font file requested by a stylesheet. |
| 060 | `gpt_pt_cpp_0004` | CWE-22 | hard_positive | `relative_check_misses_absolute` | std::remove | 21-40 | web or network handler that receives a request object | web_request | descriptive | without | late | path_containment_check | Read a plugin manifest from a plugin folder. |
| 061 | `gpt_pt_cpp_0005` | CWE-22 | safe | `plain` | ifstream or ofstream | 6-10 | command line tool function | command_line | descriptive | without | - | - | Return a preview of a stored image. |
| 062 | `gpt_rnd_cpp_0019` | CWE-338 | normal | `plain` | std::default_random_engine | 11-20 | command line tool function | not_applicable | terse | without | early | secure_generator_api | Issue a temporary access code for a visitor badge. |
| 063 | `gpt_cmdi_cpp_0001` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | system | 6-10 | command line tool function | command_line | descriptive | without | - | - | Add a user to a group with the system tool. |
| 064 | `gpt_sqli_cpp_0008` | CWE-89 | safe | `plain` | MySQL Connector/C++ | 11-20 | plain function | command_line | descriptive | without | - | - | Report order totals grouped by a chosen category. |
| 065 | `gpt_pt_cpp_0011` | CWE-22 | normal | `plain` | fopen | 41-100 | helper called by another function | file | descriptive | with | early | base_name_only | Read a language pack for a game. |
| 066 | `gpt_rnd_cpp_0008` | CWE-338 | safe | `plain` | std::default_random_engine | 21-40 | web or network handler that receives a request object | not_applicable | descriptive | with | - | - | Generate a temporary password for a new account. |
| 067 | `gpt_pt_cpp_0006` | CWE-22 | normal | `plain` | fopen | 21-40 | plain function | network_message | terse | without | late | allow_list_mapping | Rename a document inside the storage folder. |
| 068 | `gpt_pt_cpp_0024` | CWE-22 | normal | `plain` | std::remove | 6-10 | web or network handler that receives a request object | web_request | descriptive | with | middle | path_containment_check | Read a language pack for a game. |
| 069 | `gpt_cmdi_cpp_0020` | CWE-78 | normal | `plain` | Boost.Process | 41-100 | web or network handler that receives a request object | web_request | descriptive | with | early | quoting | Convert an audio file to another bitrate. |
| 070 | `gpt_sqli_cpp_0007` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 11-20 | class method | network_message | descriptive | without | early | prepared_statement_bind | Report order totals grouped by a chosen category. |
| 071 | `gpt_sqli_cpp_0002` | CWE-89 | hard_negative | `placeholder_list_for_in` | sqlite3 C API | 21-40 | plain function | function_argument | descriptive | with | - | - | Look up a coupon by its code. |
| 072 | `gpt_cmdi_cpp_0005` | CWE-78 | hard_negative | `user_data_after_end_of_options` | QProcess | 11-20 | plain function | database_value | terse | without | - | - | Pack an installer from a folder with a packaging tool. |
| 073 | `gpt_rnd_cpp_0003` | CWE-338 | normal | `plain` | rand | 11-20 | class method | not_applicable | terse | without | early | secure_bytes_encoded | Create a salt for hashing a password. |
| 074 | `gpt_rnd_cpp_0011` | CWE-338 | hard_positive | `weak_value_hashed` | std::mt19937 | 6-10 | command line tool function | not_applicable | terse | with | late | secure_bytes_encoded | Issue a ticket secret for a QR code. |
| 075 | `gpt_cmdi_cpp_0006` | CWE-78 | safe | `plain` | Boost.Process | 11-20 | command line tool function | command_line | terse | with | - | - | Scan an uploaded file with a command line scanner. |
| 076 | `gpt_sqli_cpp_0009` | CWE-89 | normal | `plain` | PQexec | 6-10 | plain function | web_request | terse | without | late | type_conversion | List the files shared with a user. |
| 077 | `gpt_sqli_cpp_0020` | CWE-89 | hard_negative | `bound_via_builder` | sqlite3 C API | 6-10 | class method | command_line | descriptive | without | - | - | Mark a notification as read for a user. |
| 078 | `gpt_rnd_cpp_0017` | CWE-338 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | descriptive | with | - | - | Convert a token to uppercase for display. |
| 079 | `gpt_pt_cpp_0017` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | std::filesystem | 11-20 | helper called by another function | network_message | terse | without | - | - | Store a user's avatar image. |
| 080 | `gpt_pt_cpp_0021` | CWE-22 | no_code | `plain` | none | 6-10 | web or network handler that receives a request object | not_applicable | terse | without | - | - | Normalize repeated slashes in a path string. |
| 081 | `gpt_rnd_cpp_0005` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | std::default_random_engine | 11-20 | web or network handler that receives a request object | not_applicable | descriptive | without | early | secure_generator_api | Create a cookie value for a remember-me login. |
| 082 | `gpt_sqli_cpp_0003` | CWE-89 | no_code | `plain` | none | 1-5 | plain function | not_applicable | terse | with | - | - | Build a display name from first and last name. |
| 083 | `gpt_pt_cpp_0020` | CWE-22 | safe | `plain` | ifstream or ofstream | 41-100 | helper called by another function | environment | descriptive | with | - | - | Write a crash report file under a given id. |
| 084 | `gpt_cmdi_cpp_0024` | CWE-78 | hard_positive | `dash_argument_injection` | Boost.Process | 6-10 | helper called by another function | environment | terse | without | late | strict_validation | Trace the network route to a host. |
| 085 | `gpt_rnd_cpp_0023` | CWE-338 | safe | `plain` | std::default_random_engine | 6-10 | web or network handler that receives a request object | not_applicable | descriptive | without | - | - | Generate a shared secret for a time-based one-time password setup. |
| 086 | `gpt_rnd_cpp_0013` | CWE-338 | normal | `plain` | rand | 1-5 | class method | not_applicable | terse | with | late | rejection_sampling_secure_index | Generate a password reset token to email to a user. |
| 087 | `gpt_sqli_cpp_0023` | CWE-89 | hard_positive | `keyword_blocklist` | sqlite3 C API | 21-40 | class method | environment | descriptive | without | late | allow_list | Get the loyalty points of a customer. |
| 088 | `gpt_rnd_cpp_0001` | CWE-338 | safe | `plain` | std::default_random_engine | 21-40 | plain function | not_applicable | descriptive | with | - | - | Create a one-time code for two-factor sign in. |
| 089 | `gpt_cmdi_cpp_0014` | CWE-78 | normal | `plain` | system | 21-40 | class method | function_argument | terse | with | middle | argv_no_shell | Show the fingerprint of an ssh key file. |
| 090 | `gpt_sqli_cpp_0021` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 1-5 | class method | function_argument | terse | with | late | prepared_statement_bind | List recent transactions for an account sorted by amount or date. |
| 091 | `gpt_cmdi_cpp_0004` | CWE-78 | normal | `plain` | Boost.Process | 21-40 | plain function | environment | terse | with | late | argv_no_shell | Add a user to a group with the system tool. |
| 092 | `gpt_rnd_cpp_0004` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | std::default_random_engine | 6-10 | helper called by another function | not_applicable | descriptive | with | late | secure_bytes_encoded | Generate an access token for a mobile app. |
| 093 | `gpt_rnd_cpp_0012` | CWE-338 | hard_negative | `ordinary_random_sampling` | rand | 21-40 | helper called by another function | not_applicable | descriptive | without | - | - | Pick a random sample of users for a satisfaction survey. |
| 094 | `gpt_cmdi_cpp_0023` | CWE-78 | hard_positive | `validator_accepts_too_much` | Boost.Process | 6-10 | helper called by another function | network_message | terse | with | early | allow_list | Resize an image to a requested size with an external tool. |
| 095 | `gpt_rnd_cpp_0016` | CWE-338 | normal | `plain` | std::mt19937 | 11-20 | class method | not_applicable | terse | without | middle | secure_generator_api | Generate an initialization vector for encrypting a file. |
| 096 | `gpt_rnd_cpp_0002` | CWE-338 | hard_negative | `ordinary_random_simulation` | std::default_random_engine | 21-40 | helper called by another function | not_applicable | terse | without | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 097 | `gpt_sqli_cpp_0014` | CWE-89 | safe | `plain` | mysql_query | 11-20 | web or network handler that receives a request object | web_request | terse | with | - | - | Delete expired sessions older than a number of days. |
| 098 | `gpt_pt_cpp_0018` | CWE-22 | hard_negative | `library_confined_access` | fopen | 6-10 | helper called by another function | web_request | terse | without | - | - | Serve a static asset such as an image or stylesheet. |
| 099 | `gpt_cmdi_cpp_0008` | CWE-78 | no_code | `plain` | none | 11-20 | command line tool function | not_applicable | descriptive | without | - | - | Check the shape of a host name string. |
| 100 | `gpt_pt_cpp_0012` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | fopen | 11-20 | callback, lambda or asynchronous task | web_request | terse | with | - | - | Return the contents of a shared snippet file. |
