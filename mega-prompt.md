# Kitchen remodel film — current design brief

> **PRODUCTION PAUSED BY USER — 2026-10-09.** This document records design intent;
> it is not execution authorization. Read `HANDOFF.md` before resuming. No generation,
> quoting through upload/submission flows or automatic continuation while paused.
> The proposed 205-credit cap has NOT been approved; current ceiling remains 200.


Current design authority, consolidated 2026-10-09 and revised for REF-K/French doors. Create a photorealistic **60.000-second** construction film of the kitchen at 14145 N 92nd St #2130, Scottsdale AZ 85260. This brief contains active instructions only. Prior contradictory proposals are archived in `docs/archive/mega-prompt-before-consolidation-2026-10-09.md` and are not production authority.

## 1. Locked locations and design intent

**Coffee location is resolved.** Wine fridge AND coffee garage occupy the SAME blank end wall beside the main refrigerator, both FLUSH WITH THE WALL FACE. This is the user's north wall, called west-end wall in the source kitchen schedule. No projecting cabinet, tower, countertop box, Italy print or other poster, spice shelf or tech device on that wall. Exact vertical placement and dimensions must preserve source architecture and be reconciled in reviewed concepts; do not invent an approved position absent evidence.

Spice/tech nook occupies the OTHER designated kitchen-side wall LEFT of the sink, near the microwave. Keep the wall identities distinct across cameras; never move this nook above the wine fridge. Preserve outlets, switches, opening and usable sink-side counter. Restrained matching spice jars, compact smart speaker and neat charging dock; warm accent light where selected. No extra unrelated shelves.

The full counter above the dishwasher remains CLEAR: no coffee machine, garage or tall panel there. Coffee/wine wall follows REF-K as an integrated, recessed composition: warm-lit glass-front storage, a compact coffee niche, a small recessed preparation alcove and low wine storage. Scale the espresso unit down from REF-K; retain our white Shaker cabinetry, pale oak accents, quartz and warm light. Closed appliance/cabinet fronts remain flush to the wall, with shelves/work surface recessed rather than projecting. No plain utility-hatch appearance. A pocket front may conceal the compact machine; an open state shows the actual coffee function. A kitchen-side insert may show the front opening and a supported tray presenting the machine, with closure only if the eventual edited sequence calls for it. For the next concept, show the lit coffee niche open as in REF-K, with a smaller machine; the old blank hatch is superseded. Do not morph the machine or imply verified runners, travel, wiring, plumbing or operating clearance.

**Wall-flush appliances are visual concepts, not verified cavities or construction plans.** Existing wall depth, structure, ventilation and services are unverified. Never represent a render or generated door opening as proof of physical installation feasibility. Do not carve a new room, widen the aisle or alter the exterior envelope to explain them.

## 2. Source authority and reference register

Explicit current user choices and this active brief govern final design. Original BEFORE photographs govern room topology, viewpoint and camera handedness, but do NOT establish the final appliances, floors, cabinets or coffee arrangement. Detailed kitchen dimensions/elevations govern module estimates; apartment notes govern adjacency. Inspiration governs only the listed appearance. Generated drafts establish no real geometry or surveyed dimensions. Do not mirror the room to reconcile SVG page orientation.

| Ref | Existing file | Authority / role |
|---|---|---|
| REF-A | `references/original/ref-a-cooking-run.webp` | Master camera, cooking run, refrigerator position, wall planes, refrigerator-side corner |
| REF-B | `references/original/ref-b-sink-run.webp` | Sink-run camera, sink/DW relationship, raised ledge, opening, apartment beyond |
| REF-C | `references/original/ref-c-wider-sink-run.webp` | Duplicate of REF-B; no additional viewpoint |
| REF-D | `references/original/ref-d-end-wall-closeup.webp` | Duplicate of REF-A; no additional viewpoint |
| REF-H | `references/original/ref-h-apartment-facing.webp` | Original photo-02: living-room-to-kitchen view, opening, bar front, three stools, dining adjacency |
| REF-I | `references/original/ref-i-empty-kitchen-living.webp` | Original photo-26: empty kitchen/living junction, carpet/tile boundary, wall planes, balcony sightline |
| REF-E | `references/inspiration/ref-e-cabinetry.webp` | White Shaker cabinetry, frosted/translucent upper inserts, veined stone finishes |
| REF-F | `references/inspiration/ref-f-cooking-zone.webp` | Pale box/chimney hood, brushed pot filler, cooking-wall material |
| REF-G | `references/inspiration/ref-g-full-room.webp` | Material character only; floor finish superseded by concrete; preserve current ceiling-track continuity |
| REF-H-DESIGN | `references/inspiration/ref-h-finished-apartment-facing.png` | User-supplied finished-design apartment-facing image; appearance/viewpoint intent only, not original geometry. Its electric cooktop and stainless undercabinet hood do not supersede the gas Wolf range and REF-F hood requirements. |
| REF-J | `references/inspiration/ref-j-sink-microwave.png` | User-supplied sink-side microwave placement reference; its faucet is rejected, and its double basin/floor do not supersede current design |

