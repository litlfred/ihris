---
title: "IHRIS Qualify Form Fields"
source: http://open.intrahealth.org/w/index.php?oldid=34896
contributors: ["Litlfred"]
pages: 297-324
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Qualify Form Fields

These are the forms and fields in iHRIS Qualify version 4.0.7

There is also a graphical visualization \[1\] of this data. Warning: this is a very large file and you may wish to save it to your desktop instead of viewing it in your browser.

Here is a description of the Field types.

## academic\_level

The form academic\_level is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

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

## cadre

The form cadre is implemented by the class: iHRIS\_Cadre It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- isco:

- Header: ISCO Classification Code
- Type: STRING\_LINE
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique
- qualification:

- Header: Minimum Qualification Required
- Type: MAP
- Restrictions: Required
- Maps To Forms: qualification

## certificate

The form certificate is implemented by the class: iHRIS\_Certificate It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- academic\_level:

- Header: Academic Level
- Type: MAP
- Restrictions: Required
- Maps To Forms: academic\_level
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {academic\_level}

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

The form demographic is implemented by the class: iHRIS\_QualifyDemographic It has the following fields:

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
- birth\_location:

- Header: Birth Location
- Type: MAP
- Maps To Forms: county,district

## deployment

The form deployment is implemented by the class: iHRIS\_Deployment It has the following fields:

- deployment\_date:

- Header: Deployment Date
- Type: DATE\_YMD
- Restrictions: Required
- health\_facility:

- Header: Health Facility
- Type: MAP
- Restrictions: Required
- Maps To Forms: health\_facility
- job\_code:

- Header: Job/Post Code
- Type: STRING\_LINE
- job\_title:

- Header: Job/Post Title
- Type: STRING\_LINE

## disciplinary\_action

The form disciplinary\_action is implemented by the class: iHRIS\_DisciplinaryAction It has the following fields:

- action\_date:

- Header: Date Disciplinary Action Occurred
- Type: DATE\_YMD
- Restrictions: Required
- disciplinary\_action\_reason:

- Header: Disciplinary Action Reason
- Type: MAP
- Restrictions: Required
- Maps To Forms: disciplinary\_action\_reason
- notes:

- Header: Notes
- Type: STRING\_TEXT
- reinstate\_date:

- Header: Reinstatement Date
- Type: DATE\_YMD
- suspend:

- Header: Suspend License?
- Type: YESNO

## disciplinary\_action\_category

The form disciplinary\_action\_category is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## disciplinary\_action\_reason

The form disciplinary\_action\_reason is implemented by the class: iHRIS\_DisciplinaryActionReason It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- disciplinary\_action\_category:

- Header: Disciplinary Action Category
- Type: MAP
- Restrictions: Required

- Maps To Forms: disciplinary\_action\_category
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

The form education is implemented by the class: iHRIS\_SecondaryEducation It has the following fields:

- certificate:

- Header: Certificate
- Type: MAP
- Restrictions: Required
- Maps To Forms: certificate
- certificate\_number:

- Header: Certificate Number

- Type: STRING\_LINE
- grade:

- Header: Grade Obtained
- Type: STRING\_LINE
- sec\_school:

- Header: Secondary School Name
- Type: STRING\_LINE
- Restrictions: Required

## exam

The form exam is implemented by the class: iHRIS\_Exam It has the following fields:

- application\_date:

- Header: Application Date
- Type: DATE\_YMD
- Restrictions: Required
- endorser\_date:

- Header: Endorser Date
- Type: DATE\_YMD
- endorser\_name:

- Header: Endorser Name
- Type: STRING\_LINE
- endorser\_qualifications:

- Header: Endorser Qualifications
- Type: STRING\_MLINE
- exam\_date:

- Header: Exam Date
- Type: DATE\_YMD
- exam\_number:

- Header: Exam Number
- Type: STRING\_LINE
- materials\_approved:

- Header: Materials Approved?
- Type: YESNO
- materials\_received:

- Header: Materials Received?
- Type: YESNO
- results:

- Header: Exam Results
- Type: MAP
- Maps To Forms: exam\_result
- try:

- Header: Exam Try
- Type: MAP
- Maps To Forms: exam\_try

