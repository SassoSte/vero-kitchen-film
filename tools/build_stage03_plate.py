"""Stage-03 plate built locally on the selected MASTER (kitchen-smeg-enclosure-v2).

Uses only: MASTER, its pre-B06a source (bare wall around a freestanding fridge), and
pieces of paid return stage-03-plate-v1 (old top-freezer fridge, framed niche, sink
cutout) mapped onto MASTER's measured corners. Room/camera/cabinet geometry comes from
MASTER. Writes the plate plus a change mask. No network access.
usage: build_stage03_plate.py OUT [RANGE_FILL]
"""
import hashlib, json, sys
from pathlib import Path
import cv2
import numpy as np

R = Path(__file__).resolve().parents[1]
K = R / 'outputs/keyframes'
master = cv2.imread(str(K / 'kitchen-smeg-enclosure-v2.png')).astype(np.float32)
pre = cv2.imread(str(K / 'kitchen-smeg-realism-v1.png')).astype(np.float32)
ret = cv2.imread(str(R / 'outputs/construction/raw/stage-03-plate-v1.png')).astype(np.float32)
H, W = master.shape[:2]
rng = np.random.default_rng(3)

def poly(pts):
    m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [np.array(pts, np.int32)], 1); return m > 0
def feather(mask, r):
    return np.clip(cv2.distanceTransform(mask.astype(np.uint8), cv2.DIST_L2, 5) / r, 0, 1)[..., None]
def put(dst, src, mask, r=3):
    a = feather(mask, r); return dst * (1 - a) + src * a
def lp(im, s): return cv2.GaussianBlur(im, (0, 0), s)

plate = master.copy()
b06a = cv2.imread(str(R / 'outputs/review/b06a-local-enclosure-v1-mask.png'), 0) > 0
plate[b06a] = pre[b06a]                       # back to bare wall / freestanding fridge

# ---- plaster wall texture quilted from MASTER's plain north wall ----------------
src = master[150:1150, 1010:1280]
tex = np.zeros((H, W, 3), np.float32); wsum = np.zeros((H, W, 1), np.float32)
P = 240; step = 170
win = np.outer(np.hanning(P), np.hanning(P)).astype(np.float32)[..., None] + 1e-3
for y in range(-60, H, step):
    for x in range(-60, W, step):
        sy, sx = rng.integers(0, src.shape[0] - P), rng.integers(0, src.shape[1] - P)
        patch = src[sy:sy + P, sx:sx + P]
        if rng.random() < .5: patch = patch[:, ::-1]
        y0, x0 = max(y, 0), max(x, 0); y1, x1 = min(y + P, H), min(x + P, W)
        tex[y0:y1, x0:x1] += (patch * win)[y0 - y:y1 - y, x0 - x:x1 - x]
        wsum[y0:y1, x0:x1] += win[y0 - y:y1 - y, x0 - x:x1 - x]
tex /= wsum
detail = tex - lp(tex, 40)                    # mottling + grain, no tone
# light field: return's smooth wall illumination, regraded to MASTER's wall palette
nw_m = master[300:1100, 1010:1280].reshape(-1, 3).mean(0)
nw_r = ret[300:1100, 1010:1280].reshape(-1, 3).mean(0)
field = lp(ret, 45) * (nw_m / nw_r)
wall = field + detail * 1.0
ceil_col = master[5:80, 1160:1440].reshape(-1, 3).mean(0)
ceiling_px = master[0:90, 1150:1480]

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
# east-wall ceiling junction: (1500,148) rising to the right at slope -0.667
ceil = (xx >= 1500) & (yy < 148 - 0.667 * (xx - 1500))
ceil |= (xx < 1500) & (yy < 97 + 0.146 * (xx - 1150))

