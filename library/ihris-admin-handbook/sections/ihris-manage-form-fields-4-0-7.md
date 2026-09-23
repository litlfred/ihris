---
title: "IHRIS Manage Form Fields - 4.0.7"
source: http://open.intrahealth.org/w/index.php?oldid=34902
contributors: ["Litlfred"]
pages: 223-273
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Manage Form Fields - 4.0.7

These are the forms and fields in iHRIS Manage version 4.0.7

There is also a graphical visualization \[1\] of this data. Warning: this is a very large file and you may wish to save it to your desktop instead of viewing it in your browser.

Here is a description of the Field types.

## accident

The form accident is implemented by the class: iHRIS\_Accident It has the following fields:

- accident\_type:

- Header: Accident Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: accident\_type
- end\_date:

- Header: End of Applicability
- Type: DATE\_YMD
- followup:

- Header: Follow-up Required
- Type: STRING\_MLINE
- occurence\_date:

- Header: Date of Occurence
- Type: DATE\_YMD
- persons\_involved:

- Header: People Involved
- Type: STRING\_MLINE
- start\_date:

- Header: Start of Applicability
- Type: DATE\_YMD
- Restrictions: Required

## accident\_type

The form accident\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## application

The form application is implemented by the class: iHRIS\_Applicant It has the following fields:

- desired\_wage:

- Header: Desired Wage
- Type: CURRENCY
- Maps To Forms: currency
- felony:

- Header: Have you ever been convicted of a felony?
- Type: YESNO
- felony\_circumstance:

- Header: If yes, give the circumstances.
- Type: STRING\_MLINE
- full\_time:

- Header: Are you looking for full-time employment?
- Type: YESNO
- hear:

- Header: How did you hear of this opening?
- Type: STRING\_MLINE
- hours:

- Header: If no, what hours are you available?
- Type: STRING\_MLINE
- other\_info:

- Header: In addition to your work history, are there other skills, qualifications or experience we should consider?
- Type: STRING\_MLINE
- position:

- Header: Position(s)
- Type: MAP\_MULT
- Restrictions: Required
- Maps To Forms: position
- start\_date:

- Header: When can you start?
- Type: DATE\_YMD

## archived\_report

The form archived\_report is implemented by the class: I2CE\_ArchivedReport It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- date:

- Header: Generation Date
- Type: DATE\_YMD
- Restrictions: Required
- name:

- Header: Title
- Type: STRING\_LINE
- Restrictions: Required
- report:

- Header: Report
- Type: DOCUMENT
- report\_view:

- Header: Report View
- Type: STRING\_LINE
- Restrictions: Unique in {date}

## benefit

The form benefit is implemented by the class: iHRIS\_Benefit It has the following fields:

- amount:

- Header: Amount
- Type: CURRENCY
- Restrictions: Required
- Maps To Forms: currency
- end\_date:

- Header: End Date
- Type: DATE\_YMD
- recurrence:

- Header: Recurrence Frequency
- Type: MAP
- Restrictions: Required
- Maps To Forms: benefit\_recurrence
- source:

- Header: Source
- Type: MAP
- Restrictions: Required
- Maps To Forms: salary\_source
- start\_date:

- Header: Start Date
- Type: DATE\_YMD

- Restrictions: Required
- type:

- Header: Benefit Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: benefit\_type

## benefit\_recurrence

The form benefit\_recurrence is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## benefit\_type

The form benefit\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cadre

The form cadre is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_asource

The form cl\_asource is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_cstype

The form cl\_cstype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_currency

The form cl\_currency is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_day

The form cl\_day is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_disagg

The form cl\_disagg is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_disease

The form cl\_disease is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_disstat

The form cl\_disstat is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_dsource

The form cl\_dsource is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_dstype

The form cl\_dstype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_dtype

The form cl\_dtype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_fperiod

The form cl\_fperiod is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_gboundary\_type

The form cl\_gboundary\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_gcode\_country

The form cl\_gcode\_country is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_gender

The form cl\_gender is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_glevel

The form cl\_glevel is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_glocation

The form cl\_glocation is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_hif1

The form cl\_hif1 is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_hif2

The form cl\_hif2 is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_income

The form cl\_income is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_logical

The form cl\_logical is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_metype

