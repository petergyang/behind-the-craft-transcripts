#!/usr/bin/env bash
# Weekly transcript archive sync: fetch new episodes, validate, commit only
# updater-owned paths, push, then rebuild the personal-os search index.
# Never pulls, merges, rebases, resets, or force-pushes. Prints a JSON summary.
set -euo pipefail

REPO="/Users/peteryang/Projects/behind-the-craft-transcripts"
PERSONAL_OS="/Users/peteryang/Projects/personal-os"
PY=/usr/bin/python3
cd "$REPO"

fail() { echo "{\"status\":\"failed\",\"reason\":\"$1\"}"; exit 1; }

[ "$(git branch --show-current)" = "main" ] || fail "branch is not main"
PRE_STATUS="$(git status --short)"
[ -z "$(git diff --cached --name-only)" ] || fail "staged changes already present"
if git status --short | grep -vE '^\?\? drafts/|^ M (README\.md|scripts/fetch_new_episodes\.py)$|^ M (index|transcripts)/' | grep -q .; then
  fail "tracked changes outside README.md, index/, transcripts/, or scripts/fetch_new_episodes.py"
fi

git fetch origin
read -r BEHIND AHEAD <<<"$(git rev-list --left-right --count origin/main...main)"
[ "$BEHIND" = "0" ] || fail "origin/main is ahead or diverged"

$PY scripts/fetch_new_episodes.py --cookies-from-browser chrome
$PY scripts/fetch_new_episodes.py --check-only | grep -q 'missing=0' || fail "check-only did not report missing=0"

PYTHONPYCACHEPREFIX="${TMPDIR:-/tmp}/btc-transcripts-pyc" $PY -m py_compile scripts/fetch_new_episodes.py scripts/add_frontmatter.py scripts/build-index.py
ruby -e 'require "yaml"; YAML.load_file(".github/workflows/update-transcripts.yml")'
git diff --check

# Stage only updater-owned paths that changed this run.
STAGE=()
while IFS= read -r line; do
  path="${line:3}"
  case "$path" in
    transcripts/*.md|index/*.md|README.md) STAGE+=("$path") ;;
  esac
done < <(git status --short)

COMMIT=""
if [ "${#STAGE[@]}" -gt 0 ]; then
  git add -- "${STAGE[@]}"
  git diff --cached --check
  git commit -q -m "Add new Behind the Craft transcripts (automated)"
  COMMIT="$(git rev-parse --short HEAD)"
fi
[ "$AHEAD" = "0" ] && [ -z "$COMMIT" ] || git push -q origin main

read -r BEHIND AHEAD <<<"$(git fetch origin >/dev/null 2>&1; git rev-list --left-right --count origin/main...main)"
[ "$BEHIND$AHEAD" = "00" ] || fail "origin/main does not match main after push"
POST_STATUS="$(git status --short)"

cd "$PERSONAL_OS"
python3 scripts/reference_index.py >/dev/null
S1="$(python3 scripts/search_reference.py "reward hacked" --source transcript --limit 1)"
S2="$(python3 scripts/search_reference.py "Codex product work" --source newsletter --limit 1)"
[ -n "$S1" ] && [ -n "$S2" ] || fail "search verification returned no result"

python3 - "$COMMIT" "${#STAGE[@]}" "$PRE_STATUS" "$POST_STATUS" <<'EOF'
import json, sys
commit, staged, pre, post = sys.argv[1:5]
print(json.dumps({
    "status": "ok",
    "commit": commit or None,
    "files_committed": int(staged),
    "pre_existing_status": pre.splitlines(),
    "remaining_status": post.splitlines(),
    "index_rebuilt": True,
}, indent=2))
EOF
