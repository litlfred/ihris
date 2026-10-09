# location-related-location - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **location-related-location**

## SearchParameter: location-related-location 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/location-related-location | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related location resources for security |

 
Search by related location for a Location resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "location-related-location",
  "url" : "http://ihris.org/fhir/SearchParameter/location-related-location",
  "version" : "0.1.0",
  "name" : "Search Parameter on related location resources for security",
  "status" : "active",
  "date" : "2026-10-09T12:24:25+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by related location for a Location resource.",
  "code" : "related-location",
  "base" : ["Location"],
  "type" : "string",
  "expression" : "Location.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location') | Location.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location').empty()",
  "xpathUsage" : "normal"
}

```
