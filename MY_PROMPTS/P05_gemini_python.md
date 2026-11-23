# P05 · Gemini · Python · 100 prompts

> **This one file has everything you need to paste.** Your answers go into ONE other file: [`submissions/P05_gemini_python.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P05_gemini_python.txt).

## What to do (the short version)

1. Open **Gemini** (the free base model). Start a **new chat**.
2. Copy the **MASTER PROMPT** below (the copy button is in the top right corner of the box) and paste it into the chat. Wait until the model answers `ready`.
3. Copy **ROW 001**, paste it into the chat. The model answers with a block of JSON.
4. Copy the whole answer and paste it into `submissions/P05_gemini_python.txt` **under the line `=== 001`**.
5. Do the same for the next rows. **After 10 rows, start a new chat** and paste the MASTER PROMPT again (the file tells you where).

**Order:** first do the **STEP 1 warm-up (rows 001 to 005, five prompts)** and hand it in, so the lead can tell you if you are doing it right. Only then do the rest (STEP 2).
6. When you finish, check your answers with Claude (see the README, step 5) and hand in the one file.

Do not change the model's answer. Do not leave out rows. If a row goes wrong, ask the same row again in a new chat and replace the answer.

---

## MASTER PROMPT (paste this first in every new chat)

````text
You are helping to build a training dataset for a research project that teaches software tools to detect, locate and repair security weaknesses in source code. The code you write is used defensively, to train and test vulnerability detectors. It will never be deployed or run against any real system. Write realistic code of the kind found in real programs.

I will send you one task at a time. For each task, reply with ONE JSON object and nothing else.

## What a reply is
Exactly one JSON object, no text before or after it, no explanation, with these eight keys:
- "code": the function, as one string, with its original indentation and line breaks written as \n.
- "fixed_code": the same function made safe. Only for vulnerable rows (see below). An empty string "" for every other row.
- "vulnerable_lines": a JSON list of line numbers of "code", counted from 1 (the first line of the function is line 1), for example [3, 5, 6]. Only for vulnerable rows. An empty list [] for every other row.
- "task_description": one natural sentence saying what the function does. No hint of whether it is safe or vulnerable.
- "sink": the call in your code that is the dangerous call (or the safe call used in its place), for example "cursor.execute" or "fopen". Empty string for code without such a call.
- "build_style": how the dangerous value is built, for example "concatenation", "f_string", "path_join", "snprintf", "libc_rand". "none" for code without a dangerous call.
- "fix_type": the kind of fix used in fixed_code, as named in the task. An empty string for rows without a fix.
- "cwe_detail": the operation or variant involved, for example "rename", "sqlite3", "hex", "subprocess". "none" if not applicable.

## The four weaknesses
- CWE-89 SQL injection: untrusted input becomes part of the text of an SQL statement.
- CWE-78 OS command injection: untrusted input can change which command or shell syntax is executed.
- CWE-22 Path traversal: untrusted input can make a file operation reach outside the intended folder.
- CWE-338 Weak random generator: a non-cryptographic random generator produces a security value (token, password, key, one-time code, session id, salt, reset code).

## The five kinds of row (the task tells you which one)
- plainly vulnerable (label 1): the function has the weakness. Give fixed_code and vulnerable_lines.
- protected in a way that looks correct but fails (label 1): there is a check, filter, escape or similar that looks right, but the function is still vulnerable. A careful reader must be able to show how it fails. Give fixed_code and vulnerable_lines.
- safe, written the standard way (label 0): no weakness. fixed_code "" and vulnerable_lines [].
- completely safe, while using the dangerous call or looking like the vulnerable form (label 0): really safe, but a quick reader might think it is not. For CWE-338 this includes ordinary random used for something harmless (simulation, shuffling, sampling, retry jitter, games, test data, a fixed seed for a reproducible experiment). fixed_code "" and vulnerable_lines [].
- ordinary code from the same kind of program that does not use any dangerous call for this weakness (label 0). fixed_code "", vulnerable_lines [], sink "", build_style "none".

## Rules for every reply
1. ONE complete function in the language asked for. A method is written alone, as the method. No main program, no includes or imports outside the function (in Python put imports inside the function body; in C, C++ and Go assume the usual headers or imports exist and do not write them). Never more than one function. No helper functions after it.
2. The function must stand alone: do not call helper functions that are not defined or imported inside it, especially for the part that makes it safe or vulnerable. Write that logic inside the function.
3. Follow the task exactly: pattern, where the input comes from, call family, program shape, names (descriptive = full words, terse = short names), comments, where the flaw sits, fix type. If the call family does not fit the task, use the closest natural call of the same kind.
4. Length: aim for the number of lines the task asks for (count the signature, blank lines and every other line). It is better to be a few lines off than to pad. Never add code after a return, break or throw, never repeat statements, never add empty comments. To write a longer function add real logic around the task: input validation, a loop over several items, error handling, logging, building a result, a second step inside the same function.
5. Comments: if the task says comments, write a few plain comment lines or a docstring that explain what the code does. If it says none, write no comments and no docstring at all.
6. fixed_code changes as few lines as possible, at most 10, keeps the same function name, signature and behaviour for normal input, and really removes the weakness. Find EVERY place where the untrusted value reaches the dangerous call and cover each one. Use the standard library or the library the task names, not unusual extra packages. Do not rewrite the function.
7. vulnerable_lines: first number the lines of "code" from 1, then list the lines that build the dangerous value, any faulty check that is meant to protect it, and the line that uses it in the dangerous call. Not the whole function. Check each number against your numbering before you answer.
8. Never write any comment, name, string or message that says or hints whether the code is safe or vulnerable. Forbidden words in code, comments, names and strings: vulnerable, insecure, unsafe, safe, secure (as a label), fixed, bug, attack, exploit, injection, sanitize. Do not write attack strings, payloads or exploit steps.
9. Make every function different: different names, structure and logic. Do not reuse the same layout from one answer to the next in this chat.

## Check before you answer (silently, every time)
- One function only, nothing after a return, line count close to the target?
- Comments exactly as the task says?
- For vulnerable rows: does fixed_code cover every use of the untrusted value, change at most 10 lines and keep the signature? Do the numbers in vulnerable_lines match your numbering of "code"?
- Does "sink" appear in "code"? No label-revealing words anywhere?
- The reply is only one JSON object.

If you understand, reply only with: ready
````

---

# 🟩 STEP 1: WARM-UP CHAT. DO THIS FIRST (rows 001 to 005, only 5 prompts)

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → paste these 5 rows one by one → paste each answer into your hand-in file.** Then do the warm-up pull request (README, section 3) and wait for the lead's reply before you continue with CHAT 2.

### ▶ ROW 001 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 001`

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

### ▶ ROW 002 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; safe
Save the answer under `=== 002`

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

### ▶ ROW 003 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; safe
Save the answer under `=== 003`

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

### ▶ ROW 004 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 004`

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

### ▶ ROW 005 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 005`

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

---

# 🟦 STEP 2: CHAT 1 of 10: rows 006 to 015

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 006 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 006`

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

### ▶ ROW 007 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 007`

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

### ▶ ROW 008 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 008`

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

### ▶ ROW 009 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 009`

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

### ▶ ROW 010 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 010`

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

### ▶ ROW 011 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 011`

```text
Write one Python function for this task: Show the fingerprint of an ssh key file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: argument_list_with_user_data (an argument-list call with user data as separate arguments and no shell). Input comes from: a function argument.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: subprocess.Popen with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 012 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 012`

```text
Write one Python function for this task: List a user's orders with a given status.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: handwritten_escaping (hand-written escaping of quotes that does not cover every case). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: Django raw(). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 013 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 013`

```text
Write one Python function for this task: Write an exported spreadsheet under a requested name.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: resolve_then_separator_aware_check (the path is resolved first, then checked for containment with a separator-aware test). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: shutil.copy. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 014 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 014`

```text
Write one Python function for this task: Create a verification code for a phone number.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as async function or callback.
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 015 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; safe
Save the answer under `=== 015`

```text
Write one Python function for this task: Move a processed file to an archive folder.
It must be safe, written the standard way for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: shutil.copy (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 2 of 10: rows 016 to 025

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 016 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; safe
Save the answer under `=== 016`

```text
Write one Python function for this task: Return the text of an uploaded file.
It must be safe, written the standard way for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 30 lines long (target band 21-40 lines), written as async function or callback.
Preferred call family: os.remove (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 017 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 017`

```text
Write one Python function for this task: Compress a log file after rotation.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 4 lines long (target band 1-5 lines), written as class method (write the method alone, with self).
Preferred call family: os.popen. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: strict_validation. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 018 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 018`

```text
Write one Python function for this task: Create a one-time code for two-factor sign in.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: secure_generator_api.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 019 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 019`

```text
Write one Python function for this task: Open a video file for streaming.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 4 lines long (target band 1-5 lines), written as plain function.
Preferred call family: send_file. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: library_confinement. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 020 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 020`

```text
Write one Python function for this task: List the employees of a department.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: identifier_allowlist (a table or column name chosen from a fixed allow-list, values bound). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as helper called by another function.
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 021 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 021`

```text
Write one Python function for this task: Find all students enrolled in a course.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: constant_fragments_only (a query assembled from constant fragments only, values bound). Input comes from: a network message.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 022 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; safe
Save the answer under `=== 022`

```text
Write one Python function for this task: Issue an invitation link token.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: the secure source of the language (secrets, os.urandom or random.SystemRandom). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 023 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 023`

```text
Write one Python function for this task: Resize an image to a requested size with an external tool.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 4 lines long (target band 1-5 lines), written as async function or callback.
Preferred call family: os.popen. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 024 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 024`

```text
Write one Python function for this task: Delete temporary files that match a name.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: open. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: base_name_only.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 025 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 025`

```text
Write one Python function for this task: Rotate the logs of one application.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 4 lines long (target band 1-5 lines), written as class method (write the method alone, with self).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: quoting. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 3 of 10: rows 026 to 035

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 026 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 026`

```text
Write one Python function for this task: Generate a PIN for a card activation.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: secure_sounding_name_weak_generator (a secure-sounding name over a weak generator). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: secure_bytes_encoded.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 027 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 027`

```text
Write one Python function for this task: Find all accounts created through an affiliate code.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: one_branch_bound (parameters in one branch but string building in another). Input comes from: a database value.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: MySQL driver (PyMySQL or mysql-connector). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: orm_query_builder.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 028 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 028`

```text
Write one Python function for this task: Estimate pi with a Monte Carlo simulation.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: ordinary_random_simulation (ordinary random used in a simulation (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, with self).
Preferred call family: random.choices. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 029 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 029`

```text
Write one Python function for this task: Pick a random spawn position for an enemy in a game.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: ordinary_random_games (ordinary random used in a game (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 030 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 030`

```text
Write one Python function for this task: Generate a nonce for a signed request.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: seed_from_clock_or_pid (the generator is seeded from the clock or the process id). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: secure_generator_api.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 031 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 031`

```text
Write one Python function for this task: Count the lines of a file with a standard tool.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 30 lines long (target band 21-40 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: os.system. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 032 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 032`

```text
Write one Python function for this task: Look up the DNS records of a host name.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: user_data_after_end_of_options (user data placed after an end-of-options marker such as --). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.popen. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 033 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 033`

```text
Write one Python function for this task: Draw the same sample every run for a reproducible experiment.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: fixed_seed_reproducible (ordinary random with a fixed seed for a reproducible experiment (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, with self).
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 034 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; no_code
Save the answer under `=== 034`

```text
Write one Python function for this task: Escape a string for display in an HTML page.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 035 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; safe
Save the answer under `=== 035`

```text
Write one Python function for this task: Set the stock quantity of a product after a delivery.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as plain function.
Preferred call family: psycopg2 (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 4 of 10: rows 036 to 045

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 036 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; no_code
Save the answer under `=== 036`

```text
Write one Python function for this task: Split a token into its prefix and body.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as helper called by another function.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 037 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 037`

```text
Write one Python function for this task: Simulate customer arrivals at a shop with random gaps between them.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: ordinary_random_simulation (ordinary random used in a simulation (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 038 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; no_code
Save the answer under `=== 038`

```text
Write one Python function for this task: Return the parent part of a path string.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 039 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 039`

```text
Write one Python function for this task: Return the contents of a shared snippet file.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: archive extraction (zipfile or tarfile). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list_mapping.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 040 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 040`

```text
Write one Python function for this task: Create a salt for hashing a password.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as async function or callback.
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: secure_generator_api. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 041 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 041`

```text
Write one Python function for this task: Create a cookie value for a remember-me login.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: seed_from_clock_or_pid (the generator is seeded from the clock or the process id). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: random.randint. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 042 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 042`

```text
Write one Python function for this task: Extract a thumbnail frame from a video file.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: subprocess.Popen with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: quoting. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 043 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 043`

```text
Write one Python function for this task: Find all accounts created through an affiliate code.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 044 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 044`

```text
Write one Python function for this task: Pack an installer from a folder with a packaging tool.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: user_data_after_end_of_options (user data placed after an end-of-options marker such as --). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: subprocess.run with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 045 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 045`

```text
Write one Python function for this task: Generate a booking confirmation code.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: secure_secret_plus_ordinary_random_elsewhere (the secret comes from a secure generator while ordinary random is used for something harmless in the same function). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 5 of 10: rows 046 to 055

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 046 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 046`

```text
Write one Python function for this task: Read a font file requested by a stylesheet.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.remove. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 047 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 047`

```text
Write one Python function for this task: Check whether a port is open on a host.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: quoting_in_wrong_context (quoting applied in the wrong context). Input comes from: a function argument.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: subprocess.run with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 048 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; no_code
Save the answer under `=== 048`

```text
Write one Python function for this task: Estimate password strength from its length.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 049 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 049`

```text
Write one Python function for this task: Store a user's avatar image.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: pathlib. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 050 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 050`

```text
Write one Python function for this task: Search a product catalogue with optional filters for price and brand.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: integer_forced (a number forced to an integer before it is formatted into the query). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 051 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 051`

```text
Write one Python function for this task: Start a background job from a script name.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: subprocess.check_output. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 052 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 052`

```text
Write one Python function for this task: Show the commit history of a repository for one author.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: subprocess.run with shell=True (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 053 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 053`

```text
Write one Python function for this task: Create a backup copy of a document.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: archive extraction (zipfile or tarfile). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list_mapping.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 054 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; no_code
Save the answer under `=== 054`

```text
Write one Python function for this task: Build a display name from first and last name.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as async function or callback.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 055 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 055`

```text
Write one Python function for this task: Load the translation file for a locale.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: safe_filename_helper_fixed_folder (a safe-filename helper combined with a fixed folder). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: shutil.copy. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 6 of 10: rows 056 to 065

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 056 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 056`

```text
Write one Python function for this task: Write a user's settings file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: resolve_then_separator_aware_check (the path is resolved first, then checked for containment with a separator-aware test). Input comes from: an environment variable.
Make it about 8 lines long (target band 6-10 lines), written as async function or callback.
Preferred call family: pathlib. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 057 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 057`

```text
Write one Python function for this task: Restart a named system service.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: subprocess.run with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 058 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 058`

```text
Write one Python function for this task: Copy a template file into a user's workspace.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: single_pass_parent_removal (a single-pass removal of parent-directory sequences). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: pathlib. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: base_name_only.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 059 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 059`

```text
Write one Python function for this task: Trace the network route to a host.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: partial_shell_character_filter (a filter that removes or rejects only some shell characters). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: subprocess.check_output. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: strict_validation. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 060 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; safe
Save the answer under `=== 060`

```text
Write one Python function for this task: Hash the contents of a stored file.
It must be safe, written the standard way for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: open (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 061 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 061`

```text
Write one Python function for this task: Read the expiry date of a certificate file.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: validator_accepts_too_much (a validator that accepts more than it appears to). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: subprocess.Popen with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 062 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 062`

```text
Write one Python function for this task: Record an audit entry for an administrator action.
It must be protected in a way that looks correct but fails, so it is still vulnerable for SQL injection (CWE-89).
Use this pattern: bound_but_input_identifier (values are bound, but a table name or sort column comes from the input). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: Django raw(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: type_conversion.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 063 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 063`

```text
Write one Python function for this task: Insert a new product review.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: type_conversion.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 064 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 064`

```text
Write one Python function for this task: Return a page of articles sorted by a column chosen by the caller.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: constant_fragments_only (a query assembled from constant fragments only, values bound). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: Django raw(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 065 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; safe
Save the answer under `=== 065`

```text
Write one Python function for this task: Generate a password reset token to email to a user.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: the secure source of the language (secrets, os.urandom or random.SystemRandom). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 7 of 10: rows 066 to 075

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 066 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 066`

```text
Write one Python function for this task: Compute a retry delay with random jitter so clients do not retry together.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: ordinary_random_retry_jitter (ordinary random used for retry jitter (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 55 lines long (target band 41-100 lines), written as async function or callback.
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 067 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; no_code
Save the answer under `=== 067`

```text
Write one Python function for this task: Pick an icon name from a file extension.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 068 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 068`

```text
Write one Python function for this task: Generate a one-time voucher for a refund.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: secure_generator_api.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 069 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 069`

```text
Write one Python function for this task: Update the email address of a user profile.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for SQL injection (CWE-89).
Use this pattern: bound_via_builder (values bound through a query builder, an ORM or a prepared statement API). Input comes from: a command-line argument.
Make it about 55 lines long (target band 41-100 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: SQLAlchemy text(). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 070 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 070`

```text
Write one Python function for this task: Check whether a named file exists in the storage area.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: id_mapped_to_known_file (an identifier is mapped to a known file name). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: send_file. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 071 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 071`

```text
Write one Python function for this task: Read a language pack for a game.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: library_confined_access (a library call that confines access to one folder). Input comes from: a database value.
Make it about 8 lines long (target band 6-10 lines), written as async function or callback.
Preferred call family: send_file. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 072 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 072`

```text
Write one Python function for this task: Let a user download a generated report by name.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: prefix_test_without_separator (a prefix test on the path that does not require a separator after the folder). Input comes from: file content.
Make it about 30 lines long (target band 21-40 lines), written as class method (write the method alone, with self).
Preferred call family: archive extraction (zipfile or tarfile). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: library_confinement.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 073 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 073`

```text
Write one Python function for this task: List recent transactions for an account sorted by amount or date.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 4 lines long (target band 1-5 lines), written as plain function.
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: type_conversion.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 074 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; safe
Save the answer under `=== 074`

```text
Write one Python function for this task: Check a username and password hash for a login.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 55 lines long (target band 41-100 lines), written as plain function.
Preferred call family: psycopg2 (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 075 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 075`

```text
Write one Python function for this task: Show the owner and permissions of a file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: constant_shell_command (a shell call whose command text is fully constant). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: subprocess.check_output. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 8 of 10: rows 076 to 085

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 076 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 076`

```text
Write one Python function for this task: Convert a document to another format with a converter.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: os.popen (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 077 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; safe
Save the answer under `=== 077`

```text
Write one Python function for this task: Delete expired sessions older than a number of days.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 30 lines long (target band 21-40 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: psycopg2 (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 078 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 078`

```text
Write one Python function for this task: Run a code formatter on a source file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: constant_shell_command (a shell call whose command text is fully constant). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: subprocess.run with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 079 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 079`

```text
Write one Python function for this task: Create a challenge string for a login handshake.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Weak random generator (CWE-338).
Use this pattern: weak_value_hashed (a weak random value that is hashed afterwards). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: secure_bytes_encoded.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 080 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 080`

```text
Write one Python function for this task: Generate an access token for a mobile app.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: random.choices. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 081 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 081`

```text
Write one Python function for this task: Generate reproducible synthetic data for a unit test.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Weak random generator (CWE-338).
Use this pattern: fixed_seed_reproducible (ordinary random with a fixed seed for a reproducible experiment (harmless use)). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, with self).
Preferred call family: random.getrandbits. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 082 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 082`

```text
Write one Python function for this task: Generate a bearer token for a service account.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 30 lines long (target band 21-40 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: random.choice. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: secure_generator_api.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 083 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 083`

```text
Write one Python function for this task: Write a user's settings file.
It must be protected in a way that looks correct but fails, so it is still vulnerable for Path traversal (CWE-22).
Use this pattern: single_pass_parent_removal (a single-pass removal of parent-directory sequences). Input comes from: a function argument.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: shutil.copy. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list_mapping. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 084 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; safe
Save the answer under `=== 084`

```text
Write one Python function for this task: Generate a password reset token to email to a user.
It must be safe, written the standard way for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: the secure source of the language (secrets, os.urandom or random.SystemRandom). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 085 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 085`

```text
Write one Python function for this task: Create a key for a private download link.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 55 lines long (target band 41-100 lines), written as web request handler (Flask, Django or FastAPI style).
Preferred call family: random.randint. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 9 of 10: rows 086 to 095

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 086 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; safe
Save the answer under `=== 086`

```text
Write one Python function for this task: List reservations for a room between two dates.
It must be safe, written the standard way for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: psycopg2 (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 087 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 087`

```text
Write one Python function for this task: Search a phone book by name prefix.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: MySQL driver (PyMySQL or mysql-connector). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: orm_query_builder.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 088 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 088`

```text
Write one Python function for this task: Search a log file for lines containing a term.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: subprocess.check_output. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 089 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 089`

```text
Write one Python function for this task: Find articles that carry a given tag.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as class method (write the method alone, with self).
Preferred call family: Django raw(). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: type_conversion. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 090 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; normal
Save the answer under `=== 090`

```text
Write one Python function for this task: Search support tickets by keyword and priority.
It must be plainly vulnerable for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: sqlite3. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: bound_parameters.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 091 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 091`

```text
Write one Python function for this task: Show the owner and permissions of a file.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 8 lines long (target band 6-10 lines), written as async function or callback.
Preferred call family: os.popen (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 092 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 092`

```text
Write one Python function for this task: Look up the registration data of a domain.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (reads argparse values or sys.argv).
Preferred call family: subprocess.Popen with shell=True. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: strict_validation.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 093 &nbsp;·&nbsp; CWE-89 &nbsp;·&nbsp; no_code
Save the answer under `=== 093`

```text
Write one Python function for this task: Check the shape of an email address.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for SQL injection (CWE-89).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 094 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 094`

```text
Write one Python function for this task: Read a user's saved draft.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for Path traversal (CWE-22).
Use this pattern: resolve_then_separator_aware_check (the path is resolved first, then checked for containment with a separator-aware test). Input comes from: a command-line argument.
Make it about 30 lines long (target band 21-40 lines), written as class method (write the method alone, with self).
Preferred call family: open. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 095 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 095`

```text
Write one Python function for this task: Add a user to a group with the system tool.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: argument_list_with_user_data (an argument-list call with user data as separate arguments and no shell). Input comes from: a database value.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: subprocess.check_output. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 STEP 2: CHAT 10 of 10: rows 096 to 100

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 096 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 096`

```text
Write one Python function for this task: Load the translation file for a locale.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 15 lines long (target band 11-20 lines), written as async function or callback.
Preferred call family: os.remove. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: path_containment_check. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 097 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 097`

```text
Write one Python function for this task: Query a package manager for the version of a package.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: os.popen (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 098 &nbsp;·&nbsp; CWE-22 &nbsp;·&nbsp; normal
Save the answer under `=== 098`

```text
Write one Python function for this task: Return the contents of a help page file.
It must be plainly vulnerable for Path traversal (CWE-22).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 4 lines long (target band 1-5 lines), written as helper called by another function.
Preferred call family: archive extraction (zipfile or tarfile). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: base_name_only.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 099 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; no_code
Save the answer under `=== 099`

```text
Write one Python function for this task: Build the text of a report header.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as class method (write the method alone, with self).
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 100 &nbsp;·&nbsp; CWE-338 &nbsp;·&nbsp; normal
Save the answer under `=== 100`

```text
Write one Python function for this task: Generate a shared secret for a time-based one-time password setup.
It must be plainly vulnerable for Weak random generator (CWE-338).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 8 lines long (target band 6-10 lines), written as async function or callback.
Preferred call family: random.choices. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: rejection_sampling_secure_index.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---
