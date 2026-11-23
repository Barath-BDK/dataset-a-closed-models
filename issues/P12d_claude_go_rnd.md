## Your job

Write **25 rows** with **Claude** (free base model) in **Go** (CWE-338).

| | |
|---|---|
| **Your prompts (one file)** | [`MY_PROMPTS/P12d_claude_go_rnd.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/P12d_claude_go_rnd.md) |
| **Your hand-in file (the only file you hand in)** | [`submissions/P12d_claude_go_rnd.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P12d_claude_go_rnd.txt) |
| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |
| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |

### Steps (tick them in your pull request)

- [ ] Personal branch `dev/<your-github-username>` made from `main`; issue branch `issue/<number>-P12d_claude_go_rnd` made from your personal branch
- [ ] All 25 prompts pasted into Claude (new chat for every 10 rows, master prompt first) and every answer pasted under its `=== NNN` line in `submissions/P12d_claude_go_rnd.txt`
- [ ] Check A done with Claude (rules); every REDO row generated again
- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)
- [ ] Pull request from the issue branch into your personal branch with **only** `submissions/P12d_claude_go_rnd.txt`; the exact model name written in the description
- [ ] After approval: merged into your personal branch, then one last pull request `dev/<your-github-username>` into `main`

Mix of rows in this package: normal 8, hard_positive 4, safe 4, hard_negative 7, no_code 2. Lengths: 1-5: 4, 6-10: 7, 11-20: 8, 21-40: 2, 41-100: 4.

<details><summary>Table of all rows (for reference; the prompts already contain all of this)</summary>

| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | `cla_rnd_go_0015` | CWE-338 | hard_positive | `secure_sounding_name_weak_generator` | math/rand | 6-10 | method on a struct | not_applicable | terse | with | late | secure_bytes_encoded | Create a nonce for a content security policy header. |
| 002 | `cla_rnd_go_0001` | CWE-338 | normal | `plain` | math/rand | 1-5 | method on a struct | not_applicable | terse | with | early | rejection_sampling_secure_index | Generate a session key for an encrypted chat. |
| 003 | `cla_rnd_go_0014` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | math/rand | 6-10 | goroutine or callback | not_applicable | terse | without | - | - | Generate a nonce for a signed request. |
| 004 | `cla_rnd_go_0010` | CWE-338 | hard_negative | `secure_secret_plus_ordinary_random_elsewhere` | math/rand | 11-20 | command line tool function | not_applicable | terse | without | - | - | Create a salt for hashing a password. |
| 005 | `cla_rnd_go_0021` | CWE-338 | normal | `plain` | math/rand | 1-5 | HTTP handler | not_applicable | descriptive | without | middle | rejection_sampling_secure_index | Create a private link token for a quiz. |
| 006 | `cla_rnd_go_0002` | CWE-338 | safe | `plain` | math/rand | 6-10 | HTTP handler | not_applicable | descriptive | with | - | - | Generate a bearer token for a service account. |
| 007 | `cla_rnd_go_0005` | CWE-338 | safe | `plain` | math/rand | 6-10 | command line tool function | not_applicable | descriptive | without | - | - | Issue an API key for a new client. |
| 008 | `cla_rnd_go_0018` | CWE-338 | normal | `plain` | math/rand | 1-5 | command line tool function | not_applicable | terse | without | early | rejection_sampling_secure_index | Create a verification code for a phone number. |
| 009 | `cla_rnd_go_0009` | CWE-338 | no_code | `plain` | none | 1-5 | command line tool function | not_applicable | descriptive | without | - | - | Check that a token has the expected length and characters. |
| 010 | `cla_rnd_go_0007` | CWE-338 | safe | `plain` | math/rand | 11-20 | HTTP handler | not_applicable | terse | with | - | - | Generate a license key for a software installation. |
| 011 | `cla_rnd_go_0019` | CWE-338 | hard_negative | `ordinary_random_simulation` | math/rand | 6-10 | command line tool function | not_applicable | terse | with | - | - | Simulate customer arrivals at a shop with random gaps between them. |
| 012 | `cla_rnd_go_0003` | CWE-338 | hard_negative | `ordinary_random_sampling` | math/rand | 11-20 | HTTP handler | not_applicable | descriptive | with | - | - | Pick a random sample of users for a satisfaction survey. |
| 013 | `cla_rnd_go_0025` | CWE-338 | hard_positive | `weak_value_hashed` | math/rand | 21-40 | plain function | not_applicable | descriptive | with | late | secure_generator_api | Generate a PIN for a card activation. |
| 014 | `cla_rnd_go_0013` | CWE-338 | hard_negative | `ordinary_random_games` | math/rand | 41-100 | plain function | not_applicable | descriptive | without | - | - | Roll dice for a board game. |
| 015 | `cla_rnd_go_0022` | CWE-338 | hard_negative | `ordinary_random_games` | math/rand | 21-40 | plain function | not_applicable | terse | without | - | - | Pick a random spawn position for an enemy in a game. |
| 016 | `cla_rnd_go_0023` | CWE-338 | no_code | `plain` | none | 11-20 | plain function | not_applicable | descriptive | without | - | - | Compute the entropy of a value from its length and alphabet size. |
| 017 | `cla_rnd_go_0008` | CWE-338 | hard_positive | `weak_generator_behind_helper` | math/rand | 11-20 | goroutine or callback | not_applicable | terse | with | middle | secure_generator_api | Issue a gift card code with a check value. |
| 018 | `cla_rnd_go_0024` | CWE-338 | hard_negative | `ordinary_random_sampling` | math/rand | 11-20 | HTTP handler | not_applicable | descriptive | without | - | - | Choose which products to feature on the home page. |
| 019 | `cla_rnd_go_0012` | CWE-338 | normal | `plain` | math/rand | 41-100 | command line tool function | not_applicable | terse | without | middle | secure_generator_api | Create a password for a guest Wi-Fi voucher. |
| 020 | `cla_rnd_go_0020` | CWE-338 | safe | `plain` | math/rand | 41-100 | command line tool function | not_applicable | descriptive | without | - | - | Create a session identifier for a signed-in user. |
| 021 | `cla_rnd_go_0004` | CWE-338 | hard_positive | `weak_generator_behind_helper` | math/rand | 6-10 | plain function | not_applicable | descriptive | with | early | rejection_sampling_secure_index | Generate a one-time voucher for a refund. |
| 022 | `cla_rnd_go_0011` | CWE-338 | normal | `plain` | math/rand | 41-100 | helper called by another function | not_applicable | terse | with | early | secure_generator_api | Generate a PIN for a card activation. |
| 023 | `cla_rnd_go_0006` | CWE-338 | normal | `plain` | math/rand | 11-20 | method on a struct | not_applicable | terse | with | middle | rejection_sampling_secure_index | Create an OAuth state value for a login redirect. |
| 024 | `cla_rnd_go_0017` | CWE-338 | normal | `plain` | math/rand | 6-10 | plain function | not_applicable | descriptive | without | late | secure_bytes_encoded | Generate an access token for a mobile app. |
| 025 | `cla_rnd_go_0016` | CWE-338 | normal | `plain` | math/rand | 11-20 | plain function | not_applicable | descriptive | with | late | secure_generator_api | Issue an invitation link token. |

</details>
