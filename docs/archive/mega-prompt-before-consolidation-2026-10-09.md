# Kitchen remodel construction film — production brief

> **CURRENT DESIGN RESET — 2026-10-09.** The projecting end-wall tower and Italy
> artwork are rejected. Wine fridge must be flush with the blank end-wall face beside
> the main fridge. Spice/tech nook belongs on the kitchen-side wall left of the sink,
> near the microwave, not above the wine fridge. Keep above-DW counter clear. Coffee
> garage location is unresolved; no further paid generation until that placement is
> agreed. Original geometry remains evidence; flush recesses are visual intent, not
> verified cavities or construction plans. The later historical Q/R proposals are
> superseded by this reset.


Create a photorealistic 60-second construction film of the kitchen at 14145 N 92nd St
#2130, Scottsdale AZ 85260 (The Allison Condominiums, «Tallbot» 2B2B, 1,029 sqft).
Reference photographs and dimensioned blueprints are in this repo — use them as
ground truth. Produce one consistent kitchen across every viewpoint and stage.

## Cross-view geometry contract — 2026-10-09

`outputs/production/geometry-lock.json` is the shared dimension and appliance
checklist derived from the source plans/photos and the Bosch manufacturer sheet.
Every angle must use the same room and appliance state. No generated frame establishes
architecture or overrides the original photos. Never present a mixed-version gallery
as a current finished kitchen.

- apartment-v6 and master-v4 are outdated: old top-freezer and over-fridge cupboard.
- apartment-v7 corrects the front fridge/cupboard and faucet; inspect before acceptance.
- sink-v3-concept is a component reference only; exposed espresso placement is rejected.
- End-wall tower/poster frames remain rejected even though they show the newer fridge.
- There is currently no fully reconciled three-view set. Coffee location is unresolved.

## A. SOURCE AUTHORITY

Original photographs (this repo, `references/original/`) govern architecture.
Inspiration photographs (this repo, `references/inspiration/`) govern appearance.
The supplied blueprint (`kitchen-blueprint/dimensions.md` + `plan.svg`) governs dimensions.
Generated drafts establish neither.

### Geometry references

| Ref | File | What it governs |
|---|---|---|
| REF-A | `references/original/ref-a-cooking-run.webp` | Master camera, cooking run, refrigerator position, wall planes, refrigerator-side corner |
| REF-B | `references/original/ref-b-sink-run.webp` | Sink-run camera, sink/DW relationship, raised ledge, opening, apartment beyond |
| REF-C | `references/original/ref-c-wider-sink-run.webp` | Duplicate of REF-B; no additional viewpoint |
| REF-D | `references/original/ref-d-end-wall-closeup.webp` | Duplicate of REF-A; no additional viewpoint |

| REF-H | `references/original/ref-h-apartment-facing.webp` | Original photo-02: living-room-to-kitchen view, opening, bar front, three stools, dining adjacency |
| REF-I | `references/original/ref-i-empty-kitchen-living.webp` | Original photo-26: empty kitchen/living junction, carpet/tile boundary, wall planes, balcony sightline |

REF-H/I are copied without alteration from the original unit gallery in the local
`vero/deco` project; `references/source-manifest.json` records provenance and hashes.
The original apartment-facing reference is now available; no replacement photograph
is required from the user.

### Appearance references

| Ref | File | What it governs |
|---|---|---|
| REF-E | `references/inspiration/ref-e-cabinetry.webp` | White Shaker cabinetry, frosted/translucent upper inserts, veined stone finishes |
| REF-F | `references/inspiration/ref-f-cooking-zone.webp` | Pale box/chimney hood, brushed pot filler, cooking-wall material |
| REF-G | `references/inspiration/ref-g-full-room.webp` | Material character only; floor finish superseded by concrete; preserve current ceiling-track continuity |
| REF-H-DESIGN | `references/inspiration/ref-h-finished-apartment-facing.png` | User-supplied finished-design apartment-facing image; appearance/viewpoint intent only, not original geometry. Its electric cooktop and stainless undercabinet hood do not supersede the gas Wolf range and REF-F hood requirements. |
| REF-J | `references/inspiration/ref-j-sink-microwave.png` | User-supplied sink-side microwave placement reference; its faucet is rejected, and its double basin/floor do not supersede current design |

Appearance references do not authorize copying their room dimensions, island, floor plan,
or cabinet arrangement. Photographs govern architecture; inspiration governs appearance.

## B. KITCHEN GEOMETRY — SUPPLIED DIMENSIONS

