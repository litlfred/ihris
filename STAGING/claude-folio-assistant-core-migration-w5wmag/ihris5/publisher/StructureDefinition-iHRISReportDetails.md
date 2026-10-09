# Details of a report - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Details of a report**

## Extension: Details of a report 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/iHRISReportDetails | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisReportDetails |

Defines the primary resource of the relationship

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Resources Relationship Profile](StructureDefinition-iHRISRelationship.md) and [iHRIS Report](StructureDefinition-ihris-report.md)
* Examples for this Extension: [Basic/ihris-es-report-mhero-send-message](Basic-ihris-es-report-mhero-send-message.md) and [Basic/ihris-es-report-staff-directorate](Basic-ihris-es-report-staff-directorate.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-iHRISReportDetails.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-iHRISReportDetails.csv), [Excel](StructureDefinition-iHRISReportDetails.xlsx), [Schematron](StructureDefinition-iHRISReportDetails.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "iHRISReportDetails",
  "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportDetails",
  "version" : "0.1.0",
  "name" : "IhrisReportDetails",
  "title" : "Details of a report",
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
  "description" : "Defines the primary resource of the relationship",
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
    "expression" : "Basic"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "Details of a report",
      "definition" : "Defines the primary resource of the relationship"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 3
    },
    {
      "id" : "Extension.extension:name",
      "path" : "Extension.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:name.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:name.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "name"
    },
    {
      "id" : "Extension.extension:name.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Unique name of the primary resource in the relationship",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:label",
      "path" : "Extension.extension",
      "sliceName" : "label",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:label.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:label.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "label"
    },
    {
      "id" : "Extension.extension:label.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Relationship title",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:resource",
      "path" : "Extension.extension",
      "sliceName" : "resource",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resource"
    },
    {
      "id" : "Extension.extension:resource.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Resource type of the primary resource",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:resourcePage",
      "path" : "Extension.extension",
      "sliceName" : "resourcePage",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resourcePage.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resourcePage.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resourcePage"
    },
    {
      "id" : "Extension.extension:resourcePage.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Resource Page to display the data on click",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:resourcePageID",
      "path" : "Extension.extension",
      "sliceName" : "resourcePageID",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resourcePageID.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resourcePageID.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resourcePageID"
    },
    {
      "id" : "Extension.extension:resourcePageID.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Resource ID of the resource to display the data on click",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:parameters",
      "path" : "Extension.extension",
      "sliceName" : "parameters",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISReportParameters"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:initialFilter",
      "path" : "Extension.extension",
      "sliceName" : "initialFilter",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:initialFilter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:initialFilter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "initialFilter"
    },
    {
      "id" : "Extension.extension:initialFilter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Initial Profile filter to limit instances of this resource",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:query",
      "path" : "Extension.extension",
      "sliceName" : "query",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:query.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:query.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "query"
    },
    {
      "id" : "Extension.extension:query.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "FHIR path to limit instances of this resource",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:cachingDisabled",
      "path" : "Extension.extension",
      "sliceName" : "cachingDisabled",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:cachingDisabled.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:cachingDisabled.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "cachingDisabled"
    },
    {
      "id" : "Extension.extension:cachingDisabled.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Disable caching data for this relationship",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "Extension.extension:displayCheckbox",
      "path" : "Extension.extension",
      "sliceName" : "displayCheckbox",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:displayCheckbox.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:displayCheckbox.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "displayCheckbox"
    },
    {
      "id" : "Extension.extension:displayCheckbox.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Whether rows of the report are selectable or not",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "Extension.extension:locationBasedConstraint",
      "path" : "Extension.extension",
      "sliceName" : "locationBasedConstraint",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:locationBasedConstraint.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:locationBasedConstraint.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "locationBasedConstraint"
    },
    {
      "id" : "Extension.extension:locationBasedConstraint.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Whether rows of the report are are limited by location or not",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "Extension.extension:reportelement",
      "path" : "Extension.extension",
      "sliceName" : "reportelement",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISReportElement"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/iHRISReportDetails"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
