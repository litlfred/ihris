---
title: "IHRIS Ideas List"
source: http://open.intrahealth.org/w/index.php?oldid=29132
contributors: ["Lduncan", "Litlfred"]
pages: 188-191
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Ideas List

If you wish to work on any of these projects, you can contact us at our Project Communication page.

## iHRIS Core System Improvements

### Self Service

Difficulty: High

Mentor: TBD

This would be an expansion of the current role/task system that would allow person records in the system to login and have access to certain information about themselves or the people they supervise. The current access system is handled by tasks and roles. Certain pages and template content can only be seen by users who can do the associated tasks. With Self Service, the permission parser needs to be modified to allow checking for tasks based on the record that is being seen or modified. In some cases there may be multiple levels of checking such as a supervisor being able to modify records of all supervised employees or a facility manager being able to view all employees working in that facility.

### SDMX-HD

Difficulty: Medium

Mentor: TBD

SDMX-HD \[1\] is a data exchange standard for indicator definitions and data. iHRIS would like to support exporting aggregate (reporting) data to SDMX-HD for import into aggregate systems.

### Mobile Updates

Difficulty: High

Mentor: TBD

Build an interface that can work on various levels of mobile phones to interface with iHRIS. Perhaps using OpenRosa \[2\]. This would allow remote users to look up or make small data updates through SMS or over the Internet. This work would involve building the SMS gateway as well as creating an easy way for administrators to define pages that will be viewed and updated from the mobile application.

### Convert Configuration Data (MagicData) to MongoDB (or others?)

Difficulty: Low

Mentor: TBD

Build a faster interface for MagicData to save using MongoDB instead of MySQL to try to improve speed to this information since it is access so frequently. Will possibly need to retain mysql as a write storage mechanism so that magic data form storage remains fast.

### Form and Page Editors

Difficulty: High

Mentor: TBD

Build an administrative interface to allow customization of forms through the application instead of using module configuration files. Building on that, create an interface to define display and edit pages based on the existing forms so more customization work can be done through the application instead of manually editing XML configuration files. More information: Custom Forms and Custom Pages.

### Context Sensitive Help

Difficulty: Medium

Mentor: TBD

Set up more help links within the application so users can get direct access to help instead of having to find the relevant section in the manual. Perhaps even rewrite how the manual is used in the application.

### Web Services

Difficulty: High

Mentor: TBD

Build a web services interface so other applications can access and update allowed data without having to export/import at regular intervals.

### Write MagicData Objects as C

Difficulty: High

Mentor: TBD

Rewrite the MagicData PHP classes in C to speed up usage.

### Upgrade to PHP 5.3

Difficulty: Medium

Mentor: TBD

Take advantage of the new features available in PHP version 5.3 to iHRIS PHP 5.3 Clean Up clean up the code.

## iHRIS Modules

### Leave Tracking Module

Difficulty: Medium

Mentor: TBD

Add a module to iHRIS Manage to track an employees leave. If done in concert with Self Service this could allow employees to request and view leave details directly. This would involve working with users in other countries to make sure the specifications fit their needs as well as being able to generalize it for the core system.

### Mobile Roll-Call

Difficulty: Medium

Mentor: TBD

The Roll-Call module is an extension of mobile updates to allow supervisors or workers (i.e. community health workers) to log their activity.

### Organizational Chart

Difficulty: Medium

Mentor: TBD

Produce a org chart for iHRIS Manage that show employees and their supervisors. Could make use of the position report that has an employee and their supervisors Two main possibilities. Make it ajaxy and put everything on the client (maybe use canvas?), or produce org-charts on the server via graphviz.

### Job Application Questions

Difficulty: Low

Mentor: TBD

A module to ask applicants a series of standard questions \[3\]

## Reporting

### Replace Flash Charts with Images

Difficulty: Medium

Mentor: TBD

We would like to remove the Flash charts and replace it with images. This can be done using pChart \[4\] or anything similar.

### JavaScript Charts

Difficulty: Medium

Mentor: TBD

A second step would be to add the option for using Canvas \[5\] for the charts as well. We'd like to add some additional features to the reporting to allow more complex charts to view the data.

### General Reporting Improvements

Difficulty: Low

Mentor: TBD

There are also some smaller additions like displaying all the limits chosen for a particular report so it's clear what is being displayed and improving the interface for end users to work with reports. Interface improvements can also be made for the form relationship and report builder pages.

### Geographic / OpenLayers Reporting

Difficulty: High

Mentor: TBD

Incorporate OpenLayers \[6\] into the reporting system: Reports which are tagged with geo-data (e.g. Lat and Long coordinates for a facility) will have numeric and aggregate data for the report plotted on a map.

## Country Implementations

Difficulty: Varied

Mentor: TBD

Countries where iHRIS is installed may have additional needs for assistance on customizations and modules. Capacity Project's iHRIS Suite page has more information on countries where we work. Please contact us \[7\] if you're interested in this type of work.

## Non iHRIS Ideas

### Use Cases Wiki

Difficulty: High

Mentor: TBD

The iHRIS Project was built using use cases \[8\], but we would like a more open model to work on updates and customizations to our systems. This would be a module for a wiki (whichever seems best) that will allow easier editing of use cases so this work can be shared. It will make it easier for people making customizations to modify use cases for their purposes.

## References

\[1\] http://sdmx-hd.org/ \[2\] http://www.openrosa.org/ \[3\] http://www.capacityproject.org/hris/suite/UseCaseReport-iHRISManage.

htm#REQ-50251c96-e13a-463c-bb24-ec1b885949dfREQ-PT10

\[4\] http://pchart.sourceforge.net/ \[5\] http://en.wikipedia.org/wiki/Canvas\_element \[6\] http://openlayers.org/ \[7\] http://www.capacityproject.org/hris/contact/ \[8\] http://en.wikipedia.org/wiki/Use\_case
