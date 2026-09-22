---
title: "Create a Job Structure"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_create_a_job_structure.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_create_a_job_structure.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Create a Job Structure

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**

iHRIS Manage enables HR Managers and Staff to design and manage a job structure for the organization. Jobs may be categorized by health professional cadre, job classification and salary grade, and may be assigned standard titles, codes and job descriptions. Click Administer Database under Configure System to create the job structure, add new positions that may be filled by employees or applicants and manage existing positions.

## Add Cadres

A *cadre* is a broad category of health workers characterized by the specific training, certification or other qualifications required to practice or be licensed in that field. Examples of cadres include Nurse, Physician and Pharmacist. Each job can be linked to one cadre for reporting purposes. You may add new cadres or edit any cadre that was previously added. Only the HR Manager or System Administrator can update the cadres.

Cadres should only be used to categorize health professionals. Other job categories should be added as job classifications. If your organization does not employ health professionals, you can skip this step.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Create Job Structure" section, select Cadres. | Image:JobStructure.png |
| The Cadre page opens, showing all cadres entered in the database. Either click Add New Cadre or select an existing cadre and then click Update This Information to edit it. | Image:Cadres1.png |
| The Cadre form opens. Enter the **Name** of the cadre. Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Cadres2.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the name of the cadre has not already been entered. Change the name and try saving again. If you do not want to add the cadre after all, click `Return (do not save changes)`.

## Add Job Classifications

A *job classification* is a broad category used to organize jobs. Each job can be optionally linked to one job classification for organization and reporting purposes. Examples of job classifications include Manager, Professional, Technician, Service Worker and Clerical Worker.

You should add all the job classifications in use in your organization to the system; you may also edit any job classification previously added. If your organization does not use job classifications to organize jobs, you can skip this step. Only the HR Manager or System Administrator can update job classifications.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Create Job Structure" section, select Job Classifications. | Image:JobStructure.png |
| The Job Classification page opens, showing all job classifications entered in the database. Either click Add New Job Classification or select an existing job classification and then click Update This Information to edit it. | Image:Classification1.png |
| The Job Classification form opens.    Enter the **Name** of the job classification.    Enter a brief **Description** of the job classification (optional).    Enter a **Code** for the job classification (optional).    Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Classification2.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure the name of the job classification has not already been entered. Change the name and try saving again. If you do not want to add the cadre after all, click `Return (do not save changes)`.

## Add Salary Grades

If your organization defines *salary grades* or bands -- pay ranges for one or more jobs -- add those grades to the system. (If your organization does not define salary grades, you can skip this step.) A job can then be linked to its corresponding salary grade. Only the HR Manager or System Administrator can add or edit salary grades.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Create Job Structure" section, select Salary Grades. | Image:JobStructure.png |
| The Salary Grades page opens, showing all salary grades entered in the database. Either click Add New Salary Grade or select an existing salary grade and then click Update This Information to edit it. | Image:SalaryGrade1.png |
| The Salary Grades form opens.    Enter the **Name**, or identifier, of the salary grade.    Enter any **Notes** to record about the salary grade (optional).    Select a **Currency** for the starting salary and enter the amount of the **Start** salary (the lowest salary in the band).    Select a **Currency** for the ending salary and enter the amount of the **End** salary (the highest salary in the band).    Select a **Currency** for the midpoint salary and enter the amount of the **Midpoint** salary (the midpoint is the average salary in the band offered to a new hire, which may or may not be the equivalent of the true average of the starting and ending salaries). This is optional.    Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:SalaryGrade2.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the salary grade name, starting salary and ending salary have been entered and that the salary grade has not previously been entered. Required fields are outlined in red. Fill in any missing information or change the name and try saving again. If you do not want to add the salary grade after all, click `Return (do not save changes)`.

**The correct currency is not available for selection.**

The currency must be added to the system by an HR Manager (see [Add a currency](ihris_add_geographical_areas.html#Add_a_Currency "Add Geographical Areas")).

## Add Jobs

A *job* is a general set of qualifications, duties and responsibilities as specified in a job description. Each job has a unique job code and may be linked to a cadre, job classification and salary grade.

There may be multiple instances of the same job within an organization. Each of these instances is filled by one employee and is referred to as a *position*. Before a position can be created in the system, its generic job must be added. After creating a generic job, it can be reused as needed for multiple positions that perform the same general duties. For example, a Clinical Nurse, Pediatric Nurse and Intensive Care Nurse may all be positions with the same generic job of Nurse. Only the HR Manager or System Administrator can add or edit jobs.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    Under the "Create Job Structure" section, select Jobs. | Image:JobStructure.png |
| The Job page opens, showing all jobs entered in the database. Either click Add New Job or select an existing job and then click Update This Information to edit it. | Image:Job1.png |
| The Job form opens.    Enter a **Title** for the job.    Enter a **Code** for the job (optional).    Enter a **Description** for the job (optional).   Select the **Salary Grade** for the job (optional).    Select the **Cadre** for the job (optional). Only select a cadre for health professional jobs.    Select the **Classification** for the job (optional).    Click `Confirm` and confirm that the name entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Job2.png |

### Troubleshooting

**An error message displays when the Confirm button is clicked.**

Make sure that the job has not already been added. Change the name and try saving again. If you do not want to add the job after all, click `Return (do not save changes)`.

**The correct salary grade is not available for selection.**

The salary grade must be added to the system before adding the job (see [Add salary grades](#Add_Salary_Grades "Create a Job Structure")).

**The correct cadre is not available for selection.**

The cadre must be added to the system before adding the job (see [Add cadres](#Add_Cadres "Create a Job Structure")).

**The correct classification is not available for selection.**

The job classification must be added to the system before adding the job (see [Add job classifications](#Add_Job_Classifications "Create a Job Structure")).

***Return to the* [iHRIS Manage User Manual index page](ihris_manage_user_manual.html "iHRIS Manage User Manual").**
