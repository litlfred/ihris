---
title: "Form Storage -- Entry/Last Entry"
source: http://open.intrahealth.org/w/index.php?oldid=4209
contributors: ["Litlfred", "MarkAHershberger"]
pages: 92-93
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Form Storage -- Entry/Last Entry

This is the default storage mechanism that a form uses

## Features

This entry storage mechanism tracks changes made to the data by user and time.

## Database Structure

This is a vertical database structure.

### Entry and Last Entry

All data is stored in two structurally identical tables, entry and last\_entry. The entry table contains all data saved into the system, while last\_entry only saves the current version of the data. Each row of this table corresponds to one field of one instance of a form. These references are made by the columns record and form\_field which are the id's of the tables record and form\_field

### Record

The record table has one row for each form instance. A form instance is the name of a form and an id.

The record table contains the columns id, form, parent\_form and parent\_id. The form column matches the id column in the form table and which tells us which form this record, or instance, is. The parent\_form column is a string and tells us the name, if any, of a parent form for this form instance. Similarly, the parent\_id tells us the id, if any, of the parent form. The parent form may or may not be saved into the entry table.

The id is referenced by the entry and last\_entry tables

There is also a modification time which tracks the last time any field of this form instance was modified.

### Form

The form table describe the forms which have been saved into the entry table. There are columns id and name. It's id is referenced by the form field table.

### Field

The field table describe all of the fields and their database types. It contains the columns: id, name and type. There is one row for each pair (name of a field, field database type) which is assigned an id. The database type, tells us which column that the field data is saved in the last\_entry and entry tables. It's id column is referenced by the form\_field table.

### Form Field

The form field table has on row for each pair of (form, field id). It's id column is referenced by the entry and last entry tables.

## Sample SQL Queries

### Getting all the data for a form

Suppose you want to get all the fields for the 'person' form with id '10260.' This can be done by:

```
SELECT
   field.name AS `Field`,
   field.type AS `Type`,
   last_entry.integer_value AS `Integer`,
   last_entry.string_value AS `String`,
   last_entry.text_value AS `Text`,
   last_entry.date_value AS `Date`
FROM last_entry
JOIN form_field ON last_entry.form_field = form_field.id
JOIN field ON form_field.field = field.id
WHERE last_entry.record = '10260'
AND last_entry.form_field IN
  (SELECT form_field.id FROM form_field
  JOIN form on form_field.form = form.id
```

WHERE form.name = 'person')