| REF-K | `references/inspiration/ref-k-integrated-coffee-wine.png` | User reference for recessed coffee/wine composition, lit glass storage and preparation alcove; use a smaller espresso unit. Its single-door fridge is superseded by requested French doors. |

REF-C/D duplicate REF-B/A and supply no additional viewpoint. REF-H/I are copied original photographs; provenance is in `references/source-manifest.json`. REF-H-DESIGN does not authorize its electric cooktop or undercabinet hood. REF-J (`references/inspiration/ref-j-sink-microwave.png`) governs the built-in microwave LEFT of sink, not its double basin, old faucet or floor.

Shared geometry/appliance checklist: `outputs/production/geometry-lock.json`. Original sheets: `kitchen-blueprint/plan.svg`, `kitchen-blueprint/elevations.svg`, `kitchen-blueprint/dimensions.md`, `apartment-blueprint/living-room-plan.svg`, `apartment-blueprint/living-room-dimensions.md`, `apartment-blueprint/unit-plan.svg`. Original drawings remain unchanged. `kitchen-blueprint/end-wall-proposed.svg` and `.json`, their render and the projecting end-wall images associated with commit `6d821ae` are REJECTED historical proposals, not current geometry/design authorities.

## 3. Fixed architecture and confidence

- Two parallel 123-inch runs; 105-inch kitchen zone depth; 54-inch aisle; 96-inch kitchen ceiling. Counters 36 AFF, depth 25.5. Uppers bottom 54/top 84, leaving 12 inches to ceiling.
- Cooking Run A sequence: original 33-inch fridge bay + 24-inch base + 30-inch range opening + 36-inch base. Keep actual fridge-side corner; no added bay, alcove, passage or room.
- Sink Run B: 66-inch pre-sink segment + 33-inch single-sink zone + 24-inch dishwasher segment. New microwave sits within base cabinetry LEFT of sink; exact model/cutout remains unverified. The rejected projecting-unit R1 plan does not authorize a blind return or relocated microwave coordinates.
- Preserve raised pass-through ledge, approximately 60 × 12 inches at 42–44 AFF, and 66-inch bar with three stool positions. Preserve opening, adjacent apartment, wall planes and floor levels. No island, extended bar or raised kitchen ceiling.
- Living room approximately 157 × 152 inches; dining approximately 102 × 80. Original photos control visual adjacency.
- Kitchen H estimates ±2–3 inches, E ±3–5; living/dining render-derived ±4–6. Not surveyed and insufficient for ordering appliances.
- Dimension/elevation approximately 60-inch cap overrides the plan's 45-inch stroke. Whole-unit schematic dishwasher/stool labels and opposite orientation do not override detailed sources. Its 142-sqft kitchen label conflicts with 123 × 105 inches (about 89.7 sqft); its 462-inch conversion is also wrong. Do not expand room geometry from these labels.

## 4. Finished design, consistent across all views

White Shaker cabinetry, frosted/translucent upper inserts, warm cabinet-interior light and continuous warm undercabinet light illuminating veined quartz/full-height slab backsplash. Preserve ceiling-light positions through matching angles. Light-oak ribbed bar front remains.

Continuous warm light-grey concrete through visible kitchen/living/dining, with restrained neutral rug under dining table/chairs. No oak floor or wall-to-wall carpet. Remove wooden standing lamp with brown rods/circular discs; retain kitchen ceiling lights.

