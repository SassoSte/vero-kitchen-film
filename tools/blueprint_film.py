"""30 s 'blueprint' transformation film (local, no people, no fire).
Old kitchen -> blueprint of the new kitchen draws over it -> old fades, blueprint
fills into the build -> view 1 build, view 2 build, view 3 build -> hold.
Silent 1920x1080, 24 fps, 720 frames."""
import os, subprocess, sys
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]; C = R / 'outputs/construction'; K = R / 'outputs/keyframes'
M = R / 'outputs/magic'; work = M / 'work'; W, H, FPS = 1920, 1080, 24
LINE = np.float32([255, 235, 200])            # pale cyan-white (BGR)
BLUE = np.float32([120, 62, 18])              # blueprint navy (BGR)
def sh(*a, env=None): subprocess.run([str(x) for x in a], check=True, env=env)
def load(p): return cv2.resize(cv2.imread(str(p)), (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)
def edges(img):
    g = cv2.GaussianBlur(cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2GRAY), (0, 0), 1.4)
    e = cv2.Canny(g, 35, 100).astype(np.float32) / 255
    return np.maximum(e, cv2.GaussianBlur(e, (0, 0), 0.8) * 1.5).clip(0, 1)
def writer(out):
    return subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', str(out)], stdin=subprocess.PIPE)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
grid = (((xx % 48) < 1.2) | ((yy % 48) < 1.2)).astype(np.float32) * 0.35 + (((xx % 240) < 2) | ((yy % 240) < 2)).astype(np.float32) * 0.35
def blueprint(lines, a):          # navy sheet + grid + lines, blended at opacity a
    sheet = np.ones((H, W, 3), np.float32) * BLUE + grid[..., None] * LINE * 0.25
    return sheet, lines
def ease(t): t = np.clip(t, 0, 1); return t * t * (3 - 2 * t)

old = load(C / 'base-ref-a-cooking-run.png')
master_seq = sorted(work.glob('stage-*-nofridge.png'), key=lambda p: ['stage-02-bare', 'stage-02-bases', 'stage-03-plate', 'stage-04-master-done', 'stage-05a-backsplash', 'stage-05b-uppers', 'stage-06a-hood', 'stage-06c-range'].index(p.name.replace('-nofridge.png', '')))
master_seq += [C / 'stage-07-master.png', C / 'stage-09-niche-empty.png', C / 'stage-09c-espresso.png', C / 'stage-11c-kettle.png']
west_seq = [C / f'stage-04-west-{x}.png' for x in ('pre', 'sink', 'faucet', 'done')] + [C / 'stage-09d-phone.png']
final_seq = [C / 'stage-07-final-empty.png', C / 'stage-07-final-newfridge.png', C / 'stage-10-final-oak.png', C / 'stage-11-final-threestools.png']

# --- carry the 2026-10-12 finish revisions into every intermediate plate -----------
# Where a plate already matches the previously selected view (element installed /
# unchanged), take the revised view's pixels; smooth remaining bare-wall plaster with
# the same guided filter used on the selected views. The revised view ends each build.
def guided(I, p, r, eps):
    mean = lambda x: cv2.boxFilter(x, -1, (r, r))
    mI, mp = mean(I), mean(p); a = (mean(I * p) - mI * mp) / (mean(I * I) - mI * mI + eps); b = mp - a * mI
    return mean(a) * I + mean(b)
def poly(polys, shape):
    m = np.zeros(shape, np.uint8)
    for q in polys: cv2.fillPoly(m, [np.array(q, np.int32)], 1)
    return m > 0
CROP3 = (600, 230, 2088, round(2088 * 1520 / 2688))
def big(p, crop=None):
    im = cv2.imread(str(p))
    if crop: x0, y0, w, h = crop; im = cv2.resize(im[y0:y0 + h, x0:x0 + w], (2688, 1520), interpolation=cv2.INTER_LANCZOS4)
    return cv2.resize(im, (2688, 1520), interpolation=cv2.INTER_AREA).astype(np.float32)
