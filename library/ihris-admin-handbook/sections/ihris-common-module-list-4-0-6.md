---
title: "IHRIS Common Module List (4.0.6)"
source: http://open.intrahealth.org/w/index.php?oldid=33771
contributors: ["Litlfred"]
pages: 159-187
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# IHRIS Common Module List (4.0.6)

This is a list of all modules available in version 4.0.6-release of the package iHRIS Common \[1\]

## CEUs

This describes version 4.0.1.1 of the module CEUs (CEUs)

- Source: common/modules/CEUs \[2\]

- Module Class: The module class is implemented by iHRIS\_Module\_CEUs
- Description: Makes Continuing Education Unit (CEU) information available to the system
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1
- Paths:

- Configs: modules/CEUs/configs \[3\]

- Classes: modules/CEUs/lib \[4\]

- iHRIS\_Module\_CEUs
- Templates: modules/CEUs/templates \[5\]

view\_list\_continuing\_education\_course.html, lists\_form\_continuing\_education\_course.html

## Contact

This describes version 4.0.6.1 of the module Contact (Contact)

- Source: common/modules/Contact \[6\]

- Module Class: The module class is implemented by iHRIS\_Module\_Contact
- Description: Makes Contact information available to the system
- Requirements:

- Geography at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Contact/configs \[7\]

- Classes: modules/Contact/lib \[8\]

- iHRIS\_Contact, iHRIS\_Module\_Contact
- Templates: modules/Contact/templates \[9\]

lists\_form\_contact.html, form\_contact.html

## Currency

This describes version 4.0.6.2 of the module Currency (Currency)

- Source: common/modules/Currency \[10\]

- Module Class: The module class is implemented by iHRIS\_Module\_Currency
- Description: Makes Currency information available to the system
- Requirements:

- Geography at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Currency/configs \[11\]

- Classes: modules/Currency/lib \[12\]

- iHRIS\_FormField\_CURRENCY, iHRIS\_Module\_Currency
- Templates: modules/Currency/templates \[13\]

view\_list\_currency.html, lists\_form\_currency.html

## Document

This describes version 4.0.0 of the module Document (Document)

- Source: common/modules/Document \[14\]

- Description: Makes Document information available to the system
- Requirements:

- BinField at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Document/configs \[15\]

- Classes: modules/Document/lib \[16\]

## Facility

This describes version 4.0.0 of the module Facility (Facility)

- Source: common/modules/Facility \[17\]

- Module Class: The module class is implemented by iHRIS\_Module\_Facility
- Description: Makes Facility information available to the system
- Requirements:

- Geography at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Facility/configs \[18\]

- Classes: modules/Facility/lib \[19\]

- iHRIS\_Module\_Facility
- Modules: modules/Facility/modules \[20\]

- FacilityContact
- Templates: modules/Facility/templates \[21\]

lists\_form\_facility.html, view\_list\_facility.html, view\_list\_facility\_type.html

## FacilityContact

This describes version 4.0.0 of the module Facility Contact (FacilityContact)

- Source: common/modules/Facility/modules/FacilityContact \[22\]

- Module Class: The module class is implemented by iHRIS\_Module\_FacilityContact
- Description: Adds contact information to a facility
- Requirements:

- Facility at least 4.0 and less than 4.1
- Contact at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Facility/modules/FacilityContact/configs \[23\]

- Templates: modules/Facility/modules/FacilityContact/templates \[24\]

- view\_list\_facility\_contact.html, lists\_form\_facility\_contact.html
- Classes: modules/Facility/modules/FacilityContact/lib \[25\]

iHRIS\_Module\_FacilityContact

## Geography

This describes version 4.0.6.1 of the module Geography (Geography)

- Source: common/modules/Geography \[26\]

- Module Class: The module class is implemented by iHRIS\_Module\_Geography
- Description: Makes Geography information available to the system
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Geography/configs \[27\]

- Classes: modules/Geography/lib \[28\]

iHRIS\_Country, iHRIS\_Module\_Geography

- Templates: modules/Geography/templates \[29\]

view\_list\_district.html, view\_list\_county.html, lists\_form\_district.html, lists\_form\_country.html, lists\_form\_county.html, view\_list\_country.html, lists\_form\_region.html, view\_list\_region.html

## Person

This describes version 4.0.0 of the module Person (Person)

- Source: common/modules/Person \[30\]

- Module Class: The module class is implemented by iHRIS\_Module\_Person
- Description: Makes Person information available to the system
- Requirements:

- Geography at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Person/configs \[31\]

- Classes: modules/Person/lib \[32\]

- iHRIS\_Module\_Person, iHRIS\_PageFormParentPerson, iHRIS\_PageFormPerson, iHRIS\_PageView, iHRIS\_Person
- Modules: modules/Person/modules \[33\]

