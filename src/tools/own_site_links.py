#!/usr/bin/env python3
"""Keep the folio rail's links to THIS site's own pages on this site (the beans icon, its count, the
folders ihris renders), around cat-harness's rail-standalone-pages.ts --foreign-site.

  python3 src/tools/own_site_links.py --harness cat-harness/docs/_data/harness.json   # before the rail
  python3 src/tools/own_site_links.py --site _site                                     # after the rail

Two platform pieces disagree for a folio that is the ROOT of its own site, and this bridges them
until cat-harness reconciles them (bean ihris-yvow):

- sync-docs-harness.ts writes the root instance's own pages root-relative (`/beans/`), while the
  foreign-site scope (lib/foreign-site-scope.ts) keeps a state graph's link only when it is under
  `/<instance>/`, so `/beans/` read as "not published on this site". --harness re-roots the folio's
  own root-relative paths in the navbar data under `/ihris/`; the scope then keeps them and turns them
  back into `/beans/`. Absolute (platform) links are left alone.
- the rail writes the row's `data-fa-root` as the PLATFORM's address, which navbar-row.js composes
  every root-relative href AND the badge's count.json with, so `/beans/` would open the platform's
  work plan and show its count. --site points `data-fa-root` at this page's own site root, relative
  to the page, so links and counts resolve on whichever deploy serves the page (live or staging).
  The chrome's code still loads from the platform: those are absolute URLs, untouched.
"""
import json
import os
import re
import sys

INSTANCE = "ihris"
ROW = re.compile(r'(<script type="application/json" id="fa-navbar-row" data-fa-root=")[^"]*(")')


def declared_pages():
    """The site paths ihris's OWN visualisers publish (`docs/x/index.html` -> `/x/`), read from ihris.json.
    Only these are re-rooted: a root-relative path the platform composed for another instance (its
    `/cat-harness/uploads/...`) is not ihris's and keeps the scope's 'not published on this site'."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    decl = json.load(open(os.path.join(root, "ihris.json"), encoding="utf-8"))
    out = set()
    for x in decl.get("directories") or []:
        v = (x.get("coverage") or {}).get("visualiser")
        for ref in ([v] if isinstance(v, str) else [y["ref"] for y in v or []]):
            page = re.sub(r"^docs/", "", ref)
            page = re.sub(r"(^|/)index\.(html|md)$", r"\1", page)
            out.add("/" + page)
    return out


OWN = None


def own(p):
    return f"/{INSTANCE}{p}" if isinstance(p, str) and p in OWN else p


def harness(path):
    global OWN
    OWN = declared_pages()
    d = json.load(open(path, encoding="utf-8"))
    nb = d.get("navbar") or {}
    nb["hrefs"] = {k: own(v) for k, v in (nb.get("hrefs") or {}).items()}
    for f in nb.get("folders") or []:
        if "path" in f:
            f["path"] = own(f["path"])
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"own_site_links: {len(nb['hrefs'])} icon link(s) and the folders re-rooted under /{INSTANCE}/")


def site(root):
    n = 0
    for d, _, fs in os.walk(root):
        for name in fs:
            if not name.endswith(".html"):
                continue
            p = os.path.join(d, name)
            text = open(p, encoding="utf-8").read()
            up = os.path.relpath(root, d).replace(os.sep, "/")
            new, k = ROW.subn(lambda m: m.group(1) + ("." if up == "." else up) + m.group(2), text)
            if k:
                open(p, "w", encoding="utf-8").write(new)
                n += 1
    print(f"own_site_links: {n} page(s) resolve their own links and counts on this site")


if __name__ == "__main__":
    if "--harness" in sys.argv:
        harness(sys.argv[sys.argv.index("--harness") + 1])
    elif "--site" in sys.argv:
        site(sys.argv[sys.argv.index("--site") + 1])
    else:
        sys.exit("usage: own_site_links.py --harness <harness.json> | --site <dir>")