## exam\_result

The form exam\_result is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## exam\_try

The form exam\_try is implemented by the class: I2CE\_SimpleList It has the following fields:

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

## facility\_agent

The form facility\_agent is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

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

## facility\_institution

The form facility\_institution is implemented by the class: iHRIS\_FacilityInstitution It has the following fields:

- active:

- Header: Active?
- Type: BOOL
- Restrictions: Required
- health\_facility:

- Header: Health Facility
- Type: MAP
- Restrictions: Required, Unique in {training\_institution}
- Maps To Forms: health\_facility
- training\_institution:

- Header: Training Institution
- Type: MAP
- Restrictions: Required, Unique in {health\_facility}
- Maps To Forms: training\_institution

## facility\_institution\_edit\_fac

The form facility\_institution\_edit\_fac is implemented by the class: iHRIS\_FacilityInstitutionEditFacility It has the following fields:

- health\_facility:

- Header: Health Facility
- Type: MAP
- Restrictions: Required
- Maps To Forms: health\_facility
- training\_institution:

- Header: Training Institution
- Type: MAP\_MULT
- Restrictions: Required
- Maps To Forms: training\_institution

## facility\_institution\_edit\_inst

The form facility\_institution\_edit\_inst is implemented by the class: iHRIS\_FacilityInstitutionEditInstitution It has the following fields:

- health\_facility:

- Header: Health Facility
- Type: MAP\_MULT
- Restrictions: Required
- Maps To Forms: health\_facility
- training\_institution:

- Header: Training Institution

- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_institution

## facility\_status

The form facility\_status is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

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

## health\_facility

The form health\_facility is implemented by the class: iHRIS\_HealthFacility It has the child forms:

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
- facility\_agent:

- Header: Facility Agent
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility\_agent
- facility\_status:

- Header: Facility Status
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility\_status
- id\_code:

- Header: Identification Code
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

## institution\_inspection

The form institution\_inspection is implemented by the class: iHRIS\_InstitutionInspection It has the following fields:

- date:

- Header: Inspection Date
- Type: DATE\_YMD
- Restrictions: Required
- notes:

- Header: Notes
- Type: STRING\_TEXT
- pass:

- Header: Passed?
- Type: YESNO

## license

The form license is implemented by the class: iHRIS\_License It has the following fields:

- end\_date:

- Header: End Date
- Type: DATE\_YMD
- Restrictions: Required
- license\_number:

- Header: License Number
- Type: INT\_GENERATE
- Restrictions: Required
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required
- suspend:

- Header: Suspended?
- Type: YESNO

## marital\_status

The form marital\_status is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

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

## out\_migration

The form out\_migration is implemented by the class: iHRIS\_OutMigration It has the following fields:

- country:

- Header: Country
- Type: MAP
- Restrictions: Required
- Maps To Forms: country
- new\_address:

- Header: Address in new Country
- Type: STRING\_MLINE
- organization:

- Header: Organization Requesting Verification
- Type: STRING\_LINE
- out\_migration\_reason:

- Header: Out Migration Reason
- Type: MAP
- Restrictions: Required
- Maps To Forms: out\_migration\_reason
- request\_date:

- Header: Request Date

- Type: DATE\_YMD

## out\_migration\_reason

The form out\_migration\_reason is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## person

The form person is implemented by the class: iHRIS\_QualifyPerson

This form holds basic information about a person such as their names and residence

It has the child forms:

- demographic
- deployment
- education
- notes
- out\_migration
- person\_archive\_scan
- person\_contact\_emergency
- person\_contact\_other
- person\_contact\_personal
- person\_contact\_work
- person\_id
- person\_photo\_passport
- record\_verify
- training

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
- home:

- Header: Home
- Type: MAP
- Maps To Forms: county,district

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

## private\_practice

The form private\_practice is implemented by the class: iHRIS\_PrivatePractice It has the following fields:

- end\_date:

- Header: End Date
- Type: DATE\_YMD
- Restrictions: Required
- health\_facility:

- Header: Health Facility
- Type: MAP
- Restrictions: Required
- Maps To Forms: health\_facility
- inspection\_date:

- Header: Inspection Date
- Type: DATE\_YMD
- inspection\_results:

