"""02B END: move partner down onto the range-bay floor (return placed him ~95 px high
relative to the plate), keep lead in place and on top. Local, unpaid."""
import cv2
import numpy as np
comp = cv2.imread('outputs/construction/raw/02B-end-v2-composite.png').astype(np.float32)
plate = cv2.imread('outputs/construction/stage-02-bases.png').astype(np.float32)
pm = cv2.imread('outputs/construction/raw/02B-end-v2-composite-personmask.png', 0) > 0
H, W = pm.shape
def poly(p):
    m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [np.array(p, np.int32)], 1); return m > 0
leadpoly = poly([[1875, 380], [2688, 380], [2688, 1520], [1745, 1520], [1752, 1000], [1845, 900], [1862, 780]])
lead = pm & leadpoly
par = pm & ~leadpoly
n, lab, st, _ = cv2.connectedComponentsWithStats(par.astype(np.uint8))
par = lab == (1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])))
DY = 95
base = comp.copy(); g = cv2.dilate(par.astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
base[g] = plate[g]
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
base *= (1 - 0.3 * np.exp(-(((xx - 1630) / 150) ** 2 + ((yy - 1475) / 18) ** 2)))[..., None]
M = np.float32([[1, 0, 0], [0, 1, DY]])
layer = cv2.warpAffine(comp, M, (W, H))
a = cv2.GaussianBlur(cv2.warpAffine(par.astype(np.float32), M, (W, H)), (0, 0), 1)[..., None]
out = base * (1 - a) + layer * a
# residue of the unmoved partner (thin sliver by the lead's shoulder; floor smear)
clean = (poly([[1855, 470], [1900, 470], [1900, 760], [1855, 760]]) | poly([[1420, 1400], [1560, 1400], [1560, 1520], [1420, 1520]]) | poly([[1420, 1440], [1500, 1440], [1500, 1510], [1420, 1510]])) & ~(a[..., 0] > 0.05)
out[clean] = plate[clean]
al = cv2.GaussianBlur(lead.astype(np.float32), (0, 0), 1)[..., None]
out = out * (1 - al) + comp * al
cv2.imwrite('outputs/construction/raw/02B-end-v2-final.png', np.clip(out, 0, 255).astype(np.uint8))
