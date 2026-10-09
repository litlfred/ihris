---
# ihris-0uoj
title: Migrate to a folio-assistant-core dependent repository (as who-iris)
status: completed
type: task
tags:
    - platform
created_at: 2026-10-09T10:48:54Z
updated_at: 2026-10-09T10:48:54Z
---

Owner, 2026-10-09: *"migrrate to new folio-assistant-core dependent repo https://litlfred.github.io/who-iris"*.

litlfred/folio-assistant no longer holds folio-assistant-core/ or cat-harness/ in its tree: each layer is its own repository, and folio-assistant is an index of remote mounts. CI cloned folio-assistant main for the zod schemas, so after the cutover it found no layers and every commit failed (`CI: no folio-assistant checkout`).

ihris now depends on folio-assistant-core as litlfred/who-iris does:

- `ihris.json` declares `needs: ["folio-assistant-core"]` and `repository`.
- `index.config.json` (`folio-index-config/v1`) has ihris local at `.` and pins folio-assistant-core plus its closure (cat-harness, cat-harness-tools, bootstrap, bootstrap-tools) to SHAs, at the pins core's and cat-harness's own indexes name. Trust is by the owner's consent, recorded with this request as evidence.
- `index.lock.json` was written by cat-harness's `mount:remote`. `src/tools/mount_platform.sh` replays it with cat-harness's `mount-from-lock.ts`, which on a fresh clone is fetched alone at the locked SHA. The mounts land at `<name>/`, inside the generated `.gitignore` block.
- `src/tools/folio_platform.py` is the one place tools learn where the layers are (who-iris's `platform.ts`). validate.py and qa.py skip the mounts.
- `package.json` + `bun.lock`: zod, yaml, playwright, the packages ihris's code and the mounted schemas import.

The cutover also brought these upstream schema changes, which ihris now follows:

- directories (and `remoteGraphs`) declare `graphTypologies`, not `graphKinds`;
- core reserves a declaration's `source` for `{kind: "git", repository, ref}` (bean `bamf`), so ihris's own provenance key is now `upstream`;
- core's `toSkos()` adds `rdfs` to the context, plus `rdfs:isDefinedBy`, `dcterms:requires`, own term IRIs and ordered collections. `build_glossary.py`'s mirror follows it.

QA: `platform-dependency` covers `folio-index-config/v1` and `cat-harness-mount-lock/v1`. ihris must be the local root, every need must be a remote mount, the lock must pin exactly those SHAs, and .gitignore must keep every mount out. It was shown to fail on a bumped pin, an unignored mount, a dropped need and a stray lock entry.
