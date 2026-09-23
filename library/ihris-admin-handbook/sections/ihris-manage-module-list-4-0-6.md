---
title: "IHRIS Manage Module List (4.0.6)"
source: http://open.intrahealth.org/w/index.php?oldid=33768
contributors: ["Litlfred"]
pages: 273-292
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Manage Module List (4.0.6)

This is a list of all modules available in version 4.0.6-release of the package iHRIS Manage \[1\]

## ManageRegistration

This describes version 4.0.0 of the module iHRIS Manage Registration (ManageRegistration)

- Source: manage/modules/ManageRegistration \[2\]

- Module Class: The module class is implemented by iHRIS\_Module\_ManageRegistration
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_registration() via action\_registration()
- Description: A Person's Registration Details
- Requirements:

- ihris-manage-Person at least 4.0
- Paths:

- Configs: modules/ManageRegistration/configs \[3\]

- Templates: modules/ManageRegistration/templates \[4\]

- view\_list\_council.html, view\_registration.html, form\_registration.html
- Classes: modules/ManageRegistration/lib \[5\]

iHRIS\_Module\_ManageRegistration

## SampleData-accident\_type

This describes version 4.0.4.2 of the module Accident Type (SampleData-accident\_type)

- Source: manage/modules/BaseData/modules/SampleData-accident\_type \[6\]

- Description: Sample Data for form: accidentid\_type
- Requirements:

- accident at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-accident\_type/ \[7\]

## SampleData-benefit\_type

This describes version 4.0.0 of the module Benefit Type (SampleData-benefit\_type)

- Source: manage/modules/BaseData/modules/SampleData-benefit\_type \[8\]

- Description: Sample Data for form: benefit\_type
- Requirements:

- ihris-manage-Benefit at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-benefit\_type/ \[9\]

## SampleData-cadre

This describes version 4.0.0 of the module Cadre (SampleData-cadre)

- Source: manage/modules/MedicalData/modules/SampleData-cadre \[10\]

- Description: Sample Data for form: cadre
- Requirements:

- ihris-manage-Job at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-cadre/ \[11\]

## SampleData-classification

This describes version 4.0.0 of the module Classification (SampleData-classification)

- Source: manage/modules/MedicalData/modules/SampleData-classification \[12\]

- Description: Sample Data for form: classification
- Requirements:

- ihris-manage-Job at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-classification/ \[13\]

## SampleData-competency

This describes version 4.0.0 of the module Competency (SampleData-competency)

- Source: manage/modules/MedicalData/modules/SampleData-competency \[14\]

- Description: Sample Data for form: competency
- Requirements:

- SampleData-competency\_type at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-competency/ \[15\]

## SampleData-competency\_type

This describes version 4.0.0 of the module Competency Type (SampleData-competency\_type)

- Source: manage/modules/MedicalData/modules/SampleData-competency\_type \[16\]

- Description: Sample Data for form: competency\_type
- Requirements:

- simple-competency at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-competency\_type/ \[17\]

## SampleData-confirmation\_type

This describes version 4.0.6 of the module Sample Data Confirmation Type (SampleData-confirmation\_type)

- Source: manage/modules/SampleData/modules/SampleData-confirmation\_type \[18\]

- Description: Sample data for confirmation types.
- Paths:

- Classes: modules/SampleData/modules/SampleData-confirmation\_type/ \[19\]

## SampleData-council

This describes version 4.0.0 of the module Registration Councils (SampleData-council)

- Source: manage/modules/MedicalData/modules/SampleData-council \[20\]

- Description: Sample Data for form: council
- Requirements:

- ManageRegistration at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-council/ \[21\]

## SampleData-department

This describes version 4.0.0 of the module Department (SampleData-department)

- Source: manage/modules/MedicalData/modules/SampleData-department \[22\]

- Description: Sample Data for form: department
- Requirements:

- ihris-manage-PersonPosition at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-department/ \[23\]

## SampleData-disciplinary\_action\_type

This describes version 4.0.4.1 of the module Disciplinary Action Type (SampleData-disciplinary\_action\_type)

- Source: manage/modules/MedicalData/modules/SampleData-disciplinary\_action\_type \[24\]

- Description: Sample Data for form: disciplinary\_action\_type
- Requirements:

