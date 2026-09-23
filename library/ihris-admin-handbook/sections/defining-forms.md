---
title: "Defining Forms"
source: http://open.intrahealth.org/w/index.php?oldid=9046
contributors: ["Litlfred", "MarkAHershberger"]
pages: 77-80
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Defining Forms

Please read the overview of forms and fields.

The data defining a form is saved into magic data and the paths below are paths in magic data.

## Forms

Forms are the basic way to group data. A form $form, such as 'person', is stored under:

```
/modules/forms/forms/$form
```

which contains the following children:

- class: Required. The class which implements the logic, such as validation, for the form. Example is 'iHRIS\_Person'.
- displayName: Optional. An end-user name for this form. For example 'person' might have a display name 'Person'
- storage: Optional. Defaults to 'entry.' It is the storage mechanism that the form should use
- meta: Optional. A node with lots of children where information about displaying this form are saved. The data here is used by the implementing form class

- description: A description of this form. It is displayed, for example, when creating a form relationship
- child\_forms: An list of any forms that are child forms of this form.
- child\_form\_data: Optional. Meta data that are associated with child forms. There is possibly a node for each of the child forms.

The nodes in child forms data allow you to specify different groupings for child forms. For example the form 'training\_course' has as a child form 'scheduled\_training\_course.' We may want to group the 'scheduled\_training\_courses' into open and closed. Then we can select to only display the open or closed scheduled training courses by specifying the limits as below. We can also chose to specify the order that the scheduled training courses are displayed in. For example:

```
'default'  => Array [
 'scheduled_training_course' => Array [
  'order' => 'start_date,end_date'
 ]
]
'open' => Array [
 'scheduled_training_course' => Array [
  'limits' => Array [
    'operator' => 'FIELD_LIMIT'
    'field' => 'start_date'
    'style' => 'greaterthan_now'
  ]
  'order' => 'start_date,end_date'
 ]
]
'closed' => Array [
  'scheduled_training_course' => Array [
   'limits' => Array [
     'operator' => 'FIELD_LIMIT'
     'field' => 'start_date'
     'style' => 'lessthan_now'
   ]
   'order' => 'start_date,end_date'
 ]
]
```

The limits are specified according to this structure. The 'order' is a list of the fields to sort by. In the above we sort first by 'start\_date' and then by 'end\_date.' If we wanted to sort by a field in descending order we would prefix a -.

### Componentized Forms

If you are setting up an aggregating instance of iHRIS Manage (or Qualify) some of your forms will be componentized. This means that the data for each of these forms is being managed by distinct localities (e.g. regions or districts or even departments) and you wish to aggregate this de-centralized data. Whether or not a form is localized is determined the form storage mechanism being used. If a form is componentized, then any id's that reference that form are appended with an '@' and the name of the component.

## Form Classes

A form class $formClass is defined under:

```
/modules/forms/formClasses/$formClass
```

It has sub-nodes:

- fields: Optional. Contains information about the fields provided by this class
- extends: Required. Which class this form class extends. This needs to be either I2CE\_Form or a subclass of it.

### Dynamic Creation

If there is no file $formClass.php then the class is created dynamically as:

```
class $formClass extends $extendClass {}
```

where $extendClass is the value under the 'extends' node.

### Lists

The form class I2CE\_List is a special form which allows you to deal easily with lists of data. Any mapped field should take values in a form whose implementing class is a subclass of I2CE\_List.

I2CE\_List has a subclass I2CE\_SimpleList whose only field is 'name'. Examples of simple lists are:

- gender
- marital\_status
- language

## Fields

Each form class $formClass contains a list of fields. A field $field in $formClass is defined at:

```
/modules/forms/formClasses/$formClass/fields/$field
```

which has the following sub-nodes

- formfield: Required. Needs should be on of the field type such as INT
- in\_db: Optional. It should be either 0 or 1. If not set, defaults to 1. If 1, then this field should be saved into the database
- required: Optional. It should be either 0 or 1. If not set, defaults to 0. If 1, then this field needs to be set before it can be considered valid
- unique: Optional. It should be either 0 or 1. If not set, defaults to 0. If 1, then the value of this field needs to be unique among all instances of the form
- headers: Optional. It is itself a parent node, each child node is a string value. You can choose a different header by specifying the header attribute in a template file.

