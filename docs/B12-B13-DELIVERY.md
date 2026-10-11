# B12–B13 — assembly and delivery review (2026-10-10)

**Master:** [`outputs/kitchen_remodel_60s.mp4`](../outputs/kitchen_remodel_60s.mp4) · built by `tools/assemble_film.py` (local, 0 credits).

## Verified technical spec

| Requirement | Measured |
|---|---|
| 1920×1080, 24 fps | 1920×1080, 24/1 |
| exactly 1440 frames / 60.000 s | 1440 frames counted (`ffprobe -count_frames`), 60.000000 s |
| H.264 / AAC | h264 + aac 48 kHz stereo |
| 13 named shot exports | `outputs/shots/shot-01…13-*.mp4`, durations 5/5/5/5/5/6/4/4/5/5/6/2/3 s = 60 |
| Construction sound only; no narration, music, captions or overlays | Procedural construction foley + room tone only; no text overlays |
| Loudness | −19.2 LUFS integrated, −1.2 dBFS peak (loudnorm target −18 / TP −1.5) |

Edit: 30 atomic takes cut on frame boundaries `round(edit_time × 24)` from `construction-state-plan.json`; 1912-px Kling clips scaled/cropped to 1920×1080. Trims: 05B source frames 30–72 slowed ×0.7; 11B frames 0–12 slowed ×0.625; others are straight trims (offsets in `TAKES`). 01A/12A/13A are slow push-ins on photographs.

## Sound (option A, user-chosen)

No sound library on this Mac and downloads were not authorized, so all sound is synthesized locally (numpy/scipy): thuds, clanks, clicks, scrapes, appliance rumble, drill, brad nailer, trowel swish, footsteps, switch clicks, light hum, room tone — each placed on the action in its cut (event list in the script). License-clean. Limit: synthetic timbre; sparse by design; a pro foley pass would sound richer.

## Visual review (lead)

Per-second contact sheet and a frame-pair at all 29 cuts inspected. Cumulative state is coherent across joins: old fridge until 07, sink/microwave by 04, cooking equipment by 06, lights commissioned in 08 (MASTER), north station and nook in 09, oak/stools/toaster/kettle/rug/vase in 10–11, reveals 12–13.

Known limits carried from take reviews: cabinet/under-cabinet lights already lit in 04–07 and in FINAL-view shots; track light lit throughout; 05B and 11B are trims of partial takes; several small-motion takes (06C, 07B, 09B–09D); 01D lamp design differs between frames; minor compositing patches noted in T1–T4 logs. Visual approval only — not a fit/clearance certification.

## Audio removed (2026-10-10)

Stefan: "the sound that's playing is terrible; remove all audio." Master and all 13 shot exports re-muxed video-only (video stream copied, frames unchanged: 1440). `assemble_film.py` now builds silent by default (`SILENT = True`); the synthesized track is kept at `outputs/audio/` for reference only. This supersedes the brief's H.264/AAC construction-sound requirement.

**Status:** delivered silent for Stefan's review.
