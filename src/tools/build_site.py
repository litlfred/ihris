#!/usr/bin/env python3
"""Build the ihris harness site: an iHRIS-themed static site for GitHub Pages.

Owner, 2026-09-23: a harness page for ihris like folio-assistant's per-instance
pages, but iHRIS-themed ("see css in ihris suite"), published from THIS repository
at litlfred.github.io/ihris/.

Everything here is GENERATED from committed data, never transcribed:

  ihris.json + each instance's <name>.json   the landing board
  src/*/data-model/4.3.3/*.json               one page per package and per class,
                                              laid out as the accepted wireframe H2
                                              (docs/design/wireframes/data-model-site/acceptance.json)
  src/site/theme/ihris-classic.json           the theme (src/tools/extract_theme.py)

Output goes to _site/ (git-ignored). The Pages workflow builds it and commits it to the gh-pages branch. Links are all
relative, so the site works under /ihris/ and from a local file.

  python3 src/tools/build_site.py [--out DIR] [--check-links]
"""
import collections
import html
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RELEASE = "4.3.3"
PACKAGES = ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify"]
REPO = "https://github.com/litlfred/ihris"
E = html.escape
AC = ' aria-current="page"'
DASH53 = ' stroke-dasharray="5 3"'
DASH43 = ' stroke-dasharray="4 3"'
BOLD = ' font-weight="700"'


def load(p):
    with open(os.path.join(ROOT, p)) as f:
        return json.load(f)


# ---------------------------------------------------------------- the data model
def data_model():
    recs = []
    for pkg in PACKAGES:
        d = os.path.join(ROOT, "src", pkg, "data-model", RELEASE)
        for f in sorted(os.listdir(d)):
            if f.endswith(".json"):
                r = load(os.path.join("src", pkg, "data-model", RELEASE, f))
                r["_pkg"] = pkg
                recs.append(r)
    return recs


def page_of(pkg, cls):
    return f"data-model/{pkg}/{cls}.html"


def rel(frm, to):
    """Relative URL from page `frm` to site path `to` (both site-root relative)."""
    return os.path.relpath(to, os.path.dirname(frm) or ".").replace(os.sep, "/")


