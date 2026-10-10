"""Translate one composited person (person-mask pixels inside a box) by (dx, dy);
uncovered pixels come from the plate. usage: shift_person.py COMP PM PLATE OUT x0 y0 x1 y1 dx dy"""
import sys
import cv2
import numpy as np
comp = cv2.imread(sys.argv[1]).astype(np.float32); pm = cv2.imread(sys.argv[2], 0) > 0
plate = cv2.imread(sys.argv[3]).astype(np.float32)
x0, y0, x1, y1, dx, dy = map(int, sys.argv[5:11]); H, W = pm.shape
sel = np.zeros_like(pm); sel[y0:y1, x0:x1] = pm[y0:y1, x0:x1]
if len(sys.argv) > 11:                          # optional polygon limit (JSON)
    import json
    lim = np.zeros((H, W), np.uint8); cv2.fillPoly(lim, [np.array(json.loads(sys.argv[11]), np.int32)], 1)
    sel &= lim > 0
base = comp.copy(); g = cv2.dilate(sel.astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
base[g] = plate[g]
M = np.float32([[1, 0, dx], [0, 1, dy]])
layer = cv2.warpAffine(comp, M, (W, H)); a = cv2.warpAffine(sel.astype(np.float32), M, (W, H))
a = cv2.GaussianBlur(a, (0, 0), 1.0)[..., None]
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
fx = (x0 + min(x1, x0 + 320)) / 2 + dx; fy = y1 + dy
sh = np.exp(-(((xx - fx) / ((x1 - x0) * 0.45)) ** 2 + ((yy - fy) / 22) ** 2))
base *= (1 - 0.3 * sh[..., None])
cv2.imwrite(sys.argv[4], np.clip(base * (1 - a) + layer * a, 0, 255).astype(np.uint8))
print({'moved_px': int(sel.sum())})
