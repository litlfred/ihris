---
title: "I2CE Module List (4.0.6)"
source: http://open.intrahealth.org/w/index.php?oldid=33765
contributors: ["Litlfred"]
pages: 104-159
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# I2CE Module List (4.0.6)

This is a list of all modules available in version 4.0.6-release of the package I2CE \[1\]

## BackgroundProcess

This describes version 4.0.0 of the module Background Processes (BackgroundProcess)

- Source: i2ce/modules/BackgroundProcess \[2\]

- Module Class: The module class is implemented by I2CE\_BackgroundProcess
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;launchBackgroundProcess() via launchBackgroundProcess()
- Implements the method I2CE\_Module-&gt;launchBackgroundProcess() via launchBackgroundProcess()
- Implements the method I2CE\_Template-&gt;launchBackgroundProcess() via launchBackgroundProcess()
- Implements the method I2CE\_Page-&gt;launchBackgroundPHPScript() via launchBackgroundPHPScript()
- Implements the method I2CE\_Module-&gt;launchBackgroundPHPScript() via launchBackgroundPHPScript()
- Implements the method I2CE\_Template-&gt;launchBackgroundPHPScript() via launchBackgroundPHPScript()
- Implements the method I2CE\_Page-&gt;launchBackgroundPage() via launchBackgroundPage()
- Implements the method I2CE\_Module-&gt;launchBackgroundPage() via launchBackgroundPage()
- Implements the method I2CE\_Template-&gt;launchBackgroundPage() via launchBackgroundPage()
- Description: A convenience module to allow the running of process in the background
- Requirements:

- pages at least 4.0 and less than 4.1
- Paths:

- Configs: modules/BackgroundProcess/configs \[3\]

- Templates: modules/BackgroundProcess/templates \[4\]

- background\_process\_menu.html
- Css: modules/BackgroundProcess/css \[5\]

- Classes: modules/BackgroundProcess/ \[6\]

I2CE\_BackgroundProcess, I2CE\_Page\_BackgroundProcess, I2CE\_Page\_Run\_SQL

## BinField

This describes version 4.0.6.0 of the module Binary Fields (BinField)

- Source: i2ce/modules/Forms/modules/Binary\_Files \[7\]

- Module Class: The module class is implemented by I2CE\_Module\_BinaryFiles
- Description: A module that allows binary files for form fields
- Requirements:

- forms at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- MimeTypes at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/Binary\_Files/lib \[8\]

- I2CE\_FormField\_BINARY\_FILE, I2CE\_FormField\_DB\_BLOB, I2CE\_FormField\_DOCUMENT, I2CE\_FormField\_IMAGE, I2CE\_Module\_BinaryFiles, I2CE\_Page\_BinaryField
- Sql: modules/Forms/modules/Binary\_Files/sql \[9\]

## CachedForms

This describes version 4.0.6.1 of the module Cached Forms (CachedForms)

- Source: i2ce/modules/Forms/modules/CachedForms \[10\]

- Module Class: The module class is implemented by I2CE\_Module\_CachedForms
- Fuzzy Methods:

- Implements the method I2CE\_FormField-&gt;cachedTableReference() via cachedTableReference()
- Command Line Inteterprecter (CLI) Fuzzy Methods:

- Implements the CLI method I2CE\_FormField-&gt;cachedTableReference() via cachedTableReference()
- Description: A module that allow the creation of a cached table corresponding to a form
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- BackgroundProcess at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/CachedForms/configs \[11\]

- Classes: modules/Forms/modules/CachedForms/lib \[12\]

- I2CE\_CachedForm, I2CE\_Module\_CachedForms, I2CE\_Page\_CachedForm
- Templates: modules/Forms/modules/CachedForms/templates \[13\]

cachedforms\_menu\_each.html, cachedforms\_menu.html, cachedforms\_menu\_exportProfile.html, cachedforms\_menu\_exportProfile\_each.html

## ColorPicker

This describes version 4.0.0 of the module Color Picker (ColorPicker)

- Source: i2ce/modules/MooTools/modules/ColorPicker \[14\]

- Module Class: The module class is implemented by I2CE\_Module\_ColorPicker
- Fuzzy Methods:

- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_triple\_hex\_single() via processValues\_color\_triple\_hex\_single()
- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_triple\_hex\_many() via processValues\_color\_triple\_hex\_many()
- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_triple\_rgb\_single() via processValues\_color\_triple\_rgb\_single()
- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_triple\_rgb\_many() via processValues\_color\_triple\_rgb\_many()
- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_hex\_single() via processValues\_color\_hex\_single()
- Implements the method I2CE\_MagicDataTemplate-&gt;processValues\_color\_hex\_many() via processValues\_color\_hex\_many()
- Implements the method I2CE\_Page-&gt;addColorPickerTriple() via addColorPickerTriple()
- Implements the method I2CE\_Template-&gt;addColorPickerTriple() via addColorPickerTriple()
- Description: Uses the MooTools Color Picker written by Kelly Anderson at http://www.sweetvision.com/projects/javascript-color-picker/.Enable some additional functionality for configuration as well
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MooTools/modules/ColorPicker/scripts \[15\]

- Templates: modules/MooTools/modules/ColorPicker/templates \[16\]

- configuration\_color\_triple\_hex\_single.html, configuration\_color\_triple\_single.html, configuration\_color\_triple\_rgb\_single.html
- Css: modules/MooTools/modules/ColorPicker/css \[17\]

- Classes: modules/MooTools/modules/ColorPicker/ \[18\]

I2CE\_Module\_ColorPicker

## CustomReports

This describes version 4.0.5 of the module Custom Reports (CustomReports)

- Source: i2ce/modules/CustomReports \[19\]

- Module Class: The module class is implemented by I2CE\_Module\_CustomReports
- Fuzzy Methods:

- Implements the method I2CE\_Form-&gt;isNumeric() via isNumeric()
- Implements the method I2CE\_FormField-&gt;isNumeric() via isNumericField()
- Description: Custom Reports
- Requirements:

- pages at least 4.0 and less than 4.1
- formRelationships at least 4.0 and less than 4.1

- magicDataExport at least 4.0 and less than 4.1
- CachedForms at least 4.0 and less than 4.1
- jumper at least 4.0 and less than 4.1
- Paths:

- Configs: modules/CustomReports/configs \[20\]

- Classes: modules/CustomReports/lib \[21\]

- I2CE\_CustomReport, I2CE\_CustomReport\_Display, I2CE\_CustomReport\_Display\_Default, I2CE\_CustomReport\_Template, I2CE\_Module\_CustomReports, I2CE\_Page\_CustomReports, I2CE\_Page\_Report\_MagicDataExport, I2CE\_Swiss\_CustomReports\_Base, I2CE\_Swiss\_CustomReports\_Report, I2CE\_Swiss\_CustomReports\_ReportView, I2CE\_Swiss\_CustomReports\_ReportView\_Base, I2CE\_Swiss\_CustomReports\_ReportView\_Displays, I2CE\_Swiss\_CustomReports\_ReportView\_Field, I2CE\_Swiss\_CustomReports\_ReportView\_Fields, I2CE\_Swiss\_CustomReports\_ReportViews, I2CE\_Swiss\_CustomReports\_Report\_Base, I2CE\_Swiss\_CustomReports\_Report\_Meta, I2CE\_Swiss\_CustomReports\_Report\_ReportingForm, I2CE\_Swiss\_CustomReports\_Report\_ReportingForm\_Field, I2CE\_Swiss\_CustomReports\_Report\_ReportingForm\_Field\_Limit, I2CE\_Swiss\_CustomReports\_Report\_ReportingForm\_Field\_Limits, I2CE\_Swiss\_CustomReports\_Report\_ReportingForm\_Fields, I2CE\_Swiss\_CustomReports\_Report\_ReportingForms, I2CE\_Swiss\_CustomReports\_Report\_ReportingFunction, I2CE\_Swiss\_CustomReports\_Report\_ReportingFunction\_Limits, I2CE\_Swiss\_CustomReports\_Report\_ReportingFunctions, I2CE\_Swiss\_CustomReports\_Reports
- Css: modules/CustomReports/css \[22\]

- Images: modules/CustomReports/images \[23\]

- Templates: modules/CustomReports/templates \[24\]

customReports\_reportViews\_existing\_reportview.html, customReports\_report\_limits\_each.html, customReports\_report\_form\_field.html, customReports\_reportViews\_edit.html, customReports\_menu.html, customReports\_report\_form\_field\_limit.html, customReports\_report\_forms\_each.html, customReports\_table\_data\_cell.html, customReports\_reportViews\_reports\_view.html, customReports\_report\_form.html, customReports\_display\_Default\_base.html, customReports\_reportView\_displays\_each.html, customReports\_reportView\_field\_numeric.html, customReports\_reportView\_displays.html, customReports\_reports\_no\_new.html, customReports\_table\_data\_row.html, customReports\_table.html, customReports\_reportView\_edit.html, customReports\_reports\_category.html, customReports\_table\_link\_cell.html, customReports\_report\_form\_fields.html, customReports\_reportView\_fields.html, customReports\_report\_functions\_each.html, customReports\_reportViews\_views\_each\_view.html, customReports\_reportView\_view.html, customReports\_report\_forms\_form.html, customReports\_report\_meta.html, customReports\_table\_head\_cell.html, customReports\_report\_limits.html, customreports\_options.html, customReports\_report\_function.html, customReports\_reportViews\_reports\_edit.html, customReports\_nav\_menu.html, customReports\_report\_functions.html, customReports\_reportViews\_views\_each\_edit.html, customReports\_notfound.html, customReports\_reportView\_field.html, customReports\_reports\_new.html, customReports\_reportView\_fields\_each.html, customReports\_report\_forms.html, customReports\_reportViews\_views\_view.html, customReports\_report\_form\_fields\_each.html, customReports\_reports\_categories.html, customReports\_reports\_category\_report.html, customReports\_report.html, customReports\_reportViews\_views\_edit.html, customReports\_reports.html, customReports\_reportViews\_view.html, customReports\_display\_control\_Default.html

- Xml: modules/CustomReports/xml \[25\]

- Modules: modules/CustomReports/modules \[26\]

CustomReports\_Export, CustomReports\_PDF, CustomReports\_PieChart, ReportArchiver

## CustomReports\_Export

This describes version 4.0.6.1 of the module Export Reports (CustomReports\_Export)

- Source: i2ce/modules/CustomReports/modules/Export \[27\]

- Description: Configuration options for exported reports
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Paths:

- Templates: modules/CustomReports/modules/Export/templates \[28\]

- swiss\_xslt.html, swiss\_xslts.html, swiss\_xslts\_each.html, customReports\_display\_control\_Export.html, swiss\_exporteditor.html
- Classes: modules/CustomReports/modules/Export/lib \[29\]

I2CE\_CustomReport\_Display\_Export, I2CE\_Swiss\_CustomReport\_ReportView\_ExportEditor, I2CE\_Swiss\_XSLT, I2CE\_Swiss\_XSLTS

## CustomReports\_PDF

This describes version 4.0.0 of the module PDF Reports (CustomReports\_PDF)

- Source: i2ce/modules/CustomReports/modules/PDF \[30\]

- Description: Configuration options for reports that use PDF
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- textlayout at least 4.0 and less than 4.1
- ColorPicker at least 4.0 and less than 4.1
- Paths:

- Templates: modules/CustomReports/modules/PDF/templates \[31\]

- customReports\_display\_control\_PDF.html
- Classes: modules/CustomReports/modules/PDF/lib \[32\]

I2CE\_CustomReport\_Display\_PDF

## CustomReports\_PieChart

This describes version 4.0.5.0 of the module Pie and Chart (CustomReports\_PieChart)

- Source: i2ce/modules/CustomReports/modules/PieChart \[33\]

- Description: Configuration options for reports that use Pie and Charts
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- ColorPicker at least 4.0 and less than 4.1
- maani-charts at least 4.7
- Paths:

- Configs: modules/CustomReports/modules/PieChart/configs \[34\]

- Templates: modules/CustomReports/modules/PieChart/templates \[35\]

customReports\_display\_control\_PieChart.html, customReports\_display\_PieChart\_base.html

- Classes: modules/CustomReports/modules/PieChart/lib \[36\]

- I2CE\_CustomReport\_Display\_PieChart
- Css: modules/CustomReports/modules/PieChart/css \[37\]

## DatePicker

This describes version 1.16 of the module Date Picker (DatePicker)

- Source: i2ce/modules/MooTools/modules/DatePicker \[38\]

- Module Class: The module class is implemented by I2CE\_Module\_DatePicker
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;addDatePicker() via addDatePicker()
- Implements the method I2CE\_Template-&gt;addDatePicker() via addDatePicker()
- Description: Uses the MooTools Color Date http://www.monkeyphysics.com/mootools/script/2/datepicker
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MooTools/modules/DatePicker/scripts \[39\]

- Css: modules/MooTools/modules/DatePicker/css \[40\]

- Classes: modules/MooTools/modules/DatePicker/ \[41\]

I2CE\_Module\_DatePicker

## DisplayData

This describes version 4.0.0 of the module I2CE Display Data (DisplayData)

- Source: i2ce/modules/TemplateData/modules/DisplayData \[42\]

