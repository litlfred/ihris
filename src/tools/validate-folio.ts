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
//   library/*/images.json (folio-document-images/v1) ImagesSidecarSchema
//   methodologies/*/*.md front matter             MethodologyFrontMatterSchema (folio-methodology/v1)
//   <scenarios dir>/roles.json                    RoleGraphSchema (every directory declaring graphKinds ["scenarios"])
//   <scenarios dir>/actors/*.json                 ActorDefSchema, strict: an actor carries nothing else (no login)
//   <glossary dir>/*.glossary.json                GlossarySchema (folio-glossary/v1; every directory declaring
//                                                 graphKinds ["glossary"]), and core's own toSkos() of each scheme
//                                                 must equal the SKOS JSON-LD the site published (build_glossary.py
//                                                 mirrors toSkos in Python; this holds the mirror to it). The site
//                                                 is <this-repo>/.build/site (validate.py builds it first) and the
//                                                 instance namespace is argv[3] (build_glossary.NS).
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

const { ImagesSidecarSchema } = await S("cat-harness/schemas/document-image.ts");
const { MethodologyFrontMatterSchema } = await S("cat-harness/schemas/methodology.ts");
const { RoleGraphSchema, ActorDefSchema } = await S("cat-harness/schemas/role-graph.ts");
// folio-glossary/v1 is core's, from litlfred/folio-assistant#1218 (issue #1217). Say so on an older checkout.
const { GlossarySchema, toSkos } = await S("folio-assistant-core/schemas/glossary.ts").catch(() => {
  console.log("folio-assistant checkout predates folio-assistant-core/schemas/glossary.ts (#1218): update it");
  process.exit(1);
});
const { parse: parseYaml } = await import(resolve(process.cwd(), "node_modules/yaml/dist/index.js"));

const root = process.argv[2];
const glossaryNs = process.argv[3];
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
  else if (doc?.$schema === "folio-document-images/v1") check(rel, doc.$schema, ImagesSidecarSchema, doc);
}

for (const rel of new Glob("methodologies/*/*.md").scanSync(root)) {
  const m = readFileSync(resolve(root, rel), "utf8").match(/^---\n([\s\S]*?)\n---\n/);
  if (!m) {
    bad++;
    console.log(`${rel}: no front matter`);
    continue;
  }
  let fm: unknown;
  try {
    fm = parseYaml(m[1]);
  } catch (e) {
    bad++;
    console.log(`${rel}: front matter is not valid YAML: ${(e as Error).message.split("\n")[0]}`);
    continue;
  }
  check(rel, "folio-methodology/v1", MethodologyFrontMatterSchema, fm);
}

const decl = read("ihris.json");
check("ihris.json", "declaration", CatHarnessDeclarationSchema, decl);
for (const i of decl.instances ?? []) {
  const rel = `${i.path}/${i.name}.json`;
  check(rel, "declaration", CatHarnessDeclarationSchema, read(rel));
}
// The `scenarios` graph kind: a role graph, and the actors beside it. Found from the declarations,
// never from a hard-coded path, so a new scenarios directory is validated the moment it is declared.
const decls: [string, any][] = [["ihris.json", decl], ...(decl.instances ?? []).map((i: any) => [`${i.path}/${i.name}.json`, read(`${i.path}/${i.name}.json`)])];
for (const [rel, d] of decls) {
  const base = rel.includes("/") ? rel.slice(0, rel.lastIndexOf("/")) : ".";
  for (const dir of d.directories ?? []) {
    if (!(dir.graphKinds ?? []).includes("scenarios")) continue;
    const at = resolve(root, base, dir.path).slice(resolve(root).length + 1);
    let roles: any;
    try {
      roles = read(`${at}/roles.json`);
    } catch {
      bad++;
      console.log(`${rel}: scenarios directory ${dir.path} has no readable roles.json`);
      continue;
    }
    check(`${at}/roles.json`, "role-graph", RoleGraphSchema, roles);
    for (const a of new Glob(`${at}/actors/*.json`).scanSync(root)) check(a, "actor", ActorDefSchema.strict(), read(a));
  }
}
// The `glossary` graph kind: every *.glossary.json in a declared glossary directory, and its SKOS as core emits it.
for (const [rel, d] of decls) {
  const base = rel.includes("/") ? rel.slice(0, rel.lastIndexOf("/")) : ".";
  for (const dir of d.directories ?? []) {
    if (!(dir.graphKinds ?? []).includes("glossary")) continue;
    const at = resolve(root, base, dir.path).slice(resolve(root).length + 1);
    for (const g of new Glob(`${at}/*.glossary.json`).scanSync(root)) {
      const doc = read(g);
      check(g, "folio-glossary/v1", GlossarySchema, doc);
      const r = GlossarySchema.safeParse(doc);
      if (!r.success) continue;
      if (!glossaryNs) {
        bad++;
        console.log(`${g}: no instance namespace given (argv[3]), so its SKOS was not compared with core's toSkos`);
        continue;
      }
      const published = resolve(root, ".build/site/assets/glossary", `${d.name}--${r.data.id}.skos.jsonld`);
      let site: unknown;
      try {
        site = JSON.parse(readFileSync(published, "utf8"));
      } catch {
        bad++;
        console.log(`${g}: the site published no SKOS at ${published.slice(resolve(root).length + 1)} (build the site first)`);
        continue;
      }
      counts["glossary SKOS = core toSkos"] = (counts["glossary SKOS = core toSkos"] ?? 0) + 1;
      if (JSON.stringify(toSkos(r.data, glossaryNs)) !== JSON.stringify(site)) {
        bad++;
        console.log(`${g}: the site's SKOS differs from core's toSkos() (src/tools/build_glossary.py to_skos drifted)`);
      }
    }
  }
}
check("ihris.config.json", "harness-config", HarnessConfigSchema, read("ihris.config.json"));
check("beans/beans.json", "bean-graph", BeanGraphSchema, read("beans/beans.json"));
check("src/skills/package-manifest.json", "skill-package", SkillPackageManifestSchema, read("src/skills/package-manifest.json"));

console.log(`folio-assistant zod: ${JSON.stringify(counts)}; ${bad} invalid`);
process.exit(bad ? 1 : 0);
