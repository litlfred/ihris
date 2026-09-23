#!/usr/bin/env python3
"""Derive the iHRIS "Classic Manage" site theme from the verified 4.3.3 release.

Owner, 2026-09-23: the ihris harness site is themed like iHRIS ("see css in ihris
suite"): the classic Manage look, with the iHRIS logo credited under the GPL.

Nothing is transcribed by hand. This reads, from uploads/ihris-suite-4.3.3/*.tar.bz2
(MD5 matched against Launchpad, sha256 pinned in its manifest):

  ihris-common/css/globalStyles.css   the base layer
  ihris-manage/css/themeStyles.css    Manage's theme, which @imports after it and wins
  ihris-common/images/iHRIS_logo.png  the logo

and writes src/site/theme/ihris-classic.json (the tokens, each with the selector and
file it was measured from) plus src/site/theme/iHRIS_logo.png.

MEASURED vs APPLIED. Every colour is kept as measured. Where a measured colour fails
WCAG 2 AA (4.5:1) in the role the site uses it for, the applied token takes the first
OTHER colour measured from the same stylesheets that passes, and records why. No
colour is invented.

  python3 src/tools/extract_theme.py           # write
  python3 src/tools/extract_theme.py --check   # fail if the committed theme is stale
Without the tarball, --check verifies the logo against its recorded sha256 and exits 0
with a warning. That is not a full check.
"""
import hashlib
import json
import os
import re
import sys
import tarfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UP = os.path.join(ROOT, "uploads", "ihris-suite-4.3.3")
OUT = os.path.join(ROOT, "src", "site", "theme")
GLOBAL = "ihris-common/css/globalStyles.css"
THEME = "ihris-manage/css/themeStyles.css"
LOGO = "ihris-common/images/iHRIS_logo.png"


def _hex(c):
    c = c.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c


