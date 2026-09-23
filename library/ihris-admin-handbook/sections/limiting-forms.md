---
title: "Limiting Forms"
source: http://open.intrahealth.org/w/index.php?oldid=4384
contributors: ["Lduncan", "Litlfred", "MarkAHershberger"]
pages: 453-457
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Limiting Forms

In version 3.2 and greater we have unified the ability to search for forms by limiting the values of their fields.

## Uses

The limit data structure is used in, for example:

- I2CE\_Form::search()
- I2CE\_Form::listFields()
- Form Relationships
- Report Limits

The methods of I2CE\_Form add in the ability to limit values based on the storage mechanism. If you wish to create a new form storage mechanism with search capabilities, you will need to either produce some code to parse the limiting data structure described below or, if you storage mechanism is accessible to the database, you may simply subclass I2CE\_FormStorage\_Helper\_DB.

## Limit Styles

There are many ways that you may wish to limit the values of a particular field, we refer to these as a limit style. For example, equals or like.

Recall that every field is has a type, such as INT or INT\_LIST, which translates to a class, such as I2CE\_FormField\_INT or I2CE\_FormField\_INT\_LIST, all of which sub-class I2CE\_FormField. A type is made available to some sub-class (as well as well of all of its sub-classes) of I2CE\_FormField.

Most of these limit style, and their attendant code, can be found in the module form-limits.

## Structure of Limiting Data

We allow, on a per-form basis, logical compounds of limits of any field through a nested array (or magic data) structure. The structure of a limit expression node is as follows:

- operator: Required. Tells us what type of node this expression node is. Valid values are 'FIELD\_LIMIT', 'AND', 'XOR', 'OR', and 'NOT'
- operand: Used only in the case of 'AND', 'XOR', 'OR' and 'NOT' in which case it is required. It is a sub-array/sub-node consisting of zero or more limit expression nodes. In the case of 'NOT' there is the further limitation that the number is exactly one.
- field: Used only need in the case of 'FIELD\_LIMIT' in which case it is required. It is the name of the field for this form we are limiting on.
- style: Used only need in the case of 'FIELD\_LIMIT' in which case it is required. It is the limit style.
- data: Used only need in the case of 'FIELD\_LIMIT.' It is a associative array of data used to limit the data by. If not set, it should be interpreted as the empty array.

For example for a person, we may have:

```
array(
  'operator'=>'AND',
  'operand'=>array(
    0=>array(
      'operator'=>'FIELD_LIMIT',
      'field'=>'surname',
      'style'=>'like',
      'data'=>array(
        'value'=>'N%th'
      )
    )
    1=>array(
      'operator'=>'NOT',
      'operand'=>array(
        0=>array(
          'operator'=>'OR',
          'operand'=>array(
            0=>array(
              'operator'=>'FIELD_LIMIT',
              'field'=>'othername',
              'style'=>'equals',
              'data'=>array(
                'value'=>'Mike'
               )
            ),
            1=>array(
              'operator'=>'FIELD_LIMIT',
              'field'=>'othername',
              'style'=>'equals',
              'data'=>array(
               'value'=>'Michael'
              )
            )
          )
        )
      )
    )
  )
```

would be interpreted in SQL as:

```
((`person+surname` LIKE 'N%th') AND ( NOT (( `person+othername` = 'Mike') OR (`person+othername` = 'Michael'))))
```

Unfortunately, with such a statement, you would not find Mike Nesmith \[1\].

## Existing Styles

These are the limit styles provided by form-limits version 3.2.0. Please see the class itself for more up-to-date information.

- I2CE\_FormField

- null: No data array.
- not\_null: No data array.
- null\_not\_null: Choose if a value is null or not. Data array has key 'value' which is either (evaluates to) true for null, or (evaluates to) false for not null.
- max\_parent: No data array. Only valid in form relationship context.
- min\_parent: No data array. Only valid in form relationship context.
- max\_parent\_form: No data array. Only valid in form relationship context.
- min\_parent\_form: No data array. Only valid in form relationship context.
- I2CE\_FormField\_BOOL

- truefalse: No data array.
- true: No data array.
- false: No data array.
- I2CE\_FormField\_DB\_DATE

- greaterthan\_now: No data array.
- lessthan\_now: No data array.
- I2CE\_FormField\_DATE\_Y

- greaterthan: Data array has key 'year' which is a year (integer).
- greaterthan\_equals: Data array has key 'year' which is a year (integer).
- equals: Data array has key 'year' which is a year (integer).
- lessthan\_equals: Data array has key 'year' which is a year (integer).
- less\_than: Data array has key 'year' which is a year (integer).
- between: Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer).
- I2CE\_FormField\_DATE\_YMD

- greaterthan: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- greaterthan\_equals: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- equals: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- lessthan\_equals: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- less\_than: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- between: Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- I2CE\_FormField\_DATE\_MD

- greaterthan: Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).

- greaterthan\_equals: Data array has key'month' which is a month (integer), and 'day' which is the day of the month (integer).

- equals: Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- lessthan\_equals: Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- less\_than: Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- between: Data array has keys 'min' and 'max' each of which is an array containing the key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- I2CE\_FormField\_DATE\_HMS:

- greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- greaterthan\_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- lessthan\_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
- I2CE\_FormField\_DATE\_TIME:

- greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- greaterthan\_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- lessthan\_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
- between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).

- I2CE\_FormField\_DB\_INT

- between. Data array has keys 'min' and 'max.'

- equals. Data array has key 'value' which is a scalar.
- in. Data array has key 'value' which is a an array of scalar values.

- greaterthan. Data array has key 'value' which is a scalar.
- greaterthan\_equals. Data array has key 'value' which is a scalar.
- lessthan. Data array has key 'value' which is a scalar.
- lessthan\_equals. Data array has key 'value' which is a scalar.
- I2CE\_FormField\_DB\_STRING

- between. Data array has keys 'min' and 'max.'
- equals. Data array has key 'value' which is a scalar.
- in. Data array has key 'value' which is a an array of scalar values.
- greaterthan. Data array has key 'value' which is a scalar.
- greaterthan\_equals. Data array has key 'value' which is a scalar.
- lessthan. Data array has key 'value' which is a scalar.
- lessthan\_equals. Data array has key 'value' which is a scalar.
- like. Data array has key 'value' which is a scalar.
- lowerlike. Data array has key 'value' which is a scalar. match is case insensitive
- contains. Data array has key 'value' which is a scalar. match is case insensitive
- I2CE\_FormField\_DB\_TEXT

- between. Data array has keys 'min' and 'max.'
- equals. Data array has key 'value' which is a scalar.
- in. Data array has key 'value' which is a an array of scalar values.
- greaterthan. Data array has key 'value' which is a scalar.
- greaterthan\_equals. Data array has key 'value' which is a scalar.
- lessthan. Data array has key 'value' which is a scalar.
- lessthan\_equals. Data array has key 'value' which is a scalar.
- like. Data array has key 'value' which is a scalar.
- lowerlike. Data array has key 'value' which is a scalar. match is case insensitive
- contains. Data array has key 'value' which is a scalar. match is case insensitive
- I2CE\_FormField\_YESNO

- yesno: No data array.
- yes: No data array.
- no: No data array.

## References

\[1\] http://en.wikipedia.org/wiki/Michael\_Nesmith#The\_Monkees