- disciplinary\_action at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-disciplinary\_action\_type/ \[25\]

## SampleData-establishment

This describes version 4.0.6.2010.08.03.01 of the module Establishment Sample Data (SampleData-establishment)

- Source: manage/modules/SampleData/modules/SampleData-Establishment \[26\]

- Requirements:

- ihris-manage-sample-data at least 4.0 and less than 4.1
- establishment at least 4.0 and less than 4.1
- Paths:

- Configs: modules/SampleData/modules/SampleData-Establishment/configs \[27\]

- Classes: modules/SampleData/modules/SampleData-Establishment/ \[28\]

## SampleData-facility

This describes version 4.0.0 of the module Office/Facility (SampleData-facility)

- Source: manage/modules/SampleData/modules/SampleData-facility \[29\]

- Description: Sample Data for form: facility
- Requirements:

- Facility at least 4.0
- Paths:

- Classes: modules/SampleData/modules/SampleData-facility/ \[30\]

## SampleData-facility\_type

This describes version 4.0.0 of the module Facility Type (SampleData-facility\_type)

- Source: manage/modules/MedicalData/modules/SampleData-facility\_type \[31\]

- Description: Sample Data for form: facility\_type
- Requirements:

- Facility at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-facility\_type/ \[32\]

## SampleData-id\_type

This describes version 4.0.0 of the module Identification Type (SampleData-id\_type)

- Source: manage/modules/BaseData/modules/SampleData-id\_type \[33\]

- Description: Sample Data for form: id\_type
- Requirements:

- PersonID at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-id\_type/ \[34\]

## SampleData-job

This describes version 4.0.0 of the module Job (SampleData-job)

- Source: manage/modules/MedicalData/modules/SampleData-job \[35\]

- Description: Sample Data for form: job
- Requirements:

- SampleData-cadre at least 4.0
- SampleData-classification at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-job/ \[36\]

## SampleData-language

This describes version 4.0.0 of the module Language (SampleData-language)

- Source: manage/modules/BaseData/modules/SampleData-language \[37\]

- Description: Sample Data for form: language
- Requirements:

- PersonLanguage at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-language/ \[38\]

## SampleData-marital\_status

This describes version 4.0.0 of the module Marital Status (SampleData-marital\_status)

- Source: manage/modules/BaseData/modules/SampleData-marital\_status \[39\]

- Description: Sample Data for form: marital\_status
- Requirements:

- PersonDemographic at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-marital\_status/ \[40\]

## SampleData-pos\_change\_reason

This describes version 4.0.0 of the module Reasons for Departure (SampleData-pos\_change\_reason)

- Source: manage/modules/BaseData/modules/SampleData-pos\_change\_reason \[41\]

- Description: Sample Data for form: pos\_change\_reason
- Requirements:

- ihris-manage-PersonPosition at least 4.0
- Paths:

- Classes: modules/BaseData/modules/SampleData-pos\_change\_reason/ \[42\]

## SampleData-position\_type

This describes version 4.0.0 of the module Position Type (SampleData-position\_type)

- Source: manage/modules/MedicalData/modules/SampleData-position\_type \[43\]

- Description: Sample Data for form: position\_type
- Requirements:

- ihris-manage-PersonPosition at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-position\_type/ \[44\]

## SampleData-salary\_grade

This describes version 4.0.0 of the module Salary Grade (SampleData-salary\_grade)

- Source: manage/modules/MedicalData/modules/SampleData-salary\_grade \[45\]

- Description: Sample Data for form: salary\_grade
- Requirements:

- ihris-manage-Job at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-salary\_grade/ \[46\]

## SampleData-salary\_source

This describes version 4.0.0 of the module Salary Source (SampleData-salary\_source)

- Source: manage/modules/MedicalData/modules/SampleData-salary\_source \[47\]

- Description: Sample Data for form: salary\_source
- Requirements:

- ihris-manage-Salary at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-salary\_source/ \[48\]

## SampleData-training\_course\_category

This describes version 4.0.0 of the module Training Course Category (SampleData-training\_course\_category)

- Source: manage/modules/MedicalData/modules/SampleData-training\_course\_category \[49\]

- Description: Sample Data for form: training\_course\_category
- Requirements:

- training-course at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-training\_course\_category/ \[50\]

