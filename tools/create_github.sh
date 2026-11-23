#!/usr/bin/env bash
# Creates the GitHub repository, the labels and one issue per package, and assigns the issues.
# Needs the GitHub CLI (gh) and a login:  gh auth login
# Fill assignments.csv (column github_username) first. Packages with an empty name get an issue without an assignee.
#   tools/create_github.sh my-org/dataset-a-closed-models [private|public] [--skip-repo] [--invite]
set -euo pipefail
cd "$(dirname "$0")/.."
REPO="${1:?usage: create_github.sh owner/name [private|public] [--skip-repo] [--invite]}"
VIS="${2:-private}"
SKIP=0; INVITE=0
for a in "$@"; do [ "$a" = "--skip-repo" ] && SKIP=1; [ "$a" = "--invite" ] && INVITE=1; done
command -v gh >/dev/null || { echo "The GitHub CLI (gh) is not installed: https://cli.github.com/ then gh auth login"; exit 1; }
gh auth status >/dev/null

if [ "$SKIP" = 0 ]; then
  if [ ! -d .git ]; then git init -b main >/dev/null; git add -A; git commit -m "Initial commit: dataset A (closed models) job" >/dev/null; fi
  gh repo create "$REPO" "--$VIS" --source . --remote origin --push
fi

for l in "model:chatgpt 10a37f" "model:gemini 4285f4" "model:claude d97757" "lang:python 3572a5" "lang:c 555555" "lang:cpp f34b7d" "lang:go 00add8" "package 0e8a16" "question d876e3"; do
  set -- $l; gh label create "$1" --color "$2" --repo "$REPO" --force >/dev/null
done

tail -n +2 assignments.csv | while IFS=, read -r pkg title user; do
  user="$(echo "${user:-}" | tr -d '\r" ')"
  model="$(echo "$pkg" | cut -d_ -f2)"; lang="$(echo "$pkg" | cut -d_ -f3)"
  args=(issue create --repo "$REPO" --title "$(cat "issues/$pkg.title.txt")" --body-file "issues/$pkg.md" --label "package,model:$model,lang:$lang")
  if [ -n "$user" ]; then
    [ "$INVITE" = 1 ] && gh api -X PUT "repos/$REPO/collaborators/$user" -f permission=push >/dev/null
    args+=(--assignee "$user")
  else
    echo "WARNING: no GitHub user for $pkg: issue created without an assignee"
  fi
  gh "${args[@]}"
done
echo "Done. Protect the main branch (Settings > Branches) so that it only accepts pull requests."