- PersonArchivedScan, PersonContact, PersonDemographic, PersonEducation, PersonEmployment, PersonID, PersonLanguage, PersonNotes, PersonPassportPhoto, PersonResume, dependents, nextOfKin, person-simple-competency
- Templates: modules/Person/templates \[34\]

view.html, menu\_view\_link.html, form\_person\_base.html, menu\_view\_person.html, form\_person.html

## PersonArchivedScan

This describes version 4.0.6.2 of the module Archived Paper Records (PersonArchivedScan)

- Source: common/modules/Person/modules/ArchivalScans \[35\]

- Module Class: The module class is implemented by iHRIS\_Module\_ArchivedScan
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_archive\_scan() via action\_person\_archive\_scan()
- Description: Provides place to archive scans of paper records
- Requirements:

- Person at least 4.0
- Photo at least 4.0
- Paths:

- Configs: modules/Person/modules/ArchivalScans/configs \[36\]

- Classes: modules/Person/modules/ArchivalScans/lib \[37\]

- iHRIS\_Module\_ArchivedScan
- Templates: modules/Person/modules/ArchivalScans/templates \[38\]

view\_person\_archive\_scan.html, form\_person\_archive\_scan.html

## PersonContact

This describes version 4.0.0 of the module iHRIS Person Contact (PersonContact)

