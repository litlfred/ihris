#!/usr/bin/env bun
/**
 * Write this folio's work-plan projection, `assets/beans/index.json` (`folio-bean-index/v1`) and
 * `assets/beans/count.json`, into a built site, with the PLATFORM's own functions.
 *
 *   bun run src/tools/gen_beans_data.ts --out <site dir>
 *
 * This is the bean block of cat-harness's `gen-docs-pages.ts`, which writes the same two files for
 * the platform's own Jekyll site and cannot be pointed at another one. Every value comes from the
 * same function it calls there (the store, the block edges both ways, the findings, the milestone
 * rollup, the open count and its unit), so the dashboard (`work-plan.js`) and the navbar's beans
 * badge read exactly the shape they read on the platform. Nothing is computed here that the
 * platform does not compute. Only the composition is restated, and it is short.
 *
 * Imports reach the mounted cat-harness (src/tools/mount_platform.sh); without it this cannot run.
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";

import { beanFindings, blockEdges, blockedBy, blocksOf, readBeans } from "../../cat-harness/scripts/beans.ts";
import { milestoneRollup } from "../../cat-harness/scripts/milestone-rollup.ts";
import { OPEN_BEANS_UNIT, openBeanCount } from "../../cat-harness/scripts/bean-store-read.ts";
import { tileCounts } from "../../cat-harness/schemas/tile-count.ts";
import { detectRepoUrl } from "../../cat-harness/src/core/git-refs.ts";

/** The platform's preview length (`BEAN_BODY_PREVIEW` in gen-docs-pages.ts). */
const BEAN_BODY_PREVIEW = 400;

const at = process.argv.indexOf("--out");
if (at < 0 || !process.argv[at + 1]) {
  console.error("usage: gen_beans_data.ts --out <site dir>");
  process.exit(2);
}
const out = resolve(process.argv[at + 1]!);
const root = resolve(import.meta.dir, "..", "..");

const beans = readBeans(root);
if (beans === null) {
  // "No store" is not "a store with nothing in it": write nothing, and the board says so.
  console.error("gen_beans_data: no bean store here (.beans.yml); nothing written");
  process.exit(1);
}
const { edges, dangling } = blockEdges(beans);
const blockers = blockedBy(beans);
const blocks = blocksOf(beans);
const counts = tileCounts({ beans: [openBeanCount(beans), OPEN_BEANS_UNIT] });
const doc = {
  $schema: "folio-bean-index/v1",
  ...counts,
  repoWeb: detectRepoUrl(root) ?? "https://github.com/litlfred/ihris",
  items: beans.map((b) => ({
    id: b.id,
    title: b.title,
    status: b.status,
    type: b.type,
    priority: b.priority,
    parent: b.parent,
    blocking: blocks.get(b.id) ?? [],
    blockedBy: blockers.get(b.id) ?? [],
    createdAt: b.createdAt,
    updatedAt: b.updatedAt,
    preview: b.body.trim().slice(0, BEAN_BODY_PREVIEW),
    file: b.file,
  })),
  edges,
  findings: beanFindings(beans),
  plan: milestoneRollup(beans),
};
const dir = join(out, "assets", "beans");
mkdirSync(dir, { recursive: true });
writeFileSync(join(dir, "index.json"), JSON.stringify(doc, null, 2) + "\n");
writeFileSync(join(dir, "count.json"), JSON.stringify(counts, null, 2) + "\n");
console.log(
  `assets/beans/index.json: ${doc.items.length} bean(s), ${openBeanCount(beans)} open, ${edges.length} block edge(s), ` +
    `${dangling.length} dangling, ${doc.findings.length} finding(s)`,
);
