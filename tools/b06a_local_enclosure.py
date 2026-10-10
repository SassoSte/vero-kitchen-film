"""B06a unpaid local continuity composite.

Adds the selected view-3 fridge enclosure (two-door Shaker cupboard above, fitted
side panels) into selected view 1 by perspective-warping view 3's own cupboard
pixels and painting the side panel, confined to an explicit mask. Pixels outside
the mask are copied byte-for-byte from the selected view 1. Sources are read-only.
"""
import hashlib, json, sys
from pathlib import Path
import cv2
import numpy as np

root = Path(__file__).resolve().parents[1]
V1 = root / 'outputs/keyframes/kitchen-smeg-realism-v1.png'
V3 = root / 'outputs/keyframes/apartment-fridge-reconstruction-v11.png'
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'outputs/review/b06a-local-enclosure-rebuild.png'  # accepted output: outputs/keyframes/kitchen-smeg-enclosure-v2.png

v1 = cv2.imread(str(V1), cv2.IMREAD_COLOR).astype(np.float32)
v3 = cv2.imread(str(V3), cv2.IMREAD_COLOR).astype(np.float32)
H, W = v1.shape[:2]

def poly(pts):
    m = np.zeros((H, W), np.uint8)
    cv2.fillPoly(m, [np.array(pts, np.int32)], 255)
    return m > 0

def mean_bgr(im, x0, y0, x1, y1):
    return im[y0:y1, x0:x1].reshape(-1, 3).mean(0)

# Grain from the selected image itself, so new surfaces carry view 1's texture.
blur = cv2.GaussianBlur(v1, (0, 0), 5)
# Grain is tiled from a plain stretch of view 1's north wall (no edges), so the
# fridge outline that is being covered does not print through.
wall = v1[150:1180, 1000:1285]
wall_hp = wall - cv2.GaussianBlur(wall, (0, 0), 5)
reps = (H // wall_hp.shape[0] + 1, W // wall_hp.shape[1] + 1, 1)
grain = np.tile(wall_hp, reps)[:H, :W]
lum = cv2.cvtColor(v1.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)

# --- Geometry in view-1 pixels (measured from the selected image) ---------------
L_IN, R_IN = 1296, 1477          # fridge front-left / front-right door edges
STRIP = 9                         # ~3/4in panel front edge at this depth
cup_q = np.float32([[L_IN, 118], [R_IN, -40], [R_IN, 384], [L_IN, 450]])   # TL TR BR BL
reveal = poly([[L_IN, 450], [R_IN, 384], [R_IN, 392], [L_IN, 458]])
left_strip = poly([[L_IN - STRIP, 120], [L_IN, 118], [L_IN + 9, 1222], [L_IN + 9 - STRIP, 1222]])
front_strip = poly([[R_IN, -60], [R_IN + STRIP, -60], [R_IN + STRIP, 866], [R_IN, 866]])
# south side panel face: fridge side to east-wall line, ceiling to worktop,
# behind the glass-front upper and the toaster
side = poly([[R_IN + STRIP, -60], [1700, -60], [1700, 862], [R_IN + STRIP, 866]])
glass_upper = poly([[1560, 232], [1712, 162], [1712, 566], [1562, 570]])
# toaster silhouette (kept from view 1): rounded body + chrome base
tm = np.zeros((H, W), np.uint8)
r = 18
cv2.rectangle(tm, (1585 + r, 727), (1760, 838), 255, -1)
cv2.rectangle(tm, (1585, 727 + r), (1760, 838), 255, -1)
cv2.circle(tm, (1585 + r, 727 + r), r, 255, -1)
cv2.rectangle(tm, (1591, 836), (1760, 870), 255, -1)
toaster_fill = tm > 0
side &= ~glass_upper & ~toaster_fill

# --- Cupboard: view 3's own cupboard pixels, projected into view 1 -------------
src = np.float32([[808, 148], [1062, 148], [1062, 388], [808, 388]])
M = cv2.getPerspectiveTransform(src, cup_q)
warped = cv2.warpPerspective(v3, M, (W, H), flags=cv2.INTER_CUBIC)
cup_mask = poly(cup_q)
cup_mask &= ~left_strip & ~front_strip
# view 3's warm living-room grade -> view 1's white Shaker grade
t = mean_bgr(v1, 1566, 260, 1580, 540)              # view-1 upper-cabinet white
s_ = mean_bgr(v3, 812, 160, 1058, 384)
cup = warped * (t / s_) * 0.97
cup = cup + 0.6 * grain

# --- Side panel: painted white, shaded by view 1's own light field ------------
white = t * np.float32([0.985, 0.985, 0.985])
shade = cv2.GaussianBlur(lum, (0, 0), 25)
ref_amb = np.median(lum[150:350, 1350:1450])        # wall above fridge, ambient only
uc = poly([[1562, 572], [1712, 568], [1712, 866], [1562, 866]])
pool = cv2.GaussianBlur(uc.astype(np.float32), (0, 0), 10) * uc + \
       cv2.GaussianBlur(uc.astype(np.float32), (0, 0), 30) * ~uc * 0.6
ratio = np.clip(shade / np.median(shade[uc]), 0.7, 1.6)
s_amb = 1 + pool * (ratio - 1)
orig_tint = cv2.GaussianBlur(v1, (0, 0), 25) / np.maximum(cv2.GaussianBlur(v1, (0, 0), 25).mean(2, keepdims=True), 1)
tint = 1 + pool[..., None] * (np.clip(orig_tint, 0.6, 1.4) - 1) * 0.55
yy = np.arange(H, dtype=np.float32)[:, None]
vert = 0.95 + 0.06 * np.clip(yy / 860, 0, 1)        # slightly dimmer toward ceiling
panel = white[None, None, :] * (s_amb * (1 + 0 * yy) * vert)[..., None] * tint * 0.93
# soft contact shadow where the face meets the east wall and the cupboard edge
xx = np.arange(W, dtype=np.float32)[None, :]
ao = 1 - 0.10 * np.exp(-np.clip(1700 - xx, 0, None) / 18)
panel *= ao[..., None]
panel += 0.6 * grain

strip_col = t * 1.05                                 # front-lit edge, a touch brighter
comp = v1.copy()
comp[side] = panel[side]
comp[cup_mask] = cup[cup_mask]
comp[reveal & ~front_strip] = v1[reveal & ~front_strip] * 0.0 + np.float32([62, 66, 72])
for m in (left_strip, front_strip):
    comp[m] = strip_col + 0.6 * grain[m]

mask = side | cup_mask | reveal | left_strip | front_strip
# feather 1.5px only at the mask boundary toward untouched pixels
soft = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 0.8)
soft = np.where(mask, np.maximum(soft, 0.5), 0)[..., None]
final = np.where(mask[..., None], soft * comp + (1 - soft) * v1, v1)
final = np.clip(final, 0, 255).astype(np.uint8)
assert (final[~mask] == v1.astype(np.uint8)[~mask]).all(), 'pixels outside mask changed'

out.parent.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(out), final)
cv2.imwrite(str(out.with_name(out.stem + '-mask.png')), mask.astype(np.uint8) * 255)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
print(json.dumps({'output': str(out), 'mask_px': int(mask.sum()),
                  'mask_fraction': round(float(mask.mean()), 5),
                  'mask_bbox': [int(v) for v in (*np.argwhere(mask).min(0)[::-1], *np.argwhere(mask).max(0)[::-1])],
                  'v1_sha256': sha(V1), 'v3_sha256': sha(V3), 'output_sha256': sha(out)}, indent=1))
