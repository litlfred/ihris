# I2CE modules and data model in iHRIS 4.3.3

*Generated from the checksum-verified `ihris-suite-4.3.3.tar.bz2`. Do not edit by hand.*

| instance | modules | with description | form classes | fields | sites |
|---|---|---|---|---|---|
| [`i2ce`](../../src/i2ce/README.md) | 129 | 113 | 12 | 29 |  |
| [`ihris-common`](../../src/ihris-common/README.md) | 115 | 115 | 93 | 334 |  |
| [`ihris-manage`](../../src/ihris-manage/README.md) | 78 | 73 | 26 | 124 | Demo, TwitterBootstrap, blank |
| [`ihris-qualify`](../../src/ihris-qualify/README.md) | 29 | 27 | 25 | 98 | Demo, blank |

## i2ce: top-level modules

| module | name | description |
|---|---|---|
| `BackgroundProcess` | Background Processes | A convenience module to allow the running of process in the background |
| `CustomReports` | Custom Reports | Custom Reports |
| `ImportExport` | Import Export Support | Enables an XML Import and Export tool which allows offline access. |
| `Mailer` | Mailer | Wrapper for PEAR Mail module |
| `MimeTypes` | Mime Types | Adds a in mime type capabilities |
| `MooTools` | MooTools | MooTools javascript library |
| `OpenLayers` | Open Layers Mapping | The OpenLayers library for creating interactive maps. |
| `Timer` | I2CE Timer | Adds a timer class |
| `YAML_spyc` | YAML | YAML parser provided by spyc.  Also enabled processing of .YAML config files |
| `forms` | I2CE Forms | Adds a few basic forms to the system as well as some form functionality to the template |
| `i2ce-site` | Site | Marker for I2CE Site |
| `jumper` | Page Jumper | Creates a page jumper for elements of a page. |
| `maani-charts` | Charted Reports | Configuration options for the Maani chart reporting software http://www.maani.us/charts |
| `magicDataExport` | Magic Data Export | Export Magic Data |
| `messageHandler` | Message Handler | A handler for user messages |
| `pChart` | pChart Charting | Configuration options for the pChart chart reporting software http://www.pchart.net/ |
| `pages` | Pages | Provides pages, Users and Templates |
| `permissions` | Permission System | A module that enables role and task based permissions |
| `swissfactory` | Swiss Factory | The Swiss Factory Magic Data Editing System |
| `template-data` | Template Data | A module that allows you to associate arbitray types of data to any node of the template DOM |
| `user` | User | Provides Users |
| `web-services` | Web Services | Provides Web Services |
| `yaml_magicdata(unnamed)` |  |  |

## ihris-common: top-level modules