- Header: Inspection Results
- Type: STRING\_MLINE
- license\_number:

- Header: License Number
- Type: INT\_GENERATE
- Restrictions: Required
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required

## qualification

The form qualification is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## record\_verify

The form record\_verify is implemented by the class: iHRIS\_RecordVerify It has the following fields:

- verify\_change:

- Header: Changes Made
- Type: MAP\_MULT
- Maps To Forms: verify\_change
- verify\_date:

- Header: Verification Date
- Type: DATE\_YMD

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

- application\_date:

- Header: Application Date
- Type: DATE\_YMD
- Restrictions: Required
- practice\_type:

- Header: Practice Type
- Type: MAP
- Restrictions: Required
- Maps To Forms: registration\_type
- registration\_date:

- Header: Registration Date
- Type: DATE\_YMD
- Restrictions: Required
- registration\_number:

- Header: Registration Number
- Type: INT\_GENERATE
- Restrictions: Required, Unique

## registration\_type

The form registration\_type is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training

The form training is implemented by the class: iHRIS\_Training It has the child forms:

- continuing\_education
- disciplinary\_action
- exam
- license
- private\_practice
- registration
- training\_disrupt

It has the following fields:

- cadre:

- Header: Cadre
- Type: MAP

- Maps To Forms: cadre
- graduation:

- Header: Graduation Date
- Type: DATE\_YMD
- index\_num:

- Header: Index Number
- Type: INT\_GENERATE
- Restrictions: Required
- intake\_date:

- Header: Intake Date
- Type: DATE\_YMD
- Restrictions: Required
- out\_country:

- Header: Country Trained in
- Type: MAP
- Maps To Forms: country
- out\_institution:

- Header: Training Institution
- Type: STRING\_LINE
- trained\_outside:

- Header: Trained Outside this Country
- Type: BOOL
- training\_institution:

- Header: Training Institution
- Type: MAP
- Maps To Forms: training\_institution

## training\_disrupt

The form training\_disrupt is implemented by the class: iHRIS\_TrainingDisrupt It has the following fields:

- disruption\_date:

- Header: Disruption Date
- Type: DATE\_YMD
- Restrictions: Required
- disruption\_reason:

- Header: Disruption Reason
- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_disruption\_reason
- resumption\_date:

- Header: Resumption Date
- Type: DATE\_YMD

## training\_disruption\_category

The form training\_disruption\_category is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## training\_disruption\_reason

The form training\_disruption\_reason is implemented by the class: iHRIS\_TrainingDisruptionReason It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique in {training\_disruption\_category}
- training\_disruption\_category:

- Header: Training Disruption Category
- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_disruption\_category

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

The form training\_institution is implemented by the class: iHRIS\_QualifyTrainingInstitution It has the child forms:

- facility\_contact
- institution\_inspection

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
- facility\_agent:

- Header: Facility Agent
- Type: MAP

- Restrictions: Required
- Maps To Forms: facility\_agent
- facility\_status:

- Header: Facility Status
- Type: MAP
- Restrictions: Required
- Maps To Forms: facility\_status
- id\_code:

- Header: Identification Code
- Type: STRING\_LINE

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

## training\_program

The form training\_program is implemented by the class: iHRIS\_TrainingProgram It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- cadre:

- Header: Cadre
- Type: MAP
- Restrictions: Required, Unique in {training\_institution}
- Maps To Forms: cadre
- end\_date:

- Header: End Date
- Type: DATE\_YMD
- num\_students:

- Header: Number of Students
- Type: INT
- start\_date:

- Header: Start Date
- Type: DATE\_YMD
- Restrictions: Required
- training\_institution:

- Header: Training Institution
- Type: MAP
- Restrictions: Required
- Maps To Forms: training\_institution

## verify\_change

The form verify\_change is implemented by the class: I2CE\_SimpleList It has the following fields:

- i2ce\_hidden:

- Header: Hide
- Type: YESNO
- name:

- Header: Name
- Type: STRING\_LINE
- Restrictions: Required, Unique

## References

\[1\] http://open.intrahealth.org/visualizations/forms-ihris-qualify-site-demo\_4\_0\_7.gif
