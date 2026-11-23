"""Checks of one generated row against its brief. A row with a hard problem is not written to the final file; the person generates that row again."""
import ast, builtins, difflib, io, re, sys, tokenize

import spec as S

LEAK = re.compile(S.LEAK_WORDS, re.I)
STDLIB = set(getattr(sys, "stdlib_module_names", ()))
ALLOWED_EXTRA = {"flask", "werkzeug", "django", "sqlalchemy", "psycopg2", "pymysql", "mysql", "MySQLdb", "requests", "boto3"}
SOURCE_HINTS = {"web_request": ("request", "http", "flask", "form", "query", "header", "req."), "environment": ("environ", "getenv", "env"),
                "command_line": ("argv", "argparse", "flag.", "os.args", "getopt", "args"), "file": ("open", "read", "file", "load", "fopen", "ifstream", "readfile"),
                "database_value": ("row", "cursor", "record", "db", "query", "fetch", "select"),
                "network_message": ("socket", "recv", "packet", "message", "payload", "network", "msg", "conn", "body")}


# ------------------------------------------------------------ language helpers
def strip_c_like(code):
    out, i, n = [], 0, len(code)
    while i < n:
        c = code[i]
        if code.startswith("//", i):
            j = code.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i)); i = j
        elif code.startswith("/*", i):
            j = code.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append("".join("\n" if ch == "\n" else " " for ch in code[i:j])); i = j
        elif c in "\"'`":
            q, j = c, i + 1
            while j < n and code[j] != q:
                j += 2 if code[j] == "\\" else 1
            j = min(j + 1, n)
            out.append("".join("\n" if ch == "\n" else " " for ch in code[i:j])); i = j
        else:
            out.append(c); i += 1
    return "".join(out)


def count_functions(code, lang):
    if lang == "python":
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return None
        return sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) for n in tree.body)
    if lang == "go":
        return len(re.findall(r"(?m)^func\b", code))
    clean = strip_c_like(code)
    depth, count, last = 0, 0, ""
    for m in re.finditer(r"[{}]|[^{}\s]", clean):
        ch = m.group(0)
        if ch == "{":
            if depth == 0 and last in (")", "t", "e", "x"):
                count += 1
            depth += 1
        elif ch == "}":
            depth = max(0, depth - 1)
        else:
            last = ch
    return count


def unreachable_python(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False

    def block(stmts):
        for s in stmts[:-1]:
            if isinstance(s, (ast.Return, ast.Raise, ast.Break, ast.Continue)):
                return True
        for s in stmts:
            for attr in ("body", "orelse", "finalbody"):
                sub = getattr(s, attr, None)
                if isinstance(sub, list) and sub and block([x for x in sub if isinstance(x, ast.stmt)]):
                    return True
            for h in getattr(s, "handlers", []) or []:
                if block(h.body):
                    return True
        return False
    return any(block(n.body) for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)))


def unreachable_c_like(code):
    clean = strip_c_like(code).splitlines()
    for i, l in enumerate(clean[:-1]):
        t = l.strip()
        if re.match(r"(return\b|break;|continue;|goto\b|throw\b)", t) and t.endswith(";"):
            prev = next((x.strip() for x in reversed(clean[:i]) if x.strip()), "")
            if (prev.endswith(")") and not prev.endswith(";")) or prev == "else":
                continue
            nxt = next((x for x in clean[i + 1:] if x.strip()), "")
            if nxt and nxt.strip() not in ("}", "};") and not re.match(r"\s*(case\b|default\b|else\b)", nxt):
                if len(nxt) - len(nxt.lstrip()) == len(l) - len(l.lstrip()):
                    return True
    return False


def comment_lines(code, lang):
    n = 0
    if lang == "python":
        try:
            for tok in tokenize.generate_tokens(io.StringIO(code).readline):
                if tok.type == tokenize.COMMENT:
                    n += 1
            for node in ast.walk(ast.parse(code)):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and ast.get_docstring(node):
                    n += 3
        except (tokenize.TokenError, SyntaxError, IndentationError):
            n += len(re.findall(r"(?m)^\s*#", code))
        return n
    for raw, cl in zip(code.splitlines(), strip_c_like(code).splitlines()):
        if raw.strip() and not cl.strip() and ("//" in raw or "/*" in raw or "*" in raw.strip()[:2]):
            n += 1
        elif "//" in raw and cl.strip() != raw.strip():
            n += 1
    return n


def undefined_calls(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    defined = set(dir(builtins))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            if not isinstance(node, ast.Lambda):
                defined.add(node.name)
            a = node.args
            for x in a.posonlyargs + a.args + a.kwonlyargs + ([a.vararg] if a.vararg else []) + ([a.kwarg] if a.kwarg else []):
                defined.add(x.arg)
        elif isinstance(node, ast.Import):
            defined |= {(x.asname or x.name).split(".")[0] for x in node.names}
        elif isinstance(node, ast.ImportFrom):
            defined |= {x.asname or x.name for x in node.names}
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            defined.add(node.id)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            defined.add(node.name)
    called = {n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    return sorted(c for c in called if c not in defined)


def numbered(code):
    return "\n".join(f"{i:3d} {l}" for i, l in enumerate(code.splitlines(), 1))


def sink_token(sink):
    t = re.sub(r"\(.*", "", str(sink)).strip()
    return re.split(r"[.\s]|::", t)[-1] if t else ""


def changed_lines(a, b):
    return sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False).get_opcodes() if t != "equal")


