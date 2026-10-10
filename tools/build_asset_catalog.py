#!/usr/bin/env python3
"""Build a paused-production asset inventory. Reads assets; never generates media."""
from pathlib import Path
import hashlib, json, re, html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'; E=html.escape
KNOWN={
'master-v1':('rejected','Upper cabinets incorrectly extend to ceiling; required 84–96 inch gap absent.','Cabinet geometry failed; later finish/fridge changes supersede it.'),
'master-v2':('rejected','Cabinet gap restored but range has six knobs, inconsistent with Wolf reference.','Wolf control mismatch; later design revisions.'),
'master-v3':('historical-partial','Gap and five-red-knob Wolf layout corrected; provisional first-phase visual reference.','Concrete, coffee and French-door revisions supersede final-design use.'),
'master-v4':('historical-partial','Concrete revision viewed; later audit found old top-freezer and over-fridge cupboard.','Current French-door configuration not shown.'),
'sink-v1':('historical-partial','Topology/floor boundary passed then-current visual review; exact espresso/cup details uncertain.','Old floor and ornate/exposed coffee design superseded.'),
'sink-v2':('historical-partial','Concrete and sleek exposed machine above DW viewed.','Above-DW coffee placement rejected.'),
'sink-v3-concept':('component-reference','Microwave left of single basin, L-faucet and separate spice/tech nook visually reviewed; exposed espresso above DW remains.','Exposed coffee placement rejected; use only relevant components.'),
'sink-v4':('component-reference','Nano Banana Pro cleanup removed espresso/cups above DW; clear counter, microwave, L-faucet and nook viewed by production lead.','Not reconciled with latest REF-K/French-door complete design.'),
'apartment-v1':('rejected','Fridge configuration and six-knob range incorrect.','Replaced by later revisions; current design also changed.'),
'apartment-v2':('rejected','Espresso too small and ceiling treatment conflict.','Replaced by subsequent revisions.'),
'apartment-v3':('rejected','Espresso support/placement conflict.','Replaced by subsequent revisions.'),
'apartment-v4':('rejected','Duplicate espresso and invented foreground counter.','Failed geometry/prop continuity.'),
'apartment-v5':('historical-partial','Passed independent first-phase reference review with fine-detail uncertainty.','Floor, coffee and fridge revisions superseded it.'),
'apartment-v6':('historical-partial','Concrete/rug and removed lamp viewed; later audit found old top-freezer, cupboard and gooseneck.','Fridge/faucet wrong; replaced by v7, itself now superseded.'),
'apartment-v7':('historical-partial','Independent targeted partial pass: single tall upper fridge, lower drawer, cupboard removed, L-faucet corrected. Dimensions/hinge operation unproved.','Latest refrigerator requires TWO French upper doors; not a current complete design.'),
'workers-v1':('identity-reference','Two differentiated full-body workers with prescribed clothing/boots; accepted for earlier pilot identity only.','No claim of final-design or completed-film approval.'),
'pilot-quartz-start-v1':('rejected','Invented central cabinet and camera-facing pose.','Replaced by start-v2.'),
'pilot-quartz-start-v2':('historical-pilot-source','Action moved to cooking-wall base; inspected isolated motion source.','Early sink counter and quartz finish prevent production Shot03 acceptance; later finishes changed.'),
'pilot-fridge-start-v1':('rejected','Conversation-derived review: visually inspected and rejected because refrigerator handles were on the wrong side.','Replaced by start-v2; not a production source.'),
'pilot-fridge-start-v2':('historical-pilot-source','Conversation-derived review: handles moved left; visually inspected and used for the isolated fridge motion test.','Not production-approved; later French-door design supersedes prior fridge appearance.'),
'pilot-stool-start-v1':('historical-pilot-source','Conversation-derived review: visually inspected two parked stools and one held stool with workers; used for isolated placement test.','Not final accepted; resulting pilot failed center-stool orientation; design subsequently changed.'),
'coffee-garage-open-v1':('rejected','Read as a standalone countertop box rather than integrated opening.','Entire above-DW location subsequently rejected.'),
'coffee-garage-closed-v1':('rejected','Closed derivative of rejected countertop-box concept.','Above-DW location rejected; no mechanical proof.'),
'coffee-garage-open-v2':('rejected','Improved integrated tall panel and tray visual concept above DW.','User rejected above-DW location and counter consumption.'),
'coffee-garage-closed-v2':('rejected','Matched tall fitted panel; closed front hid machine/tray/cups.','User rejected above-DW location; mechanism not proved.'),
'end-wall-closed-v1':('rejected','Wrong full-height side cupboard and miniature wine fridge.','Projecting wall-unit scheme later rejected entirely.'),
'end-wall-closed-v2':('rejected','Then-current visual pass after wine-size correction.','User rejected projecting tower, Italy art and merged spice/coffee location.'),
'end-wall-open-v1':('rejected','Matching partial coffee reveal; not full operating extension.','Projecting tower, Italy art and merged locations rejected.'),
'end-wall-flush-v1':('historical-partial','Independent visual-intent pass: flush wine front and closed white coffee panel; no tower/poster/tech.','REF-K replaces blank panel with open lit niche/glass storage; single-door fridge superseded.'),
'end-wall-proposed':('rejected-diagram','Nominal projecting wine-base/combined upper concept diagram, including revised microwave coordinate.','User rejected projecting scheme; original diagrams remain separate geometry sources.'),
'quartz-v1':('failed-pilot','6-fps contacts/full-size endpoint: released misaligned slab; cabinet opening exposed near 4.8–5.04s.','Not production Shot03; earlier design; no every-frame/playback claim.'),
'fridge-v1':('historical-pilot-partial','6-fps contacts/endpoint suggest controlled placement; partner occludes endpoint. Candidate motion pass only.','Not production acceptance; current French-door design supersedes appearance.'),
'stool-v1':('failed-pilot','Center stool ends facing away from bar. Shrinkage suspicion NOT confirmed.','Orientation failed; earlier finish revision; no every-frame/playback claim.')}
roles={'original':'Original BEFORE geometry plate','inspiration':'Appearance reference','products':'Product reference'}
# Titles supplement, never replace, exact filenames and stable IDs.
def semantic_title(p):
 stem=p.stem
 exact={
 'ref-a-cooking-run':'Original kitchen — cooking/fridge wall',
 'ref-b-sink-run':'Original kitchen — sink run',
 'ref-c-wider-sink-run':'Original sink run — duplicate REF-B',
 'ref-d-end-wall-closeup':'Original cooking wall — duplicate REF-A',
 'ref-h-apartment-facing':'Original apartment-facing kitchen — photo 02',
 'ref-i-empty-kitchen-living':'Original empty kitchen/living junction — photo 26',
 'ref-e-cabinetry':'White Shaker cabinetry and stone — REF-E',
 'ref-f-cooking-zone':'Pale hood and pot filler — REF-F',
 'ref-g-full-room':'Material palette — REF-G',
 'ref-h-finished-apartment-facing':'Finished apartment-facing inspiration — REF-H-DESIGN',
 'ref-j-sink-microwave':'Built-in microwave beside sink — REF-J',
 'ref-k-integrated-coffee-wine':'Integrated lit coffee/wine bank — REF-K',
 'wolf-gr304':'Wolf GR304 gas range — product reference',
 'bosch-b30bb130ss-front':'Superseded single-door Bosch fridge — product reference',
 'tallbot-marketing-reference':'Tallbot apartment marketing floor plan',
 'workers-v1':'Two-worker identity sheet — v1',
 'end-wall-proposed':'Rejected projecting end-wall layout — diagram'}
 if stem in exact:return exact[stem]
 if stem.startswith('unit2130-photo-'):return 'Original unit 2130 photograph — '+stem.rsplit('-',1)[1]
 patterns=[
 (r'apartment-(v\d+)','Apartment-facing kitchen — {}'),
 (r'master-(v\d+)','Cooking/fridge wall — {}'),
 (r'sink-(v\d+)-concept','Sink-side nook/microwave — {} concept'),
 (r'sink-(v\d+)','Sink-side kitchen — {}'),
 (r'coffee-garage-(open|closed)-(v\d+)','Above-DW coffee garage — {} {}'),
 (r'end-wall-(open|closed)-(v\d+)','Rejected end-wall tower — {} {}'),
 (r'end-wall-flush-(v\d+)','Flush wine front and closed coffee panel — {}'),
 (r'pilot-quartz-start-(v\d+)','Quartz-seating pilot starting frame — {}'),
 (r'pilot-fridge-start-(v\d+)','Fridge-placement pilot starting frame — {}'),
 (r'pilot-stool-start-(v\d+)','Stool-placement pilot starting frame — {}')]
 for pattern,template in patterns:
  m=re.fullmatch(pattern,stem)
  if m:return template.format(*m.groups())
 m=re.fullmatch(r'(quartz|fridge|stool)-(v\d+)(?:-(6fps|end))?',stem)
 if m:
  label={'quartz':'Quartz-seating','fridge':'Fridge-placement','stool':'Stool-placement'}[m[1]]
  kind={'6fps':'6-fps contact sheet','end':'ending frame',None:'motion pilot'}[m[3]]
  return f'{label} — {m[2]} {kind}'
 return stem.replace('-',' ').title()

