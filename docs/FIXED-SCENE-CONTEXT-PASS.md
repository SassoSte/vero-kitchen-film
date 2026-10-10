# Fixed-scene context/material pass — 2026-10-10

[Current v3 render](../outputs/review/kitchen-fixed-materials-v3.png) · [HDR](../outputs/review/kitchen-fixed-materials-v3.exr) · [Scene receipt](../outputs/review/kitchen-fixed-materials-v3-scene.json) · [Source](../tools/render_fixed_scene.py)

User authorized continuing from the local fixed-geometry material study. No media-provider calls or paid credits. Local Mitsuba3.9.1 scalar path tracing,1200×679,512 samples/pixel, two threads; final288.19 seconds. Observed~199% CPU and~162MB resident. Process exited; no server.

## Changes and inspection

Restored left doorway and right dining-room context as approximate modeled architecture. Added wood dining table, rug, four chairs and pendant; rounded/tapered upholstery forms on three bar stools and explicit chair/stool back supports. Improved small-appliance body profiles, metal treatment and branding detail. Dining artwork is UV-sampled directly from existing apartment-v7.png into two wall rectangles; source pixels/files are not changed, and no new artwork was invented. Original raster stays byte-identical. These are approximate contextual/modeling choices, not a verified reconstruction of all furnishings.

Initial high-sample v2 exposed a context error: hallway rear wall occluded left part of fridge and intersected its handle envelope. V2 is preserved as a **failed context draft**, not a candidate. Corrected hallway placement, added an intersection guard against fridge envelope, inspected small preview and rerendered v3. One intermediate owned process was terminated to finish support geometry before final render. Final image shows both fridge doors and the original camera framing; no visible hallway blockage. No paid retries occurred.

Verified current scene against v1 receipt: camera parameters and core case/door/freezer, both enclosure panels, over-fridge cabinet, bar wall and bar cap bounding volumes unchanged. Separate scene guard prevents contextual boxes intruding into refrigerator/handle envelope. Rendered scene uses true geometry and light transport; no generative whole-frame edit.

## Limits and next state

This is a **model-based review image**, not a user-approved third production view or a certified architectural photograph. Camera/opening uncertainty from the geometry study remains (fitted87.7-inch opening vs old66-inch bar schedule). Context doorway/dining placement is approximate; detailed furnishings/appliance assets are procedural rather than exact manufacturer models. Some sampling grain and simplified detail remain. Hinge sweep, services and actual installation clearance remain unverified. Do not modify user-locked north/east or west images automatically.

No new credits spent; task ledger remains295.75/296. The fixed geometry is ready for user review and targeted local refinement; third-view approval and final production readiness remain open.

Reproduce using the pinned environment from FIXED-SCENE-MATERIAL-PASS.md:

```sh
/tmp/vero-render-runtime/bin/python tools/render_fixed_scene.py --width 1200 --spp 512 --name kitchen-fixed-materials-v3
```

Use a new output name for future reviewed versions. Preview files are in `/tmp/vero-fixed-render/previews`. V2 is historical failure, v3 the current local candidate.
