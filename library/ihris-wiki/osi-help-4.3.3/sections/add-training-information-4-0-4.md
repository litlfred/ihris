---
title: "Add Training Information (4.0.4)"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_add_training_information.html
  - ihris-manage/modules/manage-help/static/help/ihris_add_training_information_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_training_information.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_training_information_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Add Training Information (4.0.4)

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**

## Add a Training

Before a registration or license can be issued for a health worker, the pre-service training program that the health worker completed to become qualified to practice in that cadre must be recorded. The training program information can be recorded when the student enters school, while the program is in progress or after it has been completed, and it may have been completed inside or outside the country. Each training receives a unique index number used to identify a student in a training program in a particular cadre. The index number may be issued by the training institution. A health worker can complete multiple training programs; each additional program is called an upgrade and qualifies the health worker to practice in another cadre.

1. In the person's record click Training Information, in the side menu to jump to the "Training Information" section.
2. Click Add Training; a new screen opens.
3. Enter the **Index Number** for the training, or check the box beside "Generate next Index Number" to automatically assign an index number to the training.
4. Select the **Intake Date**, the date the student began training (optional).
5. If the student has completed training, enter the **Graduation Date** (the graduation date can also be set at a later time). If the student was trained outside the country, the graduation date is required.
6. If the student was trained in the country, select the **Training Institution** where the student has been admitted under "Trained In Country". By clicking on "Select Value", and selecting a training institution, a list of training programs, or **Cadres**, will display for that training institution. Select the program that the student is trained in.
7. If the student was trained outside the country, first select the **Country Trained In** under "Trained Outside the Country," then type in the name of the **Training Institution**. Select the **Cadre** that the student received training in.
8. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the training information added. To update the training information or issue a registration to a student who has completed training, click Update Registrations/Licenses beside the training information in the student's record. Once the changes have been made, click Return to Main Record to return to the original page.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make certain that all required fields have been completed. Required fields are outlined in red. An index number and a cadre must be assigned for each training. Also make certain that the graduation date is not set to earlier than the intake date. If the person was trained outside the country, the graduation date is required. Fill in or correct the information and try saving again. If you do not want to add a training after all, click `Return (do not save changes)`.

**The correct Training Institution or Cadre is not available for selection.**

Only the Data Operations Manager can add new training institutions or cadres to the system (see Add a Training Institution or Add a Pre-service Training Program).

**There is an error in the training information.**

Open the record, go to the "Training Information" section, click Update Registrations/Licenses and then click Correct This Information beside the training. Correct any errors and click `Confirm` to save. Only the Data Operations Manager can correct training information.

## Record a Discontinuation in Training

A *discontinuation* occurs when a student leaves a training program for any reason. To record a discontinuation, you must first add a training.

1. In the person's record click Training Information in the side menu to jump to the "Training Information" section.
2. Click Update Registrations/Licenses beside the appropriate training program.
3. The system displays the full details of the training program. Above it, click Record Discontinuation.
4. Select the **Category** of disruption reason.
5. The system displays all specific reasons for that category. Select the appropriate **Disruption Reason**.
6. Select the **Disruption Date**.
7. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the discontinuation added. No further information can be added for that training or cadre unless the student resumes training and a resumption is recorded (see Record a Resumption in Training). Once the changes have been made, click Return to Main Record to return to the original page.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make certain that all required fields have been completed. Required fields are outlined in red. Fill in or correct the information and try saving again. If you do not want to add a discontinuation after all, click `Return (do not save changes)`.

**The correct Training Disruption Category or Reason is not available for selection.**

Only the Data Operations Manager can add new training disruption categories or reasons to the system (see Add a Training Disruption Category or Add a Reason for Training Disruption).

## Record a Resumption in Training

A *resumption* occurs when a student returns to a training program that s/he previously discontinued. To record a resumption, you must first enter a discontinuation.

1. In the person's record click Training Information in the side menu to jump to the "Training Information" section.
2. Click Update Registrations/Licenses beside the training program that was previously discontinued.
3. The system displays the full details of the training program. Above it, click Resume Training.
4. Select the **Resumption Date**.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the resumption added. Now a graduation date can be set for the training (see Set a Graduation Date). Once the changes have been made, click Return to Main Record to return to the original page.

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make certain that the resumption date has been entered and does not occur before the disruption date. Correct the date and try saving again. If you do not want to add a resumption after all, click `Return (do not save changes)`.

## Set a Graduation Date

Set the graduation date when a student has completed a pre-service training program. Setting a graduation date makes the student eligible to receive registration in the cadre in which s/he was trained.

1. In the person's record click Training Information in the side menu to jump to the "Training Information" section.
2. Click Update Registrations/Licenses beside the appropriate training program.
3. The system displays the full details of the training program. Beside it, click Set Graduation Date.
4. Enter the **Graduation Date**.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The training program is marked completed and the option to add a registration becomes available (see Issue a Registration).

### Troubleshooting

**The option to set a graduation date does not appear.**

Make sure that the training has not been marked discontinued and that the graduation date was not already set.

## Record Examination Information

When a student has completed a pre-service training program, s/he may be required to pass a national examination before being registered to practice in that cadre. In that case, record the details of the student's examination attempts to track the student's eligibility for registration. Recording examination details is optional in this system.

1. In the person's record click Training Information in the side menu to jump to the "Training Information" section.
2. Click Update Registrations/Licenses beside the training program for which the student has taken the examination.
3. The full training details are displayed. Under "Exam Information," click Add Exam Information. All of the fields on this screen are optional.
4. The **Application Date**, the date the student applied to sit for the exam, is set to today's date by default; if it is different, change the date.
5. Under **Materials Received?** indicate whether the student's required application materials have been received.
6. Under **Materials Approved?** indicate whether the student's required application materials have been approved.
7. Enter the endorsement information, including the **Endorser Name**, the **Endorsement Date** and the **Endorser Qualifications**.
8. Change the **Exam Date**, the date that the student took the examination, if necessary. It is also set to today's date by default.
9. Under **Exam Try**, select the number of times the student has taken the exam. By default, the student must pass the exam within three attempts.
10. Select the **Exam Results**: Pass, Fail or Did not sit for exam.
11. Enter the **Examination Number**.
12. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

The system displays the person's record with the examination information added beneath the training information. Once the changes have been made, click Return to Main Record to return to the original page.

### Troubleshooting

**The system displays an error when the Confirm button is clicked.**

Make certain that the Examination Date does not occur before the Application Date. Correct the appropriate date and try saving again.

**The examination information needs to be changed.**

In the record under the "Training Information" section, click Update This information beside the examination information to update any of the fields.

**An error message appears when the Confirm button is clicked.**

Make certain that the graduation date entered doesn't come before the intake date. If it does, correct the date to fall after the intake date and try saving again. If you do not want to add a graduation date after all, click `Return (do not save changes)`.

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**