These are source estimates with V/H/E confidence, not surveyed dimensions. Preserve
the source tolerances (H ±2–3″; E ±3–5″). See
`kitchen-blueprint/dimensions.md` and `kitchen-blueprint/plan.svg` for the full record.

The kitchen is a compact **galley**: two parallel 123″ runs separated by a **54″ aisle**.
Ceiling: **96″ flat** over kitchen; vaulted beyond the pony wall into the living room.
No window in the kitchen — a clerestory awning window on the hall wall illuminates the aisle.

### Run A — cooking/refrigerator wall (hall/dining side)

| Segment | Dim |
|---|---|
| Total length | 123″ (10′3″) |
| Refrigerator bay (west end wall) | 33″ clear — **FIXED ARCHITECTURAL CORNER** |
| Base cabinet, fridge→range | 24″ |
| Range opening | 30″ (smoothtop electric) |
| Base cabinet, range→east opening | 36″ |
| Counter depth | 25.5″ (incl. 1.5″ overhang) |
| Counter height | 36″ AFF |
| Uppers | 12″ deep, bottom 54″ AFF, top 84″ AFF; no soffit |
| OTR microwave | 30″ wide, bottom rail ≈67″ AFF, recirculating |

The microwave is **over-the-range in the original kitchen only**. Remove it during
strip-out; it must not appear above the range in the finished kitchen. A NEW built-in
microwave is authorized in the sink-side base cabinetry (see Section D). The original smoothtop range
is replaced by the Wolf range specified below. Existing-appliance measurements
above describe the BEFORE state, not the finished appliance selection.

The wall behind Run A is an interior stud partition (hall/dining side). A pot-filler
water line is retrofittable here. Two four-head black track lights illuminate the aisle.

### Run B — sink/bar wall (living room side, pony wall)

| Segment | Dim |
|---|---|
| Total length | 123″ (10′3″) |
| Bar | 66″ at west (open) end; 3 stools at 21–22″ centers; 12–13″ overhang to living; top 36″ AFF |
| Sink base | 33″ — double-bowl SS drop-in, high-arc faucet |
| Raised granite pass-through cap | ≈60″ long × 12″ deep, top 42–44″ AFF, spans the sink zone |
| Dishwasher | 24″ opening, adjacent to the Run A corner |

No uppers on Run B — open to the 96″ ceiling. The pass-through faces the living room.

### The west end wall (refrigerator-side corner)

The source notes identify this as the building-envelope end wall. No survey of its
construction or usable cavity exists here. The user calls this the NORTH WALL and has
confirmed it means the blank end wall BESIDE the main refrigerator, not the cooking
wall. Treat a built-in wine fridge as a properly dimensioned cabinet installation in
front of that wall; do not assume it can disappear into a wall cavity. See Section Q.

### Floor

Original state: beige kitchen tile and living/dining carpet. Final design, revised by
the user: continuous warm light-grey concrete flooring through the visible kitchen,
living and dining areas, with subtle natural variation and a matte/satin finish. One
tasteful neutral area rug sits under the dining table/chairs. No wall-to-wall carpet
or oak floor remains in the finished visible rooms. Preserve room boundaries and
levels; the material transition is intentionally removed, not the architecture.

## C. PRESERVE

- The actual kitchen footprint and 96″ ceiling
- Existing wall planes, corners, and circulation
- The opposing cooking and sink runs
- The raised pass-through ledge and bar
- The original apartment architecture visible beyond the opening; flooring changes
  to concrete as explicitly authorized
- Existing room boundaries and floor levels, with continuous final concrete flooring
- The refrigerator-side corner — do not extend the cooking wall past it or invent an
  extra bay, alcove, passage, or room behind it
- The sink and faucet belong on Run B; the range belongs on Run A beneath the hood;
  the pot filler goes on the cooking backsplash above the range
- No sink, sink cutout, or faucet on the cooking run
- No island, no extended bar, no raised ceiling, no moved opening

## D. FINAL DESIGN

Translate the inspiration photographs into the supplied geometry:

- White Shaker cabinetry with frosted/translucent glass upper inserts
- Warm interior lighting within glass cabinets
- Continuous warm undercabinet lighting visibly illuminating the backsplash
- Reference-matched veined quartz countertops and full-height slab backsplash
- Continuous warm light-grey concrete floor through kitchen/living/dining, with a
  restrained neutral rug under the dining table and chairs; no carpet or oak floor
