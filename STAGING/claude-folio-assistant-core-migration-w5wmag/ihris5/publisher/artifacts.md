# Artifacts Summary - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Behavior: Search Parameters 

These define the properties by which a RESTful server can be searched. They can also be used for sorting and including related resources.

| | |
| :--- | :--- |
| [active-user](SearchParameter-active-user.md) | Search by active status for a Person resource. |
| [basic-location-constraint](SearchParameter-basic-location-constraint.md) | Search by related location for a Basic resource Role. |
| [basic-name](SearchParameter-basic-name.md) | Search by name for a Basic resource. |
| [basic-practitioner](SearchParameter-basic-practitioner.md) | Search by practitioner for a Basic resource. |
| [basic-related-location](SearchParameter-basic-related-location.md) | Search by related location for a Basic resource. |
| [basic-related-practitioner](SearchParameter-basic-related-practitioner.md) | Search by related practitioner for a Basic resource. |
| [employment-status-search](SearchParameter-employment-status-search.md) | Search for a practitionerRole employment-status. |
| [gofr-search-isbroadcast](SearchParameter-gofr-search-isbroadcast.md) | search parameter for broadcasted messages |
| [gofr-search-isflowstart](SearchParameter-gofr-search-isflowstart.md) | search parameter for flow starts |
| [job-search](SearchParameter-job-search.md) | Search for a practitionerRole job. |
| [leaveperiod-search](SearchParameter-leaveperiod-search.md) | Search for a practitioner's Leave Period |
| [leavetype-search](SearchParameter-leavetype-search.md) | Search for a practitioner's Leave Type. |
| [location-related-location](SearchParameter-location-related-location.md) | Search by related location for a Location resource. |
| [performanceperiod-search](SearchParameter-performanceperiod-search.md) | Search for a practitioner's Performance Period |
| [position-status-search](SearchParameter-position-status-search.md) | Search for a practitionerRole position status. |
| [practitioner-birthdate](SearchParameter-practitioner-birthdate.md) | Search by birthdate for a Practitioner resource. |
| [practitioner-employeeNumber](SearchParameter-practitioner-employeeNumber.md) | Search by employee number for a practitioner resource. |
| [practitioner-phone](SearchParameter-practitioner-phone.md) | Search by phone for a Practitioner resource. |
| [practitioner-related-location](SearchParameter-practitioner-related-location.md) | Search by related location for a Practitioner resource. |
| [practitioner-related-practitioner](SearchParameter-practitioner-related-practitioner.md) | Search by related practitioner for a Practitioner resource. |
| [practitioner-renewrole](SearchParameter-practitioner-renewrole.md) | Search by employee ID for a practitioner resource. |
| [practitionerrole-related-location](SearchParameter-practitionerrole-related-location.md) | Search by related location for a PractitionerRole resource. |
| [practitionerrole-related-practitioner](SearchParameter-practitionerrole-related-practitioner.md) | Search by related practitioner for a PractitionerRole resource. |

### Structures: Questionnaires 

These define forms used by systems conforming to this implementation guide to capture or expose data to end users.

