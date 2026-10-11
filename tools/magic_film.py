"""30 s magic-transformation film (local assembly). No people.
Before photo -> golden-line transition -> v2 fridge burn -> cloud clears ->
golden wireframe builds of view 1, view 2, view 3 -> hold. Silent, 1920x1080, 24 fps, 720 frames."""
import subprocess, sys
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]; C = R / 'outputs/construction'; K = R / 'outputs/keyframes'; M = R / 'outputs/magic'
W_, H_, FPS = 1920, 1080, 24
work = M / 'work'; work.mkdir(parents=True, exist_ok=True)
rd = lambda p: cv2.imread(str(p)).astype(np.float32)
def sh(*a): subprocess.run([str(x) for x in a], check=True)

# --- fridge-free MASTER plates: corner patch from v1 frame 34, registered to stage-02-bare
cap = cv2.VideoCapture(str(M / 'magic-pilot-v1.mp4')); cap.set(cv2.CAP_PROP_POS_FRAMES, 34); _, fr = cap.read()
fr = cv2.resize(fr, (2688, 1520), interpolation=cv2.INTER_CUBIC)
bare = rd(C / 'stage-02-bare.png')
orb = cv2.ORB_create(6000); keep = np.full((1520, 2688), 255, np.uint8); keep[300:1450, 1200:1800] = 0
k1, d1 = orb.detectAndCompute(bare.astype(np.uint8), keep); k2, d2 = orb.detectAndCompute(fr, keep)
mm = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1), key=lambda x: x.distance)[:1500]
Hm, _ = cv2.findHomography(np.float32([k2[x.queryIdx].pt for x in mm]), np.float32([k1[x.trainIdx].pt for x in mm]), cv2.RANSAC, 3)
fr = cv2.warpPerspective(fr, Hm, (2688, 1520)).astype(np.float32)
def fridge_mask(n):
    m = np.zeros((1520, 2688), np.float32)
    cv2.rectangle(m, (1255, 420), (1492, 1445), 1, -1)                 # front
    side_bottom = 1440 if n == 'stage-02-bare' else 868                 # side panel above worktop/cabinet
    cv2.rectangle(m, (1488, 420), (1700, side_bottom), 1, -1)
    if n in ('stage-05b-uppers', 'stage-06a-hood', 'stage-06c-range'):
        pass
    m = cv2.dilate(m, np.ones((61, 61), np.uint8))
    return cv2.GaussianBlur(m, (0, 0), 12)[..., None]
fm = fridge_mask('stage-02-bare')
lum = lambda im, m: im[(m[..., 0] < 0.01) & (np.abs(np.arange(2688)[None, :] - 1375) < 260) & (np.abs(np.arange(1520)[:, None] - 900) < 450)].mean(0)
names = ['stage-02-bare', 'stage-02-bases', 'stage-03-plate', 'stage-04-master-done', 'stage-05a-backsplash',
         'stage-05b-uppers', 'stage-06a-hood', 'stage-06c-range']
nf = []
for n in names:
    im = rd(C / f'{n}.png'); m = fridge_mask(n)
    ring = ((cv2.GaussianBlur(m[..., 0], (0, 0), 30) > 0.02) & (m[..., 0] < 0.02)).astype(np.float32)[..., None]
    nc = lambda x: cv2.GaussianBlur(x * ring, (0, 0), 60) / (cv2.GaussianBlur(ring, (0, 0), 60)[..., None] + 1e-4)
    g = np.clip((nc(im) + 1) / (nc(fr) + 1), 0.7, 1.4)
    if n in ('stage-05b-uppers', 'stage-06a-hood', 'stage-06c-range'):
        keepm = np.zeros((1520, 2688), np.float32); cv2.rectangle(keepm, (1550, 140), (1730, 590), 1, -1)
        m = m * (1 - cv2.GaussianBlur(keepm, (0, 0), 2)[..., None])     # glass upper stays
    if n != 'stage-02-bare':
        cab = np.zeros((1520, 2688), np.float32); cv2.rectangle(cab, (1492, 872), (1900, 1520), 1, -1)
        m = m * (1 - cv2.GaussianBlur(cab, (0, 0), 2)[..., None])       # narrow cabinet stays
    out = im * (1 - m) + fr * g * m
    p = work / f'{n}-nofridge.png'; cv2.imwrite(str(p), np.clip(out, 0, 255).astype(np.uint8)); nf.append(p)
