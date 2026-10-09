#!/usr/bin/env python3
"""Derive the iHRIS site's DARK scheme from the measured light theme and a chosen set of grounds.

  python3 src/tools/derive_dark_theme.py                       # write src/site/theme/ihris-classic-dark.json
  python3 src/tools/derive_dark_theme.py --check               # fail if it is stale
  python3 src/tools/derive_dark_theme.py --grounds <g.json> --out <theme.json>   # a candidate's theme
  python3 src/tools/derive_dark_theme.py --grounds <g.json> --page <built.html> --css <ihris.css> --to <out.html>
                                                               # a candidate page, standalone, forced dark

The 4.3.3 release has no dark stylesheet, so a dark palette cannot be MEASURED. What a person
decides is small and written down (`ihris-site-theme-dark-grounds/v1`, the owner's choice after
wireframe-design-review): the grounds, i.e. how dark the page, the panel, a raised surface and a rule
are, each as a lightness on the hue of a MEASURED colour. Everything else is derived here, by one rule:

  every foreground keeps the hue and saturation of the colour the light theme applies for that role,
  and takes the LOWEST lightness at or above its own that reaches its WCAG target on every ground it
  sits on (the panel and the raised surface).

So a heading stays Manage's green or blue, only lighter, and no colour is invented. The navbar keeps
its light values: white on Manage's green already passes AA, and the green is the iHRIS mark.
"""
import colorsys
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
THEME = os.path.join(ROOT, "src", "site", "theme")
LIGHT = os.path.join(THEME, "ihris-classic.json")
CHOICE = os.path.join(THEME, "ihris-classic-dark.grounds.json")
OUT = os.path.join(THEME, "ihris-classic-dark.json")
# The iHRIS logo for a dark ground: the owner's choice of logo treatment applied to the file, for surfaces
# that are dark in BOTH schemes and that this folio's CSS cannot reach, such as the folio chrome's rail,
# whose avatar is this file (ihris.json `images`, `icon: "mark"`). Under the instance's site directory
# (`docs/`), as cat-harness resolves a declared mark's published path.
MARK = os.path.join(ROOT, "docs", "assets", "img", "iHRIS_logo-on-dark.svg")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_theme import _hex, _lum, contrast  # noqa: E402  the same WCAG arithmetic as the light theme


def exact(a, b):
    """The contrast ratio unrounded: `contrast` rounds to 2 places, so 4.498 would read as 4.5 and pass."""
    la, lb = sorted((_lum(_hex(a)), _lum(_hex(b))), reverse=True)
    return (la + 0.05) / (lb + 0.05)

# The site's own constants that are not in the measured theme (build_site.css() used them as literals).
# Their light values are unchanged; listed once here so the dark derivation and the light sheet agree.
SITE_LIGHT = {
    "mute": "#5c5c5c",          # secondary text: crumbs, captions, counts
    "sideBackground": "#fafaf6",  # the catalogue's side panel
    "control": "#767676",       # input and button borders
    "diagramBackground": "#ffffff",
    "diagramBase": "#f2f2f2",   # a base class's box in the neighbourhood graph
    "diagramInk": "#1b1b1b",
}

# Foreground roles: (token, where its light value comes from, target key).
FOREGROUNDS = [
    ("text", "applied.text", "text"),
    ("sideNavText", "applied.sideNavText", "text"),
    ("diagramInk", "site.diagramInk", "text"),  # also sits on a base class's box (the rule ground)
    ("h1", "applied.h1", "default"), ("h2", "applied.h2", "default"),
    ("h3", "applied.h3", "default"), ("h4", "applied.h4", "default"),
    ("siteName", "applied.siteName", "default"),
    ("link", "applied.link", "default"), ("linkHover", "applied.linkHover", "default"),
    ("sideNavActive", "applied.sideNavActive", "default"),
    ("mute", "site.mute", "default"),
    ("control", "site.control", "nonText"),
]
# The iHRIS logo is a black mark on a transparent ground (measured: every opaque pixel is #000000), so it
# disappears on a dark panel. The grounds file says how it is shown; the PNG itself is never altered.
LOGO = {
    "invert": "header.site img { filter:invert(1); }\n",  # the same mark, white: its shape is unchanged
    "tile": "header.site img { background:#ffffff; border-radius:50%; padding:3px; }\n",  # the black mark on a white disc
}
KEEP = ("navBar", "navBarText", "navBarHover", "navBarAccent", "font", "brandFont")