The form cl\_metype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_month

The form cl\_month is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_mult

The form cl\_mult is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_operand

The form cl\_operand is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_orphan

The form cl\_orphan is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_otype

The form cl\_otype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_periodicity

The form cl\_periodicity is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_preg

The form cl\_preg is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_pstatus

The form cl\_pstatus is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_ptype

The form cl\_ptype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_quarter

The form cl\_quarter is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_race

The form cl\_race is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_sector

The form cl\_sector is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_sex

The form cl\_sex is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_special\_value

The form cl\_special\_value is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_stype

The form cl\_stype is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_tpop

The form cl\_tpop is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_unit

The form cl\_unit is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_value\_type

The form cl\_value\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_vstatus

The form cl\_vstatus is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_vulnstat

The form cl\_vulnstat is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_week

The form cl\_week is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## cl\_year

The form cl\_year is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## classification

The form classification is implemented by the class: iHRIS\_Classification It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- code:

- Header: Code
- Type: STRING\_LINE
- description:

- Header: Description

- Type: STRING\_LINE
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## competency

The form competency is implemented by the class: iHRIS\_Competency It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- competency\_type:

- Header: Competency Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: competency\_type
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {competency\_type}
- notes:

- Header: Notes
- Type: STRING\_MLINE

## competency\_evaluation

The form competency\_evaluation is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## competency\_type

The form competency\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## confirmation

The form confirmation is implemented by the class: iHRIS\_Confirmation It has the following fields:

- confirmation\_type:

- Header: Confirmation Type
- Type: MAP
- Restrictions: Required, Unique in {parent}
- Maps To Forms: confirmation\_type
- date:

- Header: Date
- Type: DATE\_YMD
- Restrictions: Required
- record:

- Header: Record
- Type: DOCUMENT
- valid:

- Header: Valid
- Type: YESNO
- Restrictions: Required

## confirmation\_type

The form confirmation\_type is implemented by the class: iHRIS\_ConfirmationType It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- job:

- Header: Associated Job
- Type: MAP
- Maps To Forms: job
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {job}
- probation\_period:

- Header: Probationary Period (Months)
- Type: INT
- Restrictions: Required

## continuing\_education

The form continuing\_education is implemented by the class: iHRIS\_ContinuingEducation It has the following fields:

- continuing\_education\_course:

- Header: Continuing Education Course
- Type: MAP
- Restrictions: Required
- Maps To Forms: continuing\_education\_course
- credit\_hours:

- Header: Credit Hours
- Type: INT
- Restrictions: Required
- end\_date:

- Header: End Date
- Type: DATE\_YMD
- Restrictions: Required
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required

## continuing\_education\_course

The form continuing\_education\_course is implemented by the class: iHRIS\_ContinuingEducationCourse It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- credit\_hours:

- Header: Credit Hours
- Type: INT
- Restrictions: Required
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required

## council

The form council is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## country

The form country is implemented by the class: iHRIS\_Country It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- alpha\_two:

- Header: 2 Character Alpha Code
- Type: STRING\_LINE
- Restrictions: Required, Unique
- code:

- Header: ISO Numeric Code
- Type: INT
- location:

- Header: Use for Location Selection
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique
- primary:

- Header: Primary Country
- Type: YESNO

## county

The form county is implemented by the class: iHRIS\_County It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- district:

- Header: District
- Type: MAP

- Restrictions: Required
- Maps To Forms: district

- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {district}

## currency

The form currency is implemented by the class: iHRIS\_Currency It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- code:

- Header: Currency Code
- Type: STRING\_LINE
- Restrictions: Required, Unique
- country:

- Header: Country
- Type: MAP
- Maps To Forms: country
- name:

- Header: Name
- Type: STRING\_LINE
- symbol:

- Header: Symbol
- Type: STRING\_LINE

## degree

The form degree is implemented by the class: iHRIS\_Degree It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- edu\_type:

- Header: Education Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: edu\_type
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {edu\_type}

## demographic

The form demographic is implemented by the class: iHRIS\_ManageDemographic It has the following fields:

- birth\_date:

- Header: Date of Birth
- Type: DATE\_YMD
- gender:

- Header: Gender
- Type: MAP
- Maps To Forms: gender
- marital\_status:

