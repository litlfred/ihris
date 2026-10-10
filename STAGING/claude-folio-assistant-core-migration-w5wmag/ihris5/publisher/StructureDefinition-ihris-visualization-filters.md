# iHRIS Visualization Filters - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Visualization Filters**

## Extension: iHRIS Visualization Filters 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-visualization-filters | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisVisualizationFilters |

iHRIS visualization filters

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-visualization-filters.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-visualization-filters.csv), [Excel](StructureDefinition-ihris-visualization-filters.xlsx), [Schematron](StructureDefinition-ihris-visualization-filters.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-visualization-filters",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-filters",
  "version" : "0.1.0",
  "name" : "IhrisVisualizationFilters",
  "title" : "iHRIS Visualization Filters",
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
  "description" : "iHRIS visualization filters",
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
      "short" : "iHRIS Visualization Filters",
      "definition" : "iHRIS visualization filters"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-filters"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "label" : "Filters",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    }]
  }
}

```
