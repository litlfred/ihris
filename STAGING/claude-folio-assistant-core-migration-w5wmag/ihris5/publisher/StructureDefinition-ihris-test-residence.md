# iHRIS Practitioner Residence - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Practitioner Residence**

## Extension: iHRIS Practitioner Residence 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-test-residence | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisTestResidence |

iHRIS Test extension for Practitioner residence.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [IhrisTestPractitioner](StructureDefinition-ihris-test-practitioner.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-test-residence.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-test-residence.csv), [Excel](StructureDefinition-ihris-test-residence.xlsx), [Schematron](StructureDefinition-ihris-test-residence.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-test-residence",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-test-residence",
  "version" : "0.1.0",
  "name" : "IhrisTestResidence",
  "title" : "iHRIS Practitioner Residence",
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
  "description" : "iHRIS Test extension for Practitioner residence.",
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
    "expression" : "Practitioner"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Practitioner Residence",
      "definition" : "iHRIS Test extension for Practitioner residence."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-test-residence"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "label" : "Residence",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/Location"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.value[x].reference",
      "path" : "Extension.value[x].reference",
      "label" : "Location",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Extension.value[x].type",
      "path" : "Extension.value[x].type",
      "max" : "0"
    },
    {
      "id" : "Extension.value[x].identifier",
      "path" : "Extension.value[x].identifier",
      "max" : "0"
    },
    {
      "id" : "Extension.value[x].display",
      "path" : "Extension.value[x].display",
      "max" : "0"
    }]
  }
}

```
