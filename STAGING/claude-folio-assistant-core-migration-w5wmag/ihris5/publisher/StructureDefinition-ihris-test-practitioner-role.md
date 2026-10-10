# iHRIS Test Practitioner Role - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Test Practitioner Role**

## Resource Profile: iHRIS Test Practitioner Role 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-test-practitioner-role | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisTestPractitionerRole |

 
iHRIS Test profile of Practitioner Role. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-test-practitioner-role.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-test-practitioner-role.csv), [Excel](StructureDefinition-ihris-test-practitioner-role.xlsx), [Schematron](StructureDefinition-ihris-test-practitioner-role.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-test-practitioner-role",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-test-practitioner-role",
  "version" : "0.1.0",
  "name" : "IhrisTestPractitionerRole",
  "title" : "iHRIS Test Practitioner Role",
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
  "description" : "iHRIS Test profile of Practitioner Role.",
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
  "type" : "PractitionerRole",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/PractitionerRole",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "PractitionerRole",
      "path" : "PractitionerRole"
    },
    {
      "id" : "PractitionerRole.identifier",
      "path" : "PractitionerRole.identifier",
      "label" : "Identifier",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.identifier.use",
      "path" : "PractitionerRole.identifier.use",
      "label" : "Use",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.identifier.type",
      "path" : "PractitionerRole.identifier.type",
      "label" : "Type",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.identifier.type.coding",
      "path" : "PractitionerRole.identifier.type.coding",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.identifier.system",
      "path" : "PractitionerRole.identifier.system",
      "label" : "System",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.identifier.value",
      "path" : "PractitionerRole.identifier.value",
      "label" : "Value",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.active",
      "path" : "PractitionerRole.active",
      "label" : "Active",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.period",
      "path" : "PractitionerRole.period",
      "label" : "Period of Employment",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.period.start",
      "path" : "PractitionerRole.period.start",
      "label" : "Start Date",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.period.end",
      "path" : "PractitionerRole.period.end",
      "label" : "End Date",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.practitioner",
      "path" : "PractitionerRole.practitioner",
      "label" : "Health Worker",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.code",
      "path" : "PractitionerRole.code",
      "label" : "Job",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true,
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://ihris.org/fhir/ValueSet/ihris-job"
      }
    },
    {
      "id" : "PractitionerRole.code.coding",
      "path" : "PractitionerRole.code.coding",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.specialty",
      "path" : "PractitionerRole.specialty",
      "label" : "Specialty",
      "mustSupport" : true
    },
    {
      "id" : "PractitionerRole.location",
      "path" : "PractitionerRole.location",
      "label" : "Facility",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    }]
  }
}

```