# ---- wall fill: cooking wall above worktop, fridge corner --------------------------
Wm = poly([[1278, 0], [2688, 0], [2688, 971], [2190, 900], [1830, 866], [1490, 866], [1490, 1250], [1296, 1250], [1296, 1196], [1278, 1196]])
fill = np.where(ceil[..., None], ceil_col + detail * 0.5, wall)
# 1px soft junction line wall/ceiling
edge = np.abs(cv2.Laplacian(ceil.astype(np.float32), cv2.CV_32F)) > 0
fill[edge] *= 0.94
plate = put(plate, fill, Wm, 2)
# north-wall baseboard continued across the strip uncovered left of the fridge
bb = poly([[1270, 1192], [1300, 1192], [1300, 1250], [1270, 1250]])
plate = put(plate, cv2.warpAffine(plate, np.float32([[1, 0, 45], [0, 1, 6]]), (W, H), borderMode=cv2.BORDER_REFLECT), bb, 4)

# ---- old fridge from the return (already on MASTER's footprint) -------------------
fr = poly([[1297, 532], [1455, 501], [1458, 500], [1681, 518], [1681, 866], [1490, 866], [1490, 1392],
           [1420, 1392], [1297, 1262]])
plate = put(plate, ret, fr, 2)
# its door handles project left of the cabinet line: take only the dark handle pixels
hd = poly([[1276, 528], [1298, 528], [1298, 905], [1276, 905]]) & (ret.mean(2) < 168)
hd = cv2.dilate(hd.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
plate = put(plate, ret, hd, 1)

# ---- framed north niche: return quad -> MASTER quad -------------------------------
def quad(srcq, dstq, grow=0):
    M = cv2.getPerspectiveTransform(np.float32(srcq), np.float32(dstq))
    return cv2.warpPerspective(ret, M, (W, H), flags=cv2.INTER_LANCZOS4)
niche_m = [[605, 192], [978, 225], [978, 1255], [602, 1300]]
niche = quad([[605, 195], [987, 227], [990, 1302], [602, 1322]], niche_m)
nm = poly([[598, 186], [985, 219], [985, 1262], [596, 1306]])
g = (plate[~nm & poly([[560, 150], [1030, 150], [1030, 1340], [560, 1340]])].reshape(-1, 3).mean(0) + 1) / \
    (niche[~nm & poly([[560, 150], [1030, 150], [1030, 1340], [560, 1340]])].reshape(-1, 3).mean(0) + 1)
plate = put(plate, niche * np.clip(g, .85, 1.15), nm, 3)

# ---- west sink -> empty cutout --------------------------------------------------
sink = quad([[0, 1002], [322, 985], [200, 1076], [0, 1090]], [[0, 947], [310, 937], [165, 1047], [0, 1055]])
sm = poly([[0, 940], [318, 930], [170, 1052], [0, 1060]])
plate = put(plate, sink, sm, 2)

# ---- worktop under kettle/plant: clone stone from the left along the run -----------
# periodic remap of the clean worktop span x 2205-2345 along the run's slope;
# two tilings offset by half a period, cross-faded, so seams do not repeat
def run_clone(slope, region, x_src=2205, per=140, x_dst=2345):
    out = np.zeros_like(plate)
    acc = np.zeros((H, W, 1), np.float32)
    for off in (0, per // 2):
        t = ((xx - x_dst + off) % per)
        xs = x_src + t
        ys = yy - slope * (xx - xs)
        wgt = (1 - np.abs(t / per * 2 - 1))[..., None] + 1e-3
        out += cv2.remap(plate, xs.astype(np.float32), ys.astype(np.float32), cv2.INTER_LINEAR) * wgt
        acc += wgt
    return out / acc
front = lambda x: 955 + 0.163 * (x - 1800)
topm = poly([[2345, 917], [2688, 967], [2688, int(front(2688)) - 2], [2345, int(front(2345)) - 2]])
facem = poly([[2345, int(front(2345)) - 2], [2688, int(front(2688)) - 2], [2688, int(front(2688)) + 52], [2345, int(front(2345)) + 52]])
plate = put(plate, run_clone(0.143, topm), topm, 8)
plate = put(plate, run_clone(0.163, facem), facem, 8)

# ---- range opening (optional externally prepared fill) --------------------------
rm = poly([[1536, 845], [2190, 845], [2190, 900], [1830, 900], [1830, 1520], [1536, 1520]])
# From this camera the empty opening is dominated by the narrow cabinet's south side
# panel; the back wall is hidden below worktop height (confirmed by attempt 2's return).
cab = master[1000:1300, 1505:1535].reshape(-1, 3).mean(0)       # narrow cabinet white
stone = master[868:898, 1495:1535].reshape(-1, 3).mean(0)       # narrow worktop edge
y_j = lambda x: 900 - 0.143 * (2190 - x)                        # wall/worktop junction
y_c = lambda x: 959 - 0.137 * (x - 1800)                        # right worktop north edge (+5 covers grate rim)
corner = poly([[1803, 961], [1834, 957], [1834, 998], [1803, 1000]])
opening = rm.copy()
# shadowed back wall seen over the right worktop's north edge
band = poly([[1825, y_j(1825) - 8], [2210, y_j(2210) - 8], [2210, y_c(2210) + 2], [1825, y_c(1825) + 2]])
t = np.clip((yy - y_j(xx) + 8) / np.maximum(y_c(xx) - y_j(xx) + 10, 1), 0, 1)[..., None]
# no worktop in the opening: the wall continues past the junction line and darkens
# into the cavity; mirror the wall above across y_j so there is no edge
mir_y = np.clip(2 * (y_j(xx) - 8) - yy, 0, H - 1).astype(np.float32)
cont = cv2.remap(plate, xx.astype(np.float32), mir_y, cv2.INTER_LINEAR)
shadow_wall = cont * (1 - 0.05 * t ** 2)
plate = put(plate, shadow_wall, band & ~corner, 2)
# narrow worktop edge + side panel: attempt 2's rendered panel (real shading, toe kick)
# warped from its own corners onto this camera's measured quad, regraded to MASTER white
r2 = cv2.imread(str(R / 'outputs/construction/raw/stage-03-plate-v2-range.png')).astype(np.float32)
sx, sy = 1227 / r2.shape[1], 920 / r2.shape[0]        # return -> crop scale, crop origin (1290, 600)
src_q = (np.float32([[600, 550], [1035, 545], [1020, 1345], [610, 1535]]) * np.float32([sx, sy]) + np.float32([1290, 600])).astype(np.float32)
r2c = cv2.resize(r2, (1227, 920), interpolation=cv2.INTER_AREA)
r2f = np.zeros_like(plate); r2f[600:1520, 1290:2517] = r2c
dst_q = np.float32([[1541, 864], [1829, 844], [1829, 1424], [1541, 1522]])
Mq = cv2.getPerspectiveTransform(src_q, dst_q)
pan = cv2.warpPerspective(r2f, Mq, (W, H), flags=cv2.INTER_LANCZOS4)
r2_front = r2c[int(850 * sy):int(1450 * sy), int(420 * sx):int(590 * sx)].reshape(-1, 3).mean(0)
pan = pan * np.clip(cab / r2_front, 0.8, 1.2) + detail * 0.3
side = poly(dst_q.tolist()) & ~corner
plate = put(plate, pan, side, 1.5)
# concrete floor in front of the panel, cloned from the open floor to the left
flo = poly([[1541, 1522], [1823, 1426], [1823, 1520], [1541, 1520]])
fsrc = cv2.warpAffine(plate, np.float32([[1, 0, 300], [0, 1, 0]]), (W, H), borderMode=cv2.BORDER_REFLECT)
contact = np.exp(-np.clip(yy - (1522 - 0.34 * (xx - 1541)), 0, None) / 14)[..., None]
plate = put(plate, fsrc * (1 - 0.25 * contact), flo, 2)
if len(sys.argv) > 2:
    rf = cv2.imread(sys.argv[2]).astype(np.float32); plate = put(plate, rf, rm, 3)

out = Path(sys.argv[1]); out.parent.mkdir(parents=True, exist_ok=True)
plate = np.clip(plate, 0, 255).astype(np.uint8)
cv2.imwrite(str(out), plate)
changed = (plate != master.astype(np.uint8)).any(2)
cv2.imwrite(str(out.with_name(out.stem + '-changed.png')), changed.astype(np.uint8) * 255)
cv2.imwrite(str(out.with_name(out.stem + '-range-mask.png')), rm.astype(np.uint8) * 255)
print(json.dumps({'output': str(out), 'changed_fraction': round(float(changed.mean()), 4),
                  'sha256': hashlib.sha256(out.read_bytes()).hexdigest()}))