def classify(p):
 stem=p.stem; rel=p.relative_to(ROOT).as_posix()
 if rel=='apartment-blueprint/tallbot-marketing-reference.jpg':
  return 'original','Marketing floor-plan reference','source-context','Byte-exact copied marketing diagram; background apartment context, not surveyed geometry or final appliance placement.','Original unit photos and detailed module sources override schematic marketing layout; no new visual inspection.',None
 if '/review/' in rel:
  name=re.sub(r'-(6fps|end)$','',stem); status,verdict,why=KNOWN.get(name,('not-inspected-record','No review mapped.',''))
  return 'pilot-review',('Endpoint frame' if stem.endswith('-end') else '6-fps contact sheet'),status,verdict,why,name
 if 'references/original/' in rel:
  descriptions={'ref-a-cooking-run':'Master cooking-run camera, refrigerator corner and wall planes.','ref-b-sink-run':'Sink-run camera, sink/DW, raised ledge, opening and apartment beyond.','ref-h-apartment-facing':'Original photo-02, living-room-to-kitchen opening, bar and dining adjacency.','ref-i-empty-kitchen-living':'Original photo-26, empty kitchen/living junction, old carpet/tile boundary and wall planes.'}
  desc=descriptions.get(stem,'Original BEFORE photograph; no individual new visual inspection claimed.')+' BEFORE plate governs topology/camera, not final appliance or finish design.'
  if stem.startswith('ref-c'):desc+=' Duplicate of REF-B; no new viewpoint.'
  if stem.startswith('ref-d'):desc+=' Duplicate of REF-A; no new viewpoint.'
  return 'original',roles['original'],'source-geometry',desc,'Historical BEFORE appearance must not override final choices.',None
 if 'references/inspiration/' in rel:
  if stem.startswith('ref-k'):return 'inspiration','Latest user appearance reference','current-user-reference','REF-K: integrated recessed coffee/wine bank, lit glass storage/prep alcove, small espresso. Its own single-door fridge is NOT adopted.','Current request requires French upper door pair; exact model/fit pending.',None
  if stem.startswith('ref-j'):return 'inspiration','Microwave component reference','component-reference','Sink-side built-in microwave left of sink only; do not copy double basin, old faucet or floor.','Does not define complete final kitchen.',None
  desc={'ref-e-cabinetry':'White Shaker cabinetry, frosted inserts and veined stone appearance.','ref-f-cooking-zone':'Pale box/chimney hood, brushed pot filler and cooking-wall material.','ref-g-full-room':'Overall material character only; its floor is superseded by concrete and ceiling must preserve established source continuity.','ref-h-finished-apartment-facing':'User-supplied apartment-facing appearance/composition intent only; its electric cooktop and undercabinet hood are not adopted.'}.get(stem,'Appearance source only; no individual review invented.')
  return 'inspiration',roles['inspiration'],'component-reference',desc,'Original room geometry and latest brief control; conflicting source appliances/floors/room size are not adopted.',None
 if 'references/products/' in rel:
  if 'bosch' in stem:return 'products','Superseded fridge product reference','superseded-product','Bosch single-door product reference; previously used for tall door/lower drawer.','French-door revision supersedes model, single door and model-based 84-inch opening.',None
  return 'products','Wolf range product reference','current-product-reference','Wolf GR304 reference for range appearance/control layout.','Reference image is not installed-fit or whole-design approval.',None
 status,verdict,why=KNOWN.get(stem,('not-inspected-record','No per-asset review recorded in catalog source map.','Not accepted as a final/current design.'))
 return ('videos' if p.suffix.lower() in VIDEO else 'generated'),('Isolated motion pilot' if p.suffix.lower() in VIDEO else 'Generated still / diagram'),status,verdict,why,stem
