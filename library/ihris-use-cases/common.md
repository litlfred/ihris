---
title: "iHRIS Common use cases (2009)"
source: uploads/ihris-use-cases/iHRISCommonUseCases.doc
licence: owner permission, 2026-09-23 (see ihris-use-cases.json)
---

# iHRIS Common: use cases (2009)

*Serlio Software Case Complete, 7/13/2009 3:33 PM. From the iHRIS use-case model by IntraHealth International / the Capacity Project iHRIS team, published here with the owner's permission. Parsed by `src/tools/ingest_use_cases.py`; do not edit by hand.*

These are use cases and requirements shared by multiple iHRIS products.

- Core version 3.1 released August 15, 2008. *(9/29/2008)*
- Core version 4.0 released July 13, 2009. *(7/13/2009)*

Related documents: https://launchpad.net/ihris-common

## Actors

### A-ICE1 System Administrator

The System Administrator has complete access and control over the HRIS and supporting hardware and software systems; installs, supports and troubleshoots the software; and creates and manages access accounts for all users.

**Goals**

- Install and configure the system for use.
- Add and update user accounts.
- Define report relationships and create reports.

**Notes**

- This is the same as the System Administrator role for iHRIS Plan, iHRIS Manage and iHRIS Qualify.
- Can perform any use case and view all data entered in the system.
- All system developers should have a System Administrator login.

**Use cases:** UC-ICE7 Add a user account, UC-ICE1 Configure modules, UC-ICE14 Create a report relationship, UC-ICE20 Export data, UC-ICE19 Import data, UC-ICE8 Update a user account

### A-ICE2 Data Manager

This person manages the database, creates standard data lists and oversees data entry.

**Goals**

- Spot-check records for errors and oversee data quality.
- Correct erroneous data.
- Define reports and report views for users to access.

**Notes**

- This role is equivalent to the HR Manager in iHRIS Manage, the Data Operations Manager in iHRIS Qualify and the Health Workforce Planner in iHRIS Plan.

**Use cases:** UC-ICE16 Add a report view, UC-ICE6 Correct data, UC-ICE15 Create a report

### A-ICE3 Data Analyst

This person generates reports in the system for the purposes of analyzing data.

**Goals**

- Define and generate reports to analyze data entered in the system.

**Notes**

- This role is equivalent to the Health Workforce Planner in iHRIS Plan, the Executive Manager in iHRIS Manage or the Decision Maker in iHRIS Qualify.

**Use cases:** UC-ICE17 Run a report

### A-ICE4 Any User

A generic user (applies to all users of the system).

**Goals**

- Access the system by logging in or out.
- Retrieve a forgotten password.
- Change a password.
- Give feedback.
- Search for and view a record.
- Update and save records.
- Run a standard report.
- Uses the Windows-based iHRIS Suite.

**Use cases:** UC-ICE11 Change password, UC-ICE12 Give feedback, UC-ICE25 Install sample data, UC-ICE18 Install the Windows version, UC-ICE9 Log in, UC-ICE13 Log out, UC-ICE10 Retrieve a password or username, UC-ICE2 Save a record, UC-ICE3 Search for a record, UC-ICE5 Update a record, UC-ICE4 View a record

## 1.1 System-wide

System-wide actions that do not apply to any other package.

- Documentation needs to be written for the following configuration functions: Browse Magic Data; Manage Locales; Background Processes; and Cached Forms. To be included in the System Administrator manual. *(7/29/2008)*

### UC-ICE1 Configure modules

The System Administrator configures modules that will be used by the system.

| | |
|---|---|
| Priority | P7 |
| Primary actors | System Administrator |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** Hardware and supporting software have been set up properly. There is a network connection. The system files have been installed. The database connection has been established. The System Administrator account has been created.

**Success guarantee.** The system is configured and can be used. Modules, configuration options and roles perform as configured.

**Main success scenario**

