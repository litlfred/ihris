---
title: "IHRIS Manage Form Fields - 4.0"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_manage_form_fields_4.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_manage_form_fields_4.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# IHRIS Manage Form Fields - 4.0

These are the forms and fields in iHRIS Manage version 4.0.1

There is also a graphical visualization of this data.
**Warning:** this is a very large file and you may wish to save it to your desktop instead of viewing it in your browser.

Here is a description of the Field types.

## application

The form *application* is implemented by the class: iHRIS\_Applicant
It has the following fields:

* position:
  + Header: Position(s)
  + Type: MAP\_MULT
  + Restrictions: Required
  + Maps To Forms: [position](#position)
* felony:
  + Header: Have you ever been convicted of a felony?
  + Type: YESNO
* felony\_circumstance:
  + Header: If yes, give the circumstances.
  + Type: STRING\_MLINE
* other\_info:
  + Header: In addition to your work history, are there other skills, qualifications or experience we should consider?
  + Type: STRING\_MLINE
* hear:
  + Header: How did you hear of this opening?
  + Type: STRING\_MLINE
* start\_date:
  + Header: When can you start?
  + Type: DATE\_YMD
* desired\_wage:
  + Header: Desired Wage
  + Type: CURRENCY
  + Maps To Forms: [currency](#currency)
* full\_time:
  + Header: Are you looking for full-time employment?
  + Type: YESNO
* hours:
  + Header: If no, what hours are you available?
  + Type: STRING\_MLINE

## benefit

The form *benefit* is implemented by the class: iHRIS\_Benefit
It has the following fields:

* type:
  + Header: Benefit Type
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [benefit\_type](#benefit_type)
* source:
  + Header: Source
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [salary\_source](#salary_source)
* recurrence:
  + Header: Recurrence Frequency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [benefit\_recurrence](#benefit_recurrence)
* amount:
  + Header: Amount
  + Type: CURRENCY
  + Restrictions: Required
  + Maps To Forms: [currency](#currency)
* start\_date:
  + Header: Start Date
  + Type: DATE\_YMD
  + Restrictions: Required
* end\_date:
  + Header: End Date
  + Type: DATE\_YMD

## benefit\_recurrence

The form *benefit\_recurrence* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## benefit\_type

The form *benefit\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## cadre

The form *cadre* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## classification

The form *classification* is implemented by the class: iHRIS\_Classification
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* description:
  + Header: Description
  + Type: STRING\_LINE
* code:
  + Header: Code
  + Type: STRING\_LINE

## competency

The form *competency* is implemented by the class: iHRIS\_Competency
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique in {competency\_type}
* competency\_type:
  + Header: Competency Type
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [competency\_type](#competency_type)
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## competency\_evaluation

The form *competency\_evaluation* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## competency\_type

The form *competency\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## contact

The form *contact* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## continuing\_education

The form *continuing\_education* is implemented by the class: iHRIS\_ContinuingEducation
It has the following fields:

* continuing\_education\_course:
  + Header: Continuing Education Course
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [continuing\_education\_course](#continuing_education_course)
* credit\_hours:
  + Header: Credit Hours
  + Type: INT
  + Restrictions: Required
* start\_date:
  + Header: Start Date
  + Type: DATE\_YMD
  + Restrictions: Required
* end\_date:
  + Header: End Date
  + Type: DATE\_YMD
  + Restrictions: Required

## continuing\_education\_course

The form *continuing\_education\_course* is implemented by the class: iHRIS\_ContinuingEducationCourse
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required
* credit\_hours:
  + Header: Credit Hours
  + Type: INT
  + Restrictions: Required

## council

The form *council* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## country

The form *country* is implemented by the class: iHRIS\_Country
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* alpha\_two:
  + Header: 2 Character Alpha Code
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* code:
  + Header: ISO Numeric Code
  + Type: INT
* primary:
  + Header: Primary Country
  + Type: YESNO
* location:
  + Header: Use for Location Selection
  + Type: YESNO

## county

The form *county* is implemented by the class: iHRIS\_County
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique in {district}
* district:
  + Header: District
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [district](#district)

## currency

The form *currency* is implemented by the class: iHRIS\_Currency
It has the following fields:

* code:
  + Header: Currency Code
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* name:
  + Header: Name
  + Type: STRING\_LINE
* country:
  + Header: Country
  + Type: MAP
  + Maps To Forms: [country](#country)
* symbol:
  + Header: Symbol
  + Type: STRING\_LINE

## degree

The form *degree* is implemented by the class: iHRIS\_Degree
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique in {edu\_type}
* edu\_type:
  + Header: Education Type
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [edu\_type](#edu_type)

## demographic

The form *demographic* is implemented by the class: iHRIS\_ManageDemographic
It has the following fields:

* birth\_date:
  + Header: Date of Birth
  + Type: DATE\_YMD
* gender:
  + Header: Gender
  + Type: MAP
  + Maps To Forms: [gender](#gender)
* marital\_status:
  + Header: Marital Status
  + Type: MAP
  + Maps To Forms: [marital\_status](#marital_status)
* dependents:
  + Header: Number of Dependents
  + Type: INT

## department

The form *department* is implemented by the class: iHRIS\_Department
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## district

The form *district* is implemented by the class: iHRIS\_District
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique in {region:country}
* region:
  + Header: Region
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [region](#region)
* code:
  + Header: Code
  + Type: STRING\_LINE

## edu\_type

The form *edu\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## education

The form *education* is implemented by the class: iHRIS\_Education
It has the following fields:

* degree:
  + Header: Degree
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [degree](#degree)
* institution:
  + Header: Institution Name
  + Type: STRING\_LINE
  + Restrictions: Required
* location:
  + Header: Institution Location
  + Type: STRING\_LINE
* year:
  + Header: Year of Graduation (leave blank if In Progress)
  + Type: DATE\_Y
* major:
  + Header: Major
  + Type: STRING\_LINE

## employee\_status

The form *employee\_status* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## employment

The form *employment* is implemented by the class: iHRIS\_Employment
It has the following fields:

* company\_name:
  + Header: Company Name
  + Type: STRING\_LINE
  + Restrictions: Required
* company\_address:
  + Header: Company Address
  + Type: STRING\_MLINE
* company\_phone:
  + Header: Company Telephone
  + Type: STRING\_LINE
* start\_date:
  + Header: Date Started
  + Type: DATE\_YMD
  + Restrictions: Required
* start\_wage:
  + Header: Starting Wage
  + Type: CURRENCY
  + Maps To Forms: [currency](#currency)
* start\_position:
  + Header: Starting Position
  + Type: STRING\_LINE
* end\_date:
  + Header: Date Ended (leave blank if still employed)
  + Type: DATE\_YMD
* end\_wage:
  + Header: Ending Wage
  + Type: CURRENCY
  + Maps To Forms: [currency](#currency)
* end\_position:
  + Header: Ending Position
  + Type: STRING\_LINE
* supervisor:
  + Header: Supervisor
  + Type: STRING\_LINE
* contact\_ok:
  + Header: Ok to Contact?
  + Type: YESNO
* responsibilities:
  + Header: Job Responsibilities
  + Type: STRING\_MLINE
* reason\_for\_leaving:
  + Header: Reason for Leaving
  + Type: STRING\_MLINE

## facility

The form *facility* is implemented by the class: iHRIS\_Facility

This form is used to descibe basic information about a facility

It has the child forms:

* [facility\_contact](#child_form)

It has the following fields:

* location:
  + Header: Location
  + Type: MAP
  + Maps To Forms: [county](#county),[district](#district)
* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* facility\_type:
  + Header: Facility Type
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [facility\_type](#facility_type)

## facility\_contact

The form *facility\_contact* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## facility\_type

The form *facility\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## gender

The form *gender* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## id\_type

The form *id\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## isco\_88\_major

The form *isco\_88\_major* is implemented by the class: iHRIS\_ISCO\_88\_Major
It has the following fields:

* name:
  + Header: Major Group
  + Type: STRING\_LINE
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_MLINE

## isco\_88\_minor

The form *isco\_88\_minor* is implemented by the class: iHRIS\_ISCO\_88\_Minor
It has the following fields:

* name:
  + Header: Minor Group
  + Type: STRING\_LINE
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_MLINE
* isco\_88\_sub\_major:
  + Header: Sub-Major Group
  + Type: MAP
  + Maps To Forms: [isco\_88\_sub\_major](#isco_88_sub_major)

## isco\_88\_sub\_major

The form *isco\_88\_sub\_major* is implemented by the class: iHRIS\_ISCO\_88\_Sub\_Major
It has the following fields:

* name:
  + Header: Sub-Major Group
  + Type: STRING\_LINE
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_MLINE
* isco\_88\_major:
  + Header: Major Group
  + Type: MAP
  + Maps To Forms: [isco\_88\_major](#isco_88_major)

## isco\_88\_unit

The form *isco\_88\_unit* is implemented by the class: iHRIS\_ISCO\_88\_Unit
It has the following fields:

* name:
  + Header: Unit
  + Type: STRING\_LINE
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_LINE
* isco\_88\_minor:
  + Header: Minor Group
  + Type: MAP
  + Maps To Forms: [isco\_88\_minor](#isco_88_minor)

## job

The form *job* is implemented by the class: iHRIS\_Job
It has the following fields:

* title:
  + Header: Title
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* code:
  + Header: Code
  + Type: STRING\_LINE
* description:
  + Header: Description
  + Type: STRING\_MLINE
* salary\_grade:
  + Header: Salary Grade
  + Type: MAP
  + Maps To Forms: [salary\_grade](#salary_grade)
* cadre:
  + Header: Cadre (Health Professionals Only)
  + Type: MAP
  + Maps To Forms: [cadre](#cadre)
* classification:
  + Header: Classification
  + Type: MAP
  + Maps To Forms: [classification](#classification)
* isco\_88\_unit:
  + Header: ISCO 88 Code
  + Type: MAP
  + Maps To Forms: [isco\_88\_unit](#isco_88_unit)

## language

The form *language* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## language\_proficiency

The form *language\_proficiency* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## marital\_status

The form *marital\_status* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## notes

The form *notes* is implemented by the class: iHRIS\_Notes
It has the following fields:

* note:
  + Header: Note
  + Type: STRING\_MLINE
  + Restrictions: Required
* date\_added:
  + Header: Date Added
  + Type: DATE\_YMD
  + Restrictions: Required

## person

The form *person* is implemented by the class: iHRIS\_ManagePerson

This form holds basic information about a person such as their names and residence

It has the child forms:

* [application](#child_form)
* [benefit](#child_form)
* [demographic](#child_form)
* [education](#child_form)
* [employment](#child_form)
* [notes](#child_form)
* [person\_competency](#child_form)
* [person\_contact\_emergency](#child_form)
* [person\_contact\_other](#child_form)
* [person\_contact\_personal](#child_form)
* [person\_contact\_work](#child_form)
* [person\_id](#child_form)
* [person\_language](#child_form)
* [person\_photo\_passport](#child_form)
* [person\_position](#child_form)
* [person\_resume](#child_form)
* [person\_scheduled\_training\_course](#child_form)
* [position\_decision](#child_form)
* [position\_interview](#child_form)
* [registration](#child_form)

It has the following fields:

* nationality:
  + Header: Nationality
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [country](#country)
* residence:
  + Header: Residence
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [county](#county),[district](#district)
* surname:
  + Header: Surname
  + Type: STRING\_LINE
  + Restrictions: Required
* firstname:
  + Header: First Name
  + Type: STRING\_LINE
  + Restrictions: Required
* othername:
  + Header: Other Names
  + Type: STRING\_LINE

## person\_competency

The form *person\_competency* is implemented by the class: iHRIS\_PersonCompetency
It has the following fields:

* evaluation\_date:
  + Header: Last Evaluated
  + Type: DATE\_YMD
* competency\_evaluation:
  + Header: Evaluation
  + Type: MAP
  + Maps To Forms: [competency\_evaluation](#competency_evaluation)
* competency:
  + Header: Competency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [competency](#competency)

## person\_contact\_emergency

The form *person\_contact\_emergency* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## person\_contact\_other

The form *person\_contact\_other* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## person\_contact\_personal

The form *person\_contact\_personal* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## person\_contact\_work

The form *person\_contact\_work* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## person\_id

The form *person\_id* is implemented by the class: iHRIS\_PersonID

This form holds basic information about an identification for a person

It has the following fields:

* id\_type:
  + Header: Identification Type
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [id\_type](#id_type)
* id\_num:
  + Header: Identification Number
  + Type: STRING\_LINE
  + Restrictions: Required

## person\_language

The form *person\_language* is implemented by the class: iHRIS\_PersonLanguage
It has the following fields:

* speaking:
  + Header: Speaking Proficiency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [language\_proficiency](#language_proficiency)
* reading:
  + Header: Reading Proficiency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [language\_proficiency](#language_proficiency)
* writing:
  + Header: Writing Proficiency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [language\_proficiency](#language_proficiency)
* language:
  + Header: Language
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [language](#language)

## person\_photo\_passport

The form *person\_photo\_passport* is implemented by the class: iHRIS\_Photo
It has the following fields:

* image:
  + Header: Image
  + Type: IMAGE
* date:
  + Header: Date
  + Type: DATE\_YMD
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_LINE

## person\_position

The form *person\_position* is implemented by the class: iHRIS\_PersonPosition

This form is used to link a person to a pariticular position residence

It has the child forms:

* [salary](#child_form)

It has the following fields:

* reason:
  + Header: Reason for Departure
  + Type: MAP
  + Maps To Forms: [pos\_change\_reason](#pos_change_reason)
* position:
  + Header: Position
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [position](#position)
* start\_date:
  + Header: Start Date
  + Type: DATE\_YMD
  + Restrictions: Required
* end\_date:
  + Header: End Date
  + Type: DATE\_YMD

## person\_resume

The form *person\_resume* is implemented by the class: iHRIS\_Document
It has the following fields:

* document:
  + Header: Document
  + Type: DOCUMENT
* date:
  + Header: Date
  + Type: DATE\_YMD
  + Restrictions: Required
* description:
  + Header: Description
  + Type: STRING\_LINE

## person\_scheduled\_training\_course

The form *person\_scheduled\_training\_course* is implemented by the class: iHRIS\_Person\_Scheduled\_Training\_Course
It has the child forms:

* [training\_course\_competency\_evaluation](#child_form)

It has the following fields:

* is\_retraining:
  + Header: Retraining
  + Type: YESNO
* completed:
  + Header: Completed
  + Type: YESNO
* request\_date:
  + Header: Request Date
  + Type: DATE\_YMD
  + Restrictions: Required
* notes:
  + Header: Notes
  + Type: STRING\_MLINE
* training\_course\_evaluation:
  + Header: Evaluation
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [training\_course\_evaluation](#training_course_evaluation)
* training\_course\_requestor:
  + Header: Requested By
  + Type: MAP
  + Maps To Forms: [training\_course\_requestor](#training_course_requestor)
* scheduled\_training\_course:
  + Header: Instance
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [scheduled\_training\_course](#scheduled_training_course)

## pos\_change\_reason

The form *pos\_change\_reason* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## position

The form *position* is implemented by the class: iHRIS\_Position
It has the following fields:

* source:
  + Header: Source
  + Type: MAP\_MULT
  + Maps To Forms: [salary\_source](#salary_source)
* supervisor:
  + Header: Supervisor
  + Type: MAP
  + Maps To Forms: [position](#position)
* pos\_type:
  + Header: Position Type
  + Type: MAP
  + Maps To Forms: [position\_type](#position_type)
* status:
  + Header: Status
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [position\_status](#position_status)
* code:
  + Header: Position Code
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* job:
  + Header: Job
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [job](#job)
* title:
  + Header: Position Title
  + Type: STRING\_LINE
  + Restrictions: Required
* description:
  + Header: Position Description
  + Type: STRING\_MLINE
* proposed\_salary:
  + Header: Proposed Salary
  + Type: CURRENCY
  + Maps To Forms: [currency](#currency)
* facility:
  + Header: Facility
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [facility](#facility)
* department:
  + Header: Department
  + Type: MAP
  + Maps To Forms: [department](#department)
* proposed\_end\_date:
  + Header: Proposed End Date
  + Type: DATE\_YMD
* proposed\_hiring\_date:
  + Header: Proposed Hiring Date
  + Type: DATE\_YMD
* posted\_date:
  + Header: Date Posted
  + Type: DATE\_YMD
* comments:
  + Header: Position Comments
  + Type: STRING\_TEXT
* interview\_comments:
  + Header: Interview Comments
  + Type: STRING\_TEXT

## position\_decision

The form *position\_decision* is implemented by the class: iHRIS\_PositionDecision
It has the following fields:

* date:
  + Header: Date of Decision
  + Type: DATE\_YMD
  + Restrictions: Required
* offer:
  + Header: Make a Job Offer?
  + Type: YESNO
* comments:
  + Header: Comments
  + Type: STRING\_MLINE

## position\_interview

The form *position\_interview* is implemented by the class: iHRIS\_PositionInterview
It has the following fields:

* date:
  + Header: Date of Interview
  + Type: DATE\_YMD
  + Restrictions: Required
* person:
  + Header: People Attending
  + Type: STRING\_LINE
  + Restrictions: Required
* comments:
  + Header: Comments
  + Type: STRING\_MLINE

## position\_status

The form *position\_status* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## position\_type

The form *position\_type* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## region

The form *region* is implemented by the class: iHRIS\_Region
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique in {country}
* country:
  + Header: Country
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [country](#country)
* code:
  + Header: Code
  + Type: STRING\_LINE

## registration

The form *registration* is implemented by the class: iHRIS\_Registration
It has the following fields:

* council:
  + Header: Registration Council
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [council](#council)
* registration\_number:
  + Header: Registration Number
  + Type: STRING\_LINE
* license\_number:
  + Header: License Number
  + Type: STRING\_LINE
* registration\_date:
  + Header: Registration Date
  + Type: DATE\_YMD
* license\_expiration:
  + Header: License Expiration Date
  + Type: DATE\_YMD

## role

The form *role* is implemented by the class: I2CE\_Role
It has the following fields:

* trickle\_up:
  + Header: Trickle Up
  + Type: MAP\_MULT
  + Maps To Forms: [role](#role)
* name:
  + Header: Role
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* assignable:
  + Header: Can Assign To User
  + Type: YESNO
  + Restrictions: Required

## salary

The form *salary* is implemented by the class: iHRIS\_Salary
It has the following fields:

* start\_date:
  + Header: Start Date
  + Type: DATE\_YMD
  + Restrictions: Required
* salary:
  + Header: Salary
  + Type: CURRENCY
  + Restrictions: Required
  + Maps To Forms: [currency](#currency)
* end\_date:
  + Header: End Date
  + Type: DATE\_YMD
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## salary\_grade

The form *salary\_grade* is implemented by the class: iHRIS\_SalaryGrade
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* start:
  + Header: Start
  + Type: CURRENCY
  + Restrictions: Required
  + Maps To Forms: [currency](#currency)
* end:
  + Header: End
  + Type: CURRENCY
  + Restrictions: Required
  + Maps To Forms: [currency](#currency)
* midpoint:
  + Header: MidPoint
  + Type: CURRENCY
  + Maps To Forms: [currency](#currency)
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## salary\_source

The form *salary\_source* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## scheduled\_training\_course

The form *scheduled\_training\_course* is implemented by the class: iHRIS\_Scheduled\_Training\_Course
It has the following fields:

* location:
  + Header: Location
  + Type: MAP
  + Maps To Forms: [county](#county),[district](#district)
* training\_course:
  + Header: Training Course
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [training\_course](#training_course)
* name:
  + Header: Site
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* num\_students:
  + Header: Maximum Number of Students
  + Type: INT
  + Restrictions: Required
* notes:
  + Header: Notes
  + Type: STRING\_MLINE
* instructors:
  + Header: Instructors
  + Type: STRING\_MLINE
* start\_date:
  + Header: Start Date
  + Type: DATE\_YMD
  + Restrictions: Required
* end\_date:
  + Header: End Date
  + Type: DATE\_YMD
  + Restrictions: Required

## training\_course

The form *training\_course* is implemented by the class: iHRIS\_Training\_Course

This form holds basic information about a training course

It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* topic:
  + Header: Topic
  + Type: STRING\_LINE
  + Restrictions: Required
* notes:
  + Header: Notes
  + Type: STRING\_MLINE
* training\_institution:
  + Header: Training Institution
  + Type: MAP
  + Maps To Forms: [training\_institution](#training_institution)
* training\_funder:
  + Header: Training Funders
  + Type: MAP\_MULT
  + Maps To Forms: [training\_funder](#training_funder)
* continuing\_education\_course:
  + Header: CEUs Provided
  + Type: MAP\_MULT
  + Maps To Forms: [continuing\_education\_course](#continuing_education_course)
* training\_course\_status:
  + Header: Status
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [training\_course\_status](#training_course_status)
* training\_course\_category:
  + Header: Category
  + Type: MAP
  + Maps To Forms: [training\_course\_category](#training_course_category)
* competency:
  + Header: Competencies Provided
  + Type: MAP\_MULT
  + Maps To Forms: [competency](#competency)

## training\_course\_category

The form *training\_course\_category* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## training\_course\_competency\_evaluation

The form *training\_course\_competency\_evaluation* is implemented by the class: iHRIS\_Training\_Course\_Competency\_Evaluation
It has the following fields:

* notes:
  + Header: Notes
  + Type: STRING\_MLINE
* evaluation\_date:
  + Header: Evaluation Date
  + Type: DATE\_YMD
  + Restrictions: Required
* competency\_evaluation:
  + Header: Evaluation
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [competency\_evaluation](#competency_evaluation)
* competency:
  + Header: Competency
  + Type: MAP
  + Restrictions: Required
  + Maps To Forms: [competency](#competency)

## training\_course\_evaluation

The form *training\_course\_evaluation* is implemented by the class: iHRIS\_Training\_Course\_Evaluation
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique
* competency\_evaluation:
  + Header: Competency Evaluation
  + Type: MAP
  + Maps To Forms: [competency\_evaluation](#competency_evaluation)

## training\_course\_requestor

The form *training\_course\_requestor* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## training\_course\_status

The form *training\_course\_status* is implemented by the class: I2CE\_SimpleList
It has the following fields:

* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## training\_funder

The form *training\_funder* is implemented by the class: iHRIS\_ListByCountry
It has the child forms:

* [training\_funder\_contact](#child_form)

It has the following fields:

* location:
  + Header: Location
  + Type: MAP
  + Maps To Forms: [county](#county),[district](#district)
* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## training\_funder\_contact

The form *training\_funder\_contact* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## training\_institution

The form *training\_institution* is implemented by the class: iHRIS\_ListByCountry
It has the child forms:

* [training\_institution\_contact](#child_form)

It has the following fields:

* location:
  + Header: Location
  + Type: MAP
  + Maps To Forms: [county](#county),[district](#district)
* name:
  + Header: Name
  + Type: STRING\_LINE
  + Restrictions: Required, Unique

## training\_institution\_contact

The form *training\_institution\_contact* is implemented by the class: iHRIS\_Contact
It has the following fields:

* address:
  + Header: Mailing Address
  + Type: STRING\_MLINE
* telephone:
  + Header: Telephone Number
  + Type: STRING\_LINE
* alt\_telephone:
  + Header: Alternate Telephone Number
  + Type: STRING\_LINE
* fax:
  + Header: Fax Number
  + Type: STRING\_LINE
* email:
  + Header: Email Address
  + Type: STRING\_LINE
* notes:
  + Header: Notes
  + Type: STRING\_MLINE

## user

The form *user* is implemented by the class: I2CE\_User\_Form
It has the following fields:

* username:
  + Header: Username
  + Type: STRING\_LINE
  + Restrictions: Required
* password:
  + Header: Password (leave blank to keep the same password)
  + Type: STRING\_PASS
* firstname:
  + Header: First Name
  + Type: STRING\_LINE
  + Restrictions: Required
* lastname:
  + Header: Surname
  + Type: STRING\_LINE
  + Restrictions: Required
* email:
  + Header: Email
  + Type: STRING\_LINE
* role:
  + Header: Role
  + Type: MAP
  + Maps To Forms: [role](#role)
* creator:
  + Header:
  + Type: INT
