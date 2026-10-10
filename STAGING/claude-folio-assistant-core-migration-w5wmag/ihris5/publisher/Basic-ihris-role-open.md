# iHRIS Open Role - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Open Role**

## Example Basic: iHRIS Open Role

Profile: [iHRIS Role](StructureDefinition-ihris-role.md)

**iHRIS Basic Name**: Open Role

**iHRIS Role Primary**: true

**iHRIS Assign Task**: [Basic iHRIS Task](Basic-ihris-task-read-structure-definition.md)

**iHRIS Assign Task**: [Basic iHRIS Task](Basic-ihris-task-read-code-system.md)

**iHRIS Assign Task**: [Basic iHRIS Task](Basic-ihris-task-read-value-set.md)

**iHRIS Assign Task**: [Basic iHRIS Task](Basic-ihris-task-read-document-reference.md)

**code**: iHRIS Role



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-role-open",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-role"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "Open Role"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-role-primary",
    "valueBoolean" : true
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-structure-definition"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-code-system"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-value-set"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-document-reference"
    }
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "role"
    }]
  }
}

```
