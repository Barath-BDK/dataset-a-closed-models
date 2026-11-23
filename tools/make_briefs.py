#!/usr/bin/env python3
"""Builds the whole job from the distribution in the specification: one brief per row (1,200 rows), 12 packages (3 models x 4 languages),
the filled prompt for every row, and the text of every GitHub issue.

    python tools/make_briefs.py                  (run from the repository root; overwrites data/, packages/, issues/)

Distribution per cell (one weakness in one language, 75 rows, 25 from each model):
  normal 25 (9/8/8), hard_positive 12 (4/4/4), safe 12 (4/4/4), hard_negative 20 (7/7/6), no_code 6 (2/2/2);
  bands 1-5: 7, 6-10: 19, 11-20: 22, 21-40: 19, 41-100: 8; at least 4 shapes (none above 40%), 4 input sources, 3 fix types, 30 tasks per cell,
  no task for more than 3 rows, half descriptive / half terse names, half with / without comments, flaw early / middle / late,
  indirection in about a third of the vulnerable rows, no pattern above 25% of a cell's hard rows.
"""
import collections, csv, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import spec as S
from task_banks import NO_CODE_TASKS, PLAIN_RANDOM_TASKS, VULN_TASKS

SHAPES = {
    "python": ["plain function", "class method (write the method alone, with self)", "web request handler (Flask, Django or FastAPI style)",
               "command line tool function (reads argparse values or sys.argv)", "helper called by another function", "async function or callback"],
    "c": ["plain function", "request handler that receives a struct or buffer", "command line tool function (uses argc and argv values)",
          "helper called by another function", "callback passed as a function pointer", "small embedded or library utility"],
    "cpp": ["plain function", "class method (write the method alone, as Class::method)", "web or network handler that receives a request object",
            "command line tool function (uses argc and argv values)", "helper called by another function", "callback, lambda or asynchronous task"],
    "go": ["plain function", "method on a struct", "HTTP handler (http.HandlerFunc or a handler method)", "command line tool function (uses flags or os.Args values)",
           "helper called by another function", "goroutine or callback"],
}
SOURCE_LIST = ["function_argument", "web_request", "file", "environment", "command_line", "database_value", "network_message"]
SOURCE_TEXT = {"function_argument": "a function argument", "web_request": "a web request", "file": "file content", "environment": "an environment variable",
               "command_line": "a command-line argument", "database_value": "a database value", "network_message": "a network message",
               "not_applicable": "not applicable: the function takes no untrusted input"}
BAND_TARGET = {"1-5": 4, "6-10": 8, "11-20": 15, "21-40": 30, "41-100": 55}
CASE_DESC = {"normal": "plainly vulnerable", "hard_positive": "protected in a way that looks correct but fails, so it is still vulnerable",
             "safe": "safe, written the standard way", "hard_negative": "completely safe, while using the dangerous call or looking like the vulnerable form",
             "no_code": "ordinary code from the same kind of program that does not use any dangerous call for this weakness"}
CWE_NAME = {"CWE-89": "SQL injection", "CWE-78": "OS command injection", "CWE-22": "Path traversal", "CWE-338": "Weak random generator"}
SAFE_API_338 = {"python": "secrets, os.urandom or random.SystemRandom", "c": "/dev/urandom or getrandom", "cpp": "std::random_device or /dev/urandom", "go": "crypto/rand"}

