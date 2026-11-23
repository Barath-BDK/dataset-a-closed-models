## 🟦 STEP 2 of 3

**Assigned to: dHEENA0644.** Do this **after** your first issue (#20) is approved. Rows **006 to 100** (Gemini × Python).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P05_gemini_python.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P05_gemini_python.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P05_gemini_python.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P05_gemini_python.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P05_gemini_python` made from your personal branch `dev/dHEENA0644` (after the earlier steps are merged)
- [ ] Prompts for rows 006-100 pasted into Gemini (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P05_gemini_python.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/dHEENA0644` with **only** `submissions/P05_gemini_python.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/dHEENA0644`; when all your steps are merged, one last pull request `dev/dHEENA0644` into `main`

Mix of rows: normal 32, hard_negative 25, hard_positive 16, safe 14, no_code 8.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006 | `gem_sqli_py_0001` | CWE-89 | normal | `plain` | sqlite3 | 21-40 | async function or callback | function_argument | terse | with | early | bound_parameters | Export the orders of a given month. |
| 007 | `gem_sqli_py_0013` | CWE-89 | hard_negative | `bound_via_builder` | sqlite3 | 21-40 | plain function | web_request | terse | with | - | - | Find events happening in a given city. |
| 008 | `gem_cmdi_py_0004` | CWE-78 | hard_positive | `quoting_in_wrong_context` | subprocess.Popen with shell=True | 21-40 | web request handler | web_request | descriptive | without | late | strict_validation | Run a unit conversion script on a value. |
| 009 | `gem_pt_py_0011` | CWE-22 | hard_positive | `check_before_normalising` | os.remove | 11-20 | helper called by another function | database_value | terse | with | early | library_confinement | Open a certificate file by name. |
| 010 | `gem_sqli_py_0007` | CWE-89 | hard_positive | `keyword_blocklist` | psycopg2 | 11-20 | plain function | file | terse | with | early | allow_list | Mark a notification as read for a user. |
| 011 | `gem_cmdi_py_0001` | CWE-78 | hard_negative | `argument_list_with_user_data` | subprocess.Popen with shell=True | 6-10 | class method | function_argument | terse | with | - | - | Show the fingerprint of an ssh key file. |
| 012 | `gem_sqli_py_0023` | CWE-89 | hard_positive | `handwritten_escaping` | Django raw() | 21-40 | plain function | function_argument | terse | with | middle | bound_parameters | List a user's orders with a given status. |
| 013 | `gem_pt_py_0018` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | shutil.copy | 6-10 | web request handler | web_request | terse | without | - | - | Write an exported spreadsheet under a requested name. |
| 014 | `gem_rnd_py_0004` | CWE-338 | normal | `plain` | random.getrandbits | 1-5 | async function or callback | not_applicable | terse | with | early | rejection_sampling_secure_index | Create a verification code for a phone number. |
| 015 | `gem_pt_py_0025` | CWE-22 | safe | `plain` | shutil.copy | 11-20 | plain function | command_line | terse | without | - | - | Move a processed file to an archive folder. |
| 016 | `gem_pt_py_0021` | CWE-22 | safe | `plain` | os.remove | 21-40 | async function or callback | file | descriptive | without | - | - | Return the text of an uploaded file. |
| 017 | `gem_cmdi_py_0020` | CWE-78 | normal | `plain` | os.popen | 1-5 | class method | database_value | terse | with | middle | strict_validation | Compress a log file after rotation. |
| 018 | `gem_rnd_py_0005` | CWE-338 | normal | `plain` | random.choice | 11-20 | web request handler | not_applicable | terse | with | late | secure_generator_api | Create a one-time code for two-factor sign in. |
| 019 | `gem_pt_py_0019` | CWE-22 | normal | `plain` | send_file | 1-5 | plain function | function_argument | terse | without | late | library_confinement | Open a video file for streaming. |
| 020 | `gem_sqli_py_0011` | CWE-89 | hard_negative | `identifier_allowlist` | SQLAlchemy text() | 41-100 | helper called by another function | web_request | descriptive | with | - | - | List the employees of a department. |
| 021 | `gem_sqli_py_0021` | CWE-89 | hard_negative | `constant_fragments_only` | sqlite3 | 21-40 | web request handler | network_message | descriptive | without | - | - | Find all students enrolled in a course. |
| 022 | `gem_rnd_py_0022` | CWE-338 | safe | `plain` | random.getrandbits | 11-20 | helper called by another function | not_applicable | terse | without | - | - | Issue an invitation link token. |
| 023 | `gem_cmdi_py_0017` | CWE-78 | normal | `plain` | os.popen | 1-5 | async function or callback | network_message | descriptive | with | early | argv_no_shell | Resize an image to a requested size with an external tool. |
| 024 | `gem_pt_py_0013` | CWE-22 | normal | `plain` | open | 6-10 | command line tool function | command_line | descriptive | without | middle | base_name_only | Delete temporary files that match a name. |
| 025 | `gem_cmdi_py_0009` | CWE-78 | normal | `plain` | os.system | 1-5 | class method | environment | descriptive | without | early | quoting | Rotate the logs of one application. |
| 026 | `gem_rnd_py_0010` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | random.choice | 21-40 | web request handler | not_applicable | descriptive | without | early | secure_bytes_encoded | Generate a PIN for a card activation. |
| 027 | `gem_sqli_py_0003` | CWE-89 | hard_positive | `one_branch_bound` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | async function or callback | database_value | descriptive | with | middle | orm_query_builder | Find all accounts created through an affiliate code. |
| 028 | `gem_rnd_py_0006` | CWE-338 | hard_negative | `ordinary_random_simulation` | random.choices | 11-20 | class method | not_applicable | terse | with | - | - | Estimate pi with a Monte Carlo simulation. |
| 029 | `gem_rnd_py_0013` | CWE-338 | hard_negative | `ordinary_random_games` | random.getrandbits | 6-10 | helper called by another function | not_applicable | terse | with | - | - | Pick a random spawn position for an enemy in a game. |
| 030 | `gem_rnd_py_0024` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | random.choice | 6-10 | helper called by another function | not_applicable | descriptive | with | late | secure_generator_api | Generate a nonce for a signed request. |
| 031 | `gem_cmdi_py_0005` | CWE-78 | normal | `plain` | os.system | 21-40 | command line tool function | command_line | descriptive | with | middle | argv_no_shell | Count the lines of a file with a standard tool. |
| 032 | `gem_cmdi_py_0013` | CWE-78 | hard_negative | `user_data_after_end_of_options` | os.popen | 11-20 | web request handler | web_request | descriptive | with | - | - | Look up the DNS records of a host name. |
| 033 | `gem_rnd_py_0021` | CWE-338 | hard_negative | `fixed_seed_reproducible` | random.getrandbits | 11-20 | class method | not_applicable | terse | without | - | - | Draw the same sample every run for a reproducible experiment. |
| 034 | `gem_cmdi_py_0015` | CWE-78 | no_code | `plain` | none | 6-10 | plain function | not_applicable | terse | without | - | - | Escape a string for display in an HTML page. |
| 035 | `gem_sqli_py_0006` | CWE-89 | safe | `plain` | psycopg2 | 41-100 | plain function | web_request | descriptive | without | - | - | Set the stock quantity of a product after a delivery. |
| 036 | `gem_rnd_py_0012` | CWE-338 | no_code | `plain` | none | 1-5 | helper called by another function | not_applicable | descriptive | with | - | - | Split a token into its prefix and body. |
| 037 | `gem_rnd_py_0023` | CWE-338 | hard_negative | `ordinary_random_simulation` | random.choice | 11-20 | plain function | not_applicable | terse | without | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 038 | `gem_pt_py_0008` | CWE-22 | no_code | `plain` | none | 6-10 | web request handler | not_applicable | descriptive | without | - | - | Return the parent part of a path string. |
| 039 | `gem_pt_py_0017` | CWE-22 | normal | `plain` | archive extraction (zipfile or tarfile) | 11-20 | helper called by another function | web_request | terse | with | middle | allow_list_mapping | Return the contents of a shared snippet file. |
| 040 | `gem_rnd_py_0009` | CWE-338 | normal | `plain` | random.choice | 1-5 | async function or callback | not_applicable | terse | without | late | secure_generator_api | Create a salt for hashing a password. |
| 041 | `gem_rnd_py_0025` | CWE-338 | hard_positive | `seed_from_clock_or_pid` | random.randint | 6-10 | class method | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Create a cookie value for a remember-me login. |
| 042 | `gem_cmdi_py_0021` | CWE-78 | normal | `plain` | subprocess.Popen with shell=True | 6-10 | helper called by another function | web_request | descriptive | with | late | quoting | Extract a thumbnail frame from a video file. |
| 043 | `gem_sqli_py_0025` | CWE-89 | normal | `plain` | SQLAlchemy text() | 11-20 | helper called by another function | file | terse | with | middle | bound_parameters | Find all accounts created through an affiliate code. |
| 044 | `gem_cmdi_py_0022` | CWE-78 | hard_negative | `user_data_after_end_of_options` | subprocess.run with shell=True | 6-10 | command line tool function | command_line | terse | with | - | - | Pack an installer from a folder with a packaging tool. |
| 045 | `gem_rnd_py_0018` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | random.getrandbits | 11-20 | plain function | not_applicable | terse | with | - | - | Generate a booking confirmation code. |
| 046 | `gem_pt_py_0023` | CWE-22 | normal | `plain` | os.remove | 21-40 | web request handler | web_request | terse | with | middle | library_confinement | Read a font file requested by a stylesheet. |
| 047 | `gem_cmdi_py_0008` | CWE-78 | hard_positive | `quoting_in_wrong_context` | subprocess.run with shell=True | 11-20 | plain function | function_argument | terse | without | late | allow_list | Check whether a port is open on a host. |
| 048 | `gem_rnd_py_0008` | CWE-338 | no_code | `plain` | none | 1-5 | web request handler | not_applicable | descriptive | with | - | - | Estimate password strength from its length. |
| 049 | `gem_pt_py_0002` | CWE-22 | normal | `plain` | pathlib | 6-10 | class method | environment | descriptive | with | late | library_confinement | Store a user's avatar image. |
| 050 | `gem_sqli_py_0015` | CWE-89 | hard_negative | `integer_forced` | SQLAlchemy text() | 11-20 | web request handler | web_request | descriptive | without | - | - | Search a product catalogue with optional filters for price and brand. |
| 051 | `gem_cmdi_py_0025` | CWE-78 | normal | `plain` | subprocess.check_output | 11-20 | helper called by another function | environment | terse | with | early | argv_no_shell | Start a background job from a script name. |
| 052 | `gem_cmdi_py_0024` | CWE-78 | safe | `plain` | subprocess.run with shell=True | 41-100 | web request handler | web_request | terse | without | - | - | Show the commit history of a repository for one author. |
| 053 | `gem_pt_py_0015` | CWE-22 | normal | `plain` | archive extraction (zipfile or tarfile) | 11-20 | async function or callback | web_request | terse | with | late | allow_list_mapping | Create a backup copy of a document. |
| 054 | `gem_sqli_py_0022` | CWE-89 | no_code | `plain` | none | 1-5 | async function or callback | not_applicable | descriptive | with | - | - | Build a display name from first and last name. |
| 055 | `gem_pt_py_0007` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | shutil.copy | 11-20 | web request handler | network_message | terse | with | - | - | Load the translation file for a locale. |
| 056 | `gem_pt_py_0010` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | pathlib | 6-10 | async function or callback | environment | descriptive | with | - | - | Write a user's settings file. |
| 057 | `gem_cmdi_py_0010` | CWE-78 | normal | `plain` | subprocess.run with shell=True | 11-20 | async function or callback | network_message | terse | with | early | allow_list | Restart a named system service. |
| 058 | `gem_pt_py_0020` | CWE-22 | hard_positive | `single_pass_parent_removal` | pathlib | 11-20 | web request handler | web_request | descriptive | without | early | base_name_only | Copy a template file into a user's workspace. |
| 059 | `gem_cmdi_py_0012` | CWE-78 | hard_positive | `partial_shell_character_filter` | subprocess.check_output | 21-40 | plain function | function_argument | descriptive | with | late | strict_validation | Trace the network route to a host. |
| 060 | `gem_pt_py_0001` | CWE-22 | safe | `plain` | open | 6-10 | plain function | environment | descriptive | without | - | - | Hash the contents of a stored file. |
| 061 | `gem_cmdi_py_0003` | CWE-78 | hard_positive | `validator_accepts_too_much` | subprocess.Popen with shell=True | 11-20 | helper called by another function | network_message | terse | with | middle | argv_no_shell | Read the expiry date of a certificate file. |
| 062 | `gem_sqli_py_0005` | CWE-89 | hard_positive | `bound_but_input_identifier` | Django raw() | 11-20 | helper called by another function | web_request | descriptive | with | early | type_conversion | Record an audit entry for an administrator action. |
| 063 | `gem_sqli_py_0002` | CWE-89 | normal | `plain` | SQLAlchemy text() | 6-10 | command line tool function | command_line | terse | with | middle | type_conversion | Insert a new product review. |
| 064 | `gem_sqli_py_0009` | CWE-89 | hard_negative | `constant_fragments_only` | Django raw() | 6-10 | helper called by another function | command_line | descriptive | with | - | - | Return a page of articles sorted by a column chosen by the caller. |
| 065 | `gem_rnd_py_0002` | CWE-338 | safe | `plain` | random.randint | 21-40 | plain function | not_applicable | descriptive | without | - | - | Generate a password reset token to email to a user. |
| 066 | `gem_rnd_py_0020` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | random.choice | 41-100 | async function or callback | not_applicable | descriptive | without | - | - | Compute a retry delay with random jitter so clients do not retry together. |
| 067 | `gem_pt_py_0004` | CWE-22 | no_code | `plain` | none | 11-20 | command line tool function | not_applicable | descriptive | without | - | - | Pick an icon name from a file extension. |
| 068 | `gem_rnd_py_0003` | CWE-338 | normal | `plain` | random.getrandbits | 6-10 | web request handler | not_applicable | descriptive | without | late | secure_generator_api | Generate a one-time voucher for a refund. |
| 069 | `gem_sqli_py_0024` | CWE-89 | hard_negative | `bound_via_builder` | SQLAlchemy text() | 41-100 | command line tool function | command_line | terse | without | - | - | Update the email address of a user profile. |
| 070 | `gem_pt_py_0012` | CWE-22 | hard_negative | `id_mapped_to_known_file` | send_file | 6-10 | command line tool function | command_line | terse | with | - | - | Check whether a named file exists in the storage area. |
| 071 | `gem_pt_py_0006` | CWE-22 | hard_negative | `library_confined_access` | send_file | 6-10 | async function or callback | database_value | terse | without | - | - | Read a language pack for a game. |
| 072 | `gem_pt_py_0016` | CWE-22 | hard_positive | `prefix_test_without_separator` | archive extraction (zipfile or tarfile) | 21-40 | class method | file | descriptive | without | middle | library_confinement | Let a user download a generated report by name. |
| 073 | `gem_sqli_py_0004` | CWE-89 | normal | `plain` | sqlite3 | 1-5 | plain function | environment | descriptive | with | middle | type_conversion | List recent transactions for an account sorted by amount or date. |
| 074 | `gem_sqli_py_0017` | CWE-89 | safe | `plain` | psycopg2 | 41-100 | plain function | web_request | descriptive | with | - | - | Check a username and password hash for a login. |
| 075 | `gem_cmdi_py_0002` | CWE-78 | hard_negative | `constant_shell_command` | subprocess.check_output | 11-20 | async function or callback | web_request | terse | with | - | - | Show the owner and permissions of a file. |
| 076 | `gem_cmdi_py_0006` | CWE-78 | safe | `plain` | os.popen | 21-40 | web request handler | web_request | descriptive | without | - | - | Convert a document to another format with a converter. |
| 077 | `gem_sqli_py_0018` | CWE-89 | safe | `plain` | psycopg2 | 21-40 | web request handler | network_message | terse | with | - | - | Delete expired sessions older than a number of days. |
| 078 | `gem_cmdi_py_0011` | CWE-78 | hard_negative | `constant_shell_command` | subprocess.run with shell=True | 11-20 | command line tool function | command_line | descriptive | without | - | - | Run a code formatter on a source file. |
| 079 | `gem_rnd_py_0016` | CWE-338 | hard_positive | `weak_value_hashed` | random.choice | 11-20 | helper called by another function | not_applicable | terse | without | early | secure_bytes_encoded | Create a challenge string for a login handshake. |
| 080 | `gem_rnd_py_0007` | CWE-338 | normal | `plain` | random.choices | 6-10 | helper called by another function | not_applicable | descriptive | with | late | rejection_sampling_secure_index | Generate an access token for a mobile app. |
| 081 | `gem_rnd_py_0019` | CWE-338 | hard_negative | `fixed_seed_reproducible` | random.getrandbits | 11-20 | class method | not_applicable | terse | without | - | - | Generate reproducible synthetic data for a unit test. |
| 082 | `gem_rnd_py_0011` | CWE-338 | normal | `plain` | random.choice | 21-40 | command line tool function | not_applicable | terse | without | middle | secure_generator_api | Generate a bearer token for a service account. |
| 083 | `gem_pt_py_0003` | CWE-22 | hard_positive | `single_pass_parent_removal` | shutil.copy | 6-10 | helper called by another function | function_argument | descriptive | with | late | allow_list_mapping | Write a user's settings file. |
| 084 | `gem_rnd_py_0001` | CWE-338 | safe | `plain` | random.choices | 6-10 | command line tool function | not_applicable | terse | with | - | - | Generate a password reset token to email to a user. |
| 085 | `gem_rnd_py_0014` | CWE-338 | normal | `plain` | random.randint | 41-100 | web request handler | not_applicable | descriptive | with | middle | rejection_sampling_secure_index | Create a key for a private download link. |
| 086 | `gem_sqli_py_0008` | CWE-89 | safe | `plain` | psycopg2 | 6-10 | class method | network_message | terse | with | - | - | List reservations for a room between two dates. |
| 087 | `gem_sqli_py_0014` | CWE-89 | normal | `plain` | MySQL driver (PyMySQL or mysql-connector) | 11-20 | helper called by another function | web_request | descriptive | without | middle | orm_query_builder | Search a phone book by name prefix. |
| 088 | `gem_cmdi_py_0014` | CWE-78 | normal | `plain` | subprocess.check_output | 21-40 | helper called by another function | database_value | descriptive | with | middle | allow_list | Search a log file for lines containing a term. |
| 089 | `gem_sqli_py_0020` | CWE-89 | normal | `plain` | Django raw() | 6-10 | class method | command_line | descriptive | without | early | type_conversion | Find articles that carry a given tag. |
| 090 | `gem_sqli_py_0019` | CWE-89 | normal | `plain` | sqlite3 | 21-40 | helper called by another function | database_value | descriptive | without | middle | bound_parameters | Search support tickets by keyword and priority. |
| 091 | `gem_cmdi_py_0007` | CWE-78 | safe | `plain` | os.popen | 6-10 | async function or callback | function_argument | descriptive | without | - | - | Show the owner and permissions of a file. |
| 092 | `gem_cmdi_py_0016` | CWE-78 | normal | `plain` | subprocess.Popen with shell=True | 6-10 | command line tool function | command_line | descriptive | with | early | strict_validation | Look up the registration data of a domain. |
| 093 | `gem_sqli_py_0012` | CWE-89 | no_code | `plain` | none | 11-20 | helper called by another function | not_applicable | terse | without | - | - | Check the shape of an email address. |
| 094 | `gem_pt_py_0009` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | open | 21-40 | class method | command_line | descriptive | without | - | - | Read a user's saved draft. |
| 095 | `gem_cmdi_py_0019` | CWE-78 | hard_negative | `argument_list_with_user_data` | subprocess.check_output | 11-20 | helper called by another function | database_value | descriptive | without | - | - | Add a user to a group with the system tool. |
| 096 | `gem_pt_py_0005` | CWE-22 | normal | `plain` | os.remove | 11-20 | async function or callback | environment | terse | without | middle | path_containment_check | Load the translation file for a locale. |
| 097 | `gem_cmdi_py_0023` | CWE-78 | safe | `plain` | os.popen | 21-40 | plain function | file | descriptive | without | - | - | Query a package manager for the version of a package. |
| 098 | `gem_pt_py_0014` | CWE-22 | normal | `plain` | archive extraction (zipfile or tarfile) | 1-5 | helper called by another function | function_argument | terse | without | late | base_name_only | Return the contents of a help page file. |
| 099 | `gem_cmdi_py_0018` | CWE-78 | no_code | `plain` | none | 11-20 | class method | not_applicable | descriptive | with | - | - | Build the text of a report header. |
| 100 | `gem_rnd_py_0015` | CWE-338 | normal | `plain` | random.choices | 6-10 | async function or callback | not_applicable | descriptive | without | late | rejection_sampling_secure_index | Generate a shared secret for a time-based one-time password setup. |

</details>