- Header: Marital Status
- Type: MAP
- Maps To Forms: marital\_status
- dependents:

- Header: Number of Dependents
- Type: INT

## department

The form department is implemented by the class: iHRIS\_Department It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## dependent

The form dependent is implemented by the class: iHRIS\_Dependent It has the following fields:

- date\_of\_birth:

- Header: Date of Birth
- Type: DATE\_YMD
- gender:

- Header: Gender
- Type: MAP
- Maps To Forms: gender
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required

## disciplinary\_action

The form disciplinary\_action is implemented by the class: iHRIS\_DisciplinaryAction It has the following fields:

- action\_date:

- Header: Date of Discussion
- Type: DATE\_YMD
- disciplinary\_action\_type:

- Header: Action Taken
- Type: MAP
- Restrictions: Required
- Maps To Forms: disciplinary\_action\_type
- end\_date:

- Header: End of Applicability
- Type: DATE\_YMD
- notes:

- Header: Notes
- Type: STRING\_MLINE
- persons\_present:

- Header: People Present
- Type: STRING\_MLINE
- start\_date:

- Header: Start of Applicability
- Type: DATE\_YMD
- Restrictions: Required

## disciplinary\_action\_type

The form disciplinary\_action\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## district

The form district is implemented by the class: iHRIS\_District It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- code:

- Header: Code

- Type: STRING\_LINE
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {region:country}
- region:

- Header: Region
- Type: MAP
- Restrictions: Required
- Maps To Forms: region

## edu\_type

The form edu\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## education

The form education is implemented by the class: iHRIS\_Education It has the following fields:

- degree:

- Header: Degree
- Type: MAP
- Restrictions: Required
- Maps To Forms: degree
- institution:

- Header: Institution Name
- Type: STRING\_LINE
- Restrictions: Required
- location:

- Header: Institution Location
- Type: STRING\_LINE
- major:

- Header: Major
- Type: STRING\_LINE
- year:

- Header: Year of Graduation (leave blank if In Progress)
- Type: DATE\_Y

## employment

The form employment is implemented by the class: iHRIS\_Employment It has the following fields:

- company\_address:

- Header: Company Address
- Type: STRING\_MLINE
- company\_name:

- Header: Company Name
- Type: STRING\_LINE
- Restrictions: Required
- company\_phone:

- Header: Company Telephone
- Type: STRING\_LINE
- contact\_ok:

- Header: Ok to Contact?
- Type: YESNO
- end\_date:

- Header: Date Ended (leave blank if still employed)
- Type: DATE\_YMD
- end\_position:

- Header: Ending Position
- Type: STRING\_LINE
- end\_wage:

- Header: Ending Wage
- Type: CURRENCY
- Maps To Forms: currency
- reason\_for\_leaving:

- Header: Reason for Leaving
- Type: STRING\_MLINE
- responsibilities:

- Header: Job Responsibilities
- Type: STRING\_MLINE
- start\_date:

- Header: Date Started
- Type: DATE\_YMD
- Restrictions: Required
- start\_position:

- Header: Starting Position
- Type: STRING\_LINE
- start\_wage:

- Header: Starting Wage
- Type: CURRENCY
- Maps To Forms: currency

- supervisor:

- Header: Supervisor

- Type: STRING\_LINE

## establishment

The form establishment is implemented by the class: iHRIS\_Establishment It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- amount:

- Header: Number of Health Workers
- Type: INT
- Restrictions: Required
- establishment\_period:

- Header: Establishment Period
- Type: MAP
- Restrictions: Required, Unique in {job\_cadre,location}
- Maps To Forms: establishment\_period
- job\_cadre:

- Header: Job or Cadre
- Type: MAP
- Restrictions: Required
- Maps To Forms: cadre,job
- location:

- Header: Facility or Faciltiy Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility,facility\_type

## establishment\_period

The form establishment\_period is implemented by the class: iHRIS\_EstablishmentPeriod It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- establishment\_type:

- Header: Establishment Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: establishment\_type
- year:

- Header: Year of Applicability
- Type: DATE\_Y
- Restrictions: Required, Unique in {establishment\_type}

## establishment\_type

The form establishment\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## facility

