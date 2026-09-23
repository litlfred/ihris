#!/usr/bin/env python3
"""Parse the four 2009 iHRIS use-case reports into library/ihris-use-cases/.

The sources are Serlio CaseComplete "Complete Report" exports (Word 97 .doc) for
iHRIS Common, Manage, Qualify and Plan, uploaded by the owner and published with
the owner's permission (2026-09-23, see ihris-use-cases.json).

Deterministic, in order:

1. Verify each uploads/ihris-use-cases/*.doc against manifest.json (md5 AND sha256).
2. Extract text with `antiword -w 0` (tables come out as |cell|cell| rows at a fixed width).
3. Parse packages -> use cases (every Details field, Main Success Scenario steps,
   Extensions, Notes, Referenced Requirements), actors (goals, notes, the use cases
   each plays a role in) and requirements. A table row that fills its column to the
   last character wrapped, and the next row continues it; a Notes row with no date
   continues the note above. Anything the parser does not recognise stops it: it
   never skips text silently.
4. Record references the reports cite but never describe (dangling), across all four.
5. Crosswalk every use case to the iHRIS 4.3.3 data model in this repository
   (src/*/modules, src/*/data-model), by NAME MATCHING only: a form matches when its
   name (underscores as spaces) or its module-declared display name occurs, word for
   word, in the use case's title (simple plural folding on both sides). Unmatched use
   cases stay null (AGENTS.md §7). iHRIS Plan has no data model here, so its entries
   say so instead of matching.
6. Declare the actors the reports describe (A-PT1 HR Manager, ...) as ROLES in the
   iHRIS domain: scenarios/roles.json, folio-assistant's `scenarios` graph kind
   (RoleGraphSchema, cat-harness/schemas/role-graph.ts). Each use case's primary and
   supporting actors become role ids, resolved by name within the product and then in
   Common. A name that resolves to nothing stops the build.
7. The glossary. Each report's document summary (OLE SummaryInformation, read with
   olefile) has the Subject "Use cases, actor goal list, glossary and packages". Record
   that claim, and whether the report TEXT holds a glossary: any line naming a glossary
   stops the build until the parser reads it verbatim, and none found means `terms: []`
   and a note saying what was checked. A glossary is never invented
   (src/tools/build_glossary.py turns what is recorded into the SKOS glossary).
8. Write <product>.json (ihris-use-cases/v1), <product>.md, roles.md, crosswalk.json
   (ihris-use-case-crosswalk/v1) and manifest.jsonld.
9. Leak check: fail if any withheld name or initials appear as a whole token in
   library/ihris-use-cases/ or in the built site (built into a temporary directory).
   Only this tool holds the uploads, so only it can run this check; CI cannot.

Withheld on purpose: `Assigned To` (staff initials) and a requirement's `Source`
(a named person). Owner, 2026-09-23: one OPAQUE actor per distinct person,
scenarios/actors/ihris-2009-staff-NN.json (folio-assistant's ActorDef), and the field
becomes {"actor": "ihris-2009-staff-NN"}. NN is the order of first appearance, reading
Common, Manage, Qualify, Plan, each in document order. Who a number stands for lives
in the data store only: this tool holds it in memory while it runs and never writes it.

  python3 src/tools/ingest_use_cases.py      # needs antiword and olefile
"""
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UP = os.path.join(ROOT, "uploads", "ihris-use-cases")
OUT = os.path.join(ROOT, "library", "ihris-use-cases")
ENTRY = "library/ihris-use-cases"
RELEASE = "4.3.3"
PRODUCTS = {"common": "iHRIS Common", "manage": "iHRIS Manage", "qualify": "iHRIS Qualify", "plan": "iHRIS Plan"}
# The packages whose data model a product's use cases may be matched against.
SCOPE = {"common": ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify"],
         "manage": ["i2ce", "ihris-common", "ihris-manage"],
         "qualify": ["i2ce", "ihris-common", "ihris-qualify"],
         "plan": []}
DETAIL_LABELS = {"Parent": "parent", "Primary Actors": "primaryActors", "Supporting Actors": "supportingActors",
                 "Preconditions": "preconditions", "Success Guarantee": "successGuarantee", "Level": "level",
                 "Complexity": "complexity", "Use Case Status": "status", "Implementation Status": "implementationStatus",
                 "Assigned To": "assignedTo", "Release": "release", "Type": "type", "Status": "status", "Source": "source"}
WITHHELD = {"assignedTo": "staff initials", "source": "a named person"}
WHY = {k: f"{v}: referenced by an opaque actor (scenarios/actors/ihris-2009-staff-NN.json), identity withheld"
       for k, v in WITHHELD.items()}
FIELD_LABEL = {"assignedTo": "Assigned To", "source": "Source"}
STAFF = "ihris-2009-staff-{:02d}"
SCEN = os.path.join(OUT, "scenarios")
# Forms left out of matching: the csd_* forms are the OpenHIE Care Services Discovery model added to
# ihris-common long after these 2009 use cases, and their generic display names ("Service",
# "Organization", "Facility") would match titles that mean something else.
EXCLUDE_PREFIX = ("csd_",)


def md5_sha(p):
    b = open(p, "rb").read()
    return hashlib.md5(b).hexdigest(), hashlib.sha256(b).hexdigest()


def iso(d):
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", d.strip())
    return datetime.date(int(m.group(3)), int(m.group(1)), int(m.group(2))).isoformat() if m else None


def clean(s):
    return " ".join(s.split())


def join(a, b):
    return clean((a or "") + " " + b)


class ParseError(Exception):
    pass


