# Design intent: a dark scheme for the iHRIS site (bean ihris-u3fg)

**Who:** a reader of the iHRIS Knowledge Base (implementer, analyst, data manager) whose OS is set to dark, or who presses the folio chrome's light/dark switch. They may be on a laptop or a phone.

**What they need:** the same pages, readable on a dark ground, without a flash of light when they have picked dark, and still recognisably iHRIS.

**What it must show:** real pages: the class page `iHRIS_Position` (header, navbar, side catalogue, field table, neighbourhood graph and its edge table) and the home page (the harness board).

**Constraints:**
- The 4.3.3 release has no dark stylesheet, so a dark palette cannot be measured. What a person decides is kept small (`ihris-site-theme-dark-grounds/v1`): how dark the page, panel, raised surface and rule are, each as a lightness on the hue of a measured colour, the targets, and how the logo is shown. Every other colour is derived by one rule (`src/tools/derive_dark_theme.py`): same hue and saturation as the light role, the lowest lightness at or above it that reaches the target on the panel and the raised ground. No colour is invented.
- WCAG 2: body text 7:1, other text 4.5:1, control borders 3:1.
- The switch and the OS both decide: cat-harness's `darkRules` and `withSavedScheme` (`src/tools/scheme_css.ts`).
- The iHRIS logo is a black mark on a transparent ground (every opaque pixel is `#000000`), so it disappears on dark. The PNG is never altered.

**Both layouts:** web (1280 wide) and mobile (390 wide) for every candidate.

**A colour design, so not monochrome:** WireGen's mid-fidelity rule asks for monochrome candidates. Here colour IS the design, so the candidates are the real pages with each palette applied (`derive_dark_theme.py --page`).

## Candidates

- **A: Manage blue at night** (`a.grounds.json`): every ground on the hue of Manage's page blue `#467495`; the logo inverted to white.
- **B: Neutral charcoal** (`b.grounds.json`): a grey panel, Manage's blue kept only at the page edges; the logo on a white disc.

The navbar keeps its light colours in both: white on Manage's green already passes AA, and the green is the iHRIS mark.
