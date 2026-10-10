# Vero kitchen-remodel video — paused handoff

Updated **2026-10-09, America/Phoenix**. User explicitly said to **pause**, document the work, identify the stills, anchor the source material, and prepare this handoff/backlog. Documentation is complete; **production must not resume automatically**.

## Start here

1. [This handoff](HANDOFF.md): current truth and resume boundary.
2. [Source register](docs/SOURCE-REGISTER.md): original plans, dimensions, specifications, photos and provenance.
3. [Current design brief](mega-prompt.md): desired video/design, not permission to generate.
4. [Searchable stills gallery](outputs/stills-gallery.html) and [asset catalog](docs/ASSET-CATALOG.md): every still with role/status/path and receipts.
5. [Detailed backlog](docs/BACKLOG.md): ordered work, dependencies and acceptance evidence.
6. [Lessons](docs/LESSONS.md): mistakes and operating rules to preserve.

**Actual workspace:** `/Users/stefansassoon/projects/vero-kitchen-film`.
**Repository:** `git@github.com:SassoSte/vero-kitchen-film.git`, branch `main` at pause.
The chat initially opened in `~/projects/indigo`; that is NOT the kitchen workspace. Indigo supplied prior production lessons, not this kitchen's geometry.
**Architectural source workspace:** `/Users/stefansassoon/projects/vero/deco`.

## Deliverable and actual completion

Requested deliverable: a photoreal **60.000-second kitchen-remodel video**, 1920×1080, 24 fps, H.264 with AAC construction sound only. Two consistent workers; 13 editorial shots. No narration, music, captions or overlays. Visible installation/furnishing continues to second 55, followed by reveals.

**Not produced:** the complete film, its 13 final shot exports, final sound, or a current accepted set of construction states.

**Produced:** source-grounded design experiments, worker/installation test stills, three silent five-second diagnostic clips, editable shotlist, request/quote/result receipts, and the documentation package. Catalog contains **54 stills and 3 videos**. A still count includes sources and review images, not 54 paid generations.

There is **no generated still that fully implements the latest REF-K + French-door design**, and no current complete accepted three-view set. Earlier phrases such as “visual lock” meant a limited then-current internal review, not current user approval.

## Current user intent — do not reopen settled preferences

- **Coffee and wine:** SAME blank end wall beside the main refrigerator. User calls it the north wall; older kitchen notes call it the west end. Identify it by photographs, not compass shorthand.
- Latest appearance authority is [REF-K](references/inspiration/ref-k-integrated-coffee-wine.png): integrated recessed coffee/wine composition, warm-lit glass-front storage, a small preparation alcove and low wine storage. Use a **smaller sleek espresso unit** than pictured. Fronts are integrated/flush with the wall; no projecting tower or countertop box. The earlier plain white utility-hatch concept is superseded.
- **Spice/tech:** OTHER designated kitchen-side wall LEFT of sink near the microwave; neat spice jars, charging and compact Alexa-type device. Do not combine it with the wine wall.
- **Above dishwasher:** clear usable worktop. No exposed machine or garage there.
- **Main fridge:** now **French doors**—two upper doors meeting centrally, outer hinges, paired center handles—with a lower pull-out freezer drawer. **Exact model/height/cabinet surround and corner clearance are unresolved.** The single-door Bosch is superseded. Do not simply split its pictured door or preserve its 84-inch model-specific opening by habit.
- **Range:** Wolf GR304-style 30-inch gas range, red knobs, mandatory pale box/chimney hood and brushed pot filler. Viking choice superseded. Old OTR microwave removed; hood stays above range.
- **Microwave:** built into base cabinetry LEFT of sink, per [REF-J](references/inspiration/ref-j-sink-microwave.png). No countertop/over-range unit. Reject the forced x27–51 relocation introduced solely to fit the rejected projecting wine tower.
- **Sink/faucet:** one deep undermount basin; refined slim brushed-metal L-shaped faucet and matching dispenser. REF-J's double basin and old bulky faucet are not adopted.
- **Finishes:** white Shaker cabinets, frosted/translucent inserts, warm internal and continuous undercabinet lighting, pale veined quartz/full-height backsplash. Preserve ceiling-light continuity and source ceiling height.
- **Floor:** continuous warm-grey concrete through visible kitchen/living/dining; neutral rug under dining table. No oak floor or wall-to-wall carpet. Ribbed oak BAR FRONT remains.
- **Styling:** red SMEG toaster left of range and kettle right; three cream stools; flowers and low fruit bowl. No wooden floor lamp, Italy poster/map, wall wine racks or unrequested clutter.

