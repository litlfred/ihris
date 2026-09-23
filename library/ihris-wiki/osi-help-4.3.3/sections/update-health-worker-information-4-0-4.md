---
title: "Update Health Worker Information (4.0.4)"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_update_health_worker_information.html
  - ihris-manage/modules/manage-help/static/help/ihris_update_health_worker_information_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_update_health_worker_information.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_update_health_worker_information_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Update Health Worker Information (4.0.4)

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**

## Record a Deployment

When a health worker is deployed to a particular job, that information can be recorded in the system.

1. In the person's record click Deployment in the side menu to jump to the "Deployment" section.
2. Click Add Deployment.
3. Select the **Health Facility** where the health worker has been deployed.
4. Enter the **Deployment Date** (if no date is entered, today's date is saved by default).
5. Enter the **Job / Post Title**.
6. Enter the **Job / Post Code**.
7. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the deployment information added. All past deployments are saved in the health worker's deployment history. To view them, click View Deployment History under the "Deployment" section.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make certain that all required fields have been completed. Required fields are outlined in red. The health facility must be recorded. Fill in or correct the information and try saving again. If you do not want to add an out migration verification request after all, click `Return (do not save changes)`.

**The correct Health Facility is not available for selection.**

Only the Data Operations Manager can add new health facilities to the system (see Add a Health Facility).

**There is an error in the deployment information.**

Open the record, go to the "Deployment Information" section and click Correct This Information. Correct any errors and click `Confirm` to save. Only the Data Operations Manager can correct deployment information.

## Record an Out Migration Verification Request

If a health worker applies to practice in another country, the certification or licensing authority in the foreign country usually requests verification of the health worker's credentials. Recording this information with the health worker's record enables the system to track possible out migrations of health workers and the reasons for leaving the country, which can be useful in analyzing health worker retention issues. A request for verification for out migration does not mean that the health worker has actually out migrated; that cannot be determined with this system.

1. In the person's record click Out Migration in the side menu to jump to the "Out Migration" section.
2. Click Add Out Migration.
3. Select the **Country** where the request came from, or the country where the health worker plans to emigrate.
4. Enter the health worker's **Address in the New Country**, if known.
5. Select the **Out Migration Reason**.
6. Record the name of the **Organization Requesting Verification**, if known.
7. Enter the **Request Date** (today's date is saved by default if no date is selected).
8. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the out migration information added. To add another request for out migration verification, click Add Out Migration again. There is no limit to the number of requests that can be recorded.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make certain that all required fields have been completed. Required fields are outlined in red. The country and the reason for out migration must be recorded. Fill in or correct the information and try saving again. If you do not want to add an out migration verification request after all, click `Return (do not save changes)`.

**The correct Country is not available for selection.**

Only the Data Operations Manager can add new country to the system (see Add a Country).

**The correct Out Migration Reason is not available for selection.**

Only the Data Operations Manager can add new reasons for out migration to the system (see Add a Reason for Out Migration).

**The out migration information needs to be changed.**

In the record under the "Out Migration Information" section, click Update This information to update any of the fields.

## Add Notes

At any time, a Records Officer, Registration Supervisor or Data Operations Manager may add notes to a person's record. All notes are saved to a log and may be reviewed as necessary.

1. In the person's record, click Notes in the left menu to jump to the "Notes" section.
2. Click Add Note.
3. Enter a **Date** for the note; if no date is entered, today's date is saved by default.
4. Enter the text of the **Note**.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

All notes will appear in chronological order at the bottom of the person's record.

### Troubleshooting

**An error message displays when the Confirm button is clicked.**

Entering the note text is required. The required field is outlined in red. Try filling in the missing field and saving again. If you do not want to enter a note after all, click `Return (do not save changes)`.

**The note needs to be changed.**

In the record under the "Notes" section, click Update This information beside the note to update it.

## Add a Verification

When a data entry person or a data manager verifies a person's record, such as when the health worker requests a change in the record or the record is verified against another form, that verification can be recorded in the person's record. This data quality measure enables managers to log all changes made through verifications and keep a history of those changes in the record itself.

1. In the person's record click Record Verification in the side menu to jump to the "Record Verification" section.
2. Click Add Verification.
3. Set the **Verification Date**.
4. Select the **Changes Made**; if more than one change was made, hold down the CTRL key while clicking to select them.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the verification changes that were made. If the record has been verified more than once, all changes are logged in the Verification History. Click View Verification History to display them.

### Troubleshooting

**The correct Verification Change is not available for selection.**

Only the Data Operations Manager can add new verification changes to the system (see Record Verification Changes).

**The verification change needs to be updated.**

In the record under the "Record Verification" section, click Update This information to update any of the fields.

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**
