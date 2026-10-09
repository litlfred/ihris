# iHRIS Task To Write DocumentReference - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Write DocumentReference**

## Example Basic: iHRIS Task To Write DocumentReference

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: write-document-reference

> **Task Attributes**
* permission: write
* resource: DocumentReference
* constraint: category.exists(coding.exists(code = 'open'))

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-read-document-reference.md)

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-write-document-reference",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "write-document-reference"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "write"
    },
    {
      "url" : "resource",
      "valueCode" : "DocumentReference"
    },
    {
      "url" : "constraint",
      "valueString" : "category.exists(coding.exists(code = 'open'))"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-document-reference"
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
