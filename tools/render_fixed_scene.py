"""Local Mitsuba material/light render, fixed appliance geometry; no media-provider calls."""
from pathlib import Path
import os, json, math, argparse, time
os.environ['MI_DEFAULT_VARIANT']='scalar_rgb'
import mitsuba as mi, drjit as dr, numpy as np
from PIL import Image
mi.set_variant('scalar_rgb');dr.set_thread_count(2)
print('Renderer PID',os.getpid(),'requested threads',dr.thread_count(),flush=True)
ROOT=Path(__file__).resolve().parents[1];CACHE=Path('/tmp/vero-fixed-render');CACHE.mkdir(exist_ok=True)
parser=argparse.ArgumentParser();parser.add_argument('--width',type=int,default=1200);parser.add_argument('--spp',type=int,default=96);parser.add_argument('--name',default='kitchen-fixed-materials-v1');args=parser.parse_args()
cam=json.loads((ROOT/'outputs/review/kitchen-fixed-geometry-camera.json').read_text())['camera_parameters']
T=mi.ScalarTransform4f
rng=np.random.default_rng(2130)
# Materials use linear reflectance, not source photograph pixels.
def rgb(v):return {'type':'rgb','value':v}
def texture(kind):
 h=w=512;y,x=np.mgrid[0:h,0:w]
 if kind=='oak':
  wav=np.sin(x*.47+2*np.sin(y*.019)+.8*np.sin(y*.08));v=.025*wav+.017*np.sin(x*1.77+y*.002)+rng.normal(0,.009,(h,w));base=np.array([.36,.23,.12])
 elif kind=='stone':
  vein=np.exp(-((np.sin(x*.012+y*.009+np.sin(y*.013)*.7))/.065)**2);v=-.045*vein+rng.normal(0,.003,(h,w));base=np.array([.72,.70,.65])
 else:v=rng.normal(0,.006,(h,w));base=np.array([.43,.44,.42])
 arr=np.clip(base+v[...,None],.01,.95).astype(np.float32);f=CACHE/(kind+'.exr');mi.Bitmap(arr).write(str(f));return {'type':'bitmap','filename':str(f),'filter_type':'bilinear'}
def plastic(col,rough=.2):return {'type':'roughplastic','distribution':'ggx','alpha':rough,'diffuse_reflectance':rgb(col)}
mat={'wall':{'type':'diffuse','reflectance':rgb([.70,.69,.65])},'paint':plastic([.64,.64,.59],.24),'stone':{'type':'roughplastic','distribution':'ggx','alpha':.18,'diffuse_reflectance':texture('stone')},'oak':{'type':'roughplastic','alpha':.3,'diffuse_reflectance':texture('oak')},'floor':{'type':'roughplastic','alpha':.32,'diffuse_reflectance':texture('concrete')},'steel':{'type':'roughconductor','distribution':'ggx','material':'Al','alpha_u':.28,'alpha_v':.09},'chrome':{'type':'roughconductor','material':'Cr','alpha':.10},'black':plastic([.015,.017,.018],.16),'red':plastic([.39,.013,.009],.12),'cream':{'type':'diffuse','reflectance':rgb([.63,.60,.53])},'wooddark':plastic([.09,.063,.038],.35),'glass':{'type':'roughdielectric','distribution':'ggx','alpha':.18,'int_ior':1.5,'ext_ior':1.0},'brass':{'type':'roughconductor','material':'Cu','alpha':.3}}
scene={'type':'scene','integrator':{'type':'path','max_depth':8,'rr_depth':5,'hide_emitters':True}}
for k,v in mat.items():scene[k]=v
records=[];counter=0