- Module Class: The module class is implemented by I2CE\_DisplayData
- Fuzzy Methods:

- Implements the method I2CE\_Template-&gt;setDisplayData() via setDisplayData()
- Implements the method I2CE\_Template-&gt;setDisplayDataImmediate() via setDisplayDataImmediate()
- Implements the method I2CE\_Template-&gt;selectOptionsImmediate() via selectOptionsImmediate()
- Implements the method I2CE\_Page-&gt;selectOptionsImmediate() via selectOptionsImmediate()
- Implements the method I2CE\_Page-&gt;setDisplayData() via setDisplayData()
- Implements the method I2CE\_Page-&gt;setDisplayDataImmediate() via setDisplayDataImmediate()
- Description: Adds display data to the template
- Requirements:

- I2CE at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- Paths:

- Classes: modules/TemplateData/modules/DisplayData/ \[43\]

I2CE\_DisplayData

## Fields

This describes version 4.0.6 of the module I2CE Fields (Fields)

- Source: i2ce/modules/Forms/modules/Fields \[44\]

- Module Class: The module class is implemented by I2CE\_Module\_Fields
- Description: Adds a few basic forms to the system as well as some form functionality to the template
- Requirements:

- I2CE at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- DisplayData at least 4.0 and less than 4.1
- Optionally Enables: DatePicker
- Paths:

- Configs: modules/Forms/modules/Fields/configs \[45\]

- Classes: modules/Forms/modules/Fields/lib \[46\] ,modules/Forms/modules/Fields/lib/fields \[47\]

- I2CE\_Entry, I2CE\_FieldContainer, I2CE\_FieldContainer\_Factory, I2CE\_FormField, I2CE\_FormField\_BOOL, I2CE\_FormField\_DATE\_HMS, I2CE\_FormField\_DATE\_MD, I2CE\_FormField\_DATE\_TIME, I2CE\_FormField\_DATE\_Y, I2CE\_FormField\_DATE\_YMD, I2CE\_FormField\_DB\_DATE, I2CE\_FormField\_DB\_INT, I2CE\_FormField\_DB\_STRING, I2CE\_FormField\_DB\_TEXT, I2CE\_FormField\_INT, I2CE\_FormField\_INT\_GENERATE, I2CE\_FormField\_INT\_LIST, I2CE\_FormField\_STRING\_LINE, I2CE\_FormField\_STRING\_MLINE, I2CE\_FormField\_STRING\_PASS, I2CE\_FormField\_STRING\_TEXT, I2CE\_FormField\_YESNO, I2CE\_Module\_Fields
- Templates: modules/Forms/modules/Fields/templates \[48\]

- form\_field.html, display\_field.html, simple\_display\_field.html
- Scripts: modules/Forms/modules/Fields/scripts \[49\]

- Modules: modules/Forms/modules/Fields/modules \[50\]

## FileDump

This describes version 4.0.0 of the module File Dump (FileDump)

- Source: i2ce/modules/Pages/modules/FileDump \[51\]

- Description: File Download Utility
- Requirements:

- MimeTypes at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Pages/modules/FileDump/configs \[52\]

- Classes: modules/Pages/modules/FileDump/ \[53\]

I2CE\_FileDump

## Float

This describes version 4.0.0 of the module Float (Float)

- Source: i2ce/modules/Forms/modules/Float \[54\]

- Module Class: The module class is implemented by I2CE\_Module\_Float
- Description: A module that allows the float formfield
- Requirements:

- forms at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/Float/lib \[55\]

I2CE\_FormField\_DB\_FLOAT, I2CE\_FormField\_FLOAT, I2CE\_Module\_Float

## FormWorm

This describes version 4.0.0 of the module Form Worm (FormWorm)

- Source: i2ce/modules/MooTools/modules/FormWorm \[56\]

- Module Class: The module class is implemented by I2CE\_Module\_FormWorm
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;addFormWorm() via addFormWorm()
- Implements the method I2CE\_Template-&gt;addFormWorm() via addFormWorm()
- Description: A collection of javascript utilities to handle form verification and submission of forms with multiple actions
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools-I2CE at least 4.0 and less than 4.1
- Paths:

- Scripts: modules/MooTools/modules/FormWorm/scripts \[57\]

- Css: modules/MooTools/modules/FormWorm/css \[58\]

- Classes: modules/MooTools/modules/FormWorm/ \[59\]

I2CE\_Module\_FormWorm

## I2CE

This describes version 4.0.6.0 of the module I2CE Basic System (I2CE) It is the top module of this package

- Source: i2ce/ \[60\]

- Module Class: The module class is implemented by I2CE\_Module\_Core
- Description: The I2CE Core System Configuration
- Paths:

- Misc: /I2CE\_config.inc.php \[61\] ,/I2CE\_structure.sql \[62\]

- Classes: /lib \[63\]

I2CE, I2CE\_Configurator, I2CE\_Date, I2CE\_Dumper, I2CE\_FileSearch, I2CE\_FileSearch\_Caching, I2CE\_Fuzzy, I2CE\_Locales, I2CE\_MagicData, I2CE\_MagicDataNode, I2CE\_MagicDataStorage, I2CE\_MagicDataStorageAPC, I2CE\_MagicDataStorageDB, I2CE\_MagicDataStorageDBAlt, I2CE\_MagicDataStorageMem, I2CE\_MagicDataStorageMemcached, I2CE\_MagicDataStorageMongoDB, I2CE\_MagicDataTemplate, I2CE\_Module, I2CE\_ModuleFactory, I2CE\_Module\_Core, I2CE\_Process, I2CE\_TemplateMeister, I2CE\_Updater, I2CE\_UserAccess\_Mechanism, I2CE\_Util, I2CE\_Validate, I2CE\_Error, I2CE\_Error

- Modules: /modules \[64\]

- BackgroundProcess, CustomReports, ImportExport, MimeTypes, MooTools, Timer, YAML\_spyc, forms, jumper, maani-charts, magicDataExport, messageHandler, pages, swissfactory, template-data, user
- Scripts: /scripts \[65\]

- Sql: /sql \[66\]

## ImportExport

This describes version 0.9 of the module Import Export Support (ImportExport)

- Source: i2ce/modules/ImportExport \[67\]

- Module Class: The module class is implemented by I2CE\_Import\_Export
- Description: Enables an XML Import and Export tool which allows offline access.
- Paths:

- Sql: modules/ImportExport/sql \[68\]

- Classes: modules/ImportExport/lib \[69\]

I2CE\_Import\_Export

## Lists

This describes version 4.0.6.1 of the module Form Lists (Lists)

- Source: i2ce/modules/Forms/modules/Lists \[70\]

- Module Class: The module class is implemented by I2CE\_Module\_Lists
- Description: Database Lists
- Requirements:

- forms at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1
- TreeSelect at least 4.0 and less than 4.1
- jumper at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/Lists/configs \[71\]

- Classes: modules/Forms/modules/Lists/lib \[72\]

- I2CE\_FormField\_MAP, I2CE\_FormField\_MAPPED, I2CE\_FormField\_MAP\_MULT, I2CE\_List, I2CE\_Module\_Lists, I2CE\_PageFormLists, I2CE\_PageViewList, I2CE\_SimpleList
- Templates: modules/Forms/modules/Lists/templates \[73\]

- lists\_type\_header.html, lists\_form\_simple.html, button\_confirm\_admin.html, lists\_type\_list.html, lists\_type\_select.html, lists\_type\_dual\_row.html, lists\_type\_row.html, view\_list.html, lists\_type\_mapped.html, menu\_view.html, lists\_type\_dual.html, lists\_type\_mapped\_default.html, lists\_form\_base.html, view\_list\_simple.html
- Sql: modules/Forms/modules/Lists/sql \[74\]

- Modules: modules/Forms/modules/Lists/modules \[75\]

Lists-LinkTo

## Lists-LinkTo

This describes version 4.0.5.0 of the module List Link to Data (Lists-LinkTo)

- Source: i2ce/modules/Forms/modules/Lists/modules/ListLink \[76\]

- Description: Lists that are linked to other data. This module is meant to be extended to defined what type of data this list links to. You can extend the I2CE\_ListLink class to add new fields to link to. Alone this class doesn't do much.
- Requirements:

- Lists at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/Lists/modules/ListLink/configs \[77\]

- Modules: modules/Forms/modules/Lists/modules/ListLink/modules \[78\]

- Lists-LinkTo-List, Lists-LinkTo-String
- Classes: modules/Forms/modules/Lists/modules/ListLink/ \[79\]

## Lists-LinkTo-List

This describes version 4.0.5.0 of the module List Link to List (Lists-LinkTo-List)

- Source: i2ce/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList \[80\]

- Description: Lists that are linked to another list form. Multiple forms are defined here that can be used to link lists to other lists for different storage mechanisms. You must enable the required form storage module yourself to avoid extra modules being loaded. You should use the same form storage that is used for the List form you're linking. Certain storage mechanisms may need extra storage options defined.
- Requirements:

- forms-storage-CSV at least 4.0 and less than 4.1
- forms-storage-flat at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1
- Lists-LinkTo at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/configs \[81\]

- Classes: modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/ \[82\]

## Lists-LinkTo-String

This describes version 4.0.5.0 of the module List Link to String (Lists-LinkTo-String)

- Source: i2ce/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString \[83\]

- Description: Lists that are linked to a string (id). Multiple forms are defined here that can be used to link lists to strings for different storage mechanisms. You must enable the required form storage module yourself to avoid extra modules being loaded. You should use the same form storage that is used for the List form you're linking. Certain storage mechanisms may need extra storage options defined.
- Requirements:

- Lists-LinkTo at least 4.0 and less than 4.1
- forms-storage-CSV at least 4.0 and less than 4.1
- forms-storage-flat at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1

- Paths:

- Configs: modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/configs \[84\]

- Classes: modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/ \[85\]

## LocaleForm

This describes version 4.0.3.7 of the module Locale Form (LocaleForm)

- Source: i2ce/modules/Forms/modules/LocaleForm \[86\]

- Description:
- Requirements:

- forms at least 4.0 and less than 4.1
- forms-storage-eval at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/LocaleForm/configs \[87\]

- Classes: modules/Forms/modules/LocaleForm/ \[88\]

## LoginPage

This describes version 4.0.0 of the module Login Page (LoginPage)

- Source: i2ce/modules/Pages/modules/Login \[89\]

- Module Class: The module class is implemented by I2CE\_Module\_Login
- Fuzzy Methods:

- Implements the method I2CE\_Wrangler-&gt;manipulateWrangler\_I2CE\_logout() via manipulateWrangler()
- Description: The login Page
- Requirements:

- pages at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Pages/modules/Login/configs \[90\]

- Css: modules/Pages/modules/Login/css \[91\]

- Classes: modules/Pages/modules/Login/lib \[92\]

- I2CE\_Module\_Login, I2CE\_PageFeedback, I2CE\_PageForgot, I2CE\_PageLogin, I2CE\_PageLogout, I2CE\_PagePassword
- Templates: modules/Pages/modules/Login/templates \[93\]

password\_wrong.html, login.html, password\_cant\_change.html, password.html, forgot.html, feedback.html, password\_none.html, password\_form.html, feedback\_thanks.html, password\_no\_match.html, feedback\_form.html, password\_success.html

## MimeTypes

This describes version 4.0.0.1 of the module Mime Types (MimeTypes)

- Source: i2ce/modules/MimeTypes \[94\]

- Description: Adds a in mime type capabilities
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Paths:

- Configs: modules/MimeTypes/configs \[95\]

- Classes: modules/MimeTypes/lib \[96\]

- I2CE\_MimeTypes
- Mime: modules/MimeTypes/mime \[97\]

## MooTools

This describes version 1.2.4 of the module MooTools (MooTools)

- Source: i2ce/modules/MooTools \[98\]

- Description: MooTools javascript library
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Paths:

- Scripts: modules/MooTools/scripts \[99\]

- Modules: modules/MooTools/modules \[100\]

- ColorPicker, DatePicker, FormWorm, MooTools-I2CE, StretchPage, TreeSelect, fancyDebug, menu\_select
- Classes: modules/MooTools/ \[101\]

I2CE\_MootoolsCore, I2CE\_Module\_Debugging, I2CE\_Module\_MenuSelect, I2CE\_Module\_StretchPage, I2CE\_Module\_TreeSelect

## MooTools-I2CE

This describes version 4.0.0 of the module I2CE Library (MooTools-I2CE)

- Source: i2ce/modules/MooTools/modules/Core \[102\]

- Module Class: The module class is implemented by I2CE\_MootoolsCore
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;getClassValue() via getClassValue()
- Implements the method I2CE\_Template-&gt;getClassValue() via getClassValue()
- Implements the method I2CE\_Page-&gt;loadClassValues() via loadClassValues()
- Implements the method I2CE\_Template-&gt;loadClassValues() via loadClassValues()
- Implements the method I2CE\_Page-&gt;setClassValue() via setClassValue()
- Implements the method I2CE\_Template-&gt;setClassValue() via setClassValue()
- Implements the method I2CE\_Page-&gt;setClassValues() via setClassValues()
- Implements the method I2CE\_Template-&gt;setClassValues() via setClassValues()
- Description: I2CE MooTools core library
- Requirements:

- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MooTools/modules/Core/scripts \[103\]

- Css: modules/MooTools/modules/Core/css \[104\]

- Classes: modules/MooTools/modules/Core/ \[105\]

## Options

This describes version 4.0.0 of the module I2CE Options Data (Options)

- Source: i2ce/modules/TemplateData/modules/Options \[106\]

- Module Class: The module class is implemented by I2CE\_Template\_Options
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;addOption() via addOption()
- Implements the method I2CE\_Template-&gt;addOption() via addOption()
- Implements the method I2CE\_Page-&gt;addOptions() via addOptions()
- Implements the method I2CE\_Template-&gt;addOptions() via addOptions()
- Description: Adds options data to the template
- Requirements:

- I2CE at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- Paths:

- Classes: modules/TemplateData/modules/Options/ \[107\]

I2CE\_Template\_Options

## PrintedForms

This describes version 4.0.5.6 of the module Printed Forms (PrintedForms)

- Source: i2ce/modules/Forms/modules/PrintedForms \[108\]

- Module Class: The module class is implemented by I2CE\_Module\_PrintedForms
- Description: Engine used to generated standard printed forms from a form relationship
- Requirements:

- pages at least 4.0 and less than 4.1
- formRelationships at least 4.0 and less than 4.1
- textlayout at least 4.0 and less than 4.1
- Optionally Enables: BinField
- Paths:

- Configs: modules/Forms/modules/PrintedForms/configs \[109\]

- Classes: modules/Forms/modules/PrintedForms/lib \[110\]

- I2CE\_Module\_PrintedForms, I2CE\_Page\_PrintedForms, I2CE\_PrintedForm\_Render, I2CE\_PrintedForm\_Render\_PDF
- Images: modules/Forms/modules/PrintedForms/images \[111\]

- Templates: modules/Forms/modules/PrintedForms/templates \[112\]

printed\_forms\_menu\_archive\_each.html, printed\_forms\_menu\_each.html, printed\_forms\_menu.html

## ReportArchiver

This describes version 4.0.6.5 of the module Custom Reports Archiver (ReportArchiver)

- Source: i2ce/modules/CustomReports/modules/ReportArchiver \[113\]

- Module Class: The module class is implemented by I2CE\_Module\_ReportArchiver
- Description: Custom Reports
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- CustomReports\_Export at least 4.0 and less than 4.1
- BinField at least 4.0 and less than 4.1
- Paths:

- Configs: modules/CustomReports/modules/ReportArchiver/configs \[114\]

- Classes: modules/CustomReports/modules/ReportArchiver/lib \[115\]

- I2CE\_Module\_ReportArchiver, I2CE\_Page\_ArchiveReport, I2CE\_Page\_CustomReport\_ArchiveMenu
- Templates: modules/CustomReports/modules/ReportArchiver/templates \[116\]

reportArchive\_menu.html, archiveReports\_menu.html

## StretchPage

This describes version 4.0.0 of the module Page Stretcher (StretchPage)

- Source: i2ce/modules/MooTools/modules/StretchPage \[117\]

- Module Class: The module class is implemented by I2CE\_Module\_StretchPage
- Description: Makes sure that the page is at least as high as the browser window. Use bad adding a div with id='StretchPage' to the containing element that you want stretched.
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Classes: modules/MooTools/modules/StretchPage/lib \[118\]

- Scripts: modules/MooTools/modules/StretchPage/scripts \[119\]

- Css: modules/MooTools/modules/StretchPage/css \[120\]

## Tags

This describes version 4.0.0 of the module Tags (Tags)

- Source: i2ce/modules/TemplateData/modules/Tags \[121\]

- Module Class: The module class is implemented by I2CE\_Module\_Tags
- Description: Adds module and script tag processing to the template
- Requirements:

- I2CE at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- DisplayData at least 4.0 and less than 4.1
- Paths:

- Classes: modules/TemplateData/modules/Tags/ \[122\]

I2CE\_Module\_Tags, I2CE\_PluralForms

## Timer

This describes version 4.0.0 of the module I2CE Timer (Timer)

- Source: i2ce/modules/Timer \[123\]

- Module Class: The module class is implemented by I2CE\_Timer
- Description: Adds a timer class
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Timer/configs \[124\]

- Classes: modules/Timer/ \[125\]

I2CE\_Timer

## TreeSelect

This describes version 4.0.0 of the module Tree Select (TreeSelect)

- Source: i2ce/modules/MooTools/modules/TreeSelect \[126\]

- Module Class: The module class is implemented by I2CE\_Module\_TreeSelect
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;addAutoCompleteInputTreeById() via addAutoCompleteInputTreeById()
- Implements the method I2CE\_Template-&gt;addAutoCompleteInputTreeById() via addAutoCompleteInputTreeById()
- Implements the method I2CE\_Page-&gt;addAutoCompleteInputTree() via addAutoCompleteInputTree()
- Implements the method I2CE\_Template-&gt;addAutoCompleteInputTree() via addAutoCompleteInputTree()
- Description: Tree Select
- Requirements:

- MooTools-I2CE at least 4.0 and less than 4.1
- Paths:

- Scripts: modules/MooTools/modules/TreeSelect/scripts \[127\]

- Css: modules/MooTools/modules/TreeSelect/css \[128\]

- Classes: modules/MooTools/modules/TreeSelect/ \[129\]

## UserAccess

This describes version 4.0.0 of the module User (UserAccess)

- Source: i2ce/modules/User/modules/UserAccess \[130\]

- Module Class: The module class is implemented by I2CE\_Module\_UserAccess
- Description: Provides Deafult User Access Mechansim
- Requirements:

- user at least 4.0 and less than 4.1
- Paths:

- Classes: modules/User/modules/UserAccess/lib \[131\]

I2CE\_Module\_UserAccess, I2CE\_UserAccess

- Sql: modules/User/modules/UserAccess/sql \[132\]

- Templates: modules/User/modules/UserAccess/templates \[133\]

user\_form.html, user\_form\_edit.html

## UserAccess\_DHIS

This describes version 4.0.0 of the module User (UserAccess\_DHIS)

- Source: i2ce/modules/User/modules/UserAccess\_DHIS \[134\]

- Module Class: The module class is implemented by I2CE\_Module\_UserAccess\_DHIS
- Description: Provides DHIS User Access Mechansim
- Paths:

- Classes: modules/User/modules/UserAccess\_DHIS/lib \[135\]

- I2CE\_Module\_UserAccess\_DHIS, I2CE\_UserAccess\_DHIS
- Sql: modules/User/modules/UserAccess\_DHIS/sql \[136\]

- Templates: modules/User/modules/UserAccess\_DHIS/templates \[137\]

user\_form\_DHIS.html, user\_form\_edit\_DHIS.html

## UserAccess\_LDAP

This describes version 4.0.0 of the module User (UserAccess\_LDAP)

- Source: i2ce/modules/User/modules/UserAccess\_LDAP \[138\]

- Module Class: The module class is implemented by I2CE\_Module\_UserAccess\_LDAP
- Description: Provides LDAP User Access Mechansim
- Paths:

- Classes: modules/User/modules/UserAccess\_LDAP/lib \[139\]

- I2CE\_Module\_UserAccess\_LDAP, I2CE\_UserAccess\_LDAP
- Templates: modules/User/modules/UserAccess\_LDAP/templates \[140\]

user\_form\_LDAP.html, user\_form\_edit\_LDAP.html

## UserAccess\_LDAP\_Hybrid

This describes version 4.0.0 of the module User (UserAccess\_LDAP\_Hybrid)

- Source: i2ce/modules/User/modules/UserAccess\_LDAP\_Hybrid \[141\]

- Module Class: The module class is implemented by I2CE\_Module\_UserAccess\_LDAP\_Hybrid
- Description: Provides a hybrid database and LDAP User Access Mechansim
- Paths:

- Classes: modules/User/modules/UserAccess\_LDAP\_Hybrid/lib \[142\]

- I2CE\_Module\_UserAccess\_LDAP\_Hybrid, I2CE\_UserAccess\_LDAP\_DB
- Templates: modules/User/modules/UserAccess\_LDAP\_Hybrid/templates \[143\]

user\_form\_LDAP\_DB.html, user\_form\_edit\_LDAP\_DB.html

## UserForm

This describes version 4.0.7 of the module User Form (UserForm)

- Source: i2ce/modules/Forms/modules/UserForm \[144\]

- Description:
- Requirements:

- forms at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1

- LocaleForm at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/UserForm/configs \[145\]

- Classes: modules/Forms/modules/UserForm/lib \[146\]

- I2CE\_FormStorage\_userform, I2CE\_PageFormUser, I2CE\_User\_Form
- Templates: modules/Forms/modules/UserForm/templates \[147\]

button\_confirm\_user.html, user\_list.html

## YAML\_spyc

This describes version 0.3.0 of the module YAML (YAML\_spyc)

- Source: i2ce/modules/YAML \[148\]

- Module Class: The module class is implemented by I2CE\_Module\_YAML
- Fuzzy Methods:

- Implements the method I2CE\_Configurator-&gt;loadConfigFile\_YAML() via loadConfigFile\_YAML()
- Description: YAML parser provided by spyc. Also enabled processing of .YAML config files
- Paths:

- Classes: modules/YAML/lib \[149\]

- I2CE\_MagicDataTemplate\_YAML, I2CE\_Module\_YAML, Spyc
- Xml: modules/YAML/xml \[150\]

## admin

This describes version 4.0.0 of the module Modules Administation (admin)

- Source: i2ce/modules/Pages/modules/Admin \[151\]

- Description: The I2CE module administration system
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- FormWorm at least 4.0 and less than 4.1
- Optionally Enables: swissConfig
- Paths:

- Configs: modules/Pages/modules/Admin/configs \[152\]

- Classes: modules/Pages/modules/Admin/lib \[153\]

- I2CE\_PageAdmin
- Templates: modules/Pages/modules/Admin/templates \[154\]

- module\_module.html, module\_menu.html, module\_sub\_module.html, module\_category.html, no\_configuration.html
- Modules: modules/Pages/modules/Admin/modules \[155\]

- modulePrompter
- Css: modules/Pages/modules/Admin/css \[156\]

- Scripts: modules/Pages/modules/Admin/scripts \[157\]

- Images: modules/Pages/modules/Admin/images \[158\]

## fancyDebug

This describes version 4.0.0 of the module Fancy Debugger (fancyDebug)

- Source: i2ce/modules/MooTools/modules/Debugger \[159\]

- Module Class: The module class is implemented by I2CE\_Module\_Debugging
- Description: A fancy error displaying system
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MooTools/modules/Debugger/scripts \[160\]

- Images: modules/MooTools/modules/Debugger/images \[161\]

- Css: modules/MooTools/modules/Debugger/css \[162\]

- Classes: modules/MooTools/modules/Debugger/ \[163\]

## field-limits

This describes version 4.0.5 of the module Form Limits (field-limits)

- Source: i2ce/modules/Forms/modules/FieldLimits \[164\]

- Module Class: The module class is implemented by I2CE\_Module\_FieldLimits
- Fuzzy Methods:

- Implements the method I2CE\_FormField-&gt;getLimitStyles() via getFieldLimitStyles()
- Implements the method I2CE\_FormField-&gt;generateLimit() via generateFieldLimit()
- Implements the method I2CE\_FormField-&gt;generateLimit\_null() via generateLimit\_null()
- Implements the method I2CE\_FormField-&gt;generateLimit\_not\_null() via generateLimit\_not\_null()
- Implements the method I2CE\_FormField-&gt;generateLimit\_null\_not\_null() via generateLimit\_not\_null()
- Implements the method I2CE\_FormField-&gt;checkLimit\_null() via checkLimit\_null()
- Implements the method I2CE\_FormField-&gt;checkLimit\_not\_null() via checkLimit\_not\_null()
- Implements the method I2CE\_FormField-&gt;checkLimit\_null\_not\_null() via checkLimit\_not\_null()
- Implements the method I2CE\_FormField-&gt;checkLimitString\_null() via checkLimitString\_null()
- Implements the method I2CE\_FormField-&gt;checkLimitString\_not\_null() via checkLimitString\_not\_null()
- Implements the method I2CE\_FormField-&gt;checkLimitString\_null\_not\_null() via checkLimitString\_null\_not\_null()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_null() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_null()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_not\_null() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_not\_null()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_null\_not\_null() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_null\_not\_null()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_null() via I2CE\_FormField\_PROCESSFIELDSTYLE\_null()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_not\_null() via I2CE\_FormField\_PROCESSFIELDSTYLE\_not\_null()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_null\_not\_null() via I2CE\_FormField\_PROCESSFIELDSTYLE\_null\_not\_null()

- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_null() via generateLimit\_DB\_DATE\_null()

- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_not\_null() via generateLimit\_DB\_DATE\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_null\_not\_null() via generateLimit\_DB\_DATE\_null\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_null() via checkLimit\_DB\_DATE\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_not\_null() via checkLimit\_DB\_DATE\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_null\_not\_null() via checkLimit\_DB\_DATE\_null\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_null() via checkLimitString\_DB\_DATE\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_not\_null() via checkLimitString\_DB\_DATE\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_null\_not\_null() via checkLimitString\_DB\_DATE\_null\_not\_null()
- Implements the method I2CE\_FormField-&gt;generateLimit\_max\_parent() via generateLimit\_max\_parent()
- Implements the method I2CE\_FormField-&gt;generateLimit\_min\_parent() via generateLimit\_min\_parent()
- Implements the method I2CE\_FormField-&gt;generateLimit\_max\_parent\_form() via generateLimit\_max\_parent\_form()
- Implements the method I2CE\_FormField-&gt;generateLimit\_min\_parent\_form() via generateLimit\_min\_parent\_form()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_max\_parent() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_max\_parent()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_min\_parent() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_min\_parent()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_max\_parent\_form() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_max\_parent\_form()
- Implements the method I2CE\_FormField-&gt;getLimitMenu\_min\_parent\_form() via I2CE\_FormField\_DISPLAYFIELDSTYLE\_min\_parent\_form()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_max\_parent() via I2CE\_FormField\_PROCESSFIELDSTYLE\_max\_parent()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_min\_parent() via I2CE\_FormField\_PROCESSFIELDSTYLE\_min\_parent()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_max\_parent\_form() via I2CE\_FormField\_PROCESSFIELDSTYLE\_max\_parent\_form()
- Implements the method I2CE\_FormField-&gt;processLimitMenu\_min\_parent\_form() via I2CE\_FormField\_PROCESSFIELDSTYLE\_min\_parent\_form()
- Implements the method I2CE\_FormField\_BOOL-&gt;generateLimit\_truefalse() via generateLimit\_BOOL\_truefalse()
- Implements the method I2CE\_FormField\_BOOL-&gt;generateLimit\_true() via generateLimit\_BOOL\_true()
- Implements the method I2CE\_FormField\_BOOL-&gt;generateLimit\_false() via generateLimit\_BOOL\_false()
- Implements the method I2CE\_FormField\_YESNO-&gt;generateLimit\_yesno() via generateLimit\_YESNO\_yesno()
- Implements the method I2CE\_FormField\_YESNO-&gt;generateLimit\_yes() via generateLimit\_YESNO\_yes()
- Implements the method I2CE\_FormField\_YESNO-&gt;generateLimit\_no() via generateLimit\_YESNO\_no()

- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_in() via generateLimit\_DB\_INT\_in()

- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_in() via generateLimit\_DB\_STRING\_in()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_in() via generateLimit\_DB\_TEXT\_in()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_in() via generateLimit\_DB\_DATE\_in()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_equals() via generateLimit\_DB\_INT\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_equals() via generateLimit\_DB\_STRING\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_equals() via generateLimit\_DB\_TEXT\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_greaterthan() via generateLimit\_DB\_INT\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_greaterthan() via generateLimit\_DB\_STRING\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_greaterthan() via generateLimit\_DB\_TEXT\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_lessthan() via generateLimit\_DB\_INT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_lessthan() via generateLimit\_DB\_STRING\_lessthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_lessthan() via generateLimit\_DB\_TEXT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_greaterthan\_equals() via generateLimit\_DB\_INT\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_greaterthan\_equals() via generateLimit\_DB\_STRING\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_greaterthan\_equals() via generateLimit\_DB\_TEXT\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_lessthan\_equals() via generateLimit\_DB\_INT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_lessthan\_equals() via generateLimit\_DB\_STRING\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_lessthan\_equals() via generateLimit\_DB\_TEXT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;generateLimit\_between() via generateLimit\_DB\_INT\_between()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_between() via generateLimit\_DB\_STRING\_between()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_between() via generateLimit\_DB\_TEXT\_between()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_greaterthan\_now() via generateLimit\_greaterthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;generateLimit\_lessthan\_now() via generateLimit\_lessthan\_now()

- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_like() via generateLimit\_DB\_STRING\_like()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_like() via generateLimit\_DB\_TEXT\_like()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_lowerlike() via generateLimit\_DB\_STRING\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_lowerlike() via generateLimit\_DB\_TEXT\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_lowerequals() via generateLimit\_DB\_STRING\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_lowerequals() via generateLimit\_DB\_TEXT\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;generateLimit\_contains() via generateLimit\_DB\_STRING\_contains()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;generateLimit\_contains() via generateLimit\_DB\_TEXT\_contains()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_null() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_null() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_not\_null() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_not\_null() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_null\_not\_null() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_null\_not\_null()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_null\_not\_null() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_null\_not\_null()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimit\_truefalse() via checkLimit\_BOOL\_truefalse()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimitString\_truefalse() via checkLimitString\_BOOL\_truefalse()
- Implements the method I2CE\_FormField\_BOOL-&gt;getLimitMenu\_truefalse() via I2CE\_FormField\_BOOL\_DISPLAYFIELDSTYLE\_truefalse()
- Implements the method I2CE\_FormField\_BOOL-&gt;processLimitMenu\_truefalse() via I2CE\_FormField\_BOOL\_PROCESSFIELDSTYLE\_truefalse()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimit\_true() via checkLimit\_BOOL\_true()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimitString\_true() via checkLimitString\_BOOL\_true()
- Implements the method I2CE\_FormField\_BOOL-&gt;getLimitMenu\_true() via I2CE\_FormField\_BOOL\_DISPLAYFIELDSTYLE\_true()
- Implements the method I2CE\_FormField\_BOOL-&gt;processLimitMenu\_true() via I2CE\_FormField\_BOOL\_PROCESSFIELDSTYLE\_true()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimit\_false() via checkLimit\_BOOL\_false()
- Implements the method I2CE\_FormField\_BOOL-&gt;checkLimitString\_false() via checkLimitString\_BOOL\_false()
- Implements the method I2CE\_FormField\_BOOL-&gt;getLimitMenu\_false() via I2CE\_FormField\_BOOL\_DISPLAYFIELDSTYLE\_false()

- Implements the method I2CE\_FormField\_BOOL-&gt;processLimitMenu\_false() via I2CE\_FormField\_BOOL\_PROCESSFIELDSTYLE\_false()

- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimit\_yesno() via checkLimit\_YESNO\_yesno()
- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimitString\_yesno() via checkLimitString\_YESNO\_yesno()
- Implements the method I2CE\_FormField\_YESNO-&gt;getLimitMenu\_yesno() via I2CE\_FormField\_YESNO\_DISPLAYFIELDSTYLE\_yesno()
- Implements the method I2CE\_FormField\_YESNO-&gt;processLimitMenu\_yesno() via I2CE\_FormField\_YESNO\_PROCESSFIELDSTYLE\_yesno()
- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimit\_yes() via checkLimit\_YESNO\_yes()
- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimitString\_yes() via checkLimitString\_YESNO\_yes()
- Implements the method I2CE\_FormField\_YESNO-&gt;getLimitMenu\_yes() via I2CE\_FormField\_YESNO\_DISPLAYFIELDSTYLE\_yes()
- Implements the method I2CE\_FormField\_YESNO-&gt;processLimitMenu\_yes() via I2CE\_FormField\_YESNO\_PROCESSFIELDSTYLE\_yes()
- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimit\_no() via checkLimit\_YESNO\_no()
- Implements the method I2CE\_FormField\_YESNO-&gt;checkLimitString\_no() via checkLimitString\_YESNO\_no()
- Implements the method I2CE\_FormField\_YESNO-&gt;getLimitMenu\_no() via I2CE\_FormField\_YESNO\_DISPLAYFIELDSTYLE\_no()
- Implements the method I2CE\_FormField\_YESNO-&gt;processLimitMenu\_no() via I2CE\_FormField\_YESNO\_PROCESSFIELDSTYLE\_no()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_in() via checkLimit\_DB\_INT\_in()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_in() via checkLimitString\_DB\_INT\_in()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_in() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_in() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_in() via checkLimit\_DB\_STRING\_in()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_in() via checkLimitString\_DB\_STRING\_in()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_in() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_in() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_in() via checkLimit\_DB\_TEXT\_in()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_in() via checkLimitString\_DB\_TEXT\_in()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_in() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_in() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_in() via checkLimit\_DB\_DATE\_in()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_in() via checkLimitString\_DB\_DATE\_in()

- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_in() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_in()

- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_in() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_in()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_equals() via checkLimit\_DB\_INT\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_equals() via checkLimitString\_DB\_INT\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_equals() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_equals() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_equals() via checkLimit\_DB\_STRING\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_equals() via checkLimitString\_DB\_STRING\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_equals() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_equals() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_equals() via checkLimit\_DB\_TEXT\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_equals() via checkLimitString\_DB\_TEXT\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_equals() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_equals() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_greaterthan() via checkLimit\_DB\_INT\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_greaterthan() via checkLimitString\_DB\_INT\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_greaterthan() via checkLimit\_DB\_STRING\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_greaterthan() via checkLimitString\_DB\_STRING\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_greaterthan() via checkLimit\_DB\_TEXT\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_greaterthan() via checkLimitString\_DB\_TEXT\_greaterthan()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_greaterthan()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_greaterthan() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_greaterthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_lessthan() via checkLimit\_DB\_INT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_lessthan() via checkLimitString\_DB\_INT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_lessthan() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_lessthan() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_lessthan() via checkLimit\_DB\_STRING\_lessthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_lessthan() via checkLimitString\_DB\_STRING\_lessthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_lessthan() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_lessthan() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_lessthan() via checkLimit\_DB\_TEXT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_lessthan() via checkLimitString\_DB\_TEXT\_lessthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_lessthan() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_lessthan() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_lessthan()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_greaterthan\_equals() via checkLimit\_DB\_INT\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_greaterthan\_equals() via checkLimitString\_DB\_INT\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_greaterthan\_equals() via checkLimit\_DB\_STRING\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_greaterthan\_equals() via checkLimitString\_DB\_STRING\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_greaterthan\_equals() via checkLimit\_DB\_TEXT\_greaterthan\_equals()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_greaterthan\_equals() via checkLimitString\_DB\_TEXT\_greaterthan\_equals()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_greaterthan\_equals() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_lessthan\_equals() via checkLimit\_DB\_INT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_lessthan\_equals() via checkLimitString\_DB\_INT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_lessthan\_equals() via checkLimit\_DB\_STRING\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_lessthan\_equals() via checkLimitString\_DB\_STRING\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_lessthan\_equals() via checkLimit\_DB\_TEXT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_lessthan\_equals() via checkLimitString\_DB\_TEXT\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_lessthan\_equals() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimit\_between() via checkLimit\_DB\_INT\_between()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;checkLimitString\_between() via checkLimitString\_DB\_INT\_between()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;getLimitMenu\_between() via I2CE\_FormField\_DB\_INT\_DISPLAYFIELDSTYLE\_between()
- Implements the method I2CE\_FormField\_DB\_INT-&gt;processLimitMenu\_between() via I2CE\_FormField\_DB\_INT\_PROCESSFIELDSTYLE\_between()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_between() via checkLimit\_DB\_STRING\_between()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_between() via checkLimitString\_DB\_STRING\_between()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_between() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_between()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_between() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_between()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_between() via checkLimit\_DB\_TEXT\_between()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_between() via checkLimitString\_DB\_TEXT\_between()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_between() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_between()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_between() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_between()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_greaterthan\_now() via checkLimit\_DB\_DATE\_greaterthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_greaterthan\_now() via checkLimitString\_DB\_DATE\_greaterthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_greaterthan\_now() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_greaterthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_greaterthan\_now() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_greaterthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimit\_lessthan\_now() via checkLimit\_DB\_DATE\_lessthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;checkLimitString\_lessthan\_now() via checkLimitString\_DB\_DATE\_lessthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;getLimitMenu\_lessthan\_now() via I2CE\_FormField\_DB\_DATE\_DISPLAYFIELDSTYLE\_lessthan\_now()
- Implements the method I2CE\_FormField\_DB\_DATE-&gt;processLimitMenu\_lessthan\_now() via I2CE\_FormField\_DB\_DATE\_PROCESSFIELDSTYLE\_lessthan\_now()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_like() via checkLimit\_DB\_STRING\_like()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_like() via checkLimitString\_DB\_STRING\_like()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_like() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_like()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_like() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_like()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_like() via checkLimit\_DB\_TEXT\_like()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_like() via checkLimitString\_DB\_TEXT\_like()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_like() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_like()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_like() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_like()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_lowerlike() via checkLimit\_DB\_STRING\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_lowerlike() via checkLimitString\_DB\_STRING\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_lowerlike() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_lowerlike() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_lowerlike()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_lowerlike() via checkLimit\_DB\_TEXT\_lowerlike()

- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_lowerlike() via checkLimitString\_DB\_TEXT\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_lowerlike() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_lowerlike() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_lowerlike()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_lowerequals() via checkLimit\_DB\_STRING\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_lowerequals() via checkLimitString\_DB\_STRING\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_lowerequals() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_lowerequals() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_lowerequals() via checkLimit\_DB\_TEXT\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_lowerequals() via checkLimitString\_DB\_TEXT\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_lowerequals() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_lowerequals() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_lowerequals()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimit\_contains() via checkLimit\_DB\_STRING\_contains()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;checkLimitString\_contains() via checkLimitString\_DB\_STRING\_contains()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;getLimitMenu\_contains() via I2CE\_FormField\_DB\_STRING\_DISPLAYFIELDSTYLE\_contains()
- Implements the method I2CE\_FormField\_DB\_STRING-&gt;processLimitMenu\_contains() via I2CE\_FormField\_DB\_STRING\_PROCESSFIELDSTYLE\_contains()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimit\_contains() via checkLimit\_DB\_TEXT\_contains()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;checkLimitString\_contains() via checkLimitString\_DB\_TEXT\_contains()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;getLimitMenu\_contains() via I2CE\_FormField\_DB\_TEXT\_DISPLAYFIELDSTYLE\_contains()
- Implements the method I2CE\_FormField\_DB\_TEXT-&gt;processLimitMenu\_contains() via I2CE\_FormField\_DB\_TEXT\_PROCESSFIELDSTYLE\_contains()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_equals() via DATE\_generateLimit\_DATE\_YMD\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_equals() via DATE\_checkLimit\_DATE\_YMD\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_equals() via DATE\_checkLimit\_DATE\_YMD\_equals()

- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_equals() via DATE\_getLimitMenu\_DATE\_YMD\_equals()

- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_equals() via DATE\_processLimitMenu\_DATE\_YMD\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_equals() via DATE\_generateLimit\_DATE\_MD\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_equals() via DATE\_checkLimit\_DATE\_MD\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_equals() via DATE\_checkLimit\_DATE\_MD\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_equals() via DATE\_getLimitMenu\_DATE\_MD\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_equals() via DATE\_processLimitMenu\_DATE\_MD\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_equals() via DATE\_generateLimit\_DATE\_Y\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_equals() via DATE\_checkLimit\_DATE\_Y\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_equals() via DATE\_checkLimit\_DATE\_Y\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_equals() via DATE\_getLimitMenu\_DATE\_Y\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_equals() via DATE\_processLimitMenu\_DATE\_Y\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_equals() via DATE\_generateLimit\_DATE\_HMS\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_equals() via DATE\_checkLimit\_DATE\_HMS\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_equals() via DATE\_checkLimit\_DATE\_HMS\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_equals() via DATE\_getLimitMenu\_DATE\_HMS\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_equals() via DATE\_processLimitMenu\_DATE\_HMS\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_equals() via DATE\_generateLimit\_DATE\_TIME\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_equals() via DATE\_checkLimit\_DATE\_TIME\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_equals() via DATE\_checkLimit\_DATE\_TIME\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_equals() via DATE\_getLimitMenu\_DATE\_TIME\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_equals() via DATE\_processLimitMenu\_DATE\_TIME\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_greaterthan() via DATE\_generateLimit\_DATE\_YMD\_greaterthan()

- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_greaterthan() via DATE\_checkLimit\_DATE\_YMD\_greaterthan()

- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_greaterthan() via DATE\_checkLimit\_DATE\_YMD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_greaterthan() via DATE\_getLimitMenu\_DATE\_YMD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_greaterthan() via DATE\_processLimitMenu\_DATE\_YMD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_greaterthan() via DATE\_generateLimit\_DATE\_MD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_greaterthan() via DATE\_checkLimit\_DATE\_MD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_greaterthan() via DATE\_checkLimit\_DATE\_MD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_greaterthan() via DATE\_getLimitMenu\_DATE\_MD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_greaterthan() via DATE\_processLimitMenu\_DATE\_MD\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_greaterthan() via DATE\_generateLimit\_DATE\_Y\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_greaterthan() via DATE\_checkLimit\_DATE\_Y\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_greaterthan() via DATE\_checkLimit\_DATE\_Y\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_greaterthan() via DATE\_getLimitMenu\_DATE\_Y\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_greaterthan() via DATE\_processLimitMenu\_DATE\_Y\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_greaterthan() via DATE\_generateLimit\_DATE\_HMS\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_greaterthan() via DATE\_checkLimit\_DATE\_HMS\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_greaterthan() via DATE\_checkLimit\_DATE\_HMS\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_greaterthan() via DATE\_getLimitMenu\_DATE\_HMS\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_greaterthan() via DATE\_processLimitMenu\_DATE\_HMS\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_greaterthan() via DATE\_generateLimit\_DATE\_TIME\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_greaterthan() via DATE\_checkLimit\_DATE\_TIME\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_greaterthan() via DATE\_checkLimit\_DATE\_TIME\_greaterthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_greaterthan() via DATE\_getLimitMenu\_DATE\_TIME\_greaterthan()

- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_greaterthan() via DATE\_processLimitMenu\_DATE\_TIME\_greaterthan()

- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_lessthan() via DATE\_generateLimit\_DATE\_YMD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_lessthan() via DATE\_checkLimit\_DATE\_YMD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_lessthan() via DATE\_checkLimit\_DATE\_YMD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_lessthan() via DATE\_getLimitMenu\_DATE\_YMD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_lessthan() via DATE\_processLimitMenu\_DATE\_YMD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_lessthan() via DATE\_generateLimit\_DATE\_MD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_lessthan() via DATE\_checkLimit\_DATE\_MD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_lessthan() via DATE\_checkLimit\_DATE\_MD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_lessthan() via DATE\_getLimitMenu\_DATE\_MD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_lessthan() via DATE\_processLimitMenu\_DATE\_MD\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_lessthan() via DATE\_generateLimit\_DATE\_Y\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_lessthan() via DATE\_checkLimit\_DATE\_Y\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_lessthan() via DATE\_checkLimit\_DATE\_Y\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_lessthan() via DATE\_getLimitMenu\_DATE\_Y\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_lessthan() via DATE\_processLimitMenu\_DATE\_Y\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_lessthan() via DATE\_generateLimit\_DATE\_HMS\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_lessthan() via DATE\_checkLimit\_DATE\_HMS\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_lessthan() via DATE\_checkLimit\_DATE\_HMS\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_lessthan() via DATE\_getLimitMenu\_DATE\_HMS\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_lessthan() via DATE\_processLimitMenu\_DATE\_HMS\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_lessthan() via DATE\_generateLimit\_DATE\_TIME\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_lessthan() via DATE\_checkLimit\_DATE\_TIME\_lessthan()

- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_lessthan() via DATE\_checkLimit\_DATE\_TIME\_lessthan()

- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_lessthan() via DATE\_getLimitMenu\_DATE\_TIME\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_lessthan() via DATE\_processLimitMenu\_DATE\_TIME\_lessthan()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_greaterthan\_equals() via DATE\_generateLimit\_DATE\_YMD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_YMD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_YMD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_greaterthan\_equals() via DATE\_getLimitMenu\_DATE\_YMD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_greaterthan\_equals() via DATE\_processLimitMenu\_DATE\_YMD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_greaterthan\_equals() via DATE\_generateLimit\_DATE\_MD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_MD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_MD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_greaterthan\_equals() via DATE\_getLimitMenu\_DATE\_MD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_greaterthan\_equals() via DATE\_processLimitMenu\_DATE\_MD\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_greaterthan\_equals() via DATE\_generateLimit\_DATE\_Y\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_Y\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_Y\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_greaterthan\_equals() via DATE\_getLimitMenu\_DATE\_Y\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_greaterthan\_equals() via DATE\_processLimitMenu\_DATE\_Y\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_greaterthan\_equals() via DATE\_generateLimit\_DATE\_HMS\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_HMS\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_HMS\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_greaterthan\_equals() via DATE\_getLimitMenu\_DATE\_HMS\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_greaterthan\_equals() via DATE\_processLimitMenu\_DATE\_HMS\_greaterthan\_equals()

- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_greaterthan\_equals() via DATE\_generateLimit\_DATE\_TIME\_greaterthan\_equals()

- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_TIME\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_greaterthan\_equals() via DATE\_checkLimit\_DATE\_TIME\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_greaterthan\_equals() via DATE\_getLimitMenu\_DATE\_TIME\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_greaterthan\_equals() via DATE\_processLimitMenu\_DATE\_TIME\_greaterthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_lessthan\_equals() via DATE\_generateLimit\_DATE\_YMD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_lessthan\_equals() via DATE\_checkLimit\_DATE\_YMD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_lessthan\_equals() via DATE\_checkLimit\_DATE\_YMD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_lessthan\_equals() via DATE\_getLimitMenu\_DATE\_YMD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_lessthan\_equals() via DATE\_processLimitMenu\_DATE\_YMD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_lessthan\_equals() via DATE\_generateLimit\_DATE\_MD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_lessthan\_equals() via DATE\_checkLimit\_DATE\_MD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_lessthan\_equals() via DATE\_checkLimit\_DATE\_MD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_lessthan\_equals() via DATE\_getLimitMenu\_DATE\_MD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_lessthan\_equals() via DATE\_processLimitMenu\_DATE\_MD\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_lessthan\_equals() via DATE\_generateLimit\_DATE\_Y\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_lessthan\_equals() via DATE\_checkLimit\_DATE\_Y\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_lessthan\_equals() via DATE\_checkLimit\_DATE\_Y\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_lessthan\_equals() via DATE\_getLimitMenu\_DATE\_Y\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_lessthan\_equals() via DATE\_processLimitMenu\_DATE\_Y\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_lessthan\_equals() via DATE\_generateLimit\_DATE\_HMS\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_lessthan\_equals() via DATE\_checkLimit\_DATE\_HMS\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_lessthan\_equals() via DATE\_checkLimit\_DATE\_HMS\_lessthan\_equals()

- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_lessthan\_equals() via DATE\_getLimitMenu\_DATE\_HMS\_lessthan\_equals()

- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_lessthan\_equals() via DATE\_processLimitMenu\_DATE\_HMS\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_lessthan\_equals() via DATE\_generateLimit\_DATE\_TIME\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_lessthan\_equals() via DATE\_checkLimit\_DATE\_TIME\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_lessthan\_equals() via DATE\_checkLimit\_DATE\_TIME\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_lessthan\_equals() via DATE\_getLimitMenu\_DATE\_TIME\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_lessthan\_equals() via DATE\_processLimitMenu\_DATE\_TIME\_lessthan\_equals()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;getLimitMenu\_between() via DATE\_getLimitMenu\_DATE\_YMD\_between()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;generateLimit\_between() via DATE\_generateLimit\_DATE\_YMD\_between()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimit\_between() via DATE\_checkLimit\_DATE\_YMD\_between()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;checkLimitString\_between() via DATE\_checkLimitString\_DATE\_YMD\_between()
- Implements the method I2CE\_FormField\_DATE\_YMD-&gt;processLimitMenu\_between() via DATE\_processLimitMenu\_DATE\_YMD\_between()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;getLimitMenu\_between() via DATE\_getLimitMenu\_DATE\_MD\_between()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;generateLimit\_between() via DATE\_generateLimit\_DATE\_MD\_between()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimit\_between() via DATE\_checkLimit\_DATE\_MD\_between()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;checkLimitString\_between() via DATE\_checkLimitString\_DATE\_MD\_between()
- Implements the method I2CE\_FormField\_DATE\_MD-&gt;processLimitMenu\_between() via DATE\_processLimitMenu\_DATE\_MD\_between()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;getLimitMenu\_between() via DATE\_getLimitMenu\_DATE\_Y\_between()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;generateLimit\_between() via DATE\_generateLimit\_DATE\_Y\_between()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimit\_between() via DATE\_checkLimit\_DATE\_Y\_between()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;checkLimitString\_between() via DATE\_checkLimitString\_DATE\_Y\_between()
- Implements the method I2CE\_FormField\_DATE\_Y-&gt;processLimitMenu\_between() via DATE\_processLimitMenu\_DATE\_Y\_between()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;getLimitMenu\_between() via DATE\_getLimitMenu\_DATE\_HMS\_between()

- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;generateLimit\_between() via DATE\_generateLimit\_DATE\_HMS\_between()

- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimit\_between() via DATE\_checkLimit\_DATE\_HMS\_between()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;checkLimitString\_between() via DATE\_checkLimitString\_DATE\_HMS\_between()
- Implements the method I2CE\_FormField\_DATE\_HMS-&gt;processLimitMenu\_between() via DATE\_processLimitMenu\_DATE\_HMS\_between()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;getLimitMenu\_between() via DATE\_getLimitMenu\_DATE\_TIME\_between()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;generateLimit\_between() via DATE\_generateLimit\_DATE\_TIME\_between()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimit\_between() via DATE\_checkLimit\_DATE\_TIME\_between()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;checkLimitString\_between() via DATE\_checkLimitString\_DATE\_TIME\_between()
- Implements the method I2CE\_FormField\_DATE\_TIME-&gt;processLimitMenu\_between() via DATE\_processLimitMenu\_DATE\_TIME\_between()
- Description: A module that enables limits for fields.
- Requirements:

- Fields at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FieldLimits/lib \[165\]

- I2CE\_Module\_FieldLimits
- Templates: modules/Forms/modules/FieldLimits/templates \[166\]