| | |
| :--- | :--- |
| [iHRIS Add Task Workflow](Questionnaire-ihris-task.md) | iHRIS workflow to record a Role |
| [iHRIS AddRole Workflow](Questionnaire-ihris-role.md) | iHRIS workflow to record a Role |
| [iHRIS Test Questionnaire](Questionnaire-ihris-test.md) | iHRIS Test initial data entry questionnaire. |

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [IHEmCSDFacilityLocation](StructureDefinition-IHE.mCSD.FacilityLocation.md) |  |
| [IHEmCSDLocation](StructureDefinition-IHE.mCSD.Location.md) |  |
| [IhrisTestPractitioner](StructureDefinition-ihris-test-practitioner.md) | iHRIS profile of Practitioner for tests. |
| [iHRIS Audit Event](StructureDefinition-ihris-auditevent.md) | iHRIS profile for AuditEvent |
| [iHRIS Dashboard](StructureDefinition-ihris-dashboard.md) | iHRIS Profile of the Basic resource to manage dashboards. |
| [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md) | iHRIS Profile of the Basic resource to manage visualizations. |
| [iHRIS Document](StructureDefinition-ihris-document.md) | iHRIS Profile of the DocumentReference resource to manage static documents. |
| [iHRIS Module](StructureDefinition-ihris-module.md) | iHRIS profile of Library resource to manage modules. |
| [iHRIS Page](StructureDefinition-ihris-page.md) | iHRIS Profile of the Basic resource to manage pages. |
| [iHRIS Parameters Local Config](StructureDefinition-ihris-parameters-local-config.md) | Configuration Parameters to be loaded from a local file for iHRIS. |
| [iHRIS Parameters Remote Config](StructureDefinition-ihris-parameters-remote-config.md) | Configuration Parameters to be loaded from a remote file for iHRIS. |
| [iHRIS Questionnaire](StructureDefinition-ihris-questionnaire.md) | iHRIS Profile of the Questionnaire resource for data entry and validation. |
| [iHRIS Report](StructureDefinition-ihris-report.md) | iHRIS Profile of the Basic resource to manage reports. |
| [iHRIS Resources Relationship Profile](StructureDefinition-iHRISRelationship.md) | iHRIS Resources Relationship Profile |
| [iHRIS Role](StructureDefinition-ihris-role.md) | iHRIS Profile of the Basic resource to manage roles. |
| [iHRIS Task](StructureDefinition-ihris-task.md) | iHRIS Profile of the Basic resource to manage tasks. |
| [iHRIS Test Practitioner Role](StructureDefinition-ihris-test-practitioner-role.md) | iHRIS Test profile of Practitioner Role. |

