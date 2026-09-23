# Restoring iHRIS documentation

## Recovered

- **User manuals** for iHRIS Manage and iHRIS Qualify: the wiki pages exported into the 4.3.3 help modules, now in [`library/ihris-wiki/osi-help-4.3.3/`](../library/ihris-wiki/osi-help-4.3.3/).
- **Module reference** for i2ce, ihris-common, ihris-manage and ihris-qualify 4.3.3: every module's own `displayName` / `description` / requirements, in `src/<instance>/modules/4.3.3/`.
- **Release notes** from Launchpad milestone pages, in each instance's `catalogue/records/release--*.json` and summarized in its README.
- **Implementation process**: the six toolkit stages, in [`library/ihris-toolkit/`](../library/ihris-toolkit/).

## Missing, and where it could come from

| gap | likely source | blocked by |
|---|---|---|
| developer/implementer wiki pages (module guides, installation, customization) | MediaWiki dump; web.archive.org captures of `wiki.ihris.org`; people's copies | wiki.ihris.org and web.archive.org egress-blocked |
| the 47 tool documents hosted on the toolkit | toolkit.ihris.org | egress-blocked; upload them to `uploads/toolkit/` |
| ihris-plan and openhie-pr modules | their release tarballs | launchpadlibrarian.net blocked; upload them (MD5s are already recorded) |
| branch history, bugs, blueprints, answers | code/bugs/blueprints/answers.launchpad.net | egress-blocked |
| iHRIS 5 docs text | `iHRIS/ihris-documentation` | no licence file, so it is referenced only until the owner confirms a licence |