# ------------------------------------------------------------ the row check
def check(reply, brief):
    """returns (hard, soft, notes); also may repair reply['vulnerable_lines'] (adds the line with the sink call) and sets reply['_note']."""
    hard, soft, notes = [], [], []
    lang, case = brief["language"], brief["case_type"]
    vuln = case in S.VULNERABLE_CASES
    code = reply.get("code") or ""
    fixed = reply.get("fixed_code") or ""
    if len(code.strip()) < 15 or code.strip() in ("[]", "...", "{}", "null"):
        return ["`code` is empty or a placeholder"], soft, notes
    n = len(code.splitlines())
    real = S.band_of(n)
    if real != brief["band"]:
        far = abs(S.BANDS.index(real) - S.BANDS.index(brief["band"]))
        notes.append(f"length {n} lines = band {real} (brief {brief['band']}{', 2+ bands off' if far >= 2 else ''})")
    nf = count_functions(code, lang)
    if nf is None:
        hard.append("the Python code does not parse")
    elif nf != 1:
        hard.append(f"`code` contains {nf} top-level functions or classes; it must be exactly ONE function")
    if unreachable_python(code) if lang == "python" else unreachable_c_like(code):
        hard.append("unreachable code after a return, break, continue or throw")
    want_c = brief["comments"] == "with"
    cl = comment_lines(code, lang)
    if want_c and cl < 1:
        hard.append("the brief asks for comments or a docstring but `code` has none")
    if not want_c and cl:
        hard.append("the brief says no comments, but `code` has comments or a docstring")
    if LEAK.search(code) or LEAK.search(reply.get("task_description") or ""):
        hard.append("a word that reveals the label appears in the code, a comment or the task sentence")
    sink = reply.get("sink") or ""
    if case != "no_code":
        tok = sink_token(sink)
        if not tok:
            hard.append("`sink` is empty")
        elif tok not in code:
            hard.append(f"`sink` {sink!r} does not appear in the code")
    vl = reply.get("vulnerable_lines")
    if vuln:
        if not fixed.strip():
            hard.append("`fixed_code` is missing")
        else:
            if changed_lines(code, fixed) > S.MAX_FIX_LINES:
                hard.append(f"`fixed_code` changes more than {S.MAX_FIX_LINES} lines")
            if fixed.strip() == code.strip():
                hard.append("`fixed_code` is identical to `code`")
            if lang == "python":
                try:
                    a, f = ast.parse(code).body[0], ast.parse(fixed).body[0]
                    if a.name != f.name or [x.arg for x in a.args.args] != [x.arg for x in f.args.args]:
                        hard.append("`fixed_code` must keep the same function name and arguments")
                except (SyntaxError, IndexError):
                    hard.append("`fixed_code` does not parse")
        if not isinstance(vl, list) or not vl or not all(isinstance(x, int) and not isinstance(x, bool) for x in vl):
            hard.append("`vulnerable_lines` must be a non-empty list of line numbers")
        elif any(x < 1 or x > n for x in vl):
            hard.append(f"`vulnerable_lines` {vl} are outside 1..{n}")
        else:
            lines = code.splitlines()
            tok = sink_token(sink)
            hit = [i for i, l in enumerate(lines, 1) if tok and tok in l and not re.match(r"\s*(import\b|from\b.*\bimport\b|#include|using\b)", l)]
            if hit and not set(hit) & set(vl):
                reply["vulnerable_lines"] = sorted(set(vl) | {hit[0]})
                reply["_note"] = f"script added line {hit[0]} (the sink call {tok}) to vulnerable_lines; model gave {vl}"
                notes.append(f"vulnerable_lines {vl} did not include the sink call line {hit[0]}: line added, noted in `notes`")
            if n > 5 and len(set(vl)) > max(6, 0.6 * n):
                hard.append("`vulnerable_lines` cover almost the whole function")
    else:
        if fixed.strip():
            hard.append("`fixed_code` must be empty for this case type")
        if vl not in ([], "", None):
            hard.append("`vulnerable_lines` must be empty for this case type")
    if lang == "python":
        und = undefined_calls(code)
        if und:
            msg = f"`code` calls {', '.join(und)}, which is not defined or imported inside the function"
            (hard if case in ("safe", "hard_negative") else soft).append(msg)
        try:
            mods = set()
            for node in ast.walk(ast.parse(code)):
                if isinstance(node, ast.Import):
                    mods |= {a.name.split(".")[0] for a in node.names}
                elif isinstance(node, ast.ImportFrom) and node.module:
                    mods.add(node.module.split(".")[0])
            odd = sorted(m for m in mods if STDLIB and m not in STDLIB and m not in ALLOWED_EXTRA)
            if odd:
                soft.append(f"third-party import(s): {', '.join(odd)}")
        except SyntaxError:
            pass
    src = brief["source"]
    if src in SOURCE_HINTS and not any(h in code.lower() for h in SOURCE_HINTS[src]):
        soft.append(f"input source {src} is not visible in the code")
    return hard, soft, notes
