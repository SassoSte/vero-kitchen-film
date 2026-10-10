"""Read-only validation of the paused handoff; never calls a media provider."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
errors=[];checks=[]
def check(ok,label):
 (checks if ok else errors).append(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'outputs/production/state.json').read_text())
budget_path=ROOT/'outputs/production/budget.json';budget=json.loads(budget_path.read_text())
check(state.get('status')=='paused' and state.get('generation_allowed') is False,'Explicit pause/generation guard state')
check(budget['ceiling_credits']==200,'Approved cap remains200;205 not silently adopted')
quote_total=round(sum(x['quote'] for x in budget['jobs']),2)
check(quote_total==198.25 and budget['task_quote_total']==quote_total,'32 job quotes total198.25')
check(len(budget['jobs'])==32 and all(x['status']=='generated' for x in budget['jobs']),'All32 recorded jobs terminal/generated')
check(round(200-quote_total,2)==budget['remaining_phase_credits']==1.75,'Remaining task allowance1.75')
name='integrated-wall-frenchdoor-v1'
check(not any(x['name']==name for x in budget['jobs']) and not (ROOT/f'outputs/production/{name}-result.json').exists(),'Prepared request not submitted or counted as paid asset')
check((ROOT/f'outputs/production/{name}-request.json').exists() and json.loads((ROOT/f'outputs/production/{name}-quote.json').read_text())['credits']==6.5,'Prepared request and6.5 quote retained')
cat=json.loads((ROOT/'docs/asset-catalog.json').read_text());assets=cat['assets']
check(len({x['id'] for x in assets})==len(assets),'Unique stable asset IDs')
exts={'.png','.jpg','.jpeg','.webp','.mp4','.mov','.webm','.m4v'}
actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.suffix.lower() in exts}
check(actual=={a['path'] for a in assets},'Every raster/video is cataloged exactly once')
for a in assets:
 p=ROOT/a['path'];check(p.is_file() and digest(p)==a['sha256'],f'Asset hash {a["path"]}')
 for kind,rel in a.get('receipts',{}).items():check((ROOT/rel).is_file(),f'Receipt {rel}')
check(cat['still_count']==54 and cat['video_count']==3,'Inventory54 stills /3 videos')
manifest=json.loads((ROOT/'references/source-manifest.json').read_text())
for group in ['files','supplemental_documents_captured_2026_10_09']:
 for a in manifest.get(group,[]):
  p=ROOT/a['local'];check(p.is_file() and digest(p)==a['sha256'],f'Source-copy hash {a["local"]}')
for a in json.loads((ROOT/'references/products/specs/capture-manifest.json').read_text()):
 if 'local' in a:
  p=ROOT/a['local'];check(p.is_file() and p.read_bytes().startswith(b'%PDF-') and digest(p)==a['sha256'],f'Manufacturer PDF {a["local"]}')
# Verify local Markdown links across current handoff docs (ignore web URLs and headings).
for rel in ['README.md','HANDOFF.md','AGENTS.md','docs/SOURCE-REGISTER.md','docs/BACKLOG.md','docs/LESSONS.md','docs/ASSET-CATALOG.md']:
 p=ROOT/rel
 for target in re.findall(r'\]\(([^\n)]+)\)',p.read_text()):
  target=target.strip().strip('<>')
  if target.startswith(('https://','http://','#','mailto:')):continue
  target=urllib.parse.unquote(target.split('#')[0]);path=Path(target)
  if not path.is_absolute():path=p.parent/path
  check(path.exists(),f'Link {rel} -> {target}')
# HTML paths: decode entities, skip external/data/hash links; code strings aren't links.
import html
for rel in ['outputs/stills-gallery.html','outputs/shotlist.html']:
 p=ROOT/rel;text=p.read_text()
 for target in re.findall(r'(?:src|href)=["\x27]([^"\x27]+)["\x27]',text):
  target=html.unescape(target)
  if target.startswith(('http:','https:','data:','#','blob:','mailto:')):continue
  path=Path(urllib.parse.unquote(target.split('#')[0]));path=path if path.is_absolute() else p.parent/path
  check(path.exists(),f'HTML link {rel} -> {target}')
 scripts=re.findall(r'<script\b[^>]*>(.*?)</script>',text,re.S)
 for script in scripts:
  proc=subprocess.run(['node','--check','-'],input=script,text=True,capture_output=True)
  check(proc.returncode==0,f'JavaScript syntax {rel}')
# Paid runner must abort before uploads/quotes/mutations while paused.
before=digest(budget_path)
proc=subprocess.run([sys.executable,str(ROOT/'tools/run_image_job.py'),name],cwd=ROOT,text=True,capture_output=True)
check(proc.returncode!=0 and 'Production paused by user' in proc.stderr+proc.stdout,'Paid runner rejects invocation before quoting/submission')
check(before==digest(budget_path) and not (ROOT/f'outputs/production/{name}-result.json').exists(),'Pause-guard test leaves budget/results unchanged')
print(json.dumps({'status':'PASS' if not errors else 'FAIL','checks_passed':len(checks),'stills':cat['still_count'],'videos':cat['video_count'],'task_quote_total':quote_total,'errors':errors},indent=2))
sys.exit(bool(errors))
