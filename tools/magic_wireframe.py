"""Local 'matrix' build: sequence of same-camera stage plates; for each step the
newly added pixels are first traced as glowing golden wireframe (edges of the next
plate inside the change mask), then fill in bottom-up behind a bright scan line,
with drifting sparkles and a slow camera push. Deterministic, no generation.
usage: magic_wireframe.py OUT.mp4 SECONDS plate1 plate2 ... """
import subprocess, sys
import cv2
import numpy as np

out, total = sys.argv[1], float(sys.argv[2]); plates = sys.argv[3:]
FPS, W, H = 24, 1920, 1080
ims = [cv2.resize(cv2.imread(p), (2688, 1520), interpolation=cv2.INTER_AREA).astype(np.float32) for p in plates]
rng = np.random.default_rng(3)
GOLD = np.float32([90, 200, 255])  # BGR

def step_assets(a, b):
    d = np.abs(cv2.GaussianBlur(a, (0, 0), 2) - cv2.GaussianBlur(b, (0, 0), 2)).max(2)
    m = (d > 18).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    m = cv2.dilate(m, np.ones((9, 9), np.uint8)) > 0
    g = cv2.cvtColor(b.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    e = cv2.Canny(cv2.GaussianBlur(g, (0, 0), 1.2), 40, 110) > 0
    e &= m
    e = cv2.dilate(e.astype(np.uint8), np.ones((2, 2), np.uint8)) > 0
    ys, xs = np.nonzero(m)
    y0, y1 = (ys.min(), ys.max()) if len(ys) else (0, 1)
    # draw order: sweep from a seed point outward (distance transform from mask centroid)
    cy, cx = (ys.mean(), xs.mean()) if len(ys) else (760, 1344)
    yy, xx = np.mgrid[0:1520, 0:2688]
    dist = np.hypot(yy - cy, xx - cx); dist = dist / (dist[m].max() + 1) if m.any() else dist
    return m, e, y0, y1, dist

steps = [step_assets(ims[i], ims[i + 1]) for i in range(len(ims) - 1)]
import os
nF = int(round(total * FPS)); hold0, hold1 = int(float(os.environ.get('HOLD0', 0.6)) * FPS), int(float(os.environ.get('HOLD1', 1.0)) * FPS)
PUSH = float(os.environ.get('PUSH', 0.04))
per = (nF - hold0 - hold1) / len(steps)
spark = np.zeros((0, 4), np.float32)  # x, y, vy, life

ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
for f in range(nF):
    if f < hold0: k, t = 0, 0.0
    elif f >= nF - hold1: k, t = len(steps) - 1, 1.0
    else: k = min(len(steps) - 1, int((f - hold0) // per)); t = ((f - hold0) - k * per) / per
    base = ims[k].copy(); nxt = ims[k + 1]; m, e, y0, y1, dist = steps[k]
    glow = np.zeros(base.shape[:2], np.float32)
    # phase 1 (0-.45): wireframe draws outward;  phase 2 (.35-1): fill bottom-up behind scan line
    tw = np.clip(t / 0.45, 0, 1); lines = e & (dist <= tw * 1.02)
    glow[lines] = 1.0
    tf = np.clip((t - 0.35) / 0.6, 0, 1)
    if tf > 0:
        yl = y1 - tf * (y1 - y0 + 40)
        rows = (np.arange(1520) >= yl)[:, None]
        fill = m & rows
        base[fill] = nxt[fill]
        band = m & (np.abs(np.arange(1520)[:, None] - yl) < 6)
        glow[band] = np.maximum(glow[band], 1.0)
        glow[m & ~rows & lines] = 1.0
        if tf >= 1: glow[lines] *= 0.0
        # spawn sparkles along the scan front
        xs = np.nonzero(m[int(np.clip(yl, 0, 1519))])[0]
        if len(xs) and tf < 1:
            pick = rng.choice(xs, size=min(18, len(xs)))
            spark = np.vstack([spark, np.stack([pick, np.full(len(pick), yl), rng.uniform(-3, -0.5, len(pick)), np.ones(len(pick))], 1)])
    fade = 1 - np.clip((t - 0.85) / 0.15, 0, 1) if tf < 1 else 0.0
    g = cv2.GaussianBlur(glow, (0, 0), 6) * 1.6 + cv2.GaussianBlur(glow, (0, 0), 1.2)
    frame = base + (g * fade)[..., None] * GOLD * 0.9
    # sparkles
    if len(spark):
        spark[:, 1] += spark[:, 2]; spark[:, 0] += rng.normal(0, 0.6, len(spark)); spark[:, 3] -= 0.035
        spark = spark[spark[:, 3] > 0]
        sp = np.zeros(base.shape[:2], np.float32)
        ix = np.clip(spark[:, 0].astype(int), 0, 2687); iy = np.clip(spark[:, 1].astype(int), 0, 1519)
        sp[iy, ix] = spark[:, 3]
        frame += cv2.GaussianBlur(sp, (0, 0), 2.2)[..., None] * GOLD * 6
    # warm glow lift + slow camera push (4%) with slight drift
    z = 1.0 + PUSH * f / nF; cxp = 1344 + (30 if PUSH else 0) * np.sin(f / nF * np.pi); cyp = 760
    M = np.float32([[z, 0, (1 - z) * cxp], [0, z, (1 - z) * cyp]])
    frame = cv2.warpAffine(np.clip(frame, 0, 255), M, (2688, 1520), flags=cv2.INTER_LINEAR)
    ff.stdin.write(cv2.resize(frame, (W, H), interpolation=cv2.INTER_AREA).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print('ok', nF)
