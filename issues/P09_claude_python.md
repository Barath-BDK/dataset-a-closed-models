## 🟦 STEP 2 of 3

**Assigned to: kanishkagopiramanan-ai.** Do this **after** the warm-up (issue #24) is approved. Rows **006 to 100** (Claude × Python).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P09_claude_python.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P09_claude_python.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P09_claude_python.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P09_claude_python.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P09_claude_python` made from your personal branch `dev/kanishkagopiramanan-ai` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into Claude (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P09_claude_python.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/kanishkagopiramanan-ai` with **only** `submissions/P09_claude_python.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/kanishkagopiramanan-ai`; when all your steps are merged, one last pull request `dev/kanishkagopiramanan-ai` into `main`

Mix of rows: hard_positive 16, hard_negative 26, normal 31, no_code 8, safe 14.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `cla_pt_py_0006` | CWE-22 | hard_positive | `relative_check_misses_absolute` | open | 11-20 | web request handler | web_request | descriptive | with | late | base_name_only | Return the contents of a help page file. |
| 007 | `cla_pt_py_0024` | CWE-22 | hard_positive | `extension_check_only` | open | 21-40 | async function or callback | web_request | descriptive | with | middle | base_name_only | Store a user's avatar image. |
| 008 | `cla_cmdi_py_0009` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | os.popen | 6-10 | helper called by another function | command_line | descriptive | with | - | - | Run a spell checker on a text file. |
| 009 | `cla_rnd_py_0008` | CWE-338 | normal | `plain` | random.choices | 6-10 | plain function | not_applicable | terse | without | late | secure_bytes_encoded | Create a deletion confirmation token. |
| 010 | `cla_pt_py_0005` | CWE-22 | no_code | `plain` | none | 1-5 | class method | not_applicable | descriptive | without | - | - | Count the segments of a path string. |
| 011 | `cla_rnd_py_0019` | CWE-338 | normal | `plain` | random.randint | 11-20 | command line tool function | not_applicable | terse | without | late | secure_generator_api | Create a password for a guest Wi-Fi voucher. |
| 012 | `cla_cmdi_py_0004` | CWE-78 | safe | `plain` | os.popen | 41-100 | helper called by another function | function_argument | descriptive | without | - | - | Extract a thumbnail frame from a video file. |
| 013 | `cla_sqli_py_0011` | CWE-89 | hard_positive | `keyword_blocklist` | psycopg2 | 6-10 | class method | database_value | terse | without | late | allow_list | Count the unread messages of a user. |
| 014 | `cla_cmdi_py_0006` | CWE-78 | normal | `plain` | subprocess.check_output | 1-5 | command line tool function | command_line | descriptive | without | early | allow_list | Run a database backup tool for one schema. |
| 015 | `cla_cmdi_py_0008` | CWE-78 | hard_positive | `dash_argument_injection` | subprocess.check_output | 11-20 | command line tool function | command_line | descriptive | with | late | argv_no_shell | Back up a directory to another location with a sync tool. |
| 016 | `cla_cmdi_py_0019` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | subprocess.run with shell=True | 11-20 | async function or callback | command_line | terse | without | - | - | Read the last lines of a log file. |
| 017 | `cla_cmdi_py_0024` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | subprocess.check_output | 21-40 | web request handler | web_request | terse | with | - | - | Run a unit conversion script on a value. |
| 018 | `cla_pt_py_0018` | CWE-22 | normal | `plain` | open | 6-10 | helper called by another function | web_request | terse | without | middle | base_name_only | Read the first line of a stored file. |
| 019 | `cla_cmdi_py_0020` | CWE-78 | no_code | `plain` | none | 1-5 | web request handler | not_applicable | descriptive | without | - | - | Check that a port number is in range. |
| 020 | `cla_sqli_py_0006` | CWE-89 | hard_negative | `identifier_allowlist` | MySQL driver (PyMySQL or mysql-connector) | 21-40 | web request handler | web_request | terse | with | - | - | Find a customer record by email address. |
| 021 | `cla_rnd_py_0017` | CWE-338 | hard_positive | `weak_generator_behind_helper` | random.randint | 41-100 | plain function | not_applicable | descriptive | without | early | secure_generator_api | Generate a CSRF token for a form. |
| 022 | `cla_sqli_py_0023` | CWE-89 | safe | `plain` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | async function or callback | file | terse | without | - | - | Find books by author name. |
| 023 | `cla_rnd_py_0006` | CWE-338 | safe | `plain` | random.randint | 21-40 | command line tool function | not_applicable | descriptive | with | - | - | Create an encryption key for a local vault. |
| 024 | `cla_sqli_py_0021` | CWE-89 | hard_negative | `bound_via_builder` | MySQL driver (PyMySQL or mysql-connector) | 21-40 | class method | environment | terse | without | - | - | Record an audit entry for an administrator action. |
| 025 | `cla_rnd_py_0004` | CWE-338 | hard_positive | `weak_generator_behind_helper` | random.choice | 21-40 | plain function | not_applicable | descriptive | without | early | rejection_sampling_secure_index | Generate a pairing code for a device. |
| 026 | `cla_pt_py_0017` | CWE-22 | hard_negative | `base_name_only` | archive extraction (zipfile or tarfile) | 21-40 | command line tool function | command_line | descriptive | with | - | - | Read a plugin manifest from a plugin folder. |
| 027 | `cla_cmdi_py_0025` | CWE-78 | hard_negative | `argument_list_with_user_data` | subprocess.Popen with shell=True | 6-10 | class method | function_argument | terse | without | - | - | Run a linter on a submitted file and return its report. |
| 028 | `cla_pt_py_0003` | CWE-22 | normal | `plain` | pathlib | 41-100 | helper called by another function | network_message | descriptive | without | early | allow_list_mapping | Return the contents of a shared snippet file. |
| 029 | `cla_pt_py_0012` | CWE-22 | normal | `plain` | open | 6-10 | command line tool function | command_line | terse | without | middle | path_containment_check | Truncate a log file chosen by name. |
| 030 | `cla_sqli_py_0003` | CWE-89 | hard_positive | `one_branch_bound` | Django raw() | 6-10 | async function or callback | environment | terse | with | middle | orm_query_builder | Insert a new product review. |
| 031 | `cla_cmdi_py_0022` | CWE-78 | normal | `plain` | subprocess.Popen with shell=True | 11-20 | command line tool function | command_line | terse | without | early | allow_list | Stop a process by name. |
| 032 | `cla_sqli_py_0009` | CWE-89 | hard_negative | `placeholder_list_for_in` | psycopg2 | 21-40 | class method | network_message | terse | with | - | - | Find articles that carry a given tag. |
| 033 | `cla_sqli_py_0017` | CWE-89 | safe | `plain` | sqlite3 | 11-20 | web request handler | web_request | descriptive | with | - | - | Find events happening in a given city. |
| 034 | `cla_sqli_py_0022` | CWE-89 | no_code | `plain` | none | 6-10 | plain function | not_applicable | descriptive | without | - | - | Convert a status code into a label. |
| 035 | `cla_rnd_py_0007` | CWE-338 | safe | `plain` | random.choices | 11-20 | helper called by another function | not_applicable | descriptive | without | - | - | Create a private link token for a quiz. |
| 036 | `cla_sqli_py_0015` | CWE-89 | normal | `plain` | sqlite3 | 21-40 | helper called by another function | command_line | terse | with | late | allow_list | Return the stock quantity for a product code. |
| 037 | `cla_sqli_py_0010` | CWE-89 | hard_negative | `integer_forced` | sqlite3 | 11-20 | command line tool function | command_line | terse | without | - | - | Fetch the configuration value for a given key and environment. |
| 038 | `cla_sqli_py_0005` | CWE-89 | no_code | `plain` | none | 11-20 | async function or callback | not_applicable | terse | without | - | - | Group a list of records by a key. |
| 039 | `cla_rnd_py_0001` | CWE-338 | hard_negative | `ordinary_random_games` | random.choices | 11-20 | async function or callback | not_applicable | descriptive | with | - | - | Roll dice for a board game. |
| 040 | `cla_pt_py_0022` | CWE-22 | normal | `plain` | os.remove | 6-10 | class method | web_request | descriptive | without | late | base_name_only | Rename a document inside the storage folder. |
| 041 | `cla_pt_py_0007` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | archive extraction (zipfile or tarfile) | 21-40 | helper called by another function | command_line | descriptive | without | - | - | Read the first line of a stored file. |
| 042 | `cla_rnd_py_0003` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | random.choice | 21-40 | command line tool function | not_applicable | terse | with | - | - | Choose a polling interval spread between workers. |
| 043 | `cla_cmdi_py_0017` | CWE-78 | safe | `plain` | subprocess.run with shell=True | 6-10 | command line tool function | command_line | terse | with | - | - | Mount a network share with given options. |
| 044 | `cla_cmdi_py_0023` | CWE-78 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | descriptive | without | - | - | Convert Celsius to Fahrenheit. |
| 045 | `cla_rnd_py_0009` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random.choices | 21-40 | helper called by another function | not_applicable | descriptive | without | middle | secure_generator_api | Generate an unlock code for a smart lock. |
| 046 | `cla_sqli_py_0016` | CWE-89 | normal | `plain` | Django raw() | 1-5 | command line tool function | command_line | descriptive | with | middle | allow_list | Find a customer record by email address. |
| 047 | `cla_rnd_py_0025` | CWE-338 | no_code | `plain` | none | 11-20 | class method | not_applicable | descriptive | without | - | - | Convert a token to uppercase for display. |
| 048 | `cla_pt_py_0015` | CWE-22 | normal | `plain` | shutil.copy | 41-100 | async function or callback | database_value | descriptive | without | late | path_containment_check | Fetch a user's uploaded resume. |
| 049 | `cla_pt_py_0011` | CWE-22 | hard_positive | `prefix_test_without_separator` | send_file | 11-20 | web request handler | web_request | terse | with | middle | allow_list_mapping | Open a video file for streaming. |
| 050 | `cla_sqli_py_0014` | CWE-89 | normal | `plain` | psycopg2 | 11-20 | plain function | command_line | descriptive | with | middle | orm_query_builder | Search products whose name contains a keyword. |
| 051 | `cla_pt_py_0020` | CWE-22 | hard_negative | `id_mapped_to_known_file` | open | 6-10 | plain function | web_request | terse | with | - | - | Unzip a theme package into the themes folder. |
| 052 | `cla_cmdi_py_0010` | CWE-78 | normal | `plain` | os.system | 1-5 | class method | network_message | descriptive | without | early | quoting | Run a database backup tool for one schema. |
| 053 | `cla_rnd_py_0014` | CWE-338 | no_code | `plain` | none | 6-10 | web request handler | not_applicable | terse | with | - | - | Format a recovery code list for printing. |
| 054 | `cla_rnd_py_0013` | CWE-338 | safe | `plain` | random.randint | 41-100 | web request handler | not_applicable | descriptive | without | - | - | Generate a one-time login link token. |
| 055 | `cla_cmdi_py_0011` | CWE-78 | safe | `plain` | os.popen | 11-20 | async function or callback | network_message | terse | without | - | - | Unpack an uploaded archive into a working folder. |
| 056 | `cla_pt_py_0009` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | open | 21-40 | helper called by another function | function_argument | descriptive | with | - | - | Save a note under a given name. |
| 057 | `cla_sqli_py_0007` | CWE-89 | hard_positive | `handwritten_escaping` | sqlite3 | 21-40 | web request handler | network_message | terse | without | middle | bound_parameters | Fetch an invoice by its number. |
| 058 | `cla_rnd_py_0015` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random.randint | 21-40 | helper called by another function | not_applicable | terse | with | early | rejection_sampling_secure_index | Pick the words of a recovery phrase for a wallet. |
| 059 | `cla_cmdi_py_0016` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | os.system | 11-20 | web request handler | web_request | terse | without | - | - | Start a background job from a script name. |
| 060 | `cla_sqli_py_0001` | CWE-89 | normal | `plain` | SQLAlchemy text() | 11-20 | async function or callback | environment | descriptive | without | middle | allow_list | Remove a product from a wishlist. |
| 061 | `cla_rnd_py_0018` | CWE-338 | hard_negative | `ordinary_random_sampling` | random.choices | 21-40 | web request handler | not_applicable | descriptive | without | - | - | Pick a random sample of users for a satisfaction survey. |
| 062 | `cla_cmdi_py_0013` | CWE-78 | safe | `plain` | subprocess.run with shell=True | 6-10 | plain function | file | terse | with | - | - | Send a document to a named printer. |
| 063 | `cla_pt_py_0013` | CWE-22 | normal | `plain` | shutil.copy | 1-5 | class method | network_message | terse | with | early | path_containment_check | Unzip a theme package into the themes folder. |
| 064 | `cla_rnd_py_0010` | CWE-338 | normal | `plain` | random.getrandbits | 1-5 | async function or callback | not_applicable | terse | without | late | secure_generator_api | Create a list of recovery codes for an account. |
| 065 | `cla_rnd_py_0024` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | random.getrandbits | 11-20 | web request handler | not_applicable | descriptive | with | - | - | Create an OAuth state value for a login redirect. |
| 066 | `cla_rnd_py_0002` | CWE-338 | normal | `plain` | random.choice | 41-100 | async function or callback | not_applicable | descriptive | without | middle | secure_generator_api | Issue a ticket secret for a QR code. |
| 067 | `cla_sqli_py_0013` | CWE-89 | normal | `plain` | Django raw() | 6-10 | command line tool function | command_line | terse | with | late | bound_parameters | Report order totals grouped by a chosen category. |
| 068 | `cla_rnd_py_0011` | CWE-338 | hard_negative | `ordinary_random_shuffling` | random.choices | 21-40 | async function or callback | not_applicable | terse | with | - | - | Shuffle a playlist before playing it. |
| 069 | `cla_cmdi_py_0007` | CWE-78 | normal | `plain` | subprocess.check_output | 6-10 | class method | web_request | descriptive | without | late | argv_no_shell | Search a log file for lines containing a term. |
| 070 | `cla_rnd_py_0020` | CWE-338 | normal | `plain` | random.getrandbits | 21-40 | async function or callback | not_applicable | descriptive | without | middle | secure_bytes_encoded | Issue a device registration token. |
| 071 | `cla_pt_py_0002` | CWE-22 | safe | `plain` | shutil.copy | 11-20 | helper called by another function | function_argument | terse | without | - | - | Return a preview of a stored image. |
| 072 | `cla_pt_py_0004` | CWE-22 | normal | `plain` | pathlib | 11-20 | class method | file | terse | with | late | library_confinement | Return the text of an uploaded file. |
| 073 | `cla_pt_py_0014` | CWE-22 | normal | `plain` | shutil.copy | 41-100 | async function or callback | network_message | descriptive | without | middle | base_name_only | Count the lines of a stored text file. |
| 074 | `cla_pt_py_0023` | CWE-22 | no_code | `plain` | none | 1-5 | class method | not_applicable | terse | with | - | - | Shorten a long name with an ellipsis. |
| 075 | `cla_cmdi_py_0002` | CWE-78 | normal | `plain` | os.system | 41-100 | plain function | database_value | terse | with | middle | quoting | Print the version of a tool chosen from a list. |
| 076 | `cla_rnd_py_0005` | CWE-338 | safe | `plain` | random.getrandbits | 11-20 | plain function | not_applicable | terse | without | - | - | Create a share link secret for a document. |
| 077 | `cla_sqli_py_0008` | CWE-89 | safe | `plain` | Django raw() | 11-20 | plain function | database_value | descriptive | with | - | - | Find the members of a team by role. |
| 078 | `cla_cmdi_py_0014` | CWE-78 | hard_positive | `validation_of_other_variable` | os.system | 21-40 | class method | command_line | descriptive | with | late | quoting | Query the status of a container by name. |
| 079 | `cla_rnd_py_0021` | CWE-338 | normal | `plain` | random.getrandbits | 11-20 | command line tool function | not_applicable | descriptive | without | early | rejection_sampling_secure_index | Create a webhook signing secret. |
| 080 | `cla_pt_py_0008` | CWE-22 | hard_negative | `library_confined_access` | shutil.copy | 21-40 | async function or callback | network_message | terse | without | - | - | Return the modification time of a stored file. |
| 081 | `cla_sqli_py_0019` | CWE-89 | hard_negative | `placeholder_list_for_in` | SQLAlchemy text() | 21-40 | helper called by another function | web_request | descriptive | with | - | - | Return the latest comments on a post. |
| 082 | `cla_cmdi_py_0001` | CWE-78 | hard_positive | `quoting_in_wrong_context` | os.system | 11-20 | web request handler | web_request | terse | without | middle | quoting | Execute a report generator with a chosen template. |
| 083 | `cla_sqli_py_0004` | CWE-89 | safe | `plain` | psycopg2 | 11-20 | helper called by another function | environment | descriptive | without | - | - | Transfer a balance between two accounts inside a transaction. |
| 084 | `cla_sqli_py_0020` | CWE-89 | hard_positive | `bound_but_input_identifier` | MySQL driver (PyMySQL or mysql-connector) | 6-10 | class method | network_message | descriptive | with | early | type_conversion | List a user's orders with a given status. |
| 085 | `cla_cmdi_py_0015` | CWE-78 | normal | `plain` | os.system | 21-40 | class method | function_argument | terse | without | late | quoting | Create a snapshot of a virtual machine by name. |
| 086 | `cla_cmdi_py_0018` | CWE-78 | hard_positive | `validation_of_other_variable` | os.popen | 41-100 | async function or callback | web_request | terse | with | middle | allow_list | Send a document to a named printer. |
| 087 | `cla_rnd_py_0022` | CWE-338 | normal | `plain` | random.randint | 6-10 | class method | not_applicable | terse | with | late | rejection_sampling_secure_index | Create an invite code for a team. |
| 088 | `cla_pt_py_0016` | CWE-22 | normal | `plain` | send_file | 1-5 | plain function | command_line | descriptive | with | late | library_confinement | Serve a PDF from the document library. |
| 089 | `cla_pt_py_0001` | CWE-22 | hard_negative | `base_name_only` | shutil.copy | 41-100 | command line tool function | command_line | descriptive | with | - | - | Load a configuration file for a named profile. |
| 090 | `cla_sqli_py_0012` | CWE-89 | normal | `plain` | psycopg2 | 6-10 | async function or callback | database_value | descriptive | without | late | bound_parameters | Check a username and password hash for a login. |
| 091 | `cla_cmdi_py_0003` | CWE-78 | normal | `plain` | subprocess.check_output | 11-20 | web request handler | web_request | descriptive | without | middle | argv_no_shell | Mount a network share with given options. |
| 092 | `cla_rnd_py_0012` | CWE-338 | hard_negative | `fixed_seed_reproducible` | random.getrandbits | 21-40 | plain function | not_applicable | descriptive | with | - | - | Draw the same sample every run for a reproducible experiment. |
| 093 | `cla_sqli_py_0024` | CWE-89 | normal | `plain` | psycopg2 | 1-5 | async function or callback | network_message | terse | with | late | bound_parameters | Update the status of a support ticket. |
| 094 | `cla_sqli_py_0018` | CWE-89 | hard_negative | `placeholders_only_format` | sqlite3 | 6-10 | web request handler | database_value | terse | without | - | - | Find patients by surname. |
| 095 | `cla_sqli_py_0025` | CWE-89 | hard_negative | `placeholder_list_for_in` | SQLAlchemy text() | 6-10 | command line tool function | command_line | terse | without | - | - | Find patients by surname. |
| 096 | `cla_sqli_py_0002` | CWE-89 | normal | `plain` | psycopg2 | 41-100 | command line tool function | command_line | terse | with | late | orm_query_builder | List reservations for a room between two dates. |
| 097 | `cla_rnd_py_0016` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | random.getrandbits | 6-10 | command line tool function | not_applicable | descriptive | with | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 098 | `cla_pt_py_0021` | CWE-22 | safe | `plain` | archive extraction (zipfile or tarfile) | 21-40 | async function or callback | web_request | terse | without | - | - | Read a language pack for a game. |
| 099 | `cla_pt_py_0010` | CWE-22 | hard_positive | `relative_check_misses_absolute` | shutil.copy | 41-100 | command line tool function | command_line | terse | without | early | allow_list_mapping | Append a line to a user's activity log. |
| 100 | `cla_cmdi_py_0005` | CWE-78 | hard_negative | `constant_shell_command` | subprocess.Popen with shell=True | 11-20 | class method | function_argument | descriptive | without | - | - | Zip the contents of a folder into a named archive. |

</details>
