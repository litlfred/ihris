#!/usr/bin/env bash
# Build the iHRIS 5 IG with fhir-harness, from the source ihris5.json pins, into one site
# directory published (only) on gh-pages at /ihris/ihris5/ by .github/workflows/ihris5-ig.yml.
#
#   bash src/tools/build_ihris5_ig.sh [--out <dir>] [--baseurl /ihris/ihris5]
#
# The pipeline is fhir-harness's, end to end; nothing here re-implements a step:
#
#   1. source      src/tools/mount_sources.py mounts iHRIS/iHRIS at the pinned commit (ihris5-source/).
#   2. workspace   the IG is copied to .build/ihris5-ig/ and the declared patches
#                  (src/ihris5/ig-build-patches.json) are applied to the COPY only.
#   3. AST         litlfred/fhir-ig-publisher's ast-export (pinned below), Maven-built, runs ONE
#                  ordinary IG Publisher build (SUSHI first) and writes the AST beside output/.
#   4. index       fhir-harness ast-to-artifact-index.ts: the artefact index, from the AST.
#                  ingest-ig-menu.ts: the IG's menu, from its sushi-config.yaml at the pin.
#   5. pages       gen-ig-pages.ts: one THIN page per artefact, in IG-site mode (owner, 2026-10-11,
#                  option A: "tiny html w/ dynamic load from json(ld) KG"; thin is fhir-harness's
#                  default since 2026-10-12, "make thin default"): each artifact/<Type>-<id>.html is a
#                  few KB of identity and a pointer to its JSON-LD node (artifact/<Type>-<id>.jsonld,
#                  fhir-harness ig-artifact-jsonld.ts), plus the index node artifact/index.jsonld,
#                  drawn in the browser by one shared renderer (assets/ig-artifact.js).
#   6. site        cat-harness compose-docs.ts --shell (the platform chrome, scoped to ihris)
#                  + fhir-harness stage-ig-sites.ts (the IG's own narrative and menu, composed at
#                  the root) + Jekyll with just-the-docs, the gem the platform's Gemfile pins. Thin by
#                  default: artifacts.html and toc.html are shells over artifact/index.jsonld, and the
#                  narrative pages wear fhir-harness's thin layout, prose kept, chrome linked. Then
#                  cat-harness-tools rail-standalone-pages.ts gives every page the rail, LINKED
#                  (the platform's navbar css/js by URL), never inlined.
#   7. bytes       the AST's resources at <out>/ast-data/. The Publisher's own HTML (output/) is
#                  NOT copied: it is not deployed (owner, 2026-10-11), so the artefact index claims
#                  no "published" address and the pages draw no links to it. Then the JSON-LD
#                  nodes' QA (ig-artifact-jsonld.ts check): one node per artefact, each its own,
#                  and every resource it names on the site.
#
# Needs: the platform mounted (src/tools/mount_platform.sh, which includes fhir-harness), java 17+,
# maven, node with fsh-sushi, ruby with bundler, and the FHIR package hosts (packages.fhir.org,
# build.fhir.org, fhir.github.io, tx.fhir.org). Where a package host is refused, seed the cache
# first: fhir-harness's fhir-cache-seed-npm.ts (npm, template repos, --mirror).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

OUT="$ROOT/.build/ihris5-ig/site"
BASEURL="/ihris/ihris5"
while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT="$(mkdir -p "$2" && cd "$2" && pwd)"; shift 2 ;;
    --baseurl) BASEURL="$2"; shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

# The AST producer, pinned: litlfred/fhir-ig-publisher@claude/ast-export (fhir-harness Tool ig-ast-export).
FIGP_REPO="https://github.com/litlfred/fhir-ig-publisher"
FIGP_REF="bfa914b3910356019b646d64e723e3589392a459"
LABEL="iHRIS 5 Implementation Guide"
W="$ROOT/.build/ihris5-ig"
step() { printf '\n== %s\n' "$*"; }

step "1. source (pinned by src/ihris5/ihris5.json)"
python3 src/tools/mount_sources.py
SRC="$(python3 src/tools/mount_sources.py --print ihris5)"

step "2. workspace copy, declared patches applied to the copy"
rm -rf "$W/ig" "$W/stage" "$W/shell" "$W/work" "$W/jekyll"
mkdir -p "$W"
cp -r "$SRC" "$W/ig"
rm -rf "$W/ig/output" "$W/ig/fsh-generated" "$W/ig/output-ast" "$W/ig/temp" "$W/ig/template"
python3 src/tools/apply_ig_patches.py src/ihris5/ig-build-patches.json "$W/ig"

step "3. AST: one ordinary IG Publisher build through ast-export"
F="$W/fhir-ig-publisher"
if [ "$(git -C "$F" rev-parse HEAD 2>/dev/null || true)" != "$FIGP_REF" ] || [ ! -f "$F/ast-export/cp.txt" ]; then
  rm -rf "$F" && mkdir -p "$F"
  git -C "$F" init -q
  git -C "$F" fetch -q --depth 1 "$FIGP_REPO" "$FIGP_REF"
  git -C "$F" checkout -q FETCH_HEAD
  (cd "$F/ast-export" && mvn -q -B package -DskipTests && mvn -q -B dependency:build-classpath -Dmdep.outputFile=cp.txt)
