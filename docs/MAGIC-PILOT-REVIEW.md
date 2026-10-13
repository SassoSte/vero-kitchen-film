# Magic-transformation pilot — review (2026-10-11)

Direction (Stefan): drop the workers; rapid "magical" transformation like the reference reel (@Interiorarchdes, 15 s, downloaded locally for study only — not used in any output); Matrix-like morphology; 30 s 16:9 film. Allowance: [magic-pilot-authorization](../outputs/production/magic-pilot-authorization.json) (25 credits, 2 jobs).

Reference read (2 fps contact sheet): empty room, slow steady camera drift, elements materialize one at a time with golden dust/sparkles; translucent-to-solid builds; warm light; no people.

## v1 — `magic-pilot-v1` (12.5 credits) → `outputs/magic/magic-pilot-v1.mp4`
Kling O3 frames pro, 10 s, start `stage-02-bare` → end selected view 1, one mega-prompt.
- Good (5–10 s): ordered assembly; glowing light-lines trace the fridge; uppers, hood, range, niche, toaster/kettle materialize cleanly; locked camera; ends on the selected view.
- **Defects (2–4.5 s):** "floor polish wave" renders as a grey smear across the floor; base cabinets appear as crude stepped white blocks before resolving.
- Finding → v2: remove the floor wave; every element first draws as a thin glowing golden wireframe, then fills solid (what worked in v1).

## v2 — `magic-pilot-v2` (12.5 credits) → `outputs/magic/magic-pilot-v2.mp4`
- **Fail:** "golden dust" rendered as a large orange fireball/smoke cloud over the fridge and cabinets for ~1–6 s (reads as fire). Wireframe outlines visible under the smoke 2.5–5 s; final 6–10 s clean.
- Allowance exhausted (2 jobs, 25 credits).

## Local wireframe build (0 credits) → `outputs/magic/local-wireframe-master-v1.mp4`
`tools/magic_wireframe.py`, 12 s, 13 same-camera MASTER plates (bare → final). Each step: edges of the newly added elements draw in as glowing golden lines, then fill bottom-up behind a bright scan line with sparkles; slow 4% camera push. Deterministic — no smoke, no warping; inherits the plates' known compositing patches. Lead view: strongest of the three for control; v1's 5–10 s is the strongest *physical* motion.

## Mixed 30 s film (0 credits) → `outputs/kitchen_magic_30s.mp4`
Stefan liked v2's burn and the local wireframe; built `tools/magic_film.py`:
0–1.5 s before photo (cropped original) · 1 s golden-line dissolve to bare room · 2.3 s v2 fridge burn (frames 0–54) · 1 s clear · 10 s view-1 wireframe build (fridge-free plates: old fridge replaced by v1 frame-34 corner, tone-matched) · 1 s golden transition · 5 s view-2 build (sink, faucet, microwave, phone) · 1 s transition · 6 s view-3 build (fridge, oak, stools, styling) · hold on selected view 3. 720 frames, 1920×1080, 24 fps, silent, no people.
Limits: faint lighter patch where the old fridge was removed in the early view-1 plates; inherited plate patches; transitions between views are dissolves (camera positions differ).

## Revision — old cabinets and range burn (0 credits)
Stefan: "burn the old cabinets and range too, then commit". `tools/burn_old.py`: fire lifted from pilot v2 (frames 18–60, alpha keyed on orange) placed over the original photo's upper cabinets, microwave, range, base cabinets and counters; objects char under the fire; the bare room dissolves in under peak fire, then v2's fridge burn follows. New timing: 1.0 s before · 3.0 s cabinet/range burn · 2.3 s fridge burn · 1 s clear · 8.5 s view-1 build · 1 s · 5 s view-2 · 1 s · 6 s view-3 · hold. 720 frames verified.
Limits: fire sprites repeat (same source clip, flipped/scaled); flame shapes are column-like.

## Blueprint cut (current, 0 credits) → `outputs/kitchen_blueprint_30s.mp4`
Stefan: fire doesn't work; old kitchen → blueprint drawn over it → transformation. `tools/blueprint_film.py`: 0–1.5 s old kitchen · navy blueprint sheet and grid fade over it while white line drawing of the finished kitchen sweeps in · blueprint fills to the bare room behind a scan line (7.5 s) · white-line wireframe build of view 1 (9.5 s) · blueprint transition · view 2 build (4.5 s) · blueprint transition · view 3 build (5 s) · hold. 720 frames, 1920×1080, silent, no people, no fire.

## Rebuild with revised views (2026-10-12, 0 credits)
User: "Yes, let's do it." `tools/blueprint_film.py` now ends each build on the 2026-10-12 selected views (v3 / v2 / v12) and carries the finish revisions into every intermediate plate: pixels matching the previous selected view take the revised view's pixels; remaining bare-wall plaster is smoothed with the same guided filter. Living-room build uses the closer v12 framing. Blueprint line drawing traced from v3. Previous cut kept as `outputs/magic/kitchen_blueprint_30s-2026-10-11.mp4`. 720 frames verified.
Limit: the new backsplashes are present from the first plate in which their counter exists, so they don't "build" separately.
