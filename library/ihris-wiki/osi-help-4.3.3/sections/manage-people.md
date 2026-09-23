---
title: "Manage People"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_manage_people.html
  - ihris-manage/modules/manage-help/static/help/ihris_manage_people_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_manage_people.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_manage_people_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Manage People

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

Click Manage People to add a new employee or applicant record to the system. If you are using the job application module, you can also complete applications for open positions, review completed applications and assign a position to the successful applicant.

## Add Person

To track a person in the database, whether an employee or a job applicant, add a record for that person by clicking the Add Person option. Certain information is required to start a new record. Once the record is generated, additional options for adding data about the person will become available. Either an HR Staff person or an HR Manager can add a new person to the system.

|  |  |
| --- | --- |
| On the Home page or in the left side menu, click Manage People. Click Add Person. |  |
| The Add Person form opens. Enter the person's **Surname**, **First Name** and any **Other Names** in the appropriate fields.    Select the person's **Nationality** from the menu.    Type or select the name of the person's country, region and district of residence under **Residence**.    Click `Confirm`. |  |
| The data that you just entered will appear. Confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The person's new record opens with options to add additional information divided into sections.    Note that you can click the Hide/Expand option at the top of any section to hide or display that section. You can edit or update a person's record at any time by searching for the record (see [Search Records](ihris_search_records_in_ihris_manage.html "Search Records in iHRIS Manage")). |  |

### Troubleshooting

**An error message displays when the Confirm button is clicked.**

Make sure all required fields have been completed. Required fields will be outlined in red. Fill in the missing information and try saving again. If you do not want to add a new record after all, click `Return (do not save changes)`.

**An error message appears when the name is entered.**

There may be another record in the system with the same first name and surname. The system will provide a link to the matching record to review. If the records are for the same person, the original record may be updated with any new information by clicking that link. If the records are for different people, check the box to ignore the error and confirm the new record.

**The nationality is not available for selection.**

The HR Manager must add the nationality as a country (see [Add a country](ihris_add_geographical_areas.html#Add_a_Country "Add Geographical Areas")).

**The correct residence is not available for selection.**

The HR Manager must add the country, region and district before they can be selected (see [Add geographical areas](ihris_add_geographical_areas.html "Add Geographical Areas")).

## Set Position

Immediately after an employee has been added to the system, the employee's record displays. The next step is to set the position that the employee will fill. Until the position has been set, the employee will not appear in any current employee lists. The employee's position must have been created in the system and have been designated as open (the position is not filled by another employee or discontinued).

If an employee leaves a position and is not assigned a new one, that employee is considered an "old employee" who has left the organization. However, the employee may return to work in a new position. In that case, also follow these steps to set a position for the old employee.

|  |  |
| --- | --- |
| From the employee's record, click Set Position under the "Individual Information" section. |  |
| The Make a Job Offer form opens.    Under **Position**, either type or select the position code and title of the open position that the employee will fill.    The **Start Date,** the date that the employee started work in that position, is set to today's date by default. Select a new date from the menu if the start date is different.    Under **Salary**, select the currency that the employee is paid in and enter the salary that the employee is paid.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The new position information will appear in the employee's record in the "Position Information" section. Click the position title to view information about that position. |  |

### Troubleshooting

**The Set Position option does not appear for an old employee.**

The Job Application module is enabled. Complete an application form for the employee (see Add an Application) and then make a job offer for that employee to set the position (see [Make a Job Offer](ihris_manage_job_applicants.html#Make_a_Job_Offer "Manage Job Applicants")). Alternatively, the System Administrator can disable the Application module, and the Set Position option will become available (see [Disable the Application Module](ihris_administer_the_system.html#Disable_the_Application_Module "Administer the System")).

**An error message appears when Confirm is clicked.**

Make certain that a position has been selected and the salary has been entered. All required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to set a position after all, click `Return (do not save changes)`.

**There is no open position to set for the employee.**

The position must be created in the system and marked open before it can be assigned to an employee (see [Add a position](ihris_administer_positions.html#Add_Positions "Administer Positions")).

**The correct currency is not available for selection.**

The currency must be added to the system by an HR Manager (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
