# Links to the primary resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Links to the primary resource**

## Extension: Links to the primary resource 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/iHRISReportLink | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisReportLink |

Links to the primary resource

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Resources Relationship Profile](StructureDefinition-iHRISRelationship.md)
* Examples for this Extension: [Basic/ihris-es-report-mhero-send-message](Basic-ihris-es-report-mhero-send-message.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-iHRISReportLink.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-iHRISReportLink.csv), [Excel](StructureDefinition-iHRISReportLink.xlsx), [Schematron](StructureDefinition-iHRISReportLink.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "iHRISReportLink",
  "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportLink",
  "version" : "0.1.0",
  "name" : "IhrisReportLink",
  "title" : "Links to the primary resource",
  "status" : "active",
  "date" : "2026-10-09T12:31:23+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Links to the primary resource",
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
      "short" : "Links to the primary resource",
      "definition" : "Links to the primary resource"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 4
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
      "label" : "Unique name of the link",
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
      "label" : "FHIR resource type being linked",
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
      "id" : "Extension.extension:linkElement",
      "path" : "Extension.extension",
      "sliceName" : "linkElement",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:linkElement.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:linkElement.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "linkElement"
    },
    {
      "id" : "Extension.extension:linkElement.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "FHIR path of the field this resource used to link to the relationship",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:linkTo",
      "path" : "Extension.extension",
      "sliceName" : "linkTo",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:linkTo.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:linkTo.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "linkTo"
    },
    {
      "id" : "Extension.extension:linkTo.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "FHIR path to the field of the resource that this resource linked to",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:linkElementSearchParameter",
      "path" : "Extension.extension",
      "sliceName" : "linkElementSearchParameter",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:linkElementSearchParameter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:linkElementSearchParameter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "linkElementSearchParameter"
    },
    {
      "id" : "Extension.extension:linkElementSearchParameter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Search parameter to the resource this resource links to, only for reverse links",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:multiple",
      "path" : "Extension.extension",
      "sliceName" : "multiple",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:multiple.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "multiple"
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
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/iHRISReportLink"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
