"""Pages for the instances other than the data model (bean ihris-k1sv).

Imported by build_site.py. Every page is generated from committed, schema-validated
data (src/tools/validate.py; src/schemas/bindings.json). Licence decides what a page
may reproduce (AGENTS.md §2.4):

  Launchpad sources, modules, data lists   GPL: described in full, with source paths and checksums
  library/ihris-wiki help pages            GPL (shipped in the 4.3.3 release): rendered in full, with attribution
  library/ihris-admin-handbook             GFDL-1.2 text (stated in the export) and images (owner's permission): in full,
                                           with each article's revision and contributors; only while both are recorded
  library/ihris-use-cases                  the owner's permission (2026-09-23): in full, attributed; only while recorded
                                           People the reports name only as opaque actors (roles page)
  library/ihris-toolkit                    the text only while its declaration records a licence (the owner's
                                           permission, 2026-09-23, bean ihris-kngr); otherwise structure only.
                                           Reader comments never: third parties' words and names
  iHRIS/iHRIS (LGPL-3.0)                   inventory: FSH definition headers and paths
  iHRIS/ihris-documentation (no licence)   path and heading only
  src/ihris-data-dictionary, 4-on-fhir     this repository's own derived content: in full
"""
import collections
import glob
import html
import json
import os
import re
import shutil

import markdown

import build_site as bs

E, ROOT, REPO, RELEASE = bs.E, bs.ROOT, bs.REPO, bs.RELEASE
LP_INSTANCES = ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify", "ihris-plan", "openhie-pr"]
WIKI = "library/ihris-wiki/osi-help-4.3.3"

# The page each landing card opens (build_site.landing reads this).
INSTANCE_PAGE = {**{n: f"sources/{n}/index.html" for n in LP_INSTANCES},
                 "ihris5": "sources/ihris5/index.html", "ihris-toolkit": "library/toolkit/index.html",
                 "ihris-wiki": "library/wiki/index.html", "ihris-data-dictionary": "data-dictionary/index.html",
                 "ihris-4-on-fhir": "fhir/index.html", "ihris-admin-handbook": "library/handbook/index.html",
                 "ihris-use-cases": "library/use-cases/index.html"}
HANDBOOK = "library/ihris-admin-handbook"
USE_CASES = "library/ihris-use-cases"


def J(p):
    return bs.load(p)


