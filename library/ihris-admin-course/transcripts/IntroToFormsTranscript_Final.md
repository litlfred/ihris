# Introduction to Forms (audio transcript)

## Slide 1

Forms are the central part of the data structure in I2CE and iHRIS. A form is a collection of data elements, called ‘fields’, or sometimes called ‘form fields.’ A basic example to keep in mind is a form called Person with the fields Surname, First Name, Date of Birth, and Gender.

If you want, you can think of a form as a table in a database, and the columns of that table are the fields. A row of that table is an ‘instance’ of the form and is determined by a special field called Id.

Forms can be related to each other. There is another special field that all forms have called Parent, which allows you to create a ‘parent-child’ relationship between two forms. There are also special ‘mapped’ fields that let you link any form to special ‘List’ forms.

In this module, we will look at how forms are defined in magic data and created within the system by the ‘form factory.’ We will see that a form can be stored multiple ways in the database, and in fact does not need to be stored in the database at all.

## Slide 2

As previously mentioned, the data elements of a form are called fields, which you can think of as columns in a database. The field is not just a data value, but is a class in PHP, specifically a sub-class of I2CE\_FormField. This class controls how that type of field is displayed and edited by the end-user, and also determines the value of that field when it gets stored to the database.

There are many types of fields that you can use. For example, Yes/No fields, Integers, Strings, Multi-line strings, Dates, and Mapped Values.

In addition to each field, we have associated ‘limits.’ Limits are used to search for all forms that have a particular value for that field. For example, a limit could be used to find all Person Forms with a surname that starts with the letter ‘M.’ As another example, you can look for all salaries that are greater than $20,000.

## Slide 3

Let us look a bit closer at two examples, or instances, of a Person Form. Every form we look at has a special field called the Id that tells us which instance of the form we are looking at. Remember, if you are thinking of the form as a table, then the instance is just the row of that table, and the id is the unique identifier for that row.

In our two instances, we have Ids ‘10’ and ‘11.’ The vertical bar is called a ‘pipe,’ and if we need to refer to these two instances of the Person Form, we refer to them as ‘person\|10’ and ‘person\|11.’ Next we have the fields Surname and First Name. These fields have type STRING\_LINE which means that the person's first name and surname is just a line of text.

There is a birth\_date field with type DATE\_YMD, meaning that the birth date is a date where you need to choose the Year, Month, and Day.

We have a field called Gender which is a special type of field called a MAP field. MAP fields are links to elements of a list, which is a special type of form. In this case, the list is the list of genders, Male and Female. The two instances of the Gender Form are ‘gender\|M’ and ‘gender\|F,’ which is the value stored for each person's gender.

Did you notice any data quality issues here? Look at the date of birth for ‘person\|11.’

## Slide 4

Let's take a closer look at the Gender Form. The Gender Form is a ‘list,’ in fact a ‘simple list,’ with only two fields: the special Id field and the Name field. We have already seen two instances of the Gender Form, one has the Id ‘M‘ and the other ‘F.’ The name field is where we store the values ‘Male’ and ‘Female.’

## Slide 5

Now let's take a look at the other special field, Parent, that all forms have. This Parent field lets you set any form as a ‘child’ of another form. By adding a child form to another form, you can add more information to that form.

For example, we could associate a passport photo to a Person Form. Here we create a new form called Passport Photo. It has, as all forms do, the special field Id. We set the field Parent to ‘person\|10’ and in this way we know that this passport\_photo is associated to ‘person\|10,’ in other words, to ‘Carl.’

The last field is Photo, which has type IMAGE. The value of this field is the actual image we want associated to the person as a passport photo. Here we have only set ‘passport\_photo\|10’ associated to person\|10. In fact, we can add as many Passport Photo Forms as children of person\|10 as we want.

## Slide 6

