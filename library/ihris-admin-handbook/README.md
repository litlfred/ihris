# iHRIS Administrator Handbook, 2010 wiki export (`ihris-admin-handbook`)

*iHRIS Administator Handbook* (sic) is a 534-page PDF that mwlib/PediaPress generated on 2010-09-17 from **79 articles of the iHRIS wiki** (`open.intrahealth.org`, "Osi"). It holds technical overviews, tutorials, module, role and task lists, and data dictionaries for iHRIS 4.0. The owner uploaded it on 2026-09-23. The PDF itself is in `uploads/ihris-admin-handbook/`, which is git-ignored; [`manifest.json`](../../uploads/ihris-admin-handbook/manifest.json) pins it by MD5 and SHA-256.

## Licence and attribution

- **Text: GNU Free Documentation License 1.2**, as the export's last page states (page 534, <http://www.gnu.org/copyleft/fdl.html>). The text comes from the iHRIS wiki, by its contributors (IntraHealth International and the iHRIS community). Each section's front matter gives the article's wiki revision (`source: ...?oldid=`) and its contributors, taken from the export's "Article Sources and Contributors" appendix. These are listed below and in [`book.json`](book.json).
- **Images: published with the owner's permission** (litlfred, 2026-09-23). The export's "Image Sources, Licenses and Contributors" appendix gives **License: unknown** for each of its 11 images. Each image keeps its credit line.
- **Redacted:** real e-mail addresses and phone numbers (4 redactions, each listed in `book.json`). Placeholder addresses in example configuration are kept. The export has no talk or user pages, so it has no reader comments.

## What is here

| file | what |
|---|---|
| [`sections/`](sections/) | one Markdown file per wiki article, from the PDF's own text: headings, code blocks and lists kept; running page headers dropped; mwlib's spaces inside URLs undone |
| [`images/`](images/), [`images.json`](images.json) | the 11 placed images, extracted by folio-assistant's `pdf-images` rung (`folio-document-images/v1`) |
| [`book.json`](book.json) | `ihris-wiki-book/v1`: articles (pages, revision, contributors, section sha256), image credits, licences and redactions |
| [`structure.json`](structure.json) | folio-assistant's `pdf-structure/v1`: the full outline (1357 entries) with page ranges |
| [`manifest.jsonld`](manifest.jsonld) | the library node and its sections |

All of it is **generated** by `src/tools/ingest_handbook.py` (Tool `ihris-ingest-handbook`) from the verified PDF. Change the tool, never the output.

## How it relates to `ihris-wiki`

[`library/ihris-wiki`](../ihris-wiki/) restores the same wiki from the user-manual pages exported into the 4.3.3 help modules (GPL). The handbook is a different cut of the same wiki, taken earlier (2010) and under a different licence (GFDL-1.2). It holds mostly the **administrator and developer** articles that `ihris-wiki` lists as still to restore. The two share one page by title: *IHRIS Manage Form Fields - 4.0*. They are kept as separate entries because the provenance and the licence differ. When the developer pages are restored into `ihris-wiki` (skill `restore-wiki-from-help-export`), the handbook is a source for them, at the revisions its appendix names.

## Articles