# ---------------------------------------------------------------- chrome
def css(t):
    a = t["applied"]
    return f"""
:root {{ --page:{a['pageBackground']}; --panel:{a['contentBackground']}; --ink:{a['text']}; --h1:{a['h1']}; --h2:{a['h2']};
  --h3:{a['h3']}; --h4:{a['h4']}; --link:{a['link']}; --nav:{a['navBar']}; --nav-ink:{a['navBarText']}; --nav-hover:{a['navBarHover']};
  --nav-accent:{a['navBarAccent']}; --brand:{a['siteName']}; --rule:{a['sideNavRule']}; --active:{a['sideNavActive']};
  --active-bg:{a['subNavActiveBackground']}; --mute:#5c5c5c; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font:15px/1.5 {a['font']}; color:var(--ink); background:var(--page); }}
a {{ color:var(--link); }} a:hover {{ text-decoration-thickness:2px; }}
code {{ font-size:13px; }}
.skip {{ position:absolute; left:-9999px; top:0; background:var(--panel); border:2px solid var(--ink); padding:8px 12px; }}
.skip:focus {{ left:8px; top:8px; z-index:10; }}
.wrap {{ max-width:1240px; margin:0 auto; background:var(--panel); min-height:100vh; }}
header.site {{ display:flex; align-items:center; gap:16px; padding:12px 20px; border-bottom:4px solid var(--nav-accent); }}
header.site img {{ height:56px; width:auto; }}
.brand {{ font:26px/1.1 {a['brandFont']}; color:var(--brand); margin:0; }}
.brand a {{ color:inherit; text-decoration:none; }}
.tag {{ margin:2px 0 0; color:var(--mute); font-size:13px; }}
nav.top {{ background:var(--nav); }}
nav.top ul {{ list-style:none; margin:0; padding:0 12px; display:flex; flex-wrap:wrap; }}
nav.top a {{ display:flex; align-items:center; min-height:44px; padding:0 14px; color:var(--nav-ink); text-decoration:none; font-weight:700; border-right:1px solid var(--nav-hover); }}
nav.top a:hover, nav.top a[aria-current] {{ background:var(--nav-hover); }}
main {{ padding:20px 28px 32px; }}
h1 {{ color:var(--h1); font-size:28px; margin:4px 0 6px; }}
h2 {{ color:var(--h2); font-size:19px; margin:24px 0 8px; }}
h3 {{ color:var(--h3); font-size:16px; margin:0 0 6px; }}
.mute, .crumbs, .legend, .src {{ color:var(--mute); font-size:13px; }}
footer {{ border-top:1px solid var(--rule); padding:14px 28px; color:var(--mute); font-size:12px; }}
table {{ width:100%; border-collapse:collapse; margin:8px 0 12px; }}
th, td {{ text-align:left; border-bottom:1px solid var(--rule); padding:6px 8px; vertical-align:top; }}
th {{ background:var(--active-bg); font-size:13px; }}
.req {{ font-weight:700; }}
td, th, h1, h2, code, .side a, .crumbs, .src a, main p, main li, .badge {{ overflow-wrap:break-word; }}
h1, .crumbs, .side a, .hood td, .hood code, .fields td, .fields code {{ overflow-wrap:anywhere; }}
.tscroll {{ overflow-x:auto; }}
.wiki img {{ max-width:100%; height:auto; }}
.wiki table {{ display:block; overflow-x:auto; }}
.wiki pre {{ overflow-x:auto; }}
details > summary {{ cursor:pointer; min-height:32px; padding:4px 0; font-weight:600; }}
main {{ min-width:0; }}
.board {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:14px; }}
.card {{ border:1px solid var(--rule); border-top:4px solid var(--nav-accent); padding:12px 14px; display:flex; flex-direction:column; gap:6px; }}
.card .kind {{ font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--h2); font-weight:700; }}
.card p {{ margin:0; font-size:14px; }}
.card .stats {{ color:var(--mute); font-size:13px; }}
.card a.go {{ margin-top:auto; font-weight:700; }}
.layout {{ display:grid; grid-template-columns:260px minmax(0,1fr); }}
.side {{ border-right:1px solid var(--rule); padding:16px; background:#fafaf6; }}
.search label {{ display:block; font-size:12px; color:var(--mute); margin-bottom:2px; }}
.search input {{ width:100%; border:1px solid #767676; padding:6px 8px; font:inherit; margin-bottom:14px; }}
.side ul {{ list-style:none; margin:0; padding:0 0 0 12px; }}
.side > nav > ul {{ padding:0; }}
.side li {{ padding:3px 0; }}
.side .count, .side .more {{ color:var(--mute); font-size:12px; }}
.side [aria-current] {{ font-weight:700; color:var(--active); border-left:3px solid var(--active); padding-left:6px; margin-left:-9px; display:inline-block; }}
.side .note {{ color:var(--mute); font-size:12px; padding-top:8px; }}
.menu-btn {{ display:none; }}
.badges {{ display:flex; flex-wrap:wrap; gap:6px; margin:8px 0 12px; }}
.badge {{ border:1px solid var(--h3); padding:1px 8px; font-size:12px; }}
.base {{ border-style:dashed; }}
.hood {{ display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,1fr); gap:16px; align-items:start; }}
svg {{ width:100%; height:auto; border:1px solid var(--rule); background:#fff; }}
.rels {{ display:none; }}
@media (max-width:700px) {{
  header.site {{ padding:10px 16px; }} header.site img {{ height:40px; }} .brand {{ font-size:20px; }}
  main {{ padding:16px; }} h1 {{ font-size:22px; }}
  .layout {{ grid-template-columns:1fr; }}
  .side {{ border-right:0; border-bottom:1px solid var(--rule); padding:10px 16px; }}
  .side nav, .side .tile {{ display:none; }}
  .side.open nav {{ display:block; }}
  .menu-btn {{ display:inline-flex; align-items:center; gap:6px; border:1px solid var(--ink); padding:6px 10px; background:#fff; min-height:44px; font:inherit; }}
  .search input {{ min-height:44px; margin:8px 0 0; }}
  .side a {{ display:inline-flex; align-items:center; min-height:44px; }}
  .fields, .fields thead, .fields tbody, .fields tr, .fields th, .fields td {{ display:block; }}
  .fields thead {{ display:none; }}
  .fields tr {{ border:1px solid var(--rule); margin-bottom:10px; padding:6px 10px; }}
  .fields td {{ border:0; padding:2px 0; }}
  .fields td::before {{ content:attr(data-h) ": "; color:var(--mute); font-size:12px; }}
  .hood {{ display:none; }} .rels {{ display:block; }}
  .rels details {{ border:1px solid var(--rule); margin-bottom:8px; }}
  .rels summary {{ padding:10px; min-height:44px; font-weight:600; }}
  .rels ul {{ margin:0; padding:0 10px 10px 28px; }}
}}
"""


