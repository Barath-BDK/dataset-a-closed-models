## Your job

Write **100 rows** with **Gemini** (free base model) in **C++** (CWE-22, CWE-338, CWE-78, CWE-89).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P07_gemini_cpp.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P07_gemini_cpp.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P07_gemini_cpp.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P07_gemini_cpp.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Personal branch `dev/<your-github-username>` made from `main`; issue branch `issue/<number>-P07_gemini_cpp` made from your personal branch
- [ ] All 100 prompts pasted into Gemini (new chat for every 10 rows, master prompt first) and every answer pasted under its `=== NNN` line in `submissions/P07_gemini_cpp.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into your personal branch with **only** `submissions/P07_gemini_cpp.txt`; the exact model name written in the description
- [ ] After approval: merged into your personal branch, then one last pull request `dev/<your-github-username>` into `main`

Mix of rows in this package: normal 33, hard_positive 16, safe 16, hard_negative 27, no_code 8. Lengths: 1-5: 5, 6-10: 28, 11-20: 32, 21-40: 29, 41-100: 6.

<details><summary>Table of all rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `gem_cmdi_cpp_0003` | CWE-78 | hard_positive | `quoting_in_wrong_context` | system | 21-40 | class method | function_argument | descriptive | without | middle | argv_no_shell | Count the lines of a file with a standard tool. |
| 002 | `gem_sqli_cpp_0001` | CWE-89 | hard_positive | `bound_but_input_identifier` | PQexec | 41-100 | plain function | database_value | descriptive | without | middle | prepared_statement_bind | Look up a city by postal code. |
| 003 | `gem_rnd_cpp_0002` | CWE-338 | normal | `plain` | rand | 6-10 | plain function | not_applicable | descriptive | with | late | secure_bytes_encoded | Create an encryption key for a local vault. |
| 004 | `gem_sqli_cpp_0011` | CWE-89 | no_code | `plain` | none | 11-20 | helper called by another function | not_applicable | descriptive | with | - | - | Compute a discount tier from an amount. |
| 005 | `gem_rnd_cpp_0019` | CWE-338 | no_code | `plain` | none | 6-10 | web or network handler that receives a request object | not_applicable | terse | without | - | - | Split a token into its prefix and body. |
| 006 | `gem_sqli_cpp_0021` | CWE-89 | hard_negative | `placeholder_list_for_in` | mysql_query | 21-40 | class method | web_request | descriptive | without | - | - | Find books by author name. |
| 007 | `gem_rnd_cpp_0003` | CWE-338 | safe | `plain` | std::mt19937 | 11-20 | callback, lambda or asynchronous task | not_applicable | terse | without | - | - | Create a cookie value for a remember-me login. |
| 008 | `gem_pt_cpp_0002` | CWE-22 | normal | `plain` | std::filesystem | 11-20 | plain function | web_request | descriptive | with | early | path_containment_check | Write an exported spreadsheet under a requested name. |
| 009 | `gem_rnd_cpp_0010` | CWE-338 | hard_positive | `weak_generator_behind_helper` | std::mt19937 | 21-40 | class method | not_applicable | terse | without | middle | secure_generator_api | Create a private link token for a quiz. |
| 010 | `gem_pt_cpp_0017` | CWE-22 | hard_positive | `check_before_normalising` | fopen | 21-40 | class method | function_argument | descriptive | with | middle | path_containment_check | Check whether a named file exists in the storage area. |
| 011 | `gem_pt_cpp_0004` | CWE-22 | normal | `plain` | fopen | 21-40 | plain function | command_line | descriptive | without | late | path_containment_check | Read the lines of a CSV import file. |
| 012 | `gem_sqli_cpp_0024` | CWE-89 | hard_negative | `placeholders_only_format` | PQexec | 21-40 | web or network handler that receives a request object | web_request | terse | with | - | - | Search products whose name contains a keyword. |
| 013 | `gem_pt_cpp_0005` | CWE-22 | no_code | `plain` | none | 11-20 | class method | not_applicable | descriptive | without | - | - | Return the parent part of a path string. |
| 014 | `gem_pt_cpp_0006` | CWE-22 | normal | `plain` | ifstream or ofstream | 11-20 | web or network handler that receives a request object | web_request | terse | without | middle | allow_list_mapping | Truncate a log file chosen by name. |
| 015 | `gem_pt_cpp_0011` | CWE-22 | hard_negative | `base_name_only` | std::remove | 6-10 | class method | file | terse | without | - | - | Read the first line of a stored file. |
| 016 | `gem_rnd_cpp_0017` | CWE-338 | normal | `plain` | std::mt19937 | 21-40 | plain function | not_applicable | terse | with | middle | secure_generator_api | Create a webhook signing secret. |
| 017 | `gem_cmdi_cpp_0004` | CWE-78 | normal | `plain` | Boost.Process | 11-20 | plain function | file | descriptive | without | middle | allow_list | Zip the contents of a folder into a named archive. |
| 018 | `gem_pt_cpp_0012` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | fopen | 11-20 | web or network handler that receives a request object | web_request | terse | without | - | - | Read a log file of a named service. |
| 019 | `gem_rnd_cpp_0022` | CWE-338 | hard_negative | `ordinary_random_simulation` | std::default_random_engine | 11-20 | callback, lambda or asynchronous task | not_applicable | descriptive | without | - | - | Estimate pi with a Monte Carlo simulation. |
| 020 | `gem_pt_cpp_0003` | CWE-22 | normal | `plain` | ifstream or ofstream | 11-20 | callback, lambda or asynchronous task | network_message | descriptive | with | early | base_name_only | Return the modification time of a stored file. |
| 021 | `gem_rnd_cpp_0014` | CWE-338 | hard_negative | `ordinary_random_games` | std::mt19937 | 21-40 | web or network handler that receives a request object | not_applicable | descriptive | with | - | - | Roll dice for a board game. |
| 022 | `gem_rnd_cpp_0025` | CWE-338 | no_code | `plain` | none | 11-20 | command line tool function | not_applicable | terse | with | - | - | Compute the entropy of a value from its length and alphabet size. |
| 023 | `gem_pt_cpp_0007` | CWE-22 | hard_negative | `library_confined_access` | fopen | 6-10 | class method | environment | terse | without | - | - | Return a preview of a stored image. |
| 024 | `gem_pt_cpp_0024` | CWE-22 | safe | `plain` | std::remove | 21-40 | command line tool function | command_line | terse | with | - | - | Read a user's saved draft. |
| 025 | `gem_sqli_cpp_0010` | CWE-89 | safe | `plain` | MySQL Connector/C++ | 6-10 | web or network handler that receives a request object | database_value | terse | with | - | - | List the appointments of a doctor on a given day. |
| 026 | `gem_sqli_cpp_0016` | CWE-89 | safe | `plain` | sqlite3 C API | 11-20 | callback, lambda or asynchronous task | command_line | terse | with | - | - | Find all accounts created through an affiliate code. |
| 027 | `gem_rnd_cpp_0001` | CWE-338 | normal | `plain` | std::default_random_engine | 6-10 | plain function | not_applicable | descriptive | with | late | rejection_sampling_secure_index | Create an unguessable id for a private upload. |
| 028 | `gem_cmdi_cpp_0014` | CWE-78 | safe | `plain` | QProcess | 11-20 | command line tool function | command_line | terse | with | - | - | Run a unit conversion script on a value. |
| 029 | `gem_cmdi_cpp_0020` | CWE-78 | no_code | `plain` | none | 6-10 | plain function | not_applicable | terse | without | - | - | Compute a percentage of a total. |
| 030 | `gem_rnd_cpp_0011` | CWE-338 | hard_negative | `ordinary_random_games` | rand | 6-10 | class method | not_applicable | terse | with | - | - | Pick a random spawn position for an enemy in a game. |
| 031 | `gem_sqli_cpp_0007` | CWE-89 | normal | `plain` | sqlite3 C API | 21-40 | command line tool function | command_line | descriptive | with | early | query_builder_bind | Return the stock quantity for a product code. |
| 032 | `gem_cmdi_cpp_0022` | CWE-78 | normal | `plain` | popen | 11-20 | callback, lambda or asynchronous task | file | descriptive | without | middle | quoting | Stop a process by name. |
| 033 | `gem_rnd_cpp_0012` | CWE-338 | hard_negative | `ordinary_random_shuffling` | rand | 11-20 | web or network handler that receives a request object | not_applicable | descriptive | without | - | - | Shuffle a playlist before playing it. |
| 034 | `gem_sqli_cpp_0014` | CWE-89 | normal | `plain` | mysql_query | 11-20 | callback, lambda or asynchronous task | web_request | terse | without | early | query_builder_bind | Return the top sellers for a given region. |
| 035 | `gem_rnd_cpp_0013` | CWE-338 | normal | `plain` | std::default_random_engine | 1-5 | plain function | not_applicable | terse | without | late | secure_bytes_encoded | Generate a pairing code for a device. |
| 036 | `gem_pt_cpp_0014` | CWE-22 | safe | `plain` | ifstream or ofstream | 11-20 | class method | network_message | terse | without | - | - | Open a certificate file by name. |
| 037 | `gem_cmdi_cpp_0012` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | popen | 11-20 | callback, lambda or asynchronous task | environment | descriptive | with | - | - | Create a snapshot of a virtual machine by name. |
| 038 | `gem_sqli_cpp_0008` | CWE-89 | hard_negative | `constant_fragments_only` | PQexec | 11-20 | plain function | database_value | descriptive | with | - | - | Search a phone book by name prefix. |
| 039 | `gem_sqli_cpp_0003` | CWE-89 | normal | `plain` | PQexec | 11-20 | callback, lambda or asynchronous task | command_line | descriptive | without | late | prepared_statement_bind | Mark a notification as read for a user. |
| 040 | `gem_rnd_cpp_0023` | CWE-338 | safe | `plain` | rand | 6-10 | command line tool function | not_applicable | terse | with | - | - | Generate an unlock code for a smart lock. |
| 041 | `gem_rnd_cpp_0021` | CWE-338 | safe | `plain` | rand | 6-10 | web or network handler that receives a request object | not_applicable | descriptive | with | - | - | Generate a booking confirmation code. |
| 042 | `gem_pt_cpp_0008` | CWE-22 | normal | `plain` | std::filesystem | 21-40 | web or network handler that receives a request object | web_request | terse | with | middle | allow_list_mapping | Return the contents of a help page file. |
| 043 | `gem_pt_cpp_0023` | CWE-22 | normal | `plain` | std::remove | 41-100 | plain function | database_value | terse | with | middle | allow_list_mapping | Load a configuration file for a named profile. |
| 044 | `gem_pt_cpp_0020` | CWE-22 | normal | `plain` | fopen | 6-10 | callback, lambda or asynchronous task | file | descriptive | without | early | path_containment_check | Restore a document from a version folder. |
| 045 | `gem_rnd_cpp_0024` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | rand | 6-10 | callback, lambda or asynchronous task | not_applicable | descriptive | without | middle | secure_generator_api | Create a list of recovery codes for an account. |
| 046 | `gem_pt_cpp_0013` | CWE-22 | safe | `plain` | ifstream or ofstream | 6-10 | callback, lambda or asynchronous task | function_argument | descriptive | with | - | - | Store a user's avatar image. |
| 047 | `gem_pt_cpp_0010` | CWE-22 | safe | `plain` | ifstream or ofstream | 11-20 | callback, lambda or asynchronous task | function_argument | terse | with | - | - | Create a thumbnail file next to the original image. |
| 048 | `gem_cmdi_cpp_0009` | CWE-78 | normal | `plain` | system | 1-5 | plain function | web_request | descriptive | without | early | strict_validation | Restart a named system service. |
| 049 | `gem_cmdi_cpp_0025` | CWE-78 | hard_negative | `all_arguments_shell_quoted` | system | 11-20 | callback, lambda or asynchronous task | database_value | descriptive | without | - | - | Run a code formatter on a source file. |
| 050 | `gem_sqli_cpp_0023` | CWE-89 | hard_positive | `one_branch_bound` | MySQL Connector/C++ | 41-100 | class method | database_value | descriptive | without | middle | query_builder_bind | Look up a coupon by its code. |
| 051 | `gem_rnd_cpp_0016` | CWE-338 | hard_positive | `weak_generator_behind_helper` | rand | 6-10 | command line tool function | not_applicable | descriptive | without | middle | secure_bytes_encoded | Create a deletion confirmation token. |
| 052 | `gem_cmdi_cpp_0019` | CWE-78 | safe | `plain` | system | 21-40 | web or network handler that receives a request object | web_request | terse | without | - | - | Show the mount information of a device. |
| 053 | `gem_cmdi_cpp_0017` | CWE-78 | hard_negative | `command_from_fixed_map` | QProcess | 21-40 | class method | function_argument | terse | with | - | - | Back up a directory to another location with a sync tool. |
| 054 | `gem_sqli_cpp_0018` | CWE-89 | normal | `plain` | PQexec | 21-40 | class method | environment | descriptive | without | middle | query_builder_bind | Find patients by surname. |
| 055 | `gem_pt_cpp_0018` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | std::filesystem | 11-20 | web or network handler that receives a request object | network_message | terse | with | - | - | Unzip a theme package into the themes folder. |
| 056 | `gem_cmdi_cpp_0005` | CWE-78 | no_code | `plain` | none | 6-10 | class method | not_applicable | terse | with | - | - | Convert Celsius to Fahrenheit. |
| 057 | `gem_sqli_cpp_0005` | CWE-89 | hard_positive | `handwritten_escaping` | PQexec | 11-20 | class method | function_argument | descriptive | without | early | type_conversion | Find articles that carry a given tag. |
| 058 | `gem_sqli_cpp_0025` | CWE-89 | hard_negative | `constant_fragments_only` | Qt QSqlQuery | 21-40 | callback, lambda or asynchronous task | network_message | terse | with | - | - | Set the stock quantity of a product after a delivery. |
| 059 | `gem_sqli_cpp_0015` | CWE-89 | hard_negative | `bound_via_builder` | PQexec | 11-20 | command line tool function | command_line | terse | without | - | - | List the employees of a department. |
| 060 | `gem_sqli_cpp_0019` | CWE-89 | safe | `plain` | mysql_query | 21-40 | callback, lambda or asynchronous task | environment | terse | with | - | - | List recent transactions for an account sorted by amount or date. |
| 061 | `gem_cmdi_cpp_0018` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | Boost.Process | 21-40 | web or network handler that receives a request object | database_value | descriptive | with | - | - | Compress a log file after rotation. |
| 062 | `gem_cmdi_cpp_0002` | CWE-78 | normal | `plain` | QProcess | 1-5 | command line tool function | command_line | terse | without | early | quoting | Extract a thumbnail frame from a video file. |
| 063 | `gem_rnd_cpp_0004` | CWE-338 | hard_positive | `weak_value_hashed` | std::mt19937 | 21-40 | helper called by another function | not_applicable | descriptive | without | late | secure_generator_api | Generate a nonce for a signed request. |
| 064 | `gem_cmdi_cpp_0023` | CWE-78 | hard_negative | `argument_list_with_user_data` | popen | 6-10 | web or network handler that receives a request object | database_value | descriptive | without | - | - | Send a document to a named printer. |
| 065 | `gem_rnd_cpp_0007` | CWE-338 | normal | `plain` | std::mt19937 | 21-40 | helper called by another function | not_applicable | descriptive | without | late | secure_generator_api | Create a share link secret for a document. |
| 066 | `gem_rnd_cpp_0020` | CWE-338 | normal | `plain` | std::mt19937 | 21-40 | callback, lambda or asynchronous task | not_applicable | terse | with | late | secure_bytes_encoded | Create a token for confirming a newsletter subscription. |
| 067 | `gem_pt_cpp_0025` | CWE-22 | hard_positive | `extension_check_only` | std::filesystem | 11-20 | command line tool function | command_line | descriptive | with | middle | allow_list_mapping | Serve a static asset such as an image or stylesheet. |
| 068 | `gem_sqli_cpp_0006` | CWE-89 | hard_negative | `placeholder_list_for_in` | mysql_query | 6-10 | command line tool function | command_line | descriptive | with | - | - | Remove a product from a wishlist. |
| 069 | `gem_cmdi_cpp_0011` | CWE-78 | normal | `plain` | popen | 6-10 | web or network handler that receives a request object | web_request | terse | with | late | quoting | Compare two files and show the differences. |
| 070 | `gem_pt_cpp_0015` | CWE-22 | hard_positive | `prefix_test_without_separator` | ifstream or ofstream | 6-10 | web or network handler that receives a request object | web_request | terse | with | early | path_containment_check | Delete temporary files that match a name. |
| 071 | `gem_pt_cpp_0021` | CWE-22 | hard_negative | `id_mapped_to_known_file` | std::remove | 6-10 | web or network handler that receives a request object | web_request | terse | with | - | - | Open a certificate file by name. |
| 072 | `gem_rnd_cpp_0006` | CWE-338 | safe | `plain` | rand | 41-100 | web or network handler that receives a request object | not_applicable | terse | without | - | - | Create an encryption key for a local vault. |
| 073 | `gem_cmdi_cpp_0006` | CWE-78 | hard_positive | `validation_of_other_variable` | popen | 21-40 | callback, lambda or asynchronous task | file | descriptive | without | early | strict_validation | Run a database backup tool for one schema. |
| 074 | `gem_cmdi_cpp_0015` | CWE-78 | safe | `plain` | popen | 6-10 | plain function | environment | terse | with | - | - | Convert an audio file to another bitrate. |
| 075 | `gem_sqli_cpp_0020` | CWE-89 | hard_negative | `placeholders_only_format` | sqlite3 C API | 21-40 | helper called by another function | web_request | descriptive | without | - | - | Find events happening in a given city. |
| 076 | `gem_sqli_cpp_0017` | CWE-89 | normal | `plain` | PQexec | 1-5 | web or network handler that receives a request object | network_message | terse | with | early | prepared_statement_bind | Set the stock quantity of a product after a delivery. |
| 077 | `gem_cmdi_cpp_0021` | CWE-78 | safe | `plain` | system | 11-20 | class method | web_request | terse | with | - | - | Compute the checksum of a file. |
| 078 | `gem_rnd_cpp_0005` | CWE-338 | hard_negative | `ordinary_random_sampling` | rand | 41-100 | callback, lambda or asynchronous task | not_applicable | terse | with | - | - | Choose which products to feature on the home page. |
| 079 | `gem_rnd_cpp_0008` | CWE-338 | normal | `plain` | std::default_random_engine | 21-40 | command line tool function | not_applicable | terse | with | early | secure_bytes_encoded | Generate a CSRF token for a form. |
| 080 | `gem_cmdi_cpp_0001` | CWE-78 | hard_positive | `validator_accepts_too_much` | system | 21-40 | command line tool function | command_line | terse | with | late | quoting | Run a spell checker on a text file. |
| 081 | `gem_rnd_cpp_0018` | CWE-338 | normal | `plain` | std::mt19937 | 11-20 | class method | not_applicable | terse | with | middle | rejection_sampling_secure_index | Create a challenge string for a login handshake. |
| 082 | `gem_sqli_cpp_0013` | CWE-89 | hard_positive | `bound_but_input_identifier` | PQexec | 11-20 | plain function | database_value | terse | with | middle | prepared_statement_bind | Find patients by surname. |
| 083 | `gem_sqli_cpp_0022` | CWE-89 | normal | `plain` | Qt QSqlQuery | 1-5 | helper called by another function | network_message | terse | without | late | type_conversion | Look up the shipping address of an order. |
| 084 | `gem_sqli_cpp_0002` | CWE-89 | no_code | `plain` | none | 6-10 | callback, lambda or asynchronous task | not_applicable | terse | with | - | - | Shorten a long description for a list view. |
| 085 | `gem_sqli_cpp_0012` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 21-40 | command line tool function | command_line | descriptive | without | late | allow_list | Search a product catalogue with optional filters for price and brand. |
| 086 | `gem_cmdi_cpp_0016` | CWE-78 | hard_positive | `dash_argument_injection` | popen | 11-20 | helper called by another function | database_value | terse | with | early | allow_list | Show the owner and permissions of a file. |
| 087 | `gem_sqli_cpp_0004` | CWE-89 | safe | `plain` | Qt QSqlQuery | 21-40 | web or network handler that receives a request object | web_request | terse | without | - | - | Record an audit entry for an administrator action. |
| 088 | `gem_pt_cpp_0016` | CWE-22 | no_code | `plain` | none | 6-10 | web or network handler that receives a request object | not_applicable | terse | without | - | - | Format a timestamp for a file listing. |
| 089 | `gem_sqli_cpp_0009` | CWE-89 | normal | `plain` | MySQL Connector/C++ | 6-10 | class method | database_value | terse | with | middle | prepared_statement_bind | Find the members of a team by role. |
| 090 | `gem_cmdi_cpp_0007` | CWE-78 | hard_negative | `user_data_after_end_of_options` | popen | 41-100 | web or network handler that receives a request object | web_request | descriptive | with | - | - | Resize an image to a requested size with an external tool. |
| 091 | `gem_cmdi_cpp_0008` | CWE-78 | normal | `plain` | QProcess | 21-40 | class method | network_message | descriptive | without | middle | strict_validation | Run a database backup tool for one schema. |
| 092 | `gem_pt_cpp_0009` | CWE-22 | hard_positive | `single_pass_parent_removal` | std::filesystem | 6-10 | command line tool function | command_line | descriptive | with | late | base_name_only | Create a backup copy of a document. |
| 093 | `gem_cmdi_cpp_0024` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | popen | 11-20 | class method | function_argument | terse | with | - | - | Mount a network share with given options. |
| 094 | `gem_pt_cpp_0019` | CWE-22 | normal | `plain` | std::remove | 21-40 | class method | file | descriptive | without | middle | allow_list_mapping | Save a note under a given name. |
| 095 | `gem_cmdi_cpp_0013` | CWE-78 | normal | `plain` | QProcess | 6-10 | class method | network_message | terse | without | late | argv_no_shell | Unpack an uploaded archive into a working folder. |
| 096 | `gem_cmdi_cpp_0010` | CWE-78 | normal | `plain` | popen | 6-10 | plain function | command_line | descriptive | with | late | strict_validation | Read the last lines of a log file. |
| 097 | `gem_pt_cpp_0001` | CWE-22 | normal | `plain` | fopen | 21-40 | plain function | network_message | descriptive | with | late | allow_list_mapping | Report the size of a stored file. |
| 098 | `gem_pt_cpp_0022` | CWE-22 | hard_negative | `id_mapped_to_known_file` | ifstream or ofstream | 6-10 | helper called by another function | network_message | descriptive | without | - | - | Move a processed file to an archive folder. |
| 099 | `gem_rnd_cpp_0009` | CWE-338 | hard_negative | `ordinary_random_retry_jitter` | std::mt19937 | 11-20 | class method | not_applicable | descriptive | with | - | - | Choose a polling interval spread between workers. |
| 100 | `gem_rnd_cpp_0015` | CWE-338 | hard_negative | `ordinary_random_sampling` | rand | 11-20 | web or network handler that receives a request object | not_applicable | descriptive | without | - | - | Pick a random sample of users for a satisfaction survey. |

</details>
