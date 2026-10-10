#!/usr/bin/env python3
"""Apply a sub-instance's declared IG build patches to a WORKSPACE copy of its source.

  python3 src/tools/apply_ig_patches.py <patches.json> <ig-workspace-dir> [--as <repository path of the workspace>]

A patch either replaces one exact text, exactly once, or copies one file of the same pinned source into the
workspace (`copyFrom`). A patch's paths are relative to the declared source path (ig/, the default `--as`) unless its
`base` is `repository`. Only the patches whose file lies in this workspace are applied, so one list serves every IG
of the repository. A replacement whose text is absent, or present more than once, is an error, and so is a copy onto
a file that exists: the build stops rather than building something nobody reviewed.
Never point this at a mount (<name>-source/): the mounted source is the upstream's bytes.

map_ihris5.py calls `apply()` with the workspace's own map from workspace file to repository file, because its
workspaces resolve the backend IGs' `core` symlink into a copy.
"""
import json
import os
import shutil
import sys

SOURCE_PATH = "ig"  # the iHRIS 5 sub-instance's declared source path (src/ihris5/ihris5.json `source.path`)


def repo_path(p, source_path=SOURCE_PATH):
    """A patch's `file` (or `copyFrom`) as a path from the repository root."""
    return lambda key: p[key] if p.get("base") == "repository" else f"{source_path}/{p[key]}"


def apply(spec, workspace, ws_of_repo, source_root=None, log=print):
    """Apply every patch whose target is in this workspace. `ws_of_repo` maps a repository-relative path (file or
    directory) to its path in the workspace. `source_root` is the mounted source, for `copyFrom`. Returns the ids of
    the patches applied."""
    applied = []
    for p in spec["patches"]:
        at = repo_path(p)
        target = at("file")
        if "copyFrom" in p:
            parent = ws_of_repo.get(os.path.dirname(target))
            if parent is None:
                continue
            dest = os.path.join(parent, os.path.basename(target))
            if os.path.exists(dest):
                sys.exit(f"{target}: copyFrom would overwrite a file of the source (upstream changed? re-check the patch)")
            if source_root is None:
                sys.exit(f"{target}: copyFrom needs the mounted source")
            shutil.copyfile(os.path.join(source_root, at("copyFrom")), dest)
            log(f"added {target} from {at('copyFrom')}: {p['reason'][:90]}...")
        else:
            path = ws_of_repo.get(target)
            if path is None:
                continue
            text = open(path, encoding="utf-8").read()
            n = text.count(p["find"])
            if n != 1:
                sys.exit(f"{target}: the patch text occurs {n} times, not once (upstream changed? see the patch list)")
            open(path, "w", encoding="utf-8").write(text.replace(p["find"], p["replace"]))
            log(f"patched {target}: {p['reason'][:90]}...")
        applied.append(p["id"])
    return applied


def walk_map(workspace, as_path):
    """Workspace paths keyed by repository path, for a workspace that is a plain copy of `as_path`."""
    m = {as_path: workspace}
    for d, dirs, files in os.walk(workspace):
        rel = os.path.relpath(d, workspace)
        base = as_path if rel == "." else f"{as_path}/{rel}"
        m[base] = d
        for f in files:
            m[f"{base}/{f}"] = os.path.join(d, f)
    return m


def main():
    a = sys.argv[1:]
    as_path = SOURCE_PATH
    if "--as" in a:
        i = a.index("--as")
        as_path = a[i + 1]
        del a[i:i + 2]
    patches_file, ig = a[0], a[1]
    if os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(ig)))).endswith("-source"):
        sys.exit(f"{ig}: refusing to patch a mounted source; copy it to a workspace first")
    spec = json.load(open(patches_file, encoding="utf-8"))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import folio_platform
    apply(spec, ig, walk_map(ig, as_path), source_root=os.path.join(folio_platform.ROOT, folio_platform.source_mount_path("ihris5")))


if __name__ == "__main__":
    main()
