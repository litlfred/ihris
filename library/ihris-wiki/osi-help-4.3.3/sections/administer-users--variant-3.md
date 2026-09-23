---
title: "Administer Users"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-qualify/modules/qualify-help/static/help/ihris_administer_users.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Administer Users

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**

Click Administer Users to create, update and disable user accounts to enforce secure access to the system. Only the System Administrator can add and update user accounts.

## Add a User

In order to allow a user to access the system, the System Administrator must create a user account for the person, with a unique username and password. Each user is assigned a role, which determines the actions that the user can perform in the system.

|  |  |
| --- | --- |
| On the Home page or left menu, click Configure System. Click Administer Users.    Select Add New User from the dropdown menu and click the `Add` button. | Image:AddUser1.jpg |
| The Administer Users form opens. Enter a **Username** for the user: one word with no special characters (letters and numbers only).    Enter the **First Name** and **Surname** of the user.    Enter an **Email** for the user, if known (optional).    Select the **Role** of the user (see below for roles). If no role is selected, the user will be disabled and cannot access the system in any capacity.    Select the option to randomly **Generate New Password** or enter a **Password** for the user. If the password is entered, re-enter it to confirm. The two passwords must match.    Click `Confirm` and confirm that the account entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:AddUser2.jpg |

If an email address was entered, an email message will be sent to the user with the username and password. Otherwise, you will have to provide the user with the username and password.

### iHRIS Qualify User Roles

* **Administrator:** has full access to the system

* **Data Operations Manager:** manages system data, including correcting data and managing data selection lists; can search for, view, enter data in and correct any record and generate any report

* **Decision Maker:** generates reports in order to analyze data; can search for and view any record but cannot enter data into the system

* **Records Officer:** enters general information about health workers, including demographic, education, identification, contact, training, deployment and out migration information, as well as notes

* **Registration Supervisor:** enters all general information about health workers, plus issues registrations, licenses and private practice licenses, and enters continuing education information and disciplinary notices

### iHRIS Manage User Roles

* **Administrator:** has full access to the system

* **Executive Manager:** generates reports in order to analyze data; can search for and view any record but cannot enter data into the system

* **HR Manager:** manages system data, including correcting data and managing data selection lists; can search for, view, enter data in and correct any record and generate any report

* **HR Staff:** enters and updates records and positions; can generate any report

* **Training Manager:** sets up the in-service training management program, schedules employees for trainings and evaluates employees performance in trainings

### Troubleshooting

**A required field was not completed.**

The system will display an error message. The required field(s) will be outlined in red. Complete the missing fields and try saving again. If you do not want to add the user account after all, click `Return (do not save changes)`.

**The username is already in the system.**

The system will generate an error for duplicate usernames. Return to the Administer Users screen and select the username from the dropdown menu to edit the user account (see [Update a User](#Update_a_User "Administer Users")).

## Update a User

If information about a user has changed, the System Administrator can update the user account with the change. Usernames and passwords may also be changed. If a user no longer has access to the system, the account can be disabled.

|  |  |
| --- | --- |
| On the Home page or left menu, click Configure System. Click Administer Users.    From the menu select the user account to change. | File:UpdateUser2.jpg |
| The user account information is displayed. Make the change or select "No Access" from the **Role** menu to disable the account.    Click `Confirm` and confirm that the changes entered are correct. If they are not correct, click `Edit` to change them. If they are, click `Save` to save them. | File:UpdateUser3.png |

### Troubleshooting

**A required field was not completed.**

The system will display an error message. The required field(s) will be outlined in red. Complete the missing fields and try saving again. If you do not want to update the user account after all, click `Return (do not save changes)`.

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**
