## Your job

Write **25 rows** with **Claude** (free base model) in **Go** (CWE-78).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P12b_claude_go_cmdi.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P12b_claude_go_cmdi.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P12b_claude_go_cmdi.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P12b_claude_go_cmdi.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Personal branch `dev/<your-github-username>` made from `main`; issue branch `issue/<number>-P12b_claude_go_cmdi` made from your personal branch
- [ ] All 25 prompts pasted into Claude (new chat for every 10 rows, master prompt first) and every answer pasted under its `=== NNN` line in `submissions/P12b_claude_go_cmdi.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into your personal branch with **only** `submissions/P12b_claude_go_cmdi.txt`; the exact model name written in the description
- [ ] After approval: merged into your personal branch, then one last pull request `dev/<your-github-username>` into `main`

Mix of rows in this package: normal 8, hard_positive 4, safe 4, hard_negative 7, no_code 2. Lengths: 1-5: 3, 6-10: 8, 11-20: 9, 21-40: 5, 41-100: 0.

<details><summary>Table of all rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_cmdi_go_0014` | CWE-78 | hard_positive | `dash_argument_injection` | exec.Command with sh -c | 11-20 | goroutine or callback | network_message | terse | without | late | allow_list | Trace the network route to a host. |
| 002 | `cla_cmdi_go_0021` | CWE-78 | normal | `plain` | exec.Command with arguments | 6-10 | command line tool function | command_line | descriptive | without | middle | strict_validation | Add a user to a group with the system tool. |
| 003 | `cla_cmdi_go_0023` | CWE-78 | safe | `plain` | exec.Command with sh -c | 6-10 | plain function | function_argument | descriptive | with | - | - | Resize an image to a requested size with an external tool. |
| 004 | `cla_cmdi_go_0010` | CWE-78 | normal | `plain` | exec.Command with arguments | 11-20 | command line tool function | command_line | descriptive | without | middle | allow_list | Download a web page with a command line client. |
| 005 | `cla_cmdi_go_0025` | CWE-78 | no_code | `plain` | none | 11-20 | plain function | not_applicable | terse | with | - | - | Check the shape of a host name string. |
| 006 | `cla_cmdi_go_0016` | CWE-78 | normal | `plain` | exec.Command with arguments | 11-20 | goroutine or callback | network_message | terse | without | early | quoting | Execute a report generator with a chosen template. |
| 007 | `cla_cmdi_go_0020` | CWE-78 | safe | `plain` | exec.Command with arguments | 21-40 | method on a struct | environment | terse | without | - | - | Check whether a host answers a network ping. |
| 008 | `cla_cmdi_go_0001` | CWE-78 | hard_negative | `strict_parser_then_no_shell` | exec.Command with arguments | 6-10 | HTTP handler | web_request | terse | without | - | - | Run a spell checker on a text file. |
| 009 | `cla_cmdi_go_0024` | CWE-78 | safe | `plain` | exec.Command with arguments | 6-10 | plain function | file | terse | without | - | - | Trace the network route to a host. |
| 010 | `cla_cmdi_go_0012` | CWE-78 | normal | `plain` | exec.Command with sh -c | 1-5 | method on a struct | web_request | descriptive | with | early | quoting | Convert an audio file to another bitrate. |
| 011 | `cla_cmdi_go_0002` | CWE-78 | hard_negative | `argument_list_with_user_data` | exec.Command with arguments | 6-10 | HTTP handler | web_request | descriptive | with | - | - | Run a unit conversion script on a value. |
| 012 | `cla_cmdi_go_0005` | CWE-78 | normal | `plain` | exec.Command with sh -c | 11-20 | command line tool function | command_line | descriptive | without | early | allow_list | Compare two files and show the differences. |
| 013 | `cla_cmdi_go_0007` | CWE-78 | hard_negative | `constant_shell_command` | exec.Command with sh -c | 11-20 | command line tool function | command_line | descriptive | without | - | - | Check whether a port is open on a host. |
| 014 | `cla_cmdi_go_0008` | CWE-78 | hard_positive | `quoting_in_wrong_context` | exec.Command with sh -c | 21-40 | plain function | environment | descriptive | with | middle | quoting | Restart a named system service. |
| 015 | `cla_cmdi_go_0006` | CWE-78 | hard_negative | `command_from_fixed_map` | exec.Command with sh -c | 6-10 | helper called by another function | file | terse | with | - | - | Zip the contents of a folder into a named archive. |
| 016 | `cla_cmdi_go_0003` | CWE-78 | safe | `plain` | exec.Command with arguments | 21-40 | helper called by another function | web_request | descriptive | with | - | - | Scan an uploaded file with a command line scanner. |
| 017 | `cla_cmdi_go_0017` | CWE-78 | hard_negative | `command_from_fixed_map` | exec.Command with arguments | 6-10 | method on a struct | environment | terse | without | - | - | Run a unit conversion script on a value. |
| 018 | `cla_cmdi_go_0013` | CWE-78 | normal | `plain` | exec.Command with sh -c | 11-20 | HTTP handler | web_request | descriptive | with | middle | argv_no_shell | Read the last lines of a log file. |
| 019 | `cla_cmdi_go_0004` | CWE-78 | hard_positive | `validation_of_other_variable` | exec.Command with arguments | 21-40 | plain function | function_argument | terse | with | early | strict_validation | Stop a process by name. |
| 020 | `cla_cmdi_go_0009` | CWE-78 | normal | `plain` | exec.Command with sh -c | 1-5 | method on a struct | network_message | descriptive | with | early | argv_no_shell | Stop a process by name. |
| 021 | `cla_cmdi_go_0011` | CWE-78 | normal | `plain` | exec.Command with arguments | 6-10 | goroutine or callback | database_value | terse | without | late | strict_validation | Print the version of a tool chosen from a list. |
| 022 | `cla_cmdi_go_0022` | CWE-78 | hard_positive | `validation_of_other_variable` | exec.Command with arguments | 21-40 | helper called by another function | function_argument | descriptive | with | middle | argv_no_shell | Check whether a host answers a network ping. |
| 023 | `cla_cmdi_go_0019` | CWE-78 | hard_negative | `argument_list_with_user_data` | exec.Command with sh -c | 11-20 | helper called by another function | command_line | descriptive | with | - | - | Query a package manager for the version of a package. |
| 024 | `cla_cmdi_go_0015` | CWE-78 | hard_negative | `command_from_fixed_map` | exec.Command with arguments | 11-20 | command line tool function | command_line | descriptive | without | - | - | Execute a report generator with a chosen template. |
| 025 | `cla_cmdi_go_0018` | CWE-78 | no_code | `plain` | none | 1-5 | goroutine or callback | not_applicable | terse | without | - | - | Compute a percentage of a total. |

</details>
