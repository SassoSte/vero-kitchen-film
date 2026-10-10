# Fixed-geometry perspective check — 2026-10-10

User authorized a plain shaded 3D check, with no paid generation. Built using `tools/build_camera_geometry_check.py`: deterministic NumPy ray/box intersections and light visibility, not a generated image or a source-photo edit.

## Deliverables

- [Estimated camera view](../outputs/review/kitchen-fixed-geometry-camera-v1.png)
- [Same-camera foreground cutaway](../outputs/review/kitchen-fixed-geometry-cutaway-v1.png)
- [Oblique volume diagnostic](../outputs/review/kitchen-fixed-geometry-volume-v1.png) — different camera only to inspect depth
- [Editable geometric scene OBJ](../outputs/review/kitchen-fixed-geometry-scene.obj), inches
- [Camera fit and anchor receipt](../outputs/review/kitchen-fixed-geometry-camera.json)

## Fixed dimensions

Refrigerator36W×70H, case28.5D, doors33.3D, handles35.7D plus1-inch rear gap. Enclosure side panels28.875 deep, upper underside71/top84; proposed43.5-inch fridge/enclosure allocation plus13.5 base preserves range start57 in123-inch run. Foreground bar43 high at nominal105-inch depth from rear kitchen wall. These retain prior manufacturer-based appliance numbers and provisional room schedule.

## What the model establishes within its assumptions

The doors/handles project beyond the enclosure and adjacent25.5-inch counter. The freezer and its handle are behind the foreground bar, and should be occluded in this frontal view. Sampled visibility on the refrigerator front centerline begins at approximately33.9 inches AFF; freezer-top20.6 and handle17 fall below that. This is ray-traced model occlusion, not real-world proof. Near-frontal view exposes little side depth; forcing broad visible side faces would change camera or geometry.

## Camera match limits — do not conceal

Ten manually approximated image anchors on generated apartment-continuity-v8 (opening and upper cabinet edges; refrigerator excluded). Mean reprojection error39.5px on2688-wide reference. Bounded eye height reaches66in and camera distance reaches nominal far edge of157-inch living span (rear-wall y262). Fitted opening width87.7in, conflicting with old66-inch bar schedule. Opening dimensions were never measured. Unconstrained trial preferred eye height~80in and rear-wall distance~331in, outside nominal room assumptions, further indicating source/image inconsistency. Those unconstrained settings were rejected for this deliverable.

Consequently this is an **estimated image alignment**, NOT a calibrated architectural match. Do not promote fitted opening width to authoritative plan or change originals. A measured opening width/bar height and camera/room evidence are needed to certify physical matching. Door-swing and drawer-removal geometry are omitted; no operating-clearance certification. Box geometry also omits fine bevels/hinges/handles curves. Shaded views intentionally omit decor/stools for visibility and are not new style proposals.

## State

No provider calls, no spending; task remains295.75/296. First two approved raster files unchanged. Third photoreal view remains unapproved. This scene provides fixed geometry for review and future controlled rendering; it does not fix the old generated image automatically. All rendering commands completed; no server started.
