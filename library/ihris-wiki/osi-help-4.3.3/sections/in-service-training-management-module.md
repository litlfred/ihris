---
title: "In-service Training Management Module"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_in_service_training_management_module.html
  - ihris-manage/modules/manage-help/static/help/ihris_in_service_training_management_module_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_in_service_training_management_module.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_in_service_training_management_module_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# In-service Training Management Module

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

## Add a Training Course

A *training course* is a course that an employee may take to gain new competencies or continuing education credits. A training course covers only one topic, but it may have multiple classes that are available for employees to attend. Either the Training Manager or the HR Manager can add a training course.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Training Courses.
3. Either select Add New Training Course and click the `Add` button, or select an existing training course to edit from the menu and click the `View` button, then click Update This Information.
4. Enter the **Name** of the training course.
5. Select the **Category** of the training course.
6. Enter the **Topic** of the course.
7. Select the name of the **Training Institution** giving the course.
8. Select any **CEUs** (continuing education units) earned by completing the course; hold down the CTRL key and click to select more than one.
9. Select the training course **Status**.
10. Enter any **Notes** about the course.
11. Select the names of the **Training Funders;** hold down the CTRL key and click to select more than one.
12. Select any **Competencies** gained by completing the course; hold down the CTRL key and click to select more than one.
13. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

After saving the course information, the screen for entering the class schedule will appear (see Schedule a Course).

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that all required information has been entered. Fill in the required fields (outlined in red) and try saving again. If you do not want to add the training course after all, click `Return (do not save changes)`.

**The category is not available for selection.**

First add the training course categories (see Add a Category of Training Course).

**The training institution is not available for selection.**

First add the training institutions (see Add a Training Institution).

**The correct CEUs are not available for selection.**

First add the continuing education courses (see Add a Continuing Education Course).

**The status is not available for selection.**

First add the training course status (see Add a Status of Training Course).

**The training funders are not available for selection.**

First add the training funders (see Add a Training Funder).

**The correct competencies are not available for selection.**

First add the competencies (see Add a Competency). Only the HR Manager can add competencies.

## Schedule a Course

After adding a training course, you need to schedule at least one class for that course. The class information includes the dates of the class and the location where the class is given. When an employee is scheduled to take a training course, that employee is assigned to one of these classes. A training course can have several classes.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Training Courses.
3. From the dropdown menu, select the training course to schedule and click the `View` button.
4. Under "Scheduled Courses" click Schedule a Course.
5. Enter the **Maximum Number of Students** who can attend the class.
6. Select the **Start Date** and **End Date** for the class (today's date is entered for both by default).
7. Enter any **Notes** about the class.
8. Enter the class's **Site**, or the location where the class is taking place.
9. Enter the name(s) of the class's **Instructors**, if known.
10. Select the **Country**, **District** and **County** where the class is located (optional).
11. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that all required information has been entered. Fill in the required fields (outlined in red) and try saving again. If you do not want to schedule the class after all, click `Return (do not save changes)`.

**The country, district or county name is not available for selection.**

Under the "Geographical Location" menu, click Add New and add the country, district or county (only the HR Manager can do this). Then click Administer Database and follow the steps above to schedule the class. You will have to re-enter any information that you previously entered for the class.

## Add a Status of a Training Course

The training course *status* classifies whether the course is open, closed or any other status of your choosing. At least one status should be added.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Status of a Training Course.
3. Either select Add New Training Course Status or select an existing status to edit.
4. Enter the **Name** of the status.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that the status has not already been entered. Change the name and try saving again. If you do not want to add the status after all, click `Return (do not save changes)`.

## Add Requestors of a Training Course

The training course *requestors* are any person or group who requests that an employee attend a training course. Examples of requestors include the employee, the employee's supervisor, the human resources department or a donor organization.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Requestors of a Training Course.
3. Either select Add New Training Requestor or select an existing requestor name to edit.
4. Enter the **Name** of the requestor.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that the requestor has not already been entered. Change the name and try saving again. If you do not want to add the requestor after all, click `Return (do not save changes)`.

## Add an Evaluation of a Training Course

The training course *evaluation* is used to evaluate an employee's performance in a training course. Examples of evaluations include Pass, Fail and Incomplete. At least one evaluation option should be added.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Evaluation of a Training Course.
3. Either select Add New Training Course Evaluation or select an existing evaluation option to edit.
4. Enter the **Name** of the evaluation option.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that the evaluation option has not already been entered. Change the name and try saving again. If you do not want to add the evaluation option after all, click `Return (do not save changes)`.

## Add a Category of a Training Course

Training course *categories* group similar courses. The category is generally more broad than the training course topic. Using training course categories is optional.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Category of a Training Course.
3. Either select Add New Training Course Category or select an existing category to edit.
4. Enter the **Name** of the category.
5. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that the category has not already been entered. Change the name and try saving again. If you do not want to add the category after all, click `Return (do not save changes)`.

## Add a Training Institution

*Training institutions* are organizations that give courses. Using training institutions is optional.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Training Institution.
3. Either select Add New Training Institution and click the `Add` button, or select an existing training institution to edit from the menu and click the `View` button, then click Update This Information.
4. Enter the **Name** of the training institution.
5. Select the **Country**, **District** and **County** where the training institution is located.
6. Enter the **Contact Information** known for the training institution.
7. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that all required fields have been completed. Fill in any missing fields (outlined in red) and try saving again. If you do not want to add the training institution after all, click `Return (do not save changes)`.

**The country, district or county name is not available for selection.**

Under the "Geographical Location" menu, click Add New and add the country, district or county (only the HR Manager can do this). Then click Administer Database and follow the steps above to enter the training institution. You will have to re-enter any information that you previously entered for the training institution.

## Add a Training Funder

*Training funders* are organizations that fund employees to take training courses. Using training funders is optional.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Training Funder.
3. Either select Add New Training Funder and click the `Add` button, or select an existing training funder to edit from the menu and click the `View` button, then click Update This Information.
4. Enter the **Name** of the training funder.
5. Select the **Country**, **District** and **County** where the training funder is located.
6. Enter the **Contact Information** known for the training funder.
7. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that all required fields have been completed. Fill in any missing fields (outlined in red) and try saving again. If you do not want to add the training funder after all, click `Return (do not save changes)`.

**The country, district or county name is not available for selection.**

Under the "Geographical Location" menu, click Add New and add the country, district or county (only the HR Manager can do this). Then click Administer Database and follow the steps above to enter the training funder. You will have to re-enter any information that you previously entered for the training funder.

## Add a Continuing Education Course

*Continuing education courses* provide official continuing education units (CEUs) for employees, which may be needed to renew a license or obtain professional registration. A training course can be associated with more than one continuing education course. Using CEUs is optional.

1. From the home page or left menu, click Administer Database under Configure System.
2. In the "Training Course Information" section, select Continuing Education Course.
3. Either select Add New Continuing Education Course and click the `Add` button, or select an existing course to edit from the menu and click the `View` button, then click Update This Information.
4. Enter the **Name** of the continuing education course.
5. Enter the number of **Credit Hours** earned by completing the course.
6. Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it.

### Troubleshooting

**This option is not available.**

Make certain that the In-service Training Management Module has been enabled (see Enable the In-Service Training Management Module{linkID=650}). Only the System Administrator can turn on the module.

**An error message appears when Confirm is clicked.**

Make certain that all required fields have been completed. Fill in any missing fields (outlined in red) and try saving again. If you do not want to add the continuing education course after all, click `Return (do not save changes)`.

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
