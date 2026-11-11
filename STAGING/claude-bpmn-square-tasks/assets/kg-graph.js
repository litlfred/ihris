/* KG subgraph viewer: a Graphviz layout drawn in the browser, then made movable.
 *
 * Every element <div class="kg-graph" data-dot-src="x.dot"> is laid out from its DOT by Graphviz compiled to
 * WebAssembly (@hpcc-js/wasm-graphviz), the i2ce Form Documentor's pipeline: `unflatten -f -l 2 -c 2 | dot`.
 * The reader can then:
 *   - pan (drag the background) and zoom (wheel, or the + / - / fit buttons);
 *   - drag a node: the edges that touch it follow, their ends moved with it and their middles in proportion;
 *   - find a node by name (the search box centres and outlines it).
 * Written by src/tools/build_site.py beside the DOT that src/tools/kg_layout.py writes. No build step.
 */
import { Graphviz } from "https://cdn.jsdelivr.net/npm/@hpcc-js/wasm-graphviz@1.6.1/dist/index.js";

const SVGNS = "http://www.w3.org/2000/svg";
let gvPromise = null;
const graphviz = () => (gvPromise ||= Graphviz.load());

/** Numbers of an SVG path or points attribute, as [x, y] pairs. */
function pairs(s) {
  const n = (s.match(/-?\d*\.?\d+(?:e-?\d+)?/gi) || []).map(Number);
  const out = [];
  for (let i = 0; i + 1 < n.length; i += 2) out.push([n[i], n[i + 1]]);
  return out;
}

function pathFrom(pts) {
  // Graphviz edges are `M p0 C p1 p2 p3 [p4 p5 p6 ...]`.
  const f = (p) => `${p[0].toFixed(2)},${p[1].toFixed(2)}`;
  return `M${f(pts[0])}C` + pts.slice(1).map(f).join(" ");
}

function title(g) {
  const t = g.querySelector(":scope > title");
  return t ? t.textContent : "";
}

