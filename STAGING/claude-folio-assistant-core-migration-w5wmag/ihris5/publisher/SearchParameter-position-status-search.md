# position-status-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **position-status-search**

## SearchParameter: position-status-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/position-status-search | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter for a practitionerRole position status |

 
Search for a practitionerRole position status. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "position-status-search",
  "url" : "http://ihris.org/fhir/SearchParameter/position-status-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitionerRole position status",
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
  "description" : "Search for a practitionerRole position status.",
  "code" : "positionstatus",
  "base" : ["PractitionerRole"],
  "type" : "token",
  "expression" : "PractitionerRole.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-practitionerrole-position-status')",
  "xpathUsage" : "normal"
}

```