def hls(c):
    c = _hex(c)
    return colorsys.rgb_to_hls(*(int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)))


def to_hex(h, l, s):
    return "#" + "".join(f"{round(v * 255):02x}" for v in colorsys.hls_to_rgb(h, max(0.0, min(1.0, l)), s))


def ground(spec, light):
    h, _, s = hls(light["measured"][spec["hueOf"]]["value"])
    return to_hex(h, spec["lightness"], s if spec.get("saturation") is None else spec["saturation"])


def lift(c, grounds, target):
    """The lowest lightness >= c's own, same hue and saturation, that reaches `target` on every ground."""
    h, l, s = hls(c)
    for step in range(0, 1001):
        cand = to_hex(h, l + step / 1000, s)
        if all(exact(cand, g) >= target for g in grounds):
            return cand
    raise SystemExit(f"derive_dark_theme: no lightness of {c} reaches {target}:1 on {grounds}")


def derive(choice, light):
    g = {k: ground(v, light) for k, v in choice["grounds"].items()}
    # The grounds each foreground sits on: the panel and the raised surface, and for the diagram's ink also
    # the base-class box, which is drawn in the rule ground.
    sits = lambda role: ["panel", "raised"] + (["rule"] if role == "diagramInk" else [])  # noqa: E731
    src = {"applied": light["applied"], "site": SITE_LIGHT}
    applied, derivations = {}, []
    for role, frm, tkey in FOREGROUNDS:
        base, key = frm.split(".")
        lc = src[base][key]
        target = choice["targets"][tkey]
        v = lift(lc, [g[k] for k in sits(role)], target)
        applied[role] = v
        derivations.append({"role": role, "light": lc, "applied": v, "target": target,
                            "contrast": {k: contrast(v, g[k]) for k in sits(role)}})
    for k in KEEP:
        applied[k] = light["applied"][k]
    applied.update({
        "pageBackground": g["page"], "contentBackground": g["panel"], "sideBackground": g["raised"],
        "subNavActiveBackground": g["raised"], "sideNavRule": g["rule"], "navBarBorder": g["rule"],
        "diagramBackground": g["raised"], "diagramBase": g["rule"], "siteTag": applied["mute"],
    })
    return {
        "$schema": "ihris-site-theme-dark/v1",
        "id": f"{light['id']}-dark",
        "title": f"{light['title']}, dark",
        "derivedFrom": {"theme": os.path.relpath(LIGHT, ROOT), "grounds": choice["id"],
                        "rule": "same hue and saturation as the light role; the lowest lightness at or above it that "
                                "reaches the target on the panel and the raised ground"},
        "licence": light["licence"],
        "wcag": {"target": "AA", "targets": choice["targets"]},
        "grounds": g,
        "logo": choice["logo"],
        "applied": applied,
        "derivations": derivations,
    }


def flat_rules(t):
    """The dark scheme as flat CSS rules (cat-harness darkRules takes flat rules only)."""
    a = t["applied"]
    return (
        f":root {{ --page:{a['pageBackground']}; --panel:{a['contentBackground']}; --ink:{a['text']}; --h1:{a['h1']}; "
        f"--h2:{a['h2']}; --h3:{a['h3']}; --h4:{a['h4']}; --link:{a['link']}; --nav:{a['navBar']}; --nav-ink:{a['navBarText']}; "
        f"--nav-hover:{a['navBarHover']}; --nav-accent:{a['navBarAccent']}; --brand:{a['siteName']}; --rule:{a['sideNavRule']}; "
        f"--active:{a['sideNavActive']}; --active-bg:{a['subNavActiveBackground']}; --mute:{a['mute']}; "
        f"--side-bg:{a['sideBackground']}; --control:{a['control']}; --diagram-bg:{a['diagramBackground']}; "
        f"--diagram-base:{a['diagramBase']}; --diagram-ink:{a['diagramInk']}; color-scheme:dark; }}\n"
        + LOGO[t["logo"]]
    )


