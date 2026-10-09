#!/usr/bin/env python3
"""Lay out a knowledge-graph subgraph as a Graphviz diagram, the way the i2ce Form Documentor did.

  python3 src/tools/kg_layout.py --forms ihris-manage [--out FILE]   # the iHRIS Manage forms, as DOT
  python3 src/tools/kg_layout.py --forms ihris-qualify [--out FILE]

The convention is I2CE_Page_FormDocumentor::dot() (i2ce 4.3.3, i2ce/modules/Forms/modules/FormDocumentor), the
"giant diagram" of an iHRIS site's forms (owner, 2026-10-09: "this is skill to generalize for layout of KG subgraphs
visualizer"). It is restated here over a PROJECTION, so any subgraph can be drawn with it, not only forms:

  {"title": str, "graphOptions": ["key:value", ...], "colors": ["substring:colour", ...],
   "nodes": [{"id": str, "header": str, "rows": [[text, subtext-or-null], ...]}],
   "edges": [{"from": id, "to": id-or-[ids], "label": str-or-null, "kind": "ref" | "child"}]}

Rules, each the Form Documentor's own:
- a node is an Mrecord whose label is a table: the header boxed on white, then one row per property, with its
  annotation (a field's label, required `*`, unique `!`) in grey30 beneath;
- a node is filled with the colour of the FIRST `substring:colour` whose substring occurs in its id, else ivory3;
- a `ref` edge with one target is labelled with its property unless the property is named after the target; with
  several targets it fans out through a point (a "splitter"), labelled once, with an arrowless first leg;
- a `child` edge is firebrick;
- the graph carries the declared options, `ratio = auto`, and a label (the title) when none is declared;
- the layout is `unflatten -f -l 2 -c 2 | dot` (run by the viewer, src/site/kg-graph.js, with Graphviz in WebAssembly).

Adapters build projections: `forms_projection` (an iHRIS product's forms from the committed data model and module
records). Others (a layer's KG declaration schema) take the same renderer.
"""
import collections
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RELEASE = "4.3.3"
DEFAULT_FILL = "ivory3"


def q(s):
    """A DOT double-quoted id."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def h(s):
    """Text inside an HTML-like label."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def to_dot(p):
    colors = [c.split(":", 1) for c in p.get("colors") or [] if ":" in c]
    nodes, paths, splitters = [], [], []
    for n in sorted(p["nodes"], key=lambda n: n["id"]):
        # A node may carry its own `fill` (an adapter colouring by a theme); otherwise the Form Documentor's rule.
        fill = n.get("fill") or next((col for sub, col in colors if sub in n["id"]), DEFAULT_FILL)
        fill = q(fill) if fill.startswith("#") else fill
        rows = "".join(f"<tr><td ALIGN='LEFT'>{h(t)}</td></tr>" + (f"<tr><td ALIGN='LEFT'>  <font color='grey30'>{h(s)}</font></td></tr>" if s else "")
                       for t, s in n["rows"])
        label = f"<table border='0' cellborder='0'><tr><td BGCOLOR='white' BORDER='1'>{h(n['header'])} </td></tr>{rows}</table>"
        nodes.append(f"{q(n['id'])} [style=filled fillcolor = {fill}   label =<{label}> shape = \"Mrecord\"   ];")
    ids = {n["id"] for n in p["nodes"]}
    for e in p["edges"]:
        targets = [t for t in (e["to"] if isinstance(e["to"], list) else [e["to"]]) if t in ids]
        if e["from"] not in ids or not targets:
            continue
        if e["kind"] == "child":
            paths += [f"{q(e['from'])} -> {q(t)} [color=firebrick];" for t in targets]
        elif len(targets) > 1:
            sp = f"splitter+{e['from']}+{e.get('label') or ''}"
            splitters.append(f"{q(sp)} [shape=point size = 1 label = \"\"  ] ;")
            paths.append(f"{q(e['from'])} -> {q(sp)} [arrowhead = none label = {q(e.get('label') or '')} ];")
            paths += [f"{q(sp)} -> {q(t)}  ;" for t in sorted(targets)]
        else:
            t = targets[0]
            lab = e.get("label")
            paths.append(f"{q(e['from'])} -> {q(t)} [ label = {q(lab)} ]  ;" if lab and lab != t else f"{q(e['from'])} -> {q(t)}  ;")
    opts = [o.split(":", 1) for o in p.get("graphOptions") or [] if ":" in o]
    if not any(k == "label" for k, _ in opts):
        opts.append(("label", q(p["title"])))
    graph = "graph [" + "".join(f"\n\t\t{k}={v}" for k, v in opts) + "\n\t];\n\tratio = auto;\n"
    return "digraph g {\n\t" + graph + "\t" + "\n\t".join(splitters + nodes) + "\n\t" + "\n\t".join(paths) + "\n}\n"


