# P06_gemini_c · batch 1 of 10 (10 rows)

**Model:** Gemini (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P06_gemini_c/replies/<row_no>.json` (for example `001.json`).

## Row 001 · `gem_cmdi_c_0013` · CWE-78 · hard_negative

```text
Write one C function for this task: Run a unit conversion script on a value.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: all_arguments_shell_quoted (every argument properly shell-quoted for the context it is used in). Input comes from: file content.
Make it about 15 lines long (target band 11-20 lines), written as callback passed as a function pointer.
Preferred call family: popen. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 002 · `gem_cmdi_c_0010` · CWE-78 · normal

```text
Write one C function for this task: Show the mount information of a device.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 4 lines long (target band 1-5 lines), written as command line tool function (uses argc and argv values).
Preferred call family: execl through sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 003 · `gem_sqli_c_0016` · CWE-89 · hard_positive

```text
Write one C function for this task: Count signups per day for a date range.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: handwritten_escaping (hand-written escaping of quotes that does not cover every case). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as request handler that receives a struct or buffer.
Preferred call family: PQexec. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 004 · `gem_pt_c_0013` · CWE-22 · hard_positive

```text
Write one C function for this task: Serve a PDF from the document library.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: check_before_normalising (the check is done before the path is normalised). Input comes from: a network message.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: rename. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: path_containment_check.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 005 · `gem_cmdi_c_0009` · CWE-78 · normal

```text
Write one C function for this task: Compress a log file after rotation.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as small embedded or library utility.
Preferred call family: execvp. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: argv_no_shell. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 006 · `gem_rnd_c_0002` · CWE-338 · normal

```text
Write one C function for this task: Pick the words of a recovery phrase for a wallet.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as request handler that receives a struct or buffer.
Preferred call family: random. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: secure_bytes_encoded.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 007 · `gem_sqli_c_0007` · CWE-89 · normal

```text
Write one C function for this task: Find the members of a team by role.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 4 lines long (target band 1-5 lines), written as command line tool function (uses argc and argv values).
Preferred call family: mysql_query. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: type_conversion.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 008 · `gem_cmdi_c_0006` · CWE-78 · safe

```text
Write one C function for this task: Restart a named system service.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 55 lines long (target band 41-100 lines), written as callback passed as a function pointer.
Preferred call family: execl through sh -c (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 009 · `gem_sqli_c_0010` · CWE-89 · normal

```text
Write one C function for this task: Insert a new product review.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 8 lines long (target band 6-10 lines), written as callback passed as a function pointer.
Preferred call family: mysql_query. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 010 · `gem_pt_c_0015` · CWE-22 · hard_positive

```text
Write one C function for this task: Move a processed file to an archive folder.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: relative_check_misses_absolute (a check for relative sequences that misses absolute paths). Input comes from: a command-line argument.
Make it about 55 lines long (target band 41-100 lines), written as command line tool function (uses argc and argv values).
Preferred call family: rename. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: base_name_only. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
