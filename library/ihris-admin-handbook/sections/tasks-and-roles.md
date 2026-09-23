---
title: "Tasks and Roles"
source: http://open.intrahealth.org/w/index.php?oldid=4219
contributors: ["Litlfred", "MarkAHershberger"]
pages: 513-516
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Tasks and Roles

## Roles

A role is a collection of tasks that can be assigned to a user's account.

- role names are defined as the children of the magic data path /I2CE/roles/names
- a role $role has a display name defined at /I2CE/roles/names/$role/display\_name
- roles can inherit tasks from one another by adding it as a value of a child node of /I2CE/toles/names/$role/trickle\_up For example, in iHRIS Manage at the /I2CE/roles/names/hr\_staff we have:

- display\_name =&gt; HR Staff
- trickle\_up =&gt; Array

- 0 =&gt; admin
- 1 =&gt; hr\_manager

says that the role hr\_staff is displayed as 'HR Staff' and that an hr\_manager or admin has all the tasks that a hr\_staff has.

## Tasks

A task can be both a collection of sub-tasks that this task has and description of some action that can be checked for permission. Task information is stored in magic data under /I2CE/tasks/. To create a task you create a scalar type child node of /I2CE/tasks/task\_description. That name node of the node is the name used to reference the task. The value of the node is the description of the task displayed in the Task and Role Management page. For example, the magic data node /I2CE/tasks/task\_description may look something like:

- custom\_report\_admin =&gt; Allows administration of the Custom Reporting System
- custom\_reports\_can\_access =&gt; Allows minimal access to the Custom Reporting System
- custom\_reports\_delete =&gt; Allows deletion of data about custom reports
- custom\_reports\_can\_access\_relationships =&gt; Allows access to the Custom Report Relationships

You can define the sub tasks of a task $task by specifying /I2CE/tasks/task\_trickle\_down\_task. For example, the magic data node /I2CE/tasks/task\_trickle\_down/custom\_reports\_admin may look like:

- 0 =&gt; custom\_reports\_can\_access
- 1 =&gt; custom\_reports\_delete\_reports

which says that the 'custom\_report\_admin' task has all the tasks and rights defined by 'custom\_reports\_can\_access' and 'custom\_reports\_delete\_reports.'

The tasks that are assigned to a role $role are the values of the children under /I2CE/tasks/role\_trickle\_down/$role

A user with the role 'admin' has all tasks.

## Uses of Tasks and Roles

The tasks and roles are used in several places:

- The main I2CE\_Page class checks for basic permission for the page.
- Several pages perform checks for specific roles and tasks in their action() method.
- Just before displaying the HTML the I2CE\_Template, class verifies that all tasks, roles and permissions are satisfied on each node.

## Task and Role Administration

For deployment across many computers, tasks and roles should be set up in an appropriate module configuration file.

For setting tasks and roles dynamically, the module 'tasks-roles' provides the page named 'roles' and the page named 'tasks' that allows creating new roles and tasks as well as defining the permission inheritance.

## Permissions and the Permission Parser

The permission parser allows logical expressions to combine severals types permissions, such as task, roles, into a permission string.

We can assign tasks, roles and permissions to DOM nodes by:

- Setting the attribute role. If the values is X, this results in the permission string role(X) which is passed to the permission parser
- Setting the attribute task. If the values is X, this results in the permission string task(X) which is passed to the permission parser
- Setting the attribute permission.

If the node fails any of the role, task or permission checks it will remove the node

## Permission Types: task and role

The task and role type permissions are formed by surrounding a role name with role() or a task name with task(). For example, you can create the following permission string:

```
(task(can_edit_database_list_facility_type) & task(can_edit_database_list_fav_color) || role(admin)
```

By default, tasks and roles are 'OR'ed together so the following are all the same:

- task(can\_edit\_database\_list\_facility\_type) or task(can\_edit\_database\_list\_fav\_color)
- task(can\_edit\_database\_list\_facility\_type) | task(can\_edit\_database\_list\_fav\_color)
- task(can\_edit\_database\_list\_facility\_type) task(can\_edit\_database\_list\_fav\_color)
- task(can\_edit\_database\_list\_facility\_type,can\_edit\_database\_list\_fav\_color)
- task(can\_edit\_database\_list\_facility\_type can\_edit\_database\_list\_fav\_color)
- task(can\_edit\_database\_list\_facility\_type|can\_edit\_database\_list\_fav\_color)

## Permission Type: module

Any public function of a module class can be called by the permission parser. For example, suppose that the module 'my\_module' has a method 'my\_method()' then we can use as the permission string with arguments:

```
module('my_module','my_method', [arg1], ... , [argN])
```

which would results in the call:

```
$module->my_method($arg1,..,$argN)
```

where $module is the instance of the module class for the module 'my\_module.'

## Permission Type: form

The 'forms' module adds in the form type. The permission string with arguments:

```
form('form_name', 'form_method', [arg1] , .., [argN])
```

results in the call:

```
$form->form_method($arg1,..,$argN)
```

where $form is the result of getting the form by the name of 'form\_name' via template data for node (if there was any) the permission string was assigned to.

## Arguments

A permission type (such as role, task, form or module) in a permission string behaves essentially like a function. Suppose that we have the general shape for a piece of a permission string:

```
type([arg1],[arg2],...,[argN])
```

Then this results in the method call:

```
$permissionParsrer->hasPermission_$type($node,$args)
```

where $node is the DOMNode the permission string was called on and $args is the array($arg1,..$argN). The permission parser turns \[argM\] into $argM according to the following rules:

- if \[argM\] starts with a $ then it refers to template data and the following rules apply:

- The string has the form $abcd. The value of $argM becomes the template display data with name 'abcd.'
- The string has the form ${WXYZ}abcd. The value of $argM becomes the template data with category 'WXYZ' and with name 'abcd.'
- &lt;NODE&gt; becomes the instance of DOMNode (if any) that the permission string was called on
- &lt;TEMPLATE&gt; becomes the instance of I2CE\_Template (if any) that the permission parser was called on
- &lt;USER&gt; becomes the instance of I2CE\_User that is this session
- if \[argM\] starts with a single quote ' then it is a string until the next non-escaped ' is found
- if \[argM\] starts with a double quote " then is is a string until the next non-escaped " is found. In addition the following substitution rules apply:

- any substring starting with $ and consisting of alpha-numeric characters, - or \_ is interpreted as template display data to be substituted For example "my name is $name" becomes "my name is Joe" if the template data named 'name' and with type DISPLAY is "Joe"

- any substring starting with {$ is read until an enclosing } is found. The string between the ${ and } is the name of DISPLAY template data which is then substituted.
- To prevent the above, { and $ may be escaped with a \\
- any other string of alpha-numeric characters (and a few permitted punctuation marks) is interpreted as a string

Arguments may be separated by a comma a space or a |.

## New Types

A module can add in a fuzzy method of the form hasPermision\_$type to the I2CE\_PermissionParser class to enable a new permission type. For example the 'forms' module does this by adding in a new permission type 'form.'