The form facility is implemented by the class: iHRIS\_Facility

This form is used to descibe basic information about a facility

It has the child forms:

- facility\_contact

It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- location:

- Header: Location
- Type: MAP
- Maps To Forms: county,district
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique
- facility\_type:

- Header: Facility Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility\_type

## facility\_contact

The form facility\_contact is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address

- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number

- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## facility\_type

The form facility\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## gender

The form gender is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## generated\_doc

The form generated\_doc is implemented by the class: I2CE\_GeneratedDoc It has the following fields:

- date:

- Header: Date
- Type: DATE\_YMD
- Restrictions: Required
- description:

- Header: Description
- Type: STRING\_LINE
- document:

- Header: Document
- Type: DOCUMENT
- primary\_form:

- Header: Primary Form ID
- Type: STRING\_LINE

## id\_type

The form id\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## isco\_88\_major

The form isco\_88\_major is implemented by the class: iHRIS\_ISCO\_88\_Major It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- description:

- Header: Description
- Type: STRING\_MLINE
- name:

- Header: Major Group
- Type: STRING\_LINE
- Restrictions: Required

## isco\_88\_minor

The form isco\_88\_minor is implemented by the class: iHRIS\_ISCO\_88\_Minor It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- description:

- Header: Description
- Type: STRING\_MLINE
- isco\_88\_sub\_major:

- Header: Sub-Major Group
- Type: MAP
- Maps To Forms: isco\_88\_sub\_major
- name:

- Header: Minor Group
- Type: STRING\_LINE
- Restrictions: Required

## isco\_88\_sub\_major

The form isco\_88\_sub\_major is implemented by the class: iHRIS\_ISCO\_88\_Sub\_Major It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- description:

- Header: Description
- Type: STRING\_MLINE
- isco\_88\_major:

- Header: Major Group
- Type: MAP
- Maps To Forms: isco\_88\_major
- name:

- Header: Sub-Major Group
- Type: STRING\_LINE
- Restrictions: Required

## isco\_88\_unit

The form isco\_88\_unit is implemented by the class: iHRIS\_ISCO\_88\_Unit It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- description:

- Header: Description

- Type: STRING\_LINE
- isco\_88\_minor:

- Header: Minor Group
- Type: MAP
- Maps To Forms: isco\_88\_minor
- name:

- Header: Unit
- Type: STRING\_LINE
- Restrictions: Required

## job

The form job is implemented by the class: iHRIS\_ManageJob It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- cadre:

- Header: Cadre (Health Professionals Only)
- Type: MAP
- Maps To Forms: cadre
- classification:

- Header: Classification
- Type: MAP
- Maps To Forms: classification
- code:

- Header: Code
- Type: STRING\_LINE
- description:

- Header: Description
- Type: STRING\_MLINE
- isco\_88\_unit:

- Header: ISCO 88 Code
- Type: MAP
- Maps To Forms: isco\_88\_unit
- title:

- Header: Title
- Type: STRING\_LINE
- Restrictions: Required, Unique
- salary\_grade:

- Header: Salary Grade
- Type: MAP
- Maps To Forms: salary\_grade

## language

The form language is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## language\_proficiency

The form language\_proficiency is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## marital\_status

The form marital\_status is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## nextofkin

The form nextofkin is implemented by the class: iHRIS\_NextOfKin It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number

- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required
- relationship:

- Header: Relationship
- Type: STRING\_LINE
- Restrictions: Required

## notes

The form notes is implemented by the class: iHRIS\_Notes It has the following fields:

- date\_added:

- Header: Date Added
- Type: DATE\_YMD
- Restrictions: Required
- note:

- Header: Note
- Type: STRING\_MLINE
- Restrictions: Required

## person

The form person is implemented by the class: iHRIS\_ManagePerson

This form holds basic information about a person such as their names and residence

It has the child forms:

- accident
- application
- benefit
- confirmation
- demographic
- dependent
- disciplinary\_action

- education
- employment

- nextofkin
- notes
- person\_archive\_scan
- person\_competency
- person\_contact\_emergency
- person\_contact\_other
- person\_contact\_personal
- person\_contact\_work
- person\_id
- person\_language
- person\_photo\_passport
- person\_position
- person\_resume
- person\_scheduled\_training\_course
- position\_decision
- position\_interview
- registration

