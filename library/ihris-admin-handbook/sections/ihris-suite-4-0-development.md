---
title: "IHRIS Suite 4.0 Development"
source: http://open.intrahealth.org/w/index.php?oldid=33708
contributors: ["Lduncan", "Litlfred"]
pages: 355-362
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Suite 4.0 Development

## Version 4.0.0

Released week of July 13, 2009.

## Version 4.0.2

Released November 13, 2009.

### Completed

- Custom reports/Form Limits -- allow you to sprecify the values that a limit can take in the getLimitMenu() and int he custom reports
- added fancy updater
- fixed up fatal errors so it provides a mailto form
- fixed up fatal errors so it is the same fancy level as the updater
- fixed bug in finding conflicts when installing optional modules
- fixes for custom report:

- charts -- now works w/o url rewritting enabled
- non-enabled fields are not longer displayed and sort order is preserved in a view
- fixed aggregation of fields
- add XML export (to non-standard but hopefully useful) format
- add command line option --force-restart=1 to force the restart of an install/update (used in conjunction with --update=1)
- add time stamp to PDF
- add form documentor as a CLI page
- Debug training module
- Ensure all templates are localized (done in 4.0.0)
- Cleanup ISCO-88 Job Codes (done in development for 4.0.1)
- Finish Flat Storage mechanism for forms.
- Add in Multi-Flat Storage mechanism for forms

- Fix this: http://www.2shared.com/file/6929841/7587e315/bad\_css.html
- Add cache stale times on a per form basis
- Add cache stale times on a per form storage mechanism basis

- Add ability to turn of form caching by background process
- Add cache stale times on a per report basis
- Add ability to turn of report generation by background process
- Change so that caching a report triggers the caching of the forms needed for the report if they are stale
- Change so that forced caching a report triggers forced caching of the forms needed for the report
- Replace I2CE\_Form::validate() mapped values check with something from I2CE\_List, e.g. monsterMash()
- separate form field validation logic into the appropriate modules
- fix bug in export of custom reports to html
- logout page now really logs out
- added command line option --clear\_cache=1 which will clear the magic data cache
- added special URL: $site\_url/clear\_cache.php which will clear the magic data cache, the apc cache and destroy the session
- fix limits for dates
- fix bug in setting the order in which fields are displayed in a report view
- fix bug in defining a form relationship when linking from a form.
- added index to string\_Value column of last\_entry table to speed of cache generation
- added in index on mapped fields in hippo\_tables to speed up report generation,
- fixed ie7 javascript errors that were causing problems for custom reports
- upgraded to mootools 1.2.3
- speed display of lists in administer database
- added a db-like version of magic data form storage which is used if the "permanent" magic data storage is in the config table (this causes localization support to be dropped from magic data)
- fixed issue for default display of custom reports where limits where lost when resorting the table
- Add paging for list display pages
- add photo upload
- add resume upload
- Fix bug with report views not displaying fields the first time you try to edit it
- Report limits with dates are being set to the current date by default
- Fix sort order of headers on report views
- Migrate iHRIS Qualify

## Version 4.0.3

Release in Friday March 5, 2010.

### Completed

- when editing a database list with a select field, not choosing a select field should display everything (e.g. not choosing the location to limit the facilities shows all the facilities)
- allow list members to be disabled so that they don't appear in the default drop-down menu.
- add option meta/form\_any so that a mapped field can take values in any form
- make the flat form storage mechanism writable as much as possible
- add a UUID module so that any form can be assigned a uuid via the form uuid\_map
- fixed up processing of &lt;eval&gt; tag for external module requirements
- fixed issue when classes were not loaded when a install was restarted
- added CSV form storage mechanism

- added eval form storage mechanism
- created locale form (via eval form storage) for selecting available/selectable locals

- Windows: allow relocatable paths so USB-Toolkit \[1\] will work
- added moveData()/exportData()/importData() for form storage mechanisms
- Add in different role/password authentifications for users

- DHIS users
- LDAP
- there is now an adminisitrtive user 'i2ce\_admin' whose password is the password used to access the db
- Mysql's unix socket often lives in /var/lib/mysql (or elsewhere), not /var/run/mysqld. (jstrope) -- fixed by adding intializeDSN() to I2CE class which allows you to pass a DSN. we can now handle RHEL setting the dsn if we ever package .rpms for it.
- Cleanup user and user\_form.
- Make iHRIS work out of the box on RHEL:

- Fedora has no /etc/timezone -- that info lives in /etc/sysconfig/clock (but you can't just do a file\_get\_contents on it -- has comments and dditional info and the time zones don't always match the format returned by date\_default\_timezone\_get) (jstrope)

- relevant Bug report \[2\] and here \[3\] and here \[4\]

- iHRIS didn't give much of an indication of why the initialization failed. If you had an error handler that said "set your date.timezone setting in php.ini", that would probably suffice. (jstrope)
- upgrade mootools to 1.2.4
- Remove all mootools' $ references from javascript dollar sage mode \[5\]

- Add workplace accident module to ihris manage
- Add disciplinary action module to ihris manage
- FormCache is smarter: forms are marked dirty when they are saved and clean when they are cached. this way we don't need to even bother trying to re-cache a form if it has not been saved since the last time it was cached.
- Magic Data Browser: the path is now a bunch of links so you can easily skip to the top.
- FormStorageEntry: flattened out the sub-query into a single query so that indices on last\_entry can be taken advantage of in a where clause
- modify limit templates to display differently for report view limits and relationship editing.
- function signatures fixed for validate() method of personPostion,application
- function signature fixed for filedump-&gt;display() and ajax\_text-&gt;display()
- function signature fixed for formfield\_currrency-&gt;createdomeditable()
- made collation utf8\_bin (instead of utf8\_general\_ci) across all columns in hippo tables (cuts report generation times by half)
- cleaned up code for setting default values for form fields (now lookup value is handled by MAP)
- added indices to entry table to speed up cached form generation (form\_field,string\_value) and (formfield,integer\_value)
- speed-up for getting max in int\_generate so that it uses the (formfied,integer\_value) index
- changed magic data to be stored in config\_alt table rather than config table to deal with:

- config table did not allow children with commas in their names
- performance was slowed as the size of the config table grew
- increase the speed when doing a join with a parent and child (form storage magic data)
- call page stretch when the page goes through an ajax update
- fix issues with the updater/configurator when moving to a new version of the software library while the old version stayed in the same place
- fixed issues with classes of dependent modules not being loaded on a module update

- added a 'Recent Forms' menu option to the search page so you can see which forms (e.g. person or position) have recently been edited/created. useful if they are not yet in the search report

- moved all of the SearchPages classes from manage and qualify into common with the search reports being displayed by magic data
- fixed error checking/null checking when getting the last modified time for a form stored in magic data
- allow to check the modification time on individual fields of a form or of the record for entry
- fixed pagination issues when view lists in the 'Administer database'
- Removed caching all forms from the generate\_complete background process since each form makes sure the required forms are cached. Removed the restriction of passing multiple forms to the generate custom reports command lin
- fixed header for CSS that was breaking Chrome and Safari
- various fixes of function signatures
- marked all translatable nodes in configuration .xml files.
- fixed up translation of .html and config .xml files from .mo files

## Version 4.0.4

### Completed

- Added memcached magic data storage to sit between APC and DB. Reduces load on DB and speeds up start-up time for background processes.
- Fixed issues with magic data storage and initialization not setting everything in DB storage.
- Module Configuration via SwissConifg now works (at least the basic parts)
- fixed prepared statement for config\_alt table that was problematic in mysql 5.0
- fixed PageStretch lowest element calculation when there were scrollable elements
- In fatal bugs, the mailto form now looks nicer and includes a full error trace.
- Fixed issue in loading in localized magic data from a delimited type... the loaded language would overwrite en\_US string.
- Added a play button for error messages.
- FormField Date\_YMD now uses the DatePicker \[6\] mootools script
- On module update load as many modules class paths as possible
- Fixed bug with reports not displaying when the default view displayed multiple columns but the selected view was only one.
- Modified flash charts to better display labels so the chart and labels aren't cut off.
- Added display of error message to raiseError when the error is about running out of memory.
- Added error message to charts and HTML views when the report hasn't been generated or the limits don't return any results.
- Reports: Change the buttons on reports to pull up the options window and remove the options link.
- Form documentor can now localize
- Added in checking to Multi-flat storage to see if desired databases exist
- Date Picker

- Defaults to decade
- Allows blank values
- Report date limits now use data picker
- Removed (Options) links for report buttons. now buttons will pop up the options menu
- fixup width of passport photos
- I2CE\_FormField\_Binary\_File -- filename and modtime are now stored.

## Version 4.0.5

### Completed