def rows_table(head, rows, label=None, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    lab = f' aria-label="{E(label)}"' if label else ""
    return f'<div class="tscroll"><table{lab}{cls}><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def page(path, title, crumbs, inner, theme, current):
    r = lambda p: bs.rel(path, p)  # noqa: E731
    cr = " / ".join([f'<a href="{r(p)}">{E(n)}</a>' for p, n in crumbs] + [E(title)])
    body = f'<main id="main" tabindex="-1"><div class="crumbs">{cr}</div>\n<h1>{E(title)}</h1>\n{inner}\n</main>'
    return path, bs.shell(path, title, body, theme, current=current)


def md_to_html(text, link_map=None):
    """Markdown (front matter stripped) to HTML; `link_map(href)` may rewrite or drop links."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    out = markdown.markdown(text, extensions=["tables", "fenced_code"], output_format="html")
    if link_map:
        def sub(m):
            new = link_map(html.unescape(m.group(1)))
            if new is None:  # no page for it here: keep the words, drop the dead link
                return f'<span class="mute" title="not restored in this folio">{m.group(3)}</span>'
            return f'<a href="{E(new)}"{m.group(2)}>{m.group(3)}</a>'
        out = re.sub(r'<a href="([^"]*)"([^>]*)>(.*?)</a>', sub, out, flags=re.S)
    return out


# ------------------------------------------------------------------ Launchpad sources
def lp_records(inst):
    recs = [J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, "src", inst, "catalogue", "records", "*.json"))]
    return [r for r in recs if r["level"] == "series"], [r for r in recs if r["level"] in ("release", "milestone")]


def module_path(inst, mod):
    return f"sources/{inst}/modules/{mod}.html"


def sources_index(theme):
    path = "sources/index.html"
    projs = sorted((J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, "src/catalogue/records/project--*.json"))),
                   key=lambda p: p["project"]["name"])
    order = ["core", "tool", "related", "country-customization"]
    parts = []
    for c in order:
        rows = []
        for p in (x for x in projs if x["project"]["classification"] == c):
            pr = p["project"]
            here = pr["name"] if pr["name"] in LP_INSTANCES else None
            name = f'<a href="{E(bs.rel(path, INSTANCE_PAGE[here]))}">{E(pr["title"])}</a>' if here else E(pr["title"])
            rows.append([name, f'<code>{E(p["refs"].get("lp") or "")}</code>', E(pr.get("summary") or ""),
                         E(", ".join(pr.get("licences") or []) or "not stated"), f'<a href="{E(p["refs"]["web"])}">Launchpad</a>'])
        parts.append(f"<h2>{E(c.replace('-', ' ').capitalize())} ({len(rows)})</h2>" +
                     rows_table(["Project", "Branch", "Summary", "Licence", "Upstream"], rows, f"{c} projects"))
    gh = f'<p>On GitHub: <a href="{bs.rel(path, INSTANCE_PAGE["ihris5"])}">iHRIS 5</a>, pinned by commit.</p>'
    inner = (f"<p>The {len(projs)} Launchpad projects of the iHRIS Suite and around it, <b>described, never copied</b>: "
             "each is referenced by its <code>lp:</code> branch, with release files pinned by the MD5 Launchpad publishes. "
             "Core is the owner's call.</p>" + gh + "".join(parts))
    return page(path, "Sources", [("index.html", "Home")], inner, theme, "sources/index.html")


def lp_instance_page(inst, theme, have_modules):
    path = INSTANCE_PAGE[inst]
    decl = J(f"src/{inst}/{inst}.json")
    proj = J(f"src/catalogue/records/project--{inst}.json")["project"]
    series, rels = lp_records(inst)
    srows = [[f'<code>{E(s["series"]["name"])}</code>' + (" <b>(focus)</b>" if s["series"].get("isDevelopmentFocus") else ""),
              "<br>".join(f"<code>{E(b)}</code>" for b in s["series"].get("branches") or []) or "&mdash;",
              f'<a href="{E(s["refs"]["web"])}">Launchpad</a>'] for s in sorted(series, key=lambda s: s["series"]["name"])]
    def key(r):
        return (r["release"].get("released") or r["release"].get("expected") or "", r["release"]["name"])
    rrows = []
    for r in sorted(rels, key=key, reverse=True):
        rel_ = r["release"]
        files = "<br>".join(f'<a href="{E(f["url"])}">{E(f["name"])}</a> <span class="mute">md5 <code>{E(f["md5"] or "?")}</code></span>'
                            for f in rel_.get("files") or []) or "&mdash;"
        when = rel_.get("released") or (f'expected {rel_["expected"]}' if rel_.get("expected") else "&mdash;")
        notes = E((rel_.get("releaseNotes") or "")[:240]) + ("&hellip;" if len(rel_.get("releaseNotes") or "") > 240 else "")
        rrows.append([f'<a href="{E(r["refs"]["web"])}">{E(rel_["name"])}</a>', E(rel_.get("series") or ""), E(when),
                      notes or "&mdash;", files])
    extra = ""
    if have_modules:
        n = len(glob.glob(os.path.join(ROOT, "src", inst, "modules", RELEASE, "*.json")))
        ncls = len(glob.glob(os.path.join(ROOT, "src", inst, "data-model", RELEASE, "*.json")))
        nl = len(glob.glob(os.path.join(ROOT, "src", inst, "data-lists", RELEASE, "*.json")))
        extra = (f'<h2>Release {RELEASE}</h2><p><a href="{bs.rel(path, f"sources/{inst}/modules/index.html")}">{n} I2CE modules</a> &middot; '
                 f'<a href="{bs.rel(path, f"data-model/{inst}/index.html")}">{ncls} form classes</a> &middot; '
                 f'<a href="{bs.rel(path, f"sources/{inst}/data-lists.html")}">{nl} shipped data lists</a>, '
                 f'all derived from the MD5-verified <code>ihris-suite-{RELEASE}.tar.bz2</code>.</p>')
    else:
        extra = f"<h2>Release {RELEASE}</h2><p class=\"mute\">No modules extracted yet: the release tarball is needed (its MD5 is recorded below).</p>"
    inner = f"""<p>{E(proj.get('summary') or decl.get('description') or '')}</p>
<div class="badges"><span class="badge">{E(proj['classification'])}</span><span class="badge"><code>{E(decl['source']['lp'])}</code></span>
<span class="badge">licence {E(', '.join(proj.get('licences') or []) or 'not stated')}</span><span class="badge">{E(decl.get('materialization', ''))}</span></div>
<p><a href="{E(decl['source']['web'])}">launchpad.net/{E(inst)}</a>. Maintainer: {E((proj.get('maintainer') or {}).get('name') or 'not stated')}.</p>
{extra}
<h2>Series ({len(srows)})</h2>{rows_table(['Series', 'Branches', 'Upstream'], srows, 'Series')}
<h2>Releases and milestones ({len(rrows)})</h2>{rows_table(['Release', 'Series', 'Released', 'Notes', 'Files (MD5 from Launchpad)'], rrows, 'Releases')}"""
    return page(path, proj.get("title") or inst, [("index.html", "Home"), ("sources/index.html", "Sources")], inner, theme, "sources/index.html")


def modules_pages(inst, theme, cls_index):
    out = []
    mods = sorted((J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, "src", inst, "modules", RELEASE, "*.json"))),
                  key=lambda m: m["module"].lower())
    key = lambda m: m["id"].split("/module/")[-1]  # noqa: E731  (module@site: one page per site variant)
    all_keys = {}   # key -> package
    by_name = collections.defaultdict(list)  # module name -> [(key, site)]
    for f in glob.glob(os.path.join(ROOT, "src/*/modules", RELEASE, "*.json")):
        k = os.path.basename(f)[:-5]
        all_keys[k] = f.split(os.sep)[-4]
        by_name[k.split("@")[0]].append((k, k.split("@")[1] if "@" in k else None))
    idx_path = f"sources/{inst}/modules/index.html"
    rows = [[f'<a href="{E(key(m))}.html">{E(key(m))}</a>', E(m.get("displayName") or ""), E(m.get("description") or ""),
             E(m.get("site") or "")] for m in mods]
    crumbs = [("index.html", "Home"), ("sources/index.html", "Sources"), (INSTANCE_PAGE[inst], inst)]
    out.append(page(idx_path, f"{inst} modules ({RELEASE})", crumbs,
                    f"<p>{len(mods)} I2CE modules in {E(inst)} {RELEASE}.</p>" + rows_table(["Module", "Name", "Description", "Site"], rows, "Modules"),
                    theme, "sources/index.html"))

    def klink(path, k):
        pkg = all_keys.get(k)
        return f'<a href="{E(bs.rel(path, module_path(pkg, k)))}">{E(k)}</a>' if pkg else E(k)

    def mlink(path, name, site):
        """A requirement names a module, not a site variant: prefer this module's own site."""
        cands = by_name.get(name, [])
        pick = [k for k, st in cands if st == site] or ([cands[0][0]] if len(cands) == 1 else [])
        return klink(path, pick[0]) if pick else E(name)

    for m in mods:
        path = module_path(inst, key(m))
        req = ", ".join(mlink(path, q["module"], m.get("site")) + (f' <span class="mute">&ge;{E(q["atLeast"])}</span>' if q.get("atLeast") else "")
                        for q in m.get("requirements") or []) or "none"
        forms = ", ".join((f'<a href="{E(bs.rel(path, bs.page_of(cls_index[f["class"]], f["class"])))}">{E(f["form"])}</a>'
                           if f.get("class") in cls_index else E(f["form"])) for f in m.get("forms") or []) or "none"
        pages_ = ", ".join(f'<code>{E(p["page"])}</code>' for p in m.get("pages") or []) or "none"
        lists = ", ".join(f"{E(k)} ({v})" for k, v in (m.get("dataLists") or {}).items()) or "none"
        parent = klink(path, m["parent"].split("/module/")[-1]) if m.get("parent") else "none"
        s = m["source"]
        inner = f"""<p>{E(m.get('description') or '')}</p>
<div class="badges"><span class="badge">version {E(m.get('version') or '?')}</span><span class="badge">class <code>{E(m.get('className') or '?')}</code></span>
{f'<span class="badge">site {E(m["site"])}</span>' if m.get('site') else ''}</div>
{rows_table(['', ''], [['Display name', E(m.get('displayName') or '')], ['Parent module', parent], ['Requires', req], ['Forms', forms], ['Pages', pages_], ['Data lists', lists]], 'Module facts')}
<h2>Source</h2><p class="src"><code>{E(s['path'])}</code> in ihris-suite-{RELEASE}, sha256 <code>{E(s['sha256'])}</code>.
Release file MD5 <code>{E(s['releaseFileMd5'])}</code> (matches Launchpad).</p>"""
        out.append(page(path, key(m), crumbs + [(idx_path, "modules")], inner, theme, "sources/index.html"))
    return out


def data_lists_page(inst, theme):
    path = f"sources/{inst}/data-lists.html"
    lists = sorted((J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, "src", inst, "data-lists", RELEASE, "*.json"))),
                   key=lambda d: d["form"])
    parts = []
    for d in lists:
        prov = collections.Counter(r.get("provenance") for r in d["records"])
        sample = "; ".join(E(next(iter(r["fields"].values()), r["id"]) if r.get("fields") else r["id"]) for r in d["records"][:6])
        parts.append([f'<code>{E(d["form"])}</code>', str(len(d["records"])), E(", ".join(f"{k} {v}" for k, v in prov.items())),
                      sample + ("&hellip;" if len(d["records"]) > 6 else "")])
    inner = ("<p>Records each list ships in this package. <b>default</b> records install with a module; <b>sample</b> records illustrate "
             "one example deployment and are never a standard code set.</p>" +
             rows_table(["List", "Records", "Provenance", "First entries"], parts, "Data lists"))
    return page(path, f"{inst} data lists ({RELEASE})", [("index.html", "Home"), ("sources/index.html", "Sources"), (INSTANCE_PAGE[inst], inst)],
                inner, theme, "sources/index.html")


