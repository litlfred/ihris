---
title: "iHRIS Qualify use cases (2009)"
source: uploads/ihris-use-cases/iHRISQualifyUseCases.doc
licence: owner permission, 2026-09-23 (see ihris-use-cases.json)
---

# iHRIS Qualify: use cases (2009)

*Serlio Software Case Complete, 3/25/2009 4:18 PM. From the iHRIS use-case model by IntraHealth International / the Capacity Project iHRIS team, published here with the owner's permission. Parsed by `src/tools/ingest_use_cases.py`; do not edit by hand.*

iHRIS Qualify is a health worker training, licensing and certification tracking system.

- This documentation refers to the core version of the Training, Certification and Licensure database (working title: PowerSupply) *(8/2/2006)*
- This documentation was based on specifications gathered for Uganda UNMC release and also serves as documentation for that release. (UNMC release version 1.0) *(7/13/2006)*
- Version 3.0 of iHRIS Qualify was released on March 18, 2007. *(7/24/2008)*
- Core version 1.0 released August 8, 2008. *(9/29/2008)*

Related documents: https://launchpad.net/ihris-qualify, http://www.capacityproject.org/hris/suite/ihris\_qualify.php

## Actors

### A-PS1 Data Operations Manager

Role: [Data Operations Manager](roles.md#ihris-a-ps1) (`ihris-a-ps1`)

This person is responsible for managing data entry and data entry roles, including verifying and correcting data and updating standard lists in the system.

**Goals**

- Create or update standard lists of data within the system.
- Check for, correct and report on data entry errors.

**Notes**

- Can perform any use case that a Records Officer, Examination Supervisor or Registration Supervisor can.

**Use cases:** UC-PS2 Add or update a cadre, UC-PS10 Add or update a certificate, UC-PS3 Add or update a continuing education course, UC-PS13 Add or update a country, UC-PS16 Add or update a county, UC-PS4 Add or update a disciplinary action category, UC-PS15 Add or update a district, UC-PS23 Add or update a facility agent, UC-PS25 Add or update a facility status, UC-PS24 Add or update a facility type, UC-PS17 Add or update a health facility, UC-PS12 Add or update a marital status, UC-PS26 Add or update a personal title, UC-PS21 Add or update a pre-service training program, UC-PS1 Add or update a qualification, UC-PS5 Add or update a reason for disciplinary action, UC-PS6 Add or update a reason for out migration, UC-PS8 Add or update a reason for training disruption, UC-PS14 Add or update a region, UC-PS7 Add or update a training disruption category, UC-PS19 Add or update a training institution, UC-PS51 Add or update a verification change, UC-PS9 Add or update an academic level, UC-PS11 Add or update an identification type, UC-PS20 Associate a health facility with a training institution, UC-PS18 Associate a training institution with a health facility, UC-PS22 Enter inspection information

### A-PS2 Records Officer

Role: [Records Officer](roles.md#ihris-a-ps2) (`ihris-a-ps2`)

This person is responsible for basic data entry, including initial indexing and upgrades of health professional students entering training programs, tracking out migration verifications and demographic data entry.

**Goals**

- Create a new record for a health worker or student.
- Add information to or update a record with demographic, contact, identification or academic information.
- Add training program information to a health student's record.
- Record out migration verification requests and deployments in a health worker's record.
- Add notes to a record.
- Re-enter a record to ensure data quality.

**Notes**

- Can enter examination results when they are not required and the Examination Supervisor role is not activated.

**Use cases:** UC-PS30 Add academic information, UC-PS31 Add contact information, UC-PS29 Add demographic information, UC-PS28 Add identification information, UC-PS27 Enter a new record, UC-PS35 Index a training, UC-PS36 Record a discontinuation, UC-PS37 Record a resumption, UC-PS39 Record exam details, UC-PS32 Record notes, UC-PS48 Record out migration verification, UC-PS50 Record verification, UC-PS38 Set a graduation date, UC-PS47 Update deployment information

### A-PS3 Registration Supervisor

Role: [Registration Supervisor](roles.md#ihris-a-ps3) (`ihris-a-ps3`)

This person is responsible for data entry related to licensing updates, including entering initial registration, issuing new licenses and license renewals, issuing and renewing private practice licenses, and registering and licensing foreign-trained health care professionals applying to work in the country.

**Goals**

- Issue registrations and licenses to a health worker.
- Record continuing education credits in a health worker's record.
- Record disciplinary actions in a health worker's record.
- Record deployment information in a health worker's record.

**Notes**

- Can perform any use cases that a Records Officer can.

**Use cases:** UC-PS43 Add continuing education credits, UC-PS45 Document a disciplinary action, UC-PS46 Document a reinstatement, UC-PS41 Issue a license, UC-PS44 Issue a private practice license, UC-PS40 Issue a registration, UC-PS32 Record notes, UC-PS42 Renew a license, UC-PS47 Update deployment information

### A-PS4 Examination Supervisor

Role: [Examination Supervisor](roles.md#ihris-a-ps4) (`ihris-a-ps4`)

This person is responsible for data entry related to national exams, including verifying applications to take exams and recording results. This is an optional role, used only when entering examination results is required for the system.

**Goals**

- Record information about national exam applications and results.

**Notes**

- Can perform any use case that a Records Officer can.
- The Examination Supervisor will not be a role in the core release system.

**Use cases:** UC-PS39 Record exam details

### A-PS5 Decision Maker

Role: [Decision Maker](roles.md#ihris-a-ps5) (`ihris-a-ps5`)

This person runs reports in order to view and analyze data, and make health workforce policy and planning decisions. This person does not perform any data entry tasks.

**Goals**

- Generate reports to analyze data entered in the system.

### A-PS6 Any User

Role: [Any User](roles.md#ihris-a-ice4) (`ihris-a-ice4`)

A generic user (applies to all users of the system).

**Goals**

- Search for and view a record.

## 1.1 Data Administration

Create and update standard lists of data for selection in system menus.

- Access is limited to System Administrators and Data Operations Managers. *(10/15/2007)*
- Locate these functions via the Configure System / Administer Database link on the main menu. *(10/15/2007)*

### UC-PS1 Add or update a qualification

The Data Operations Manager adds or edits the list of qualifications that are available for selection within the system.

| | |
|---|---|
| Priority | P7 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new qualification is saved and available for selection in various use cases.

**Main success scenario**

1. The user selects the option to manage the list of qualifications.
2. The system displays all qualifications entered in the system.
3. The user adds a new qualification.
4. The user enters the description of the qualification.
5. The user saves the record (UC-ICE2).
6. The system makes the qualification available for selection when adding cadres.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item and enables it to be edited.
- **5.a** The system determines that the name of the qualification matches a qualification already entered in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `qualification` (I2CE_SimpleList) in ihris-qualify

### UC-PS2 Add or update a cadre

The Data Operations Manager enters or edits a cadre for selection within the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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
5. The user enters the ISCO classification code for the cadre (optional).
6. The user selects the minimum qualification for the cadre.
7. The user saves the record (UC-ICE2).
8. The system displays the new or edited cadre in selection lists of cadres.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **6.a** The user enters a new qualification if the correct one does not appear (UC-PS1)
    1. The user returns to Step 1 to enter the cadre.
- **7.a** The system determines that the cadre name already exists in the database.
    1. The system displays an error message and will not proceed.

**iHRIS 4.3.3 forms** (derived by name matching): `cadre` (I2CE_SimpleList) in ihris-common, `cadre` (iHRIS_Cadre) in ihris-qualify

### UC-PS3 Add or update a continuing education course

The Data Operations Manager enters valid continuing education courses for selection when renewing a license.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new continuing education course is saved and available for selection in appropriate use cases.

**Main success scenario**

1. The user selects the option to update the list of continuing education courses.
2. The system displays all continuing education courses added to the system.
3. The user adds a new continuing education course.
4. The user enters the name of the course.
5. The user enters the number of credit hours that can be earned by completing the course.
6. The user saves the record (UC-ICE2).
7. The system makes the new course available for selection when adding continuing education information to a record.

**Extensions**

- **3.a** The user selects an existing continuing education course name.
    1. The system opens the course's details and provides the option to update them.

**iHRIS 4.3.3 forms** (derived by name matching): `continuing_education_course` (iHRIS_ContinuingEducationCourse) in ihris-common

### UC-PS4 Add or update a disciplinary action category

The Data Operations Manager adds a new broad category to contain reasons for disciplinary action.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The category is successfully added to the system and is available for selection in applicable use cases.

**Main success scenario**

1. The user selects the option to update disciplinary action categories.
2. The system displays all disciplinary action categories entered in the system.
3. The user adds a new category.
4. The user enters a description for the category.
5. The user saves the record (UC-ICE2).
6. The system makes the disciplinary action category available for selection when adding disciplinary actions.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the disciplinary action category already exists in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `disciplinary_action_category` (I2CE_SimpleList) in ihris-qualify

### UC-PS5 Add or update a reason for disciplinary action

The Data Operations Manager adds or edits a reason for disciplinary action for display in selection menus.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The reason is successfully added to the system and is available for selection whenever its parent category is selected.

**Main success scenario**

1. The user selects the option to update the list of disciplinary action reasons.
2. The system displays all reasons entered in the system.
3. The user adds a new reason.
4. The user selects a category for the reason.
5. The user enters a description for the reason.
6. The user saves the record (UC-ICE2).
7. The system makes the reason available for selection when adding disciplinary actions.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **4.a** The user adds a new disciplinary action category (UC-PS4).
    1. The user returns to Step 1 to add the disciplinary action reason.
- **6.a** The system determines that the disciplinary action reason is already in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `disciplinary_action` (iHRIS_DisciplinaryAction) in ihris-qualify

### UC-PS6 Add or update a reason for out migration

The Data Operations Manager adds or edits a reason for out migration to the system and makes it available for selection.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The out migration reason is saved to the system and is available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage out migration reasons.
2. The system displays all reasons entered in the system.
3. The user adds a new out migration reason.
4. The user enters a description for the out migration reason.
5. The user saves the record (UC-ICE2).
6. The system makes the reason available for selection when recording out migration verification requests.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the out migration reason already exists in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `out_migration` (iHRIS_OutMigration) in ihris-qualify

### UC-PS7 Add or update a training disruption category

The Data Operations Manager adds a new broad category to contain reasons for training disruption.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The category is successfully added to the system and is available for selection in applicable use cases.

**Main success scenario**

1. The user selects the option to manage the list of training disruption categories.
2. The system displays all categories entered in the system.
3. The user adds a new category.
4. The user enters a description for the category.
5. The user saves the record (UC-ICE2).
6. The system makes the training disruption category available for selection when adding training disruptions.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the training disruption category already exists in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `training_disruption_category` (I2CE_SimpleList) in ihris-qualify

### UC-PS8 Add or update a reason for training disruption

The Data Operations Manager adds or edits a reason for training disruption for display in selection menus.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The reason is successfully added to the system and is available for selection whenever its parent disruption category is selected.

**Main success scenario**

1. The user selects the option to update the list of reasons for training disruption.
2. The system displays all reasons entered in the system.
3. The user adds a new reason.
4. The user selects a category for the reason.
5. The user enters a description for the reason.
6. The user saves the record (UC-ICE2).
7. The system makes the reason available for selection when adding training disruptions.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **4.a** The user adds a new training disruption category (UC-PS7).
    1. The user returns to Step 1 to add the training disruption reason.
- **7.a** The system determines that the training disruption reason has already been entered in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `training_disrupt` (iHRIS_TrainingDisrupt) in ihris-qualify

### UC-PS9 Add or update an academic level

The Data Operations Manager adds or edits the list of academic levels that are available for selection within the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new academic level is saved and available for selection in various use cases.

**Main success scenario**

1. The user selects the option to manage the list of academic levels.
2. The system displays all academic levels entered in the system.
3. The user adds a new academic level.
4. The user enters the description of the academic level.
5. The user saves the record (UC-ICE2).
6. The system makes the academic level available for selection when adding academic information.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing
- **5.a** The system determines that the academic level has already been entered in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `academic_level` (I2CE_SimpleList) in ihris-qualify

### UC-PS10 Add or update a certificate

The Data Operations Manager updates the list of certificates that are available for selection within the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The certificate is added to the system and available for selection when its parent academic level is selected.

**Main success scenario**

1. The user selects the option to manage the list of certificates held.
2. The system displays all certificates entered in the system.
3. The user adds a new certificate.
4. The user selects the academic level to which the certificate belongs.
5. The user enters a description of the certificate.
6. The user saves the record (UC-ICE2).
7. The system makes the certificate available for selection when adding academic information.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **4.a** The user adds a new academic level (UC-PS9).
    1. The user returns to Step 1 to add the certificate.
- **6.a** The system determines that the certificate already exists in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `certificate` (iHRIS_Certificate) in ihris-qualify

### UC-PS11 Add or update an identification type

The Data Operations Manager updates a list of identification types that are available for selection within the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the identification type already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is identical for both iHRIS Manage and Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `id_type` (iHRIS_PersonID_Type) in ihris-common

### UC-PS12 Add or update a marital status

The Data Operations Manager adds a new marital status to the system that is available in selection lists.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the marital status was already entered in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is the same for both iHRIS Manage and Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `marital_status` (I2CE_SimpleList) in ihris-common

### UC-PS13 Add or update a country

The Data Operations Manager updates the list of countries available for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
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

- **3.a** The user selects an existing country
    1. The system opens the item for editing.
- **6.a** The user selects the country as the primary country.
    1. The system displays the country first in all country selection menus.
- **6.b** The user selects more than one country as the primary country.
    1. The system displays all primary countries at the top of selection menus in alphabetical order.
- **7.a** The user selects that the country is used for location selection.
    1. The system makes the country available for selection when a location, such as an address, is being specified.
- **8.a** The system determines that the country and country code are already in the database.
    1. The system displays an error and will not continue.

**Notes**

- This use case is the same for iHRIS Manage, iHRIS Plan and iHRIS Qualify. *(10/31/2007)*
- Geographical locations are tied together from largest to smallest: country --> region --> district, state or province --> county or sector. *(10/31/2007)*
- The country list also displays nationalities for selection. Disabling the location selection limits the country to nationality selection only (new feature in version 3.0). *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `country` (iHRIS_Country) in ihris-common

### UC-PS14 Add or update a region

The Data Operations Manager updates the list of regions available for selection in the system and establishes the region's parent country.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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
8. The user enters the code for the region.
9. The user saves the record (UC-ICE2).
10. The system makes the region available for reporting.

**Extensions**

- **2.a** The user does not select a country.
    1. The system provides only the option to add a new region.
    2. Skip to Step 5.
- **6.a** The user adds a new country (UC-PS13).
    1. The user returns to Step 1 to add the region.
- **6.b** The system detects that the country was previously selected.
    1. The system fills in the selected country.
- **7.a** The system determines that the region and its parent are the same as a location previously entered in the database.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `region` (iHRIS_Region) in ihris-common

### UC-PS15 Add or update a district

The Data Operations Manager updates the list of districts available for selection in the system and establishes the district's parent region.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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
    1. The system displays its information for editing.
- **8.a** The system detects that the country and region were previously selected.
    1. The system fills in the selections for the district.
- **9.a** The systerm determines that the district and its parents are the same as a location previously entered in the database.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `district` (iHRIS_District) in ihris-common

### UC-PS16 Add or update a county

The Data Operations Manager updates the list of counties available for selection in the system and establishes the county's parent district.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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
    1. The system displays all information entered for that county and provides the option to update that information.
- **10.a** The system detects that the country, region and district were previously selected.
    1. The system fills in the previous selections for the county.
- **11.a** The system determines that the county and its parents are the same as a location previously entered in the database.
    1. The system displays an error message and will not continue.

**Notes**

- The use case is the same for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `county` (iHRIS_County) in ihris-common

### UC-PS17 Add or update a health facility

The Data Operations Manager adds a new health facility or updates an existing health facility in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The health facility is added to the system and is available for selection from lists in various use cases.

**Main success scenario**

1. The user selects the option to manage the list of health facilities.
2. The system displays all health facilities entered in the system.
3. The user adds a new health facility.
4. The user enters the name of the health facility.
5. The user enters a health facility identification code.
6. The user adds contact information (UC-PS31).
7. The user selects the country where the health facility is located.
8. The system displays a list of districts in that country.
9. The user selects the district where the health facility is located.
10. The system displays a list of counties in that district.
11. The user selects the county where the health facility is located (optional).
12. The user selects the facility agent.
13. The user selects the facility type.
14. The user selects the status of the health facility.
15. The user saves the record (UC-ICE2).
16. The system makes the health facility available for selection.
17. The system provides the option to update the health facility.

**Extensions**

- **3.a** The user selects an existing health facility.
    1. The system displays the health facility's record with options to edit any of the information.
- **7.a** The user adds the country, district or county.
    1. The user returns to Step 1 to add the health facility.
- **12.a** The user adds the facility agent (UC-PS23).
    1. The user returns to Step 1 to add the health facility.
- **13.a** The user adds the facility type (UC-PS24).
    1. The user returns to Step 1 to add the health facility.
- **14.a** The user adds the facility status (UC-PS25).
    1. The user returns to Step 1 to add the health facility.
- **16.a** The system determines that the health facility name already exists in the database.
    1. The system displays an error and will not continue.

**Notes**

- The health facility identification code is optional and is numbers only. *(8/23/2006)*

**iHRIS 4.3.3 forms** (derived by name matching): `health_facility` (iHRIS_HealthFacility) in ihris-qualify

### UC-PS18 Associate a training institution with a health facility

The Data Operations Manager selects one or more training institutions that are associated with a particular health facility.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system. The health facility's record must have been previously created.

**Success guarantee.** The health facility is successfully associated with the training institution.

**Main success scenario**

1. The user selects the option to manage the list of health facilities.
2. The system displays all health facilities entered in the system.
3. The user selects the health facility to edit.
4. The user selects the option to associate a training institution.
5. The user selects the training institution(s) associated with the health facility.
6. The user saves the record (UC-ICE2).
7. The system displays the training institution with the health facility's record.

**Extensions**

- **5.a** The user adds a training institution (UC-PS19).
    1. The user returns to Step 1 to associate the training institution with the health facility.

**iHRIS 4.3.3 forms** (derived by name matching): `training_institution` (iHRIS_ListByCountry) in ihris-common, `health_facility` (iHRIS_HealthFacility) in ihris-qualify, `training_institution` (iHRIS_QualifyTrainingInstitution) in ihris-qualify

### UC-PS19 Add or update a training institution

The Data Operations Manager enters identifying information about a training institution so that it may be used within the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The training institution is successfully entered into the database and is available for selection in other use cases.

**Main success scenario**

1. The user selects the option to manage the list of training institutions.
2. The system displays all training institutions entered in the system.
3. The user adds a training institution.
4. The user enters the name of the training institution.
5. The user enters the training institution's identification code (optional).
6. The user adds contact information (UC-PS31).
7. The user selects the country where the training institution is located.
8. The system displays a list of districts within that country.
9. The user selects the district where the training institution is located.
10. The system displays a list of counties within that district.
11. The user selects the county where the training institution is located (optional).
12. The user selects the agent under which the training institution belongs.
13. The user selects the status of the training institution.
14. The user saves the record (UC-ICE2).
15. The system displays the training institution information and provides the option to associate a health facility with a training institution (UC-PS20), add a cadre offered by a training institution (UC-PS21) or add inspection information for a training institution (UC-PS22).
16. The system provides the option to update the training institution information.

**Extensions**

- **3.a** The user selects an existing training institution.
    1. The system displays the training institution's record and provides options to update the information.
- **7.a** The user adds a new country, district or county.
    1. The user returns to Step 1 to add the training institution.
- **12.a** The user adds a new facility agent (UC-PS23).
    1. The user returns to Step 1 to add the training institution.
- **13.a** The user adds a new facility status (UC-PS25).
    1. The user returns to Step 1 to add the training institution.
- **14.a** The system determines that the training institution has already been entered in the database.
    1. The system displays an error and will not continue.

**Notes**

- The institution/centre code is numbers only and is optional. *(8/23/2006)*

**iHRIS 4.3.3 forms** (derived by name matching): `training_institution` (iHRIS_ListByCountry) in ihris-common, `training_institution` (iHRIS_QualifyTrainingInstitution) in ihris-qualify

### UC-PS20 Associate a health facility with a training institution

The Data Operations Manager selects one or more health facilities that are associated with a particular training institution.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system. The training institution's record must have been previously created.

**Success guarantee.** The training institution is successfully associated with the health facility.

**Main success scenario**

1. The user selects the option to manage training institutions.
2. The system displays all training institutions that have been entered in the system.
3. The user selects a training institution.
4. The system displays the training institution's record.
5. The user selects the option to associate a health facility.
6. The user selects the health facility or facilities associated with the training institution.
7. The user saves the record (UC-ICE2).
8. The system displays the health facility with the training institution's record.

**Extensions**

- **6.a** The user adds a new health facility (UC-PS17).
    1. The user returns to Step 1 to associate the health facility with the training institution.

**iHRIS 4.3.3 forms** (derived by name matching): `training_institution` (iHRIS_ListByCountry) in ihris-common, `health_facility` (iHRIS_HealthFacility) in ihris-qualify, `training_institution` (iHRIS_QualifyTrainingInstitution) in ihris-qualify

### UC-PS21 Add or update a pre-service training program

The Data Operations Manager associates a cadre with a training institution so that when a new training is added to a student's record, the cadre is available for selection when that training institution is selected.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The training institution has been added to the system. The user must be logged in to the system.

**Success guarantee.** The program is associated with the training institution so that when the training institution is selected in other use cases, the program is displayed.

**Main success scenario**

1. The user selects the option to update a training institution.
2. The system displays all training institutions entered in the system.
3. The user selects a training institution to edit.
4. The system displays the training institution's record with all training programs entered for that institution.
5. The user selects the option to add a training program or select an existing training program to edit.
6. The user selects the cadre.
7. The system displays today's date for the program's start date.
8. The user changes the start date for the program, if necessary.
9. If the program is no longer being offered, The user selects an end date for it.
10. The user enters the recommended number of students for the program.
11. The user saves the record (UC-ICE2).
12. The system displays the program information with the training institution's record and provides the option to add another program or edit the existing programs.

**Extensions**

- **5.a** The user selects an existing training program.
    1. The system displays all of the training program's information and enables any field to be changed.
- **6.a** The user adds a cadre (UC-PS2).
    1. The user returns to Step 1 to add the training program.
- **6.b** The system determines that a cadre has already been added for that training institution.
    1. The system removes the cadre from the selection list.
- **10.a** The user does not enter a recommended number of students.
    1. The system saves 0 by default.

**iHRIS 4.3.3 forms** (derived by name matching): `training_program` (iHRIS_TrainingProgram) in ihris-qualify

### UC-PS22 Enter inspection information

The Data Operations Manager records the details of a training institution's inspection.

| | |
|---|---|
| Priority | P2 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The training institution has already been added to the system. The user must be logged in to the system.

**Success guarantee.** The inspection information is saved with the training institution's record.

**Main success scenario**

1. The user selects the option to manage the list of training institutions.
2. The system displays all training institutions entered in the system.
3. The user selects the training institution to edit.
4. The system displays the training institution's record.
5. The user selects the option to add inspection information.
6. The system displays today's date for the inspection date.
7. The user changes the date of the inspection, if necessary.
8. The user enters any notes about the inspection.
9. The user selects whether the training institution passed or failed inspection.
10. The user saves the record (UC-ICE2).
11. The system saves the inspection information and displays it with the training institution's record.
12. The system saves the previous inspection information as historical data and displays it in the inspection history.
13. The system provides the option to view the training institution's inspection history and update the current inspection information.

**Extensions**

- **9.a** The user does not select any inspection results.
    1. The system selects Pass by default.

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS23 Add or update a facility agent

The Data Operations Manager adds or edits a facility agent for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The facility agent is added to the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage facility agents.
2. The system displays all facility agents entered in the system.
3. The user adds a new facility agent.
4. The user enters a description for the facility agent.
5. The user saves the record (UC-ICE2).
6. The system makes the facility agent available for selection when adding facilities.

**Extensions**

- **3.a** The user selects an existing facility agent.
    1. The system opens the item for editing.
- **5.a** The system determines that the facility agent already exists in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `facility_agent` (I2CE_SimpleList) in ihris-qualify

### UC-PS24 Add or update a facility type

The Data Operations Manager adds a new facility type for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
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

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the facility type has already been entered in the database.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is identical for iHRIS Manage and Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `facility_type` (I2CE_SimpleList) in ihris-common

### UC-PS25 Add or update a facility status

The Data Operations Manager adds a new facility status for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The facility status is added to the system and is available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage the list of facility statuses.
2. The system displays all facility statuses entered in the system.
3. The user adds a new facility status.
4. The user enters a description or name for the facility status.
5. The user saves the record (UC-ICE2).
6. The system makes the facility status available for selection when adding facilities.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the facility status has already been entered in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `facility_status` (I2CE_SimpleList) in ihris-qualify

### UC-PS51 Add or update a verification change

The Data Operations Manager adds a new verification change option for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Data Operations Manager](roles.md#ihris-a-ps1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1.1 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The verification change is added to the system and is available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage the list of verification changes.
2. The system displays all verification changes entered in the system.
3. The user adds a new verification change.
4. The user enters a description or name for the verification change.
5. The user saves the record (UC-ICE2).
6. The system makes the verification change available for selection when recording verifications.

**Extensions**

- **3.a** The user selects an existing item.
    1. The system opens the item for editing.
- **5.a** The system determines that the verification change has already been entered in the database.
    1. The system displays an error and will not continue.

**iHRIS 4.3.3 forms** (derived by name matching): `verify_change` (I2CE_SimpleList) in ihris-qualify

## 1.2 Record Management

Add a new record to the system and update records that have been entered into the system.

- Access these functions via the Add Person link on the main menu. *(10/15/2007)*

## 1.2.1 General

This module enables entering general information about a person into his/her record that is not related to training, registration or licensing.

- These functions become available when a new record is added or when a person's record is displayed; this is the first editable screen that appears. *(10/15/2007)*

### UC-PS27 Enter a new record

The Records Officer creates an initial record for a person in the system.

| | |
|---|---|
| Priority | P4 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system. The personal title, nationality, country and district of residence have been entered in the system.

**Success guarantee.** The health worker's basic details are recorded in the system and a new record for the person is created.

**Main success scenario**

1. The user selects the option to add a new record.
2. The user selects the title for the person (optional).
3. The user enters the name of the person:
    - surname (required)
    - first name (required)
    - any other names
    - suffix
4. The user selects the person's nationality / citizenship (required).
5. The user selects the country where the person resides (required).
6. The system displays all districts in the country.
7. The user selects the district where the person resides (the home district; required).
8. The system displays all counties within that district.
9. The user selects the county where the person resides (the home county), if known.
10. The user selects the person's home (permanent) country.
11. The system displays all districts in that country.
12. The user selects the person's home (permanent) district.
13. The system displays all counties within that district.
14. The user selects the person's home county.
15. The user saves the record (UC-ICE2).
16. The system validates that the name does not already exist in the system.
17. The system logs the system date as the entry date for the index.
18. The system displays the new record and the option to add additional information.
19. The system provides the option to update the name or other information.

**Extensions**

- **15.a** The system determines that the surname and first name combination match a record that is already in the system.
    1. The system prompts the user to compare the two records and determine whether they are the same.
    2. The user selects the matching record and edits it, or continues editing the new record, if it is different.
- **19.a** The user selects the update option and changes the person's name.
    1. The system saves the former name in the person's name history.
    2. The system provides the option to view the name history.

**Notes**

- This use case generally occurs after the student has been admitted to a training institution or has received a registration or license. *(2/11/2008)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS28 Add identification information

The Records Officer enters identifications into a person's record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The required identification types have been added to the system. The person has a record in the system. The user must be logged in to the system.

**Success guarantee.** The identification information is saved to the database and displayed with the person's record.

**Main success scenario**

1. The user selects the option to add an identification to a person's record.
2. The user selects a type of identification.
3. The user enters the identification number.
4. The user saves the record (UC-ICE2).
5. The system displays the new identification information in the person's record.
6. The system provides the option to update the identification.
7. The user repeats Steps 1-6 for each required type of identification.

**Notes**

- Identification checking will have to be implemented at the time of customization because requirements change so much depending on where the system is located. *(10/31/2007)*
- This use case is the same in both iHRIS Manage and iHRIS Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS29 Add demographic information

The Records Officer adds demographic information about a person to his or her record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has a record in the system. The user must be logged in to the system. The marital status and country, district and county have been entered into the system for selection.

**Success guarantee.** The demographic information is saved and is displayed with the person's record.

**Main success scenario**

1. The user selects the option to add demographic information to a person's record.
2. The user sets the date of birth.
3. The user selects the gender.
4. The user selects the marital status.
5. The user selects the country of birth.
6. The system displays all districts in that country.
7. The user selects the district of birth.
8. The system displays all counties within that district.
9. The user selects the county of birth for the person, if known.
10. The user saves the record (UC-ICE2).
11. The system displays the demographic information in the record.
12. The system provides the option to update the demographic information.

**Notes**

- This use case is essentially the same for iHRIS Manage and iHRIS Qualify. *(10/31/2007)*
- Country, district and county of birth data entry fields are implemented in iHRIS Qualify only. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `demographic` (iHRIS_Demographic) in ihris-common, `demographic` (iHRIS_QualifyDemographic) in ihris-qualify

### UC-PS30 Add academic information

The Records Officer adds secondary education information about a person to his or her record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The person has a record in the system. The correct academic levels and certificates have been entered into the system. The user is logged in.

**Success guarantee.** The health worker's academic qualification details are recorded in the system and displayed with his/her record.

**Main success scenario**

1. The user selects the option to add secondary education information to a person's record.
2. The user enters the name of the secondary school that the person attended.
3. The user selects the highest academic level achieved.
4. The system displays all certificates for that academic level.
5. The user selects the certificate that the person holds.
6. The user enters the grade obtained (optional).
7. The user enters the certificate number (optional).
8. The user saves the record (UC-ICE2).
9. The system displays the academic information in the person's record.
10. The system provides the option to update the academic information.

**Notes**

- Academic information refers to any education that took place prior to entering the health training program. *(11/1/2007)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS31 Add contact information

The Records Officer adds any type of contact information for a person or institution.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | Subfunction |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The record exists in the system. The user must be logged in to the system.

**Success guarantee.** The contact information is saved with the appropriate record.

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

- **1.a** The system determines that a contact of that type has previously been added.
    1. The system does not provide the option to allow another contact of the same type.

**Notes**

- This use case is the same for iHRIS Manage and iHRIS Qualify, although the specific types of contacts for each are slightly different. *(10/31/2007)*
- All fields are optional. *(10/31/2007)*
- This subfunction is referenced wherever contact information additions or updates are required. *(10/31/2007)*
- Institutions only have one contact type (as opposed to people records). The contact type does not need to be selected, as the contact information can be entered with the institution's other details. *(2/11/2008)*

**iHRIS 4.3.3 forms** (derived by name matching): `contact` (iHRIS_Contact) in ihris-common

### UC-PS32 Record notes

The Records Officer or Registration Supervisor records notes about a particular person and saves them with the person's record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2), [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The person has a record in the system. The user must be logged in to the system.

**Success guarantee.** The notes are entered and saved with the person's record.

**Main success scenario**

1. The user selects the option to add a note to a person's record.
2. The user enters any notes or special information about the person.
3. The system displays today's date as the note entry date.
4. The user changes the note entry date, if it is different.
5. The user saves the record (UC-ICE2).
6. The system maintains and displays a log of all notes that were entered in reverse chronological order.
7. The system provides an option to update each note.

**Notes**

- The notes area is an open area that can be used for any purpose. *(10/31/2007)*
- This use case is the same for iHRIS Manage and Qualify. *(10/31/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `notes` (iHRIS_Notes) in ihris-common

### UC-PS50 Record verification

The Records Officer records a verification of a user's record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 3.1.1 |

**Preconditions.** The verification change has been entered in the system. The user is logged in.

**Success guarantee.** The verification change is saved in the person's verification history and can be viewed in the record.

**Main success scenario**

1. The user selects the option to record a verification in a record.
2. The user selects the date of the verification.
3. The user selects any verification changes made.
4. The user saves the record (UC-ICE2).
5. The system saves the verification changes to the person's verification history and displays the latest verification change in the record.

**Extensions**

- **2.a** The user does not select a date.
    1. The system records today's date by default.

**Notes**

- This is a new use case to fulfill a verification requirement requested by the Uganda users of the system. *(10/7/2008)*

**iHRIS 4.3.3 forms** (derived by name matching): `record_verify` (iHRIS_RecordVerify) in ihris-qualify

## 1.2.2 Training

This module enables adding a pre-service training program to a person's record. It includes optional functions for recording national exam results.

- These functions are available when clicking Add Training in a person's record. *(10/15/2007)*
- The person's pre-service training program determines the health worker's cadre in the system. A person may have completed more than one training program and thus be registered/licensed in more than one cadre. *(10/15/2007)*
- At least one pre-service training program, with a graduation date, must be added to a person's record before the person can be registered. Each registration/license is linked to one pre-service training program. *(10/15/2007)*

### UC-PS35 Index a training

The Records Officer records details about the training program that the student is enrolled in.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The training institution and its cadres have already been entered into the system. The initial record for the student has been created. The user must be logged in to the system.

**Success guarantee.** The student's record is updated and saved with the training information, and the student is assigned an index number for that training.

**Main success scenario**

1. The user selects the option to add a training to a person's record.
2. The user enters the index number for the training.
3. The user selects the date of intake (optional).
4. The user selects the training institution where the student has been admitted.
5. The system displays the cadres offered by the training institution.
6. The user selects the cadre where the student is to be indexed.
7. The user enters the training end (graduation) date if the student has completed training.
8. The user saves the record (UC-ICE2).
9. The system displays the record with the training information and provides the option to document a disruption (UC-PS36), record an application to sit for the exam (UC-PS40) or issue a registration (UC-PS40).
10. The system provides the option to correct the information.

**Extensions**

- **2.a** The user selects the option to generate a new index number.
    1. The system generates the next index number available upon saving the record.
- **4.a** The user selects the country where the person was trained if the training was outside the country.
    1. The user enters the name of the training institution, if known.
    2. Continue to Step 6.
- **7.a** The user sets the graduation date for before the intake date.
    1. The system displays an error message and will not continue.
- **7.b** The user enters a foreign country where the training took place.
    1. The system prompts the user to enter the graduation date.
- **9.a** The user leaves the end date blank.
    1. The system marks the training as "in progress."
    2. The system provides the option to set a graduation date (UC-PS38).
    3. The system does not provide the option to issue a registration.

**Notes**

- Once a student has passed an exam for a particular cadre inside the country, the person cannot enroll in another training in that same cadre. *(9/22/2006)*
- A training or upgrade, either inside or outside the country, can be added for any person at any time. *(6/4/2007)*
- The training end date (graduation date) signifies that the person is eligible for registration. *(6/4/2007)*
- To ensure the system is universal, the student can be registered in more than one instance of the same training program (cadre). It is up to the data entry person to ensure this information is entered correctly. Some implementations may be customized to prevent double-entry of cadres. *(7/26/2007)*
- The training may be the student's first or an upgrade. The training program may be inside or outside the country. Training information may be recorded separately, when the student enters a training program, or as part of the registration process, after training is complete. *(11/1/2007)*
- Index number is not unique. A new index number is issued with each training, and index numbers may be duplicated. The index number is linked to the training rather than to the entire record. The index number is used primarily for searching and display. *(2/11/2008)*

**iHRIS 4.3.3 forms** (derived by name matching): `training` (iHRIS_Training) in ihris-qualify

### UC-PS36 Record a discontinuation

If a student has discontinued a training program, the Records Officer notes this with the student's record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The appropriate disruption category and disruption reason have been added to the system. The student record has been created and the enrollment in a training program has been recorded in the student's record. The user must be logged in to the system.

**Success guarantee.** The disruption in training is correctly recorded with the student's record, and no registrations or licenses can be issued to the student.

**Main success scenario**

1. The user selects the option to update a training in the student's record.
2. The user selects the option to disrupt training.
3. The user selects the disruption category.
4. The system displays a list of specific reasons for disruption in that disruption category.
5. The user selects the specific disruption reason.
6. The user selects the date of disruption.
7. The user saves the record (UC-ICE2).
8. The system displays the record with the updated training disruption information and provides the option to document a resumption. (UC-PS37)

**Extensions**

- **2.a** The system determines that a disruption has already been recorded for the training and no resumption has been recorded.
    1. The system does not provide the option to disrupt training again.
- **6.a** The user enters a disruption date that comes before the date of intake.
    1. The system displays an error and prompts to enter a valid date.

**Notes**

- This use case is triggered by the report of a training disruption from the training institution to the Licensing and Certification Authority. *(7/14/2006)*
- This use case is optional and is not needed if disruptions are not recorded. *(6/4/2007)*
- All fields are required if used. *(8/2/2007)*

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS37 Record a resumption

If the student has resumed training after a disruption, the Records Officer notes this along with the resumption date.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The student's training disruption has been recorded with the student's record in the system. The user must be logged in to the system.

**Success guarantee.** The resumption in training is correctly recorded with the student's record, and a graduation date can be set for the training program.

**Main success scenario**

1. The user selects the option to update a training in a health student's record.
2. The user selects the option to resume training.
3. The user enters the date of resumption.
4. The user saves the record (UC-ICE2).
5. The system displays the record with the new resumption information and provides the option to document a disruption (UC-PS36) as well as the option to set a graduation date (UC-PS38).

**Extensions**

- **3.a** The user enters a resumption date that occurred before the disruption date.
    1. The system displays an error message and will not continue.

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS38 Set a graduation date

The Records Officer sets a graduation date for a student to indicate that the student has completed training.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The user is logged in to the system. The student has entered a training program, which has been entered in the system, but has not completed or discontinued it.

**Success guarantee.** The graduation date is recorded in the student's record, and a registration can be issued to the student.

**Main success scenario**

1. The user selects the option to update a training in a student's record.
2. The user selects the option to set a graduation date.
3. The user enters the graduation date.
4. The user saves the record (UC-ICE2).
5. The system displays the graduation date, marks the training as complete and provides the option to issue a registration to the student (UC-PS40).

**Extensions**

- **2.a** The system determines that the training was marked discontinued.
    1. The system does not provide the option to set a graduation date.
- **3.a** The user sets a graduation date that falls before the intake date.
    1. The system generates an error message and will not proceed.

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS39 Record exam details

The Examination Supervisor or Records Officer documents a student's application to take the national exam and the results.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Examination Supervisor](roles.md#ihris-a-ps4), [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The student has completed a training and training information has been entered in the student's record. The user must be logged in to the system.

**Success guarantee.** The student's record is successfully updated with their examination application information and the results of the examination that s/he took.

**Main success scenario**

1. The user selects the option to update a training in a student's record.
2. The user selects the option to record an exam.
3. The system displays today's date for the application date.
4. The user changes the date, if it is different.
5. The user indicates whether the student's required application materials have been received.
6. The user indicates whether the student's required application materials have been approved.
7. The user enters the endorser information, if known:
    - name
    - date of endorsement
    - qualifications
8. The system displays today's date for the exam date.
9. The user changes the exam date, if it is different.
10. The user selects the number of tries for the exam:
    - First
    - Re-try
    - Final
11. The user selects the examination results:
    - pass
    - fail
    - did not sit for exam
12. The user enters the examination number.
13. The user saves the record (UC-ICE2).
14. The system displays the record with the exam application information.
15. The system provides the option to correct the exam information.

**Extensions**

- **5.a** The user does not select an option.
    1. The system saves yes by default.
- **6.a** The user does not select an option.
    1. The system saves yes by default.
- **9.a** The user sets the exam date for before the application date.
    1. The system displays an error and will not continue.
- **10.a** The user selects final.
    1. The system does not allow the exam results to be updated.
- **11.a** The user selects fail or did not sit for exam.
    1. The system provides the option to update the exam information.
    2. When exam performance is re-recorded, the system displays the new results and saves the previous results to an examination history.
- **11.b** The user selects pass.
    1. The system does not allow any more updates to the exam information.

**Notes**

- Exams are optional in the base system. In some implementations, entering exam results may be required, in which case a registration cannot be issued until a passing exam result is recorded by an Examination Supervisor, a special role authorized to enter examination results. When exams are optional, the Records Officer can enter exam results. *(6/4/2007)*
- If the exam is passed, the graduation date must also be recorded so a registration can be added. *(7/19/2007)*
- This use case is triggered when a student has completed a training program and has submitted an application to sit for the final exam (conducted annually). *(11/1/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `exam` (iHRIS_Exam) in ihris-qualify

## 1.2.3 Licensing

This module captures registration, licensing and other post-graduation actions, such as private practice licensing, out migration verification requests and deployment records.

- These functions are only enabled once a pre-service training program with a graduation date is recorded in a health worker's record. *(10/15/2007)*
- These functions can be accessed by clicking Update Registrations/Licenses beside the training program in the Training Information section of a person's record. *(10/15/2007)*

### UC-PS40 Issue a registration

The Registration Supervisor documents an application for registration and issues a registration number.

| | |
|---|---|
| Priority | P7 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The student completed a training (the end date of the training has been recorded). The user must be logged in to the system.

**Success guarantee.** The student's record is successfully updated and a registration number is issued; a license can now be issued to the health worker.

**Main success scenario**

1. The user selects the option to update a training in a student's record.
2. The user selects the option to add a registration.
3. The user enters the registration number.
4. The system displays today's date for the application date.
5. The user changes the application date, if it is different.
6. The system displays today's date for the registration date.
7. The user changes the registration date, if it is different.
8. The user selects whether the practice type is temporary or permanent.
9. The user saves the record (UC-ICE2).
10. The system validates that the registration number does not already exist in the system.
11. The system displays the record with the registration information and provides the option to issue a new license (UC-PS41).
12. The system provides the option to correct the registration information.

**Extensions**

- **3.a** The user selects the option to generate a registration number.
    1. The system generates the next registration number when the record is saved.
- **8.a** The user does not select a practice type.
    1. The system enters permanent by default.
- **10.a** The system determines that the number exists in the database.
    1. The system prompts the user to correct the number or generate a new number.

**Notes**

- This is not reflected in this use case, but there can be a duplicate registration number for different cadres. This should only occur when entering historical data; new data should have a unique registration number every time. *(7/14/2006)*
- This use case is triggered when a person applies for registration. *(11/1/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `registration` (iHRIS_Registration) in ihris-common, `registration` (iHRIS_Registration) in ihris-qualify

### UC-PS41 Issue a license

The Registration Supervisor issues a new license to a health care professional who has successfully registered, with a license number.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has been issued a registration, and that has been recorded in his/her record. The user must be logged in to the system.

**Success guarantee.** The license is successfully added to the health worker's record, and a license number is issued to the health worker.

**Main success scenario**

1. The user selects the option to update a registration in a health worker's record.
2. The user selects the option to add a license.
3. The system displays the registration number for the license number.
4. The user enters a new license number, if it is different.
5. The system displays today's date for the license start date.
6. The user changes the start date for the license, if it is different.
7. The user enters the end date for the license.
8. The user saves the record (UC-ICE2).
9. The system displays the record with the license information and provides these options: Renew a license (UC-PS45); Add a completed continuing education course (UC-PS45); Issue or renew a private practice license (UC-PS45); Document a disciplinary action (UC-PS45).
10. The system provides the option to correct the license information.

**Extensions**

- **4.a** The user generates a new license number rather than entering one.
    1. The system generates the next license number when the record is saved.
- **7.a** The system determines that the end date entered comes before or is the same as the start date.
    1. The system displays an error and prompts the user to enter a different end date.

**Notes**

- In the ideal situation, the registration number will be used to identify every transaction, including issuing a license. However, a separate license number may be needed. The use case provides the option of entering a different license number or reusing the registration number as the license number. *(6/5/2007)*
- This use case is triggered when a health worker applies for a new license. *(11/1/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `license` (iHRIS_License) in ihris-qualify

### UC-PS42 Renew a license

The Registration Supervisor records a license renewal.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has previously been issued a license number in the system. The user must be logged in to the system.

**Success guarantee.** The record is successfully updated with the new license information and number; the previous license is recorded in the person's license history.

**Main success scenario**

1. The user selects the option to update a license in a health worker's record.
2. The user selects the option to renew the license.
3. The system displays the previously issued license number for the license number of the renewal.
4. The system displays today's date for the license start date.
5. The user changes the start date for the renewal, if it is different.
6. The user enters the end date for the renewal.
7. The user saves the record (UC-ICE2).
8. The system saves the previous license to the person's license history.
9. The system displays the record with the latest license and provides an option to display the license history.
10. The system provides the option to correct the license information.

**Extensions**

- **5.a** The system determines that the start date entered comes before the end date for a previous license.
    1. The system displays an error and prompts the user to correct the date.
- **6.a** The system determines that the end date entered comes before or the same as the start date.
    1. The system displays an error message and prompts the user to enter a new end date.

**Notes**

- In the ideal situation, the registration number will be used to identify every transaction, including issuing a license. However, a separate license number may be needed. The use case covers both situations by reusing the previous license number as the license number for the renewal. *(6/5/2007)*
- This use case is triggered when a worker applies for a license renewal. *(2/11/2008)*

**iHRIS 4.3.3 forms** (derived by name matching): `license` (iHRIS_License) in ihris-qualify

### UC-PS43 Add continuing education credits

The Registration Supervisor documents continuing medical education requirements that have been fulfilled by the health worker to meet license renewal requirements.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has been issued a license, which has been recorded in his/her record. The appropriate continuing education courses have been entered in the system for selection. The user must be logged in to the system.

**Success guarantee.** The record is successfully updated with the completed continuing education courses.

**Main success scenario**

1. The user selects the option to update a license in a health worker's record.
2. The user selects the option to record a continuing education course.
3. The user selects a continuing education course that was completed.
4. The user enters the number of credit hours that were earned.
5. The user enters the start and end dates for the course.
6. The user saves the record (UC-ICE2).
7. The system displays the completed course information in the person's record.
8. The system provides the option to correct the continuing education information.
9. The user repeats Steps 1-8 for each course that the health worker has completed.

**Extensions**

- **5.a** The system determines that the end date comes before the start date.
    1. The system displays an error message and prompts the user to enter a new end date.

**iHRIS 4.3.3 forms** (derived by name matching): `continuing_education` (iHRIS_ContinuingEducation) in ihris-common, `person_training` (iHRIS_PersonTraining) in ihris-qualify

### UC-PS44 Issue a private practice license

The Registration Supervisor issues a private practice license to a health care worker applying to operate a private health facility.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The worker has received a license, which has been recorded in the system. The health facility where the person will be practicing has been entered in the database. The user must be logged in to the system.

**Success guarantee.** The private practice license number is issued and the person's record is updated with the private practice license information.

**Main success scenario**

1. The user selects the option to update a license in a health worker's record.
2. The user selects the option to issue a private practice license.
3. The system displays the registration number for the private practice license number.
4. The user enters a private practice license number, if it is different.
5. The system displays today's date for the license start date.
6. The user changes the start date for the license, if it is different.
7. The user enters the end date for the license.
8. The user enters the inspection results, if known.
9. The system displays today's date for the inspection date.
10. The user changes the inspection date, if it is different.
11. The user selects the health facility where the person will be practicing.
12. The user saves the record (UC-ICE2).
13. The system displays the record with the private practice license information.
14. The system provides the option to correct the private practice license information.

**Extensions**

- **4.a** The user generates a new private practice license number.
    1. The system generates the next private practice license number when the record is saved.
- **7.a** The system determines that the end date comes before or is the same as the start date.
    1. The system displays an error message and prompts the user to enter a new end date.
- **13.a** The system determines that a private practice license has previously been issued for that person.
    1. The system saves the previous license as historical data and provides the option to review the past private practice license history.

**Notes**

- In the ideal situation, the registration number will be used to identify every transaction, including issuing a license. However, a separate private practice license number may be needed. The use case provides the option of entering a different license number or reusing the registration number as the license number. *(6/5/2007)*
- This use case is triggered by an application for a private practice license. *(11/1/2007)*
- The private practice license is issued and maintained separately from the health worker's license to practice. *(2/11/2008)*

**iHRIS 4.3.3 forms** (derived by name matching): `private_practice` (iHRIS_PrivatePractice) in ihris-qualify

### UC-PS45 Document a disciplinary action

If a member has been disciplined, the Registration Supervisor notes this with the member's record.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The health worker has been issued a license, which has been recorded in the system. The appropriate disciplinary category and reason have been added to the system. The user must be logged in to the system.

**Success guarantee.** The disciplinary action is correctly recorded with the member's record. If the license is suspended, the system prevents any further license renewals or related information to be recorded.

**Main success scenario**

1. The user selects the option to update a license in a health worker's record.
2. The user selects the option to record a disciplinary action.
3. The user selects the disciplinary action category.
4. The system displays a list of specific reasons for that category.
5. The user selects the specific disciplinary action.
6. The system displays today's date for the date of the disciplinary action.
7. The user changes the date of the disciplinary action, if it is different.
8. The user indicates whether the license is suspended (yes or no).
9. The user enters any notes about the disciplinary action.
10. The user saves the record (UC-ICE2).
11. The system displays the record with the updated disciplinary action information.
12. The system provides the option to correct the disciplinary action information.

**Extensions**

- **8.a** The user suspends the license.
    1. The system does not permit any new actions recorded on the record other than documenting a reinstatement (UC-PS46).

**Notes**

- Disciplinary actions can only be taken after licensing. *(6/4/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `disciplinary_action` (iHRIS_DisciplinaryAction) in ihris-qualify

### UC-PS46 Document a reinstatement

If the member has been reinstated after a disciplinary action, the Registration Supervisor notes this along with the reinstatement date.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The health worker has been issued a license that has been suspended, and this has been recorded in the system. The user must be logged in to the system.

**Success guarantee.** The reinstatement is correctly recorded with the health worker's record, and license renewals and other actions can be recorded for that person's current license.

**Main success scenario**

1. The user selects the option to update a license in a health worker's record.
2. The user selects the option to enter a reinstatement.
3. The user enters the date of the reinstatement.
4. The user enters any notes about the reinstatement.
5. The user saves the record (UC-ICE2).
6. The system displays the record with the new reinstatement information and makes all license options available.

**Extensions**

- **3.a** The system determines that the reinstatement date occurred before the suspension date.
    1. The system displays an error and prompts the user to change the reinstatement date.

**iHRIS 4.3.3 forms:** no form name occurs in the title (not linked).

### UC-PS47 Update deployment information

The Registration Supervisor or Records Officer enters or updates a health care worker's deployment information.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2), [Registration Supervisor](roles.md#ihris-a-ps3) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 2.0 |

**Preconditions.** The person has been registered, which has been entered in the system. The health care facility where the person is deployed has been entered into the database. The user must be logged in to the system.

**Success guarantee.** The deployment information is entered correctly and saved with the person's record.

**Main success scenario**

1. The user selects the option to add deployment information to a health worker's record.
2. The user selects the health facility where the person has been deployed.
3. The user enters the job or post title.
4. The user enters the job or post code, if known.
5. The system displays today's date for the date of deployment.
6. The user changes the date of deployment., if it is different.
7. The user saves the record (UC-ICE2).
8. The system displays the record with the deployment information.
9. The system provides the option to correct the deployment information.

**Extensions**

- **8.a** The system determines that a deployment has previously been entered for this health care worker.
    1. The system saves the past deployment to the person's deployment history and provides an option to view all past deployments.

**iHRIS 4.3.3 forms** (derived by name matching): `deployment` (iHRIS_Deployment) in ihris-qualify

### UC-PS48 Record out migration verification

When a verification request is received for a health care worker, the Records Officer documents such details as the country the person is migrating to and the reason for migrating, which may be useful in analyzing health worker retention issues.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Records Officer](roles.md#ihris-a-ps2) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The person has been issued a registration in the system. The user must be logged in to the system.

**Success guarantee.** The details of out migration are captured by the system during the process of verification and saved with the health worker's record.

**Main success scenario**

1. The user selects the option to record out migration verification in a person's record.
2. The user selects the country where the request came from.
3. The user enters the worker's new address in the foreign country, if known.
4. The user selects the reason given for out migration.
5. The user records the name of the organization requesting the verification (country board), if known.
6. The system displays today's date for the date of the verification request.
7. The user changes the date of the verification request, if it is different.
8. The user saves the record (UC-ICE9).
9. The system displays the record with the out migration details.
10. The system provides the option to update the out migration details.
11. The user repeats Steps 1-8 for each out migration verification request.

**Extensions**

- **9.a** The system determines that a verification request for out migration has previously been recorded for this person.
    1. The system saves and displays all out migration verification requests that have been recorded.

**Notes**

- A request for verification for out migration does not mean that the health care worker has actually out migrated; that cannot be determined with this system. *(11/1/2007)*

**iHRIS 4.3.3 forms** (derived by name matching): `out_migration` (iHRIS_OutMigration) in ihris-qualify

## 1.3 Requirements

### REQ-PS3 Index numbers

Each training receives a unique index number, which is tied to that training program in that cadre. An index number can be typed or automatically generated. The index number is used only to identify the training and may be issued by the training institution.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS35

### REQ-PS4 Upgrades

When a person receives a subsequent training in another cadre other than the one s/he is initially registered in, this is called an upgrade. If the training is received in-country, the person cannot receive an upgrade in the same cadre. (The person can receive upgrades for the same cadre when trained outside the country.)

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS35

### REQ-PS5 Training location

A training may be received inside or outside the country.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS35

### REQ-PS6 Examination numbers

Recording examination results is optional. The examination number must be unique.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS39

### REQ-PS7 Examination attempts

A person can retake the exam three times by default. They must receive a passing exam result on one try to be eligible for registration, if exam results are required. If they do not receive a passing result in three tries, no more examination results can be recorded for that person.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 1.0 |

Referenced by: UC-PS39

### REQ-PS8 Private practice license numbers

When a person opens a clinic, s/he receives a private practice license in their name associated with the registration that they will be practicing. The registration number is reused for the private practice license number by default, or a new number may be entered.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS44

### REQ-PS9 Disciplinary action

Disciplinary action can only be recorded after a license has been issued.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS45

### REQ-PS10 License renewal dates

The start date for a license renewal cannot occur before the end date of the previous license period.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Release | 1.0 |

Referenced by: UC-PS43, UC-PS42

### REQ-PS11 Registration numbers

The registration number is the person's main identification number. It must be unique within a cadre. It can be reused for all licenses and license renewals.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS40

### REQ-PS12 Registration requirements

The only details about a training that must be recorded are the cadre and training end date. This specifies which cadre a person has received pre-service training in and makes that person eligible for registration in that cadre.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS35, UC-PS40

### REQ-PS13 Multiple registrations

Registration numbers are tied to cadres. When a person receives more than one registration in multiple cadres, a new registration number is issued for each subsequent registration.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 1.0 |

Referenced by: UC-PS40

### REQ-PS14 License numbers

When the person applies for a license, the registration number is reused for the license number by default. A new license number may be entered. License numbers do not have to be unique.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS41

### REQ-PS15 License renewals

When a license is renewed, the original license number is provided for the renewal by default. A new license number may not be typed in.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Source | [2009 iHRIS staff member 02 (identity withheld)](roles.md#ihris-2009-staff-02) |
| Release | 2.0 |

Referenced by: UC-PS43, UC-PS42

### REQ-PS16 Suspension of license

If a license is suspended, no actions can be performed on the person's record until the license is reinstated.

| | |
|---|---|
| Priority | P1 |
| Type | Business Rule |
| Status | Implemented |
| Release | 2.0 |

Referenced by: UC-PS45

## Cited but not described

The report cites these, but describes none of them:

- UC-PS26 *Add or update a personal title* (cited by A-PS1)
