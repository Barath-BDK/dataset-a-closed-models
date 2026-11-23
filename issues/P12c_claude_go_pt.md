## 🟦 STEP 3 of 3: extra package

**Assigned to: kanishkagopiramanan-ai.** Do this after your other steps. All 25 rows (Claude × Go × CWE-22).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P12c_claude_go_pt.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P12c_claude_go_pt.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P12c_claude_go_pt.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P12c_claude_go_pt.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P12c_claude_go_pt` made from your personal branch `dev/kanishkagopiramanan-ai` (after the earlier steps are merged)
- [ ] Prompts for rows 001-025 pasted into Claude (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P12c_claude_go_pt.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/kanishkagopiramanan-ai` with **only** `submissions/P12c_claude_go_pt.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/kanishkagopiramanan-ai`; when all your steps are merged, one last pull request `dev/kanishkagopiramanan-ai` into `main`

Mix of rows: normal 9, hard_negative 6, no_code 2, hard_positive 4, safe 4.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_pt_go_0018` | CWE-22 | normal | `plain` | os.Create | 21-40 | helper called by another function | database_value | descriptive | with | early | base_name_only | Unzip a theme package into the themes folder. |
| 002 | `cla_pt_go_0005` | CWE-22 | hard_negative | `resolve_then_separator_aware_check` | http.ServeFile | 6-10 | helper called by another function | file | terse | without | - | - | Store a user's avatar image. |
| 003 | `cla_pt_go_0001` | CWE-22 | normal | `plain` | os.Open | 6-10 | method on a struct | web_request | terse | without | middle | path_containment_check | Return a preview of a stored image. |
| 004 | `cla_pt_go_0023` | CWE-22 | no_code | `plain` | none | 6-10 | goroutine or callback | not_applicable | descriptive | with | - | - | Format a timestamp for a file listing. |
| 005 | `cla_pt_go_0008` | CWE-22 | hard_positive | `prefix_test_without_separator` | os.ReadFile | 6-10 | method on a struct | function_argument | terse | with | late | path_containment_check | Read a language pack for a game. |
| 006 | `cla_pt_go_0010` | CWE-22 | hard_negative | `id_mapped_to_known_file` | os.Open | 6-10 | command line tool function | command_line | descriptive | without | - | - | Read an email template by name. |
| 007 | `cla_pt_go_0016` | CWE-22 | normal | `plain` | os.Create | 21-40 | goroutine or callback | file | terse | without | late | allow_list_mapping | Read a data file for a selected report. |
| 008 | `cla_pt_go_0014` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 6-10 | HTTP handler | database_value | terse | without | - | - | Return the contents of a help page file. |
| 009 | `cla_pt_go_0006` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 41-100 | HTTP handler | web_request | descriptive | without | - | - | List the files in a sub folder of the storage area. |
| 010 | `cla_pt_go_0021` | CWE-22 | hard_positive | `extension_check_only` | http.ServeFile | 6-10 | goroutine or callback | command_line | terse | with | middle | base_name_only | Return the text of an uploaded file. |
| 011 | `cla_pt_go_0019` | CWE-22 | normal | `plain` | os.Create | 21-40 | HTTP handler | network_message | terse | with | middle | allow_list_mapping | Serve a static asset such as an image or stylesheet. |
| 012 | `cla_pt_go_0012` | CWE-22 | normal | `plain` | os.Open | 41-100 | command line tool function | command_line | descriptive | without | middle | library_confinement | Save a note under a given name. |
| 013 | `cla_pt_go_0003` | CWE-22 | hard_positive | `relative_check_misses_absolute` | http.ServeFile | 6-10 | command line tool function | command_line | terse | without | early | base_name_only | Read the lines of a CSV import file. |
| 014 | `cla_pt_go_0024` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | os.Create | 11-20 | helper called by another function | command_line | descriptive | with | - | - | Copy a template file into a user's workspace. |
| 015 | `cla_pt_go_0017` | CWE-22 | normal | `plain` | os.Open | 1-5 | command line tool function | command_line | descriptive | with | middle | library_confinement | Load the translation file for a locale. |
| 016 | `cla_pt_go_0002` | CWE-22 | normal | `plain` | os.Open | 6-10 | command line tool function | command_line | terse | with | late | base_name_only | Append a line to a user's activity log. |
| 017 | `cla_pt_go_0013` | CWE-22 | safe | `plain` | archive extraction (archive/zip) | 6-10 | helper called by another function | web_request | terse | without | - | - | Fetch a user's uploaded resume. |
| 018 | `cla_pt_go_0011` | CWE-22 | hard_negative | `library_confined_access` | os.Open | 11-20 | command line tool function | command_line | terse | with | - | - | Serve a PDF from the document library. |
| 019 | `cla_pt_go_0022` | CWE-22 | hard_negative | `base_name_only` | archive extraction (archive/zip) | 21-40 | helper called by another function | network_message | descriptive | with | - | - | Hash the contents of a stored file. |
| 020 | `cla_pt_go_0020` | CWE-22 | normal | `plain` | os.Open | 6-10 | command line tool function | command_line | terse | with | early | allow_list_mapping | Delete a user's attachment. |
| 021 | `cla_pt_go_0004` | CWE-22 | normal | `plain` | http.ServeFile | 41-100 | goroutine or callback | web_request | descriptive | without | middle | base_name_only | Check whether a named file exists in the storage area. |
| 022 | `cla_pt_go_0009` | CWE-22 | hard_negative | `safe_filename_helper_fixed_folder` | os.ReadFile | 21-40 | plain function | file | descriptive | with | - | - | Create a thumbnail file next to the original image. |
| 023 | `cla_pt_go_0007` | CWE-22 | safe | `plain` | os.Open | 11-20 | command line tool function | command_line | terse | with | - | - | Remove an old export file. |
| 024 | `cla_pt_go_0025` | CWE-22 | hard_positive | `single_pass_parent_removal` | http.ServeFile | 21-40 | plain function | function_argument | terse | without | late | path_containment_check | Delete a user's attachment. |
| 025 | `cla_pt_go_0015` | CWE-22 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | descriptive | without | - | - | Shorten a long name with an ellipsis. |

</details>
