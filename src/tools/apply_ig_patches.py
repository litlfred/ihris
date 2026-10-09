#!/usr/bin/env python3
"""Apply a sub-instance's declared IG build patches to a WORKSPACE copy of its source.

  python3 src/tools/apply_ig_patches.py <patches.json> <ig-workspace-dir>

Each patch replaces one exact text, exactly once. A patch whose text is absent, or present
more than once, is an error: the build stops rather than building something nobody reviewed.
Never point this at a mount (<name>-source/): the mounted source is the upstream's bytes.
"""
import json
import os
import sys


def main():
    patches_file, ig = sys.argv[1], sys.argv[2]
    if os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(ig)))).endswith("-source"):
        sys.exit(f"{ig}: refusing to patch a mounted source; copy it to a workspace first")
    spec = json.load(open(patches_file, encoding="utf-8"))
    for p in spec["patches"]:
        path = os.path.join(ig, p["file"])
        text = open(path, encoding="utf-8").read()
        n = text.count(p["find"])
        if n != 1:
            sys.exit(f"{p['file']}: the patch text occurs {n} times, not once (upstream changed? see {patches_file})")
        open(path, "w", encoding="utf-8").write(text.replace(p["find"], p["replace"]))
        print(f"patched {p['file']}: {p['reason'][:100]}...")


if __name__ == "__main__":
    main()
