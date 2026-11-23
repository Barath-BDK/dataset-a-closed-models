# P09_claude_python · batch 6 of 10 (10 rows)

**Model:** Claude (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P09_claude_python/replies/<row_no>.json` (for example `001.json`).

## Row 051 · `cla_pt_py_0020` · CWE-22 · hard_negative

```text
Write one Python function for this task: Unzip a theme package into the themes folder.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: id_mapped_to_known_file (an identifier is mapped to a known file name). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: open. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 052 · `cla_cmdi_py_0010` · CWE-78 · normal

```text
Write one Python function for this task: Run a database backup tool for one schema.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 4 lines long (target band 1-5 lines), written as class method (write the method alone, with self).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 053 · `cla_rnd_py_0014` · CWE-338 · no_code

```text
Write one Python function for this task: Format a recovery code list for printing.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 054 · `cla_rnd_py_0013` · CWE-338 · safe

```text
Write one Python function for this task: Generate a one-time login link token.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 55 lines long (target band 41-100 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: the secure source of the language (secrets, os.urandom or random.SystemRandom). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 055 · `cla_cmdi_py_0011` · CWE-78 · safe

```text
Write one Python function for this task: Unpack an uploaded archive into a working folder.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: os.popen (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 056 · `cla_pt_py_0009` · CWE-22 · hard_negative

```text
Write one Python function for this task: Save a note under a given name.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: safe_filename_helper_fixed_folder (a safe-filename helper combined with a fixed folder). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: open. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 057 · `cla_sqli_py_0007` · CWE-89 · hard_positive

```text
Write one Python function for this task: Fetch an invoice by its number.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: handwritten_escaping (hand-written escaping of quotes that does not cover every case). Input comes from: a network message.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 058 · `cla_rnd_py_0015` · CWE-338 · hard_positive

```text
Write one Python function for this task: Pick the words of a recovery phrase for a wallet.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: secure_sounding_name_weak_generator (a secure-sounding name over a weak generator). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: random.randint. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 059 · `cla_cmdi_py_0016` · CWE-78 · hard_negative

```text
Write one Python function for this task: Start a background job from a script name.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: strict_parser_then_no_shell (input checked by a strict parser (for example an IP address parser) and passed without a shell). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 060 · `cla_sqli_py_0001` · CWE-89 · normal

```text
Write one Python function for this task: Remove a product from a wishlist.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
