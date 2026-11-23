## Your job

Write **100 rows** with **Gemini** (free base model) in **Go** (CWE-22, CWE-338, CWE-78, CWE-89).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P08_gemini_go.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P08_gemini_go.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P08_gemini_go.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P08_gemini_go.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Personal branch `dev/<your-github-username>` made from `main`; issue branch `issue/<number>-P08_gemini_go` made from your personal branch
- [ ] All 100 prompts pasted into Gemini (new chat for every 10 rows, master prompt first) and every answer pasted under its `=== NNN` line in `submissions/P08_gemini_go.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into your personal branch with **only** `submissions/P08_gemini_go.txt`; the exact model name written in the description
- [ ] After approval: merged into your personal branch, then one last pull request `dev/<your-github-username>` into `main`

Mix of rows in this package: normal 33, hard_positive 16, safe 16, hard_negative 27, no_code 8. Lengths: 1-5: 5, 6-10: 23, 11-20: 32, 21-40: 25, 41-100: 15.

<details><summary>Table of all rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `gem_rnd_go_0013` | CWE-338 | normal | `plain` | math/rand | 21-40 | helper called by another function | not_applicable | descriptive | without | late | secure_generator_api | Create a token for confirming a newsletter subscription. |
| 002 | `gem_sqli_go_0021` | CWE-89 | safe | `plain` | database/sql Query | 21-40 | goroutine or callback | command_line | terse | with | - | - | Return the stock quantity for a product code. |
| 003 | `gem_cmdi_go_0021` | CWE-78 | safe | `plain` | exec.Command with sh -c | 41-100 | method on a struct | function_argument | terse | with | - | - | Start a background job from a script name. |
| 004 | `gem_cmdi_go_0014` | CWE-78 | hard_negative | `argument_list_with_user_data` | exec.Command with arguments | 21-40 | helper called by another function | web_request | terse | with | - | - | Print the version of a tool chosen from a list. |
| 005 | `gem_rnd_go_0002` | CWE-338 | normal | `plain` | math/rand | 6-10 | plain function | not_applicable | terse | with | late | secure_bytes_encoded | Generate a session key for an encrypted chat. |
| 006 | `gem_pt_go_0006` | CWE-22 | normal | `plain` | http.ServeFile | 1-5 | method on a struct | environment | terse | with | late | allow_list_mapping | Return the contents of a help page file. |
| 007 | `gem_rnd_go_0009` | CWE-338 | hard_negative | `ordinary_random_shuffling` | math/rand | 6-10 | helper called by another function | not_applicable | descriptive | without | - | - | Shuffle a playlist before playing it. |
| 008 | `gem_cmdi_go_0022` | CWE-78 | safe | `plain` | exec.Command with sh -c | 11-20 | helper called by another function | web_request | descriptive | without | - | - | Mount a network share with given options. |
| 009 | `gem_sqli_go_0004` | CWE-89 | hard_negative | `identifier_allowlist` | database/sql QueryRow | 6-10 | helper called by another function | environment | descriptive | without | - | - | Update the email address of a user profile. |
| 010 | `gem_sqli_go_0013` | CWE-89 | hard_negative | `placeholders_only_format` | database/sql Exec | 11-20 | plain function | command_line | descriptive | with | - | - | Update the status of a support ticket. |
| 011 | `gem_pt_go_0016` | CWE-22 | normal | `plain` | http.ServeFile | 41-100 | plain function | command_line | descriptive | with | early | base_name_only | Extract the entries of an uploaded archive into a folder. |
| 012 | `gem_cmdi_go_0025` | CWE-78 | normal | `plain` | exec.Command with arguments | 6-10 | command line tool function | command_line | terse | without | late | argv_no_shell | Look up the registration data of a domain. |
| 013 | `gem_cmdi_go_0007` | CWE-78 | normal | `plain` | exec.Command with sh -c | 21-40 | method on a struct | environment | descriptive | with | early | quoting | Count the lines of a file with a standard tool. |
| 014 | `gem_sqli_go_0002` | CWE-89 | safe | `plain` | database/sql Exec | 41-100 | command line tool function | command_line | descriptive | with | - | - | Delete a user's saved bookmarks that match a title. |
| 015 | `gem_rnd_go_0021` | CWE-338 | hard_negative | `ordinary_random_test_data` | math/rand | 6-10 | HTTP handler | not_applicable | terse | without | - | - | Create random order amounts for a demo database. |
| 016 | `gem_cmdi_go_0017` | CWE-78 | safe | `plain` | exec.Command with sh -c | 6-10 | helper called by another function | function_argument | descriptive | without | - | - | Restart a named system service. |
| 017 | `gem_cmdi_go_0020` | CWE-78 | safe | `plain` | exec.Command with sh -c | 41-100 | plain function | environment | descriptive | without | - | - | Convert an audio file to another bitrate. |
| 018 | `gem_pt_go_0004` | CWE-22 | no_code | `plain` | none | 6-10 | HTTP handler | not_applicable | descriptive | with | - | - | Get the extension of a file name given as text. |
| 019 | `gem_pt_go_0007` | CWE-22 | normal | `plain` | archive extraction (archive/zip) | 11-20 | helper called by another function | command_line | descriptive | without | middle | path_containment_check | Serve a static asset such as an image or stylesheet. |
| 020 | `gem_pt_go_0017` | CWE-22 | hard_positive | `relative_check_misses_absolute` | archive extraction (archive/zip) | 21-40 | goroutine or callback | database_value | terse | with | late | allow_list_mapping | Read the first line of a stored file. |
| 021 | `gem_pt_go_0009` | CWE-22 | no_code | `plain` | none | 11-20 | HTTP handler | not_applicable | descriptive | without | - | - | Compute a human readable size label. |
| 022 | `gem_rnd_go_0017` | CWE-338 | no_code | `plain` | none | 11-20 | plain function | not_applicable | terse | with | - | - | Group a token into blocks of four characters. |
| 023 | `gem_sqli_go_0003` | CWE-89 | normal | `plain` | gorm Raw | 6-10 | plain function | file | terse | without | middle | type_conversion | Search a phone book by name prefix. |
| 024 | `gem_pt_go_0018` | CWE-22 | hard_negative | `library_confined_access` | http.ServeFile | 11-20 | method on a struct | network_message | descriptive | with | - | - | Read a log file of a named service. |
| 025 | `gem_cmdi_go_0005` | CWE-78 | no_code | `plain` | none | 6-10 | goroutine or callback | not_applicable | terse | with | - | - | Format a duration in seconds as hours and minutes. |
| 026 | `gem_rnd_go_0006` | CWE-338 | normal | `plain` | math/rand | 6-10 | HTTP handler | not_applicable | terse | with | early | secure_bytes_encoded | Create a token for confirming a newsletter subscription. |
| 027 | `gem_rnd_go_0003` | CWE-338 | safe | `plain` | math/rand | 21-40 | helper called by another function | not_applicable | terse | with | - | - | Generate a temporary password for a new account. |
| 028 | `gem_sqli_go_0011` | CWE-89 | hard_positive | `one_branch_bound` | database/sql Query | 11-20 | method on a struct | network_message | terse | with | late | allow_list | Record an audit entry for an administrator action. |
| 029 | `gem_sqli_go_0024` | CWE-89 | normal | `plain` | sqlx | 11-20 | plain function | database_value | descriptive | without | middle | bound_parameters | List the appointments of a doctor on a given day. |
| 030 | `gem_rnd_go_0025` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | math/rand | 21-40 | plain function | not_applicable | terse | without | late | secure_generator_api | Create a cookie value for a remember-me login. |
| 031 | `gem_pt_go_0001` | CWE-22 | hard_positive | `check_before_normalising` | os.ReadFile | 41-100 | method on a struct | network_message | descriptive | with | late | path_containment_check | Read the lines of a CSV import file. |
| 032 | `gem_pt_go_0020` | CWE-22 | hard_positive | `check_before_normalising` | http.ServeFile | 11-20 | plain function | file | terse | without | middle | allow_list_mapping | Return the contents of a shared snippet file. |
| 033 | `gem_rnd_go_0012` | CWE-338 | no_code | `plain` | none | 6-10 | method on a struct | not_applicable | descriptive | without | - | - | Compute the check digit of a number. |
| 034 | `gem_sqli_go_0020` | CWE-89 | normal | `plain` | sqlx | 11-20 | goroutine or callback | environment | terse | without | early | query_builder | List the files shared with a user. |
| 035 | `gem_pt_go_0021` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 21-40 | plain function | database_value | descriptive | without | - | - | Append a line to a user's activity log. |
| 036 | `gem_sqli_go_0015` | CWE-89 | hard_negative | `constant_fragments_only` | database/sql Query | 21-40 | plain function | environment | terse | with | - | - | Set the stock quantity of a product after a delivery. |
| 037 | `gem_pt_go_0010` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | os.Create | 11-20 | goroutine or callback | web_request | descriptive | without | - | - | Read a plugin manifest from a plugin folder. |
| 038 | `gem_rnd_go_0004` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | math/rand | 6-10 | HTTP handler | not_applicable | terse | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 039 | `gem_rnd_go_0016` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | math/rand | 21-40 | helper called by another function | not_applicable | terse | with | early | secure_generator_api | Create a one-time code for two-factor sign in. |
| 040 | `gem_pt_go_0022` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | http.ServeFile | 6-10 | plain function | web_request | terse | with | - | - | Return the modification time of a stored file. |
| 041 | `gem_sqli_go_0010` | CWE-89 | hard_negative | `identifier_allowlist` | database/sql QueryRow | 11-20 | plain function | network_message | descriptive | with | - | - | Return the top sellers for a given region. |
| 042 | `gem_cmdi_go_0023` | CWE-78 | normal | `plain` | exec.Command with sh -c | 21-40 | HTTP handler | web_request | descriptive | with | early | strict_validation | Pack an installer from a folder with a packaging tool. |
| 043 | `gem_pt_go_0013` | CWE-22 | normal | `plain` | os.Create | 11-20 | method on a struct | database_value | terse | without | early | library_confinement | Unzip a theme package into the themes folder. |
| 044 | `gem_sqli_go_0008` | CWE-89 | safe | `plain` | gorm Raw | 21-40 | HTTP handler | web_request | descriptive | without | - | - | Count the unread messages of a user. |
| 045 | `gem_pt_go_0023` | CWE-22 | hard_negative | `base_name_only` | os.Create | 11-20 | method on a struct | environment | descriptive | with | - | - | Load a configuration file for a named profile. |
| 046 | `gem_sqli_go_0017` | CWE-89 | no_code | `plain` | none | 11-20 | HTTP handler | not_applicable | terse | without | - | - | Parse a CSV line into fields. |
| 047 | `gem_cmdi_go_0003` | CWE-78 | normal | `plain` | exec.Command with arguments | 6-10 | goroutine or callback | command_line | descriptive | with | middle | allow_list | Run a spell checker on a text file. |
| 048 | `gem_cmdi_go_0010` | CWE-78 | hard_positive | `dash_argument_injection` | exec.Command with arguments | 11-20 | HTTP handler | database_value | terse | with | middle | quoting | Show the mount information of a device. |
| 049 | `gem_pt_go_0019` | CWE-22 | hard_negative | `base_name_only` | archive extraction (archive/zip) | 41-100 | plain function | command_line | descriptive | without | - | - | Read a language pack for a game. |
| 050 | `gem_cmdi_go_0002` | CWE-78 | normal | `plain` | exec.Command with arguments | 1-5 | HTTP handler | database_value | terse | without | late | strict_validation | Show the commit history of a repository for one author. |
| 051 | `gem_rnd_go_0005` | CWE-338 | hard_negative | `ordinary_random_shuffling` | math/rand | 41-100 | goroutine or callback | not_applicable | terse | with | - | - | Shuffle a playlist before playing it. |
| 052 | `gem_rnd_go_0008` | CWE-338 | normal | `plain` | math/rand | 11-20 | method on a struct | not_applicable | terse | without | late | secure_generator_api | Create a webhook signing secret. |
| 053 | `gem_cmdi_go_0004` | CWE-78 | normal | `plain` | exec.Command with sh -c | 6-10 | HTTP handler | database_value | terse | with | early | allow_list | Query the status of a container by name. |
| 054 | `gem_pt_go_0005` | CWE-22 | normal | `plain` | http.ServeFile | 21-40 | method on a struct | function_argument | descriptive | without | late | library_confinement | List the files in a sub folder of the storage area. |
| 055 | `gem_sqli_go_0007` | CWE-89 | hard_positive | `handwritten_escaping` | database/sql Exec | 41-100 | goroutine or callback | command_line | descriptive | without | early | query_builder | Remove a product from a wishlist. |
| 056 | `gem_pt_go_0015` | CWE-22 | normal | `plain` | os.ReadFile | 6-10 | plain function | environment | descriptive | with | late | path_containment_check | Count the lines of a stored text file. |
| 057 | `gem_cmdi_go_0018` | CWE-78 | normal | `plain` | exec.Command with sh -c | 21-40 | plain function | file | terse | with | late | argv_no_shell | Run a linter on a submitted file and return its report. |
| 058 | `gem_sqli_go_0014` | CWE-89 | normal | `plain` | database/sql Query | 11-20 | method on a struct | file | terse | without | early | allow_list | Get the loyalty points of a customer. |
| 059 | `gem_cmdi_go_0015` | CWE-78 | hard_negative | `user_data_after_end_of_options` | exec.Command with sh -c | 11-20 | method on a struct | database_value | terse | without | - | - | Extract a thumbnail frame from a video file. |
| 060 | `gem_sqli_go_0023` | CWE-89 | hard_negative | `identifier_allowlist` | gorm Raw | 21-40 | method on a struct | function_argument | descriptive | without | - | - | Transfer a balance between two accounts inside a transaction. |
| 061 | `gem_rnd_go_0024` | CWE-338 | normal | `plain` | math/rand | 11-20 | helper called by another function | not_applicable | terse | with | early | secure_generator_api | Issue a device registration token. |
| 062 | `gem_pt_go_0014` | CWE-22 | normal | `plain` | os.ReadFile | 11-20 | method on a struct | command_line | descriptive | with | early | path_containment_check | Truncate a log file chosen by name. |
| 063 | `gem_pt_go_0003` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | os.ReadFile | 6-10 | command line tool function | command_line | descriptive | with | - | - | Read a font file requested by a stylesheet. |
| 064 | `gem_cmdi_go_0016` | CWE-78 | hard_positive | `quoting_in_wrong_context` | exec.Command with sh -c | 11-20 | plain function | command_line | descriptive | with | middle | argv_no_shell | Show the fingerprint of an ssh key file. |
| 065 | `gem_rnd_go_0015` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | math/rand | 41-100 | command line tool function | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Generate an initialization vector for encrypting a file. |
| 066 | `gem_sqli_go_0025` | CWE-89 | hard_positive | `one_branch_bound` | gorm Raw | 21-40 | HTTP handler | web_request | descriptive | without | early | allow_list | Search a product catalogue with optional filters for price and brand. |
| 067 | `gem_pt_go_0011` | CWE-22 | normal | `plain` | http.ServeFile | 11-20 | helper called by another function | web_request | terse | with | late | base_name_only | Delete temporary files that match a name. |
| 068 | `gem_cmdi_go_0006` | CWE-78 | hard_positive | `partial_shell_character_filter` | exec.Command with arguments | 11-20 | HTTP handler | database_value | descriptive | without | middle | argv_no_shell | Zip the contents of a folder into a named archive. |
| 069 | `gem_sqli_go_0009` | CWE-89 | normal | `plain` | gorm Raw | 21-40 | goroutine or callback | web_request | descriptive | with | early | query_builder | Update the status of a support ticket. |
| 070 | `gem_pt_go_0008` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 41-100 | HTTP handler | web_request | descriptive | with | - | - | Create a backup copy of a document. |
| 071 | `gem_cmdi_go_0013` | CWE-78 | hard_negative | `command_from_fixed_map` | exec.Command with arguments | 6-10 | HTTP handler | web_request | terse | without | - | - | Download a web page with a command line client. |
| 072 | `gem_rnd_go_0011` | CWE-338 | hard_negative | `fixed_seed_reproducible` | math/rand | 11-20 | command line tool function | not_applicable | descriptive | without | - | - | Draw the same sample every run for a reproducible experiment. |
| 073 | `gem_pt_go_0012` | CWE-22 | hard_positive | `prefix_test_without_separator` | http.ServeFile | 21-40 | helper called by another function | file | terse | with | middle | library_confinement | Let a user download a generated report by name. |
| 074 | `gem_pt_go_0024` | CWE-22 | hard_negative | `library_confined_access` | os.ReadFile | 11-20 | command line tool function | command_line | terse | with | - | - | Report the size of a stored file. |
| 075 | `gem_sqli_go_0012` | CWE-89 | normal | `plain` | database/sql Query | 1-5 | helper called by another function | network_message | descriptive | with | late | type_conversion | Find all students enrolled in a course. |
| 076 | `gem_sqli_go_0022` | CWE-89 | hard_negative | `constant_fragments_only` | sqlx | 21-40 | HTTP handler | web_request | terse | without | - | - | Update the email address of a user profile. |
| 077 | `gem_pt_go_0002` | CWE-22 | safe | `plain` | os.Create | 21-40 | plain function | file | terse | without | - | - | Read a user's saved draft. |
| 078 | `gem_rnd_go_0018` | CWE-338 | normal | `plain` | math/rand | 11-20 | method on a struct | not_applicable | terse | with | middle | secure_bytes_encoded | Generate a secret for a shared team calendar link. |
| 079 | `gem_sqli_go_0018` | CWE-89 | hard_positive | `keyword_blocklist` | sqlx | 6-10 | helper called by another function | environment | terse | with | middle | bound_parameters | Search support tickets by keyword and priority. |
| 080 | `gem_sqli_go_0005` | CWE-89 | safe | `plain` | database/sql Exec | 11-20 | goroutine or callback | file | descriptive | without | - | - | Fetch an invoice by its number. |
| 081 | `gem_cmdi_go_0011` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | exec.Command with sh -c | 21-40 | method on a struct | network_message | terse | with | - | - | Search a log file for lines containing a term. |
| 082 | `gem_rnd_go_0007` | CWE-338 | hard_negative | `fixed_seed_reproducible` | math/rand | 41-100 | helper called by another function | not_applicable | descriptive | with | - | - | Generate reproducible synthetic data for a unit test. |
| 083 | `gem_cmdi_go_0012` | CWE-78 | no_code | `plain` | none | 1-5 | HTTP handler | not_applicable | descriptive | with | - | - | Join a list of words into a title. |
| 084 | `gem_sqli_go_0001` | CWE-89 | normal | `plain` | database/sql Exec | 41-100 | method on a struct | file | descriptive | with | middle | allow_list | Delete a user's saved bookmarks that match a title. |
| 085 | `gem_sqli_go_0016` | CWE-89 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | descriptive | without | - | - | Compute an age from a birth date. |
| 086 | `gem_pt_go_0025` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 11-20 | helper called by another function | command_line | terse | without | - | - | Open a video file for streaming. |
| 087 | `gem_cmdi_go_0019` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | exec.Command with arguments | 11-20 | command line tool function | command_line | terse | with | - | - | Unpack an uploaded archive into a working folder. |
| 088 | `gem_rnd_go_0014` | CWE-338 | safe | `plain` | math/rand | 21-40 | helper called by another function | not_applicable | descriptive | without | - | - | Generate a one-time login link token. |
| 089 | `gem_rnd_go_0019` | CWE-338 | normal | `plain` | math/rand | 6-10 | goroutine or callback | not_applicable | terse | with | early | secure_bytes_encoded | Generate an unlock code for a smart lock. |
| 090 | `gem_sqli_go_0006` | CWE-89 | hard_negative | `integer_forced` | sqlx | 21-40 | command line tool function | command_line | descriptive | with | - | - | Find events happening in a given city. |
| 091 | `gem_rnd_go_0001` | CWE-338 | hard_positive | `weak_value_hashed` | math/rand | 6-10 | method on a struct | not_applicable | descriptive | with | late | secure_bytes_encoded | Generate a password reset token to email to a user. |
| 092 | `gem_sqli_go_0019` | CWE-89 | normal | `plain` | database/sql QueryRow | 41-100 | goroutine or callback | database_value | descriptive | with | late | bound_parameters | Count signups per day for a date range. |
| 093 | `gem_cmdi_go_0008` | CWE-78 | hard_negative | `constant_shell_command` | exec.Command with sh -c | 6-10 | method on a struct | function_argument | descriptive | without | - | - | Sync a folder to a remote host over ssh. |
| 094 | `gem_rnd_go_0023` | CWE-338 | hard_negative | `ordinary_random_simulation` | math/rand | 21-40 | plain function | not_applicable | terse | with | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 095 | `gem_rnd_go_0020` | CWE-338 | safe | `plain` | math/rand | 21-40 | goroutine or callback | not_applicable | descriptive | without | - | - | Issue a ticket secret for a QR code. |
| 096 | `gem_cmdi_go_0024` | CWE-78 | hard_positive | `partial_shell_character_filter` | exec.Command with sh -c | 41-100 | goroutine or callback | file | terse | without | middle | allow_list | Extract a thumbnail frame from a video file. |
| 097 | `gem_rnd_go_0022` | CWE-338 | normal | `plain` | math/rand | 41-100 | method on a struct | not_applicable | terse | without | late | secure_bytes_encoded | Generate a booking confirmation code. |
| 098 | `gem_cmdi_go_0001` | CWE-78 | normal | `plain` | exec.Command with sh -c | 1-5 | plain function | network_message | terse | without | late | allow_list | Convert a document to another format with a converter. |
| 099 | `gem_cmdi_go_0009` | CWE-78 | normal | `plain` | exec.Command with sh -c | 11-20 | HTTP handler | web_request | terse | with | late | quoting | Resize an image to a requested size with an external tool. |
| 100 | `gem_rnd_go_0010` | CWE-338 | safe | `plain` | math/rand | 11-20 | command line tool function | not_applicable | terse | without | - | - | Generate a shared secret for a time-based one-time password setup. |

</details>
