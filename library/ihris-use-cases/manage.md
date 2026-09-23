---
title: "iHRIS Manage use cases (2009)"
source: uploads/ihris-use-cases/iHRISManageUseCases.doc
licence: owner permission, 2026-09-23 (see ihris-use-cases.json)
---

# iHRIS Manage: use cases (2009)

*Serlio Software Case Complete, 7/13/2009 3:28 PM. From the iHRIS use-case model by IntraHealth International / the Capacity Project iHRIS team, published here with the owner's permission. Parsed by `src/tools/ingest_use_cases.py`; do not edit by hand.*

iHRIS Manage is a human resources management tool that enables an organization to design and manage a comprehensive human resources strategy.

- This documentation refers to the core version of the HR Management database (working title: PowerTrack). *(9/13/2006)*
- The specifications were based on the requirements gathered for the Rwanda release Version 1.0. It also includes some specifications gathered for release to IntraHealth HR department. *(9/13/2006)*
- An earlier version of the system was released in Rwanda as RW-MOH 0.9a *(9/13/2006)*
- Core Version 2.0 released April 16, 2007. *(5/7/2007)*
- Core Version 3.0 released March 18, 2008. *(7/24/2008)*
- Core Version 3.1 released August 15, 2008. *(9/29/2008)*
- Core Version 4.0 released July 13, 2009. *(7/13/2009)*

Related documents: https://launchpad.net/ihris-manage, http://www.capacityproject.org/hris/suite/ihris\_manage.php

## Actors

### A-PT1 HR Manager

This person is a manager of HR personnel and is responsible for ensuring that data in the system are complete, correct and up to date. This person will also run reports and analyze data in order to make organizational or individual HR decisions. This person has permission to view any record in the system.

**Goals**

- Create standard lists of data for selection in the system.
- Add geographical locations to the organizational structure.
- Add offices and facilities to the organizational structure.
- Create a job structure for the organization.
- Check for and correct data errors.
- Report on data quality.
- Create report views.

**Notes**

- Can perform any use case that HR Staff, Training Manager or Executive Manager can perform.

**Use cases:** UC-PT8 Add or update a benefit type, UC-PT17 Add or update a cadre, UC-PT69 Add or update a continuing education course, UC-PT11 Add or update a country, UC-PT14 Add or update a county, UC-PT15 Add or update a currency, UC-PT5 Add or update a degree, UC-PT3 Add or update a department, UC-PT13 Add or update a district, UC-PT1 Add or update a facility type, UC-PT18 Add or update a job classification, UC-PT6 Add or update a language, UC-PT9 Add or update a marital status, UC-PT22 Add or update a position type, UC-PT10 Add or update a reason for departure, UC-PT12 Add or update a region, UC-PT70 Add or update a registration council, UC-PT21 Add or update a salary source, UC-PT4 Add or update an education type, UC-PT7 Add or update an identification type, UC-PT2 Add or update an office or facility, UC-PT49 Create a competency model, UC-PT20 Create a job, UC-PT19 Create a salary grade, UC-PT35 Record a salary change

### A-PT2 HR Staff

This person is responsible for entering and updating data in the system. This person can update and view any record in the system.

**Goals**

- Create and update positions.
- Enter application information for a job applicant.
- Review applicants and make a job offer to an applicant.
- Add a new employee record.
- Enter information into or update information in an employee's record.
- Record position and salary changes in an employee's record.
- Generate standard position lists, organizational charts, staff lists and staff directories.

**Notes**

- Can perform any use case that a Training Manager can perform.
- This person cannot create customized report views.

**Use cases:** UC-PT31 Add contact information, UC-PT30 Add demographic information, UC-PT29 Add identification information, UC-PT36 Add language proficiencies, UC-PT71 Add registrations, UC-PT40 Apply for a position, UC-PT50 Assess an employee's competencies, UC-PT23 Create a position, UC-PT25 Discontinue a position, UC-PT27 Enter a new record, UC-PT44 Enter educational history, UC-PT43 Enter employment history, UC-PT42 Log a hiring decision, UC-PT41 Log interview details, UC-PT46 Make a job offer, UC-PT34 Record a position change, UC-PT35 Record a salary change, UC-PT32 Record a special payment, UC-PT37 Record notes, UC-PT45 Review applicants, UC-PT28 Set a position for an employee, UC-PT33 Terminate an employee, UC-PT24 Update a position

### A-PT3 Executive Manager

This person will run reports and analyze data in order to make organizational HR decisions.

**Goals**

- Search for and view employee and position records.
- Run standard reports to analyze data entered in the system.
- Assess organizational competencies held by all employees and search for employee qualifications.
- Review applicants for a position.

**Notes**

- This person has permission to view any record in the system but cannot update or change data in an employee record.
- This person cannot create customized report views.

**Use cases:** UC-PT45 Review applicants

### A-PT8 Training Manager

This person is responsible for managing training programs taken by employees and updating employee competencies.

**Goals**

- Create a competency model for the organization.
- Assess an employee's competencies.
- Search for employees who hold particular competencies.
- Add training information and manage the list of available training programs.
- Schedule trainings for employees.
- Assess an employee's training results and update the employee's training history.
- Report on employees who have received trainings.

**Notes**

- This is a new actor who is focused on the training module functions. HR Staff may complete any use case that the HR Training Manager can.

**Use cases:** UC-PT68 Add or update a competency evaluation, UC-PT55 Add or update a training course category, UC-PT67 Add or update a training course evaluation, UC-PT66 Add or update a training course requestor, UC-PT65 Add or update a training course status, UC-PT53 Add or update a training funder, UC-PT54 Add or update a training organization, UC-PT56 Add or update an in-service training program, UC-PT50 Assess an employee's competencies, UC-PT60 Assess training results and update competencies, UC-PT49 Create a competency model, UC-PT57 Enter the schedule for a training program, UC-PT59 Schedule a training for an employee

## 1.1 Data Administration

Create and update standard lists of data for selection in system menus.

- Access is limited to HR Managers and System Administrators. *(5/7/2007)*
- Locate these functions via the Configure System --> Administer Database link on the main menu. *(9/28/2007)*

### UC-PT1 Add or update a facility type

The HR Manager adds a new facility type for selection in the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The facility type is added to the system and is available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage the list of facility types.
2. The system displays all facility types entered in the system.
3. The user adds a new facility type.
4. The user enters a description or name for the facility type.
5. The user saves the record (UC-ICE2).
6. The system makes the facility type available for selection when adding facilities.

**Extensions**

- **3.a** The user selects an existing facility type.
    1. The system opens the facility type for editing.
- **5.a** The system determines that the facility type already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `facility_type` (I2CE_SimpleList) in ihris-common

### UC-PT2 Add or update an office or facility

The HR Manager adds a new office or facility for selection within the system and ties it to an institution type.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The office/facility is saved to the system and is available for selection within various use cases and for reporting.

**Main success scenario**

1. The user selects the option to manage the list of offices/facilities.
2. The system displays all offices/facilities entered in the system.
3. The user adds a new office/facility.
4. The user enters the name (description) of the office/facility.
5. The user selects the facility type for the office/facility.
6. The user adds the facility's contact information (UC-PT31).
7. The user selects the country where the office/facility is located.
8. The system displays all districts in that country.
9. The user selects the district where the office/facility is located.
10. The system displays all counties in that district.
11. The user selects the county where the office/facility is located (optional).
12. The user saves the record (UC-ICE2).
13. The system displays the office or facility's record.
14. The system provides the option to update the office or facility information.
15. The system makes the office or facility available for selection and reporting.

**Extensions**

- **3.a** The user selects an existing office or facility.
    1. The system opens the item for editing.
- **5.a** The user adds a new facility type (UC-PT1).
    1. The user returns to Step 1 to add the office/facility.
- **7.a** The user adds a new country (UC-PT11).
    1. The user returns to Step 1 to add the office/facility.
- **8.a** The user adds a new district (UC-PT13).
    1. The user returns to Step 1 to add the office/facility.
- **10.a** The user adds a new county (UC-PT14).
    1. The user returns to Step 1 to add the office/facility.
- **12.a** The system determines that the office/facility name already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `facility` (iHRIS_Facility) in ihris-common

### UC-PT3 Add or update a department

The HR Manager adds a new department to the list of departments available for selection in the system.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The department is saved and is available for selection within various use cases and for reporting.

**Main success scenario**

1. The user selects the option to update the list of departments.
2. The system displays all departments previously entered into the system.
3. The user adds a new department.
4. The user enters the name of the department.
5. The user saves the record (UC-ICE2).
6. The system makes the department available for selection when adding positions.

**Extensions**

- **3.a** The user selects an existing department.
    1. The system opens the department for editing.
