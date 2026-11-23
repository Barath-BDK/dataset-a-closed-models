## 🟦 STEP 2 of 3

**Assigned to: vinoth96-hub.** Do this **after** the warm-up (issue #16) is approved. Rows **006 to 100** (ChatGPT × Python).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P01_chatgpt_python.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P01_chatgpt_python.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P01_chatgpt_python.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P01_chatgpt_python.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P01_chatgpt_python` made from your personal branch `dev/vinoth96-hub` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into ChatGPT (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P01_chatgpt_python.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/vinoth96-hub` with **only** `submissions/P01_chatgpt_python.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/vinoth96-hub`; when all your steps are merged, one last pull request `dev/vinoth96-hub` into `main`

Mix of rows: hard_negative 25, normal 32, safe 14, hard_positive 16, no_code 8.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `gpt_pt_py_0006` | CWE-22 | hard_negative | `id_mapped_to_known_file` | os.remove | 11-20 | class method | database_value | terse | with | - | - | Delete a user's attachment. |
| 007 | `gpt_rnd_py_0004` | CWE-338 | normal | `plain` | random.randint | 6-10 | class method | not_applicable | terse | with | early | secure_bytes_encoded | Generate a session key for an encrypted chat. |
| 008 | `gpt_rnd_py_0015` | CWE-338 | normal | `plain` | random.choices | 41-100 | class method | not_applicable | terse | with | middle | secure_bytes_encoded | Generate a temporary password for a new account. |
| 009 | `gpt_pt_py_0004` | CWE-22 | normal | `plain` | open | 21-40 | class method | environment | terse | with | middle | allow_list_mapping | Load a configuration file for a named profile. |
| 010 | `gpt_sqli_py_0023` | CWE-89 | normal | `plain` | psycopg2 | 6-10 | command line tool function | command_line | descriptive | without | late | type_conversion | Look up a city by postal code. |
| 011 | `gpt_sqli_py_0007` | CWE-89 | normal | `plain` | psycopg2 | 21-40 | web request handler | database_value | descriptive | with | early | type_conversion | Look up a coupon by its code. |
| 012 | `gpt_pt_py_0009` | CWE-22 | safe | `plain` | pathlib | 21-40 | plain function | file | terse | with | - | - | Read an email template by name. |
| 013 | `gpt_pt_py_0010` | CWE-22 | normal | `plain` | os.remove | 21-40 | plain function | command_line | descriptive | with | early | path_containment_check | Serve a PDF from the document library. |
| 014 | `gpt_cmdi_py_0006` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | subprocess.check_output | 21-40 | web request handler | web_request | descriptive | without | - | - | Convert a document to another format with a converter. |
| 015 | `gpt_sqli_py_0010` | CWE-89 | hard_positive | `keyword_blocklist` | Django raw() | 21-40 | class method | file | terse | without | middle | allow_list | Mark a notification as read for a user. |
| 016 | `gpt_pt_py_0005` | CWE-22 | safe | `plain` | open | 41-100 | plain function | database_value | descriptive | without | - | - | Remove an old export file. |
| 017 | `gpt_cmdi_py_0021` | CWE-78 | hard_negative | `user_data_after_end_of_options` | subprocess.check_output | 6-10 | web request handler | database_value | descriptive | with | - | - | Read the last lines of a log file. |
| 018 | `gpt_sqli_py_0009` | CWE-89 | normal | `plain` | psycopg2 | 6-10 | helper called by another function | environment | terse | with | middle | orm_query_builder | Look up the shipping address of an order. |
| 019 | `gpt_rnd_py_0020` | CWE-338 | safe | `plain` | random.choices | 11-20 | helper called by another function | not_applicable | descriptive | without | - | - | Generate a nonce for a signed request. |
| 020 | `gpt_cmdi_py_0008` | CWE-78 | safe | `plain` | subprocess.check_output | 21-40 | web request handler | database_value | terse | without | - | - | Execute a report generator with a chosen template. |
| 021 | `gpt_cmdi_py_0023` | CWE-78 | normal | `plain` | subprocess.check_output | 6-10 | helper called by another function | environment | descriptive | with | early | argv_no_shell | Trace the network route to a host. |
| 022 | `gpt_cmdi_py_0010` | CWE-78 | normal | `plain` | subprocess.Popen with shell=True | 41-100 | web request handler | web_request | descriptive | without | middle | strict_validation | Show the commit history of a repository for one author. |
| 023 | `gpt_cmdi_py_0014` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | os.system | 41-100 | async function or callback | database_value | descriptive | with | - | - | Look up the DNS records of a host name. |
| 024 | `gpt_pt_py_0019` | CWE-22 | normal | `plain` | open | 6-10 | plain function | network_message | terse | without | late | allow_list_mapping | Restore a document from a version folder. |
| 025 | `gpt_pt_py_0001` | CWE-22 | hard_negative | `id_mapped_to_known_file` | archive extraction (zipfile or tarfile) | 21-40 | web request handler | web_request | terse | without | - | - | Create a thumbnail file next to the original image. |
| 026 | `gpt_cmdi_py_0013` | CWE-78 | safe | `plain` | subprocess.run with shell=True | 41-100 | async function or callback | function_argument | terse | with | - | - | Run a code formatter on a source file. |
| 027 | `gpt_cmdi_py_0024` | CWE-78 | normal | `plain` | subprocess.Popen with shell=True | 6-10 | command line tool function | command_line | terse | without | middle | quoting | Compare two files and show the differences. |
| 028 | `gpt_pt_py_0002` | CWE-22 | hard_positive | `relative_check_misses_absolute` | archive extraction (zipfile or tarfile) | 6-10 | async function or callback | web_request | descriptive | with | late | library_confinement | Serve a static asset such as an image or stylesheet. |
| 029 | `gpt_rnd_py_0022` | CWE-338 | normal | `plain` | random.randint | 1-5 | plain function | not_applicable | terse | with | middle | rejection_sampling_secure_index | Generate an access token for a mobile app. |
| 030 | `gpt_sqli_py_0024` | CWE-89 | no_code | `plain` | none | 6-10 | plain function | not_applicable | descriptive | with | - | - | Parse a CSV line into fields. |
| 031 | `gpt_cmdi_py_0009` | CWE-78 | normal | `plain` | os.system | 6-10 | async function or callback | database_value | terse | without | early | allow_list | Sync a folder to a remote host over ssh. |
| 032 | `gpt_rnd_py_0010` | CWE-338 | normal | `plain` | random.getrandbits | 11-20 | async function or callback | not_applicable | terse | with | early | secure_bytes_encoded | Generate a license key for a software installation. |
| 033 | `gpt_sqli_py_0002` | CWE-89 | hard_negative | `placeholder_list_for_in` | SQLAlchemy text() | 6-10 | async function or callback | command_line | descriptive | without | - | - | Find a vehicle by its registration number. |
| 034 | `gpt_pt_py_0024` | CWE-22 | normal | `plain` | shutil.copy | 21-40 | class method | file | terse | without | early | path_containment_check | Read a log file of a named service. |
| 035 | `gpt_rnd_py_0025` | CWE-338 | hard_negative | `ordinary_random_sampling` | random.choices | 21-40 | web request handler | not_applicable | terse | without | - | - | Choose which products to feature on the home page. |
| 036 | `gpt_sqli_py_0003` | CWE-89 | hard_negative | `placeholders_only_format` | Django raw() | 6-10 | web request handler | web_request | descriptive | with | - | - | Delete a user's saved bookmarks that match a title. |
| 037 | `gpt_cmdi_py_0005` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | os.system | 21-40 | class method | file | descriptive | with | - | - | Check whether a host answers a network ping. |
| 038 | `gpt_rnd_py_0023` | CWE-338 | normal | `plain` | random.choices | 11-20 | plain function | not_applicable | descriptive | with | early | secure_generator_api | Generate an initialization vector for encrypting a file. |
| 039 | `gpt_cmdi_py_0020` | CWE-78 | no_code | `plain` | none | 6-10 | helper called by another function | not_applicable | terse | without | - | - | Compute a percentage of a total. |
| 040 | `gpt_sqli_py_0013` | CWE-89 | hard_negative | `placeholders_only_format` | sqlite3 | 41-100 | helper called by another function | file | descriptive | without | - | - | Count the unread messages of a user. |
| 041 | `gpt_sqli_py_0006` | CWE-89 | hard_positive | `handwritten_escaping` | MySQL driver (PyMySQL or mysql-connector) | 21-40 | web request handler | network_message | terse | without | late | bound_parameters | Look up the shipping address of an order. |
| 042 | `gpt_sqli_py_0017` | CWE-89 | hard_negative | `integer_forced` | Django raw() | 41-100 | class method | function_argument | descriptive | with | - | - | Return the top sellers for a given region. |
| 043 | `gpt_sqli_py_0004` | CWE-89 | hard_negative | `integer_forced` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | plain function | web_request | terse | with | - | - | Update the status of a support ticket. |
| 044 | `gpt_sqli_py_0001` | CWE-89 | hard_positive | `one_branch_bound` | SQLAlchemy text() | 6-10 | web request handler | web_request | descriptive | without | early | orm_query_builder | Return the top sellers for a given region. |
| 045 | `gpt_rnd_py_0017` | CWE-338 | hard_positive | `weak_value_hashed` | random.getrandbits | 11-20 | web request handler | not_applicable | terse | with | early | secure_generator_api | Issue an email confirmation token. |
| 046 | `gpt_sqli_py_0014` | CWE-89 | safe | `plain` | SQLAlchemy text() | 11-20 | web request handler | web_request | terse | with | - | - | List the files shared with a user. |
| 047 | `gpt_rnd_py_0013` | CWE-338 | normal | `plain` | random.randint | 21-40 | command line tool function | not_applicable | terse | with | middle | secure_bytes_encoded | Create a challenge string for a login handshake. |
| 048 | `gpt_pt_py_0007` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | pathlib | 41-100 | plain function | database_value | terse | with | - | - | Extract the entries of an uploaded archive into a folder. |
| 049 | `gpt_sqli_py_0019` | CWE-89 | normal | `plain` | sqlite3 | 21-40 | class method | function_argument | descriptive | without | early | bound_parameters | Find the members of a team by role. |
| 050 | `gpt_cmdi_py_0012` | CWE-78 | hard_negative | `constant_shell_command` | subprocess.run with shell=True | 21-40 | plain function | command_line | terse | without | - | - | Look up the registration data of a domain. |
| 051 | `gpt_sqli_py_0025` | CWE-89 | no_code | `plain` | none | 1-5 | class method | not_applicable | descriptive | without | - | - | Merge two lists without duplicates. |
| 052 | `gpt_pt_py_0023` | CWE-22 | hard_positive | `prefix_test_without_separator` | pathlib | 6-10 | plain function | network_message | descriptive | with | middle | path_containment_check | Delete a user's attachment. |
| 053 | `gpt_sqli_py_0022` | CWE-89 | normal | `plain` | SQLAlchemy text() | 1-5 | command line tool function | command_line | terse | with | late | allow_list | Search products whose name contains a keyword. |
| 054 | `gpt_sqli_py_0020` | CWE-89 | safe | `plain` | sqlite3 | 21-40 | command line tool function | command_line | terse | without | - | - | List the files shared with a user. |
| 055 | `gpt_rnd_py_0012` | CWE-338 | safe | `plain` | random.getrandbits | 41-100 | class method | not_applicable | terse | without | - | - | Create a token for confirming a newsletter subscription. |
| 056 | `gpt_pt_py_0012` | CWE-22 | hard_negative | `base_name_only` | send_file | 11-20 | helper called by another function | function_argument | descriptive | with | - | - | Read the lines of a CSV import file. |
| 057 | `gpt_sqli_py_0012` | CWE-89 | normal | `plain` | SQLAlchemy text() | 41-100 | async function or callback | file | descriptive | without | early | orm_query_builder | List recent transactions for an account sorted by amount or date. |
| 058 | `gpt_rnd_py_0019` | CWE-338 | normal | `plain` | random.randint | 21-40 | plain function | not_applicable | terse | with | late | secure_generator_api | Generate a bearer token for a service account. |
| 059 | `gpt_cmdi_py_0004` | CWE-78 | no_code | `plain` | none | 11-20 | plain function | not_applicable | descriptive | with | - | - | Join a list of words into a title. |
| 060 | `gpt_cmdi_py_0011` | CWE-78 | normal | `plain` | subprocess.run with shell=True | 21-40 | async function or callback | file | terse | without | middle | strict_validation | Sync a folder to a remote host over ssh. |
| 061 | `gpt_cmdi_py_0022` | CWE-78 | hard_positive | `dash_argument_injection` | subprocess.run with shell=True | 21-40 | command line tool function | command_line | terse | with | late | quoting | Count the lines of a file with a standard tool. |
| 062 | `gpt_cmdi_py_0019` | CWE-78 | safe | `plain` | subprocess.Popen with shell=True | 11-20 | async function or callback | file | terse | with | - | - | Pack an installer from a folder with a packaging tool. |
| 063 | `gpt_pt_py_0008` | CWE-22 | hard_positive | `extension_check_only` | open | 11-20 | plain function | function_argument | descriptive | with | early | path_containment_check | Count the lines of a stored text file. |
| 064 | `gpt_pt_py_0020` | CWE-22 | normal | `plain` | pathlib | 21-40 | command line tool function | command_line | descriptive | without | early | path_containment_check | Serve a static asset such as an image or stylesheet. |
| 065 | `gpt_pt_py_0015` | CWE-22 | no_code | `plain` | none | 11-20 | web request handler | not_applicable | descriptive | without | - | - | Compare two version strings. |
| 066 | `gpt_cmdi_py_0003` | CWE-78 | safe | `plain` | subprocess.run with shell=True | 11-20 | helper called by another function | network_message | terse | with | - | - | Run a linter on a submitted file and return its report. |
| 067 | `gpt_sqli_py_0011` | CWE-89 | hard_negative | `identifier_allowlist` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | class method | function_argument | terse | without | - | - | Look up a city by postal code. |
| 068 | `gpt_pt_py_0021` | CWE-22 | hard_negative | `base_name_only` | send_file | 11-20 | command line tool function | command_line | descriptive | with | - | - | Restore a document from a version folder. |
| 069 | `gpt_rnd_py_0009` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | random.choices | 11-20 | class method | not_applicable | terse | without | - | - | Create a list of recovery codes for an account. |
| 070 | `gpt_cmdi_py_0017` | CWE-78 | normal | `plain` | os.system | 6-10 | helper called by another function | web_request | descriptive | with | middle | allow_list | Report the disk usage of a folder. |
| 071 | `gpt_cmdi_py_0018` | CWE-78 | hard_positive | `partial_shell_character_filter` | subprocess.Popen with shell=True | 11-20 | plain function | file | descriptive | with | late | allow_list | Add a user to a group with the system tool. |
| 072 | `gpt_rnd_py_0014` | CWE-338 | no_code | `plain` | none | 6-10 | class method | not_applicable | terse | with | - | - | Compare the lengths of two tokens. |
| 073 | `gpt_rnd_py_0002` | CWE-338 | safe | `plain` | random.randint | 6-10 | helper called by another function | not_applicable | descriptive | with | - | - | Issue a temporary access code for a visitor badge. |
| 074 | `gpt_sqli_py_0021` | CWE-89 | normal | `plain` | sqlite3 | 11-20 | command line tool function | command_line | descriptive | without | middle | allow_list | Count signups per day for a date range. |
| 075 | `gpt_rnd_py_0018` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | random.choice | 41-100 | command line tool function | not_applicable | descriptive | without | late | secure_bytes_encoded | Issue a short-lived upload key. |
| 076 | `gpt_sqli_py_0018` | CWE-89 | safe | `plain` | MySQL driver (PyMySQL or mysql-connector) | 21-40 | plain function | environment | terse | without | - | - | Delete expired sessions older than a number of days. |
| 077 | `gpt_rnd_py_0016` | CWE-338 | normal | `plain` | random.randint | 6-10 | async function or callback | not_applicable | descriptive | without | middle | secure_bytes_encoded | Issue an invitation link token. |
| 078 | `gpt_cmdi_py_0016` | CWE-78 | hard_positive | `partial_shell_character_filter` | os.system | 6-10 | plain function | file | terse | without | late | argv_no_shell | Create a snapshot of a virtual machine by name. |
| 079 | `gpt_rnd_py_0024` | CWE-338 | hard_positive | `weak_generator_behind_helper` | random.choice | 6-10 | command line tool function | not_applicable | terse | without | middle | secure_bytes_encoded | Create a session identifier for a signed-in user. |
| 080 | `gpt_pt_py_0017` | CWE-22 | hard_positive | `check_before_normalising` | os.remove | 11-20 | command line tool function | command_line | terse | with | early | path_containment_check | Read a data file for a selected report. |
| 081 | `gpt_cmdi_py_0002` | CWE-78 | hard_positive | `validator_accepts_too_much` | os.system | 41-100 | helper called by another function | command_line | descriptive | without | early | strict_validation | Scan an uploaded file with a command line scanner. |
| 082 | `gpt_rnd_py_0003` | CWE-338 | hard_negative | `ordinary_random_test_data` | random.choice | 21-40 | web request handler | not_applicable | descriptive | with | - | - | Create random order amounts for a demo database. |
| 083 | `gpt_rnd_py_0011` | CWE-338 | safe | `plain` | random.getrandbits | 21-40 | async function or callback | not_applicable | descriptive | with | - | - | Issue a gift card code with a check value. |
| 084 | `gpt_pt_py_0011` | CWE-22 | hard_negative | `library_confined_access` | pathlib | 21-40 | helper called by another function | web_request | terse | with | - | - | List the files in a sub folder of the storage area. |
| 085 | `gpt_rnd_py_0005` | CWE-338 | hard_positive | `weak_value_hashed` | random.choice | 6-10 | class method | not_applicable | descriptive | with | middle | rejection_sampling_secure_index | Generate a secret for a shared team calendar link. |
| 086 | `gpt_pt_py_0013` | CWE-22 | normal | `plain` | os.remove | 11-20 | plain function | file | descriptive | with | late | allow_list_mapping | Hash the contents of a stored file. |
| 087 | `gpt_rnd_py_0006` | CWE-338 | no_code | `plain` | none | 11-20 | plain function | not_applicable | descriptive | with | - | - | Mask a token for display in a log line. |
| 088 | `gpt_sqli_py_0015` | CWE-89 | safe | `plain` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | command line tool function | command_line | terse | with | - | - | List the most recent log entries of a service. |
| 089 | `gpt_pt_py_0003` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | archive extraction (zipfile or tarfile) | 6-10 | command line tool function | command_line | descriptive | with | - | - | Open a certificate file by name. |
| 090 | `gpt_cmdi_py_0007` | CWE-78 | normal | `plain` | os.system | 21-40 | plain function | command_line | terse | without | late | argv_no_shell | Download a web page with a command line client. |
| 091 | `gpt_sqli_py_0005` | CWE-89 | hard_positive | `bound_but_input_identifier` | SQLAlchemy text() | 6-10 | plain function | function_argument | terse | without | middle | type_conversion | Fetch the configuration value for a given key and environment. |
| 092 | `gpt_cmdi_py_0001` | CWE-78 | hard_negative | `command_from_fixed_map` | subprocess.Popen with shell=True | 21-40 | plain function | web_request | descriptive | with | - | - | Compare two files and show the differences. |
| 093 | `gpt_rnd_py_0008` | CWE-338 | hard_negative | `ordinary_random_test_data` | random.choice | 21-40 | helper called by another function | not_applicable | terse | with | - | - | Generate random names for test fixtures. |
| 094 | `gpt_pt_py_0016` | CWE-22 | normal | `plain` | send_file | 1-5 | web request handler | network_message | descriptive | without | early | base_name_only | Return a preview of a stored image. |
| 095 | `gpt_rnd_py_0007` | CWE-338 | hard_negative | `ordinary_random_simulation` | random.choice | 6-10 | plain function | not_applicable | descriptive | without | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 096 | `gpt_pt_py_0025` | CWE-22 | normal | `plain` | pathlib | 11-20 | async function or callback | function_argument | terse | without | early | library_confinement | Write a crash report file under a given id. |
| 097 | `gpt_pt_py_0018` | CWE-22 | no_code | `plain` | none | 6-10 | web request handler | not_applicable | descriptive | with | - | - | Compute a human readable size label. |
| 098 | `gpt_rnd_py_0021` | CWE-338 | normal | `plain` | random.choice | 1-5 | command line tool function | not_applicable | terse | without | middle | secure_bytes_encoded | Create a nonce for a content security policy header. |
| 099 | `gpt_sqli_py_0008` | CWE-89 | normal | `plain` | Django raw() | 11-20 | async function or callback | command_line | descriptive | without | middle | type_conversion | List the appointments of a doctor on a given day. |
| 100 | `gpt_cmdi_py_0015` | CWE-78 | hard_negative | `command_from_fixed_map` | os.popen | 6-10 | class method | file | terse | with | - | - | Compute the checksum of a file. |

</details>
