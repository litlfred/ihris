# Resource Fields - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Resource Fields**

## Extension: Resource Fields 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/iHRISReportElement | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisReportElement |

Lists fields of a resource to be displayed/cached

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [Details of a report](StructureDefinition-iHRISReportDetails.md) and [Links to the primary resource](StructureDefinition-iHRISReportLink.md)
* Examples for this Extension: [Basic/ihris-es-report-mhero-send-message](Basic-ihris-es-report-mhero-send-message.md) and [Basic/ihris-es-report-staff-directorate](Basic-ihris-es-report-staff-directorate.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-iHRISReportElement.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-iHRISReportElement.csv), [Excel](StructureDefinition-iHRISReportElement.xlsx), [Schematron](StructureDefinition-iHRISReportElement.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "iHRISReportElement",
  "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement",
  "version" : "0.1.0",
  "name" : "IhrisReportElement",
  "title" : "Resource Fields",
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
  "description" : "Lists fields of a resource to be displayed/cached",
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
    "expression" : "Element"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "Resource Fields",
      "definition" : "Lists fields of a resource to be displayed/cached"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:fhirpath",
      "path" : "Extension.extension",
      "sliceName" : "fhirpath",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:fhirpath.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:fhirpath.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "fhirpath"
    },
    {
      "id" : "Extension.extension:fhirpath.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "FHIR path to the field",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:function",
      "path" : "Extension.extension",
      "sliceName" : "function",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:function.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:function.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "function"
    },
    {
      "id" : "Extension.extension:function.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "External function to be called to calculate value",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:script",
      "path" : "Extension.extension",
      "sliceName" : "script",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:script.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:script.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "script"
    },
    {
      "id" : "Extension.extension:script.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Elasticsearch script to calculate field value",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
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
      "label" : "Name of the field unique to the relationship",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:type",
      "path" : "Extension.extension",
      "sliceName" : "type",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:type.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:type.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "type"
    },
    {
      "id" : "Extension.extension:type.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Data Type",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:display",
      "path" : "Extension.extension",
      "sliceName" : "display",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:display.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:display.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "display"
    },
    {
      "id" : "Extension.extension:display.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Human readable name if the relation is to be displayed on the UI",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:displayformat",
      "path" : "Extension.extension",
      "sliceName" : "displayformat",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:displayformat.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "displayformat"
    },
    {
      "id" : "Extension.extension:filter",
      "path" : "Extension.extension",
      "sliceName" : "filter",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:filter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "filter"
    },
    {
      "id" : "Extension.extension:filter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Display as a filter",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "Extension.extension:dropDownFilter",
      "path" : "Extension.extension",
      "sliceName" : "dropDownFilter",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:dropDownFilter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:dropDownFilter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "dropDownFilter"
    },
    {
      "id" : "Extension.extension:dropDownFilter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Display as a dropdown filter",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "Extension.extension:order",
      "path" : "Extension.extension",
      "sliceName" : "order",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:order.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:order.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "order"
    },
    {
      "id" : "Extension.extension:order.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Order of the Field",
      "min" : 1,
      "type" : [{
        "code" : "integer"
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/iHRISReportElement"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
