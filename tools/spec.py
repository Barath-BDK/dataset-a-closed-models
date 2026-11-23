"""Dataset A (closed models) as data: columns, allowed values, distribution. Source: docs/Dataset_A_Closed_Models.docx (version 1, 23 November 2026)."""

COLUMNS = ["sample_id", "language", "cwe", "case_type", "label", "task_description", "cwe_detail", "n_lines", "band", "build_style", "source",
           "fix_type", "code", "fixed_code", "vulnerable_lines", "sink", "n_tokens", "pattern", "runnable", "exploit_confirmed",
           "fix_resists_exploit", "behaviour_preserved", "label_source", "label_confidence", "group_id", "origin", "suggested_split"]
EXTRA_COLUMNS = ["generator", "prompt_id", "notes"]
ALL_COLUMNS = COLUMNS + EXTRA_COLUMNS          # 30 columns

LANGUAGES = ["python", "c", "cpp", "go"]
LANG_TITLE = {"python": "Python", "c": "C", "cpp": "C++", "go": "Go"}
LANG_SHORT = {"python": "py", "c": "c", "cpp": "cpp", "go": "go"}
CWES = ["CWE-89", "CWE-78", "CWE-22", "CWE-338"]
CWE_SHORT = {"CWE-89": "sqli", "CWE-78": "cmdi", "CWE-22": "pt", "CWE-338": "rnd"}
MODELS = [("chatgpt", "gpt", "ChatGPT"), ("gemini", "gem", "Gemini"), ("claude", "cla", "Claude")]
MODEL_PREFIX = {m: p for m, p, _ in MODELS}
MODEL_TITLE = {m: t for m, _, t in MODELS}

CASE_TYPES = ["normal", "hard_positive", "safe", "hard_negative", "no_code"]
VULNERABLE_CASES = {"normal", "hard_positive"}
BANDS = ["1-5", "6-10", "11-20", "21-40", "41-100"]
BAND_TOP = (5, 10, 20, 40, 100)
SOURCES = ["function_argument", "web_request", "file", "environment", "command_line", "database_value", "network_message", "not_applicable"]
LABEL_SOURCES = ["dynamic_exploit", "two_reviewers", "by_design"]
CONFIDENCE = ["high", "medium"]

# section 4.1: rows per cell (all three models) and band counts per cell of 75
CASE_PER_CELL = {"normal": 25, "hard_positive": 12, "safe": 12, "hard_negative": 20, "no_code": 6}
BAND_PER_CELL = {"1-5": 7, "6-10": 19, "11-20": 22, "21-40": 19, "41-100": 8}
ROWS_PER_CELL = 75
ROWS_PER_MODEL_PER_CELL = 25
MAX_FIX_LINES = 10
MAX_ROWS_PER_TASK = 3
MIN_TASKS_PER_CELL = 30
LEAK_WORDS = r"vulnerab|insecure|\bunsafe\b|exploit|inject|\bfixed\b|\bbug\b|attack|sanitiz|\bsecure\b|\bsafe\b"


def band_of(n):
    return next((b for b, top in zip(BANDS, BAND_TOP) if n <= top), "41-100")