RASTER={'.png','.jpg','.jpeg','.webp'};VIDEO={'.mp4','.mov','.webm','.m4v'}
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.suffix.lower() in RASTER|VIDEO)
budget=json.loads((OUT/'production/budget.json').read_text()); jobs={j['name']:j for j in budget.get('jobs',[])}
manifest=json.loads((ROOT/'references/source-manifest.json').read_text())
provenance={r['local']:r for group in ['files','supplemental_documents_captured_2026_10_09'] for r in manifest.get(group,[]) if 'local' in r}
assets=[]
for p in paths:
 rel=p.relative_to(ROOT).as_posix();cat,role,status,verdict,why,jobname=classify(p)
 job=jobs.get(jobname,{}) if jobname else {}; receipts={}
 if jobname:
  for kind in ['request','quote','result','stderr']:
   receipt=OUT/'production'/f'{jobname}-{kind}.{ "txt" if kind=="stderr" else "json"}'
   if receipt.exists():receipts[kind]=receipt.relative_to(ROOT).as_posix()
 jobid=job.get('job_id')
 if not jobid and receipts.get('result'):
  try:
   data=json.loads((ROOT/receipts['result']).read_text())
   def findid(x):
    if isinstance(x,dict):
     for k in ['job_id','jobId','generation_id']:
      if isinstance(x.get(k),str):return x[k]
     for v in x.values():
      r=findid(v)
      if r:return r
    if isinstance(x,list):
     for v in x:
      r=findid(v)
      if r:return r
   jobid=findid(data)
  except (ValueError,OSError):pass
 assets.append({'id':'ASSET-'+hashlib.sha256(rel.encode()).hexdigest()[:12].upper(),'title':semantic_title(p),'path':rel,'absolute_path':str(p),'kind':'video' if p.suffix.lower() in VIDEO else 'still','category':cat,'role':role,'status':status,'verdict':verdict,'superseded_reason':why,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'job_name':jobname,'job_id':jobid,'receipts':receipts,'source_provenance':provenance.get(rel),'review_source_note':('Conversation-derived visual review provided by production lead; supplements omissions in outputs/inspection.txt.' if p.stem in {'pilot-fridge-start-v1','pilot-fridge-start-v2','pilot-stool-start-v1'} else 'Recorded inspection/conversation findings or source-reference role; not a new visual inspection.')})
