"""B12 assembly (local): cut the 30 accepted takes to their edit slots, build the
procedural construction-sound track, export 13 shot files and the 60 s master.
Frame boundaries are round(edit_time * 24), so the master is exactly 1440 frames."""
import json, subprocess, sys
from pathlib import Path
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

R = Path(__file__).resolve().parents[1]
T = R / 'outputs/takes'; C = R / 'outputs/construction'; K = R / 'outputs/keyframes'
FPS, SR = 24, 48000
plan = json.loads((R / 'outputs/production/construction-state-plan.json').read_text())

# take -> (source, source_start_s, speed). speed<1 slows (stretches) the source.
TAKES = {
 '01A': (C / 'base-ref-a-cooking-run.png', 0, 1), '01B': (T / '01B-take-v2.mp4', 0, 1),
 '01C': (T / '01C-take-v1.mp4', 0, 1), '01D': (T / '01D-take-v2.mp4', 0, 1),
 '02A': (T / '02A-take-v1.mp4', 0, 1), '02B': (T / '02B-take-v1.mp4', 0, 1),
 '03A': (T / '03A-pilot-v2.mp4', 0, 1),
 '04A': (T / '04A-take-v1.mp4', 0.5, 1), '04B': (T / '04B-take-v1.mp4', 1.0, 1), '04C': (T / '04C-take-v1.mp4', 1.0, 1),
 '05A': (T / '05A-take-v2.mp4', 0, 1), '05B': (T / '05B-take-v1.mp4', 30 / 24, 0.7),
 '06A': (T / '06A-take-v1.mp4', 0.5, 1), '06B': (T / '06B-take-v1.mp4', 1.0, 1), '06C': (T / '06C-take-v1.mp4', 0.5, 1),
 '07A': (T / '07A-take-v2.mp4', 0, 1), '07B': (T / '07B-take-v1.mp4', 0.5, 1),
 '08A': (T / '08A-take-v1.mp4', 0.5, 1),
 '09A': (T / '09A-take-v1.mp4', 0, 1), '09B': (T / '09B-take-v1.mp4', 1.5, 1),
 '09C': (T / '09C-take-v1.mp4', 1.8, 1), '09D': (T / '09D-take-v1.mp4', 2.2, 1),
 '10A': (T / '10A-take-v1.mp4', 0, 1), '11A': (T / '11A-take-v1.mp4', 0.3, 1),
 '11B': (T / '11B-take-v1.mp4', 0, 0.625), '11C': (T / '11C-take-v1.mp4', 1.5, 1),
 '11D': (T / '11D-take-v1.mp4', 1.0, 1), '11E': (T / '11E-take-v1.mp4', 1.0, 1),
 '12A': (T / '12A-hold.mp4', 0, 1), '13A': (T / '13A-hold.mp4', 0, 1),
}
VF = 'scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1'

def fr(t): return int(round(t * FPS))

def cut(take, f0, f1, out):
    src, ss, sp = TAKES[take]; n = f1 - f0
    if src.suffix == '.png':     # 01A: slow push on the cropped original
        cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', str(src), '-vf',
               f"scale=3840:-1,zoompan=z='1+0.015*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps={FPS},setsar=1"]
    else:
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{ss:.4f}', '-i', str(src), '-an', '-vf',
               f'setpts=(PTS-STARTPTS)/{sp},fps={FPS},{VF},tpad=stop_mode=clone:stop_duration=2']
    cmd += ['-frames:v', str(n), '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', str(out)]
    subprocess.run(cmd, check=True)
    got = int(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries',
                              'stream=nb_read_frames', '-of', 'csv=p=0', str(out)], capture_output=True, text=True).stdout.strip())
    assert got == n, (take, got, n)

