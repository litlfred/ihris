"""The ONE place ihris's tools learn where the folio-assistant platform lives.

ihris is a folio-assistant-core DEPENDENT repository, laid out as litlfred/who-iris is
(who-iris/platform.ts plays this role there; not named platform.py, which would shadow the standard library). `index.config.json` names the platform
layers as remote mounts pinned to SHAs, `index.lock.json` records what they resolved
to, and `src/tools/mount_platform.sh` lays them down at `<root>/<name>/`, git-ignored.

So the platform root is the directory holding `folio-assistant-core/`, `cat-harness/`
and the rest side by side: this repository's root by default, or $FOLIO_PLATFORM
when the layers were laid down somewhere else. Before the cutover this was a
litlfred/folio-assistant checkout ($FOLIO_ASSISTANT); that repository no longer holds
these layers in its tree, so it is not looked for.
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REQUIRED = ("folio-assistant-core", "cat-harness")


def mounts():
    """{instance name: repository-relative path} for every remote instance index.config.json declares."""
    with open(os.path.join(ROOT, "index.config.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = {}
    for i in idx["instances"]:
        remote = (i.get("source") or {}).get("remote")
        if remote:
            out[i["name"]] = ((remote.get("overrides") or {}).get(i["name"]) or {}).get("path") or i["name"]
    return out


def declared_sources():
    """{sub-instance name: its `source`} for every instance ihris.json lists whose declaration carries
    core's git source (`{kind: "git", repository, ref, path}`): a source mounted like a remote layer,
    pinned in OUR declaration because the upstream has no index of its own (src/tools/mount_sources.py)."""
    with open(os.path.join(ROOT, "ihris.json"), encoding="utf-8") as f:
        root = json.load(f)
    out = {}
    for i in root.get("instances") or []:
        with open(os.path.join(ROOT, i["path"], f"{i['name']}.json"), encoding="utf-8") as f:
            src = json.load(f).get("source")
        if isinstance(src, dict) and src.get("kind") == "git":
            out[i["name"]] = src
    return out


def source_mount_path(name):
    """Where a sub-instance's declared source is mounted: `<name>-source/` at the root, git-ignored."""
    return f"{name}-source"


def mount_prefixes():
    """Repository-relative prefixes ('cat-harness/', 'ihris5-source/', ...) a scan of THIS folio's files must skip."""
    return tuple(p.rstrip("/") + "/" for p in list(mounts().values()) + [source_mount_path(n) for n in declared_sources()])


def platform_root():
    """The directory holding the mounted layers, or None when they are not there.
    None is never a pass: a caller reports the check it could not run."""
    base = os.environ.get("FOLIO_PLATFORM") or ROOT
    paths = mounts()
    if all(os.path.isdir(os.path.join(base, paths.get(n, n))) for n in REQUIRED):
        return base
    return None


def layer(name):
    """The path of one mounted layer, e.g. layer('cat-harness'), or None when it is not mounted."""
    base = platform_root()
    return os.path.join(base, mounts().get(name, name)) if base else None
