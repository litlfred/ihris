---
title: "iHRIS Plan use cases (2009)"
source: uploads/ihris-use-cases/iHRISPlanUseCases.doc
licence: owner permission, 2026-09-23 (see ihris-use-cases.json)
---

# iHRIS Plan: use cases (2009)

*Serlio Software Case Complete, 3/25/2009 4:13 PM. From the iHRIS use-case model by IntraHealth International / the Capacity Project iHRIS team, published here with the owner's permission. Parsed by `src/tools/ingest_use_cases.py`; do not edit by hand.*

iHRIS Plan is workforce planning and modeling software.

- This documentation refers to the core version of iHRIS Plan (working title: PowerPlan). *(2/22/2008)*
- This documentation is based on the outputs of the Workforce Planning Model Workshop, held in December 2007, and the HRH Workforce Projection Model, specifically the simplified John Dewdney version of the model. *(2/22/2008)*
- Core version 1.0 released August 8, 2008. *(9/29/2008)*

Related documents: http://www.capacityproject.org/suite/ihris\_plan.php, http://launchpad.net/ihris-plan/

## Actors

### A-PP1 Health Workforce Planner

Role: [Health Workforce Planner](roles.md#ihris-a-pp1) (`ihris-a-pp1`)

The Health Workforce Planner enters workforce data into the software, creates projections, runs scenarios, and analyzes and reports on the results. This is the primary user of the software. This person has some knowledge of workforce planning methods and access to necessary data for creating projections.

**Goals**

- Enter workforce planning data and assumptions.
- Create a projection of health workforce supply, need and costs.
- Model the effects of interventions on the health workforce projection.
- Produce health workforce plans and supporting reports.

**Use cases:** UC-PP2 Add or update a cadre, UC-PP3 Add or update a country, UC-PP1 Add or update a currency, UC-PP20 Apply interventions to a base projection model, UC-PP21 Compare actual results to predicted results, UC-PP24 Copy a projection, UC-PP8 Create a cadre pool, UC-PP12 Create a pool change, UC-PP5 Create a projection, UC-PP14 Enter attrition assumptions, UC-PP6 Enter population, UC-PP15 Enter pre-service training assumptions, UC-PP11 Enter pre-service training data, UC-PP13 Enter retirement assumptions, UC-PP9 Enter supply, UC-PP10 Enter targets, UC-PP19 Generate a base projection, UC-PP23 Import supply data, UC-PP22 Produce a health workforce implementation plan

## 1.1 Data Administration

Create and update standard lists of data for selection in system menus.

- Access is limited to Health Workforce Planners and System Administrators. *(2/6/2008)*
- Access these functions via the Configure System --> Administer Database menu links. *(7/25/2008)*

### UC-PP1 Add or update a currency

The Health Workforce Planner adds a currency for selection when setting monetary amounts.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new currency is added to the system and can be selected whenever specifying monetary amounts.

**Main success scenario**

1. Select the option to update the list of currencies.
2. The system displays all currencies entered in the system.
3. Select the option to add a new currency or update an existing one.
4. Enter the currency code.
5. Enter the name of the currency.
6. Enter the symbol for the currency.
7. Save a record (UC-ICE2).
8. The system makes the currency available for selection by symbol and code.

**Extensions**

- **3.a** An existing currency is selected.
    1. The currency opens and its information can be edited.

**Notes**

- This use case is identical to the one used in iHRIS Manage. *(2/2/2007)*

### UC-PP2 Add or update a cadre

The Health Workforce Planner enters or edits a cadre for selection within the system.

| | |
|---|---|
| Priority | P7 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** Each cadre, as applied by the health professionals, is defined within the system and available for selection in various use cases.

**Main success scenario**

1. Select the option to update the list of cadres.
2. The system displays all cadres entered in the system.
3. Select the option to add a new cadre or update an existing one.
4. Enter the name of the cadre.
5. Save a record (UC-ICE2).
6. The system displays the new or edited cadre in selection lists of cadres.

**Extensions**

- **3.a** An existing item is selected.
    1. The item form opens and the item can be edited.

**Notes**

- This use case is similar to the Add a Cadre use for iHRIS Qualify and Manage, but the qualification is not required. *(2/6/2008)*

### UC-PP3 Add or update a country

The Health Workforce Planner updates the list of countries available for selection in the system.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in to the system.

**Success guarantee.** The new or changed country is defined within the system and available for selection within various use cases.

**Main success scenario**

1. The user selects the option to manage lists of countries.
2. The system displays all countries entered in the system.
3. The user adds a new country.
4. The user enters the two-letter country code.
5. The user enters the ISO numeric code for the country (optional).
6. The user selects whether the country is the primary country for the system.
7. The user saves the record (UC-ICE2).
8. The system makes the country available for selection whenever adding geographical locations or nationalities/citizenships.

**Extensions**

- **3.a** The user selects an existing country.
    1. The system opens the country for editing.
- **6.a** The user selects the country as the primary country.
    1. The system displays the country first in all country selection menus.
- **6.b** The system determines that more than one country was selected as the primary country.
    1. The system displays all primary countries at the top of selection menus in alphabetical order.
- **7.a** The system determines that the name and country code are the same as a country previously entered.
    1. The system displays an error message and will not continue.

**Notes**

- This use case is the same for iHRIS Manage, iHRIS Plan and iHRIS Qualify. *(10/31/2007)*
- The option to use the country for location selection does not apply to Plan and is hidden. *(8/5/2008)*

## 1.2 Projection

This package enables the user to create and save a new projection or update a saved projection. The user can enter a target and non-cadre specific demographic data for projections.

- This is the first step in the workforce projection process and should appear first on the model map. *(2/6/2008)*
- The section will need to be completed before proceeding on to any other sections. *(2/6/2008)*
- Access these functions and all projection-related actions via the Manage Projections menu link. *(7/25/2008)*

### UC-PP5 Create a projection

The Health Workforce Planner creates a new projection for modeling.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in.

**Success guarantee.** The projection is saved and additional data can be added.

**Main success scenario**

1. Select the option to create a projection.
2. Enter a brief name by which to identify the projection.
3. Enter the name of the category under which to group the projection.
4. Type in a text description of the targeted goals for the projection.
5. Select the country for the projection.
6. Select the start year for the projection.
7. Enter the projection duration in years.
8. Save a record (UC-ICE2).
9. The system saves the projection and displays the entered data.
10. The system provides the options to enter additional information into the projection.

**Notes**

- The first-release model does not take into account the difference between short-term and long-term projections. *(7/23/2008)*

### UC-PP24 Copy a projection

The Health Workforce Planner copies an existing projection.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0.1 |

**Preconditions.** The projection to copy has already been entered in the system. The user is logged in.

**Success guarantee.** The original projection is copied with a new name and all of its data. The copied data can be modified or updated.

**Main success scenario**

1. Select the option to find a projection.
2. Enter the name of the projection to copy.
3. The system displays all matching projections.
4. Open the projection to copy.
5. Copy the projection.
6. The system copies all the projection data to the new projection.
7. The system makes the projection available for modifications.

**Notes**

- This is a new use case based on a request from Namibia. The purpose is to allow users to easily reuse projection data. *(9/11/2008)*

### UC-PP6 Enter population

The Health Workforce Planner enters the starting population and population growth rate for the projection.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in. The projection must be created and saved.

**Success guarantee.** The population and population growth rate are saved and are used by the system to calculate workforce requirements.

**Main success scenario**

1. Open the projection to modify.
2. Select the option to enter the population.
3. Select the year for which the population is known.
4. Enter the total population.
5. Enter the population growth rate as a percentage.
6. Enter the source of the population data.
7. Save a record (UC-ICE2).
8. The system calculates the population growth for each year in the projection.
9. The system uses the population to determine requirements.

**Extensions**

- **2.a** The population has already been entered.
    1. The system provides the option to correct the data that has been entered or to add new population data for another year.
- **3.a** The year is before the start of the projection.
    1. The system does not provide the option to select a year before the projection base year.

## 1.3 Cadre Pools

This package enables a user to define the cadres that will be modeled in the projection, enter supply and requirements data for the cadre, and enter assumptions that will affect the size of the cadre over time.

- This is the second step in the workforce planning process and should appear second on the model map. *(2/6/2008)*
- This step will need to be repeated for each cadre in the workforce projection. *(2/6/2008)*
- Assumptions should include explanation of numbers used and any defaults that are pre-entered, as well as extensive help with reaching the assumptions. *(2/6/2008)*

### UC-PP8 Create a cadre pool

The Health Workforce Planner selects a cadre and saves it as a pool of health workers in the health workforce that is being modeled.

| | |
|---|---|
| Priority | P1 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user is logged in. The target and demographics have been entered and saved. The cadre has been entered in the selection menu.

**Success guarantee.** The cadre is saved and a pool is created for that cadre that the user can add data to and update over time.

**Main success scenario**

1. Open the projection to modify.
2. Enter a name for the cadre pool.
3. Select the cadre from the dropdown menu.
4. Save a record (UC-ICE2).
5. The system saves the cadre pool name and cadre to identify the cadre pool.
6. The system provides the option to enter data for that cadre or to create another cadre pool.

**Notes**

- All data entered after this point pertain solely to the selected cadre. *(2/6/2008)*

### UC-PP9 Enter supply

The Health Workforce Planner enters data to project the actual supply of health workers.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Medium |
| Status | Released |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user must be logged in. The projection must be started or updated and population data entered. The cadre pool has been created. The currency has been entered in the system.

**Success guarantee.** The system can project the workforce supply and salary costs in that cadre for each year in the projection range.

**Main success scenario**

1. Open the projection to modify.
2. Select the cadre pool to update.
3. Select the option to enter supply data.
4. Select the year for which supply data are being entered.
5. Enter the number of staff actually employed at the start of the year.
6. Enter the data source.
7. Select the currency of the salary.
8. Enter the average salary for a worker in the cadre pool.
9. Enter the average percentage by which salaries increase each year.
10. Save a record (UC-ICE2).
11. The system calculates the population per employee at the year start.

**Extensions**

- **3.a** The supply data have already been entered.
    1. The system provides the option to correct the previously entered data or to enter new supply data for a subsequent year.
- **4.a** The year is prior to the base year of the projection.
    1. The system does not allow a year before the base year to be selected.

**Notes**

- The population per employee can be compared to the population per position calculated in the requirements. *(2/6/2008)*
- The total number of staff at year end can be compared to the required number of positions at the beginning of the next year to analyze the gap between actual and required staff. *(2/6/2008)*

### UC-PP10 Enter targets

The Health Workforce Planner enters the required number of positions for the cadre.

| | |
|---|---|
| Priority | P2 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Medium |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The user is logged in. The user has started or is updating a projection and has entered population data for the projection. The cadre pool has been created.

**Success guarantee.** The requirements are correctly calculated and can be graphed in the results.

**Main success scenario**

1. Open the projection to modify.
2. Select the cadre pool for which to enter target data.
3. Select the option to enter target data.
4. Select the year for which targets are known.
5. Enter the target as either:
    - the number of positions to be filled in the year or
6. the health worker-to-population ratio target.
7. Enter the data source.
8. Save a record (UC-ICE2).
9. The system calculates the required number of positions needed to maintain the initial position-to-population ratio for each year in the projection range.

**Extensions**

- **2.a** The target data have already been entered.
    1. The system provides the option to correct the previously entered data or to add new target data for a subsequent year.
- **4.a** The year is before the base year of the projection.
    1. The system does not provide an option to select a year prior to the base year.
- **5.a** Both a number and a ratio are entered.
    1. The system generates an error and will not continue.

**Notes**

- The population per position remains the same for each year; requirements are calculated based on this figure. *(2/6/2008)*

### UC-PP12 Create a pool change

The Health Workforce Planner creates a change in the pool supply due to an increase or decrease in health workers to be applied to the projection.

| | |
|---|---|
| Priority | P6 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Status | Updated |
| Implementation status | Complete |
| Release | 1.0 |

**Preconditions.** The projection has been created and a cadre pool has been created for it. Supply data have been entered for the cadre pool. The currency has been entered in the system.

**Success guarantee.** The system calculates the changes to the supply of health workers and displays the results in the projection.

**Main success scenario**

1. Open the projection to modify.
2. Select the cadre pool to update.
3. Select the option to enter a pool change.
4. Enter a name for the pool change.
5. Enter a description of the assumption being made.
6. Select whether to enable the pool change.
7. Select whether the pool change is a:
    - intake, or increase in health workers
    - exit, or decrease in health workers
8. Enter the data source.
9. Enter the change amount as either the number or the percentage of health workers to increase or decrease the supply by.
10. Enter a maximum amount for the change (optional).
11. Select a currency for any costs associated with the change.
12. Enter the average cost of the change per year per worker (optional).
13. Enter the average percentage increase in the costs per year (optional).
14. Select the initial year to apply the change.
15. Enter the number of years to apply the change.
16. Save the change (UC-ICE2).
17. The system calculates the effects of the change on the projected workforce and the costs.

**Extensions**

- **6.a** The pool change is disabled.
    1. The change does not affect the projection and the data are not displayed in the projection.
- **9.a** A number of health workers is entered.
    1. Enter the rate by which to increase the amount of workers added to or subtracted from the supply (optional).
- **9.b** Both an amount and a percentage are entered.
    1. The system generates an error and will not continue.
- **14.a** A year is not selected.
    1. The system selects the base year for the initial year.
- **15.a** The number of years is not entered.
    1. The system calculates the change for the entire projection duration.
- **17.a** There is more than one change affecting the cadre pool.
    1. Repeat all steps for each pool change.

## 1.4 Data Modeling

This module enables a user to graph the actual and required human resources pools, showing changes over time as determined by the influences. The user may then define one or more interventions on actual human resources by adjusting variables from a menu of options. The graph will dynamically update, showing the results of the interventions as they are adjusted.

### UC-PP19 Generate a base projection

Before the Health Workforce Planner can run any interventions, a base projection must be generated showing the gap between resources and requirements.

| | |
|---|---|
| Priority | P3 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | Low |
| Status | Updated |
| Implementation status | Partially Complete |
| Release | 1.0 |

**Preconditions.** The user is logged in. The projection has been created and all requirements, supply and pool change data have been entered.

**Success guarantee.** The base projection and costs projection are generated, and all data for the projection are displayed.

**Main success scenario**

1. Select a projection model.
2. Select the cadre pools within the projection to include in the model.
3. The system generates the base projection graph of changes in total numbers for all health workers and all required workers over the date range of the projection.
4. The system graphs the costs of all workers over the duration of the projection.
5. The system displays the data for all selected cadre pools by year.
6. The system provides the option to print the base projection as a graph or table.

**Extensions**

- **3.a** Supply and target data have been entered for more than one year in the projection.
    1. The system displays separate graph lines for each year that data were entered.
- **5.a** The user disables a cadre pool change in the model.
    1. The system hides the pool change data and does not include the data in calculating the results of the model.
    2. The system graphs the new supply and the original supply on the same model.

### UC-PP21 Compare actual results to predicted results

After proposed interventions have been implemented, the Health Workforce Planner regularly imports new actual human resources data to determine whether the interventions are having the desired effect and to make adjustments as needed.

| | |
|---|---|
| Priority | P2 |
| Primary actors | [Health Workforce Planner](roles.md#ihris-a-pp1) |
| Level | User |
| Complexity | High |
| Status | Documented |
| Implementation status | Complete |
| Release | 1.0.1 |

**Preconditions.** The user is logged in. A projection has been completed created and saved.

**Success guarantee.** Interventions are producing results.

**Main success scenario**

1. Select a saved projection.
2. Enter a new starting year subsequent to the initial data.
3. The system creates a projection with the new starting year using all assumptions and requirements entered for the saved projection.
4. Enter the training data for the new starting year (UC-PP11).
5. Enter the workforce data for the new starting year (UC-PP9).
6. Save the projection for comparison.
7. The system generates a report comparing the projected results for the original projection to the actual results.
8. The system provides the option to adjust the assumptions for the new projection.
9. The system provides the option to adjust the requirements for the new projection.

**Notes**

- Assumptions: Proposed interventions in the model have been implemented for at least one calendar year; human resources data have been collected for the preceding year. *(11/12/2007)*
- Triggered when new human resources data are available; this use case will generally occur on an annual cycle. *(11/12/2007)*

## 1.5 Requirements

This package holds miscellaneous requirements for the project.

- Requirements are still in the process of being defined. See the wiki for a full list of proposed requirements. *(2/6/2008)*

Related documents: http://open.intrahealth.org/wiki/index.php/Planned\_Features\_--\_Software, http://open.intrahealth.org/wiki/index.php/Planned\_Features\_--\_Workforce\_Projection\_Model

## Cited but not described

The report cites these, but describes none of them:

- UC-PP11 *Enter pre-service training data* (cited by A-PP1, UC-PP21)
- UC-PP13 *Enter retirement assumptions* (cited by A-PP1)
- UC-PP14 *Enter attrition assumptions* (cited by A-PP1)
- UC-PP15 *Enter pre-service training assumptions* (cited by A-PP1)
- UC-PP20 *Apply interventions to a base projection model* (cited by A-PP1)
- UC-PP22 *Produce a health workforce implementation plan* (cited by A-PP1)
- UC-PP23 *Import supply data* (cited by A-PP1)
