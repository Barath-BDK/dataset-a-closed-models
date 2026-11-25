# For the lead / owner only (contributors do not need this file)

The checking of the labels with scripts is done once by the lead, not by each person:

```bash
python tools/assemble.py <package> --generator "<exact model name>"   # builds the 30-column file + qa_report.md from the .txt
python tools/make_judge_prompts.py <package>                          # Claude label pass prompts (see prompts/CLAUDE_JUDGE_PROMPT.md)
python tools/apply_judge.py <package> --judge-version "<claude version>"
python tools/validate.py <package>                                    # counts and format check
```

Also: fill `config.yml`; the packages merge into one Excel or JSON Lines file per model (see section 10 of the specification: pilot of 48 rows, then batches of about 200, then the final files and count table). Where possible the labels should also be tested by running the code with a harmless attack (section 8 of the specification).


## Checklist per package after its pull request is merged

- [ ] `python tools/assemble.py <package> --generator "<exact model name>"`: QA report has no rows left to generate again
- [ ] Labels verified (section 8 of the specification): `label_source` set for every row
- [ ] Final Claude pass done (`tools/make_judge_prompts.py`, `tools/apply_judge.py`): `label_confidence` set; every disagreement re-checked by a person
- [ ] `python tools/validate.py <package>` shows no errors

## Repository administration

- Create repo, labels and issues: `tools/create_github.ps1`.
- Issues: one per part (10 prompts, the prompts are in the issue). `tools/make_part_issues.py` builds the texts (data in `data/briefs.jsonl`), `tools/create_part_issues.py` creates/edits them on GitHub (resumable; `--close-old` closes the old Step 2/3 issues #1-#15).
- `main` is protected (pull request required). Each person has ONE pull request `dev/<user>` -> `main` opened after Part 1 and kept open; check Part 1 there, then merge it when they write ALL DONE (use a merge commit, not squash).
