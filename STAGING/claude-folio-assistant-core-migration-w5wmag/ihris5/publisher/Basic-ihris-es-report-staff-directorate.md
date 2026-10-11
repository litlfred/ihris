# ihris-es-report-staff-directorate - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ihris-es-report-staff-directorate**

## Example Basic: ihris-es-report-staff-directorate

> **Details of a report**
> **url**label
**value**: Staff Directorate
> **url**displayCheckbox
**value**: false
> **url**name
**value**: staffdirectorate
> **url**locationBasedConstraint
**value**: true
> **url**resource
**value**: Practitioner
> **url**resourcePage
**value**: practitioner**Display Name**: Fullname**name**: fullname
> **displayformat**
* format: %s, %s
* order: given, family
* paths:given:fhirpath: name.where(use='official').given
* paths:given:join: -
* paths:family:fhirpath: name.where(use='official').family

**filter**: true**dropDownFilter**: false**order**: 0
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)
**Display Name**: Gender**name**: gender**fhirpath**: gender**filter**: true**dropDownFilter**: true**order**: 1
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)
**Display Name**: Date of Birth**name**: dob**fhirpath**: birthDate**filter**: true**dropDownFilter**: false**order**: 4
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)
**Display Name**: Phone Number**name**: phone**fhirpath**: telecom.where(system='phone').value**filter**: true**order**: 2
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)
**name**: ihris-related-group**fhirpath**: extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension.where(url='location').valueString
> **url**[Resource Fields](StructureDefinition-iHRISReportElement.md)

**code**: iHRISRelationship



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-es-report-staff-directorate",
  "extension" : [{
    "extension" : [{
      "url" : "label",
      "valueString" : "Staff Directorate"
    },
    {
      "url" : "displayCheckbox",
      "valueBoolean" : false
    },
    {
      "url" : "name",
      "valueString" : "staffdirectorate"
    },
    {
      "url" : "locationBasedConstraint",
      "valueBoolean" : true
    },
    {
      "url" : "resource",
      "valueString" : "Practitioner"
    },
    {
      "url" : "resourcePage",
      "valueString" : "practitioner"
    },
    {
      "extension" : [{
        "url" : "display",
        "valueString" : "Fullname"
      },
      {
        "url" : "name",
        "valueString" : "fullname"
      },
      {
        "extension" : [{
          "url" : "format",
          "valueString" : "%s, %s"
        },
        {
          "url" : "order",
          "valueString" : "given, family"
        },
        {
          "url" : "paths:given:fhirpath",
          "valueString" : "name.where(use='official').given"
        },
        {
          "url" : "paths:given:join",
          "valueString" : "-"
        },
        {
          "url" : "paths:family:fhirpath",
          "valueString" : "name.where(use='official').family"
        }],
        "url" : "displayformat"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "dropDownFilter",
        "valueBoolean" : false
      },
      {
        "url" : "order",
        "valueInteger" : 0
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "extension" : [{
        "url" : "display",
        "valueString" : "Gender"
      },
      {
        "url" : "name",
        "valueString" : "gender"
      },
      {
        "url" : "fhirpath",
        "valueString" : "gender"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "dropDownFilter",
        "valueBoolean" : true
      },
      {
        "url" : "order",
        "valueInteger" : 1
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "extension" : [{
        "url" : "display",
        "valueString" : "Date of Birth"
      },
      {
        "url" : "name",
        "valueString" : "dob"
      },
      {
        "url" : "fhirpath",
        "valueString" : "birthDate"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "dropDownFilter",
        "valueBoolean" : false
      },
      {
        "url" : "order",
        "valueInteger" : 4
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "extension" : [{
        "url" : "display",
        "valueString" : "Phone Number"
      },
      {
        "url" : "name",
        "valueString" : "phone"
      },
      {
        "url" : "fhirpath",
        "valueString" : "telecom.where(system='phone').value"
      },
      {
        "url" : "filter",
        "valueBoolean" : true
      },
      {
        "url" : "order",
        "valueInteger" : 2
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "extension" : [{
        "url" : "name",
        "valueString" : "ihris-related-group"
      },
      {
        "url" : "fhirpath",
        "valueString" : "extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension.where(url='location').valueString"
      }],
      "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportDetails"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/ValueSet/ihris-resource",
      "code" : "iHRISRelationship"
    }],
    "text" : "iHRISRelationship"
  }
}

```
