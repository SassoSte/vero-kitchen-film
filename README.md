# vero-kitchen-film

Public payload repo for a Higgsfield `/shotlist-director` kitchen-remodel
construction film. Production decisions and unresolved inputs are recorded in
`mega-prompt.md`, including the mandatory hood above a Viking range and the
200-credit first-phase ceiling.

## What's here

| Path | Content |
|---|---|
| `mega-prompt.md` | The full production brief — reference hierarchy, dimensioned kitchen geometry, finished-design spec, 13-shot list with timings, continuity rules, and inspection protocol. Drop this into your Higgsfield prompt. |
| `kitchen-blueprint/dimensions.md` | Photo-locked kitchen dimensions (V/H/E confidence), appliance schedule, and materials. The ground truth for every measurement in the prompt. |
| `kitchen-blueprint/plan.svg` | To-scale plan (1 unit = 1 inch) showing both runs, the aisle, the bar, and the refrigerator-side corner. |
| `references/original/` | Four labelled files, two unique original views: REF-C duplicates REF-B; REF-D duplicates REF-A. |
| `references/inspiration/` | REF-E, REF-F, and REF-G are present; use them for appearance, not room geometry. |

## One missing original

If you have the apartment-facing photograph (the CleanShot taken from the living room
looking into the kitchen), save it as `references/original/ref-h-apartment-facing.png`.
The prompt needs it for apartment-facing coverage. Without it, hold those shots until
revised coverage is explicitly agreed; the existing originals do not show that view.

## Using with Higgsfield

1. Use the selected Viking gas model; resolve the knob preference and blueprint discrepancy recorded in the brief.
2. Add `ref-h-apartment-facing.png` to `references/original/`, or agree revised coverage.
3. Point Higgsfield at this repo and say:

> Read the full production brief from `mega-prompt.md`. Follow it exactly — every
> dimension, every reference file, every continuity rule. Start by establishing one
> consistent finished kitchen across three keyframes before generating any video.
> Do not skip the inspection pass.

## Accuracy

The kitchen dimensions are photo-locked to the original 2023 MLS gallery of unit 2130
at The Allison Condominiums (14145 N 92nd St #2130, Scottsdale AZ 85260). The full
evidence chain — assessor ArcGIS record, sibling-unit gallery, marketing render
calibration — is in the deco project repo (`SassoSte/vero`, `kitchen-blueprint/`).