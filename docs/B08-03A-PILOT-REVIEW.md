# B08 — 03A quartz-seating motion pilot (2026-10-10)

Allowance: [b08-03a-pilot-authorization](../outputs/production/b08-03a-pilot-authorization.json)
(≤2 kling_o3_flf pro jobs, ≤18 credits; v2 only after a written finding).

## Pilot v1 — `03A-pilot-v1` (9 credits) → `outputs/takes/03A-pilot-v1.mp4`

1912×1080, 24 fps, 121 frames (5.04 s), H.264 + AAC. Inspected every 3rd frame 0–30, then every 12th.

- Good: fixed camera; room, fridge, niche, cabinets stable; identities and wardrobe stable;
  slab descends evenly with the hands from n=0 to seating at ~n=18–21 (~0.8 s), stays rigid,
  hands remain in contact after seating and release only at the end (n≈96–120).
- **Defect:** from seating onward the slab top shows a stepped second edge near the lead's
  hands. Cause traced to the **END keyframe composite**, not the video model: END used the
  return's slab corner under the hands and the plate's slab elsewhere, leaving a visible
  step that Kling reproduced.
- Not tested: sound review (audio present, 5.04 s).

## Fix (unpaid) and v2

`03A-end-v2.png`: END re-composited from the same paid return (`03A-end-v1`) with the whole
slab and its front edge taken from the return (bbox to frame edge; slab contact polygon),
so START and END both carry the return-family slab. Accepted v1 END preserved as
`03A-end-v1-accepted.png`. Pilot v2 uses START unchanged + END v2, same prompt.

## Pilot v2 — `03A-pilot-v2` (9 credits) → `outputs/takes/03A-pilot-v2.mp4`

1912×1080, 24 fps, 121 frames (5.04 s), H.264 + AAC. Inspected every 3rd frame 0–36, then 60/90/120, plus wide frames and waveform.

- **Lead verdict: pilot pass, pending Stefan's review.** Single rigid slab throughout (step
  defect gone); even descent with both workers' hands on it; full contact at ~n=18–24
  (~0.9 s); hands stay until well after seating and lift off n≈90–120; camera, room,
  fridge, niche and cabinetry stable; identities stable.
- Limits: grip is on the top/front edge (inherited from START), not from below; output is
  1912 px wide (8 px short of 1920; scale/pad at assembly); native audio has a stone
  contact thud at ~1.0 s that matches seating plus an unmotivated second knock at ~2.7 s —
  trim or replace in the B12 sound pass.
- Edit slot for 03A is 10.0–15.0 s (5 s): v2 is usable in full or trimmed.

## Allowance closeout

2 jobs, 18 credits. Task 352.75 / 352.75; generation disabled.

**User decision 2026-10-10:** pilot v2 accepted ("Accept pilot v2, commit, and quote the B10 plan").
