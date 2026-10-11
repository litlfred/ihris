# iHRIS Test Practitioner Page - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Test Practitioner Page**

## Example Basic: iHRIS Test Practitioner Page

Profile: [iHRIS Page](StructureDefinition-ihris-page.md)

> **iHRIS Page Display**
* resource: [StructureDefinition IhrisTestPractitioner](StructureDefinition-ihris-test-practitioner.md)
* search: Surname|name.where(use='official').family
* search: Given Name(s)|name.where(use='official').given
* search: Birth Date|birthDate
* search: Gender|gender
* filter: Name|name:contains
* filter: Gender|gender

> **iHRIS Page Section**
* title: Health Worker
* description: Primary demographic details
* name: Practitioner
* field: Practitioner.name
* field: Practitioner.name.given
* field: Practitioner.name.family
* field: Practitioner.birthDate
* field: Practitioner.gender
* field: Practitioner.extension:residence

> **iHRIS Page Section**
* title: Identifiers
* description: Personal identifiers
* name: identifiers
* field: Practitioner.identifier
* field: Practitioner.identifier.use
* field: Practitioner.identifier.type
* field: Practitioner.identifier.value
* field: Practitioner.identifier.system

> **iHRIS Page Section**
> **url**title
**value**: Position
> **url**description
**value**: Position the person holds
> **url**name
**value**: position
> **url**field
**value**: PractitionerRole.code**resource**: [StructureDefinition iHRIS Test Practitioner Role](StructureDefinition-ihris-test-practitioner-role.md)**linkfield**: PractitionerRole.practitioner
> **column**
* header: Job
* field: PractitionerRole.code.coding[0]

> **column**
* header: Start Date
* field: PractitionerRole.period.start

> **url**resource

**code**: iHRIS Page



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-page-test-practitioner",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "resource",
      "valueReference" : {
        "reference" : "StructureDefinition/ihris-test-practitioner"
      }
    },
    {
      "url" : "search",
      "valueString" : "Surname|name.where(use='official').family"
    },
    {
      "url" : "search",
      "valueString" : "Given Name(s)|name.where(use='official').given"
    },
    {
      "url" : "search",
      "valueString" : "Birth Date|birthDate"
    },
    {
      "url" : "search",
      "valueString" : "Gender|gender"
    },
    {
      "url" : "filter",
      "valueString" : "Name|name:contains"
    },
    {
      "url" : "filter",
      "valueString" : "Gender|gender"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Health Worker"
    },
    {
      "url" : "description",
      "valueString" : "Primary demographic details"
    },
    {
      "url" : "name",
      "valueString" : "Practitioner"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.name"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.name.given"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.name.family"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.birthDate"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.gender"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.extension:residence"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Identifiers"
    },
    {
      "url" : "description",
      "valueString" : "Personal identifiers"
    },
    {
      "url" : "name",
      "valueString" : "identifiers"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.identifier"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.identifier.use"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.identifier.type"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.identifier.value"
    },
    {
      "url" : "field",
      "valueString" : "Practitioner.identifier.system"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Position"
    },
    {
      "url" : "description",
      "valueString" : "Position the person holds"
    },
    {
      "url" : "name",
      "valueString" : "position"
    },
    {
      "url" : "field",
      "valueString" : "PractitionerRole.code"
    },
    {
      "extension" : [{
        "url" : "resource",
        "valueReference" : {
          "reference" : "StructureDefinition/ihris-test-practitioner-role"
        }
      },
      {
        "url" : "linkfield",
        "valueString" : "PractitionerRole.practitioner"
      },
      {
        "extension" : [{
          "url" : "header",
          "valueString" : "Job"
        },
        {
          "url" : "field",
          "valueString" : "PractitionerRole.code.coding[0]"
        }],
        "url" : "column"
      },
      {
        "extension" : [{
          "url" : "header",
          "valueString" : "Start Date"
        },
        {
          "url" : "field",
          "valueString" : "PractitionerRole.period.start"
        }],
        "url" : "column"
      }],
      "url" : "resource"
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
