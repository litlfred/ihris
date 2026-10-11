# iHRIS Salary Grade - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Salary Grade**

## CodeSystem: iHRIS Salary Grade 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-salary-grade | *Version*:0.1.0 |
| Active as of 2020-09-25 | *Computable Name*:IhrisSalaryGrade |

 
Sample iHRIS CodeSystem for: iHRISSalaryGrade 

 This Code system is referenced in the content logical definition of the following value sets: 

* [iHRIS Salary Grade](ValueSet-ihris-salary-grade.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-salary-grade",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-salary-grade",
  "version" : "0.1.0",
  "name" : "IhrisSalaryGrade",
  "title" : "iHRIS Salary Grade",
  "status" : "active",
  "date" : "2020-09-25T20:48:33.646Z",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Sample iHRIS CodeSystem for: iHRISSalaryGrade",
  "content" : "complete",
  "count" : 8,
  "property" : [{
    "code" : "start",
    "description" : "The starting salary for this grade.",
    "type" : "Coding"
  },
  {
    "code" : "midpoint",
    "description" : "The midpoint salary for this grade.",
    "type" : "Coding"
  },
  {
    "code" : "end",
    "description" : "The end point salary for this grade.",
    "type" : "Coding"
  },
  {
    "code" : "currency",
    "description" : "The currency used (urn:iso:std:iso:4217).",
    "type" : "Coding"
  }],
  "concept" : [{
    "code" : "entry-level",
    "display" : "Entry-Level",
    "definition" : "Entry-level and support positions."
  },
  {
    "code" : "prof-entry-level",
    "display" : "Professional Entry-Level",
    "definition" : "Professional first grade."
  },
  {
    "code" : "prof-mid-level",
    "display" : "Professional Mid-Level or Managerial"
  },
  {
    "code" : "director",
    "display" : "Director",
    "definition" : "Director"
  },
  {
    "code" : "specialist",
    "display" : "Technical Specialist",
    "definition" : "Not included in any standard salary grades."
  },
  {
    "code" : "nurse",
    "display" : "Nurse",
    "definition" : "Nurse"
  },
  {
    "code" : "allied-health",
    "display" : "Allied Health",
    "definition" : "Allied Health Professionals"
  },
  {
    "code" : "doctor",
    "display" : "Doctor",
    "definition" : "Doctor"
  }]
}

```
