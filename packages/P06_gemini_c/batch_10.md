# P06_gemini_c · batch 10 of 10 (10 rows)

**Model:** Gemini (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P06_gemini_c/replies/<row_no>.json` (for example `001.json`).

## Row 091 · `gem_rnd_c_0020` · CWE-338 · normal

```text
Write one C function for this task: Generate a secret for a shared team calendar link.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: rand. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 092 · `gem_sqli_c_0003` · CWE-89 · normal

```text
Write one C function for this task: List recent transactions for an account sorted by amount or date.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 4 lines long (target band 1-5 lines), written as command line tool function (uses argc and argv values).
Preferred call family: PQexec. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: prepared_statement_bind.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 093 · `gem_sqli_c_0022` · CWE-89 · hard_negative

```text
Write one C function for this task: Export the orders of a given month.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: identifier_allowlist (a table or column name chosen from a fixed allow-list, values bound). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as small embedded or library utility.
Preferred call family: sqlite3_exec. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 094 · `gem_sqli_c_0011` · CWE-89 · safe

```text
Write one C function for this task: Mark a notification as read for a user.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 15 lines long (target band 11-20 lines), written as callback passed as a function pointer.
Preferred call family: sqlite3_exec (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 095 · `gem_cmdi_c_0001` · CWE-78 · safe

```text
Write one C function for this task: Query the status of a container by name.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 15 lines long (target band 11-20 lines), written as small embedded or library utility.
Preferred call family: execl through sh -c (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 096 · `gem_sqli_c_0012` · CWE-89 · normal

```text
Write one C function for this task: Get the loyalty points of a customer.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 30 lines long (target band 21-40 lines), written as small embedded or library utility.
Preferred call family: PQexec. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: prepared_statement_bind. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 097 · `gem_rnd_c_0022` · CWE-338 · hard_positive

```text
Write one C function for this task: Issue an email confirmation token.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: secure_sounding_name_weak_generator (a secure-sounding name over a weak generator). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: random. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 098 · `gem_cmdi_c_0025` · CWE-78 · safe

```text
Write one C function for this task: Trace the network route to a host.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (uses argc and argv values).
Preferred call family: execl through sh -c (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 099 · `gem_sqli_c_0018` · CWE-89 · hard_negative

```text
Write one C function for this task: List a user's orders with a given status.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: placeholders_only_format (a formatted string that contains only placeholders). Input comes from: a function argument.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: mysql_query. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 100 · `gem_rnd_c_0018` · CWE-338 · hard_positive

```text
Write one C function for this task: Generate a pairing code for a device.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: weak_generator_behind_helper (the weak generator is hidden behind a helper function). Input comes from: not applicable: the function takes no untrusted input.
Make it about 55 lines long (target band 41-100 lines), written as small embedded or library utility.
Preferred call family: rand. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
