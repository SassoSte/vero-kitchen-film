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

## Accuracy

The kitchen dimensions are photo-locked to the original 2023 MLS gallery of unit 2130
at The Allison Condominiums (14145 N 92nd St #2130, Scottsdale AZ 85260). The full
evidence chain — assessor ArcGIS record, sibling-unit gallery, marketing render
calibration — is in the deco project repo (`SassoSte/vero`, `kitchen-blueprint/`).