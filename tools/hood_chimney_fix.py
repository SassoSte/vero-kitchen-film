"""View 1: the hood chimney carried the old mottled wall texture, so it read as plaster
next to the stainless canopy. Smooth it (edge-preserving guided filter) and give it the
canopy's cool brushed-stainless tone. Operates in place on kitchen-smeg-enclosure-v3.png
(local, unpaid); pixels outside the chimney polygon are untouched (asserted)."""
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]; f = R / 'outputs/keyframes/kitchen-smeg-enclosure-v3.png'
im = cv2.imread(str(f)).astype(np.float32); H, W = im.shape[:2]
m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [np.array([[1708, 0], [2152, 0], [2152, 203], [1708, 296]], np.int32)], 1)
def guided(I, p, r, eps):
    mean = lambda x: cv2.boxFilter(x, -1, (r, r))
    mI, mp = mean(I), mean(p); a = (mean(I * p) - mI * mp) / (mean(I * I) - mI * mI + eps); b = mp - a * mI
    return mean(a) * I + mean(b)
g = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
sm = np.stack([guided(g, im[..., c] / 255, 121, 0.004) * 255 for c in range(3)], -1)
canopy = im[232:250, 1880:2060].reshape(-1, 3).mean(0)          # stainless canopy top face
print('canopy BGR', canopy.round(1))
lum = sm.mean(2, keepdims=True)
steel = lum * (canopy / canopy.mean())                          # canopy hue, chimney's own shading
rng = np.random.default_rng(1)
brush = cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), sigmaX=0.6, sigmaY=18)[..., None] * 2.2
out = steel + brush
a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.0); a[a < 0.01] = 0; a = a[..., None]
res = np.clip(im * (1 - a) + out * a, 0, 255).astype(np.uint8)
far = cv2.dilate(m, np.ones((9, 9), np.uint8)) == 0
assert (res[far] == im.astype(np.uint8)[far]).all()
cv2.imwrite(str(f), res); print('ok')