- Mandatory pale box/chimney hood matching REF-F, centered above the Wolf range
- Brushed wall-mounted pot filler above the range on Run A
- Modern deep single-bowl undermount sink on Run B (retain the current single basin).
- Refined slim brushed-stainless/nickel faucet with a clean gently squared L-shaped
  spout and restrained single lever, matching the cabinet hardware and pot filler.
  Avoid the bulky drooping spray head in REF-J. Pair with a minimal matching soap
  dispenser; lock the selected silhouette across all viewpoints.
- Stainless main refrigerator in the original 33″ bay
- Wolf GR304 30″ gas range, stainless steel with red control knobs, beneath the
  mandatory REF-F-style hood and pot filler. This supersedes the earlier Viking choice.
  Product reference: https://www.subzero-wolf.com/wolf/ranges/gas-range/30-inch-gas-range
  Knob reference: https://www.subzero-wolf.com/products/marketing-accessories/gas-range-knobs
  Preserve the existing 30″ opening. Gas is the approved film/design intent, not
  evidence that the existing apartment has a gas connection.
- Tastefully arranged SMEG small appliances: matching red toaster LEFT of the range
  and red kettle RIGHT, on the adjacent counters with usable preparation space around
  them. Use the approved reference appearance consistently; avoid a crowded appliance
  display or extra units added just to fill the counter.
- Keep the entire worktop above the dishwasher CLEAR and usable. The previous coffee
  garage at that position, including its tall fitted panel, is rejected and removed.
- Coffee garage location is unresolved. The candidate for discussion is the sink-side
  wall above the microwave-side worktop, under the spice/tech nook. This is not yet
  selected. Do not bundle coffee with the wine fridge or place it above the dishwasher.
- Remove the tall wooden floor lamp/sculptural light with brown vertical rods and
  circular discs from the living-room foreground. Keep the kitchen ceiling lights.
- One tasteful vase of fresh flowers, with a restrained white/cream arrangement and
  natural greenery, toward one end of the apartment-facing bar. Keep the faucet,
  opening, hood, and cooking wall readable.
- One elegant low fruit bowl with a modest arrangement of fresh fruit on the bar,
  separated from the flowers. Preserve clear counter space and three usable stool
  positions. Flowers and fruit bowl are mandatory finished-design elements.
- Original over-the-range microwave removed; the Wolf retains its mandatory hood.
- NEW built-in microwave in the sink-side base cabinetry to the LEFT of the sink,
  as shown in `references/inspiration/ref-j-sink-microwave.png`: restrained black glass
  face with brushed stainless trim, flush integrated into the cabinet run below the
  worktop. No countertop microwave, no microwave above the Wolf, no displaced dishwasher
  or sink. REF-J controls this appliance placement, not its double-bowl sink or floor.
  Exact model/cutout/ventilation remain to be selected before claiming physical fit.
- Kitchen-side spice/tech nook: on the wall immediately LEFT of the sink worktop near
  the microwave, treated separately from the wine-fridge wall. Never on the apartment-facing wall. One shallow white-framed joinery
  module with pale oak lining, an upper shelf of restrained matching spice jars,
  and a lower integrated tech shelf for one compact Alexa-type speaker and neat phone
  charging dock. Warm concealed accent light, concealed cable route, usable worktop
  beneath. Preserve existing switch/outlet positions and opening geometry. Show this
  as a shallow built-OUT panel/module; do not assume a cavity or cut into the existing
  wall. This is a visual design concept, not proof of wall-recess feasibility.
- Light-oak vertical/ribbed treatment on the apartment-facing bar front
- Three cream upholstered counter-height stools with slim legs/footrails,
  credible spacing, feet resting on the floor
- Restrained artwork/decor on an available wall surface

Do not add: unrelated floating shelves (the integrated spice/tech module is the specific
authorized exception), wall-mounted wine racks, a countertop microwave, an island,
wall-to-wall carpet, oak flooring, the rejected wooden floor lamp, or an ornate
espresso machine.

## E. WINE-FRIDGE REQUIREMENT

Compact built-in wine fridge on the blank end wall beside the main refrigerator,
front flush WITH THE WALL FACE. No projecting cabinet, tower, shelf or countertop
around/above it. U-Line 15-inch class remains a candidate appearance/size reference,
not confirmed installation fit. No Italy poster or map. The prior 18x24-inch projecting
cabinet and its related blind-corner/microwave relocation are REJECTED.

