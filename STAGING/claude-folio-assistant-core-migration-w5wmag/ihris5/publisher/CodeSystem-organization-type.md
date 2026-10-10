# Organization type - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Organization type**

## CodeSystem: Organization type 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://terminology.hl7.org/CodeSystem/organization-type | *Version*:0.1.0 | |
| * Standards status: *[Draft](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:OrganizationType |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.1128 | | |

 
This example value set defines a set of codes that can be used to indicate a type of organization. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Organization type](ValueSet-organization-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "organization-type",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:57.505+03:00",
    "source" : "#p4w49vQd1ZBWk4fI",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablecodesystem"]
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "pa"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "draft"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 1
  }],
  "url" : "http://terminology.hl7.org/CodeSystem/organization-type",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.1128"
  }],
  "version" : "0.1.0",
  "name" : "OrganizationType",
  "title" : "Organization type",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "This example value set defines a set of codes that can be used to indicate a type of organization.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/organization-type",
  "content" : "complete",
  "count" : 12,
  "concept" : [{
    "code" : "prov",
    "display" : "Healthcare Provider",
    "definition" : "An organization that provides healthcare services."
  },
  {
    "code" : "dept",
    "display" : "Hospital Department",
    "definition" : "A department or ward within a hospital (Generally is not applicable to top level organizations)"
  },
  {
    "code" : "team",
    "display" : "Organizational team",
    "definition" : "An organizational team is usually a grouping of practitioners that perform a specific function within an organization (which could be a top level organization, or a department)."
  },
  {
    "code" : "govt",
    "display" : "Government",
    "definition" : "A political body, often used when including organization records for government bodies such as a Federal Government, State or Local Government."
  },
  {
    "code" : "ins",
    "display" : "Insurance Company",
    "definition" : "A company that provides insurance to its subscribers that may include healthcare related policies."
  },
  {
    "code" : "pay",
    "display" : "Payer",
    "definition" : "A company, charity, or governmental organization, which processes claims and/or issues payments to providers on behalf of patients or groups of patients."
  },
  {
    "code" : "edu",
    "display" : "Educational Institute",
    "definition" : "An educational institution that provides education or research facilities."
  },
  {
    "code" : "reli",
    "display" : "Religious Institution",
    "definition" : "An organization that is identified as a part of a religious institution."
  },
  {
    "code" : "crs",
    "display" : "Clinical Research Sponsor",
    "definition" : "An organization that is identified as a Pharmaceutical/Clinical Research Sponsor."
  },
  {
    "code" : "cg",
    "display" : "Community Group",
    "definition" : "An un-incorporated community group."
  },
  {
    "code" : "bus",
    "display" : "Non-Healthcare Business or Corporation",
    "definition" : "An organization that is a registered business or corporation but not identified by other types."
  },
  {
    "code" : "other",
    "display" : "Other",
    "definition" : "Other type of organization not already specified."
  }]
}

```