# ------------------------------------------------------------------ iHRIS 5 (GitHub)
def ihris5_page(theme):
    path = INSTANCE_PAGE["ihris5"]
    app, doc = J("src/ihris5/inventory/iHRIS.json"), J("src/ihris5/inventory/ihris-documentation.json")
    at = lambda repo, p: f'{repo["url"]}/blob/{repo["commit"]}/{p}'  # noqa: E731
    kinds = collections.defaultdict(list)
    for d in app["fshDefinitions"]:
        kinds[d["kind"]].append(d)
    fsh = "".join(f"<details><summary>{E(k)} ({len(v)})</summary>" + rows_table(["Name", "Id", "Title", "File"], [
        [E(d["name"]), f'<code>{E(d.get("id") or "")}</code>', E(d.get("title") or ""), f'<a href="{E(at(app, d["file"]))}">{E(d["file"].split("/")[-1])}</a>']
        for d in sorted(v, key=lambda d: d["name"])], f"{k} definitions") + "</details>" for k, v in sorted(kinds.items(), key=lambda kv: -len(kv[1])))
    dpages = rows_table(["Heading", "Path"], [[E(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", p["heading"] or "").strip()),
                                              f'<a href="{E(at(doc, p["path"]))}"><code>{E(p["path"])}</code></a>'] for p in doc["markdownPages"]], "Documentation pages")
    inner = f"""<p>iHRIS 5, the FHIR-based rewrite, is on GitHub. Both repositories are <b>pinned by commit</b> and inventoried by path; nothing is copied.</p>
<h2><a href="{E(app['url'])}">iHRIS/iHRIS</a></h2>
<div class="badges"><span class="badge">commit <code>{E(app['commit'][:12])}</code></span><span class="badge">{E(app['committedAt'][:10])}</span>
<span class="badge">licence {E(app.get('licence') or 'none')}</span></div>
<p>Top level: {', '.join(f'<code>{E(t)}</code>' for t in app.get('topLevel') or [])}.</p>
<h3>FHIR Implementation Guide: {len(app['fshDefinitions'])} FSH definitions</h3>{fsh}
<h2><a href="{E(doc['url'])}">iHRIS/ihris-documentation</a></h2>
<div class="badges"><span class="badge">commit <code>{E(doc['commit'][:12])}</code></span><span class="badge">{E(doc['committedAt'][:10])}</span>
<span class="badge">licence: none</span></div>
<p>No licence file, so pages are listed by <b>path and heading only</b> and link to GitHub at the pinned commit.</p>
<details><summary>{len(doc['markdownPages'])} documentation pages</summary>{dpages}</details>"""
    return page(path, "iHRIS 5", [("index.html", "Home"), ("sources/index.html", "Sources")], inner, theme, "sources/index.html")


# ------------------------------------------------------------------ toolkit (structure only)
def toolkit_pages(theme, out_dir):
    """The toolkit. Its text is published only while library/ihris-toolkit/ihris-toolkit.json
    records a licence (`stated`, or the owner's `permission`, bean ihris-kngr). Without one the
    pages fall back to structure only, so removing that record is enough to withdraw the text.
    Reader comments are never published: they are third parties' words and names."""
    out = []
    decl = J("library/ihris-toolkit/ihris-toolkit.json")
    lic = decl.get("licence")
    full = bool(lic and lic.get("status") in ("stated", "permission"))
    stages = sorted((J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, "library/ihris-toolkit/stages/*.json"))), key=lambda s: s["ordinal"])
    struct = J("library/ihris-toolkit/structure.json")
    idx = "library/toolkit/index.html"
    if full:
        how = ("published with the owner's permission (" + E(lic["grantedOn"]) + ")" if lic["status"] == "permission"
               else "published under " + E(lic.get("id", "")))
        attrib = E(lic["attribution"]).replace("toolkit.ihris.org", '<a href="https://toolkit.ihris.org/">toolkit.ihris.org</a>', 1)
        note = f'<p class="src">{attrib} Text {how}; reader comments from the original site are not reproduced.</p>'
    else:
        note = ('<p class="mute">No licence is recorded for toolkit.ihris.org, so this folio shows its <b>structure only</b>: stages, domains and '
                'tool titles, each linking to the original. The text stays on the toolkit.</p>')
    counts = collections.Counter((t["stage"], t["domain"]) for t in J("library/ihris-toolkit/tools-index.json"))
    head = ["Domain"] + [f'<a href="stage-{s["ordinal"]}.html">{E(s["name"])}</a>' for s in stages]
    rows = [[E(d)] + [str(counts.get((s["name"], d), "")) or "&middot;" for s in stages] for d in struct["domains"]]
    cards = "".join(f'<article class="card"><span class="kind">stage {s["ordinal"]}</span><h3>{E(s["name"])}</h3><p>{E(s["tagline"])}</p>'
                    f'<a class="go" href="stage-{s["ordinal"]}.html">{"Read the stage" if full else "Tools by domain"}</a></article>' for s in stages)
    inner = (f'<p><a href="https://toolkit.ihris.org/">toolkit.ihris.org</a>: {len(stages)} implementation stages across {len(struct["domains"])} domains, '
             f'{struct["toolCount"]} tools ({struct["toolsHostedOnToolkit"]} hosted on the toolkit).</p>{note}<div class="board">{cards}</div>'
             f'<h2>Tools per stage and domain</h2>{rows_table(head, rows, "Tools per stage and domain")}')
    out.append(page(idx, "iHRIS Implementation Toolkit", [("index.html", "Home"), ("library/index.html", "Library")], inner, theme, "library/index.html"))
    if full:
        os.makedirs(os.path.join(out_dir, "library/toolkit/images"), exist_ok=True)

    def tool_li(t):
        return (f'<li><a href="{E(t["href"])}">{E(t["title"])}</a> <span class="mute">{E(t.get("kind") or "")}'
                f'{"" if t.get("hostedOnToolkit") else " · external"}</span></li>')

    for s in stages:
        path = f"library/toolkit/stage-{s['ordinal']}.html"
        parts = [f'<p><i>{E(s["tagline"])}</i> &middot; <a href="{E(s["url"])}">this stage on toolkit.ihris.org</a></p>', note]
        if full:
            parts += [f"<p>{E(t)}</p>" for t in s.get("intro") or []]
            g = s.get("graphic")
            if g and g.get("localPath") and os.path.exists(os.path.join(ROOT, g["localPath"])):
                name = os.path.basename(g["localPath"])
                shutil.copy(os.path.join(ROOT, g["localPath"]), os.path.join(out_dir, "library/toolkit/images", name))
                parts.append(f'<figure class="wiki" style="margin:16px 0"><img src="images/{E(name)}" alt="{E(g.get("alt") or "")}">'
                             f'<figcaption class="legend">{E(g.get("caption") or "")}</figcaption></figure>')
        for d in s.get("domains") or []:
            objs = d.get("objectives") or []
            if full:
                items = "".join(f'<li>{E(o["objective"])}' + (f'<ul>{"".join(tool_li(t) for t in o.get("tools") or [])}</ul>' if o.get("tools") else "")
                                + "</li>" for o in objs)
                if items:
                    parts.append(f"<h2>{E(d['domain'])}</h2><ul>{items}</ul>")
            else:
                tools = [t for o in objs for t in o.get("tools") or []]
                if tools:
                    parts.append(f"<h2>{E(d['domain'])}</h2><ul>{''.join(tool_li(t) for t in tools)}</ul>")
        if full and s.get("challenges"):
            parts.append(f"<h2>Challenges</h2><p>{E(s['challenges'])}</p>")
        if full and s.get("technicalTerms"):
            parts.append("<h2>Technical terms</h2><dl>" + "".join(f"<dt><b>{E(t['term'])}</b></dt><dd>{E(t.get('definition') or '')}</dd>"
                                                             for t in s["technicalTerms"]) + "</dl>")
        out.append(page(path, f"Stage {s['ordinal']}: {s['name']}", [("index.html", "Home"), ("library/index.html", "Library"), (idx, "Toolkit")],
                        "".join(parts), theme, "library/index.html"))
    return out