| article | pages | contributors (wiki usernames) |
|---|---|---|
| [Adding Fields to the Person Form - 4.0](sections/adding-fields-to-the-person-form-4-0.md) | 2–11 | Litlfred |
| [Adding Forms and Fields](sections/adding-forms-and-fields.md) | 11–24 | Lduncan, MarkAHershberger |
| [Adding ISCO 88 Job Codes to iHRIS Manage](sections/adding-isco-88-job-codes-to-ihris-manage.md) | 24–31 | Litlfred, Lucaswood, MarkAHershberger |
| [Automatically Generated Integers](sections/automatically-generated-integers.md) | 32–32 | Lduncan |
| [Configuration (Magic) Data](sections/configuration-magic-data.md) | 32–40 | Litlfred, MarkAHershberger |
| [Configuring Form Cache Generation Timing](sections/configuring-form-cache-generation-timing.md) | 40–44 | Lduncan |
| [Configuring Report Generation Timing](sections/configuring-report-generation-timing.md) | 44–45 | Lduncan |
| [Creating a New Form Field](sections/creating-a-new-form-field.md) | 45–48 | Litlfred |
| [Creating Translations](sections/creating-translations.md) | 48–50 | Lduncan, Litlfred, MarkAHershberger |
| [Custom Reporting -- An Overview](sections/custom-reporting-an-overview.md) | 51–51 | Litlfred |
| [Custom Reporting -- Creating a Staff List Example](sections/custom-reporting-creating-a-staff-list-example.md) | 52–59 | Litlfred |
| [Custom Reporting -- Creating Form Relationships](sections/custom-reporting-creating-form-relationships.md) | 59–61 | Litlfred |
| [Custom Reporting -- Creating Report Views](sections/custom-reporting-creating-report-views.md) | 61–63 | Litlfred |
| [Custom Reporting -- Creating Reports](sections/custom-reporting-creating-reports.md) | 63–64 | Litlfred |
| [Customizing Form and Field Headers](sections/customizing-form-and-field-headers.md) | 65–66 | Lduncan, Litlfred |
| [Customizing iHRIS Manage](sections/customizing-ihris-manage.md) | 67–69 | Litlfred, MarkAHershberger, Sturlington |
| [Data Interoperability](sections/data-interoperability.md) | 69–71 | Litlfred, MarkAHershberger |
| [Database Structure](sections/database-structure.md) | 71–75 | Lduncan, Litlfred, MarkAHershberger |
| [Decentralized iHRIS Data Policy](sections/decentralized-ihris-data-policy.md) | 75–76 | Litlfred |
| [Defining Forms](sections/defining-forms.md) | 77–80 | Litlfred, MarkAHershberger |
| [Enabling Translations](sections/enabling-translations.md) | 81–81 | Litlfred |
| [Exporting and Updating Form Caches Using Profiles - 4.0.6](sections/exporting-and-updating-form-caches-using-profiles-4-0-6.md) | 82–83 | Litlfred |
| [Exporting Standardized Data](sections/exporting-standardized-data.md) | 83–90 | Litlfred |
| [File Search Paths](sections/file-search-paths.md) | 90–91 | Litlfred, MarkAHershberger |
| [Form Caches](sections/form-caches.md) | 92–92 | Lduncan, Litlfred |
| [Form Storage -- Entry/Last Entry](sections/form-storage-entry-last-entry.md) | 92–93 | Litlfred, MarkAHershberger |
| [Form Storage -- Flat Table](sections/form-storage-flat-table.md) | 94–95 | Litlfred, MarkAHershberger |
| [Form Storage -- Magic Data](sections/form-storage-magic-data.md) | 96–96 | Litlfred, MarkAHershberger |
| [Form Storage -- Multi-Flat Table](sections/form-storage-multi-flat-table.md) | 97–99 | Litlfred, MarkAHershberger |
| [Form Storage Mechanisms](sections/form-storage-mechanisms.md) | 100–100 | Lduncan, Litlfred, MarkAHershberger |
| [Forms and Form Classes](sections/forms-and-form-classes.md) | 101–102 | Litlfred, MarkAHershberger |
| [HowTo: Install Memcached](sections/howto-install-memcached.md) | 103–104 | Lduncan, Litlfred |
| [I2CE Module List (4.0.6)](sections/i2ce-module-list-4-0-6.md) | 104–159 | Litlfred |
| [IHRIS Common Module List (4.0.6)](sections/ihris-common-module-list-4-0-6.md) | 159–187 | Litlfred |
| [IHRIS Ideas List](sections/ihris-ideas-list.md) | 188–191 | Lduncan, Litlfred |
| [IHRIS Manage Form Fields - 4.0](sections/ihris-manage-form-fields-4-0.md) | 192–223 | Litlfred |
| [IHRIS Manage Form Fields - 4.0.7](sections/ihris-manage-form-fields-4-0-7.md) | 223–273 | Litlfred |
| [IHRIS Manage Module List (4.0.6)](sections/ihris-manage-module-list-4-0-6.md) | 273–292 | Litlfred |
| [IHRIS Module List (4.0.6)](sections/ihris-module-list-4-0-6.md) | 293–297 | Litlfred |
| [IHRIS Qualify Form Fields](sections/ihris-qualify-form-fields.md) | 297–324 | Litlfred |
| [IHRIS Qualify Form Fields - 4.0.7](sections/ihris-qualify-form-fields-4-0-7.md) | 325–351 | Litlfred |
| [IHRIS Qualify Module List (4.0.6)](sections/ihris-qualify-module-list-4-0-6.md) | 352–352 | Litlfred |
| [IHRIS Regional Rollout](sections/ihris-regional-rollout.md) | 352–353 | Cbales, Litlfred |
| [IHRIS Role List (4.0.6)](sections/ihris-role-list-4-0-6.md) | 354–355 | Litlfred |
| [IHRIS Suite 4.0 Development](sections/ihris-suite-4-0-development.md) | 355–362 | Lduncan, Litlfred |
| [IHRIS Task List (4.0.6)](sections/ihris-task-list-4-0-6.md) | 362–408 | Litlfred |
| [iHRIS:Data Dictionary (4.0.4)](sections/ihris-data-dictionary-4-0-4.md) | 409–421 | Litlfred |
| [iHRIS:Data Dictionary (4.0.5)](sections/ihris-data-dictionary-4-0-5.md) | 422–434 | Cbales |
| [Installing a Custom Site from Launchpad](sections/installing-a-custom-site-from-launchpad.md) | 435–446 | Litlfred |
| [Installing iHRIS on Ubuntu 10.4 (Lucid)](sections/installing-ihris-on-ubuntu-10-4-lucid.md) | 446–447 | Lduncan, Litlfred |
| [Installing on Mini-Box](sections/installing-on-mini-box.md) | 448–452 | Litlfred, MarkAHershberger |
| [Limiting Forms](sections/limiting-forms.md) | 453–457 | Lduncan, Litlfred, MarkAHershberger |
| [Linking Facilities and Departments](sections/linking-facilities-and-departments.md) | 458–466 | Litlfred |
| [Linux (RedHat-Fedora) Installation](sections/linux-redhat-fedora-installation.md) | 467–471 | Jstrope |
| [Linux (Ubuntu) Installation - 4.0.4](sections/linux-ubuntu-installation-4-0-4.md) | 471–477 | Lduncan |
| [Magic Data Storage Mechanisms](sections/magic-data-storage-mechanisms.md) | 478–478 | Litlfred, MarkAHershberger |
| [Managing A Site In Launchpad](sections/managing-a-site-in-launchpad.md) | 479–482 | Litlfred |
| [Managing Decentralized iHRIS Manage with Launchpad](sections/managing-decentralized-ihris-manage-with-launchpad.md) | 482–483 | Litlfred |
| [Migrating Forms from Entry to MagicData](sections/migrating-forms-from-entry-to-magicdata.md) | 483–485 | Lduncan, MarkAHershberger |
| [Module Structure](sections/module-structure.md) | 485–491 | Lduncan, Litlfred, MarkAHershberger |
| [Pages and Templates](sections/pages-and-templates.md) | 492–497 | Litlfred, MarkAHershberger |
| [Pluggable Authentication](sections/pluggable-authentication.md) | 497–497 | Litlfred |
| [Printed Forms](sections/printed-forms.md) | 497–502 | Lduncan, Litlfred |
| [README File for iHRIS](sections/readme-file-for-ihris.md) | 502–505 | Cbales, Litlfred, Sturlington |
| [Recreate All Form Caches](sections/recreate-all-form-caches.md) | 505–505 | Lduncan, Litlfred |
| [Setting An Establishment](sections/setting-an-establishment.md) | 506–507 | Litlfred |
| [Supporting Software](sections/supporting-software.md) | 507–507 | Litlfred, MarkAHershberger, Sturlington |
| [Swiss Magic Data -- Form Relationships](sections/swiss-magic-data-form-relationships.md) | 508–510 | Litlfred |
| [Swiss Magic Data Editor](sections/swiss-magic-data-editor.md) | 510–512 | Litlfred |
| [Tasks and Roles](sections/tasks-and-roles.md) | 513–516 | Litlfred, MarkAHershberger |
| [Technical Overview: Form Storage -- CSV](sections/technical-overview-form-storage-csv.md) | 516–517 | Litlfred |
| [Technical Overview: Form Storage -- Eval](sections/technical-overview-form-storage-eval.md) | 518–518 | Litlfred |
| [Technical Overview: Form Storage -- SDMX CrossSectional](sections/technical-overview-form-storage-sdmx-crosssectional.md) | 518–519 | Litlfred |
| [Technical Overview: Form Storage -- SDMX-HD](sections/technical-overview-form-storage-sdmx-hd.md) | 520–521 | Lduncan, Litlfred |
| [Technical Overview: Form Storage -- XML](sections/technical-overview-form-storage-xml.md) | 522–523 | Litlfred |
| [TextLayout Tools Module List (4.0.6)](sections/textlayout-tools-module-list-4-0-6.md) | 523–524 | Litlfred |
| [Turn Off Background Processes](sections/turn-off-background-processes.md) | 524–524 | Lduncan, Litlfred |
| [Upgrading From 3.1](sections/upgrading-from-3-1.md) | 525–527 | Lduncan, Litlfred, MarkAHershberger, Mnamutso |
| [Using Bazaar to Contribute Code](sections/using-bazaar-to-contribute-code.md) | 527–530 | Litlfred, Lucaswood, MarkAHershberger |

