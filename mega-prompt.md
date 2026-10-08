# Kitchen remodel construction film — production brief

Create a photorealistic 60-second construction film of the kitchen at 14145 N 92nd St
#2130, Scottsdale AZ 85260 (The Allison Condominiums, «Tallbot» 2B2B, 1,029 sqft).
Reference photographs and dimensioned blueprints are in this repo — use them as
ground truth. Produce one consistent kitchen across every viewpoint and stage.

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
strip-out; it must not appear in the finished kitchen. The original smoothtop range
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

The wall behind the fridge bay is the **building envelope wall** — exterior stucco beyond.
Recessing a wine fridge into it is structurally infeasible. A base-cabinet-depth wine
fridge on Run A (the interior partition wall) or integrated into Run B cabinetry is the
practical alternative. If the design requires a wall recess, flag this conflict before
any footage is generated.

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
- Modern deep undermount sink, slim pull-down faucet, soap dispenser on Run B
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
- Compact sleek espresso machine: clean modern lines, brushed stainless and matte
  dark accents, no ornate boiler, finial, exposed clock-like dial or decorative chrome
  tower. It sits on the LOWER kitchen-side counter directly above the dishwasher on
  Run B, tucked behind the left opening pier/raised ledge from the apartment camera.
  It must NOT be visible in the apartment-facing final reveal, and must never sit on
  the bar cap. It can be visible from the sink/cooking-side views that establish its
  proper location. Two small cups may sit beside it within that concealed station.
- Remove the tall wooden floor lamp/sculptural light with brown vertical rods and
  circular discs from the living-room foreground. Keep the kitchen ceiling lights.
- One tasteful vase of fresh flowers, with a restrained white/cream arrangement and
  natural greenery, toward one end of the apartment-facing bar. Keep the faucet,
  opening, hood, and cooking wall readable.
- One elegant low fruit bowl with a modest arrangement of fresh fruit on the bar,
  separated from the flowers. Preserve clear counter space and three usable stool
  positions. Flowers and fruit bowl are mandatory finished-design elements.
- Original over-the-range microwave removed; no microwave in the finished design
- Light-oak vertical/ribbed treatment on the apartment-facing bar front
- Three cream upholstered counter-height stools with slim legs/footrails,
  credible spacing, feet resting on the floor
- Restrained artwork/decor on an available wall surface

Do not add: floating shelves, wall-mounted wine racks, a countertop microwave, an island,
wall-to-wall carpet, oak flooring, the rejected wooden floor lamp, or an ornate
espresso machine.

## E. WINE-FRIDGE REQUIREMENT

The west end wall cannot accommodate a wall-recessed wine fridge (see Section B). If the
design includes one, place it as a base-cabinet-unit on Run A or Run B. Before rendering,
verify the appliance's actual dimensions and the available bay width. A generated
refrigerator-door opening is an animation, not proof of clearance.

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
| 04 | 00:15–00:20 | Sink run (REF-B) | Sink/worktop assembly seated on the sink run, then faucet fitting. Preserve DW, ledge, opening, apartment beyond. | `outputs/shots/04_sink_install.mp4` |
| 05 | 00:20–00:25 | Master | Separate beats with time jump: backsplash fitting, then upper-cabinet fastening. Shaker doors and glass inserts visible. | `outputs/shots/05_backsplash_uppers.mp4` |
| 06 | 00:25–00:31 | Master | Separate actions with time jumps: hood fitting, pot-filler fastening to backsplash, then Wolf range placement beneath hood. No microwave returns. | `outputs/shots/06_cooking_equipment.mp4` |
| 07 | 00:31–00:35 | Master incl. real corner | Remove old fridge, place new one in the same 33″ bay. | `outputs/shots/07_fridge_replacement.mp4` |
| 08 | 00:35–00:39 | Cooking-wall view | Worker installs and tests interior-cabinet and continuous undercabinet lighting. Illuminated backsplash clearly visible. Lighting stays ON for the rest of the film. | `outputs/shots/08_lighting_install.mp4` |
| 09 | 00:39–00:44 | Supported viewpoint | Wall-finish work and artwork hanging. If the wine-fridge base-cabinet design is locked: workers install it here. Preserve the west corner. | `outputs/shots/09_wall_finish_and_wine.mp4` |
| 10 | 00:44–00:49 | Apartment-facing (original REF-H) | Both workers position and secure the oak bar-front treatment. Preserve opening, counter, faucet, room boundaries. All lighting stays on. | `outputs/shots/10_bar_front.mp4` |
| 11 | 00:49–00:55 | Apartment-facing + inserts | Three cream stools carried in and positioned by workers. Red SMEG toaster and kettle, sleek concealed espresso station with two cups, fresh flowers, fruit bowl, and dining rug placed through separate short action inserts. End with visible positioning work, not prolonged wiping. | `outputs/shots/11_stools_and_staging.mp4` |
| 12 | 00:55–00:57 | Widest original kitchen angle | Complete reveal: both runs, all boundaries, all completed features including SMEG appliances, sleek concealed espresso station, flowers, and fruit bowl. Interior/undercabinet/hood lighting on. | `outputs/shots/12_reveal.mp4` |
| 13 | 00:57–01:00 | Apartment-facing | Final reveal: complete opening, finished bar with flowers and fruit bowl, three stools, sink faucet, cooking wall; retain SMEG appliances and sleek concealed espresso station in their established positions. Restrained camera move allowed if geometry is preserved. | `outputs/shots/13_final_reveal.mp4` |

