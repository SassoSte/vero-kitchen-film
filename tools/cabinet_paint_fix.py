"""Make painted cabinet fronts read as smooth painted wood, distinct from the veined
stone (user, 2026-10-12: "the marble countertops need to be distinct from the cabinet
materials"). Local, unpaid. Inside hand-drawn cabinet polygons, on bright low-saturation
pixels only: an edge-preserving guided filter removes the marble-like mottling
(panel lines, handles and shadows survive), then a gentle warm-white paint tint.
Stone, walls and everything else are untouched (asserted). Also builds the closer
living-room framing. Sources stay unchanged; outputs are new versions."""
import json
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]; K = R / 'outputs/keyframes'

def guided(I, p, r, eps):
    mean = lambda x: cv2.boxFilter(x, -1, (r, r))
    mI, mp = mean(I), mean(p); a = (mean(I * p) - mI * mp) / (mean(I * I) - mI * mI + eps); b = mp - a * mI
    return mean(a) * I + mean(b)

def fix(src, dst, polys, exclude=(), tint=(0.965, 0.995, 1.025), sat=70, val=140, chroma=0.4, src_dir=None):
    im = cv2.imread(str((src_dir or K) / src)).astype(np.float32); H, W = im.shape[:2]
    m = np.zeros((H, W), np.uint8)
    for p in polys: cv2.fillPoly(m, [np.array(p, np.int32)], 1)
    for p in exclude: cv2.fillPoly(m, [np.array(p, np.int32)], 0)
    hsv = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_BGR2HSV)
    paint = (m > 0) & (hsv[..., 1] < sat) & (hsv[..., 2] > val)
    paint = cv2.morphologyEx(paint.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) > 0
    g = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
    out = im.copy()
    for c in range(3):                                   # guided by luminance: keeps panel edges
        out[..., c] = guided(g, im[..., c] / 255, 61, 0.0025) * 255
    # paint tone: warm soft white, keeping each pixel's smoothed shading
    lum = out.mean(2, keepdims=True); tint = np.float32(tint)  # BGR
    out = lum * tint + (out - lum) * chroma
    a = cv2.GaussianBlur(paint.astype(np.float32), (0, 0), 1.2); a[a < 0.01] = 0; a = a[..., None]
    res = np.clip(im * (1 - a) + out * a, 0, 255).astype(np.uint8)
    assert (res[cv2.dilate(m, np.ones((9, 9), np.uint8)) == 0] == im.astype(np.uint8)[cv2.dilate(m, np.ones((9, 9), np.uint8)) == 0]).all()
    cv2.imwrite(str(K / dst), res)
    return {'src': src, 'dst': dst, 'painted_fraction': round(float(paint.mean()), 4)}

def backsplash(name, quads, src_box, match_box, clip=None, gain=1.0):
    im = cv2.imread(str(K / name)).astype(np.float32); H, W = im.shape[:2]
    st = cv2.imread(str(R / 'outputs/construction/master-stone-clean.png')).astype(np.float32)
    x0, y0, x1, y1 = src_box; tex = st[y0:y1, x0:x1]
    tex = tex / (cv2.GaussianBlur(tex, (0, 0), 35) + 1) * tex.reshape(-1, 3).mean(0)   # flatten lighting, keep veining
    lowf = cv2.GaussianBlur(im, (0, 0), 25)
    for q, top_lip in quads:
        q = np.float32(q); th, tw = tex.shape[:2]
        Mq = cv2.getPerspectiveTransform(np.float32([[0, 0], [tw, 0], [tw, th], [0, th]]), q)
        t = cv2.warpPerspective(tex, Mq, (W, H)); m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [q.astype(np.int32)], 1)
        shade = lowf.mean(2, keepdims=True) / (t[m > 0].mean() + 1)
        mx0, my0, mx1, my1 = match_box
        tgt = cv2.imread(str(K / name)).astype(np.float32)[my0:my1, mx0:mx1].reshape(-1, 3).mean(0)
        t = t * (tgt / (t[m > 0].reshape(-1, 3).mean(0) + 1)) * np.clip(shade / shade[m > 0].mean(), 0.85, 1.15) * gain
        if clip is not None:
            cm = np.zeros((H, W), np.uint8); cv2.fillPoly(cm, [np.array(clip, np.int32)], 1); m = m & cm
        a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 0.8)[..., None]
        im = im * (1 - a) + t * a
        if top_lip:                                    # slab top edge: thin highlight + soft shadow under it
            p0, p1 = q[0].astype(int), q[1].astype(int)
            cv2.line(im, tuple(p0), tuple(p1), (232, 236, 240), 2)
            sh = np.zeros((H, W), np.float32); cv2.line(sh, tuple(p0 + [0, 4]), tuple(p1 + [0, 4]), 1, 6)
            im *= (1 - 0.12 * cv2.GaussianBlur(sh, (0, 0), 3))[..., None]
    cv2.imwrite(str(K / name), np.clip(im, 0, 255).astype(np.uint8))

