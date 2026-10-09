#!/usr/bin/env python3
"""The data/ETL workflow of this folio as a Mermaid flowchart, GENERATED from what the skills and Tools declare.

  python3 src/tools/gen_workflow.py            # print the Mermaid
  python3 src/tools/gen_workflow.py --json     # the same graph as nodes and edges

Nothing here is drawn by hand (owner, 2026-10-09: "Tool nodes should get read/write from Skill i/o, no?"):

- an ARTEFACT is a kind of data, defined once in src/schemas/skills/artefacts.schema.json (where it lives, what its
  records are, where it is published);
- a SKILL reads the artefacts its `input:` contract names and writes those its `output:` contract names;
- the TOOLS that perform a skill are the Tool nodes that `satisfy` it (QA `skill-contracts` checks they cover it).

So the diagram changes when a contract changes, and cannot disagree with the declarations it is drawn from.
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFACTS = "src/schemas/skills/artefacts.schema.json"


def J(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


def front(rel):
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def layer(d):
    """Which band of the diagram an artefact sits in, read from where it lives."""
    p = d.get("default") or ""
    if d.get("x-published"):
        return "published", "Published on gh-pages"
    if p.startswith(("uploads/", "<clone-dir>", "ihris5-source/")):
        return "sources", "Sources: uploaded or mounted, never committed"
    if re.match(r"src/\*/|library/|src/ihris5/", p):
        return "kg", "Generated knowledge graph"
    if p.startswith(("src/ihris-data-dictionary/", "glossary/", "src/site/theme/", "src/ihris-4-on-fhir/")):
        return "derived", "Derived assets"
    return "work", "Work plan, processes, design and gates"


def graph():
    defs = J(ARTEFACTS)["$defs"]
    tools = [J(os.path.relpath(f, ROOT)) for f in sorted(glob.glob(os.path.join(ROOT, "src/tools/*.tool.json")))]
    skills = []
    for f in sorted(glob.glob(os.path.join(ROOT, "src/skills/*.md"))):
        rel = os.path.relpath(f, ROOT)
        fm = front(rel)
        io = {}
        for kind in ("input", "output"):
            c = J(fm[kind]) if fm.get(kind) else {"properties": {}}
            io[kind] = [p["$ref"].rsplit("/", 1)[-1] for p in c.get("properties", {}).values()]
        skills.append({"name": fm["name"], "inputs": io["input"], "outputs": io["output"],
                       "tools": [t["id"] for t in tools if fm["name"] in (t.get("satisfies") or [])]})
    used = {a for s in skills for a in s["inputs"] + s["outputs"]}
    arts = [{"id": a, "title": d["title"], "path": d.get("default"), "layer": layer(d)[0], "band": layer(d)[1],
             **({"published": d["x-published"]} if d.get("x-published") else {})} for a, d in defs.items() if a in used]
    edges = [(a, s["name"], "reads") for s in skills for a in s["inputs"]] + \
            [(s["name"], a, "writes") for s in skills for a in s["outputs"]]
    return {"artefacts": arts, "skills": skills, "edges": edges}


def mermaid(g):
    # Mermaid entity codes: a quote ends the label, and `<clone-dir>` would read as markup.
    esc = lambda s: s.replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")  # noqa: E731
    out = ["flowchart LR",
           "  classDef art fill:#eef6e2,stroke:#406002,color:#1d2733",
           "  classDef src fill:#eef3f8,stroke:#1e5483,color:#1d2733",
           "  classDef pub fill:#e8e4f5,stroke:#5a4a9a,color:#1d2733",
           "  classDef skill fill:#fff7e0,stroke:#9a7a12,color:#1d2733"]
    bands = {}
    for a in g["artefacts"]:
        bands.setdefault((a["layer"], a["band"]), []).append(a)
    order = ["sources", "kg", "derived", "work", "published"]
    for (lay, band), arts in sorted(bands.items(), key=lambda kv: order.index(kv[0][0])):
        out.append(f'  subgraph {lay}["{esc(band)}"]')
        for a in arts:
            cls = "src" if lay == "sources" else "pub" if lay == "published" else "art"
            out.append(f'    {a["id"]}(["{esc(a["title"])}<br/><small>{esc(a["path"] or "")}</small>"]):::{cls}')
        out.append("  end")
    for s in g["skills"]:
        tools = ", ".join(t.replace("ihris-", "") for t in s["tools"]) or "by hand"
        out.append(f'  sk_{s["name"].replace("-", "_")}["<b>{esc(s["name"])}</b><br/><small>{esc(tools)}</small>"]:::skill')
    for a, b, kind in g["edges"]:
        if kind == "reads":
            out.append(f'  {a} --> sk_{b.replace("-", "_")}')
        else:
            out.append(f'  sk_{a.replace("-", "_")} --> {b}')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    g = graph()
    print(json.dumps(g, indent=2) if "--json" in sys.argv else mermaid(g), end="")
