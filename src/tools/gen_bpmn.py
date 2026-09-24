#!/usr/bin/env python3
"""Generate a BPMN 2.0 file (with diagram) from a compact JSON process spec.

    python3 src/tools/gen_bpmn.py processes/specs/<name>.json   # writes processes/<name>.bpmn
    python3 src/tools/gen_bpmn.py --check                       # every spec: output up to date?

The spec is the source; the .bpmn is generated (AGENTS.md: generated means
generated). It follows folio-assistant's BPMN conventions: one pool, one lane
per role (`<bootstrap.processes:role ref>`), every task names its skill
(`<bootstrap.processes:skill ref>`) or says why it has none
(`<cat-harness.processes:no-skill reason>`), and a call activity
descends into another process by id (`calledElement`), so an existing
process is called rather than copied.

Spec shape:
  {"id": "Process_X", "name": "...", "documentation": "...", "file": "x.bpmn",
   "lanes": [{"id": "Lane_A", "name": "...", "role": "reviewer", "documentation": "..."}],
   "nodes": [{"id": "T1", "type": "task|callActivity|startEvent|endEvent|exclusiveGateway",
              "lane": "Lane_A", "col": 0, "name": "...", "documentation": "...",
              "skill": "...", "noSkill": "...", "calledElement": "Process_Y"}],
   "flows": [{"from": "T1", "to": "T2", "name": "..."}]}
Layout is mechanical: x from `col`, y from the lane. Back-edges (to an equal or
earlier column) route beneath their lane.
"""
import glob
import json
import os
import sys
from xml.sax.saxutils import escape, quoteattr

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LANE_H, COL_W, X0, POOL_X, LANE_X = 170, 190, 250, 160, 190
SIZE = {"task": (140, 80), "callActivity": (140, 80), "startEvent": (36, 36), "endEvent": (36, 36), "exclusiveGateway": (50, 50)}


