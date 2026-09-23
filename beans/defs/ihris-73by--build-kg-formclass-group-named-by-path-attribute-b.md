---
# ihris-73by
title: 'build_kg: formClass group named by path attribute becomes a phantom class'
status: todo
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
