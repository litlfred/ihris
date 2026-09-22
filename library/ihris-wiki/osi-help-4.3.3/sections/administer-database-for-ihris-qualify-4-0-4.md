---
title: "Administer Database for iHRIS Qualify (4.0.4)"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_administer_database_for_ihris_qualify.html
  - ihris-manage/modules/manage-help/static/help/ihris_administer_database_for_ihris_qualify_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_administer_database_for_ihris_qualify.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_administer_database_for_ihris_qualify_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Administer Database for iHRIS Qualify (4.0.4)

To ensure that standard data types such as cadres, marital status, geographical locations and the like are enforced across the system, those standard data types must be created as lists. These lists are used to create selection menus that provide standard options for selection when adding records, jobs and positions. Click Administer Database to create and update standards lists of data for selection in system menus. Only the Data Operations Manager and System Administrator can create data types.

## Add a Qualification

A *qualification* is the minimum educational requirement for a person to be trained and qualified in a particular cadre. Each cadre must have an associated minimum qualification.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Qualification.
3. Either click Add New Qualification or choose an existing qualification to edit.
4. Enter or edit the **Name** of the qualification.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the qualification has not already been entered. Change the name and try saving again. If you do not want to add the qualification after all, click `Return (do not save changes)`.

## Add a Cadre

A *cadre* is a broad category of health workers characterized by the specific training or other qualifications required to practice or be licensed in that field. A health worker receives training in a particular cadre and then may be registered and licensed to practice in that cadre. Add new cadres or edit any cadre that was previously added.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Cadre.
3. Either click Add New Cadre or choose an existing cadre to edit.
4. Enter or edit the **Name** of the cadre.
5. Select the **Minimum Qualification** for the cadre.
6. Enter the **ISCO Classification Code** for the cadre (optional). Here is the link to the ISCO-88 codes: http://www.ilo.org/public/english/bureau/stat/isco/isco88/index.htm
7. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the cadre has not already been entered. Change the name and try saving again. If you do not want to add the cadre after all, click `Return (do not save changes)`.

**The minimum qualification is not available for selection.**

Click Add New underneath the selection menu and add the qualification that is needed. Then click Administer Database and follow the steps above to add the new cadre. You will have to re-enter any information that you previously entered for the cadre.

## Add a Continuing Education Course

A *continuing education course* is an in-service training course that a health worker takes, usually to meet license renewal requirements.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Continuing Education Course.
3. Select Add New Continuing Education Course and click `Add` to add a new course. (To edit an existing course, select it the menu and click `View`; then click Update This Information.)
4. Enter or edit the **Name** of the course.
5. Enter the number of **Credit Hours** earned by taking the course.
6. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure all fields have been completed. The required fields will be outlined in red. Complete the missing fields and try saving again. If you do not want to add the course after all, click `Return (do not save changes)`.

## Add a Disciplinary Action Category

Add a broad category for disciplinary action reasons to track in the system.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Disciplinary Action Category.
3. Either click Add New Disciplinary Action Category or select an existing category to edit.
4. Enter the **Name** of the category.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the category has not already been entered. Change the category's name and try saving again. If you do not want to add the disciplinary action category after all, click `Return (do not save changes)`.

## Add a Disciplinary Action Reason

Add a reason for disciplinary action to track in the system and associate it with a broader category.

1. From the home page or left menu, Configure System, then click Administer Database.
2. Under the "License Lists" section, click Disciplinary Action Reason.
3. Either click Add New Disciplinary Action Reason or select an existing reason to edit.
4. Select a **Disciplinary Action Category** for the reason.
5. Enter the **Name** of the reason.
6. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure all fields have been completed and that the reason has not already been entered. The required fields will be outlined in red. Complete the missing fields or change the name and try saving again. If you do not want to add the disciplinary action reason after all, click `Return (do not save changes)`.

**The category is not available for selection.**

