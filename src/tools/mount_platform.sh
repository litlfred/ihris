#!/usr/bin/env bash
# Lay down the folio-assistant platform layers this folio depends on, from the committed
# index.lock.json, then install the npm packages they and ihris's own code import.
#
#   bash src/tools/mount_platform.sh           # mount (or refresh) every locked layer, then bun install
#   bash src/tools/mount_platform.sh --check   # no network: is every locked layer on disk and intact?
#
# ihris is a folio-assistant-core DEPENDENT repository (as litlfred/who-iris is): index.config.json
# pins each layer to a SHA, index.lock.json records what each resolved to (tree digests included),
# and the layers land at <root>/<name>/, git-ignored by the generated block in .gitignore.
#
# The replay is cat-harness-tools' own `mount-from-lock.ts` (cat-harness's until the 70lx move
# took the harness's code to cat-harness-tools), reused rather than restated: it imports only
# node:*, verifies every directory against the lock's treeDigest, and never writes over a path
# that holds somebody's work. It lives INSIDE cat-harness-tools, which is itself one of the layers
# it mounts, so on a fresh clone it is fetched alone first, at the very SHA the lock pins
# cat-harness-tools to (a raw URL at a commit SHA is content-addressed by git).
#
# To bump a pin: edit index.config.json, then re-run cat-harness-tools' `remote-mount.ts` (it
# rewrites index.lock.json and the .gitignore block); `validate.py` fails when the three disagree.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

script="cat-harness-tools/scripts/mount-from-lock.ts"
if [ ! -f "$script" ]; then
  sha="$(python3 -c 'import json; print(next(m["ref"] for m in json.load(open("index.lock.json"))["mounts"] if m["harness"] == "cat-harness-tools"))')"
  mkdir -p .build
  script=".build/mount-from-lock.$sha.ts"
  [ -f "$script" ] || curl -sSfL -o "$script" "https://raw.githubusercontent.com/litlfred/cat-harness-tools/$sha/scripts/mount-from-lock.ts"
fi

if [ "${1:-}" = "--check" ]; then
  exec bun "$script" --check --root "$ROOT"
fi
bun "$script" --root "$ROOT"
bun install --frozen-lockfile
