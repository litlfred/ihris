---
title: "Add and Edit Health Facilities and Training Institutions (4.0.4)"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_add_and_edit_health_facilities_and_training_institutions.html
  - ihris-manage/modules/manage-help/static/help/ihris_add_and_edit_health_facilities_and_training_institutions_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_and_edit_health_facilities_and_training_institutions.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_and_edit_health_facilities_and_training_institutions_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Add and Edit Health Facilities and Training Institutions (4.0.4)

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**

To ensure that standard data types such as cadres, marital status, geographical locations and the like are enforced across the system, those standard data types must be created as lists. These lists are used to create selection menus that provide standard options for selection when adding records, jobs and positions. Click Administer Database to create and update standards lists of data for selection in system menus. Only the Data Operations Manager and System Administrator can create data types.

## Add a Health Facility

Add a health facility for each facility where health workers will be deployed or practicing privately.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Health Facility.
3. From the menu select Add New Health Facility and click the `Add` button. (To edit an existing health facility, select it from the menu and click the `View` button, then click Update This Information.)
4. Enter or edit the **Name** of the health facility.
5. Enter the **Identification Code** of the health facility (optional).
6. Select the **Facility Agent** under which the health facility belongs.
7. Select the **Facility Type** for the health facility.
8. Select the **Country** where the health facility is located.
9. All districts located in the country are displayed beneath the country. Select the **District** where the health facility is located.
10. All counties located in the district are displayed beneath the district. Select the **County** where the health facility is located (optional).
11. Select the **Facility Status** for the health facility.
12. Add **Contact Information** for the health facility (optional).
13. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The new health facility record is displayed with the option to associate training institutions with the health facility.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the health facility's name, country, facility agent, facility type and facility status have been entered -- these fields are required. Required fields will be outlined in red. Also make sure that a health facility by that name has not already been entered. Try completing the missing fields and saving again. If you do not want to add the health facility after all, click `Return (do not save changes)`.

**The correct facility agent, facility type, facility status or geographical location is not available for selection.**

Click Add New underneath the selection menu and add the item that is needed. Then click Administer Database and follow the steps above to add the new health facility. You will have to re-enter any information that you previously entered for the health facility.

**The health facility information has changed.**

Select the health facility name, click the `View` button and click Update This Information in the health facility's record to update any of the fields.

## Associate a Training Institution with a Health Facility

For each health facility in the system, select one or more training institutions that are officially associated with that facility.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Health Facility.
3. Select the health facility to edit from the dropdown menu and click the `View` button.
4. Click Update Associated Training Institutions.
5. Select the name of each **Training Institution** to associate with the health facility. Press CTRL while clicking to select more than one name.
6. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The associated training institutions are displayed in the health facility's record.

### Troubleshooting

**The correct training institution is not available for selection.**

Click Add New Training Institution underneath the selection menu and add the item that is needed (see Add a Training Institution). Then click Administer Database and follow the steps above to associate the new training institution with the health facility.

## Add a Training Institution

Add a training institution for each training program in the country where health workers receive pre-service training.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Training Institution.
3. From the menu either Add New Training Institution and click the `Add` button. (To edit an existing training institution, select it from the menu and click the `View` button, then click Update This Information).
4. Enter or edit the **Name** of the training institution.
5. Enter the **Identification Code** of the training institution (optional).
6. Select the **Facility Agent** under which the training institution belongs.
7. Select the **Country** where the training institution is located.
8. All districts located in the country are displayed beneath the country. Select the **District** where the training institution is located.
9. All counties located in the district are displayed beneath the district. Select the **County** where the training institution is located (optional).
10. Select the **Facility Status** for the training institution.
11. Add **Contact Information** for the training institution.
12. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The new training institution record is displayed with the option to associate health facilities with the training institution, add a pre-service training program or enter inspection information.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the training institution name, country, facility agent and facility status have been entered -- these fields are required. Required fields will be outlined in red. Also make sure that the training institution's name has not already been entered. Try completing the missing fields and saving again. If you do not want to add the training institution after all, click `Return (do not save changes)`.

**The correct facility agent, facility status or geographical location is not available for selection.**