The room documentation does not establish a cavity of the required depth. Treat the
flush installation as the user's visual concept, keep that feasibility gap explicit,
and do not enlarge the room or claim real fit from a generated image.

## F. ESTABLISH ONE FINISHED KITCHEN BEFORE ANIMATION

Create three finished-design keyframes grounded in the original photographs:

1. Finished master kitchen view (from REF-A).
2. Finished sink-run view (from REF-B).
3. Finished apartment-facing view from original REF-H, cross-checked with REF-I and
   the kitchen/living-room drawings; REF-H-DESIGN controls finish intent only.

They must agree on wall boundaries, sink/range locations, refrigerator model and position,
cabinet layout, glass inserts, hood, pot filler, quartz/backsplash, interior cabinet
lighting, undercabinet lighting, bar finish, faucet, three stools, countertop appliances,
floor boundary, sleek espresso-machine detailing and hidden front-view placement, flower arrangement, vase, fruit bowl,
and wine-fridge location if used.

Do not independently redesign the kitchen for each viewpoint. Save the keyframes to
`outputs/keyframes/`.

## G. FILM LANGUAGE

Photorealistic materials, believable weight, contact shadows, rigid appliances, plausible
tool use. Two identifiable workers throughout:
- Lead: short grey hair, navy work shirt, dark work trousers, tan tool belt
- Partner: grey shirt, dark trousers, dark cap, dark tool belt

Stable cameras based on original photographic viewpoints; construction shots use locked
framing. Editorial time jumps represent elapsed time — components must not morph, dissolve,
or teleport during an uninterrupted action. Each action addresses the correct component
(drill into mounting surfaces, not appliance doors).

## H. 60-SECOND SHOT LIST

Shots show edited screen times. Generate source takes long enough for readable actions and
trim appropriately.

| Shot | Time | Viewpoint | Action | Output |
|---|---|---|---|---|
| 01 | 00:00–00:05 | Master (REF-A) | Strip-out: establish existing kitchen, show removal of old components including the OTR microwave and old range, time jump to prepared room; retain old fridge until Shot 07 | `outputs/shots/01_strip_out.mp4` |
| 02 | 00:05–00:10 | Master | Floor-fitting action then time jump to workers levelling/fastening new base cabinets. Concrete continues through kitchen/living/dining; dining rug is added during staging. | `outputs/shots/02_floor_and_bases.mp4` |
| 03 | 00:10–00:15 | Master | Both workers lower and seat the quartz worktop on the cooking run. NO sink cutout or faucet on this run. | `outputs/shots/03_cooking_counter.mp4` |
| 04 | 00:15–00:20 | Sink run (REF-B) | Sink/worktop assembly seated on the sink run, then faucet fitting. Preserve DW, ledge, opening, apartment beyond. A separate insert installs the sink-side built-in microwave in the left base cabinet. | `outputs/shots/04_sink_install.mp4` |
| 05 | 00:20–00:25 | Master | Separate beats with time jump: backsplash fitting, then upper-cabinet fastening. Shaker doors and glass inserts visible. | `outputs/shots/05_backsplash_uppers.mp4` |
| 06 | 00:25–00:31 | Master | Separate actions with time jumps: hood fitting, pot-filler fastening to backsplash, then Wolf range placement beneath hood. No over-the-range microwave returns; sink-side built-in remains separate. | `outputs/shots/06_cooking_equipment.mp4` |
| 07 | 00:31–00:35 | Master incl. real corner | Remove old fridge, place new one in the same 33″ bay. | `outputs/shots/07_fridge_replacement.mp4` |
| 08 | 00:35–00:39 | Cooking-wall view | Worker installs and tests interior-cabinet and continuous undercabinet lighting. Illuminated backsplash clearly visible. Lighting stays ON for the rest of the film. | `outputs/shots/08_lighting_install.mp4` |
| 09 | 00:39–00:44 | Supported viewpoint | Wall-finish work and artwork hanging; if the spice/tech concept is adopted, fit the shallow module to the sink-side wall near the microwave in a separate action. Install the wall-flush wine fridge only after its visual location is locked; no projecting cabinet. Preserve the west corner. | `outputs/shots/09_wall_finish_and_wine.mp4` |
| 10 | 00:44–00:49 | Apartment-facing (original REF-H) | Both workers position and secure the oak bar-front treatment. Preserve opening, counter, faucet, room boundaries. All lighting stays on. | `outputs/shots/10_bar_front.mp4` |
| 11 | 00:49–00:55 | Apartment-facing + inserts | Three cream stools carried in and positioned by workers. Red SMEG toaster and kettle, coffee garage with compact sleek machine and two cups, fresh flowers, fruit bowl, and dining rug placed through separate short action inserts. End with visible positioning work, not prolonged wiping. | `outputs/shots/11_stools_and_staging.mp4` |
| 12 | 00:55–00:57 | Widest original kitchen angle | Complete reveal: both runs, all boundaries, all completed features including SMEG appliances, coffee garage (closed in the apartment-facing view), flowers, and fruit bowl. Interior/undercabinet/hood lighting on. | `outputs/shots/12_reveal.mp4` |
| 13 | 00:57–01:00 | Apartment-facing | Final reveal: complete opening, finished bar with flowers and fruit bowl, three stools, sink faucet, cooking wall; retain SMEG appliances and coffee garage (closed in the apartment-facing view) in their established positions. Restrained camera move allowed if geometry is preserved. | `outputs/shots/13_final_reveal.mp4` |