| module | name | description |
|---|---|---|
| `CEUs` | CEUs | Makes Continuing Education Unit (CEU) information available to the system |
| `CSD` | Care Services Discovery (CSD) | Holds base CSD modules |
| `Calendar` | Calendar | An abstract page for displaying a calendar |
| `Contact` | Contact | Makes Contact information available to the system |
| `Currency` | Currency | Makes Currency information available to the system |
| `DHIS-Dashboard` | DHIS Dashboard | Integrate DHIS Dashboard into iHRIS |
| `DHIS_Metadata` | DHIS Metadata | Makes DHIS Meta Data such as organizational Units information available to the system |
| `Document` | Document | Makes Document information available to the system |
| `FHIR` | FHIR Services | Holds various FHIR based modules |
| `Facility` | Facility | Makes Facility information available to the system |
| `Geography` | Geography | Makes Geography information available to the system |
| `Person` | Person | Makes Person information available to the system |
| `Photo` | Photo | Makes Photo information available to the system |
| `SDMX-HD-CodeLists` | SDMX-HD Code Lists | Information to load SDMX-HD Code Lists. |
| `SVS` | Sharing Value Sets (SVS) Repository | Allows publishing of lists as SVS according to http://www.ihe.net/Technical_Framework/upload/IHE_ITI_Suppl_SVS_Rev2-1_TI_2010-08-10.pdf |
| `SampleData-Common` | iHRIS Common Sample Data | Sample Data for iHRIS Common forms. |
| `UUID_map` | UUID Map | Allows administrator to associate a UUID with any form id |
| `UserAlerts` | User Alerts | A module that enables assigning an alert to a user to be seen on an alert page. |
| `UserCronReports` | User Cron Reports | A module that enables assigning a report view to a user to be sent at regular intervals. |
| `UserStatistics` | User Statistics | User Statistics page and updates for user view page. |
| `UserTriggers` | User Triggers | A module that enables assigning a trigger to a user to be notified when the trigger is called. |
| `establishment` | iHRIS Manage Establishment | The iHRIS Manage Establishment provides establishment information by cadre |
| `ihris-common-Cadre` | iHRIS Commone Cadre | The iHRIS Manage Job |
| `ihris-common-Job` | iHRIS Common Job | The iHRIS Common Job |
| `ihris-common-RecentForm` | Recent Form Page | The iHRIS Recent Form page. |
| `ihris-common-Search` | Search Page | The iHRIS Search page. |
| `simple-competency` | Simple Competency | A simple two-tiered compotency module |
| `training-course` | Training Course | Adds functionality to add training courses to the system |
| `training-institution` | Training Institution | Adds basic training institution and funder functionality |

## ihris-manage: top-level modules

| module | name | description |
|---|---|---|
| `ManageAccessDepartment` | Manage Access Department | A module that enables permission based on assigning a department and any positions that belong to that department. |
| `ManageAccessFacility` | Manage Access Facility | A module that enables permission based on assigning a facility or the geographic region where a facility is and any positions that belong to that facility. |
| `ManageAccessSupervisor` | Manage Access Supervisor | A module that enables permission based on assigning a department and any positions that belong to that department. |
| `ManageDashboard` | iHRIS Manage Dashboard | A module for configuring iHRIS Manage Dashboard |
| `ManageRegistration` | iHRIS Manage Registration | A Person's Registration Details |
| `ManageSelfService` | iHRIS Manage Self Service |  |
| `PersonAttendance` | iHRIS Manage Person Attendance | A Person's Attendance |
| `SampleOpenLayers` | Sample Open Layers Mapping | Sample Open Layers page for examples and testing. |
| `accident` | Workplace Accident | A Workplace Accident Tracking Module |
| `change-position` | Change Position | Add simple page to create and change to a new position. |
| `disciplinary_action` | Disciplinary Action | A Disciplinary Action Tracking Module |
| `ihris-manage-Application` | iHRIS Manage Application | The iHRIS Manage Application Module. |
| `ihris-manage-AutoList` | iHRIS Manage Auto List Configuration | iHRIS Manage Auto List |
| `ihris-manage-Benefit` | iHRIS Manage Benefit | The iHRIS Manage Benefit module provides basic benfit related information |
| `ihris-manage-CustomReports` | iHRIS Manage Custom Reports | The Manage Reporting System |
| `ihris-manage-CustomReports-FilledPositions` | iHRIS Manage Filled Positions Reports | The Manage Report for Filled Positions |
| `ihris-manage-CustomReports-facility-reports` | iHRIS Manage Facility Reports | The Manage Reports based on the Facility relationship. |
| `ihris-manage-CustomReports-position-reports` | iHRIS Manage Position Reports | The Manage Reports based on the Position relationship |
| `ihris-manage-CustomReports-search-people` | Custom Reports - Search People | The definition of the search people report for Manage. |
| `ihris-manage-CustomReports-staff-reports` | iHRIS Manage Custom Staff Reports | The Manage Staff Reports |
| `ihris-manage-FacilityTree` | Facility Tree Report | This module defines the facility_tree report and configures the position facility field to use this report for displaying the tree to speed up generation of thi |
| `ihris-manage-Job` | iHRIS Manage Job | The iHRIS Manage Job |
| `ihris-manage-MassDeleteFacility` | Mass Delete by Facility | Facility report to list by positions and pages to do mass deletion of records by facility. |
| `ihris-manage-Person` | iHRIS Manage Person | The iHRIS Manage Person |
| `ihris-manage-PersonDemographic` | iHRIS Manage Person Demographic | The iHRIS Manage Person Demographic |
| `ihris-manage-PersonPosition` | iHRIS Manage Person Position | The iHRIS Manage Position. Adds a position which is linked to a person and is defined by a job, |
| `ihris-manage-PositionTree` | Position Tree Report | This module defines the position_tree report and configures the position supervisor field to use this report for displaying the tree to speed up generation of t |
| `ihris-manage-base-data` | iHRIS Manage Base Data | iHRIS Manage Base Data |
| `ihris-manage-confirmation` | iHRIS Manage Confirmation | The iHRIS Manage Confirmation module provides confirmation tracking |
| `ihris-manage-csd-qus` | CSD Query For Updated Services | CSD Query For Updated Services |
| `ihris-manage-help` | iHRIS Manage Help | The iHRIS Manage Help system. |
| `ihris-manage-mcsd-update-supplier` | mCSD Update Supplier | mCSD Update Supplier |
| `ihris-manage-medical-data` | iHRIS Manage Medical Base Data | iHRIS Manage Medical Base Data |
| `ihris-manage-sample-data` | iHRIS Manage Sample Data | iHRIS Manage Sample Data |
| `leave` | Leave | Leave Tracking Module |
| `manage-auto-page` | Manage Auto Pages |  |
| `manage-training-course` | Manage Traning Course | Makes the training course module available to iHRIS Manage |