# ------------------------------------------------------------------ wiki (GPL help pages, in full)
def wiki_pages(theme, out_dir):
    out = []
    st = J(f"{WIKI}/structure.json")
    imgs = {os.path.basename(i["file"]) for i in st.get("images") or []}
    if imgs:
        os.makedirs(os.path.join(out_dir, "library/wiki/images"), exist_ok=True)
        for n in imgs:
            shutil.copy(os.path.join(ROOT, WIKI, "images", n), os.path.join(out_dir, "library/wiki/images", n))

    def img_src(m):
        n = os.path.basename(html.unescape(m.group(2)))
        return f'{m.group(1)}images/{E(n)}"' if n in imgs else m.group(0)
    by_file = {}
    for p in st["pages"]:
        for s in p["shippedIn"]:
            by_file[os.path.basename(s)] = p["id"]
    ids = {p["id"] for p in st["pages"] if os.path.exists(os.path.join(ROOT, WIKI, "sections", p["id"] + ".md"))}

    def link_map(href):
        if href.startswith(("http:", "https:", "mailto:", "#")):
            return href
        f, _, frag = href.partition("#")
        pid = by_file.get(os.path.basename(f))
        if pid in ids:
            return f"{pid}.html" + (f"#{frag}" if frag else "")
        return None

    idx = "library/wiki/index.html"
    crumbs = [("index.html", "Home"), ("library/index.html", "Library"), (idx, "Wiki")]
    rows = []
    for p in sorted(st["pages"], key=lambda p: p["title"].lower()):
        if p["id"] not in ids:
            continue
        rows.append([f'<a href="{E(p["id"])}.html">{E(p["title"])}</a>', str(len(p["shippedIn"]))])
        text = open(os.path.join(ROOT, WIKI, "sections", p["id"] + ".md"), encoding="utf-8").read()
        body = re.sub(r'(<img [^>]*?src=")([^"]*)"', img_src, md_to_html(text, link_map))
        body = re.sub(r"\A\s*<h1>.*?</h1>", "", body, flags=re.S)  # the page shell prints the title
        shipped = "".join(f"<li><code>{E(s)}</code></li>" for s in p["shippedIn"])
        inner = (f'<div class="wiki">{body}</div><h2>Source</h2><p class="src">Help page shipped in ihris-suite-{RELEASE} (GPL-3.0, '
                 f'&copy; IntraHealth International), sha256 <code>{E(p["sha256"])}</code>, at:</p><ul class="src">{shipped}</ul>')
        out.append(page(f"library/wiki/{p['id']}.html", p["title"], crumbs, inner, theme, "library/index.html"))
    inner = (f"<p>The iHRIS user manual as shipped in the {RELEASE} help modules: {len(rows)} pages, restored from "
             f"<code>{E(st['source'])}</code> (GPL). Links between pages are rewritten to this site; a link to a page the release did not ship "
             "is kept as text.</p>" + rows_table(["Page", "Shipped at (paths)"], rows, "Wiki pages"))
    out.append(page(idx, "iHRIS wiki (user manual)", crumbs[:2], inner, theme, "library/index.html"))
    return out, ids


def library_index(theme):
    path = "library/index.html"
    inner = f"""<div class="board">
<article class="card"><span class="kind">knowledge source</span><h3>iHRIS Implementation Toolkit</h3><p>Six stages, nine domains, the tools for each.</p><a class="go" href="toolkit/index.html">Open</a></article>
<article class="card"><span class="kind">knowledge source</span><h3>iHRIS wiki</h3><p>The user manual as shipped in the {RELEASE} release.</p><a class="go" href="wiki/index.html">Open</a></article>
<article class="card"><span class="kind">knowledge source</span><h3>iHRIS Administrator Handbook</h3><p>79 wiki articles for administrators and developers, exported 2010-09-17 (GFDL-1.2).</p><a class="go" href="handbook/index.html">Open</a></article>
<article class="card"><span class="kind">knowledge source</span><h3>iHRIS use cases (2009)</h3><p>Use cases, actors and requirements of Common, Manage, Qualify and Plan, with a crosswalk to the data model.</p><a class="go" href="use-cases/index.html">Open</a></article>
</div>"""
    return page(path, "Library", [("index.html", "Home")], inner, theme, "library/index.html")