Output format: 1920×1080, 24 fps, H.264 with AAC audio (construction sounds only — no
speech, music, subtitles, or overlays). Final film: `outputs/kitchen_remodel_60s.mp4`.
Shotlist: `outputs/shotlist.html`. Inspection record: `outputs/inspection.txt`.

## I. CONTINUITY RULES

Once installed, a feature stays installed. Specifically:
- The sink stays on Run B; a second sink never appears on Run A
- The Wolf range stays beneath the hood and pot filler after Shot 06
- The microwave is removed in Shot 01 and never returns
- The refrigerator changes only during Shot 07
- Cabinet-interior and undercabinet lighting stay on after Shot 08 through the final frame
- The three stools arrive through worker actions in Shot 11 and remain afterward
- SMEG appliances, sleek concealed espresso machine and two cups, vase/flowers, and fruit bowl
  are staged by the end of Shot 11 and remain unchanged through Shots 12–13. Preserve
  their positions and appearance across cuts; do not clutter the worktops.
- Cabinet arrangement, hardware, stone surfaces, appliance positions, and floor boundaries
  remain consistent across all shots

The final 20 seconds must contain actual installation and furnishing progress until second 55.
Worker presence alone is insufficient.

## J. INSPECT THE EXPORTED FILM

Watch the complete exported film and inspect every cut against the actual returned frames:

- Shots 03/04/06: correct cooking-run vs sink-run assignment
- Shot 06 onward: selected Wolf range beneath the mandatory hood; no microwave
- Shots 07/09/13: same refrigerator position, real corner, supported wine-fridge geometry
- Shots 08/10/11/12/13: same interior-cabinet, undercabinet, and hood lighting
- Shots 10/11/13: same bar, faucet, three stools, opening, apartment-facing geometry
- Shots 11–13: all final countertop styling present by second 55; stable SMEG
  appliances, sleek concealed espresso machine/two cups, flowers/vase, and fruit bowl. Verify
  their correct placement across the two reveal angles and usable counter/stool space.
  Espresso is visible only from kitchen-side views, concealed in apartment-facing view.
- Final views: continuous concrete floor, dining-area rug, no wooden floor lamp.
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
film production. Omit the optional wine fridge until its model and bay are locked.

## N. DESIGN REVISION — CONCRETE AND CONCEALED COFFEE STATION

The user rejected the wooden floor lamp, carpet floor and ornate espresso machine.
This revision supersedes those features in all earlier candidate images, shotlist
prompts and motion proofs. Preserve old assets as drafts; invalidate their final-design
acceptance. Concrete extends across visible kitchen/living/dining, with a dining rug;
the oak bar-front treatment remains. The sleek espresso machine is over the dishwasher
on the lower work counter and hidden from the apartment-facing camera. No new motion
until the revised reference views agree.
