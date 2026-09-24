#!/usr/bin/env python3
"""Build the ihris glossary: SKOS concept schemes (folio-assistant's `folio-glossary/v1`).

Owner, 2026-09-23: *"everything extracted to glosasay / skos? accesible in ihris
page/search?"*, *"it should be part of general pracice w/ glossary/ page"* and *"can
glossary be refefences to external skos schema?"*. So: reference first, define second.
The schema, the three states and the SKOS shape are folio-assistant's
(`folio-assistant-core/schemas/glossary.ts`, PR #1218, issue #1217); nothing here
re-decides them.

Deterministic, from committed files only (so CI can run `--check`). One scheme per source:

  (a) toolkit-technical-terms   every stage's "Technical terms" (library/ihris-toolkit/stages/*.json),
                                term and definition verbatim, `authored`, while the toolkit's
                                declaration records a licence (the owner's permission, bean
                                ihris-kngr). Without one, the terms are `candidate`s with no
                                definition, as the site shows the toolkit's structure only.
  (b) use-cases-2009            the glossaries of the four 2009 use-case reports, as
                                src/tools/ingest_use_cases.py recorded them (`glossary` in
                                library/ihris-use-cases/<product>.json). The reports' document
                                summary names a glossary, and no report holds one, so this scheme
                                has no terms and says so. None is invented.
  (c) code-list-<form>          one scheme per iHRIS 4.3.3 code list with DEFAULT records
                                (src/*/data-lists/4.3.3/<form>.json, merged across packages as I2CE
                                merges them: the first record with an id wins). notation = the
                                record id, prefLabel = its `name`. `candidate` unless the record
                                carries a definition (a non-empty `description`, verbatim:
                                ISCO-88). SAMPLE records illustrate one deployment, are never a
                                standard code set (as in the DAK), and are left out.

External matches are never invented. A term gets a SKOS match only from a ConceptMap the
repository already verified (src/ihris-data-dictionary/terminology, built by build_dak.py),
and only for an equivalence that implies one:

  equal, equivalent   -> exactMatch      wider, subsumes   -> broadMatch
  narrower, specializes -> narrowMatch   anything else (inexact, relatedto, unmatched) -> none

and only when the map's target system is an external scheme this folio references
(`remoteGraphs` with graphKinds ["glossary"] in ihris.json). The IRI follows the
publisher's own pattern: the EU Publications Office authority tables
(`.../authority/country/` + ISO 3166-1 alpha-3, from pycountry, the same data the map was
verified with; `.../authority/currency/` + ISO 4217) and ESCO for ISCO-08
(`http://data.europa.eu/esco/isco/C` + code). The IRIs are BUILT BY PATTERN: the building
session cannot reach those hosts, so none was dereferenced.

One second basis, and only the one the owner accepted: VALUESET IDENTITY. No ConceptMap
targets ISCO-08; build_dak.py instead binds iHRIS's `isco_08_*` lists, as a ValueSet, to the
ILO's ISCO-08 system itself, so an iHRIS record id IS the ISCO-08 code. The owner ruled on
2026-09-24 (ihris PR #19, "Accept ValueSet identity") that this is enough for exactMatch. So a
code-list term gets exactMatch to ESCO for each concept of a ValueSet that is this
repository's ValueSet for that code list (`<CANONICAL>/ValueSet/<form>`) and whose include
system is in VALUESET_IDENTITY. No other system is accepted this way until the owner says so,
and the scheme's description names the basis.

IRIs are in the namespace of the SUB-INSTANCE THAT OWNS THE SOURCE (owner, 2026-09-24: "make sure
all glossary terms properly localed to ihris so [no] collision w/ other subgraphs. general rule/skill";
folio-assistant skill `glossary-terms`, Conventions): `<ns>glossary/<scheme>/<term>`, with
ns = `<publication root><sub-instance>/ns#`, core's `instanceNs` rule applied to this repository's own
publication root, https://litlfred.github.io/ihris/. Never the root instance's namespace just because
glossary/ is declared at the root. The owner of a scheme (`scheme_owner`):
  toolkit technical terms   ihris-toolkit     (library/ihris-toolkit)
  use-case glossaries       ihris-use-cases   (library/ihris-use-cases)
  a code list               the package whose data model DECLARES the form (a class's `forms`), even
                            when other packages extend the list (e.g. `role`: i2ce defines it; common,
                            manage and qualify add records, and each term's `source` still names its
                            contributing package)
The owner must be one of ihris.json's instances, so two schemes never share an IRI across sub-instances,
and no ihris IRI can fall in another folio's namespace (a different publication root).

SKOS JSON-LD: `to_skos()` mirrors core's `toSkos()` in Python rather than calling it through
bun. The Pages workflow (.github/workflows/pages.yml) builds the site with Python alone, and
the site must carry the SKOS files; requiring bun and a folio-assistant checkout there would
make publishing depend on the platform's checkout. The mirror is held to the original:
src/tools/validate-folio.ts runs core's own `toSkos()` on every scheme and fails unless it is
identical, key order included, to what the site published (.build/site).

  python3 src/tools/build_glossary.py            # write glossary/*.glossary.json
  python3 src/tools/build_glossary.py --check    # fail if the committed files are stale
"""
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_dak  # noqa: E402  (CANONICAL, RELEASE, ISO_SYSTEMS, ILO_ISCO08: one answer, not two)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RELEASE = build_dak.RELEASE
PUBLICATION_ROOT = "https://litlfred.github.io/ihris/"
INSTANCE = "ihris"
NS = f"{PUBLICATION_ROOT}{INSTANCE}/ns#"  # the root instance's own namespace: owns no glossary scheme today
SCHEMA = "folio-glossary/v1"
SKOS_NS = "http://www.w3.org/2004/02/skos/core#"
DCTERMS_NS = "http://purl.org/dc/terms/"
LOCAL_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
IRI = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)
TOOLKIT = "library/ihris-toolkit"
USE_CASES = "library/ihris-use-cases"
PRODUCTS = ["common", "manage", "qualify", "plan"]
PACKAGES = ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify"]

