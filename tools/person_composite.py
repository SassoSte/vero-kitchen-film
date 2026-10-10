"""Transfer only added people (plus their floor shadows and named contact areas)
from a registered paid return onto a fixed stage plate.

usage: person_composite.py PLATE RETURNED OUT BBOX_JSON
BBOX_JSON: {"bbox":[x0,y0,x1,y1], "contact":[[[x,y],...],...], "thr":22}
Everything outside the person mask/contact polygons is the plate, except a
multiplicative shadow ratio (<=1) inside the bbox. No network access.
"""
import hashlib, json, sys
from pathlib import Path
import cv2
import numpy as np

plate_p, ret_p, out_p, cfg = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), json.loads(sys.argv[4])
plate = cv2.imread(str(plate_p)); ret = cv2.imread(str(ret_p))
H, W = plate.shape[:2]
if ret.shape[:2] != (H, W): ret = cv2.resize(ret, (W, H), interpolation=cv2.INTER_LANCZOS4)
x0, y0, x1, y1 = cfg['bbox']
box = np.zeros((H, W), bool); box[y0:y1, x0:x1] = True
keep = (~cv2.dilate(box.astype(np.uint8), np.ones((61, 61), np.uint8)).astype(bool)).astype(np.uint8) * 255
orb = cv2.ORB_create(8000)
g1, g2 = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY), cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)
k1, d1 = orb.detectAndCompute(g1, keep); k2, d2 = orb.detectAndCompute(g2, keep)
m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1), key=lambda x: x.distance)[:2000]
src = np.float32([k2[x.queryIdx].pt for x in m]); dst = np.float32([k1[x.trainIdx].pt for x in m])
Hm, st = cv2.findHomography(src, dst, cv2.RANSAC, 2.5)
al = cv2.warpPerspective(ret, Hm, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
prot = keep > 0
diff_reg = float(np.abs(al.astype(int) - plate.astype(int))[prot].mean())
# colour match on protected area
gain = (plate[prot].reshape(-1, 3).astype(float).mean(0) + 1) / (al[prot].reshape(-1, 3).astype(float).mean(0) + 1)
alf = np.clip(al.astype(np.float32) * gain, 0, 255)
d = np.abs(cv2.GaussianBlur(alf, (0, 0), 2) - cv2.GaussianBlur(plate.astype(np.float32), (0, 0), 2)).max(2)
thr = np.full((H, W), float(cfg.get('thr', 22)), np.float32)
for poly, t in cfg.get('strict', []):            # e.g. stone the hands rest on
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); thr[c > 0] = t
pm = ((d > thr) & box).astype(np.uint8)
pm = cv2.morphologyEx(pm, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
pm = cv2.morphologyEx(pm, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, stats, _ = cv2.connectedComponentsWithStats(pm)
pm = np.isin(lab, [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] > cfg.get('min_area', 6000)])
# fill only small holes (texture dropouts); large holes are background between limbs
inv = (~pm).astype(np.uint8)
n, lab, stats, _ = cv2.connectedComponentsWithStats(inv)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
small = [i for i in range(1, n) if i not in border and stats[i, cv2.CC_STAT_AREA] < cfg.get('hole', 1500)]
pm |= np.isin(lab, small)
if cfg.get('saliency'):
    sal = cv2.imread(cfg['saliency'], 0).astype(np.float32) / 255
    sal = cv2.warpPerspective(sal, Hm, (W, H))       # saliency was computed on the raw return
    hull = cv2.morphologyEx(pm.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((61, 61), np.uint8)) > 0
    pm |= hull & (sal > cfg.get('sal_thr', 0.65)) & box
    pm |= (cv2.dilate(pm.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0) & (sal > 0.9) & box
for poly in cfg.get('contact', []):
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); pm |= c > 0
for poly, t in cfg.get('strict_final', []):     # e.g. an appliance behind a person
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); c = c > 0
    keep = c & (d > t)
    if cfg.get('saliency') and cfg.get('strict_final_sal'):
        _s = cv2.warpPerspective(cv2.imread(cfg['saliency'], 0).astype(np.float32) / 255, Hm, (W, H))
        keep &= _s > cfg['strict_final_sal']
    keep = cv2.morphologyEx(keep.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)) > 0
    pm = (pm & ~c) | (keep & pm)