- Reports: When joining in a specific form on a mapped field which can take values in multiple forms, all values of the joined form are populated. E.g. joining district to facility on the location field will populate the district data if either the location maps to a district or a county
- Reports: speed improvements -- the parent form in a relationship is no longer joined in. Rather necessary data are read directly from the reports
- Form Relationships: Added the ability to get all the forms satisfying a relationship given the id of a primary form
- Added in the Printed Forms module with samples:

- iHRIS Manage: Staff Hire Letter
- iHRIS Qualify: Registration Form
- iHRIS Qualify: License
- Added the "Dependents Module" to iHRIS Common which was \[coded-in-country \[7\]\]
- cleaned up the required strings to translate for exported custom reports
- If you chose the non-default locale on the login page, then that user's locale is set on a successful login
- Cleaned up tasks and their descriptions
- Simple lists can now share a common html template
- Fixed various CSV form storage bugs
- Added some changes to smooth over transition to Ubuntu Lucid:

- Set default sessions path to /tmp if it has not been set
- die after display non-modified headers
- fixup pagination of html reports --- limit values were not being preserved
- MagicDataNode-&gt;setIfIsSet() now sets values based on set locale.
- Magic Data Browser -- shows locale that is being displayed.
- Magic Data Browser -- works better when editing translatable values
- Updated magic number data file
- Added SDMX-HD form storage to view SDMX-HD code lists as iHRIS forms.
- Added default link forms to be used to link lists to other lists as well as to string (for IDs) to map to other data standards if necessary.

## Version 4.0.6

Plan for release in August 2010

### Completed

- Add in "ancestral form" join condition on form relationships
- modification times are stored (and indexed) in the hippo\_XXXX tables (Done to support smaller size updates of databases to remote aggregating database)
- added next of kin module to ihris-common
- created a field container/field container factory which form/form factory sub class
- removed I2CE\_List class constants, MAIN\_FIELD, SEC\_FIELD, SORT\_FIELD and replaced with extended sprintf functionality stored magic data "/modules/forms/formClasses/$form/list/display/default/XXX"
- Have the I2CE\_List::listOptions() make use of the new sprintf data rather than implode('-',$vals)

- Add Report Archive module
- workaround MDB2 bug with \\0 terminated data in I2CE\_FormField\_Binary
- Added support to zip report exports

- FormStorage/Lists: allowed multiple fields to be checked against for uniquness by specifying a comma seperated list in the unqiue\_field. also made the error message a bit more useful if there is a non-uniqueness problem
- Added ability to upload XSLT to a report view that can be used to transform the .xml export (mostly done to export SDMX-HD)
- form relationships (SQL ONLY) allow ability to join on a child field which is mapped such that it traverses the linking data
- added in establishment module to iHRIS Manage
- added in sample data and sample report for establishment module (staffing norms 2010)
- Added module to archive Scanned Paper Records to a person
- Fixed bug w/ selected tree values not being preserved on a submit/confirm page for database lists
- Added ability to specify max document size in KB for a binary form field by setting /modules/forms/formClasses/$formClass/fields/$field/meta/max\_size\_kb
- Fixed issues w/ id field not being set/read from when loading forms from request variables
- added ability to create profiles of forms and to cache or mysqldump the forms based on the profiles
- added ability to delete default display for a custom report view
- added generic XML-based form storage mechanism
- added SDMX CrossSectionalData form storage mechanism
- when a list is read-only, then do not show the 'edit/update' link from the database lists page. instead go to the view list page.
- added gzip compression for report view export
- added bzip2 compression for report view export
- added arbitrary stream support for file based form storage mechanisms -- e.g. now you can read things across http:// not just the file system. In particular this applies to CSV, XML, and the SDMX-HD form storage mechanisms.
- mapped the user access mechanisms to a user form storage mechanism
- fixed bug with listing fields in the generic form storage mechansim
- split out Job and Cadre modules from Manage into Common. ManageJob remains w/ salary grade
- added Confirmation/Probationary work period module
- allow upload of meeting notes for position changes and interviews

## Outstanding

- Form Relationship:

- Allow for more complicated joins in a form relationship -- e.g. "secondary" conditions on ancestral forms. Done for SQL. Needs to be done for getFormsSatisfying()
- Allow for joining a child form in a relationship multiply (both in a report and in the getFormsSatisfying())
- handle joining "any" form and make joining forms clearer
- Add easy support for multiple platforms:

- Add tests to determine platforms, e.g. ie7, firefox, safari, chrome, mobile (which ones?)
- platform should be saved in a session variable
- Add support to the file search for platform specific files (e.g. for css). For example:

```
  <path name='css'>
  <!-- the default platform-->
  <value>./css/default</value>
</path>
<path name='css' platform='ie7'>
  <value>./css/ie7</value>
</path>
```

- Add support for "platform resolution." For example search for ie7, then ie then the default
- Field Containers

- Break up existing limits to separate modules for fields and relationships
- Add in form limits
- Standardized letters/forms:

- Add in return/view links for standardized letter menu
- Search results can be used to generate multiple letters at once
- add new display "table" which can loop through multiple child forms in a relationship

- Qualify: Use tasks for permission handling instead of roles for everything instead of just a few places.
- Manage: when a person passes a training course which has CEUs, those CEUS are added as a child form to that person.
- in the "Configure System" page, when the user's role is 'admin' provide a link to the 'Project Communication' page and 'Technical Documentation' page on the wiki. People are not finding this when they need to
- when a list is read-only, then do not show the 'edit/update' link from the database lists page. instead go to the view list page.
- allow way to see a list of the forms and their instances that a related to a particular form (parent-child or mapped value to a list)
- form storage entry should allow string id's not just unique integers across all forms stored in entry.
- the FormStorage::migrateForm() method should not create the named form in the entry table if it is not already present -- causes an issues with loading of the sample data b/c facility\_contact could for example be created in the FacilityContact module before the sample data defining facility contact is loaded.
- add in iso currencies to pre-populate currencies
- Display the limits that a report is currently set to on the report display.
- CSV/Excel report export -- add option to show metadata about what limits were chosen, when report was generated (ask Julie S.)
- Move all string from php to templates
- Add in Simply Joined mechanisim for forms to enable reading in data from openMRS style vertical tables.
- Review strings in .pot files to ensure that they translatable as sentences and rework templates/make printf substitutions as appropriate
- Fix-up selection list to be a tree for position+facility rather than a drop down list: we should be able to set position+facility to have default display fields 'facility+location:county:district:\[region\]:country' the problem is that currently, facility+location can take values in either the forms 'county' or 'district' and using the the above display fields string, we would only list the facilities whose location are a county.
- Custom Reports: when a form is componentized, add "easy" option to limit based on the components. e.g. show only the people within "Northern Region" Optionally define and use the metadata at /modules/forms/form\_storage/options/$storage/component/name
- Speedup validation of mapfields w/ unique\_field set to be something like 'country:region'
- Speedup I2CE\_List::monsterMash and I2Ce\_List::createDataTree

- short circuit and return once a match is found instead of getting all the matches
- If two successive forms have storage mechanisms subclassing I2CE\_FormStorage\_DB try to use a sub-select rather than process through PHP

- replace instances of foreach($something) { $this-&gt;template-&gt;appendTemplateFile('some.html',$appendNode);} with $add\_node = $this-&gt;template-&gt;loadHTMLFile('some.html'); foreach ($something) { $this-&gt;template-&gt;appendNode($add\_node-&gt;clone(true),$append\_node);}

- Add tasks to Qualify
- add in limits for dates where date is(requested form MVC):

- after a given time period from now (e.g. after 6 months pervious to now)

- period in months (as int)
- period in year (as int)
- before a given time period from now (e.g. after 6 months pervious to now)

- period in months (as int)
- period in year (as int)
- Training Sample data should be separated from Medical Sample Data. Currently ManageMedicalData enables SampleData-training\_course\_category which requires training-course.
- Add in MongoDB Magic Data Storage
- Modify Magic Data Storage to add a canonical/permanent flag so permanent storage will never be cleared. Add initialize option to choose MongoDB or DB to be used as permanent storage.

## References

\[1\] http://www.openhealthconsortium.org/wiki/doku.php?id=PHIT \[2\] https://bugzilla.redhat.com/show\_bug.cgi?id=469532 \[3\] http://trac.agavi.org/ticket/1008 \[4\] http://derickrethans.nl/distributions\_please\_dont\_cripple\_php\_or\_red\_hat\_stop\_fucking\_around.php \[5\] http://mootools.net/blog/2009/06/22/the-dollar-safe-mode/ \[6\] http://www.monkeyphysics.com \[7\] http://www.capacityproject.org/hris/blog/index.php/2010/05/tanzania-advances-use-of-hr-management-software-part-1/