# ------------------------------------------------------------------ handbook (GFDL text, images by permission)
def handbook_pages(theme, out_dir):
    """The 2010 Administrator Handbook. The text is published only while ihris-admin-handbook.json records the
    stated licence, and the images only while it records the owner's permission for them."""
    decl = J(f"{HANDBOOK}/ihris-admin-handbook.json")
    lic = decl.get("licence") or {}
    text_ok = lic.get("status") == "stated"
    img_ok = text_ok and (lic.get("images") or {}).get("status") == "permission"
    book = J(f"{HANDBOOK}/book.json")
    idx = "library/handbook/index.html"
    crumbs = [("index.html", "Home"), ("library/index.html", "Library"), (idx, "Handbook")]
    credit = {i["id"]: i for i in book["images"]}
    if img_ok:
        os.makedirs(os.path.join(out_dir, "library/handbook/images"), exist_ok=True)
        for i in book["images"]:
            shutil.copy(os.path.join(ROOT, HANDBOOK, i["file"]), os.path.join(out_dir, "library/handbook/images", os.path.basename(i["file"])))
    ids = {a["id"] for a in book["articles"]}
    by_title = {a["title"].lower(): a["id"] for a in book["articles"]}
    note = (f'<p class="src">{E(lic.get("attribution", ""))} Text under the <a href="https://www.gnu.org/licenses/old-licenses/fdl-1.2.html">GNU FDL 1.2</a>'
            f'{"; images published with the owner&#39;s permission (" + E(lic["images"]["grantedOn"]) + ")" if img_ok else ""}. '
            f'E-mail addresses and phone numbers are redacted.</p>')
    out, rows = [], []
    for a in book["articles"]:
        rows.append([f'<a href="{E(a["id"])}.html">{E(a["title"])}</a>', f'{a["pageStart"]}&ndash;{a["pageEnd"]}', E(", ".join(a["contributors"]))])
        if not text_ok:
            continue
        text = open(os.path.join(ROOT, HANDBOOK, a["file"]), encoding="utf-8").read()
        body = re.sub(r"\A\s*<h1>.*?</h1>", "", md_to_html(text), flags=re.S)

        def fig(m):
            iid = os.path.basename(html.unescape(m.group(1)))[:-4]
            c = credit.get(iid)
            if not (img_ok and c):
                return f'<p class="mute">[image {E(iid)} not published]</p>'
            cr = c["credit"]
            return (f'<figure style="margin:16px 0"><img src="images/{E(iid)}.png" alt="{E(cr["name"])}">'
                    f'<figcaption class="legend"><a href="{E(cr["source"])}">{E(cr["name"])}</a>, by {E(", ".join(cr["contributors"]))}. '
                    f'Licence stated in the export: {E(cr["licence"])}; published with the owner&#39;s permission.</figcaption></figure>')
        body = re.sub(r'<p><img alt="[^"]*" src="([^"]+)" ?/?></p>', fig, body)
        body = re.sub(r'<img alt="[^"]*" src="([^"]+)" ?/?>', fig, body)
        src = (f'<h2>Source</h2><p class="src">iHRIS wiki, <a href="{E(a["source"])}">revision {a["oldid"]}</a>; contributors: '
               f'{E(", ".join(a["contributors"]))}. Pages {a["pageStart"]}&ndash;{a["pageEnd"]} of the 2010-09-17 export '
               f'(sha256 <code>{E(book["source"]["sha256"][:16])}&hellip;</code>). GNU FDL 1.2.</p>')
        out.append(page(f"library/handbook/{a['id']}.html", a["title"], crumbs, f'<div class="wiki">{body}</div>{src}', theme, "library/index.html"))
    wiki_rel = ('<p>It is a different cut of the wiki that <a href="../wiki/index.html">the iHRIS wiki</a> restores from the '
                f'{RELEASE} help modules: earlier (2010), under a different licence, and mostly the administrator and developer articles '
                'that the help modules never shipped. The two share one page by title (<i>IHRIS Manage Form Fields - 4.0</i>).</p>')
    imgs = "".join(f'<li><code>{E(i["credit"]["name"])}</code> (page {i["page"]}, licence stated: {E(i["credit"]["licence"])}), by '
                   f'{E(", ".join(i["credit"]["contributors"]))}</li>' for i in book["images"])
    inner = (f'<p><i>{E(book["title"])}</i> (sic), {len(book["articles"])} articles of the iHRIS wiki (open.intrahealth.org), exported to a '
             f'{book["source"]["pages"]}-page PDF by {E(book["generator"])} on {E(book["generatedAt"][:10])}.</p>{note}{wiki_rel}'
             + ("" if text_ok else '<p class="mute">No licence is recorded, so only the article list is shown.</p>')
             + rows_table(["Article", "Pages", "Contributors (wiki usernames)"], rows, "Handbook articles")
             + (f"<h2>Image credits</h2><ul>{imgs}</ul>" if img_ok else ""))
    out.append(page(idx, "iHRIS Administrator Handbook (2010)", crumbs[:2], inner, theme, "library/index.html"))
    return out


