---
title: "Custom Reporting -- An Overview"
source: http://open.intrahealth.org/w/index.php?oldid=4351
contributors: ["Litlfred"]
pages: 51-51
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Custom Reporting -- An Overview

The Custom Reporting is a three part process:

- Create A Form Relationship This defines the relationship between the data in the system. It is intended for a relatively advanced user that has some understanding on how the data is related.
- Create A Report Choosing, a form relationship, this specifies the data fields for a report as well as the limits allowed for the various views of the report. It is intended for a data manager. Only a moderate understanding of the way the data is related in the system is required. It is in this step that generates the cached 'zebra\_XXXX' report tables.
- Create A Report View. This is intended for all end user's that might need to create a different view of a report. For example, it would be useful for someone who needs to generate monthly reports for different slices of the data.

## Tasks

There are a several tasks that control general access to the creation and view of custom reports:

- custom\_reports\_can\_access Allows minimal access to the Custom Reporting System System
- custom\_reports\_delete Allows deletion of data defining custom reports
- custom\_reports\_can\_access\_relationships Allows access to the Custom Report Relationships
- custom\_reports\_can\_access\_reports Allows access to the Custom Reports
- custom\_reports\_can\_view\_reportViews Allows view of the Custom Report Views
- custom\_reports\_can\_edit\_reportViews Allows editing of the Custom Report Views
- custom\_reports\_admin Administrator for custom reports. Can perform all tasks associated with custom reports

In addition you may also limit access to a specific Report View $view by specifying:

```
/modules/CustomReports/reportViews/$view/limit_report_to
```

to be any valid permission string.
