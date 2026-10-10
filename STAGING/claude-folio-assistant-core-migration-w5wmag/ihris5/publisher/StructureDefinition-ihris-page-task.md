# iHRIS Page Task - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Page Task**

## Extension: iHRIS Page Task 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-page-task | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisPageTask |

iHRIS Page Task details.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Page](StructureDefinition-ihris-page.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-page-task.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-page-task.csv), [Excel](StructureDefinition-ihris-page-task.xlsx), [Schematron](StructureDefinition-ihris-page-task.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-page-task",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-task",
  "version" : "0.1.0",
  "name" : "IhrisPageTask",
  "title" : "iHRIS Page Task",
  "status" : "active",
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Page Task details.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "IhrisPage"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Page Task",
      "definition" : "iHRIS Page Task details."
    },
    {
      "id" : "Extension.extension:view",
      "path" : "Extension.extension",
      "sliceName" : "view",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:view.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:view.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "view"
    },
    {
      "id" : "Extension.extension:view.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "View Page Task",
      "min" : 1,
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:create",
      "path" : "Extension.extension",
      "sliceName" : "create",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:create.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:create.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "create"
    },
    {
      "id" : "Extension.extension:create.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Create Page Task",
      "min" : 1,
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:update",
      "path" : "Extension.extension",
      "sliceName" : "update",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:update.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:update.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "update"
    },
    {
      "id" : "Extension.extension:update.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Update Page Task",
      "min" : 1,
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:delete",
      "path" : "Extension.extension",
      "sliceName" : "delete",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:delete.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:delete.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "delete"
    },
    {
      "id" : "Extension.extension:delete.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Delete Page Task",
      "min" : 1,
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-page-task"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