for poly, t in cfg.get('solid', []):             # one person: largest blob of diff|saliency, holes filled
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); c = c > 0
    _s = cv2.warpPerspective(cv2.imread(cfg['saliency'], 0).astype(np.float32) / 255, Hm, (W, H))
    b = ((d > t) | ((_s > 0.5) & (d > cfg.get('solid_min_d', 15)))) & c
    b = cv2.morphologyEx(b.astype(np.uint8), cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, np.ones((21, 21), np.uint8))
    n, lab, st2, _ = cv2.connectedComponentsWithStats(b)
    blob = lab == (1 + int(np.argmax(st2[1:, cv2.CC_STAT_AREA]))) if n > 1 else b > 0
    cn, _ = cv2.findContours(blob.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    f = np.zeros((H, W), np.uint8); cv2.drawContours(f, cn, -1, 1, -1)
    pm = (pm & ~c) | (f > 0)
for poly in cfg.get('contact', []):                 # contact areas survive 'solid'
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); pm |= c > 0
for poly in cfg.get('exclude', []):
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); pm &= ~(c > 0)
ycc = cv2.cvtColor(al, cv2.COLOR_BGR2YCrCb)
skin = (ycc[..., 1] > 135) & (ycc[..., 1] < 180) & (ycc[..., 2] > 80) & (ycc[..., 2] < 135)
skin = cv2.morphologyEx(skin.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8)) > 0
for poly in cfg.get('skin_only', []):               # contact bands: keep hands, drop the rest
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1)
    pm &= ~((c > 0) & ~skin)
# local tone match: low-frequency gain plate/return measured on non-person pixels,
# spread by normalized convolution, so background riding inside the mask matches
core = cv2.dilate(((d > 40) & box).astype(np.uint8), np.ones((15, 15), np.uint8)) == 0
sg = cfg.get('tone_sigma', 20)
def nconv(img, w):
    return cv2.GaussianBlur(img * w, (0, 0), sg) / (cv2.GaussianBlur(w, (0, 0), sg) + 1e-4)
wv = core.astype(np.float32)
tm = alf.copy()
for ch in range(3):
    gch = nconv(plate[..., ch].astype(np.float32), wv) / (nconv(alf[..., ch], wv) + 1)
    tm[..., ch] = np.clip(alf[..., ch] * np.clip(gch, 0.7, 1.4), 0, 255)
# people (strong difference, and saliency if given) keep their own colour
person_core = cv2.dilate(((d > 40) & box).astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
if cfg.get('saliency'):
    person_core |= (sal > 0.8) & box
_y = cv2.cvtColor(al, cv2.COLOR_BGR2YCrCb)
person_core |= (_y[..., 1] > 135) & (_y[..., 1] < 180) & (_y[..., 2] > 80) & (_y[..., 2] < 135) & box
pw = cv2.GaussianBlur(person_core.astype(np.float32), (0, 0), 3)[..., None]
alf = alf * pw + tm * (1 - pw) if cfg.get('tone', True) else alf
# shadows: darkening ratio from the return, inside bbox, outside people
lp = lambda im: cv2.GaussianBlur(im.astype(np.float32), (0, 0), 6)
ratio = np.clip((lp(alf).mean(2) + 1) / (lp(plate).mean(2) + 1), 0.45, 1.0)
so = np.zeros((H, W), bool)
for poly in cfg.get('shadow_only', []):          # return's cast shadow: keep as soft darkening only
    c = np.zeros((H, W), np.uint8); cv2.fillPoly(c, [np.array(poly, np.int32)], 1); so |= c > 0
pm &= ~(so & (d < cfg.get('shadow_d', 40)))
sh = box & ~(cv2.erode(pm.astype(np.uint8), np.ones((11, 11), np.uint8)) > 0) & (ratio < 0.97) & ((np.mgrid[0:H, 0:W][0] > cfg.get('floor_y', 0)) | cv2.dilate(so.astype(np.uint8), np.ones((15, 15), np.uint8)).astype(bool))
ratio = np.where(sh, cv2.GaussianBlur(ratio, (0, 0), 4), 1.0)[..., None]
out = plate.astype(np.float32) * ratio
pm = cv2.erode(pm.astype(np.uint8), np.ones((cfg.get('erode', 1) * 2 + 1,) * 2, np.uint8)) > 0
a = np.clip(cv2.distanceTransform(pm.astype(np.uint8), cv2.DIST_L2, 5) / 2.0, 0, 1)[..., None]
out = out * (1 - a) + alf * a
out = np.clip(out, 0, 255).astype(np.uint8)
cv2.imwrite(str(out_p), out)
cv2.imwrite(str(out_p.with_name(out_p.stem + '-personmask.png')), pm.astype(np.uint8) * 255)
untouched = (out == plate).all(2)
print(json.dumps({'plate': str(plate_p), 'returned': str(ret_p), 'output': str(out_p), 'ransac_inliers': int(st.sum()),
    'protected_mean_abs_diff_registered': round(diff_reg, 2), 'person_mask_fraction': round(float(pm.mean()), 4),
    'pixels_identical_to_plate_fraction': round(float(untouched.mean()), 4),
    'output_sha256': hashlib.sha256(out_p.read_bytes()).hexdigest()}, indent=1))