Wolf GR304 30-inch stainless GAS range with red knobs in existing opening, beneath mandatory pale box/chimney hood per REF-F and brushed wall-mounted pot filler. Old electric range and old over-range microwave removed. No countertop or over-range microwave. NEW flush black-glass/stainless-trim built-in microwave in Run B base cabinetry LEFT of single-bowl sink. Do not move DW or sink to fit it.

Deep SINGLE-BOWL undermount sink, refined slim brushed-stainless/nickel faucet with gently squared L-spout and restrained lever; minimal matching soap dispenser. No old gooseneck or bulky drooping spray head. Preserve this silhouette across views.

**Main-fridge visual direction:** French doors: two upper refrigerator doors meeting at the center, paired central handles and outer hinges, with a lower pull-out freezer drawer. Preserve the existing 33-inch bay. The Bosch single-door selection and its 84-inch opening are superseded; exact French-door model, height, cabinet surround and wall-side opening clearance remain unverified. Do not create a fictitious French-door Bosch or widen the room. Reference image REF-K itself has a single upper door; do not copy that feature.

U-Line URWC315-IG01A is the preferred compact wine-fridge appearance candidate; its prior projecting cabinet arrangement is rejected. Current wine door must read flush with the blank wall face beside the main refrigerator. Do not claim this proves a recess, ventilation or fit.

Red SMEG toaster LEFT of range and matching kettle RIGHT, with usable preparation space. Compact sleek espresso machine and two small cups inside the wall-flush coffee garage on SAME wall as wine fridge. No ornate chrome tower or exposed above-DW coffee station.

One white/cream flower arrangement with greenery in a vase near one end of bar; one separate elegant low fruit bowl. Keep faucet/opening readable and counter space usable. Exactly three cream upholstered counter-height stools with plausible spacing and floor contact. No Italy art, unrelated shelves, wall-mounted wine rack or countertop clutter.

## 5. Current evidence and production gate

- `outputs/keyframes/apartment-v7.png`: targeted partial correction, generated and independently reviewed. Tall upper door/left handle, lower freezer drawer/horizontal handle, cupboard removal and L-faucet corrected; opening/stools/concrete/dining preserved. Exact dimensions/hinge operation unproved; wine wall outside view.
- `master-v4` and `apartment-v6`: OUTDATED old top-freezer/cupboard; v6 also old gooseneck. Never call these current approved frames.
- `sink-v3-concept`: component reference only. Microwave/faucet/spice styling may inform review, but exposed above-DW espresso is rejected and must be removed.
- Prior above-DW garages, projecting wine/coffee towers and Italy-art frames: REJECTED historical concepts.
- `outputs/keyframes/end-wall-flush-v1.png`: generated and independently passed visual intent. Separate wall-flush wine front and CLOSED white coffee panel above, no projecting tower/poster/tech, same Bosch configuration. Closed panel does not prove the coffee mechanism; a reviewed open state is still required before depicting operation.
- `outputs/keyframes/sink-v4.png`: generated with Nano Banana Pro cleanup and viewed by production lead. Exposed coffee machine/cups above DW removed; lower working counter clear. Microwave, L-faucet and separate spice/tech nook retained. Candidate sink view, not surveyed-fit proof. Coffee location is resolved; do not ask again.
- HISTORICAL candidate set, superseded by REF-K and French-door revision: apartment-v7 + end-wall-flush-v1 + sink-v4; exclude old master-v4. Reconcile these candidates and any additional required coverage before new motion. Exact surveyed fit and coffee mechanism remain unproved. No new motion has been generated from this set. Derive and inspect construction-stage START/END frames and worker identities before animation. Finished AFTER frames do not excuse inaccurate BEFORE or construction states.

## 6. Direction, takes and edit

Photoreal materials, believable weight/contact shadows, rigid components and plausible tool contact. Lead worker: short grey hair, navy work shirt, dark trousers, tan tool belt. Partner: grey shirt, dark trousers, dark cap, dark tool belt. Lock identity references.

