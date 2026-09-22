---
title: "Add and Edit Geographical Areas (4.0.4)"
source: MediaWiki page exported into the iHRIS 4.3.3 help modules
shippedIn:
  - ihris-manage/modules/manage-help/static/help/ihris_add_and_edit_geographical_areas.html
  - ihris-manage/modules/manage-help/static/help/ihris_add_and_edit_geographical_areas_4.0.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_and_edit_geographical_areas.html
  - ihris-qualify/modules/qualify-help/static/help/ihris_add_and_edit_geographical_areas_4.0.html
licence: GPL-3.0 (as part of the iHRIS source)
---

# Add and Edit Geographical Areas (4.0.4)

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**

To ensure that standard data types such as cadres, marital status, geographical locations and the like are enforced across the system, those standard data types must be created as lists. These lists are used to create selection menus that provide standard options for selection when adding records, jobs and positions. Click Administer Database to create and update standards lists of data for selection in system menus. Only the Data Operations Manager and System Administrator can create data types.

## Add a Country

You will need to add at least one country to the system for selection whenever a geographical location is required. This should be the country where your organization's headquarters are located. In addition, you should add the names of all countries where employees are located or all nationalities you would like to track in the system.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    In the "Geographic Information" section, select Country. | Image:AddCountry1.png |
| The Country page opens, showing all the countries entered in the database. Click Add New Country. (To edit an existing country, click its name and then click Update This Information.) | Image:AddCountry2.png |
| The Country form opens. Enter or edit the **Name** of the country.    Enter the **2 Character Alpha Code** for the country.    Enter the **ISO Numeric Code** for the country (optional).    If the country is the primary country where your organization is located, select Yes in the **Primary Country** menu. This will place the country name at the top of all country selection menus. Otherwise, leave the default as No. There can be multiple primary countries.    If the country is to be used for locations, such as addresses, select Yes in the **Use for Location Selection** menu. Selecting No will not display the country in any location selection menus, only for nationality selection.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:AddCountry3.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Make sure that the country and two-letter country code have not previously been entered into the system. The system will not allow duplicate countries. Also check that the country name and code have been entered -- these fields are required. Required fields will be outlined in red. Try completing the missing fields or changing the country name and saving again. If you do not want to add the country after all, click `Return (do not save changes)`.

**The required 2-Character Alpha Code is not known.**

Find a complete list of 2-letter country codes on the International Organization for Standardization (ISO) website.

## Add a Region

