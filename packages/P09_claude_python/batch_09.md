# P09_claude_python · batch 9 of 10 (10 rows)

**Model:** Claude (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P09_claude_python/replies/<row_no>.json` (for example `001.json`).

## Row 081 · `cla_sqli_py_0019` · CWE-89 · hard_negative

```text
Write one Python function for this task: Return the latest comments on a post.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: placeholder_list_for_in (a placeholder list generated to match the length of a list, values bound). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 082 · `cla_cmdi_py_0001` · CWE-78 · hard_positive

```text
Write one Python function for this task: Execute a report generator with a chosen template.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: quoting_in_wrong_context (quoting applied in the wrong context). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 083 · `cla_sqli_py_0004` · CWE-89 · safe

```text
Write one Python function for this task: Transfer a balance between two accounts inside a transaction.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: psycopg2 (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 084 · `cla_sqli_py_0020` · CWE-89 · hard_positive

```text
Write one Python function for this task: List a user's orders with a given status.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: bound_but_input_identifier (values are bound, but a table name or sort column comes from the input). Input comes from: a network message.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: MySQL driver (PyMySQL or mysql-connector). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: type_conversion.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 085 · `cla_cmdi_py_0015` · CWE-78 · normal

```text
Write one Python function for this task: Create a snapshot of a virtual machine by name.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as class method (write the method alone, with self).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 086 · `cla_cmdi_py_0018` · CWE-78 · hard_positive

```text
Write one Python function for this task: Send a document to a named printer.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: validation_of_other_variable (validation applied to a different variable from the one actually used). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as async function or callback.
Preferred call family: os.popen. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 087 · `cla_rnd_py_0022` · CWE-338 · normal

```text
Write one Python function for this task: Create an invite code for a team.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: random.randint. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 088 · `cla_pt_py_0016` · CWE-22 · normal

```text
Write one Python function for this task: Serve a PDF from the document library.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 4 lines long (target band 1-5 lines), written as plain function.
Preferred call family: send_file. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 089 · `cla_pt_py_0001` · CWE-22 · hard_negative

```text
Write one Python function for this task: Load a configuration file for a named profile.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: base_name_only (only the base name of the input is used). Input comes from: a command-line argument.
Make it about 55 lines long (target band 41-100 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: shutil.copy. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 090 · `cla_sqli_py_0012` · CWE-89 · normal

```text
Write one Python function for this task: Check a username and password hash for a login.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 8 lines long (target band 6-10 lines), written as async function or callback.
Preferred call family: psycopg2. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