# ------------------------------------------------------------------ the glossary
def report_glossary(path, text, product):
    """(Subject, glossary record) for one report. The Subject is the document summary's; the glossary
    is read from the report TEXT. A line naming a glossary stops the build: its entries must be parsed
    verbatim, and this parser does not read one yet, so it may not guess at one or skip it."""
    try:
        import olefile
    except ImportError:
        sys.exit("olefile is needed to read the report's document summary: pip install olefile")
    with olefile.OleFileIO(path) as ole:
        raw = ole.get_metadata().subject or b""
    subject = raw.decode("cp1252").strip()
    for n, line in enumerate(text.split("\n"), 1):
        if re.search(r"\bglossar", line, re.I):
            raise ParseError(f"{product} line {n}: the report text names a glossary; parse its entries verbatim "
                             "(term and definition) before deriving anything from this report")
    claimed = subject if re.search(r"\bglossar", subject, re.I) else None
    note = ("The document summary's Subject names a glossary, but the report text holds none: no line of the "
            "extracted text (antiword -w 0) names a glossary, and everything after the table of contents parses as "
            "packages, actors, use cases and requirements. No term is recorded, and none is invented.") if claimed else \
        "The report neither names a glossary nor holds one."
    return subject, {"claimedBy": f"document summary, Subject: {claimed}" if claimed else None, "found": False, "terms": [], "note": note}


# ------------------------------------------------------------------ the report
def cells(line):
    """Raw cell strings of a |a|b| row (padding kept: a cell with no trailing space was filled)."""
    return line.rstrip("\n")[1:].rstrip()[:-1].split("|") if line.rstrip().endswith("|") else line[1:].split("|")


def read_table(lines, i):
    rows = []
    while i < len(lines) and lines[i].startswith("|"):
        rows.append(cells(lines[i]))
        i += 1
    return rows, i


def wraps(prev_raw, cur_raw):
    """Did the row above wrap into this one? Word wrap moved this row's first word down because it
    did not fit in what was left of the row above. A row above that ends a sentence, followed by
    one that starts with a capital, is two items even so."""
    prev, cur = prev_raw.rstrip(), cur_raw.strip()
    if not prev.strip() or not cur:
        return False
    if prev.endswith((".", ":")) and cur[0].isupper():
        return False
    if cur.startswith(("http://", "https://")):
        return False  # one link per row
    return len(prev) + 1 + len(cur.split()[0]) > len(prev_raw)


def single_col(rows):
    """Items of a one-column table, wrapped rows joined."""
    out, prev = [], ""
    for r in rows:
        t = clean(r[0])
        if out and wraps(prev, r[0]):
            out[-1] = join(out[-1], t)
        elif t:
            out.append(t)
        prev = r[0]
    return out


def parse_notes(rows):
    out = []
    for r in rows[1:]:
        text, date = clean(r[0]), clean(r[1]) if len(r) > 1 else ""
        if not text and not date:
            continue
        if not date and out:
            out[-1]["text"] = join(out[-1]["text"], text)
        else:
            out.append({"text": text, "dateAdded": date or None, "date": iso(date) if date else None})
    return out


def parse_details(rows, rec, staff):
    last, order = [None, None], []
    for r in rows[1:]:
        for col, raw in enumerate(r[:2]):
            t = clean(raw)
            if not t:
                continue
            m = re.match(r"^(" + "|".join(map(re.escape, DETAIL_LABELS)) + r"):\s*(.*)$", t)
            if m:
                key = DETAIL_LABELS[m.group(1)]
                last[col] = key
                order.append(key)
                rec[key] = m.group(2) or None
            elif last[col]:
                rec[last[col]] = join(rec.get(last[col]), t)
            else:
                raise ParseError(f"details row with no label: {t!r}")
    for k in sorted(WITHHELD, key=lambda k: order.index(k) if k in order else len(order)):
        v = rec.pop(k, None)
        if v:
            staff.append((k, v, rec))  # held in memory only; replaced by an opaque actor before anything is written
    for k in ("primaryActors", "supportingActors"):
        if k in rec:
            rec[k] = [a.strip() for a in (rec[k] or "").split(",") if a.strip()]


def parse_flow(rows, uc, stats):
    steps, exts, phase, prev = [], [], None, ""
    for r in rows[1:]:
        raw = r[0]
        t = clean(raw)
        prev_full = wraps(prev, raw)
        prev = raw
        if t == "Main Success Scenario:":
            phase, prev = "mss", ""
            continue
        if t == "Extensions:":
            phase, prev = "ext", ""
            continue
        if not t:
            continue
        if phase == "mss":
            if prev_full and steps:
                tgt = steps[-1]["options"] if steps[-1].get("options") else None
                if tgt:
                    tgt[-1] = join(tgt[-1], t)
                else:
                    steps[-1]["text"] = join(steps[-1]["text"], t)
            elif steps and steps[-1]["text"].endswith(":") and not t.endswith((".", ":")):
                steps[-1].setdefault("options", []).append(t)
            else:
                steps.append({"step": len(steps) + 1, "text": t})
        elif phase == "ext":
            m = re.match(r"^(\*|\d+(?:\.\d+)*)\.([a-z])\s+(.*)$", t)
            n = re.match(r"^(\d+)\.\s+(.*)$", t)
            if prev_full and exts and not m and not n:
                tgt = exts[-1]["steps"][-1] if exts[-1]["steps"] else exts[-1]
                tgt["text"] = join(tgt["text"], t)
            elif m:
                exts.append({"id": f"{m.group(1)}.{m.group(2)}", "atStep": m.group(1), "text": m.group(3), "steps": []})
            elif n and exts:
                exts[-1]["steps"].append({"step": int(n.group(1)), "text": n.group(2)})
            elif exts and exts[-1]["steps"]:
                # an unnumbered row under an extension step: an option list, as in the main scenario
                exts[-1]["steps"][-1].setdefault("options", []).append(t)
                stats["unnumbered extension rows"] = stats.get("unnumbered extension rows", 0) + 1
            else:
                raise ParseError(f"{uc['id']}: extension row not understood: {t!r}")
        else:
            raise ParseError(f"{uc['id']}: flow row outside a section: {t!r}")
    uc["mainSuccessScenario"], uc["extensions"] = steps, exts


