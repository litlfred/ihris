# employment-status-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **employment-status-search**

## SearchParameter: employment-status-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/employment-status-search | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter for a practitionerRole employment-status |

 
Search for a practitionerRole employment-status. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "employment-status-search",
  "url" : "http://ihris.org/fhir/SearchParameter/employment-status-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitionerRole employment-status",
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
  "description" : "Search for a practitionerRole employment-status.",
  "code" : "employmentstatus",
  "base" : ["PractitionerRole"],
  "type" : "token",
  "expression" : "PractitionerRole.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-practitionerrole-employment-status')",
  "xpathUsage" : "normal"
}

```
