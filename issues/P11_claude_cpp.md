## 🟦 STEP 2 of 2

**Assigned to: jeevikaar.** Do this **after** the warm-up (issue #26) is approved. Rows **006 to 100** (Claude × C++).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P11_claude_cpp.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P11_claude_cpp.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P11_claude_cpp.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P11_claude_cpp.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P11_claude_cpp` made from your personal branch `dev/jeevikaar` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into Claude (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P11_claude_cpp.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/jeevikaar` with **only** `submissions/P11_claude_cpp.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/jeevikaar`; when all your steps are merged, one last pull request `dev/jeevikaar` into `main`

Mix of rows: hard_negative 25, no_code 7, normal 33, safe 14, hard_positive 16.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `cla_rnd_cpp_0002` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | std::default_random_engine | 41-100 | command line tool function | not_applicable | descriptive | without | - | - | Issue a gift card code with a check value. |
| 007 | `cla_sqli_cpp_0024` | CWE-89 | hard_negative | `placeholders_only_format` | mysql_query | 21-40 | command line tool function | command_line | descriptive | with | - | - | Find articles that carry a given tag. |
| 008 | `cla_sqli_cpp_0018` | CWE-89 | no_code | `plain` | none | 11-20 | class method | not_applicable | descriptive | with | - | - | Compute an age from a birth date. |
| 009 | `cla_rnd_cpp_0007` | CWE-338 | no_code | `plain` | none | 1-5 | callback, lambda or asynchronous task | not_applicable | descriptive | with | - | - | Group a token into blocks of four characters. |
| 010 | `cla_rnd_cpp_0003` | CWE-338 | normal | `plain` | std::default_random_engine | 41-100 | callback, lambda or asynchronous task | not_applicable | descriptive | with | middle | secure_generator_api | Create a key for a private download link. |
| 011 | `cla_pt_cpp_0017` | CWE-22 | hard_negative | `base_name_only` | std::filesystem | 11-20 | callback, lambda or asynchronous task | command_line | descriptive | with | - | - | Hash the contents of a stored file. |
| 012 | `cla_cmdi_cpp_0003` | CWE-78 | hard_negative | `user_data_after_end_of_options` | QProcess | 21-40 | callback, lambda or asynchronous task | command_line | descriptive | without | - | - | Run a unit conversion script on a value. |
| 013 | `cla_cmdi_cpp_0017` | CWE-78 | safe | `plain` | QProcess | 41-100 | web or network handler that receives a request object | web_request | descriptive | without | - | - | Check whether a port is open on a host. |
| 014 | `cla_rnd_cpp_0018` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | std::default_random_engine | 11-20 | plain function | not_applicable | terse | without | late | rejection_sampling_secure_index | Generate a session key for an encrypted chat. |
| 015 | `cla_pt_cpp_0019` | CWE-22 | hard_negative | `base_name_only` | ifstream or ofstream | 41-100 | command line tool function | command_line | terse | with | - | - | Read a data file for a selected report. |
| 016 | `cla_sqli_cpp_0021` | CWE-89 | normal | `plain` | sqlite3 C API | 1-5 | command line tool function | command_line | terse | with | late | allow_list | List reservations for a room between two dates. |
| 017 | `cla_rnd_cpp_0024` | CWE-338 | normal | `plain` | rand | 21-40 | web or network handler that receives a request object | not_applicable | descriptive | with | late | rejection_sampling_secure_index | Create a key for a private download link. |
| 018 | `cla_cmdi_cpp_0021` | CWE-78 | normal | `plain` | Boost.Process | 1-5 | command line tool function | command_line | terse | without | early | quoting | Execute a report generator with a chosen template. |
| 019 | `cla_cmdi_cpp_0005` | CWE-78 | normal | `plain` | Boost.Process | 21-40 | helper called by another function | web_request | descriptive | with | late | argv_no_shell | Show the mount information of a device. |
| 020 | `cla_sqli_cpp_0014` | CWE-89 | hard_negative | `identifier_allowlist` | mysql_query | 6-10 | command line tool function | command_line | descriptive | with | - | - | Get the loyalty points of a customer. |
| 021 | `cla_sqli_cpp_0015` | CWE-89 | hard_negative | `bound_via_builder` | Qt QSqlQuery | 11-20 | class method | file | terse | without | - | - | Find all accounts created through an affiliate code. |
| 022 | `cla_sqli_cpp_0016` | CWE-89 | safe | `plain` | PQexec | 21-40 | callback, lambda or asynchronous task | environment | descriptive | without | - | - | Insert a new product review. |
| 023 | `cla_cmdi_cpp_0014` | CWE-78 | safe | `plain` | popen | 11-20 | helper called by another function | web_request | terse | without | - | - | Report the disk usage of a folder. |
| 024 | `cla_cmdi_cpp_0004` | CWE-78 | safe | `plain` | system | 11-20 | helper called by another function | environment | terse | without | - | - | Read the expiry date of a certificate file. |
| 025 | `cla_sqli_cpp_0013` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 6-10 | helper called by another function | web_request | terse | with | early | type_conversion | Export the orders of a given month. |
| 026 | `cla_sqli_cpp_0007` | CWE-89 | normal | `plain` | sqlite3 C API | 6-10 | callback, lambda or asynchronous task | command_line | terse | with | middle | query_builder_bind | Return the latest comments on a post. |
| 027 | `cla_pt_cpp_0016` | CWE-22 | normal | `plain` | std::filesystem | 6-10 | callback, lambda or asynchronous task | function_argument | descriptive | with | late | path_containment_check | Truncate a log file chosen by name. |
| 028 | `cla_rnd_cpp_0005` | CWE-338 | safe | `plain` | std::mt19937 | 21-40 | plain function | not_applicable | terse | with | - | - | Create a password for a guest Wi-Fi voucher. |
| 029 | `cla_pt_cpp_0005` | CWE-22 | normal | `plain` | ifstream or ofstream | 1-5 | callback, lambda or asynchronous task | database_value | descriptive | with | middle | base_name_only | Load a configuration file for a named profile. |
| 030 | `cla_rnd_cpp_0014` | CWE-338 | normal | `plain` | rand | 1-5 | web or network handler that receives a request object | not_applicable | terse | with | late | rejection_sampling_secure_index | Issue an invitation link token. |
| 031 | `cla_cmdi_cpp_0006` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | system | 6-10 | web or network handler that receives a request object | database_value | descriptive | without | - | - | Query the status of a container by name. |
| 032 | `cla_sqli_cpp_0003` | CWE-89 | hard_positive | `keyword_blocklist` | MySQL Connector/C++ | 6-10 | plain function | file | descriptive | with | middle | allow_list | Update the email address of a user profile. |
| 033 | `cla_sqli_cpp_0020` | CWE-89 | hard_negative | `integer_forced` | mysql_query | 6-10 | web or network handler that receives a request object | network_message | terse | without | - | - | Update the status of a support ticket. |
| 034 | `cla_cmdi_cpp_0025` | CWE-78 | normal | `plain` | QProcess | 41-100 | callback, lambda or asynchronous task | function_argument | terse | with | late | allow_list | Start a background job from a script name. |
| 035 | `cla_cmdi_cpp_0023` | CWE-78 | normal | `plain` | system | 1-5 | command line tool function | command_line | descriptive | with | middle | argv_no_shell | Convert a document to another format with a converter. |
| 036 | `cla_sqli_cpp_0004` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 6-10 | web or network handler that receives a request object | web_request | terse | with | early | allow_list | List a user's orders with a given status. |
| 037 | `cla_pt_cpp_0008` | CWE-22 | normal | `plain` | std::filesystem | 21-40 | plain function | command_line | terse | without | middle | allow_list_mapping | Write a user's settings file. |
| 038 | `cla_sqli_cpp_0005` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 21-40 | plain function | environment | terse | with | late | type_conversion | Find a customer record by email address. |
| 039 | `cla_cmdi_cpp_0008` | CWE-78 | hard_positive | `validation_of_other_variable` | system | 6-10 | command line tool function | command_line | terse | without | early | allow_list | Sync a folder to a remote host over ssh. |
| 040 | `cla_rnd_cpp_0004` | CWE-338 | normal | `plain` | rand | 11-20 | callback, lambda or asynchronous task | not_applicable | terse | without | middle | secure_generator_api | Generate a PIN for a card activation. |
| 041 | `cla_cmdi_cpp_0022` | CWE-78 | hard_negative | `argument_list_with_user_data` | QProcess | 21-40 | plain function | environment | terse | without | - | - | Send a document to a named printer. |
| 042 | `cla_sqli_cpp_0022` | CWE-89 | normal | `plain` | sqlite3 C API | 6-10 | plain function | function_argument | descriptive | without | middle | allow_list | List reservations for a room between two dates. |
| 043 | `cla_rnd_cpp_0020` | CWE-338 | safe | `plain` | rand | 6-10 | plain function | not_applicable | descriptive | with | - | - | Create an invite code for a team. |
| 044 | `cla_cmdi_cpp_0002` | CWE-78 | hard_positive | `validation_of_other_variable` | system | 6-10 | helper called by another function | database_value | descriptive | without | middle | quoting | Compare two files and show the differences. |
| 045 | `cla_pt_cpp_0009` | CWE-22 | normal | `plain` | std::remove | 1-5 | plain function | function_argument | descriptive | with | middle | base_name_only | Load the translation file for a locale. |
| 046 | `cla_pt_cpp_0010` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | std::filesystem | 41-100 | callback, lambda or asynchronous task | web_request | terse | with | - | - | Load the translation file for a locale. |
| 047 | `cla_pt_cpp_0022` | CWE-22 | hard_positive | `single_pass_parent_removal` | ifstream or ofstream | 41-100 | command line tool function | command_line | descriptive | without | late | allow_list_mapping | Open a video file for streaming. |
| 048 | `cla_sqli_cpp_0023` | CWE-89 | hard_positive | `handwritten_escaping` | MySQL Connector/C++ | 21-40 | helper called by another function | web_request | terse | with | middle | type_conversion | Transfer a balance between two accounts inside a transaction. |
| 049 | `cla_sqli_cpp_0017` | CWE-89 | normal | `plain` | PQexec | 11-20 | class method | function_argument | terse | with | middle | type_conversion | Return the top sellers for a given region. |
| 050 | `cla_pt_cpp_0001` | CWE-22 | normal | `plain` | std::remove | 11-20 | plain function | function_argument | descriptive | with | early | path_containment_check | Append a line to a user's activity log. |
| 051 | `cla_rnd_cpp_0023` | CWE-338 | normal | `plain` | std::default_random_engine | 6-10 | callback, lambda or asynchronous task | not_applicable | descriptive | without | middle | secure_generator_api | Create a verification code for a phone number. |
| 052 | `cla_rnd_cpp_0012` | CWE-338 | hard_negative | `ordinary_random_test_data` | std::mt19937 | 41-100 | helper called by another function | not_applicable | descriptive | without | - | - | Generate random names for test fixtures. |
| 053 | `cla_rnd_cpp_0017` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | rand | 6-10 | class method | not_applicable | terse | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 054 | `cla_rnd_cpp_0010` | CWE-338 | hard_negative | `ordinary_random_games` | std::default_random_engine | 6-10 | class method | not_applicable | descriptive | with | - | - | Roll dice for a board game. |
| 055 | `cla_sqli_cpp_0002` | CWE-89 | hard_negative | `constant_fragments_only` | Qt QSqlQuery | 11-20 | callback, lambda or asynchronous task | function_argument | terse | without | - | - | List a user's orders with a given status. |
| 056 | `cla_cmdi_cpp_0015` | CWE-78 | no_code | `plain` | none | 1-5 | callback, lambda or asynchronous task | not_applicable | descriptive | with | - | - | Turn a byte count into a short size label. |
| 057 | `cla_pt_cpp_0004` | CWE-22 | normal | `plain` | std::remove | 21-40 | class method | environment | terse | with | early | path_containment_check | Report the size of a stored file. |
| 058 | `cla_pt_cpp_0011` | CWE-22 | normal | `plain` | std::remove | 21-40 | command line tool function | command_line | terse | with | late | base_name_only | Read an email template by name. |
| 059 | `cla_cmdi_cpp_0007` | CWE-78 | hard_negative | `argument_list_with_user_data` | Boost.Process | 6-10 | helper called by another function | environment | descriptive | with | - | - | Run a spell checker on a text file. |
| 060 | `cla_pt_cpp_0025` | CWE-22 | hard_positive | `extension_check_only` | std::remove | 21-40 | web or network handler that receives a request object | network_message | descriptive | without | middle | path_containment_check | Create a thumbnail file next to the original image. |
| 061 | `cla_cmdi_cpp_0001` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | system | 11-20 | plain function | environment | descriptive | without | - | - | Extract a thumbnail frame from a video file. |
| 062 | `cla_sqli_cpp_0012` | CWE-89 | normal | `plain` | Qt QSqlQuery | 41-100 | helper called by another function | web_request | terse | with | late | query_builder_bind | Fetch an invoice by its number. |
| 063 | `cla_rnd_cpp_0015` | CWE-338 | safe | `plain` | std::default_random_engine | 21-40 | web or network handler that receives a request object | not_applicable | descriptive | with | - | - | Issue a device registration token. |
| 064 | `cla_rnd_cpp_0011` | CWE-338 | hard_positive | `weak_generator_behind_helper` | std::default_random_engine | 41-100 | class method | not_applicable | descriptive | without | middle | rejection_sampling_secure_index | Issue an email confirmation token. |
| 065 | `cla_cmdi_cpp_0013` | CWE-78 | hard_positive | `partial_shell_character_filter` | Boost.Process | 41-100 | class method | web_request | terse | without | middle | argv_no_shell | Search a log file for lines containing a term. |
| 066 | `cla_sqli_cpp_0019` | CWE-89 | no_code | `plain` | none | 1-5 | web or network handler that receives a request object | not_applicable | descriptive | without | - | - | Parse a CSV line into fields. |
| 067 | `cla_rnd_cpp_0016` | CWE-338 | no_code | `plain` | none | 1-5 | callback, lambda or asynchronous task | not_applicable | terse | without | - | - | Compute the check digit of a number. |
| 068 | `cla_sqli_cpp_0025` | CWE-89 | safe | `plain` | Qt QSqlQuery | 11-20 | web or network handler that receives a request object | web_request | descriptive | without | - | - | Fetch the configuration value for a given key and environment. |
| 069 | `cla_rnd_cpp_0001` | CWE-338 | normal | `plain` | rand | 21-40 | command line tool function | not_applicable | terse | without | early | secure_generator_api | Create a session identifier for a signed-in user. |
| 070 | `cla_pt_cpp_0012` | CWE-22 | hard_positive | `extension_check_only` | fopen | 21-40 | helper called by another function | environment | terse | without | late | base_name_only | Read a data file for a selected report. |
| 071 | `cla_rnd_cpp_0019` | CWE-338 | normal | `plain` | std::mt19937 | 1-5 | class method | not_applicable | terse | without | middle | rejection_sampling_secure_index | Generate a one-time login link token. |
| 072 | `cla_rnd_cpp_0021` | CWE-338 | hard_positive | `weak_value_hashed` | std::default_random_engine | 21-40 | plain function | not_applicable | descriptive | without | late | rejection_sampling_secure_index | Generate a one-time voucher for a refund. |
| 073 | `cla_cmdi_cpp_0011` | CWE-78 | hard_positive | `partial_shell_character_filter` | popen | 41-100 | plain function | command_line | terse | with | late | strict_validation | Print the version of a tool chosen from a list. |
| 074 | `cla_cmdi_cpp_0016` | CWE-78 | hard_negative | `constant_shell_command` | popen | 6-10 | command line tool function | command_line | terse | with | - | - | Scan an uploaded file with a command line scanner. |
| 075 | `cla_sqli_cpp_0006` | CWE-89 | safe | `plain` | mysql_query | 21-40 | command line tool function | command_line | descriptive | without | - | - | Return a page of articles sorted by a column chosen by the caller. |
| 076 | `cla_pt_cpp_0013` | CWE-22 | safe | `plain` | std::filesystem | 11-20 | plain function | environment | terse | without | - | - | Delete temporary files that match a name. |
| 077 | `cla_pt_cpp_0021` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | std::remove | 11-20 | plain function | command_line | descriptive | with | - | - | Check whether a named file exists in the storage area. |
| 078 | `cla_sqli_cpp_0009` | CWE-89 | hard_positive | `keyword_blocklist` | PQexec | 21-40 | command line tool function | command_line | terse | without | early | allow_list | Update the email address of a user profile. |
| 079 | `cla_pt_cpp_0015` | CWE-22 | no_code | `plain` | none | 1-5 | web or network handler that receives a request object | not_applicable | descriptive | with | - | - | Check that a file name uses only plain characters. |
| 080 | `cla_pt_cpp_0024` | CWE-22 | hard_negative | `id_mapped_to_known_file` | fopen | 21-40 | callback, lambda or asynchronous task | command_line | descriptive | without | - | - | Write a user's settings file. |
| 081 | `cla_cmdi_cpp_0010` | CWE-78 | normal | `plain` | system | 11-20 | callback, lambda or asynchronous task | file | terse | without | early | argv_no_shell | Query a package manager for the version of a package. |
| 082 | `cla_pt_cpp_0014` | CWE-22 | safe | `plain` | std::remove | 21-40 | plain function | command_line | terse | without | - | - | Extract the entries of an uploaded archive into a folder. |
| 083 | `cla_sqli_cpp_0010` | CWE-89 | hard_positive | `handwritten_escaping` | MySQL Connector/C++ | 6-10 | web or network handler that receives a request object | network_message | descriptive | with | early | type_conversion | List the most recent log entries of a service. |
| 084 | `cla_cmdi_cpp_0012` | CWE-78 | hard_negative | `constant_shell_command` | system | 21-40 | class method | function_argument | descriptive | with | - | - | Check whether a host answers a network ping. |
| 085 | `cla_pt_cpp_0020` | CWE-22 | hard_positive | `check_before_normalising` | std::filesystem | 11-20 | helper called by another function | environment | terse | with | late | base_name_only | Count the lines of a stored text file. |
| 086 | `cla_rnd_cpp_0025` | CWE-338 | normal | `plain` | std::default_random_engine | 11-20 | command line tool function | not_applicable | terse | with | late | secure_generator_api | Issue a short-lived upload key. |
| 087 | `cla_rnd_cpp_0022` | CWE-338 | hard_negative | `ordinary_random_shuffling` | std::mt19937 | 6-10 | plain function | not_applicable | terse | with | - | - | Deal a shuffled deck of cards to four players. |
| 088 | `cla_sqli_cpp_0008` | CWE-89 | safe | `plain` | mysql_query | 41-100 | plain function | command_line | descriptive | without | - | - | Search support tickets by keyword and priority. |
| 089 | `cla_pt_cpp_0018` | CWE-22 | normal | `plain` | ifstream or ofstream | 1-5 | command line tool function | command_line | descriptive | with | late | path_containment_check | Copy a template file into a user's workspace. |
| 090 | `cla_sqli_cpp_0011` | CWE-89 | normal | `plain` | sqlite3 C API | 11-20 | class method | network_message | descriptive | without | late | query_builder_bind | Transfer a balance between two accounts inside a transaction. |
| 091 | `cla_pt_cpp_0003` | CWE-22 | safe | `plain` | std::remove | 6-10 | class method | environment | descriptive | with | - | - | Delete a user's attachment. |
| 092 | `cla_cmdi_cpp_0024` | CWE-78 | normal | `plain` | popen | 11-20 | class method | function_argument | terse | with | late | allow_list | Compute the checksum of a file. |
| 093 | `cla_rnd_cpp_0013` | CWE-338 | safe | `plain` | std::mt19937 | 11-20 | callback, lambda or asynchronous task | not_applicable | descriptive | without | - | - | Generate a CSRF token for a form. |
| 094 | `cla_pt_cpp_0007` | CWE-22 | hard_negative | `library_confined_access` | std::filesystem | 11-20 | class method | database_value | terse | without | - | - | List the files in a sub folder of the storage area. |
| 095 | `cla_pt_cpp_0006` | CWE-22 | no_code | `plain` | none | 11-20 | class method | not_applicable | descriptive | without | - | - | Compare two version strings. |
| 096 | `cla_rnd_cpp_0009` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | std::mt19937 | 41-100 | command line tool function | not_applicable | terse | with | early | rejection_sampling_secure_index | Issue a ticket secret for a QR code. |
| 097 | `cla_pt_cpp_0023` | CWE-22 | hard_negative | `library_confined_access` | ifstream or ofstream | 21-40 | plain function | file | descriptive | without | - | - | Fetch a user's uploaded resume. |
| 098 | `cla_rnd_cpp_0006` | CWE-338 | normal | `plain` | rand | 1-5 | class method | not_applicable | terse | without | early | rejection_sampling_secure_index | Issue an API key for a new client. |
| 099 | `cla_cmdi_cpp_0019` | CWE-78 | normal | `plain` | QProcess | 21-40 | helper called by another function | web_request | descriptive | without | middle | strict_validation | Print the version of a tool chosen from a list. |
| 100 | `cla_sqli_cpp_0001` | CWE-89 | hard_negative | `identifier_allowlist` | sqlite3 C API | 21-40 | callback, lambda or asynchronous task | file | descriptive | without | - | - | Count the unread messages of a user. |

</details>
