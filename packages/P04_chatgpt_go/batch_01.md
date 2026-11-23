# P04_chatgpt_go · batch 1 of 10 (10 rows)

**Model:** ChatGPT (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P04_chatgpt_go/replies/<row_no>.json` (for example `001.json`).

## Row 001 · `gpt_sqli_go_0006` · CWE-89 · hard_negative

```text
Write one Go function for this task: Search products whose name contains a keyword.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: placeholder_list_for_in (a placeholder list generated to match the length of a list, values bound). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as method on a struct.
Preferred call family: database/sql QueryRow. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 002 · `gpt_sqli_go_0016` · CWE-89 · safe

```text
Write one Go function for this task: Report order totals grouped by a chosen category.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: gorm Raw (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 003 · `gpt_pt_go_0020` · CWE-22 · normal

```text
Write one Go function for this task: Move a processed file to an archive folder.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 4 lines long (target band 1-5 lines), written as plain function.
Preferred call family: os.Create. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: path_containment_check.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 004 · `gpt_rnd_go_0024` · CWE-338 · normal

```text
Write one Go function for this task: Create a share link secret for a document.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: math/rand. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: secure_bytes_encoded. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 005 · `gpt_pt_go_0001` · CWE-22 · hard_positive

```text
Write one Go function for this task: Return a preview of a stored image.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: check_before_normalising (the check is done before the path is normalised). Input comes from: a database value.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: os.ReadFile. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 006 · `gpt_pt_go_0019` · CWE-22 · hard_positive

```text
Write one Go function for this task: Extract the entries of an uploaded archive into a folder.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: single_pass_parent_removal (a single-pass removal of parent-directory sequences). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: http.ServeFile. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: base_name_only.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 007 · `gpt_pt_go_0003` · CWE-22 · hard_negative

```text
Write one Go function for this task: Load a configuration file for a named profile.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: library_confined_access (a library call that confines access to one folder). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: os.ReadFile. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 008 · `gpt_pt_go_0022` · CWE-22 · safe

```text
Write one Go function for this task: Fetch a user's uploaded resume.
It must be safe, written the standard way for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 8 lines long (target band 6-10 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: archive extraction (archive/zip) (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 009 · `gpt_rnd_go_0023` · CWE-338 · hard_positive

```text
Write one Go function for this task: Issue a short-lived upload key.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: weak_value_hashed (a weak random value that is hashed afterwards). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: math/rand. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 010 · `gpt_pt_go_0025` · CWE-22 · hard_positive

```text
Write one Go function for this task: Return the modification time of a stored file.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: extension_check_only (only the file extension is checked). Input comes from: a function argument.
Make it about 15 lines long (target band 11-20 lines), written as method on a struct.
Preferred call family: os.Open. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list_mapping.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