async function mount(el) {
  const status = el.querySelector(".kg-graph-status") || el.appendChild(Object.assign(document.createElement("p"), { className: "kg-graph-status" }));
  status.textContent = "Laying out the graph…";
  let svgText;
  try {
    const dot = await (await fetch(el.dataset.dotSrc)).text();
    const gv = await graphviz();
    const [l, f, c] = (el.dataset.unflatten || "2,1,2").split(",").map(Number);
    svgText = gv.dot(l > 0 ? gv.unflatten(dot, l, !!f, c) : dot);
  } catch (e) {
    status.textContent = `The graph could not be laid out here (${e.message}). The DOT is at ${el.dataset.dotSrc}.`;
    return;
  }
  status.remove();
  const stage = document.createElement("div");
  stage.className = "kg-graph-stage";
  stage.innerHTML = svgText.replace(/^[\s\S]*?(<svg)/, "$1");
  el.appendChild(stage);
  const svg = stage.querySelector("svg");
  const root = svg.querySelector("g.graph");
  svg.removeAttribute("width");
  svg.removeAttribute("height");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", el.dataset.label || "Graph");

  // ---- the view: pan and zoom by rewriting the viewBox
  // The view always has the stage's aspect ratio, so a screen point maps to the viewBox without letterboxing.
  const vb0 = svg.viewBox.baseVal;
  const drawn = { x: vb0.x, y: vb0.y, w: vb0.width, h: vb0.height };
  const fitted = () => {
    const r = svg.getBoundingClientRect(), k = r.height / r.width || 1;
    const w = Math.max(drawn.w, drawn.h / k), h = w * k;
    return { x: drawn.x - (w - drawn.w) / 2, y: drawn.y - (h - drawn.h) / 2, w, h };
  };
  let full = fitted();
  let view = { ...full };
  const apply = () => svg.setAttribute("viewBox", `${view.x} ${view.y} ${view.w} ${view.h}`);
  apply();
  new ResizeObserver(() => {
    const k = (svg.getBoundingClientRect().height / svg.getBoundingClientRect().width) || 1;
    full = fitted();
    view = { ...view, h: view.w * k };
    apply();
  }).observe(stage);
  const toSvg = (cx, cy) => {
    const r = svg.getBoundingClientRect();
    return [view.x + ((cx - r.left) / r.width) * view.w, view.y + ((cy - r.top) / r.height) * view.h];
  };
  const zoom = (k, cx, cy) => {
    const r = svg.getBoundingClientRect();
    const [px, py] = cx === undefined ? [view.x + view.w / 2, view.y + view.h / 2] : toSvg(cx, cy);
    view = { x: px - (px - view.x) * k, y: py - (py - view.y) * k, w: view.w * k, h: view.h * k };
    apply();
  };
  svg.addEventListener("wheel", (e) => { e.preventDefault(); zoom(e.deltaY > 0 ? 1.15 : 1 / 1.15, e.clientX, e.clientY); }, { passive: false });

  // ---- what moves with a node: each edge's endpoints, from its title "a->b"
  const nodes = new Map();
  for (const g of root.querySelectorAll("g.node")) nodes.set(title(g), { g, dx: 0, dy: 0 });
  const edges = [];
  for (const g of root.querySelectorAll("g.edge")) {
    const m = title(g).split("->");
    const path = g.querySelector("path");
    if (m.length !== 2 || !path) continue;
    edges.push({
      from: m[0], to: m[1], path, pts: pairs(path.getAttribute("d")),
      heads: [...g.querySelectorAll("polygon")].map((p) => ({ el: p, pts: pairs(p.getAttribute("points")) })),
      labels: [...g.querySelectorAll("text")].map((t) => ({ el: t, x: +t.getAttribute("x"), y: +t.getAttribute("y") })),
    });
  }
  const shift = (name) => nodes.get(name) || { dx: 0, dy: 0 };
  function redraw(e) {
    const a = shift(e.from), b = shift(e.to), n = e.pts.length - 1;
    const pts = e.pts.map(([x, y], i) => [x + a.dx + (b.dx - a.dx) * (i / n), y + a.dy + (b.dy - a.dy) * (i / n)]);
    e.path.setAttribute("d", pathFrom(pts));
    for (const h of e.heads) h.el.setAttribute("points", h.pts.map(([x, y]) => `${x + b.dx},${y + b.dy}`).join(" "));
    for (const l of e.labels) { l.el.setAttribute("x", l.x + (a.dx + b.dx) / 2); l.el.setAttribute("y", l.y + (a.dy + b.dy) / 2); }
  }

  // ---- dragging: a node moves itself and its edges; the background pans
  let drag = null;
  svg.addEventListener("pointerdown", (e) => {
    e.preventDefault(); // a drag, not a text selection
    const g = e.target.closest("g.node");
    const [x, y] = toSvg(e.clientX, e.clientY);
    drag = g ? { node: nodes.get(title(g)), x, y } : { pan: true, x: e.clientX, y: e.clientY, v: { ...view } };
    svg.setPointerCapture(e.pointerId);
    svg.classList.add("kg-dragging");
  });
  svg.addEventListener("pointermove", (e) => {
    if (!drag) return;
    if (drag.pan) {
      const r = svg.getBoundingClientRect();
      view = { ...drag.v, x: drag.v.x - ((e.clientX - drag.x) / r.width) * drag.v.w, y: drag.v.y - ((e.clientY - drag.y) / r.height) * drag.v.h };
      apply();
      return;
    }
    const [x, y] = toSvg(e.clientX, e.clientY);
    drag.node.dx += x - drag.x;
    drag.node.dy += y - drag.y;
    drag.x = x;
    drag.y = y;
    drag.node.g.setAttribute("transform", `translate(${drag.node.dx} ${drag.node.dy})`);
    const name = title(drag.node.g);
    for (const ed of edges) if (ed.from === name || ed.to === name) redraw(ed);
  });
  const end = () => { drag = null; svg.classList.remove("kg-dragging"); };
  svg.addEventListener("pointerup", end);
  svg.addEventListener("pointercancel", end);

  // ---- controls
  const bar = document.createElement("div");
  bar.className = "kg-graph-bar";
  bar.innerHTML = `<label>Find <input type="search" list="${el.id}-names" autocomplete="off"></label>
<datalist id="${el.id}-names">${[...nodes.keys()].filter((n) => !n.startsWith("splitter+")).sort().map((n) => `<option value="${n.replace(/"/g, "&quot;")}">`).join("")}</datalist>
<button type="button" data-z="in" aria-label="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out">&minus;</button>
<button type="button" data-z="fit">Fit</button><button type="button" data-z="reset">Reset layout</button>`;
  el.insertBefore(bar, stage);
  bar.addEventListener("click", (e) => {
    const z = e.target.dataset && e.target.dataset.z;
    if (z === "in") zoom(1 / 1.3);
    else if (z === "out") zoom(1.3);
    else if (z === "fit") { view = { ...full }; apply(); }
    else if (z === "reset") {
      for (const n of nodes.values()) { n.dx = n.dy = 0; n.g.removeAttribute("transform"); }
      edges.forEach(redraw);
    }
  });
  const find = bar.querySelector("input");
  find.addEventListener("change", () => {
    const n = nodes.get(find.value.trim());
    root.querySelectorAll(".kg-found").forEach((g) => g.classList.remove("kg-found"));
    if (!n) return;
    n.g.classList.add("kg-found");
    // The node's box on screen, in viewBox units (Graphviz draws inside a translated group, so getBBox is not).
    const r = n.g.getBoundingClientRect(), s = svg.getBoundingClientRect();
    const [cx, cy] = toSvg(r.left + r.width / 2, r.top + r.height / 2);
    const bw = (r.width / s.width) * view.w;
    const w = Math.max(bw * 4, full.w / 12), h = w * (view.h / view.w);
    view = { x: cx - w / 2, y: cy - h / 2, w, h };
    apply();
  });
}

document.querySelectorAll(".kg-graph[data-dot-src]").forEach(mount);
