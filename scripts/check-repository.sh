#!/usr/bin/env bash
# Read-only repository baseline check. No installation or system changes.
set -euo pipefail
cd "$(dirname "$0")/.."
for file in README.md LICENSE SECURITY.md CONTRIBUTING.md CHANGELOG.md; do
  if [[ ! -s "$file" ]]; then
    printf 'Missing or empty: %s\n' "$file" >&2
    exit 1
  fi
done
printf 'Repository documentation baseline: OK\n'
