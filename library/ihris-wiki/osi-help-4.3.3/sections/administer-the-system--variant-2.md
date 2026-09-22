---
title: "Administer the System"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_administer_the_system_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_administer_the_system_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Administer the System

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").** ***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

## Configure System

|  |  |
| --- | --- |
| Click Configure System on the main menu to access options for setting up and customizing iHRIS. Here is where you can administer the database (set up dropdown menus, configure modules that will be used in the system, export and import data, and create and update user accounts), manage reports, browse configuration data, examine background processes, control cached forms, and administer users. Only the System Administrator and the HR Manager can access the Configure System page. The Administrator can access all functions on this page, but the HR Manager can only access the Administer Database functions. |  |

The System Administrator manual (to be written) will contain extensive documentation for the following functions in the Configure System menu:

* Configure Modules

* Manage Reports

* Browse Magic Data

* Manage Locales

* Background Processes

* Cached Forms

See the section **Configure the Database for Use** under [iHRIS Manage](ihris_administer_database_for_ihris_manage.html "Administer Database for iHRIS Manage") or [iHRIS Qualify](ihris_administer_database_for_ihris_qualify.html "Administer Database for iHRIS Qualify") for help with administering the database. See [Administer User Accounts](ihris_administer_users.html "Administer Users") for help with administering users. See [The Customized Report Builder](ihris_create_reports.html "Create Reports") section for more information on managing reports.

## Configure Modules

|  |  |
| --- | --- |
| Click Configure Modules to enable new modules and customize all modules that have been installed for use in iHRIS. This page lists all modules that have been installed for the system, including those that were installed with the main software package and any modules you may have installed separately. Only the System Administrator can configure modules.    A checkbox appears beside most module names. If the checkbox is checked, the module is enabled, or turned on. Most modules are enabled by default. Click the checkbox to remove the check and disable the module, if it is not needed; you will then have to click the `Enable` button at the bottom of the page to save the change. The module can be re-enabled at any time by re-checking the box and clicking `Enable` again. Note that if the checkbox does not appear, the module is required for iHRIS to operate properly and cannot be disabled.    Beside most modules a Configure link appears. Click Configure to open a new screen showing all options for that module. These modules will change depending on the module that is selected. Use this page to customize settings for the module. |  |

## Disable the Record Verify Module

|  |  |
| --- | --- |
| **The Record Verify Module is currently available only in iHRIS Qualify.** By default, the Record Verify Module is turned on when iHRIS Qualify is installed. This module is optional and is intended to be used if the data manager wants to track verifications and updates to health worker records. If this functionality is not needed, it may be disabled to simplify the interface.  The System Administrator can disable this module in the Configure Modules page. To turn off the module, follow these steps:   1. Click Configure Modules. 2. Scroll down to the "Application" section and locate iHRIS Qualify. 3. Click Sub-Modules to the right of iHRIS Qualify. 4. Under the "Application Component" section, click the checkbox next to **RecordVerify**. 5. Scroll to the bottom of the page and click the `Enable` button. The module will be disabled, and record verification functions will no longer be available in the system (see Add a Verification for details). |  |

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").** ***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