# ------------------------------------------------------------------ use cases (owner's permission)
def use_case_pages(theme, cls_index):
    decl = J(f"{USE_CASES}/ihris-use-cases.json")
    lic = decl.get("licence") or {}
    ok = lic.get("status") in ("stated", "permission")
    xw = J(f"{USE_CASES}/crosswalk.json")
    prods = [J(f"{USE_CASES}/{p}.json") for p in ("common", "manage", "qualify", "plan")]
    idx = "library/use-cases/index.html"
    crumbs = [("index.html", "Home"), ("library/index.html", "Library"), (idx, "Use cases")]
    note = (f'<p class="src">{E(lic.get("attribution", ""))} Published with the owner&#39;s permission ({E(lic.get("grantedOn", ""))}). '
            'Staff initials (&ldquo;Assigned To&rdquo;) and requirement sources naming a person are referenced by '
            '<a href="roles.html#opaque-actors">opaque actors</a>, with the identity withheld.</p>') if ok else \
        '<p class="mute">No licence or permission is recorded, so only counts are shown.</p>'
    out = []
    rows = []
    for d in prods:
        c = d["counts"]
        name = d["title"]
        link = f'<a href="{E(d["product"])}.html">{E(name)}</a>' if ok else E(name)
        rows.append([link, E(d["report"]["generatedAt"]), str(c["useCases"]), str(c["actors"]), str(c["requirements"]), str(c["steps"]), str(c["extensions"])])
        if ok:
            text = open(os.path.join(ROOT, USE_CASES, d["product"] + ".md"), encoding="utf-8").read()
            body = re.sub(r"\A\s*<h1>.*?</h1>", "", md_to_html(text, _uc_link), flags=re.S)
            out.append(page(f"library/use-cases/{d['product']}.html", name + " (2009)", crumbs, note + f'<div class="wiki">{body}</div>', theme, "library/index.html"))
    xrows = []
    for e in xw["entries"]:
        if e["matches"]:
            links = []
            for m in e["matches"]:
                cls = m.get("class")
                target = bs.page_of(cls_index[cls], cls) if cls and cls in cls_index else None
                f = f"<code>{E(m['form'])}</code>"
                links.append((f'<a href="{E(bs.rel("library/use-cases/crosswalk.html", target))}">{f}</a>' if target else f) + f' <span class="mute">{E(m["package"])}</span>')
            forms = ", ".join(links)
        else:
            forms = '<span class="mute">' + ("no data model here" if e["status"] == "no-data-model" else "not linked") + "</span>"
        uc = f'<a href="{E(e["product"])}.html">{E(e["useCase"])}</a>' if ok else E(e["useCase"])
        xrows.append([uc, E(e["title"]), forms])
    c = xw["counts"]
    out.append(page("library/use-cases/crosswalk.html", "Use cases to iHRIS forms", crumbs,
                    f'<p>{E(xw["method"])}</p><p>{c["matched"]} use cases linked ({c["links"]} links), {c["unmatched"]} not linked, '
                    f'{c["no-data-model"]} in iHRIS Plan, which has no data model in this folio.</p>'
                    + rows_table(["Use case", "Title", f"iHRIS {xw['release']} forms (name match)"], xrows, "Use case crosswalk"), theme, "library/index.html"))
    dang = "".join(f'<li><code>{E(x["id"])}</code> ({E(x["kind"])}, {E(x["product"])}){": <i>" + E(x["title"]) + "</i>" if x.get("title") else ""}, '
                   f'cited by {E(", ".join(x["citedBy"]))}</li>' for d in prods for x in d["dangling"])
    inner = (f'<p>The use-case model of iHRIS Common, Manage, Qualify and Plan: four Serlio CaseComplete reports from 2009, parsed into '
             f'structured records.</p>{note}' + rows_table(["Product", "Report generated", "Use cases", "Actors", "Requirements", "Steps", "Extensions"], rows, "Use-case reports")
             + f'<h2>Crosswalk</h2><p><a href="crosswalk.html">Each use case to the iHRIS {xw["release"]} forms its title names</a>, by name matching only: '
               f'{c["matched"]} linked, {c["unmatched"]} not linked, {c["no-data-model"]} without a data model (iHRIS Plan).</p>'
             + ('<h2>Roles and actors</h2><p><a href="roles.html">The roles the use cases name, and the opaque actors</a> '
                'standing for the people the reports name, identity withheld.</p>' if ok else "")
             + f"<h2>Cited but not described</h2><ul>{dang}</ul>")
    if ok:
        out.append(roles_page(prods, theme, crumbs))
    out.append(page(idx, "iHRIS use cases (2009)", crumbs[:2], inner, theme, "library/index.html"))
    return out


def _uc_link(href):
    """The use-case Markdown links actors to roles.md#<id>; on the site that is roles.html#<id>."""
    return "roles.html" + href[len("roles.md"):] if href.startswith("roles.md") else href


def roles_page(prods, theme, crumbs):
    """The use-case roles (scenarios/roles.json) and opaque actors (scenarios/actors/), each with an anchor
    the product pages link to, and where each is used."""
    path = "library/use-cases/roles.html"
    g = J(f"{USE_CASES}/scenarios/roles.json")
    actors = [J(os.path.relpath(f, ROOT)) for f in sorted(glob.glob(os.path.join(ROOT, USE_CASES, "scenarios", "actors", "*.json")))]
    src, plays, refs = {}, collections.defaultdict(list), collections.defaultdict(list)
    for d in prods:
        for a in d["actors"]:
            src[a["role"]] = (d, a["id"])
        stack = [d["root"]]
        while stack:
            p = stack.pop(0)
            stack += p["packages"]
            for u in p["useCases"]:
                for r in (u.get("primaryActors") or []) + (u.get("supportingActors") or []):
                    if (d["product"], u["id"]) not in plays[r]:
                        plays[r].append((d["product"], u["id"]))
                if u.get("assignedTo"):
                    refs[u["assignedTo"]["actor"]].append((d["product"], u["id"], "Assigned To"))
            for r in p["requirements"]:
                if r.get("source"):
                    refs[r["source"]["actor"]].append((d["product"], r["id"], "Source"))
    rrows = []
    for r in g["roles"]:
        d, aid = src[r["id"]]
        uses = ", ".join(f'<a href="{E(p)}.html">{E(u)}</a>' for p, u in plays[r["id"]]) or '<span class="mute">none</span>'
        rrows.append([f'<span id="{E(r["id"])}"><b>{E(r["title"])}</b></span><br><code>{E(r["id"])}</code>',
                      f'{E(aid)}<br><span class="mute">{E(d["title"])}</span>', E(r["description"]), uses])
    arows = []
    for a in actors:
        used = ", ".join(f'<a href="{E(p)}.html">{E(x)}</a> <span class="mute">({E(f)})</span>' for p, x, f in refs[a["id"]])
        arows.append([f'<span id="{E(a["id"])}"><b>{E(a["title"])}</b></span><br><code>{E(a["id"])}</code>', E(a["kind"]),
                      E(a["description"]), used])
    inner = ('<p>Each actor a 2009 report describes is a <b>role</b> in the iHRIS domain, declared in folio-assistant&#39;s '
             '<code>scenarios</code> graph kind (<code>library/ihris-use-cases/scenarios/roles.json</code>). Title and description '
             'are the report&#39;s own. A-ICE4 (Common) and A-PS6 (Qualify) are both &ldquo;Any User&rdquo;: two roles, and whether '
             'they are the same is undecided.</p>'
             + rows_table(["Role", "Actor in the report", "Description", "Plays in"], rrows, "Use-case roles")
             + '<h2 id="opaque-actors">Opaque actors</h2><p>People the reports name in &ldquo;Assigned To&rdquo; (staff initials) or in a '
               'requirement&#39;s &ldquo;Source&rdquo;. Each distinct person is one actor, numbered in order of first appearance, and '
               'who they are is withheld: the mapping lives in the data store only, never in this repository.</p>'
             + rows_table(["Actor", "Kind", "Description", "Referenced by"], arows, "Opaque actors"))
    return page(path, "Roles and actors (2009 use cases)", crumbs, inner, theme, "library/index.html")


