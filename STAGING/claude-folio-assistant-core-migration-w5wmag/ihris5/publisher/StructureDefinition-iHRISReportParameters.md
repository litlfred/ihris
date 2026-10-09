# ihRIS Report parameters - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ihRIS Report parameters**

## Extension: ihRIS Report parameters 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/iHRISReportParameters | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisReportParameters |

Lists parameters

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [Details of a report](StructureDefinition-iHRISReportDetails.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-iHRISReportParameters.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-iHRISReportParameters.csv), [Excel](StructureDefinition-iHRISReportParameters.xlsx), [Schematron](StructureDefinition-iHRISReportParameters.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "iHRISReportParameters",
  "url" : "http://ihris.org/fhir/StructureDefinition/iHRISReportParameters",
  "version" : "0.1.0",
  "name" : "IhrisReportParameters",
  "title" : "ihRIS Report parameters",
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
  "description" : "Lists parameters ",
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
      "short" : "ihRIS Report parameters",
      "definition" : "Lists parameters "
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:esFieldName",
      "path" : "Extension.extension",
      "sliceName" : "esFieldName",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:esFieldName.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:esFieldName.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "esFieldName"
    },
    {
      "id" : "Extension.extension:esFieldName.value[x]",
      "path" : "Extension.extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:parameter",
      "path" : "Extension.extension",
      "sliceName" : "parameter",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:parameter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:parameter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "parameter"
    },
    {
      "id" : "Extension.extension:parameter.value[x]",
      "path" : "Extension.extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/iHRISReportParameters"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
