# iHRIS Task To Read PractitionerRole Page - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Read PractitionerRole Page**

## Example Basic: iHRIS Task To Read PractitionerRole Page

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-ihris-page-practitioner-role

> **Task Attributes**
* permission: read
* resource: Basic
* instance: ihris-page-practitionerrole

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-write-practitioner-role-resource.md)

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-write-practitioner-resource.md)

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-write-location-resource.md)

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-read-ihris-page-practitioner-role",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "read-ihris-page-practitioner-role"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "read"
    },
    {
      "url" : "resource",
      "valueCode" : "Basic"
    },
    {
      "url" : "instance",
      "valueId" : "ihris-page-practitionerrole"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-write-practitioner-role-resource"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-write-practitioner-resource"
    }
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-write-location-resource"
    }
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "task"
    }]
  }
}

```