def roundedmesh(w,d,h,r):
 key=f'{w}_{d}_{h}_{r}'.replace('.','p');f=CACHE/(key+'.ply')
 if f.exists():return f
 half=np.array([w,d,h])/2;r=min(r,float(half.min())*.9);inn=half-r
 vv=[];nn=[];uv=[];ff=[]
 # Surface winding checked against outward rounded normal.
 for axis in range(3):
  other=[j for j in range(3) if j!=axis]
  for sign in [-1,1]:
   grids=[]
   for j in other:
    a=half[j];grids.append([-a,-a+r,0,a-r,a])
   start=len(vv)
   for ai,A in enumerate(grids[0]):
    for bi,B in enumerate(grids[1]):
     q=np.zeros(3);q[axis]=sign*half[axis];q[other[0]]=A;q[other[1]]=B
     c=np.clip(q,-inn,inn);normal=q-c;normal/=np.linalg.norm(normal);v=c+normal*r
     vv.append(v);nn.append(normal);uv.append((ai/4,bi/4))
   for a in range(4):
    for b in range(4):
     ids=[start+a*5+b,start+(a+1)*5+b,start+(a+1)*5+b+1,start+a*5+b+1]
     if np.dot(np.cross(vv[ids[1]]-vv[ids[0]],vv[ids[2]]-vv[ids[0]]),nn[ids[0]])<0:ids.reverse()
     ff.extend([(ids[0],ids[1],ids[2]),(ids[0],ids[2],ids[3])])
 with f.open('w') as out:
  out.write(f'ply\nformat ascii 1.0\nelement vertex {len(vv)}\nproperty float x\nproperty float y\nproperty float z\nproperty float nx\nproperty float ny\nproperty float nz\nproperty float s\nproperty float t\nelement face {len(ff)}\nproperty list uchar int vertex_indices\nend_header\n')
  for v,n,u in zip(vv,nn,uv):out.write(' '.join(map(str,[*v,*n,*u]))+'\n')
  for face in ff:out.write('3 '+' '.join(map(str,face))+'\n')
 return f

def box(name,x,y,z,w,d,h,material='paint',r=0):
 global counter;counter+=1;records.append({'name':name,'min':[x,y,z],'size':[w,d,h],'material':material,'bevel':r})
 if r:
  ob={'type':'ply','filename':str(roundedmesh(w,d,h,r)),'to_world':T.translate([x+w/2,y+d/2,z+h/2])}
 else:ob={'type':'cube','to_world':T.translate([x+w/2,y+d/2,z+h/2])@T.scale([w/2,d/2,h/2])}
 ob['bsdf']={'type':'ref','id':material};scene[f'shape{counter}']=ob

def cyl(name,p0,p1,r,material='chrome'):
 global counter;counter+=1;records.append({'name':name,'p0':p0,'p1':p1,'radius':r,'material':material})
 scene[f'shape{counter}']={'type':'cylinder','p0':p0,'p1':p1,'radius':r,'bsdf':{'type':'ref','id':material}}

def ball(name,center,scale,material):
 global counter;counter+=1
 f=CACHE/('ellipsoid_'+'_'.join(map(str,scale))+'.ply')
 if not f.exists():
  verts=[];norms=[];faces=[]
  for i in range(17):
   th=math.pi*i/16
   for j in range(32):
    ph=2*math.pi*j/32;v=np.array([math.sin(th)*math.cos(ph),math.sin(th)*math.sin(ph),math.cos(th)])
    verts.append(v*np.array(scale));nn=v/np.array(scale);norms.append(nn/np.linalg.norm(nn))
  for i in range(16):
   for j in range(32):
    a=i*32+j;b=i*32+(j+1)%32;c=(i+1)*32+(j+1)%32;d=(i+1)*32+j
    for tri in [(a,c,b),(a,d,c)]:
     if np.dot(np.cross(verts[tri[1]]-verts[tri[0]],verts[tri[2]]-verts[tri[0]]),norms[tri[0]])<0:tri=tri[::-1]
     faces.append(tri)
  with f.open('w') as out:
   out.write(f'ply\nformat ascii 1.0\nelement vertex {len(verts)}\nproperty float x\nproperty float y\nproperty float z\nproperty float nx\nproperty float ny\nproperty float nz\nelement face {len(faces)}\nproperty list uchar int vertex_indices\nend_header\n')
   for v,n in zip(verts,norms):out.write(' '.join(map(str,[*v,*n]))+'\n')
   for tri in faces:out.write('3 '+' '.join(map(str,tri))+'\n')
 scene[f'shape{counter}']={'type':'ply','filename':str(f),'to_world':T.translate(center),'bsdf':{'type':'ref','id':material}}