MENU_JS = """<script>
document.querySelectorAll('.menu-btn').forEach(function(b){b.addEventListener('click',function(){
  var s=b.closest('.side');var o=s.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');
  b.lastChild.textContent=o?' Close':' Menu';});});
</script>"""


def shell(path, title, body, theme, current=None, scripts=""):
    r = lambda p: rel(path, p)  # noqa: E731
    items = [("index.html", "Home"), ("data-model/index.html", "Data model"), ("data-dictionary/index.html", "Data dictionary"),
             ("sources/index.html", "Sources"), ("library/index.html", "Library"), ("schemas/index.html", "Schemas"),
             ("data-model/search.html", "Search"), (None, "GitHub")]
    nav = "".join(
        f'<li><a href="{E(r(p) if p else REPO)}"{AC if p == current else ""}>{E(n)}</a></li>'
        for p, n in items)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · iHRIS Knowledge Base</title>
<link rel="stylesheet" href="{r('assets/ihris.css')}">
<link rel="icon" href="{r('assets/iHRIS_logo.png')}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="site">
  <a href="{r('index.html')}"><img src="{r('assets/iHRIS_logo.png')}" alt="iHRIS"></a>
  <div><p class="brand"><a href="{r('index.html')}">iHRIS Knowledge Base</a></p>
  <p class="tag">A folio that describes iHRIS: source, data model, toolkit and wiki</p></div>
</header>
<nav class="top" aria-label="Site"><ul>{nav}</ul></nav>
{body}
<footer>{E(theme['licence']['attribution'])} Generated by <code>src/tools/build_site.py</code> from
<a href="{REPO}">litlfred/ihris</a>; edit the generator or its inputs, never this page.</footer>
</div>
{scripts}
</body>
</html>
"""


# ---------------------------------------------------------------- landing board
def instance_stats(inst, recs):
    p = os.path.join(ROOT, inst["path"])
    name = inst["name"]
    if name in PACKAGES:
        n = sum(1 for r in recs if r["_pkg"] == name)
        mods = len(os.listdir(os.path.join(p, "modules", RELEASE))) if os.path.isdir(os.path.join(p, "modules", RELEASE)) else 0
        return f"{n} form classes, {sum(len(r['fields']) for r in recs if r['_pkg'] == name)} fields, {mods} modules", \
            f"data-model/{name}/index.html"
    if name == "ihris-data-dictionary":
        dd = os.path.join(p, "data-dictionary")
        n = len([f for f in os.listdir(dd) if f.endswith(".json")]) if os.path.isdir(dd) else 0
        return f"{n} logical models", None
    return None, None


def landing(theme, recs):
    decl = load("ihris.json")
    cards = []
    path = "index.html"
    for inst in decl["instances"]:
        j = {}
        f = os.path.join(ROOT, inst["path"], inst["name"] + ".json")
        if os.path.exists(f):
            j = load(os.path.relpath(f, ROOT))
        stats, _ = instance_stats(inst, recs)
        import site_instances
        page = site_instances.INSTANCE_PAGE.get(inst["name"])
        href = rel(path, page) if page else f"{REPO}/tree/main/{inst['path']}"
        label = "Open" if page else "Open on GitHub"
        desc = (j.get("description") or "").split(". ")[0].rstrip(".") + "."
        cards.append(f"""<article class="card">
  <span class="kind">{E(inst['kind'].replace('-', ' '))}</span>
  <h3>{E(j.get('title') or inst['name'])}</h3>
  <p>{E(desc)}</p>
  {f'<span class="stats">{E(stats)}</span>' if stats else ''}
  <a class="go" href="{E(href)}">{label}<span class="mute"> · {E(inst['name'])}</span></a>
