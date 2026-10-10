# Code system for document categories. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Code system for document categories.**

## CodeSystem: Code system for document categories. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-document-category | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisDocumentCategoryCodeSystem |

 This Code system is referenced in the content logical definition of the following value sets: 

* [Code system for document categories.](ValueSet-ihris-document-category.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-document-category",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-document-category",
  "version" : "0.1.0",
  "name" : "IhrisDocumentCategoryCodeSystem",
  "title" : "Code system for document categories.",
  "status" : "active",
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "open",
    "display" : "Open",
    "definition" : "Any one can access."
  },
  {
    "code" : "restricted",
    "display" : "Restricted",
    "definition" : "Only certain users can view."
  }]
}

```
