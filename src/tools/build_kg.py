#!/usr/bin/env python3
"""Rebuild every generated knowledge-graph file in this repository from uploads/.

Everything under src/<instance>/catalogue, src/<instance>/modules,
src/<instance>/data-model, src/<instance>/data-lists, library/ihris-toolkit, library/ihris-wiki and
docs/generated is OUTPUT of this script. Edit the script (or the captures in
uploads/), never the output: a hand edit is overwritten on the next run.

Inputs (all under uploads/):
  launchpad/projects/*.{html,rdf}   project, +series and +download pages, +rdf
  launchpad/series/<p>@<s>.html     series pages
  launchpad/milestones/<p>@<m>.html milestone / release pages
  launchpad/release-file-md5.tsv    url <TAB> "<md5> <file>"
  ihris-suite-4.3.3/manifest.json   verified checksum of the suite tarball
  ihris-suite-4.3.3/*.tar.bz2       the tarball itself (git-ignored; optional)
  toolkit/<stage>.html + graphic    saved toolkit.ihris.org stage pages
  github/*.json                     iHRIS 5 inventories (see snapshot_github.py)

Usage:  python3 src/tools/build_kg.py            (from the repo root)
Needs:  beautifulsoup4, markdownify (pip)
"""
from __future__ import annotations

import collections
import glob
import hashlib
import html
import json
import os
import re
import shutil
import tarfile
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UP = os.path.join(ROOT, "uploads")
CAPTURED_AT = "2026-09-22"

# Owner ruling 2026-09-22 (issue #1): these are core; everything else in the
# iHRIS Suite project group is a country customization or a side tool.
CORE = ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify", "ihris-plan", "openhie-pr"]
TOOLS = {"textlayout", "lcdmenu", "offline-ihris", "ihris-retention", "ihris-graduate",
         "ihris-train", "feedback", "icsv-registry", "openhie", "openinfoman"}
SUITE_RELEASE = "4.3.3"
SUITE_FILE = "ihris-suite-4.3.3.tar.bz2"


# ---------------------------------------------------------------- helpers
def rel(p: str) -> str:
    return os.path.relpath(p, ROOT)


def write_json(path: str, obj) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def txt(s: str | None) -> str | None:
    if s is None:
        return None
    s = re.sub(r"<script.*?</script>", "", s, flags=re.S)
    s = re.sub(r"<br\s*/?>|</p>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", s)).strip()
    return s or None


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean_dir(path: str) -> None:
    if os.path.isdir(path):
        shutil.rmtree(path)


def node(id_, kind, title, parents, upstream, flavour=None, metadata_ref=None, bitstreams=None, note=None,
         state="referenced", **extra):
    m = {"state": state, "provenance": {"upstream": upstream}}
    if note:
        m["note"] = note
    m.update(extra.pop("materialization_extra", {}))
    n = {"$schema": "folio-catalogue-node/v1", "id": id_, "kind": kind}
    if flavour:
        n["flavour"] = flavour
    n["title"] = title
    n["parents"] = parents
    n.update(extra)
    if metadata_ref:
        n["metadataRef"] = metadata_ref
    if bitstreams:
        n["bitstreams"] = bitstreams
    n["materialization"] = m
    return n


def fname(id_: str) -> str:
    return id_.replace("/", "--").replace("~", "").replace("+", "-") + ".json"


# ---------------------------------------------------------------- launchpad
def lp_project(p: str) -> dict:
    d = {"name": p}
    rdf = os.path.join(UP, "launchpad/projects", p + ".rdf")
    try:
        ns = {"lp": "https://launchpad.net/rdf/launchpad#", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}
        r = ET.parse(rdf).getroot()
        prod = r[0]
        g = lambda t: (prod.findtext("lp:" + t, namespaces=ns) or "").strip() or None  # noqa: E731
        d.update(title=g("title") or g("displayName"), summary=g("shortDescription"), description=g("description"),
                 registered=g("creationDate"),
                 homepage=next((e.get("{%s}resource" % ns["rdf"]) for e in prod.findall("lp:homepage", ns)), None),
                 languages=[x.strip() for e in prod.findall("lp:programmingLanguage", ns) for x in (e.text or "").split(",") if x.strip()])
    except (ET.ParseError, FileNotFoundError):
        pass
    h = open(os.path.join(UP, "launchpad/projects", p + ".html"), encoding="utf-8").read()
    lic = re.search(r"Licen[cs]e[s]?:.*?<dd[^>]*>(.*?)</dd>", h, re.S)
    d["licences"] = [x.strip() for x in (txt(lic.group(1)) or "").split(",") if x.strip()] if lic else []
    vcs = re.search(r"Version control system:.*?<dd[^>]*>\s*(\w+)", h, re.S)
    d["vcs"] = {"Bazaar": "bzr", "Git": "git"}.get(vcs.group(1)) if vcs else None
    part = re.search(r"Part of:.*?href=\"[^\"]*/([\w\-]+)\"", h, re.S)
    d["partOf"] = part.group(1) if part else None
    mt = re.search(r"Maintainer:.*?<a[^>]*href=\"[^\"]*/~([\w\-\+\.]+)\"[^>]*>(.*?)</a>", h, re.S)
    d["maintainer"] = {"id": "~" + mt.group(1), "name": txt(mt.group(2))} if mt else None
    wk = re.search(r'href="([^"]+)"[^>]*>\s*Wiki\s*<', h)
    d["wiki"] = wk.group(1) if wk else None
    d["lp"] = sorted(set(x for x in re.findall(r"lp:[~\w\-\+/\.]+", h) if x != "lp:context"))
    d.setdefault("title", p)
    s = open(os.path.join(UP, "launchpad/projects", p + "__series.html"), encoding="utf-8").read()
    d["series"] = sorted(set(re.findall(r'href="/%s/([\w\.\-]+)"' % re.escape(p), s)) - {"trunk+"}, key=str)
    d["series"] = [x for x in d["series"] if not x.startswith("+")]
    foc = re.search(r'<a href="/%s/([\w\.\-]+)">[^<]*</a>\s*series\s*</strong>\s*is the current focus' % re.escape(p), h)
    d["focus"] = foc.group(1) if foc else None
    return d