def standalone(page, css_path, t, to):
    """A built page with its sheet inlined and the dark rules applied unconditionally: a candidate to review."""
    import re
    html = open(page, encoding="utf-8").read()
    # The built sheet without its own dark block: the candidate's rules come last and decide.
    sheet = open(css_path, encoding="utf-8").read().split("\n/* dark scheme")[0]
    html = re.sub(r'<link rel="stylesheet" href="[^"]*ihris\.css">', lambda _: f"<style>{sheet}\n{flat_rules(t)}</style>", html)
    html = re.sub(r'<link rel="icon"[^>]*>', "", html)
    import base64
    logo = "data:image/png;base64," + base64.b64encode(open(os.path.join(THEME, "iHRIS_logo.png"), "rb").read()).decode()
    html = re.sub(r'(<img [^>]*src=")[^"]*iHRIS_logo\.png(")', lambda m: m.group(1) + logo + m.group(2), html)
    html = html.replace("<html", '<html data-fa-scheme="dark"', 1)
    os.makedirs(os.path.dirname(os.path.abspath(to)), exist_ok=True)
    open(to, "w", encoding="utf-8").write(html)


def mark_on_dark(logo_treatment):
    """The verified logo (src/site/theme/iHRIS_logo.png, sha256 in ihris-classic.json) wrapped unaltered in an
    SVG that draws it for a dark ground. `invert`: every opaque pixel white, alpha kept, so the mark's shape is
    exactly the logo's. `tile`: the black mark on a white disc."""
    import base64
    png = open(os.path.join(THEME, "iHRIS_logo.png"), "rb").read()
    w = h = 62  # the logo's own size, measured: 62 x 62
    data = base64.b64encode(png).decode()
    if logo_treatment == "invert":
        body = ('<filter id="w"><feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0"/></filter>'
                f'<image width="{w}" height="{h}" filter="url(#w)" href="data:image/png;base64,{data}"/>')
    else:
        body = (f'<circle cx="{w / 2}" cy="{h / 2}" r="{w / 2}" fill="#ffffff"/>'
                f'<image x="3" y="3" width="{w - 6}" height="{h - 6}" href="data:image/png;base64,{data}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            '<title>iHRIS logo, (c) IntraHealth International, from the iHRIS 4.3.3 release (GPL)</title>'
            f'{body}</svg>\n')


def main():
    a = sys.argv
    arg = lambda f, d=None: a[a.index(f) + 1] if f in a else d  # noqa: E731
    light = json.load(open(LIGHT, encoding="utf-8"))
    choice = json.load(open(arg("--grounds", CHOICE), encoding="utf-8"))
    t = derive(choice, light)
    if "--page" in a:
        standalone(arg("--page"), arg("--css"), t, arg("--to"))
        return
    text = json.dumps(t, indent=2, ensure_ascii=False) + "\n"
    out = arg("--out", OUT)
    mark = mark_on_dark(t["logo"])
    if "--check" in a:
        stale = [os.path.relpath(f, ROOT) for f, want in ((out, text), (MARK, mark))
                 if not os.path.exists(f) or open(f, encoding="utf-8").read() != want]
        print(f"dark theme: STALE {stale}" if stale else "dark theme: OK")
        sys.exit(1 if stale else 0)
    open(out, "w", encoding="utf-8").write(text)
    if out == OUT:
        os.makedirs(os.path.dirname(MARK), exist_ok=True)
        open(MARK, "w", encoding="utf-8").write(mark)
        print(f"{os.path.relpath(MARK, ROOT)}: the logo for a dark ground ({t['logo']})")
    print(f"{os.path.relpath(out, ROOT)}: grounds {t['grounds']}")
    for d in t["derivations"]:
        print(f"  {d['role']:14} {d['light']} -> {d['applied']}  {d['contrast']['panel']}:1 / {d['contrast']['raised']}:1")


if __name__ == "__main__":
    main()
