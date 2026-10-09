# basic-related-practitioner - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **basic-related-practitioner**

## SearchParameter: basic-related-practitioner 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/basic-related-practitioner | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related practitioner resources for security |

 
Search by related practitioner for a Basic resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "basic-related-practitioner",
  "url" : "http://ihris.org/fhir/SearchParameter/basic-related-practitioner",
  "version" : "0.1.0",
  "name" : "Search Parameter on related practitioner resources for security",
  "status" : "active",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by related practitioner for a Basic resource.",
  "code" : "related-practitioner",
  "base" : ["Basic"],
  "type" : "string",
  "expression" : "Basic.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('practitioner')",
  "xpathUsage" : "normal"
}

```
