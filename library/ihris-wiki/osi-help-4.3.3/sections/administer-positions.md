---
title: "Administer Positions"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_administer_positions.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_administer_positions.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Administer Positions

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

## Add Salary Sources

If your organization tracks multiple monetary sources of salaries and/or special payments, add those to the system so the source can be linked to a salary or special payment. Only the HR Manager or System Administrator can add or edit salary sources.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Manage Positions" section, select Salary Sources. | Image:Positions.png |
| The Salary Source page opens. Either click Add New Salary Source or select an existing salary source and then click Update This Information to edit it. | Image:SalarySource1.png |
| The Salary Source form opens. Enter the **Name** of the salary source. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:SalarySource2.png |

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make sure that the salary source has not already been entered. Change the name and try saving again. If you do not want to add the salary source after all, click `Return (do not save changes)`.

## Add Position Types

To classify positions by a category or type, add those position types to the system. Examples of position types include Permanent, Temporary, Consultant, Part-time and the like. Only the HR Manager or System Administrator can add or edit position types.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Manage Positions" section, select Position Types. | Image:Positions.png |
| The Position Type page opens, showing all position types entered in the database. Either click Add New Position Type or select an existing position type and then click Update This Information to edit it. | Image:PositionType1.png |
| The Position Type form opens. Enter the **Name** of the position type. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:PositionType2.png |

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make sure that the position type has been already been entered. Change the name and try saving again. If you do not want to add the position type after all, click `Return (do not save changes)`.

## Add Positions

Adding a position creates a new position in the organization that a single employee will fill. The position must be created before it can be assigned to an existing employee or applications can be accepted for the position. A position that is not linked to an employee but for which you intend to hire someone to fill it is called an *open position*. A position that is not linked to an employee and for which you are not intending to hire someone is called a *discontinued position*. A position that is filled by an employee is called a *closed position*. Either an HR Staff person or an HR Manager can add a new position or update an existing position.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Manage Positions" section, select Positions (by Facility). | Image:Positions.png |
| The Position page opens. Click Add New Position. | Image:Position1.png |
| The Position form opens.    Select the **Job** for the new position.    Enter the **Position Title** (this may be the same as the job title).    Enter a **Position Description** as an addendum to the job description (optional).    Select a **Currency** for the salary and enter the **Proposed Salary** amount for the position; this amount will be changed to the actual salary when the position is filled (optional).    If there are one or more salary sources to track for the position, select them in the **Source** box; to select more than one salary source, hold down the CTRL key while clicking the name of each salary source (optional).    Today's date displays for the **Date Posted**, the date the position was opened. If this is incorrect, change the date.    Enter any comments or notes about the position in the **Position Comments** box (optional).    Enter the **Position Code**.    Either type or select the code and title of the position that will supervise this position under **Supervisor** (optional).    Select the office or facility where the position is located in the **Facility** menu.    Select the **Department** where the position is located (optional).    Select the **Position Type** (optional).    Select the **Proposed Hiring Date** for the position (optional).    If the position is short-term, select the **Proposed End Date** for the position (optional).    Select the **Status** of the position: Open or Discontinued. Select *Open* if you want the position to be available for assignment to an employee.    If an interview has been held for the position, enter any comments or notes about it in the **Interview Comments** box (optional).    Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Position2.png |

### Troubleshooting

**Instead of creating a new position, you want to use a position that was previously created but was discontinued.**

Under the "Manage Positions" section, select Positions (by Status). Select "Discontinued" from the **Status** menu and click the `View` button; all discontinued positions will display. Select the position to re-open and click Open This Position. Then click Update This Information to edit any of the position's fields.

**An error message displays when Confirm is clicked.**

Make certain that you have completed all required fields. Required fields are outlined in red. Fill in all missing information and try saving again. Also make certain that the position code is unique; the system will not save two positions with the same code. If you do not want to create the position after all, click `Return (do not save changes)`.

**The correct job for the position is not available for selection.**

The HR Manager must create the new job before the position can be added (see [Add jobs](ihris_create_a_job_structure.html#Add_Jobs "Create a Job Structure")). Click Add New beside the **Job** selection menu to add the job and then follow the steps above to add the position (you will have to re-enter any position information that was previously entered).

**The supervisor's position is not available for selection.**

The supervisor's position must be added to the system before it can be selected. Repeat these steps to add the supervisor's position, then edit the current position to select the correct supervisor (see [Edit a position](#Edit_a_Position "Administer Positions")).

**The correct currency is not available for selection.**

The currency must be added to the system by an HR Manager (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

**The correct salary source is not available for selection.**

The salary source must be added to the system by an HR Manager (see [Add salary sources](#Add_Salary_Sources "Administer Positions")).

**The office or facility for the position is not available for selection.**

The office or facility must be added to the system by an HR Manager (see [Add an office or facility](ihris_administer_database_for_ihris_manage.html#Add_an_Office_or_Facility "Administer Database for iHRIS Manage")).

**The department is not available for selection.**

The department must be added to the system by an HR Manager (see [Add a department](ihris_administer_database_for_ihris_manage.html#Add_a_Department "Administer Database for iHRIS Manage")).

**The position type is not available for selection.**

The position type must be added to the system by an HR Manager (see [Add position types](#Add_Position_Types "Administer Positions")).

## Edit a Position

Once a position has been created in the system, an HR Staff person or an HR Manager can change any of the information for the position.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Manage Positions" section, select Positions (by Facility) add or edit a position based on the facility where it is located or select Positions (by Status) to add or edit a position based on its status as open, closed or discontinued. | Image:Positions.png |
| The Position page opens. If you chose Positions (by Facility), select the name of the facility where the position is located from the **Facility** menu. If you chose Positions (by Status), select the status of the position from the **Status** menu. Click the `View` button to display all the positions entered for that facility or status. | Image:Position3.png |
| A list of positions already entered in the database appears. Click the name of the position to edit. | Image:Position4.png |
| The position information displays. Click Update This Information.    The Position form opens, showing the position information that was previously entered. Change any field.    Click `Confirm` and confirm that the changed information is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Position5.png |

### Troubleshooting

**An error message displays when Confirm is clicked.**

Make certain that you have completed all required fields. Required fields are outlined in red. Fill in all missing information and try saving again. Also make certain that the position code is unique; the system will not save two positions with the same code. If you do not want to update the position after all, click `Return (do not save changes)`.

## Discontinue a Position

If a position is no longer needed and is not filled by an employee, it can be discontinued. This will prevent the position from displaying in open position lists. The position can be re-opened at any time. Either an HR Staff person or an HR Manager can discontinue a position.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Manage Positions" section, select Positions (by Status). | Image:Positions.png |
| The Position page opens. Select Open from the **Status** menu and click the `View` button. All of the open positions will display. Click the name of the position to edit. | Image:Position6.png |
| The position information displays. Click Discontinue This Position to mark the position as discontinued. | Image:Position7.png |

To re-open a discontinued position, repeat the steps above but select Discontinued from the **Status** menu. Then click Open This Position beside the position information.

### Troubleshooting

**The position is not displayed in the selection menu.**

Make certain the position has not been filled by an employee. To see all filled positions, select Closed in the **Status** menu; all closed positions will display underneath. You will need to remove the employee from the position before you can discontinue the position (see [Record a departure](ihris_add_position_information.html#Record_a_Departure "Add Position Information") and [Record a position change](ihris_add_position_information.html#Record_a_Position_Change "Add Position Information")).

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

}