# ------------------------------------------------------------------ data dictionary
def dd_pages(theme, cls_index, wiki_ids):
    out = []
    base = "src/ihris-data-dictionary"
    sheets = sorted((J(os.path.relpath(f, ROOT)) for f in glob.glob(os.path.join(ROOT, base, "data-dictionary/*.json"))), key=lambda s: s["group"].lower())
    vs = J(f"{base}/value-sets.json")["valueSets"]
    vs_by_form = {v["form"]: v for v in vs}
    idx = "data-dictionary/index.html"
    crumbs = [("index.html", "Home"), (idx, "Data dictionary")]
    n_el = sum(len(s["elements"]) for s in sheets)
    n_req = sum(1 for s in sheets for e in s["elements"] if e["optionality"] == "R")
    rows = [[f'<a href="{E(s["group"])}.html">{E(s["title"])}</a>', f'<code>{E(s["class"])}</code>', str(len(s["elements"])),
             str(sum(1 for e in s["elements"] if e["optionality"] == "R"))] for s in sheets]
    iso, isco = J(f"{base}/iso-report.json"), J(f"{base}/isco-report.json")
    inner = f"""<p>A data dictionary for health workforce information in the column order of WHO's DAK L2 guide, derived mechanically from the
<a href="../data-model/index.html">iHRIS {RELEASE} data model</a>. iHRIS is independent: this is not a SMART Guidelines DAK.
Columns the source cannot answer (definitions, conditionality, indicator linkages) stay empty until a person authors them.</p>
<div class="badges"><span class="badge">{n_el} data elements</span><span class="badge">{n_req} required</span><span class="badge">{len(sheets)} logical models</span>
<span class="badge"><a href="value-sets.html">{len(vs)} value sets</a></span></div>
<p>Download: <a href="../assets/data-dictionary.xlsx">data-dictionary.xlsx</a> &middot; <a href="../assets/data-dictionary.csv">data-dictionary.csv</a></p>
<h2>Logical models</h2>{rows_table(['Model', 'iHRIS class', 'Elements', 'Required'], rows, 'Logical models')}
<h2>Standards</h2>
<p><b>ISO 3166-1 countries</b> (verified with {E(iso['verifiedWith'])}): {iso['country']['equal']} of {iso['country']['shipped']} shipped codes match;
{len(iso['country']['notCurrent'])} no longer current; {len(iso['country']['currentMissingFromIhris'])} current codes missing from iHRIS.<br>
<b>ISO 4217 currencies</b>: {iso['currency']['equal']} of {iso['currency']['shipped']} match; {len(iso['currency']['notCurrent'])} no longer current;
{len(iso['currency']['currentMissingFromIhris'])} current codes missing.<br>
<b>ISCO-08</b> as shipped: {', '.join(f'{v} {k.replace("_", "-")}' for k, v in isco['isco08'].items())} groups. ISCO-88 to ISCO-08: {E(isco['isco88to08'])}.</p>"""
    out.append(page(idx, "Data dictionary", [("index.html", "Home")], inner, theme, "data-dictionary/index.html"))

    def wiki_link(path, ev):
        pid = os.path.basename(ev)[:-3]
        return f'<a href="{E(bs.rel(path, f"library/wiki/{pid}.html"))}">{E(pid)}</a>' if pid in wiki_ids else E(pid)

    for s in sheets:
        path = f"data-dictionary/{s['group']}.html"
        rows = []
        for e in s["elements"]:
            opts = e.get("inputOptions") or []
            opts = [opts] if isinstance(opts, str) else opts
            opts = ", ".join((f'<a href="value-sets.html#{E(u.rsplit("/", 1)[-1])}">{E(u.rsplit("/", 1)[-1])}</a>'
                              if u.rsplit("/", 1)[-1] in vs_by_form else E(u)) for u in opts)
            ev = ", ".join(wiki_link(path, x) for x in (e.get("evidence") or [])[:3]) + ("&hellip;" if len(e.get("evidence") or []) > 3 else "")
            rows.append([f'<code>{E(e["id"].split(".")[-1])}</code>', E(e.get("dataElementLabel") or ""), E(e.get("dataType") or ""),
                         opts or "&mdash;", f'<b>{e["optionality"]}</b>' if e["optionality"] == "R" else E(e["optionality"] or ""),
                         E(e.get("description") or "") or '<span class="mute">to author</span>', ev or "&mdash;"])
        cls = s["class"]
        cl = f'<a href="{E(bs.rel(path, bs.page_of(cls_index[cls], cls)))}"><code>{E(cls)}</code></a>' if cls in cls_index else f"<code>{E(cls)}</code>"
        inner = (f'<p>Logical model <code>{E(s["logicalModel"])}</code>, derived from {cl}{" (extends " + E(s["extends"]) + ")" if s.get("extends") else ""}.</p>' +
                 rows_table(["Element", "Label", "Data type", "Input options", "Optionality", "Description", "Wiki evidence"], rows, f"Data elements of {s['title']}"))
        out.append(page(path, s["title"], crumbs, inner, theme, "data-dictionary/index.html"))

    # value sets, with codes from the generated FHIR terminology
    term = {}
    for f in glob.glob(os.path.join(ROOT, base, "terminology/CodeSystem-*.json")):
        c = J(os.path.relpath(f, ROOT))
        term.setdefault(c["url"], c)
    parts = []
    for v in sorted(vs, key=lambda v: v["form"]):
        cs = [c for u, c in term.items() if u.rsplit("/", 1)[-1] == v["form"] and c.get("content") == "complete"]
        codes = ""
        if cs:
            con = cs[0].get("concept") or []
            codes = (f"<details><summary>{len(con)} codes (CodeSystem <code>{E(cs[0]['url'].rsplit('/', 1)[-1])}</code>)</summary>" +
                     rows_table(["Code", "Display"], [[f"<code>{E(c['code'])}</code>", E(c.get("display") or "")] for c in con], f"Codes of {v['form']}") + "</details>")
        used = ", ".join(f'<a href="{E(u.split(".")[0])}.html">{E(u)}</a>' for u in v["usedBy"])
        parts.append(f'<section id="{E(v["form"])}"><h2>{E(v.get("displayName") or v["form"])} <code>{E(v["form"])}</code></h2>'
                     f'<p><span class="badge">{E(v["status"])}</span> {v["defaultCodes"]} default codes; sample codes: {sum(v["sampleCodes"].values())}. '
                     f'Canonical <code>{E(v["canonical"])}</code>. Used by {used or "no element"}.</p>{codes}</section>')
    inner = ("<p>Every value set, the iHRIS list behind it, and the codes the release ships as defaults. Sample codes illustrate one example "
             "deployment and are published as <code>content: example</code> CodeSystems that no ValueSet includes.</p>" + "".join(parts))
    out.append(page("data-dictionary/value-sets.html", "Value sets", crumbs, inner, theme, "data-dictionary/index.html"))
    return out