</article>""")
    classes = len({r["class"] for r in recs})
    body = f"""<main id="main" tabindex="-1">
<h1>{E(decl['title'])}</h1>
<p>{E(decl['description'].split('. ')[0])}.</p>
<p class="mute">Release {RELEASE}: {len(recs)} form-class records ({classes} distinct classes) and
{sum(len(r['fields']) for r in recs)} fields across the four core packages, from the checksum-verified
<code>ihris-suite-{RELEASE}.tar.bz2</code>.</p>
<h2>Harness</h2>
<div class="board">
<article class="card">
  <span class="kind">harness visualiser</span>
  <h3>iHRIS {RELEASE} data model</h3>
  <p>Every form class with its fields, the lists it draws from, and its neighbourhood: what it extends and what extends it.</p>
  <span class="stats">{len(recs)} records, {classes} classes</span>
  <a class="go" href="data-model/index.html">Open the data model</a>
</article>
{''.join(cards)}
</div>
</main>"""
    return shell(path, "Home", body, theme, current="index.html")


# ---------------------------------------------------------------- data-model pages
def sidebar(path, pkg_of_page, cls, recs, by_pkg):
    r = lambda p: rel(path, p)  # noqa: E731
    items = [f'<li><a href="{r("data-model/index.html")}">Overview</a></li>']
    for pkg in PACKAGES:
        names = [x["class"] for x in by_pkg[pkg]]
        sub = ""
        if pkg == pkg_of_page and cls:
            i = names.index(cls)
            lo, hi = max(0, i - 1), min(len(names), i + 3)
            lis = [f'<li class="more">&hellip; {lo} above</li>'] if lo else []
            for n in names[lo:hi]:
                cur = ' aria-current="page"' if n == cls else ""
                lis.append(f'<li><a href="{r(page_of(pkg, n))}"{cur}>{E(n)}</a></li>')
            below = len(names) - hi
            lis.append(f'<li class="more">{f"&hellip; {below} below &middot; " if below else ""}'
                       f'<a href="{r(f"data-model/{pkg}/index.html")}">all {len(names)}</a></li>')
            sub = "<ul>" + "".join(lis) + "</ul>"
        cur = ' aria-current="page"' if pkg == pkg_of_page and not cls else ""
        items.append(f'<li><a href="{r(f"data-model/{pkg}/index.html")}"{cur}>{E(pkg)}</a> '
                     f'<span class="count">{len(names)}</span>{sub}</li>')
    dup = sorted(c for c, n in collections.Counter(x["class"] for x in recs).items() if n > 1)
    note = (f'<li class="note">{len(recs)} package records, {len({x["class"] for x in recs})} distinct classes: '
            f'{", ".join(dup)} {"is" if len(dup) == 1 else "are each"} defined in two packages.</li>') if dup else ""
    return f"""<aside class="side" aria-label="Data model navigation">
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="dm-nav"><span aria-hidden="true">&#9776;</span> Menu</button>
  <form class="search" role="search" action="{r('data-model/search.html')}">
    <label for="q">Search classes, fields, lists</label>
    <input id="q" name="q" type="search" autocomplete="off">
  </form>
  <nav id="dm-nav" aria-label="Packages"><ul>{''.join(items)}{note}</ul></nav>
