## 🟦 STEP 2 of 2

**Assigned to: Puneeth-2428.** Do this **after** the warm-up (issue #19) is approved. Rows **006 to 100** (ChatGPT × Go).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P04_chatgpt_go.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P04_chatgpt_go.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P04_chatgpt_go.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P04_chatgpt_go.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P04_chatgpt_go` made from your personal branch `dev/Puneeth-2428` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into ChatGPT (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P04_chatgpt_go.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/Puneeth-2428` with **only** `submissions/P04_chatgpt_go.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/Puneeth-2428`; when all your steps are merged, one last pull request `dev/Puneeth-2428` into `main`

Mix of rows: hard_positive 15, hard_negative 25, safe 15, normal 32, no_code 8.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `gpt_pt_go_0019` | CWE-22 | hard_positive | `single_pass_parent_removal` | http.ServeFile | 11-20 | plain function | environment | descriptive | without | middle | base_name_only | Extract the entries of an uploaded archive into a folder. |
| 007 | `gpt_pt_go_0003` | CWE-22 | hard_negative | `library_confined_access` | os.ReadFile | 21-40 | helper called by another function | function_argument | terse | with | - | - | Load a configuration file for a named profile. |
| 008 | `gpt_pt_go_0022` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 6-10 | HTTP handler | database_value | terse | with | - | - | Fetch a user's uploaded resume. |
| 009 | `gpt_rnd_go_0023` | CWE-338 | hard_positive | `weak_value_hashed` | math/rand | 21-40 | HTTP handler | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Issue a short-lived upload key. |
| 010 | `gpt_pt_go_0025` | CWE-22 | hard_positive | `extension_check_only` | os.Open | 11-20 | method on a struct | function_argument | terse | without | late | allow_list_mapping | Return the modification time of a stored file. |
| 011 | `gpt_sqli_go_0025` | CWE-89 | safe | `plain` | database/sql Exec | 6-10 | command line tool function | command_line | descriptive | without | - | - | Find a customer record by email address. |
| 012 | `gpt_sqli_go_0003` | CWE-89 | hard_positive | `keyword_blocklist` | gorm Raw | 11-20 | method on a struct | web_request | descriptive | without | early | bound_parameters | Find the members of a team by role. |
| 013 | `gpt_cmdi_go_0008` | CWE-78 | hard_negative | `argument_list_with_user_data` | exec.Command with sh -c | 11-20 | command line tool function | command_line | descriptive | with | - | - | Add a user to a group with the system tool. |
| 014 | `gpt_pt_go_0010` | CWE-22 | normal | `plain` | archive extraction (archive/zip) | 11-20 | helper called by another function | web_request | descriptive | without | middle | allow_list_mapping | Return the text of an uploaded file. |
| 015 | `gpt_cmdi_go_0010` | CWE-78 | no_code | `plain` | none | 6-10 | command line tool function | not_applicable | descriptive | with | - | - | Read the average time out of a ping summary text. |
| 016 | `gpt_cmdi_go_0021` | CWE-78 | hard_negative | `user_data_after_end_of_options` | exec.Command with arguments | 11-20 | helper called by another function | environment | terse | without | - | - | Run a code formatter on a source file. |
| 017 | `gpt_cmdi_go_0002` | CWE-78 | normal | `plain` | exec.Command with arguments | 11-20 | plain function | database_value | descriptive | with | late | strict_validation | Run a code formatter on a source file. |
| 018 | `gpt_sqli_go_0023` | CWE-89 | normal | `plain` | gorm Raw | 21-40 | command line tool function | command_line | terse | without | late | type_conversion | Find books by author name. |
| 019 | `gpt_rnd_go_0007` | CWE-338 | normal | `plain` | math/rand | 11-20 | HTTP handler | not_applicable | terse | with | middle | secure_generator_api | Create a challenge string for a login handshake. |
| 020 | `gpt_rnd_go_0021` | CWE-338 | hard_negative | `ordinary_random_test_data` | math/rand | 21-40 | method on a struct | not_applicable | descriptive | without | - | - | Generate random names for test fixtures. |
| 021 | `gpt_sqli_go_0013` | CWE-89 | no_code | `plain` | none | 1-5 | plain function | not_applicable | terse | with | - | - | Compute a discount tier from an amount. |
| 022 | `gpt_cmdi_go_0017` | CWE-78 | hard_negative | `user_data_after_end_of_options` | exec.Command with sh -c | 21-40 | command line tool function | command_line | terse | without | - | - | Rotate the logs of one application. |
| 023 | `gpt_rnd_go_0019` | CWE-338 | hard_negative | `ordinary_random_simulation` | math/rand | 21-40 | goroutine or callback | not_applicable | descriptive | with | - | - | Estimate pi with a Monte Carlo simulation. |
| 024 | `gpt_pt_go_0005` | CWE-22 | no_code | `plain` | none | 1-5 | method on a struct | not_applicable | terse | with | - | - | Split a path string into its parts. |
| 025 | `gpt_pt_go_0017` | CWE-22 | no_code | `plain` | none | 11-20 | method on a struct | not_applicable | descriptive | with | - | - | Count the segments of a path string. |
| 026 | `gpt_rnd_go_0016` | CWE-338 | normal | `plain` | math/rand | 21-40 | command line tool function | not_applicable | terse | with | early | rejection_sampling_secure_index | Create a challenge string for a login handshake. |
| 027 | `gpt_rnd_go_0006` | CWE-338 | hard_positive | `weak_generator_behind_helper` | math/rand | 11-20 | plain function | not_applicable | descriptive | without | early | secure_bytes_encoded | Create an encryption key for a local vault. |
| 028 | `gpt_cmdi_go_0018` | CWE-78 | safe | `plain` | exec.Command with arguments | 6-10 | method on a struct | database_value | terse | with | - | - | Compress a log file after rotation. |
| 029 | `gpt_pt_go_0015` | CWE-22 | normal | `plain` | os.ReadFile | 21-40 | HTTP handler | web_request | descriptive | without | middle | base_name_only | Serve a PDF from the document library. |
| 030 | `gpt_sqli_go_0011` | CWE-89 | normal | `plain` | sqlx | 6-10 | HTTP handler | web_request | terse | with | middle | bound_parameters | Fetch the configuration value for a given key and environment. |
| 031 | `gpt_rnd_go_0003` | CWE-338 | safe | `plain` | math/rand | 11-20 | goroutine or callback | not_applicable | terse | without | - | - | Generate a one-time voucher for a refund. |
| 032 | `gpt_rnd_go_0009` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | math/rand | 11-20 | goroutine or callback | not_applicable | descriptive | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 033 | `gpt_rnd_go_0025` | CWE-338 | normal | `plain` | math/rand | 11-20 | goroutine or callback | not_applicable | descriptive | without | middle | rejection_sampling_secure_index | Create a key for a private download link. |
| 034 | `gpt_cmdi_go_0022` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | exec.Command with arguments | 41-100 | plain function | environment | terse | with | - | - | Back up a directory to another location with a sync tool. |
| 035 | `gpt_rnd_go_0010` | CWE-338 | hard_negative | `ordinary_random_test_data` | math/rand | 6-10 | method on a struct | not_applicable | terse | without | - | - | Generate random names for test fixtures. |
| 036 | `gpt_pt_go_0023` | CWE-22 | normal | `plain` | os.Create | 21-40 | goroutine or callback | database_value | terse | without | early | path_containment_check | Remove an old export file. |
| 037 | `gpt_cmdi_go_0024` | CWE-78 | hard_positive | `validator_accepts_too_much` | exec.Command with arguments | 21-40 | method on a struct | web_request | descriptive | without | middle | quoting | Run a database backup tool for one schema. |
| 038 | `gpt_pt_go_0016` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | archive extraction (archive/zip) | 21-40 | goroutine or callback | network_message | terse | without | - | - | Let a user download a generated report by name. |
| 039 | `gpt_sqli_go_0019` | CWE-89 | safe | `plain` | database/sql Exec | 11-20 | helper called by another function | function_argument | descriptive | without | - | - | Count the unread messages of a user. |
| 040 | `gpt_sqli_go_0024` | CWE-89 | hard_negative | `integer_forced` | database/sql Query | 11-20 | HTTP handler | web_request | terse | with | - | - | Record an audit entry for an administrator action. |
| 041 | `gpt_pt_go_0014` | CWE-22 | hard_negative | `id_mapped_to_known_file` | os.ReadFile | 11-20 | HTTP handler | web_request | descriptive | without | - | - | Restore a document from a version folder. |
| 042 | `gpt_cmdi_go_0016` | CWE-78 | hard_positive | `partial_shell_character_filter` | exec.Command with sh -c | 21-40 | helper called by another function | web_request | descriptive | with | middle | strict_validation | Look up the DNS records of a host name. |
| 043 | `gpt_rnd_go_0020` | CWE-338 | hard_negative | `ordinary_random_shuffling` | math/rand | 6-10 | goroutine or callback | not_applicable | terse | without | - | - | Deal a shuffled deck of cards to four players. |
| 044 | `gpt_pt_go_0008` | CWE-22 | normal | `plain` | os.Open | 1-5 | goroutine or callback | environment | terse | with | early | library_confinement | Restore a document from a version folder. |
| 045 | `gpt_cmdi_go_0025` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | exec.Command with sh -c | 6-10 | helper called by another function | file | descriptive | without | - | - | Run a database backup tool for one schema. |
| 046 | `gpt_sqli_go_0010` | CWE-89 | hard_positive | `handwritten_escaping` | database/sql Exec | 11-20 | plain function | function_argument | descriptive | with | late | query_builder | List the employees of a department. |
| 047 | `gpt_cmdi_go_0011` | CWE-78 | hard_positive | `validator_accepts_too_much` | exec.Command with arguments | 11-20 | goroutine or callback | command_line | descriptive | with | early | allow_list | Compute the checksum of a file. |
| 048 | `gpt_sqli_go_0022` | CWE-89 | hard_negative | `bound_via_builder` | database/sql Query | 6-10 | HTTP handler | web_request | descriptive | without | - | - | Fetch an invoice by its number. |
| 049 | `gpt_cmdi_go_0006` | CWE-78 | safe | `plain` | exec.Command with arguments | 21-40 | HTTP handler | web_request | descriptive | without | - | - | Send a document to a named printer. |
| 050 | `gpt_rnd_go_0014` | CWE-338 | normal | `plain` | math/rand | 21-40 | method on a struct | not_applicable | descriptive | with | middle | rejection_sampling_secure_index | Issue an email confirmation token. |
| 051 | `gpt_sqli_go_0009` | CWE-89 | hard_positive | `bound_but_input_identifier` | gorm Raw | 11-20 | method on a struct | network_message | descriptive | without | early | type_conversion | List the appointments of a doctor on a given day. |
| 052 | `gpt_pt_go_0013` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | archive extraction (archive/zip) | 21-40 | helper called by another function | environment | terse | without | - | - | Create a thumbnail file next to the original image. |
| 053 | `gpt_rnd_go_0022` | CWE-338 | safe | `plain` | math/rand | 21-40 | HTTP handler | not_applicable | descriptive | with | - | - | Generate a pairing code for a device. |
| 054 | `gpt_cmdi_go_0007` | CWE-78 | normal | `plain` | exec.Command with sh -c | 21-40 | helper called by another function | database_value | terse | without | middle | quoting | Create a snapshot of a virtual machine by name. |
| 055 | `gpt_pt_go_0002` | CWE-22 | normal | `plain` | os.ReadFile | 6-10 | plain function | command_line | terse | without | middle | path_containment_check | Count the lines of a stored text file. |
| 056 | `gpt_pt_go_0021` | CWE-22 | hard_negative | `id_mapped_to_known_file` | os.Create | 11-20 | goroutine or callback | file | descriptive | with | - | - | Open a certificate file by name. |
| 057 | `gpt_cmdi_go_0013` | CWE-78 | normal | `plain` | exec.Command with sh -c | 1-5 | command line tool function | command_line | descriptive | with | late | argv_no_shell | Convert a document to another format with a converter. |
| 058 | `gpt_sqli_go_0002` | CWE-89 | normal | `plain` | database/sql QueryRow | 6-10 | goroutine or callback | database_value | terse | without | early | bound_parameters | Insert a new product review. |
| 059 | `gpt_pt_go_0018` | CWE-22 | safe | `plain` | os.Open | 11-20 | method on a struct | file | descriptive | without | - | - | Rename a document inside the storage folder. |
| 060 | `gpt_pt_go_0011` | CWE-22 | safe | `plain` | os.ReadFile | 21-40 | HTTP handler | web_request | descriptive | without | - | - | Write an exported spreadsheet under a requested name. |
| 061 | `gpt_sqli_go_0014` | CWE-89 | hard_positive | `keyword_blocklist` | gorm Raw | 11-20 | plain function | network_message | terse | with | middle | bound_parameters | Search support tickets by keyword and priority. |
| 062 | `gpt_cmdi_go_0020` | CWE-78 | hard_positive | `validator_accepts_too_much` | exec.Command with arguments | 21-40 | HTTP handler | web_request | terse | without | late | strict_validation | Report the disk usage of a folder. |
| 063 | `gpt_pt_go_0006` | CWE-22 | hard_negative | `id_mapped_to_known_file` | os.Create | 41-100 | goroutine or callback | command_line | terse | with | - | - | Read the first line of a stored file. |
| 064 | `gpt_cmdi_go_0012` | CWE-78 | normal | `plain` | exec.Command with sh -c | 21-40 | plain function | web_request | descriptive | without | early | allow_list | Run a linter on a submitted file and return its report. |
| 065 | `gpt_cmdi_go_0001` | CWE-78 | normal | `plain` | exec.Command with arguments | 11-20 | method on a struct | file | terse | without | early | argv_no_shell | Report the disk usage of a folder. |
| 066 | `gpt_rnd_go_0013` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | math/rand | 11-20 | plain function | not_applicable | terse | with | middle | rejection_sampling_secure_index | Issue a temporary access code for a visitor badge. |
| 067 | `gpt_pt_go_0009` | CWE-22 | normal | `plain` | os.Open | 1-5 | HTTP handler | web_request | descriptive | with | late | library_confinement | Read a plugin manifest from a plugin folder. |
| 068 | `gpt_sqli_go_0007` | CWE-89 | no_code | `plain` | none | 6-10 | command line tool function | not_applicable | terse | with | - | - | Build a display name from first and last name. |
| 069 | `gpt_cmdi_go_0019` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | exec.Command with sh -c | 21-40 | command line tool function | command_line | descriptive | without | - | - | Unpack an uploaded archive into a working folder. |
| 070 | `gpt_cmdi_go_0005` | CWE-78 | no_code | `plain` | none | 11-20 | method on a struct | not_applicable | terse | with | - | - | Turn a byte count into a short size label. |
| 071 | `gpt_rnd_go_0012` | CWE-338 | normal | `plain` | math/rand | 1-5 | helper called by another function | not_applicable | descriptive | with | late | secure_bytes_encoded | Create a deletion confirmation token. |
| 072 | `gpt_sqli_go_0005` | CWE-89 | hard_negative | `constant_fragments_only` | database/sql Query | 41-100 | HTTP handler | web_request | terse | without | - | - | Find a vehicle by its registration number. |
| 073 | `gpt_cmdi_go_0009` | CWE-78 | normal | `plain` | exec.Command with sh -c | 6-10 | plain function | function_argument | terse | without | early | argv_no_shell | Show the owner and permissions of a file. |
| 074 | `gpt_sqli_go_0021` | CWE-89 | normal | `plain` | database/sql QueryRow | 1-5 | goroutine or callback | database_value | descriptive | with | late | bound_parameters | Return a page of articles sorted by a column chosen by the caller. |
| 075 | `gpt_rnd_go_0011` | CWE-338 | safe | `plain` | math/rand | 11-20 | goroutine or callback | not_applicable | descriptive | with | - | - | Create an unguessable id for a private upload. |
| 076 | `gpt_sqli_go_0008` | CWE-89 | hard_negative | `placeholders_only_format` | database/sql Query | 21-40 | goroutine or callback | database_value | terse | with | - | - | Return the latest comments on a post. |
| 077 | `gpt_rnd_go_0002` | CWE-338 | normal | `plain` | math/rand | 1-5 | method on a struct | not_applicable | terse | with | early | rejection_sampling_secure_index | Pick the words of a recovery phrase for a wallet. |
| 078 | `gpt_pt_go_0004` | CWE-22 | safe | `plain` | os.Open | 21-40 | command line tool function | command_line | terse | with | - | - | Move a processed file to an archive folder. |
| 079 | `gpt_pt_go_0007` | CWE-22 | hard_positive | `relative_check_misses_absolute` | http.ServeFile | 11-20 | goroutine or callback | web_request | descriptive | without | early | library_confinement | Read a font file requested by a stylesheet. |
| 080 | `gpt_cmdi_go_0014` | CWE-78 | normal | `plain` | exec.Command with arguments | 41-100 | goroutine or callback | network_message | terse | with | middle | quoting | Check whether a port is open on a host. |
| 081 | `gpt_rnd_go_0004` | CWE-338 | safe | `plain` | math/rand | 21-40 | command line tool function | not_applicable | descriptive | without | - | - | Create an invite code for a team. |
| 082 | `gpt_cmdi_go_0023` | CWE-78 | normal | `plain` | exec.Command with sh -c | 41-100 | goroutine or callback | function_argument | descriptive | with | late | strict_validation | Read the expiry date of a certificate file. |
| 083 | `gpt_rnd_go_0005` | CWE-338 | normal | `plain` | math/rand | 21-40 | HTTP handler | not_applicable | descriptive | without | late | secure_generator_api | Create a list of recovery codes for an account. |
| 084 | `gpt_sqli_go_0015` | CWE-89 | normal | `plain` | database/sql QueryRow | 21-40 | method on a struct | environment | terse | with | late | type_conversion | Look up the shipping address of an order. |
| 085 | `gpt_sqli_go_0012` | CWE-89 | normal | `plain` | database/sql QueryRow | 6-10 | command line tool function | command_line | terse | without | late | query_builder | Find patients by surname. |
| 086 | `gpt_cmdi_go_0004` | CWE-78 | safe | `plain` | exec.Command with arguments | 41-100 | helper called by another function | file | terse | with | - | - | Mount a network share with given options. |
| 087 | `gpt_rnd_go_0018` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | math/rand | 21-40 | helper called by another function | not_applicable | descriptive | with | middle | secure_bytes_encoded | Generate a bearer token for a service account. |
| 088 | `gpt_rnd_go_0001` | CWE-338 | no_code | `plain` | none | 1-5 | goroutine or callback | not_applicable | terse | without | - | - | Mask a token for display in a log line. |
| 089 | `gpt_sqli_go_0001` | CWE-89 | normal | `plain` | database/sql Exec | 21-40 | helper called by another function | function_argument | descriptive | with | early | allow_list | Look up a coupon by its code. |
| 090 | `gpt_rnd_go_0017` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | math/rand | 21-40 | method on a struct | not_applicable | terse | without | - | - | Choose a polling interval spread between workers. |
| 091 | `gpt_pt_go_0024` | CWE-22 | hard_negative | `base_name_only` | os.ReadFile | 6-10 | HTTP handler | network_message | descriptive | without | - | - | Write a crash report file under a given id. |
| 092 | `gpt_cmdi_go_0015` | CWE-78 | safe | `plain` | exec.Command with arguments | 41-100 | goroutine or callback | command_line | descriptive | without | - | - | Read the expiry date of a certificate file. |
| 093 | `gpt_sqli_go_0018` | CWE-89 | safe | `plain` | database/sql QueryRow | 21-40 | helper called by another function | command_line | terse | with | - | - | List reservations for a room between two dates. |
| 094 | `gpt_cmdi_go_0003` | CWE-78 | hard_negative | `constant_shell_command` | exec.Command with arguments | 21-40 | goroutine or callback | web_request | descriptive | without | - | - | Start a background job from a script name. |
| 095 | `gpt_sqli_go_0004` | CWE-89 | normal | `plain` | database/sql QueryRow | 21-40 | goroutine or callback | command_line | descriptive | without | early | allow_list | Transfer a balance between two accounts inside a transaction. |
| 096 | `gpt_pt_go_0012` | CWE-22 | normal | `plain` | os.Create | 21-40 | HTTP handler | database_value | terse | with | early | allow_list_mapping | Write a user's settings file. |
| 097 | `gpt_sqli_go_0020` | CWE-89 | hard_negative | `bound_via_builder` | database/sql Exec | 11-20 | HTTP handler | web_request | descriptive | without | - | - | List the most recent log entries of a service. |
| 098 | `gpt_sqli_go_0017` | CWE-89 | normal | `plain` | sqlx | 6-10 | command line tool function | command_line | descriptive | with | late | allow_list | List a user's orders with a given status. |
| 099 | `gpt_rnd_go_0015` | CWE-338 | normal | `plain` | math/rand | 11-20 | HTTP handler | not_applicable | descriptive | without | middle | secure_generator_api | Generate a CSRF token for a form. |
| 100 | `gpt_rnd_go_0008` | CWE-338 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | descriptive | without | - | - | Compare the lengths of two tokens. |

</details>
