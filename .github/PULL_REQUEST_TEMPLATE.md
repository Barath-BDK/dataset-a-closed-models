Closes #<issue number>

## Package
<!-- e.g. P05 Gemini x Python -->

## Checklist
- [ ] My base branch is my personal branch `dev/<username>` (not `main`)
- [ ] Only `submissions/<package>/` changed; no API keys or chat exports
- [ ] `python tools/assemble.py <package> --generator "<exact model>"`: the QA report has no rows left to generate again
- [ ] Every row has `label_source` and passed its check (marker-file attack run, or two reviewers, or by design)
- [ ] Final Claude pass done; every disagreement and every unrun Claude row was re-checked by a person
- [ ] `python tools/validate.py <package>` shows no errors
- [ ] No label hints in comments, names or strings; `vulnerable_lines` recounted

## Notes for the reviewer
<!-- disagreements, rows dropped, rows written with another model, anything unusual -->