def finish(seq, old_final, new_final, walls, tag, crop=None):
    of, nf = big(old_final, crop), big(new_final)
    out_dir = work / 'bp-plates'; out_dir.mkdir(exist_ok=True); res = []
    for i, p in enumerate(seq):
        pl = big(p, crop)
        same = np.abs(cv2.GaussianBlur(pl, (0, 0), 2) - cv2.GaussianBlur(of, (0, 0), 2)).max(2) < 12
        same = cv2.morphologyEx(same.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)) > 0
        a = cv2.GaussianBlur(same.astype(np.float32), (0, 0), 1.5)[..., None]
        pl = pl * (1 - a) + nf * a
        if walls:
            hsv = cv2.cvtColor(pl.astype(np.uint8), cv2.COLOR_BGR2HSV)
            wm = poly(walls, pl.shape[:2]) & ~same & (hsv[..., 1] < 60) & (hsv[..., 2] > 120)
            g = cv2.cvtColor(pl.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
            sm = np.stack([guided(g, pl[..., c] / 255, 61, 0.0025) * 255 for c in range(3)], -1)
            b = cv2.GaussianBlur(wm.astype(np.float32), (0, 0), 1.2)[..., None]
            pl = pl * (1 - b) + sm * b
        q = out_dir / f'{tag}-{i:02d}.png'; cv2.imwrite(str(q), np.clip(pl, 0, 255).astype(np.uint8)); res.append(q)
    return res + [new_final]
W1 = [[[0, 0], [612, 0], [612, 1285], [480, 1300], [480, 870], [0, 860]], [[985, 0], [1298, 0], [1298, 1225], [985, 1225]],
      [[612, 0], [985, 0], [985, 190], [612, 190]], [[1490, 0], [2688, 0], [2688, 1000], [1490, 880]]]
W2 = [[[0, 0], [2688, 0], [2688, 800], [1830, 690], [920, 665], [585, 725], [330, 760], [330, 1400], [0, 1450]]]
master_seq = finish(master_seq, K / 'kitchen-smeg-enclosure-v2.png', K / 'kitchen-smeg-enclosure-v3.png', W1, 'v1')
west_seq = finish(west_seq, K / 'west-phone-speaker-realism-v1.png', K / 'west-phone-speaker-realism-v2.png', W2, 'v2')
final_seq = finish(final_seq, K / 'apartment-fridge-reconstruction-v11.png', K / 'apartment-fridge-reconstruction-v12.png', None, 'v3', crop=CROP3)
final_master = load(K / 'kitchen-smeg-enclosure-v3.png'); bare = load(master_seq[0])
e_new = edges(final_master); e_old = edges(old)

# 1) old kitchen (2 s) -> blueprint of the NEW kitchen draws over it (4 s) -> blueprint fills to bare room (1.5 s)
s1 = work / 'bp-01-intro.mp4'; ff = writer(s1); n = int(7.5 * FPS)
order = (xx / W * 0.75 + yy / H * 0.25)        # drawing sweep, left to right
for f in range(n):
    t = f / FPS
    a = ease((t - 1.8) / 1.7)                  # sheet opacity over the old photo
    d = ease((t - 2.3) / 3.2)                  # lines drawn so far
    fill = ease((t - 6.0) / 1.5)               # blueprint -> bare room
    sheet = np.ones((H, W, 3), np.float32) * BLUE + grid[..., None] * LINE * 0.25
    img = old * (1 - 0.85 * a) + sheet * 0.85 * a
    drawn = e_new * (order <= d * 1.02)
    front = e_new * (np.abs(order - d) < 0.02) * (d < 1)
    img = img + drawn[..., None] * LINE * 0.95 * a + cv2.GaussianBlur(front, (0, 0), 4)[..., None] * LINE * 2.5
    if fill > 0:                               # material fills in behind a rising scan line
        yl = H * (1 - fill); below = (yy >= yl)[..., None].astype(np.float32)
        img = img * (1 - below) + bare * below
        img += ((np.abs(yy - yl) < 3) * (fill < 1))[..., None] * LINE * 0.9
    if t < 1.3:                                # opening: blueprint of the old kitchen resolves into the photo
        o = ease((t - 0.5) / 0.8)
        bp_old = sheet + e_old[..., None] * LINE * 0.95
        img = bp_old * (1 - o) + img * o
    ff.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()

env = dict(os.environ, HOLD0='0.2', HOLD1='0.4', PUSH='0.03', LINE_BGR='255,235,200')
def build(out, secs, seq): sh(sys.executable, R / 'tools/magic_wireframe.py', out, secs, *seq, env=env)
def last(v):
    cap = cv2.VideoCapture(str(v)); f = None
    while True:
        ok, g = cap.read()
        if not ok: break
        f = g
    return f.astype(np.float32)
def first(v): cap = cv2.VideoCapture(str(v)); return cap.read()[1].astype(np.float32)
def bp_trans(out, a, b, secs):                 # a -> blueprint lines of b -> b
    ff = writer(out); n = int(secs * FPS); eb = edges(b)
    sheet = np.ones((H, W, 3), np.float32) * BLUE + grid[..., None] * LINE * 0.25
    for f in range(n):
        t = f / (n - 1); k1 = ease(t / 0.5); k2 = ease((t - 0.5) / 0.5)
        bp = sheet + eb[..., None] * LINE * 0.95
        img = a * (1 - k1) + bp * k1 if t < 0.5 else bp * (1 - k2) + b * k2
        ff.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()
def flip_trans(out, a, b, secs):
    """Card flip between views: A rotates away about the vertical axis while turning
    into a blueprint of itself; at 90 deg it becomes the blueprint of B, which rotates
    in and then resolves from blueprint lines into the photo of B."""
    ff = writer(out); n = int(secs * FPS)
    sheet = np.ones((H, W, 3), np.float32) * BLUE + grid[..., None] * LINE * 0.25
    bpA = sheet + edges(a)[..., None] * LINE * 0.95; bpB = sheet + edges(b)[..., None] * LINE * 0.95
    bg = (np.ones((H, W, 3), np.float32) * BLUE * 0.55 + grid[..., None] * LINE * 0.12)
    src = np.float32([[0, 0], [W, 0], [W, H], [0, H]]); f0 = 2.2 * W
    def card(img, th, scale):
        pts = []
        for x, y in src:
            xc, yc = (x - W / 2) * scale, (y - H / 2) * scale
            xr, z = xc * np.cos(th), xc * np.sin(th)
            k = f0 / (f0 + z); pts.append([W / 2 + xr * k, H / 2 + yc * k])
        M = cv2.getPerspectiveTransform(src, np.float32(pts))
        warped = cv2.warpPerspective(img, M, (W, H), flags=cv2.INTER_LINEAR)
        mask = cv2.warpPerspective(np.ones((H, W), np.float32), M, (W, H))[..., None]
        return warped, mask
    for i in range(n):
        t = i / (n - 1)
        scale = 1 - 0.14 * np.sin(np.pi * t)                       # pulls back mid-flip
        if t < 0.5:
            u = ease(t / 0.5); th = u * np.pi / 2
            face = a * (1 - ease(t / 0.3)) + bpA * ease(t / 0.3)    # photo -> blueprint while turning away
        else:
            u = ease((t - 0.5) / 0.5); th = -(1 - u) * np.pi / 2
            face = bpB * (1 - ease((t - 0.7) / 0.3)) + b * ease((t - 0.7) / 0.3)   # blueprint -> photo as it lands
        th = np.clip(th, -1.5533, 1.5533)
        shade = 1 - 0.35 * np.sin(abs(th))
        w_, m = card(face * shade, th, scale)
        img = bg * (1 - m) + w_ * m
        ff.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()
s2 = work / 'bp-02-master.mp4'; build(s2, 9.0, master_seq)
s4 = work / 'bp-04-west.mp4'; build(s4, 4.5, west_seq)
s3 = work / 'bp-03-to-west.mp4'; flip_trans(s3, last(s2), first(s4), 1.5)
s6 = work / 'bp-06-final.mp4'; build(s6, 5.0, final_seq)
s5 = work / 'bp-05-to-final.mp4'; flip_trans(s5, last(s4), first(s6), 1.5)
# hold with slow push on the selected view 3
s7 = work / 'bp-07-hold.mp4'; ff = writer(s7); im = cv2.resize(cv2.imread(str(K / 'apartment-fridge-reconstruction-v12.png')), (2688, 1520))
for f in range(720 - int(7.5 * FPS) - int(9.0 * FPS) - int(1.5 * FPS) - int(4.5 * FPS) - int(1.5 * FPS) - int(5.0 * FPS)):
    z = 1.0 + 0.0004 * f; Mx = np.float32([[z, 0, (1 - z) * 1344], [0, z, (1 - z) * 760]])
    ff.stdin.write(cv2.resize(cv2.warpAffine(im, Mx, (2688, 1520)), (W, H), interpolation=cv2.INTER_AREA).tobytes())
ff.stdin.close(); ff.wait()
lst = work / 'bp-list.txt'; lst.write_text(''.join(f"file '{s}'\n" for s in (s1, s2, s3, s4, s5, s6, s7)))
out = R / 'outputs/kitchen_blueprint_30s.mp4'
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
   '-pix_fmt', 'yuv420p', '-r', '24', '-frames:v', '720', '-movflags', '+faststart', out)
print('ok')
