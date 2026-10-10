"""Register a returned paid edit to its base frame and keep ONLY masked pixels.

usage: stage_composite.py BASE RETURNED MASK OUT
Outside the mask the result is byte-identical to BASE, so camera/room drift in the
provider return cannot reach the stage frame. Reports registration and the drift the
provider introduced outside the mask (for the review record). No network access.
"""
import hashlib, json, sys
from pathlib import Path
import cv2
import numpy as np

base_p, ret_p, mask_p, out_p = map(Path, sys.argv[1:5])
base = cv2.imread(str(base_p)); ret = cv2.imread(str(ret_p)); mask = cv2.imread(str(mask_p), 0) > 0
H, W = base.shape[:2]
ret = cv2.resize(ret, (W, H), interpolation=cv2.INTER_LANCZOS4) if ret.shape[:2] != (H, W) else ret

# Homography from features in the protected (unmasked) area only.
keep = (~cv2.dilate(mask.astype(np.uint8), np.ones((41, 41), np.uint8)).astype(bool)).astype(np.uint8) * 255
orb = cv2.ORB_create(6000)
g1, g2 = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY), cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)
k1, d1 = orb.detectAndCompute(g1, keep); k2, d2 = orb.detectAndCompute(g2, keep)
Hm, inl = None, 0
if d1 is not None and d2 is not None:
    m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1), key=lambda x: x.distance)[:1500]
    if len(m) >= 12:
        src = np.float32([k2[x.queryIdx].pt for x in m]); dst = np.float32([k1[x.trainIdx].pt for x in m])
        Hm, st = cv2.findHomography(src, dst, cv2.RANSAC, 3.0); inl = int(st.sum()) if st is not None else 0
aligned = cv2.warpPerspective(ret, Hm, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE) if Hm is not None else ret

prot = ~mask
drift_raw = float(np.abs(ret.astype(int) - base.astype(int))[prot].mean())
drift_reg = float(np.abs(aligned.astype(int) - base.astype(int))[prot].mean())
# colour match the returned region to base using a ring just outside the mask
ring = cv2.dilate(mask.astype(np.uint8), np.ones((31, 31), np.uint8)).astype(bool) & prot
gain = (base[ring].reshape(-1, 3).astype(float).mean(0) + 1) / (aligned[ring].reshape(-1, 3).astype(float).mean(0) + 1)
import os
if os.environ.get('STAGE_NO_GAIN'): gain = np.ones(3)
fixed = np.clip(aligned.astype(float) * gain, 0, 255)
# feather only inward so the protected area stays exact
inner = cv2.distanceTransform(mask.astype(np.uint8), cv2.DIST_L2, 5)
a = np.clip(inner / 8.0, 0, 1)[..., None]
out = np.where(mask[..., None], a * fixed + (1 - a) * base, base).astype(np.uint8)
assert (out[prot] == base[prot]).all()
cv2.imwrite(str(out_p), out)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
print(json.dumps({'base': str(base_p), 'returned': str(ret_p), 'mask': str(mask_p), 'output': str(out_p),
    'homography': None if Hm is None else np.round(Hm, 5).tolist(), 'ransac_inliers': inl,
    'protected_mean_abs_diff_raw': round(drift_raw, 2), 'protected_mean_abs_diff_registered': round(drift_reg, 2),
    'ring_colour_gain_bgr': np.round(gain, 4).tolist(), 'protected_pixels_changed': 0,
    'output_sha256': sha(out_p)}, indent=1))