</aside>"""


def neighbourhood_svg(cls, parent, parent_has_page, kids, lists):
    W, H = 560, 330
    cx, cy = W / 2, 165
    out = ['<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
           '<path d="M0,0L10,5L0,10z" fill="#1b1b1b"/></marker></defs><g font-family="Arial, sans-serif" font-size="12" fill="#1b1b1b">']
    shown_k, shown_l = kids[:3], lists[:6]

    def box(x, y, w, label, bold=False, dashed=False, pill=False, fill="#fff"):
        out.append(f'<rect x="{x - w / 2:.0f}" y="{y - 18:.0f}" width="{w:.0f}" height="36" rx="{18 if pill else 0}" fill="{fill}" '
                   f'stroke="#1b1b1b" stroke-width="{3 if bold else 1}"{DASH53 if dashed else ""}/>'
                   f'<text x="{x:.0f}" y="{y + 4:.0f}" text-anchor="middle"{BOLD if bold else ""}>{E(label)}</text>')

    def line(x1, y1, x2, y2, dashed=False):
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1b1b1b"'
                   f'{DASH43 if dashed else ""} marker-end="url(#ar)"/>')
    if parent:
        line(cx, cy - 18, cx, 76)
    for i, k in enumerate(shown_k):
        x = W * (i + 1) / (len(shown_k) + 1)
        line(x, 262, cx + (x - cx) * 0.3, cy + 18)
    left = shown_l[len(shown_l) // 2 + len(shown_l) % 2:]
    right = shown_l[:len(shown_l) // 2 + len(shown_l) % 2]
    for side, group in ((1, right), (-1, left)):
        for i, l in enumerate(group):
            y = cy + (i - (len(group) - 1) / 2) * 44
            line(cx + side * 70, cy, cx + side * 180, y, dashed=True)
    # nodes last, so they sit over the edges
    w = max(130, 8 * len(cls))
    box(cx, cy, w, cls, bold=True)
    if parent:
        box(cx, 58, max(110, 8 * len(parent) + 30), parent + ("" if parent_has_page else " (base)"),
            dashed=not parent_has_page, fill="#f2f2f2")
    for i, k in enumerate(shown_k):
        box(W * (i + 1) / (len(shown_k) + 1), 280, min(W / (len(shown_k) + 1) - 8, max(110, 7.2 * len(k))), k)
    for side, group in ((1, right), (-1, left)):
        for i, l in enumerate(group):
            y = cy + (i - (len(group) - 1) / 2) * 44
            box(cx + side * 222, y, max(66, 8 * len(l)), l, pill=True)
    more = []
    if len(kids) > 3:
        more.append(f"+{len(kids) - 3} more subclasses")
    if len(lists) > 6:
        more.append(f"+{len(lists) - 6} more lists")
    if more:
        out.append(f'<text x="8" y="{H - 8}" font-size="11" fill="#5c5c5c">{E(" · ".join(more))} (all in the table)</text>')
    out.append("</g>")
    return W, H, "".join(out)


def class_page(rec, recs, by_pkg, cls_index, form_to_cls, theme):
    pkg, cls = rec["_pkg"], rec["class"]
    path = page_of(pkg, cls)
    r = lambda p: rel(path, p)  # noqa: E731

    def cls_link(name):
        loc = cls_index.get(name)
        return f'<a href="{r(page_of(loc, name))}">{E(name)}</a>' if loc else f"{E(name)}"

    def list_link(form):
        c = form_to_cls.get(form)
        if c and c in cls_index:
            return f'<a href="{r(page_of(cls_index[c], c))}">{E(form)}</a>', c
        return E(form), c
    parent = rec.get("extends")
    parent_page = parent in cls_index
    kids = sorted({x["class"] for x in recs if x.get("extends") == cls})
    kid_adds = {k: sorted({f["field"] for x in recs if x["class"] == k for f in x["fields"]}) for k in kids}
    via = collections.OrderedDict()
    for f in rec["fields"]:
        for l in f.get("references") or []:
            via.setdefault(l, []).append(f["field"])
    lists = list(via)

    rows = []
    for f in rec["fields"]:
        refs = ", ".join(list_link(l)[0] for l in (f.get("references") or [])) or "&mdash;"
        req = '<td role="cell" data-h="Required" class="req">yes</td>' if f.get("required") else '<td role="cell" data-h="Required">no</td>'
        label = E(f["label"]) if f.get("label") else "<i>(no label)</i>"
        rows.append(f'<tr role="row"><td role="cell" data-h="Field"><code>{E(f["field"])}</code></td><td role="cell" data-h="Label">{label}</td>'
                    f'<td role="cell" data-h="Type">{E(f.get("type") or "?")}</td>{req}<td role="cell" data-h="Draws from">{refs}</td></tr>')
    fields = (f"""<table class="fields" role="table" aria-label="Fields of {E(cls)}">