- **5.a** The system determines that the department already exists in the databse.
    1. The system displays an error and will not continue.

**Notes**

- This functionality may be accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `department` (iHRIS_Department) in ihris-manage

### UC-PT70 Add or update a registration council

The HR Manager adds a new registration council to the list of registration councils available for selection in the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 4.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The registration council is saved and is available for selection within various use cases and for reporting.

**Main success scenario**

1. The user selects the option to update the list of registration councils.
2. The system displays all registration councils previously entered into the system.
3. The user adds a new registration council.
4. The user enters the name of the registration council.
5. The user saves the record (UC-ICE2).
6. The system makes the registration council available for selection when adding a qualification to an employee record.

**Extensions**

- **3.a** The user selects an existing registration council.
    1. The system opens the registration council for editing.
- **5.a** The system determines that the registration council already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality may be accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `council` (I2CE_SimpleList) in ihris-common, `registration` (iHRIS_Registration) in ihris-common

### UC-PT4 Add or update an education type

The HR Manager updates a list of education types that are available for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new education type is saved and available for selection when adding a degree.

**Main success scenario**

1. The user selects the option to manage the list of education types.
2. The system displays all education types entered in the system..
3. The user adds a new education type.
4. The user enters the description or name of the education type.
5. The user saves the record. (UC-ICE2)
6. The system makes the education type available for selection when adding educational information.

**Extensions**

- **3.a** The user selects an existing education type.
    1. The system opens the education type for editing.
- **5.a** The system determines that the education type already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `edu_type` (I2CE_SimpleList) in ihris-common

### UC-PT5 Add or update a degree

The HR Manager adds a type of educational institution to the system and associates it with degrees that it issues.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** A new degree is associated with its education type and made available for selection from various use cases.

**Main success scenario**

1. The user selects the option to manage the list of degrees.
2. The system displays all education types entered in the system.
3. The user selects an education type.
4. The system displays a list of matching degrees for that education type.
5. The user adds a new degree.
6. The user enters the name (description) of the degree.
7. The user selects the education type for the degree.
8. The user saves the record (UC-ICE2).
9. The system makes the degree available for selection when adding educational information.

**Extensions**

- **3.a** The user does not select an education type.
    1. The system provides the option to add a new degree only.
    2. Skip to Step 6.
- **5.a** The user selects an existing degree.
    1. The system opens the degree for editing.
- **7.a** The user adds a new educational type.
    1. The user returns to Step 1 to add the degree.
- **7.b** The user already selected the education type.
    1. The system fills in the selected education type when the degree is added.
- **8.a** The system determines that the degree already exists in the database for the selected education type.
    1. The system displays an error message and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `degree` (iHRIS_Degree) in ihris-common

### UC-PT6 Add or update a language

The HR Manager updates a list of languages that are available for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new language is saved and available for selection.

**Main success scenario**

1. The user selects the option to manage languages.
2. The system displays all languages entered in the system.
3. The user adds a new language.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the language available for selection when adding language proficiency.

**Extensions**

- **3.a** The user selects an existing language.
    1. The system opens the language for editing.
- **5.a** The system determines that the language already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `language` (I2CE_SimpleList) in ihris-common

### UC-PT7 Add or update an identification type

The HR Manager updates a list of identification types that are available for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new identification type is saved and available for selection when adding an identification.

**Main success scenario**

1. The user selects the option to manage the list of identification types.
2. The system displays all identification types entered in the system.
3. The user adds a new identification type.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the identification type available for selection when adding identifications.

**Extensions**

- **3.a** The user selects an existing identification type.
    1. The system opens the identification type for editing.
- **5.a** The system determines that the identification type already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is identical for both iHRIS Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `id_type` (iHRIS_PersonID_Type) in ihris-common

### UC-PT8 Add or update a benefit type

The HR Manager updates a list of benefit types that are available for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system

**Success guarantee.** The new benefit type is saved and available for selection when adding a benefit.

**Main success scenario**

1. The user selects the option to manage benefit types.
2. The system displays all benefit types entered in the system.
3. The user adds a new benefit type.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the benefit type available for selection when adding benefits.

**Extensions**

- **3.a** The user selects an existing benefit type.
    1. The system opens the benefit type for editing.
- **5.a** The system determines that the benefit type already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `benefit_type` (I2CE_SimpleList) in ihris-manage

### UC-PT9 Add or update a marital status

The HR Manager adds a new marital status to the system that is available in selection lists.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The marital status is added to the system and is available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage the list of marital statuses.
2. The system displays all marital statuses entered in the system.
3. The user adds a new marital status.
4. The user enters a description for the marital status.
5. The user saves the record (UC-ICE2).
6. The system makes the marital status available for selection when adding demographic information.

**Extensions**

- **3.a** The user selects an existing marital status.
    1. The system opens the marital status for editing.
- **5.a** The system determines that the marital status already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is the same for both iHRIS Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `marital_status` (I2CE_SimpleList) in ihris-common

### UC-PT10 Add or update a reason for departure

The HR Manager updates a list of reasons for departure that are available for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new reason for departure is saved and available for selection.

**Main success scenario**

1. The user selects the option to manage the list reasons for departure.
2. The system displays all reasons entered in the system.
3. The user adds a new reason for departure.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the reason available for selection when recording position changes.

**Extensions**

- **3.a** The user selects an existing reason for departure.
    1. The system opens the item for editing.
- **5.a** The system determines that the reason for departure already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `pos_change_reason` (I2CE_SimpleList) in ihris-manage

### UC-PT11 Add or update a country

The HR Manager updates the list of countries available for selection in the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new or changed country is defined within the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage lists of countries.
2. The system displays all countries entered in the system.
3. The user adds a new country.
4. The user enters the two-letter country code.
5. The user enters the ISO numeric code for the country (optional).
6. The user selects whether the country is the primary country for the system.
7. The user selects whether the country is used for location selection.
8. The user saves the record (UC-ICE2).
9. The system makes the country available for selection whenever adding geographical locations or nationalities/citizenships.

**Extensions**

- **3.a** The user selects an existing country.
    1. The system opens the country for editing.
- **6.a** The user selects the country as the primary country.
    1. The system displays the country first in all country selection menus.
- **6.b** The system determines that more than one country was selected as the primary country.
    1. The system displays all primary countries at the top of selection menus in alphabetical order.
- **7.a** The user selects that the country is used for location selection.
    1. The system makes the country available for selection when a location, such as an address, is being specified.
- **8.a** The system determines that the name and country code are the same as a country previously entered.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is the same for iHRIS Manage, iHRIS Plan and iHRIS Qualify. *(10/31/2007)*
- Geographical locations are tied together from largest to smallest: country --> region --> district, state or province --> county or sector. *(10/31/2007)*
- The country list also displays nationalities for selection. Disabling the location selection limits the country to nationality selection only (new feature in version 3.0). *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `country` (iHRIS_Country) in ihris-common

### UC-PT12 Add or update a region

The HR Manager updates the list of regions available for selection in the system and establishes the region's parent country.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new or changed region is defined within the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage lists of regions.
2. The system displays all countries entered in the system.
3. The user selects the country where the region is located.
4. The system displays all regions entered for that country.
5. The user adds a new region.
6. The user selects the name of the country inside which the new region is located.
7. The user enters the name of the region.
8. The user enters the code for the region (optional).
9. The user saves the record (UC-ICE2).
10. The system makes the region available for reporting.

**Extensions**

- **2.a** The user does not select a country.
    1. The system provides only the option to add a new region.
    2. Skip to Step 5.
- **5.a** The user selects an existing region.
    1. The system opens the region for editing.
- **6.a** The user adds a new country.
    1. The user returns to Step 1 to add the region.
- **6.b** The system determines that the country was previously selected.
    1. The system fills in the selected country.
- **9.a** The system determines that the name and parent country are the same as a location previously entered.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `region` (iHRIS_Region) in ihris-common

### UC-PT13 Add or update a district

The HR Manager updates the list of districts available for selection in the system and establishes the district's parent region.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new or changed district is defined within the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage lists of districts.
2. The system displays all countries entered in the system.
3. The user selects the country where the district is located.
4. The system displays all regions entered for that country.
5. The user selects the region where the district is located.
6. The system displays all districts entered for that region.
7. The user adds a new district.
8. The user selects the name of the country and region inside which the new district is located.
9. The user enters the name of the district.
10. The user enters the code for the district.
11. The user saves the record (UC-ICE2).
12. The system makes the district available for selection when adding geographical locations.

**Extensions**

- **3.a** The user does not select a country.
    1. The system provides the option to add a new district only.
    2. Skip to Step 7.
- **7.a** The user selects an existing district.
    1. The system opens the district for editing.
