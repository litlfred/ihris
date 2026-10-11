# Roles - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Roles**

## Example Basic: Roles

Profile: [iHRIS Page](StructureDefinition-ihris-page.md)

> **iHRIS Page Display**
> **url**resource
**value**: [StructureDefinition iHRIS Role](StructureDefinition-ihris-role.md)
> **url**search
**value**: Id|Basic.id**field**: Basic.id**text**: Edit**url**: /questionnaire/ihris-role/role/FIELD**button**: true**icon**: mdi-pencil**class**: secondary
> **url**link
**field**: **text**: View Other Roles**url**: /resource/search/role**button**: true**icon**: mdi-account-arrow-right
> **url**link
**url**: /questionnaire/ihris-role/role**icon**: mdi-account-plus**class**: accent
> **url**add

> **url**search
**value**: Name|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-basic-name').valueString
> **url**search
**value**: Role Reference|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-assign-role').valueReference.reference
> **url**[FilterSearchParameter](filter)
**value**: Role|Basic.extension:id:contains

> **iHRIS Page Section**
* title: Role
* description: System User Role details
* name: Basic
* field: Basic.extension:name.value[x]:valueString
* field: Basic.extension:role.value[x]:valueReference
* field: Basic.extension:task.value[x]:valueReference
* field: Basic.extension:primary.value[x]:valueBoolean

**code**: iHRIS Page



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-page-role",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "resource",
      "valueReference" : {
        "reference" : "StructureDefinition/ihris-role"
      }
    },
    {
      "url" : "search",
      "valueString" : "Id|Basic.id"
    },
    {
      "extension" : [{
        "url" : "field",
        "valueString" : "Basic.id"
      },
      {
        "url" : "text",
        "valueString" : "Edit"
      },
      {
        "url" : "displayIn"
      },
      {
        "url" : "url",
        "valueUrl" : "/questionnaire/ihris-role/role/FIELD"
      },
      {
        "url" : "button",
        "valueBoolean" : true
      },
      {
        "url" : "icon",
        "valueString" : "mdi-pencil"
      },
      {
        "url" : "class",
        "valueString" : "secondary"
      }],
      "url" : "link"
    },
    {
      "extension" : [{
        "url" : "field",
        "valueString" : ""
      },
      {
        "url" : "text",
        "valueString" : "View Other Roles"
      },
      {
        "url" : "displayIn"
      },
      {
        "url" : "url",
        "valueUrl" : "/resource/search/role"
      },
      {
        "url" : "button",
        "valueBoolean" : true
      },
      {
        "url" : "icon",
        "valueString" : "mdi-account-arrow-right"
      }],
      "url" : "link"
    },
    {
      "extension" : [{
        "url" : "url",
        "valueUrl" : "/questionnaire/ihris-role/role"
      },
      {
        "url" : "icon",
        "valueString" : "mdi-account-plus"
      },
      {
        "url" : "class",
        "valueString" : "accent"
      }],
      "url" : "add"
    },
    {
      "url" : "search",
      "valueString" : "Name|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-basic-name').valueString"
    },
    {
      "url" : "search",
      "valueString" : "Role Reference|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-assign-role').valueReference.reference"
    },
    {
      "url" : "filter",
      "valueString" : "Role|Basic.extension:id:contains"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Role"
    },
    {
      "url" : "description",
      "valueString" : "System User Role details"
    },
    {
      "url" : "name",
      "valueString" : "Basic"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:name.value[x]:valueString"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:role.value[x]:valueReference"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:task.value[x]:valueReference"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:primary.value[x]:valueBoolean"
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
