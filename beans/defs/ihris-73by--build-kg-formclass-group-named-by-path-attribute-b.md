---
# ihris-73by
title: 'build_kg: formClass group named by path attribute becomes a phantom class'
status: completed
type: task
tags:
    - bug
    - build-kg
created_at: 2026-09-23T11:33:09Z
updated_at: 2026-09-23T11:33:09Z
---

Found by agent-2 in the round-2 wireframe review.

`src/ihris-common/data-model/4.3.3/formClass.json` is an extraction artefact. `ihris-common/modules/TrainingCourse/modules/TrainingInstructor/TrainingInstructor.xml` line 35 reads:

    <configurationGroup name="formClass" path="/modules/forms/formClasses/iHRIS_Scheduled_Training_Course">

I2CE lets a `path` attribute name the target. `src/tools/build_kg.py` (~line 397) takes `g.get("name")` as the class, so:
- a phantom class `formClass` is created;
- `iHRIS_Scheduled_Training_Course` loses its `training_instructor` field (REFERENCE to person), which the module adds.

**Fix:** when a group carries `path`, take the class from the last segment of the path (and check other walkers, forms and lists, for the same pattern). Then regenerate:
- counts become 155 records / 152 classes, unless other groups follow the same pattern;
- update `docs/design/wireframes/data-model-site/intent.md`, `round-2/intent.md` and `round-2/h.html`, which quote 93 / 156 / 153;
- the data dictionary will change: `build_dak.py` loses a logical model and `iHRIS_Scheduled_Training_Course` gains a data element.

## Outcome (2026-09-23)

`build_kg.py` now names forms, form classes and pages by the last segment of the resolved path. The bug was wider than one class:

| phantom record | real class(es) | module |
|---|---|---|
| `formClass` | field `training_instructor` merged into `iHRIS_Scheduled_Training_Course` | training-instructor |
| `class` | `I2CE_Form_Locale` | LocaleForm |
| `user_request_class_data` | `I2CE_User_Request` | RequestAccount-VerifyEmail |
| `dep_class` (two classes merged into one) | `iHRIS_Dependent` and `iHRIS_NextOfKin` | dependents, nextOfKin |

Form names were fixed too, e.g. `roleForm` becomes `role` (UserForm.xml:163, `path="/modules/forms/forms/role"`).

**Counts:**
- 156 records and 153 classes are unchanged (the four phantoms became four real classes).
- Fields go from 585 to 586.
- The data dictionary goes from 242 elements in 49 logical models to 247 in 51 (Dependent and NextOfKin are added). Elements with wiki evidence go from 156 to 160.
