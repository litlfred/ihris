# iHRIS Relationship Example - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Relationship Example**

## Example Basic: iHRIS Relationship Example

Profile: [iHRIS Resources Relationship Profile](StructureDefinition-iHRISRelationship.md)

> **Details of a report**
> **url**name
**value**: mheropractitioner
> **url**label
**value**: Employee List
> **url**resource
**value**: Practitioner
> **url**query
**value**: identifier.system=http://app.rapidpro.io/contact-uuid
> **url**displayCheckbox
**value**: true**name**: fullname**fhirpath**: name.where(use='official').last().text**Display Name**: Fullname**filter**: true**dropDownFilter**: false
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)
**name**: phone**fhirpath**: telecom.where(system='phone').value**Display Name**: Phone Number
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)

> **Links to the primary resource**
> **url**name
**value**: facility
> **url**resource
**value**: Location
> **url**linkElement
**value**: Location.id
> **url**linkTo
**value**: role.location
> **url**linkElementSearchParameter
**value**: practitioner
> **url**multiple
**value**: false**name**: facilityName**fhirpath**: name**Display Name**: Facility**filter**: true**dropDownFilter**: true
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)

**code**: iHRIS Relationship



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-es-report-mhero-send-message",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISRelationship"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "name",
      "valueString" : "mheropractitioner"
    },
    {
      "url" : "label",
      "valueString" : "Employee List"
    },
    {
      "url" : "resource",
      "valueString" : "Practitioner"
    },
    {
      "url" : "query",
      "valueString" : "identifier.system=http://app.rapidpro.io/contact-uuid"
    },
    {
      "url" : "displayCheckbox",
      "valueBoolean" : true
    },
    {
      "extension" : [{
        "url" : "name",
        "valueString" : "fullname"
      },
      {
        "url" : "fhirpath",
        "valueString" : "name.where(use='official').last().text"
      },
      {
        "url" : "display",
        "valueString" : "Fullname"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "dropDownFilter",
        "valueBoolean" : false
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "extension" : [{
        "url" : "name",
        "valueString" : "phone"
      },
      {
        "url" : "fhirpath",
        "valueString" : "telecom.where(system='phone').value"
      },
      {
        "url" : "display",
        "valueString" : "Phone Number"
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportDetails"
  },
  {
    "extension" : [{
      "url" : "name",
      "valueString" : "facility"
    },
    {
      "url" : "resource",
      "valueString" : "Location"
    },
    {
      "url" : "linkElement",
      "valueString" : "Location.id"
    },
    {
      "url" : "linkTo",
      "valueString" : "role.location"
    },
    {
      "url" : "linkElementSearchParameter",
      "valueString" : "practitioner"
    },
    {
      "url" : "multiple",
      "valueBoolean" : false
    },
    {
      "extension" : [{
        "url" : "name",
        "valueString" : "facilityName"
      },
      {
        "url" : "fhirpath",
        "valueString" : "name"
      },
      {
        "url" : "display",
        "valueString" : "Facility"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "dropDownFilter",
        "valueBoolean" : true
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportLink"
  }],
  "code" : {
    "text" : "iHRIS Relationship"
  }
}

```