Use source-based stable cameras; construction framing locked. Separate atomic actions into source takes. Time jumps occur in edit; no teleporting, morphing, dissolving or duplicate objects within an uninterrupted action. Track generated duration, selected source in/out and final edit range separately. Do not fill time with idle wiping. Installed features persist. No extra sink/faucet on Run A; no range on Run B.

## 7. Exact 60-second editorial timeline

Source takes may be longer than edited actions. Optional coffee opening/closure must fit existing Shot 11; omit the optional demonstration if unreadable rather than extend total duration. A reviewed open lit display state may remain for the REF-K appearance; do not confuse that display with a fully extended operating state. Wine/coffee operation shown separately, with no unverified simultaneous clearance claim.

| Shot | Time | Viewpoint | Action | Output |
|---|---|---|---|---|
| 01 | 00:00–00:05 | Master (REF-A) | Establish the original kitchen. Separate readable removal actions for old OTR microwave, electric range and wooden floor lamp; time jump to prepared room. Retain old fridge until Shot 07. | `outputs/shots/01_strip_out.mp4` |
| 02 | 00:05–00:10 | Master | Concrete finishing action, then time jump to levelling/fastening white base cabinets. Concrete continues through kitchen/living/dining; rug arrives during staging. | `outputs/shots/02_floor_and_bases.mp4` |
| 03 | 00:10–00:15 | Master | Both workers lower and seat solid quartz worktop on cooking Run A. No sink cutout or faucet on this run. | `outputs/shots/03_cooking_counter.mp4` |
| 04 | 00:15–00:20 | Sink run (REF-B) | Seat single-bowl sink/worktop on Run B, fit refined brushed L-spout faucet and soap dispenser, then separate insert installs the built-in microwave in base cabinetry LEFT of sink. Preserve DW, ledge and opening. | `outputs/shots/04_sink_install.mp4` |
| 05 | 00:20–00:25 | Master | Separate actions with time jump: full-height slab backsplash fitting, then Shaker upper-cabinet fastening. Frosted inserts visible. | `outputs/shots/05_backsplash_uppers.mp4` |
| 06 | 00:25–00:31 | Master | Separate actions: pale hood fitting, pot-filler fastening, Wolf GR304 gas-range placement with red knobs. No over-range microwave. | `outputs/shots/06_cooking_equipment.mp4` |
| 07 | 00:31–00:35 | Master incl. real corner | Remove old top-freezer and old over-fridge cupboard; time jump for opening preparation, then place the selected French-door refrigerator in the original bay, with two center-meeting upper doors and lower freezer drawer. Cabinet height follows the selected real model. | `outputs/shots/07_fridge_replacement.mp4` |
| 08 | 00:35–00:39 | Cooking-wall view | Test warm interior-cabinet and continuous undercabinet lighting; hood illumination on. All groups remain ON afterward. | `outputs/shots/08_lighting_install.mp4` |
| 09 | 00:39–00:44 | Supported viewpoint | Finish walls. Separate installation inserts establish wine fridge AND coffee garage flush with SAME blank end-wall face beside main fridge. Spice/tech nook is on OTHER kitchen-side wall LEFT of sink near microwave. No projecting tower or art. Visual fit only; no claimed cavity construction. | `outputs/shots/09_wall_finish_and_wine.mp4` |
| 10 | 00:44–00:49 | Apartment-facing (original REF-H) | Both workers position and secure ribbed oak bar-front treatment. Preserve opening, counters, faucet, room boundaries and lighting. | `outputs/shots/10_bar_front.mp4` |
| 11 | 00:49–00:55 | Apartment-facing + inserts | Workers position three cream stools and stage red SMEG toaster/kettle, flowers, low fruit bowl and neutral dining rug through short inserts. Coffee machine/two cups reside inside the end-wall garage. Optional kitchen-side tray opening/reveal and closure fit within this shot; coffee niche in the reviewed REF-K-inspired display state by second 55. Continue visible positioning work, not idle wiping. | `outputs/shots/11_stools_and_staging.mp4` |
| 12 | 00:55–00:57 | Widest original kitchen angle | Complete widest supported kitchen reveal with both runs and boundaries; all finished features and lights persist. Above-DW counter clear; coffee garage in the selected final state. | `outputs/shots/12_reveal.mp4` |
| 13 | 00:57–01:00 | Apartment-facing | Apartment-facing final reveal with complete opening, bar, three stools, flowers/fruit, sink faucet and cooking wall. Preserve final appliance configuration and concrete/rug. Coffee niche follows the reviewed REF-K-inspired display state; no machine or cabinet above the dishwasher. Restrained camera move only within supported geometry. | `outputs/shots/13_final_reveal.mp4` |

