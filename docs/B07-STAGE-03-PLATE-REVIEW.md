# B07 stage-03 plate — review log (2026-10-10)

Allowance: [b07-03a-frames-authorization](../outputs/production/b07-03a-frames-authorization.json)
(≤6 jobs, ≤39 credits, ≤2 attempts per frame; second only after a written finding).

## Attempt 1 — `stage-03-plate-v1` (6.5 credits, job 883c3c79-1e81-4dfd-8240-ae21ab5b5805)

Full-frame GPT Image 2 edit of MASTER. **Rejected as a plate.**

- Correct: old stainless top-freezer fridge with black side; framed unfinished north niche;
  empty sink cutout; no backsplash, uppers, hood, pot filler, toaster or kettle.
- Wrong state: the range opening was **filled with a new narrow base cabinet** instead of
  left empty.
- Layout drift: right cooking run re-proportioned (shorter run, cabinet widths changed);
  floor/baseboard ~22–47 px lower; NE corner moved.
- Re-composite through `plate-03` mask: 181 RANSAC inliers, protected-area mean
  difference 17.5 → 15.3 after registration (drift is non-rigid, not a camera shift);
  visible seams at NE corner/ceiling, cooktop strip, kettle ghost and floor. Not usable.

## Unpaid local rebuild — `stage-03-plate-local-v1`

`tools/build_stage03_plate.py` builds the plate on MASTER geometry: plaster walls and
ceiling quilted from MASTER's own north wall, lit by attempt 1's smooth light field;
attempt 1's old fridge pasted at its native position (already on MASTER's footprint,
handles included); niche and sink cutout warped from attempt-1 corners onto MASTER's
measured corners; kettle/plant worktop rebuilt by periodic clone along the run slope.
Remaining defect: the range is still present.

## Attempt 2 — `stage-03-plate-v2-range` (crop edit)

Only the range is regenerated, on a 1227×920 (4:3) crop around it, so the model sees
little room to re-layout; only `stage-03-range-crop-mask` pixels are re-composited.

### Attempt 2 result (6.5 credits) — not used directly

The crop return removed the range and drew a plausible empty bay (white side panel,
toe kick, baseboard, gas stub, outlet), but reframed the crop: narrow cabinet rebuilt
deeper, right run shifted ~150 px; registration 140 inliers, protected diff 16.4 → 14.8.
Direct composite doubled the cabinet. **Useful finding:** from this camera the empty bay
is dominated by the narrow cabinet's south side panel; the back wall is hidden below
worktop height. The return's side panel and worktop edge (real shading, toe kick) were
warped from their own corners onto MASTER's measured quad and regraded to MASTER white.

## Accepted plate — `outputs/construction/stage-03-plate.png` (lead inspection)

Built by `tools/build_stage03_plate.py` → `raw/stage-03-plate-local-v2.png`. 50.9% of
pixels differ from MASTER; everything else (west run, DW, floor, right base run and
worktop, ceiling, track light, camera) is MASTER.

- Shot-03 state: concrete; base cabinets with cooking-run and west worktops; no
  backsplash, uppers, hood, pot filler, range, toaster, kettle or plant; old stainless
  top-freezer fridge freestanding with bare wall; north niche framed/unfinished; sink
  cutout empty.
- Known limits: track light still lit (lights commission in 08); faint warm cast on the
  right worktop from MASTER's former under-cabinet light; narrow-cabinet side panel is
  brighter/flatter than surrounding cabinetry; minor baseboard offset left of the fridge.
- Plate attempts used: 2 of 2 (13 credits). Remaining allowance: 26 credits for 03A END/START.

## 03A END — `03A-end-v1` (6.5 credits) → `outputs/construction/03A-end.png`

Return kept the plate geometry well (1,131 inliers, protected diff 3.4). Only the workers
were transferred (`tools/person_composite.py`: registered difference mask + local U2-Net
saliency + explicit forearm region; local tone match on background inside the mask).
Lead and partner match workers-v1 wardrobe; slab seated; hands lifting off the front edge.
Limit: partner's lower body partly hidden by the lead; faint narrow-cabinet back edge
visible between hands.

## 03A START — attempts `03A-start-v1`, `03A-start-v2` (6.5 + 6.5 credits) → `outputs/construction/03A-start.png`

- v1: slab raised ~9 in, hands flat on top (unsupported). Rejected.
- v2 (used): slab lowered to a visible ~2–3 in gap over exposed plywood rims; same slab
  footprint as END. **Limit: hands still grip the top/front edge rather than from below**;
  attempts for this frame are exhausted, so this is accepted by the lead as the best
  available START, pending Stefan's review.
- Composited onto the empty plate (not onto END) to avoid ghosting of END's workers.

## Allowance closeout

5 jobs, 32.5 credits of the 39-credit allowance; all per-frame attempts used. Task
334.75 / 342.25. Generation disabled. Review sheet: `outputs/construction/03A-review-sheet.png`.

**User decision 2026-10-10:** frames accepted ("Accept the frames, commit, and quote the 03A motion test").