## SampleData-training\_course\_requestor

This describes version 4.0.0 of the module Training Requestor (SampleData-training\_course\_requestor)

- Source: manage/modules/MedicalData/modules/SampleData-training\_course\_requestor \[51\]

- Description: Sample Data for form: training\_course\_requestor
- Requirements:

- training-course at least 4.0
- Paths:

- Classes: modules/MedicalData/modules/SampleData-training\_course\_requestor/ \[52\]

## accident

This describes version 4.0.6.0 of the module Workplace Accident (accident)

- Source: manage/modules/Accident \[53\]

- Module Class: The module class is implemented by iHRIS\_Module\_Accident
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_accident() via action\_accident()
- Description: A Workplace Accident Tracking Module
- Requirements:

- Person at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Accident/configs \[54\]

- Classes: modules/Accident/lib \[55\]

- iHRIS\_Module\_Accident
- Templates: modules/Accident/templates \[56\]

view\_list\_accident\_type.html, form\_accident.html, view\_accident.html

## disciplinary\_action

This describes version 4.0.6.1 of the module Disciplinary Action (disciplinary\_action)

- Source: manage/modules/Disciplinary \[57\]

- Module Class: The module class is implemented by iHRIS\_Module\_DisciplinaryAction
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_disciplinary\_action() via action\_disciplinary\_action()
- Description: A Disciplinary Action Tracking Module
- Requirements:

- Person at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Disciplinary/configs \[58\]

- Classes: modules/Disciplinary/lib \[59\]

- iHRIS\_Module\_DisciplinaryAction
- Templates: modules/Disciplinary/templates \[60\]

form\_disciplinary\_action.html, view\_list\_disciplinary\_action\_type.html, view\_disciplinary\_action.html

## ihris-manage

This describes version 4.0.6.0 of the module iHRIS Manage (ihris-manage) It is the top module of this package

- Source: manage/ \[61\]

- Module Class: The module class is implemented by iHRIS\_Module\_Manage
- Description: The iHRIS Manage system.
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- ihris-manage-Person at least 4.0 and less than 4.1
- ihris-manage-PersonPosition at least 4.0 and less than 4.1
- ihris-manage-Benefit at least 4.0 and less than 4.1
- Currency at least 4.0 and less than 4.1
- simple-competency at least 4.0 and less than 4.1
- ihris-common-Search at least 4.0 and less than 4.1
- ihris-common-RecentForm at least 4.0 and less than 4.1
- Conflicts:

- ihris-qualify at least 2 and less than 5
- ihris-plan at least 1 and less than 2
- Optionally Enables: ihris-manage-CustomReports ihris-manage-Application ihris-manage-help FacilityContact ManageRegistration
- Paths:

- Configs: /configs \[62\]

- Classes: /lib \[63\]

- iHRIS\_Module\_Manage, iHRIS\_PageManage
- Templates: /templates \[64\]

- view.html, lists.html, menu\_manage.html, shell.html, manage.html, index.html, menu\_view\_person.html
- Css: /css \[65\]

- Scripts: /scripts \[66\]

- Images: /images \[67\]

- Modules: /modules \[68\]

ManageRegistration, accident, disciplinary\_action, ihris-manage-Application, ihris-manage-Benefit, ihris-manage-CustomReports, ihris-manage-Job, ihris-manage-Person, ihris-manage-PersonDemographic, ihris-manage-PersonPosition, ihris-manage-Salary, ihris-manage-base-data, ihris-manage-confirmation, ihris-manage-help, ihris-manage-medical-data, ihris-manage-sample-data, manage-training-course

## ihris-manage-Application

This describes version 4.0.0 of the module iHRIS Manage Application (ihris-manage-Application)

- Source: manage/modules/ManageApplication \[69\]

- Module Class: The module class is implemented by iHRIS\_Module\_Application
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_application() via action\_application()
- Implements the method iHRIS\_PageView-&gt;action\_position\_decision() via action\_position\_decision()
- Implements the method iHRIS\_PageView-&gt;action\_position\_interview() via action\_position\_interview()
- Description: The iHRIS Manage Application Module.

- Requirements:

- ihris-manage-PersonPosition at least 4.0 and less than 4.1

- Person at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageApplication/configs \[70\]

