---
title: "Linking Facilities and Departments"
source: http://open.intrahealth.org/w/index.php?oldid=4383
contributors: ["Litlfred"]
pages: 458-466
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Linking Facilities and Departments

In iHRIS Manage, the module ihris-manage-PersonPosition defines the position form which contains the field department and the required field facilty which are both independent lists. In this tutorial, we will discuss how customize iHRIS Manage so that, when editing a position, the departments displayed are dependent on the facility chosen.

This tutorial applies to iHRIS Manage 4.0, although the concepts involved can be applied to iHRIS Qualify as well. Please refer to these articles:

- Defining Forms
- Forms and Form Classes

for background information on forms. You can see these changes in the Zanzibar-position \[1\] module.

## Overview

Our goal is to have the departments for a position to depend on the facility chosen for the position. There are two ways that one could do this.

### Option A

To the department form, we could add a required field facility which links to the facility form. In this, way we would now have every department associated to a facility.

There are a few issues with this option:

- Suppose you have to hospitals, Central Hospital and Coastal Hospital. Each would presumably have a department such as Emergency. In this option, you would have to create an Emergency Department for each of the Hospitals. It would then make it difficult to run a report such as "list all employees in all facilities which work in the emergency department" because it really is "list all employees in all facilities which work in a department with the name Emergency." In particular, since we are entering "Emergency" multiple times, there is an increased potential for a spelling mistake which would affect data quality.
- At least for the moment, there is no built in way to first select a facility and then select a department within a form.

Due to these weaknesses, we will not implement Option A in this tutorial.

### Option B

We could create a new list form facility\_department which contains two required fields, facility and department which map the for lists of the same name. Then in the position form, we no longer link to the list facility or department but to the list facility\_department. This has the following advantages over Option A:

- We only have to enter the department Emergency once as we can associate it to many facilities via the facility\_department form
- As facility\_department is a tiered list (first select a facility, and the select a department) we can use in the built in display methods when selecting the department in the position.

We will implement option B in this tutorial.

## Creating the module

We will encapsulate all of our customizations into a module my-position in order to:

- encapsulate the customizations conceptually
- ease maintenance
- ease sharing of the code

You may wish to review the Module Structure before continuing.

In your site directory, create a sub-directory 'modules' if it does not already exist and make sure you have an appropriate:

```
 <path name='modules'>
   <value>./modules</value>
 </path>
```

in your site configuration file.

Within the modules directory, create a new directory called my\_position. Within the my\_position directory, and create the file my\_position.xml and add the following:

```
 <?xml version="1.0"?>
<!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
<I2CEConfiguration name='my-position'>
  <metadata>
    <displayName>Customized iHRIS Position</displayName>
    <category>Site</category>
    <description>Customized version of the position form to list departments by
facility</description>
    <version>4.0.0.1</version>
    <requirement name='ihris-manage-Job'>
      <atLeast version='4.0'/>
      <lessThan version='4.1'/>
    </requirement>
    <requirement name='ihris-manage-PersonPosition'>
      <atLeast version='4.0'/>
      <lessThan version='4.1'/>
    </requirement>
    <path name='classes'>
      <value>./lib</value>
    </path>
    <path name='templates'>
      <value>./templates</value>
    </path>
  </metadata>
  <configurationGroup name='my-position' path='/'>
  </configurationGroup>
 </I2CEConfiguraiton>
```

## Turning off the existing fields

Let us first look at the changes to "turn off" the facility and department fields in the position form.

The position form is implemented by the class iHRIS\_Position in the ihris-manage-PerosnPosition module. Instead of removing them from the existing iHRIS\_Position form, we will specify them as not being required and not saved in the database. We also remove the reference to them in the html template files for position.

### Magic Data/Configuration Changes

We will create a new form class My\_Position which extends the iHRIS\_Position form class and set the position form to use this class:

```
 <configurationGroup name='forms' path='/modules/forms/forms'>
   <configurationGroup name='position'>
        <!--Set the position form to use the My_Position class which we will define below
        <displayName>Position</displayName>
        <description>The Position Form</description>
        <configuration name='class' values='single'>
          <displayName>Class Name</displayName>
          <description>The name of the class providing the form</description>
          <value>My_Position</value>
        </configuration>
      </configurationGroup>
 </configurationGroup>
 <configurationGroup name='forms' path='/modules/forms/formClasses'>
      <configurationGroup name='My_Position'>
        <!--"turn off" the facility and department fields for position -->
        <configuration name="extends">
          <displayName>The class this form extends</displayName>
          <value>iHRIS_Position</value>
        </configuration>
        <configurationGroup name="fields">
          <configurationGroup name="department">
            <displayName>The field 'department'</displayName>
            <configuration name='required' type='boolean'>
              <value>false</value>
            </configuration>
            <configuration name='in_db' type='boolean'>
              <value>false</value>
            </configuration>
          </configurationGroup>
          <configurationGroup name="facility">
            <displayName>The field 'department'</displayName>
            <configuration name='required' type='boolean'>
              <value>false</value>
            </configuration>
            <configuration name='in_db' type='boolean'>
              <value>false</value>
            </configuration>
          </configurationGroup>
      </configurationGroup>
 </configurationGroup>
```