- default: Optional. The default title/header displayed for the field.

### Map Fields

A MAP or MAP\_MULT takes values in a list, which is any form whose implementing class subclasses I2CE\_List.

A field of type MAP or MAP\_MULT can specify the following 'default' sub-node. This 'default' node can contain a sub-node for each of the displays that you wish to define for the field. The default display is specified by displaying the 'default' node. For example, iHRIS\_Person has a mapped field, 'residence'. It's meta node contains the following sub-nodes:

```
'form' => Array [
         0 => county
         1 => district
         ]
 display => Array [
     default => Array [
       fields => county:district:[region]:country
       ]
   ]
```

\] The optional 'forms' is an array of list that tell us which lists this field is allowed to take values in. In this case, any member of the county or district list may be chosen as the residence for a person.

The 'display' node is optional. It's sub-node 'default' is optional. Its sub-node 'fields' is optional. The 'fields' entry is tells us how the field is mapped to other forms and should be displayed and selected. It has the general structure:

```
mapform1+mapfield1:mapform2+mapfield2:...:mapformN
```

If the +mapFieldX is not present, then we use mapFormX+1 for the value of mapFieldX. If the 'fields' entry is is not set, then it is the mapped form is the the name of field.

When we select a value for the field, we start by displaying all the values for mapFormN. Under each one of these values, we display all values for mapFormN-1 whose field mapFieldN-1 is mapFormN is and continue down until we get to mapForm1.

If mapFormXX+mapFieldXX is surrounded in square brackets, \[ \], then we don't display the data for that mapped form.

In the above example, when selecting a residence for a person, you first choose the country, then the region, then the district. You may further specify the county. When displaying a selected residence it will display either:

```
District, Country
```

or

```
County, Country District
```

depending if you have selected the district or county.

Finally, you can put limits and orders, per display style (e.g. default), by specifying the nodes 'limits' and 'orders.'

## Field Types

Each field has a type. The types define how they are displayed to the end user in both an edit and view only context. It also contains information about the type of column the data should be saved in a database. The available types are:

- BOOL is implemented by the class I2CE\_FormField\_BOOL is a choice between true and false
- DATE\_HMS is implemented by the class I2CE\_FormField\_DATE\_HMS is a time only
- DATE\_MD is implemented by the class I2CE\_FormField\_DATE\_MD is a month and day
- DATE\_TIME is implemented by the class I2CE\_FormField\_DATE\_TIME is a year, month, day and time
- DATE\_YMD is implemented by the class I2CE\_FormField\_DATE\_YMD and is a year, month and day
- DATE\_Y is implemented by the class I2CE\_FormField\_DATE\_Y and is a year
- INT\_GENERATE is implemented by the class I2CE\_FormField\_INT\_GENERATE and is integer sequence that will populate the next value in the sequence
- INT is implemented by the class I2CE\_FormField\_INT is an integer
- INT\_LIST is implemented by the class I2CE\_FormField\_INT\_LIST is an array of integers
- STRING\_LINE is implemented by the class I2CE\_FormField\_STRING\_LINE and is a string
- STRING\_MLINE is implemented by the class I2CE\_FormField\_STRING\_MLINE and is multi-line string
- STRING\_PASS is implemented by the class I2CE\_FormField\_STRING\_PASS is a password value
- STRING\_TEXT is implemented by the class I2CE\_FormField\_STRING\_TEXT is a large multi-line string
- YESNO is implemented by the class I2CE\_FormField\_YESNO and is a choice between Yes and No
- CURRENCY is implemented by the class iHRIS\_FormField\_CURRENCY and is a currency type and an amount
- MAP is implemented by the class I2CE\_FormField\_MAP and is the name and id of a list form
- MAP\_MULT is implemented by the class I2CE\_FormField\_MAP\_MULT and is an array of names and ids for list forms