## ihris-qualify: top-level modules

| module | name | description |
|---|---|---|
| `QualifySelfService` | iHRIS Qualify Self Service |  |
| `RecordVerify` | RecordVerify | Makes a record verification form available to the system |
| `ihris-qualify-CustomReports` | iHRIS Qualify Custom Reports | The Qualify Reporting System |
| `ihris-qualify-CustomReports-disruption` | Disruption relationship and reports | The relationship and reports for training disruptions. |
| `ihris-qualify-CustomReports-exam` | Exam Report and Relationship | Relationship and reports for exams. |
| `ihris-qualify-CustomReports-institution` | Training Insitution Reports | Relationship and reports for training institutions. |
| `ihris-qualify-CustomReports-license` | Qualify License Reports | License relationship and reports for Qualify. |
| `ihris-qualify-CustomReports-person` | Person Relationship and Reports | The relationship and reports for person. |
| `ihris-qualify-CustomReports-registration` | Registration Reports | Relationship and reports dealing with registrations. |
| `ihris-qualify-CustomReports-search-people` | Search People Report | The relationship and report for search people on the site. |
| `ihris-qualify-CustomReports-search-training` | Search Training Report View | The report view for searching trainings. |
| `ihris-qualify-CustomReports-training` | Qualify Training Reports | Reports based on trainings. |
| `ihris-qualify-PersonTraining` | PersonTraining | Makes a record verification form available to the system |
| `ihris-qualify-PrintedForms` | iHRIS Qualify Printed Forms | The Qualify Printed Forms |
| `ihris-qualify-base-data` | iHRIS Qualify Base Data | iHRIS Qualify Base Data |
| `ihris-qualify-csd-qus` | CSD Query For Updated Services (iHRIS Qualify) | CSD Query For Updated Services (iHRIS Qualify) |
| `ihris-qualify-help` | iHRIS Qualify Help | The iHRIS Qualify Help system. |
| `ihris-qualify-sample-data` | iHRIS Qualify Sample Data | iHRIS Qualify Sample Data |