Output format: 1920×1080, 24 fps, H.264 with AAC audio (construction sounds only — no
speech, music, subtitles, or overlays). Final film: `outputs/kitchen_remodel_60s.mp4`.
Shotlist: `outputs/shotlist.html`. Inspection record: `outputs/inspection.txt`.

## I. CONTINUITY RULES

Once installed, a feature stays installed. Specifically:
- The sink stays on Run B; a second sink never appears on Run A
- The Wolf range stays beneath the hood and pot filler after Shot 06
- The old over-the-range microwave is removed in Shot 01 and never returns. The
  NEW sink-side built-in microwave arrives in Shot 04 and remains there afterward.
- The refrigerator changes only during Shot 07
- Cabinet-interior and undercabinet lighting stay on after Shot 08 through the final frame
- The three stools arrive through worker actions in Shot 11 and remain afterward
- SMEG appliances, coffee garage, compact machine and two cups, vase/flowers, and fruit bowl
  are staged by the end of Shot 11 and remain unchanged through Shots 12–13. Preserve
  their positions and appearance across cuts; do not clutter the worktops.
- Cabinet arrangement, hardware, stone surfaces, appliance positions, and floor boundaries
  remain consistent across all shots

The final 20 seconds must contain actual installation and furnishing progress until second 55.
Worker presence alone is insufficient.

## J. INSPECT THE EXPORTED FILM

Watch the complete exported film and inspect every cut against the actual returned frames:

- Shots 03/04/06: correct cooking-run vs sink-run assignment
- Shot 06 onward: selected Wolf range beneath the mandatory hood; no over-the-range microwave
- Shots 07/09/13: same refrigerator position, real corner, supported wine-fridge geometry
- Shots 08/10/11/12/13: same interior-cabinet, undercabinet, and hood lighting
- Shots 10/11/13: same bar, faucet, three stools, opening, apartment-facing geometry
- Shots 11–13: all final countertop styling present by second 55; stable SMEG
  appliances, coffee garage/machine/two cups, flowers/vase, and fruit bowl. Verify
  their correct placement across the two reveal angles and usable counter/stool space.
  Espresso is visible only from kitchen-side views, concealed in apartment-facing view.
- Final views: continuous concrete floor, dining-area rug, no wooden floor lamp.
- Sink-side views: built-in microwave left of sink, same new faucet silhouette, and
  spice/tech module on the kitchen-side end wall if adopted. No dishwasher displacement.
- All shots: consistent workers, plausible actions, cumulative construction progress
- 00:35–01:00: no feature disappearance, layout changes, idle filler, or lighting loss

If a requirement fails, report the exact timestamp and defect. Correct the affected shot
and recheck its joins and downstream continuity. File-duration checks and motion
measurements do not establish architectural correctness.

## K. DELIVERY

- `outputs/kitchen_remodel_60s.mp4` — the complete 60.000-second film
- `outputs/shots/` — the 13 individually named shot files
- `outputs/keyframes/` — the three consistent finished-design frames
- `outputs/shotlist.html` — asset, take, and edit timing record
- `outputs/inspection.txt` — verified findings and any unresolved issue

Preserve previous versions as drafts. Raise a question only for missing information that
materially prevents the requested design from being represented correctly.

## L. APPROVED PRODUCTION APPROACH — 2026-10-08

User-approved first phase: design references and representative motion tests, with a
hard ceiling of 200 Higgsfield credits. This is not authorization to spend the proposed
500–800-credit full-film envelope. Quote jobs with their actual inputs, track submitted
and pending costs, and preserve the cap across delegates. No automatic top-ups.

