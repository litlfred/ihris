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


def mount_prefixes():
    """Repository-relative prefixes ('cat-harness/', ...) a scan of THIS folio's files must skip."""
    return tuple(p.rstrip("/") + "/" for p in mounts().values())


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