It has the following fields:

- firstname:

- Header: First Name
- Type: STRING\_LINE
- Restrictions: Required
- nationality:

- Header: Nationality
- Type: MAP
- Restrictions: Required
- Maps To Forms: country
- othername:

- Header: Other Names
- Type: STRING\_LINE
- residence:

- Header: Residence
- Type: MAP
- Restrictions: Required
- Maps To Forms: county,district
- surname:

- Header: Surname
- Type: STRING\_LINE
- Restrictions: Required

## person\_archive\_scan

The form person\_archive\_scan is implemented by the class: iHRIS\_Photo It has the following fields:

- date:

- Header: Date
- Type: DATE\_YMD
- Restrictions: Required
- description:

- Header: Description
- Type: STRING\_LINE
- image:

- Header: Image
- Type: IMAGE

## person\_competency

The form person\_competency is implemented by the class: iHRIS\_PersonCompetency It has the following fields:

- competency:

- Header: Competency
- Type: MAP
- Restrictions: Required, Unique in {parent}
- Maps To Forms: competency
- competency\_evaluation:

- Header: Evaluation
- Type: MAP
- Maps To Forms: competency\_evaluation
- evaluation\_date:

- Header: Last Evaluated
- Type: DATE\_YMD

## person\_contact\_emergency

The form person\_contact\_emergency is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number
- Type: STRING\_LINE
- email:

- Header: Email Address

- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## person\_contact\_other

The form person\_contact\_other is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number
- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## person\_contact\_personal

The form person\_contact\_personal is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE

- alt\_telephone:

- Header: Alternate Telephone Number

- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## person\_contact\_work

The form person\_contact\_work is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number
- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## person\_id

The form person\_id is implemented by the class: iHRIS\_PersonID

This form holds basic information about an identification for a person

It has the following fields:

- id\_num:

- Header: Identification Number
- Type: STRING\_LINE
- Restrictions: Required
- id\_type:

- Header: Identification Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: id\_type

## person\_language

The form person\_language is implemented by the class: iHRIS\_PersonLanguage It has the following fields:

- language:

- Header: Language
- Type: MAP
- Restrictions: Required
- Maps To Forms: language
- reading:

- Header: Reading Proficiency
- Type: MAP
- Restrictions: Required
- Maps To Forms: language\_proficiency
- speaking:

- Header: Speaking Proficiency
- Type: MAP
- Restrictions: Required
- Maps To Forms: language\_proficiency
- writing:

- Header: Writing Proficiency
- Type: MAP
- Restrictions: Required
- Maps To Forms: language\_proficiency

## person\_photo\_passport

The form person\_photo\_passport is implemented by the class: iHRIS\_Photo It has the following fields:

- date:

- Header: Date
- Type: DATE\_YMD
- Restrictions: Required
- description:

- Header: Description
- Type: STRING\_LINE
- image:

- Header: Image
- Type: IMAGE

## person\_position

The form person\_position is implemented by the class: iHRIS\_PersonPosition

This form is used to link a person to a pariticular position residence

It has the child forms:

- salary

It has the following fields:

- end\_date:

- Header: End Date
- Type: DATE\_YMD
- position:

- Header: Position
- Type: MAP
- Restrictions: Required
- Maps To Forms: position
- reason:

- Header: Reason for Departure
- Type: MAP
- Maps To Forms: pos\_change\_reason
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required

## person\_resume

The form person\_resume is implemented by the class: iHRIS\_Document It has the following fields:

- date:

- Header: Date
- Type: DATE\_YMD
- Restrictions: Required
- description:

- Header: Description
- Type: STRING\_LINE
- document:

- Header: Document
- Type: DOCUMENT

## person\_scheduled\_training\_course

The form person\_scheduled\_training\_course is implemented by the class: iHRIS\_Person\_Scheduled\_Training\_Course It has the child forms:

- training\_course\_competency\_evaluation

It has the following fields:

- completed:

- Header: Completed
- Type: YESNO
- is\_retraining:

- Header: Retraining
- Type: YESNO
- notes:

- Header: Notes
- Type: STRING\_MLINE
- request\_date:

