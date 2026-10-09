# iHRIS Visualization Categories - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Visualization Categories**

## Extension: iHRIS Visualization Categories 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-visualization-categories | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisVisualizationCategories |

iHRIS visualization categories

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-visualization-categories.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-visualization-categories.csv), [Excel](StructureDefinition-ihris-visualization-categories.xlsx), [Schematron](StructureDefinition-ihris-visualization-categories.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-visualization-categories",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-categories",
  "version" : "0.1.0",
  "name" : "IhrisVisualizationCategories",
  "title" : "iHRIS Visualization Categories",
  "status" : "active",
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS visualization categories",
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
    "expression" : "IhrisDataVisualization"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Visualization Categories",
      "definition" : "iHRIS visualization categories"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:name",
      "path" : "Extension.extension",
      "sliceName" : "name",
      "min" : 0,
      "max" : "*",
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
      "label" : "Category Name",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:selectedValues",
      "path" : "Extension.extension",
      "sliceName" : "selectedValues",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:selectedValues.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:selectedValues.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "selectedValues"
    },
    {
      "id" : "Extension.extension:selectedValues.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Filter Categories by Selected Values",
      "min" : 1,
      "type" : [{
        "code" : "base64Binary"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:defaultFilter",
      "path" : "Extension.extension",
      "sliceName" : "defaultFilter",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:defaultFilter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:defaultFilter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "defaultFilter"
    },
    {
      "id" : "Extension.extension:defaultFilter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Categories Default Filter",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filterCondition",
      "path" : "Extension.extension",
      "sliceName" : "filterCondition",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filterCondition.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:filterCondition.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "filterCondition"
    },
    {
      "id" : "Extension.extension:filterCondition.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Categories Filter Condition",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-categories"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
