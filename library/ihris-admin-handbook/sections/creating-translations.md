---
title: "Creating Translations"
source: http://open.intrahealth.org/w/index.php?oldid=32927
contributors: ["Lduncan", "Litlfred", "MarkAHershberger"]
pages: 48-50
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Creating Translations

If you update an .xml for .html file that needs to be translated, you need to update the .pot file for the module that contains that file. You may do so by running:

```
<PATH_TO_I2CE>/tools/translate_create_templates.php
```

from the top-level directory of the package. This should be done before commit to bzr. Supposedly, launchpad will watch the .pot files and update the translations available on launchpad.

## Creating the POT Files For Launchpad Upload

There are two scripts. The first creates all the .pot files and any necessary localized module configuration files. The .pot files are stored under translations/templates and the module confguration file is stored under &lt;MODULE\_DIR&gt;/configs/en\_US.

Once you are satisfied with the results you create the tarball to upload to launchpad. Hopefully, you don't need to do this step any more as the translation setting for i2ce, ihris-common, ihris-manage, ihris-qualify have been updated to pull in .pot files from the trunk branches.

### translate\_create\_templates.php

There is a utility to create .POT \[1\] translation template files to upload to launchpad. The utility creates a .pot file for each module in a package (such as I2CE, ihris-common, ihris-manage, etc) and is found in the I2CE package under:

```
i2ce/tools/translate_create_templates.php
```

It should be the run in the top-level directory &lt;DIR&gt; of a package. The usage as of version 4.0.0:

```
cd <DIR>
```

&lt;I2CE\_DIRECTORY&gt;/tools/translate\_create\_templates.php --help

```
Usage: translate_create_templates.php
  [--template_dir=$template_dir]: The directory to store .pot template files in
    If not set, we use ./translations/templates
  [--remove-strings=T/F] set to true to always remove the string from a module's .pot
    which are no longer present in the module
  [--modules=$module1,$module2..$moduleN]: The module(s) for which we wish  to operate on
    If not specified, it uses  every valid module
  [--search_dirs=$dir1,$dir2]: Set the search directories for modules
    If not specified, we search <DIR>,<DIR>/sites/*
  [--limit_search=T/F]: Limit the module search results of found sub-modules of a top-level
    Defaults to T.
  [--categories=$cat1,$cat2]: The categories to search
    If not specificed we search TEMPLATES
  [--create-configs=T/F]  set to true to always create ./configs
    directory and add to to config.xml if there are translatable strings.
  [--overwrite-configs=T/F] set to true to always overwrite the translated
    config.xml
```

### create\_launchpad\_upload.php

This should no longer be needed for ihris-XXX and i2ce as Launchpad is now configured to watch for .pot files. I'll leave it around in case someone else wants to use it.

Creates the tarball needed to upload into launchpad.

It should be the run in the top-level directory &lt;DIR&gt; of a package.

Looks for .pot files in translations/templates/

Creates the file translations/templates/lauchpad/templates-&lt;PACKAGE&gt;.tgz

It tells you where to upload the file in lauchpad.

Usage as of 4.0.0

```
Usage: translate_create_templates.php
  [--modules=$module1,$module2..$moduleN]: The module(s) for which we wish  to operate on
    If not specified, it uses  every valid module
  [--search_dirs=$dir1,$dir2]: Set the search directories for modules
    If not specified, we search <DIR>,<DIR>/sites/*
  [--limit_search=T/F]: Limit the module search results of found sub-modules of a top-level
    Defaults to T.
```

## Downloading The Translations

You can download the translation at the following links:

- https://translations.launchpad.net/i2ce/trunk/+export
- https://translations.launchpad.net/ihris-common/trunk/+export
- https://translations.launchpad.net/ihris-manage/trunk/+export
- https://translations.launchpad.net/ihris-qualify/trunk/+export

Select to download the .MO files (and not the .PO files).

Wait a long time to get the e-mail. The emailed file should be saved under:

```
<PACKAGE_DIR>/translations/launchpad-export.tar.gz
```

## translate\_templates.php

The utility translate\_templates.php is found under i2ce/tools and should be run from the top-level directory &lt;PACKAGE\_DIR&gt; of the package. It create the translated html template files and configuration files.

Usage for Version 4.0.4

```
 Usage: translate_templates.php
  [--read_po_files=$read_po_files]: Tries to read .po files for the given locale rather than an export
     Defaults to false
  [--templates_dir=$read_po_files]: Where  to read .po files from
     Defaults to $templates_dir
  [--archive=$archive]: The archive consisting of all translationd
     Defaults to ./translations/launchpad-export.tar.gz
  [--locales=$locale1,$locale2..$localeN]: The locales we wish to translate for
     If not specified, it uses  every valid subdirectory of in the translations archive file
  [--only_changed=T/F]: produce tranlslated files only when something was translated from the source document.
     Defaults to T=true
  [--only_archive=T/F]: Only create the archive -- do not recreate template files.
     Defaults to F
  [--create_archive=T/F]: generate the tarball and debian packaging info.
     If F, it output translated files within each e module as approriate.
     If T (default), it outputs archive under ./translations/archive/ with a sub-directory for each locale
  [--archive_dir=$archive_dir]: The directory to store  archive in.
     Defaults to ./translations/archive/
  [--categories=$cat1,$cat2]: The categories to search
     If not specificed we search TEMPLATES
  [--modules=$module1,$module2..$moduleN]: The module(s) for which we wish  to operate on
     If not specified, it uses  every valid module
  [--search_dirs=$dir1,$dir2]: Set the search directories for modules
    If not specified, we search <PACKAGE_DIR>,<PACKAGE_DIR>/sites/*
  [--limit_search=T/F]: Limit the module search results of found sub-modules of a
    top-level module to those that are real subdirectories of top-level's given directory
    Defaults to T.
```

## Translation from .po files

As languages become completely translated, we will maintain the .po files in the source code. In this case you do not need to download the launchpad exports. This is the case, for example, with French. Translation now is easier as you do not need to wait on downloading from launchpad:

```
translate_templates.php --create_archive=false --read_po_files=true --locales=fr
```

in &lt;PACKAGE\_DIR&gt; will produce the French translations in the source tree for use

Note: under version 4.0.6 the defaults for translate\_templates.php have been changed, so you may simply do:

```
translate_templates.php  --locales=fr
```

## Packaging Translations

Download the launchpad translations as indicated above. Running

```
translate_templates.php  --create_archive=true
```

in &lt;PACKAGE\_DIR&gt; will produce translation/archive directory

## References

\[1\] http://en.wikipedia.org/wiki/GNU\_gettext
