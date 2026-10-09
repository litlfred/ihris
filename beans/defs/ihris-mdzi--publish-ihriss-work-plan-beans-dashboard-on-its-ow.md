---
# ihris-mdzi
title: Publish ihris's work-plan (beans) dashboard on its own site, then restore the beans navbar icon
status: todo
type: task
tags:
    - site
created_at: 2026-10-09T11:53:31Z
updated_at: 2026-10-09T11:53:31Z
---

Owner, 2026-10-09: 'missing icons on navbar top'. The folio rail's icon row inherited cat-harness's todos, beans and fsh-guts icons, which link to state-graph dashboards. ihris's site (built by src/tools/build_site.py into _site, not a Jekyll docs directory) publishes none of them, so each was inert with 'reason not recorded'. ihris.json now declares navbarIcons [close, launcher].

To bring 'beans' back as a working icon: publish a dashboard of beans/defs on the ihris site (the platform's state-visualizer renders one for a Jekyll site dir; ihris's generator would need its own, or a mount of the platform's), declare the beans graph with a visualiser the harness data can resolve, and add 'beans' to navbarIcons. 'processes' could follow the same way (processes/*.bpmn already exist).