limit\_mapped\_choice\_between.html, limit\_choice\_contains.html, limit\_choice\_yesno.html, limit\_choice\_greaterthan\_now.html, limit\_date\_choice\_between.html, limit\_choice\_not\_null.html, limit\_mapped\_choice\_lessthan\_equals.html, limit\_choice\_lowerlike.html, limit\_choice\_truefalse.html, limit\_mapped\_choice\_equals.html, limit\_choice\_min\_parent.html, limit\_choice\_like.html, limit\_choice\_between.html, limit\_date\_choice.html, limit\_choice\_null\_not\_null.html, limit\_choice\_no.html, limit\_choice\_min\_parent\_form.html, limit\_choice\_greaterthan\_equals.html, limit\_choice\_true.html, limit\_choice\_lowerequals.html, limit\_mapped\_choice\_greaterthan\_equals.html, limit\_choice\_max\_parent.html, limit\_choice\_greaterthan.html, limit\_choice\_in.html, limit\_mapped\_choice\_greaterthan.html, limit\_choice\_lessthan\_now.html, limit\_choice\_max\_parent\_form.html, limit\_choice\_lessthan\_equals.html, limit\_choice\_lessthan.html, limit\_mapped\_choice\_in.html, limit\_choice\_yes.html, limit\_choice\_false.html, limit\_choice\_null.html, limit\_mapped\_choice\_lessthan.html, limit\_choice\_equals.html

## form-limits

This describes version 4.0.6 of the module Form Limits (form-limits)

- Source: i2ce/modules/Forms/modules/FormLimits \[167\]

- Module Class: The module class is implemented by I2CE\_Module\_FormLimits
- Fuzzy Methods:

- Implements the method I2CE\_Form-&gt;getLimitStyles() via getLimitStyles()
- Implements the method I2CE\_Form-&gt;checkLimit() via checkLimit()

- Implements the method I2CE\_Form-&gt;checkWhereClause() via checkWhereClause()
- Implements the method I2CE\_Form-&gt;createCheckFunction() via createCheckFunction()
- Implements the method I2CE\_Form-&gt;createCheckLimitString() via createCheckLimitString()

- Implements the method I2CE\_Form-&gt;generateLimit() via generateLimit()
- Implements the method I2CE\_Form-&gt;generateWhereClause() via generateWhereClause()
- Description: A module that enables limits for forms.
- Requirements:

- forms at least 4.0 and less than 4.1
- field-limits at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormLimits/lib \[168\]

- I2CE\_Module\_FormLimits
- Templates: modules/Forms/modules/FormLimits/templates \[169\]

## formBrowser

This describes version 4.0.0 of the module Form Browser (formBrowser)

- Source: i2ce/modules/Forms/modules/FormBrowser \[170\]

- Description: Enables Browsing of Forms
- Requirements:

- forms at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/modules/FormBrowser/configs \[171\]

- Classes: modules/Forms/modules/FormBrowser/lib \[172\]

- I2CE\_FormBrowser, I2CE\_PageFormBrowser
- Templates: modules/Forms/modules/FormBrowser/templates \[173\]

- formBrowser\_form\_details\_edit.html, formBrowser\_form\_details\_record\_edit.html, formBrowser\_form\_details\_record\_edit\_link.html, formBrowser\_form\_details.html, formBrowser.html, formBrowser\_form\_details\_no\_record.html, formBrowse\_menu.html, formBrowser\_menu.html, formBrowser\_menu\_form.html, formBrowser\_form\_details\_record.html, formBrowser\_form\_details\_record\_link.html
- Css: modules/Forms/modules/FormBrowser/css \[174\]

## formDocumentor

This describes version 4.0.3 of the module Form Documentor (formDocumentor)

- Source: i2ce/modules/Forms/modules/FormDocumentor \[175\]

- Description: Enables Documenting of existing forms and their relationship from the command line
- Requirements:

- forms at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormDocumentor/lib \[176\]

- I2Ce\_Page\_FormDocumentor
- Images: modules/Forms/modules/FormDocumentor/images \[177\]

## formRelationships

This describes version 4.0.0 of the module Form Relationships (formRelationships)

- Source: i2ce/modules/Forms/modules/FormRelationship \[178\]

- Description: Provides Form Relationships for use by a Swiss Factory
- Requirements:

- forms at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- swissfactory at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormRelationship/lib \[179\]

- I2CE\_FormRelationship, I2CE\_FormRelationship\_Template, I2CE\_Swiss\_FormRelationship, I2CE\_Swiss\_FormRelationship\_AncestralCondition, I2CE\_Swiss\_FormRelationship\_AncestralConditions, I2CE\_Swiss\_FormRelationship\_Base, I2CE\_Swiss\_FormRelationship\_Join, I2CE\_Swiss\_FormRelationship\_Joins, I2CE\_Swiss\_FormRelationship\_ReportingFunctions, I2CE\_Swiss\_FormRelationship\_Where, I2CE\_Swiss\_FormRelationship\_Where\_Operands, I2CE\_Swiss\_FormRelationships, I2CE\_Swiss\_SQLFunction
- Templates: modules/Forms/modules/FormRelationship/templates \[180\]

- swiss\_sqlfunction\_edit.html, formRelationship\_existing\_limit.html, formRelationship\_join\_container.html, formRelationship\_new\_limits.html, formRelationship\_existing\_operand\_list\_member\_view.html, formRelationship\_existing\_function\_view.html, formRelationship\_join\_drop\_empty\_view.html, formRelationship\_existing\_operand\_list\_member\_edit.html, swiss\_sqlfunction\_view.html, formRelationship\_condition.html, formrelationships\_options.html, formRelationship\_join\_drop\_empty\_edit.html, formRelationship\_view\_relation.html, formRelationship\_new\_limit\_style.html, formRelationship\_reporting\_functions\_view.html, formRelationship\_view.html, formRelationship\_existing\_function\_edit.html, formRelationship\_existing\_condition.html, formRelationship\_existing\_conditions.html, formRelationship\_menu\_relation\_copy.html, formRelationship\_new\_operand.html, formRelationship\_relationship\_each.html, formRelationship\_join.html, formRelationship\_conditions\_container.html, formRelationship\_new\_limit\_choice.html, formRelationship\_edit.html, formRelationship\_relationship.html, formRelationship\_meta\_edit.html, formRelationship\_new\_limit\_styles.html, formRelationship\_existing\_operand.html, formRelationship\_existing\_joins.html, formRelationship\_reporting\_functions\_edit.html, formRelationship\_join\_meta.html, formRelationship\_where\_container.html, formRelationship\_menu\_form.html, formRelationship\_meta\_view.html, formRelationship\_new\_condition.html, formRelationship\_existing\_operand\_list.html, formRelationship\_existing\_join.html
- Css: modules/Forms/modules/FormRelationship/css \[181\]

## forms

This describes version 4.0.6 of the module I2CE Forms (forms)

- Source: i2ce/modules/Forms \[182\]

- Module Class: The module class is implemented by I2CE\_Module\_Forms
- Fuzzy Methods:

- Implements the method I2CE\_PermissionParser-&gt;hasPermission\_form() via hasPermission\_form()
- Implements the method I2CE\_Template-&gt;setForm() via setForm()
- Implements the method I2CE\_Template-&gt;getField() via getField()
- Implements the method I2CE\_Template-&gt;setReview() via setReview()
- Implements the method I2CE\_Template-&gt;isReview() via isReview()
- Implements the method I2CE\_Template-&gt;setShowForm() via setShowForm()
- Implements the method I2CE\_Template-&gt;showForm() via showForm()
- Implements the method I2CE\_Page-&gt;setForm() via setForm()
- Implements the method I2CE\_Page-&gt;getField() via getField()
- Implements the method I2CE\_Page-&gt;setReview() via setReview()
- Implements the method I2CE\_Page-&gt;isReview() via isReview()
- Implements the method I2CE\_Page-&gt;setShowForm() via setShowForm()
- Implements the method I2CE\_Page-&gt;showForm() via showForm()
- Description: Adds a few basic forms to the system as well as some form functionality to the template
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Fields at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- DisplayData at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Forms/configs \[183\]

- Classes: modules/Forms/lib \[184\]

- I2CE\_Form, I2CE\_FormFactory, I2CE\_Module\_Forms, I2CE\_PageForm
- Templates: modules/Forms/templates \[185\]

- button\_save\_only.html, button\_confirm.html, form\_error.html, button\_save\_return.html, button\_save.html, button\_confirm\_notchild.html
- Scripts: modules/Forms/scripts \[186\]

- Modules: modules/Forms/modules \[187\]

BinField, CachedForms, Fields, Float, Lists, LocaleForm, PrintedForms, UserForm, field-limits, form-limits, formBrowser, formDocumentor, formRelationships, forms-storage

## forms-storage

This describes version 4.0.6 of the module Form Storage (forms-storage)

- Source: i2ce/modules/Forms/modules/FormStorage \[188\]

- Module Class: The module class is implemented by I2CE\_FormStorage
- Fuzzy Methods:

- Implements the method I2CE\_Form-&gt;isComponentized() via isComponentizedForm()
- Implements the method I2CE\_Form-&gt;addChild() via addChild()
- Implements the method I2CE\_Form-&gt;getChildIds() via getChildIds()
- Implements the method I2CE\_Form-&gt;getStorage() via getStorage()
- Implements the method I2CE\_Form-&gt;isWritable() via isWritable()
- Implements the method I2CE\_Form-&gt;populate() via populate()
- Implements the method I2CE\_Form-&gt;populateChild() via populateChild()
- Implements the method I2CE\_Form-&gt;populateChildren() via populateChildren()
- Implements the method I2CE\_Form-&gt;populateFirst() via populateFirst()
- Implements the method I2CE\_Form-&gt;populateHistory() via populateHistory()
- Implements the method I2CE\_Form-&gt;populateLast() via populateLast()
- Implements the method I2CE\_Form-&gt;delete() via delete()
- Implements the method I2CE\_Form-&gt;save() via save()
- Implements the method I2CE\_Form-&gt;setChangeType() via setChangeType()
- Implements the method I2CE\_FormField-&gt;save() via FF\_save()
- Implements the method I2CE\_FormField\_INT\_GENERATE-&gt;save() via FF\_IG\_save()
- Implements the method I2CE\_FormField\_STRING\_PASS-&gt;save() via FF\_SP\_save()
- Implements the method I2CE\_FormField-&gt;populateHistory() via FF\_populateHistory()
- Implements the method I2CE\_FormField\_INT\_GENERATE-&gt;setSequence() via FF\_IG\_setSequence()
- Implements the method I2CE\_FormFactory-&gt;getRecords() via getRecords()
- Description: A module that enables storage of Forms. Sub modules will enable the specific storage and retrieval options.
- Requirements:

- forms at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/lib \[189\]

- I2CE\_FormStorage, I2CE\_FormStorage\_DB, I2CE\_FormStorage\_Mechanism
- Modules: modules/Forms/modules/FormStorage/modules \[190\]

forms-storage-CSV, forms-storage-SDMXHD, forms-storage-entry, forms-storage-eval, forms-storage-file, forms-storage-flat, forms-storage-magicdata, forms-storage-multiflat, forms-storage-xml

## forms-storage-CSV

This describes version 4.0.0 of the module Form Storage - CSV (forms-storage-CSV)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageCSV \[191\]

- Description: A module that enables reading storage of Forms from a CSV file
- Requirements:

- forms-storage-file at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageCSV/lib \[192\]

I2CE\_FormStorage\_CSV

## forms-storage-SDMXHD

This describes version 4.0.5 of the module Form Storage - SDMX-HD (forms-storage-SDMXHD)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD \[193\]

- Description: A module that enables reading storage of Forms from a SDMX CodeList or CrossSectionalData
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- forms-storage-xml at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD/lib \[194\]

I2CE\_FormStorage\_SDMXHD, I2CE\_FormStorage\_SDMX\_CrossSectional

## forms-storage-entry

This describes version 4.0.6 of the module Form Storage - Entry (forms-storage-entry)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageEntry \[195\]

- Module Class: The module class is implemented by I2CE\_Module\_FormStorageEntry
- Description: A module that enables storage of Forms to a entry database structure that enables historical tracking and automatic extension for new fields.
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageEntry/lib \[196\]

- I2CE\_FormStorage\_entry, I2CE\_Module\_FormStorageEntry
- Sql: modules/Forms/modules/FormStorage/modules/FormStorageEntry/sql \[197\]

## forms-storage-eval

This describes version 4.0.0 of the module Form Storage - Eval (forms-storage-eval)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageEval \[198\]

- Description: A module that enables storage of Forms based on evalualtion of php functions
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageEval/lib \[199\]

I2CE\_FormStorage\_eval

## forms-storage-file

This describes version 4.0.6 of the module Form Storage - File (forms-storage-file)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageFile \[200\]

- Description: A module that for file based access form storage mechanisms
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageFile/lib \[201\]

I2CE\_FormStorage\_File\_Base

## forms-storage-flat

This describes version 4.0.6 of the module Form Storage - Flat (forms-storage-flat)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageFlat \[202\]

- Description: A module that enables storage of Forms to a flat fixed database structure.
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageFlat/lib \[203\]

I2CE\_FormStorage\_Flat

## forms-storage-magicdata

This describes version 4.0.6 of the module Form Storage - Magic Data (forms-storage-magicdata)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageMagicData \[204\]

- Description: A module that enables storage of Forms to MagicData Storage.
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageMagicData/lib \[205\]

I2CE\_FormStorage\_magicdata, I2CE\_FormStorage\_magicdata, I2CE\_FormStorage\_magicdata

## forms-storage-multiflat

This describes version 4.0.6 of the module Form Storage - Multi Flat (forms-storage-multiflat)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat \[206\]