master_seq = nf + [C / 'stage-07-master.png', C / 'stage-09-niche-empty.png', C / 'stage-09c-espresso.png', C / 'stage-11c-kettle.png', K / 'kitchen-smeg-enclosure-v2.png']
west_seq = [C / f'stage-04-west-{x}.png' for x in ('pre', 'sink', 'faucet', 'done')] + [C / 'stage-09d-phone.png', K / 'west-phone-speaker-realism-v1.png']
final_seq = [C / 'stage-07-final-empty.png', C / 'stage-07-final-newfridge.png', C / 'stage-10-final-oak.png',
             C / 'stage-11-final-twostools.png', C / 'stage-11-final-threestools.png', K / 'apartment-fridge-reconstruction-v11.png']

def wire(out, secs, seq, hold0=0.3, hold1=0.3):
    sh('env', f'HOLD0={hold0}', f'HOLD1={hold1}', 'PUSH=0.04', sys.executable, R / 'tools/magic_wireframe.py', out, secs, *seq)
def still(out, img, secs, z0=1.0, z1=1.03):
    n = int(round(secs * FPS)); im = cv2.resize(cv2.imread(str(img)), (2688, 1520))
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W_}x{H_}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', str(out)], stdin=subprocess.PIPE)
    for f in range(n):
        z = z0 + (z1 - z0) * f / max(n - 1, 1); Mx = np.float32([[z, 0, (1 - z) * 1344], [0, z, (1 - z) * 760]])
        ff.stdin.write(cv2.resize(cv2.warpAffine(im, Mx, (2688, 1520)), (W_, H_), interpolation=cv2.INTER_AREA).tobytes())
    ff.stdin.close(); ff.wait()
def frame_of(video, which):
    cap = cv2.VideoCapture(str(video)); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0 if which == 'first' else n - 1); ok, f = cap.read()
    if not ok:
        cap = cv2.VideoCapture(str(video)); f = None
        while True:
            ok, g = cap.read()
            if not ok: break
            f = g
    return cv2.resize(f, (W_, H_)).astype(np.float32)
GOLD = np.float32([90, 200, 255])
def trans(out, a, b, secs, glow=True):
    n = int(round(secs * FPS))
    e = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(b.astype(np.uint8), cv2.COLOR_BGR2GRAY), (0, 0), 1.2), 40, 110).astype(np.float32) / 255
    ea = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(a.astype(np.uint8), cv2.COLOR_BGR2GRAY), (0, 0), 1.2), 40, 110).astype(np.float32) / 255
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W_}x{H_}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', str(out)], stdin=subprocess.PIPE)
    for f in range(n):
        t = f / max(n - 1, 1); s = t * t * (3 - 2 * t)
        img = a * (1 - s) + b * s
        if glow:
            g = np.sin(np.pi * t)
            lines = ea * max(0, 1 - 2 * t) + e * min(1, 2 * t)
            gl = cv2.GaussianBlur(lines, (0, 0), 3) * 1.8 + lines
            img = img * (1 - 0.35 * g) + (gl * g)[..., None] * GOLD * 0.9 + 25 * g
        ff.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()

segs = []
s1 = work / '01-before.mp4'; still(s1, C / 'base-ref-a-cooking-run.png', 1.0); segs.append(s1)
s2 = work / '02-burn-old.mp4'; sh(sys.executable, R / 'tools/burn_old.py', s2, 3.0); segs.append(s2)
s3 = work / '03-burn.mp4'
sh('ffmpeg', '-v', 'error', '-y', '-i', M / 'magic-pilot-v2.mp4', '-vf', f'trim=start_frame=0:end_frame=55,setpts=PTS-STARTPTS,scale={W_}:{H_},setsar=1', '-an', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', s3)
segs.append(s3)
s5 = work / '05-master.mp4'; wire(s5, 8.5, master_seq)
s4 = work / '04-clear.mp4'; trans(s4, frame_of(s3, 'last'), frame_of(s5, 'first'), 1.0, glow=False); segs += [s4, s5]
s7 = work / '07-west.mp4'; wire(s7, 5.0, west_seq)
s6 = work / '06-to-west.mp4'; trans(s6, frame_of(s5, 'last'), frame_of(s7, 'first'), 1.0); segs += [s6, s7]
s9 = work / '09-final.mp4'; wire(s9, 6.0, final_seq)
s8 = work / '08-to-final.mp4'; trans(s8, frame_of(s7, 'last'), frame_of(s9, 'first'), 1.0); segs += [s8, s9]
s10 = work / '10-hold.mp4'; still(s10, K / 'apartment-fridge-reconstruction-v11.png', 30 - 1.0 - 3.0 - 55 / 24 - 1 - 8.5 - 1 - 5 - 1 - 6, 1.04, 1.06); segs += [s10]
lst = work / 'list.txt'; lst.write_text(''.join(f"file '{s}'\n" for s in segs))
out = R / 'outputs/kitchen_magic_30s.mp4'
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-r', '24', '-frames:v', '720', '-movflags', '+faststart', out)
print('ok')