def area(name,center,size,radiance,rotation=None):
 tr=T.translate(center)
 if rotation:tr=tr@T.rotate(rotation[0],rotation[1])
 scene[name.replace('.','_')]={'type':'rectangle','to_world':tr@T.scale([size[0]/2,size[1]/2,1]),'emitter':{'type':'area','radiance':rgb(radiance)}}
# Fixed manufacturer-based refrigerator.
box('north filler',0,0,0,5.25,28.875,84,r=.05)
box('left enclosure',5.25,0,0,.75,28.875,84,r=.06)
box('right enclosure',42.75,0,0,.75,28.875,84,r=.06)
box('upper cabinet case',6,0,71,36.75,28.875,13,r=.06)
# Subdivide over-fridge doors within same cabinet envelope.
for x in [6.1,24.4]:
 box('upper fridge door',x,28.2,71.15,18.1,.75,12.7,r=.1)
 box('upper fridge recessed panel',x+1.8,28.9,72.95,14.5,.04,9.1,r=.03)
 cyl('upper fridge pull',[x+16 if x<10 else x+2,29.55,74],[x+16 if x<10 else x+2,29.55,79],.15)
box('case',6.575,1,0,35.6,28.5,68.3,'steel',.22)
box('door shadow seam',6.375,29.45,20.8,36,.12,49.2,'black')
for x in [6.375,24.475]:box('French door',x,29.5,21,17.9,4.8,49,'steel',.22)
box('freezer drawer',6.375,29.5,0,36,4.8,20.6,'steel',.25)
for x in [22.6,25.6]:
 cyl('vertical fridge handle',[x,36.15,33],[x,36.15,61],.42)
 for z in [33.6,60.4]:cyl('handle mounting lug',[x,34.1,z],[x,36.15,z],.23)
cyl('freezer handle',[9,36.15,17],[39,36.15,17],.42)
# Adjacent bases/counters retain fixed allocations.
for x,w in [(43.5,13.5),(87,36)]:
 box('base case',x,0,0,w,24,34.5,r=.06);box('quartz',x,0,34.5,w,25.5,1.5,'stone',.08)
 for z,h in [(4,20),(24.5,9)]:
  box('Shaker base door',x+.15,24, z,w-.3,.75,h,r=.08)
  box('recessed panel',x+1.7,24.7,z+1.5,w-3.4,.035,h-3,r=.01)
 cyl('base pull',[x+w*.28,25.6,30],[x+w*.72,25.6,30],.14)
box('range body',57,0,0,30,27,36,'steel',.15)
box('oven glass',59,27,6,26,.15,21,'black',.22)
cyl('oven pull',[60,28.2,26],[84,28.2,26],.4)
box('cooktop',57,1,35.8,30,26,.7,'black',.12)
for x in [59,65,72,79,85]:cyl('red range knob',[x,27.1,32],[x,28.4,32],.85,'red')
for x in [64.5,79.5]:
 for y in [7.5,21]:
  cyl('burner',[x,y,36.3],[x,y,36.65],1.9,'black')
  for dx in [-3.5,3.5]:box('grate',x+dx-.22,y-4.7,36.5,.44,9.4,.35,'black',.08)
  box('grate',x-5,y-.22,36.5,10,.44,.35,'black',.08)