Use the directing workflow named `shotlist-director` (formerly
`seedance-shotlist-director`). One production lead owns the design/state ledger,
accepted references, paid-job queue, and edit. Delegate bounded shot preparation and
independent continuity review; workers must not redesign their assigned viewpoints.

Lock finished views and worker identities, then derive reviewed construction-stage
frames. Pilot quartz seating, refrigerator movement, and furnishing where supported
by the references. Prefer quoted Kling production initially; use Seedance selectively
when a comparison demonstrates a benefit. Split the 13 editorial shots into atomic
action takes and assemble time jumps in the edit. After two failures of the same
action, change the reference, framing, or edit strategy rather than repeat it unchanged.

## M. RECONCILED GEOMETRY SOURCES — 2026-10-08

Reviewed all four architectural SVGs in `/Users/stefansassoon/projects/vero/deco`,
including rendered sheets, supporting dimensions/specifications, asset index, research
method, and original photos 02/26. Relevant sheets are included in this payload:

- `kitchen-blueprint/plan.svg`: 123″ runs, 54″ aisle, 33″ refrigerator bay, 30″ range
  opening, opposing sink/DW run, 66″ three-stool bar.
- `kitchen-blueprint/elevations.svg`: BEFORE-state elevations; 96″ kitchen ceiling,
  counters 36″ AFF, uppers 54–84″ AFF, raised cap 42–44″ AFF. The depicted microwave
  is removed in the film, not carried into the finished design.
- `apartment-blueprint/living-room-plan.svg` and `living-room-dimensions.md`: adjacent
  living room, approximately 157″ × 152″, kitchen/bar opposite balcony slider,
  vaulted ceiling, original carpet (superseded by final concrete), and open dining
  connection. Door gaps are schematic.
- `apartment-blueprint/unit-plan.svg`: whole-apartment context only. Do not extract
  appliance placement, stool spacing, or camera handedness from this coarse sheet.

Production precedence: original unit photos fix visible topology and camera handedness;
kitchen dimension schedule and elevations fix detailed kitchen modules; living-room
notes fix adjacency. The whole-unit diagram uses the opposite orientation convention
from the living-room sheet. Do not mirror the kitchen to make their page orientations
agree. Use REF-H for the front camera and REF-I for the side relationship.

Drawing discrepancies are recorded rather than treated as absent architecture:
- Raised-cap line in kitchen plan spans 45″; the kitchen dimensions, specifications,
  and elevation all support approximately 60″ (elevation x=54 to 114). Use the latter
  as the film's approximate cap length; retain the actual photographic wall/ledge shape.
- Whole-unit sheet puts a DW label on the cooking side and spreads stools beyond the
  66″ bar. The detailed kitchen plan/photos override these schematic errors.
- Whole-unit schedule reports kitchen area 142 sqft despite 123×105″ yielding about
  89.7 sqft, and labels 462″ as 38′5″ rather than 38′6″. Do not propagate those labels
  into the film. Use linear kitchen modules, not an area-derived expansion.
- Living-room and unit SVGs use inherited CSS colors; native review with a white
  background was readable. They should not be used as style references.

The source drawings are preserved unchanged. These limits do not block reference-based
film production. The requested end-wall wine fridge remains a candidate until its bay and clearances are locked.

## N. DESIGN REVISION — CONCRETE AND CONCEALED COFFEE STATION

The user rejected the wooden floor lamp, carpet floor and ornate espresso machine.
This revision supersedes those features in all earlier candidate images, shotlist
prompts and motion proofs. Preserve old assets as drafts; invalidate their final-design
acceptance. Concrete extends across visible kitchen/living/dining, with a dining rug;
the oak bar-front treatment remains. The initial sleek-machine location over the dishwasher is now superseded by Section Q;
that counter must remain usable. No new motion
until the revised reference views agree.

## O. SINK-SIDE DESIGN ADDITIONS — 2026-10-08

User requested the sink-side built-in microwave shown in REF-J, a faucet suited to the
current design, and a possible spice nook/tech shelf with charging and an Alexa-type
device on the bare kitchen-side wall left of the sink. These supersede the blanket
no-microwave rule and the earlier faucet. Retain the single-bowl sink, concrete floor,
hidden sleek espresso above dishwasher, flowers and fruit. First review the sink-side
concept before propagating the optional joinery design or spending on motion.

## P. COFFEE GARAGE REVISION — SUPERSEDED LOCATION