# ------------------------------------------------------------------ FHIR (own README) and schemas
def fhir_page(theme):
    path = INSTANCE_PAGE["ihris-4-on-fhir"]
    text = open(os.path.join(ROOT, "src/ihris-4-on-fhir/README.md"), encoding="utf-8").read()
    body = re.sub(r"\A\s*<h1>.*?</h1>", "", md_to_html(text, lambda h: h if h.startswith(("http:", "https:", "#")) else f"{REPO}/blob/main/src/ihris-4-on-fhir/{h}"), flags=re.S)
    return page(path, "iHRIS 4 on FHIR", [("index.html", "Home")], body, theme, None)


def schemas_page(theme, out_dir):
    path = "schemas/index.html"
    bind = J("src/schemas/bindings.json")
    os.makedirs(os.path.join(out_dir, "schemas"), exist_ok=True)
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "src/schemas/*.schema.json"))):
        s = J(os.path.relpath(f, ROOT))
        shutil.copy(f, os.path.join(out_dir, "schemas", os.path.basename(f)))
        where = [b["glob"] for b in bind["bindings"] if b["schema"] == s["title"]]
        rows.append([f'<a href="{E(os.path.basename(f))}"><code>{E(s["title"])}</code></a>', E(s.get("description") or ""),
                     "<br>".join(f"<code>{E(w)}</code>" for w in where) or '<span class="mute">by <code>$schema</code> tag</span>'])
    reused = [["<code>folio-catalogue/v1</code>, <code>folio-catalogue-node/v1</code>", "catalogues and catalogue nodes", "<code>folio-assistant-core/schemas/catalogue.ts</code>"],
              ["Tool definition", "<code>src/tools/*.tool.json</code>", "<code>cat-harness/schemas/tool.ts</code>"],
              ["Instance declaration", "<code>ihris.json</code> and every instance's <code>&lt;name&gt;.json</code>", "<code>cat-harness/schemas/cat-harness.ts</code>"],
              ["Harness config", "<code>ihris.config.json</code>", "<code>cat-harness/schemas/harness-config.ts</code>"],
              ["Bean graph", "<code>beans/beans.json</code>", "<code>cat-harness/schemas/bean-graph.ts</code>"],
              ["Skill package", "<code>src/skills/package-manifest.json</code>", "<code>cat-harness/schemas/skill-package.ts</code>"],
              ["<code>pdf-structure/v1</code>", "<code>library/*/structure.json</code>", "<code>cat-harness/schemas/pdf-structure.ts</code>"],
              ["<code>folio-document-images/v1</code>", "<code>library/*/images.json</code>", "<code>cat-harness/schemas/document-image.ts</code>"],
              ["FHIR R4", "<code>src/ihris-data-dictionary/terminology/*.json</code>", "<code>fhir.resources</code> (R4)"]]
    import importlib.util as ilu
    spec = ilu.spec_from_file_location("qa", os.path.join(ROOT, "src/tools/qa.py"))
    qa = ilu.module_from_spec(spec)
    spec.loader.exec_module(qa)
    findings, coverage = qa.run()
    qrows = [[f"<code>{E(c['schema'])}</code>" + (' <span class="mute">reused</span>' if c["reused"] else ""), str(c["documents"]) if c["documents"] else "&mdash;",
              "<br>".join(f"<code>{E(k['id'])}</code>: {E(k['establishes'])}" + ("" if not k["findings"] else f' <b>({k["findings"]} finding(s))</b>')
                          for k in c["checks"]) or "<b>qa-missing</b>"] for c in coverage]
    qa_html = (f"<h2>QA coverage</h2><p>Shape is not enough. Every schema also has <b>semantic QA</b> in <code>src/tools/qa.py</code>: references resolve, "
               f"counts match what they count, files named exist. A schema with no QA check is itself a failing finding (<code>qa-missing</code>). "
               f"This build: {len(coverage)} schemas, {sum(len(c['checks']) for c in coverage)} checks, <b>{len(findings)} finding(s)</b>.</p>"
               + rows_table(["Schema", "Documents", "QA checks"], qrows, "QA coverage"))
    inner = (f"<p>Every JSON file in the repository is validated (<code>src/tools/validate.py</code>), and the build fails on a file no schema covers. "
             f"folio-assistant's own schemas come first; ihris adds a schema only where the platform has no field for the data.</p>"
             f"<h2>Reused from folio-assistant and FHIR</h2>{rows_table(['Schema', 'Covers', 'Defined in'], reused, 'Reused schemas')}"
             f"<h2>ihris schemas ({len(rows)})</h2>{rows_table(['Schema', 'Description', 'Bound to'], rows, 'ihris schemas')}" + qa_html)
    return page(path, "Schemas", [("index.html", "Home")], inner, theme, "schemas/index.html")


def all_pages(theme, cls_index, out_dir):
    pages = [sources_index(theme), ihris5_page(theme), library_index(theme), fhir_page(theme), schemas_page(theme, out_dir)]
    for inst in LP_INSTANCES:
        have = os.path.isdir(os.path.join(ROOT, "src", inst, "modules", RELEASE))
        pages.append(lp_instance_page(inst, theme, have))
        if have:
            pages += modules_pages(inst, theme, cls_index)
            pages.append(data_lists_page(inst, theme))
    pages += toolkit_pages(theme, out_dir)
    wp, wiki_ids = wiki_pages(theme, out_dir)
    pages += wp
    pages += dd_pages(theme, cls_index, wiki_ids)
    pages += handbook_pages(theme, out_dir)
    pages += use_case_pages(theme, cls_index)
    os.makedirs(os.path.join(out_dir, "assets"), exist_ok=True)
    for f in ("data-dictionary.xlsx", "data-dictionary.csv"):
        shutil.copy(os.path.join(ROOT, "src/ihris-data-dictionary", f), os.path.join(out_dir, "assets", f))
    return dict(pages)
