"""Transfer only the illumination change of a registered return onto a base frame:
out = base * smooth(ret)/smooth(base). Geometry/texture stay the base's exactly.
usage: relight_transfer.py BASE RETURNED OUT [sigma]"""
import sys
import cv2
import numpy as np
base = cv2.imread(sys.argv[1]).astype(np.float32); ret = cv2.imread(sys.argv[2])
sg = float(sys.argv[4]) if len(sys.argv) > 4 else 12
H, W = base.shape[:2]
ret = cv2.resize(ret, (W, H), interpolation=cv2.INTER_LANCZOS4) if ret.shape[:2] != (H, W) else ret
orb = cv2.ORB_create(8000)
k1, d1 = orb.detectAndCompute(cv2.cvtColor(base.astype(np.uint8), cv2.COLOR_BGR2GRAY), None)
k2, d2 = orb.detectAndCompute(cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY), None)
m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1), key=lambda x: x.distance)[:2000]
Hm, st = cv2.findHomography(np.float32([k2[x.queryIdx].pt for x in m]), np.float32([k1[x.trainIdx].pt for x in m]), cv2.RANSAC, 3.0)
al = cv2.warpPerspective(ret, Hm, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)
g = (cv2.GaussianBlur(al, (0, 0), sg) + 2) / (cv2.GaussianBlur(base, (0, 0), sg) + 2)
cv2.imwrite(sys.argv[3], np.clip(base * np.clip(g, 0.3, 1.3), 0, 255).astype(np.uint8))
print({'inliers': int(st.sum())})