- Source: common/modules/Person/modules/Contact \[39\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonContact
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_contact\_work() via action\_person\_contact\_work()
- Implements the method iHRIS\_PageView-&gt;action\_person\_contact\_personal() via action\_person\_contact\_personal()
- Implements the method iHRIS\_PageView-&gt;action\_person\_contact\_other() via action\_person\_contact\_other()
- Implements the method iHRIS\_PageView-&gt;action\_person\_contact\_emergency() via action\_person\_contact\_emergency()
- Description: A Person's Contact
- Requirements:

- Person at least 4.0
- Contact at least 4.0
- Paths:

- Configs: modules/Person/modules/Contact/configs \[40\]

- Templates: modules/Person/modules/Contact/templates \[41\]

- add\_person\_contact\_emergency.html, view\_person\_contact\_personal.html, add\_person\_contact\_personal.html, view\_person\_contact\_work.html, form\_person\_contact\_other.html, form\_person\_contact\_emergency.html, view\_person\_contact\_other.html, view\_person\_contact\_emergency.html, add\_person\_contact\_work.html, form\_person\_contact\_personal.html, form\_person\_contact\_work.html, add\_person\_contact\_other.html
- Classes: modules/Person/modules/Contact/lib \[42\]

iHRIS\_Module\_PersonContact, iHRIS\_PageFormContact

## PersonDemographic

This describes version 4.0.0 of the module iHRIS Person Demographic (PersonDemographic)

- Source: common/modules/Person/modules/Demographic \[43\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonDemographic
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_demographic() via action\_demographic()
- Description: A Person's Demographic
- Requirements:

- Person at least 4.0
- Paths:

- Configs: modules/Person/modules/Demographic/configs \[44\]

- Classes: modules/Person/modules/Demographic/lib \[45\]

- iHRIS\_Module\_PersonDemographic
- Templates: modules/Person/modules/Demographic/templates \[46\]

view\_list\_marital\_status.html, form\_demographic.html, view\_demographic.html

## PersonEducation

This describes version 4.0.0 of the module iHRIS Person Education (PersonEducation)

- Source: common/modules/Person/modules/Education \[47\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonEducation
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_education() via action\_education()
- Description: A Person's Education and Degree Details
- Requirements:

- Person at least 4.0
- Paths:

- Configs: modules/Person/modules/Education/configs \[48\]

- Templates: modules/Person/modules/Education/templates \[49\]

- view\_list\_edu\_type.html, form\_education.html, view\_education.html, lists\_form\_degree.html, view\_list\_degree.html
- Classes: modules/Person/modules/Education/lib \[50\]

iHRIS\_Module\_PersonEducation

## PersonEmployment

This describes version 4.0.0 of the module iHRIS Person Employment (PersonEmployment)

- Source: common/modules/Person/modules/Employment \[51\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonEmployment
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_employment() via action\_employment()
- Description: A Person's Employment History Details
- Requirements:

- Person at least 4.0
- Currency at least 4.0
- Paths:

- Configs: modules/Person/modules/Employment/configs \[52\]

- Classes: modules/Person/modules/Employment/lib \[53\]

- iHRIS\_Module\_PersonEmployment
- Templates: modules/Person/modules/Employment/templates \[54\]

view\_employment.html, form\_employment.html

## PersonID

This describes version 4.0.0 of the module iHRIS Person ID (PersonID)

- Source: common/modules/Person/modules/ID \[55\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonID
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_id() via action\_person\_id()
- Description: A Person's ID

- Requirements:

- Person at least 4.0
- Paths:

- Configs: modules/Person/modules/ID/configs \[56\]

- Classes: modules/Person/modules/ID/lib \[57\]

- iHRIS\_Module\_PersonID
- Templates: modules/Person/modules/ID/templates \[58\]

view\_person\_id.html, view\_list\_id\_type.html, form\_person\_id.html

## PersonLanguage

This describes version 4.0.0 of the module iHRIS Person Language (PersonLanguage)

- Source: common/modules/Person/modules/Language \[59\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonLanguage
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_language() via action\_person\_language()
- Description: Track a Person's Language Qualifications
- Requirements:

- Person at least 4.0
- Paths:

- Configs: modules/Person/modules/Language/configs \[60\]

- Classes: modules/Person/modules/Language/lib \[61\]

- iHRIS\_Module\_PersonLanguage
- Templates: modules/Person/modules/Language/templates \[62\]

view\_list\_language.html, view\_person\_language.html, form\_person\_language.html

## PersonNotes

This describes version 4.0.0 of the module Notes (PersonNotes)

- Source: common/modules/Person/modules/Notes \[63\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonNotes
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_notes() via action\_notes()
- Description: Makes Notes information available to the system
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- Person at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Person/modules/Notes/configs \[64\]

- Classes: modules/Person/modules/Notes/lib \[65\]

- iHRIS\_Module\_PersonNotes
- Templates: modules/Person/modules/Notes/templates \[66\]

view\_notes.html, form\_notes.html

## PersonPassportPhoto

This describes version 4.0.6 of the module iHRIS Person Passport Photo (PersonPassportPhoto)

- Source: common/modules/Person/modules/PersonPhoto \[67\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonPassport
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_photo\_passport() via action\_person\_photo\_passport()
- Description: A Person's Photo
- Requirements:

- Person at least 4.0
- Photo at least 4.0
- Paths:

- Configs: modules/Person/modules/PersonPhoto/configs \[68\]

- Classes: modules/Person/modules/PersonPhoto/lib \[69\]

- iHRIS\_Module\_PersonPassport
- Templates: modules/Person/modules/PersonPhoto/templates \[70\]

form\_person\_photo\_passport.html, view\_person\_photo\_passport.html

## PersonResume

This describes version 4.0.6.0 of the module iHRIS Person Resume (PersonResume)

- Source: common/modules/Person/modules/Resume \[71\]

- Module Class: The module class is implemented by iHRIS\_Module\_Resume
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_resume() via action\_person\_resume()
- Description: A Person's Resume
- Requirements:

- Person at least 4.0
- Document at least 4.0
- Paths:

- Configs: modules/Person/modules/Resume/configs \[72\]

- Classes: modules/Person/modules/Resume/lib \[73\]

- iHRIS\_Module\_Resume
- Templates: modules/Person/modules/Resume/templates \[74\]

form\_person\_resume.html, view\_person\_resume.html

## Photo

This describes version 4.0.0 of the module Photo (Photo)

- Source: common/modules/Photo \[75\]

- Description: Makes Photo information available to the system
- Requirements:

- BinField at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Photo/configs \[76\]

- Classes: modules/Photo/lib \[77\]

## SDMX-HD-CodeLists

This describes version 4.0.5.2 of the module SDMX-HD Code Lists (SDMX-HD-CodeLists)

- Source: common/modules/SDMX-HD-CodeLists \[78\]

- Description: Information to load SDMX-HD Code Lists.
- Requirements:

- ihris-common at least 4.0
- forms-storage-SDMXHD at least 4.0
- Paths:

- Configs: modules/SDMX-HD-CodeLists/configs \[79\]

- Sdmxhd: modules/SDMX-HD-CodeLists/SDMX-HD \[80\]

- Classes: modules/SDMX-HD-CodeLists/ \[81\]

## SampleData-Common

This describes version 4.0.0 of the module iHRIS Common Sample Data (SampleData-Common)

- Source: common/modules/CommonSampleData \[82\]

- Description: Sample Data for iHRIS Common forms.
- Requirements:

- ihris-common at least 4.0
- Optionally Enables: SampleData-Geography SampleData-currency SampleData-degree
- Paths:

- Modules: modules/CommonSampleData/modules \[83\]

- SampleData-Geography, SampleData-currency, SampleData-degree, SampleData-edu\_type
- Classes: modules/CommonSampleData/ \[84\]

## SampleData-Geography

This describes version 4.0.0 of the module Geography Sample Data (SampleData-Geography)

- Source: common/modules/CommonSampleData/modules/SampleData-Geography \[85\]

- Description: Sample Data for Geography forms.
- Requirements:

- Geography at least 4.0
- Optionally Enables: SampleData-country SampleData-region SampleData-district SampleData-county
- Paths:

- Modules: modules/CommonSampleData/modules/SampleData-Geography/modules \[86\]

- SampleData-country, SampleData-county, SampleData-district, SampleData-region
- Classes: modules/CommonSampleData/modules/SampleData-Geography/ \[87\]

## SampleData-country

This describes version 4.0.0 of the module Country (SampleData-country)

- Source: common/modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-country \[88\]

- Description: Sample Data for form: country
- Requirements:

- Geography at least 4.0
- Paths:

- Configs: modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-country/configs \[89\]

- Classes: modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-country/ \[90\]

## SampleData-county

This describes version 4.0.0 of the module County (SampleData-county)

- Source: common/modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-county \[91\]

- Description: Sample Data for form: county
- Requirements:

- SampleData-district at least 4.0
- Paths:

- Classes: modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-county/ \[92\]

## SampleData-currency

This describes version 4.0.0 of the module Currency (SampleData-currency)

- Source: common/modules/CommonSampleData/modules/SampleData-currency \[93\]

- Description: Sample Data for form: currency
- Requirements:

- Currency at least 4.0
- Paths:

- Configs: modules/CommonSampleData/modules/SampleData-currency/configs \[94\]

- Classes: modules/CommonSampleData/modules/SampleData-currency/ \[95\]

## SampleData-degree

This describes version 4.0.0 of the module Degree (SampleData-degree)

- Source: common/modules/CommonSampleData/modules/SampleData-degree \[96\]

- Description: Sample Data for form: degree
- Requirements:

- SampleData-edu\_type at least 4.0
- Paths:

- Configs: modules/CommonSampleData/modules/SampleData-degree/configs \[97\]

- Classes: modules/CommonSampleData/modules/SampleData-degree/ \[98\]

## SampleData-district

This describes version 4.0.0 of the module District (SampleData-district)

- Source: common/modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-district \[99\]

- Description: Sample Data for form: district
- Requirements:

- SampleData-region at least 4.0
- Paths:

- Classes: modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-district/ \[100\]

## SampleData-edu\_type

This describes version 4.0.0 of the module Education Type (SampleData-edu\_type)

- Source: common/modules/CommonSampleData/modules/SampleData-edu\_type \[101\]

- Description: Sample Data for form: edu\_type
- Requirements:

- PersonEducation at least 4.0
- Paths:

- Configs: modules/CommonSampleData/modules/SampleData-edu\_type/configs \[102\]

- Classes: modules/CommonSampleData/modules/SampleData-edu\_type/ \[103\]

## SampleData-region

This describes version 4.0.0 of the module Region (SampleData-region)

- Source: common/modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-region \[104\]

- Description: Sample Data for form: region
- Requirements:

- SampleData-country at least 4.0
- Paths:

- Classes: modules/CommonSampleData/modules/SampleData-Geography/modules/SampleData-region/ \[105\]

## UUID\_map

This describes version 4.0.6.1 of the module UUID Map (UUID\_map)

- Source: common/modules/UUID \[106\]

- Module Class: The module class is implemented by iHRIS\_Module\_UUID\_Map
- Description: Allows administrator to associate a UUID with any form id
- Requirements:

- forms-storage-flat at least 4.0 and less than 4.1
- Lists at least 4.0 and less than 4.1
- Paths:

- Configs: modules/UUID/configs \[107\]

- Classes: modules/UUID/lib \[108\]

- iHRIS\_UUID\_Map, iHRIS\_UUID\_Map, iHRIS\_Module\_UUID\_Map
- Sql: modules/UUID/sql \[109\]

## dependents

This describes version 4.0.6.1 of the module Person's Dependents (dependents)

- Source: common/modules/Person/modules/Dependents \[110\]

- Module Class: The module class is implemented by iHRIS\_Module\_Dependents
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_dependent() via show\_dependents()
- Description: Adds Dependent Information to a Person
- Requirements:

- Person at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Person/modules/Dependents/configs \[111\]

- Templates: modules/Person/modules/Dependents/templates \[112\]

- form\_dependent.html, view\_dependent.html
- Classes: modules/Person/modules/Dependents/lib \[113\]

iHRIS\_Module\_Dependents

## establishment

This describes version 4.0.6.20 of the module iHRIS Manage Establishment (establishment)

- Source: common/modules/Establishment \[114\]

- Description: The iHRIS Manage Establishment provides establishment information by cadre
- Requirements:

- ihris-common-Job at least 4.0
- Facility at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Establishment/configs \[115\]

- Classes: modules/Establishment/lib \[116\]

- Templates: modules/Establishment/templates \[117\]

establishment\_menu.html, lists\_form\_establishment\_period.html, view\_list\_establishment.html, view\_list\_establishment\_period.html, lists\_form\_establishment.html

## ihris-common

This describes version 4.0.6 of the module iHRIS Common (ihris-common) It is the top module of this package

- Source: common/ \[118\]

- Module Class: The module class is implemented by iHRIS\_Module
- Description: Commmon elements used by the iHRIS Suite
- Requirements:

- I2CE at least 4.0 and less than 4.1
- pages at least 4.0 and less than 4.1
- forms at least 4.0 and less than 4.1
- forms-storage-entry at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- UserForm at least 4.0 and less than 4.1
- Lists at least 4.0 and less than 4.1
- Tags at least 4.0 and less than 4.1
- Options at least 4.0 and less than 4.1
- template-data at least 4.0 and less than 4.1
- DisplayData at least 4.0 and less than 4.1
- admin at least 4.0 and less than 4.1
- FileDump at least 4.0 and less than 4.1
- LoginPage at least 4.0 and less than 4.1
- Optionally Enables: UserAccess
- Paths:

- Configs: /configs \[119\]

- Classes: /lib \[120\]

iHRIS\_Module, iHRIS\_PageConfigure, iHRIS\_PageFieldHistory, iHRIS\_PageFormLists, iHRIS\_PageFormUser, iHRIS\_PageHistory, iHRIS\_PageIndex, iHRIS\_PageViewList

- Templates: /templates \[121\]

- history.html, field\_history\_fullname.html, button\_confirm\_only.html, hr.html, lists.html, intro.html, display\_field\_mline.html, shell.html, search\_row.html, field\_history\_row\_fullname.html, configure.html, menu\_configure.html, user\_names.html, field\_history.html
- Css: /css \[122\]

- Scripts: /scripts \[123\]

- Images: /images \[124\]

- Modules: /modules \[125\]

CEUs, Contact, Currency, Document, Facility, Geography, Person, Photo, SDMX-HD-CodeLists, SampleData-Common, UUID\_map, establishment, ihris-common-Cadre, ihris-common-Job, ihris-common-RecentForm, ihris-common-Search, simple-competency, training-course, training-institution

## ihris-common-Cadre

This describes version 4.0.6.0 of the module iHRIS Commone Cadre (ihris-common-Cadre)

- Source: common/modules/Cadre \[126\]

- Description: The iHRIS Manage Job
- Requirements:

- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Cadre/configs \[127\]

- Classes: modules/Cadre/lib \[128\]

- Templates: modules/Cadre/templates \[129\]

- view\_list\_cadre.html
- Modules: modules/Cadre/modules \[130\]

## ihris-common-Job

This describes version 4.0.6.7 of the module iHRIS Common Job (ihris-common-Job)

- Source: common/modules/Job \[131\]

- Description: The iHRIS Common Job
- Requirements:

- ihris-common-Cadre at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Job/configs \[132\]

- Classes: modules/Job/lib \[133\]

- Templates: modules/Job/templates \[134\]

- view\_list\_classification.html, view\_list\_job.html, lists\_form\_classification.html, lists\_form\_job.html
- Modules: modules/Job/modules \[135\]

isco-08, isco-88

## ihris-common-RecentForm

This describes version 4.0.3.0 of the module Recent Form Page (ihris-common-RecentForm)

- Source: common/modules/RecentForm \[136\]

- Description: The iHRIS Recent Form page.
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- Paths:

- Configs: modules/RecentForm/configs \[137\]

- Classes: modules/RecentForm/lib \[138\]

- iHRIS\_PageRecentForm
- Templates: modules/RecentForm/templates \[139\]

search\_recent.html, recent\_form.html, recent\_desc.html, menu\_search\_recent.html, recent\_display\_form.html, recent.html, recent\_display.html, menu\_recent.html

## ihris-common-Search

This describes version 4.0.3.0 of the module Search Page (ihris-common-Search)

- Source: common/modules/Search \[140\]

- Description: The iHRIS Search page.
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- CustomReports at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Search/configs \[141\]

- Classes: modules/Search/lib \[142\]

- iHRIS\_PageSearch
- Templates: modules/Search/templates \[143\]

search.html, menu\_search.html, search\_report.html, menu\_search\_report.html

## isco-08

This describes version 4.0.6 of the module ISCO 08 Job Codes (isco-08)

- Source: common/modules/Job/modules/isco\_08 \[144\]

- Description: The ISCO 08 Job Codes
- Paths:

- Modules: modules/Job/modules/isco\_08/modules \[145\]

- isco-08-major-00, isco-08-major-01, isco-08-major-02, isco-08-major-03, isco-08-major-04, isco-08-major-05, isco-08-major-06, isco-08-major-07, isco-08-major-08, isco-08-major-09
- Classes: modules/Job/modules/isco\_08/ \[146\]

## isco-08-major-00

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-00)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_0 \[147\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_0/ \[148\]

## isco-08-major-01

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-01)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_1 \[149\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_1/ \[150\]

## isco-08-major-02

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-02)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_2 \[151\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_2/ \[152\]

## isco-08-major-03

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-03)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_3 \[153\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_3/ \[154\]

## isco-08-major-04

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-04)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_4 \[155\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_4/ \[156\]

## isco-08-major-05

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-05)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_5 \[157\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_5/ \[158\]

## isco-08-major-06

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-06)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_6 \[159\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_6/ \[160\]

## isco-08-major-07

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-07)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_7 \[161\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_7/ \[162\]

## isco-08-major-08

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-08)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_8 \[163\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_8/ \[164\]

## isco-08-major-09

This describes version 4.0.1 of the module ISCO 08 Job Codes (isco-08-major-09)

- Source: common/modules/Job/modules/isco\_08/modules/isco\_08\_major\_9 \[165\]

- Description: The ISCO 08 Job Codes
- Requirements:

- isco-08 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_08/modules/isco\_08\_major\_9/ \[166\]

## isco-88

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88)

- Source: common/modules/Job/modules/isco\_88 \[167\]

- Description: The ISCO 88 Job Codes
- Paths:

- Modules: modules/Job/modules/isco\_88/modules \[168\]

- isco-88-major-00, isco-88-major-01, isco-88-major-02, isco-88-major-03, isco-88-major-04, isco-88-major-05, isco-88-major-06, isco-88-major-07, isco-88-major-08, isco-88-major-09
- Classes: modules/Job/modules/isco\_88/ \[169\]

## isco-88-major-00

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-00)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_0 \[170\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_0/ \[171\]

## isco-88-major-01

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-01)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_1 \[172\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_1/ \[173\]

## isco-88-major-02

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-02)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_2 \[174\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_2/ \[175\]

## isco-88-major-03

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-03)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_3 \[176\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_3/ \[177\]

## isco-88-major-04

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-04)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_4 \[178\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_4/ \[179\]

## isco-88-major-05

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-05)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_5 \[180\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_5/ \[181\]

## isco-88-major-06

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-06)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_6 \[182\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_6/ \[183\]

## isco-88-major-07

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-07)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_7 \[184\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_7/ \[185\]

## isco-88-major-08

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-08)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_8 \[186\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_8/ \[187\]

## isco-88-major-09

This describes version 4.0.1 of the module ISCO 88 Job Codes (isco-88-major-09)

- Source: common/modules/Job/modules/isco\_88/modules/isco\_88\_major\_9 \[188\]

- Description: The ISCO 88 Job Codes
- Requirements:

- isco-88 at least 4.0 and less than 4.1
- Paths:

- Classes: modules/Job/modules/isco\_88/modules/isco\_88\_major\_9/ \[189\]

## nextOfKin

This describes version 4.0.6.1 of the module Person's Next of Kin (nextOfKin)

- Source: common/modules/Person/modules/NextOfKin \[190\]

- Module Class: The module class is implemented by iHRIS\_Module\_NextOfKin
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_nextofkin() via show\_nextofkin()
- Description: Adds Next of Kin Information to a Person
- Requirements:

- Person at least 4.0 and less than 4.1
- Contact at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Person/modules/NextOfKin/configs \[191\]

- Templates: modules/Person/modules/NextOfKin/templates \[192\]

- form\_nextofkin.html, view\_nextofkin.html
- Classes: modules/Person/modules/NextOfKin/lib \[193\]

iHRIS\_Module\_NextOfKin

## person-simple-competency

This describes version 4.0.6 of the module Simple Competency (person-simple-competency)

- Source: common/modules/Person/modules/SimpleCompetency \[194\]

- Module Class: The module class is implemented by iHRIS\_Module\_PersonSimpleCompetency
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_competency() via action\_person\_competency()
- Description: A simple two-tiered compotency module enabled for a person
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- Person at least 4.0 and less than 4.1
- simple-competency at least 4.0 and less than 4.1
- Paths:

- Configs: modules/Person/modules/SimpleCompetency/configs \[195\]

- Classes: modules/Person/modules/SimpleCompetency/lib \[196\]

iHRIS\_Module\_PersonSimpleCompetency, iHRIS\_Page\_Person\_Competency\_Evaluation\_History

- Templates: modules/Person/modules/SimpleCompetency/templates \[197\] personal\_competency\_evaluation\_history.html, form\_person\_competency.html, view\_person\_competency.html, personal\_competency\_evaluation\_history\_comp\_each.html,

personal\_competency\_evaluation\_history\_each.html

## simple-competency

This describes version 4.0.0 of the module Simple Competency (simple-competency)

- Source: common/modules/SimpleComptency \[198\]

- Module Class: The module class is implemented by iHRIS\_Module\_SimpleCompetency
- Description: A simple two-tiered compotency module
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage-magicdata at least 4.0 and less than 4.1
- Paths:

- Configs: modules/SimpleComptency/configs \[199\]

- Classes: modules/SimpleComptency/lib \[200\]

- iHRIS\_Module\_SimpleCompetency
- Templates: modules/SimpleComptency/templates \[201\]

view\_list\_competency.html, view\_list\_competency\_type.html, lists\_form\_competency.html, view\_list\_competency\_evaluation.html

## training-course

This describes version 4.0.46.2 of the module Training Course (training-course)

- Source: common/modules/TrainingCourse \[202\]

- Module Class: The module class is implemented by iHRIS\_Module\_Training\_Course
- Fuzzy Methods:

- Implements the method iHRIS\_PageView-&gt;action\_person\_scheduled\_training\_course() via action\_person\_scheduled\_training\_course()
- Description: Adds functionality to add training courses to the system
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- form-limits at least 4.0 and less than 4.1
- forms-storage at least 4.0 and less than 4.1
- CEUs at least 4.0 and less than 4.1
- Paths:

- Configs: modules/TrainingCourse/configs \[203\]

- Classes: modules/TrainingCourse/lib \[204\]

iHRIS\_Module\_Training\_Course, iHRIS\_PageForm\_Person\_Scheduled\_Training\_Course, iHRIS\_Scheduled\_Training\_Course, iHRIS\_Training\_Course

- Templates: modules/TrainingCourse/templates \[205\]

enrolled\_students.html, lists\_form\_training\_course\_evaluation.html, form\_person\_schedule\_training\_course.html, view\_list\_training\_course\_evaluation.html, lists\_form\_scheduled\_training\_course.html, view\_person\_scheduled\_training\_course.html, view\_list\_training\_course\_category.html, lists\_form\_training\_course.html, view\_list\_scheduled\_training\_course.html, scheduled\_course\_list\_person.html, view\_list\_training\_course\_status.html, form\_schedule\_training\_course.html, view\_list\_training\_course.html, view\_list\_training\_course\_requestor.html

- Modules: modules/TrainingCourse/modules \[206\]

training-simple-competency

## training-institution

This describes version 4.0.0 of the module Training Institution (training-institution)

- Source: common/modules/TrainingInstitution \[207\]

- Module Class: The module class is implemented by iHRIS\_Module\_TrainingInstitution
- Description: Adds basic training institution and funder functionality
- Requirements:

- ihris-common at least 4.0 and less than 4.1
- Geography at least 4.0 and less than 4.1
- Contact at least 4.0 and less than 4.1
- Paths:

- Configs: modules/TrainingInstitution/configs \[208\]

- Classes: modules/TrainingInstitution/lib \[209\]

- iHRIS\_Module\_TrainingInstitution, iHRIS\_PageFormParentTrainingInstitution
- Templates: modules/TrainingInstitution/templates \[210\]

lists\_form\_training\_funder\_contact.html, view\_list\_training\_funder\_contact.html, view\_list\_training\_institution.html, view\_list\_training\_funder.html, lists\_form\_training\_funder.html, button\_confirm\_ti.html, lists\_form\_ti\_base.html, lists\_form\_training\_institution.html, menu\_view\_ti.html, lists\_form\_training\_institution\_contact.html, view\_list\_training\_institution\_contact.html

## training-simple-competency

This describes version 4.0.12 of the module Training Competency (Simple) (training-simple-competency)

- Source: common/modules/TrainingCourse/modules/TrainingSimpleCompetency \[211\]

- Module Class: The module class is implemented by iHRIS\_Module\_TrainingSimpleCompetency
- Description: Makes the Simple Competency module available to training course module
- Requirements:

- training-course at least 4.0 and less than 4.1
- person-simple-competency at least 4.0 and less than 4.1
- Paths:

- Configs: modules/TrainingCourse/modules/TrainingSimpleCompetency/configs \[212\]

- Classes: modules/TrainingCourse/modules/TrainingSimpleCompetency/lib \[213\]

- iHRIS\_Module\_TrainingSimpleCompetency, iHRIS\_PageForm\_Evaluate\_Course\_Competencies
- Templates: modules/TrainingCourse/modules/TrainingSimpleCompetency/templates \[214\]

training\_course\_evaluation\_no\_competency.html, form\_training\_course\_competencies.html, training\_course\_evaluation\_form.html

## References

\[1\] https://launchpad.net/ihris-common \[2\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CEUs \[3\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CEUs/configs \[4\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CEUs/lib \[5\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CEUs/templates \[6\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Contact \[7\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Contact/configs \[8\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Contact/lib \[9\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Contact/templates \[10\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Currency \[11\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Currency/configs \[12\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Currency/lib \[13\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Currency/templates \[14\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Document \[15\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Document/configs \[16\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Document/lib \[17\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility \[18\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/configs \[19\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/lib \[20\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/modules \[21\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/templates \[22\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/modules/

FacilityContact \[23\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/modules/

FacilityContact/configs \[24\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/modules/

FacilityContact/templates \[25\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Facility/modules/

FacilityContact/lib \[26\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Geography \[27\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Geography/configs \[28\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Geography/lib \[29\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Geography/templates \[30\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person \[31\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/configs \[32\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/lib

\[33\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules \[34\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/templates \[35\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

ArchivalScans \[36\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

ArchivalScans/configs \[37\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

ArchivalScans/lib \[38\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

ArchivalScans/templates \[39\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Contact \[40\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Contact/

configs \[41\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Contact/

templates \[42\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Contact/lib \[43\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Demographic

\[44\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Demographic/configs

\[45\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Demographic/lib \[46\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Demographic/templates \[47\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Education \[48\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Education/

configs \[49\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Education/

templates \[50\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Education/

lib \[51\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Employment \[52\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Employment/configs \[53\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Employment/lib \[54\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Employment/templates \[55\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/ID \[56\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/ID/configs \[57\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/ID/lib \[58\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/ID/

templates \[59\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Language \[60\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Language/

configs \[61\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Language/

lib \[62\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Language/

templates \[63\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Notes \[64\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Notes/

configs \[65\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Notes/lib \[66\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Notes/

templates

\[67\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/PersonPhoto \[68\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

PersonPhoto/configs \[69\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

PersonPhoto/lib \[70\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

PersonPhoto/templates \[71\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Resume \[72\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Resume/

configs \[73\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Resume/lib \[74\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/Resume/

templates \[75\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Photo \[76\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Photo/configs \[77\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Photo/lib \[78\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SDMX-HD-CodeLists \[79\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SDMX-HD-CodeLists/

configs

\[80\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SDMX-HD-CodeLists/

SDMX-HD \[81\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SDMX-HD-CodeLists/

\[82\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData \[83\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules \[84\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/ \[85\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography \[86\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules \[87\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/ \[88\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-country \[89\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-country/configs \[90\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-country/ \[91\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-county \[92\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-county/ \[93\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-currency \[94\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-currency/configs \[95\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-currency/ \[96\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-degree \[97\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-degree/configs \[98\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-degree/ \[99\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-district \[100\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-district/ \[101\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-edu\_type \[102\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-edu\_type/configs \[103\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-edu\_type/ \[104\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-region \[105\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/CommonSampleData/

modules/SampleData-Geography/modules/SampleData-region/ \[106\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/UUID \[107\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/UUID/configs \[108\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/UUID/lib \[109\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/UUID/sql \[110\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Dependents \[111\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Dependents/configs \[112\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Dependents/templates

\[113\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

Dependents/lib \[114\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Establishment

\[115\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Establishment/configs \[116\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Establishment/lib \[117\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Establishment/templates \[118\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/ \[119\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://configs \[120\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://lib \[121\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://templates \[122\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://css \[123\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://scripts \[124\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://images \[125\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head://modules \[126\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Cadre \[127\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Cadre/configs \[128\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Cadre/lib \[129\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Cadre/templates \[130\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Cadre/modules \[131\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job \[132\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/configs \[133\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/lib \[134\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/templates \[135\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules \[136\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/RecentForm \[137\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/RecentForm/configs \[138\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/RecentForm/lib \[139\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/RecentForm/templates \[140\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Search \[141\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Search/configs \[142\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Search/lib \[143\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Search/templates \[144\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08 \[145\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules \[146\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/ \[147\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_0 \[148\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_0/

\[149\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_1 \[150\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_1/ \[151\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_2 \[152\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_2/ \[153\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_3 \[154\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_3/ \[155\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_4 \[156\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_4/ \[157\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_5

\[158\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_5/ \[159\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_6

\[160\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_6/ \[161\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_7 \[162\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_7/ \[163\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_8 \[164\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_8/ \[165\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_9 \[166\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_08/

modules/isco\_08\_major\_9/ \[167\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88 \[168\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules \[169\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/ \[170\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_0 \[171\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_0/ \[172\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_1 \[173\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_1/ \[174\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_2 \[175\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_2/ \[176\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_3 \[177\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_3/ \[178\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_4 \[179\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_4/ \[180\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_5 \[181\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_5/ \[182\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_6 \[183\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_6/ \[184\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_7 \[185\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_7/ \[186\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_8 \[187\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_8/ \[188\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_9

\[189\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Job/modules/isco\_88/

modules/isco\_88\_major\_9/ \[190\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/NextOfKin

\[191\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

NextOfKin/configs \[192\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

NextOfKin/templates \[193\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

NextOfKin/lib \[194\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

SimpleCompetency \[195\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

SimpleCompetency/configs \[196\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

SimpleCompetency/lib \[197\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/Person/modules/

SimpleCompetency/templates \[198\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SimpleComptency \[199\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SimpleComptency/configs \[200\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SimpleComptency/lib \[201\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/SimpleComptency/

templates \[202\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse \[203\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/configs \[204\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/lib \[205\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/templates \[206\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/modules \[207\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingInstitution \[208\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingInstitution/configs \[209\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingInstitution/lib \[210\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingInstitution/

templates \[211\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/modules/

TrainingSimpleCompetency \[212\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/modules/

TrainingSimpleCompetency/configs \[213\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/modules/

TrainingSimpleCompetency/lib \[214\] http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0.6-release/files/head:/modules/TrainingCourse/modules/

TrainingSimpleCompetency/templates
