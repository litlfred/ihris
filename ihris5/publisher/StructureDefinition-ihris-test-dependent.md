# iHRIS Practitioner Dependent Detail - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Practitioner Dependent Detail**

## Extension: iHRIS Practitioner Dependent Detail 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-test-dependent | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisTestDependent |

iHRIS Test extension for Practitioner Dependent Detail.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [IhrisTestPractitioner](StructureDefinition-ihris-test-practitioner.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-test-dependent.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-test-dependent.csv), [Excel](StructureDefinition-ihris-test-dependent.xlsx), [Schematron](StructureDefinition-ihris-test-dependent.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-test-dependent",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-test-dependent",
  "version" : "0.1.0",
  "name" : "IhrisTestDependent",
  "title" : "iHRIS Practitioner Dependent Detail",
  "status" : "active",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Test extension for Practitioner Dependent Detail.",
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
      "short" : "iHRIS Practitioner Dependent Detail",
      "definition" : "iHRIS Test extension for Practitioner Dependent Detail."
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
      "label" : "Dependent's Name",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:birthDate",
      "path" : "Extension.extension",
      "sliceName" : "birthDate",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:birthDate.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:birthDate.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "birthDate"
    },
    {
      "id" : "Extension.extension:birthDate.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Dependent's Date of Birth",
      "min" : 1,
      "type" : [{
        "code" : "date"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:gender",
      "path" : "Extension.extension",
      "sliceName" : "gender",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:gender.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:gender.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "gender"
    },
    {
      "id" : "Extension.extension:gender.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Dependent's Gender",
      "min" : 1,
      "type" : [{
        "code" : "code"
      }],
      "mustSupport" : true,
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hl7.org/fhir/ValueSet/administrative-gender"
      }
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-test-dependent"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