## Images

| image | page | wiki file | licence stated | contributors |
|---|---|---|---|---|
| [img-p053-1](images/img-p053-1.png) | 53 | `Image:Forms-person-position-map.gif` | unknown | Litlfred |
| [img-p054-1](images/img-p054-1.png) | 54 | `File:screenshot-create-relationship.gif` | unknown | Litlfred |
| [img-p055-1](images/img-p055-1.png) | 55 | `File:Screenshort-join-person-position.gif` | unknown | Litlfred |
| [img-p056-2](images/img-p056-2.png) | 56 | `File:Screenshot-limit-person-position-AND.png` | unknown | Litlfred |
| [img-p056-1](images/img-p056-1.png) | 56 | `File:Screenshot-limit-person-position-FIELDS.png` | unknown | Litlfred |
| [img-p057-2](images/img-p057-2.png) | 57 | `File:Screenshot-limit-person-position-FIELDS2.png` | unknown | Litlfred |
| [img-p057-1](images/img-p057-1.png) | 57 | `File:Screenshot-join-position.png` | unknown | Litlfred |
| [img-p084-2](images/img-p084-2.png) | 84 | `image:export_cadre1.png` | unknown | Litlfred |
| [img-p084-1](images/img-p084-1.png) | 84 | `image:export_cadre2.png` | unknown | Litlfred |
| [img-p448-1](images/img-p448-1.png) | 448 | `Image:Mini-box-ihris-suite.jpg` | unknown | Litlfred |
| [img-p475-1](images/img-p475-1.png) | 475 | `Image:Phpmyadmin_create_user.gif` | unknown | Litlfred |

Credits are matched to images in order of appearance (page, then position on the page). The export lists them in that order, and the counts agree (11 and 11).