def parse_report(text, product):
    lines = text.split("\n")
    head = {}
    for j, l in enumerate(lines[:12]):
        if l.startswith("Generated by "):
            head["generator"] = l[len("Generated by "):].strip()
            head["generatedAt"] = lines[j + 1].strip()
    top = next(i for i, l in enumerate(lines) if re.match(r"^1\. \S", l))
    toc_actors = {m.group(1): clean(m.group(2)) for l in lines[:top] for m in [re.match(r"^\s+(A-[A-Z]+\d+) (.+?)\t", l)] if m}
    root = {"number": "1", "name": lines[top][3:].strip(), "level": 1, "description": None, "notes": [], "relatedDocuments": [],
            "packages": [], "useCases": [], "requirements": []}
    doc = {"actors": [], "root": root}
    stack = [root]
    ctx = root
    staff, stats = [], {}
    i = top + 1
    after_header = True  # the lines right after a heading are its description
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1
            continue
        m = re.match(r"^( +)(\d+)\. (\S.*)$", l)
        if m and not l.startswith("|"):
            level = {2: 2, 3: 3, 4: 4}.get(len(m.group(1)))
            if level is None:
                raise ParseError(f"line {i + 1}: package heading at an unknown indent: {l!r}")
            while stack[-1]["level"] >= level:
                stack.pop()
            parent = stack[-1]
            pkg = {"number": f"{parent['number']}.{m.group(2)}", "name": m.group(3).strip(), "level": level, "description": None,
                   "notes": [], "relatedDocuments": [], "packages": [], "useCases": [], "requirements": []}
            parent["packages"].append(pkg)
            stack.append(pkg)
            ctx, after_header = pkg, True
            i += 1
            continue
        if l.startswith("|"):
            rows, i = read_table(lines, i)
            first = clean(rows[0][0])
            second = clean(rows[0][1]) if len(rows[0]) > 1 else ""
            if re.match(r"^UC-[A-Z]+\d+ ", first):
                uid, title = first.split(" ", 1)
                ctx = {"id": uid, "title": title, "priority": second or None, "package": stack[-1]["number"], "description": None}
                stack[-1]["useCases"].append(ctx)
                after_header = True
            elif re.match(r"^REQ-[A-Z]+\d+ ", first):
                rid, name = first.split(" ", 1)
                ctx = {"id": rid, "name": name, "priority": second or None, "package": stack[-1]["number"], "description": None}
                stack[-1]["requirements"].append(ctx)
                after_header = True
            elif re.match(r"^A-[A-Z]+\d+ ", first) and len(rows) == 1:
                aid, name = first.split(" ", 1)
                ctx = {"id": aid, "name": name, "description": None, "goals": [], "notes": [], "useCases": []}
                doc["actors"].append(ctx)
                after_header = True
            elif first == "Notes":
                ctx.setdefault("notes", []).extend(parse_notes(rows))
            elif first == "Related Documents":
                ctx.setdefault("relatedDocuments", []).extend(single_col(rows[1:]))
            elif first == "Goals":
                ctx["goals"] = single_col(rows[1:])
            elif first == "Details":
                parse_details(rows, ctx, staff)
            elif first == "Flow of Events":
                parse_flow(rows, ctx, stats)
            elif first == "Referenced Requirements":
                refs = []
                for r in rows[1:]:
                    t, typ, rid = clean(r[0]), clean(r[1]), clean(r[2])
                    if rid:
                        refs.append({"id": rid, "type": typ, "text": t})
                    elif refs:
                        refs[-1]["text"] = join(refs[-1]["text"], t)
                ctx["referencedRequirements"] = refs
            elif first == "Use cases that reference this requirement":
                ctx["referencedBy"] = [clean(r[1]) for r in rows[1:] if clean(r[1])]
            elif first == "Report Contents:":
                pass
            else:
                raise ParseError(f"{product} line {i}: unknown table {first!r}")
            if not re.match(r"^(UC|REQ|A)-[A-Z]+\d+ ", first):
                after_header = False
            continue
        if l.strip() == "Use cases that this actor plays a role in:":
            i += 1
            while i < len(lines) and lines[i].strip():
                mm = re.match(r"^\s*[.•]\s+(.*?)\s*\((UC-[A-Z]+\d+)\)\s*$", lines[i])
                if not mm:
                    raise ParseError(f"{product} line {i + 1}: actor use-case line not understood: {lines[i]!r}")
                ctx["useCases"].append({"id": mm.group(2), "title": clean(mm.group(1))})
                i += 1
            continue
        if after_header:
            ctx["description"] = (ctx["description"] + "\n\n" if ctx.get("description") else "") + l.strip()
            i += 1
            continue
        raise ParseError(f"{product} line {i + 1}: text not understood: {l!r}")
    return doc, head, toc_actors, staff, stats


def walk(pkg):
    yield pkg
    for p in pkg["packages"]:
        yield from walk(p)


def refs_in(obj):
    return set(re.findall(r"\b(UC-[A-Z]+\d+|REQ-[A-Z]+\d+)\b", json.dumps(obj)))