The source image REF-K itself has a single-door refrigerator: **copy its coffee-wall design intent, not that appliance**.

## Geometry authority and portability

[Source register](docs/SOURCE-REGISTER.md) maps each original path to its local film copy and evidence class. [Copy manifest](references/source-manifest.json) records hashes. [Specification capture manifest](references/products/specs/capture-manifest.json) records official PDF URLs and local hashes.

Nominal source dimensions: kitchen runs 123 inches; zone depth 105; aisle 54; counter depth 25.5 and height 36; kitchen ceiling 96; uppers 54–84. Cooking-run modules are 33 + 24 + 30 + 36. Sink-side schedule records 66 + 33 + 24. Living room approximately 157×152; dining zone approximately 102×80.

These numbers retain source confidence: standard appliance modules, photo estimates (typically ±2–3 inches), and render-derived room spans (approximately ±4–6) are not the same evidence. A generated image never establishes dimensions or wall cavities. Use original photographs to reconcile viewpoints and openings; do not mirror a room because two SVG sheets use different page orientations.

Known source inconsistencies are explicitly retained in the register: 45-inch cap stroke vs approximately 60-inch schedule/elevation; 142-sqft kitchen label vs 123×105 inches ≈89.7 sqft; 462 inches mislabeled as 38 ft 5 rather than 38 ft 6; coarse appliance/stool labels in the whole-unit schematic.

Portable copies now include all four architectural SVGs, kitchen/living schedules, original appliance/material specifications, a whole-unit dimension extract, Tallbot calibration image, and additional original room photos. The whole-unit extract intentionally excludes owner/valuation/sale metadata while preserving the measurement method and source errors. The original complete source remains in `vero/deco`.

**The wall recess depth, structure, services, ventilation and actual operating clearances remain unverified.** Current renders are design concepts, not construction or purchase approvals. Do not repeat the earlier overconfident “structurally infeasible” assertion as an established inspection result either.

## Which images to retrieve

Use the [gallery](outputs/stills-gallery.html), not filename version alone. It can search/filter and links to the original-size image and receipts. [JSON catalog](docs/asset-catalog.json) has stable IDs, SHA-256 and exact paths.

| Need | Asset | Correct interpretation |
|---|---|---|
| Latest requested coffee composition | `references/inspiration/ref-k-integrated-coffee-wine.png` | Current USER reference; no generated implementation yet; single-door fridge not adopted |
| Original geometry | REF-A/B/H/I and supplemental photos03/24/25 | BEFORE/source evidence; sources override generated geometry |
| Best prior front styling/camera | `outputs/keyframes/apartment-v7.png` | Partial historical reference; has superseded SINGLE-door fridge |
| Sink-side component arrangement | `outputs/keyframes/sink-v4.png` | Useful microwave/L-faucet/nook/clear-DW reference; not full latest design approval |
| Wine wall plane reference | `outputs/keyframes/end-wall-flush-v1.png` | Historical flush-front study; blank hatch and single-door fridge superseded |
| Worker identities | `outputs/keyframes/workers-v1.png` | Earlier pilot identity reference; recheck before current production |
| Projecting service tower and Italy art | `end-wall-closed-v1/v2`, `end-wall-open-v1`, proposed SVG/JSON | REJECTED; never reuse as geometry or current design |
| Above-DW coffee box/panel | `coffee-garage-*` | REJECTED location; archive only |
| New REF-K/French-door still | `integrated-wall-frenchdoor-v1` | **NOT GENERATED / NOT SUBMITTED**; only request + quote exist |

All draft filenames remain unchanged for traceability. No image was deleted during the pause cleanup.

## Motion pilot outcomes

Three raw clips at `outputs/pilots/{quartz,fridge,stool}-v1.mp4`. Each is H.264, 1912×1080, 24 fps, 5.041667 seconds, silent—not final 1920-wide shot deliveries. Metadata is in `outputs/production/pilot-file-properties.json`.

