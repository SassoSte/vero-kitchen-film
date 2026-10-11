"""Burn the old cabinets, microwave and range in the original photo using fire
lifted from Kling pilot v2 (frames where the old fridge burns), then dissolve under
peak fire to the bare MASTER room. Writes OUT mp4 (1920x1080, 24 fps). Local only.
usage: burn_old.py OUT SECONDS"""
import subprocess, sys
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]
out, secs = sys.argv[1], float(sys.argv[2]); FPS, W, H = 24, 1920, 1080
before = cv2.resize(cv2.imread(str(R / 'outputs/construction/base-ref-a-cooking-run.png')), (W, H)).astype(np.float32)
after = cv2.resize(cv2.imread(str(R / 'outputs/construction/stage-02-bare.png')), (W, H)).astype(np.float32)
# fire sprites from v2 (frames 18-60), cropped around the burning fridge, alpha from orange-ness
cap = cv2.VideoCapture(str(R / 'outputs/magic/magic-pilot-v2.mp4')); spr = []
for i in range(61):
    ok, f = cap.read()
    if not ok: break
    if i < 18: continue
    c = cv2.resize(f, (2688, 1520))[250:1500, 1050:1850].astype(np.float32)
    b, g, r = c[..., 0], c[..., 1], c[..., 2]
    a = np.clip((r - b - 35) / 110, 0, 1) * np.clip((r - 120) / 80, 0, 1)
    a = cv2.GaussianBlur(a, (0, 0), 2)
    spr.append((c, a))
# burn regions in 1920x1080 frame coords (ref-a): uppers+microwave, range+bases+counters
regions = [(860, 0, 1920, 520, 0.0), (590, 0, 860, 260, 0.15), (960, 560, 1920, 1080, 0.1), (680, 600, 1100, 1080, 0.2)]
n = int(round(secs * FPS)); rng = np.random.default_rng(5)
inst = []
for (x0, y0, x1, y1, delay) in regions:
    for _ in range(5):
        cx, cy = rng.uniform(x0, x1), rng.uniform(y0, y1)
        s = (y1 - y0) / 900 * rng.uniform(0.9, 1.8)
        inst.append((cx, cy, s, delay + rng.uniform(0, 0.15), int(rng.integers(0, 6))))
mask = np.zeros((H, W), np.float32)
for (x0, y0, x1, y1, _) in regions: mask[y0:y1, x0:x1] = 1
mask = cv2.GaussianBlur(mask, (0, 0), 25)[..., None]
char = before * 0.25 + np.float32([10, 14, 22])
ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
for f in range(n):
    t = f / (n - 1)
    burnt = np.clip((t - 0.15) / 0.35, 0, 1)                   # objects char then vanish
    base = before * (1 - mask * burnt) + char * mask * burnt
    sw = np.clip((t - 0.55) / 0.25, 0, 1); sw = sw * sw * (3 - 2 * sw)
    base = base * (1 - sw) + after * sw                      # dissolve to bare room under the fire
    fire = np.zeros((H, W, 3), np.float32); fa = np.zeros((H, W), np.float32)
    for (cx, cy, s, d, off) in inst:
        lt = (t - d) / min(0.7, 0.93 - d)
        if lt <= 0 or lt >= 1: continue
        c, a = spr[min(len(spr) - 1, int(lt * (len(spr) - 1)) + off) % len(spr)]
        env = np.sin(np.pi * lt) ** 0.7
        h, w = int(c.shape[0] * s), int(c.shape[1] * s)
        if h < 8 or w < 8: continue
        cs, as_ = cv2.resize(c, (w, h)), cv2.resize(a, (w, h)) * env
        if off % 2: cs, as_ = cs[:, ::-1], as_[:, ::-1]
        x, y = int(cx - w / 2), int(cy - h * 0.6)
        xa, ya, xb, yb = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
        if xa >= xb or ya >= yb: continue
        sub_a = as_[ya - y:yb - y, xa - x:xb - x]; sub_c = cs[ya - y:yb - y, xa - x:xb - x]
        fire[ya:yb, xa:xb] = fire[ya:yb, xa:xb] * (1 - sub_a[..., None]) + sub_c * sub_a[..., None]
        fa[ya:yb, xa:xb] = 1 - (1 - fa[ya:yb, xa:xb]) * (1 - sub_a)
    frame = base * (1 - fa[..., None]) + fire * fa[..., None]
    frame += cv2.GaussianBlur(fa, (0, 0), 40)[..., None] * np.float32([20, 70, 120]) * 0.8   # warm glow
    ff.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait(); print('ok', n)