prepared={'id':'PREP-integrated-wall-frenchdoor-v1','status':'NOT GENERATED / NOT SUBMITTED','name':'integrated-wall-frenchdoor-v1','quote_credits':6.5,'note':'Prepared request only; no still exists. Production explicitly paused by user. No cap increase approved in this inventory.','receipts':{k:f'outputs/production/integrated-wall-frenchdoor-v1-{k}.json' for k in ['request','quote'] if (OUT/f'production/integrated-wall-frenchdoor-v1-{k}.json').exists()}}
meta={'project':'vero-kitchen-film','inventory_revision':'2026-10-09-paused','production':'PAUSED by user','authority':'Latest style REF-K; two upper French doors/lower freezer drawer, model/fit pending. No generated still is final approved complete current design.','review_sources':['outputs/inspection.txt','mega-prompt.md','outputs/production/budget.json','conversation review findings'],'root':str(ROOT),'still_count':sum(a['kind']=='still' for a in assets),'video_count':sum(a['kind']=='video' for a in assets),'prepared_not_generated':[prepared],'assets':assets}
(ROOT/'docs/asset-catalog.json').write_text(json.dumps(meta,indent=2)+'\n')
lines=['# Asset catalog — production paused','',meta['authority'],'','Every existing PNG/JPG/JPEG/WebP and video is listed below. IDs are stable hashes of repository-relative paths. Hashes describe exact existing bytes; verdicts are sourced review findings, not a new visual inspection.','',f"**{meta['still_count']} stills · {meta['video_count']} videos.**",'', '[Open searchable gallery](../outputs/stills-gallery.html) · [Machine-readable catalog](asset-catalog.json)','','## Prepared, not generated','',f"`{prepared['name']}` — **NOT GENERATED / NOT SUBMITTED**, quoted 6.5 credits. Not counted as a still. Production paused.",'']
for kind,title in [('still','Stills'),('video','Videos — separate from stills')]:
 lines+=['## '+title,'']
 for a in assets:
  if a['kind']!=kind:continue
  lines += [f"### {a['id']} — {a['title']}",'',f"- Exact filename: `{Path(a['path']).name}`",f"- File: [{a['path']}](../{a['path']})",f"- Absolute path: `{a['absolute_path']}`",f"- Role: {a['role']}; status: **{a['status']}**",f"- Known verdict: {a['verdict']}",f"- Review source note: {a['review_source_note']}",f"- Limit / superseded reason: {a['superseded_reason']}",f"- Bytes: {a['bytes']}; SHA-256: `{a['sha256']}`",f"- Job ID: `{a['job_id'] or 'not recorded'}`"]
  if a['source_provenance']:lines += [f"- Original source: `{a['source_provenance']['source']}`; copy provenance in `references/source-manifest.json`."]
  lines += [f"- {k.title()} receipt: [{v}](../{v})" for k,v in a['receipts'].items()]
  lines += ['']
