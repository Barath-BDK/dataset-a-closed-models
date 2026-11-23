# P05_gemini_python · batch 1 of 10 (10 rows)

**Model:** Gemini (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P05_gemini_python/replies/<row_no>.json` (for example `001.json`).

## Row 001 · `gem_pt_py_0022` · CWE-22 · hard_negative

```text
Write one Python function for this task: Remove an old export file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: library_confined_access (a library call that confines access to one folder). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: archive extraction (zipfile or tarfile). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 002 · `gem_rnd_py_0017` · CWE-338 · safe

```text
Write one Python function for this task: Issue an API key for a new client.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as class method (write the method alone, with self).
Preferred call family: the secure source of the language (secrets, os.urandom or random.SystemRandom). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 003 · `gem_pt_py_0024` · CWE-22 · safe

```text
Write one Python function for this task: Report the size of a stored file.
It must be safe, written the standard way for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.remove (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 004 · `gem_sqli_py_0010` · CWE-89 · normal

```text
Write one Python function for this task: Count signups per day for a date range.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, with self).
Preferred call family: MySQL driver (PyMySQL or mysql-connector). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 005 · `gem_sqli_py_0016` · CWE-89 · hard_negative

```text
Write one Python function for this task: Find all students enrolled in a course.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: constant_fragments_only (a query assembled from constant fragments only, values bound). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as class method (write the method alone, with self).
Preferred call family: Django raw(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 006 · `gem_sqli_py_0001` · CWE-89 · normal

```text
Write one Python function for this task: Export the orders of a given month.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as async function or callback.
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 007 · `gem_sqli_py_0013` · CWE-89 · hard_negative

```text
Write one Python function for this task: Find events happening in a given city.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: bound_via_builder (values bound through a query builder, an ORM or a prepared statement API). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 008 · `gem_cmdi_py_0004` · CWE-78 · hard_positive

```text
Write one Python function for this task: Run a unit conversion script on a value.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: quoting_in_wrong_context (quoting applied in the wrong context). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: subprocess.Popen with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: strict_validation.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 009 · `gem_pt_py_0011` · CWE-22 · hard_positive

```text
Write one Python function for this task: Open a certificate file by name.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: check_before_normalising (the check is done before the path is normalised). Input comes from: a database value.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: os.remove. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 010 · `gem_sqli_py_0007` · CWE-89 · hard_positive

```text
Write one Python function for this task: Mark a notification as read for a user.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: keyword_blocklist (a blocklist of SQL keywords or characters). Input comes from: file content.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: psycopg2. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
