# iHRIS Admin Role - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Admin Role**

## Example Basic: iHRIS Admin Role

Profile: [iHRIS Role](StructureDefinition-ihris-role.md)

**iHRIS Basic Name**: Admin Role

**iHRIS Role Primary**: true

**iHRIS Assign Task**: [Basic iHRIS Task](Basic-ihris-task-all-permissions-to-everything.md)

**iHRIS Assign Role**: [Basic iHRIS Role](Basic-ihris-role-open.md)

**code**: iHRIS Role



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-role-admin",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-role"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "Admin Role"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-role-primary",
    "valueBoolean" : true
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-all-permissions-to-everything"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-role",
    "valueReference" : {
      "reference" : "Basic/ihris-role-open"
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
