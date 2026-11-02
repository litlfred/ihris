// The harness data that is the same on every page of a build, written ONCE
// here instead of into each page (bean `gp2f`, page weight). Measured on
// gh-pages 1ad53fa, 2026-10-23: the tiles list was 12.5 KB and the navbar icon
// row 2.5 KB of every Jekyll page, about 15 KB of a 42 KB page.
//
// `head_custom.html` keeps the two places the readers look, empty, and loads
// this as the FIRST deferred script. Deferred scripts run in document order,
// so `navbar-row.js` and `docs-ui.js` find them filled, exactly as when the
// data was inlined. If this file does not load, the islands stay named and
// empty, and the readers report a failed load instead of "declared none".
(function () {
  var row = document.getElementById("fa-navbar-row");
  if (row && row.getAttribute("data-fa-row-src") === "harness-data" && !row.textContent) {
    row.textContent = "{\"icons\":[\"close\",\"beans\",\"launcher\"],\"hrefs\":{\"beans\":\"/beans/\"},\"notes\":{},\"folders\":[{\"kind\":\"bean-defs\",\"label\":\"Bean definitions\",\"note\":\"no viewer yet\"},{\"kind\":\"beans\",\"label\":\"Beans\",\"path\":\"/beans/\"},{\"kind\":\"catalogue\",\"label\":\"Catalogue\",\"note\":\"no viewer yet\"},{\"kind\":\"code\",\"label\":\"Code\",\"note\":\"no viewer yet\"},{\"kind\":\"docs\",\"label\":\"Docs\",\"note\":\"no viewer yet\"},{\"kind\":\"glossary\",\"label\":\"Glossary\",\"path\":\"/glossary/\"},{\"kind\":\"library\",\"label\":\"Library\",\"path\":\"https://litlfred.github.io/ihris/en/cat-harness/library/ihris/\"},{\"kind\":\"processes\",\"label\":\"Processes\",\"path\":\"https://litlfred.github.io/ihris/en/cat-harness/processes/ihris/\"},{\"kind\":\"schemas\",\"label\":\"Schemas\",\"path\":\"https://litlfred.github.io/ihris/en/cat-harness/schemas/ihris/\"},{\"kind\":\"skills\",\"label\":\"Skills\",\"note\":\"no viewer yet\"},{\"kind\":\"uploads\",\"label\":\"Uploads\",\"note\":\"ihris's uploads graph is not published on this site\"}]}";
    row.removeAttribute("data-fa-row-src");
  }
  var tiles = document.querySelector('meta[name="fa-tiles"][data-fa-src="harness-data"]');
  if (tiles && !tiles.getAttribute("content")) {
    tiles.setAttribute("content", "[{\"id\":\"beans\",\"directory\":\"beans\",\"title\":\"Beans\",\"qualifier\":\"iHRIS Knowledge Base\",\"ref\":\"docs/beans/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false,\"icon\":\"beans\"},{\"id\":\"glossary\",\"directory\":\"glossary\",\"title\":\"Glossary\",\"qualifier\":\"iHRIS Knowledge Base\",\"ref\":\"docs/glossary/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false,\"readOnly\":true},{\"id\":\"library-papers\",\"directory\":\"library-papers\",\"title\":\"Library\",\"qualifier\":\"iHRIS Knowledge Base\",\"ref\":\"docs/library/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false,\"icon\":\"library\"},{\"id\":\"schemas\",\"directory\":\"schemas\",\"title\":\"Schemas\",\"qualifier\":\"iHRIS Knowledge Base\",\"ref\":\"docs/schemas/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false,\"icon\":\"schemas\"}]");
    tiles.removeAttribute("data-fa-src");
  }
})();
