"""FINAL-view states for shots 10-11 (local, unpaid): one oak panel, oak bar,
two parked stools, three stools. Stools are lifted from the selected FINAL view
by difference from the oak plate, excluding oak-hued pixels."""
from pathlib import Path
import cv2
import numpy as np
R = Path(__file__).resolve().parents[1]; C = R / 'outputs/construction'
rd = lambda p: cv2.imread(str(p)).astype(np.float32)
ply, oak, fin = rd(C / 'stage-07-final-newfridge.png'), rd(C / 'stage-10-final-oak.png'), rd(R / 'outputs/keyframes/apartment-fridge-reconstruction-v11.png')
H, W = oak.shape[:2]
def box(x0, y0, x1, y1):
    m = np.zeros((H, W), bool); m[y0:y1, x0:x1] = True; return m
def put(b, s, m, sg=1.2):
    a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), sg)[..., None]; return b * (1 - a) + s * a
one = put(ply, oak, box(770, 868, 1196, 1395))
hsv = cv2.cvtColor(fin.astype(np.uint8), cv2.COLOR_BGR2HSV)
oakhue = (hsv[..., 0] >= 5) & (hsv[..., 0] <= 22) & (hsv[..., 1] > 70)
d = np.abs(fin - oak).max(2) > 22
def stool(x0, x1):
    gray = fin.mean(2)
    m = box(x0, 900, x1, 1520) & d & ~oakhue & ~(box(x0, 1395, x1, 1520) & (gray > 120))
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)) > 0
    n, lab, st, _ = cv2.connectedComponentsWithStats(m.astype(np.uint8))
    keep = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 800]
    return np.isin(lab, keep)
s1, s2, s3 = stool(740, 1150), stool(1260, 1620), stool(1690, 2090)
two = put(oak, fin, s1 | s2); three = put(two, fin, s3)
for n, im in (('stage-10-final-onepanel', one), ('stage-11-final-twostools', two), ('stage-11-final-threestools', three)):
    cv2.imwrite(str(C / f'{n}.png'), np.clip(im, 0, 255).astype(np.uint8))
print('ok')
