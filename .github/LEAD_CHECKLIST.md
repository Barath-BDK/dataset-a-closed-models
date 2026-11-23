# Lead checklist (after a contributor's pull request is merged)

- [ ] `python tools/assemble.py <package> --generator "<exact model name>"`: QA report has no rows left to generate again
- [ ] Labels verified (section 8 of the specification): `label_source` set for every row
- [ ] Final Claude pass done (`tools/make_judge_prompts.py`, `tools/apply_judge.py`): `label_confidence` set; every disagreement re-checked by a person
- [ ] `python tools/validate.py <package>` shows no errors
