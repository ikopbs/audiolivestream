# Changelog

Each round is tagged as a GitHub release (R1, R2, …). Options cut in a round are not deleted: add `?archive` to the URL (for example `index.html?archive#home`) to see them again in the notes panel, marked “Retired in R2”.

## R2 (in progress, branch `r2`)

From the Nov 19 R1 review with Mary (notes and annotated UI fixes on the Figma Read me page).

**Decided (alternatives retired):** radio tiles in the home Live TV row; “Live” header menu; video pauses the radio; bottom player layout A; titles scroll once; Blue-Gray expanded player; short stream label; one shade per stream; equal-area logo sizing; trimmed logos; white → co-branded → call letters; coral accent; player area becomes the radio.

**Narrowed:**
- Tile and player imagery: branded field (recommended) and station scenery (for demonstration). Album art retired.
- Animation: all four kept; ambient color drift now recommended; its note removed.
- Where radio sits on /livestream: grid rows (recommended) and a new option B, a row of tiles per stream with what’s on now and the next programs. The separate radio section is retired.
- Station theme: PBS light (recommended) and PBS dark for launch. Station brand retired. In PBS light, the expanded player and the stream-list popups use Fog.
- Station site widget: all four options kept.

**New:**
- Radio badge without “RADIO”: A headphones + LIVE, B red dot + LIVE + headphones (recommended). R1’s LIVE RADIO is retired.
- Logo lab: WETA Classical (sample) with a custom stream logo uploaded by the station; filter “Custom stream logo”.
- Scenarios: a short how-to line for each one.

**Fixes:**
- Small (mobile) radio tiles: when playing, the Now Playing badge replaces the subtitle so nothing is cut off.
- Expanded player: more room around the collapse arrow (16px; 20px on phones).
- PBS light expanded player: the current program row was invisible (white on white).
- “More from … radio”: streams without a schedule show their frequency instead of repeating the name.

## R1 (Nov 19, 2026)

Version shared with Mary. Release R1, commit `87bf611`.
