---
title: "Add an Application"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_add_an_application.html
  - ihris-manage/modules/manage-help/static/help/ihris_add_an_application_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_an_application.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_an_application_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Add an Application

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

## Add Application

A job application can be added for any person in the system. Adding a job application puts the person in consideration for any open position. Records with a completed job application that do not already have a set position are considered "applicants" rather than employees of the organization. Employees with a set position can also have a job application on file for open positions, to manage internal hiring efforts. Until the applicant has applied for an open position, the applicant will not appear in any applicant lists. The applicant may only apply for positions that have been created in the system and have been designated as open (the position is not filled by another employee or discontinued).

If your organization does not need to track job applications, the Application module can be disabled by the System Administrator (see [Disable the Application Module](ihris_administer_the_system.html#Disable_the_Application_Module "Administer the System")).

|  |  |
| --- | --- |
| In the person's record, click Application in the left menu to jump to the "Application" section of the record. Click Add Application. |  |
| The Application form opens.    Under **Position(s)**, select the open position that the applicant is applying for; select more than one position by holding down the CTRL key while clicking each position.    Complete as many of the other **Applicant Questions** as are applicable.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The completed application displays in the person's record. Now managers and HR personnel can review the application, make notes about the interview process and hiring decision, and make a job offer to the applicant. The application will remain on file even after the position is filled, but it can be updated at any time by clicking Update This Information. |  |

### Troubleshooting

**The Add Application option does not appear.**

The Application module may be disabled. Consult your System Administrator (see [Disable the Application Module](ihris_administer_the_system.html#Disable_the_Application_Module "Administer the System")).

**An error message appears when Confirm is clicked.**

Make certain that a position has been selected for the application. The position is required. Other applicant questions may also be required. All required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to add an application after all, click `Return (do not save changes)`.

**No positions are available.**

There must be at least one open position that the applicant can apply for. To create an open position, add a new position and mark it as open (see [Add positions](ihris_administer_positions.html#Add_Positions "Administer Positions")), open a previously discontinued position (see [Discontinue a position](ihris_administer_positions.html#Discontinue_a_Position "Administer Positions")) or if the position is filled by another employee, record a position change (see [Record a position change](ihris_add_position_information.html#Record_a_Position_Change "Add Position Information")) or departure (see [Record a departure](ihris_add_position_information.html#Record_a_Departure "Add Position Information")) for that employee.

## Log Interview Details

While an applicant is under review, record details about any interviews with the applicant.

|  |  |
| --- | --- |
| In the person's record, click Application in the left menu to jump to the "Application" section of the record. Click Log Interview Details. |  |
| The Position Interview form opens.    The **Date of Interview** is set to today's date by default. If this is incorrect, change it.   Enter the names or titles of **People Conducting Interview**.    Enter any **Comments** about the interview (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The details of each interview are displayed in the person's record under the "Application" section and can be reviewed at any time. Update these details by clicking Update This Information.    Repeat the process for each additional interview. |  |

### Troubleshooting

**This option is not available.**

The Application module may be disabled. Consult your System Administrator (see [Disable the Application Module](ihris_administer_the_system.html#Disable_the_Application_Module "Administer the System")).

**An error message appears when Confirm is clicked.**

Make certain that the required fields have been completed. All required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to log an interview after all, click `Return (do not save changes)`.

## Log Hiring Decision

While an applicant is under review, log the details of the decision made concerning the job application. Note that if the applicant is hired, the position will also need to be set for the applicant in addition to logging the decision (see [Make a job offer](ihris_manage_job_applicants.html#Make_a_Job_Offer "Manage Job Applicants")).

|  |  |
| --- | --- |
| In the person's record, click Application in the left menu to jump to the "Application" section of the record. Click Log Hiring Decision. |  |
| The Position Decision form opens.    The **Date of Decision** is set to today's date by default. If this is incorrect, change it.    Under **Make a Job Offer?** select Yes or No. This will not set the new position. That needs to be done in a separate step (see [Make a job offer](ihris_manage_job_applicants.html#Make_a_Job_Offer "Manage Job Applicants")).    Enter any **Comments** about the decision (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The hiring decision details are displayed in the person's record under the "Application" section and can be reviewed at any time. Update these details by clicking Update This Information. |  |

### Troubleshooting

**This option is not available.**

The Application module may be disabled. Consult your System Administrator (see [Disable the Application Module](ihris_administer_the_system.html#Disable_the_Application_Module "Administer the System")).

**An error message appears when Confirm is clicked.**

Make certain that all the required fields have been completed. All required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to log a decision after all, click `Return (do not save changes)`.

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
