"""MASTER-view cumulative states for shots 04-06 (local, unpaid).
stage-03 plate + selected-view pixels added element by element:
sink (04) -> stone backsplash cut around future uppers (05A) -> uppers (05B)
-> hood (06A) -> pot filler (06B) -> range (06C). Toaster/kettle stay off until 11."""
import json
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]
rd = lambda p: cv2.imread(str(R / p)).astype(np.float32)
plate = rd('outputs/construction/stage-03-plate.png')
master = rd('outputs/keyframes/kitchen-smeg-enclosure-v2.png')
stone = rd('outputs/construction/master-stone-clean.png')
E = json.loads((R / 'outputs/production/masks/east-regions.json').read_text())
H, W = plate.shape[:2]
def poly(p):
    a = np.zeros((H, W), np.uint8); cv2.fillPoly(a, [np.array(p, np.int32)], 1); return a > 0
def put(base, src, m, s=1.5):
    a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), s)[..., None]; return base * (1 - a) + src * a
sink = poly([[0, 925], [315, 925], [315, 1075], [0, 1075]])
uppers = poly(E['uppers_glass']) | poly(E['uppers_right'])
rng = poly(E['range'])
splash = poly([[1713, 0], [2688, 0], [2688, 965], [2190, 888], [1713, 820]]) & ~uppers & ~rng & ~poly(E['grate'])
hood, pot = poly(E['hood']), poly(E['potfiller'])
s04 = put(plate, master, sink)
s05a = put(s04, stone, splash)
# grate band above the worktop: continue the stone downward from 110 px above
gb = poly(E['grate']) & poly([[1713, 0], [2688, 0], [2688, 965], [2190, 888], [1713, 820]])
s05a = put(s05a, cv2.warpAffine(stone, np.float32([[1, 0, 0], [0, 1, 110]]), (W, H), borderMode=cv2.BORDER_REFLECT), gb, 3)
s05b = put(s05a, stone, uppers)  # stone-clean has the glass upper's corner behind the hood
s06a = put(s05b, master, hood & ~uppers)
s06b = put(s06a, master, pot)
s06c = put(s06b, master, rng | poly(E['grate']))
for n, im in (('stage-04-master-done', s04), ('stage-05a-backsplash', s05a), ('stage-05b-uppers', s05b),
              ('stage-06a-hood', s06a), ('stage-06b-potfiller', s06b), ('stage-06c-range', s06c)):
    cv2.imwrite(str(R / f'outputs/construction/{n}.png'), np.clip(im, 0, 255).astype(np.uint8))
print('ok')
