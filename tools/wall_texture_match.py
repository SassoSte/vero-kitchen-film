"""Give smooth generated wall areas inside a mask the plaster texture and tone of the
selected view's walls. usage: wall_texture_match.py COMP MASK OUT [seed] [WALL_POLYS_JSON]
Only flat (low local variance) masked pixels change; fixtures/edges are left alone."""
import sys
from pathlib import Path
import cv2
import numpy as np

R = Path(__file__).resolve().parents[1]
comp = cv2.imread(sys.argv[1]).astype(np.float32); mask = cv2.imread(sys.argv[2], 0) > 0
master = cv2.imread(str(R / 'outputs/keyframes/kitchen-smeg-enclosure-v2.png')).astype(np.float32)
H, W = comp.shape[:2]; rng = np.random.default_rng(int(sys.argv[4]) if len(sys.argv) > 4 else 7)
src = master[150:1150, 1010:1280]
P, step = 240, 170
tex = np.zeros((H, W, 3), np.float32); ws = np.zeros((H, W, 1), np.float32)
win = np.outer(np.hanning(P), np.hanning(P)).astype(np.float32)[..., None] + 1e-3
for y in range(-60, H, step):
    for x in range(-60, W, step):
        sy, sx = rng.integers(0, src.shape[0] - P), rng.integers(0, src.shape[1] - P)
        pa = src[sy:sy + P, sx:sx + P][:, ::(-1 if rng.random() < .5 else 1)]
        y0, x0, y1, x1 = max(y, 0), max(x, 0), min(y + P, H), min(x + P, W)
        tex[y0:y1, x0:x1] += (pa * win)[y0 - y:y1 - y, x0 - x:x1 - x]; ws[y0:y1, x0:x1] += win[y0 - y:y1 - y, x0 - x:x1 - x]
tex /= ws
detail = tex - cv2.GaussianBlur(tex, (0, 0), 40)
g = cv2.cvtColor(comp.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
var = cv2.GaussianBlur(g * g, (0, 0), 4) - cv2.GaussianBlur(g, (0, 0), 4) ** 2
flat = mask & (var < 12) & (g > 150)
if len(sys.argv) > 5:
    import json
    wm = np.zeros((H, W), np.uint8)
    for poly in json.loads(sys.argv[5]):
        cv2.fillPoly(wm, [np.array(poly, np.int32)], 1)
    flat &= wm > 0
flat = cv2.morphologyEx(flat.astype(np.uint8), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8)) > 0
# tone: per-channel gain toward the wall just outside the mask (low-frequency field)
ring = (cv2.dilate(mask.astype(np.uint8), np.ones((41, 41), np.uint8)) > 0) & ~mask & (g > 150)
w = ring.astype(np.float32)
num = cv2.GaussianBlur(comp * w[..., None], (0, 0), 120); den = cv2.GaussianBlur(w, (0, 0), 120)[..., None] + 1e-4
target = num / den
wf = flat.astype(np.float32)
cur = cv2.GaussianBlur(comp * wf[..., None], (0, 0), 120) / (cv2.GaussianBlur(wf, (0, 0), 120)[..., None] + 1e-4)
gain = np.clip(target / (cur + 1), 0.85, 1.15)
out = comp.copy()
a = cv2.GaussianBlur(flat.astype(np.float32), (0, 0), 3)[..., None] * mask[..., None]
out = out * (1 - a) + (comp * gain + detail) * a
cv2.imwrite(sys.argv[3], np.clip(out, 0, 255).astype(np.uint8))
print({'flat_px': int(flat.sum())})
