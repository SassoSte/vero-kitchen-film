# B06a local enclosure candidate — 2026-10-10

Candidate: [kitchen-smeg-enclosure-v2](../outputs/keyframes/kitchen-smeg-enclosure-v2.png) (generated as outputs/review/b06a-local-enclosure-v1.png) ·
[comparison](../outputs/review/b06a-local-enclosure-v1-compare.png) ·
[mask overlay](../outputs/review/b06a-local-enclosure-v1-mask-overlay.png) ·
[receipt](../outputs/production/b06a-local-enclosure-v1-receipt.json) ·
script `tools/b06a_local_enclosure.py`

**Status: ACCEPTED by Stefan 2026-10-10 ("Accept option 1 and continue to B07"); promoted as selected view 1. B06a closed.** Prior view 1 file preserved unchanged.

## Method (unpaid, deterministic, local)

- View 3's own over-fridge two-door Shaker cupboard pixels are perspective-warped into
  view 1's fridge front plane (corners measured from view 1: fridge door edges x=1296/1477,
  cupboard bottom on the fridge top line, top on the ceiling line), regraded from view 3's
  warm grade to view 1's upper-cabinet white, with a dark reveal above the fridge.
- Fitted enclosure: a painted white side panel replaces the visible stainless fridge side
  from ceiling to worktop, back to the east-wall line, shaded by view 1's own light field
  (under-cabinet pool kept). Panel front edges (~3/4in) added both sides of the fridge.
- Glass-front upper, toaster, range/hood, pot filler, worktop and everything else are
  excluded from the mask. Grain is tiled from view 1's plain north wall.
- Mask: 205,669 px (5.03% of frame), bbox x 1287–1700, y 0–1222. Verified **0 pixels
  changed outside the mask**. Views 1/2/3 source hashes unchanged.
- Paid spend: 0. Budget remains 302.25 / 303.

## Lead inspection against all three views

- Matches view 3: same-width two-door Shaker cupboard with paired central bar pulls over
  the French-door fridge, white fitted side panel, glass-front single upper beside it,
  toaster/range/hood sequence unchanged.
- No layout drift: fridge, range, glass upper, hood, coffee/wine station and camera are
  the original pixels. Nook stays off-crop (view 2 only).
- Weak points: the tall panel face above the glass upper is a flat, slightly cool plane
  (reads close to plain wall); cupboard handles are projected from a frontal source so
  their 3D relief is approximate; small residual sliver at toaster top-left corner.
- Visual approval only; not a fit/clearance certification.

## Options after review

1. Accept as-is (no spend).
2. Optional paid harmonization: one masked edit using this composite as the input with
   the same mask, then hard re-composite so only masked pixels can change. Requires a new
   explicit allowance; not authorized.