# ---------------------------------------------------------------- adapter: an iHRIS product's forms
PRODUCTS = {
    "ihris-manage": {"title": "iHRIS Manage", "packages": ["i2ce", "ihris-common", "ihris-manage"]},
    "ihris-qualify": {"title": "iHRIS Qualify", "packages": ["i2ce", "ihris-common", "ihris-qualify"]},
}


def J(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def forms_projection(product):
    """The forms of one iHRIS product (i2ce + ihris-common + the product), as the Form Documentor drew them on that
    product's site: every form with a class in the committed data model, its fields (own and inherited, as the form
    object holds them) except those kept out of the database, MAP fields to the forms they select from (declared
    `references`, else I2CE's default, the form named after the field), and child forms from the module records."""
    spec = PRODUCTS[product]
    classes, form_class, children, schemes = {}, {}, collections.defaultdict(set), {}
    for pkg in spec["packages"]:
        for f in sorted(glob.glob(os.path.join(ROOT, "src", pkg, "data-model", RELEASE, "*.json"))):
            d = J(f)
            classes.setdefault(d["class"], d)
            for form in d["forms"]:
                form_class.setdefault(form, d["class"])
        for f in sorted(glob.glob(os.path.join(ROOT, "src", pkg, "modules", RELEASE, "*.json"))):
            m = J(f)
            for c in m.get("childForms") or []:
                children[c["form"]].update(c["children"])
            if m.get("formDocumentorScheme"):
                schemes[pkg] = m["formDocumentorScheme"]
    # The product's colours first (its configuration is read after ihris-common's), then the common ones; the
    # graph options are i2ce's own (FormDocumentor.xml).
    colors = (schemes.get(product, {}).get("colors") or []) + (schemes.get("ihris-common", {}).get("colors") or [])
    graph_options = schemes.get("i2ce", {}).get("graphOptions") or []

    def fields_of(cls, seen=()):
        d = classes.get(cls)
        if d is None or cls in seen:
            return []
        return fields_of(d.get("extends"), seen + (cls,)) + d["fields"]

    forms = sorted(form_class)
    nodes, edges = [], []
    for form in forms:
        cls = form_class[form]
        rows, seen = [], set()
        for fd in fields_of(cls):
            if fd["field"] in seen or fd.get("inDb") is False:
                continue
            seen.add(fd["field"])
            ann = (fd.get("label") or "").strip()
            if fd.get("required"):
                ann += " *"
            if fd.get("unique"):
                u = f"!∈ {{{fd['uniqueField']}}} " if fd.get("uniqueField") else "! "
                ann += ("," if fd.get("required") else " ") + u
            rows.append([f"{fd['field']} ({fd.get('type')})", ann.strip() or None])
            if fd.get("type") in ("MAP", "MAP_MULT"):
                targets = fd.get("references") or [fd["field"]]
                edges.append({"from": form, "to": sorted(t for t in targets if t in form_class), "label": fd["field"], "kind": "ref"})
        nodes.append({"id": form, "header": f"{form} ({cls})", "rows": rows})
        if children.get(form):
            edges.append({"from": form, "to": sorted(children[form]), "label": None, "kind": "child"})
    return {"title": f"{spec['title']} - {RELEASE}", "graphOptions": graph_options, "colors": colors,
            "nodes": nodes, "edges": edges}


if __name__ == "__main__":
    a = sys.argv
    if "--forms" not in a:
        sys.exit("usage: kg_layout.py --forms ihris-manage|ihris-qualify [--out FILE]")
    dot = to_dot(forms_projection(a[a.index("--forms") + 1]))
    if "--out" in a:
        open(a[a.index("--out") + 1], "w", encoding="utf-8").write(dot)
    else:
        sys.stdout.write(dot)
