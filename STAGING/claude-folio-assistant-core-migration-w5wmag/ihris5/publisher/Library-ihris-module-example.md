# iHRIS Module Example - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Module Example**

## Library: iHRIS Module Example 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/Library/ihris-module-example | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:ihris-example |

* * **Content: **application/javascript: ````Encoded data (4 characters)````: **Id: **
  * ?: ihris-module-example
* * **Content: **application/javascript: ````Encoded data (4 characters)````: **Version: **
  * ?: 0.1.0
* * **Content: **application/javascript: ````Encoded data (4 characters)````: **Url: **
  * ?: [iHRIS Example Module](Library-ihris-module-example.md)
* * **Content: **application/javascript: ````Encoded data (4 characters)````: **Date: **
  * ?: 2026-10-09 11:48:54+0000
* * **Content: **application/javascript: ````Encoded data (4 characters)````: **Publisher: **
  * ?: Luke Duncan



## Resource Content

```json
{
  "resourceType" : "Library",
  "id" : "ihris-module-example",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-module"]
  },
  "url" : "http://ihris.org/fhir/Library/ihris-module-example",
  "version" : "0.1.0",
  "name" : "ihris-example",
  "title" : "iHRIS Example Module",
  "status" : "active",
  "type" : {
    "coding" : [{
      "code" : "logic-library"
    }]
  },
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "author" : [{
    "name" : "Test Author",
    "telecom" : [{
      "system" : "email",
      "value" : "test@ihris.org"
    }]
  }],
  "content" : [{
    "contentType" : "text/x-sig",
    "data" : "TEST",
    "title" : "module-signature"
  },
  {
    "contentType" : "application/javascript",
    "data" : "TEST",
    "title" : "module-code"
  }]
}

```