CWE_INFO = {
    "CWE-89": dict(
        hn=["identifier_allowlist", "placeholder_list_for_in", "constant_fragments_only", "bound_via_builder", "integer_forced", "placeholders_only_format"],
        hp=["handwritten_escaping", "keyword_blocklist", "one_branch_bound", "bound_but_input_identifier"],
        fix={"python": ["bound_parameters", "allow_list", "type_conversion", "orm_query_builder"], "c": ["prepared_statement_bind", "allow_list", "type_conversion"],
             "cpp": ["prepared_statement_bind", "allow_list", "type_conversion", "query_builder_bind"], "go": ["bound_parameters", "allow_list", "type_conversion", "query_builder"]},
        api={"python": ["sqlite3", "psycopg2", "MySQL driver (PyMySQL or mysql-connector)", "SQLAlchemy text()", "Django raw()"], "c": ["sqlite3_exec", "mysql_query", "PQexec"],
             "cpp": ["sqlite3 C API", "mysql_query", "PQexec", "Qt QSqlQuery", "MySQL Connector/C++"], "go": ["database/sql Query", "database/sql Exec", "database/sql QueryRow", "sqlx", "gorm Raw"]}),
    "CWE-78": dict(
        hn=["constant_shell_command", "all_arguments_shell_quoted", "argument_list_with_user_data", "command_from_fixed_map", "strict_parser_then_no_shell", "user_data_after_end_of_options"],
        hp=["partial_shell_character_filter", "quoting_in_wrong_context", "validation_of_other_variable", "validator_accepts_too_much", "dash_argument_injection"],
        fix={l: ["argv_no_shell", "quoting", "allow_list", "strict_validation"] for l in S.LANGUAGES},
        api={"python": ["os.system", "os.popen", "subprocess.run with shell=True", "subprocess.Popen with shell=True", "subprocess.check_output"], "c": ["system", "popen", "execl through sh -c", "execvp"],
             "cpp": ["system", "popen", "QProcess", "Boost.Process"], "go": ["exec.Command with sh -c", "exec.Command with arguments"]}),
    "CWE-22": dict(
        hn=["resolve_then_separator_aware_check", "base_name_only", "id_mapped_to_known_file", "safe_filename_helper_fixed_folder", "library_confined_access"],
        hp=["check_before_normalising", "prefix_test_without_separator", "single_pass_parent_removal", "relative_check_misses_absolute", "extension_check_only"],
        fix={"python": ["path_containment_check", "base_name_only", "allow_list_mapping", "library_confinement"], "c": ["path_containment_check", "base_name_only", "allow_list_mapping"],
             "cpp": ["path_containment_check", "base_name_only", "allow_list_mapping"], "go": ["path_containment_check", "base_name_only", "allow_list_mapping", "library_confinement"]},
        api={"python": ["open", "pathlib", "shutil.copy", "os.remove", "send_file", "archive extraction (zipfile or tarfile)"], "c": ["fopen", "open", "unlink", "rename"],
             "cpp": ["ifstream or ofstream", "std::filesystem", "fopen", "std::remove"], "go": ["os.Open", "os.ReadFile", "os.Create", "http.ServeFile", "archive extraction (archive/zip)"]}),
    "CWE-338": dict(
        hn=["ordinary_random_simulation", "ordinary_random_shuffling", "ordinary_random_sampling", "ordinary_random_retry_jitter", "ordinary_random_games",
            "ordinary_random_test_data", "secure_secret_plus_ordinary_random_elsewhere", "fixed_seed_reproducible"],
        hp=["weak_generator_behind_helper", "secure_sounding_name_weak_generator", "seed_from_clock_or_pid", "weak_value_hashed"],
        fix={"python": ["secure_generator_api", "secure_bytes_encoded", "rejection_sampling_secure_index"], "c": ["secure_generator_api", "secure_bytes_encoded", "rejection_sampling_secure_index"],
             "cpp": ["secure_generator_api", "secure_bytes_encoded", "rejection_sampling_secure_index"], "go": ["secure_generator_api", "secure_bytes_encoded", "rejection_sampling_secure_index"]},
        api={"python": ["random.choice", "random.randint", "random.getrandbits", "random.choices"], "c": ["rand", "srand", "random"],
             "cpp": ["rand", "std::mt19937", "std::default_random_engine"], "go": ["math/rand"]}),
}
PATTERN_DEF = {
    "identifier_allowlist": "a table or column name chosen from a fixed allow-list, values bound",
    "placeholder_list_for_in": "a placeholder list generated to match the length of a list, values bound",
    "constant_fragments_only": "a query assembled from constant fragments only, values bound",
    "bound_via_builder": "values bound through a query builder, an ORM or a prepared statement API",
    "integer_forced": "a number forced to an integer before it is formatted into the query",
    "placeholders_only_format": "a formatted string that contains only placeholders",
    "handwritten_escaping": "hand-written escaping of quotes that does not cover every case", "keyword_blocklist": "a blocklist of SQL keywords or characters",
    "one_branch_bound": "parameters in one branch but string building in another", "bound_but_input_identifier": "values are bound, but a table name or sort column comes from the input",
    "constant_shell_command": "a shell call whose command text is fully constant", "all_arguments_shell_quoted": "every argument properly shell-quoted for the context it is used in",
    "argument_list_with_user_data": "an argument-list call with user data as separate arguments and no shell", "command_from_fixed_map": "the command chosen from a fixed map of allowed commands",
    "strict_parser_then_no_shell": "input checked by a strict parser (for example an IP address parser) and passed without a shell",
    "user_data_after_end_of_options": "user data placed after an end-of-options marker such as --",
    "partial_shell_character_filter": "a filter that removes or rejects only some shell characters", "quoting_in_wrong_context": "quoting applied in the wrong context",
    "validation_of_other_variable": "validation applied to a different variable from the one actually used", "validator_accepts_too_much": "a validator that accepts more than it appears to",
    "dash_argument_injection": "a value that starts with a dash is taken as an option by the called program",
    "resolve_then_separator_aware_check": "the path is resolved first, then checked for containment with a separator-aware test", "base_name_only": "only the base name of the input is used",
    "id_mapped_to_known_file": "an identifier is mapped to a known file name", "safe_filename_helper_fixed_folder": "a safe-filename helper combined with a fixed folder",
    "library_confined_access": "a library call that confines access to one folder", "check_before_normalising": "the check is done before the path is normalised",
    "prefix_test_without_separator": "a prefix test on the path that does not require a separator after the folder",
    "single_pass_parent_removal": "a single-pass removal of parent-directory sequences", "relative_check_misses_absolute": "a check for relative sequences that misses absolute paths",
    "extension_check_only": "only the file extension is checked",
    "ordinary_random_simulation": "ordinary random used in a simulation (harmless use)", "ordinary_random_shuffling": "ordinary random used for shuffling (harmless use)",
    "ordinary_random_sampling": "ordinary random used for sampling (harmless use)", "ordinary_random_retry_jitter": "ordinary random used for retry jitter (harmless use)",
    "ordinary_random_games": "ordinary random used in a game (harmless use)", "ordinary_random_test_data": "ordinary random used to make test data (harmless use)",
    "secure_secret_plus_ordinary_random_elsewhere": "the secret comes from a secure generator while ordinary random is used for something harmless in the same function",
    "fixed_seed_reproducible": "ordinary random with a fixed seed for a reproducible experiment (harmless use)",
    "weak_generator_behind_helper": "the weak generator is hidden behind a helper function", "secure_sounding_name_weak_generator": "a secure-sounding name over a weak generator",
    "seed_from_clock_or_pid": "the generator is seeded from the clock or the process id", "weak_value_hashed": "a weak random value that is hashed afterwards",
    "plain": "an ordinary row without a special pattern",
}