# Upper cabinets with lit frosted panes.
def upper(x,w,doors):
 for xx in [x,x+w-.75]:box('upper side',xx,0,54,.75,12,30,r=.03)
 box('upper back',x,0,54,w,.5,30);box('upper top',x,0,83.25,w,12,.75);box('upper floor',x,0,54,w,12,.75)
 for zz in [64,74]:box('glass shelf',x+.8,1,zz,w-1.6,10,.18,'glass')
 dw=w/doors
 for j in range(doors):
  X=x+j*dw
  for xx in [X+.08,X+dw-1.6]:box('door stile',xx,11.45,54.1,1.5,.75,29.8,r=.07)
  for zz in [54.1,82.4]:box('door rail',X+.1,11.45,zz,dw-.2,.75,1.5,r=.06)
  box('frosted pane',X+1.5,11.65,55.6,dw-3,.16,26.8,'glass')
  H=X+dw-2.1 if j==0 else X+2.1;cyl('upper pull',[H,12.8,60],[H,12.8,67],.15)
 area('internal'+str(x),[x+w/2,6,82.8],[w-2,9],[5,3.7,2.3],([1,0,0],180))
 area('undercab'+str(x),[x+w/2,8,53.95],[w-1,3],[4.2,3.2,2.2],([1,0,0],180))
upper(43.5,13.5,1);upper(87,36,2)
box('hood canopy',57,0,63,30,21,3,'steel',.08);box('hood chimney',64,0,66,16,12,30,'paint',.07)
area('hood light',[72,13,62.95],[22,6],[3.2,2.6,2],([1,0,0],180))
# Pot filler and red appliances.
cyl('pot filler mount',[72,.3,50],[72,2,50],.75)
cyl('pot filler',[72,2,50],[66,2,50],.25);cyl('pot filler',[66,2,50],[66,3,47],.25);cyl('pot filler',[66,3,47],[74,3,47],.25);cyl('pot filler spout',[74,3,47],[74,3,45],.3)
box('red toaster',44.5,13,36,11.5,7.5,8.2,'red',1.3);box('toaster base',44.5,13,36,11.5,7.5,.7,'chrome',.3)
for x in [47,51]:box('toaster slot',x,14,43.95,1.5,5,.1,'black',.1)
ball('kettle',[108,15,41],[3.7,3.7,5],'red');cyl('kettle base',[108,15,36],[108,15,36.7],3.8,'chrome');cyl('kettle lid',[108,15,45.6],[108,15,46],2,'chrome');ball('lid knob',[108,15,46.5],[.6,.6,.5],'red')
for a,b in [([111.5,15,44.5],[113.6,15,44]),([113.6,15,44],[113.6,15,38]),([113.6,15,38],[111.5,15,37.8])]:cyl('kettle handle',a,b,.36)
cyl('kettle spout',[105,15,42],[103,15,44],.7,'chrome')
# Room shell, bar and sink-side mass from fixed camera model.
ow=cam['opening_width_estimate'];oc=cam['opening_center_x'];left=oc-ow/2;right=oc+ow/2
box('rear wall',-80,-2,0,300,2,140,'wall');box('floor',-100,-50,-2,350,500,2,'floor')
box('kitchen ceiling',-5,0,96,135,105,2,'wall')
box('foreground left',-90,102,0,left+90,6,160,'wall');box('foreground right',right,102,0,220-right,6,160,'wall');box('opening header',left,102,96,ow,6,64,'wall')
box('bar wall',left,102,0,ow,4.5,41.5,'oak')
for x in np.arange(left+.2,right-.1,.85):box('bar oak rib',float(x),106.5,.5,.48,.45,40,'oak',.12)
box('bar quartz cap',left-2,99,41.5,ow+4,12,1.5,'stone',.09)
box('sink side base',left,79.5,0,ow,22.5,34.5,'paint')
# Surface segments around a real basin void; basin remains behind bar.
for x,y,w,d in [(left,79.5,ow,2.5),(left,99,ow,3),(left,82,62-left,17),(90,82,right-90,17)]:
 if w>0:box('sink quartz',x,y,34.5,w,d,1.5,'stone',.06)
