# vero-kitchen-film

Public payload repo for a Higgsfield `/shotlist-director` kitchen-remodel
construction film. Production decisions and unresolved inputs are recorded in
`mega-prompt.md`, including the mandatory hood above a Wolf range and the
200-credit first-phase ceiling.

## What's here

| Path | Content |
|---|---|
| `mega-prompt.md` | The full production brief — reference hierarchy, dimensioned kitchen geometry, finished-design spec, 13-shot list with timings, continuity rules, and inspection protocol. Drop this into your Higgsfield prompt. |
| `kitchen-blueprint/dimensions.md` | Photo-locked kitchen dimensions (V/H/E confidence), appliance schedule, and materials. The ground truth for every measurement in the prompt. |
| `kitchen-blueprint/plan.svg` | To-scale plan (1 unit = 1 inch) showing both runs, the aisle, the bar, and the refrigerator-side corner. |
| `references/original/` | Six labelled files, four unique views: REF-C duplicates REF-B; REF-D duplicates REF-A; REF-H/I add apartment context. |
| `references/inspiration/` | REF-E, REF-F, and REF-G are present; use them for appearance, not room geometry. |

## Geometry package

The broader source project is `/Users/stefansassoon/projects/vero/deco`.
The film payload now includes its kitchen elevations, whole-unit and living-room plans,
and original apartment-facing photo-02 (REF-H) plus empty-room photo-26 (REF-I).
`references/source-manifest.json` records exact copy provenance. The source register and
precedence rules in `mega-prompt.md` reconcile the schematic discrepancies; another
apartment photograph is not required.

## Using with Higgsfield

1. Use the selected Wolf GR304 gas range with red knobs and the mandatory hood.
2. Load the original REF-H/I photos and the reconciled geometry source register.
3. Point Higgsfield at this repo and say:

> Read the full production brief from `mega-prompt.md`. Follow it exactly — every
> dimension, every reference file, every continuity rule. Start by establishing one
> consistent finished kitchen across three keyframes before generating any video.
> Do not skip the inspection pass.


## Production started — 2026-10-08

First-phase ceiling: **200 Higgsfield credits**. The editable directing document is
[`outputs/shotlist.html`](outputs/shotlist.html): 13 editorial shots, 30 atomic takes.
Actual job quotes, request/result receipts and state are in `outputs/production/`;
[`budget.json`](outputs/production/budget.json) is the cost ledger.

Candidate finished design references (visually checked for first-phase testing; not
proof of surveyed dimensions or exact manufacturer fidelity):

- [`master-v4.png`](outputs/keyframes/master-v4.png) — cooking wall.
- [`sink-v2.png`](outputs/keyframes/sink-v2.png) — sink and sleek lower-counter espresso station.
- [`apartment-v6.png`](outputs/keyframes/apartment-v6.png) — bar, stools, flowers and fruit.
- [`workers-v1.png`](outputs/keyframes/workers-v1.png) — the two recurring workers.

Motion proofs in `outputs/pilots/` are isolated tests, not the final film or accepted
production shots. Read [`outputs/inspection.txt`](outputs/inspection.txt) before reuse.
Initial pass spent 111.75 credits; the user-directed concrete/concealed-espresso
revision added 19.5. **Previous reference-set checkpoint: 131.25 credits; 68.75 remained** under the phase ceiling,
verified against the account balance. The current views remove the wooden floor lamp,
use continuous concrete with a dining rug, and hide the sleek coffee station from
the apartment-facing angle. Old motion proofs retain superseded finishes. Sampled pilot results: quartz fails worktop seating;
fridge is provisionally plausible; stool fails final orientation (faces away from bar).
No continuous-playback or frame-by-frame acceptance is claimed. All submitted jobs
completed; no automated paid work remains running.

The full 60-second film has **not** been generated. Rejected variants are retained as
drafts; the largest remaining production risk is physical-action endpoint fidelity.


Latest sink-side concept: [`sink-v3-concept.png`](outputs/keyframes/sink-v3-concept.png)
adds the requested built-in microwave and new faucet, plus a proposed shallow spice/tech
module on the kitchen-side end wall. The optional module awaits taste review before
propagation; other views still show the prior faucet. No motion generated for this change.
Total phase spend: **137.75 credits**, with **62.25 remaining** under the 200 ceiling.

## Accuracy

The kitchen dimensions are photo-locked to the original 2023 MLS gallery of unit 2130
at The Allison Condominiums (14145 N 92nd St #2130, Scottsdale AZ 85260). The full
evidence chain — assessor ArcGIS record, sibling-unit gallery, marketing render
calibration — is in the deco project repo (`SassoSte/vero`, `kitchen-blueprint/`).