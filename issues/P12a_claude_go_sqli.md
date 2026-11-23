## 🟦 STEP 3 of 3: extra package

**Assigned to: vinoth96-hub.** Do this after your other steps. All 25 rows (Claude × Go × CWE-89).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P12a_claude_go_sqli.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P12a_claude_go_sqli.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P12a_claude_go_sqli.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P12a_claude_go_sqli.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Issue branch `issue/<this issue number>-P12a_claude_go_sqli` made from your personal branch `dev/vinoth96-hub` (after the earlier steps are merged)
- [ ] Prompts for rows 001-025 pasted into Claude (new chat for every 10 rows, master prompt first); every answer pasted under its `=== NNN` line in `submissions/P12a_claude_go_sqli.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into `dev/vinoth96-hub` with **only** `submissions/P12a_claude_go_sqli.txt`; the exact model name in the description
- [ ] After approval: merged into `dev/vinoth96-hub`; when all your steps are merged, one last pull request `dev/vinoth96-hub` into `main`

Mix of rows: normal 8, hard_positive 4, hard_negative 7, no_code 2, safe 4.

<details><summary>Table of the rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_sqli_go_0019` | CWE-89 | normal | `plain` | gorm Raw | 41-100 | helper called by another function | web_request | descriptive | without | early | query_builder | Look up a city by postal code. |
| 002 | `cla_sqli_go_0001` | CWE-89 | normal | `plain` | database/sql QueryRow | 1-5 | method on a struct | database_value | terse | with | middle | bound_parameters | Insert a new product review. |
| 003 | `cla_sqli_go_0015` | CWE-89 | normal | `plain` | database/sql Exec | 6-10 | goroutine or callback | web_request | terse | with | late | allow_list | Find books by author name. |
| 004 | `cla_sqli_go_0011` | CWE-89 | hard_positive | `bound_but_input_identifier` | database/sql Query | 6-10 | method on a struct | network_message | descriptive | without | late | type_conversion | Get the loyalty points of a customer. |
| 005 | `cla_sqli_go_0023` | CWE-89 | hard_positive | `handwritten_escaping` | gorm Raw | 21-40 | helper called by another function | network_message | descriptive | with | middle | query_builder | Count signups per day for a date range. |
| 006 | `cla_sqli_go_0004` | CWE-89 | hard_positive | `bound_but_input_identifier` | database/sql QueryRow | 6-10 | method on a struct | command_line | descriptive | with | late | type_conversion | Mark a notification as read for a user. |
| 007 | `cla_sqli_go_0018` | CWE-89 | hard_negative | `integer_forced` | database/sql QueryRow | 6-10 | command line tool function | command_line | descriptive | without | - | - | Delete expired sessions older than a number of days. |
| 008 | `cla_sqli_go_0016` | CWE-89 | no_code | `plain` | none | 11-20 | HTTP handler | not_applicable | descriptive | with | - | - | Merge two lists without duplicates. |
| 009 | `cla_sqli_go_0013` | CWE-89 | normal | `plain` | sqlx | 11-20 | HTTP handler | web_request | descriptive | with | early | type_conversion | Find a customer record by email address. |
| 010 | `cla_sqli_go_0008` | CWE-89 | normal | `plain` | sqlx | 6-10 | command line tool function | command_line | descriptive | with | middle | bound_parameters | Find a vehicle by its registration number. |
| 011 | `cla_sqli_go_0017` | CWE-89 | normal | `plain` | sqlx | 1-5 | plain function | web_request | terse | without | early | type_conversion | Return the stock quantity for a product code. |
| 012 | `cla_sqli_go_0022` | CWE-89 | hard_negative | `bound_via_builder` | sqlx | 6-10 | helper called by another function | web_request | terse | without | - | - | List recent transactions for an account sorted by amount or date. |
| 013 | `cla_sqli_go_0009` | CWE-89 | normal | `plain` | gorm Raw | 11-20 | method on a struct | web_request | terse | with | early | query_builder | Find all accounts created through an affiliate code. |
| 014 | `cla_sqli_go_0020` | CWE-89 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | terse | without | - | - | Format an order total with tax and currency. |
| 015 | `cla_sqli_go_0002` | CWE-89 | safe | `plain` | gorm Raw | 21-40 | plain function | function_argument | terse | with | - | - | Check a username and password hash for a login. |
| 016 | `cla_sqli_go_0014` | CWE-89 | hard_negative | `placeholder_list_for_in` | database/sql Query | 21-40 | helper called by another function | file | terse | without | - | - | Find all accounts created through an affiliate code. |
| 017 | `cla_sqli_go_0010` | CWE-89 | hard_negative | `placeholders_only_format` | database/sql Query | 6-10 | plain function | command_line | terse | with | - | - | Find articles that carry a given tag. |
| 018 | `cla_sqli_go_0012` | CWE-89 | normal | `plain` | sqlx | 1-5 | plain function | command_line | descriptive | without | early | query_builder | Find events happening in a given city. |
| 019 | `cla_sqli_go_0005` | CWE-89 | hard_negative | `placeholder_list_for_in` | sqlx | 21-40 | plain function | function_argument | terse | with | - | - | List the most recent log entries of a service. |
| 020 | `cla_sqli_go_0025` | CWE-89 | hard_negative | `bound_via_builder` | database/sql Exec | 41-100 | method on a struct | command_line | descriptive | without | - | - | Export the orders of a given month. |
| 021 | `cla_sqli_go_0021` | CWE-89 | hard_negative | `constant_fragments_only` | database/sql Exec | 11-20 | helper called by another function | function_argument | terse | with | - | - | Find patients by surname. |
| 022 | `cla_sqli_go_0003` | CWE-89 | safe | `plain` | sqlx | 11-20 | command line tool function | command_line | terse | without | - | - | List the employees of a department. |
| 023 | `cla_sqli_go_0007` | CWE-89 | safe | `plain` | sqlx | 41-100 | goroutine or callback | network_message | terse | with | - | - | Find articles that carry a given tag. |
| 024 | `cla_sqli_go_0006` | CWE-89 | hard_positive | `one_branch_bound` | database/sql Query | 21-40 | command line tool function | command_line | terse | without | middle | allow_list | List recent transactions for an account sorted by amount or date. |
| 025 | `cla_sqli_go_0024` | CWE-89 | safe | `plain` | database/sql QueryRow | 11-20 | HTTP handler | web_request | terse | without | - | - | Search a phone book by name prefix. |

</details>