### Structures: Data Type Profiles 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [ContactPoint](StructureDefinition-ContactPoint.md) | Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Composite Task](StructureDefinition-composite-task.md) | Tasks Inheritance |
| [Details of a report](StructureDefinition-iHRISReportDetails.md) | Defines the primary resource of the relationship |
| [Links to the primary resource](StructureDefinition-iHRISReportLink.md) | Links to the primary resource |
| [Resource Fields](StructureDefinition-iHRISReportElement.md) | Lists fields of a resource to be displayed/cached |
| [Task Attributes](StructureDefinition-task-attributes.md) | Task attributes. |
| [iHRIS Assign Role](StructureDefinition-ihris-assign-role.md) | iHRIS Assign Role to a user or other role. |
| [iHRIS Assign Task](StructureDefinition-ihris-assign-task.md) | iHRIS Assign Task to a user or other task. |
| [iHRIS Basic Name](StructureDefinition-ihris-basic-name.md) | iHRIS name field for basic resources. |
| [iHRIS Dashboard Visualization](StructureDefinition-ihris-dashboard-visualization.md) | iHRIS Dashboard Visualization |
| [iHRIS Page Display](StructureDefinition-ihris-page-display.md) | iHRIS Page Display details. |
| [iHRIS Page Section](StructureDefinition-ihris-page-section.md) | iHRIS Page Section information. |
| [iHRIS Page Task](StructureDefinition-ihris-page-task.md) | iHRIS Page Task details. |
| [iHRIS Practitioner Dependent Detail](StructureDefinition-ihris-test-dependent.md) | iHRIS Test extension for Practitioner Dependent Detail. |
| [iHRIS Practitioner Residence](StructureDefinition-ihris-test-residence.md) | iHRIS Test extension for Practitioner residence. |
| [iHRIS Resource Relationships](StructureDefinition-ihris-resource-relationships.md) | iHRIS Resource Relationships |
| [iHRIS Role Primary](StructureDefinition-ihris-role-primary.md) | iHRIS flag for roles to indicate a primary role for assignment to users. |
| [iHRIS Visualization Categories](StructureDefinition-ihris-visualization-categories.md) | iHRIS visualization categories |
| [iHRIS Visualization Dataset](StructureDefinition-ihris-visualization-dataset.md) | iHRIS visualization dataset |
| [iHRIS Visualization Filters](StructureDefinition-ihris-visualization-filters.md) | iHRIS visualization filters |
| [iHRIS Visualization Permissions](StructureDefinition-ihris-visualization-permissions.md) | iHRIS Visualization Permissions |
| [iHRIS Visualization Series](StructureDefinition-ihris-visualization-series.md) | iHRIS visualization series |
| [iHRIS Visualization Settings](StructureDefinition-ihris-visualization-settings.md) | iHRIS visualization settings for the data visualizer |
| [ihRIS Report parameters](StructureDefinition-iHRISReportParameters.md) | Lists parameters |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [AddressType](ValueSet-address-type.md) | The type of an address (physical / postal). |
| [AddressUse](ValueSet-address-use.md) | The use of an address. |
| [AdministrativeGender](ValueSet-administrative-gender.md) | The gender of a person used for administrative purposes. |
| [Code system for document categories.](ValueSet-ihris-document-category.md) |  |
| [Code system for task permissions.](ValueSet-ihris-task-permission.md) |  |
| [Code system for task permissions.](ValueSet-ihris-task-resource.md) |  |
| [Common Languages](ValueSet-languages.md) | This value set includes common codes from BCP-47 (http://tools.ietf.org/html/bcp47) |
| [Contact entity type](ValueSet-contactentity-type.md) | This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party. |
| [ContactPointSystem](ValueSet-contact-point-system.md) | Telecommunications form for contact point. |
| [ContactPointUse](ValueSet-contact-point-use.md) | Use of contact point. |
| [CurrencyCode](ValueSet-currencies.md) | Currency codes from ISO 4217 (see https://www.iso.org/iso-4217-currency-codes.html) |
| [DaysOfWeek](ValueSet-days-of-week.md) | The days of the week. |
| [IdentifierType](ValueSet-identifier-type.md) | A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. |
| [IdentifierUse](ValueSet-identifier-use.md) | Identifies the purpose for this identifier, if known . |
| [Iso 3166 Part 1: 2 Letter Codes](ValueSet-iso3166-1-2.md) | This value set defines the ISO 3166 Part 1 2-letter codes |
| [Location type](ValueSet-location-physical-type.md) | This example value set defines a set of codes that can be used to indicate the physical form of the Location. |
| [LocationMode](ValueSet-location-mode.md) | Indicates whether a resource instance represents a specific location or a class of locations. |
| [LocationStatus](ValueSet-location-status.md) | Indicates whether the location is still in use. |
| [NameUse](ValueSet-name-use.md) | The use of a human name. |
| [Organization type](ValueSet-organization-type.md) | This example value set defines a set of codes that can be used to indicate a type of organization. |
| [Practice Setting Code Value Set](ValueSet-c80-practice-codes.md) | This is the code representing the clinical specialty of the clinician or provider who interacted with, treated, or provided a service to/for the patient. The value set used for clinical specialty has been limited by HITSP to the value set reproduced from HITSP C80 Table 2-149 Clinical Specialty Value Set Definition. |
| [Service category](ValueSet-service-category.md) | This value set defines an example set of codes that can be used to classify groupings of service-types/specialties. |
| [Service type](ValueSet-service-type.md) | This value set defines an example set of codes of service-types. |
| [ServiceProvisionConditions](ValueSet-service-provision-conditions.md) | The code(s) that detail the conditions under which the healthcare service is available/offered. |
| [V3 Value SetServiceDeliveryLocationRoleType](ValueSet-v3-ServiceDeliveryLocationRoleType.md) | A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered. |
| [Value Set for iHRIS Basic Resources.](ValueSet-ihris-resource-valueset.md) |  |
| [hl7VS-degreeLicenseCertificate](ValueSet-v2-0360.md) | Concepts specifying an educational degree (e.g., MD). Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging. Used in Version 2 messaging; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7. |
| [iHRIS Cadre](ValueSet-ihris-cadre.md) | Sample iHRIS ValueSet for: IhrisCadre |
| [iHRIS Classification](ValueSet-ihris-classification.md) | Sample iHRIS ValueSet for: IhrisClassification |
| [iHRIS Job](ValueSet-ihris-job.md) | Sample iHRIS ValueSet for: IhrisJob |
| [iHRIS Salary Grade](ValueSet-ihris-salary-grade.md) | Sample iHRIS ValueSet for: iHRISSalaryGrade |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [AddressType](CodeSystem-address-type.md) | The type of an address (physical / postal). |
| [AddressUse](CodeSystem-address-use.md) | The use of an address. |
| [AdministrativeGender](CodeSystem-administrative-gender.md) | The gender of a person used for administrative purposes. |
| [Code System for Currencies.](CodeSystem-currencies.md) |  |
| [Code System for iHRIS Basic Resources.](CodeSystem-ihris-resource-codesystem.md) |  |
| [Code system for document categories.](CodeSystem-ihris-document-category.md) |  |
| [Code system for task permissions.](CodeSystem-ihris-task-permission.md) |  |
| [Code system for task permissions.](CodeSystem-ihris-task-resource.md) |  |
| [Contact entity type](CodeSystem-contactentity-type.md) | This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party. |
| [ContactPointSystem](CodeSystem-contact-point-system.md) | Telecommunications form for contact point. |
| [ContactPointUse](CodeSystem-contact-point-use.md) | Use of contact point. |
| [DaysOfWeek](CodeSystem-days-of-week.md) | The days of the week. |
| [ISO 3166-1 Codes for the representation of names of countries and their subdivisions — Part 1: Country code](CodeSystem-ISO3166Part1.md) | ISO 3166-1 establishes codes that represent the current names of countries, dependencies, and other areas of particular geopolitical interest, on the basis of country names obtained from the United Nations. |
| [IdentifierUse](CodeSystem-identifier-use.md) | Identifies the purpose for this identifier, if known . |
| [Location type](CodeSystem-location-physical-type.md) | This example value set defines a set of codes that can be used to indicate the physical form of the Location. |
| [LocationMode](CodeSystem-location-mode.md) | Indicates whether a resource instance represents a specific location or a class of locations. |
| [LocationStatus](CodeSystem-location-status.md) | Indicates whether the location is still in use. |
| [NameUse](CodeSystem-name-use.md) | The use of a human name. |
| [Organization type](CodeSystem-organization-type.md) | This example value set defines a set of codes that can be used to indicate a type of organization. |
| [SNOMED CT (all versions)](CodeSystem-snomedct.md) | SNOMED CT is the most comprehensive and precise clinical health terminology product in the world, owned and distributed around the world by The International Health Terminology Standards Development Organisation (IHTSDO). |
| [Service category](CodeSystem-service-category.md) | This value set defines an example set of codes that can be used to classify groupings of service-types/specialties. |
| [Service type](CodeSystem-service-type.md) | This value set defines an example set of codes of service-types. |
| [ServiceProvisionConditions](CodeSystem-service-provision-conditions.md) | The code(s) that detail the conditions under which the healthcare service is available/offered. |
| [degreeLicenseCertificate](CodeSystem-3654.md) | Code system of concepts specifying an educational degree (e.g., MD). Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging. Used in HL7 Version 2.x messaging in the CNN segment; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7. |
| [iHRIS Cadre](CodeSystem-ihris-cadre.md) | Sample iHRIS CodeSystem for: IhrisCadre |
| [iHRIS Classification](CodeSystem-ihris-classification.md) | Sample iHRIS CodeSystem for: IhrisClassification |
| [iHRIS Job](CodeSystem-ihris-job.md) | Sample iHRIS CodeSystem for: IhrisJob |
| [iHRIS Salary Grade](CodeSystem-ihris-salary-grade.md) | Sample iHRIS CodeSystem for: iHRISSalaryGrade |
| [iHRIS Test CodeSystem](CodeSystem-ihris-test-codesystem.md) |  |
| [identifierType](CodeSystem-2103.md) | HL7-defined code system of concepts specifying type of identifier. Used in HL7 Version 2.x messaging data types CX, PLN, PPN, XCN and XON. |
| [v3 Code System RoleCode](CodeSystem-v3-RoleCode.md) | A set of codes further specifying the kind of Role; specific classification codes for further qualifying RoleClass codes. |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| |
| :--- |
| [AuditEvent](Basic-ihris-page-auditevent.md) |
| [Country](Bundle-Country.md) |
| [Roles](Basic-ihris-page-role.md) |
| [iHRIS About Page](DocumentReference-page-about.md) |
| [iHRIS Admin Role](Basic-ihris-role-admin.md) |
| [iHRIS Module Example](Library-ihris-module-example.md) |
| [iHRIS Open Role](Basic-ihris-role-open.md) |
| [iHRIS Relationship Example](Basic-ihris-es-report-mhero-send-message.md) |
| [iHRIS Self Service Role](Basic-ihris-role-self.md) |
| [iHRIS Task To Navigate to Leave](Basic-ihris-task-navigation-leave.md) |
| [iHRIS Task To Navigate to Profile](Basic-ihris-task-navigation-profile.md) |
| [iHRIS Task To Navigate to evaluation](Basic-ihris-task-navigation-evaluation.md) |
| [iHRIS Task To Navigate to password](Basic-ihris-task-navigation-password.md) |
| [iHRIS Task To Read AuditEvent resource](Basic-ihris-task-read-auditevent-resource.md) |
| [iHRIS Task To Read Basic resource](Basic-ihris-task-read-basic-resource.md) |
| [iHRIS Task To Read CodeSystem resource](Basic-ihris-task-read-code-system.md) |
| [iHRIS Task To Read DocumentReference](Basic-ihris-task-read-document-reference.md) |
| [iHRIS Task To Read Location resource](Basic-ihris-task-read-location-resource.md) |
| [iHRIS Task To Read Organization resource](Basic-ihris-task-read-organization-resource.md) |
| [iHRIS Task To Read Person resource](Basic-ihris-task-read-person-resource.md) |
| [iHRIS Task To Read Practitioner Page](Basic-ihris-task-read-ihris-page-practitioner.md) |
| [iHRIS Task To Read Practitioner resource](Basic-ihris-task-read-practitioner-resource.md) |
| [iHRIS Task To Read PractitionerRole Page](Basic-ihris-task-read-ihris-page-practitioner-role.md) |
| [iHRIS Task To Read PractitionerRole resource](Basic-ihris-task-read-practitioner-role-resource.md) |
| [iHRIS Task To Read Questionnaire Response resource](Basic-ihris-task-read-questionnaire-response-resource.md) |
| [iHRIS Task To Read Questionnaire ihris-leave](Basic-ihris-task-read-questionnaire-leave.md) |
| [iHRIS Task To Read Questionnaire resource](Basic-ihris-task-read-questionnaire-resource.md) |
| [iHRIS Task To Read StructureDefinition Resource](Basic-ihris-task-read-structure-definition.md) |
| [iHRIS Task To Read Valueset Resource](Basic-ihris-task-read-value-set.md) |
| [iHRIS Task To Write AuditEvent resource](Basic-ihris-task-write-auditevent-resource.md) |
| [iHRIS Task To Write Basic resource](Basic-ihris-task-write-basic-resource.md) |
| [iHRIS Task To Write CodeSystem resource](Basic-ihris-task-write-code-system.md) |
| [iHRIS Task To Write DocumentReference](Basic-ihris-task-write-document-reference.md) |
| [iHRIS Task To Write Location resource](Basic-ihris-task-write-location-resource.md) |
| [iHRIS Task To Write Organization resource](Basic-ihris-task-write-organization-resource.md) |
| [iHRIS Task To Write Person resource](Basic-ihris-task-write-person-resource.md) |
| [iHRIS Task To Write Practitioner resource](Basic-ihris-task-write-practitioner-resource.md) |
| [iHRIS Task To Write PractitionerRole resource](Basic-ihris-task-write-practitioner-role-resource.md) |
| [iHRIS Task To Write Questionnaire Response resource](Basic-ihris-task-write-questionnaire-response-resource.md) |
| [iHRIS Task To Write Questionnaire ihris-leave](Basic-ihris-task-write-questionnaire-leave.md) |
| [iHRIS Task To Write Questionnaire ihris-password](Basic-ihris-task-write-questionnaire-change-password.md) |
| [iHRIS Task To Write Questionnaire resource](Basic-ihris-task-write-questionnaire-resource.md) |
| [iHRIS Task To Write StructureDefinition Resource](Basic-ihris-task-write-structure-definition.md) |
| [iHRIS Task To Write Valueset Resource](Basic-ihris-task-write-value-set.md) |
| [iHRIS Task To Write Valueset Resource](Basic-ihris-task-write-valueset-resource.md) |
| [iHRIS Task With All Permissions To Everything](Basic-ihris-task-all-permissions-to-everything.md) |
| [iHRIS Tasks](Basic-ihris-page-task.md) |
| [iHRIS Test CodeSystem Page](Basic-ihris-page-test-codesystem.md) |
| [iHRIS Test Practitioner Page](Basic-ihris-page-test-practitioner.md) |
| [ihris-dashboard](Parameters-ihris-dashboard.md) |
| [ihris-es-report-staff-directorate](Basic-ihris-es-report-staff-directorate.md) |
| [page-home](DocumentReference-page-home.md) |

