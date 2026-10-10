# iHRIS Page Display - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Page Display**

## Extension: iHRIS Page Display 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-page-display | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisPageDisplay |

iHRIS Page Display details.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Page](StructureDefinition-ihris-page.md)
* Examples for this Extension: [Basic/ihris-page-auditevent](Basic-ihris-page-auditevent.md), [Basic/ihris-page-role](Basic-ihris-page-role.md), [Basic/ihris-page-task](Basic-ihris-page-task.md), [Basic/ihris-page-test-codesystem](Basic-ihris-page-test-codesystem.md) and [Basic/ihris-page-test-practitioner](Basic-ihris-page-test-practitioner.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-page-display.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-page-display.csv), [Excel](StructureDefinition-ihris-page-display.xlsx), [Schematron](StructureDefinition-ihris-page-display.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-page-display",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display",
  "version" : "0.1.0",
  "name" : "IhrisPageDisplay",
  "title" : "iHRIS Page Display",
  "status" : "active",
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Page Display details.",
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
    "expression" : "IhrisPage"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Page Display",
      "definition" : "iHRIS Page Display details."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:resource",
      "path" : "Extension.extension",
      "sliceName" : "resource",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resource"
    },
    {
      "id" : "Extension.extension:resource.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Primary Resource",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/StructureDefinition",
        "http://hl7.org/fhir/StructureDefinition/CodeSystem"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:search",
      "path" : "Extension.extension",
      "sliceName" : "search",
      "min" : 1,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:search.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:search.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "search"
    },
    {
      "id" : "Extension.extension:search.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Search Headers",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filter",
      "path" : "Extension.extension",
      "sliceName" : "filter",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:filter.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:filter.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "filter"
    },
    {
      "id" : "Extension.extension:filter.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Search Filters",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add",
      "path" : "Extension.extension",
      "sliceName" : "add",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension",
      "path" : "Extension.extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:add.extension:url",
      "path" : "Extension.extension.extension",
      "sliceName" : "url",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:url.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:add.extension:url.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "url"
    },
    {
      "id" : "Extension.extension:add.extension:url.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Add Link URL",
      "type" : [{
        "code" : "url"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:icon",
      "path" : "Extension.extension.extension",
      "sliceName" : "icon",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:icon.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:add.extension:icon.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "icon"
    },
    {
      "id" : "Extension.extension:add.extension:icon.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Add Link Icon",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:class",
      "path" : "Extension.extension.extension",
      "sliceName" : "class",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:class.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:add.extension:class.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "class"
    },
    {
      "id" : "Extension.extension:add.extension:class.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Add Link Class",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:role",
      "path" : "Extension.extension.extension",
      "sliceName" : "role",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:role.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:add.extension:role.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "role"
    },
    {
      "id" : "Extension.extension:add.extension:role.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Roles that has access to this button",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:task",
      "path" : "Extension.extension.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.extension:task.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:add.extension:task.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "task"
    },
    {
      "id" : "Extension.extension:add.extension:task.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Tasks that has access to this button",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:add.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "add"
    },
    {
      "id" : "Extension.extension:add.value[x]",
      "path" : "Extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field",
      "path" : "Extension.extension",
      "sliceName" : "field",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension",
      "path" : "Extension.extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:field.extension:path",
      "path" : "Extension.extension.extension",
      "sliceName" : "path",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension:path.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.extension:path.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "path"
    },
    {
      "id" : "Extension.extension:field.extension:path.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Field Path from StructureDefintion",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension:type",
      "path" : "Extension.extension.extension",
      "sliceName" : "type",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension:type.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.extension:type.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "type"
    },
    {
      "id" : "Extension.extension:field.extension:type.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Display type for the field",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension:readOnlyIfSet",
      "path" : "Extension.extension.extension",
      "sliceName" : "readOnlyIfSet",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension:readOnlyIfSet.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.extension:readOnlyIfSet.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "readOnlyIfSet"
    },
    {
      "id" : "Extension.extension:field.extension:readOnlyIfSet.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Read Only if the value is set",
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:field.value[x]",
      "path" : "Extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link",
      "path" : "Extension.extension",
      "sliceName" : "link",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension",
      "path" : "Extension.extension.extension",
      "min" : 3
    },
    {
      "id" : "Extension.extension:link.extension:field",
      "path" : "Extension.extension.extension",
      "sliceName" : "field",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:field.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:field.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:link.extension:field.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "FHIRPath for field in resource",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:text",
      "path" : "Extension.extension.extension",
      "sliceName" : "text",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:text.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:text.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "text"
    },
    {
      "id" : "Extension.extension:link.extension:text.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Text for link",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:displayIn",
      "path" : "Extension.extension.extension",
      "sliceName" : "displayIn",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:displayIn.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:displayIn.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "displayIn"
    },
    {
      "id" : "Extension.extension:link.extension:displayIn.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Whether the link to be displayed on the questionnaire(questionnaire) or display page(view). Values are either questionnaire or view",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:button",
      "path" : "Extension.extension.extension",
      "sliceName" : "button",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:button.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:button.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "button"
    },
    {
      "id" : "Extension.extension:link.extension:button.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Display as button",
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:icon",
      "path" : "Extension.extension.extension",
      "sliceName" : "icon",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:icon.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:icon.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "icon"
    },
    {
      "id" : "Extension.extension:link.extension:icon.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Icon to display in button",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:url",
      "path" : "Extension.extension.extension",
      "sliceName" : "url",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:url.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:url.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "url"
    },
    {
      "id" : "Extension.extension:link.extension:url.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "URL to go to",
      "type" : [{
        "code" : "url"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:class",
      "path" : "Extension.extension.extension",
      "sliceName" : "class",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:class.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:class.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "class"
    },
    {
      "id" : "Extension.extension:link.extension:class.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Class of the link",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:role",
      "path" : "Extension.extension.extension",
      "sliceName" : "role",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:role.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:role.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "role"
    },
    {
      "id" : "Extension.extension:link.extension:role.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Roles that has access to this button",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:task",
      "path" : "Extension.extension.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.extension:task.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:link.extension:task.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "task"
    },
    {
      "id" : "Extension.extension:link.extension:task.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Tasks that has access to this button",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:link.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "link"
    },
    {
      "id" : "Extension.extension:link.value[x]",
      "path" : "Extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:mount",
      "path" : "Extension.extension",
      "sliceName" : "mount",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:mount.extension",
      "path" : "Extension.extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:mount.extension:name",
      "path" : "Extension.extension.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:mount.extension:name.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:mount.extension:name.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "name"
    },
    {
      "id" : "Extension.extension:mount.extension:name.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Unique name of the resource to be mounted",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:mount.extension:fromref",
      "path" : "Extension.extension.extension",
      "sliceName" : "fromref",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:mount.extension:fromref.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:mount.extension:fromref.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "fromref"
    },
    {
      "id" : "Extension.extension:mount.extension:fromref.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Mount resource from reference",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:mount.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "mount"
    },
    {
      "id" : "Extension.extension:mount.value[x]",
      "path" : "Extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