EU_AUTHORITY = "http://publications.europa.eu/resource/authority/"
ESCO_ISCO = "http://data.europa.eu/esco/isco/C"
EQUIVALENCE = {"equal": "exactMatch", "equivalent": "exactMatch", "wider": "broadMatch", "subsumes": "broadMatch",
               "narrower": "narrowMatch", "specializes": "narrowMatch"}
MATCHES = ("exactMatch", "closeMatch", "broadMatch", "narrowMatch")
# Systems whose ValueSet binding the owner accepted as identity (exactMatch). Owner, 2026-09-24.
VALUESET_IDENTITY = {build_dak.ILO_ISCO08: "the owner's ruling of 2026-09-24 (ihris PR #19)"}


def J(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


def slug(s):
    return re.sub(r"[^a-z0-9._-]+", "-", s.lower()).strip("-._")


# ------------------------------------------------------------------ declaration
def glossary_dir():
    """The directory ihris.json declares with graphKinds ["glossary"], repository-relative."""
    dirs = [d["path"].rstrip("/") for d in J("ihris.json").get("directories") or [] if "glossary" in (d.get("graphKinds") or [])]
    if len(dirs) != 1:
        sys.exit(f"ihris.json must declare exactly one glossary directory, not {len(dirs)}")
    return dirs[0]


def remote_glossaries():
    """{id: remoteGraph} for every external SKOS scheme ihris.json references."""
    return {g["id"]: g for g in J("ihris.json").get("remoteGraphs") or [] if "glossary" in g["graphKinds"]}


def _alpha3(alpha2):
    import pycountry  # the ISO data the country ConceptMap was verified with (pycountry==24.6.1)
    c = pycountry.countries.get(alpha_2=alpha2)
    if c is None:
        raise SystemExit(f"ISO 3166-1 alpha-2 {alpha2} is equal in the ConceptMap but unknown to pycountry: rebuild the DAK")
    return c.alpha_3


# External target system -> (remoteGraphs id, the publisher's IRI pattern).
EXTERNAL = {
    build_dak.ISO_SYSTEMS["country"]["system"]: ("eu-authority-country", lambda code: f"{EU_AUTHORITY}country/{_alpha3(code)}"),
    build_dak.ISO_SYSTEMS["currency"]["system"]: ("eu-authority-currency", lambda code: f"{EU_AUTHORITY}currency/{code}"),
    build_dak.ILO_ISCO08: ("esco-isco-08", lambda code: f"{ESCO_ISCO}{code}"),
}


# ------------------------------------------------------------------ (a) toolkit
def toolkit_term_id(term):
    return slug(term)


def toolkit_scheme():
    decl = J(f"{TOOLKIT}/ihris-toolkit.json")
    lic = decl.get("licence") or {}
    full = lic.get("status") in ("stated", "permission")
    terms, seen = [], set()
    for f in sorted(glob.glob(os.path.join(ROOT, TOOLKIT, "stages", "*.json"))):
        rel = os.path.relpath(f, ROOT)
        st = J(rel)
        for i, t in enumerate(st.get("technicalTerms") or []):
            tid = toolkit_term_id(t["term"])
            if tid in seen:
                sys.exit(f"{rel}: technical term {t['term']!r} has the id {tid} of an earlier one; decide how they differ")
            seen.add(tid)
            term = {"id": tid, "prefLabel": t["term"]}
            if full and t.get("definition"):
                term["definition"] = t["definition"]
            term["scopeNote"] = f"Toolkit stage {st['ordinal']}: {st['name']}."
            term["source"] = f"{rel}#/technicalTerms/{i}"
            term["status"] = "authored" if "definition" in term else "candidate"
            terms.append(term)
    g = {"$schema": SCHEMA, "id": "toolkit-technical-terms", "title": "iHRIS Implementation Toolkit: technical terms",
         "description": ("The technical terms each stage of the iHRIS Implementation Toolkit defines, term and definition "
                         "verbatim from the stage pages captured in uploads/toolkit/ (ingested to library/ihris-toolkit/stages/)."
                         + ("" if full else " No licence is recorded for the toolkit, so only the terms are listed.")),
         "source": f"{lic.get('attribution') or 'The iHRIS Implementation Toolkit.'} {decl['source']['web']}"}
    if full:
        how = f"granted {lic['grantedOn']} by {lic['grantedBy']}" if lic["status"] == "permission" else lic.get("id", "")
        g["license"] = (f"LicenseRef-owner-permission: {how}; {TOOLKIT}/ihris-toolkit.json#/licence"
                        if lic["status"] == "permission" else lic["id"])
    g["terms"] = terms
    return g


# ------------------------------------------------------------------ (b) use cases
def use_case_scheme():
    decl = J(f"{USE_CASES}/ihris-use-cases.json")
    lic = decl.get("licence") or {}
    full = lic.get("status") in ("stated", "permission")
    terms, notes, seen = [], [], set()
    for p in PRODUCTS:
        rel = f"{USE_CASES}/{p}.json"
        d = J(rel)
        gl = d.get("glossary")
        if gl is None:
            sys.exit(f"{rel}: no `glossary` record; rerun src/tools/ingest_use_cases.py")
        notes.append(f"{d['title']} ({d['report']['generatedAt'].split()[0]}): "
                     + ("glossary found" if gl["found"] else "no glossary section") + ".")
        for i, t in enumerate(gl["terms"]):
            tid = slug(t["term"])
            if tid in seen:
                sys.exit(f"{rel}: glossary term {t['term']!r} has the id {tid} of an earlier one; decide how they differ")
            seen.add(tid)
            term = {"id": tid, "prefLabel": t["term"]}
            if full:
                term["definition"] = t["definition"]
            term["scopeNote"] = f"{d['title']} (2009)."
            term["source"] = f"{rel}#/glossary/terms/{i}"
            term["status"] = "authored" if full else "candidate"
            terms.append(term)
    subjects = sorted({J(f"{USE_CASES}/{p}.json")["report"].get("subject") for p in PRODUCTS
                       if J(f"{USE_CASES}/{p}.json")["glossary"]["claimedBy"]})
    desc = "The glossary terms of the four 2009 iHRIS use-case reports (Common, Manage, Qualify, Plan), verbatim. "
    if not terms:
        desc += (("The reports' document summary names a glossary (Subject: " + "; ".join(f"\u201c{s}\u201d" for s in subjects)
                  + "), but " if subjects else "")
                 + "no report holds a glossary section, so this scheme has no terms. None is invented. ")
    desc += " ".join(notes)
    g = {"$schema": SCHEMA, "id": "use-cases-2009", "title": "iHRIS use-case model (2009): glossary", "description": desc,
         "hasVersion": "2009", "source": f"{lic.get('attribution') or 'The iHRIS use-case model (2009).'} uploads/ihris-use-cases/manifest.json"}
    if full:
        g["license"] = f"LicenseRef-owner-permission: granted {lic['grantedOn']} by {lic['grantedBy']}; {USE_CASES}/ihris-use-cases.json#/licence"
    g["terms"] = terms
    return g


# ------------------------------------------------------------------ (c) code lists
def code_list_records():
    """form -> [(rel, index, record)] of DEFAULT records, first id wins, in package order (as I2CE merges them)."""
    out = collections.OrderedDict()
    seen = collections.defaultdict(set)
    for pkg in PACKAGES:
        for f in sorted(glob.glob(os.path.join(ROOT, "src", pkg, "data-lists", RELEASE, "*.json"))):
            rel = os.path.relpath(f, ROOT)
            d = J(rel)
            for i, r in enumerate(d["records"]):
                if r.get("provenance") != "default" or r["id"] in seen[d["form"]]:
                    continue
                seen[d["form"]].add(r["id"])
                out.setdefault(d["form"], []).append((rel, i, r))
    return collections.OrderedDict(sorted(out.items()))


def verified_matches():
    """{form: {code: {match: [iri]}}} from the ConceptMaps build_dak.py verified, for external targets only."""
    out = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    used = {}
    remote = remote_glossaries()
    prefix = f"{build_dak.CANONICAL}/CodeSystem/"
    for f in sorted(glob.glob(os.path.join(ROOT, "src/ihris-data-dictionary/terminology/ConceptMap-*.json"))):
        cm = J(os.path.relpath(f, ROOT))
        for grp in cm.get("group") or []:
            if grp.get("target") not in EXTERNAL or not grp.get("source", "").startswith(prefix):
                continue
            rid, iri = EXTERNAL[grp["target"]]
            if rid not in remote:
                sys.exit(f"ConceptMap {cm['id']} targets {grp['target']}, but ihris.json references no remote glossary {rid}")
            form = grp["source"][len(prefix):]
            used.setdefault(form, set()).add(cm["id"])
            for el in grp.get("element") or []:
                for t in el.get("target") or []:
                    m = EQUIVALENCE.get(t.get("equivalence"))
                    if m and t.get("code"):
                        out[form][el["code"]][m].append(iri(t["code"]))
    return out, used


def valueset_identity_matches():
    """{form: {code: [iri]}} and {form: ValueSet id}: exactMatch from a code list's own ValueSet,
    bound to a system in VALUESET_IDENTITY (the owner-accepted basis; see the module docstring)."""
    out, used = collections.defaultdict(dict), {}
    remote = remote_glossaries()
    prefix = f"{build_dak.CANONICAL}/ValueSet/"
    for f in sorted(glob.glob(os.path.join(ROOT, "src/ihris-data-dictionary/terminology/ValueSet-*.json"))):
        vs = J(os.path.relpath(f, ROOT))
        if not vs.get("url", "").startswith(prefix):
            continue
        form = vs["url"][len(prefix):]
        for inc in (vs.get("compose") or {}).get("include") or []:
            if inc.get("system") not in VALUESET_IDENTITY:
                continue
            rid, iri = EXTERNAL[inc["system"]]
            if rid not in remote:
                sys.exit(f"ValueSet {vs['id']} binds {inc['system']}, but ihris.json references no remote glossary {rid}")
            used[form] = vs["id"]
            for c in inc.get("concept") or []:
                out[form][c["code"]] = [iri(c["code"])]
    return out, used


def package_licence():
    lic = {tuple(J(f"src/catalogue/records/project--{p}.json")["project"].get("licences") or []) for p in PACKAGES}
    if lic != {("GNU GPL v3",)}:
        sys.exit(f"the core packages' licences are {sorted(lic)}; decide what the code-list schemes are published under")
    return "https://www.gnu.org/licenses/gpl-3.0.html"


def code_list_schemes():
    recs = code_list_records()
    matches, used = verified_matches()
    identity, vs_used = valueset_identity_matches()
    licence = package_licence()
    remote = remote_glossaries()
    sample = collections.Counter()
    for f in glob.glob(os.path.join(ROOT, "src", "*", "data-lists", RELEASE, "*.json")):
        d = J(os.path.relpath(f, ROOT))
        sample[d["form"]] += sum(1 for r in d["records"] if r.get("provenance") == "sample")
    out = []
    for form, rows in recs.items():
        terms, ids = [], set()
        for rel, i, r in rows:
            tid = slug(r["id"])
            if not LOCAL_ID.match(tid) or tid in ids:
                sys.exit(f"{rel}: record {r['id']!r} gives term id {tid!r}, which is empty or not unique in {form}")
            ids.add(tid)
            name = r["fields"].get("name")
            term = {"id": tid, "prefLabel": name if isinstance(name, str) and name.strip() else r["id"]}
            desc = r["fields"].get("description")
            if isinstance(desc, str) and desc.strip():
                term["definition"] = desc
            term["notation"] = r["id"]
            if term["prefLabel"] == r["id"] and not (isinstance(name, str) and name.strip()):
                term["scopeNote"] = "The record has no `name`, so its code stands as its label."
            for m in MATCHES:
                got = set(matches.get(form, {}).get(r["id"], {}).get(m) or [])
                if m == "exactMatch":
                    got |= set(identity.get(form, {}).get(r["id"]) or [])
                if got:
                    term[m] = sorted(got)
            term["source"] = f"{rel}#/records/{i}"
            term["status"] = "authored" if "definition" in term else "candidate"
            terms.append(term)
        mods = sorted({r["definedIn"] for _, _, r in rows})
        pk = sorted({rel.split("/")[1] for rel, _, _ in rows})
        n_auth = sum(1 for t in terms if t["status"] == "authored")
        desc = (f"The `{form}` code list as iHRIS {RELEASE} ships it by default: {len(terms)} codes from "
                f"{', '.join(mods)}. Each term's notation is the iHRIS record id and its label the record's `name`. ")
        desc += (f"Definitions are the records' own `description`, verbatim ({n_auth} of {len(terms)})." if n_auth else
                 "The source gives no definitions, so every term is a candidate.")
        if sample[form]:
            desc += f" The {sample[form]} sample record(s) illustrate one example deployment and are left out."
        if form in used:
            n = sum(1 for t in terms if any(t.get(m) for m in MATCHES))
            titles = sorted({remote[EXTERNAL[g["target"]][0]]["title"] for f in used[form]
                             for g in J(f"src/ihris-data-dictionary/terminology/ConceptMap-{f}.json")["group"] if g["target"] in EXTERNAL})
            desc += (f" {n} term(s) link to {', '.join(titles)}, from the verified ConceptMap {', '.join(sorted(used[form]))} "
                     "(equal only); the IRIs follow the publisher's pattern and were not dereferenced.")
        if form in vs_used:
            n = sum(1 for t in terms if identity[form].get(t["notation"]))
            system = next(i["system"] for i in J(f"src/ihris-data-dictionary/terminology/ValueSet-{form}.json")["compose"]["include"]
                          if i.get("system") in VALUESET_IDENTITY)
            desc += (f" {n} term(s) have exactMatch to {remote[EXTERNAL[system][0]]['title']} by ValueSet identity: "
                     f"the ValueSet {vs_used[form]} binds this list to {system}, so each code is that system's code. "
                     f"No ConceptMap records it; the basis was accepted by {VALUESET_IDENTITY[system]}. "
                     "The IRIs follow the publisher's pattern and were not dereferenced.")
        out.append({"$schema": SCHEMA, "id": f"code-list-{slug(form)}", "title": f"iHRIS {RELEASE} code list: {form}",
                    "description": desc, "hasVersion": RELEASE,
                    "source": ", ".join(f"src/{p}/data-lists/{RELEASE}/{form}.json" for p in pk) + f" (iHRIS {RELEASE}, MD5-verified release)",
                    "license": licence, "terms": terms})
    return out


# ------------------------------------------------------------------ all
def schemes():
    return [toolkit_scheme(), use_case_scheme()] + code_list_schemes()


def dump(g):
    return json.dumps(g, indent=1, ensure_ascii=False) + "\n"


def outputs():
    d = glossary_dir()
    return collections.OrderedDict((f"{d}/{g['id']}.glossary.json", dump(g)) for g in schemes())


def instance_ns(inst):
    """core's `instanceNs`, under this repository's publication root. `inst` must be ihris or one of its instances."""
    if inst != INSTANCE and inst not in {i["name"] for i in J("ihris.json").get("instances") or []}:
        sys.exit(f"{inst} is not an instance ihris.json declares, so it has no namespace")
    return f"{PUBLICATION_ROOT}{inst}/ns#"


# Dependency order: a product package extends ihris-common, which extends i2ce. A form declared again by a
# later package is the earlier package's form extended, so the EARLIEST declarer defines it.
DEPENDENCY_ORDER = ["i2ce", "ihris-common", ("ihris-manage", "ihris-qualify", "ihris-plan")]


def _rank(pkg):
    for i, level in enumerate(DEPENDENCY_ORDER):
        if pkg == level or (isinstance(level, tuple) and pkg in level):
            return i
    return len(DEPENDENCY_ORDER)


def form_definers():
    """{form: {packages whose data model declares it in a class's `forms`}}."""
    out = collections.defaultdict(set)
    for f in sorted(glob.glob(os.path.join(ROOT, "src", "*", "data-model", RELEASE, "*.json"))):
        pkg = os.path.relpath(f, ROOT).split(os.sep)[1]
        for form in J(os.path.relpath(f, ROOT)).get("forms") or []:
            out[form].add(pkg)
    return out


def definer(form, definers):
    """The package that defines a form: the earliest declarer in dependency order; two at one level is an error."""
    pkgs = definers.get(form) or set()
    if not pkgs:
        return None
    first = min(_rank(p) for p in pkgs)
    at = sorted(p for p in pkgs if _rank(p) == first)
    if len(at) != 1:
        sys.exit(f"form {form} is declared by {at}, none of which extends another: its code list has no single owner")
    return at[0]


def scheme_owner(g, definers=None):
    """The instance that owns a scheme's source (see the module docstring). Derived from the scheme's `source`."""
    tokens = [w.strip(",.;()") for w in (g.get("source") or "").split()]
    tokens += [(t.get("source") or "").split("#")[0] for t in g.get("terms") or []]
    paths = [w for w in tokens if w.split("/")[0] in ("src", "library", "uploads") and len(w.split("/")) > 2]
    owners = sorted({w.split("/")[1] for w in paths})
    if g["id"].startswith("code-list-"):
        form = os.path.basename(paths[0])[:-5]
        definers = definers if definers is not None else form_definers()
        d = definer(form, definers)
        if d:
            return d
    if len(owners) != 1:
        sys.exit(f"scheme {g['id']}: its sources {owners} name no single owning instance")
    return owners[0]


def scheme_ns(g, definers=None):
    return instance_ns(scheme_owner(g, definers))


def load():
    """The committed schemes, in file order: [(rel, doc)]."""
    d = glossary_dir()
    return [(os.path.relpath(f, ROOT), J(os.path.relpath(f, ROOT))) for f in sorted(glob.glob(os.path.join(ROOT, d, "*.glossary.json")))]


# ------------------------------------------------------------------ SKOS (mirrors core's toSkos)
def scheme_iri(ns, g):
    return f"{ns}glossary/{g['id']}"


def term_iri(ns, g, tid):
    return f"{scheme_iri(ns, g)}/{tid}"


def _lang_values(t):
    return [{"@value": t}] if isinstance(t, str) else [{"@value": v, "@language": k} for k, v in t.items()]


def to_skos(g, ns=None):
    """folio-assistant-core/schemas/glossary.ts `toSkos`, key for key and in the same order.
    `ns` defaults to the namespace of the instance that owns the scheme's source."""
    ns = ns or scheme_ns(g)
    scheme = scheme_iri(ns, g)

    def ref(r):
        return {"@id": r if IRI.match(r) else term_iri(ns, g, r)}
    head = {"@id": scheme, "@type": "skos:ConceptScheme", "skos:prefLabel": g["title"]}
    for k, key in (("description", "skos:definition"), ("hasVersion", "dcterms:hasVersion"), ("modified", "dcterms:modified"),
                   ("source", "dcterms:source"), ("license", "dcterms:license")):
        if g.get(k):
            head[key] = g[k]
    graph = [head]
    for t in g.get("terms") or []:
        node = {"@id": term_iri(ns, g, t["id"]), "@type": "skos:Concept", "skos:inScheme": {"@id": scheme},
                "skos:prefLabel": _lang_values(t["prefLabel"])}
        if t.get("altLabel"):
            node["skos:altLabel"] = t["altLabel"]
        if t.get("definition"):
            node["skos:definition"] = _lang_values(t["definition"])
        if t.get("notation"):
            node["skos:notation"] = t["notation"]
        if t.get("scopeNote"):
            node["skos:scopeNote"] = t["scopeNote"]
        if t.get("broader"):
            node["skos:broader"] = [ref(x) for x in t["broader"]]
        if t.get("related"):
            node["skos:related"] = [ref(x) for x in t["related"]]
        for m in MATCHES:
            if t.get(m):
                node[f"skos:{m}"] = [{"@id": x} for x in t[m]]
        if t.get("source"):
            node["dcterms:source"] = t["source"]
        if t["status"] != "authored":
            node["skos:note"] = f"{t['status']}: {t['reason']}" if t.get("reason") else t["status"]
        graph.append(node)
    if g.get("members"):
        graph.append({"@id": f"{scheme}#members", "@type": "skos:Collection", "skos:prefLabel": f"{g['title']}: external terms",
                      "skos:member": [{"@id": m} for m in g["members"]]})
    return {"@context": {"skos": SKOS_NS, "dcterms": DCTERMS_NS}, "@graph": graph}


def skos_asset(g):
    """Where the site publishes a scheme's SKOS JSON-LD (core's layout: assets/glossary/<owning instance>--<scheme>)."""
    return f"assets/glossary/{scheme_owner(g)}--{g['id']}.skos.jsonld"


def skos_text(g):
    return json.dumps(to_skos(g), indent=2, ensure_ascii=False) + "\n"


# ------------------------------------------------------------------ main
def main():
    check = "--check" in sys.argv
    files = outputs()
    d = glossary_dir()
    have = {os.path.relpath(f, ROOT) for f in glob.glob(os.path.join(ROOT, d, "*.glossary.json"))}
    stale = [p for p, s in files.items() if not os.path.exists(os.path.join(ROOT, p)) or open(os.path.join(ROOT, p), encoding="utf-8").read() != s]
    orphans = sorted(have - set(files))
    if check:
        for p in stale:
            print(f"stale: {p}")
        for p in orphans:
            print(f"orphan: {p}")
        if stale or orphans:
            print("Run `python3 src/tools/build_glossary.py` and commit the result.")
            sys.exit(1)
        print(f"glossary current: {len(files)} schemes")
        return
    os.makedirs(os.path.join(ROOT, d), exist_ok=True)
    for p in orphans:
        os.remove(os.path.join(ROOT, p))
    for p, s in files.items():
        with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
            f.write(s)
    by = collections.Counter()
    for g in schemes():
        for t in g["terms"]:
            by[t["status"]] += 1
    print(f"glossary: {len(files)} schemes, {sum(by.values())} terms {dict(by)}; {len(stale)} written, {len(orphans)} removed")


if __name__ == "__main__":
    main()