<thead role="rowgroup"><tr role="row"><th role="columnheader">Field</th><th role="columnheader">Label</th><th role="columnheader">Type</th><th role="columnheader">Required</th><th role="columnheader">Draws from</th></tr></thead>
<tbody role="rowgroup">{''.join(rows)}</tbody></table>""" if rows else '<p class="mute">This record defines no fields of its own.</p>')

    edges = []
    if parent:
        edges.append(("extends", cls_link(parent) + ("" if parent_page else ' <span class="mute">(base, no page)</span>'), "&mdash;"))
    for k in kids:
        adds = ", ".join(f"<code>{E(a)}</code>" for a in kid_adds[k][:4]) + (" &hellip;" if len(kid_adds[k]) > 4 else "")
        edges.append(("extended by", cls_link(k), f"adds {adds}" if adds else "&mdash;"))
    for l in lists:
        a, c = list_link(l)
        edges.append(("draws from", a + (f" <code>{E(c)}</code>" if c else ""), ", ".join(f"<code>{E(x)}</code>" for x in via[l])))
    names = []
    if parent:
        names.append(f"{cls} extends {'the base class ' if not parent_page else ''}{parent}.")
    if kids:
        names.append(f"{', '.join(kids)} extend{'s' if len(kids) == 1 else ''} {cls}.")
    if lists:
        names.append(f"{cls} draws from the list{'s' if len(lists) > 1 else ''} {', '.join(lists)}.")
    if edges:
        W, H, svg = neighbourhood_svg(cls, parent, parent_page, kids, lists)
        edge_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in edges)
        hood = f"""<h2><span aria-hidden="true">&#9711;&#8212;&#9711;</span> Neighbourhood</h2>