- **8.a** The system determines that the user previously selected the country and region.
    1. The system fills in the selections for the district.
- **11.a** The system determines that the name and parent region and country are the same as a location previously entered.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `district` (iHRIS_District) in ihris-common

### UC-PT14 Add or update a county

The HR Manager updates the list of counties available for selection in the system and establishes the county's parent district.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new or changed county is defined within the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage lists of counties.
2. The system displays all countries entered in the system.
3. The user selects the country where the county is located.
4. The system displays a list of regions for that country.
5. The user selects the region inside which the county is located.
6. The system displays all districts entered for that region.
7. The user selects the district where the county is located.
8. The system displays all districts entered for that county.
9. The user adds a new county.
10. The user selects the country, region and district where the county is located.
11. The user enters the name of the county.
12. The user saves the record (UC-ICE2).
13. The system makes the county available for selection whenever geographical locations are added.

**Extensions**

- **2.a** The user does not select a country.
    1. The system provides the option to add a new county only.
    2. Skip to Step 9.
- **9.a** The user selects an existing county.
    1. The system opens the county for editing.
- **10.a** The system determines that the country, region and district were previously selected.
    1. The system fills in the previous selections for the county.
- **12.a** The system determines that the name and parent district are the same as a location previously entered.
    1. The system displays an error message and will not continue.

**Notes**

- The use case is the same for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `county` (iHRIS_County) in ihris-common

### UC-PT15 Add or update a currency

The HR Manager adds a currency for selection when setting salaries and other monetary amounts.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new currency is added to the system and can be selected whenever specifying monetary amounts.

**Main success scenario**

1. The user selects the option to update the list of currencies.
2. The system displays all currencies entered in the system.
3. The user adds a new currency.
4. The user enters the currency code.
5. The user enters the name of the currency.
6. The user selects the country for the currency (optional).
7. The user enters the symbol for the currency (optional).
8. The user saves the record (UC-ICE2).
9. The system makes the currency available for selection by symbol and code.

**Extensions**

- **3.a** The user selects an existing currency.
    1. The system opens the currency for editing.
- **6.a** The user adds a new country.
    1. The user returns to Step 1 to add the currency.
- **8.a** The system determines that the currency already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This is a new use case requested during testing to support internationalization. Implemented in version 2.0. *(2/2/2007)*
- This use case is identical for iHRIS Manage, iHRIS Qualify and iHRIS Plan. *(7/24/2008)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `cl_currency` (I2CE_SimpleList) in ihris-common, `currency` (iHRIS_Currency) in ihris-common

## 1.2 Position Management

Design and manage a job structure for the organization, add new positions that may be filled by employees or applicants, and manage existing positions.

- Access these functions via the Configure System --> Administer Database link on the main menu. *(9/28/2007)*
- Access is limited to HR Staff, HR Manager and System Administrator. HR Staff can only add new positions, position types and salary sources. *(10/2/2007)*

### UC-PT17 Add or update a cadre

The HR Manager enters or edits a cadre for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** Each cadre, as applied by the health professionals, is defined within the system and available for selection in various use cases.

**Main success scenario**

1. The user selects the option to update the list of cadres.
2. The system displays all cadres entered in the system.
3. The user adds a new cadre.
4. The user enters the name of the cadre.
5. The user saves the record (UC-ICE2).
6. The system displays the new or edited cadre in selection lists of cadres.

**Extensions**

- **3.a** The user selects an existing cadre.
    1. The system opens the cadre for editing.
- **5.a** The system determines that the cadre already exists in the database.
    1. The system displays an error and will not proceed.

**Notes**

- This use case may be optional if new cadres are not allowed to be defined or if cadres are not used by the organization. *(10/30/2007)*
- This use case is the same for iHRIS Plan and iHRIS Manage, but not the same as iHRIS Qualify. *(7/24/2008)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `cadre` (I2CE_SimpleList) in ihris-common

### UC-PT18 Add or update a job classification

The HR Manager adds a job classification to which jobs can be assigned.

| | |
|---|---|
| Priority | P1 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Medium |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The job classification is saved and jobs can be assigned to it.

**Main success scenario**

1. The user selects the option to manage job classifications.
2. The system displays all job classifications entered in the system.
3. The user adds a new job classification.
4. The user enters the name of the job classification.
5. The user enters the classification code (optional).
6. The user enters a description of the classification (optional).
7. The user selects an ISCO classification name and code to link to the job classification.
8. The system maps the selected ISCO classification code to the job classification that the user has entered.
9. The user saves the record (UC-ICE2).
10. The system makes the job classification available for selection when adding jobs.

**Extensions**

- **3.a** The user selects an existing job classification.
    1. The system opens the job classification for editing.
- **4.a** The user selects an ISCO standard job classification name and code from the list without entering the name of a classification.
    1. The system populates the job classification name, code and description with the ISCO standard name, code and description.
    2. Go to Step 9.
- **7.a** The ISCO classification is not selected.
    1. Go on to Step 9.
- **7.b** The ISCO classification was already selected.
    1. Skip this step.
- **9.a** The system determines that the job classification already exists in the database.
    1. The system displays an error and will not proceed.

**Notes**

- This use case is optional if job categories cannot be changed or job classifications are not used in the system. *(9/28/2006)*
- The use case has been updated to link standard ISCO classification codes to job classifications or to pre-populate the system with ISCO classifications. *(10/30/2008)*
- This functionality can be accessed through Configure System --> Administer Database. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `classification` (iHRIS_Classification) in ihris-common, `job` (iHRIS_Job) in ihris-common, `job` (iHRIS_ManageJob) in ihris-manage

### UC-PT19 Create a salary grade

The HR Manager creates a new salary grade for the organization to organize jobs.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system. The currencies used for salary bands have been entered in the system.

**Success guarantee.** The salary grade is saved and jobs can be assigned to it.

**Main success scenario**

1. The user enters the option to manage the list of salary grades.
2. The system displays all salary grades entered in the system.
3. The user adds a new salary grade.
4. The user enters the name or identifier of the grade (such as a letter).
5. The user enters the currency for salary grades.
6. The user enters the starting salary of the grade.
7. The user enters the ending salary of the grade.
8. The user enters the midpoint of the grade (optional).
9. The user enters any notes about the grade (optional).
10. The user saves the record (UC-ICE2).
11. The system makes the salary grade available for selection when adding jobs.

**Extensions**

- **3.a** The user selects an existing salary grade.
    1. The system opens the salary grade for editing.
- **10.a** The system determines that the salary grade already exists in the database.
    1. The system displays an error message and will not proceed.

**Referenced requirements:** REQ-PT9 (Non-functional)

**Notes**

- This use case is intended for an organization that has jobs organized into salary bands. It is optional and not necessary for functioning of the core system. *(9/25/2006)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `salary_grade` (iHRIS_SalaryGrade) in ihris-manage

### UC-PT20 Create a job

The HR Manager creates a new job within the organization.

| | |
|---|---|
| Priority | P5 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system. A job classification or cadre for the job must be defined, if required. If a salary grade is to be assigned, it must be defined.

**Success guarantee.** The job is saved and available for selection from various use cases.

**Main success scenario**

1. The user selects the option to manage jobs.
2. The system displays all jobs entered in the system.
3. The user creates a new job.
4. The user enters the generic title of the job.
5. The user enters the code for the job (optional).
6. The user enters a job description (optional).
7. The user selects the salary grade (optional).
8. The user selects the cadre (optional).
9. The user selects the classification (optional).
10. The user selects the competencies required by the job (optional).
11. The user saves the record (UC-ICE2).
12. The system saves the job and makes it available for creating positions.

**Extensions**

- **3.a** The user selects an existing job.
    1. The system displays the job information for editing.
- **11.a** The system determines that the job title already exists in the database.
    1. The system displays an error message and will not proceed.

**Notes**

- Selection of cadres and job classifications is optional. For each job, the user may select a cadre, a job classification, both or neither. *(1/25/2007)*
- Updated the use case to include required job competencies. *(2/11/2009)*
- This functionality can be accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `job` (iHRIS_Job) in ihris-common, `job` (iHRIS_ManageJob) in ihris-manage

### UC-PT21 Add or update a salary source

The HR Manager creates a new salary source for designating sources of salaries or special payments.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The salary source is saved and salaries and special payments can be linked to it.

**Main success scenario**

1. The user selects the option to manage the list of salary sources.
2. The system displays all salary sources entered in the system.
3. The user adds a new salary source.
4. The user enters the name of the salary source
5. The user saves the record (UC-ICE2).
6. The system makes the salary source available for selection when adding salary information.

**Extensions**

- **3.a** The user selects an existing salary source.
    1. The system opens the salary source for editing.