1. The user accesses the configuration screen.
2. The user selects the system to configure sub-modules for: Manage, Qualify or Plan.
3. The user selects the modules to install.
4. The system installs each selected module.
5. The system enables, or turns on, each new module.
6. The user selects the modules to turn off or disable.
7. The system de-activates the selected modules.
8. The user selects a module to configure.
9. The system displays the configuration options for that module.
10. The user sets the desired options for that module.
11. The user saves the configuration.
12. The system activates the options that the user has selected.

**Extensions**

- **3.a** The user does not install any modules.
    1. Skip to Step 6.
- **6.a** The system determines that a module is required to be enabled for the system to operate.
    1. The system does not allow the module to be disabled.

**Notes**

- This use case is identical for iHRIS Plan, iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- This functionality can be accessed through the Configure System --> Configure Modules menu option. *(2/7/2008)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE2 Save a record

The system confirms that data are entered correctly and all required data have been entered before saving that data.

| | |
|---|---|
| Priority | P6 |
| Primary actors | Any User |
| Level | Subfunction |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** Data have been entered into a data entry form. The user must be logged in to the system.

**Success guarantee.** The data are validated and saved to the database.

**Main success scenario**

1. The system validates that all required fields have been completed.
2. The system displays the data that the user entered.
3. The user corrects any errors.
4. The user confirms that the data are correct.
5. The system saves the data to the database.
6. The system logs the date and the username of the person who filled out the record.
7. The system displays the last modified date with the affected record.

**Extensions**

- **1.a** The user does not complete a required field.
    1. The system prompts the user to complete the field and will not continue.
- **3.a** The user does not make any corrections.
    1. Skip to Step 4.

**Notes**

- The use case is the same for iHRIS Plan, Manage and Quailfy. *(10/31/2007)*
- This use case is triggered when the Confirm button is clicked. *(10/31/2007)*
- Updated: Dual data entry actions have been removed from this use case, as we have chosen not to support dual data entry in the system. *(7/24/2008)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE3 Search for a record

The user searches for a record that has been entered in the system.

| | |
|---|---|
| Priority | P4 |
| Primary actors | Any User |
| Level | User |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The record has been entered in the system. The user must be logged in to the system.

**Success guarantee.** The record is found and displayed.

**Main success scenario**

1. The user selects the option to search records.
2. The user selections the type of record to search for.
3. The user enters the name of the item to search for.
4. The user selects any filters to limit the search.
5. The system displays the matching records.

**Extensions**

- **3.a** The user does not enter a name.
    1. The system finds all records.
- **4.a** The user does not select a filter.
    1. The system searches all records.
- **5.a** The system does not find a matching record.
    1. The system displays an error message.
- **5.b** The system locates more than one matching record.
    1. The system displays all matching records.

**Notes**