<div class="hood">
<figure style="margin:0"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{E(' '.join(names))}" aria-describedby="hood-cap">{svg}</svg>
<figcaption id="hood-cap" class="legend">Box: form class (dashed: base class, no page) &middot; pill: list &middot; solid arrow: extends &middot;
dashed arrow: a field draws from the list. The table lists every edge.</figcaption></figure>
<table aria-label="Neighbourhood edges"><thead><tr><th>Edge</th><th>Other end</th><th>Via</th></tr></thead><tbody>{edge_rows}</tbody></table>
</div>
<section class="rels" aria-label="Relationships">
{f'<details open><summary><span aria-hidden="true">&#8593;</span> Extends (1)</summary><ul><li>{edges[0][1]}</li></ul></details>' if parent else ''}
{f'<details><summary><span aria-hidden="true">&#8595;</span> Extended by ({len(kids)})</summary><ul>' + ''.join(f'<li>{cls_link(k)}</li>' for k in kids) + '</ul></details>' if kids else ''}
{f'<details><summary><span aria-hidden="true">&#128279;</span> Lists referenced ({len(lists)})</summary><ul>' + ''.join(f'<li>{list_link(l)[0]} ({", ".join(E(x) for x in via[l])})</li>' for l in lists) + '</ul></details>' if lists else ''}
</section>"""
    else:
        hood = '<h2>Neighbourhood</h2><p class="mute">No extends, subclass or list edges.</p>'

    forms = ", ".join(rec.get("forms") or []) or "none"
    mods = ", ".join(f"<code>{E(m.split('/module/')[-1])}</code> ({E(m.split('/')[0])})" for m in rec.get("definedIn") or [])
    body = f"""<div class="layout">
{sidebar(path, pkg, cls, recs, by_pkg)}
<main id="main" tabindex="-1">
<div class="crumbs"><a href="{r('data-model/index.html')}">Data model</a> / <a href="{r(f'data-model/{pkg}/index.html')}">{E(pkg)}</a> / {E(cls)}</div>
<h1>{E(cls)}</h1>
<div class="badges">
{f'<span class="badge{"" if parent_page else " base"}"><span aria-hidden="true">&#8593;</span> extends {E(parent)}{"" if parent_page else " (base class)"}</span>' if parent else ''}
<span class="badge">form {E(forms)}</span><span class="badge">package {E(pkg)}</span><span class="badge">release {RELEASE}</span>
</div>
<h2>Fields</h2>
{fields}
{hood}
<h2>Source</h2>
<p class="src">Defined in module {mods}, ihris-suite-{RELEASE} (MD5 verified against Launchpad).
Record: <a href="{REPO}/blob/main/src/{pkg}/data-model/{RELEASE}/{E(cls)}.json">src/{E(pkg)}/data-model/{RELEASE}/{E(cls)}.json</a>.</p>
</main>
</div>"""
    return path, shell(path, cls, body, theme, current="data-model/index.html", scripts=MENU_JS)


def package_page(pkg, recs, by_pkg, theme):
    path = f"data-model/{pkg}/index.html"
    rows = "".join(
        f'<tr><td><a href="{E(x["class"])}.html">{E(x["class"])}</a></td><td>{E(", ".join(x.get("forms") or []) or "—")}</td>'
        f'<td>{len(x["fields"])}</td><td>{E(x.get("extends") or "—")}</td></tr>' for x in by_pkg[pkg])
    body = f"""<div class="layout">
{sidebar(path, pkg, None, recs, by_pkg)}
<main id="main" tabindex="-1">
<div class="crumbs"><a href="../index.html">Data model</a> / {E(pkg)}</div>
<h1>{E(pkg)}</h1>
<p class="mute">{len(by_pkg[pkg])} form-class records in release {RELEASE}.</p>
<div class="tscroll"><table><thead><tr><th>Class</th><th>Form</th><th>Fields</th><th>Extends</th></tr></thead><tbody>{rows}</tbody></table></div>
</main></div>"""
    return path, shell(path, pkg, body, theme, current="data-model/index.html", scripts=MENU_JS)


def overview_page(recs, by_pkg, theme):
    path = "data-model/index.html"
    rows = "".join(f'<tr><td><a href="{pkg}/index.html">{pkg}</a></td><td>{len(by_pkg[pkg])}</td>'
                   f'<td>{sum(len(x["fields"]) for x in by_pkg[pkg])}</td></tr>' for pkg in PACKAGES)
    refs = collections.Counter(l for x in recs for f in x["fields"] for l in (f.get("references") or []))
    top = ", ".join(f"{E(l)} ({n})" for l, n in refs.most_common(6))
    body = f"""<div class="layout">
{sidebar(path, None, None, recs, by_pkg)}
<main id="main" tabindex="-1">
<h1>iHRIS {RELEASE} data model</h1>
<p>Every I2CE form class shipped in the four core packages of the checksum-verified <code>ihris-suite-{RELEASE}.tar.bz2</code>,
extracted by <code>src/tools/build_kg.py</code>. Pick a package, search, or open a class to see its fields and neighbourhood.</p>
<table><thead><tr><th>Package</th><th>Records</th><th>Fields</th></tr></thead><tbody>{rows}</tbody></table>
<p class="mute">Most referenced lists: {top}.</p>
</main></div>"""
    return path, shell(path, "Data model", body, theme, current="data-model/index.html", scripts=MENU_JS)


def search_page(recs, theme):
    path = "data-model/search.html"
    idx = [{"c": x["class"], "p": x["_pkg"], "f": [f["field"] for f in x["fields"]],
            "l": sorted({l for f in x["fields"] for l in (f.get("references") or [])})} for x in recs]
    rows = "".join(f'<li data-k="{E(" ".join([x["class"].lower()] + [f.lower() for f in i["f"]] + i["l"]))}">'
                   f'<a href="{x["_pkg"]}/{E(x["class"])}.html">{E(x["class"])}</a> <span class="mute">{x["_pkg"]} · '
                   f'{len(x["fields"])} fields</span></li>' for x, i in zip(recs, idx))
    js = """<script>
