"""Submit one named quoted media job once; preserve receipts and reserve budget."""
import json,sys,subprocess,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'outputs/production';name=sys.argv[1]
state_file=p/'state.json'
state={}
if state_file.exists():
 state=json.loads(state_file.read_text())
 if state.get('status')=='paused' or state.get('generation_allowed') is False:
  raise SystemExit('Generation disabled; explicit job and budget authorization required before quoting or submission.')
if name not in state.get('authorized_jobs', []):
 raise SystemExit('Job is outside the explicitly authorized single-concept scope.')
x=json.loads((p/f'{name}-request.json').read_text())
bpath=p/'budget.json';b=json.loads(bpath.read_text())
if any(j['name']==name for j in b['jobs']):raise SystemExit('Job already recorded; inspect or resume existing job, never resubmit.')
a=['higgsfield','generate','cost',x['model'],'--prompt',x['prompt']]
for k,v in x['params'].items():a+=['--'+k,str(v).lower() if isinstance(v,bool) else str(v)]
for ref in x.get('references',[]):a+=['--image',str(root/ref)]
for role,ref in x.get('media',{}).items():a+=['--'+role,str(root/ref)]
q=subprocess.run(a+['--json'],capture_output=True,text=True,timeout=45,check=True)
(p/f'{name}-quote.json').write_text(q.stdout);credits=json.loads(q.stdout)['credits']
b=json.loads(bpath.read_text())
if b['reserved_credits']+credits>b['ceiling_credits']:raise SystemExit('Budget cap exceeded')
auth=json.loads((root/state['authorization']).read_text())
if credits>auth.get('maximum_new_spend_credits',b['ceiling_credits']):raise SystemExit('Authorized job price exceeded')
b['reserved_credits']+=credits;b['task_quote_total']=b['reserved_credits'];b['remaining_phase_credits']=round(b['ceiling_credits']-b['reserved_credits'],2);b['jobs'].append({'name':name,'quote':credits,'status':'submitting'});bpath.write_text(json.dumps(b,indent=2))
a[2]='create'
with (p/f'{name}-result.json').open('w') as out,(p/f'{name}-stderr.txt').open('w') as err:
 task=subprocess.Popen(a+['--wait','--wait-timeout','10m','--json'],stdout=out,stderr=err,cwd=root)
 print(f'{name}: reserved {credits} credits; CLI PID {task.pid}',flush=True)
 rc=task.wait()
if rc:raise SystemExit(f'Exit {rc}; inspect receipts before any retry')
result=json.loads((p/f'{name}-result.json').read_text())[0]
if result['status']!='completed':raise SystemExit(f'Job status {result["status"]}; inspect before retry')
url=result['result_url'];dest=root/x.get('output',f'outputs/keyframes/{name}.png');dest.parent.mkdir(parents=True,exist_ok=True);urllib.request.urlretrieve(url,dest)
b=json.loads(bpath.read_text());j=next(j for j in b['jobs'] if j['name']==name);j.update(status='generated',job_id=result['id'],file=str(dest.relative_to(root)));bpath.write_text(json.dumps(b,indent=2))
state=json.loads(state_file.read_text());state.update(status='concept-review-hold',generation_allowed=False,authorized_jobs=[],phase='One authorized concept completed; further generation disabled');state_file.write_text(json.dumps(state,indent=2)+'\n')
print(f'Saved {dest}',flush=True)