def classify(p: str) -> str:
    if p in CORE:
        return "core"
    if p in TOOLS:
        return "tool" if p not in {"openhie", "openinfoman"} else "related"
    return "country-customization"


def lp_series(p: str, s: str) -> dict:
    f = os.path.join(UP, "launchpad/series", f"{p}@{s}.html")
    if not os.path.exists(f):
        return {"branches": [], "milestones": []}
    t = open(f, encoding="utf-8").read()
    br = sorted(set("lp:" + b for b in re.findall(r'href="https://code.launchpad.net/(~[^"/]+/%s/[^"/+]+)"' % re.escape(p), t)))
    ms = sorted(set(re.findall(r'href="/%s/\+milestone/([\w\.\-]+)"' % re.escape(p), t)))
    return {"branches": br, "milestones": ms}


def lp_md5s() -> dict:
    out = {}
    for line in open(os.path.join(UP, "launchpad/release-file-md5.tsv"), encoding="utf-8"):
        url, _, val = line.rstrip("\n").partition("\t")
        m = re.match(r"([0-9a-f]{32}) ", val)
        if m:
            out[url] = m.group(1)
    return out


def lp_milestone(p: str, m: str, md5s: dict) -> dict:
    t = open(os.path.join(UP, "launchpad/milestones", f"{p}@{m}.html"), encoding="utf-8").read()
    g = lambda k: (lambda x: txt(x.group(1)) if x else None)(re.search(k + r":\s*</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S))  # noqa: E731
    rn = re.search(r"Release notes(?:&nbsp;)?\s*</h2>(.*?)<h2", t, re.S)
    cl = re.search(r"Changelog(?:&nbsp;)?\s*</h2>(.*?)(?:<h2|<div class=\"portlet\")", t, re.S)
    notes, ch = (txt(rn.group(1)) if rn else None), (txt(cl.group(1)) if cl else None)
    notes = None if notes and "does not have release notes" in notes else notes
    ch = None if ch and "does not have a changelog" in ch else ch
    files, seen = [], set()
    for mm in re.finditer(r'href="(https://launchpad.net/%s/[^"]+/\+download/([^"/]+))"' % re.escape(p), t):
        if mm.group(2) in seen:
            continue
        seen.add(mm.group(2))
        f = {"name": mm.group(2), "url": mm.group(1)}
        if mm.group(1) in md5s:
            f["md5"] = md5s[mm.group(1)]
        files.append(f)
    return dict(name=m, series=g("Series"), released=g("Released"), expected=g("Expected"), registrant=g("Registrant"),
                releaseNotes=notes, changelog=ch, files=files)


def build_launchpad():
    md5s = lp_md5s()
    suite = json.load(open(os.path.join(UP, "ihris-suite-4.3.3/manifest.json")))
    projects = sorted(os.path.basename(f)[:-len("__series.html")] for f in glob.glob(os.path.join(UP, "launchpad/projects/*__series.html")))
    projects = [p for p in projects if os.path.exists(os.path.join(UP, "launchpad/projects", p + ".html"))]
    info = {p: lp_project(p) for p in projects}

    # ---- root catalogue: the project group, every project, by reference
    base = os.path.join(ROOT, "src/catalogue")
    clean_dir(base)
    group_members = [p for p in projects if info[p].get("partOf") == "ihris-suite"]
    write_json(os.path.join(base, "catalogue.json"), {
        "$schema": "folio-catalogue/v1", "id": "ihris-launchpad",
        "title": "iHRIS on Launchpad: the iHRIS Suite project group and related projects",
        "system": "Launchpad (Bazaar)", "baseUrl": "https://launchpad.net/ihris-suite",
        "totalItemsUpstream": len(group_members),
        "sizeBasis": f"Counted {CAPTURED_AT} from the project list on https://launchpad.net/ihris-suite "
                     f"({len(group_members)} projects whose page says 'Part of: iHRIS Suite'), plus "
                     "openhie-pr, openhie and openinfoman, which are separate projects outside the group.",
        "nodesDir": "nodes"})
    g = info["ihris-suite"]
    write_json(os.path.join(base, "nodes", "project-group--ihris-suite.json"), node(
        "project-group/ihris-suite", "container", g.get("title") or "iHRIS Suite", [], "https://launchpad.net/ihris-suite",
        flavour="project-group", metadata_ref="records/project-group--ihris-suite.json", childCountUpstream=len(group_members)))
    write_json(os.path.join(base, "records", "project-group--ihris-suite.json"), {
        "$schema": "ihris-source-record/v1", "id": "project-group--ihris-suite", "node": "project-group/ihris-suite",
        "host": "launchpad", "level": "project-group", "refs": {"web": "https://launchpad.net/ihris-suite"},
        "project": {"name": "ihris-suite", "title": g.get("title"), "summary": g.get("summary"), "description": g.get("description"),
                    "registered": g.get("registered"), "homepage": g.get("homepage")},
        "capturedFrom": ["uploads/launchpad/projects/ihris-suite.html", "uploads/launchpad/projects/ihris-suite.rdf"],
        "capturedAt": CAPTURED_AT})
    rows = []
    for p in projects:
        if p == "ihris-suite":
            continue
        d = info[p]
        cls = classify(p)
        inst = f"src/{p}" if p in CORE else None
        parents = [["project-group/ihris-suite"]] if d.get("partOf") == "ihris-suite" else []
        nid = f"project/{p}"
        write_json(os.path.join(base, "nodes", fname(nid)), node(
            nid, "container", d["title"], parents, f"https://launchpad.net/{p}", flavour="project",
            metadata_ref=f"records/{fname(nid)}",
            note=(f"Described in depth by the `{p}` instance at {inst}/." if inst else None)))
        write_json(os.path.join(base, "records", fname(nid)), {
            "$schema": "ihris-source-record/v1", "id": fname(nid)[:-5], "node": nid, "host": "launchpad",
            **({"vcs": d["vcs"]} if d.get("vcs") else {}), "level": "project",
            "refs": {**({"lp": d["lp"][0]} if d["lp"] else {}), "web": f"https://launchpad.net/{p}"},
            "project": {"name": p, "title": d["title"], "summary": d.get("summary"), "description": d.get("description"),
                        "registered": d.get("registered"), "licences": d["licences"], "languages": d.get("languages", []),
                        "homepage": d.get("homepage"), "wiki": d.get("wiki"), "maintainer": d.get("maintainer"),
                        "partOf": d.get("partOf"), "classification": cls, "describedBy": inst},
            "capturedFrom": [f"uploads/launchpad/projects/{p}.html", f"uploads/launchpad/projects/{p}.rdf",
                             f"uploads/launchpad/projects/{p}__series.html"],
            "capturedAt": CAPTURED_AT})
        rows.append((cls, p, d, inst))

    # ---- one instance per core project: series -> releases, with branches and checksums
    for p in CORE:
        d = info[p]
        ib = os.path.join(ROOT, "src", p, "catalogue")
        clean_dir(ib)
        write_json(os.path.join(ib, "catalogue.json"), {
            "$schema": "folio-catalogue/v1", "id": p, "title": f"{d['title']} on Launchpad",
            "system": "Launchpad (Bazaar)", "baseUrl": f"https://launchpad.net/{p}",
            "sizeBasis": f"Series and milestones as listed on https://launchpad.net/{p}/+series, {CAPTURED_AT}. "
                         "Branch history, bugs and blueprints are NOT modelled: code/bugs/blueprints.launchpad.net are "
                         "egress-blocked from the capturing session.",
            "nodesDir": "nodes"})
        pid = f"project/{p}"
        write_json(os.path.join(ib, "nodes", fname(pid)), node(
            pid, "container", d["title"], [], f"https://launchpad.net/{p}", flavour="project",
            childCountUpstream=len(d["series"]), note=f"Project-level record: src/catalogue/records/{fname(pid)}."))
        all_ms = set()
        for s in d["series"]:
            sd = lp_series(p, s)
            sid = f"series/{p}/{s}"
            all_ms |= set(sd["milestones"])
            write_json(os.path.join(ib, "nodes", fname(sid)), node(
                sid, "container", f"{d['title']} {s} series", [[pid]], f"https://launchpad.net/{p}/{s}", flavour="series",
                metadata_ref=f"records/{fname(sid)}", childCountUpstream=len(sd["milestones"])))
            write_json(os.path.join(ib, "records", fname(sid)), {
                "$schema": "ihris-source-record/v1", "id": fname(sid)[:-5], "node": sid, "host": "launchpad", "vcs": "bzr",
                "level": "series",
                "refs": {**({"lp": sd["branches"][0]} if sd["branches"] else {}), "web": f"https://launchpad.net/{p}/{s}"},
                "series": {"name": s, "isDevelopmentFocus": d.get("focus") == s, "branches": sd["branches"], "milestones": sd["milestones"]},
                "capturedFrom": [f"uploads/launchpad/series/{p}@{s}.html"], "capturedAt": CAPTURED_AT})
        for m in sorted(all_ms):
            if not os.path.exists(os.path.join(UP, "launchpad/milestones", f"{p}@{m}.html")):
                continue
            md = lp_milestone(p, m, md5s)
            for f in md["files"]:
                if f["name"] == SUITE_FILE and f.get("md5") == suite["md5"]:
                    f["sha256"], f["bytes"], f["verifiedCopy"] = suite["sha256"], suite["bytes"], "uploads/ihris-suite-4.3.3/manifest.json"
            released = bool(md["released"])
            mid = f"{'release' if released else 'milestone'}/{p}/{m}"
            ser = md["series"] or "trunk"
            write_json(os.path.join(ib, "nodes", fname(mid)), node(
                mid, "item" if md["files"] else "container", f"{d['title']} {m}", [[pid, f"series/{p}/{ser}"]],
                f"https://launchpad.net/{p}/+milestone/{m}", flavour="release" if released else "milestone",
                metadata_ref=f"records/{fname(mid)}",
                bitstreams=[{"name": f["name"], **({"bytes": f["bytes"]} if "bytes" in f else {}),
                             "materialization": {"state": "referenced", "provenance": {"upstream": f["url"]},
                                                 **({"note": f"A copy was received {CAPTURED_AT} and its MD5 matched Launchpad's; it is "
                                                              "deliberately NOT committed (owner ruling: describe, do not materialize). "
                                                              f"See {f['verifiedCopy']}."} if f.get("verifiedCopy") else {})}}
                            for f in md["files"]] or None))
            write_json(os.path.join(ib, "records", fname(mid)), {
                "$schema": "ihris-source-record/v1", "id": fname(mid)[:-5], "node": mid, "host": "launchpad", "vcs": "bzr",
                "level": "release" if released else "milestone",
                "refs": {"web": f"https://launchpad.net/{p}/+milestone/{m}"},
                "release": md, "capturedFrom": [f"uploads/launchpad/milestones/{p}@{m}.html", "uploads/launchpad/release-file-md5.tsv"],
                "capturedAt": CAPTURED_AT})
    return info, rows


# ---------------------------------------------------------------- source tarball: modules + data model
def suite_tree() -> str | None:
    tb = os.path.join(UP, "ihris-suite-4.3.3", SUITE_FILE)
    if not os.path.exists(tb):
        return None
    dest = os.path.join(ROOT, ".build", "ihris-suite-4.3.3")
    if not os.path.isdir(dest):
        man = json.load(open(os.path.join(UP, "ihris-suite-4.3.3/manifest.json")))
        if hashlib.sha256(open(tb, "rb").read()).hexdigest() != man["sha256"]:
            raise SystemExit(f"{tb}: sha256 does not match manifest.json; refusing to derive nodes from it")
        os.makedirs(dest)
        with tarfile.open(tb, "r:bz2") as t:
            t.extractall(dest, filter="data")
    return dest


def _walk(node_, base, acc):
    for g in node_:
        if g.tag not in ("configurationGroup", "configuration"):
            continue
        p, name = g.get("path"), g.get("name")
        path = (p if p.startswith("/") else base.rstrip("/") + "/" + p) if p else base.rstrip("/") + "/" + name
        path = re.sub(r"^//?I2CE(?=/)", "", path)
        acc.append((path, g))
        if g.tag == "configurationGroup":
            _walk(g, path, acc)


def _val(g, n):
    for c in g.findall("configuration"):
        if c.get("name") == n:
            v = [(x.text or "").strip() for x in c.findall("value")]
            return v[0] if len(v) == 1 else (v or None)
    return None


def _rels(md, tag):
    out = []
    for q in md.findall(tag):
        d = {"module": q.get("name")}
        for c in q:
            d[c.tag] = c.get("version")
        out.append(d)
    return out


def build_modules():
    tree = suite_tree()
    if tree is None:
        print("  (suite tarball not present: keeping existing module/data-model nodes)")
        return None
    man = json.load(open(os.path.join(UP, "ihris-suite-4.3.3/manifest.json")))
    release_file = f"src/i2ce/catalogue/nodes/{fname('release/i2ce/' + SUITE_RELEASE)}"
    stats = {}
    for inst in ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify"]:
        pkg = os.path.join(tree, inst)
        mdir = os.path.join(ROOT, "src", inst, "modules", SUITE_RELEASE)
        ddir = os.path.join(ROOT, "src", inst, "data-model", SUITE_RELEASE)
        clean_dir(mdir), clean_dir(ddir)
        files = sorted(glob.glob(os.path.join(pkg, "**", "*.xml"), recursive=True))
        mods, by_dir, overlays = [], {}, []
        for f in files:
            raw = open(f, "rb").read()
            if b"<I2CEConfiguration" not in raw:
                continue
            r = ET.fromstring(re.sub(rb"<!DOCTYPE[^>]*>", b"", raw))
            md = r.find("metadata")
            if md is None:
                continue
            relpath = os.path.relpath(f, tree)
            loc = re.search(r"/configs/([a-z]{2,3}(?:_[A-Z]{2})?)/[^/]+\.xml$", relpath)
            if loc:
                # A locale overlay (translated strings for an existing module), not a module.
                overlays.append((r.get("name"), os.path.dirname(os.path.dirname(os.path.dirname(relpath))), loc.group(1), relpath))
                continue
            parts = relpath.split("/")
            site = parts[2] if len(parts) > 2 and parts[1] == "sites" else None
            t = lambda k, md=md: (md.findtext(k) or "").strip() or None  # noqa: E731  (bind md NOW; a late-binding closure read the last module)
            acc = []
            _walk(r, "", acc)
            forms, classes, pages, lists, records = [], [], [], collections.Counter(), []
            for path, g in acc:
                if g.tag != "configurationGroup":
                    continue
                # The object is named by the LAST segment of its resolved path, not by
                # the group's `name`: a group may carry `path=` and a throwaway name
                # (TrainingInstructor.xml: name="formClass" path=".../iHRIS_Scheduled_Training_Course").
                leaf = path.rsplit("/", 1)[-1]
                if re.fullmatch(r"/modules/forms/forms/[^/]+", path):
                    forms.append({"form": leaf, "class": _val(g, "class"),
                                  "displayName": _val(g, "display") or (g.findtext("displayName") or "").strip() or None})
                elif re.fullmatch(r"/modules/forms/formClasses/[^/]+", path):
                    flds = []
                    fg = [c for c in g.findall("configurationGroup") if c.get("name") == "fields"]
                    for fd in (fg[0].findall("configurationGroup") if fg else []):
                        hdr = _val(fd, "headers")
                        hdr = hdr[0] if isinstance(hdr, list) else hdr
                        meta = [c for c in fd.iter("configurationGroup") if c.get("name") == "meta"]
                        refs = sorted({(x.text or "").strip() for mg in meta for fgp in mg.iter("configurationGroup") if fgp.get("name") == "form"
                                       for x in fgp.iter("value") if (x.text or "").strip()} |
                                      {(x.text or "").strip() for mg in meta for c in mg.findall("configuration") if c.get("name") == "form"
                                       for x in c.findall("value") if (x.text or "").strip()})
                        flds.append({"field": fd.get("name"), "type": _val(fd, "formfield"),
                                     "label": (hdr or "").replace("default:", "") or None,
                                     "required": _val(fd, "required") == "true", "unique": True if _val(fd, "unique") == "true" else None,
                                     "references": refs or None})
                    classes.append({"class": leaf, "extends": _val(g, "extends"), "fields": flds})
                elif re.fullmatch(r"/page/[^/]+", path):
                    pages.append({"page": leaf, "class": _val(g, "class"), "style": _val(g, "style")})
                mm = re.fullmatch(r"/formsData/forms/([^/]+)/([^/]+)", path)
                if mm:
                    lists[mm.group(1)] += 1
                    fg = [c for c in g.findall("configurationGroup") if c.get("name") == "fields"]
                    vals = {}
                    for c in (fg[0].findall("configuration") if fg else []):
                        v = [(x.text or "").strip() for x in c.findall("value")]
                        vals[c.get("name")] = v[0] if len(v) == 1 else v
                    # Second storage format: `fields` as ONE delimited configuration, values "field:value".
                    for c in g.findall("configuration"):
                        if c.get("name") == "fields" and c.get("type") == "delimited":
                            for x in c.findall("value"):
                                k, sep, v = (x.text or "").strip().partition(":")
                                if sep:
                                    vals[k] = v
                    records.append({"form": mm.group(1), "id": mm.group(2), "fields": vals,
                                    "lastModified": _val(g, "last_modified"), "parent": _val(g, "parent")})
            mods.append(dict(name=r.get("name") or os.path.splitext(os.path.basename(f))[0] + "(unnamed)", relpath=relpath, dir=os.path.dirname(relpath), site=site, md=md, t=t,
                             forms=forms, classes=classes, pages=pages, lists=dict(lists), records=records, sha256=hashlib.sha256(raw).hexdigest()))
        # ids: module name, disambiguated by site when a site overrides a core module name
        # ids: the module name; where a name repeats (sites override core modules,
        # and one site may carry two same-named variants) qualify by site, then by
        # directory, until unique. Filenames compare case-insensitively.
        names = collections.Counter(m["name"].lower() for m in mods)
        for m in mods:
            m["base"] = m["name"] if names[m["name"].lower()] == 1 else (f"{m['name']}@{m['site']}" if m["site"] else f"{m['name']}@core")
        again = collections.Counter(m["base"].lower() for m in mods)
        for m in mods:
            if again[m["base"].lower()] > 1:
                m["base"] = f"{m['name']}@{slug(m['dir'].split('/', 1)[1] if '/' in m['dir'] else 'root')}"
            m["id"] = f"{inst}/module/{m['base']}"
            by_dir[m["dir"]] = m["id"]
        assert len({m["id"].lower() for m in mods}) == len(mods), f"{inst}: module ids not unique"
        # overlays whose directory holds no module of that name: attach by name alone when the name is unique
        loose = {(d, nm) for nm, d, _, _ in overlays if not any(m["name"] == nm and m["dir"] == d for m in mods)}
        class_acc = {}
        for m in mods:
            parent = None
            d = os.path.dirname(m["dir"])
            while d and d != inst:
                if d in by_dir:
                    parent = by_dir[d]
                    break
                d = os.path.dirname(d)
            cls_ids = []
            for c in m["classes"]:
                cid = f"{inst}/form-class/{c['class']}"
                cls_ids.append(cid)
                a = class_acc.setdefault(c["class"], {"extends": None, "definedIn": [], "fields": collections.OrderedDict()})
                a["extends"] = a["extends"] or c["extends"]
                a["definedIn"].append(m["id"])
                for fl in c["fields"]:
                    cur = a["fields"].setdefault(fl["field"], {**fl, "definedIn": []})
                    for k in ("type", "label", "references"):
                        if cur.get(k) in (None, []) and fl.get(k):
                            cur[k] = fl[k]
                    cur["required"] = cur.get("required") or fl["required"]
                    cur["definedIn"].append(m["id"])
            t = m["t"]
            out = {"$schema": "ihris-i2ce-module/v1", "id": m["id"], "module": m["name"], "instance": inst, "release": SUITE_RELEASE,
                   "source": {"releaseFile": release_file, "releaseFileMd5": man["md5"], "path": m["relpath"], "sha256": m["sha256"]},
                   "parent": parent, "site": m["site"], "displayName": t("displayName"), "description": t("description"),
                   "version": t("version"), "className": t("className"), "category": t("category"), "creator": t("creator"),
                   "link": t("link"), "requirements": _rels(m["md"], "requirement"), "enables": _rels(m["md"], "enable"),
                   "conflicts": _rels(m["md"], "conflict"), "optional": _rels(m["md"], "optional"),
                   "forms": m["forms"], "formClasses": sorted(set(cls_ids)), "pages": m["pages"], "dataLists": m["lists"],
                   "locales": sorted({lc for nm, d, lc, _ in overlays
                                      if nm == m["name"] and (d == m["dir"] or (d, nm) in loose and names[m["name"].lower()] == 1)})}
            write_json(os.path.join(mdir, fname(m["id"].split("/module/", 1)[1])), out)
        forms_by_class = collections.defaultdict(set)
        for m in mods:
            for f in m["forms"]:
                if isinstance(f["class"], str):
                    forms_by_class[f["class"]].add(f["form"])
        for cname, a in class_acc.items():
            write_json(os.path.join(ddir, fname(cname)), {
                "$schema": "ihris-form-class/v1", "id": f"{inst}/form-class/{cname}", "class": cname, "release": SUITE_RELEASE,
                "extends": a["extends"], "forms": sorted(forms_by_class.get(cname, [])), "definedIn": sorted(set(a["definedIn"])),
                "fields": [{**v, "definedIn": sorted(set(v["definedIn"]))} for v in a["fields"].values()]})
        orphans = [o for o in overlays if (o[1], o[0]) in loose and names[o[0].lower()] != 1 if o[0]]
        orphans += [o for o in overlays if (o[1], o[0]) in loose and o[0] and o[0].lower() not in names]
        if orphans:
            print(f"  {inst}: {len(orphans)} locale overlay(s) with no matching module, e.g. {orphans[0][3]}")
        # Shipped list records (//I2CE/formsData): one node per form, every record
        # attributed to its module and marked `sample` when that module is sample
        # data (SampleData-*, QualifySampleData-*, CommonSampleData, or a site).
        ldir = os.path.join(ROOT, "src", inst, "data-lists", SUITE_RELEASE)
        clean_dir(ldir)
        by_form = collections.defaultdict(list)
        for m in mods:
            sample = bool(m["site"]) or bool(re.match(r"(Qualify|Common)?SampleData", m["name"]))
            for r in m["records"]:
                by_form[r["form"]].append({**{k: v for k, v in r.items() if k != "form" and v is not None},
                                           "definedIn": m["id"], "provenance": "sample" if sample else "default"})
        for form, recs in sorted(by_form.items()):
            write_json(os.path.join(ldir, fname(form)), {
                "$schema": "ihris-data-list/v1", "id": f"{inst}/data-list/{form}", "form": form, "release": SUITE_RELEASE,
                "source": {"releaseFile": release_file, "releaseFileMd5": man["md5"]},
                "counts": dict(collections.Counter(r["provenance"] for r in recs)), "records": recs})
        stats[inst] = {"modules": len(mods), "localeOverlays": len(overlays), "dataLists": len(by_form), "formClasses": len(class_acc),
                       "fields": sum(len(a["fields"]) for a in class_acc.values()),
                       "described": sum(1 for m in mods if m["t"]("description")),
                       "sites": sorted({m["site"] for m in mods if m["site"]}),
                       "top": [(m["id"], m["t"]("displayName"), m["t"]("description")) for m in mods
                               if m["dir"].count("/modules/") <= 1 and not m["site"] and "/modules/" in m["relpath"]]}
    return stats


# ---------------------------------------------------------------- wiki (help pages shipped inside the tarball)
def build_wiki():
    tree = suite_tree()
    base = os.path.join(ROOT, "library", "ihris-wiki")
    if tree is None:
        print("  (suite tarball not present: keeping existing wiki capture)")
        return None
    from bs4 import BeautifulSoup
    from markdownify import markdownify
    lib = os.path.join(base, "osi-help-4.3.3")
    clean_dir(lib)
    pages = collections.OrderedDict()
    for pkg, mod in [("ihris-manage", "manage-help"), ("ihris-qualify", "qualify-help")]:
        for f in sorted(glob.glob(os.path.join(tree, pkg, "modules", mod, "static", "help", "*.html"))):
            raw = open(f, encoding="utf-8", errors="replace").read()
            soup = BeautifulSoup(raw, "html.parser")
            title = (soup.title.string if soup.title else os.path.basename(f)).replace(" - Osi", "").strip()
            body = soup.find(id="bodyContent") or soup.find(id="content") or soup.body
            for sel in ["#jump-to-nav", "#siteSub", "#contentSub", ".printfooter", ".catlinks", "#toc", ".visualClear", "script", "style"]:
                for x in body.select(sel):
                    x.decompose()
            md = markdownify(str(body), heading_style="ATX", strip=["span"]).strip()
            md = re.sub(r"\n{3,}", "\n\n", md)
            key = slug(title)
            h = hashlib.sha256(md.encode()).hexdigest()
            e = pages.setdefault(key, {"title": title, "variants": collections.OrderedDict()})
            v = e["variants"].setdefault(h, {"md": md, "shippedIn": []})
            v["shippedIn"].append(f"{pkg}/modules/{mod}/static/help/{os.path.basename(f)}")
    contains, structure = [], []
    for key, e in pages.items():
        for i, (h, v) in enumerate(e["variants"].items()):
            sid = key if i == 0 else f"{key}--variant-{i + 1}"
            front = (f"---\ntitle: \"{e['title']}\"\nsource: MediaWiki page exported into the iHRIS {SUITE_RELEASE} help modules\n"
                     f"shippedIn:\n" + "".join(f"  - {s}\n" for s in v["shippedIn"]) + f"licence: GPL-3.0 (as part of the iHRIS source)\n---\n\n")
            write_text(os.path.join(lib, "sections", sid + ".md"), front + f"# {e['title']}\n\n" + v["md"])
            write_json(os.path.join(lib, "sections", sid + ".jsonld"), {
                "@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld",
                "@id": f"library/ihris-wiki/osi-help-4.3.3/sections/{sid}", "@type": ["doco:Section"], "title": e["title"],
                "derivedFrom": "library/ihris-wiki/osi-help-4.3.3/manifest", "sourceDocument": "library/ihris-wiki/osi-help-4.3.3/manifest",
                "provenance": "ingested"})
            contains.append(f"library/ihris-wiki/osi-help-4.3.3/sections/{sid}")
            structure.append({"id": sid, "title": e["title"], "sha256": h, "shippedIn": v["shippedIn"]})
    write_json(os.path.join(lib, "manifest.jsonld"), {
        "@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld",
        "@id": "library/ihris-wiki/osi-help-4.3.3/manifest", "@type": ["folio:SourceDocument"],
        "title": f"iHRIS user manual pages (Osi wiki export) as shipped in iHRIS {SUITE_RELEASE}", "contains": contains})
    # Figures the pages reference by bare file name. I2CE serves them from modules/<mod>/images/help/.
    # They are GPL, shipped in the same release, so they are restored beside the pages and pinned by sha256.
    images = {}
    for key, e in pages.items():
        for v in e["variants"].values():
            for ref in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", v["md"]):
                name = os.path.basename(ref)
                if "/" in ref.split("?")[0].lstrip("./") or name in images:
                    continue
                found = [f"{pkg}/modules/{mod}/images/help/{name}" for pkg, mod in [("ihris-manage", "manage-help"), ("ihris-qualify", "qualify-help")]
                         if os.path.isfile(os.path.join(tree, pkg, "modules", mod, "images", "help", name))]
                if not found:
                    continue
                data = open(os.path.join(tree, found[0]), "rb").read()
                digests = {hashlib.sha256(open(os.path.join(tree, x), "rb").read()).hexdigest() for x in found}
                os.makedirs(os.path.join(lib, "images"), exist_ok=True)
                with open(os.path.join(lib, "images", name), "wb") as fh:
                    fh.write(data)
                images[name] = {"file": f"images/{name}", "sha256": hashlib.sha256(data).hexdigest(), "shippedIn": found,
                                **({"variantsDiffer": True} if len(digests) > 1 else {})}
    write_json(os.path.join(lib, "structure.json"), {"source": f"uploads/ihris-suite-4.3.3/{SUITE_FILE}",
                                                      "sourceSha256": json.load(open(os.path.join(UP, 'ihris-suite-4.3.3/manifest.json')))["sha256"],
                                                      "pages": structure, "images": [images[k] for k in sorted(images)]})
    return {"pages": len(pages), "sections": len(contains)}


# ---------------------------------------------------------------- toolkit
KIND = {"document": "document", "spreadsheet": "spreadsheet", "presentation": "presentation", "pdf": "pdf", "link": "external-link"}
STAGES = ["assess", "plan", "deploy", "pilot", "scale-up", "sustain"]


def parse_stage(path: str) -> dict:
    t = open(path, encoding="utf-8").read()
    url = re.search(r"saved from url=\(\d+\)(\S+) -->", t).group(1)
    art = re.search(r'<article id="post-(\d+)" class="([^"]+)"', t)
    tags = [x[4:] for x in art.group(2).split() if x.startswith("tag-")]
    nav = re.search(r'current-menu-item[^>]*><a title="([^"]+)" href="[^"]+"><span class="ordinal">(\d)</span><span class="name">([^<]+)', t)
    content = re.search(r'<div class="entry-content">(.*?)<div id="stage-steps">', t, re.S).group(1)
    intro = [x for x in (txt(p) for p in re.findall(r"<p>(.*?)</p>", content, re.S)) if x]
    emph = sorted({txt(e) for e in re.findall(r"<em>(.*?)</em>", content, re.S) if txt(e)})
    sh = t[t.find('<div id="stage-steps">'):t.find("<!-- .entry-content -->")]
    domains = []
    for blk in re.split(r'<div class="step">', sh)[1:]:
        h = txt(re.search(r"<h3>(.*?)</h3>", blk, re.S).group(1))
        items, cur = [], None
        for m in re.finditer(r"<p>(.*?)</p>", blk, re.S):
            inner = m.group(1)
            tools = []
            for attrs, lab in re.findall(r"<a ([^>]*)>(.*?)</a>", inner, re.S):
                href, cls = re.search(r'href="([^"]+)"', attrs), re.search(r'class="tool ([\w-]+)"', attrs)
                if cls:
                    hosted = href.group(1).startswith("https://toolkit.ihris.org/")
                    tools.append({"title": txt(lab), "href": href.group(1), "kind": KIND.get(cls.group(1), cls.group(1)),
                                  "hostedOnToolkit": hosted, "materialization": "referenced"})
            plain = txt(re.sub(r'<a [^>]*class="tool[^>]*>.*?</a>', "", inner, flags=re.S))
            if tools:
                if cur is None:
                    cur = {"objective": None, "tools": []}
                    items.append(cur)
                cur["tools"] += tools
            elif plain and not plain.startswith("Go to Stage") and not plain.startswith("Key question"):
                cur = {"objective": plain, "tools": []}
                items.append(cur)
        d = {"domain": h, "objectives": items}
        kq = [txt(x) for x in re.findall(r"<li>(.*?)</li>", blk, re.S)]
        if kq:
            d["keyQuestions"] = kq
        domains.append(d)
    side = t[t.find('<div id="secondary"'):]
    img = re.search(r'<img class="graph" src="[^"]*/([^"/]+)" alt="([^"]*)"', side)
    cap = re.search(r'<div class="stats">(.*?)</div>', side, re.S)
    ch = re.search(r'<div class="stage-challenges">\s*<h3>Challenges</h3>(.*?)</div>', side, re.S)
    defs = re.search(r'<div class="stage-definition">(.*?)</div>', side, re.S)
    terms = []
    for p in re.findall(r"<p>(.*?)</p>", defs.group(1), re.S) if defs else []:
        st = re.search(r"<strong>(.*?)</strong>", p, re.S)
        if st:
            terms.append({"term": txt(st.group(1)).rstrip(", "), "definition": txt(p)})
    comments = [{"author": txt(a), "date": d, "text": txt(c)} for a, d, c in
                re.findall(r'<b class="fn">(.*?)</b>.*?<time datetime="([^"]+)">.*?<div class="comment-content">(.*?)</div>', t, re.S)]
    return dict(ordinal=int(nav.group(2)), name=nav.group(3), tagline=nav.group(1), url=url, wpPageId=int(art.group(1)), tags=tags,
                intro=intro, emphasisedTerms=emph, domains=domains,
                graphic={"file": img.group(1), "alt": img.group(2), "caption": txt(cap.group(1)) if cap else None} if img else None,
                challenges=txt(ch.group(1)) if ch else None, technicalTerms=terms, comments=comments)


def build_toolkit():
    base = os.path.join(ROOT, "library", "ihris-toolkit")
    for sub in ("stages", "sections", "images"):
        clean_dir(os.path.join(base, sub))
    contains, stages = [], []
    for s in STAGES:
        cap = os.path.join(UP, "toolkit", s + ".html")
        if not os.path.exists(cap):
            continue
        st = parse_stage(cap)
        sid = f"{st['ordinal']}-{s}"
        if st["graphic"]:
            src = glob.glob(os.path.join(UP, "toolkit", f"{s}-{st['graphic']['file']}"))
            if src:
                dst = os.path.join(base, "images", f"{sid}-{st['graphic']['file']}")
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src[0], dst)
                st["graphic"]["localPath"] = rel(dst)
        rec = {"$schema": "ihris-toolkit-stage/v1", "id": f"ihris-toolkit/stage/{s}", **st, "capturedFrom": rel(cap)}
        write_json(os.path.join(base, "stages", sid + ".json"), rec)
        stages.append(rec)
        md = [f"---\ntitle: \"Stage {st['ordinal']}: {st['name']}: {st['tagline']}\"\nsource: {st['url']}\ncapturedFrom: {rel(cap)}\n---\n",
              f"# Stage {st['ordinal']}: {st['name']}\n", f"*{st['tagline']}*\n"]
        md += [p + "\n" for p in st["intro"]]
        md.append("## Objectives and deliverables\n")
        for d in st["domains"]:
            md.append(f"### {d['domain']}\n")
            for o in d["objectives"]:
                if o["objective"]:
                    md.append(o["objective"] + "\n")
                for tl in o["tools"]:
                    md.append(f"- [{tl['title']}]({tl['href']}) ({tl['kind']}{', hosted on the toolkit' if tl['hostedOnToolkit'] else ''})")
                if o["tools"]:
                    md.append("")
            if d.get("keyQuestions"):
                md.append("**Key questions:**\n")
                md += [f"- {q}" for q in d["keyQuestions"]] + [""]
        if st["graphic"]:
            md.append("## Figure\n")
            if st["graphic"].get("localPath"):
                md.append(f"![{st['graphic']['alt']}](../images/{os.path.basename(st['graphic']['localPath'])})\n")
            if st["graphic"]["caption"]:
                md.append(st["graphic"]["caption"] + "\n")
        if st["challenges"]:
            md += ["## Challenges\n", st["challenges"] + "\n"]
        if st["technicalTerms"]:
            md.append("## Technical terms\n")
            md += [f"- **{x['term']}**: {x['definition']}" for x in st["technicalTerms"]] + [""]
        write_text(os.path.join(base, "sections", sid + ".md"), "\n".join(md))
        write_json(os.path.join(base, "sections", sid + ".jsonld"), {
            "@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld",
            "@id": f"library/ihris-toolkit/sections/{sid}", "@type": ["doco:Section"], "title": f"Stage {st['ordinal']}: {st['name']}",
            "derivedFrom": "library/ihris-toolkit/manifest", "sourceDocument": "library/ihris-toolkit/manifest", "provenance": "ingested"})
        contains.append(f"library/ihris-toolkit/sections/{sid}")
    write_json(os.path.join(base, "manifest.jsonld"), {
        "@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld", "@id": "library/ihris-toolkit/manifest",
        "@type": ["folio:SourceDocument"], "title": "iHRIS Implementation Toolkit (toolkit.ihris.org), stage pages", "contains": contains})
    # the cross-cutting matrix: stage x domain -> objectives/tools
    domains = []
    for st in stages:
        for d in st["domains"]:
            if d["domain"] not in domains:
                domains.append(d["domain"])
    matrix = {d: {st["name"]: [o["objective"] for o in next((x for x in st["domains"] if x["domain"] == d), {"objectives": []})["objectives"] if o["objective"]]
                  for st in stages} for d in domains}
    tools = [{"stage": st["name"], "domain": d["domain"], **tl} for st in stages for d in st["domains"] for o in d["objectives"] for tl in o["tools"]]
    write_json(os.path.join(base, "structure.json"), {"stages": [f"{s['ordinal']}-{slug(s['name'])}" for s in stages], "domains": domains,
                                                      "matrix": matrix, "toolCount": len(tools),
                                                      "toolsHostedOnToolkit": sum(1 for t in tools if t["hostedOnToolkit"])})
    write_json(os.path.join(base, "tools-index.json"), tools)
    return {"stages": len(stages), "tools": len(tools), "hosted": sum(1 for t in tools if t["hostedOnToolkit"]), "domains": domains}


# ---------------------------------------------------------------- iHRIS 5 (GitHub)
def build_ihris5():
    snap = os.path.join(UP, "github")
    base = os.path.join(ROOT, "src", "ihris5", "catalogue")
    if not os.path.isdir(snap):
        return None
    clean_dir(base)
    write_json(os.path.join(base, "catalogue.json"), {
        "$schema": "folio-catalogue/v1", "id": "ihris5", "title": "iHRIS 5 on GitHub", "system": "GitHub (git)",
        "baseUrl": "https://github.com/iHRIS", "sizeBasis": "Two repositories modelled, each pinned at the commit read; the GitHub "
        "organisation's full repository list was not enumerated (API access is out of scope for the capturing session).", "nodesDir": "nodes"})
    out = {}
    for f in sorted(glob.glob(os.path.join(snap, "*.json"))):
        s = json.load(open(f))
        nid = f"repository/{s['repo']}"
        write_json(os.path.join(base, "nodes", fname(nid)), node(
            nid, "container", s["title"], [], s["url"], flavour="repository", metadata_ref=f"records/{fname(nid)}",
            note=f"Pinned at {s['commit'][:7]}; inventory at src/ihris5/inventory/{os.path.basename(f)}."))
        write_json(os.path.join(base, "records", fname(nid)), {
            "$schema": "ihris-source-record/v1", "id": fname(nid)[:-5], "node": nid, "host": "github", "vcs": "git", "level": "repository",
            "refs": {"web": s["url"], "git": s["url"] + ".git"},
            "repository": {"url": s["url"], "branch": s["branch"], "commit": s["commit"], "committedAt": s["committedAt"], "licence": s.get("licence")},
            "capturedFrom": [rel(f)], "capturedAt": CAPTURED_AT})
        dst = os.path.join(ROOT, "src", "ihris5", "inventory", os.path.basename(f))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(f, dst)
        out[s["repo"]] = s
    return out


# ---------------------------------------------------------------- docs
def build_docs(info, rows, mstats, wstats, tstats, g5):
    base = os.path.join(ROOT, "docs", "generated")
    clean_dir(base)
    L = ["# Launchpad inventory: the iHRIS Suite and related projects\n",
         f"*Generated by `src/tools/build_kg.py` from captures taken {CAPTURED_AT}. Do not edit by hand.*\n",
         "Classification follows the owner's ruling on issue #1: **core** = i2ce, ihris-common, ihris-manage, "
         "ihris-qualify, ihris-plan, openhie-pr. Core projects each have their own instance under `src/<project>/`.\n"]
    for cls in ["core", "tool", "related", "country-customization"]:
        rs = [r for r in rows if r[0] == cls]
        if not rs:
            continue
        L += [f"## {cls} ({len(rs)})\n", "| project | title | series | licence | summary |", "|---|---|---|---|---|"]
        for _, p, d, inst in sorted(rs, key=lambda r: r[1]):
            name = f"[`{p}`](../../{inst}/README.md)" if inst else f"[`{p}`](https://launchpad.net/{p})"
            summ = (d.get("summary") or "").replace("|", "\\|").replace("\n", " ")[:140]
            L.append(f"| {name} | {d['title']} | {', '.join(d['series'])} | {', '.join(d['licences'])} | {summ} |")
        L.append("")
    write_text(os.path.join(base, "launchpad-inventory.md"), "\n".join(L))
    if mstats:
        M = ["# I2CE modules and data model in iHRIS 4.3.3\n",
             f"*Generated from the checksum-verified `{SUITE_FILE}`. Do not edit by hand.*\n",
             "| instance | modules | with description | form classes | fields | sites |", "|---|---|---|---|---|---|"]
        for inst, s in mstats.items():
            M.append(f"| [`{inst}`](../../src/{inst}/README.md) | {s['modules']} | {s['described']} | {s['formClasses']} | {s['fields']} | {', '.join(s['sites'])} |")
        for inst, s in mstats.items():
            M += ["", f"## {inst}: top-level modules\n", "| module | name | description |", "|---|---|---|"]
            for mid, dn, desc in sorted(s["top"]):
                M.append(f"| `{mid.split('/module/')[1]}` | {dn or ''} | {(desc or '').replace('|', '/')[:160]} |")
        write_text(os.path.join(base, "i2ce-modules-4.3.3.md"), "\n".join(M))
    write_json(os.path.join(base, "build-stats.json"), {
        "launchpadProjects": len(rows), "modules": {k: {x: v for x, v in s.items() if x != "top"} for k, s in (mstats or {}).items()},
        "wiki": wstats, "toolkit": tstats, "ihris5": sorted(g5) if g5 else None})


def main():
    print("launchpad ...")
    info, rows = build_launchpad()
    print("modules + data model ...")
    mstats = build_modules()
    print("wiki help pages ...")
    wstats = build_wiki()
    print("toolkit ...")
    tstats = build_toolkit()
    print("ihris5 ...")
    g5 = build_ihris5()
    build_docs(info, rows, mstats, wstats, tstats, g5)
    print(json.dumps({"projects": len(rows), "modules": {k: v["modules"] for k, v in (mstats or {}).items()},
                      "wiki": wstats, "toolkit": {k: v for k, v in tstats.items() if k != "domains"}, "ihris5": sorted(g5) if g5 else None}, indent=1))


if __name__ == "__main__":
    main()
