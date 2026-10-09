# practitioner-related-practitioner - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-related-practitioner**

## SearchParameter: practitioner-related-practitioner 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-related-practitioner | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related practitioner resources for security |

 
Search by related practitioner for a Practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-related-practitioner",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-related-practitioner",
  "version" : "0.1.0",
  "name" : "Search Parameter on related practitioner resources for security",
  "status" : "active",
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by related practitioner for a Practitioner resource.",
  "code" : "related-practitioner",
  "base" : ["Practitioner"],
  "type" : "string",
  "expression" : "Practitioner.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('practitioner')",
  "xpathUsage" : "normal"
}

```
