#!/usr/bin/env bun
/**
 * Make a built ihris site follow the folio chrome's light/dark switch, with the PLATFORM's functions.
 *
 *   bun run src/tools/scheme_css.ts --site <dir> --rules <flat-rules.css>
 *
 * - appends cat-harness's `darkRules(rules)` to `<dir>/assets/ihris.css`: the dark scheme applies
 *   when the OS is dark and the reader has not picked light, or whenever the reader picked dark;
 * - adds cat-harness's `withSavedScheme` snippet to the head of every page, so a reader who picked a
 *   scheme gets it at first paint, not after the rail's deferred script runs (no light flash).
 *
 * `rules` are the dark scheme as flat CSS rules, written by build_site.py from the derived theme
 * (src/site/theme/ihris-classic-dark.json, src/tools/derive_dark_theme.py). Nothing is styled here.
 */
import { appendFileSync, readFileSync, readdirSync, statSync, writeFileSync } from "node:fs";
import { join } from "node:path";

import { darkRules, withSavedScheme } from "../../cat-harness/scripts/lib/scheme-css.ts";

const arg = (f: string) => {
  const i = process.argv.indexOf(f);
  return i < 0 ? undefined : process.argv[i + 1];
};
const site = arg("--site");
const rules = arg("--rules");
if (!site || !rules) {
  console.error("usage: scheme_css.ts --site <dir> --rules <flat-rules.css>");
  process.exit(2);
}

appendFileSync(join(site, "assets", "ihris.css"), "\n/* dark scheme: cat-harness darkRules */\n" + darkRules(readFileSync(rules, "utf-8")) + "\n");

let pages = 0;
const walk = (dir: string) => {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p);
    else if (name.endsWith(".html")) {
      const html = readFileSync(p, "utf-8");
      const out = withSavedScheme(html);
      if (out !== html) {
        writeFileSync(p, out);
        pages++;
      }
    }
  }
};
walk(site);
console.log(`scheme_css: dark rules in assets/ihris.css; ${pages} page(s) restore the reader's scheme at first paint`);
