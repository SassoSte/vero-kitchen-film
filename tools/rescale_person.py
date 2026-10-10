"""Rescale one composited person about a floor anchor; background from the plate.
usage: rescale_person.py COMP PERSONMASK PLATE OUT x0 x1 anchor_x anchor_y scale
Selects person-mask pixels with x0<=x<x1, removes them (plate shows through),
scales them by `scale` about (anchor_x, anchor_y) and pastes them back."""
import sys
import cv2
import numpy as np
comp, pm, plate = cv2.imread(sys.argv[1]).astype(np.float32), cv2.imread(sys.argv[2], 0) > 0, cv2.imread(sys.argv[3]).astype(np.float32)
out = sys.argv[4]; x0, x1, ax, ay = map(int, sys.argv[5:9]); s = float(sys.argv[9])
H, W = pm.shape
sel = pm.copy(); sel[:, :x0] = False; sel[:, x1:] = False
y0lim = int(sys.argv[12]) if len(sys.argv) > 12 else 0
sel[:y0lim] = False
d = np.abs(cv2.GaussianBlur(comp, (0, 0), 2) - cv2.GaussianBlur(plate, (0, 0), 2)).max(2)
gray = cv2.cvtColor(comp.astype(np.uint8), cv2.COLOR_BGR2GRAY)
core = (d > 35) & sel & (gray < 165)
core = cv2.morphologyEx(core.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(core)
core = lab == (1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))) if n > 1 else core > 0
cnts, _ = cv2.findContours(core.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
f = np.zeros((H, W), np.uint8); cv2.drawContours(f, cnts, -1, 1, -1)
sel = (cv2.dilate(f, np.ones((5, 5), np.uint8)) > 0) & sel
base = comp.copy(); grow = cv2.dilate(sel.astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
base[grow] = plate[grow]
if len(sys.argv) > 10 and sys.argv[10] == 'clean':          # whole column band back to plate
    yb = int(sys.argv[11]) if len(sys.argv) > 11 else 0
    base[yb:, x0:x1] = plate[yb:, x0:x1]
M = np.float32([[s, 0, ax * (1 - s)], [0, s, ay * (1 - s)]])
layer = cv2.warpAffine(comp, M, (W, H), flags=cv2.INTER_LANCZOS4)
a = cv2.warpAffine(sel.astype(np.float32), M, (W, H), flags=cv2.INTER_LINEAR)
a = cv2.GaussianBlur(a, (0, 0), 1.0)[..., None]
# soft contact shadow under the scaled feet
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
fw = max(40, int(220 * s))
sh = np.exp(-(((xx - ax) / fw) ** 2 + ((yy - ay) / (fw * 0.18)) ** 2))
base = base * (1 - 0.35 * sh[..., None])
res = base * (1 - a) + layer * a
cv2.imwrite(out, np.clip(res, 0, 255).astype(np.uint8))
print({'moved_px': int(sel.sum()), 'scale': s})
