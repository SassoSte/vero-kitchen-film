"""Read-only validation of the bounded-resume handoff; never calls a media provider."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
errors=[];checks=[]
def check(ok,label):
 (checks if ok else errors).append(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'outputs/production/state.json').read_text())
budget_path=ROOT/'outputs/production/budget.json';budget=json.loads(budget_path.read_text())
check(state.get('status') in {'concept-review-hold','handoff-prepared'} and state.get('generation_allowed') is False,'One-concept complete; further generation disabled')
authorization=json.loads((ROOT/budget['authorization']).read_text())
check(authorization['budget_user_text']=='Approve 303 total; correct view 1' and authorization['max_new_jobs']==1,'Explicit one-render authorization')
check(budget['ceiling_credits']==authorization['total_ceiling_credits']==303,'Approved total ceiling303')
quote_total=round(sum(x['quote'] for x in budget['jobs']),2)
check(quote_total==302.25 and budget['task_quote_total']==quote_total,'48 job quotes total302.25')
check(len(budget['jobs'])==48 and all(x['status']=='generated' for x in budget['jobs']),'All48 recorded jobs terminal/generated')
check(round(budget['ceiling_credits']-quote_total,2)==budget['remaining_phase_credits']==0.75,'Remaining task allowance0.75')
name='master-third-view-continuity-v1'
job=next((x for x in budget['jobs'] if x['name']==name),None)
result_path=ROOT/f'outputs/production/{name}-result.json'
check(job is not None and result_path.exists(),'Authorized concept has ledger and result receipt')
result=json.loads(result_path.read_text())[0]
check(result['status']=='completed' and result['id']==job['job_id'] and (ROOT/job['file']).exists(),'Completed result matches ledger and local asset')
check(json.loads((ROOT/f'outputs/production/{name}-quote.json').read_text())['credits']==job['quote']==6.5,'Actual-input quote6.5')
check(budget['reserved_credits']==quote_total<=budget['ceiling_credits'],'Commitments reconciled within cap')
lock=json.loads((ROOT/'outputs/production/north-east-visual-lock.json').read_text())
check(digest(ROOT/lock['asset'])==lock['sha256'],'User-locked north/east image unchanged')
west_lock=json.loads((ROOT/'outputs/production/west-visual-lock.json').read_text())
check(digest(ROOT/west_lock['asset'])==west_lock['sha256'],'User-accepted west image unchanged')
apartment_lock=json.loads((ROOT/'outputs/production/apartment-visual-lock.json').read_text())
check(digest(ROOT/apartment_lock['asset'])==apartment_lock['sha256'],'Restored photographic third view unchanged')
plan=json.loads((ROOT/'outputs/production/construction-state-plan.json').read_text())
check(len(plan['shots'])==13 and sum(s['edit_out']-s['edit_in'] for s in plan['shots'])==60,'Construction plan13 shots/60 seconds')
check(all(abs(sum(t['edit_out']-t['edit_in'] for t in s['takes'])-(s['edit_out']-s['edit_in']))<1e-6 for s in plan['shots']),'Atomic edit slots reconcile')
cat=json.loads((ROOT/'docs/asset-catalog.json').read_text());assets=cat['assets']
check(len({x['id'] for x in assets})==len(assets),'Unique stable asset IDs')
exts={'.png','.jpg','.jpeg','.webp','.mp4','.mov','.webm','.m4v'}
actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.suffix.lower() in exts}
check(actual=={a['path'] for a in assets},'Every raster/video is cataloged exactly once')
for a in assets:
 p=ROOT/a['path'];check(p.is_file() and digest(p)==a['sha256'],f'Asset hash {a["path"]}')
 for kind,rel in a.get('receipts',{}).items():check((ROOT/rel).is_file(),f'Receipt {rel}')
check(cat['still_count']==82 and cat['video_count']==3,'Inventory82 stills /3 videos')
manifest=json.loads((ROOT/'references/source-manifest.json').read_text())
for group in ['files','supplemental_documents_captured_2026_10_09']:
 for a in manifest.get(group,[]):
  p=ROOT/a['local'];check(p.is_file() and digest(p)==a['sha256'],f'Source-copy hash {a["local"]}')
for a in json.loads((ROOT/'references/products/specs/capture-manifest.json').read_text()):
 if 'local' in a:
  p=ROOT/a['local'];check(p.is_file() and p.read_bytes().startswith(b'%PDF-') and digest(p)==a['sha256'],f'Manufacturer PDF {a["local"]}')
# Verify local Markdown links across current handoff docs (ignore web URLs and headings).
for rel in ['README.md','HANDOFF.md','OPUS-HANDOFF.md','AGENTS.md','docs/SOURCE-REGISTER.md','docs/BACKLOG.md','docs/LESSONS.md','docs/ASSET-CATALOG.md']:
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
before=digest(budget_path);result_before=digest(result_path)
proc=subprocess.run([sys.executable,str(ROOT/'tools/run_image_job.py'),name],cwd=ROOT,text=True,capture_output=True)
check(proc.returncode!=0 and 'Generation disabled' in proc.stderr+proc.stdout,'Paid runner rejects invocation before quoting/submission')
check(before==digest(budget_path) and digest(result_path)==result_before,'Pause-guard test leaves budget/results unchanged')
print(json.dumps({'status':'PASS' if not errors else 'FAIL','checks_passed':len(checks),'stills':cat['still_count'],'videos':cat['video_count'],'task_quote_total':quote_total,'errors':errors},indent=2))
sys.exit(bool(errors))