- Classes: modules/ManageApplication/lib \[71\]

- iHRIS\_Applicant, iHRIS\_Module\_Application
- Modules: modules/ManageApplication/modules \[72\]

- ihris-manage-ApplicationAttachment
- Templates: modules/ManageApplication/templates \[73\]

form\_position\_decision.html, form\_position\_interview.html, view\_position\_interview.html, applicant\_review\_results.html, applicant\_review\_row.html, applicant\_review\_list\_entry.html, applicant\_review\_list.html, form\_application.html, applicant\_review\_no\_results.html, view\_position\_decision.html, applicant\_review.html, view\_application.html

## ihris-manage-ApplicationAttachment

This describes version 4.0.7.2 of the module iHRIS Manage Application Attachments (ihris-manage-ApplicationAttachment)

- Source: manage/modules/ManageApplication/modules/ApplicationAttachments \[74\]

- Description: Allows attachments to Position Decisions and Position Interview forms
- Requirements:

- ihris-manage-Application at least 4.0 and less than 4.1
- BinField at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageApplication/modules/ApplicationAttachments/configs \[75\]

- Classes: modules/ManageApplication/modules/ApplicationAttachments/ \[76\]

## ihris-manage-Benefit

This describes version 4.0.4 of the module iHRIS Manage Benefit (ihris-manage-Benefit)

- Source: manage/modules/Benefit \[77\]

- Module Class: The module class is implemented by iHRIS\_Module\_Benefit
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_benefit() via action\_benefit()
- Description: The iHRIS Manage Benefit module provides basic benfit related information
- Requirements:

- Person at least 4.0
- ihris-manage-Salary at least 4.0
- Paths:

- Configs: modules/Benefit/configs \[78\]

- Classes: modules/Benefit/lib \[79\]

- iHRIS\_Benefit, iHRIS\_Module\_Benefit
- Templates: modules/Benefit/templates \[80\]

form\_benefit.html, view\_benefit.html, view\_list\_benefit\_type.html

## ihris-manage-ConfirmationAttachment

This describes version 4.0.6.0 of the module iHRIS Manage Confirmation Attachments (ihris-manage-ConfirmationAttachment)

- Source: manage/modules/Confirmation/modules/ConfirmationAttachments \[81\]

- Description: Allows attachments to Confirmation forms
- Requirements:

- ihris-manage-confirmation at least 4.0 and less than 4.1
- BinField at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Confirmation/modules/ConfirmationAttachments/configs \[82\]

- Classes: modules/Confirmation/modules/ConfirmationAttachments/ \[83\]

## ihris-manage-CustomReports

This describes version 4.0.0 of the module iHRIS Manage Custom Reports (ihris-manage-CustomReports)

- Source: manage/modules/ManageCustomReports \[84\]

- Description: The Manage Reporting System
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Optionally Enables: CustomReports\_PieChart CustomReports\_Export CustomReports\_PDF ihris-manage-CustomReports-position-reports ihris-manage-CustomReports-staff-reports ihris-manage-CustomReports-facility-reports ihris-manage-CustomReports-search-people
- Paths:

- Configs: modules/ManageCustomReports/configs \[85\]

- Pdf\_images: modules/ManageCustomReports/pdf\_images \[86\]

- Modules: modules/ManageCustomReports/Reports \[87\]

- ihris-manage-CustomReports-FilledPositions, ihris-manage-CustomReports-facility-reports, ihris-manage-CustomReports-position-reports, ihris-manage-CustomReports-search-people, ihris-manage-CustomReports-staff-reports
- Classes: modules/ManageCustomReports/ \[88\]

## ihris-manage-CustomReports-FilledPositions

This describes version 4.0.0 of the module iHRIS Manage Filled Positions Reports (ihris-manage-CustomReports-FilledPositions)

- Source: manage/modules/ManageCustomReports/Reports/FilledPositions \[89\]

- Description: The Manage Report for Filled Positions
- Requirements:

- ihris-manage-CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageCustomReports/Reports/FilledPositions/configs \[90\]

- Classes: modules/ManageCustomReports/Reports/FilledPositions/ \[91\]

## ihris-manage-CustomReports-facility-reports

This describes version 4.0.0 of the module iHRIS Manage Facility Reports (ihris-manage-CustomReports-facility-reports)

