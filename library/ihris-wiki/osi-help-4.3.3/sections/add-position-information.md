---
title: "Add Position Information"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_add_position_information.html
  - ihris-manage/modules/manage-help/static/help/ihris_add_position_information_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_position_information.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_position_information_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Add Position Information

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

## Add a Benefit or Special Payment

If an employee receives an irregular or one-time benefit or special payment -- such as an allowance, travel advance or relocation payment -- in addition to the regular salary, that can be noted in the employee's record under the employee's Position Information.

|  |  |
| --- | --- |
| In the employee's record, click Position Information in the side menu to jump to the "Position Information" section. Click Add Benefit/Special Payment. |  |
| The Benefits form opens.    Select the **Benefit Type**.    Select the **Source** of the payment.    Select the **Currency** for the payment and enter the **Amount**.    Select the **Start Date** of the payment.    Select the **End Date** of the payment.    Select the **Recurrence Frequency** of the payment: once, weekly, monthly or yearly. If the frequency is set to "once," the start date and end date should be the same or the end date may not be entered.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The information that you just entered displays in the employee's record under the "Position Information" section. Additional benefits or special payments can now be added. For each new benefit, click Add Add Benefit/Special Payment and follow these same steps. If any of the benefits information needs to be changed, click Update This information beside the incorrect benefit to edit it. |  |

### Troubleshooting

**An error message displays when the Confirm button is clicked.**

Make sure that all of the required fields have been completed. The required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to add a special payment after all, click `Return (do not save changes)`.

**The correct benefit type is not available for selection.**

The benefit type must be added to the system by an HR Manager (see [Add benefit type](ihris_administer_database_for_ihris_manage.html#Add_a_Benefit_Type "Administer Database for iHRIS Manage")).

**The correct source is not available for selection.**

The source must be added to the system by an HR Manager (see [Add salary sources](ihris_administer_positions.html#Add_Salary_Sources "Administer Positions")).

**The correct currency is not available for selection.**

The currency must be added to the system by an HR Manager (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

## Record a Departure

When an employee leaves the employment of the organization, the date of and reason for departure should be recorded in the employee's record. The employee will become an inactive (or "old") employee in the system, but the employee's data will still be available for historical reporting.

|  |  |
| --- | --- |
| In the employee's record, click Position Information in the side menu to jump to the "Position Information" section. Under the position, click Record a Departure. |  |
| The Record a Departure form opens.    The **End Date** for employment is set to today's date by default. If that is not correct, change the date.    Select the **Reason for Departure**.    Select the **New Status** for the position: Open or Discontinued; if the position is marked "Open," it will be available for assignment to another employee or applicant.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.    The information that you just entered displays in the employee's record under the "Position Information" section. |  |

### Troubleshooting

**An error message is displayed when the Confirm button is clicked.**

Make sure that all the fields have been completed. Required fields are outlined in red. Fill in any missing information and try saving again. If you do not want to record a departure after all, click `Return (do not save changes)`.

**The reason for departure is not available for selection.**

The HR Manager must add the reason for departure to the system (see [Add a reason for departure](ihris_administer_database_for_ihris_manage.html#Add_a_Reason_for_Departure "Administer Database for iHRIS Manage")).

## Record a Position Change

When an employee changes from one position to another in the organization, the position change should be recorded in the employee's record. All of the positions that the employee has held in the organization are saved to the employee's Position History, which can be reviewed at any time.

|  |  |
| --- | --- |
| In the employee's record, click Position Information in the side menu to jump to the "Position Information" section. Under the position, click Change Position. |  |
| The Make a Job Offer form opens, showing the current position title and start date.    Either type or select the position code and title of the new **Position**.    The **Start Date** for the new position is set to today's date by default. If this is not correct, change it. This will also be the end date for the employee's old position.    Select the **Currency** and enter the amount of the **Salary** for the new position; this may be the same as the employee's previous salary.    Under **Reason for Departure**, select the reason for the position change.    Select the **New Status** for the position: Open or Discontinued; if the position is marked "Open," it will be available for assignment to another employee or applicant.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. |  |
| The information that you just entered displays in the employee's record under the "Position Information" section. |  |
| Click View Position History under the "Position Information" section to view a list of all the positions that the employee has held in the organization, their start dates and end dates, and the reasons why the employee left each position. |  |

### Troubleshooting

**An error message is displayed when the Confirm button is clicked.**

Make sure that all the fields have been completed. Required fields are outlined in red. Fill in any missing information and try saving again. If you do not want to change the position after all, click `Return (do not save changes)`.

**The new position is not available for selection.**

The position must be added first and marked as an open position (see [Add a position](ihris_administer_positions.html#Add_Positions "Administer Positions")).

**The reason for the position change is not available for selection.**

The HR Manager must add the reason to the system (see [Add a reason for departure](ihris_administer_database_for_ihris_manage.html#Add_a_Reason_for_Departure "Administer Database for iHRIS Manage")).

**The correct currency is not available for selection.**

The HR Manager must add the currency to the system (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

**There is an error in any position.**

Click Correct This Information beside the position in the "Position Information" section of the employee's record to correct the error. Only the HR Manager can correct position errors.

## Record a Salary Change

If an employee's salary changes, the new salary can be updated in the employee's record. The old salary will be saved in the employee's Salary History, which may be reviewed at any time.

|  |  |
| --- | --- |
| In the employee's record, click Position Information in the side menu to jump to the "Position Information" section. Underneath the "Salary" section, click Salary Change. |  |
| The Salary Change form opens, showing the current salary information.    Select the **Currency** and enter the amount of the new **Salary**.    The **Start Date** when the new salary will become effective is set to today's date by default. If that is not correct, change it.    Enter any **Notes** about the salary change (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.    The information that you just entered displays in the employee's record under the "Position Information" section.    Click View Salary History beside the salary to review the employee's past and current salaries. |  |

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the required fields have been entered. Required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to change the salary after all, click `Return (do not save changes)`.

**The correct currency is not available for selection.**

The currency must be added to the system by an HR Manager (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

**The salary is incorrect.**

Click Correct This Information beside the salary in the "Position Information" section of the employee's record to correct the error. Only the HR Manager can correct salary errors.

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
