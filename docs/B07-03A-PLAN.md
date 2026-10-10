# B07 — first stage frames for take 03A (prepared 2026-10-10, unpaid)

**Status: requests prepared; paid execution NOT authorized.** Proposal:
[b07-03a-frames-authorization-proposal.json](../outputs/production/b07-03a-frames-authorization-proposal.json).

## Method — derive earlier states from the selected view, never re-imagine the room

The old quartz pilot (`pilot-quartz-start-v2`) failed because a full-frame generation
re-invented the room (wood floor, new proportions, wrong cabinet). B07 frames are instead:

1. **Paid edit of the selected MASTER** (`kitchen-smeg-enclosure-v2`) with an explicit
   stage prompt.
2. **Local hard re-composite** with `tools/stage_composite.py`: the return is registered to
   the base by a homography fitted only on protected pixels, colour-matched on a ring
   outside the mask, and only masked pixels are kept. Protected pixels are byte-identical
   to the base (asserted). Drift the provider introduced is recorded per job.
3. Each frame is the base of the next, so START/END share one camera and room.

Masks (`tools/build_stage_masks.py`, `outputs/production/masks/`):

| Mask | Covers | Frame share |
|---|---|---|
| `plate-03` | cooking wall above worktop, fridge corner, range, north niche, west sink | 52.5% |
| `03A-action` | right cooking-run worktop and floor where workers stand | 31.6% |

Self-test: a synthetic 1% scaled/shifted, resized return registers with 702 RANSAC
inliers; protected-area mean difference drops 8.69 → 1.45 before compositing, 0 after.

## Sequence (strictly one at a time, inspect before the next)

| Job | Base | Produces | State |
|---|---|---|---|
| `stage-03-plate-v1` | MASTER + original ref-a (old fridge) | `outputs/construction/stage-03-plate.png` | concrete + bases + cooking-run quartz; no backsplash/uppers/hood/pot filler/range; old top-freezer fridge, bare wall; unfinished north niche; sink cutout empty; lights off; no people |
| `03A-end-v1` | accepted plate + workers-v1 | `outputs/construction/03A-end.png` | slab seated; both workers have just released |
| `03A-start-v1` | accepted END + workers-v1 | `outputs/construction/03A-start.png` | same slab ~8 cm above aligned bases, both gripping |

Cost basis: 6.5 credits per GPT Image 2 high/2k job on every prior comparable receipt; an
actual-input quote is taken by the runner before each submission. Proposed allowance:
≤6 jobs (≤2 attempts per frame, second only after a written finding), ≤39 credits, task
ceiling 303 → 342.25. No video in this allowance.

## Next after the frames are accepted

03A motion pilot: Kling 3.0 Omni first/last-frame (`kling_o3_flf`) between the accepted
START and END; inspect seating, contact and release. Separate quote and authorization.
GPT Image 2 also lists native `is_inpaint`/`mask` params; their schema is undocumented
locally, so the re-composite step is the guarantee regardless.
