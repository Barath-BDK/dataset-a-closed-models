# P12b · Claude · Go · 25 prompts

> **This one file has everything you need to paste.** Your answers go into ONE other file: [`submissions/P12b_claude_go_cmdi.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/P12b_claude_go_cmdi.txt).

## What to do (the short version)

1. Open **Claude** (the free base model). Start a **new chat**.
2. Copy the **MASTER PROMPT** below (the copy button is in the top right corner of the box) and paste it into the chat. Wait until the model answers `ready`.
3. Copy **ROW 001**, paste it into the chat. The model answers with a block of JSON.
4. Copy the whole answer and paste it into `submissions/P12b_claude_go_cmdi.txt` **under the line `=== 001`**.
5. Do the same for the next rows. **After 10 rows, start a new chat** and paste the MASTER PROMPT again (the file tells you where).


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

# 🟦 CHAT 1 of 3: rows 001 to 010

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 001 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 001`

```text
Write one Go function for this task: Trace the network route to a host.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: dash_argument_injection (a value that starts with a dash is taken as an option by the called program). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as goroutine or callback.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 002 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 002`

```text
Write one Go function for this task: Add a user to a group with the system tool.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 8 lines long (target band 6-10 lines), written as command line tool function (uses flags or os.Args values).
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: strict_validation. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 003 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 003`

```text
Write one Go function for this task: Resize an image to a requested size with an external tool.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a function argument.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: exec.Command with sh -c (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 004 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 004`

```text
Write one Go function for this task: Download a web page with a command line client.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (uses flags or os.Args values).
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: allow_list. The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 005 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; no_code
Save the answer under `=== 005`

```text
Write one Go function for this task: Check the shape of a host name string.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 15 lines long (target band 11-20 lines), written as plain function.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 006 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 006`

```text
Write one Go function for this task: Execute a report generator with a chosen template.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 15 lines long (target band 11-20 lines), written as goroutine or callback.
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 007 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 007`

```text
Write one Go function for this task: Check whether a host answers a network ping.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: an environment variable.
Make it about 30 lines long (target band 21-40 lines), written as method on a struct.
Preferred call family: exec.Command with arguments (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 008 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 008`

```text
Write one Go function for this task: Run a spell checker on a text file.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: strict_parser_then_no_shell (input checked by a strict parser (for example an IP address parser) and passed without a shell). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 009 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 009`

```text
Write one Go function for this task: Trace the network route to a host.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: file content.
Make it about 8 lines long (target band 6-10 lines), written as plain function.
Preferred call family: exec.Command with arguments (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 010 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 010`

```text
Write one Go function for this task: Convert an audio file to another bitrate.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 4 lines long (target band 1-5 lines), written as method on a struct.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 CHAT 2 of 3: rows 011 to 020

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 011 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 011`

```text
Write one Go function for this task: Run a unit conversion script on a value.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: argument_list_with_user_data (an argument-list call with user data as separate arguments and no shell). Input comes from: a web request.
Make it about 8 lines long (target band 6-10 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 012 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 012`

```text
Write one Go function for this task: Compare two files and show the differences.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (uses flags or os.Args values).
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: allow_list.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 013 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 013`

```text
Write one Go function for this task: Check whether a port is open on a host.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: constant_shell_command (a shell call whose command text is fully constant). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (uses flags or os.Args values).
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 014 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 014`

```text
Write one Go function for this task: Restart a named system service.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: quoting_in_wrong_context (quoting applied in the wrong context). Input comes from: an environment variable.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: quoting.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 015 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 015`

```text
Write one Go function for this task: Zip the contents of a folder into a named archive.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: command_from_fixed_map (the command chosen from a fixed map of allowed commands). Input comes from: file content.
Make it about 8 lines long (target band 6-10 lines), written as helper called by another function.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 016 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; safe
Save the answer under `=== 016`

```text
Write one Go function for this task: Scan an uploaded file with a command line scanner.
It must be safe, written the standard way for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: exec.Command with arguments (written the safe, standard way). If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 017 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 017`

```text
Write one Go function for this task: Run a unit conversion script on a value.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: command_from_fixed_map (the command chosen from a fixed map of allowed commands). Input comes from: an environment variable.
Make it about 8 lines long (target band 6-10 lines), written as method on a struct.
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 018 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 018`

```text
Write one Go function for this task: Read the last lines of a log file.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a web request.
Make it about 15 lines long (target band 11-20 lines), written as HTTP handler (http.HandlerFunc or a handler method).
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 019 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 019`

```text
Write one Go function for this task: Stop a process by name.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: validation_of_other_variable (validation applied to a different variable from the one actually used). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as plain function.
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: strict_validation.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 020 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 020`

```text
Write one Go function for this task: Stop a process by name.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a network message.
Make it about 4 lines long (target band 1-5 lines), written as method on a struct.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the early part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---

# 🟦 CHAT 3 of 3: rows 021 to 025

**Open a NEW chat → paste the MASTER PROMPT (at the top of this file) → wait for `ready` → then paste the rows below one by one.**

### ▶ ROW 021 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; normal
Save the answer under `=== 021`

```text
Write one Go function for this task: Print the version of a tool chosen from a list.
It must be plainly vulnerable for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: a database value.
Make it about 8 lines long (target band 6-10 lines), written as goroutine or callback.
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
The flaw should sit in the late part of the function. For fixed_code use this fix type: strict_validation.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 022 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_positive
Save the answer under `=== 022`

```text
Write one Go function for this task: Check whether a host answers a network ping.
It must be protected in a way that looks correct but fails, so it is still vulnerable for OS command injection (CWE-78).
Use this pattern: validation_of_other_variable (validation applied to a different variable from the one actually used). Input comes from: a function argument.
Make it about 30 lines long (target band 21-40 lines), written as helper called by another function.
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
The flaw should sit in the middle part of the function. For fixed_code use this fix type: argv_no_shell.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 023 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 023`

```text
Write one Go function for this task: Query a package manager for the version of a package.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: argument_list_with_user_data (an argument-list call with user data as separate arguments and no shell). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as helper called by another function.
Preferred call family: exec.Command with sh -c. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: a few plain explanatory comment lines or a docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 024 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; hard_negative
Save the answer under `=== 024`

```text
Write one Go function for this task: Execute a report generator with a chosen template.
It must be completely safe, while using the dangerous call or looking like the vulnerable form for OS command injection (CWE-78).
Use this pattern: command_from_fixed_map (the command chosen from a fixed map of allowed commands). Input comes from: a command-line argument.
Make it about 15 lines long (target band 11-20 lines), written as command line tool function (uses flags or os.Args values).
Preferred call family: exec.Command with arguments. If it does not fit the task, use the closest natural call of the same kind.
Names: descriptive (full words). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

### ▶ ROW 025 &nbsp;·&nbsp; CWE-78 &nbsp;·&nbsp; no_code
Save the answer under `=== 025`

```text
Write one Go function for this task: Compute a percentage of a total.
It must be ordinary code from the same kind of program that does not use any dangerous call for this weakness for OS command injection (CWE-78).
Use this pattern: plain (an ordinary row without a special pattern). Input comes from: not applicable: the function takes no untrusted input.
Make it about 4 lines long (target band 1-5 lines), written as goroutine or callback.
Preferred call family: none. If it does not fit the task, use the closest natural call of the same kind.
Names: terse (short names). Comments: none, and no docstring.
Do not write any comment, name or string that says whether the code is safe or vulnerable.
Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.
fixed_code and vulnerable_lines are empty for safe code.
```

---
