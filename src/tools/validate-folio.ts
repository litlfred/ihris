// Validate this repository's folio-catalogue/v1 and folio-catalogue-node/v1
// files with folio-assistant's OWN zod schemas, so "valid" means what the
// platform means by it. Run from a folio-assistant checkout (validate.py does):
//   bun run <this-repo>/src/tools/validate-folio.ts <this-repo>
import { readFileSync } from "node:fs";
import { Glob } from "bun";
import { resolve } from "node:path";
const { CatalogueNodeSchema, CatalogueSchema } = await import(resolve(process.cwd(), "folio-assistant-core/schemas/catalogue.ts"));
const { ToolDefinitionSchema } = await import(resolve(process.cwd(), "cat-harness/schemas/tool.ts"));

const root = process.argv[2];
let bad = 0;
const counts: Record<string, number> = {};
for (const rel of new Glob("{src,library}/**/*.json").scanSync(root)) {
  const isTool = rel.endsWith(".tool.json");
  const path = resolve(root, rel);
  let doc: any;
  try {
    doc = JSON.parse(readFileSync(path, "utf8"));
  } catch {
    continue;
  }
  const schema = isTool
    ? ToolDefinitionSchema
    : doc?.$schema === "folio-catalogue-node/v1" ? CatalogueNodeSchema : doc?.$schema === "folio-catalogue/v1" ? CatalogueSchema : null;
  if (!schema) continue;
  const tag = isTool ? "tool" : doc.$schema;
  counts[tag] = (counts[tag] ?? 0) + 1;
  const r = schema.safeParse(doc);
  if (!r.success) {
    bad++;
    if (bad <= 20) console.log(`${rel}: ${JSON.stringify(r.error.issues.slice(0, 3))}`);
  }
}
console.log(`folio-assistant zod: ${JSON.stringify(counts)}; ${bad} invalid`);
process.exit(bad ? 1 : 0);
