# P11_claude_cpp · batch 7 of 10 (10 rows)

**Model:** Claude (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P11_claude_cpp/replies/<row_no>.json` (for example `001.json`).

## Row 061 · `cla_cmdi_cpp_0001` · CWE-78 · hard_negative

```text
Write one C++ function for this task: Extract a thumbnail frame from a video file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: all_arguments_shell_quoted (every argument properly shell-quoted for the context it is used in). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: system. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 062 · `cla_sqli_cpp_0012` · CWE-89 · normal

```text
Write one C++ function for this task: Fetch an invoice by its number.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as helper called by another function.
Preferred call family: Qt QSqlQuery. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: query_builder_bind.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 063 · `cla_rnd_cpp_0015` · CWE-338 · safe

```text
Write one C++ function for this task: Issue a device registration token.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as web or network handler that receives a request object.
Preferred call family: the secure source of the language (std::random_device or /dev/urandom). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 064 · `cla_rnd_cpp_0011` · CWE-338 · hard_positive

```text
Write one C++ function for this task: Issue an email confirmation token.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: weak_generator_behind_helper (the weak generator is hidden behind a helper function). Input comes from: not applicable: the function takes no untrusted input.
Make it about 55 lines long (target band 41-100 lines), written as class method (write the method alone, as Class::method).
Preferred call family: std::default_random_engine. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 065 · `cla_cmdi_cpp_0013` · CWE-78 · hard_positive

```text
Write one C++ function for this task: Search a log file for lines containing a term.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: partial_shell_character_filter (a filter that removes or rejects only some shell characters). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as class method (write the method alone, as Class::method).
Preferred call family: Boost.Process. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 066 · `cla_sqli_cpp_0019` · CWE-89 · no_code

```text
Write one C++ function for this task: Parse a CSV line into fields.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as web or network handler that receives a request object.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 067 · `cla_rnd_cpp_0016` · CWE-338 · no_code

```text
Write one C++ function for this task: Compute the check digit of a number.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as callback, lambda or asynchronous task.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 068 · `cla_sqli_cpp_0025` · CWE-89 · safe

```text
Write one C++ function for this task: Fetch the configuration value for a given key and environment.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web or network handler that receives a request object.
Preferred call family: Qt QSqlQuery (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 069 · `cla_rnd_cpp_0001` · CWE-338 · normal

```text
Write one C++ function for this task: Create a session identifier for a signed-in user.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as command line tool function (uses argc and argv values).
Preferred call family: rand. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: secure_generator_api.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 070 · `cla_pt_cpp_0012` · CWE-22 · hard_positive

```text
Write one C++ function for this task: Read a data file for a selected report.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: extension_check_only (only the file extension is checked). Input comes from: an environment variable.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: fopen. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: base_name_only. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
