# Audio livestream prototype

A clickable design prototype for live station radio on PBS.org (home page, Live TV) and on station sites (Bento), with a persistent bottom player. Built as one HTML file so it can be hosted anywhere.

The Figma counterpart is the Audiostream-Test file; components and copy in both are kept in sync.

## View it

Open `index.html` in a browser, or the GitHub Pages site for this repo. Add `?archive` to the URL to see options retired in earlier rounds; see CHANGELOG.md. Use the toolbar to switch pages and desktop/mobile, and **Options & notes** to compare design options and try scenarios (offline streams, long names, missing schedules).

## Update it

1. Edit `src/prototype.html` (markup, styles and behavior are all in this file).
2. Rebuild: `python3 src/build.py` (writes `index.html`).
3. Commit and push. GitHub Pages redeploys in a minute or two.

## What's in `src/`

- `prototype.html`: the source, with `{{img:…}}`, `{{svg:…}}` and `{{json:lab}}` placeholders.
- `assets/`: logos and listing images, `svg/`: the PBS logotype.
- `lab.json`: station logos and radio feeds for the Logo lab (snapshot from Station Services and radio.lls.pbs.org, Nov 18, 2026).
- `build.py`: inlines all of the above into `index.html`.

## Data

TV listings and radio schedules are a snapshot from Wed Nov 18, 2026, 4:05 PM ET; the clock in the prototype is frozen at that time. Only WXXI News and the two WTJX streams are real streams; other WXXI streams are samples, and WTJX TV listings are samples. Type is PBS Sans, loaded from pbs.org’s font server; Figtree is the fallback if it can’t load.