def generate(spec):
    lanes = {l["id"]: i for i, l in enumerate(spec["lanes"])}
    ncols = max(n["col"] for n in spec["nodes"]) + 1
    width = X0 - POOL_X + ncols * COL_W + 60
    box = {}
    for n in spec["nodes"]:
        w, h = SIZE[n["type"]]
        cx = X0 + n["col"] * COL_W + 70
        cy = 80 + lanes[n["lane"]] * LANE_H + LANE_H // 2
        box[n["id"]] = (cx - w // 2, cy - h // 2, w, h)
    q = quoteattr
    pid = spec["id"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"',
           '                  xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"',
           '                  xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"',
           '                  xmlns:di="http://www.omg.org/spec/DD/20100524/DI"',
           # Each element's prefix names the Subgraph that DECLARES it, bound to
           # that Subgraph's own address (folio-assistant bean 12s9): skill and
           # role are bootstrap's, no-skill is cat-harness's. Readers match the
           # address, never the prefix text.
           '                  xmlns:bootstrap.processes="https://litlfred.github.io/folio-assistant/bootstrap/processes/ns#"',
           *(['                  xmlns:cat-harness.processes="https://litlfred.github.io/folio-assistant/cat-harness/processes/ns#"']
             if any(n.get("noSkill") and not n.get("skill") for n in spec["nodes"] if n["type"] in ("task", "callActivity")) else []),
           f'                  id="Definitions_{pid}" targetNamespace="https://litlfred.github.io/ihris/workflows"',
           '                  exporter="ihris gen_bpmn.py" exporterVersion="1">',
           f'  <bpmn:collaboration id="Collaboration_{pid}">',
           f'    <bpmn:participant id="Participant_{pid}" name={q(spec["name"])} processRef="{pid}"/>',
           '  </bpmn:collaboration>',
           f'  <bpmn:process id="{pid}" name={q(spec["name"])} isExecutable="false">',
           f'    <bpmn:documentation>{escape(spec["documentation"])}</bpmn:documentation>',
           f'    <bpmn:laneSet id="LaneSet_{pid}">']
    for l in spec["lanes"]:
        out.append(f'      <bpmn:lane id="{l["id"]}" name={q(l["name"])}>')
        out.append(f'        <bpmn:documentation>{escape(l["documentation"])}</bpmn:documentation>')
        out.append(f'        <bpmn:extensionElements><bootstrap.processes:role ref="{l["role"]}"/></bpmn:extensionElements>')
        for n in spec["nodes"]:
            if n["lane"] == l["id"]:
                out.append(f'        <bpmn:flowNodeRef>{n["id"]}</bpmn:flowNodeRef>')
        out.append('      </bpmn:lane>')
    out.append('    </bpmn:laneSet>')
    for n in spec["nodes"]:
        attrs = f' calledElement="{n["calledElement"]}"' if n["type"] == "callActivity" else ""
        head = f'    <bpmn:{n["type"]} id="{n["id"]}" name={q(n["name"])}{attrs}'
        inner = []
        if n.get("documentation"):
            inner.append(f'      <bpmn:documentation>{escape(n["documentation"])}</bpmn:documentation>')
        if n["type"] in ("task", "callActivity"):
            if n.get("skill"):
                inner.append(f'      <bpmn:extensionElements><bootstrap.processes:skill ref="{n["skill"]}"/></bpmn:extensionElements>')
            elif n.get("noSkill"):
                inner.append(f'      <bpmn:extensionElements><cat-harness.processes:no-skill reason={q(n["noSkill"])}/></bpmn:extensionElements>')
        out += [head + ">", *inner, f'    </bpmn:{n["type"]}>'] if inner else [head + "/>"]
    for i, f in enumerate(spec["flows"], 1):
        name = f' name={q(f["name"])}' if f.get("name") else ""
        out.append(f'    <bpmn:sequenceFlow id="SF_{pid}_{i}"{name} sourceRef="{f["from"]}" targetRef="{f["to"]}"/>')
    out += ['  </bpmn:process>', f'  <bpmndi:BPMNDiagram id="Diagram_{pid}">',
            f'    <bpmndi:BPMNPlane id="Plane_{pid}" bpmnElement="Collaboration_{pid}">',
            f'      <bpmndi:BPMNShape id="Shape_Participant_{pid}" bpmnElement="Participant_{pid}" isHorizontal="true">',
            f'        <dc:Bounds x="{POOL_X}" y="80" width="{width + (LANE_X - POOL_X)}" height="{LANE_H * len(lanes)}" />',
            '      </bpmndi:BPMNShape>']
    for l, i in lanes.items():
        out += [f'      <bpmndi:BPMNShape id="Shape_{l}" bpmnElement="{l}" isHorizontal="true">',
                f'        <dc:Bounds x="{LANE_X}" y="{80 + i * LANE_H}" width="{width}" height="{LANE_H}" />',
                '      </bpmndi:BPMNShape>']
    for n in spec["nodes"]:
        x, y, w, h = box[n["id"]]
        mark = ' isMarkerVisible="true"' if n["type"] == "exclusiveGateway" else ""
        out += [f'      <bpmndi:BPMNShape id="Shape_{n["id"]}" bpmnElement="{n["id"]}"{mark}>',
                f'        <dc:Bounds x="{x}" y="{y}" width="{w}" height="{h}" />', '      </bpmndi:BPMNShape>']
    col = {n["id"]: n["col"] for n in spec["nodes"]}
    lane_of = {n["id"]: lanes[n["lane"]] for n in spec["nodes"]}
    for i, f in enumerate(spec["flows"], 1):
        sx, sy, sw, sh = box[f["from"]]
        tx, ty, tw, th = box[f["to"]]
        if col[f["to"]] > col[f["from"]]:
            a, b = (sx + sw, sy + sh // 2), (tx, ty + th // 2)
            mx = b[0] - 25
            pts = [a, b] if a[1] == b[1] else [a, (mx, a[1]), (mx, b[1]), b]
        else:  # back-edge: leave from the bottom, run beneath the lane, enter from the bottom
            low = 80 + (max(lane_of[f["from"]], lane_of[f["to"]]) + 1) * LANE_H - 12
            pts = [(sx + sw // 2, sy + sh), (sx + sw // 2, low), (tx + tw // 2, low), (tx + tw // 2, ty + th)]
        out.append(f'      <bpmndi:BPMNEdge id="Edge_SF_{pid}_{i}" bpmnElement="SF_{pid}_{i}">')
        out += [f'        <di:waypoint x="{px}" y="{py}" />' for px, py in pts]
        out.append('      </bpmndi:BPMNEdge>')
    out += ['    </bpmndi:BPMNPlane>', '  </bpmndi:BPMNDiagram>', '</bpmn:definitions>', '']
    return "\n".join(out)


def validate(spec):
    ids = {n["id"] for n in spec["nodes"]}
    lanes = {l["id"] for l in spec["lanes"]}
    errs = [f"{n['id']}: unknown lane {n['lane']}" for n in spec["nodes"] if n["lane"] not in lanes]
    errs += [f"flow {f['from']}->{f['to']}: unknown node" for f in spec["flows"] if f["from"] not in ids or f["to"] not in ids]
    errs += [f"{n['id']}: a task names a skill or says why not" for n in spec["nodes"]
             if n["type"] == "task" and not (n.get("skill") or n.get("noSkill"))]
    errs += [f"{n['id']}: callActivity needs calledElement" for n in spec["nodes"] if n["type"] == "callActivity" and not n.get("calledElement")]
    return errs


def main(argv):
    check = "--check" in argv
    specs = [a for a in argv if not a.startswith("--")] or sorted(glob.glob(os.path.join(ROOT, "processes", "specs", "*.json")))
    bad = 0
    for p in specs:
        spec = json.load(open(p))
        errs = validate(spec)
        if errs:
            bad += 1
            print(f"{os.path.relpath(p, ROOT)}: " + "; ".join(errs))
            continue
        target = os.path.join(ROOT, "processes", spec["file"])
        xml = generate(spec)
        if check:
            if not os.path.exists(target) or open(target).read() != xml:
                bad += 1
                print(f"{os.path.relpath(target, ROOT)}: stale; run src/tools/gen_bpmn.py")
        else:
            open(target, "w").write(xml)
            print(f"wrote {os.path.relpath(target, ROOT)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
