# Final label pass with Claude (section 8.1 of the specification)

Every row, from every model, goes to Claude once for a final judgement, so all rows have the same final reviewer.

- Use **one fixed Claude version for the whole dataset** (see `config.yml`) and a **new chat for every 10 rows**.
- Give Claude only the language, the weakness and the numbered code. **Not** the current label, **not** the model that wrote the row, **not** `fixed_code`.
- `python tools/make_judge_prompts.py <package>` writes these prompts for you, ten per file.

## The prompt (one per row)

```text
Here is a [LANGUAGE] function. Lines are numbered.
[NUMBERED CODE]
Question: is this function vulnerable to [WEAKNESS NAME] ([CWE])?
Reply with JSON only:
{"verdict": "vulnerable" or "safe",
 "vulnerable_lines": [line numbers, empty if safe],
 "reason": "one sentence"}
```

## What to do with the verdict (`python tools/apply_judge.py <package> --judge-version "claude-<version>"` does this)

| Check result | Claude agrees? | What to do |
|---|---|---|
| `dynamic_exploit` passed | yes | keep; `label_confidence` = `high` |
| `two_reviewers` or `by_design` | yes | keep; `label_confidence` = `medium` |
| any | no | **a person re-checks the row.** If the person confirms the original label, keep it as `medium` and note the disagreement; otherwise fix the label or drop the row |

- If Claude's `vulnerable_lines` differ from the row's, a person decides which lines are right.
- Write Claude's verdict and version in `notes`, for example `judge: claude-<version> agrees`.
- For rows that Claude itself wrote, a person re-checks every row where Claude agrees with its own label but no execution check was possible, because a model tends to agree with its own output.
- Claude is a final check, not a replacement for running the code: it can be wrong, so its verdict alone never sets `high`.
