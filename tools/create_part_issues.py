#!/usr/bin/env python3
"""Lead only. Creates the part issues from issues/parts.csv on GitHub (resumable: finished ones are in issues/created.csv).

    python tools/create_part_issues.py            # edits the 11 first issues (#16-#26) and creates all other parts, assigned
    python tools/create_part_issues.py --close-old   # then closes the old Step 2 / Step 3 issues #1-#15 with a pointer
Every person must have accepted the invitation first (GitHub silently skips assignees who have not).
"""
import csv, os, shutil, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "Barath-BDK/dataset-a-closed-models"
GH = shutil.which("gh") or r"C:\Program Files\GitHub CLI\gh.exe"
CREATED = os.path.join(ROOT, "issues", "created.csv")


def gh(*a):
    r = subprocess.run([GH, *a], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit("gh failed: %s\n%s" % (" ".join(a[:4]), r.stderr.strip()))
    return r.stdout.strip()


def main():
    parts = list(csv.DictReader(open(os.path.join(ROOT, "issues", "parts.csv"), encoding="utf-8")))
    done = {}
    if os.path.exists(CREATED):
        done = {r["key"]: r["number"] for r in csv.DictReader(open(CREATED, encoding="utf-8"))}
    first_no = {}
    for i, p in enumerate(dict.fromkeys(x["package"] for x in parts if not x["package"].startswith("P12")), 1):
        first_no[p] = 15 + i
    if "--close-old" in sys.argv:
        close_old(parts, done)
        return
    for p in parts:
        key = p["key"]
        if key in done:
            continue
        body = os.path.join(ROOT, "issues", "parts", p["file"])
        if p["package"] in first_no and p["row_from"] == "1":
            num = str(first_no[p["package"]])
            gh("issue", "edit", num, "-R", REPO, "--title", p["title"], "--body-file", body)
        else:
            args = ["issue", "create", "-R", REPO, "--title", p["title"], "--body-file", body, "--assignee", p["assignee"]]
            for l in p["labels"].split(","):
                args += ["--label", l]
            num = gh(*args).rstrip("/").split("/")[-1]
            time.sleep(2)
        done[key] = num
        new = not os.path.exists(CREATED)
        with open(CREATED, "a", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(["key", "number"])
            w.writerow([key, num])
        print(key, "-> #" + num, flush=True)


def close_old(parts, done):
    old = list(csv.DictReader(open(os.path.join(ROOT, "assignments_filled.csv"), encoding="utf-8-sig")))
    for i, a in enumerate(old, 1):
        pkg = a["package"]
        nums = [done[p["key"]] for p in parts if p["package"] == pkg and p["row_from"] != "1" or (p["package"] == pkg and pkg.startswith("P12"))]
        nums = [n for n in nums]
        text = ("This issue is replaced by smaller issues of 10 prompts each (one chat each): "
                + ", ".join("#" + n for n in nums) + ". Please use those. Nothing to do here.")
        gh("issue", "comment", str(i), "-R", REPO, "--body", text)
        gh("issue", "close", str(i), "-R", REPO, "--reason", "not planned")
        print("closed #%d" % i, flush=True)


if __name__ == "__main__":
    main()