The earlier above-dishwasher concept is rejected by the user because it consumes
needed counter space. Keep its renders as historical drafts only. A possible coffee
garage at the new wine-fridge wall must be re-planned under Section Q; do not reuse
the old location or treat the earlier paired images as an approved installation.

## Q. HISTORICAL RESEARCH — END-WALL CABINET PROPOSAL REJECTED

User confirmed the blank end wall beside the main refrigerator (called north wall by
the user; west-end wall in the kitchen source schedule). Keep this identity unambiguous.
The above-dishwasher coffee garage is REJECTED: restore that working counter. All prior
coffee-garage images are historical concepts, not production authorities.

Preferred premium main-fridge candidate: **Bosch Benchmark B30BB130SS**, stainless,
upper refrigerator door configured RIGHT-HINGED when facing its front (hinge toward
the cooking-run side, away from the blank end wall), lower freezer DRAWER. This is a
recommendation, not an appliance purchase or confirmed fit. Manufacturer spec:
- Body width 29 3/4 inches; minimum height 83 9/16; depth with doors/handles 26 7/8.
- Proud-install opening 84 H x 30 W x at least 24 D inches; flush install depth at least 25.
- Reversible upper door; full-extension freezer drawer. Official listed price $9,699
  when reviewed; installation/cabinet work extra. Existing over-fridge cupboard must
  be removed/reconfigured to make the 84-inch opening; preserve original 33-inch bay.
- Spec page 3 explicitly diagrams 90/115-degree swing and 33-inch front clearance for
  proud installation. That drawing, not a generated opening animation, governs.
- Source: https://www.bosch-home.com/us/en/product/refrigerators/bottom-freezer/built-in/B30BB130SS
- Local manufacturer spec: references/products/specs/bosch-b30bb130ss.pdf

Compact wine-fridge candidate: **U-Line URWC315-IG01A**, glass with integrated frame
finished to match cabinetry, warm-white interior light, 18 standard 750mL bottles.
- Product approximately 14 7/8 W x 34 1/8 H x 22 11/16 D inches (manufacturer table).
- Spec cutout 15 1/8 W x 34 1/4–35 1/4 H x 24 D; panel adds depth. Front grille stays clear.
- Door is field-reversible; final hinge side is NOT fixed until both appliance sweeps,
  adjacent cabinet fronts and bottle-rack extension have been checked together.
- Official integrated-frame list price $2,639 when reviewed, custom panel extra.
- Source: https://www.u-line.com/urwc315.html
- Spec: https://www.u-line.com/pub/media/u-line/spec_sheets/URWC315.PDF?new_version=92529

Earlier value candidate RF170WDRX5 N (Fisher & Paykel) is END OF LINE on its official
US page. Its 31 1/8-inch body width and bottom drawer suit the concept, but product-page
side-clearance figures differ from the family installation guide. Do not promise a
fit in 33 inches or choose it for purchase without resolving stock/spec applicability.

Nominal geometry only: kitchen runs have 54-inch separation. An 18-inch-wide end-wall
cabinet tucked toward the sink occupies the end 24 inches of aisle length; it does not
magically sit inside the wall. In the simple source coordinate system (Run A y 0–25.5,
Run B y 79.5–105), its proposed footprint is x 0–24, y 61.5–79.5. The Bosch proud-install
drawing suggests an approximate forward door envelope to y 57 (24+33), leaving only
about 4.5 inches to the candidate wine cabinet before room error, positioning and trim.
This is a screening estimate, NOT collision-free fit proof. Freezer drawer travel,
standing room, handle projections and full wine rack pull-out remain to be checked.
The source's ±2–3-inch estimates are not precise enough for ordering appliances.

End-wall art direction: one tasteful vertical Italy map/wine-region print, muted cream,
charcoal and restrained olive/terracotta, thin oak or dark frame. Starting art size
approximately 18x 24 inches; adjust to actual free wall. The wine cabinet, possible coffee
garage, Italy art and existing spice/tech nook occupy the SAME end-wall composition.
Do not independently stack all of them into the same space. Favor an uncluttered wall
and usable worktop; exact coffee/spice/art arrangement remains a layout task.

The nominal film envelope is now resolved in Section R and the proposed plan.
Concept rendering is authorized; real construction/ordering still requires measured
clearances. No claim of surveyed fit follows from the render.

## R. HISTORICAL COORDINATED TOWER — REJECTED, DO NOT EXECUTE