def band_eligible(r, band):
    if band == "1-5":
        return r["case_type"] in ("normal", "safe", "no_code")
    if r["case_type"] == "no_code":
        return band in ("6-10", "11-20")
    return True


def build_cell(rng, cwe, lang, cell_index):
    info = CWE_INFO[cwe]
    rows = [dict(case_type=ct) for ct, n in S.CASE_PER_CELL.items() for _ in range(n)]
    # bands (each cell has exactly 7 / 19 / 22 / 19 / 8)
    quota = dict(S.BAND_PER_CELL)
    nc = [r for r in rows if r["case_type"] == "no_code"]
    for r, b in zip(nc, ["1-5", "1-5", "6-10", "6-10", "11-20", "11-20"]):
        r["band"] = b
        quota[b] -= 1
    normal = [r for r in rows if r["case_type"] == "normal"]
    rng.shuffle(normal)
    for r in normal[:5]:
        r["band"] = "1-5"
        quota["1-5"] -= 1
    rest = [r for r in rows if "band" not in r]
    pool = [b for b, n in quota.items() for _ in range(n)]
    rng.shuffle(pool)
    assert len(pool) == len(rest) and all(v >= 0 for v in quota.values()), (quota, len(pool), len(rest))
    for r, b in zip(rest, pool):
        r["band"] = b
    rng.shuffle(rows)
    n = len(rows)

    def cyc(values):
        out = [values[i % len(values)] for i in range(n)]
        rng.shuffle(out)
        return out
    shapes, srcs, apis = cyc(SHAPES[lang]), cyc(SOURCE_LIST), cyc(info["api"][lang])
    names = cyc(["descriptive", "terse"])
    comm = cyc(["with", "without"])
    pos = cyc(["early", "middle", "late"])
    by_type = collections.defaultdict(list)
    for i, r in enumerate(rows):
        r.update(shape=shapes[i], source=srcs[i], names=names[i], comments=comm[i], api=apis[i], target_lines=BAND_TARGET[r["band"]])
        # the input source has to make sense for the shape of the function
        sh = r["shape"].lower()
        if "web" in sh or "http" in sh or "request handler" in sh:
            if r["source"] not in ("web_request", "network_message", "database_value"):
                r["source"] = "web_request"
        elif "command line" in sh:
            r["source"] = "command_line"
        by_type[r["case_type"]].append(r)
    for r in by_type["normal"] + by_type["safe"]:
        r["pattern"] = "plain"
    for key, ct in (("hp", "hard_positive"), ("hn", "hard_negative")):
        tags = list(info[key])
        rng.shuffle(tags)
        for i, r in enumerate(by_type[ct]):
            r["pattern"] = tags[i % len(tags)]
    for r in by_type["no_code"]:
        r["pattern"], r["api"], r["source"] = "plain", "none", "not_applicable"
    if cwe == "CWE-338":
        for r in rows:
            r["source"] = "not_applicable"
    vulnerable = by_type["normal"] + by_type["hard_positive"]
    fixes = list(info["fix"][lang])
    flags = [True] * (len(vulnerable) // 3) + [False] * (len(vulnerable) - len(vulnerable) // 3)
    rng.shuffle(flags)
    for i, r in enumerate(vulnerable):
        r["fix_type"], r["flaw"], r["indirect"] = fixes[i % len(fixes)], pos[i], flags[i]
    # tasks: every row of the cell, all three models together, so no task is used more than twice
    vt, nct = list(VULN_TASKS[cwe]), list(NO_CODE_TASKS[cwe])
    rng.shuffle(vt)
    rng.shuffle(nct)
    vcount = nccount = 0
    plain_used = collections.Counter()
    for r in rows:
        if r["case_type"] == "no_code":
            t = nct[nccount % len(nct)]
            r["task"], r["task_idx"] = t, 200 + NO_CODE_TASKS[cwe].index(t)
            nccount += 1
        elif cwe == "CWE-338" and r["pattern"] in PLAIN_RANDOM_TASKS:
            lst = PLAIN_RANDOM_TASKS[r["pattern"]]
            k = plain_used[r["pattern"]] % len(lst)
            plain_used[r["pattern"]] += 1
            r["task"], r["task_idx"] = lst[k], 100 + list(PLAIN_RANDOM_TASKS).index(r["pattern"]) * 2 + k
        else:
            t = vt[vcount % len(vt)]
            r["task"], r["task_idx"] = t, VULN_TASKS[cwe].index(t)
            vcount += 1
        r["group_id"] = f"task_{S.CWE_SHORT[cwe]}_{S.LANG_SHORT[lang]}_{r['task_idx']:03d}"
    # split between the three models: 25 rows each; the 9th normal and the 6th hard negative rotate with the cell
    rot = cell_index % 3
    want = {m: {} for m, _, _ in S.MODELS}
    for mi, (m, _, _) in enumerate(S.MODELS):
        want[m] = {"normal": 8 + (1 if mi == rot else 0), "hard_positive": 4, "safe": 4, "hard_negative": 7 - (1 if mi == rot else 0), "no_code": 2}
        assert sum(want[m].values()) == 25
    out = {m: [] for m, _, _ in S.MODELS}
    for ct in S.CASE_TYPES:
        grp = list(by_type[ct])
        rng.shuffle(grp)
        i = 0
        for m, _, _ in S.MODELS:
            out[m] += grp[i:i + want[m][ct]]
            i += want[m][ct]
        assert i == len(grp)
    return out


def api_text(r, cwe, lang):
    if r["case_type"] == "no_code":
        return "none: the function must not use any call related to this weakness"
    if cwe == "CWE-338" and r["case_type"] in ("safe", "normal") and False:
        return r["api"]
    if r["case_type"] == "safe":
        return f"{r['api']} (use the safe counterpart or the standard safe way of the language"
    return r["api"]


def row_prompt(r):
    cwe, lang = r["cwe"], r["language"]
    L = S.LANG_TITLE[lang]
    api = r["api"]
    if cwe == "CWE-338" and r["case_type"] in ("safe", "no_code"):
        api = f"the secure source of the language ({SAFE_API_338[lang]})" if r["case_type"] == "safe" else "none"
    elif r["case_type"] == "safe":
        api = f"{r['api']} (written the safe, standard way)"
    elif r["case_type"] == "no_code":
        api = "none"
    lines = [f"Write one {L} function for this task: {r['task']}",
             f"It must be {CASE_DESC[r['case_type']]} for {CWE_NAME[cwe]} ({cwe}).",
             f"Use this pattern: {r['pattern']} ({PATTERN_DEF[r['pattern']]}). Input comes from: {SOURCE_TEXT[r['source']]}.",
             f"Make it about {r['target_lines']} lines long (target band {r['band']} lines), written as {r['shape']}.",
             f"Preferred call family: {api}. If it does not fit the task, use the closest natural call of the same kind.",
             "Names: " + ("descriptive (full words)." if r["names"] == "descriptive" else "terse (short names).") + " Comments: " +
             ("a few plain explanatory comment lines or a docstring." if r["comments"] == "with" else "none, and no docstring.")]
    if r["case_type"] in S.VULNERABLE_CASES:
        extra = f"The flaw should sit in the {r['flaw']} part of the function. For fixed_code use this fix type: {r['fix_type']}."
        if r["indirect"]:
            extra += " The untrusted input must pass through a variable or a small helper step before it reaches the dangerous call."
        lines.append(extra)
    lines += ["Do not write any comment, name or string that says whether the code is safe or vulnerable.",
              "Reply with JSON only, with these keys: code, fixed_code, vulnerable_lines, task_description, sink, build_style, fix_type, cwe_detail.",
              "fixed_code and vulnerable_lines are empty for safe code."]
    return "\n".join(lines)


def main():
    rng = random.Random(20261123)
    briefs = []
    cell_index = 0
    for cwe in S.CWES:
        for lang in S.LANGUAGES:
            per_model = build_cell(rng, cwe, lang, cell_index)
            cell_index += 1
            for m, pre, _ in S.MODELS:
                rows = per_model[m]
                rng.shuffle(rows)
                for j, r in enumerate(rows, 1):
                    r.update(model=m, cwe=cwe, language=lang)
                    r["sample_id"] = f"{pre}_{S.CWE_SHORT[cwe]}_{S.LANG_SHORT[lang]}_{j:04d}"
                    briefs.append(r)
    # packages: (model, language), 100 rows each; package 12 (the last one) is split by weakness into 12a to 12d
    packages = {}
    order = [(m, lang) for m, _, _ in S.MODELS for lang in S.LANGUAGES]
    for pi, (m, lang) in enumerate(order, 1):
        rows = [r for r in briefs if r["model"] == m and r["language"] == lang]
        rng.shuffle(rows)
        pid = f"P{pi:02d}"
        if pi < 12:
            packages[f"{pid}_{m}_{lang}"] = rows
        else:
            for sub, cwe in zip("abcd", S.CWES):
                packages[f"{pid}{sub}_{m}_{lang}_{S.CWE_SHORT[cwe]}"] = [r for r in rows if r["cwe"] == cwe]
    for pkg, rows in packages.items():
        for k, r in enumerate(rows, 1):
            r["package"], r["row_no"], r["batch"] = pkg, k, (k - 1) // 10 + 1
            r["prompt"] = row_prompt(r)
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "briefs.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for pkg, rows in packages.items():
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    # per-package files
    for pkg, rows in packages.items():
        d = os.path.join(ROOT, "packages", pkg)
        os.makedirs(d, exist_ok=True)
        m, lang = rows[0]["model"], rows[0]["language"]
        nb = max(r["batch"] for r in rows)
        with open(os.path.join(d, "rows.csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["row_no", "batch", "sample_id", "weakness", "case_type", "pattern", "call_family", "target_lines", "band", "shape", "source", "names", "comments", "flaw", "fix_type", "indirect", "task"])
            for r in rows:
                w.writerow([r["row_no"], r["batch"], r["sample_id"], r["cwe"], r["case_type"], r["pattern"], r["api"], r["target_lines"], r["band"], r["shape"], r["source"],
                            r["names"], r["comments"], r.get("flaw", ""), r.get("fix_type", ""), "yes" if r.get("indirect") else "", r["task"]])
    # issues
    assign = []
    for pkg, rows in packages.items():
        m, lang = rows[0]["model"], rows[0]["language"]
        cwes = sorted({r["cwe"] for r in rows})
        nb = max(r["batch"] for r in rows)
        cnt = collections.Counter(r["case_type"] for r in rows)
        bands = collections.Counter(r["band"] for r in rows)
        title = f"[{pkg.split('_')[0]}] {S.MODEL_TITLE[m]} x {S.LANG_TITLE[lang]}" + (f" x {', '.join(cwes)}" if len(cwes) == 1 else "") + f": {len(rows)} rows"
        lines = [
            f"## Your job", "",
            f"Write **{len(rows)} rows** with **{S.MODEL_TITLE[m]}** (free base model) in **{S.LANG_TITLE[lang]}** ({', '.join(cwes)}).", "",
            "| | |", "|---|---|",
            f"| **Your prompts (one file)** | [`MY_PROMPTS/{pkg}.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/MY_PROMPTS/{pkg}.md) |",
            f"| **Your hand-in file (the only file you hand in)** | [`submissions/{pkg}.txt`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/submissions/{pkg}.txt) |",
            "| **How to do it** | [`README.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/README.md) |",
            "| **Check with Claude, in the browser** | [`prompts/CLAUDE_CHECK_PROMPT.md`](https://github.com/Barath-BDK/dataset-a-closed-models/blob/main/prompts/CLAUDE_CHECK_PROMPT.md) |", "",
            "### Steps (tick them in your pull request)", "",
            "- [ ] Personal branch `dev/<your-github-username>` made from `main`; issue branch `issue/<number>-" + pkg + "` made from your personal branch",
            f"- [ ] All {len(rows)} prompts pasted into {S.MODEL_TITLE[m]} (new chat for every 10 rows, master prompt first) and every answer pasted under its `=== NNN` line in `submissions/{pkg}.txt`",
            "- [ ] Check A done with Claude (rules); every REDO row generated again",
            "- [ ] Check B done with Claude (labels); disagreements looked at (fixed, `SKIP`, or `NOTE:`)",
            f"- [ ] Pull request from the issue branch into your personal branch with **only** `submissions/{pkg}.txt`; the exact model name written in the description",
            "- [ ] After approval: merged into your personal branch, then one last pull request `dev/<your-github-username>` into `main`", "",
            f"Mix of rows in this package: " + ", ".join(f"{k} {cnt[k]}" for k in S.CASE_TYPES) + ". Lengths: " + ", ".join(f"{b}: {bands[b]}" for b in S.BANDS) + ".", "",
            "<details><summary>Table of all rows (for reference; the prompts already contain all of this)</summary>", "",
                  "| # | id | weakness | case | pattern | call | lines | shape | input | names | comments | flaw | fix | task |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            lines.append(f"| {r['row_no']:03d} | `{r['sample_id']}` | {r['cwe']} | {r['case_type']} | `{r['pattern']}` | {r['api']} | {r['band']} | {r['shape'].split(' (')[0]} | {r['source']} | {r['names']} | {r['comments']} | "
                         f"{r.get('flaw', '-')} | {r.get('fix_type', '-')} | {r['task']} |")
        lines.append(chr(10) + "</details>")
        open(os.path.join(ROOT, "issues", f"{pkg}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        open(os.path.join(ROOT, "issues", f"{pkg}.title.txt"), "w", encoding="utf-8").write(title)
        assign.append([pkg, title, ""])
    # assignments: eleven people. P01 to P11 one package each; P12a to P12d (the twelfth package, split by weakness) are extra work for four of them
    with open(os.path.join(ROOT, "assignments.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["package", "issue_title", "github_username"])
        for row in assign:
            w.writerow(row)
    print(len(briefs), "rows in", len(packages), "packages")
    print({k: len(v) for k, v in packages.items()})


if __name__ == "__main__":
    main()