# ---------------- procedural construction sound ----------------
rng = np.random.default_rng(7)
N = 60 * SR
mix = np.zeros((N, 2), np.float32)
def bp(x, lo, hi, o=4): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)
def lp(x, f, o=4): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def env(n, a, d):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
def add(t, sig, gain=1.0, pan=0.0):
    i = int(t * SR); s = sig[:max(0, N - i)] * gain
    mix[i:i + len(s), 0] += s * (1 - pan) ** 0.5 * 0.9; mix[i:i + len(s), 1] += s * (1 + pan) ** 0.5 * 0.9
def noise(d): return rng.standard_normal(int(d * SR))
def thud(heavy=1.0):
    n = int(0.6 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (70 - 25 * t) * t) * env(n, 0.002, 0.09 * heavy)
    return mixs(body, 0.4 * lp(noise(0.6), 900) * env(n, 0.001, 0.03)) * 0.8
def clank(f=900):
    n = int(0.5 * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * k * t) / k for k in (1, 2.7, 5.1)) * env(n, 0.001, 0.08)
    return mixs(s * 0.35, 0.2 * bp(noise(0.5), 2000, 7000) * env(n, 0.001, 0.01))
def click(): return bp(noise(0.03), 1500, 6000) * env(int(0.03 * SR), 0.0005, 0.004) * 0.6
def clink(f=2600):
    n = int(0.6 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + 0.6 * np.sin(2 * np.pi * f * 1.51 * t)) * env(n, 0.001, 0.12) * 0.18
def scrape(d, lo=400, hi=2500):
    n = int(d * SR); x = bp(noise(d), lo, hi) * np.hanning(n) * (0.6 + 0.4 * np.sin(np.arange(n) / SR * 2 * np.pi * 7))
    return x * 0.35
def rumble(d): n = int(d * SR); return lp(noise(d), 180) * np.hanning(n) * 1.3 + bp(noise(d), 300, 900) * np.hanning(n) * 0.15
def drill(d):
    n = int(d * SR); t = np.arange(n) / SR; f = 210 + 25 * np.sin(2 * np.pi * 3 * t)
    ph = 2 * np.pi * np.cumsum(f) / SR; s = 2 * ((ph / (2 * np.pi)) % 1) - 1
    a = np.minimum(1, t / 0.05) * np.minimum(1, (d - t) / 0.08)
    return (bp(s, 150, 4000) * 0.35 + bp(noise(d), 1500, 6000) * 0.05) * a
def mixs(*xs):
    out = np.zeros(max(len(x) for x in xs))
    for x in xs: out[:len(x)] += x
    return out
def nailer():
    return mixs(thud(0.6) * 0.7, bp(noise(0.25), 3000, 9000) * env(int(0.25 * SR), 0.002, 0.07) * 0.4, click() * 1.5)
def swish(d=0.45): n = int(d * SR); return bp(noise(d), 600, 3500) * np.hanning(n) * 0.25
def step(): return lp(noise(0.12), 600) * env(int(0.12 * SR), 0.001, 0.02) * 0.5
def hum(d): n = int(d * SR); t = np.arange(n) / SR; return (np.sin(2 * np.pi * 120 * t) * 0.02) * np.minimum(1, t / 0.5)

