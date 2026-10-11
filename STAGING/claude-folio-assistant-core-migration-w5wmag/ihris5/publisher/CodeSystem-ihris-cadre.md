# iHRIS Cadre - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Cadre**

## CodeSystem: iHRIS Cadre 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-cadre | *Version*:0.1.0 |
| Active as of 2020-09-25 | *Computable Name*:IhrisCadre |

 
Sample iHRIS CodeSystem for: IhrisCadre 

 This Code system is referenced in the content logical definition of the following value sets: 

* [iHRIS Cadre](ValueSet-ihris-cadre.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-cadre",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-cadre",
  "version" : "0.1.0",
  "name" : "IhrisCadre",
  "title" : "iHRIS Cadre",
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
  "description" : "Sample iHRIS CodeSystem for: IhrisCadre",
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "doctor",
    "display" : "Medical Doctor"
  },
  {
    "code" : "nurse",
    "display" : "Nurse"
  },
  {
    "code" : "allied-health",
    "display" : "Allied Health Professional"
  },
  {
    "code" : "pharmacist",
    "display" : "Pharmacist"
  }]
}

```