- Header: Request Date
- Type: DATE\_YMD
- Restrictions: Required
- scheduled\_training\_course:

- Header: Instance
- Type: MAP
- Restrictions: Required
- Maps To Forms: scheduled\_training\_course
- training\_course\_evaluation:

- Header: Evaluation
- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_course\_evaluation

- training\_course\_requestor:

- Header: Requested By

- Type: MAP
- Maps To Forms: training\_course\_requestor

## pos\_change\_reason

The form pos\_change\_reason is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## position

The form position is implemented by the class: iHRIS\_Position It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- code:

- Header: Position Code
- Type: STRING\_LINE
- Restrictions: Required, Unique
- comments:

- Header: Position Comments
- Type: STRING\_TEXT
- department:

- Header: Department
- Type: MAP
- Maps To Forms: department
- description:

- Header: Position Description
- Type: STRING\_MLINE
- facility:

- Header: Facility
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility
- interview\_comments:

- Header: Interview Comments
- Type: STRING\_TEXT
- job:

- Header: Job
- Type: MAP
- Restrictions: Required

- Maps To Forms: job
- posted\_date:

- Header: Date Posted
- Type: DATE\_YMD
- pos\_type:

- Header: Position Type
- Type: MAP
- Maps To Forms: position\_type
- proposed\_end\_date:

- Header: Proposed End Date
- Type: DATE\_YMD
- proposed\_hiring\_date:

- Header: Proposed Hiring Date
- Type: DATE\_YMD
- proposed\_salary:

- Header: Proposed Salary
- Type: CURRENCY
- Maps To Forms: currency
- source:

- Header: Source
- Type: MAP\_MULT
- Maps To Forms: salary\_source
- status:

- Header: Status
- Type: MAP
- Restrictions: Required
- Maps To Forms: position\_status
- supervisor:

- Header: Supervisor
- Type: MAP
- Maps To Forms: position
- title:

- Header: Position Title
- Type: STRING\_LINE
- Restrictions: Required

## position\_decision

The form position\_decision is implemented by the class: iHRIS\_PositionDecision It has the following fields:

- comments:

- Header: Comments
- Type: STRING\_MLINE
- date:

- Header: Date of Decision
- Type: DATE\_YMD
- Restrictions: Required
- offer:

- Header: Make a Job Offer?
- Type: YESNO
- record:

- Header: Record of Decision
- Type: DOCUMENT

## position\_interview

The form position\_interview is implemented by the class: iHRIS\_PositionInterview It has the following fields:

- comments:

- Header: Comments
- Type: STRING\_MLINE
- date:

- Header: Date of Interview
- Type: DATE\_YMD
- Restrictions: Required
- person:

- Header: People Attending
- Type: STRING\_LINE
- Restrictions: Required
- record:

- Header: Interview Record
- Type: DOCUMENT

## position\_status

The form position\_status is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE

- Restrictions: Required, Unique

## position\_type

The form position\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## region

The form region is implemented by the class: iHRIS\_Region It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- code:

- Header: Code
- Type: STRING\_LINE
- country:

- Header: Country
- Type: MAP
- Restrictions: Required
- Maps To Forms: country
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {country}

## registration

The form registration is implemented by the class: iHRIS\_Registration It has the following fields:

- council:

- Header: Registration Council
- Type: MAP
- Restrictions: Required
- Maps To Forms: council
- license\_expiration:

- Header: License Expiration Date
- Type: DATE\_YMD
- license\_number:

- Header: License Number
- Type: STRING\_LINE

- registration\_date:

- Header: Registration Date

- Type: DATE\_YMD
- registration\_number:

- Header: Registration Number
- Type: STRING\_LINE

## salary

The form salary is implemented by the class: iHRIS\_Salary It has the following fields:

- end\_date:

- Header: End Date
- Type: DATE\_YMD
- notes:

- Header: Notes
- Type: STRING\_MLINE
- salary:

- Header: Salary
- Type: CURRENCY
- Restrictions: Required
- Maps To Forms: currency
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required

## salary\_grade

The form salary\_grade is implemented by the class: iHRIS\_SalaryGrade It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- end:

- Header: End
- Type: CURRENCY
- Restrictions: Required
- Maps To Forms: currency
- midpoint:

