# iHRIS Data Visualizer - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Data Visualizer**

## Resource Profile: iHRIS Data Visualizer 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-data-visualization | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisDataVisualization |

 
iHRIS Profile of the Basic resource to manage visualizations. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-data-visualization.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-data-visualization.csv), [Excel](StructureDefinition-ihris-data-visualization.xlsx), [Schematron](StructureDefinition-ihris-data-visualization.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-data-visualization",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-data-visualization",
  "version" : "0.1.0",
  "name" : "IhrisDataVisualization",
  "title" : "iHRIS Data Visualizer",
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
  "description" : "iHRIS Profile of the Basic resource to manage visualizations.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Basic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Basic",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Basic",
      "path" : "Basic"
    },
    {
      "id" : "Basic.extension",
      "path" : "Basic.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 5
    },
    {
      "id" : "Basic.extension:name",
      "path" : "Basic.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-basic-name"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:dataset",
      "path" : "Basic.extension",
      "sliceName" : "dataset",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-dataset"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:categories",
      "path" : "Basic.extension",
      "sliceName" : "categories",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-categories"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:series",
      "path" : "Basic.extension",
      "sliceName" : "series",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-series"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:filters",
      "path" : "Basic.extension",
      "sliceName" : "filters",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-filters"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:permissions",
      "path" : "Basic.extension",
      "sliceName" : "permissions",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-permissions"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:settings",
      "path" : "Basic.extension",
      "sliceName" : "settings",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-visualization-settings"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.code",
      "path" : "Basic.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
          "code" : "visualization"
        }]
      }
    }]
  }
}

```
