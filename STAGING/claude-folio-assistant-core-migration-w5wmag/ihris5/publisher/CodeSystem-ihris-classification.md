# iHRIS Classification - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Classification**

## CodeSystem: iHRIS Classification 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-classification | *Version*:0.1.0 |
| Active as of 2020-09-25 | *Computable Name*:IhrisClassification |

 
Sample iHRIS CodeSystem for: IhrisClassification 

 This Code system is referenced in the content logical definition of the following value sets: 

* [iHRIS Classification](ValueSet-ihris-classification.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-classification",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-classification",
  "version" : "0.1.0",
  "name" : "IhrisClassification",
  "title" : "iHRIS Classification",
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
  "description" : "Sample iHRIS CodeSystem for: IhrisClassification",
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "doctor",
    "display" : "Medical Doctor",
    "definition" : "Medical doctors"
  },
  {
    "code" : "nurse",
    "display" : "Nurse",
    "definition" : "Nursing and midwifery professionals"
  },
  {
    "code" : "allied-health",
    "display" : "Allied Health Professional",
    "definition" : "Modern health associate professionals (except nursing)"
  },
  {
    "code" : "non-health",
    "display" : "Non-Health Professional",
    "definition" : "Professionals, not health"
  },
  {
    "code" : "support",
    "display" : "Non-Health Support Staff",
    "definition" : "Support staff, not health-related"
  },
  {
    "code" : "pharmacist",
    "display" : "Pharmacist",
    "definition" : "Dispenses drugs."
  }]
}

```
