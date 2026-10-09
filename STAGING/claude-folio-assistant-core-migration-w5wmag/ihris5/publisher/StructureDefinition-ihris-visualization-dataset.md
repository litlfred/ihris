# iHRIS Visualization Dataset - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Visualization Dataset**

## Extension: iHRIS Visualization Dataset 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-visualization-dataset | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisVisualizationDataset |

iHRIS visualization dataset

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-visualization-dataset.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-visualization-dataset.csv), [Excel](StructureDefinition-ihris-visualization-dataset.xlsx), [Schematron](StructureDefinition-ihris-visualization-dataset.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-visualization-dataset",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-dataset",
  "version" : "0.1.0",
  "name" : "IhrisVisualizationDataset",
  "title" : "iHRIS Visualization Dataset",
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
  "description" : "iHRIS visualization dataset",
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
      "short" : "iHRIS Visualization Dataset",
      "definition" : "iHRIS visualization dataset"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:id",
      "path" : "Extension.extension",
      "sliceName" : "id",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:id.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:id.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "id"
    },
    {
      "id" : "Extension.extension:id.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Dataset ID",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
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
      "label" : "Dataset Name",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-dataset"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
