---
# ihris-qw6w
title: 'Enable GitHub Pages from the gh-pages branch for litlfred/ihris'
status: todo
type: task
tags:
    - needs-owner
created_at: 2026-09-23T12:15:52Z
updated_at: 2026-09-23T12:15:52Z
---

The `gh-pages` branch was first pushed on 2026-09-23 (the owner: "make gh-pages"). `.github/workflows/pages.yml` keeps it updated. Serving it needs **Settings → Pages → Source: Deploy from a branch → `gh-pages` / (root)** on litlfred/ihris, unless GitHub enabled that automatically when the branch was pushed. Only the owner can set it. The workflow cannot be verified from a cloud session, because litlfred.github.io is egress-blocked.