- **Quartz: failed.** Workers release a misaligned slab with cabinet cavity still exposed. Fix source/end-state geometry before another motion prompt.
- **Fridge: provisional sampled motion candidate.** Placement looks plausible, but the partner obscures final placement. Uses an obsolete fridge/design.
- **Stool: failed final orientation.** Middle stool faces away from bar. Earlier “shrinking” suspicion was withdrawn; do not revive it as a confirmed defect.

Evidence: 6-fps contact sheets and full-size endpoints in `outputs/pilots/review/`; [inspection log](outputs/inspection.txt). This was **sampled review**, not continuous playback or every-frame acceptance. All source states predate latest design.

## Budget, authorization and stopped execution

- Approved task ceiling: **200 Higgsfield credits**.
- Recorded completed jobs: **32**, quotes totaling **198.25**; task allowance remaining **1.75**.
- Latest recorded account balance: **35 credits**, observed in the previous generation pass—not refreshed as part of pause documentation. Wallet movements outside task jobs are not attributed to this task.
- Next prepared request: `outputs/production/integrated-wall-frenchdoor-v1-request.json`; quoted **6.5 credits**, NOT SUBMITTED, absent from paid ledger jobs and with no result file.
- Proposed total cap **205 was asked about but NOT approved**. One 6.5-credit job would make the task total 204.75; arithmetic is not authorization.
- Earlier 500–800-credit full-video estimate was a proposal, not approved spending.
- No top-up/purchase, publishing, new scheduled work or automatic continuation is authorized.

`outputs/production/state.json` records `status: paused` and `generation_allowed: false`. `tools/run_image_job.py` now exits BEFORE quoting/uploading/submitting while paused. The guard was tested without touching the provider. All recorded jobs are terminal/generated; no known generation client from this chat remains running.

A future resume does not itself raise the spending ceiling. Require explicit resume and sufficient approved budget before clearing the guard. Keep one paid-job queue; check pending/result receipts before retries. Never resubmit an unknown-outcome job blindly.

## Resume sequence

1. Read this handoff, current brief, source register, backlog and state. Confirm explicit resume and spending authority (B02).
2. Resolve the actual French-door model and surround from manufacturer drawings; body width alone is insufficient at the corner wall (B03).
3. Reconcile REF-K's composition, smaller machine and distinct wall locations with original photo-based geometry (B04–B05).
4. Requote the prepared concept using corrected actual inputs; do not treat its stored request as final or auto-authorized. Inspect one returned result before expanding (B06).
5. Establish one consistent reviewed set of finished views, then START/END construction frames and identities (B07).
6. Repair/test quartz and stool strategy, re-test fridge with current unit, then propose a concrete full-batch budget before executing (B08–B10).
7. Assemble accepted takes, sound and exact 60-second export; inspect complete playback and every join, preserving explicit failures (B11–B13).

See [BACKLOG.md](docs/BACKLOG.md) for detailed acceptance tests and deferred/rejected items.

## Tools and safe documentation commands

- Canonical production access used: authenticated `higgsfield` CLI. Installed account/wallet are mutable; verify only after authorized resume.
- `tools/run_image_job.py <job-name>` reads saved request, quotes, reserves within cap, submits once and saves results. It is PAUSE-GUARDED; do not run it to resume by accident.
- User workflow name: `shotlist-director`. The local revised skill read in this chat was `/Users/stefansassoon/Documents/Codex/2026-10-07/can/outputs/skill-revision/seedance-shotlist-director/SKILL.md` (revision 2.0, still old internal name). The Higgsfield preset resolver did not resolve `/shotlist-director`; do not assume an installed server command or confuse that with the saved directing instructions.
- `python3 tools/build_asset_catalog.py` safely regenerates catalog/gallery from existing local files; no generation or network.
- `python3 tools/verify_handoff.py` safely validates links, hashes, pause/budget state and the unsubmitted job.
- `tools/build_end_wall_layout.py` reproduces a REJECTED historical proposal; do not run it as current design work.
- Commit using `git -c user.name="Stefan Sassoon (Codex)" commit ...`; stage only relevant named files. Do not persist harness author globally.

No secrets or authentication files are included in this handoff. Refer to recorded job IDs/paths, not credentials.
