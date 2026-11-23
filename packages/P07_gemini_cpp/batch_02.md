# P07_gemini_cpp · batch 2 of 10 (10 rows)

**Model:** Gemini (use the same exact version for all batches). **New chat for this batch.** Paste `prompts/MASTER_PROMPT.md` first, wait for `ready`, then paste the prompts below one at a time. Save each reply as `submissions/P07_gemini_cpp/replies/<row_no>.json` (for example `001.json`).

## Row 011 · `gem_pt_cpp_0004` · CWE-22 · normal

```text
Write one C++ function for this task: Read the lines of a CSV import file.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: fopen. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: path_containment_check.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 012 · `gem_sqli_cpp_0024` · CWE-89 · hard_negative

```text
Write one C++ function for this task: Search products whose name contains a keyword.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: placeholders_only_format (a formatted string that contains only placeholders). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as web or network handler that receives a request object.
Preferred call family: PQexec. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 013 · `gem_pt_cpp_0005` · CWE-22 · no_code

```text
Write one C++ function for this task: Return the parent part of a path string.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, as Class::method).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 014 · `gem_pt_cpp_0006` · CWE-22 · normal

```text
Write one C++ function for this task: Truncate a log file chosen by name.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web or network handler that receives a request object.
Preferred call family: ifstream or ofstream. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list_mapping. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 015 · `gem_pt_cpp_0011` · CWE-22 · hard_negative

```text
Write one C++ function for this task: Read the first line of a stored file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: base_name_only (only the base name of the input is used). Input comes from: file content.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, as Class::method).
Preferred call family: std::remove. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 016 · `gem_rnd_cpp_0017` · CWE-338 · normal

```text
Write one C++ function for this task: Create a webhook signing secret.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: std::mt19937. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: secure_generator_api. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 017 · `gem_cmdi_cpp_0004` · CWE-78 · normal

```text
Write one C++ function for this task: Zip the contents of a folder into a named archive.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: Boost.Process. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 018 · `gem_pt_cpp_0012` · CWE-22 · hard_negative

```text
Write one C++ function for this task: Read a log file of a named service.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: resolve_then_separator_aware_check (the path is resolved first, then checked for containment with a separator-aware test). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web or network handler that receives a request object.
Preferred call family: fopen. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 019 · `gem_rnd_cpp_0022` · CWE-338 · hard_negative

```text
Write one C++ function for this task: Estimate pi with a Monte Carlo simulation.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: ordinary_random_simulation (ordinary random used in a simulation (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as callback, lambda or asynchronous task.
Preferred call family: std::default_random_engine. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

## Row 020 · `gem_pt_cpp_0003` · CWE-22 · normal

```text
Write one C++ function for this task: Return the modification time of a stored file.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as callback, lambda or asynchronous task.
Preferred call family: ifstream or ofstream. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: base_name_only. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```
