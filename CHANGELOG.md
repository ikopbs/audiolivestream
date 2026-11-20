# Changelog

Each round is tagged as a GitHub release (R1, R2, …). Options cut in a round are not deleted: add `?archive` to the URL (for example `index.html?archive#home`) to see them again in the notes panel, marked “Retired in R2”.

## R5 (in progress, branch `r5`)

From the R3 UI fixes notes (Figma Read me › UI Fixes R3):
- /livestream: a stream without a schedule gets one cell across the whole row, with no progress shading.
- Volume: mute state (speaker with an x) on every volume control; it also shows when the slider is dragged to zero.
- Bottom player: the expand control is a labeled pill, “Details” / “Hide details”, like the PBS video player.
- Expanded player: the whole day’s schedule in a scrolling list, opened at the current program; earlier programs are dimmed. WXXI News now uses its real full-day schedule from radio.lls.pbs.org (Nov 18, NPR Cadence; short inserts left out).
- Long titles: the bold title scrolls; the stream name stays put with an ellipsis.

## R4 (Nov 20, 2026)

- Tile and player imagery: decided A, the branded field. Station scenery photo retired (still under `?archive`).

## R3 (Nov 20, 2026)

- Notes panel: open choices stay at the top with letters and badges. Decided items move to a collapsed “Design decisions” section as plain notes (what the design does, why, and when it was decided), with no letters, badges or buttons. Retired options stay behind `?archive`. (Mary and Iko, Nov 20.)

From the R2 UI fixes notes (Figma Read me › UI Fixes R2):
- Player area: removed the “Watch WXXI TV instead” button.
- Badges: red dot + LIVE for TV, headphones + LIVE for radio. The dot + LIVE + headphones version is retired.
- No “Stopped” status: a stopped stream shows its program and time range, as when idle (player area, bottom player, station bar, side panel).
- Phones: the page no longer gets wider than the screen (the prototype toolbar was pushing it out), so the bottom player’s close button and the header are no longer cut off.
- Phones: schedule cells follow pbs.org/livestream below 768px: title (up to 3 lines) and the live bug only, no duration or play button, channel column clamp(90px, 30vw + 1rem, 200px). Fixes the squished cells and cut-off play icons.

## R2 (Nov 20, 2026)

From the Nov 19 R1 review with Mary (notes and annotated UI fixes on the Figma Read me page).

**Decided (alternatives retired):** radio tiles in the home Live TV row; “Live” header menu; video pauses the radio; bottom player layout A; titles scroll once; Blue-Gray expanded player; short stream label; one shade per stream; equal-area logo sizing; trimmed logos; white → co-branded → call letters; coral accent; player area becomes the radio.

**Narrowed:**
- Tile and player imagery: branded field (recommended) and station scenery (for demonstration). Album art retired.
- Animation: all four kept; ambient color drift now recommended; its note removed.
- Where radio sits on /livestream: decided B, grid rows where each program gets its own cell (now + next three, with start times) so upcoming shows are always visible. A (programs on the timeline) and the separate radio section are retired.
- Station theme: PBS light (recommended) and PBS dark for launch. Station brand retired. In PBS light, the expanded player and the stream-list popups use Fog.
- Station site widget: all four options kept.

**New:**
- Radio badge without “RADIO”: A headphones + LIVE, B red dot + LIVE + headphones (recommended). R1’s LIVE RADIO is retired.
- Logo lab: WETA Classical (sample) with a custom stream logo uploaded by the station; filter “Custom stream logo”.
- Scenarios: a short how-to line for each one.

**Fixes:**
- Phones: the page now renders at the phone’s width (it was missing the viewport tag, so mobile Safari showed a zoomed-out desktop layout).
- Small (mobile) radio tiles: when playing, the Now Playing badge replaces the subtitle so nothing is cut off.
- Expanded player: more room around the collapse arrow (16px; 20px on phones).
- PBS light expanded player: the current program row was invisible (white on white).
- “More from … radio”: streams without a schedule show their frequency instead of repeating the name.

## R1 (Nov 19, 2026)

Version shared with Mary. Release R1, commit `87bf611`.