box('sink floor',62,82,28,28,17,.3,'steel',.1)
for x,y,w,d in [(62,82,.25,17),(89.75,82,.25,17),(62,82,28,.25),(62,98.75,28,.25)]:box('sink inner wall',x,y,28,w,d,7.7,'steel',.06)
cyl('faucet upright',[80,98,36],[80,98,49],.45);cyl('faucet spout',[80,98,49],[73,98,49],.45);cyl('faucet nozzle',[73,98,49],[73,98,47.8],.5)
cyl('faucet control',[82,98,36],[82,98,41],.22);cyl('soap pump',[85,98,36],[85,98,41],.3)
# Three procedural stools; accessory geometry does not alter architectural volumes.
for cx in [oc-23,oc,oc+23]:
 box('stool seat',cx-8,125,24,16,14,2.4,'cream',1)
 box('stool padded back',cx-8.5,138,28,17,2.2,12,'cream',1)
 for x in [cx-6.5,cx+6.5]:
  for y in [127,137]:cyl('stool leg',[x+(x-cx)*.18,y+(y-132)*.25,0],[x,y,24],.55,'wooddark')
 cyl('stool footrest',[cx-7.1,138.5,9],[cx+7.1,138.5,9],.28,'wooddark')
# Soft studio/daylight fill and practical kitchen lighting. Bounded two-thread CPU path tracing.
area('front softbox',[oc,175,78],[100,70],[5.5,5.2,4.7],([1,0,0],90))
# Practical point emitters below track heads avoid adding a visible light panel.
scene['environment']={'type':'constant','radiance':rgb([.12,.14,.16])}
for x in [36,74,110]:
 cyl('track stem',[x,53,95],[x,53,91],.13,'brass');ball('track shade',[x,53,91],[.8,.8,.6],'brass')
 area('track emitter'+str(x),[x,53,90.35],[1.3,1.3],[70,52,32],([1,0,0],180))
 scene['trackpoint'+str(x)]={'type':'point','position':[x,53,90],'intensity':rgb([800,640,440])}
cyl('track rail',[10,53,94],[114,53,94],.15,'brass')
# Camera identical to estimated, bounded geometry-check camera.
ey=np.array([cam['eye_x'],cam['eye_y'],cam['eye_z']]);yaw=cam['yaw_radians'];pitch=cam['pitch_radians'];fw=np.array([math.sin(yaw)*math.cos(pitch),-math.cos(yaw)*math.cos(pitch),math.sin(pitch)])
fov=math.degrees(2*math.atan(2688/(2*cam['focal_px_at2688'])))
scene['sensor']={'type':'perspective','fov':fov,'fov_axis':'x','to_world':T.look_at(origin=ey,target=ey+fw,up=[0,0,1])@T.scale([-1,1,1]),'sampler':{'type':'independent','sample_count':args.spp},'film':{'type':'hdrfilm','width':args.width,'height':round(args.width*1520/2688),'pixel_format':'rgb','rfilter':{'type':'tent'}}}
# Mitsuba look_at convention projects x correctly for this frame; verified on preview.
start=time.time();s=mi.load_dict(scene);print('Scene loaded; rendering',args.width,args.spp,flush=True)
im=mi.render(s,spp=args.spp,seed=2130)
# Standard sRGB conversion, no photo manipulation/compositing.
out=ROOT/'outputs/review';out.mkdir(exist_ok=True);raw=np.array(im);mi.Bitmap(im).write(str(out/(args.name+'.exr')))
x=np.maximum(raw,0);mapped=np.clip((x*(2.51*x+.03))/(x*(2.43*x+.59)+.14),0,1).astype(np.float32)
mi.Bitmap(mapped).convert(mi.Bitmap.PixelFormat.RGB,mi.Struct.Type.UInt8,True).write(str(out/(args.name+'.png')))
(out/(args.name+'-scene.json')).write_text(json.dumps({'renderer':'Mitsuba '+mi.__version__,'threads_requested':2,'width':args.width,'samples_per_pixel':args.spp,'elapsed_seconds':time.time()-start,'camera':cam,'fov_horizontal_degrees':fov,'geometry_records':records,'paid_provider_calls':0,'limits':['Estimated camera/opening from prior study retained; not surveyed match','Procedural materials/fittings/stools; not exact product asset models','Scene is a material/light visualization, not a complete apartment reconstruction','No hinge-sweep or construction approval']},indent=2)+'\n')
print('Saved',out/(args.name+'.png'),'seconds',round(time.time()-start,2),flush=True)
