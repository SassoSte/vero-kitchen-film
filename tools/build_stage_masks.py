"""B07 stage-plate edit masks on the selected MASTER view (kitchen-smeg-enclosure-v2).

White = may change. Everything else is re-composited from MASTER after any paid edit
(tools/stage_composite.py), so room, camera and unchanged features cannot drift.
"""
import json
from pathlib import Path
import cv2
import numpy as np

R = Path(__file__).resolve().parents[1]
MASTER = R / 'outputs/keyframes/kitchen-smeg-enclosure-v2.png'
OUT = R / 'outputs/production/masks'
H, W = cv2.imread(str(MASTER)).shape[:2]

REGIONS = {
    # shot-03 state: no backsplash/uppers/hood/pot filler/range/toaster/kettle,
    # old freestanding fridge with bare wall, north niche unfinished, sink not seated
    'plate-03': {
        'east wall above worktop, hood, uppers, pot filler, kettle': [[1490, 0], [2688, 0], [2688, 1045], [2600, 1005], [1800, 885], [1500, 885]],
        'fridge + enclosure -> old fridge, bare wall': [[1262, 0], [1520, 0], [1520, 1400], [1262, 1400]],
        'range -> empty opening': [[1540, 840], [1830, 840], [1830, 1520], [1540, 1520]],
        'north coffee/wine niche -> unfinished opening': [[600, 185], [1005, 185], [1005, 1305], [600, 1305]],
        'west sink -> empty cutout': [[0, 925], [315, 925], [315, 1075], [0, 1075]],
    },
    # 03A: workers + cooking-run quartz right of the range opening, plus floor they stand on
    '03A-action': {
        'right cooking-run worktop and workers': [[1800, 700], [2688, 760], [2688, 1520], [900, 1520], [900, 950], [1500, 860]],
    },
}

OUT.mkdir(parents=True, exist_ok=True)
summary = {}
for name, polys in REGIONS.items():
    m = np.zeros((H, W), np.uint8)
    for pts in polys.values():
        cv2.fillPoly(m, [np.array(pts, np.int32)], 255)
    cv2.imwrite(str(OUT / f'{name}-mask.png'), m)
    summary[name] = {'regions': list(polys), 'fraction': round(float((m > 0).mean()), 4)}
(OUT / 'masks.json').write_text(json.dumps({'master': str(MASTER.relative_to(R)), 'masks': summary}, indent=2) + '\n')
print(json.dumps(summary, indent=1))
