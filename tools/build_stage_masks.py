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
    # shot-02 state on the stage-03 plate: all stone worktops off, cabinet boxes exposed
    'plate-02-worktops': {
        'west worktop, back ledge cap, sink cutout': [[0, 815], [205, 815], [205, 868], [490, 868], [490, 945], [0, 1435]],
        'narrow cabinet top': [[1486, 832], [1836, 826], [1836, 884], [1541, 908], [1486, 908]],
        'right cooking-run worktop + corner strip': [[1790, 826], [1840, 826], [2140, 893], [2688, 958], [2688, 1252], [1800, 1020], [1790, 1020]],
    },
    # shot-02 start state on stage-02-bases: no base cabinets or dishwasher yet
    'plate-02-bare': {
        'west base run + dishwasher': [[0, 815], [205, 815], [205, 868], [495, 868], [495, 1520], [0, 1520]],
        'narrow cabinet + right base run': [[1455, 880], [1486, 880], [1486, 826], [1840, 826], [2140, 880], [2688, 945], [2688, 1520], [1486, 1520], [1455, 1400]],
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