Now that we have an idea of how data is stored in the forms and how forms can be related to each other, we can look at the bits of iHRIS and I2CE that actually manage the forms. These are the PHP class I2CE\_Form and all its subclasses. One example of such a subclass is I2CE\_List. It is the one that handles all lists in the database.

When defining forms, it is to the form class, that the fields are actually added. As we often have multiple forms sharing the same field, we can reuse the form class for all these forms.

A good example of this is I2CE\_SimpleList. This is a form class which extends I2CE\_List, which in turn extends I2CE\_Form. The list forms such as gender, cadre, or facilty\_type are all examples of forms whose form class is I2CE\_SimpleList. So you know that each of these forms have the same fields as did the gender form, namely Id and Gender.

Another reason to use form classes is that sometimes we may want to add some extra PHP code to add additional functionality to the form. A good example of this is the I2CE\_List class which has lots of code to generate the data for the drop down lists and data trees that you see in iHRIS.

## Slide 7

Now we need to look at the thing that creates the form. This is the ‘form factory.’ In this first code snippet, we see an instance of the form factory, create a form object for the form instance, ‘gender\|M,’ and then a form object for the form instance ‘person\|10.’

Please note, here we have only created the data structures to hold the data of gender\|M and person\|10 forms. Let's look a bit more at what happens within the form factory when the gender object is created by the method ‘createForm’ called with the argument ‘gender\|M.’

First we look at the form name, ‘gender,’ and see that it is associated to the I2CE\_SimpleList form class. We will see how this association is stored in magic data a bit later. Next we create a new form object whose class is I2CE\_SimpleList. Then we add in the Name field, which is an I2CE\_FormField\_STRING\_LINE. Finally, we set the id of this form object to be M.

## Slide 8

We used the form factory to create the data structure for the form, and set the Id of the form that we are using. We have not actually read the data values from the data base. For this, you would use the ‘populate’ method.

## Slide 9

The different ways that a form can be stored in a database, or even in an XML or a CSV file, are the form storage mechanisms. There are many types, but the most important ones that you should be aware of are entry, magic data, flat, and multi-flat.

The entry form storage mechanism is the default storage mechanism used by all forms. This form storage mechanism logs all changes to the forms based on the user and time. The data here are stored in a series of tables including ‘entry,’ ‘last\_entry,’ ‘form,’ ‘field,’ ‘form\_field’ and ‘record.’ If you are familiar with OpenMRS, this is similar to the type of database structure they use.

The second storage mechanism, magic data, is primarily designed for easy management of standardized data lists that are common among many installations of iHRIS. For example, these could be the cadres allowed, or the geographic breakdown of the country. These data should be centrally managed.

The flat storage mechanism is a form storage mechanism that reads in data from what you might think of as the usual way of storing data in a database. There is one table, the rows of the table are the instances of the forms, and the columns are the fields.

Since there are many ways to the read data for a form, some of which may be very slow, we use a form caching mechanism to ensure quick reads of the data. These form caches are exactly the same as the flat tables.

The last form storage mechanism is multi-flat. This is used for decentralized iHRIS installations. In this case, you are loading many different databases, for example one for each of your districts, and you want to read in data from each of the databases as a UNION.

## Slide 10

Now that we know all of the pieces that make up a form, we can look at how to define them in magic data. Let us look at an easy form to define, the Gender Form. The values of this form populate any drop down menus that map to the Gender field, for example the Gender field in the Person Form. ‘Gender’ is how to refer to the form when programming. The form will also need a name that will be displayed to the end user. Finally, as this list is a standard list which should be shared across all sites (or installations) it should be saved in magic data.

## Slide 11

This xml snippet is all we need to define the Gender Form. Let us look at the various pieces. First we have the path ‘/modules/forms/forms/gender’ which is the path in magic data to where we store all the meta-information about the Gender Form.

## Slide 12

This next bit tells us what the form class is, which in this case is I2Ce\_SimpleList. Specifically what we have done is set the value of the magic data node at /modules/forms/forms/gender/class to be I2CE\_SimpleList.