rec = [
 fix('kitchen-smeg-enclosure-v2.png', 'kitchen-smeg-enclosure-v3.png',
     [[[1828, 1012], [2688, 1205], [2688, 1520], [1828, 1520]],          # right base run
      [[0, 1395], [405, 1035], [405, 1520], [0, 1520]],                    # left base run
      [[2150, 0], [2688, 0], [2688, 470], [2150, 470]],                    # right glass uppers (frames)
      [[1560, 165], [1715, 165], [1715, 575], [1560, 575]],               # left glass upper (frame)
      [[1300, 0], [1490, 0], [1490, 420], [1300, 420]],                    # cupboard above fridge
      [[1490, 870], [1545, 870], [1545, 1380], [1490, 1380]]]),           # narrow cabinet
 fix('west-phone-speaker-realism-v1.png', 'west-phone-speaker-realism-v2.png',
     [[[600, 828], [1800, 1178], [1800, 1520], [600, 1520]]],
     exclude=[[[612, 895], [792, 895], [792, 1172], [612, 1172]]]),      # microwave stays
 fix('apartment-fridge-reconstruction-v11.png', 'apartment-fridge-reconstruction-v12-paint.png',
     [[[800, 140], [1072, 140], [1072, 395], [800, 395]], [[1105, 335], [1300, 335], [1300, 575], [1105, 575]],
      [[1618, 335], [1962, 335], [1962, 575], [1618, 575]], [[1075, 770], [2090, 770], [2090, 840], [1075, 840]]]),
]
# walls: remove the marble-like mottling from painted walls (no tint, colour kept)
WALL = dict(tint=(1.0, 1.0, 1.0), sat=60, val=120, chroma=1.0, src_dir=K)
rec.append(fix('kitchen-smeg-enclosure-v3.png', 'kitchen-smeg-enclosure-v3.png',
    [[[0, 0], [612, 0], [612, 1285], [480, 1300], [480, 870], [0, 860]], [[985, 0], [1298, 0], [1298, 1225], [985, 1225]], [[612, 0], [985, 0], [985, 190], [612, 190]]],
    exclude=[[[0, 740], [80, 740], [80, 850], [0, 850]]], **WALL))
rec.append(fix('west-phone-speaker-realism-v2.png', 'west-phone-speaker-realism-v2.png',
    [[[0, 0], [2688, 0], [2688, 800], [1830, 690], [920, 665], [585, 725], [330, 760], [330, 1400], [0, 1450]]],
    exclude=[[[535, 405], [812, 405], [812, 645], [535, 645]], [[950, 400], [1400, 400], [1400, 690], [950, 690]], [[1700, 280], [2230, 280], [2230, 720], [1700, 720]]], **WALL))
# stone backsplash on the walls behind the counters that had none
# removed 2026-10-12 (user: "Remove both"): backsplash('kitchen-smeg-enclosure-v3.png', [([[0, 650], [478, 652], [478, 879], [0, 879]], True)], (2250, 520, 2650, 850), (40, 900, 400, 1000),
#           clip=[[0, 650], [478, 652], [478, 879], [195, 879], [195, 842], [0, 842]])
# removed 2026-10-12 (user: "Not good"): backsplash('west-phone-speaker-realism-v2.png', [([[585, 648], [915, 650], [915, 784], [585, 786]], True)], (2250, 520, 2650, 850), (2000, 1040, 2600, 1200), gain=0.93)
# re-seat objects that sit in front of the new backsplash (plant, outlet) from the source
def restore(name, src, boxes):
    a = cv2.imread(str(K / name)); b = cv2.imread(str(K / src))
    hsv = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
    for (x0, y0, x1, y1, keep) in boxes:
        sub = (hsv[y0:y1, x0:x1, 1] > 35) | (hsv[y0:y1, x0:x1, 2] < 130) if keep == 'object' else np.ones((y1 - y0, x1 - x0), bool)
        a[y0:y1, x0:x1][sub] = b[y0:y1, x0:x1][sub]
    cv2.imwrite(str(K / name), a)
restore('kitchen-smeg-enclosure-v3.png', 'kitchen-smeg-enclosure-v2.png', [(0, 745, 80, 846, 'object'), (125, 730, 172, 792, 'box')])
restore('west-phone-speaker-realism-v2.png', 'west-phone-speaker-realism-v1.png', [(722, 622, 765, 690, 'box')])
# closer living-room framing: crop out the open bedroom doorway, keep 16:9, upscale (Lanczos)
im = cv2.imread(str(K / 'apartment-fridge-reconstruction-v12-paint.png'))
x0, y0, w = 600, 230, 2088; h = round(w * 1520 / 2688)
cv2.imwrite(str(K / 'apartment-fridge-reconstruction-v12.png'), cv2.resize(im[y0:y0 + h, x0:x0 + w], (2688, 1520), interpolation=cv2.INTER_LANCZOS4))
(K / 'apartment-fridge-reconstruction-v12-paint.png').unlink()
rec.append({'dst': 'apartment-fridge-reconstruction-v12.png', 'crop': [x0, y0, x0 + w, y0 + h], 'upscale': round(2688 / w, 3)})
(R / 'outputs/production/finish-fix-2026-10-12.json').write_text(json.dumps(rec, indent=2) + '\n')
print(json.dumps(rec, indent=1))
