# iHRIS Test CodeSystem - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Test CodeSystem**

## CodeSystem: iHRIS Test CodeSystem 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-test-codesystem | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisTestCodeSystem |

 This Code system is referenced in the content logical definition of the following value sets: 

* This CodeSystem is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-test-codesystem",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-test-codesystem",
  "version" : "0.1.0",
  "name" : "IhrisTestCodeSystem",
  "title" : "iHRIS Test CodeSystem",
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
  "content" : "complete",
  "count" : 2,
  "property" : [{
    "code" : "prop1",
    "description" : "First Property",
    "type" : "string"
  },
  {
    "code" : "prop2",
    "uri" : "http://ihris.org/fhir/ValueSet/test",
    "description" : "Second Property",
    "type" : "Coding"
  }],
  "concept" : [{
    "code" : "one",
    "display" : "One",
    "definition" : "First one"
  },
  {
    "code" : "two",
    "display" : "Two",
    "definition" : "Second one"
  }]
}

```