Click Add New underneath the selection menu and add the item that is needed. Then click Administer Database and follow the steps above to add the new training institution. You will have to re-enter any information that you previously entered for the training institution.

**The training institution information has changed.**

Select the training institution name, click the `View` button and click Update This Information in the training institution's record to update any of the fields.

## Associate a Health Facility with a Training Institution

For each training institution in the system, select one or more health facilities that are officially associated with that training institution.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Training Institution.
3. Select the training institution to edit from the dropdown menu and click the `View` button.
4. Click Update Associated Health Facilities.
5. Select the name of each **Health Facility** to associate with the training institution. Press CTRL while clicking to select more than one name.
6. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The associated health facilities are displayed in the training institution's record.

### Troubleshooting

**The correct health facility is not available for selection.**

Click Add New Health Facility underneath the selection menu and add the item that is needed. Then click Administer Database and follow the steps above to associate the new health facility with the training institution.

## Add a Pre-service Training Program

For each training institution in the system, add at least one training program that the training institution offers. The training program should qualify students to be licensed in a particular cadre. When the student's record is added, the training institution and cadre will be selected based on this information.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Training Institution.
3. Select the training institution to edit from the dropdown menu and click the `View` button.
4. Click Add Training Program under the "Training Programs" section.
5. Select the **Cadre**.
6. Enter the recommended **Number of Students** for the program.
7. Select the **Start Date** for the program.
8. If the program is no longer being offered, select an **End Date** for it.
9. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The training program is displayed in the training institution's record.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the cadre has been selected and that a training program for that cadre has not already been added for this training institution. Required fields will be outlined in red. Try changing the cadre and saving again. If you do not want to add the training program after all, click `Return (do not save changes)`.

**The correct cadre is not available for selection.**

Click Add New underneath the selection menu and add the item that is needed. Then click Administer Database and follow the steps above to add the training program.

**The training program information has changed.**

Select the training institution name, click the `View` button and click Update This Information beside the training program to update any of the fields.

## Enter Inspection Information for a Training Institution

Inspection information may optionally be recorded for any training institution in the system.

1. From the home page or left menu, click Administer Database.
2. In the "Institution Lists" section, select Training Institution.
3. Select the training institution to edit from the dropdown menu and click the `View` button.
4. Click Add Institution Inspection.
5. Enter the **Inspection Date**.
6. Select whether the training institution **Passed Inspection**.
7. Enter any **Notes** about the inspection.
8. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The inspection is displayed in the training institution's record.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that all required fields have been completed. Required fields will be outlined in red. Try completing the missing fields and saving again. If you do not want to add the inspection after all, click `Return (do not save changes)`.

**The inspection information has changed.**

Select the training institution name, click the `View` button and click Update This Information beside the inspection to update any of the fields.

## Add a Facility Agent

The *facility agent* is used to identify the operator of a training institution or health facility. Examples of facility agents include Government, Nongovernmental Organization and Private.

1. From the home page or left menu, click Administer Database.
2. Under the "Institution Lists" section, select Facility Agent.
3. Either select Add New Facility Agent or select an existing facility agent to edit.
4. Enter the **Name** of the facility agent.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the facility agent has not already been entered. Change the name and try saving again. If you do not want to add the facility agent after all, click `Return (do not save changes)`.

## Add a Facility Type

The *facility type* is used to identify the type of health facility. Examples of facility types include Hospital, Clinic and Dispensary.

1. From the home page or left menu, click Administer Database.
2. Under the "Institution Lists" section, select Facility Type.
3. Either select Add New Facility Type or select an existing facility type to edit.
4. Enter the **Name** of the facility type.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the facility type has not already been entered. Change the name and try saving again. If you do not want to add the facility type after all, click `Return (do not save changes)`.

## Add a Facility Status

The *facility status* is used to identify whether a health facility or training institution is open, closed or assigned some other kind of status.

1. From the home page or left menu, click Administer Database.
2. Under the "Institution Lists" section, select Facility Status.
3. Either select Add New Facility Status or select an existing facility status to edit.
4. Enter the **Name** of the facility status.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the facility status has not already been entered. Change the name and try saving again. If you do not want to add the facility status after all, click `Return (do not save changes)`.

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**