- Source: manage/modules/ManageCustomReports/Reports/FacilityReports \[92\]

- Description: The Manage Reports based on the Facility relationship.
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageCustomReports/Reports/FacilityReports/configs \[93\]

- Classes: modules/ManageCustomReports/Reports/FacilityReports/ \[94\]

## ihris-manage-CustomReports-position-reports

This describes version 4.0.0.2 of the module iHRIS Manage Position Reports (ihris-manage-CustomReports-position-reports)

- Source: manage/modules/ManageCustomReports/Reports/PositionReports \[95\]

- Description: The Manage Reports based on the Position relationship
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageCustomReports/Reports/PositionReports/configs \[96\]

- Classes: modules/ManageCustomReports/Reports/PositionReports/ \[97\]

## ihris-manage-CustomReports-search-people

This describes version 4.0.0 of the module Custom Reports - Search People (ihris-manage-CustomReports-search-people)

- Source: manage/modules/ManageCustomReports/Reports/SearchPeople \[98\]

- Description: The definition of the search people report for Manage.
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageCustomReports/Reports/SearchPeople/configs \[99\]

- Classes: modules/ManageCustomReports/Reports/SearchPeople/ \[100\]

## ihris-manage-CustomReports-staff-reports

This describes version 4.0.8.1 of the module iHRIS Manage Custom Staff Reports (ihris-manage-CustomReports-staff-reports)

- Source: manage/modules/ManageCustomReports/Reports/StaffReports \[101\]

- Description: The Manage Staff Reports
- Requirements:

- CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageCustomReports/Reports/StaffReports/configs \[102\]

- Classes: modules/ManageCustomReports/Reports/StaffReports/ \[103\]

## ihris-manage-Job

This describes version 4.0.6.3 of the module iHRIS Manage Job (ihris-manage-Job)

- Source: manage/modules/ManageJob \[104\]

- Module Class: The module class is implemented by iHRIS\_Module\_ManageJob
- Description: The iHRIS Manage Job
- Requirements:

- ihris-common-Job at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManageJob/configs \[105\]

- Classes: modules/ManageJob/lib \[106\]

- iHRIS\_ManageJob, iHRIS\_Module\_ManageJob, iHRIS\_PageViewJob
- Templates: modules/ManageJob/templates \[107\]

- view\_list\_job.html, lists\_form\_salary\_grade.html, view\_job.html, lists\_form\_job.html, view\_list\_salary\_grade.html
- Modules: modules/ManageJob/modules \[108\]

## ihris-manage-Person

This describes version 4.0.3 of the module iHRIS Manage Person (ihris-manage-Person)

- Source: manage/modules/ManagePerson \[109\]

- Description: The iHRIS Manage Person
- Requirements:

- Person at least 4.0
- Paths:

- Classes: modules/ManagePerson/lib \[110\]

iHRIS\_PageFormPersonManage

## ihris-manage-PersonDemographic

This describes version 4.0.0 of the module iHRIS Manage Person Demographic (ihris-manage-PersonDemographic)

- Source: manage/modules/ManagePersonDemographic \[111\]

- Description: The iHRIS Manage Person Demographic
- Requirements:

- Person at least 4.0
- PersonDemographic at least 4.0
- Paths:

- Configs: modules/ManagePersonDemographic/configs \[112\]

- Templates: modules/ManagePersonDemographic/templates \[113\]

- form\_demographic.html, view\_demographic.html
- Classes: modules/ManagePersonDemographic/ \[114\]

## ihris-manage-PersonPosition

This describes version 4.0.6.2 of the module iHRIS Manage Person Position (ihris-manage-PersonPosition)

