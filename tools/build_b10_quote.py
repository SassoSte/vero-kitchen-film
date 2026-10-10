"""B10 production plan and quote from construction-state-plan.json. No network access.

Prices are actual Higgsfield quotes taken 2026-10-10 (03A inputs):
gpt_image_2 high/2k 6.5; kling_o3_flf pro 3/4/5 s = 5.4/7.2/9 (sound on), 3.75/5/6.25 (off).
"""
import json, math
from pathlib import Path

R = Path(__file__).resolve().parents[1]
plan = json.loads((R / 'outputs/production/construction-state-plan.json').read_text())
IMG = 6.5
VID = {'on': {3: 5.4, 4: 7.2, 5: 9.0}, 'off': {3: 3.75, 4: 5.0, 5: 6.25}}

DONE = {'03A'}                                   # accepted pilot is the production take
HOLD = {'01A': 'local hold/push on original ref-a photo',
        '12A': 'local hold/push on selected MASTER',
        '13A': 'local hold/push on selected FINAL'}
NO_WORKERS = {'08A': 'lights-off plate -> MASTER lights-on; switch operated off-screen'}

# Paid stage plates (one GPT Image 2 edit each, then local re-composite onto the
# selected view). Every other intermediate state is a free local composite of an
# existing plate and the selected view's own pixels (same camera).
PLATES = [
    ('P01-otr-removed', 'BEFORE-A', '01B/01C', 'original kitchen with over-range microwave removed'),
    ('P01-range-removed', 'BEFORE-A', '01C/02', 'prepared room: range removed, old fridge kept'),
    ('P01D-lamp-removed', 'BEFORE-H', '01D', 'apartment angle without floor lamp'),
    ('P02-bare', 'MASTER', '02A', 'no base cabinets; concrete floor being finished; old fridge'),
    ('P02-bases', 'MASTER', '02B/03', 'base cabinets without worktops'),
    ('W04-pre-sink', 'WEST', '04A-C', 'west counter cutout empty; no faucet; microwave opening empty'),
    ('F07-old-fridge', 'FINAL', '07A', 'old fridge in enclosure corner; bar backing exposed; no stools/styling'),
    ('F07-empty', 'FINAL', '07A/07B', 'empty fridge enclosure'),
    ('F10-backing', 'FINAL', '10A', 'bar front backing exposed, kitchen complete'),
    ('F11-pre-furnish', 'FINAL', '11A/11D/11E', 'two stools parked, rug edge not placed, no vase'),
    ('P08-lights-off', 'MASTER', '08A', 'finished kitchen with all lighting off'),
    ('P09-niche-finished', 'MASTER', '09A-C', 'north niche finished, empty (no wine unit, machine)'),
    ('W09D-nook-empty', 'WEST', '09D', 'west nook with speaker, no phone'),
]

def src_len(slot):
    return 3 if slot <= 2.5 else (4 if slot <= 3.5 else 5)

rows = []
for s in plan['shots']:
    for t in s['takes']:
        slot = round(t['edit_out'] - t['edit_in'], 3)
        r = {'take': t['id'], 'shot': s['id'], 'view': t['view'], 'action': t['action'], 'slot_s': slot}
        if t['id'] in DONE:
            r.update(kind='accepted', frames=0, video_s=0, note='03A-pilot-v2 accepted')
        elif t['id'] in HOLD:
            r.update(kind='local-hold', frames=0, video_s=0, note=HOLD[t['id']])
        elif t['id'] in NO_WORKERS:
            r.update(kind='video-no-workers', frames=0, video_s=src_len(slot), note=NO_WORKERS[t['id']])
        else:
            r.update(kind='workers', frames=2, video_s=src_len(slot), note='paid END + START worker composites')
        rows.append(r)

def totals(sound):
    plate_c = len(PLATES) * IMG
    frame_c = sum(r['frames'] for r in rows) * IMG
    vid_c = sum(VID[sound][r['video_s']] for r in rows if r['video_s'])
    first = plate_c + frame_c + vid_c
    # pilot evidence: 5 image jobs for 3 accepted frames (x1.67); videos 2 for 1
    expected = (plate_c + frame_c) * 5 / 3 + vid_c * 1.5
    ceiling = 2 * first
    return {'plates': round(plate_c, 2), 'worker_frames': round(frame_c, 2), 'videos': round(vid_c, 2),
            'first_pass': round(first, 2), 'expected_with_retries': round(expected, 2), 'ceiling_2_attempts_each': round(ceiling, 2)}

shot_groups = [('T1', ['01', '02', '03']), ('T2', ['04', '05', '06']), ('T3', ['07', '08', '09']), ('T4', ['10', '11', '12', '13'])]
def tranche(ids, sound):
    rs = [r for r in rows if r['shot'] in ids]
    pl = [p for p in PLATES if any(x[:2] in ids for x in p[2].replace('/', ' ').replace('-', ' ').split() if x[:2].isdigit())]
    f = (len(pl) + sum(r['frames'] for r in rs)) * IMG
    v = sum(VID[sound][r['video_s']] for r in rs if r['video_s'])
    return {'shots': ids, 'plates': [p[0] for p in pl], 'image_jobs': len(pl) + sum(r['frames'] for r in rs),
            'video_jobs': sum(1 for r in rs if r['video_s']), 'first_pass': round(f + v, 2), 'ceiling': round(2 * (f + v), 2)}

out = {'date': '2026-10-10', 'prices': {'gpt_image_2_high_2k': IMG, 'kling_o3_flf_pro': VID},
       'counts': {'takes': len(rows), 'accepted': len(DONE), 'local_holds': len(HOLD),
                  'paid_plates': len(PLATES), 'worker_frame_jobs': sum(r['frames'] for r in rows),
                  'video_jobs': sum(1 for r in rows if r['video_s']),
                  'video_seconds_by_len': {k: sum(1 for r in rows if r['video_s'] == k) for k in (3, 4, 5)}},
       'totals_sound_on': totals('on'), 'totals_sound_off': totals('off'),
       'tranches_sound_on': {k: tranche(v, 'on') for k, v in shot_groups},
       'plates': [dict(zip(('id', 'view', 'used_by', 'state'), p)) for p in PLATES], 'takes': rows}
(R / 'outputs/production/b10-quote.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: out[k] for k in ('counts', 'totals_sound_on', 'totals_sound_off', 'tranches_sound_on')}, indent=1))
