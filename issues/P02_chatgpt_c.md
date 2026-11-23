## 🟦 STEP 2 of 2

**Assigned to: bkvishal28.** Do this **after** the warm-up (issue #17) is approved. Rows **006 to 100** (ChatGPT × C).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P02_chatgpt_c.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P02_chatgpt_c.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P02_chatgpt_c.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P02_chatgpt_c.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P02_chatgpt_c` made from your personal branch `dev/bkvishal28` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into ChatGPT (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P02_chatgpt_c.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/bkvishal28` with **only** `submissions/P02_chatgpt_c.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/bkvishal28`; when all your steps are merged, one last pull request `dev/bkvishal28` into `main`

Mix of rows: normal 31, hard_positive 15, safe 15, hard_negative 27, no_code 7.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `gpt_rnd_c_0016` | CWE-338 | normal | `plain` | rand | 41-100 | small embedded or library utility | not_applicable | terse | without | late | secure_generator_api | Issue a temporary access code for a visitor badge. |
| 007 | `gpt_pt_c_0017` | CWE-22 | normal | `plain` | rename | 21-40 | request handler that receives a struct or buffer | database_value | descriptive | with | middle | base_name_only | Return the contents of a help page file. |
| 008 | `gpt_cmdi_c_0005` | CWE-78 | hard_positive | `validator_accepts_too_much` | popen | 6-10 | small embedded or library utility | environment | terse | without | early | allow_list | Send a document to a named printer. |
| 009 | `gpt_pt_c_0007` | CWE-22 | safe | `plain` | rename | 6-10 | small embedded or library utility | web_request | descriptive | with | - | - | Return a preview of a stored image. |
| 010 | `gpt_pt_c_0001` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | fopen | 41-100 | helper called by another function | environment | descriptive | without | - | - | Count the lines of a stored text file. |
| 011 | `gpt_rnd_c_0015` | CWE-338 | hard_negative | `ordinary_random_sampling` | srand | 21-40 | small embedded or library utility | not_applicable | descriptive | without | - | - | Choose which products to feature on the home page. |
| 012 | `gpt_pt_c_0008` | CWE-22 | safe | `plain` | open | 21-40 | request handler that receives a struct or buffer | web_request | terse | with | - | - | Rename a document inside the storage folder. |
| 013 | `gpt_sqli_c_0006` | CWE-89 | hard_positive | `handwritten_escaping` | mysql_query | 11-20 | plain function | function_argument | descriptive | with | late | type_conversion | Return the stock quantity for a product code. |
| 014 | `gpt_pt_c_0022` | CWE-22 | hard_negative | `base_name_only` | open | 6-10 | request handler that receives a struct or buffer | web_request | terse | without | - | - | Read an email template by name. |
| 015 | `gpt_pt_c_0025` | CWE-22 | normal | `plain` | fopen | 1-5 | command line tool function | command_line | descriptive | without | early | path_containment_check | Copy a template file into a user's workspace. |
| 016 | `gpt_pt_c_0010` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | rename | 11-20 | helper called by another function | function_argument | descriptive | with | - | - | Read an email template by name. |
| 017 | `gpt_sqli_c_0021` | CWE-89 | hard_negative | `constant_fragments_only` | sqlite3_exec | 41-100 | command line tool function | command_line | descriptive | without | - | - | Fetch an invoice by its number. |
| 018 | `gpt_sqli_c_0002` | CWE-89 | hard_negative | `placeholders_only_format` | PQexec | 11-20 | plain function | function_argument | descriptive | without | - | - | Find all students enrolled in a course. |
| 019 | `gpt_cmdi_c_0008` | CWE-78 | normal | `plain` | execl through sh -c | 1-5 | callback passed as a function pointer | web_request | descriptive | without | late | strict_validation | Send a document to a named printer. |
| 020 | `gpt_sqli_c_0005` | CWE-89 | normal | `plain` | PQexec | 41-100 | small embedded or library utility | command_line | descriptive | without | late | type_conversion | Report order totals grouped by a chosen category. |
| 021 | `gpt_cmdi_c_0009` | CWE-78 | normal | `plain` | execvp | 41-100 | command line tool function | command_line | terse | with | late | strict_validation | Check whether a port is open on a host. |
| 022 | `gpt_cmdi_c_0004` | CWE-78 | normal | `plain` | popen | 11-20 | callback passed as a function pointer | database_value | terse | without | early | argv_no_shell | Print the version of a tool chosen from a list. |
| 023 | `gpt_sqli_c_0023` | CWE-89 | normal | `plain` | sqlite3_exec | 21-40 | command line tool function | command_line | descriptive | with | late | allow_list | Find events happening in a given city. |
| 024 | `gpt_pt_c_0009` | CWE-22 | hard_positive | `check_before_normalising` | fopen | 11-20 | command line tool function | command_line | terse | without | middle | base_name_only | Create a thumbnail file next to the original image. |
| 025 | `gpt_sqli_c_0020` | CWE-89 | safe | `plain` | mysql_query | 11-20 | small embedded or library utility | database_value | terse | without | - | - | Set the stock quantity of a product after a delivery. |
| 026 | `gpt_rnd_c_0013` | CWE-338 | hard_negative | `ordinary_random_sampling` | rand | 21-40 | command line tool function | not_applicable | descriptive | without | - | - | Pick a random sample of users for a satisfaction survey. |
| 027 | `gpt_rnd_c_0023` | CWE-338 | hard_negative | `ordinary_random_shuffling` | srand | 21-40 | command line tool function | not_applicable | terse | with | - | - | Shuffle a playlist before playing it. |
| 028 | `gpt_cmdi_c_0006` | CWE-78 | hard_negative | `user_data_after_end_of_options` | system | 6-10 | helper called by another function | environment | descriptive | with | - | - | Look up the registration data of a domain. |
| 029 | `gpt_cmdi_c_0016` | CWE-78 | hard_negative | `argument_list_with_user_data` | execvp | 6-10 | helper called by another function | command_line | terse | without | - | - | Look up the DNS records of a host name. |
| 030 | `gpt_rnd_c_0003` | CWE-338 | normal | `plain` | rand | 41-100 | plain function | not_applicable | descriptive | with | middle | secure_bytes_encoded | Generate a bearer token for a service account. |
| 031 | `gpt_cmdi_c_0017` | CWE-78 | normal | `plain` | execvp | 21-40 | request handler that receives a struct or buffer | database_value | terse | with | early | allow_list | Resize an image to a requested size with an external tool. |
| 032 | `gpt_sqli_c_0011` | CWE-89 | hard_negative | `bound_via_builder` | mysql_query | 21-40 | callback passed as a function pointer | function_argument | descriptive | with | - | - | List the most recent log entries of a service. |
| 033 | `gpt_sqli_c_0012` | CWE-89 | safe | `plain` | PQexec | 21-40 | command line tool function | command_line | descriptive | with | - | - | Mark a notification as read for a user. |
| 034 | `gpt_rnd_c_0017` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | srand | 21-40 | command line tool function | not_applicable | descriptive | with | - | - | Generate an initialization vector for encrypting a file. |
| 035 | `gpt_cmdi_c_0014` | CWE-78 | hard_positive | `validator_accepts_too_much` | execl through sh -c | 41-100 | command line tool function | command_line | terse | with | late | argv_no_shell | Convert an audio file to another bitrate. |
| 036 | `gpt_sqli_c_0010` | CWE-89 | safe | `plain` | sqlite3_exec | 6-10 | plain function | environment | terse | with | - | - | Remove a product from a wishlist. |
| 037 | `gpt_sqli_c_0008` | CWE-89 | normal | `plain` | sqlite3_exec | 1-5 | helper called by another function | file | terse | without | middle | prepared_statement_bind | Search products whose name contains a keyword. |
| 038 | `gpt_rnd_c_0001` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random | 21-40 | plain function | not_applicable | terse | without | early | secure_bytes_encoded | Issue a device registration token. |
| 039 | `gpt_pt_c_0004` | CWE-22 | normal | `plain` | open | 21-40 | callback passed as a function pointer | web_request | terse | with | late | base_name_only | Read the first line of a stored file. |
| 040 | `gpt_sqli_c_0009` | CWE-89 | hard_positive | `keyword_blocklist` | PQexec | 11-20 | callback passed as a function pointer | command_line | descriptive | with | early | allow_list | Look up the shipping address of an order. |
| 041 | `gpt_cmdi_c_0021` | CWE-78 | hard_negative | `constant_shell_command` | execvp | 11-20 | plain function | command_line | descriptive | without | - | - | Search a log file for lines containing a term. |
| 042 | `gpt_rnd_c_0008` | CWE-338 | normal | `plain` | rand | 41-100 | callback passed as a function pointer | not_applicable | descriptive | without | late | secure_generator_api | Generate a one-time login link token. |
| 043 | `gpt_cmdi_c_0019` | CWE-78 | normal | `plain` | popen | 1-5 | plain function | web_request | descriptive | with | early | allow_list | Back up a directory to another location with a sync tool. |
| 044 | `gpt_pt_c_0002` | CWE-22 | normal | `plain` | unlink | 11-20 | callback passed as a function pointer | network_message | descriptive | without | early | base_name_only | Read a user's saved draft. |
| 045 | `gpt_sqli_c_0019` | CWE-89 | hard_negative | `integer_forced` | PQexec | 11-20 | callback passed as a function pointer | web_request | terse | without | - | - | List the appointments of a doctor on a given day. |
| 046 | `gpt_cmdi_c_0010` | CWE-78 | safe | `plain` | popen | 21-40 | small embedded or library utility | command_line | descriptive | without | - | - | Run a linter on a submitted file and return its report. |
| 047 | `gpt_cmdi_c_0018` | CWE-78 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | terse | with | - | - | Format a duration in seconds as hours and minutes. |
| 048 | `gpt_rnd_c_0007` | CWE-338 | safe | `plain` | rand | 11-20 | small embedded or library utility | not_applicable | descriptive | without | - | - | Create a list of recovery codes for an account. |
| 049 | `gpt_pt_c_0020` | CWE-22 | no_code | `plain` | none | 1-5 | plain function | not_applicable | terse | without | - | - | Normalize repeated slashes in a path string. |
| 050 | `gpt_cmdi_c_0001` | CWE-78 | hard_negative | `argument_list_with_user_data` | system | 21-40 | callback passed as a function pointer | web_request | descriptive | without | - | - | Query a package manager for the version of a package. |
| 051 | `gpt_sqli_c_0024` | CWE-89 | hard_positive | `bound_but_input_identifier` | PQexec | 41-100 | callback passed as a function pointer | web_request | terse | with | early | prepared_statement_bind | Find a vehicle by its registration number. |
| 052 | `gpt_pt_c_0016` | CWE-22 | normal | `plain` | unlink | 6-10 | request handler that receives a struct or buffer | web_request | descriptive | without | early | allow_list_mapping | Load a configuration file for a named profile. |
| 053 | `gpt_pt_c_0011` | CWE-22 | normal | `plain` | rename | 41-100 | request handler that receives a struct or buffer | web_request | descriptive | without | early | path_containment_check | Check whether a named file exists in the storage area. |
| 054 | `gpt_rnd_c_0018` | CWE-338 | no_code | `plain` | none | 6-10 | request handler that receives a struct or buffer | not_applicable | terse | with | - | - | Compute the check digit of a number. |
| 055 | `gpt_rnd_c_0022` | CWE-338 | normal | `plain` | srand | 1-5 | helper called by another function | not_applicable | terse | without | early | secure_bytes_encoded | Create a token for confirming a newsletter subscription. |
| 056 | `gpt_rnd_c_0004` | CWE-338 | normal | `plain` | rand | 21-40 | request handler that receives a struct or buffer | not_applicable | descriptive | without | middle | secure_bytes_encoded | Generate a temporary password for a new account. |
| 057 | `gpt_rnd_c_0010` | CWE-338 | normal | `plain` | srand | 11-20 | command line tool function | not_applicable | terse | without | late | secure_bytes_encoded | Create a challenge string for a login handshake. |
| 058 | `gpt_pt_c_0005` | CWE-22 | hard_positive | `prefix_test_without_separator` | open | 11-20 | request handler that receives a struct or buffer | web_request | terse | without | early | allow_list_mapping | Hash the contents of a stored file. |
| 059 | `gpt_cmdi_c_0007` | CWE-78 | normal | `plain` | popen | 11-20 | command line tool function | command_line | descriptive | with | late | argv_no_shell | Add a user to a group with the system tool. |
| 060 | `gpt_cmdi_c_0002` | CWE-78 | hard_positive | `validation_of_other_variable` | system | 21-40 | plain function | database_value | terse | without | middle | argv_no_shell | Run a database backup tool for one schema. |
| 061 | `gpt_pt_c_0023` | CWE-22 | hard_negative | `library_confined_access` | unlink | 11-20 | request handler that receives a struct or buffer | web_request | descriptive | with | - | - | Return the contents of a shared snippet file. |
| 062 | `gpt_cmdi_c_0003` | CWE-78 | safe | `plain` | execvp | 6-10 | command line tool function | command_line | descriptive | without | - | - | Show the commit history of a repository for one author. |
| 063 | `gpt_rnd_c_0021` | CWE-338 | no_code | `plain` | none | 11-20 | callback passed as a function pointer | not_applicable | terse | with | - | - | Format a recovery code list for printing. |
| 064 | `gpt_rnd_c_0024` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random | 11-20 | callback passed as a function pointer | not_applicable | descriptive | with | late | secure_generator_api | Create a cookie value for a remember-me login. |
| 065 | `gpt_rnd_c_0019` | CWE-338 | hard_positive | `weak_value_hashed` | random | 11-20 | helper called by another function | not_applicable | terse | without | early | secure_generator_api | Create a private link token for a quiz. |
| 066 | `gpt_cmdi_c_0022` | CWE-78 | hard_negative | `user_data_after_end_of_options` | popen | 6-10 | request handler that receives a struct or buffer | web_request | terse | without | - | - | Compute the checksum of a file. |
| 067 | `gpt_cmdi_c_0025` | CWE-78 | no_code | `plain` | none | 1-5 | plain function | not_applicable | terse | without | - | - | Compute a percentage of a total. |
| 068 | `gpt_cmdi_c_0020` | CWE-78 | hard_negative | `argument_list_with_user_data` | popen | 21-40 | plain function | environment | descriptive | with | - | - | Check whether a host answers a network ping. |
| 069 | `gpt_rnd_c_0025` | CWE-338 | hard_negative | `fixed_seed_reproducible` | random | 6-10 | helper called by another function | not_applicable | terse | with | - | - | Draw the same sample every run for a reproducible experiment. |
| 070 | `gpt_cmdi_c_0011` | CWE-78 | normal | `plain` | execl through sh -c | 21-40 | helper called by another function | command_line | terse | without | early | argv_no_shell | Show the fingerprint of an ssh key file. |
| 071 | `gpt_cmdi_c_0013` | CWE-78 | safe | `plain` | execvp | 11-20 | helper called by another function | environment | descriptive | without | - | - | Pack an installer from a folder with a packaging tool. |
| 072 | `gpt_pt_c_0003` | CWE-22 | safe | `plain` | unlink | 21-40 | plain function | network_message | descriptive | with | - | - | Serve a static asset such as an image or stylesheet. |
| 073 | `gpt_pt_c_0006` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | unlink | 21-40 | small embedded or library utility | database_value | descriptive | with | - | - | Open a video file for streaming. |
| 074 | `gpt_sqli_c_0018` | CWE-89 | no_code | `plain` | none | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | without | - | - | Compute an age from a birth date. |
| 075 | `gpt_sqli_c_0003` | CWE-89 | hard_positive | `keyword_blocklist` | PQexec | 41-100 | small embedded or library utility | file | terse | with | late | type_conversion | Find books by author name. |
| 076 | `gpt_cmdi_c_0012` | CWE-78 | safe | `plain` | system | 6-10 | plain function | network_message | descriptive | without | - | - | Compress a log file after rotation. |
| 077 | `gpt_cmdi_c_0024` | CWE-78 | normal | `plain` | popen | 11-20 | command line tool function | command_line | terse | without | middle | quoting | Resize an image to a requested size with an external tool. |
| 078 | `gpt_pt_c_0024` | CWE-22 | no_code | `plain` | none | 11-20 | plain function | not_applicable | terse | without | - | - | Compute a human readable size label. |
| 079 | `gpt_sqli_c_0015` | CWE-89 | normal | `plain` | mysql_query | 6-10 | command line tool function | command_line | terse | without | early | type_conversion | Delete expired sessions older than a number of days. |
| 080 | `gpt_sqli_c_0025` | CWE-89 | hard_negative | `bound_via_builder` | PQexec | 21-40 | request handler that receives a struct or buffer | web_request | descriptive | without | - | - | Get the loyalty points of a customer. |
| 081 | `gpt_rnd_c_0005` | CWE-338 | normal | `plain` | random | 11-20 | callback passed as a function pointer | not_applicable | terse | with | early | secure_generator_api | Create an encryption key for a local vault. |
| 082 | `gpt_pt_c_0012` | CWE-22 | hard_positive | `extension_check_only` | unlink | 6-10 | plain function | command_line | terse | with | early | path_containment_check | Delete a user's attachment. |
| 083 | `gpt_rnd_c_0012` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | srand | 21-40 | plain function | not_applicable | terse | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 084 | `gpt_sqli_c_0007` | CWE-89 | normal | `plain` | PQexec | 6-10 | helper called by another function | network_message | descriptive | with | middle | type_conversion | Look up a city by postal code. |
| 085 | `gpt_rnd_c_0020` | CWE-338 | safe | `plain` | random | 21-40 | command line tool function | not_applicable | descriptive | with | - | - | Generate a CSRF token for a form. |
| 086 | `gpt_sqli_c_0017` | CWE-89 | normal | `plain` | sqlite3_exec | 21-40 | request handler that receives a struct or buffer | database_value | descriptive | without | early | allow_list | Return a page of articles sorted by a column chosen by the caller. |
| 087 | `gpt_pt_c_0021` | CWE-22 | normal | `plain` | rename | 1-5 | command line tool function | command_line | terse | with | late | base_name_only | Load the translation file for a locale. |
| 088 | `gpt_sqli_c_0001` | CWE-89 | hard_negative | `integer_forced` | PQexec | 21-40 | plain function | web_request | descriptive | without | - | - | Set the stock quantity of a product after a delivery. |
| 089 | `gpt_cmdi_c_0023` | CWE-78 | hard_positive | `dash_argument_injection` | system | 11-20 | callback passed as a function pointer | command_line | terse | with | early | strict_validation | Run a linter on a submitted file and return its report. |
| 090 | `gpt_pt_c_0014` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | fopen | 6-10 | small embedded or library utility | file | terse | with | - | - | Read a plugin manifest from a plugin folder. |
| 091 | `gpt_cmdi_c_0015` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | execl through sh -c | 6-10 | helper called by another function | file | descriptive | without | - | - | Unpack an uploaded archive into a working folder. |
| 092 | `gpt_pt_c_0013` | CWE-22 | safe | `plain` | open | 6-10 | callback passed as a function pointer | web_request | terse | without | - | - | Write a crash report file under a given id. |
| 093 | `gpt_rnd_c_0014` | CWE-338 | hard_negative | `ordinary_random_test_data` | rand | 6-10 | plain function | not_applicable | descriptive | with | - | - | Create random order amounts for a demo database. |
| 094 | `gpt_pt_c_0015` | CWE-22 | normal | `plain` | open | 11-20 | command line tool function | command_line | terse | without | middle | allow_list_mapping | Create a thumbnail file next to the original image. |
| 095 | `gpt_sqli_c_0014` | CWE-89 | normal | `plain` | sqlite3_exec | 11-20 | plain function | network_message | terse | without | middle | allow_list | Find all students enrolled in a course. |
| 096 | `gpt_sqli_c_0013` | CWE-89 | safe | `plain` | sqlite3_exec | 11-20 | helper called by another function | network_message | terse | without | - | - | Find events happening in a given city. |
| 097 | `gpt_pt_c_0019` | CWE-22 | normal | `plain` | rename | 21-40 | command line tool function | command_line | terse | with | early | base_name_only | Unzip a theme package into the themes folder. |
| 098 | `gpt_sqli_c_0004` | CWE-89 | hard_negative | `identifier_allowlist` | sqlite3_exec | 6-10 | callback passed as a function pointer | function_argument | terse | with | - | - | Fetch the configuration value for a given key and environment. |
| 099 | `gpt_rnd_c_0009` | CWE-338 | hard_positive | `weak_value_hashed` | random | 11-20 | small embedded or library utility | not_applicable | terse | without | early | secure_bytes_encoded | Generate a session key for an encrypted chat. |
| 100 | `gpt_rnd_c_0006` | CWE-338 | safe | `plain` | random | 6-10 | request handler that receives a struct or buffer | not_applicable | descriptive | with | - | - | Create a session identifier for a signed-in user. |

</details>
