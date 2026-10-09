# iHRIS Resource Relationships - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Resource Relationships**

## Extension: iHRIS Resource Relationships 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-resource-relationships | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisResourceRelationships |

iHRIS Resource Relationships

**Context of Use**

**Usage info**

**Usages:**

* This Extension is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-resource-relationships.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-resource-relationships.csv), [Excel](StructureDefinition-ihris-resource-relationships.xlsx), [Schematron](StructureDefinition-ihris-resource-relationships.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-resource-relationships",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-resource-relationships",
  "version" : "0.1.0",
  "name" : "IhrisResourceRelationships",
  "title" : "iHRIS Resource Relationships",
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
  "description" : "iHRIS Resource Relationships",
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
    "expression" : "IhrisResourceRelationships"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Resource Relationships",
      "definition" : "iHRIS Resource Relationships"
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
      "label" : "Resource Name",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/StructureDefinition"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field",
      "path" : "Extension.extension",
      "sliceName" : "field",
      "min" : 1,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:field.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Report Fields",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filter",
      "path" : "Extension.extension",
      "sliceName" : "filter",
      "min" : 1,
      "max" : "*",
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
      "label" : "Data filters",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
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
      "label" : "Query to Include Resource",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-resource-relationships"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
