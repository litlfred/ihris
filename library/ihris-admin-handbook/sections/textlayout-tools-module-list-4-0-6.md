---
title: "TextLayout Tools Module List (4.0.6)"
source: http://open.intrahealth.org/w/index.php?oldid=33777
contributors: ["Litlfred"]
pages: 523-524
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# TextLayout Tools Module List (4.0.6)

This is a list of all modules available in version 4.0.6-release of the package TextLayout Tools \[1\]

## tcpdf

This describes version 4.0.0 of the module tcpdf (tcpdf)

- Source: textlayout/modules/tcpdf \[2\]

- Description: This is a wrapper for the tcpdf PDF generation utility
- Requirements:

- I2CE at least 4 and less than 5
- Paths:

- Classes: modules/tcpdf/tcpdf \[3\]

C128AObject, C128BObject, C128CObject, C39Object, I25Object

## textlayout

This describes version 4.0.6 of the module Text Layout (textlayout) It is the top module of this package

- Source: textlayout/ \[4\]

- Description: I2CE Text Layout Tool
- Requirements:

- I2CE at least 4 and less than 5
- tcpdf at least 4.0 and less than 4.1
- Paths:

- Classes: /lib \[5\] ,/tcpdf \[6\]

- I2CE\_Encoding, I2CE\_FontMetric, I2CE\_FontMetricAFM, I2CE\_FontMetricMultiDirection, I2CE\_FontMetricTTF, I2CE\_Hyphen, I2CE\_PDF, I2CE\_TextCell, I2CE\_TextTable, I2CE\_UTF8
- Afm\_path: /CoreFonts \[7\]

- Pdf\_core: /CoreFonts \[7\]

- Ttf\_path: /usr/share/fonts/truetype/\*\* ,/usr/local/share/fonts/truetype/\*\*
- Hyphen\_path: /dicts \[8\] ,/usr/share/myspell/dicts
- Modules: /modules \[9\]

tcpdf

## References

\[1\] https://launchpad.net/textlayout \[2\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head:/modules/tcpdf \[3\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head:/modules/tcpdf/tcpdf \[4\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head:/ \[5\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head://lib \[6\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head://tcpdf \[7\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head://CoreFonts \[8\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head://dicts \[9\] http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.0.6-release/files/head://modules
