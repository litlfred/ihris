# iHRIS Dashboard Visualization - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Dashboard Visualization**

## Extension: iHRIS Dashboard Visualization 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-dashboard-visualization | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisDashboardVisualization |

iHRIS Dashboard Visualization

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Dashboard](StructureDefinition-ihris-dashboard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-dashboard-visualization.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-dashboard-visualization.csv), [Excel](StructureDefinition-ihris-dashboard-visualization.xlsx), [Schematron](StructureDefinition-ihris-dashboard-visualization.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-dashboard-visualization",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-dashboard-visualization",
  "version" : "0.1.0",
  "name" : "IhrisDashboardVisualization",
  "title" : "iHRIS Dashboard Visualization",
  "status" : "active",
  "date" : "2026-10-09T12:24:25+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Dashboard Visualization",
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
    "expression" : "IhrisDashboard"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Dashboard Visualization",
      "definition" : "iHRIS Dashboard Visualization"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 8
    },
    {
      "id" : "Extension.extension:vizID",
      "path" : "Extension.extension",
      "sliceName" : "vizID",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:vizID.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:vizID.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "vizID"
    },
    {
      "id" : "Extension.extension:vizID.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization ID",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:horizontal",
      "path" : "Extension.extension",
      "sliceName" : "horizontal",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:horizontal.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:horizontal.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "horizontal"
    },
    {
      "id" : "Extension.extension:horizontal.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Horizontal Position",
      "min" : 1,
      "type" : [{
        "code" : "decimal"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:vertical",
      "path" : "Extension.extension",
      "sliceName" : "vertical",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:vertical.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:vertical.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "vertical"
    },
    {
      "id" : "Extension.extension:vertical.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Vertical Position",
      "min" : 1,
      "type" : [{
        "code" : "decimal"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:width",
      "path" : "Extension.extension",
      "sliceName" : "width",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:width.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:width.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "width"
    },
    {
      "id" : "Extension.extension:width.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Width Position",
      "min" : 1,
      "type" : [{
        "code" : "decimal"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:height",
      "path" : "Extension.extension",
      "sliceName" : "height",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:height.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:height.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "height"
    },
    {
      "id" : "Extension.extension:height.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Height Position",
      "min" : 1,
      "type" : [{
        "code" : "decimal"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:heightPx",
      "path" : "Extension.extension",
      "sliceName" : "heightPx",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:heightPx.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:heightPx.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "heightPx"
    },
    {
      "id" : "Extension.extension:heightPx.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Height Position In Pixel",
      "min" : 1,
      "type" : [{
        "code" : "decimal"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:itemID",
      "path" : "Extension.extension",
      "sliceName" : "itemID",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:itemID.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:itemID.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "itemID"
    },
    {
      "id" : "Extension.extension:itemID.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Unique ID On The Dashboard",
      "min" : 1,
      "type" : [{
        "code" : "integer"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:static",
      "path" : "Extension.extension",
      "sliceName" : "static",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:static.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:static.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "static"
    },
    {
      "id" : "Extension.extension:static.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Whether Visualization Can Be Moved or Not",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-dashboard-visualization"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
