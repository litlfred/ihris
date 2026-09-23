---
title: "IHRIS Role List (4.0.6)"
source: http://open.intrahealth.org/w/index.php?oldid=33753
contributors: ["Litlfred"]
pages: 354-355
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Role List (4.0.6)

This is a list of all the roles available in the iHRIS System

## admin

The role Administrator is defined in the module pages of the package I2CE.

- Can perform the following tasks: cached\_forms\_can\_administer, custom\_reports\_admin, printed\_forms\_admin, custom\_reports\_archiver\_admin, tasks\_and\_roles\_admin

## exec\_manager

The role Executive Manager is defined in the module ihris-manage of the package iHRIS Manage.

- Any of the tasks that a Executive Manager can perform can be performed by any the following roles: Administrator
- Can perform the following tasks: custom\_reports\_can\_view\_reportViews, can\_change\_own\_password, person\_can\_view\_child\_forms, can\_view\_database\_list\_position, can\_view\_database\_list\_job

## hr\_manager

The role HR Manager is defined in the module ihris-manage of the package iHRIS Manage.

- Any of the tasks that a HR Manager can perform can be performed by any the following roles: Administrator
- Can perform the following tasks: custom\_reports\_can\_access\_reports, custom\_reports\_can\_edit\_reportViews, custom\_reports\_can\_view\_reportViews, can\_edit\_all\_database\_lists, person\_can\_edit, person\_can\_edit\_child\_forms, users\_can\_edit, person\_can\_change\_child\_form\_salary, person\_can\_change\_child\_form\_person\_position, can\_change\_own\_password, can\_edit\_all\_planning\_database\_lists, establishment\_can\_edit

## hr\_staff

The role HR Staff is defined in the module ihris-manage of the package iHRIS Manage.

- Any of the tasks that a HR Staff can perform can be performed by any the following roles: Administrator,HR Manager

- Can perform the following tasks: can\_view\_all\_database\_lists, custom\_reports\_can\_view\_reportViews, person\_can\_edit\_child\_form\_person\_scheduled\_training\_course, person\_can\_view\_child\_form\_person\_scheduled\_training\_course, competency\_can\_view\_history, person\_can\_view\_child\_forms, person\_can\_edit\_child\_form\_application, person\_can\_edit\_child\_form\_benefit, person\_can\_edit\_child\_form\_dependent, person\_can\_edit\_child\_form\_employment, person\_can\_edit\_child\_form\_education, person\_can\_edit\_child\_form\_person\_id, person\_can\_edit\_child\_form\_nextofkin, person\_can\_edit\_child\_form\_notes, person\_can\_edit\_child\_form\_person\_competency, person\_can\_edit\_child\_form\_person\_contact\_emergency, person\_can\_edit\_child\_form\_person\_contact\_other, person\_can\_edit\_child\_form\_person\_contact\_personal, person\_can\_edit\_child\_form\_person\_contact\_work, person\_can\_edit\_child\_form\_person\_position, person\_can\_edit\_child\_form\_position\_decision, person\_can\_edit\_child\_form\_position\_interview, person\_can\_edit\_child\_form\_salary, person\_competency\_can\_view\_evaluation\_history, can\_edit\_database\_list\_department, can\_edit\_database\_list\_facility, can\_edit\_all\_manage\_positions\_database\_lists, can\_configure\_system, can\_change\_own\_password, person\_can\_edit\_child\_form\_accident, can\_edit\_database\_list\_accident\_type,

person\_can\_edit\_child\_form\_disciplinary\_action, can\_edit\_database\_list\_disciplinary\_action\_type, can\_view\_recent\_forms

## training\_manager

The role Training Manager is defined in the module ihris-manage of the package iHRIS Manage.

- Any of the tasks that a Training Manager can perform can be performed by any the following roles: Administrator,HR Manager
- Can perform the following tasks: custom\_reports\_can\_view\_reportViews, can\_edit\_database\_lists\_training, can\_edit\_scheduled\_training\_course, person\_can\_view\_child\_form\_person\_scheduled\_training\_course, person\_can\_edit\_child\_form\_person\_scheduled\_training\_course, person\_can\_view\_child\_forms, person\_scheduled\_training\_course\_can\_edit\_evaluation, can\_change\_own\_password, can\_configure\_system
