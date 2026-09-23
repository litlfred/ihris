---
title: "Forms and Form Classes"
source: http://open.intrahealth.org/w/index.php?oldid=4195
contributors: ["Litlfred", "MarkAHershberger"]
pages: 101-102
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Forms and Form Classes

Records are stored in the Intrahealth Informatics Core Engine (I2CE) in forms which consist of a collection fields. You may roughly think of a form as table in a database and a field as a column of that table.

The logic of a form is handled by a Form Class which extends I2CE\_Form. The logic of a field is handled by a class extending I2CE\_FormField.

## Referencing in Templates

The templating system allows easy reference to data stored in a form in an html template. For example to reference a person's firstname you can use:

```
<p  id='my_person'>You are looking at <span type='form' name='person:firstname'/> <span type='form' name='person:surname'/>!</p>
```

Would be turned into

```
<p id='my_person'>You are looking at Joe Smith!</p>
```

if there was a 'person' form set at or above the node with id 'my\_person'. The html is modified by the templating system. In version 3.1, this is done by the 'processForms()' method of the forms module class, I2CE\_Module\_Forms, by hooking into the hook 'process\_templatedata\_FORM' defined in I2CE\_Module\_TemplateData.

It is the responsibility of the page to make sure the appropriate form is assigned to the appropriate node in the template.

## Forms and Their Classes

A form $form is linked to a form classes by specifying the data at /modules/forms/forms/$form/class to be the name of the form class. For example:

```
I2CE::getConfig()->modules->forms->person->class = 'I2CE_ManagePerson';
```

The classes may or may not exist as files. If there is logic that a form needs to perform, for instance on its validate() and save() methods it will exist. Otherwise, they exist virtually. Starting in version 3.2 such a virtual class is generated 'on-the-fly' by making use of the \_\_autoload() method.

## Fields and Their Clases

All fields of a form have a name and a type. The name of the fields is how the field is referenced by the form as a public variable by using the \_\_get() and \_\_set() methods. For example:

```
if ($person instanceof I2CE_Person)  {
 echo "$person->firstname . "\n";
}
```

The types effect how the data is stored in the database and how the data is displayed and entered in the system. The following are a list of common types:

- BOOL A boolean True/False value
- CURRENCY A currency value
- DATE\_HMS A hour, minute, second time

- DATE\_MD A month and date
- DATE\_TIME A time

- DATE\_Y A year
- DATE\_YMD A year, month and date
- INT An integer value
- INT\_LIST A list of integers
- INT\_GENEREATE An integer which automatically increments
- STRING\_LINE A line of text
- STRING\_MLINE Several lines of text
- STRING\_PASS A password
- STRING\_TEXT A lot of text
- YESNO A Yes/No value

A $type is handled by the class I2CE\_FormField\_$type

## Forms and Their Fields

The structure of forms, their classes and fields and where they are defined in can be easily browsed at:

- Form and Field Browser \[1\] Applies to development version 3.2

## How the Data is Stored

Although you may loosely think of a form as being a table in the database, it is not quite so.

## Version 3.1

In version 3.1 all data stored in forms is stored in the 'entry' and 'last\_entry' tables. These tables keep a history of the changes made to the data based on the user that changed the data, the type of the change, and the time of the change. The 'entry' table has all of the history, while the 'last\_entry' table only contains the most recent changes to a field.

## Version 3.2

Starting in this version we are enabling multiple storage mechanisms for a form. The default storage mechanism will still be through the 'entry' and 'last\_entry' table.

In addition we will enable storage to specified database tables to allow the administrator to easily incorporate outside data sources into the Custom Reporting utility. This will be either read-only or read-write as the user specified.

We also allow storage in Magic Data. This is primarily intended for list data that a administrator wishes to maintain centrally in a module and then ship out to regional offices. In addition, the lists stored in Magic Data will be localizable.

## References

\[1\] http://open.intrahealth.org/ihris-docs/form\_documentor/