## Slide 13

Next we are setting the display name, which is the name that will display to the end user, for this form. Specifically we set the value of the magic data node /modules/forms/forms/gender/display

to be ‘Gender.’ You will also notice that we have set the locale attribute to: en\_US. This is the way that we mark that ‘Gender’ should be translated.

## Slide 14

Finally, we set the magic data node /modules/forms/forms/gender/storage to be “magicadata” which means that we want to store the data values for all instances of this form in magic data.

## Slide 15

Since we have set the form storage mechanism for the Gender Form to be magic data, this means that we can define all data values for all instances of the Gender Form in magic data. And this is what we are looking at here. Here we see that all the data values for the Gender Forms are stored under the magic data node /I2CE/formsData/forms/gender

## Slide 16

Now we are looking at the instance of the Gender Form with id ‘F.’ All of the data values for this instance are stored under the node /I2Ce/formsData/forms/gender/F

We should also have similar snippet for the Male gender which would live under

/I2Ce/formsData/forms/gender/M

## Slide 17

The first node living under /I2CE/formsData/forms/gender/F is the node "last\_modified." This value of this node is the date that this form was last modified. This is an optional value, but setting it appropriately will speed up the caching of Gender Form data as it can use the last\_modified time to quickly see if the cache is out of date.

## Slide 18

The next node living under /I2CE/formsData/forms/gender/F is the node ‘fields’ which contains all of the data values for the form instance ‘gender\|F.’ As gender was a simple list, there is only one field name. In this case the name is ‘Female’ and setting the locale attribute tells the system that we should look for translations of the word female. The delimited attribute on the fields node means that everything under it should be read as key-value pairs with the key to the left of the colon and the value to the right of the colon. Specifically what we have done here is set the value of the node

/I2CE/formsData/forms/gender/fields/name to have its English value as "Female."

## Slide 19

Now that we understand a bit about how forms are defined in magic data, let us look at an example of defining the underlying form class. The form classes are also defined in magic data, this time under the node /modules/forms/formClasses.

Let us take a look at the form class I2CE\_SimpleList which is associated to the Gender Form.

All of the data for the I2CE\_SimpleList form class lives under /modules/forms/formClasses/I2CE\_SimpleList.

Recall that we had said the form class was I2CE\_SimpleList which extends form I2CE\_List. And we have captured this information here by setting the value of the /modules/forms/formClasses/I2CE\_SimpleList/extends to I2Ce\_List.

## Slide 20

Now we need to enter in the field information for the I2CE\_SimpleList which will live under the sub-node ‘fields.’ For the simple list, we only had one field name which had type STRING\_LINE, and this is what we see here. Specifically we are setting the value of the magic data node

/modules/forms/formClasses/I2CE\_SimpleList/fields/name/formfield to STRING\_LINE

## Slide 21

Next we need to set the ‘header’ for the Name Field. This is the label for the field that gets displayed to the end user next to the data value. You can have many headers for a single field that you can use in various contexts but you should always have a default header. In this case, we want the default header to be "Name," so we set the value of magic data node

/modules/forms/formClasses/I2CE\_SimpleList/fields/name/headers/default to have value ‘Name.’

Since we wanted "Name" to be translatable, we have set the locale attribute to en\_US as usual.

## Slide 22

As the value of Name Field is what is displayed in the drop down lists, we want to ensure that the Name Field is always set, or required. This is what we are doing here. Specifically, we are setting the magic data node /modules/forms/formClasses/I2CE\_SimpleList/fields/name/required to have the Boolean value, ‘true.’

## Slide 23

Finally, since the Name Field is what is used in the drop down lists, we want to ensure that it is not only set, but that it is unique. This is what we are doing here by setting the magic data node

/modules/forms/formClasses/I2CE\_SimpleList/fields/name/unique to have the Boolean value, ‘true.’
