# iHRIS Test CodeSystem Page - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Test CodeSystem Page**

## Example Basic: iHRIS Test CodeSystem Page

Profile: [iHRIS Page](StructureDefinition-ihris-page.md)

> **iHRIS Page Display**
* resource: [CodeSystem iHRIS Test CodeSystem](CodeSystem-ihris-test-codesystem.md)
* search: Property One|prop1
* search: Property Two|prop2

> **iHRIS Page Section**
* title: Test CodeSystem
* description: Code system details
* name: CodeSystem
* field: CodeSystem.code
* field: CodeSystem.definition
* field: CodeSystem.display
* field: CodeSystem.prop2
* field: CodeSystem.prop1

**code**: iHRIS Page



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-page-test-codesystem",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "resource",
      "valueReference" : {
        "reference" : "CodeSystem/ihris-test-codesystem"
      }
    },
    {
      "url" : "search",
      "valueString" : "Property One|prop1"
    },
    {
      "url" : "search",
      "valueString" : "Property Two|prop2"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Test CodeSystem"
    },
    {
      "url" : "description",
      "valueString" : "Code system details"
    },
    {
      "url" : "name",
      "valueString" : "CodeSystem"
    },
    {
      "url" : "field",
      "valueString" : "CodeSystem.code"
    },
    {
      "url" : "field",
      "valueString" : "CodeSystem.definition"
    },
    {
      "url" : "field",
      "valueString" : "CodeSystem.display"
    },
    {
      "url" : "field",
      "valueString" : "CodeSystem.prop2"
    },
    {
      "url" : "field",
      "valueString" : "CodeSystem.prop1"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "page"
    }]
  }
}

```