# ------------------------------------------------------------------ crosswalk
def fold(tok):
    if len(tok) > 4 and tok.endswith("ies"):
        return tok[:-3] + "y"
    if tok.endswith("sses"):
        return tok[:-2]
    if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
        return tok[:-1]
    return tok


def toks(s):
    return [fold(t) for t in re.findall(r"[a-z0-9]+", s.lower().replace("'s", ""))]


def data_model_forms():
    """{package: {form: {class, displayNames, modules}}} from src/*/modules and src/*/data-model at RELEASE."""
    out = {}
    for pkg in {p for s in SCOPE.values() for p in s}:
        forms = out.setdefault(pkg, {})
        for f in sorted(glob.glob(os.path.join(ROOT, "src", pkg, "modules", RELEASE, "*.json"))):
            m = json.load(open(f))
            for x in m.get("forms") or []:
                e = forms.setdefault(x["form"], {"class": None, "displayNames": set(), "modules": set()})
                e["modules"].add(m["id"])
                if x.get("class"):
                    e["class"] = e["class"] or x["class"]
                if x.get("displayName"):
                    e["displayNames"].add(x["displayName"])
        for f in sorted(glob.glob(os.path.join(ROOT, "src", pkg, "data-model", RELEASE, "*.json"))):
            c = json.load(open(f))
            for form in c.get("forms") or []:
                e = forms.setdefault(form, {"class": None, "displayNames": set(), "modules": set()})
                e["class"] = e["class"] or c["class"]
                e["classId"] = c["id"]
                e["modules"].update(c.get("definedIn") or [])
    return out


def match_title(title, candidates):
    """[(form entry, matchedOn, matchedText, span)] for each longest phrase found in the title."""
    tt = toks(title)
    hits = []
    for pkg, form, e in candidates:
        phrases = [("form name", form.replace("_", " "))] + [("display name", d) for d in sorted(e["displayNames"])]
        for on, ph in phrases:
            pt = toks(ph)
            if not pt:
                continue
            for k in range(len(tt) - len(pt) + 1):
                if tt[k:k + len(pt)] == pt:
                    hits.append((pkg, form, e, on, ph, (k, k + len(pt))))
                    break
    # drop a hit whose span sits strictly inside a longer hit's span
    keep = [h for h in hits if not any(o[5][0] <= h[5][0] and h[5][1] <= o[5][1] and (o[5][1] - o[5][0]) > (h[5][1] - h[5][0]) for o in hits)]
    best = {}
    for h in keep:  # one entry per (package, form); prefer the form-name match
        k = (h[0], h[1])
        if k not in best or (best[k][3] != "form name" and h[3] == "form name"):
            best[k] = h
    return [best[k] for k in sorted(best)]


def crosswalk(docs):
    dm = data_model_forms()
    entries = []
    for product, doc in docs.items():
        cands = [(pkg, form, e) for pkg in SCOPE[product] for form, e in sorted(dm.get(pkg, {}).items()) if not form.startswith(EXCLUDE_PREFIX)]
        for p in walk(doc["root"]):
            for uc in p["useCases"]:
                if not SCOPE[product]:
                    entries.append({"useCase": uc["id"], "product": product, "title": uc["title"], "status": "no-data-model", "matches": None})
                    continue
                hs = match_title(uc["title"], cands)
                entries.append({"useCase": uc["id"], "product": product, "title": uc["title"],
                                "status": "matched" if hs else "unmatched",
                                "matches": [{"form": form, "class": e["class"], "package": pkg,
                                             "formClass": e.get("classId"), "modules": sorted(e["modules"]),
                                             "matchedOn": on, "matchedText": ph, "derivedBy": "name-match"}
                                            for pkg, form, e, on, ph, _ in hs] or None})
    from collections import Counter
    c = Counter(e["status"] for e in entries)
    return {
        "$schema": "ihris-use-case-crosswalk/v1",
        "release": RELEASE,
        "method": ("Name matching only (src/tools/ingest_use_cases.py): a form matches a use case when the form's name, with underscores read as "
                   "spaces, or a display name a module declares for it, occurs word for word in the use case's TITLE, after folding simple plurals "
                   "on both sides. A shorter match inside a longer one is dropped. Nothing is inferred from meaning: an unmatched use case has "
                   "`matches: null` until a person links it (AGENTS.md §7). Every link says `derivedBy: name-match`."),
        "scope": {k: v for k, v in SCOPE.items()},
        "excludedForms": "forms whose name starts with csd_ (the OpenHIE Care Services Discovery model, added to ihris-common after 2009)",
        "noDataModel": {"plan": "iHRIS Plan has no data model in this repository: src/ihris-plan holds series and releases only, and its modules "
                                "need a release tarball (see src/ihris-plan/README.md). Its use cases are listed with status no-data-model."},
        "counts": {"matched": c.get("matched", 0), "unmatched": c.get("unmatched", 0), "no-data-model": c.get("no-data-model", 0),
                   "links": sum(len(e["matches"] or []) for e in entries)},
        "entries": entries,
    }


# ------------------------------------------------------------------ roles and opaque actors
def shape(v):
    """What a withheld value looks like, never what it says (for error messages)."""
    return re.sub(r"[a-z]", "x", re.sub(r"[A-Z]", "X", v))


def person_key(field, v):
    """The same initials, or the same name, is the same person. A requirement's Source may add a
    parenthesised qualifier after the name; it is part of the withheld field, not of the name."""
    v = clean(v)
    if field == "assignedTo":
        if not re.fullmatch(r"[A-Z]{2,4}", v):
            raise ParseError(f"Assigned To is not initials (shape {shape(v)!r}): teach person_key this form")
        return ("initials", v), [v]
    m = re.fullmatch(r"([A-Z][A-Za-z'.-]+(?: [A-Z][A-Za-z'.-]+)+)(?: \([^()]+\))?", v)
    if not m:
        raise ParseError(f"Source is not one person's name (shape {shape(v)!r}): teach person_key this form")
    name = m.group(1)
    return ("name", name.casefold()), [name] + [w for w in name.split() if len(w) >= 3]


