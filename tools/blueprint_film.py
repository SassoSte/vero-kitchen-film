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
master_seq += [C / 'stage-07-master.png', C / 'stage-09-niche-empty.png', C / 'stage-09c-espresso.png', C / 'stage-11c-kettle.png', K / 'kitchen-smeg-enclosure-v2.png']
west_seq = [C / f'stage-04-west-{x}.png' for x in ('pre', 'sink', 'faucet', 'done')] + [C / 'stage-09d-phone.png', K / 'west-phone-speaker-realism-v1.png']
final_seq = [C / 'stage-07-final-empty.png', C / 'stage-07-final-newfridge.png', C / 'stage-10-final-oak.png', C / 'stage-11-final-threestools.png', K / 'apartment-fridge-reconstruction-v11.png']
final_master = load(K / 'kitchen-smeg-enclosure-v2.png'); bare = load(master_seq[0])
e_new = edges(final_master)

# 1) old kitchen (2 s) -> blueprint of the NEW kitchen draws over it (4 s) -> blueprint fills to bare room (1.5 s)
s1 = work / 'bp-01-intro.mp4'; ff = writer(s1); n = int(7.5 * FPS)
order = (xx / W * 0.75 + yy / H * 0.25)        # drawing sweep, left to right
for f in range(n):
    t = f / FPS
    a = ease((t - 1.5) / 2.0)                  # sheet opacity over the old photo
    d = ease((t - 2.0) / 3.5)                  # lines drawn so far
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
s2 = work / 'bp-02-master.mp4'; build(s2, 9.5, master_seq)
s4 = work / 'bp-04-west.mp4'; build(s4, 4.5, west_seq)
s3 = work / 'bp-03-to-west.mp4'; bp_trans(s3, last(s2), first(s4), 1.25)
s6 = work / 'bp-06-final.mp4'; build(s6, 5.0, final_seq)
s5 = work / 'bp-05-to-final.mp4'; bp_trans(s5, last(s4), first(s6), 1.25)
# hold with slow push on the selected view 3
s7 = work / 'bp-07-hold.mp4'; ff = writer(s7); im = cv2.resize(cv2.imread(str(K / 'apartment-fridge-reconstruction-v11.png')), (2688, 1520))
for f in range(720 - int(7.5 * FPS) - int(9.5 * FPS) - int(1.25 * FPS) - int(4.5 * FPS) - int(1.25 * FPS) - int(5.0 * FPS)):
    z = 1.03 + 0.0004 * f; Mx = np.float32([[z, 0, (1 - z) * 1344], [0, z, (1 - z) * 760]])
    ff.stdin.write(cv2.resize(cv2.warpAffine(im, Mx, (2688, 1520)), (W, H), interpolation=cv2.INTER_AREA).tobytes())
ff.stdin.close(); ff.wait()
lst = work / 'bp-list.txt'; lst.write_text(''.join(f"file '{s}'\n" for s in (s1, s2, s3, s4, s5, s6, s7)))
out = R / 'outputs/kitchen_blueprint_30s.mp4'
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
   '-pix_fmt', 'yuv420p', '-r', '24', '-frames:v', '720', '-movflags', '+faststart', out)
print('ok')