Click Add New underneath the selection menu and add the category that is needed. Then click Administer Database and follow the steps above to add the new reason. You will have to re-enter any information that you previously entered for the reason.

## Add Out Migration Reason

Add a reason for out migration to track in the system.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Out Migration Reason.
3. Either click Add New Out Migration Reason or select an existing reason to edit.
4. Enter the **Name** of the reason.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the reason has not already been entered. Change the name and try saving again. If you do not want to add the out migration reason after all, click `Return (do not save changes)`.

## Add a Training Disruption Category

Add a broad category for training discontinuation reasons to track in the system.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Training Disruption Category.
3. Either click Add New Category or select an existing category to edit.
4. Enter the **Name** of the category.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the category has not already been entered. Change the name and try saving again. If you do not want to add the training disruption category after all, click `Return (do not save changes)`.

## Add Training Disruption Reason

Add a reason for discontinuing training to track in the system and associate it with a broader category.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "License Lists" section, click Training Disruption Reason.
3. Either click Add New Reason or select an existing reason to edit.
4. Select a Training Disruption Category for the reason.
5. Enter the **Name** of the reason.
6. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure all fields have been completed and that the reason has not already been entered. The required fields will be outlined in red. Complete the missing fields or change the name and try saving again. If you do not want to add the training disruption reason after all, click code>Return (do not save changes)</code>.

**The category is not available for selection.**

Click Add New underneath the selection menu and add the category that is needed. Then click Administer Database and follow the steps above to add the new reason. You will have to re-enter any information that you previously entered for the reason.

## Add an Academic Level

The *academic level* is the highest level of education achieved before a health worker enters pre-service training.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "Demographic Lists" section, click Academic Level.
3. Either click Add New Academic Level or select an existing academic level to edit.
4. Enter or edit the **Name** of the academic level.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the name of the academic level has not already been entered. Change the name and try saving again. If you do not want to add the academic level after all, click `Return (do not save changes)`.

## Add a Certificate

The *certificate* is the diploma or degree earned at the highest level of education before the health worker entered pre-service training.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "Demographic Lists" section, click Certificate.
3. Either click Add New Certificate or select an existing certificate to edit.
4. Select the **Academic Level** with which the certificate is associated.
5. Enter or edit the **Name** of the certificate.
6. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure all fields were entered and that the certificate has not already been entered. The required fields will be outlined in red. Complete the missing fields and try saving again. If you do not want to add the certificate after all, click `Return (do not save changes)`.

## Add an Identification Type

The *identification type* classifies a type of identification, or non-changing information, used to identify a person. Examples of identification types include Passport, Social Security Number and National Health Insurance Card.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "Demographic Lists" section, select Identification Type.
3. Either click Add New Identification Type or select an existing identification type to edit.
4. Enter the **Name** of the identification type.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the identification type was not previously entered. Change the name and try saving again. If you do not want to add the identification type after all, click `Return (do not save changes)`.

## Add a Marital Status

*Marital status* is used to identify a person's legal status. Examples of marital status include Single, Married, Divorced and Widowed.

1. From the home page or left menu, click Configure System, then click Administer Database.
2. Under the "Demographic Lists" section, select Marital Status.
3. Either select Add New Marital Status or select an existing marital status to edit.
4. Enter the **Name** of the marital status.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain the marital status has not already been entered. Change the name and try saving again. If you do not want to add the marital status after all, click `Return (do not save changes)`.

## Record Verification Changes

A *verification change* is an option that can be selected whenever a person's record is verified. Typical options might include: Corrected Demographics; Corrected Training; Corrected License/Registration and No Changes Made.

1. From the home page or left menu, click Administer Database.
2. Under the "Administrative Lists" section, select Record Verification Changes.
3. Either select Add New Verification Change or select an existing verification change to edit.
4. Enter the **Name** of the verification change.
5. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make certain that the verification change has not already been entered. Change the name and try saving again. If you do not want to add the verification change after all, click `Return (do not save changes)`.