def assign_staff(staff_by_product):
    """Number each distinct person in order of first appearance (PRODUCTS order, then document order),
    and replace every withheld value with {"actor": id}. Returns the actor records and, in memory only,
    the strings the leak check must never find."""
    ids, actors, secrets = {}, {}, []
    for product in PRODUCTS:
        for field, value, rec in staff_by_product[product]:
            key, toks = person_key(field, value)
            if key not in ids:
                ids[key] = STAFF.format(len(ids) + 1)
                actors[ids[key]] = {"fields": [], "products": []}
            aid = ids[key]
            for lst, x in ((actors[aid]["fields"], field), (actors[aid]["products"], product)):
                if x not in lst:
                    lst.append(x)
            secrets += [(key[0], t) for t in toks]
            rec[field] = {"actor": aid}
    out = []
    for aid, a in actors.items():
        n = aid.rsplit("-", 1)[1]
        where = " and ".join(f"“{FIELD_LABEL[f]}”" for f in a["fields"])
        prods = ", ".join(PRODUCTS[p] for p in a["products"])
        out.append({"id": aid, "title": f"2009 iHRIS staff member {n} (identity withheld)", "kind": "person",
                    "description": (f"A person the 2009 iHRIS use-case model names in its {where} field ({prods}). Opaque on purpose: "
                                    "who this is is withheld, and the mapping from the person to this actor lives in the data store "
                                    "only, never in this repository. Numbered in order of first appearance.")})
    return out, sorted(set(secrets))


def role_id(aid):
    return "ihris-" + aid.lower()


def build_roles(docs):
    """One Role per actor the reports describe, in PRODUCTS order then document order. Title and
    description are the document's own; an actor with no description cannot be a Role (a Role needs
    one), and none is invented."""
    roles = []
    for product in PRODUCTS:
        for a in docs[product]["actors"]:
            if not a.get("description"):
                raise ParseError(f"{product}: actor {a['id']} has no description, and a Role needs one: ask the owner")
            a["role"] = role_id(a["id"])
            roles.append({"id": a["role"], "title": a["name"], "description": a["description"],
                          "actorKinds": ["person"], "skills": []})
    if len({r["id"] for r in roles}) != len(roles):
        raise ParseError("two actors share an id across the reports")
    return roles


def resolve_actors(docs):
    """Each use case's primary and supporting actors, by name: within the product, then in Common.
    A name that resolves to nothing, or to two actors, stops the build."""
    by = {p: {} for p in PRODUCTS}
    for p in PRODUCTS:
        for a in docs[p]["actors"]:
            if a["name"] in by[p]:
                raise ParseError(f"{p}: two actors are named {a['name']!r}")
            by[p][a["name"]] = a["role"]
    bad, n = [], 0
    for p in PRODUCTS:
        for pkg in walk(docs[p]["root"]):
            for uc in pkg["useCases"]:
                for k in ("primaryActors", "supportingActors"):
                    if k not in uc:
                        continue
                    ids = []
                    for name in uc[k]:
                        rid = by[p].get(name) or by["common"].get(name)
                        if not rid:
                            bad.append(f"{p} {uc['id']} {k}: {name!r}")
                        ids.append(rid)
                        n += 1
                    uc[k] = ids
    if bad:
        raise ParseError("actor names that resolve to no role:\n  " + "\n  ".join(bad))
    return n