## 8. Continuity and actual-footage inspection

Old fridge stays until Shot 07; selected French-door refrigerator and its model-specific cabinet arrangement persist afterward. New sink-side microwave arrives Shot 04 and persists. Range/hood/pot filler stay fixed after Shot 06. Interior/undercabinet/hood lights stay ON from Shot 08. Stools and styling present by second 55; coffee garage in the selected final state through final frame. Wine/coffee wall and separate spice/tech wall never exchange identity. Above-DW counter remains clear.

Inspect returned footage, every join and ending against actual frames and source authority. Check readable installation work through second 55, stable workers/materials/props, correct floor and fixture locations, all final styling and consistent appliance door configuration. State review coverage honestly; sampled contacts are not every-frame or playback review. Record timestamps and defects; recheck affected joins/downstream shots after changes.

Earlier motion tests are diagnostic, not accepted production: quartz-v1 FAILED (released misaligned slab; cabinet opening exposed); stool-v1 FAILED (center stool facing away from bar; shrinking suspicion NOT confirmed); fridge-v1 sampled candidate motion pass only. Those clips are from superseded finishes. Review used 6-fps contacts/full-size endpoints, not every-frame/playback. Raw pilots 1912×1080, 24 fps, 5.041667 s, silent; not final film.

## 9. Budget, ownership and delivery

Hard first-phase ceiling **200 Higgsfield credits**, including pending/submitted jobs. `outputs/production/budget.json` owns task quotes/commitments. Global wallet movements may include unrelated work; never infer task spend solely from balance deltas. No automatic top-ups and no authorization for the earlier 500–800-credit full-film envelope.

One production lead owns design/state, paid queue, accepted references and edit. Delegates prepare bounded work and independently review actual evidence. Use `shotlist-director`; prefer quoted Kling initially, Seedance only where a demonstrated comparison warrants it. After two failures of unchanged action, change reference/framing/edit strategy. Account for outstanding jobs before retrying.

Deliver `outputs/kitchen_remodel_60s.mp4`: exactly 60.000 seconds / 1,440 frames, 1920×1080, 24 fps, H.264/AAC, construction sounds only, no music/speech/subtitles/overlays. Also deliver 13 named shot files, `outputs/keyframes/`, editable `outputs/shotlist.html`, and `outputs/inspection.txt`. Codec/duration checks establish properties, not architectural correctness. Preserve drafts and clearly distinguish planned, generated, inspected and accepted assets.

## Latest reference and French-door revision — 2026-10-09

REF-K supersedes the plain closed coffee-panel appearance: use an integrated recessed
coffee/wine composition adapted to our finishes, smaller compact espresso unit, warm
glass-front storage and small preparation alcove. Do not copy its overall width or
reintroduce a projecting tower. Spice/tech remains on the OTHER sink-side wall.

Main-fridge style is now French doors meeting in the middle with lower freezer drawer.
The previous Bosch single-door model and related height/cupboard decision are no longer
locked. A left outer hinge requires clearance beside the end wall. No 36-inch model
may be squeezed into the 33-inch bay or rendered as a confirmed fit.

Screened candidate FRFG1723AV: manufacturer's product sheet lists 31.3-inch closed
width but 37.5-inch width at 90-degree door opening, 67.9-inch height, 31-inch depth with
handle. Thus it is a size candidate, NOT a confirmed corner fit. Samsung RF18A5101SR
is 32.125 inches wide and its latest reviewed spec asks 3.75-inch wall-side clearance;
not assumed to fit this bay. F&P RF170ADJX4 is listed end-of-line. Final model pending
clearance verification. Do not use stock body width alone as an acceptance test.
Source: https://frigidaire.bynder.com/m/699ef842ab2132f7/original/FRFG1723A_EN-pdf.pdf

The next concept is prepared but NOT submitted: current cap 200, used 198.25, left 1.75.
Further paid generation requires a new explicit budget allowance.