EV = [  # (time s, sound, gain, pan) — synced to the action in each cut
 (1.3, clank(500), .8, .2), (2.15, thud(), .9, .1), (2.45, rumble(1.25), .7, .2), (3.6, thud(.7), .5, .2),
 (4.1, step(), .6, -.3), (4.5, step(), .6, -.3), (5.3, swish(), 1, -.2), (6.1, swish(), 1, -.2), (6.9, swish(), 1, -.2),
 (8.5, drill(0.7), .9, .3), (9.6, click(), .8, .2), (10.2, scrape(0.6, 300, 1500), .7, .3), (10.9, thud(1.4), 1.0, .3),
 (12.9, step(), .5, .3), (13.3, step(), .5, .3),
 (16.3, clank(700), .8, 0), (17.6, click(), 1, 0), (17.9, click(), 1, 0), (18.2, click(), 1, 0),
 (18.9, scrape(0.6, 500, 3000), .6, -.3), (19.6, thud(.5), .6, -.3), (19.65, click(), 1, -.3),
 (20.8, thud(.9), .8, .3), (21.3, step(), .3, .3), (23.4, drill(0.8), .9, .4),
 (25.9, clank(1100), .7, .2), (27.4, click(), 1, .2), (27.7, click(), 1, .2), (28.05, clank(1800), .4, .2),
 (28.7, rumble(1.3), .6, .1), (30.2, thud(.8), .8, .1),
 (31.0, rumble(1.5), .8, -.1), (32.6, rumble(1.4), .6, -.2), (34.3, thud(.7), .7, -.2),
 (35.4, click(), 1.2, 0), (36.1, click(), 1.2, 0), (37.0, click(), 1.2, 0), (35.5, hum(3.5), 1, 0),
 (39.3, click(), .9, -.4), (39.9, click(), .9, -.4), (40.7, scrape(0.8, 400, 2000), .6, -.4), (41.6, thud(.6), .6, -.4),
 (42.7, clank(1500), .4, -.4), (43.7, click(), .9, -.5),
 (45.2, nailer(), .9, -.3), (45.9, nailer(), .9, -.3), (47.0, nailer(), .9, -.3), (47.6, nailer(), .9, -.3),
 (50.3, clank(400), .5, .3), (50.45, thud(.4), .5, .3), (52.05, thud(.4), .5, 0), (52.65, clank(1300), .4, .2),
 (53.2, scrape(0.6, 200, 1200), .4, .5), (54.5, clink(), 1, .3), (54.8, step(), .4, .3),
]
for t, s, g, p in EV: add(t, s.astype(np.float32), g, p)
tone = lp(rng.standard_normal(N), 400) * 0.006 + bp(rng.standard_normal(N), 400, 3000) * 0.0015
mix += np.stack([tone, np.roll(tone, 2400)], 1).astype(np.float32)
fade = np.ones(N, np.float32); fade[-SR:] = np.linspace(1, 0, SR); mix *= fade[:, None]
mix *= 0.89 / np.abs(mix).max()                       # peak -1 dBFS
wav = R / 'outputs/audio/construction-sound.wav'
raw_wav = R / 'outputs/audio/construction-sound-raw.wav'
wavfile.write(raw_wav, SR, (mix * 32767).astype(np.int16))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(raw_wav), '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11', '-ar', str(SR), str(wav)], check=True)

# ---------------- cut, concat, mux ----------------
work = R / 'outputs/audio/segments'; work.mkdir(parents=True, exist_ok=True)
segs = []
for s in plan['shots']:
    for t in s['takes']:
        f0, f1 = fr(t['edit_in']), fr(t['edit_out']); out = work / f"{t['id']}.mp4"
        cut(t['id'], f0, f1, out); segs.append((s['id'], t['id'], f0, f1, out))
lst = work / 'list.txt'; lst.write_text(''.join(f"file '{o}'\n" for *_, o in segs))
silent = work / 'master-video.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(silent)], check=True)
master = R / 'outputs/kitchen_remodel_60s.mp4'
SILENT = True   # 2026-10-10 user: "the sound that's playing is terrible; remove all audio."
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(silent)] + ([] if SILENT else ['-i', str(wav)]) + ['-map', '0:v'] + ([] if SILENT else ['-map', '1:a']) + [
                '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-r', '24',
                ] + (['-an'] if SILENT else ['-c:a', 'aac', '-b:a', '192k', '-ar', '48000']) + ['-t', '60', '-movflags', '+faststart', str(master)], check=True)
for s in plan['shots']:
    a, b = s['edit_in'], s['edit_out']
    out = R / f"outputs/shots/shot-{s['id']}-{s['title'].split(' ')[0].lower().replace('→','')}.mp4"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(master), '-ss', f'{a}', '-to', f'{b}',
                    '-c:v', 'libx264', '-crf', '17'] + (['-an'] if SILENT else ['-c:a', 'aac', '-b:a', '192k']) + [str(out)], check=True)
print(json.dumps({'master': str(master.relative_to(R)), 'segments': len(segs), 'frames': segs[-1][3]}))