Current concept authority: `kitchen-blueprint/end-wall-proposed.json` and `.svg`.
These are NEW proposal files; original plans remain unchanged.

- Main fridge: Bosch candidate in original 33-inch bay, 30-inch opening and 84-inch
  height, right upper hinge away from end wall, bottom freezer drawer. Remove the old
  above-fridge cupboard to make that height.
- End-wall unit: 18 inches overall along the wall, 24 inches deep into room, at the
  sink-side end (plan x0–24, y61.5–79.5). Wine appliance below a 36-inch worktop.
- Upper module: 18 inches wide and 18 high, approximately 36–54 AFF. Coffee bay takes
  roughly 11.5 inches gross width; slim spice/tech niche takes remaining 6.5. These
  SHARE the same enclosure, not an additional shelf in the main-fridge swing area.
- Coffee sizing reference: DeLonghi Dedica Arte EC885M, manufacturer-listed 5.9W x 13D
  x 12H inches. Compact brushed-metal machine, stored behind flush front. Tray has
  approximately 14-inch full extension so machine is brought clear of its housing for
  use, front open. Final runners, cable movement and operating clearances unverified.
  Source: https://www.delonghi.com/en-us/ec885m-dedica-arte/p/EC885M
- Spice/tech side niche: two small spice ledges above a lower charging/speaker cubby.
  No extra drawer above the wine fridge and no separate projecting wall shelf.
- Italy map: 18 x 24 inches INCLUDING frame, flat on wall above cabinet, approx 57–81 AFF.
- Above-dishwasher counter remains fully usable and has NO coffee garage or machine.

Nominal screening: manufacturer 33-inch forward envelope from an installed front at
24–25.5 gives a 57–58.5 extent; candidate unit starts 61.5. Resulting 3–4.5 inches is
only a nominal separation before room uncertainty/trim/handles. It is NOT installation
approval. Wine handing/rack extraction, actual freezer drawer travel, working/standing
space and simultaneous opening remain unverified. Operate one pull-out at a time in
the concept; do not show impossible simultaneous openings.

The video can use this coherent nominal design after returned-image review. For an
actual renovation, physical measurements and manufacturer installation details still
govern. Full kitchen angle propagation follows the chosen end-wall concept.

### R1. HISTORICAL CORNER WORKAROUND — WITHDRAWN WITH TOWER

The added end-wall unit blocks front access to the first 24 inches of Run B. Revise
that 66-inch pre-sink segment to 24-inch blind/fixed return + 3-inch filler + 24-inch
microwave bay + 15-inch base. Microwave moves to plan x27–51, still left of sink x66–99.
DW remains x99–123 and its entire countertop stays clear. Do not draw working front
drawers behind the wine unit. With wine body ending x24 this gives 3 inches nominal
lateral separation to microwave bay. Coffee tray extends to about x38, so open tray,
wine door and microwave share operating space. They are NOT demonstrated safe to
open together; film inserts operate them separately.

Upper 18-inch unit: after three illustrative 3/4-inch side/divider panels, total clear
width is 15.75 inches. Allocate approximately 10 clear to coffee and 5.75 clear to the
spice/tech side. Gross 11.5/6.5 labels are zones, not usable internal clearances. Keep
tech items compact and staggered in depth; do not invent a side pull-out in the wine
appliance's ventilation/cutout allowance. Mechanical hardware remains a build detail.

## S. TWO-SURFACE RESET — 2026-10-09

1. Blank end wall beside main fridge: only the flush wine fridge; no protruding tower,
   no artwork, no spice/electronics assembly. Bosch main-fridge candidate retains
   intended right upper hinge and bottom freezer drawer; dimensions remain provisional.
2. Kitchen-side wall left of sink, near built-in microwave: spice/tech nook with tidy
   jars, charging and compact smart device, following the user's original placement.
   Keep this separate from the wine-fridge wall in directing instructions.
3. Coffee garage: UNRESOLVED. Proposed next location is flush within the sink-side wall
   above the microwave-side worktop, below the spice/tech nook, so no permanent cabinet
   sits on the counter. This is a proposal for user location selection, not a locked
   design or evidence of a feasible recess. Above-dishwasher placement stays rejected.

Return to approved finishes: concrete with dining rug, no wooden floor lamp, white
Shaker/frosted uppers and warm lights, Wolf/red knobs and pale hood, red SMEG, refined
faucet and single basin, flowers/fruit, sink-side built-in microwave. Do not inherit
the rejected tower, poster or forced microwave shift from the last render.