fi
# The packages the IG names, where the hosts are reachable this is a no-op the Publisher repeats.
bun run fhir-harness/scripts/fhir-cache-seed-npm.ts --sushi-config "$W/ig/sushi-config.yaml" || true
(cd "$F/ast-export" && java -Xmx6g -cp "target/classes:$(cat cp.txt)" org.hl7.fhir.igtools.ast.AstExportCli -ig "$W/ig" ${IG_TX:+-tx "$IG_TX"})
test -f "$W/ig/output-ast/manifest.json" || { echo "no AST was written" >&2; exit 1; }

step "4. index and menu"
I="$W/stage/ihris5"
mkdir -p "$I/fhir-artifact-index"
# The staging copy of the declaration also declares the IG-site docs directory, which exists only
# in this build (declaring it in the committed ihris5.json would declare a directory that is not there).
python3 - "$ROOT/src/ihris5/ihris5.json" "$I/ihris5.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
d.setdefault("directories", []).append({"id": "ihris5-ig-site", "path": "docs/", "graphTypologies": ["docs"], "igSite": True,
    "description": "BUILD-TIME ONLY: the IG's artefact pages, generated from the AST by src/tools/build_ihris5_ig.sh."})
json.dump(d, open(sys.argv[2], "w"), indent=2)
PY
bun run fhir-harness/scripts/ingest-ig-menu.ts --source "$SRC" --out "$I/fhir-artifact-index"
# No --published-base: the Publisher's HTML is not deployed (owner, 2026-10-11), so no artefact
# claims a published address.
bun run fhir-harness/scripts/ast-to-artifact-index.ts --ast "$W/ig/output-ast" --instance-id ihris5 \
  --out "$I/fhir-artifact-index/index.json"

step "5. artefact pages (IG-site mode)"
# --compiled-data is a path from the DOCS root, which in an IG site is the site root: the resources
# are at <site>/ast-data/. (It was ../ast-data, which pointed one level above the site, so every
# full artefact page's resource answered 404.)
bun run fhir-harness/scripts/gen-ig-pages.ts --instance "$I" --label "$LABEL" \
  --index "$I/fhir-artifact-index/index.json" --out "$I/docs" --compiled-data ast-data \
  --jsonld-base "https://litlfred.github.io$BASEURL/"

step "6. site: platform chrome scoped to ihris, the IG composed at its root, Jekyll"
# The mounted cat-harness carries the PLATFORM's harness list; regenerate it from this checkout so
# the chrome names ihris and what it needs (no smart-base, no smart-trust).
bun run cat-harness-tools/scripts/sync-docs-harness.ts
bun run cat-harness-tools/scripts/compose-docs.ts --out "$W/shell" --shell --instance ihris --title "$LABEL" --link-root https://litlfred.github.io/ihris
bun run cat-harness-tools/scripts/gen-navbar-include.ts --instance ihris --link-root https://litlfred.github.io/ihris \
  --title "$LABEL" --out "$W/shell/_includes/generated/navbar-footer.html"
(cd "$W/stage" && bun run "$ROOT/fhir-harness/scripts/stage-ig-sites.ts" --work "$W/work" --baseurl "$BASEURL" \
  --only ihris5 --source "$W/ig" --compose-into "$W/shell" --compose-at-root)
# just-the-docs as the gem the platform's Gemfile.lock pins, not a remote_theme download.
printf 'remote_theme: ""\ntheme: just-the-docs\nplugins: []\ntitle: "%s"\n' "$LABEL" > "$W/jekyll-override.yml"
rm -rf "$OUT" && mkdir -p "$OUT"
BUNDLE_GEMFILE="$ROOT/cat-harness/site-chrome/Gemfile" bundle exec jekyll build --source "$W/shell" --destination "$OUT" \
  --baseurl "$BASEURL" --config "$W/shell/_config.yml,$W/jekyll-override.yml"
bun run fhir-harness/scripts/build-ig-site.ts --dedupe-ids "$OUT"
# The thin pages carry no rail of their own; they ask for it LINKED (folio-navbar: linked).
# Pages Jekyll already railed are skipped. Before the sweep below, which keeps only referenced rail data.
bun run cat-harness-tools/scripts/rail-standalone-pages.ts --site "$OUT" --built cat-harness --foreign-site \
  --home-label "iHRIS Knowledge Base" --instance ihris
# The platform's own data, copied in with the shell, is not this site's: its library, glossary,
# diagrams and any rail data no page here references.
rm -rf "$OUT/assets/library" "$OUT/assets/glossary" "$OUT/assets/img/uml"
for r in "$OUT"/assets/navbar/rail-*.js; do
  [ -e "$r" ] || continue
  grep -rlq --include='*.html' "$(basename "$r")" "$OUT" || rm -f "$r"
done

step "7. the AST's resources (the Publisher's HTML is not deployed)"
mkdir -p "$OUT/ast-data" && cp -r "$W/ig/output-ast/resources" "$OUT/ast-data/resources"
touch "$OUT/.nojekyll"
bun run fhir-harness/scripts/ig-artifact-jsonld.ts check --index "$I/fhir-artifact-index/index.json" --dir "$OUT"
python3 - "$OUT/artifact" <<'PY'
import os, sys
d = sys.argv[1]
sizes = [os.path.getsize(os.path.join(d, f)) for f in os.listdir(d) if f.endswith(".html")]
print(f"artefact pages: {len(sizes)}, mean {sum(sizes) / max(len(sizes), 1) / 1024:.1f} KB, max {max(sizes, default=0) / 1024:.1f} KB")
PY
echo "site: $(find "$OUT" -name '*.html' | wc -l) html file(s) -> $OUT (base $BASEURL)"