def _lum(c):
    r, g, b = (int(c[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted((_lum(_hex(a)), _lum(_hex(b))), reverse=True)
    return round((la + 0.05) / (lb + 0.05), 2)


def parse_css(text):
    """{selector: {prop: value}}; later rules override earlier ones, as in the cascade."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    rules = {}
    for sels, body in re.findall(r"([^{}]+)\{([^{}]*)\}", text):
        props = {}
        for decl in body.split(";"):
            if ":" in decl:
                k, v = decl.split(":", 1)
                props[k.strip().lower()] = v.strip()
        for s in sels.split(","):
            s = " ".join(s.split())
            if s and not s.startswith("@"):
                rules.setdefault(s, {}).update(props)
    return rules


def _font_family(v):
    # `font: 62.5% Arial, Helvetica, sans-serif` -> `Arial, Helvetica, sans-serif`
    m = re.search(r"((?:\"[^\"]+\"|[A-Za-z][\w-]*)(?:\s*,\s*(?:\"[^\"]+\"|[A-Za-z][\w-]*))+)\s*$", v)
    return m.group(1) if m else v


def build(tar_path):
    with tarfile.open(tar_path, "r:bz2") as t:
        raw = {p: t.extractfile(p).read() for p in (GLOBAL, THEME, LOGO)}
    g, th = parse_css(raw[GLOBAL].decode("latin-1")), parse_css(raw[THEME].decode("latin-1"))

    def m(file_rules, file, sel, prop, conv=_hex):
        v = file_rules[sel][prop]
        return {"value": conv(v), "from": f"{file} `{sel}` {prop}"}

    measured = {
        "pageBackground": m(th, THEME, "body", "background-color"),
        "contentBackground": m(g, GLOBAL, ".autoHideNav #siteInnerWrap", "background"),
        "text": m(g, GLOBAL, "body", "color"),
        "font": m(g, GLOBAL, "body", "font", _font_family),
        "brandFont": m(g, GLOBAL, "#siteHeader p#siteName", "font", _font_family),
        "siteName": m(th, THEME, "#siteHeader p#siteName", "color"),
        "siteTag": m(th, THEME, "#siteHeader p#siteTag", "color"),
        "h1": m(th, THEME, "h1", "color"),
        "h2": m(th, THEME, "h2", "color"),
        "h3": m(th, THEME, "h3", "color"),
        "h4": m(th, THEME, "h4", "color"),
        "link": m(th, THEME, "a", "color"),
        "linkHover": m(th, THEME, "a:hover", "color"),
        "linkVisited": m(th, THEME, "a:visited", "color"),
        "navBar": m(th, THEME, "#inlineNavBar", "background-color"),
        "navBarText": m(th, THEME, "#inlineNavBar ul li a", "color"),
        "navBarHover": m(th, THEME, "#inlineNavBar ul li a:hover", "background-color"),
        "navBarBorder": m(th, THEME, "#inlineNavBar ul li a", "border-right-color"),
        "sideNavText": m(th, THEME, "#navBar li a", "color"),
        "sideNavRule": m(th, THEME, "#navBar li a", "border-bottom-color"),
        "sideNavActive": m(th, THEME, "#navBar li a.active", "color"),
        "subNavActiveBackground": m(th, THEME, "#navBar ul ul li a.active", "background-color"),
    }
    # Every colour the two stylesheets measure, in cascade order: the candidate pool
    # for substitutes. The site never uses a colour from outside it.
    pool = []
    for rules in (g, th):
        for props in rules.values():
            for v in props.values():
                for c in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", v):
                    if _hex(c) not in pool:
                        pool.append(_hex(c))

    AA = 4.5
    applied, adjustments = {}, []

    def use(role, token, bg_token, prefer):
        bg = applied.get(bg_token) or measured[bg_token]["value"]
        v = measured[token]["value"]
        if contrast(v, bg) >= AA:
            applied[role] = v
            return
        for cand in prefer + [c for c in pool if c not in prefer]:
            if contrast(cand, bg) >= AA:
                applied[role] = cand
                adjustments.append({"role": role, "measured": v, "contrast": contrast(v, bg), "on": bg,
                                    "applied": cand, "appliedContrast": contrast(cand, bg),
                                    "reason": f"{token} {v} is {contrast(v, bg)}:1 on {bg}, below WCAG AA {AA}:1; "
                                              f"{cand} is measured from the same stylesheets"})
                return
        raise SystemExit(f"no measured colour passes AA for {role}")

    for k in ("pageBackground", "contentBackground", "text", "font", "brandFont", "siteTag", "sideNavRule",
              "subNavActiveBackground", "navBarHover", "navBarBorder"):
        applied[k] = measured[k]["value"]
    for role in ("h1", "h2", "h3", "h4", "siteName", "sideNavText"):
        use(role, role, "contentBackground", [])
    ml = [measured[k]["value"] for k in ("linkHover", "h1", "h3")]
    use("link", "link", "contentBackground", ml)
    use("linkHover", "linkHover", "contentBackground", [measured["h1"]["value"]])
    use("sideNavActive", "sideNavActive", "contentBackground", [measured["h2"]["value"]])
    # The navbar is text on a coloured bar: the bar colour is the one that must yield.
    nb, nt = measured["navBar"]["value"], measured["navBarText"]["value"]
    if contrast(nb, nt) >= AA:
        applied["navBar"] = nb
    else:
        for cand in [measured[k]["value"] for k in ("navBarBorder", "navBarHover", "h2")]:
            if contrast(cand, nt) >= AA:
                applied["navBar"] = cand
                adjustments.append({"role": "navBar", "measured": nb, "contrast": contrast(nb, nt), "on": nt,
                                    "applied": cand, "appliedContrast": contrast(cand, nt),
                                    "reason": f"white navbar text on {nb} is {contrast(nb, nt)}:1, below AA; {cand} is "
                                              "Manage's own navbar border/hover green"})
                break
    applied["navBarText"] = nt
    applied["navBarAccent"] = nb  # the measured bar green survives as the accent stripe

    sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
    theme = {
        "$schema": "ihris-site-theme/v1",
        "id": "ihris-classic",
        "title": "iHRIS Classic Manage",
        "derivedFrom": {
            "release": "ihris-suite-4.3.3",
            "tarballSha256": json.load(open(os.path.join(UP, "manifest.json")))["sha256"],
            "files": {GLOBAL: sha(raw[GLOBAL]), THEME: sha(raw[THEME])},
            "cascade": [GLOBAL, THEME],
        },
        "licence": {"id": "GPL-3.0-or-later", "basis": "iHRIS Suite (ihris-common, ihris-manage) is GPL; see i2ce/COPYING in the release",
                    "attribution": "Colours, fonts and logo from iHRIS Manage 4.3.3, (c) IntraHealth International, GPL."},
        "wcag": {"target": "AA", "ratio": AA},
        "measured": measured,
        "applied": applied,
        "adjustments": adjustments,
        "logo": {"file": "iHRIS_logo.png", "from": LOGO, "sha256": sha(raw[LOGO]),
                 "attribution": "iHRIS logo, (c) IntraHealth International, from the iHRIS 4.3.3 release (GPL)."},
    }
    return theme, raw[LOGO]


def main():
    check = "--check" in sys.argv
    tjson, tlogo = os.path.join(OUT, "ihris-classic.json"), os.path.join(OUT, "iHRIS_logo.png")
    tars = [f for f in os.listdir(UP) if f.endswith(".tar.bz2")] if os.path.isdir(UP) else []
    if not tars:
        if not check:
            raise SystemExit(f"no tarball in {UP}; upload ihris-suite-4.3.3.tar.bz2 first")
        cur = json.load(open(tjson))
        ok = hashlib.sha256(open(tlogo, "rb").read()).hexdigest() == cur["logo"]["sha256"]
        print(("WARN: tarball absent; logo sha256 verified only" if ok else "FAIL: logo sha256 mismatch"), file=sys.stderr)
        sys.exit(0 if ok else 1)
    tb = os.path.join(UP, tars[0])
    want = json.load(open(os.path.join(UP, "manifest.json")))["sha256"]
    h = hashlib.sha256()
    with open(tb, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    if h.hexdigest() != want:
        raise SystemExit(f"refusing: {tb} sha256 does not match uploads manifest")
    theme, logo = build(tb)
    text = json.dumps(theme, indent=2, ensure_ascii=False) + "\n"
    if check:
        stale = (not os.path.exists(tjson) or open(tjson).read() != text
                 or not os.path.exists(tlogo) or open(tlogo, "rb").read() != logo)
        print("theme: STALE" if stale else "theme: OK")
        sys.exit(1 if stale else 0)
    os.makedirs(OUT, exist_ok=True)
    open(tjson, "w").write(text)
    open(tlogo, "wb").write(logo)
    print(json.dumps({"applied": theme["applied"], "adjustments": [(a["role"], a["measured"], a["applied"]) for a in theme["adjustments"]]}, indent=1))


if __name__ == "__main__":
    main()