- **5.a** The system determines that the salary source already exists in the database.
    1. The system displays an error and will not proceed.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `salary_source` (I2CE_SimpleList) in ihris-manage

### UC-PT22 Add or update a position type

The HR Manager creates a new position type for categorizing positions.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The position type is saved and positions can be assigned to it.

**Main success scenario**

1. The user selects the option to manage the list of position types.
2. The system displays all position types entered in the system.
3. The user adds a new position type.
4. The user enters the name of the position type.
5. The user saves the record (UC-ICE2).
6. The system makes the position type available for selection when adding positions.

**Extensions**

- **1.a** The user selects an existing position type.
    1. The system opens the position type for editing.
- **5.a** The system determines that the position type already exists in the database.
    1. The system displays an error and will not proceed.

**Notes**

- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position_type` (I2CE_SimpleList) in ihris-manage

### UC-PT23 Create a position

HR Staff creates a position within the organization to be filled by a hire, promotion or transfer; this may be either a new position or re-enabling a previously discontinued position.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Updated |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system. The generic job for the position has been created. The office/facility where the position is located has been defined in the system. The department, position type and salary source have been defined in the system, if used. The currency for the proposed salary has been defined in the system, if used.

**Success guarantee.** The position has been created and marked open. The position is visible in the position hierarchy as well as available for filling by an employee or applicant.

**Main success scenario**

1. The user selects the option to manage positions.
2. The system displays all positions entered in the system by status.
3. The user creates a new position.
4. The user selects the job for the position.
5. The system displays the job title as the position title.
6. The user edits the job title as a specific position title, if different.
7. The user enters a supplemental position description (optional).
8. The user selects the currency for the salary.
9. The user enters the proposed salary (optional).
10. The user selects the salary sources (optional).
11. Repeat for each salary source for the position.
12. The user enters a code for the position.
13. The system displays today's date for the position post date.
14. The user changes the post date, if necessary.
15. The user enters any comments or notes about the position (optional).
16. The user enters any comments or notes about interviews for the position (optional).
17. The user selects the office/facility where the position is located.
18. The user selects the supervisor's position.
19. The user selects a department (optional).
20. The user selects the position type (optional).
21. The user enters the proposed hiring date (optional).
22. The user enters the proposed ending date (optional).
23. The user saves the record (UC-ICE2).
24. The system saves the position as an open position and makes it available for job applications or filling by an employee.

**Extensions**

- **3.a** The user selects the position from a list of discontinued positions.
    1. The user changes the position status to open.
    2. The user selects the position to edit it.
- **3.b** The user selects an existing position.
    1. The system displays all the position information for editing.

**Notes**

- A facility is always tied to a position. That is how the position's geographical location is determined. *(1/25/2007)*
- For right now, only one position can be entered at a time. *(2/7/2008)*
- Added the post date, comments and interview comments, implemented in version 3.0. *(2/7/2008)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

### UC-PT24 Update a position

HR Staff changes any information pertaining to a position.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** All updates are made and displayed with the position's information.

**Main success scenario**

1. The user selects the facility where the position is located or selects the position status: open, closed or discontinued.
2. The system displays all positions in that facility or with that status.
3. The user selects the position to update.
4. The system displays the position information.
5. The user makes updates to the position's information.
6. The user saves the record (UC-ICE2).
7. The system saves and displays the new position information.

**Extensions**

- **2.a** The position is not found.
    1. The system provides the option to add a new position.

**Notes**

- Added the ability to locate positions by either status or facility in version 4.0. *(6/29/2009)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

### UC-PT25 Discontinue a position

When a position is no longer needed and no employee is filling it, HR Staff removes it from the position hierarchy.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The employee has vacated the position, and the position is marked as open. The user must be logged in to the system.

**Success guarantee.** The position is no longer displayed in the position hierarchy or available for selection by may be re-enabled.

**Main success scenario**

1. The user selects the option to display all open positions.
2. The system displays all open positions.
3. The user selects a position.
4. The user marks the position as discontinued.
5. The system removes the position from selection or reporting in the system.

**Extensions**

- **2.a** The system finds no open positions.
    1. The use case stops.

**Notes**

- Closed positions cannot be discontinued because they are still filled by an employee. The employee must be removed from the position before the position can be discontinued. *(2/11/2008)*
- This functionality is accessed via an open position record from the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

## 1.3 Employee Management

Add a new employee or applicant record to the system, and search for and update records that have been entered into the system.

- Access these functions via the Manage People link on the main menu. *(9/28/2007)*

### UC-PT27 Enter a new record

HR Staff creates a record for a new employee or applicant and enters all the pertinent information about that person.

| | |
|---|---|
| Priority | P1 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system. The personal title, nationality, country and district of residence have been entered in the system.

**Success guarantee.** All of the information is saved to the database and displayed with the person's record.

**Main success scenario**

1. The user selects the option to add a new record.
2. The user selects the title for the person (optional).
3. The user adds the person's name:
    - surname
    - first name
    - other names (optional)
    - suffix
4. The user selects a nationality/citizenship.
5. The user selects a country where the person resides.
6. The system displays a list of matching districts for that selection.
7. The user selects the district where the person resides.
8. The system displays a list of matching counties/sectors for that district.
9. The user selects the county/sector where the person resides.
10. The user saves the record (UC-ICE2).
11. The system displays the personal information in the record.
12. The system provides the option to update the name or other personal information.

**Extensions**

- **3.a** The system determines that the surname and first name combination match a record that is already in the database.
    1. The system prompts the user to compare the two records and determine whether they are the same.
    2. The user either selects the matching record and edits it, or tells the system to ignore the error and continues editing the new record, if it is different.
- **12.a** The user changes the name.
    1. The system saves the former name to the person's name history.
    2. The system provides the option to view the name history.

**Notes**

- Updated use case by adding a personal title (as distinguished from a job title) such as Mr., Mrs. or Dr.; this was a feature request from Uganda. *(2/28/2008)*
- Updated use case by adding a suffix field for names (for Jr., III, etc.) *(7/24/2008)*
- This functionality is accessible via the Manage People --> Add Person screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT28 Set a position for an employee

HR Staff sets a position for an employee of the organization.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system. The position has been created in the system. The employee record has been created. The employee is not currently assigned a position. The currency for the salary has been defined in the system.

**Success guarantee.** The employee is associated with a position and that position is marked as closed.

**Main success scenario**

1. The user selects the option to set a position in an employee's record.
2. The user selects the position for the employee from the list of open positions.
3. The user enters the actual start date.
4. The user selects the currency for the salary.
5. The user enters the actual salary.
6. The user saves the record (UC-ICE2).
7. The system links the position to the employee.
8. The system marks the position as closed.
9. The system displays the position in the employee's record.
10. The system provides the option to correct the position information, change the position, record a departure or view the position history.

**Notes**

- If the job application module is disabled, this is the only way to set a position for a new or existing employee. *(11/3/2008)*
- This functionality is accessible via a person's record if the person does not already have a position set. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

### UC-PT29 Add identification information

HR Staff enters identifications into a person's record.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The identification types have been added to the system. The person has a record in the system. The user must be logged in to the system.

**Success guarantee.** All of the information is saved to the database and displayed with the person's record.

**Main success scenario**

1. The user selects the option to add an identification to a person's record.
2. The user selects a type of identification.
3. The user enters the identification number.
4. The user saves the record (UC-ICE2).
5. The system displays the new identification information in the person's record.
6. The system provides the option to update the identification information.
7. The user repeats Steps 1-4 for each identification.

**Notes**

- Identification checking will have to be implemented at time of customization because requirements change so much depending on where the system is located. *(10/31/2007)*
- This use case is the same in both iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- Identifications need to be hidden or obscured when a record is viewed by anyone other than HR Staff or an HR Manager. *(2/7/2008)*
- This functionality can be accessed via the Individual Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT30 Add demographic information

HR Staff adds demographic information about a person to his or her record.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has a record in the system. The user must be logged in to the system. The marital status has been entered into the system for selection.

**Success guarantee.** The demographic information is saved and is displayed with the person's record.

**Main success scenario**

1. The user selects the option to add demographic information to a person's record.
2. The user selects the date of birth.
3. The user selects the gender.
4. The user selects the marital status.
5. The user enters the number of dependents.
6. The user saves the record (UC-ICE2).
7. The system displays the demographic information in the record.
8. The system provides the option to update the demographic information.

**Notes**

- This use case is essentially the same for iHRIS Manage and iHRIS Qualify, although Qualify also captures the place of birth. *(10/31/2007)*
- This functionality can be accessed via the Individual Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `demographic` (iHRIS_Demographic) in ihris-common, `demographic` (iHRIS_ManageDemographic) in ihris-manage

### UC-PT31 Add contact information

HR Staff adds or updates any type of contact information for a person or institution.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | Subfunction |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The record exists in the system. The user must be logged in to the system.

**Success guarantee.** The contact information is saved and displayed with the appropriate record.

**Main success scenario**

1. The user selects the type of contact to add to a record.
2. The user enters the full mailing address.
3. The user enters the telephone number.
4. The user enters the alternate telephone number.
5. The user enters the fax number.
6. The user enters the email address.
7. The user enters notes about the contact.
8. The user saves the record (UC-ICE2).
9. The system displays the contact information in the record.
10. The system provides the option to update the contact information.
11. The user repeats Steps 1-10 for each contact.

**Extensions**

- **1.a** The system determines that a contact of that type already exists for the record.
    1. The system disables the option to add another contact of that type.

**Notes**

- This use case is the same for iHRIS Manage and iHRIS Qualify, although the specific types of contacts for each are slightly different. *(10/31/2007)*
- All fields are optional. *(10/31/2007)*
- This subfunction is referenced wherever contact information additions or updates are required. *(10/31/2007)*
- Institutions only have one contact type (as opposed to people records). The contact type does not need to be selected, as the contact information can be entered with the institution's other details. *(2/11/2008)*
- This functionality is accessed via the Contact section of a person or organization record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `contact` (iHRIS_Contact) in ihris-common

### UC-PT32 Record a special payment

HR Staff records a payment for an employee that is paid in addition to the salary.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The employee has a record in the system. The user must be logged in to the system. The special payment type and source have been entered into the system. The currency has been entered in the system.

**Success guarantee.** The special payment is saved with the employee's record.

**Main success scenario**

1. The user selects the type of special payment (such as bonus, benefit or allowance) to add to the employee's record.
2. The user selects the currency for the payment.
3. The user enters the amount of the payment.
4. The user selects the source of the special payment.
5. The user selects whether the payment is recurring or one-time.
6. The user saves the record (UC-ICE2).
7. The system displays the special payment in the person's record.
8. The system provides the option to update the benefit details.
9. The user repeats Steps 1-8 for each special payment the employee receives.

**Extensions**

- **5.a** The user indicates that the payment is recurring.
    1. The user selects the frequency of the recurrence.
    2. The user selects the start and end dates of the recurrence period.
- **5.b** The user indicates that the payment is one-time.
    1. The user enters the date the payment is distributed for the start date.

**Referenced requirements:** REQ-PT11 (Business Rule); REQ-PT9 (Non-functional)

**Notes**

- This functionality is accessed via the Position Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT33 Terminate an employee

HR staff records the departure of an employee from the organization.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The employee has a record in the system. The user must be logged in to the system. The reason for departure must be entered into the system.

**Success guarantee.** The old position is reopened or discontinued, the reason for the departure is recorded, and the employee is converted to old employee status.

**Main success scenario**

1. The user selects the option to record a departure in the employee's record.
2. The system displays today's date for the end date.
3. The user changes the end date, if it is different.
4. The user selects the reason for the departure.
5. The user selects whether the employee's former position is open or discontinued.
6. The system changes the status of the former position and displays it either in the open positions list or the list of discontinued positions.
7. The user saves the record (UC-ICE2).
8. The system removes the option to change the position from the employee's record.
9. The system saves the employee's last held position to the employee's position history.
10. The system enters the end date for the position as the end date of the salary and saves this to the employee's salary history.
11. The system removes the option to change the salary.
12. The system converts the employee to an "old employee" and removes the employee from any active staff lists.

**Notes**

- This functionality is accessed via the Position Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT34 Record a position change

HR Staff notes that an employee has been transferred or promoted to a new position and either reopens the position that the employee held or discontinues it.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The employee has a record in the system. The user must be logged in to the system. The reason for departure must be entered into the system. The currency for the new position must be entered in the system. The new position must be added as an open position.

**Success guarantee.** The old position is reopened or discontinued, the reason for the position change is recorded, and the new position is displayed in the employee's record.

**Main success scenario**

1. The user selects the option to record a position change in an employee's record.
2. The user selects the new position for an employee.
3. The system displays today's date for the start date.
4. The user changes the start date, if necessary.
5. The system sets the start date as the end date of the old position.
6. The user enters the salary for the new position.
7. The system saves the employee's old salary to the salary history.
8. The user selects the reason for the position change.
9. The user selects whether the employee's former position is open or discontinued.
10. The system changes the status of the former position and displays it either in the open positions list or the list of discontinued positions.
11. The user saves the record (UC-ICE2).
12. The system displays the new position in the employee's record.
13. The system provides the option to correct the position information.
14. The system saves the employee's last held position to the employee's position history and provides the option to view the position history.

**Notes**

- This functionality is accessed via the Position Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

### UC-PT35 Record a salary change

HR Staff records a change in salary for an employee and updates the employee's salary history.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Manager, HR Staff |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The employee has a record in the system. The user must be logged in to the system. The currency must be entered in the system.

**Success guarantee.** The new salary is saved with the employee's record.

**Main success scenario**

1. The user selects the option to update the salary in an employee's record.
2. The user enters the new salary.
3. The user selects a currency for the salary, if it has changed.
4. The system displays today's date for the effective date for the salary change.
5. The user changes the effective date, if it is different.
6. The user saves the record (UC-ICE2).
7. The system displays the new salary in the employee's record.
8. The system provides the option to correct the salary.
9. The system adds the previous salary to the employee's salary history with the salary starting and ending date and provides the option to view the salary history.

**Referenced requirements:** REQ-PT11 (Business Rule)

**Notes**

- This use case will typically be used when the employee has received a raise; if there is a position change, the salary change is recorded as part of that change. *(9/29/2006)*
- This functionality is accessed via the Position Information section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `salary` (iHRIS_Salary) in ihris-manage

### UC-PT71 Add registrations

HR Staff adds licenses or registrations to a person's record.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | Subfunction |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 4.0 |

**Preconditions.** The registration council must be added to the database. The person's record must have been created in the system. The user must be logged in to the system.

**Success guarantee.** The registration information is recorded correctly in the person's record.

**Main success scenario**

1. The user selects the option to add a registration to an employee's record.
2. The user selects the name of the registration council that issued the license or registration.
3. The user enters the registration number or license number.
4. The user enters the registration date or license expiration date.
5. The user saves the record (UC-ICE2).
6. The system displays the registration or license information in the person's record.
7. The system provides the option to update the registration.

**Notes**

- This functionality can be accessed via the Qualifications section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `registration` (iHRIS_Registration) in ihris-common

### UC-PT36 Add language proficiencies

HR Staff adds language skills to a person's record.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | Subfunction |
| Complexity | Low |
| Status | Updated |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The language must be added to the database. The person's record must have been created in the system. The user must be logged in to the system.

**Success guarantee.** The language proficiency is recorded correctly in the person's record.

**Main success scenario**

1. The user selects the option to add a language to an employee's record.
2. The user selects the name of the language.
3. The user selects the speaking proficiency.
4. The user selects the reading proficiency.
5. The user selects the writing proficiency.
6. The user saves the record (UC-ICE2).
7. The system displays the language information in the person's record.
8. The system provides the option to update the language proficiency.
9. The user repeats Steps 1-8 for each language skill.

**Notes**

- This functionality can be accessed via the Qualifications section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `language_proficiency` (I2CE_SimpleList) in ihris-common

### UC-PT43 Enter employment history

Enter a history of past employers of a person into the system.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user has a record in the system. The currency of former salaries has been defined in the system. The user must be logged in to the system.

**Success guarantee.** The past employment history is saved and displayed with the person's record.

**Main success scenario**

1. The user selects the option to add employment history to a record.
2. The user enters the company name.
3. The user enters the company address.
4. The user enters the company telephone number.
5. The user selects the date started work.
6. The user enters the starting wage and currency.
7. The user enters the starting position.
8. The user selects the date ended work.
9. The user enters the ending wage and currency.
10. The user enters the ending position.
11. The user enters the name of the supervisor.
12. The user selects yes or no as to whether the past employer can be contacted.
13. The user enters the job responsibilities.
14. The user enters the reason for leaving.
15. The user saves the record (UC-ICE2).
16. The system displays the employment history item in the person's record.
17. The system provides the option to update the item.
18. The user repeats Steps 1-17 for each past employer.

**Notes**

- This use case is intended as part of the job application process but can be used, for example, by employees to add an employment history, if needed. *(9/28/2006)*
- This form appears even if the applicant module is disabled. Moved to the Employee Management module. *(11/3/2008)*
- This functionality is accessed via the Employment History section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `employment` (iHRIS_Employment) in ihris-common

### UC-PT44 Enter educational history

HR Staff enters educational history into the system.

| | |
|---|---|
| Priority | P6 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user has a record in the system. At least one educational institution type and associated degree has been entered in the system. The user must be logged in to the system.

**Success guarantee.** The educational history is saved and is displayed with the person's record.

**Main success scenario**

1. The user selects the option to add educational history to a person's record.
2. The user enters the name of the educational institution.
3. The user enters the location of the educational institution.
4. The user enters the year of graduation.
5. The user selects the type of educational institution.
6. The system displays the degrees offered by that type of educational institution.
7. The user selects the degree for that type of educational institution.
8. The user enters the major.
9. The user saves the record (UC-ICE2).
10. The system displays the new item in the person's record.
11. The system provides the option to update the item.
12. The user repeats Steps 1-11 for each educational institution attended.

**Notes**

- The educational history is intended to be part of the job application process but can be entered for any employee at any time. *(2/7/2008)*
- This form appears even if the applicant module is disabled. Moved to the Employee Management module. *(11/3/2008)*
- This functionality is accessed via the Educational History section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT37 Record notes

HR Staff records notes about a particular person and saves them with the person's record.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The person has a record in the system. The user must be logged in to the system.

**Success guarantee.** The notes are entered and saved with the person's record.

**Main success scenario**

1. The user enters any notes about the person in the person's record.
2. The system enters today's date for the note's date.
3. The user changes the date of the note, if necessary.
4. The user saves the record (UC-ICE2).
5. The system maintains and displays a log of all notes that were entered in reverse chronological order.
6. The system provides the option to update each note.

**Notes**

- The notes are an open field that can be used for any purpose. *(10/31/2007)*
- This use case is the same for iHRIS Manage and Qualify. *(10/31/2007)*
- This functionality is accessed via the Notes section of a record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `notes` (iHRIS_Notes) in ihris-common

## 1.4 Job Applicant Management

The module is for managing job applications for open positions, reviewing completed job applications, recording interview notes and assigning a position to the successful applicant.

- This module may be disabled if not used by the organization on the Configure Modules page for iHRIS Manage. *(1/25/2007)*
- Access these functions via the Manage People link on the main menu. *(9/28/2007)*

### UC-PT40 Apply for a position

An HR staff person completes a job application form and records information about a job applicant in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 2.0 |

**Preconditions.** The position has been created and is listed as an open position. The application module is enabled.

**Success guarantee.** The application is successfully completed and submitted; the form data is recorded in the system and is available for review.

**Main success scenario**

1. The user logs in (UC-ICE5).
2. The system checks the user's role.
3. The system displays the new record form.
4. The user enters a new record (UC-PT27).
5. The user selects the option to add an application.
6. The system displays the job application form.
7. The user selects the open position to apply for.
8. The user completes the applicant questions.
9. The user adds language proficiencies (UC-PT36), if applicable.
10. The user adds skills (UC-PT50), if applicable.
11. The user uploads a resume.
12. The user saves the record (UC-ICE2).
13. The system displays the application in the person's record and makes it available for review with the open position.
14. The system provides the option to update the application.
15. The user creates a username and password.
16. The system adds the user account with Applicant access to the application.

**Extensions**

- **2.a** The system detects that an Employee has logged in.
    1. The system displays the Employee's record.
    2. The system provides the option for the Employee to apply for an open position using the job application form.
- **2.b** The system detects that an HR Staff person has logged in.
    1. The system provides the option to add an applicant (as for enter a new record (UC-PT27)) or to add an application to an existing record.
- **15.a** The user has logged in with a non-guest username and password.
    1. Skip this step.

**Referenced requirements:** REQ-PT10 (Business Rule)

**Notes**

- This use case should be optional. If this information is not entered at this point, it can be entered when creating a new employee record. *(9/25/2006)*
- In version 2.0, HR Staff can enter a job application for any record. *(2/7/2008)*
- Use case was updated to include uploading a resume. *(7/10/2009)*
- This functionality is accessible through the Application section of a person's record. In the current version, applicants/employees cannot fill out an application themselves. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `position` (iHRIS_MultiPosition) in ihris-manage

### UC-PT41 Log interview details

HR Staff can enter details about an interview with a job applicant.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The application module is enabled. An application has been completed for the position. The user must be logged into the system. .

**Success guarantee.** The interview details are saved with the job application.

**Main success scenario**

1. The user selects the option to log interview details in an applicant's record.
2. The system enters today's date for the interview date.
3. The user changes the date of the interview, if necessary.
4. The user enters the names of people conducting the interview.
5. The user enters any comments about the interview.
6. The user saves the record (UC-ICE2).
7. The system displays the interview details in the person's record.
8. The system provides the option to update the interview details.
9. The user repeats Steps 1-8 for each additional interview.

**Notes**

- This use case was separated from the Review Applicants (UC-PT45) use case for clarity. *(2/7/2008)*
- This functionality is accessed via the Application section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT42 Log a hiring decision

HR Staff logs a decision whether or not to hire an applicant for a position for which the applicant has applied.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The application module is enabled. An application has been completed for the position. The user must be logged into the system.

**Success guarantee.** The hiring decision details are saved with the job application.

**Main success scenario**

1. The user selects the option to log a hiring decision in the applicant's record.
2. The user selects the decision whether to hire the applicant for the job.
3. The system enters today's date for the date of the decision.
4. The user changes the date of the decision, if applicable.
5. The user records any comments.
6. The user saves the record (UC-ICE2).
7. The system displays the hiring decision in the person's record.
8. The system provides the option to update the hiring decision.

**Notes**

- This use case was separated from the Review Applicants (UC-PT45) use case for clarity. *(2/7/2008)*
- Note that logging a hiring decision will not set the position for the applicant; that needs to be done in the "Make a job offer" step. *(2/7/2008)*
- This functionality is accessed via the Application section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT45 Review applicants

The Manager lists the names of Applicants for a particular position and reviews the applications.

| | |
|---|---|
| Priority | P6 |
| Primary actors | Executive Manager, HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The application module is enabled. An applicant has completed an application form for the position. The user must be logged in to the system.

**Success guarantee.** The applicant information for all people who applied for a position can be displayed.

**Main success scenario**

1. The user displays the list of open positions.
2. The user selects the position to review.
3. The system lists all applicants who applied for the position, including the date they completed the application form.
4. The user selects an applicant's name.
5. The system checks the user's role.
6. The system displays the applicant's record with the completed application form and provides the option to update the information if the role is allowed to update.

**Notes**

- Only HR Staff can update an application. *(2/7/2008)*
- This functionality is accessible via the Manage People --> Review Applicants screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `application` (iHRIS_Applicant) in ihris-manage

### UC-PT46 Make a job offer

HR Staff moves a job applicant into an open position, fills out any information required for hiring the person and enters work contact information.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Staff |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The application module is enabled. The applicant has applied for a position. The user must be logged in to the system. The currency must be defined in the system for the position salary.

**Success guarantee.** The applicant is linked with the position and entered as an employee in the system, if not already an employee; the position is closed.

**Main success scenario**

1. The user displays the list of open positions.
2. The user selects the position to fill.
3. The system displays the position information and all applicants who applied for the position.
4. The user selects the applicant who will fill the position.
5. The system determines whether the applicant already has an employee record in the system.
6. The system displays today's date for the start date.
7. The user changes the start date, if necessary.
8. The user selects the currency for the salary.
9. The user enters the starting salary for the position.
10. The user saves the record (UC-ICE2).
11. The system saves the employee record and associates it with the new position.
12. The system removes the person from the list of applicants.
13. The system marks the position as closed as of the start date.

**Extensions**

- **5.a** The system determines that an employee record exists for the applicant and the employee is assigned to another position.
    1. The system prompts the user to select a status for the employee's former position: open or discontinued.
    2. The system prompts the user to select a reason for the position change.
    3. The system changes the status of the employee's former position as of the change date and makes it available in the open position list or list of discontinued positions.
    4. The system adds the employee's former position to the position history with the change date as the end date for that position.
- **9.a** The system determines that the applicant already held a position with a salary.
    1. The system changes the salary to the new position's salary and adds the former salary to the employee's salary history.

**Notes**

- This use case turns an applicant into an employee and associates a position with the new employee; it can also be used to change the position for an existing employee. *(9/25/2006)*
- Assumes that the offer has been made to the applicant and the applicant has accepted the offer (trigger). *(11/28/2006)*
- This functionality is accessed via the Manage People --> Review Applicants screens; an open position must be selected. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `job` (iHRIS_Job) in ihris-common, `job` (iHRIS_ManageJob) in ihris-manage

## 1.5 Competency Model

Defines successful job performance in the organization and enables the organization to assess employee's competencies in various skills.

- This module is currently in development. Core functions have been released. *(10/16/2007)*
- Also modified UC-PT20 (Create a job) to link a job to its required competencies. *(10/16/2007)*
- The blueprint for the Competency Model module was written and posted to the wiki. *(10/18/2007)*

Related documents: http://open.intrahealth.org/wiki/index.php/Competency\_Model

### UC-PT49 Create a competency model

The Training Manager updates a list of competency categories or competencies.

| | |
|---|---|
| Priority | P5 |
| Primary actors | HR Manager, Training Manager |
| Level | User |
| Complexity | Medium |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new competency is saved and linked to any selected parent category, and it is available for selection in various use cases.

**Main success scenario**

1. The user selects the option to update the competency model.
2. The system displays a list of competencies organized by category.
3. The user adds a new competency.
4. The user selects whether the item is a parent category.
5. The user enters the name of the item.
6. The user enters a definition for the competency.
7. The user saves the record (UC-ICE2).
8. The system makes the competency available for selection when adding competencies to a record.

**Extensions**

- **3.a** The user selects an existing competency.
    1. The system opens the competency for editing.
- **3.b** The user selects an existing parent category.
    1. The system provides the option to add competencies underneath the parent category.
- **4.a** The user designates the competency as a parent category.
    1. The system enables competencies to be added beneath the parent category.
- **7.a** A system determines that the competency with the same parent categories already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case was updated for the Competency Model module: it was expanded to add additional parent categories and to combine the competency type and competency addition into one step. Also, the primary actor was changed, and the use case was moved into a separate module that can be disabled in the system. *(10/16/2007)*
- The system currently supports adding a competency type and several competencies under each type, which can be recorded in the qualifications section of a record; implemented in version 2.0. *(2/7/2008)*
- This functionality can be accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `competency` (iHRIS_Competency) in ihris-common

### UC-PT68 Add or update a competency evaluation

The Training Manager updates the competency evaluations for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new competency evaluation is saved and available for selection when evaluating a course completed by an employee.

**Main success scenario**

1. The user selects the option to manage the list of competency evaluations.
2. The system displays all evaluations entered in the system.
3. The user adds a new competency evaluation.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the competency evaluations available for selection when evaluating employees who have completed training courses.

**Extensions**

- **3.a** The user selects an existing competency evaluation.
    1. The system opens the item for editing.

**Notes**

- This is a new use case to create dropdown menus of competency evaluations as part of the Competency Model module. *(10/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `competency_evaluation` (I2CE_SimpleList) in ihris-common

### UC-PT50 Assess an employee's competencies

The Training Manager adds to or updates the list of competencies obtained by an employee.

| | |
|---|---|
| Priority | P5 |
| Primary actors | HR Staff, Training Manager |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 3.1 |

**Preconditions.** The person has a record in the system. The user must be logged in to the system. The competency and competency evaluation must be added to the system.

**Success guarantee.** The employee's competencies are saved and displayed with their record, the evaluation history for each competency is updated, and the competencies are available for searching.

**Main success scenario**

1. The user selects the option to add competencies to a person's record.
2. The system displays the competency model.
3. The user selects the competency to add.
4. The user selects the competency evaluation (optional).
5. The user selects the date of the evaluation.
6. The user enters a date when the assessment expires or should be re-evaluated (optional).
7. The system sets a flag to appear on the person's record when the date has passed that reminds the user that the person needs reassessment.
8. The user saves the record (UC-ICE2).
9. The system saves the competency information and displays it in the record.
10. The system provides the option to update the competency or view the evaluation history for any competency.

**Extensions**

- **3.a** The system detects that the competency is a parent category.
    1. The user checks the category to add all subcategories and competencies within that category to the record.
    2. The user expands the category to select subcategories or competencies within the category for addition to the record.
- **5.a** The user does not select an evaluation date.
    1. The system enters today's date by default.

**Notes**

- This use case was previously limited to adding a compentency to an employee's record, implemented in version 2.0. *(10/18/2007)*
- Updated this use case to expand the competency model and assessment procedures as part of the Competency Model module. *(2/7/2008)*
- This functionality can be accessed via the Qualifications section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `competency` (iHRIS_Competency) in ihris-common

## 1.6 Training Management

This module is to manage a training program offered to employees for trainings offered by the employer or external organizations. It tracks trainings that an employee has completed and assesses employee competencies achieved as a result. It also enables the organization to maintain lists of trainers and training funders.

- This module may be disabled if not used by the organization on the Configure Modules page for iHRIS Manage. *(1/25/2007)*
- The blueprint for the Training Management module was written and posted to the wiki. *(10/18/2007)*
- This module was developed and released in version 3.1. *(9/29/2008)*

Related documents: http://open.intrahealth.org/wiki/index.php/In-service\_Training\_Module\_for\_iHRIS\_Manage

### UC-PT53 Add or update a training funder

The Training Manager adds details about a training funder to the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The training funder is added to the system and is made available for selection in various use cases.

**Main success scenario**

1. The user selects the option to manage the list of training funders.
2. The system displays all funders that have been entered in the system.
3. The user adds a training funder.
4. The user enters the name of the funder.
5. The user adds contact information (UC-PT31).
6. The user saves the record (UC-ICE2).
7. The system makes the training funder available for selection when adding training programs.

**Extensions**

- **3.a** The user selects an existing funder.
    1. The system displays the funder's record and provides the option to edit any of the information.

**Notes**

- This is a new use case to create funders of training programs as part of the Training Management module. *(10/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_funder` (iHRIS_ListByCountry) in ihris-common