- Description: A module that enables aggregated storage of Forms from a flat fixed database structure.
- Requirements:

- forms-storage at least 4.0 and less than 4.1
- Lists at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat/lib \[207\]

I2CE\_FormStorage\_multi\_flat

## forms-storage-xml

This describes version 4.0.6 of the module Form Storage - XML (forms-storage-xml)

- Source: i2ce/modules/Forms/modules/FormStorage/modules/FormStorageXML \[208\]

- Description: A module that enables reading storage of Forms from a XML file
- Requirements:

- forms-storage-file at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Forms/modules/FormStorage/modules/FormStorageXML/lib \[209\]

I2CE\_FormStorage\_XML, I2CE\_FormStorage\_XML\_BASE

## jumper

This describes version 4.0.0 of the module Page Jumper (jumper)

- Source: i2ce/modules/Jumper \[210\]

- Module Class: The module class is implemented by I2CE\_Module\_Jumper
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;makeJumper() via makeJumper()
- Implements the method I2CE\_Template-&gt;makeJumper() via makeJumper()
- Description: Creates a page jumper for elements of a page.
- Requirements:

- pages at least 4.0 and less than 4.1
- Optionally Enables: stub
- Paths:

- Images: modules/Jumper/images \[211\]

- Css: modules/Jumper/css \[212\]

- Classes: modules/Jumper/ \[213\]

I2CE\_Module\_Jumper

## localeSelector

This describes version 4.0.3.3 of the module Locale Selector (localeSelector)

- Source: i2ce/modules/Pages/modules/LocaleSelector \[214\]

- Module Class: The module class is implemented by I2CE\_Module\_LocaleSelector
- Description: Provides Locale Selector for a page as well information for locales
- Requirements:

- pages at least 4.0 and less than 4.1
- swissfactory at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Pages/modules/LocaleSelector/lib \[215\]

- I2CE\_Module\_LocaleSelector, I2CE\_Page\_LocaleAdmin, I2CE\_Swiss\_Locale, I2CE\_Swiss\_Locales
- Images: modules/Pages/modules/LocaleSelector/images \[216\]

- Misc: modules/Pages/modules/LocaleSelector/Flags.xml \[217\]

- Configs: modules/Pages/modules/LocaleSelector/configs \[218\]

- Templates: modules/Pages/modules/LocaleSelector/templates \[219\]

language\_choice\_icon.html, site\_locale\_add.html, language\_choice.html, site\_locale\_base\_edit.html, site\_locale\_each.html, site\_locale\_base.html, locale\_view.html, locale\_edit.html

## maani-charts

This describes version 4.7 of the module Charted Reports (maani-charts)

- Source: i2ce/modules/FlashCharts \[220\]

- Description: Configuration options for the Maani chart reporting software http://www.maani.us/charts
- Requirements:

- FileDump at least 4.0 and less than 4.1
- Paths:

- Maani\_chart\_files: modules/FlashCharts/maani\_charts \[221\]

- Swf: modules/FlashCharts/maani\_charts \[221\]

- Scripts: modules/FlashCharts/scripts \[222\]

- Classes: modules/FlashCharts/ \[223\]

## magicDataBrowser

This describes version 4.0.0 of the module Magic Data Browser (magicDataBrowser)

- Source: i2ce/modules/Pages/modules/MagicDataBrowser \[224\]

- Description: Browse Magic Data
- Requirements:

- pages at least 4.0 and less than 4.1
- FormWorm at least 4.0 and less than 4.1
- Optionally Enables: magicDataExport
- Paths:

- Configs: modules/Pages/modules/MagicDataBrowser/configs \[225\]

- Scripts: modules/Pages/modules/MagicDataBrowser/scripts \[226\]

- Templates: modules/Pages/modules/MagicDataBrowser/templates \[227\]

- browser\_value\_node\_notset\_mini.html, browser\_value\_node\_mini.html, browser\_node.html, browser\_value\_node\_notset.html, magicdata\_export\_controls.html, browser\_value\_node.html, browser.html, browser\_node\_mini.html, browser\_add\_node.html
- Css: modules/Pages/modules/MagicDataBrowser/css \[228\]

- Classes: modules/Pages/modules/MagicDataBrowser/ \[229\]

I2CE\_Page\_MagicDataBrowser

## magicDataExport

This describes version 4.0.0 of the module Magic Data Export (magicDataExport)

- Source: i2ce/modules/MagicDataExport \[230\]

- Description: Export Magic Data
- Requirements:

- pages at least 4.0 and less than 4.1
- Paths:

- Xml: modules/MagicDataExport/xml \[231\]

- Classes: modules/MagicDataExport/ \[232\]

I2CE\_MagicDataExport\_Template, I2CE\_Page\_MagicDataExport

## menu\_select

This describes version 4.0.0 of the module Menu Select (menu\_select)

- Source: i2ce/modules/MooTools/modules/MenuSelect \[233\]

- Module Class: The module class is implemented by I2CE\_Module\_MenuSelect
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;menuSelect() via menuSelect()
- Implements the method I2CE\_Template-&gt;menuSelect() via menuSelect()
- Implements the method I2CE\_Page-&gt;addUpdateSelect() via addUpdateSelect()
- Implements the method I2CE\_Template-&gt;addUpdateSelect() via addUpdateSelect()
- Description: Handles Nested Select Options
- Requirements:

- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MooTools/modules/MenuSelect/scripts \[234\]

- Classes: modules/MooTools/modules/MenuSelect/ \[235\]

## messageBox

This describes version 4.0.0 of the module Message Box (messageBox)

- Source: i2ce/modules/MessageHandler/modules/MessageBox \[236\]

- Module Class: The module class is implemented by I2CE\_MessageBox
- Description: Displays the default message in a box
- Requirements:

- messageHandler at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MessageHandler/modules/MessageBox/scripts \[237\]

- Css: modules/MessageHandler/modules/MessageBox/css \[238\]

- Classes: modules/MessageHandler/modules/MessageBox/ \[239\]

I2CE\_MessageBox

## messageHandler

This describes version 4.0.0 of the module Message Handler (messageHandler)

- Source: i2ce/modules/MessageHandler \[240\]

- Module Class: The module class is implemented by I2CE\_MessageHandler
- Fuzzy Methods:

- Implements the method I2CE\_Fuzzy-&gt;userMessage() via addUserMessage()
- Description: A handler for user messages
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Paths:

- Modules: modules/MessageHandler/modules \[241\]

- messageBox, messageNotice
- Classes: modules/MessageHandler/ \[242\]

I2CE\_MessageHandler, I2CE\_MessageNotice

## messageNotice

This describes version 4.0.0 of the module Message Notices (messageNotice)

- Source: i2ce/modules/MessageHandler/modules/MessageNotice \[243\]

- Module Class: The module class is implemented by I2CE\_MessageNotice
- Description: Displays any messages taggged with 'notice' in a notice box box
- Requirements:

- pages at least 4.0 and less than 4.1
- messageHandler at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Scripts: modules/MessageHandler/modules/MessageNotice/scripts \[244\]

- Css: modules/MessageHandler/modules/MessageNotice/css \[245\]

- Images: modules/MessageHandler/modules/MessageNotice/images \[246\]

- Classes: modules/MessageHandler/modules/MessageNotice/ \[247\]

## modDocumentor

This describes version 4.0.3 of the module Mod Documentor (modDocumentor)

- Source: i2ce/modules/Pages/modules/ModDocumentor \[248\]

- Description: Enables Documenting of existing mods and their relationship from the command line
- Requirements:

- pages at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Pages/modules/ModDocumentor/lib \[249\]

I2Ce\_Page\_ModDocumentor

## modulePrompter

This describes version 4.0.0 of the module Module Prompter (modulePrompter)

- Source: i2ce/modules/Pages/modules/Admin/modules/ModulePrompter \[250\]

- Module Class: The module class is implemented by I2CE\_Module\_ModulePrompter
- Fuzzy Methods:

- Implements the method I2CE\_Wrangler-&gt;manipulateWrangler\_I2CE\_home() via changeHomePage()
- Description: Module to prompt the enable/disable of specific modules upon login
- Requirements:

- I2CE at least 4.0 and less than 4.1
- admin at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Pages/modules/Admin/modules/ModulePrompter/lib \[251\]

I2CE\_Module\_ModulePrompter

## pages

This describes version 4.0.0 of the module Pages (pages)

- Source: i2ce/modules/Pages \[252\]

- Description: Provides pages, Users, Permissions and Templates
- Requirements:

- I2CE at least 4.0 and less than 4.1
- user at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Pages/configs \[253\]

- Modules: modules/Pages/modules \[254\]

- FileDump, LoginPage, admin, localeSelector, magicDataBrowser, modDocumentor, stub, tasks-roles
- Templates: modules/Pages/templates \[255\]

- noaccess.html, main.html
- Classes: modules/Pages/lib \[256\]

I2CE\_Page, I2CE\_PermissionParser, I2CE\_Template, I2CE\_Wrangler

## stub

This describes version 4.0.0 of the module Page Stubs (stub)

- Source: i2ce/modules/Pages/modules/Stub \[257\]

- Module Class: The module class is implemented by I2CE\_Stub
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;addAjaxUpdate() via addAjaxUpdate()
- Implements the method I2CE\_Template-&gt;addAjaxUpdate() via addAjaxUpdate()
- Implements the method I2CE\_Page-&gt;addAjaxToggle() via addAjaxToggle()
- Implements the method I2CE\_Template-&gt;addAjaxToggle() via addAjaxToggle()
- Implements the method I2CE\_Page-&gt;addAjaxRequestFunction() via addAjaxRequestFunction()
- Implements the method I2CE\_Template-&gt;addAjaxRequestFunction() via addAjaxRequestFunction()
- Implements the method I2CE\_Page-&gt;addAjaxCompleteFunction() via addAjaxCompleteFunction()
- Implements the method I2CE\_Template-&gt;addAjaxCompleteFunction() via addAjaxCompleteFunction()
- Implements the method I2CE\_Page-&gt;addAjaxToggleOnFunction() via addAjaxToggleOnFunction()
- Implements the method I2CE\_Template-&gt;addAjaxToggleOnFunction() via addAjaxToggleOnFunction()
- Implements the method I2CE\_Page-&gt;addAjaxToggleOffFunction() via addAjaxToggleOffFunction()
- Implements the method I2CE\_Template-&gt;addAjaxToggleOffFunction() via addAjaxToggleOffFunction()
- Implements the method I2CE\_Page-&gt;hasAjax() via hasAjaxFuzzy()
- Implements the method I2CE\_Template-&gt;hasAjax() via hasAjaxFuzzy()
- Description: Request only the stub of a page -- intended for ajax use.
- Requirements:

- I2CE at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- MooTools at least 1.2 and less than 1.3
- Paths:

- Configs: modules/Pages/modules/Stub/configs \[258\]

- Scripts: modules/Pages/modules/Stub/scripts \[259\]

- Images: modules/Pages/modules/Stub/images \[260\]

- Css: modules/Pages/modules/Stub/css \[261\]

- Classes: modules/Pages/modules/Stub/ \[262\]

I2CE\_Page\_Stub, I2CE\_Page\_Stub\_Ajax\_Test, I2CE\_Stub

## swissConfig

This describes version 4.0.0 of the module Swiss Config (swissConfig)

- Source: i2ce/modules/SwissFactory/modules/SwissConfig \[263\]

- Description: The Swiss Factory Module to display configuration files
- Requirements:

- swissfactory at least 4.0 and less than 4.1
- Paths:

- Configs: modules/SwissFactory/modules/SwissConfig/configs \[264\]

- Classes: modules/SwissFactory/modules/SwissConfig/lib \[265\]

I2CE\_Page\_SwissConfig, I2CE\_SwissConfigFactory

## swissMagic

This describes version 4.0.0 of the module Swiss Magic (swissMagic)

- Source: i2ce/modules/SwissFactory/modules/SwissMagic \[266\]

- Description: The Swiss Factory Module to display magic data directly
- Requirements:

- swissfactory at least 4.0 and less than 4.1
- Paths:

- Configs: modules/SwissFactory/modules/SwissMagic/configs \[267\]

- Classes: modules/SwissFactory/modules/SwissMagic/lib \[268\]

I2CE\_Page\_SwissMagic

## swissfactory

This describes version 4.0.0 of the module Swiss Factory (swissfactory)

- Source: i2ce/modules/SwissFactory \[269\]

- Module Class: The module class is implemented by I2CE\_Module\_SwissFactory
- Fuzzy Methods:

- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_string\_single() via editValue\_string\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_string\_many() via editValue\_string\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_delimited\_single() via editValue\_delimited\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_delimited\_many() via editValue\_delimited\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_boolean\_single() via editValue\_boolean\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_boolean\_many() via editValue\_boolean\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_list\_single() via editValue\_list\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;editValue\_list\_many() via editValue\_list\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_string\_single() via viewValue\_string\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_string\_many() via viewValue\_string\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_delimited\_single() via viewValue\_delimited\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_delimited\_many() via viewValue\_delimited\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_boolean\_single() via viewValue\_boolean\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_boolean\_many() via viewValue\_boolean\_many()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_list\_single() via viewValue\_list\_single()
- Implements the method I2CE\_Swiss\_Default\_Leaf-&gt;viewValue\_list\_many() via viewValue\_list\_many()
- Description: The Swiss Factory Magic Data Editing System
- Requirements:

