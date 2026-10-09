# IhrisTestPractitioner - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **IhrisTestPractitioner**

## Resource Profile: IhrisTestPractitioner 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-test-practitioner | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisTestPractitioner |

 
iHRIS profile of Practitioner for tests. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-test-practitioner.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-test-practitioner.csv), [Excel](StructureDefinition-ihris-test-practitioner.xlsx), [Schematron](StructureDefinition-ihris-test-practitioner.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-test-practitioner",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-test-practitioner",
  "version" : "0.1.0",
  "name" : "IhrisTestPractitioner",
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
  "description" : "iHRIS profile of Practitioner for tests.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "servd",
    "uri" : "http://www.omg.org/spec/ServD/1.0/",
    "name" : "ServD"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Practitioner",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Practitioner",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Practitioner",
      "path" : "Practitioner"
    },
    {
      "id" : "Practitioner.extension",
      "path" : "Practitioner.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Practitioner.extension:residence",
      "path" : "Practitioner.extension",
      "sliceName" : "residence",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-test-residence"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.extension:dependent",
      "path" : "Practitioner.extension",
      "sliceName" : "dependent",
      "label" : "Dependent Details",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-test-dependent"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier",
      "path" : "Practitioner.identifier",
      "label" : "Identifier",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier.use",
      "path" : "Practitioner.identifier.use",
      "label" : "Use",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier.type",
      "path" : "Practitioner.identifier.type",
      "label" : "Type",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier.type.coding",
      "path" : "Practitioner.identifier.type.coding",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier.system",
      "path" : "Practitioner.identifier.system",
      "label" : "System",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.identifier.value",
      "path" : "Practitioner.identifier.value",
      "label" : "Value",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name",
      "path" : "Practitioner.name",
      "label" : "Name",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name.use",
      "path" : "Practitioner.name.use",
      "label" : "Use",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name.family",
      "path" : "Practitioner.name.family",
      "label" : "Family",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name.given",
      "path" : "Practitioner.name.given",
      "label" : "Given Name",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name.prefix",
      "path" : "Practitioner.name.prefix",
      "label" : "Prefix",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.name.suffix",
      "path" : "Practitioner.name.suffix",
      "label" : "Suffix",
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.gender",
      "path" : "Practitioner.gender",
      "label" : "Gender",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Practitioner.birthDate",
      "path" : "Practitioner.birthDate",
      "label" : "Birth Date",
      "mustSupport" : true
    }]
  }
}

```
