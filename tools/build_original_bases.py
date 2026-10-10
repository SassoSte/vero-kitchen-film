"""Shot-01 bases: crop the original listing photos above/right of the
'(c)2023 ARMLS' notice (user-selected option 1, 2026-10-10), keep MASTER's 2688x1520
aspect, upscale (Lanczos). Originals are untouched."""
import json
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parents[1]
out = {}
for name in ('ref-a-cooking-run', 'ref-h-apartment-facing'):
    im = Image.open(R / f'references/original/{name}.webp').convert('RGB')   # 1138x640
    h = 596                                   # notice occupies y>=600
    w = round(h * 2688 / 1520)                # 1054
    x0 = (im.width - w) // 2 + 20             # bias right, away from the corner
    box = (x0, 0, x0 + w, h)
    dst = R / f'outputs/construction/base-{name}.png'
    im.crop(box).resize((2688, 1520), Image.LANCZOS).save(dst)
    out[name] = {'crop_box': box, 'output': str(dst.relative_to(R))}
print(json.dumps(out))
