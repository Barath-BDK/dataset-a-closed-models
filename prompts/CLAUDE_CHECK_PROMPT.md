# Check your rows with Claude (no commands needed)

Use this after you have pasted the answers into your hand-in file. Do it **10 rows at a time**, in a **new Claude chat** each time (claude.ai, the free base model is fine).

There are two checks. Do **Check A** first, then **Check B**.

---

## Check A: do the rows follow the rules?

1. Open a new Claude chat and paste the box below.
2. Directly under it, paste the 10 rows, each like this (the prompt is in your `MY_PROMPTS` file, the answer is in your hand-in file):

```
ROW 003
PROMPT: <the prompt you sent>
ANSWER: <the model's JSON answer>
```

3. Claude replies with a table. Every row marked **REDO** you generate again (new chat, same prompt) and paste over the old answer.

````text
You are a strict reviewer for a dataset of code that is used to train vulnerability detectors. I will give you up to 10 rows. Each row has the PROMPT that was sent to an AI model and the model's ANSWER (a JSON object). Check each row against these rules and be strict:

1. The answer is valid JSON with exactly these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail. "code" is not empty.
2. "code" is ONE complete function in the language asked for. No second function, no main program, no includes or imports outside it, nothing after the function.
3. The function does not call any helper function that is not defined or imported inside it.
4. It follows the PROMPT: language, task, pattern, where the input comes from, call family (or the closest natural call), program shape, naming style.
5. Comments: if the prompt said "none", there is no comment and no docstring. If it asked for comments, there are a few plain comments that explain what the code really does.
6. Length: close to the number of lines asked for. Padding (useless lines, code after a return, unused variables added only to be longer) is NOT allowed.
7. No word anywhere (comment, name, string) says whether the code is safe, vulnerable, insecure, fixed, bad, good, secure.
8. Rows that are vulnerable (the prompt says "vulnerable" or "looks protected but is not"): "fixed_code" is present, changes at most 10 lines, keeps the same behaviour for normal input, and really removes the weakness. "vulnerable_lines" lists the line numbers (counted from 1 in "code") that build or use the dangerous value, including the line with the dangerous call. Count the lines yourself and say if the numbers are wrong.
9. Rows that are safe (the prompt says "safe", "completely safe" or "ordinary code"): "fixed_code" is "" and "vulnerable_lines" is []. And the code really IS safe. Think hard about a second input, a special value or a second code path that makes it exploitable.
10. "sink" really appears in "code".

Reply with ONE table and nothing else. Columns: row | OK or REDO | what is wrong (one short sentence, or "-"). For every REDO row also write one short sentence telling me what to ask the model to do differently. If you are not sure about a row, mark it REDO and say why.

Wait for my rows.
````

---

## Check B: is the label right? (second, separate chat)

The label is the most important thing in the dataset. Models often call code safe when it can still be attacked. So a second opinion is asked **without telling Claude what the label should be**.

1. Open a **new** Claude chat (not the one from Check A).
2. For each of the 10 rows, paste this (fill in the three things). Paste only the `code` of the answer, not `fixed_code`, and do not say what the label is:

````text
Here is a [LANGUAGE] function.
[THE CODE]
Question: is this function vulnerable to [WEAKNESS NAME] ([CWE])?
Reply with JSON only:
{"verdict": "vulnerable" or "safe",
 "vulnerable_lines": [line numbers counted from 1, empty if safe],
 "reason": "one sentence"}
````

3. Compare with the row's case:
   - the row is **vulnerable** (normal, hard_positive) and Claude says **vulnerable** → fine
   - the row is **safe** (safe, hard_negative, no_code) and Claude says **safe** → fine
   - **Claude disagrees** → look at the code yourself. If Claude is right, fix the row (generate again) or write `SKIP` with the reason. If you think Claude is wrong, keep the row and write one line under the answer in your hand-in file: `NOTE: Claude said vulnerable, but <your reason>`.

Weakness names: CWE-89 SQL injection · CWE-78 OS command injection · CWE-22 Path traversal · CWE-338 Weak random generator.

If you want to use the ready-made command-line version of Check B instead (for the lead): `python tools/make_judge_prompts.py <package>`.
