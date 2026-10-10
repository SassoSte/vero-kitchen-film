"""Shot-04 west states (local, unpaid): add view-2 pixels back region by region
onto stage-04-west-pre.png. Regions from outputs/production/masks/west-regions.json."""
import json
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]
W = cv2.imread(str(R / 'outputs/keyframes/west-phone-speaker-realism-v1.png')).astype(np.float32)
pre = cv2.imread(str(R / 'outputs/construction/stage-04-west-pre.png')).astype(np.float32)
reg = json.loads((R / 'outputs/production/masks/west-regions.json').read_text())
H, Wd = pre.shape[:2]
def m(*names, minus=()):
    a = np.zeros((H, Wd), np.uint8)
    for n in names: cv2.fillPoly(a, [np.array(reg[n], np.int32)], 1)
    for n in minus: cv2.fillPoly(a, [np.array(reg[n], np.int32)], 0)
    return cv2.GaussianBlur(a.astype(np.float32), (0, 0), 1.5)[..., None]
def put(base, mask): return base * (1 - mask) + W * mask
s1 = put(pre, m('sink', minus=('faucet', 'dispenser')))
s2 = put(s1, m('faucet', 'dispenser'))
s3 = put(s2, m('microwave'))
for name, im in (('stage-04-west-sink', s1), ('stage-04-west-faucet', s2), ('stage-04-west-done', s3)):
    cv2.imwrite(str(R / f'outputs/construction/{name}.png'), np.clip(im, 0, 255).astype(np.uint8))
print('ok')
