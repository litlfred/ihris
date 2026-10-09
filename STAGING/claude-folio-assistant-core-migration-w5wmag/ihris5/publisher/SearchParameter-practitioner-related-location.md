# practitioner-related-location - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-related-location**

## SearchParameter: practitioner-related-location 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-related-location | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related location resources for security |

 
Search by related location for a Practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-related-location",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-related-location",
  "version" : "0.1.0",
  "name" : "Search Parameter on related location resources for security",
  "status" : "active",
  "date" : "2026-10-09T11:54:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by related location for a Practitioner resource.",
  "code" : "related-location",
  "base" : ["Practitioner"],
  "type" : "string",
  "expression" : "Practitioner.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location') | Practitioner.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location').empty()",
  "xpathUsage" : "normal"
}

```
