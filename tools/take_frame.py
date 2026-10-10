"""One paid worker frame: write request, allowlist it, run the guarded runner,
compute saliency, and composite people (+ named contact regions) onto a state plate.
usage: take_frame.py NAME BASE_STATE REF_JSON PROMPT_FILE BBOX_JSON [extra_cfg_json]
Final candidate: outputs/construction/raw/NAME-composite.png (inspect before promoting)."""
import json, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]; P = R / 'outputs/production'
name, base, refs, pfile, bbox = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4], json.loads(sys.argv[5])
extra = json.loads(sys.argv[6]) if len(sys.argv) > 6 else {}
raw = f'outputs/construction/raw/{name}.png'
if not (R / raw).exists():
    req = {'model': 'gpt_image_2', 'params': {'quality': 'high', 'resolution': '2k', 'aspect_ratio': '16:9'},
           'references': refs, 'prompt': Path(pfile).read_text().strip(), 'output': raw}
    (P / f'{name}-request.json').write_text(json.dumps(req, indent=2) + '\n')
    st = json.loads((P / 'state.json').read_text()); st.update(generation_allowed=True, authorized_jobs=[name])
    (P / 'state.json').write_text(json.dumps(st, indent=2) + '\n')
    r = subprocess.run([sys.executable, str(R / 'tools/run_image_job.py'), name], cwd=R, capture_output=True, text=True)
    print(r.stdout[-300:], r.stderr[-300:])
    if r.returncode: sys.exit(r.returncode)
sal = f'outputs/construction/raw/{name}-saliency.png'
x0, y0, x1, y1 = bbox
subprocess.run([sys.executable, str(R / 'tools/u2net_saliency.py'), raw, str(max(0, x0 - 20)), str(max(0, y0 - 20)), str(min(2688, x1 + 20)), str(min(1520, y1 + 20)), sal], cwd=R, check=True)
cfg = {'bbox': bbox, 'thr': 30, 'saliency': sal, 'sal_thr': 0.6, 'floor_y': 1520, 'erode': 2, 'tone': False,
       'solid': [[[[x0, y0], [x1, y0], [x1, y1], [x0, y1]], 40]]}
cfg.update(extra)
(P / f'{name}-composite-config.json').write_text(json.dumps(cfg))
out = subprocess.run([sys.executable, str(R / 'tools/person_composite.py'), base, raw, f'outputs/construction/raw/{name}-composite.png', json.dumps(cfg)],
                     cwd=R, capture_output=True, text=True, check=True).stdout
(P / f'{name}-composite.json').write_text(out)
d = json.loads(out); print(name, 'inliers', d['ransac_inliers'], 'resid', d['protected_mean_abs_diff_registered'], 'mask', d['person_mask_fraction'])