- Header: MidPoint
- Type: CURRENCY
- Maps To Forms: currency
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique
- notes:

- Header: Notes
- Type: STRING\_MLINE

- start:

- Header: Start
- Type: CURRENCY
- Restrictions: Required
- Maps To Forms: currency

## salary\_source

The form salary\_source is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## scheduled\_training\_course

The form scheduled\_training\_course is implemented by the class: iHRIS\_Scheduled\_Training\_Course It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- end\_date:

- Header: End Date
- Type: DATE\_YMD
- Restrictions: Required
- instructors:

- Header: Instructors
- Type: STRING\_MLINE
- location:

- Header: Location
- Type: MAP
- Maps To Forms: county,district
- name:

- Header: Site
- Type: STRING\_LINE
- Restrictions: Required, Unique
- notes:

- Header: Notes
- Type: STRING\_MLINE
- num\_students:

- Header: Maximum Number of Students
- Type: INT
- Restrictions: Required

- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required
- training\_course:

- Header: Training Course
- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_course

## training\_course

The form training\_course is implemented by the class: iHRIS\_Training\_Course

This form holds basic information about a training course

It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- competency:

- Header: Competencies Provided
- Type: MAP\_MULT
- Maps To Forms: competency
- continuing\_education\_course:

- Header: CEUs Provided
- Type: MAP\_MULT
- Maps To Forms: continuing\_education\_course
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique
- notes:

- Header: Notes
- Type: STRING\_MLINE
- topic:

- Header: Topic
- Type: STRING\_LINE
- Restrictions: Required
- training\_course\_category:

- Header: Category
- Type: MAP
- Maps To Forms: training\_course\_category
- training\_course\_status:

- Header: Status

- Type: MAP
- Restrictions: Required

- Maps To Forms: training\_course\_status
- training\_funder:

- Header: Training Funders
- Type: MAP\_MULT
- Maps To Forms: training\_funder
- training\_institution:

- Header: Training Institution
- Type: MAP
- Maps To Forms: training\_institution

## training\_course\_category

The form training\_course\_category is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_course\_competency\_evaluation

The form training\_course\_competency\_evaluation is implemented by the class: iHRIS\_Training\_Course\_Competency\_Evaluation It has the following fields:

- competency:

- Header: Competency
- Type: MAP
- Restrictions: Required
- Maps To Forms: competency
- competency\_evaluation:

- Header: Evaluation
- Type: MAP
- Restrictions: Required
- Maps To Forms: competency\_evaluation
- evaluation\_date:

- Header: Evaluation Date
- Type: DATE\_YMD
- Restrictions: Required
- notes:

- Header: Notes
- Type: STRING\_MLINE

## training\_course\_evaluation

The form training\_course\_evaluation is implemented by the class: iHRIS\_Training\_Course\_Evaluation It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- competency\_evaluation:

- Header: Competency Evaluation
- Type: MAP
- Maps To Forms: competency\_evaluation
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_course\_requestor

The form training\_course\_requestor is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_course\_status

The form training\_course\_status is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_funder

The form training\_funder is implemented by the class: iHRIS\_ListByCountry It has the child forms:

- training\_funder\_contact

It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- location:

- Header: Location
- Type: MAP
- Maps To Forms: county,district
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_funder\_contact

The form training\_funder\_contact is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number
- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## training\_institution

The form training\_institution is implemented by the class: iHRIS\_ListByCountry It has the child forms:

- training\_institution\_contact

It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- location:

- Header: Location
- Type: MAP
- Maps To Forms: county,district
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_institution\_contact

The form training\_institution\_contact is implemented by the class: iHRIS\_Contact It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- address:

- Header: Mailing Address
- Type: STRING\_MLINE
- alt\_telephone:

- Header: Alternate Telephone Number
- Type: STRING\_LINE
- email:

- Header: Email Address
- Type: STRING\_LINE
- fax:

- Header: Fax Number
- Type: STRING\_LINE
- notes:

- Header: Notes
- Type: STRING\_MLINE
- telephone:

- Header: Telephone Number
- Type: STRING\_LINE

## References

\[1\] http://open.intrahealth.org/visualizations/forms-ihris-manage-site-demo\_4\_0\_7.gif