### UC-PT54 Add or update a training organization

The Training Manager adds details about a training organization to the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The training organization is added to the system and is made available when adding training programs.

**Main success scenario**

1. The user selects the option to manage the list of training organizations.
2. The system displays all organizations that have been entered in the system.
3. The user adds a training organization.
4. The user enters the name of the organization.
5. The user adds contact information (UC-PT31).
6. The user saves the record (UC-ICE2).
7. The system makes the training organization available for selection when adding training programs.

**Extensions**

- **3.a** The user selects an existing organization.
    1. The system displays the organization's record and provides the option to edit any of the information.

**Notes**

- This is a new use case to create organizations that provide training programs as part of the Training Management module. *(10/16/2007)*
- This use case does not track locations of training organizations, trainers or other details that properly belong in a training administration system. *(11/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT65 Add or update a training course status

The Training Manager updates the status of training courses for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The new training program status is saved and available for selection when adding a training program.

**Main success scenario**

1. The user selects the option to manage the status of training courses.
2. The system displays all training course statuses entered in the system.
3. The user adds a new training course status.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the training course status available for selection when adding training courses.

**Extensions**

- **3.a** The user selects an existing training program status.
    1. The system opens the item for editing.

**Notes**

- This is a new use case to create dropdown menus of training program statuses as part of the Training Management module. *(10/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_course_status` (I2CE_SimpleList) in ihris-common

### UC-PT66 Add or update a training course requestor

The Training Manager updates the list of requestors of training courses for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The new training program requestor is saved and available for selection when scheduling a training course for an employee.

**Main success scenario**

1. The user selects the option to manage the requestors of training courses.
2. The system displays all training course requestors entered in the system.
3. The user adds a new training course requestor.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the training course requestor available for selection when scheduling training courses for an employee.

**Extensions**

- **3.a** The user selects an existing training program requestor.
    1. The system opens the item for editing.

**Notes**

- This is a new use case to create dropdown menus of training program requestors as part of the Training Management module. *(10/16/2007)*
- A requestor is any person or organization who requests that an employee complete a training course (such as Employee, Supervisor, Human Resources, Donor, etc.). *(7/30/2008)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_course_requestor` (I2CE_SimpleList) in ihris-common

### UC-PT67 Add or update a training course evaluation

The Training Manager updates the list of training course evaluations, or the grade or assessment an employee earned after taking a training course, for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The new training program evaluation is saved and available for selection when scheduling a training course for an employee.

**Main success scenario**

1. The user selects the option to manage the evaluations of training courses.
2. The system displays all training course evaluations entered in the system.
3. The user adds a new training course evaluation.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the training course evaluation available for selection when scheduling training courses for an employee.

**Extensions**

- **3.a** The user selects an existing training program evaluation.
    1. The system opens the item for editing.

**Notes**

- This is a new use case to create dropdown menus of training program evaluation as part of the Training Management module. *(10/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_course_evaluation` (iHRIS_Training_Course_Evaluation) in ihris-common

### UC-PT55 Add or update a training course category

The Training Manager updates the list of training course categories for selection within the system.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The new training program category is saved and available for selection when adding a training program.

**Main success scenario**

1. The user selects the option to manage the list of training course categories.
2. The system displays all training course categories entered in the system.
3. The user adds a new training course category.
4. The user enters the description or name of the item.
5. The user saves the record (UC-ICE2).
6. The system makes the training course category available for selection when adding training course.

**Extensions**

- **3.a** The user selects an existing training program category.
    1. The system opens the item for editing.

**Notes**

- This is a new use case to create dropdown menus of training program categories as part of the Training Management module. *(10/16/2007)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_course_category` (I2CE_SimpleList) in ihris-common

### UC-PT69 Add or update a continuing education course

The HR manager enters valid continuing education courses for selection when renewing a license.

| | |
|---|---|
| Priority | P10 |
| Primary actors | HR Manager |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system.

**Success guarantee.** The new continuing education course is saved and available for selection in appropriate use cases.

**Main success scenario**

1. The user selects the option to update the list of continuing education courses.
2. The system displays all continuing education courses added to the system.
3. The user adds a new continuing education course.
4. The user enters the name of the course.
5. The user enters the number of credit hours that can be earned by completing the course.
6. The user saves the record (UC-ICE2).
7. The system makes the new course available for selection when adding training courses.

**Extensions**

- **3.a** The user selects an existing continuing education course name.
    1. The system opens the course's details and provides the option to update them.

**Notes**

- This is a new use case that is part of the training management module. *(7/30/2008)*
- This use case is identical to the same use case for iHRIS Qualify. *(7/30/2008)*
- This functionality is accessed via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `continuing_education_course` (iHRIS_ContinuingEducationCourse) in ihris-common

### UC-PT56 Add or update an in-service training program

The Training Manager adds a training offering to the system that can be requested for employees to complete.

| | |
|---|---|
| Priority | P1 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The competencies must be entered in the system. The training category, status, funder and organization must be entered in the system. The user must be logged in to the system.

**Success guarantee.** The training program is added to the system and is made available for selection.

**Main success scenario**

1. The user selects the option to manage the list of training courses.
2. The system displays all training courses entered in the system.
3. The user adds a training program.
4. The user enters the name of the training program.
5. The user selects the category of the training (optional).
6. The user enters a specific topic for the training.
7. The user selects the program status.
8. The user selects the name of the training funder (optional).
9. Repeat for each additional training funder.
10. The user selects the name of the training organization giving the training (optional).
11. The user checks all competencies associated with the training (optional).
12. The user selects any Continuing Education course credits earned in the training program (optional).
13. The user enters any notes about the training (optional).
14. The user saves the record (UC-ICE2).
15. The system displays the training course information.
16. The user enters the schedule for a training program (UC-PT57).

**Extensions**

- **3.a** The user selects an existing program.
    1. The system displays the training program record and provides the option to edit the training program information.
- **7.a** The user does not select a status.
    1. The system sets the status to open.
- **7.b** The user selects the closed status.
    1. The system removes the training from scheduling on an employee's record.
- **10.a** The user checks a parent competency category.
    1. The system selects all subcategories and competencies within that category for the training.
- **10.b** The user expands a parent competency category.
    1. The system makes any subcategory or competency within that category available for selection.

**Notes**

- This use case has been significantly revised to capture more data about training programs as part of the Training Management module. *(10/16/2007)*
- This functionality can be accessed via the Configure System --> Administer Database screens. *(7/10/2009)*
- The In-Service Training Management module must be enabled for the use case to function and is disabled by default. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT57 Enter the schedule for a training program

The Training Manager enters the specific dates, duration and location of training program classes, either when entering the training program details or scheduling an employee to take a training.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | Subfunction |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The training program has been entered in the system. The country, district and county where the training program is located must be entered in the system. The user is logged in.

**Success guarantee.** The training class details are saved with the training program and made available for later reference.

**Main success scenario**

1. The user selects the training course to schedule.
2. The user selects the option to schedule a training program.
3. The user enters the maximum number of students.
4. The user selects the date the training program begins.
5. The user selects the date the training program ends.
6. The user enters the name of the site where the training program is to be held.
7. The user enters the trainers' name(s) (optional).
8. The user selects the country where the training program takes place.
9. The system displays all districts in that country.
10. The user selects the district where the training program takes place.
11. The system displays all counties in that district.
12. The user selects the county where the training program takes place (optional).
13. The user saves the record (UC-ICE2).
14. The system saves the class details with the training program information and makes the class available for scheduling for employees.

**Extensions**

- **4.a** The date is not entered.
    1. The system selects the current date.
- **5.a** The end date is before the start date.
    1. The system displays an error and will not continue.

**Notes**

- This use case was added to allow scheduling of specific instances of a training program. *(12/3/2007)*
- This functionality is accessed from a training course's record via the Configure System --> Administer Database screens. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT59 Schedule a training for an employee

The Training Manager adds an employee to the schedule for a training class.

| | |
|---|---|
| Priority | P10 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. The user must be logged in to the system. The employee must have a record in the system. The training program must have been added to the system and at least one class must have been added for it. The requestor and evaluation must have been added to the system.

**Success guarantee.** The training program is listed as scheduled in the employee's training history.

**Main success scenario**

1. The user selects the option to schedule a training in an employee's record.
2. The system lists all training programs.
3. The user selects the training program.
4. The system displays all scheduled classes for that program.
5. The user selects the training class to schedule.
6. The system displays today's date for the date of the request.
7. The user changes the date of the request, if applicable.
8. The user selects the person who requested or recommended the training (optional).
9. The user selects whether this is a new training or a retraining for the employee.
10. The user enters any notes about the training request.
11. The user selects whether the course has been completed.
12. The user selects an evaluation for the course.
13. The user saves the record (UC-ICE2).
14. The system adds the training program to the list of the trainings in which the employee is scheduled to take to the employee's training history.

**Extensions**

- **11.a** The user doesn't select an option.
    1. The system records No by default.

**Notes**

- This is a new use case as part of the Training Management module. *(10/16/2007)*
- This functionality is accessed via the Training section of a person's record. The In-Service Training Management Module must be enabled. *(7/10/2009)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PT60 Assess training results and update competencies

After an employee has completed a training, the Training Manager assesses their performance and updates their qualifications accordingly.

| | |
|---|---|
| Priority | P1 |
| Primary actors | Training Manager |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Partially Complete |
| Release | 3.1 |

**Preconditions.** The training module is enabled. A training with associated competencies has been scheduled for the employee. The competency evaluation has been entered in the system. The user must be logged in to the system.

**Success guarantee.** The training is marked complete and the results are recorded in the Employee's training history.

**Main success scenario**

1. The user opens an employee's training history in the employee's record.
2. The user selects the course competency evaluation for the training that the employee completed from the list of scheduled trainings.
3. The system displays all competencies selected for the training, if any.
4. For each competency associated with the training, the user selects the evaluation (optional).
5. The user enters the date of the evaluation.
6. The user enters a date when the assessment expires or should be re-evaluated (optional).
7. The system sets a flag to appear on the person's record when the date has passed that reminds the user that the person needs reassessment.
8. The user enters any notes about the evaluation.
9. The user saves the record (UC-ICE2).
10. The system saves the completed training in the employee's training history as completed (rather than scheduled) and records the performance.
11. The system adds the assessed competencies to the employee's record.

**Extensions**

- **5.a** No date is entered.
    1. The system records today's date by default.

**Notes**

- This is a new use case as part of the Training Management module. *(10/16/2007)*
- The In-Service Training Management Module must be enabled to access this functionality. It is disabled by default. *(7/10/2009)*
- This functionality is accessed via the Training section of a person's record. *(7/10/2009)*

**iHRIS 4.3.3 forms** (derived by name matching): `competency` (iHRIS_Competency) in ihris-common

## 1.7 Requirements

Requirements for iHRIS Manage.

### REQ-PT9 Localization

The system must support different international currencies.

| | |
|---|---|
| Priority | P10 |

Referenced by: UC-PT19, UC-PT32

### REQ-PT10 Job applicant questions

Specifies all questions that the organization requires be asked of a job applicant, such as to satisfy a law or the organization's need.

Example job applicant questions: If you are not a citizen, are you authorized to work in the country? Have you ever been convicted of a felony? If yes, describe the circumstances. How did you hear of this opening? When can you start work? What is your desired wage? Are you looking for full-time employment? What hours are you available?

| | |
|---|---|
| Priority | P6 |

Referenced by: UC-PT40

### REQ-PT11 Privacy

Some data cannot be viewed except by specified roles in HR and management. These may change depending on laws and organizational policies, but will probably always include salary and identification numbers.

| | |
|---|---|
| Priority | P1 |

Referenced by: UC-PT29, UC-PT35, UC-PT32

## Cited but not described

The report cites these, but describes none of them:

- A-PT9 *Any User* (cited by table of contents)
