---
title: "Enabling Translations"
source: http://open.intrahealth.org/w/index.php?oldid=34882
contributors: ["Litlfred"]
pages: 81-81
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Enabling Translations

## Main Languages

As of version 4.0.6 translations for French, Swahili, Portuguese, and Italian are automatically available to the system. These are called locales..

A locale is a language and country/location. The main locales are:

- French: fr\_FR
- Italian: it\_IT
- Portuguese: pt\_PT
- Swahili: sw\_TZ

## Enabling the Locale Selector Module

- Go to "Configure System"
- Go to "Configure Modules"
- Scroll down to "Pages" and click the "Sub-Modules" link
- Check the checkbox next to "Locale Selector"
- Scroll to the bottom of the screen and click the "Enable" button

## Adding A Locale

- Go to "Configure System"
- Go to "Manage Locales"
- "Add" the locale you want. For example fr\_FR or it\_IT

## Other Languages

Some other languages have only been partially translated and you will need to generate the translations of .html and .xml files. For example, in order to add the locale pt\_BR (Brazilian Portuguese) to the system, you will need to open a terminal on the server and:

```
cd /var/lib/iHRIS/lib/4.0/6/I2CE path may be different depending on your installation
php ../I2CE/tools/translate_templates.php  --locales=pt_BR
cd ../ihris-common
php ../I2CE/tools/translate_templates.php  --locales=pt_BR
cd ../ihris-manage if you are using iHRIS Manage
php ../I2CE/tools/translate_templates.php  --locales=pt_BR
cd ../ihris-qualify if you are using iHRIS Qualify
```

php ../I2CE/tools/translate\_templates.php --locales=pt\_BR
