#!/usr/bin/env python3
"""Mount every sub-instance's declared git source, as a remote mount without a remote index.

Owner, 2026-10-09, on iHRIS 5: "treat more like a remote mount, except there is no remote
index.config.json. rather i want litlfred/ihris to say that ihris-5 is a named subgraph
using fhir-harness". cat-harness's mount:remote cannot take iHRIS/iHRIS (it has no
`<name>.json` declaration, and remote mounts read the upstream's declaration), so the pin
lives in OUR declaration instead: core's own `source: {kind: "git", repository, ref, path}`
on the sub-instance (bean bamf). This tool lays that source down the way a mount is laid
down: at the pinned 40-character commit, verified after checkout, at `<name>-source/`,
git-ignored, never committed, and never written over a directory that is not that commit.

  python3 src/tools/mount_sources.py            # mount (or confirm) every declared source
  python3 src/tools/mount_sources.py --check    # no network: is each one on disk at its pin?
  python3 src/tools/mount_sources.py --print ihris5   # the source's IG directory, for a build

Exit 0 when every declared source is at its pin, 1 when one is missing or at another commit,
2 when a fetch failed (could not determine).
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import folio_platform  # noqa: E402

ROOT = folio_platform.ROOT
SHA = re.compile(r"^[0-9a-f]{40}$")


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def head(path):
    if not os.path.isdir(os.path.join(path, ".git")):
        return None
    r = git("rev-parse", "HEAD", cwd=path)
    return r.stdout.strip() if r.returncode == 0 else None


def mount(name, src, check):
    path = os.path.join(ROOT, folio_platform.source_mount_path(name))
    ref = src["ref"]
    if not SHA.match(ref):
        return 1, f"{name}: source.ref {ref!r} is not a 40-character commit; a mount is pinned, never a branch"
    at = head(path)
    if at == ref and not check and git("remote", "get-url", "origin", cwd=path).returncode != 0:
        url = src["repository"] if "://" in src["repository"] else f"https://github.com/{src['repository']}"
        git("remote", "add", "origin", url, cwd=path)
    if at == ref:
        status = git("status", "--porcelain", cwd=path).stdout.strip()
        return (0, f"current  {name}  {src['repository']}@{ref[:12]}") if not status else \
            (1, f"{name}: {path} is at the pin but has local changes; left as it is")
    if check:
        return 1, f"missing  {name}  {src['repository']}@{ref[:12]} (not on disk" + (f", at {at[:12]})" if at else ")")
    if os.path.exists(path) and at is None and os.listdir(path):
        return 1, f"{name}: {path} holds something that is not a checkout; refusing to write over it"
    os.makedirs(path, exist_ok=True)
    if at is None:
        git("init", "-q", cwd=path)
    url = src["repository"] if "://" in src["repository"] else f"https://github.com/{src['repository']}"
    # `origin` is the provenance a consumer reads (fhir-harness's ingest-ig-menu refuses a menu without it).
    if git("remote", "set-url", "origin", url, cwd=path).returncode != 0:
        git("remote", "add", "origin", url, cwd=path)
    r = git("fetch", "-q", "--depth", "1", "origin", ref, cwd=path)
    if r.returncode != 0:
        return 2, f"{name}: fetch of {url}@{ref[:12]} failed: {r.stderr.strip()[-300:]}"
    git("checkout", "-q", "--detach", "FETCH_HEAD", cwd=path)
    if head(path) != ref:
        return 1, f"{name}: checked out {head(path)}, not the pin {ref}"
    return 0, f"mounted  {name}  {src['repository']}@{ref[:12]} -> {os.path.relpath(path, ROOT)}"


def main():
    args = sys.argv[1:]
    sources = folio_platform.declared_sources()
    if "--print" in args:
        name = args[args.index("--print") + 1]
        src = sources[name]
        print(os.path.join(ROOT, folio_platform.source_mount_path(name), src.get("path") or ""))
        return 0
    worst = 0
    for name, src in sorted(sources.items()):
        code, line = mount(name, src, "--check" in args)
        print(line)
        worst = max(worst, code)
    if not sources:
        print("no sub-instance declares a git source")
    return worst


if __name__ == "__main__":
    sys.exit(main())