- pages at least 4.0 and less than 4.1

- FormWorm at least 4.0 and less than 4.1
- menu\_select at least 4.0 and less than 4.1

- Paths:

- Classes: modules/SwissFactory/lib \[270\]

- I2CE\_Module\_SwissFactory, I2CE\_Swiss, I2CE\_SwissFactory, I2CE\_SwissMagicFactory, I2CE\_Swiss\_Default, I2CE\_Swiss\_Default\_Base, I2CE\_Swiss\_Default\_Leaf
- Templates: modules/SwissFactory/templates \[271\]

- configuration\_list\_single.html, configuration\_list\_many.html, configurations.html, configuration\_string\_single.html, configuration\_string\_many.html, configuration\_delimited\_individual\_view.html, configuration\_list\_single\_view.html, configuration\_delimited\_single\_individual.html, configuration\_delimited\_single.html, configuration\_delimited\_many.html, configuration\_delimited\_individual.html, swiss\_factory\_view.html, configuration\_string\_many\_individual.html, configuration\_string\_many\_individual\_view.html, configuration\_string\_single\_view.html, configuration\_list\_many\_view.html, configuration\_noindex\_string\_many\_individual.html, configuration\_noindex\_string\_many\_individual\_view.html, configurationGroup\_default.html, configuration\_options.html, swiss\_factory\_edit.html, configuration\_noindex\_string\_many.html, configurationGroups.html, configuration\_boolean\_single\_view.html, configuration\_boolean\_single.html, configuration\_main.html
- Modules: modules/SwissFactory/modules \[272\]

- swissConfig, swissMagic
- Css: modules/SwissFactory/css \[273\]

## tasks-roles

This describes version 4.0.0 of the module Tasks and Roles (tasks-roles)

- Source: i2ce/modules/Pages/modules/TasksAndRoles \[274\]

- Description: Provides administator interface to define tasks and role
- Requirements:

- pages at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Pages/modules/TasksAndRoles/configs \[275\]

- Templates: modules/Pages/modules/TasksAndRoles/templates \[276\]

- roles\_and\_tasks\_view\_all\_roles.html, roles\_and\_tasks\_edit\_role.html, roles\_and\_tasks\_view\_all\_tasks.html, roles\_and\_tasks\_view\_all\_tasks\_each.html, roles\_and\_tasks\_view\_all\_roles\_no\_edit.html, roles\_and\_tasks\_menu.html, roles\_and\_tasks\_view\_all\_roles\_each.html, roles\_and\_tasks\_view\_all.html, roles\_and\_tasks\_edit\_task.html
- Classes: modules/Pages/modules/TasksAndRoles/lib \[277\]

I2CE\_Page\_TasksAndRoles

## template-data

This describes version 4.0.0 of the module Template Data (template-data)

- Source: i2ce/modules/TemplateData \[278\]

- Module Class: The module class is implemented by I2CE\_Module\_TemplateData
- Fuzzy Methods:

- Implements the method I2CE\_Page-&gt;setDataTypePriority() via setDataTypePriority()
- Implements the method I2CE\_Template-&gt;setDataTypePriority() via setDataTypePriority()
- Implements the method I2CE\_Page-&gt;setData() via setData()
- Implements the method I2CE\_Template-&gt;setData() via setData()
- Implements the method I2CE\_Page-&gt;getData() via getData()
- Implements the method I2CE\_Template-&gt;getData() via getData()
- Implements the method I2CE\_Page-&gt;getDefaultData() via getDefaultData()
- Implements the method I2CE\_Template-&gt;getDefaultData() via getDefaultData()
- Implements the method I2CE\_Page-&gt;removeData() via removeData()
- Implements the method I2CE\_Template-&gt;removeData() via removeData()
- Implements the method I2CE\_Page-&gt;getDataNames() via getDataNames()
- Implements the method I2CE\_Template-&gt;getDataNames() via getDataNames()
- Implements the method I2CE\_Page-&gt;ensureNode() via ensureNode()
- Implements the method I2CE\_Template-&gt;ensureNode() via ensureNode()
- Description: A module that allows you to associate arbitray types of data to any node of the template DOM
- Requirements:

- I2CE at least 4.0 and less than 4.1
- Paths:

- Modules: modules/TemplateData/modules \[279\]

- DisplayData, Options, Tags
- Classes: modules/TemplateData/ \[280\]

I2CE\_Module\_TemplateData

## user

This describes version 4.0.0 of the module User (user)

- Source: i2ce/modules/User \[281\]

- Description: Provides Users
- Requirements:

- I2CE at least 4.0.3 and less than 4.1
- Paths:

- Classes: modules/User/lib \[282\]

- I2CE\_User
- Modules: modules/User/modules \[283\]

UserAccess, UserAccess\_DHIS, UserAccess\_LDAP, UserAccess\_LDAP\_Hybrid

## References

\[1\] https://launchpad.net/i2ce \[2\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/BackgroundProcess \[3\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/BackgroundProcess/configs \[4\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/BackgroundProcess/templates \[5\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/BackgroundProcess/css \[6\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/BackgroundProcess/ \[7\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Binary\_Files \[8\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Binary\_Files/lib \[9\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Binary\_Files/sql \[10\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/CachedForms \[11\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/CachedForms/configs \[12\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/CachedForms/lib \[13\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/CachedForms/

templates \[14\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/ColorPicker \[15\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/ColorPicker/

scripts \[16\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/ColorPicker/

templates \[17\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/ColorPicker/css \[18\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/ColorPicker/ \[19\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports \[20\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/configs \[21\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/lib \[22\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/css \[23\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/images \[24\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/templates \[25\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/xml \[26\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules \[27\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/Export \[28\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/Export/

templates \[29\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/Export/lib \[30\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PDF \[31\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PDF/

templates

\[32\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PDF/lib \[33\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PieChart \[34\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PieChart/

configs \[35\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PieChart/

templates \[36\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PieChart/lib \[37\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/PieChart/css \[38\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/DatePicker \[39\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/DatePicker/scripts \[40\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/DatePicker/css \[41\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/DatePicker/ \[42\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/DisplayData \[43\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/DisplayData/ \[44\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields \[45\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/configs \[46\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/lib \[47\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/lib/fields

\[48\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/templates \[49\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/scripts \[50\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Fields/modules

\[51\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/FileDump \[52\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/FileDump/configs \[53\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/FileDump/ \[54\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Float \[55\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Float/lib \[56\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/FormWorm \[57\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/FormWorm/

scripts \[58\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/FormWorm/css \[59\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/FormWorm/ \[60\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/ \[61\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://I2CE\_config.inc.php \[62\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://I2CE\_structure.sql \[63\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://lib \[64\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://modules \[65\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://scripts \[66\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head://sql \[67\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/ImportExport \[68\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/ImportExport/sql \[69\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/ImportExport/lib \[70\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists \[71\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/configs \[72\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/lib \[73\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/templates \[74\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/sql \[75\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules \[76\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink \[77\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/configs \[78\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules \[79\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/ \[80\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToList \[81\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToList/configs \[82\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToList/ \[83\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToString \[84\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToString/configs \[85\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/Lists/modules/

ListLink/modules/ListLinkToString/ \[86\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/LocaleForm \[87\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/LocaleForm/configs \[88\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/LocaleForm/ \[89\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Login \[90\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Login/configs \[91\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Login/css \[92\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Login/lib \[93\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Login/templates \[94\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MimeTypes \[95\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MimeTypes/configs

\[96\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MimeTypes/lib \[97\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MimeTypes/mime \[98\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools

\[99\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/scripts \[100\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules \[101\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/ \[102\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Core \[103\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Core/scripts \[104\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Core/css \[105\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Core/ \[106\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/Options \[107\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/Options/ \[108\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/PrintedForms \[109\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/PrintedForms/

configs \[110\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/PrintedForms/lib \[111\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/PrintedForms/

images \[112\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/PrintedForms/

templates \[113\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/

ReportArchiver \[114\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/

ReportArchiver/configs \[115\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/

ReportArchiver/lib \[116\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/CustomReports/modules/

ReportArchiver/templates \[117\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/StretchPage \[118\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/StretchPage/lib \[119\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/StretchPage/

scripts \[120\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/StretchPage/css \[121\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/Tags \[122\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules/Tags/ \[123\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Timer \[124\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Timer/configs \[125\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Timer/ \[126\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/TreeSelect \[127\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/TreeSelect/

scripts \[128\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/TreeSelect/css \[129\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/TreeSelect/ \[130\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess \[131\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess/lib \[132\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess/sql \[133\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess/templates \[134\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_DHIS \[135\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_DHIS/lib \[136\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_DHIS/sql \[137\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_DHIS/

templates \[138\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_LDAP \[139\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_LDAP/

lib \[140\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/UserAccess\_LDAP/

templates \[141\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/

UserAccess\_LDAP\_Hybrid

\[142\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/

UserAccess\_LDAP\_Hybrid/lib

\[143\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules/

UserAccess\_LDAP\_Hybrid/templates \[144\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/UserForm \[145\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/UserForm/configs \[146\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/UserForm/lib \[147\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/UserForm/templates \[148\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/YAML \[149\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/YAML/lib \[150\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/YAML/xml \[151\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin \[152\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/configs \[153\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/lib \[154\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/templates \[155\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/modules \[156\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/css \[157\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/scripts \[158\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/images \[159\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Debugger \[160\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Debugger/scripts \[161\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Debugger/

images \[162\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Debugger/css \[163\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/Debugger/ \[164\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FieldLimits \[165\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FieldLimits/lib \[166\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FieldLimits/

templates \[167\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormLimits \[168\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormLimits/lib \[169\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormLimits/

templates \[170\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormBrowser \[171\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormBrowser/

configs \[172\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormBrowser/lib \[173\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormBrowser/

templates

\[174\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormBrowser/css \[175\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormDocumentor \[176\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormDocumentor/

lib \[177\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormDocumentor/

images \[178\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormRelationship \[179\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormRelationship/

lib \[180\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormRelationship/

templates \[181\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormRelationship/

css \[182\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms \[183\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/configs \[184\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/lib \[185\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/templates \[186\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/scripts \[187\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules

\[188\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage \[189\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/lib

\[190\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules \[191\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageCSV \[192\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageCSV/lib \[193\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageSDMXHD \[194\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageSDMXHD/lib \[195\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageEntry \[196\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageEntry/lib \[197\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageEntry/sql \[198\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageEval \[199\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageEval/lib \[200\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageFile \[201\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageFile/lib \[202\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageFlat \[203\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageFlat/lib \[204\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageMagicData \[205\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageMagicData/lib \[206\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageMultiFlat \[207\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageMultiFlat/lib \[208\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageXML \[209\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Forms/modules/FormStorage/

modules/FormStorageXML/lib \[210\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Jumper \[211\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Jumper/images \[212\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Jumper/css \[213\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Jumper/ \[214\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector \[215\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector/lib \[216\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector/

images \[217\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector/

Flags.xml \[218\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector/

configs \[219\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/LocaleSelector/

templates \[220\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/FlashCharts \[221\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/FlashCharts/maani\_charts

\[222\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/FlashCharts/scripts \[223\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/FlashCharts/ \[224\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser

\[225\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser/

configs \[226\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser/

scripts \[227\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser/

templates \[228\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser/

css \[229\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/MagicDataBrowser/ \[230\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MagicDataExport \[231\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MagicDataExport/xml \[232\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MagicDataExport/ \[233\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/MenuSelect \[234\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/MenuSelect/

scripts \[235\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MooTools/modules/MenuSelect/ \[236\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageBox \[237\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageBox/scripts \[238\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageBox/css \[239\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageBox/ \[240\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler \[241\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules \[242\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/ \[243\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageNotice \[244\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageNotice/scripts \[245\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageNotice/css \[246\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageNotice/images \[247\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/MessageHandler/modules/

MessageNotice/

\[248\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/ModDocumentor \[249\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/ModDocumentor/lib \[250\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/modules/

ModulePrompter \[251\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Admin/modules/

ModulePrompter/lib \[252\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages \[253\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/configs \[254\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules \[255\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/templates \[256\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/lib \[257\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub \[258\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub/configs \[259\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub/scripts \[260\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub/images \[261\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub/css \[262\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/Stub/ \[263\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissConfig

\[264\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissConfig/

configs \[265\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissConfig/

lib

\[266\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissMagic \[267\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissMagic/

configs \[268\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules/SwissMagic/

lib \[269\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory \[270\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/lib \[271\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/templates \[272\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/modules \[273\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/SwissFactory/css \[274\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/TasksAndRoles \[275\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/TasksAndRoles/

configs \[276\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/TasksAndRoles/

templates \[277\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/Pages/modules/TasksAndRoles/lib \[278\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData \[279\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/modules \[280\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/TemplateData/ \[281\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User \[282\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/lib \[283\] http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.0.6-release/files/head:/modules/User/modules
