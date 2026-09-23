// Validate this repository's platform-shaped files with folio-assistant's OWN zod
// schemas, so "valid" means what the platform means by it. Run from a
// folio-assistant checkout (validate.py does):
//   bun run <this-repo>/src/tools/validate-folio.ts <this-repo>
//
// What it covers, by schema:
//   folio-catalogue/v1, folio-catalogue-node/v1   CatalogueSchema, CatalogueNodeSchema (by $schema tag)
//   *.tool.json                                   ToolDefinitionSchema
//   ihris.json and every instance declaration     CatHarnessDeclarationSchema (the paths come from ihris.json)
//   ihris.config.json                             HarnessConfigSchema
//   beans/beans.json                              BeanGraphSchema
//   src/skills/package-manifest.json              SkillPackageManifestSchema
//   library/*/structure.json (pdf-structure/v1)   PdfStructureSchema
//
// zod drops keys a schema does not declare. So a declaration passing here says
// nothing about ihris's own fields (`source`, `materialization`, ...). validate.py
// checks those against src/schemas/ihris-instance-extension.schema.json.
import { readFileSync } from "node:fs";
import { Glob } from "bun";
import { resolve } from "node:path";
const S = (p: string) => import(resolve(process.cwd(), p));
const { CatalogueNodeSchema, CatalogueSchema } = await S("folio-assistant-core/schemas/catalogue.ts");
const { ToolDefinitionSchema } = await S("cat-harness/schemas/tool.ts");
const { CatHarnessDeclarationSchema } = await S("cat-harness/schemas/cat-harness.ts");
const { HarnessConfigSchema } = await S("cat-harness/schemas/harness-config.ts");
const { BeanGraphSchema } = await S("cat-harness/schemas/bean-graph.ts");
const { SkillPackageManifestSchema } = await S("cat-harness/schemas/skill-package.ts");
// pdf-structure/v1 was defined upstream in litlfred/folio-assistant#1113 (issue #1112).
// An older checkout has no such module: say so, never pass silently.
const { PdfStructureSchema } = await S("cat-harness/schemas/pdf-structure.ts").catch(() => {
  console.log("folio-assistant checkout predates cat-harness/schemas/pdf-structure.ts (#1112): update it");
  process.exit(1);
});

const root = process.argv[2];
let bad = 0;
const counts: Record<string, number> = {};
const read = (rel: string) => JSON.parse(readFileSync(resolve(root, rel), "utf8"));

function check(rel: string, tag: string, schema: any, doc: any) {
  counts[tag] = (counts[tag] ?? 0) + 1;
  const r = schema.safeParse(doc);
  if (!r.success) {
    bad++;
    if (bad <= 20) console.log(`${rel}: ${JSON.stringify(r.error.issues.slice(0, 3))}`);
  }
}

for (const rel of new Glob("{src,library}/**/*.json").scanSync(root)) {
  let doc: any;
  try {
    doc = read(rel);
  } catch {
    continue;
  }
  if (rel.endsWith(".tool.json")) check(rel, "tool", ToolDefinitionSchema, doc);
  else if (doc?.$schema === "folio-catalogue-node/v1") check(rel, doc.$schema, CatalogueNodeSchema, doc);
  else if (doc?.$schema === "folio-catalogue/v1") check(rel, doc.$schema, CatalogueSchema, doc);
  else if (doc?._schema === "pdf-structure/v1") check(rel, doc._schema, PdfStructureSchema, doc);
}

const decl = read("ihris.json");
check("ihris.json", "declaration", CatHarnessDeclarationSchema, decl);
for (const i of decl.instances ?? []) {
  const rel = `${i.path}/${i.name}.json`;
  check(rel, "declaration", CatHarnessDeclarationSchema, read(rel));
}
check("ihris.config.json", "harness-config", HarnessConfigSchema, read("ihris.config.json"));
check("beans/beans.json", "bean-graph", BeanGraphSchema, read("beans/beans.json"));
check("src/skills/package-manifest.json", "skill-package", SkillPackageManifestSchema, read("src/skills/package-manifest.json"));

console.log(`folio-assistant zod: ${JSON.stringify(counts)}; ${bad} invalid`);
process.exit(bad ? 1 : 0);