(ROOT/'docs/ASSET-CATALOG.md').write_text('\n'.join(lines))
cards=[]
for a in assets:
 url='../'+a['path'];receipts=' · '.join(f'<a href="../{E(v)}">{E(k)}</a>' for k,v in a['receipts'].items())
 media=f'<a href="{E(url)}"><img loading="lazy" src="{E(url)}" alt="{E(a["role"]+": "+Path(a["path"]).name)}"></a>' if a['kind']=='still' else f'<a class="video-link" href="{E(url)}">Open video · {E(Path(a["path"]).name)}</a>'
 cards.append(f'''<article data-kind="{a['kind']}" data-category="{E(a['category'])}" data-status="{E(a['status'])}">{media}<h3>{E(a['title'])}</h3><p class="hash">{E(Path(a['path']).name)}</p><p class="badge">{E(a['status'])}</p><p>{E(a['role'])}</p><p>{E(a['verdict'])}</p><p class="muted">{E(a['superseded_reason'])}</p><p><code>{a['id']}</code></p><label for="path-{a['id']}">Absolute path</label><input id="path-{a['id']}" readonly value="{E(a['absolute_path'])}"><button data-copy="path-{a['id']}">Copy path</button><p><a href="{E(url)}">Open original file</a></p><details><summary>Provenance and exact bytes</summary><p>{a['bytes']:,} bytes</p><p class="hash">SHA-256 {a['sha256']}</p><p class="hash">Job ID: {E(a['job_id'] or 'not recorded')}</p><p>{E(a['review_source_note'])}</p><p>{receipts or 'No job receipts mapped; source/reference or unmapped asset.'}</p></details></article>''')