def write_scenarios(roles, actors):
    os.makedirs(os.path.join(SCEN, "actors"), exist_ok=True)
    graph = {"_comment": ("GENERATED by src/tools/ingest_use_cases.py; do not edit. The actors the 2009 iHRIS use-case reports describe, "
                          "declared as Roles in the iHRIS domain (folio-assistant's scenarios graph kind, RoleGraphSchema; "
                          "cat-harness/docs/proposals/odrl-prov-actor-model.md section 5 step 6). Title and description are the "
                          "report's own words. A-ICE4 and A-PS6 are both 'Any User': two roles, their equivalence undecided."),
             "name": "ihris-use-cases", "roles": roles}
    with open(os.path.join(SCEN, "roles.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=1, ensure_ascii=False)
        f.write("\n")
    keep = set()
    for a in actors:
        fn = a["id"] + ".json"
        keep.add(fn)
        with open(os.path.join(SCEN, "actors", fn), "w", encoding="utf-8") as f:
            json.dump(a, f, indent=1, ensure_ascii=False)
            f.write("\n")
    for fn in os.listdir(os.path.join(SCEN, "actors")):
        if fn not in keep:
            os.remove(os.path.join(SCEN, "actors", fn))


def write_roles_md(roles, actors, docs):
    plays, refs = {}, {}
    for p in PRODUCTS:
        for pkg in walk(docs[p]["root"]):
            for uc in pkg["useCases"]:
                for k in ("primaryActors", "supportingActors"):
                    for r in uc.get(k) or []:
                        plays.setdefault(r, []).append(uc["id"])
                if uc.get("assignedTo"):
                    refs.setdefault(uc["assignedTo"]["actor"], []).append(f"{uc['id']} (Assigned To)")
            for r in pkg["requirements"]:
                if r.get("source"):
                    refs.setdefault(r["source"]["actor"], []).append(f"{r['id']} (Source)")
    src = {a["role"]: (p, a["id"]) for p in PRODUCTS for a in docs[p]["actors"]}
    L = ["---", 'title: "Roles and actors in the iHRIS use-case model (2009)"', "---", "",
         "# Roles and actors (2009 use cases)", "",
         "*Generated by `src/tools/ingest_use_cases.py` from the same reports; do not edit by hand. The data is "
         "[`scenarios/roles.json`](scenarios/roles.json) (folio-assistant's `scenarios` graph kind) and "
         "[`scenarios/actors/`](scenarios/actors/).*", "",
         "## Roles", "",
         "Each actor a report describes is a **role** in the iHRIS domain. Title and description are the report's own. "
         "A-ICE4 (Common) and A-PS6 (Qualify) are both “Any User”: they are kept as two roles, and whether they are "
         "the same is undecided.", ""]
    for r in esc_all(roles):
        p, aid = src[r["id"]]
        L += [f'<a id="{r["id"]}"></a>', "", f"### {r['title']}", "",
              f"`{r['id']}`: {aid} in {PRODUCTS[p]}.", "", r["description"], ""]
        if plays.get(r["id"]):
            L += ["Plays in: " + ", ".join(sorted(set(plays[r["id"]]), key=lambda x: plays[r["id"]].index(x))), ""]
    L += ["## Opaque actors", "",
          "People the reports name in “Assigned To” (staff initials) or in a requirement’s “Source”. "
          "Each distinct person is one actor, and who they are is withheld: the mapping lives in the data store only.", ""]
    for a in esc_all(actors):
        L += [f'<a id="{a["id"]}"></a>', "", f"### {a['title']}", "", f"`{a['id']}`, kind `{a['kind']}`.", "", a["description"], "",
              "Referenced by: " + ", ".join(refs.get(a["id"], [])), ""]
    with open(os.path.join(OUT, "roles.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L).rstrip() + "\n")


def leak_check(secrets):
    """Fail if a withheld string appears as a whole token in library/ihris-use-cases/ or in the built site.
    Names are checked case-insensitively everywhere. Initials are case-sensitive, and in the built site
    are checked on the use-case pages only: short initials collide with ordinary tokens (country codes,
    abbreviations) on pages that never read the use cases. Findings name the file, never the string."""
    import tempfile
    site = tempfile.mkdtemp(prefix="ihris-site-")
    try:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "src", "tools", "build_site.py"), "--out", site],
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("leak check: the site did not build:\n" + (r.stdout + r.stderr)[-2000:])
        scopes = [(OUT, OUT, None), (site, os.path.join(site, "library", "use-cases"), "names-only-outside")]
        found = []
        for i, (kind, tok) in enumerate(secrets):
            rx = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(tok).replace(r"\ ", r"\s+") + r"(?![A-Za-z0-9_])",
                            0 if kind == "initials" else re.I)
            for base, uc_dir, mode in scopes:
                for d, _, fs in os.walk(base):
                    for fn in fs:
                        p = os.path.join(d, fn)
                        if mode and kind == "initials" and not p.startswith(uc_dir + os.sep):
                            continue
                        try:
                            text = open(p, encoding="utf-8").read()
                        except (UnicodeDecodeError, OSError):
                            continue
                        if rx.search(text):
                            where = os.path.relpath(p, ROOT) if base == OUT else "site:" + os.path.relpath(p, site)
                            found.append(f"withheld {kind} string #{i + 1} appears in {where}")
        if found:
            sys.exit("LEAK: a withheld identity reached published output:\n  " + "\n  ".join(found))
        return len(secrets)
    finally:
        import shutil
        shutil.rmtree(site, ignore_errors=True)


# ------------------------------------------------------------------ markdown
def md_uc(uc, xw, titles):
    def who(ids):
        return ", ".join(f"[{titles[i]}](roles.md#{i})" for i in ids or []) or None

    def ref(x):
        return f"[{titles[x['actor']]}](roles.md#{x['actor']})" if x else None
    L = [f"### {uc['id']} {uc['title']}", ""]
    if uc.get("description"):
        L += [uc["description"], ""]
    meta = [("Priority", uc.get("priority")), ("Primary actors", who(uc.get("primaryActors"))),
            ("Supporting actors", who(uc.get("supportingActors"))), ("Level", uc.get("level")),
            ("Complexity", uc.get("complexity")), ("Status", uc.get("status")), ("Implementation status", uc.get("implementationStatus")),
            ("Assigned to", ref(uc.get("assignedTo"))), ("Release", uc.get("release"))]
    L += ["| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in meta if v] + [""]
    if uc.get("preconditions"):
        L += [f"**Preconditions.** {uc['preconditions']}", ""]
    if uc.get("successGuarantee"):
        L += [f"**Success guarantee.** {uc['successGuarantee']}", ""]
    if uc.get("mainSuccessScenario"):
        L += ["**Main success scenario**", ""]
        for s in uc["mainSuccessScenario"]:
            L.append(f"{s['step']}. {s['text']}")
            L += [f"    - {o}" for o in s.get("options") or []]
        L.append("")
    if uc.get("extensions"):
        L += ["**Extensions**", ""]
        for e in uc["extensions"]:
            L.append(f"- **{e['id']}** {e['text']}")
            for s in e["steps"]:
                L.append(f"    {s['step']}. {s['text']}")
                L += [f"        - {o}" for o in s.get("options") or []]
        L.append("")
    if uc.get("referencedRequirements"):
        L += ["**Referenced requirements:** " + "; ".join(f"{r['id']} ({r['type']})" for r in uc["referencedRequirements"]), ""]
    if uc.get("notes"):
        L += ["**Notes**", ""] + [f"- {n['text']}" + (f" *({n['dateAdded']})*" if n.get("dateAdded") else "") for n in uc["notes"]] + [""]
    x = xw.get(uc["id"])
    if x and x["status"] == "matched":
        L += ["**iHRIS 4.3.3 forms** (derived by name matching): " + ", ".join(
            f"`{m['form']}`" + (f" ({m['class']})" if m.get("class") else "") + f" in {m['package']}" for m in x["matches"]), ""]
    elif x and x["status"] == "unmatched":
        L += ["**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).", ""]
    return L


def esc_all(o):
    """Every source string made safe for Markdown (the text is the source's, not markup)."""
    if isinstance(o, str):
        o = o.replace("\\", "\\\\").replace("&", "&amp;").replace("<", "&lt;")
        for c in "`*_":
            o = o.replace(c, "\\" + c)
        return o
    if isinstance(o, list):
        return [esc_all(x) for x in o]
    if isinstance(o, dict):
        return {k: esc_all(v) for k, v in o.items()}
    return o


def write_md(product, doc, head, xw, dangling, titles):
    doc, head, dangling, titles = esc_all(doc), esc_all(head), esc_all(dangling), esc_all(titles)
    L = ["---", f"title: {json.dumps(PRODUCTS[product] + ' use cases (2009)')}", f"source: uploads/ihris-use-cases/{doc['source']['file']}",
         "licence: owner permission, 2026-09-23 (see ihris-use-cases.json)", "---", "",
         f"# {PRODUCTS[product]}: use cases (2009)", "",
         f"*{head.get('generator', '')}, {head.get('generatedAt', '')}. From the iHRIS use-case model by IntraHealth International / the Capacity "
         "Project iHRIS team, published here with the owner's permission. Parsed by `src/tools/ingest_use_cases.py`; do not edit by hand.*", ""]
    root = doc["root"]
    if root.get("description"):
        L += [root["description"], ""]
    for n in root.get("notes") or []:
        L.append(f"- {n['text']}" + (f" *({n['dateAdded']})*" if n.get("dateAdded") else ""))
    L.append("")
    if root.get("relatedDocuments"):
        L += ["Related documents: " + ", ".join(root["relatedDocuments"]), ""]
    L += ["## Actors", ""]
    for a in doc["actors"]:
        L += [f"### {a['id']} {a['name']}", "", f"Role: [{titles[a['role']]}](roles.md#{a['role']}) (`{a['role']}`)", ""]
        if a.get("description"):
            L += [a["description"], ""]
        if a.get("goals"):
            L += ["**Goals**", ""] + [f"- {g}" for g in a["goals"]] + [""]
        if a.get("notes"):
            L += ["**Notes**", ""] + [f"- {n['text']}" for n in a["notes"]] + [""]
        if a.get("useCases"):
            L += ["**Use cases:** " + ", ".join(f"{u['id']} {u['title']}" for u in a["useCases"]), ""]
    for p in list(walk(root))[1:]:
        L += [f"## {p['number']} {p['name']}", ""]
        if p.get("description"):
            L += [p["description"], ""]
        if p.get("notes"):
            L += [f"- {n['text']}" + (f" *({n['dateAdded']})*" if n.get("dateAdded") else "") for n in p["notes"]] + [""]
        if p.get("relatedDocuments"):
            L += ["Related documents: " + ", ".join(p["relatedDocuments"]), ""]
        for uc in p["useCases"]:
            L += md_uc(uc, xw, titles)
        for r in p["requirements"]:
            L += [f"### {r['id']} {r['name']}", ""]
            if r.get("description"):
                L += [r["description"], ""]
            src = f"[{titles[r['source']['actor']]}](roles.md#{r['source']['actor']})" if r.get("source") else None
            meta = [("Priority", r.get("priority")), ("Type", r.get("type")), ("Status", r.get("status")), ("Source", src),
                    ("Release", r.get("release"))]
            if any(v for _, v in meta):
                L += ["| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in meta if v] + [""]
            if r.get("referencedBy"):
                L += ["Referenced by: " + ", ".join(r["referencedBy"]), ""]
    mine = [d for d in dangling if d["product"] == product]
    if mine:
        L += ["## Cited but not described", "", "The report cites these, but describes none of them:", ""]
        L += [f"- {d['id']}" + (f" *{d['title']}*" if d.get("title") else "") + " (cited by " + ", ".join(d["citedBy"]) + ")" for d in mine] + [""]
    with open(os.path.join(OUT, f"{product}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L).rstrip() + "\n")


# ------------------------------------------------------------------ main
def main():
    man = json.load(open(os.path.join(UP, "manifest.json")))
    os.makedirs(OUT, exist_ok=True)
    docs, heads, extras = {}, {}, {}
    for fe in man["files"]:
        p = os.path.join(UP, fe["file"])
        if not os.path.exists(p):
            sys.exit(f"{p}: missing. Upload it (see uploads/ihris-use-cases/manifest.json).")
        md5, sha = md5_sha(p)
        if (md5, sha) != (fe["md5"], fe["sha256"]):
            sys.exit(f"{p}: checksum does not match the manifest; refusing to derive from it")
        # a fixed UTF-8 locale, so the text (and textSha256) does not depend on who runs it
        text = subprocess.run(["antiword", "-w", "0", p], capture_output=True, text=True, check=True,
                              env={**os.environ, "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}).stdout
        doc, head, toc_actors, staff, stats = parse_report(text, fe["product"])
        head["subject"], doc["glossary"] = report_glossary(p, text, fe["product"])
        doc["source"] = {"file": fe["file"], "md5": md5, "sha256": sha, "extractedWith": "antiword -w 0",
                         "textSha256": hashlib.sha256(text.encode()).hexdigest(), "manifest": "uploads/ihris-use-cases/manifest.json"}
        docs[fe["product"]], heads[fe["product"]] = doc, head
        extras[fe["product"]] = (toc_actors, staff, stats)
    if sorted(docs) != sorted(PRODUCTS):
        sys.exit(f"the manifest holds {sorted(docs)}, not the four products {list(PRODUCTS)}")

    # Roles from the described actors; use-case actors resolved to them; withheld people to opaque actors.
    roles = build_roles(docs)
    n_actor_refs = resolve_actors(docs)
    staff_actors, secrets = assign_staff({p: extras[p][1] for p in PRODUCTS})
    labels = {r["id"]: r["title"] for r in roles} | {a["id"]: a["title"] for a in staff_actors}

    described = {uc["id"] for d in docs.values() for p in walk(d["root"]) for uc in p["useCases"]}
    described |= {r["id"] for d in docs.values() for p in walk(d["root"]) for r in p["requirements"]}
    actors = {a["id"] for d in docs.values() for a in d["actors"]}
    dangling = {}
    for product, d in docs.items():
        titles = {u["id"]: u["title"] for a in d["actors"] for u in a["useCases"]}
        for a in d["actors"]:
            for u in a["useCases"]:
                if u["id"] not in described:
                    dangling.setdefault(u["id"], {"id": u["id"], "kind": "use-case", "product": product, "title": u["title"], "citedBy": set()})["citedBy"].add(a["id"])
        for p in walk(d["root"]):
            for x in p["useCases"] + p["requirements"]:
                for r in sorted(refs_in({k: v for k, v in x.items() if k != "id"})):
                    if r not in described:
                        e = dangling.setdefault(r, {"id": r, "kind": "use-case" if r.startswith("UC-") else "requirement", "product": product,
                                                    "title": titles.get(r), "citedBy": set()})
                        e["citedBy"].add(x["id"])
        for aid, name in extras[product][0].items():
            if aid not in actors:
                dangling.setdefault(aid, {"id": aid, "kind": "actor", "product": product, "title": name, "citedBy": set()})["citedBy"].add("table of contents")
    dangling = [{**v, "citedBy": sorted(v["citedBy"])} for _, v in sorted(dangling.items(), key=lambda kv: (kv[1]["product"], kv[0]))]

    xw = crosswalk(docs)
    xw_by = {e["useCase"]: e for e in xw["entries"]}
    for product, d in docs.items():
        toc_actors, staff, stats = extras[product]
        withheld = {}
        for k, _, _ in staff:
            withheld[k] = withheld.get(k, 0) + 1
        ucs = [uc for p in walk(d["root"]) for uc in p["useCases"]]
        reqs = [r for p in walk(d["root"]) for r in p["requirements"]]
        rec = {
            "$schema": "ihris-use-cases/v1",
            "product": product,
            "title": PRODUCTS[product] + " use cases",
            "report": {"title": "Use Case Model - Complete Report", "generator": heads[product].get("generator"),
                       "generatedAt": heads[product].get("generatedAt"), "author": "sturlington", "subject": heads[product]["subject"]},
            "source": d["source"],
            "attribution": "iHRIS use-case model, IntraHealth International / the Capacity Project iHRIS team (2009). Published with the owner's permission.",
            "counts": {"useCases": len(ucs), "actors": len(d["actors"]), "requirements": len(reqs),
                       "packages": len(list(walk(d["root"]))), "steps": sum(len(u.get("mainSuccessScenario") or []) for u in ucs),
                       "extensions": sum(len(u.get("extensions") or []) for u in ucs)},
            "withheld": [{"field": k, "why": WHY[k], "count": withheld[k]} for k in sorted(withheld)],
            "actors": d["actors"],
            "root": d["root"],
            "dangling": [x for x in dangling if x["product"] == product],
            "glossary": d["glossary"],
        }
        with open(os.path.join(OUT, f"{product}.json"), "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1, ensure_ascii=False)
            f.write("\n")
        write_md(product, d, heads[product], xw_by, dangling, labels)
        print(f"{product}: {rec['counts']}, withheld {rec['withheld']}, {stats}")
    write_scenarios(roles, staff_actors)
    write_roles_md(roles, staff_actors, docs)
    print(f"roles: {len(roles)}; use-case actor references resolved: {n_actor_refs}; opaque actors: {len(staff_actors)}, "
          f"referenced {sum(len(extras[p][1]) for p in PRODUCTS)} times")
    with open(os.path.join(OUT, "crosswalk.json"), "w", encoding="utf-8") as f:
        json.dump(xw, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(OUT, "manifest.jsonld"), "w", encoding="utf-8") as f:
        json.dump({"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld", "@id": f"{ENTRY}/manifest",
                   "@type": ["folio:SourceDocument"], "title": "iHRIS use-case model (Common, Manage, Qualify, Plan), 2009",
                   "contains": [f"{ENTRY}/{p}" for p in PRODUCTS] + [f"{ENTRY}/roles"], "provenance": "ingested",
                   "meta": {"source_files": [fe["file"] for fe in man["files"]], "document_class": "use-case-model",
                            "licence": "owner permission, 2026-09-23",
                            "disposition": ("ingested: parsed to ihris-use-cases/v1 and Markdown, with the actors declared as roles "
                                            "(scenarios/roles.json) and the people named as opaque actors (scenarios/actors/); "
                                            "the .doc files are held in uploads/ (git-ignored)")}},
                  f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"crosswalk: {xw['counts']}; dangling: {[d['id'] for d in dangling]}")
    print(f"leak check: {leak_check(secrets)} withheld strings, none found in {ENTRY}/ or the built site")


if __name__ == "__main__":
    main()
