"""Like stage_composite.py, but matches the return's low-frequency tone to the base
locally (normalized convolution from a ring outside the mask) and feathers wider.
For flat surfaces (stone, plaster) where a single global gain leaves visible blocks.
usage: tone_blend_composite.py BASE RETURNED MASK OUT [feather_px] [sigma]"""
import sys
import cv2
import numpy as np
base = cv2.imread(sys.argv[1]).astype(np.float32); ret = cv2.imread(sys.argv[2])
mask = cv2.imread(sys.argv[3], 0) > 0; out = sys.argv[4]
fe = float(sys.argv[5]) if len(sys.argv) > 5 else 24; sg = float(sys.argv[6]) if len(sys.argv) > 6 else 30
H, W = mask.shape
ret = cv2.resize(ret, (W, H), interpolation=cv2.INTER_LANCZOS4) if ret.shape[:2] != (H, W) else ret
keep = (~cv2.dilate(mask.astype(np.uint8), np.ones((41, 41), np.uint8)).astype(bool)).astype(np.uint8) * 255
orb = cv2.ORB_create(6000)
k1, d1 = orb.detectAndCompute(cv2.cvtColor(base.astype(np.uint8), cv2.COLOR_BGR2GRAY), keep)
k2, d2 = orb.detectAndCompute(cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY), keep)
m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1), key=lambda x: x.distance)[:1500]
Hm, _ = cv2.findHomography(np.float32([k2[x.queryIdx].pt for x in m]), np.float32([k1[x.trainIdx].pt for x in m]), cv2.RANSAC, 3.0)
al = cv2.warpPerspective(ret, Hm, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)
# per-pixel low-frequency gain: base/al measured on the ring, spread into the mask
ring = (cv2.dilate(mask.astype(np.uint8), np.ones((61, 61), np.uint8)) > 0) & ~mask
w = ring.astype(np.float32)
def nc(img): return cv2.GaussianBlur(img * w[..., None], (0, 0), sg) / (cv2.GaussianBlur(w, (0, 0), sg)[..., None] + 1e-4)
gain_ring = (nc(base) + 1) / (nc(al) + 1)
# spread further with a bigger kernel where the small one has no support
wide = (cv2.GaussianBlur(base * w[..., None], (0, 0), sg * 4) + 1) / (cv2.GaussianBlur(al * w[..., None], (0, 0), sg * 4) + 1)
sup = np.clip(cv2.GaussianBlur(w, (0, 0), sg) * 6, 0, 1)[..., None]
gain = np.clip(gain_ring * sup + wide * (1 - sup), 0.75, 1.3)
fixed = al * gain
a = np.clip(cv2.distanceTransform(mask.astype(np.uint8), cv2.DIST_L2, 5) / fe, 0, 1)[..., None]
res = np.where(mask[..., None], a * fixed + (1 - a) * base, base)
cv2.imwrite(out, np.clip(res, 0, 255).astype(np.uint8))
print({'protected_changed': int((np.clip(res, 0, 255).astype(np.uint8)[~mask] != base.astype(np.uint8)[~mask]).any(-1).sum())})