options=lambda field:'<option value="">All</option>'+''.join(f'<option>{E(x)}</option>' for x in sorted({a[field] for a in assets}))
css='''*{box-sizing:border-box}body{margin:0;background:#f4f1eb;color:#232d27;font:16px/1.55 system-ui,sans-serif}header,main,footer{max-width:1450px;margin:auto;padding:26px}h1{font:48px/1.1 Georgia,serif}h2{font:30px Georgia,serif}h3{font-size:18px;overflow-wrap:anywhere}.notice{border-left:5px solid #a25a25;padding:18px;background:#fff}.filters{display:flex;gap:18px;flex-wrap:wrap;margin:24px 0}.filters>div{flex:1;min-width:180px}label{display:block;font-size:13px;font-weight:600}input,select,button{font:inherit;padding:9px;border:1px solid #829182;border-radius:5px;background:white;min-height:40px}input,select{width:100%}button{cursor:pointer;margin-top:8px;color:#22543d}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}article{background:#fffdf8;border:1px solid #d2d8cc;border-radius:8px;padding:16px}img{width:100%;height:225px;object-fit:contain;background:white}a{color:#235f48}.badge{font-size:12px;text-transform:uppercase;letter-spacing:.07em;font-weight:700}.muted{color:#60695f;font-size:14px}.hash{font:12px/1.5 monospace;overflow-wrap:anywhere}details{border-top:1px solid #ddd;padding-top:10px}summary{cursor:pointer}.video-link{display:block;padding:35px 12px;background:#e8eee6}.skip{position:absolute;top:-80px}.skip:focus{top:5px}:focus-visible{outline:3px solid #ad5929;outline-offset:3px}[hidden]{display:none!important}#feedback{min-height:26px}'''
js='''const cards=[...document.querySelectorAll('article[data-kind]')];const search=document.getElementById('search'),category=document.getElementById('category'),status=document.getElementById('status');function filter(){const q=search.value.toLowerCase().trim();let counts={still:0,video:0};for(const c of cards){c.hidden=!!((q&&!c.textContent.toLowerCase().includes(q)&&!c.querySelector('input').value.toLowerCase().includes(q))||(category.value&&c.dataset.category!==category.value)||(status.value&&c.dataset.status!==status.value));if(!c.hidden)counts[c.dataset.kind]++}document.getElementById('counts').textContent=`Showing ${counts.still} stills and ${counts.video} videos`;};[search,category,status].forEach(e=>e.addEventListener('input',filter));document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{const p=document.getElementById(b.dataset.copy);try{if(!navigator.clipboard)throw Error();await navigator.clipboard.writeText(p.value);document.getElementById('feedback').textContent='Absolute path copied.'}catch{p.focus();p.select();document.getElementById('feedback').textContent='Path selected; press Command+C or Ctrl+C.'}}));filter();'''
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vero · every still and pilot</title><style>{css}</style></head><body><a class="skip" href="#content">Skip to catalog</a><header><p>VERO KITCHEN · ASSET CATALOG · PAUSED</p><h1>Every still, clearly identified.</h1><p>{meta['still_count']} existing stills and {meta['video_count']} videos · original files, no image transforms.</p><div class="notice"><b>Production paused by user.</b><p>{E(meta['authority'])}</p><p>Prepared <code>integrated-wall-frenchdoor-v1</code>: quoted 6.5 credits, <strong>NOT GENERATED / NOT SUBMITTED</strong>. It is not an image and is excluded from the still count.</p></div><p><a href="../docs/ASSET-CATALOG.md">Readable catalog</a> · <a href="../docs/asset-catalog.json">JSON catalog with hashes and receipts</a> · <a href="#videos">Videos</a></p><div class="filters"><div><label for="search">Search filename, ID, path or findings</label><input type="search" id="search"></div><div><label for="category">Role/category</label><select id="category">{options('category')}</select></div><div><label for="status">Status</label><select id="status">{options('status')}</select></div></div><p id="counts" role="status"></p><p id="feedback" role="status"></p></header><main id="content" tabindex="-1"><h2>Stills</h2><div class="grid">{''.join(c for c,a in zip(cards,assets) if a['kind']=='still')}</div><section id="videos"><h2>Videos · separate pilot records</h2><p>Links open the original clips. Contact sheets and endpoint frames remain individually cataloged above; no sampled review establishes every-frame acceptance.</p><div class="grid">{''.join(c for c,a in zip(cards,assets) if a['kind']=='video')}</div></section></main><footer>Review statements are recorded evidence, not a new visual review. Rebuild with tools/build_asset_catalog.py after adding assets; newly unmapped files remain uninspected.</footer><script>{js}</script></body></html>'''
(OUT/'stills-gallery.html').write_text(page)
print(json.dumps({'stills':meta['still_count'],'videos':meta['video_count'],'cataloged_bytes':sum(a['bytes'] for a in assets),'unmapped':sum(a['status']=='not-inspected-record' for a in assets)}))
if __name__=='__main__':pass