(function(){var q=new URLSearchParams(location.search).get('q')||'';var box=document.getElementById('sq');box.value=q;
function run(){var v=box.value.trim().toLowerCase();var n=0;document.querySelectorAll('#hits li').forEach(function(li){
var ok=!v||li.dataset.k.indexOf(v)>=0;li.hidden=!ok;if(ok)n++;});document.getElementById('n').textContent=n;}
box.addEventListener('input',run);run();})();
</script>"""
    body = f"""<main id="main" tabindex="-1">
<h1>Search the data model</h1>
<form role="search" onsubmit="return false"><label for="sq">Class, field or list name</label><br>
<input id="sq" type="search" style="width:100%;max-width:520px;padding:8px;font:inherit;min-height:44px;border:1px solid #767676"></form>
<p class="mute" aria-live="polite"><span id="n">{len(recs)}</span> matching records</p>
<ul id="hits">{rows}</ul>
</main>"""
    return path, shell(path, "Search", body, theme, current="data-model/search.html", scripts=js)


# ---------------------------------------------------------------- main
def main():
    out = os.path.join(ROOT, sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else os.path.join(ROOT, "_site")
    theme = load("src/site/theme/ihris-classic.json")
    recs = data_model()
    by_pkg = {p: sorted((x for x in recs if x["_pkg"] == p), key=lambda x: x["class"]) for p in PACKAGES}
    cls_index = {}
    for x in recs:
        cls_index.setdefault(x["class"], x["_pkg"])
    form_to_cls = {}
    for x in recs:
        for fm in x.get("forms") or []:
            form_to_cls.setdefault(fm, x["class"])
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    pages = {"index.html": landing(theme, recs)}
    for fn in (lambda: overview_page(recs, by_pkg, theme), lambda: search_page(recs, theme)):
        p, h = fn()
        pages[p] = h
    for pkg in PACKAGES:
        p, h = package_page(pkg, recs, by_pkg, theme)
        pages[p] = h
    for x in recs:
        p, h = class_page(x, recs, by_pkg, cls_index, form_to_cls, theme)
        pages[p] = h
    import site_instances
    pages.update(site_instances.all_pages(theme, cls_index, out))
    for p, h in pages.items():
        dst = os.path.join(out, p)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w") as f:
            f.write(h)
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    with open(os.path.join(out, "assets", "ihris.css"), "w") as f:
        f.write(css(theme))
    shutil.copy(os.path.join(ROOT, "src/site/theme/iHRIS_logo.png"), os.path.join(out, "assets", "iHRIS_logo.png"))
    open(os.path.join(out, ".nojekyll"), "w").close()
    print(f"site: {len(pages)} pages -> {os.path.relpath(out, ROOT)}")
    if "--check-links" in sys.argv:
        bad = broken_links(out)
        for b in bad[:20]:
            print(f"  broken: {b[0]} -> {b[1]}")
        sys.exit(1 if bad else 0)


def broken_links(out):
    """Every relative href/src in the built site must resolve to a built file."""
    import re
    bad = []
    for d, _, fs in os.walk(out):
        for f in fs:
            if f.endswith(".html"):
                p = os.path.join(d, f)
                for u in re.findall(r'(?:href|src|action)="([^"]+)"', open(p).read()):
                    u = html.unescape(u)
                    if u.startswith(("http:", "https:", "#", "mailto:")):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(d, u.split("?")[0].split("#")[0]))):
                        bad.append((os.path.relpath(p, out), u))
    return bad


if __name__ == "__main__":
    main()
