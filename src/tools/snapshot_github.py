#!/usr/bin/env python3
"""Snapshot an iHRIS GitHub repository into uploads/github/<repo>.json.

Records WHAT IS THERE, pinned at a commit, without copying content: the
commit, the licence, the top-level layout, every FSH definition (kind, name,
parent, title), every Markdown page (path and first heading) and the package
versions. build_kg.py turns the snapshot into catalogue nodes and an inventory.

Usage:  python3 src/tools/snapshot_github.py <clone-dir> <owner/repo> [title]
        (clone with: git clone --depth 1 https://github.com/<owner/repo>)
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP = {".git", "node_modules", "site", "output", "fsh-generated", "temp", "template"}


def git(clone, *a):
    return subprocess.check_output(["git", "-C", clone, *a], text=True).strip()


def main(clone, full, title=None):
    owner, repo = full.split("/")
    lic = None
    for n in ("LICENSE", "LICENSE.md", "COPYING"):
        p = os.path.join(clone, n)
        if os.path.exists(p):
            head = open(p, encoding="utf-8", errors="replace").read(400)
            lic = ("LGPL-3.0" if "LESSER GENERAL PUBLIC LICENSE" in head and "Version 3" in head else
                   "GPL-3.0" if "GENERAL PUBLIC LICENSE" in head and "Version 3" in head else
                   "Apache-2.0" if "Apache License" in head else head.splitlines()[0].strip())
    fsh, pages, pkgs = [], [], []
    for dp, dns, fns in os.walk(clone):
        dns[:] = sorted(d for d in dns if d not in SKIP)
        for fn in sorted(fns):
            p = os.path.join(dp, fn)
            r = os.path.relpath(p, clone)
            if fn.endswith(".fsh"):
                cur = None
                for line in open(p, encoding="utf-8", errors="replace"):
                    m = re.match(r"^(Profile|Extension|Logical|Resource|CodeSystem|ValueSet|Instance|Invariant|RuleSet|Mapping|Alias)\s*:\s*(\S+)", line)
                    if m:
                        cur = {"file": r, "kind": m.group(1), "name": m.group(2)}
                        fsh.append(cur)
                    elif cur and (m := re.match(r"^(Parent|InstanceOf|Title|Id|Usage)\s*:\s*(.+)", line)):
                        cur[m.group(1).lower()] = m.group(2).strip().strip('"')
            elif fn.endswith(".md"):
                h = next((l.lstrip("#").strip() for l in open(p, encoding="utf-8", errors="replace") if l.startswith("#")), None)
                pages.append({"path": r, "heading": h})
            elif fn == "package.json":
                try:
                    d = json.load(open(p))
                    pkgs.append({"path": r, "name": d.get("name"), "version": d.get("version")})
                except ValueError:
                    pass
    nav = None
    mk = os.path.join(clone, "mkdocs.yml")
    if os.path.exists(mk):
        nav = [l.strip() for l in open(mk) if re.match(r"\s+- ", l)]
    snap = {
        "repo": repo, "owner": owner, "title": title or full, "url": f"https://github.com/{full}",
        "branch": git(clone, "rev-parse", "--abbrev-ref", "HEAD"), "commit": git(clone, "rev-parse", "HEAD"),
        "committedAt": git(clone, "log", "-1", "--format=%cI"), "licence": lic,
        "topLevel": sorted(x for x in os.listdir(clone) if x != ".git"),
        "fshDefinitions": fsh, "markdownPages": pages, "packages": pkgs, "mkdocsNav": nav,
        "note": "Inventory only. File CONTENTS are not copied; every entry is a path at `commit`. "
                + ("No licence file: content is referenced, never reproduced." if lic is None else ""),
    }
    out = os.path.join(ROOT, "uploads", "github", f"{repo}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(snap, open(out, "w"), indent=2, ensure_ascii=False)
    print(out, len(fsh), "fsh defs,", len(pages), "md pages")


if __name__ == "__main__":
    main(*sys.argv[1:])
