# Vero kitchen-remodel video

**PAUSED by the user — 2026-10-09.** No generation or automatic continuation.
The requested 60-second video has not been produced.

## Start here

- **[HANDOFF.md](HANDOFF.md)** — current status, design preferences, exact resume boundary and next steps.
- **[Searchable stills gallery](outputs/stills-gallery.html)** — 54 stills with previews, semantic names, statuses and original-file links; three video tests separately listed.
- **[Asset catalog](docs/ASSET-CATALOG.md)** / [JSON](docs/asset-catalog.json) — stable IDs, exact paths, hashes, reviews and generation receipts.
- **[Source register](docs/SOURCE-REGISTER.md)** — blueprints, floor plans, dimension schedules, specifications, photos and provenance.
- **[Detailed backlog](docs/BACKLOG.md)** — ordered gates, dependencies, acceptance evidence, optional work and rejected designs.
- **[Lessons](docs/LESSONS.md)** — succinct findings to preserve across handoffs.
- **[Current design brief](mega-prompt.md)** / [editable shotlist](outputs/shotlist.html) — design and timeline intent; neither authorizes execution while paused.

## Current direction

Latest user reference is **REF-K**, an integrated recessed coffee/wine composition with
lit glass storage and a small preparation alcove, adapted to our style with a smaller
espresso unit. Coffee and wine share the blank end wall beside the main fridge;
fronts are wall-flush. Spice/tech stays on the other sink-side wall near the microwave.
The dishwasher counter remains clear. Main fridge now requires **French upper doors
meeting centrally and a lower freezer drawer**; the real model and fit are unresolved.

Retain Wolf gas range/red knobs and pale hood, red SMEG toaster/kettle, white Shaker and
frosted inserts, warm lighting, refined L-faucet/single sink, built-in sink-side microwave,
concrete floor/dining rug, oak bar, three cream stools, flowers and fruit.

No current generated three-view set fully represents REF-K + French doors. Old single-door
fridge frames, plain hatch concepts and rejected towers are cataloged as historical or
partial—not final approved designs. The next concept request is prepared but **not submitted**.

## Budget and pause

Recorded task quotes: **198.25 / 200 credits**, **1.75 remaining**. The proposed
**205-credit cap is NOT approved**. No top-ups or new paid jobs are authorized.
[Budget ledger](outputs/production/budget.json) and [paused state](outputs/production/state.json)
are authoritative; account-wide wallet changes are not task spend.

The paid runner refuses to quote or submit while paused. Explicit resume plus sufficient
approved budget is required before clearing that guard.

## Source geometry

Original source project: `/Users/stefansassoon/projects/vero/deco`.
The film repo holds portable copies of all four architectural SVGs, relevant dimensions,
original specifications, calibration plan and room photos. Their source paths and hashes
are in the [source register](docs/SOURCE-REGISTER.md) and [copy manifest](references/source-manifest.json).
Manufacturer PDFs have a separate [capture manifest](references/products/specs/capture-manifest.json).
Original-source estimates are not surveyed measurements; generated images establish no
real wall cavity or appliance clearance. Rejected proposed drawings are not source plans.

## Safe documentation maintenance

```bash
python3 tools/build_asset_catalog.py
python3 tools/verify_handoff.py
```

These operate on existing local files. Do not use the paid runner or historical
end-wall-layout builder as documentation commands.
