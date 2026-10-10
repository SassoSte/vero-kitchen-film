# Local fixed-scene material pass — 2026-10-10

[Rendered checkpoint](../outputs/review/kitchen-fixed-materials-v1.png) · [HDR render](../outputs/review/kitchen-fixed-materials-v1.exr) · [Scene/receipt](../outputs/review/kitchen-fixed-materials-v1-scene.json) · [Reproducible script](../tools/render_fixed_scene.py)

User authorized continuing from fixed geometry. No paid media provider used. Installed isolated Mitsuba3.9.1 runtime under `/tmp/vero-render-runtime` using local Python3.13 and pinned [requirements](../tools/fixed-render-requirements.txt); no system application installed. Official runtime reference: https://mitsuba.readthedocs.io/en/stable/ . Preview files/cache under `/tmp/vero-fixed-render` are disposable, not final assets.

## What was rendered

Deterministic path tracing at1200×679,768 samples/pixel, two requested CPU threads, seed2130. Final pass324.32 seconds. Observed process~197% CPU,72–120MB resident; exited. No localhost server or ongoing job. Added bevelled mesh fronts, cylinders/ellipsoids, procedural oak/stone/concrete textures, painted cabinet frames, rough glass, metal reflections, practical lights, bar ribs and three simple stools. Photographic source pixels were not composited or edited. HDR source retained; display PNG uses documented ACES-style tone curve and sRGB conversion.

Fixed fridge case35.6×28.5×68.3, front36×70, separate4.8-inch door thickness and protruding handles. Enclosure panels0.75×28.875×84, upper cabinet underside71/top84, narrow base13.5 and original range start57. Verified geometry records against these values and reused prior estimated camera unchanged. Foreground bar occludes freezer through actual geometry, not painted shadows.

## Honest result and limitations

This is a **material/lighting checkpoint**, not the requested finished professionally photographed apartment image. Metallic volume is now deterministic, but metal exposure remains bright, some noise persists, stools/SMEG forms are procedural approximations rather than faithful product models, glass cupboards have no finished contents, and dining-room context is omitted. Lighting is an illustrative studio/practical setup, not reconstructed measured luminaires. Do not replace any user-locked design image or call architectural fidelity solved.

Camera/opening uncertainty from FIXED-GEOMETRY-CHECK remains: fitted opening87.7 inches conflicts with old66-inch bar schedule; manual anchors taken from an AI-generated view, not a calibrated photograph. No true room survey, full hinge-sweep or operational clearance model. Full photoreal finalization still needs reconciled dimensions/camera and faithful asset/detail work. No claim of construction approval.

Task cost remains295.75/296. Source photos/plans and two user-locked raster files unchanged. Third production view remains unapproved; no additional paid generation authority inferred.

## Reproduce

```sh
uv venv --python /opt/homebrew/bin/python3.13 /tmp/vero-render-runtime
uv pip install --python /tmp/vero-render-runtime/bin/python -r tools/fixed-render-requirements.txt
/tmp/vero-render-runtime/bin/python tools/render_fixed_scene.py --width 1200 --spp 768 --name kitchen-fixed-materials-v1
```

The script generates its own intermediate meshes/textures in `/tmp/vero-fixed-render`; they can be rebuilt from source. Use a new output name for future reviewed versions. Current script does not overwrite source images.