- This use case is the same for iHRIS Qualify, Plan and Manage, although search fields may differ between the two systems. *(10/31/2007)*
- These functions are found via the Search Records menu option on Manage and Qualify, and via Manage Projections --> Find Projection on Plan. *(7/25/2008)*
- Searching is done by creating a report. *(6/29/2009)*
- In iHRIS Manage, Positions and Staff can be searched. Search can be limited to Nationality, Facility or Department. *(6/29/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE4 View a record

The user displays a record and all the data entered for it.

| | |
|---|---|
| Priority | P6 |
| Primary actors | Any User |
| Level | Subfunction |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The record exists in the system. The user is logged into the system.

**Success guarantee.** The record is displayed to the user, along with any actions the user can take based on the user's role.

**Main success scenario**

1. The user searches for a record (UC-ICE3).
2. The user selects the record to view.
3. The system checks the role of the user.
4. The system displays the record and all the data entered for it that the user is authorized to view.
5. The system provides options for updating or adding new data depending on the user's role and the level of data already entered in the record.

**Notes**

- This use case is the same for iHRIS Manage, Plan and Qualify. *(10/31/2007)*
- Employees can only view their own record, Supervisors can only view records of employees they supervise, and Managers can only view records of employees they manage. *(10/31/2007)*
- This functionality is accessed by clicking on a person's name. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE5 Update a record

When a change in information is reported, the user updates the system with that information.

| | |
|---|---|
| Priority | P6 |
| Primary actors | Any User |
| Level | User |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 2.0 |

**Preconditions.** The record has previously been entered in the system. The user must be logged in to the system. The user must have the access privileges required to edit the record.

**Success guarantee.** The record is updated with the correct information and the previous information is saved for validation purposes.

**Main success scenario**

1. The user opens the record to update.
2. In the record, the user selects the option to update specific information.
3. The system checks the user's role.
4. The user changes the appropriate fields.
5. The user saves the record (UC-ICE2).
6. The system logs the date of the update.
7. The system marks all changed data as "updated."
8. The system saves the previously entered information in that item's history log.
9. The system displays the new data and the date of the most recent update with the record.

**Extensions**

- **3.a** The user's role does not allow the user to update the information.
    1. The system does not provide the option to update the record.

**Notes**

- In iHRIS Manage, position and salary information cannot be updated. It must be corrected by an HR Manager. *(2/7/2008)*
- This use case is the same for iHRIS Manage, Plan and Qualify. *(2/11/2008)*
- In iHRIS Plan, a record is updated by adding new data; new data cannot be added to a record for the same year as data that have already been entered. *(8/5/2008)*
- This use case has been updated to specify that the date of the update should be logged and displayed. *(2/11/2009)*
- This functionality is accessed via the Update This Information link on a record (Manage and Qualify). *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.2 User Administration

Create, update and disable user accounts to enforce secure access to the system.

- Access is limited to the System Administrator. *(10/30/2007)*
- Locate these functions via the Configure System --> Administer Users link on the main menu. *(10/30/2007)*

### UC-ICE7 Add a user account

The System Administrator creates a user account so the user can log on to the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | System Administrator |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The user account is created; the new user can log in and work on the system.

**Main success scenario**

1. The user selects the option to create a new user account.
2. The user enters a username for the new user.
3. The user enters the name of the new user, if known:
    - first name
    - surname
4. The user enters an email address for the new user (optional).
5. The user selects the option to generate a random password or enter a new password for the new user.
6. If the password is entered, the user re-enters it to confirm.
7. The user selects the role of the new user.
8. The user saves the record (UC-ICE2).
9. The system enables the user account and permits a log in with that username and password.
10. The system sends an email message to the user with the username and password.

**Extensions**

- **4.a** The user does not enter an email address.
    1. The system does not email the user information to the user.
- **5.a** The user enters the new password but does not re-enter it.
    1. The system prompts the user to re-enter the password and will not proceed.
- **5.b** The system determines that the two passwords do not match.
    1. The system displays an error and prompts the user to re-enter the password.
- **6.a** The user does not select a role.
    1. The system marks the new user as disabled and does not permit the new user to log in with that username and password.
- **7.a** The system determines that the username is already in the system.
    1. The system displays an error message and will not proceed.

**Notes**

- This use case applies to iHRIS Plan, iHRIS Manage and iHRIS Qualify. *(10/30/2007)*
- This functionality is accessed via the Configure System --> Administer Users screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `user` (I2CE_User_Form) in i2ce, `user` in ihris-common, `user` in ihris-manage

### UC-ICE8 Update a user account

The system administrator changes the details for a user account or closes the account.

| | |
|---|---|
| Priority | P10 |
| Primary actors | System Administrator |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user account has been created. The user must be logged in to the system.

**Success guarantee.** The account information is changed or the account is disabled so that the user cannot access the system.

**Main success scenario**

1. The user selects the option to manage user accounts.
2. The system displays all user accounts.
3. The user selects the user account to change.
4. The system displays the user account information.
5. The user makes any changes.
6. The user saves the record (UC-ICE2).
7. The system saves the changes to the user account.

**Extensions**

- **5.a** The user selects No Access for the user role.
    1. The system disables the account or gives it Guest access.

**Notes**

- This use case is the same for iHRIS Plan, iHRIS Qualify and iHRIS Manage. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Users screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `user` (I2CE_User_Form) in i2ce, `user` in ihris-common, `user` in ihris-manage

## 1.3 User Access

General actions that the user can perform to access and use the system.

### UC-ICE9 Log in

The user logs in to authenticate his/her access to the system and role and to perform any other task.

| | |
|---|---|
| Priority | P6 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** A user account for the user has been created.

**Success guarantee.** The user can successfully log in and perform actions appropriate for his/her role.

**Main success scenario**

1. The user connects to the system.
2. The user enters the username and password.
3. The system validates the username and password.
4. The system determines the user's role and displays that role to the user.
5. The system displays a list of actions the user can perform based on the user's role.

**Extensions**

- **3.a** The system determines that the password is incorrect for the username entered.
    1. The system prompts the user to re-enter the password.
    2. The system provides the option to retrieve a forgotten password.
- **3.b** The system determines that the username does not match a username for any account.
    1. The system displays an error message.
- **4.a** The system determines that the user has no role assigned in the system.
    1. The system does not allow access.

**Notes**

- This use case is similar for iHRIS Plan, Manage and iHRIS Qualify, although there may be some additional role actions in Manage. *(10/31/2007)*
- This functionality is accessed via the home page. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE10 Retrieve a password or username

If the user has forgotten a password or username, s/he can generate a new one.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user has a user account on the system.

**Success guarantee.** The user is able to retrieve the password or username and log in to the system.

**Main success scenario**

1. From the login page, the user selects the option to retrieve a forgotten username or password.
2. To reset the password, the user enters their username.
3. The system emails the new password to the user.
4. To recover the username, the user enters their email address.
5. The system displays the username.

**Extensions**

- **2.1.a** The system does not find the user's email address in the database.
    1. The system displays an error message.
- **3.a** The system does not find the user's email address in the database.
    1. The system cannot recover the username and displays an error message.

**Notes**

- The use case is identical for iHRIS Manage, Plan and Qualify. *(10/31/2007)*
- This functionality is accessed via the home page (Forgot password or username link). *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE11 Change password

A user can change his/her own password for logging into the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** A user account has been created for the user. The user must be logged in to the system.

**Success guarantee.** The user resets his/her password and can use it to log in to the system.

**Main success scenario**

1. The user selects the option to change the password.
2. The user enters the current password.
3. The user enters the desired new password.
4. The user re-enters the new password.
5. The system resets the password.

**Extensions**

- **4.a** The system determines that the passwords do not match.
    1. The system displays an error and prompts the user to re-enter the passwords.

**Notes**

- This use case is identical for iHRIS Plan, Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Change Password screen. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE12 Give feedback

The user provides feedback on a specific page in the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged into the system.

**Success guarantee.** The feedback is captured and emailed.

**Main success scenario**

1. The user selects the option to give feedback.
2. The system captures the system form that is open.
3. The system captures the username and role of the user who is logged in.
4. The system opens the feedback form.
5. The user enters their name and contact information.
6. The user enters questions or comments.
7. The user indicates whether they would like to be contacted.
8. The user sends the form.
9. The system emails the form to a feedback address including information about the system form the user was working on when they provided the feedback, the username and the user role, plus the date and time the form was submitted.
10. The system logs the contents of the feedback form.

**Notes**

- This use case is identical for iHRIS Plan, Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Feedback button. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE13 Log out

The user logs out of the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user is logged in to the system.

**Success guarantee.** The user can no longer perform any actions without logging back in.

**Main success scenario**

1. The user selects the option to log out.
2. The system displays the login page.
3. The system disables the user from accessing any actions in the system.

**Notes**

- This use case is the same for iHRIS Plan, Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Log Out button in the upper right corner of any screen. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.4 Reporting

Reports enable analysis of human resource data in various ways. Customize, display and print staff lists, statistical charts and other standard reports.

- Access these functions via the Configure System link on the main menu of iHRIS Manage or iHRIS Qualify. *(10/30/2007)*
- The custom report-building tool was released in version 3.1. *(7/24/2008)*
- Reports may be implemented differently in iHRIS Plan. *(7/24/2008)*
- Creating custom reports is complicated, and most functions are limited to System Administrators. These functions will be fully documented in the System Administrator's manual. *(8/11/2008)*

Related documents: http://open.intrahealth.org/wiki/index.php/Customizing\_Reports

### UC-ICE14 Create a report relationship

The System Administrator creates a relationship between forms for defining reports.

| | |
|---|---|
| Priority | P10 |
| Primary actors | System Administrator |
| Level | User |
| Complexity | High |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The user must be logged in.

**Success guarantee.** The report relationship is defined and made available for creating reports.

**Main success scenario**

1. The user selects the option to create a report relationship.
2. The user enters a name, display name and description of the report relationship.
3. The user selects the system forms that will be used in the report.
4. The user enters a name and description of each joined form.
5. The user defines any limits for the selected fields.
6. The user defines any functions necessary for the report relationship.
7. The user saves the report relationship.
8. The system makes the defined report relationships available for building reports.

**Extensions**

- **3.a** The relationship has already been defined.
    1. The user can edit, copy or delete the relationship.
- **6.a** The function has already been defined.
    1. The user can edit or delete the function.

**Notes**

- This use case applies to iHRIS Manage, Qualify and Plan. *(8/11/2008)*
- This use case has not been implemented in iHRIS Plan and may not be. *(8/11/2008)*
- This functionality is accessed via the Configure System --> Report Relationships screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE15 Create a report

The Data Manager designs a report using the data contained within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Data Manager |
| Level | User |
| Complexity | High |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** Some data have been entered into the system. The report relationship to be used for the report has been defined. The user must be logged in to the system.

**Success guarantee.** The user can specify the report fields and generate a report that includes all of the desired data.

**Main success scenario**

1. The user selects the option to create a report.
2. The user enters a name for the report.
3. The user selects the defined report relationship to base the report on.
4. The user creates the report.
5. The system displays those selection fields and functions taken from the report relationship that contain data.
6. The user selects the data fields and functions to include in the report.
7. The user specifies the limit options for each data field (optional).
8. The user specifies the link options for each data field (optional).
9. The user enters the header text to display for the field.
10. The user saves the report.
11. The system makes the report available for creating report views.

**Extensions**

- **9.a** The user does not enter a header.
    1. The system takes the header from the field name.

**Notes**

- This use case is probably the same for iHRIS Plan, Qualify and Manage. *(10/31/2007)*
- The blueprint for the customizing report procedure was written and posted to the wiki. *(10/31/2007)*
- This function has not been implemented in iHRIS Plan and may not be. *(8/5/2008)*
- This functionality is accessed via the Configure System --> Reports screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE16 Add a report view

The Data Manager creates a new view of a report to display the data differently.

| | |
|---|---|
| Priority | P1 |
| Primary actors | Data Manager |
| Level | User |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 3.1 |

**Preconditions.** Some data have been entered into the system. The user must be logged in to the system. The report relationship and report have been defined.

**Success guarantee.** The user can create the report view to display the appropriate data.

**Main success scenario**

1. The user selects the report views option.
2. The system displays all saved reports and their views.
3. The user adds a view for the desired report.
4. The user enters a name for the view.
5. The user enters a description of the view.
6. The user selects whether to display the total number of rows in the view.
7. The user selects the fields to display.
8. For each field, the user selects whether to aggregate and display the total.
9. The user selects which roles are authorized to access the report view.
10. The user saves the view.
11. The system makes the view available under the report and enables the user to run the report (UC-ICE17).

**Extensions**

- **3.a** The view already exists.
    1. The user case edit or delete the view.

**Notes**

- This use case applies to iHRIS Manage, Plan and Qualify. *(7/30/2008)*
- This is a new use case for the customized reports functionality. *(7/30/2008)*
- This function has not been implemented in iHRIS Plan and may not be. *(8/5/2008)*
- The use case was updated to specify that roles should be associated with report views, so that some reports may be restricted. This has not been implemented. *(2/11/2009)*
- This functionality can be accessed via the Configure System --> Report Views screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE17 Run a report

The user runs a report to answer a policy question.

| | |
|---|---|
| Priority | P1 |
| Primary actors | Data Analyst |
| Level | User |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 3.1 |

**Preconditions.** Some data have been entered into the system. The user must be logged in to the system. The report relationship, report and a view for the report have been defined.

**Success guarantee.** The user can successfully run a report to answer a policy question.

**Main success scenario**

1. The user selects the report views option.
2. The system displays all saved reports and their views that the user is authorized to view based on the user's role.
3. The user selects the report view from the list to display.
4. The user selects limits for the report.
5. The system displays the requested report, including all selected limits and the date the report was generated.
6. The system provides the option to:
    - convert the report to a chart
    - export the data from the report
    - format the report for printing
7. The user clicks a linked item in the report.
8. The system displays the full record for the item.

**Extensions**

- **4.a** The user does not select any filters.
    1. The system displays all report data.
- **4.b** The user selects more than one filter.
    1. The system applies all filters to the report.
- **5.a** The user enters new data into the database to display in the report.
    1. The system downloads and displays the most recent dataset in the report.

**Notes**

- This use case applies to iHRIS Manage, Plan and Qualify. *(10/31/2007)*
- Some roles may be limited in the reports they can run; this will be decided for each system individually. *(2/7/2008)*
- System Administrators, data managers and executive managers/decision makers can always access all reports. *(2/7/2008)*
- Use case updated for custom reports, which includes the ability to program report views. *(7/30/2008)*
- This function has not been implemented in iHRIS Plan and may not be. *(8/5/2008)*
- The use case was updated to specify that the system checks the role before displaying the report. *(2/11/2009)*
- This functionality can be accessed via View Reports or via Configure System --> Report Views. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.5 Data Management

Import and export data for use in other instances of iHRIS or in another system. These functions are primarily intended to be use to send standard data from a centralized server to implementations at the district or facility level, and to regularly update the centralized server with record changes from the district or facility level for reporting.

Related documents: http://open.intrahealth.org/mediawiki/Import\_and\_Export\_Data

### UC-ICE19 Import data

A user imports data from another instance of the system, such as from a district or facility office to the central location.

| | |
|---|---|
| Priority | P10 |
| Primary actors | System Administrator |
| Level | User |
| Status | Full |
| Implementation status | Complete |
| Release | 4.0 |

**Preconditions.** An exported file of data from another instance of the system is available for importing. The user is logged in.

**Success guarantee.** The data are imported and can be viewed and updated in the system.

**Main success scenario**

1. The user selects the option to import a site.
2. The user selects the dataset to import (such as people records, position records, facility records, standard data lists).
3. The system imports the data and saves it to a temporary table.
4. The system displays a report of the imported data.
5. The user checks for duplicate records (UC-ICE26).
6. The user verifies the imported data.
7. The system merges the imported data into the current dataset.

**Extensions**

- **6.a** The user does not verify the imported data.
    1. The system deletes the imported data and returns the dataset to its state before the import began.

**Notes**

- This use case applies to iHRIS Manage and Qualify. *(12/12/2008)*
- Data for import are grouped by type. To import all data from a system may require multiple separate imports. *(12/12/2008)*
- Import Data functions are found under Configure System --> Cached Forms. *(6/29/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE20 Export data

The user exports data to a file for import into another instance of the system, for example to export centrally managed data to an instance installed at a district office or facility.

| | |
|---|---|
| Priority | P10 |
| Primary actors | System Administrator |
| Level | User |
| Complexity | High |
| Status | Full |
| Implementation status | Complete |
| Release | 4.0 |

**Preconditions.** Data have been entered or imported into the system. The user is logged in.

**Success guarantee.** The data file is correctly exported and can be imported into another instance of the system.

**Main success scenario**

1. The user selects the option to export the site.
2. The user selects the type of data to export.
3. The system exports all of the selected data.
4. The system notifies the user when the exported data file is ready.
5. The user selects the location to save the file.
6. The system saves the file to that location.

**Notes**

- This use case applies to iHRIS Manage and Qualify. *(12/12/2008)*
- Data for export are grouped by type. To export all data from a system may require multiple separate exports. *(12/12/2008)*
- The Export function is located under Configure System --> Browse Magic Data. *(6/29/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.6 Data Quality

Enables HR Managers to check and correct data entered by HR Staff and evaluate whether data are being entered correctly. Also incorporates other data quality functions, such as merging duplicate records.

- This module previously included dual data entry, which we have decided not to include in the core system. Legacy use cases have been retained. *(7/24/2008)*
- Spot-checking has not been implemented in any system. *(7/24/2008)*

Related documents: http://open.intrahealth.org/wiki/index.php/Dual\_Data\_Entry\_Procedure

### UC-ICE6 Correct data

The Data Manager corrects any data previously entered in the system if those data are found to be incorrect or incomplete.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Data Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The information to be corrected has been entered in the system. The user must be logged in to the system. The user must be assigned a role that is allowed to correct data in the system.

**Success guarantee.** The record is overwritten with the correct information and is marked as corrected. The date and username of the person correcting the record is logged.

**Main success scenario**

1. The user opens a record.
2. The user selects the option to correct information in the record.
3. The system checks the user's role.
4. The user changes the appropriate fields.
5. The user saves the record (UC-ICE2).
6. The system marks all changed fields as "corrected".
7. The system displays the record with the corrected information.
8. The system logs that the record has been checked and the username and date of the person who made the corrections.

**Extensions**

- **3.a** The user does not have a role at the data or system administrator level.
    1. The system does not provide the option to correct the record.

**Notes**

- In iHRIS Manage, only position and salary information requires correcting by an HR Manager; all other data can be updated by HR Staff. *(2/7/2008)*
- This use case is the same for iHRIS Manage, Plan and Qualify. *(2/11/2008)*
- In iHRIS Qualify, the following types of data can only be corrected by the Data Operations Manager: deployment, out migration, training, examination, registration, license, continuing education, private practice license and disciplinary action. *(7/25/2008)*
- Only Data Operations Managers, HR Managers, Health Workforce Planners and System Administrators can correct information. *(7/25/2008)*
- In iHRIS Plan, correcting information overwrites previously entered data; to add additional data for another year, the Add New Data option must be selected instead. *(8/5/2008)*
- This functionality is accessed via the Correct This Information link on a record (Manage and Qualify). *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.7 Windows Version (Offline Tool)

The offline tool provides a working Windows Installer for a standalone version of the software so that it can be used to enter data and run reports on a Windows desktop without being connected to a server or network.

Related documents: http://open.intrahealth.org/wiki/index.php/Offline\_iHRIS

### UC-ICE18 Install the Windows version

A user installs the offline tool on a local computer.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Any User |
| Level | User |
| Status | Updated |
| Implementation status | Complete |
| Release | 3.0 |

**Preconditions.** The user has downloaded the installer program to his or her local computer.

**Success guarantee.** The offline tool is installed successfully and all functions of the system become available to the user.

**Main success scenario**

1. The user starts the installer.
2. The system opens the installation wizard.
3. The user starts the installation.
4. The user accepts the license agreement.
5. The user selects which components to install.
6. The user selects the folder where the program will be installed.
7. The user enters an SMTP server and email address (optional).
8. The user selects whether the software should run on the local network or desktop.
9. The user sets the port numbers for the web server and database.
10. The user enters a database password.
11. The user creates Quick Launch and/or Desktop icons for the installation.
12. The system installs the files on the user's computer.
13. The system launches the software program in the user's default browser.
14. The system provides the option to launch Plan, Manage or Qualify.

**Extensions**

- **\*.a** The user cancels the installation.
    1. The system stops the installation and exits the installer.
- **4.a** The user does not accept the license agreement.
    1. The system provides only the option to cancel the installation, not to continue the installation.
- **6.a** The user does not select a folder.
    1. The system installs to the default folder.
- **7.a** The user does not enter a SMTP server or email address.
    1. The system prompts the user to accept the default values and continue the installation.
- **9.a** The user does not enter the port numbers.
    1. The system prompts the user to accept the default values and continue the installation.
- **13.a** The user deselects the option to launch the software after finishing the installation.
    1. The system does not launch the software.
- **14.a** A component was not installed.
    1. The system does not provide the option to launch that component.

**Notes**

- A Windows computer is required for the offline tool only. *(1/31/2008)*
- The login account is also set up as username admin and password admin. *(1/31/2008)*
- The user has full System Administrator access to the offline tool and its data. *(1/31/2008)*
- An offline version of iHRIS Plan is now available; use case has been updated for this and some other new features available in version 3.1. *(10/3/2008)*
- Use case is updated with name change to Windows iHRIS. *(11/20/2008)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-ICE25 Install sample data

The user can install data in the offline version for demonstration purposes.

| | |
|---|---|
| Priority | P7 |
| Primary actors | Any User |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** Offline iHRIS has been installed with at least one component of iHRIS (Plan, Manage or Qualify).

**Success guarantee.** Offline data selected by the user is loaded into Offline iHRIS and can be seen in dropdown menus and reports.

**Main success scenario**

1. The user launches Windows iHRIS.
2. The user selects one of the components to launch.
3. The system displays the login page with the administrator login credentials.
4. The user logs in as the administrator.
5. The system prompts the user to load sample data.
6. The user selects the sample datasets to load.
7. The system loads the selected data and makes that data available when using Windows iHRIS.

**Notes**

- This is a new use case to fulfill the sample data requirement for version 3.1. *(10/3/2008)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

## 1.8 Requirements

This package holds miscellaneous requirements for the project.

### REQ-ICE1 Cadres

Cadres refer only to health professionals. Non-health professionals should not be included in a cadre.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE2 Technology requirements

The system must run on an Apache web server running Linux with PHP and a MySQL database. A web browser--IE 5+, Firefox, Safari--is required to use the system.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE3 Multilingual support

The system should be able to support translation of all commands and instructions into multiple languages.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE4 Log usage

Log which pages are viewed, by whom and when so system usage data can be reported.

| | |
|---|---|
| Priority | P7 |

### REQ-ICE5 Leveragability

If the system is being used in conjunction with other systems in the suite, common functionality should be shared among all systems to reduce redundancy; for example, user accounts should only be defined once for all systems in use.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE6 Integratability

The system should be able to exchange data with the other iHRIS systems.

| | |
|---|---|
| Priority | P7 |

### REQ-ICE7 Idle logout

If the user is idle for a certain period of time, the person is automatically logged out by the system.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE9 Extensibility

The system should be extensible to other modules to be developed.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE10 Data reliability

Data errors are more highly tolerated in ongoing use of the system than in mass entry of historical data. The system's functions support the highest level of data quality and reduction of errors/duplication.

| | |
|---|---|
| Priority | P7 |

### REQ-ICE11 Compatibility

As much as is known, data fields should configure to standards set by global bodies such as WHO and the HR/professional licensing industry in general, to ensure better compatibility with other HR systems.

| | |
|---|---|
| Priority | P1 |

### REQ-ICE12 Caching of report data

All reports are cached for faster display. Caches can be updated manually by the user (after adding data, for instance) and will automatically regenerate on a periodic basis to ensure that the displayed data are up to date.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE13 Authorization

All user accounts have an assigned role that determines which actions the user can perform within the system. All non-authorized data and actions are hidden from the user. Role access is described in the use cases.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE14 Auditing

All user actions need to be logged for auditing purposes: record username, date and time the action was taken, the number of the record being modified, the name of the table being modified, the code number if there is a unique one for that table, and a note about the type of modification.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE15 Archival

All data should be archived indefinitely. Data can only be deleted through the database by a System Administrator. Archived data must be available for reporting functions.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE16 Authentication

Users must be authenticated via username and password before they can access any system actions or data.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE18 User error reporting

Error alerts should provide meaningful messages to users when an error or bug is encountered.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE20 Customized Roles

The user can create roles and assign tasks to them to create customized roles.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE22 Geographical locations

There are four levels of geographical location: country --> region --> district/state/province --> county/sector. At least one region is required for each country. At least one district is required for each region.

| | |
|---|---|
| Priority | P10 |

### REQ-ICE23 Customization

The system should be easily customizable with regard to field names, fields that are displayed, etc., to easily adapt to different organization's HR procedures. For example, field names should be linked to alternates so that they can be changed globally. Fields that are not used can be disabled.

| | |
|---|---|
| Priority | P10 |

## Cited but not described

The report cites these, but describes none of them:

- UC-ICE26 (cited by UC-ICE19)