### Template File Changes

Create a directory called 'templates' in the 'my\_position' directory and copy these files:

- templates/en\_US/lists\_form\_position.html
- templates/en\_US/view\_position.html

from the ihris-manage-PersonPosition module into the this directory. On the new copy lists\_form\_position.html remove the lines:

```
  <span type="form" name="facility" showhead="default"></span>
  <span type="form" name="department" showhead="default"></span>
```

On the new copy of view\_position.html remove the lines:

```
  <span type="form" name="position:facility" showhead="default" class="even"></span>
  <span type="form" name="position:department" showhead="default"></span>
```

and the line:

```
  <li task='can_edit_database_list_position'>
     <span type="form" name="position:facility"
href="lists?type=position&amp;field=facility&amp;forms%3Aposition%3A0%3Afields%3Afacility
     >Select another Position</span>
  </li>
```

## Creating the facility\_department

We will create a new form facility\_department which is implemented by the form class My\_Facility\_Department which contains the mapped fields facility and department.

### Magic Data/Configuration Changes

All of these changes are in the my\_position.xml file.

First, we need to create the form class 'My\_Facility\_Department'. To do this, we add in the following under the configurationGroup named 'formClasses':

```
 <configurationGroup name='My_Facility_Department'>
 <!-- pairs up facilities with a department list-->
  <configuration name="extends">
   <displayName>The class this form extends</displayName>
   <value>I2CE_List</value>
  </configuration>
  <configurationGroup name="fields">
   <configurationGroup name='facility'>
    <configuration name="formfield">
     <displayName>The form field type</displayName>
     <value>MAP</value>
    </configuration>
    <configuration name="required" type="boolean">
     <displayName>This field is required to be set</displayName>
     <value>true</value>
    </configuration>
   </configurationGroup>
   <configurationGroup name='department'>
    <configuration name="formfield">
     <displayName>The form field type</displayName>
     <value>MAP</value>
    </configuration>
    <configuration name="unique" type="boolean">
     <displayName>This field is requried to be unique</displayName>
     <value>true</value>
    </configuration>
    <configuration name="unique_field">
     <displayName>This field is required to be unique for each facility</displayName>
     <value>facility</value>
    </configuration>
    <configuration name="required" type="boolean">
     <displayName>This field is required to be set</displayName>
     <value>true</value>
    </configuration>
   </configurationGroup>
 </configurationGroup>
</configurationGroup>
```

Next, let us add in the 'facility\_department' form. To do this, we add in the following under the configurationGroup named 'forms':

```
 <configurationGroup name='facility_department'>
  <displayName>Facility Department</displayName>
  <description>The Facility Department Form</description>
  <configuration name='class' values='single'>
  <displayName>Class Name</displayName>
   <description>The name of the class providing the form</description>
   <value>My_Facility_Department</value>
  </configuration>
  <configuration name='display' values='single'>
    <displayName>Display name</displayName>
    <description>The display name for this form</description>
     <value>Facilitiy/Department</value>
  </configuration>
  <configuration name="storage" values='single'>
    <displayName>Storage Details</displayName>
    <description>The storage mechanism for this form.</description>
    <value>magicdata</value>
  </configuration>
 </configurationGroup>
```

Next, we need to add in the 'facility\_department' as a mapped field to the 'My\_Position' class. To do this, we add in the following:

```
          <configurationGroup name="facility_department">
            <configuration name="formfield">
              <displayName>The form field type</displayName>
              <value>MAP</value>
            </configuration>
            <configuration name="headers" type="delimited">
              <displayName>The headers for this field.</displayName>
              <value>default:Department</value>
            </configuration>
            <configuration name="required" type="boolean">
              <displayName>This field is requried to be set</displayName>
              <value>true</value>
            </configuration>
              <configurationGroup name="meta">
                <configurationGroup name="display">
                  <configurationGroup name="default">
                    <configuration name="fields">
                      <!-- the says that the default display is to first show/select the
                      <value>facility_department:facility</value>
                    </configuration>
                  </configurationGroup>
                </configurationGroup>
              </configurationGroup>
          </configurationGroup>
```

under the fields node for My\_Position.

Finally, we want to create a 'task' that deals with editing and viewing the 'facility\_department' list. We will want to make sure that the edit task implies the view task. We will also want to add these tasks to the the edit/view organization list task. To do so, we add in the following:

```
    <configurationGroup name='tasks' path='/I2CE/tasks/task_description'>
      <configuration name='can_edit_database_list_facility_department'>
        <value>Edit the facility/department list</value>
      </configuration>
      <configuration name='can_view_database_list_facility_department'>
        <value>View the facility/department list</value>
      </configuration>
    </configurationGroup>
    <configurationGroup name='tasks_trickle_down' path='/I2CE/tasks/task_trickle_down/' >
      <configuration name='can_edit_database_list_facility_department' values='many'>
        <value>can_edit_organization_database_lists</value>
        <value>can_view_database_list_facility_department</value>
      </configuration>
      <configuration name='can_edit_all_organization_database_lists' values='many'>
        <value>can_edit_database_list_facility_department</value>
      </configuration>
      <configuration name='can_view_all_organization_database_lists' values='many'>
        <value>can_view_database_list_facility_department</value>
      </configuration>
    </configurationGroup>
```

### Template File Changes

In your copy of the view\_postion.html file, add the following:

```
  <!-- Show the facility_department with the default header -->
  <span type="form" name="position:facility_department" showhead="default" class="even"><
```

and:

```
  <li task='can_edit_database_list_position'>
    <span type="form"
          name="position:facility_department"
href="lists?type=position&amp;field=facility_department&amp;forms%3Aposition%3A0%3Afields
      Select another Position
    </span>
  </li>
```

where you deleted the similar lines above.

In your copy of the file list\_form\_position.html add in the the following line:

```
 <span type="form" name="facility_department" showhead="default"></span>
```

where you deleted the lines above.

### Templates for facility\_department

We need to create two templates to view and edit the facility\_department form. We will put these in the 'my\_postion/templates' directory. Create the file 'lists\_form\_facility\_department.html' and add the following:

```
<tbody id="list_fields">
  <tr>
    <td class="formdata">
      <span type="form" name="facility_department:facility" showhead="default" addlink="l
    </td>
    <td class="formdata">
      <span type="form" name="facility_department:department" showhead="default" addlink=
    </td>
  </tr>
</tbody>
```

Now create the file 'view\_list\_facility\_department.html' and add the following:

```
 <div id="list_display" task='can_view_database_list_facility_department'>
  <div class="editRecord">
    <p>Edit This Information</p>
    <ul>
      <li task='can_edit_database_list_facility_department'><span type="form" name="facil
      <li><a href="lists?type=facility_department&amp;field=facility" >Select another Fac
    </ul>
  </div> <!-- editRecord -->
  <div class="dataTable">
    <table border="0" cellspacing="0" cellpadding="0">
      <tr>
        <th colspan="2">Associate Departments to A Facility</th>
      </tr>
      <span type="form" name="facility_department:facility" showhead="default" addlink="l
      <span type="form" name="facility_department:department" showhead="default" addlink=
    </table>
  </div> <!-- dataTable -->
</div> <!-- list_display -->
```

### The Facility Departments class

When a field maps to the facility\_department form we want the display to be first the facility and then the department. In order to do this, we need to create the My\_Facility\_Department class as a file. To do so, first create the directory 'lib' in the 'my\_position' directory. In this new directory, create a file 'My\_Facility\_Department.php' and add the contents:

```
 class My_Facility_Department extends I2CE_List {
     /**
     * The main field name used for display a description of a record.
     */
    const MAIN_FIELD = "facility";
    /**
     * The secondary field name used for displaying a description of a
record in combination with the MAIN_FIELD.
     */
    const SEC_FIELD = "department";
    /**
     * The sort field name to be used for sorting the display list.
This can't be used with the SEC_FIELD option for display.
     */
 }
```

(In an upcoming step, we shall remove this step and allow you to specify it in magic data.)

### Edit Database List Templates

We finally want to customize our Edit Database Lists page so that the new list, facility\_department shows up. First, create the directory templates in your site directory, if it doesn't already exist, and ensure that your site configuration file has the line:

```
 <path name='templates'>
   <value>./templates</value>
 </path>
```

Now, copy the files lists.html from the iHRIS Manage to this new directory. Edit the new copy and add the line:

```
 <li task='can_edit_database_list_facility_department'><a href="lists?type=facility_depar
```

just after the similar line for Department.

Next, change the line:

```
 <li task='can_edit_database_list_position'><a href="lists?type=position&amp;field=facili
```

to:

```
 <li task='can_edit_database_list_position'><a href="lists?type=position&amp;field=facili
```

## Enabling the Module

You can now enable your module by adding the following:

```
 <requirement name='my-position'>
   <atLeast version='4.0'/>
   <lessThan version='4.1'/>
 </requirement>
```

to your site configuration file.

## Reporting and Form Relationship

Because the form relationships have changed:

- Old: the position form links to the facility and department forms.
- New: the position form links to the facility\_department form which in turn links to the facility and department forms.

our form relationship used to define the staff reports need to be changed. Rather than detailing these changes in this tutorial you may look at them here \[2\]

## References

\[1\] http://bazaar.launchpad.net/~ihris%2Bzanzibar/ihris-manage-zanzibar/central-4.0/files/head%3A/modules/ZNZPosition/ \[2\] http://bazaar.launchpad.net/~ihris%2Bzanzibar/ihris-manage-zanzibar/central-4.0/files/head%3A/modules/ZNZReports/Reports/

StaffReports/