- Source: manage/modules/ManagePersonPosition \[115\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonPosition
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_position() via action\_person\_position()
- Implements the method iHRIS\_Person-&gt;getLastPosition() via getLastPosition()
- Implements the method iHRIS\_Person-&gt;isActive() via isActive\_Person()
- Implements the method iHRIS\_PersonPosition-&gt;isActive() via isActive\_PersonPosution()
- Description: The iHRIS Manage Position. Adds a position which is linked to a person and is defined by a job,
- Requirements:

- ihris-manage-Job at least 4.0 and less than 4.1
- Person at least 4.0 and less than 4.1
- Facility at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- ihris-manage-Benefit at least 4.0 and less than 4.1
- Paths:

- Configs: modules/ManagePersonPosition/configs \[116\]

- Classes: modules/ManagePersonPosition/lib \[117\]

- iHRIS\_Module\_PersonPosition, iHRIS\_PageFormDeparture, iHRIS\_PageFormMakeOffer, iHRIS\_PageFormSalary, iHRIS\_PageViewPosition, iHRIS\_PersonPosition, iHRIS\_Position, iHRIS\_SalaryHistoryPage
- Templates: modules/ManagePersonPosition/templates \[118\]

salary\_history.html, view\_position\_open\_link.html, view\_list\_position\_type.html, view\_salary.html, lists\_form\_department.html, lists\_type\_mapped\_position\_status.html, salary\_history\_position.html, view\_job\_positions.html, button\_confirm\_position.html, view\_position\_discontinued\_link.html, form\_person\_position.html, form\_departure.html, form\_salary.html, view\_position\_row.html, salary\_history\_add.html, salary\_history\_salary.html, lists\_form\_position.html, view\_person\_position.html, view\_list\_pos\_change\_reason.html, form\_salary\_change.html, form\_make\_offer.html, view\_position\_supervised.html, form\_make\_promotion.html, view\_position.html, view\_list\_department.html, view\_position\_person.html

## ihris-manage-Salary

This describes version 4.0.0 of the module iHRIS Manage Salary (ihris-manage-Salary)

- Source: manage/modules/Salary \[119\]

- Module Class: The module class is implemented by iHRIS\_Module\_ManageSalary
- Description: The iHRIS Manage Salary module provides salary and salary source forms
- Requirements:

- ihris-manage-Person at least 4.0
- Currency at least 4.0
- Paths:

- Configs: modules/Salary/configs \[120\]

- Classes: modules/Salary/lib \[121\]

iHRIS\_Module\_ManageSalary

- Templates: modules/Salary/templates \[122\]

view\_list\_salary\_source.html

## ihris-manage-base-data

This describes version 4.0.4 of the module iHRIS Manage Base Data (ihris-manage-base-data)

- Source: manage/modules/BaseData \[123\]

- Description: iHRIS Manage Base Data
- Requirements:

- BackgroundProcess at least 4.0 and less than 4.1
- ihris-manage at least 4.0 and less than 4.1
- SampleData-Common at least 4.0
- Optionally Enables: SampleData-benefit\_type SampleData-language SampleData-marital\_status SampleData-pos\_change\_reason SampleData-id\_type SampleData-accident\_type
- Paths:

- Modules: modules/BaseData/modules \[124\]

- SampleData-accident\_type, SampleData-benefit\_type, SampleData-id\_type, SampleData-language, SampleData-marital\_status, SampleData-pos\_change\_reason
- Classes: modules/BaseData/ \[125\]

## ihris-manage-confirmation

This describes version 4.0.6.2 of the module iHRIS Manage Confirmation (ihris-manage-confirmation)

- Source: manage/modules/Confirmation \[126\]

- Module Class: The module class is implemented by iHRIS\_Module\_Confirmation
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_confirmation() via action\_confirmation()
- Description: The iHRIS Manage Confirmation module provides confirmation tracking
- Requirements:

- Person at least 4.0 and less than 4.1
- ihris-manage-PersonPosition at least 4.0 and less than 4.1
- ihris-common-Job at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Confirmation/configs \[127\]

- Classes: modules/Confirmation/lib \[128\]

- iHRIS\_Module\_Confirmation
- Modules: modules/Confirmation/modules \[129\]

- ihris-manage-ConfirmationAttachment
- Templates: modules/Confirmation/templates \[130\]

form\_confirmation.html, view\_list\_confirmation\_type.html, add\_confirmation.html, view\_confirmation.html, lists\_form\_confirmation\_type.html

## ihris-manage-help

This describes version 4.0.0 of the module iHRIS Manage Help (ihris-manage-help)

- Source: manage/modules/manage-help \[131\]

- Description: The iHRIS Manage Help system.
- Requirements:

- ihris-manage at least 4.0 and less than 4.1
- Paths:

- Static: modules/manage-help/static \[132\]

- Images: modules/manage-help/images \[133\]

- Scripts: modules/manage-help/scripts \[134\]

- Css: modules/manage-help/css \[135\]

- Classes: modules/manage-help/ \[136\]

## ihris-manage-medical-data

This describes version 4.0.0 of the module iHRIS Manage Medical Base Data (ihris-manage-medical-data)

- Source: manage/modules/MedicalData \[137\]

- Description: iHRIS Manage Medical Base Data
- Requirements:

- ihris-manage-base-data at least 4.0 and less than 4.1
- Optionally Enables: SampleData-cadre SampleData-department SampleData-salary\_grade SampleData-classification SampleData-facility\_type SampleData-salary\_source SampleData-competency SampleData-job SampleData-training\_course\_category SampleData-competency\_type SampleData-position\_type SampleData-training\_course\_requestor SampleData-council SampleData-disciplinary\_action\_type
- Paths:

- Modules: modules/MedicalData/modules \[138\]

- SampleData-cadre, SampleData-classification, SampleData-competency, SampleData-competency\_type, SampleData-council, SampleData-department, SampleData-disciplinary\_action\_type, SampleData-facility\_type, SampleData-job, SampleData-position\_type, SampleData-salary\_grade, SampleData-salary\_source, SampleData-training\_course\_category, SampleData-training\_course\_requestor
- Classes: modules/MedicalData/ \[139\]

## ihris-manage-sample-data

This describes version 4.0.0 of the module iHRIS Manage Sample Data (ihris-manage-sample-data)

- Source: manage/modules/SampleData \[140\]

- Module Class: The module class is implemented by iHRIS\_Module\_Manage\_SampleData
- Description: iHRIS Manage Sample Data
- Requirements:

- ihris-manage-medical-data at least 4.0 and less than 4.1
- Optionally Enables: SampleData-facility SampleData-establishment SampleData-confirmation\_type
- Paths:

- Sql: modules/SampleData/sql \[141\]

- Modules: modules/SampleData/modules \[142\]

SampleData-confirmation\_type, SampleData-establishment, SampleData-facility

- Classes: modules/SampleData/ \[143\]

iHRIS\_Module\_Manage\_SampleData

## manage-training-course

This describes version 4.0.0 of the module Manage Traning Course (manage-training-course)

- Source: manage/modules/ManageTrainingCourse \[144\]

- Description: Makes the training course module available to iHRIS Manage
- Requirements:

- ihris-manage at least 4.0 and less than 4.1
- training-course at least 4.0 and less than 4.1
- Optionally Enables: manage-training-institution manage-training-simple-competency
- Paths:

- Modules: modules/ManageTrainingCourse/modules \[145\]

- manage-training-institution, manage-training-simple-competency
- Classes: modules/ManageTrainingCourse/ \[146\]

## manage-training-institution

This describes version 4.0.0 of the module Manage Training Institutions (manage-training-institution)

- Source: manage/modules/ManageTrainingCourse/modules/ManageTrainingInstitutions \[147\]

- Description: Makes training institution and funder information available to iHRIS Manage training course module
- Requirements:

- manage-training-course at least 4.0 and less than 4.1
- training-institution at least 4.0 and less than 4.1
- Paths:

- Classes: modules/ManageTrainingCourse/modules/ManageTrainingInstitutions/ \[148\]

## manage-training-simple-competency

This describes version 4.0.0 of the module Manage Training Competency (Simple) (manage-training-simple-competency)

- Source: manage/modules/ManageTrainingCourse/modules/ManageTrainingSimpleCompetency \[149\]

- Description: Makes the Simple Competency module available to iHRIS Manage training course module
- Requirements:

- manage-training-course at least 4.0 and less than 4.1
- training-simple-competency at least 4.0 and less than 4.1
- Paths:

- Classes: modules/ManageTrainingCourse/modules/ManageTrainingSimpleCompetency/ \[150\]

## References

\[1\] https://launchpad.net/ihris-manage \[2\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageRegistration \[3\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageRegistration/configs \[4\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageRegistration/templates \[5\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageRegistration/lib \[6\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-accident\_type \[7\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-accident\_type/ \[8\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-benefit\_type \[9\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-benefit\_type/ \[10\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-cadre \[11\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-cadre/ \[12\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-classification \[13\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-classification/ \[14\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-competency \[15\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-competency/ \[16\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-competency\_type \[17\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-competency\_type/ \[18\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-confirmation\_type \[19\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-confirmation\_type/ \[20\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-council \[21\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-council/ \[22\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-department \[23\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-department/ \[24\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-disciplinary\_action\_type \[25\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-disciplinary\_action\_type/ \[26\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-Establishment \[27\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-Establishment/configs \[28\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-Establishment/ \[29\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-facility

\[30\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules/

SampleData-facility/ \[31\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-facility\_type

\[32\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-facility\_type/ \[33\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-id\_type \[34\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-id\_type/ \[35\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-job \[36\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-job/ \[37\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-language \[38\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-language/ \[39\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-marital\_status \[40\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-marital\_status/ \[41\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-pos\_change\_reason \[42\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules/

SampleData-pos\_change\_reason/ \[43\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-position\_type \[44\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-position\_type/ \[45\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-salary\_grade \[46\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-salary\_grade/ \[47\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-salary\_source \[48\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-salary\_source/ \[49\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-training\_course\_category \[50\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-training\_course\_category/ \[51\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-training\_course\_requestor \[52\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules/

SampleData-training\_course\_requestor/ \[53\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Accident \[54\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Accident/configs \[55\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Accident/lib \[56\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Accident/templates \[57\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Disciplinary \[58\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Disciplinary/configs \[59\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Disciplinary/lib \[60\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Disciplinary/templates \[61\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/ \[62\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://configs \[63\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://lib \[64\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://templates \[65\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://css \[66\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://scripts

\[67\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://images \[68\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head://modules \[69\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication

\[70\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/configs \[71\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/lib \[72\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/modules \[73\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/templates \[74\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/modules/

ApplicationAttachments \[75\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/modules/

ApplicationAttachments/configs \[76\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageApplication/modules/

ApplicationAttachments/ \[77\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Benefit \[78\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Benefit/configs \[79\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Benefit/lib \[80\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Benefit/templates \[81\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/modules/

ConfirmationAttachments \[82\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/modules/

ConfirmationAttachments/configs \[83\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/modules/

ConfirmationAttachments/ \[84\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports \[85\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

configs \[86\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

pdf\_images \[87\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports \[88\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/ \[89\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FilledPositions \[90\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FilledPositions/configs \[91\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FilledPositions/ \[92\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FacilityReports \[93\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FacilityReports/configs \[94\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/FacilityReports/ \[95\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/PositionReports \[96\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/PositionReports/configs \[97\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/PositionReports/ \[98\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/SearchPeople \[99\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/SearchPeople/configs \[100\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/SearchPeople/ \[101\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/StaffReports \[102\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/StaffReports/configs

\[103\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageCustomReports/

Reports/StaffReports/ \[104\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageJob

\[105\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageJob/configs \[106\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageJob/lib \[107\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageJob/templates \[108\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageJob/modules \[109\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePerson \[110\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePerson/lib \[111\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonDemographic \[112\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonDemographic/

configs \[113\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonDemographic/

templates \[114\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonDemographic/ \[115\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonPosition \[116\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonPosition/

configs \[117\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonPosition/lib \[118\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManagePersonPosition/

templates \[119\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Salary \[120\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Salary/configs \[121\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Salary/lib \[122\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Salary/templates \[123\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData \[124\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/modules \[125\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/BaseData/ \[126\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation \[127\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/configs \[128\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/lib \[129\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/modules \[130\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/Confirmation/templates \[131\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help \[132\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help/static \[133\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help/images \[134\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help/scripts \[135\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help/css \[136\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/manage-help/ \[137\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData

\[138\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/modules \[139\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/MedicalData/ \[140\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData \[141\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/sql \[142\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/modules \[143\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/SampleData/ \[144\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse \[145\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/

modules \[146\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/ \[147\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/

modules/ManageTrainingInstitutions \[148\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/

modules/ManageTrainingInstitutions/ \[149\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/

modules/ManageTrainingSimpleCompetency \[150\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0.6-release/files/head:/modules/ManageTrainingCourse/

modules/ManageTrainingSimpleCompetency/