A *region* is a major subdivision of a country. Region choices depend on which country is selected; only a region that is associated with a particular country can be chosen when that country is selected. For each country you have entered in the system, add at least one region.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    In the "Geographic Information" section, select Region. | Image:AddCountry1.png |
| The Region page opens. Click Add New Region. (To edit an existing region, select its country from the menu and click the `View` button; then click the region's name and click Update This Information.) | Image:AddRegion1.png |
| The Region form opens. Enter or edit the **Name** of the region.    Type the name of or select the **Country** in which the region is located.    Enter a **Code** for the region (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:AddRegion2.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Check that a region with the same name has not already been entered for that country. There cannot be two regions with the same name in the same country. Also make sure that the region name was entered and its country was selected -- these fields are required. Required fields are outlined in red. Fill in the missing information and try saving again. If you do not want to add the region after all, click `Return (do not save changes)`.

**The country name is not available for selection.**

Next to "Country", click Add New and add the country. Then click Administer Database and follow the steps above to add the new region. You will have to re-enter any information that you previously entered for the region.

## Add a District

A *district* is a subdivision of a region. In some locations, the district may be called the *state* or *province*. District choices depend on which country is selected; only a district that is associated with a particular country can be chosen when the country is selected. For each region you have entered in the system, add at least one district.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    In the "Geographic Information" section, select District. | Image:AddCountry1.png |
| The District page opens. Click Add New District. (To edit an existing district, type or select the region where it is located and click the `View` button; then click the district's name and click Update This Information.) | Image:AddDistrict1.png |
| The District form opens. Enter or edit the **Name** of the district. | Image:AddDistrict2.png |
| Type the name of the **Region** or select the **Country** and then the **Region** in which the district is located.    Enter a **Code** for the district (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:Add District3.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Check that a district with the same name has not already been entered for that region. There cannot be two districts with the same name in the same region. Also make sure that the district name has been entered and the country and region for the district were selected -- these fields are required. Required fields are outlined in red. Fill in the missing fields and try saving again. If you do not want to add the district after all, click `Return (do not save changes)`.

**The region name is not available for selection.**

Beside **Region**, click Add New and add region. Then click Administer Database and follow the steps above to add the new district. You will have to re-enter any information that you previously entered for the district.

## Add a County

A *county* is a smaller geographical division within a district. The term *county* corresponds to *sector* in some locations. Assigning counties is optional for this system. County choices depend on which district is selected; only a county that is associated with a particular district can be chosen after that district is selected. For any district entered in the system, you may add multiple counties.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    In the "Geographic Information" section, select County. | Image:AddCountry1.png |
| The County page opens. Click Add New County. (To edit an existing county, type or select the district where it is located and click the `View` button; then click the county's name and click Update This Information.)    Enter or edit the **Name** of the county. | Image:AddCounty1.png |
| The County form opens. Type the name of the **District** or select the **Country**, the **Region** and the **District** in which the county is located.    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:AddCounty2.png |

### Troubleshooting

**An error message appears when the Confirm button is clicked.**

Check that a county with the same name has not already been entered for that district. There cannot be two counties with the same name in the same district. Also check that the county name has been entered and the country, region and district have been selected -- these fields are required. Required fields will be outlined in red. Try completing the missing fields and saving again. If you do not want to add the county after all, click `Return (do not save changes)`.

**The correct district is not available for selection.**

Click Add New beside **District** and add the new district. Then click Administer Database and follow the steps above to add the new county. You will have to re-enter any information you previously entered for the county.

## Add a Currency

If your organization pays salaries or other payments in more than one currency, you should add each currency. The correct currency may then be selected when entering the salary or special payment. At least one currency should be added.

|  |  |
| --- | --- |
| From the home page or left menu, click Administer Database under Configure System.    In the "Geographic Information" section, select Currency. | Image:AddCountry1.png |
| The Currency page opens, showing all currencies entered in the database. Click Add New Currency. (To edit an existing currency, click its name; then click Update This Information.) | Image:AddCurrency1.png |
| The Currency form opens. Enter the **Currency Code**, an abbreviation that will identify the currency in selection menus.    Enter the **Name** of the currency (optional).    Select the **Country** for the currency (optional).    Enter the **Symbol** for the currency; the symbol will also appear in selection menus (optional).    Click `Confirm` and confirm that the information entered is correct. If it is not correct, click `Edit` to change it. If it is, click `Save` to save it. | Image:AddCurrency2.png |

### Troubleshooting

**An error message appears when Confirm is clicked.**

Make sure the currency code was entered and that it is not the same as a code that has already been entered. Change the code and try saving again. If you do not want to add the currency after all, click `Return (do not save changes)`.

**The currency code is not known.**

Find a list of all standard currency codes at the International Organization for Standards (ISO) website.

**The country for the new currency is not available for selection.**

Click Add New next to **Country** and add the country name. Then click Administer Database and follow the steps above to add the new currency. You will need to re-enter any information you previously entered for the currency.

**How do I enter a currency symbol that does not appear on my keyboard?**

If you are using a Windows computer and have a separate numeric keypad on your keyboard, you may enter a currency symbol by holding down the ALT key and typing in the code for the symbol on the numeric keypad, then releasing the ALT key.

* British pound: ALT+0163

* Euro: ALT+0128

* Yen: ALT+0165

* Generic currency symbol: ALT+0164

The symbol is optional and may be omitted.

***Return to the* [iHRIS Qualify User Manual index page](ihris_qualify_user_manual.html "iHRIS Qualify User Manual").**
