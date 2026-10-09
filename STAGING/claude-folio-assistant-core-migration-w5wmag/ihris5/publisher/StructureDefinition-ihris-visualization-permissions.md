# iHRIS Visualization Permissions - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Visualization Permissions**

## Extension: iHRIS Visualization Permissions 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-visualization-permissions | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisVisualizationPermissions |

iHRIS Visualization Permissions

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-visualization-permissions.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-visualization-permissions.csv), [Excel](StructureDefinition-ihris-visualization-permissions.xlsx), [Schematron](StructureDefinition-ihris-visualization-permissions.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-visualization-permissions",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-permissions",
  "version" : "0.1.0",
  "name" : "IhrisVisualizationPermissions",
  "title" : "iHRIS Visualization Permissions",
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
  "description" : "iHRIS Visualization Permissions",
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
      "short" : "iHRIS Visualization Permissions",
      "definition" : "iHRIS Visualization Permissions"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:shared",
      "path" : "Extension.extension",
      "sliceName" : "shared",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:shared.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:shared.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "shared"
    },
    {
      "id" : "Extension.extension:shared.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Visualization Sharing",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-visualization-permissions"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
