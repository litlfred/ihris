# iHRIS Parameters Remote Config - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Parameters Remote Config**

## Resource Profile: iHRIS Parameters Remote Config 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-parameters-remote-config | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisParametersRemoteConfig |

 
Configuration Parameters to be loaded from a remote file for iHRIS. 

**Usages:**

* Examples for this Profile: [Parameters/ihris-dashboard](Parameters-ihris-dashboard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-parameters-remote-config.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-parameters-remote-config.csv), [Excel](StructureDefinition-ihris-parameters-remote-config.xlsx), [Schematron](StructureDefinition-ihris-parameters-remote-config.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-parameters-remote-config",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-parameters-remote-config",
  "version" : "0.1.0",
  "name" : "IhrisParametersRemoteConfig",
  "title" : "iHRIS Parameters Remote Config",
  "status" : "active",
  "date" : "2026-10-09T12:31:23+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Configuration Parameters to be loaded from a remote file for iHRIS.",
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
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Parameters",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Parameters",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Parameters",
      "path" : "Parameters"
    },
    {
      "id" : "Parameters.parameter",
      "path" : "Parameters.parameter",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "name"
        }],
        "rules" : "closed"
      },
      "min" : 2,
      "max" : "2"
    },
    {
      "id" : "Parameters.parameter:Signature",
      "path" : "Parameters.parameter",
      "sliceName" : "Signature",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Parameters.parameter:Signature.name",
      "path" : "Parameters.parameter.name",
      "patternString" : "signature"
    },
    {
      "id" : "Parameters.parameter:Signature.value[x]",
      "path" : "Parameters.parameter.value[x]",
      "slicing" : {
        "rules" : "closed"
      },
      "min" : 1,
      "type" : [{
        "code" : "Signature"
      }]
    },
    {
      "id" : "Parameters.parameter:Signature.value[x].type",
      "path" : "Parameters.parameter.value[x].type",
      "max" : "1",
      "patternCoding" : {
        "system" : "urn:iso-astm:E1762-95:2013",
        "code" : "1.2.840.10065.1.12.1.14"
      }
    },
    {
      "id" : "Parameters.parameter:Signature.value[x].data",
      "path" : "Parameters.parameter.value[x].data",
      "min" : 1
    },
    {
      "id" : "Parameters.parameter:Signature.resource",
      "path" : "Parameters.parameter.resource",
      "max" : "0"
    },
    {
      "id" : "Parameters.parameter:Signature.part",
      "path" : "Parameters.parameter.part",
      "max" : "0"
    },
    {
      "id" : "Parameters.parameter:Config",
      "path" : "Parameters.parameter",
      "sliceName" : "Config",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Parameters.parameter:Config.name",
      "path" : "Parameters.parameter.name",
      "patternString" : "config"
    },
    {
      "id" : "Parameters.parameter:Config.value[x]",
      "path" : "Parameters.parameter.value[x]",
      "max" : "0"
    },
    {
      "id" : "Parameters.parameter:Config.resource",
      "path" : "Parameters.parameter.resource",
      "max" : "0"
    },
    {
      "id" : "Parameters.parameter:Config.part",
      "path" : "Parameters.parameter.part",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "name"
        }],
        "rules" : "closed"
      },
      "min" : 1
    },
    {
      "id" : "Parameters.parameter:Config.part:ConfigId",
      "path" : "Parameters.parameter.part",
      "sliceName" : "ConfigId",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Parameters.parameter:Config.part:ConfigId.value[x]",
      "path" : "Parameters.parameter.part.value[x]",
      "slicing" : {
        "rules" : "closed"
      },
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Parameters.parameter:Config.part:ConfigId.resource",
      "path" : "Parameters.parameter.part.resource",
      "max" : "0"
    },
    {
      "id" : "Parameters.parameter:Config.part:ConfigId.part",
      "path" : "Parameters.parameter.part.part",
      "max" : "0"
    }]
  }
}

```
