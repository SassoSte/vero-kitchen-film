"""Unpaid deterministic perspective ray-box study. Dimensions inches; no source image edits."""
from pathlib import Path
import json, math
import numpy as np
from scipy.optimize import least_squares
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'outputs/review';OUT.mkdir(exist_ok=True)
# Approximate manually identified image anchors in apartment-continuity-v8,2688x1520.
# Opening corners and rear upper-cabinet edges; fridge excluded from camera fitting.
target=np.array([[812,162],[2034,162],[812,854],[2034,854],[1122,354],[1300,354],[1122,582],[1626,354],[1962,354],[1962,582]],float)
def basis(p):
 ex,ey,ez,yaw,pitch,f,ow,oc=p
 fw=np.array([math.sin(yaw)*math.cos(pitch),-math.cos(yaw)*math.cos(pitch),math.sin(pitch)])
 rt=np.cross([0,0,1],fw);rt/=np.linalg.norm(rt);up=np.cross(fw,rt)
 return np.array([ex,ey,ez]),fw,rt,up

def points(p):
 ow,oc=p[6:];l=oc-ow/2;r=oc+ow/2
 return np.array([[l,105,96],[r,105,96],[l,105,43],[r,105,43],[33,12,84],[57,12,84],[33,12,54],[87,12,84],[123,12,84],[123,12,54]])
def project(pts,p):
 e,fw,rt,up=basis(p);q=pts-e;dep=q@fw
 return np.column_stack([1344+p[5]*(q@rt)/dep,760-p[5]*(q@up)/dep])
initial=[61.5,220,59,0,-.04,1600,92,61.5]
fit=least_squares(lambda p:(project(points(p),p)-target).ravel(),initial,bounds=([20,135,40,-.35,-.25,500,60,35],[100,262,66,.35,.25,4500,115,85]))
p=fit.x;proj=project(points(p),p);errs=np.linalg.norm(proj-target,axis=1)
boxes=[]
def box(name,x,y,z,w,d,h,color):boxes.append((name,np.array([x,y,z]),np.array([x+w,y+d,z+h]),np.array(color,float)))
# Cabinet and fridge volumes, independent of camera fitting.
white=[.73,.72,.67];metal=[.48,.54,.57];dark=[.19,.22,.23]
box('north filler',0,0,0,5.25,28.875,84,white)
box('left enclosure panel',5.25,0,0,.75,28.875,84,white)
box('right enclosure panel',42.75,0,0,.75,28.875,84,white)
box('over-fridge cabinet',6,0,71,36.75,28.875,13,white)
box('case',6.575,1,0,35.6,28.5,68.3,metal)
box('left fridge door',6.375,29.5,21,17.9,4.8,49,[.59,.63,.64])
box('right fridge door',24.475,29.5,21,17.9,4.8,49,[.57,.61,.63])
box('freezer drawer',6.375,29.5,0,36,4.8,20.6,metal)
box('left upper handle',22.6,34.3,33,.7,2.4,28,dark)
box('right upper handle',25.6,34.3,33,.7,2.4,28,dark)
box('freezer handle',9,34.3,17,30,2.4,.8,dark)
box('narrow base',43.5,0,0,13.5,24,34.5,white);box('narrow counter',43.5,0,34.5,13.5,25.5,1.5,[.87,.85,.79])
box('range',57,0,0,30,27,36,[.48,.49,.48]);box('far base',87,0,0,36,24,34.5,white);box('far counter',87,0,34.5,36,25.5,1.5,[.87,.85,.79])
box('narrow upper',43.5,0,54,13.5,12,30,white);box('far upper',87,0,54,36,12,30,white);box('hood',57,0,64,30,20,32,[.78,.77,.71])
# Kitchen walls and foreground opening. Width is fitted, not measured.
ow,oc=p[6:];left=oc-ow/2;right=oc+ow/2
box('rear wall',-80,-2,0,300,2,140,[.85,.84,.79]);box('floor',-100,-50,-2,350,500,2,[.62,.63,.61])
box('ceiling',-5,0,96,135,105,2,[.82,.81,.77])
box('foreground left wall',-90,102,0,left+90,6,160,[.85,.84,.79]);box('foreground right wall',right,102,0,220-right,6,160,[.85,.84,.79])
box('opening header',left,102,96,ow,6,64,[.85,.84,.79])
box('bar wall',left,102,0,ow,4.5,41.5,[.57,.55,.48]);box('bar cap',left-2,99,41.5,ow+4,12,1.5,[.87,.85,.79])
box('sink-side counter mass',left,79.5,0,ow,22.5,36,white)
# Proper per-pixel intersections, no painter-order artifacts.
def hit(orig,dirs,scene):
 count=len(dirs);best=np.full(count,np.inf);ids=np.full(count,-1,int);norm=np.zeros((count,3))
 for j,(_,lo,hi,col) in enumerate(scene):
  safe=np.where(np.abs(dirs)<1e-9,1e-9,dirs);a=(lo-orig)/safe;b=(hi-orig)/safe
  near=np.minimum(a,b);far=np.maximum(a,b);enter=near.max(axis=1);leave=far.min(axis=1)
  valid=(leave>=np.maximum(enter,1e-5))&(enter<best)&(enter>1e-5)
  if not valid.any():continue
  axis=near[valid].argmax(axis=1);best[valid]=enter[valid];ids[valid]=j;norm[valid]=0
  rows=np.flatnonzero(valid);norm[rows,axis]=-np.sign(dirs[rows,axis])
 return best,ids,norm

def render(p,w=1200,h=679,scene=None):
 scene=boxes if scene is None else scene;e,fw,rt,up=basis(p)
 yy,xx=np.mgrid[0:h,0:w];u=((xx+.5)*2688/w-1344)/p[5];v=(760-(yy+.5)*1520/h)/p[5]
 dirs=(fw+u[...,None]*rt+v[...,None]*up).reshape(-1,3);dirs/=np.linalg.norm(dirs,axis=1)[:,None]
 t,ids,norm=hit(e,dirs,scene);rgb=np.tile([.93,.93,.90],(len(dirs),1));valid=ids>=0
 pos=e+dirs[valid]*t[valid,None];n=norm[valid];light=np.array([55,65,91])-pos;dist=np.linalg.norm(light,axis=1);ld=light/dist[:,None]
 st,si,sn=hit(pos+n*.002,ld,scene);shadow=st<dist-.01
 lam=np.maximum(0,(n*ld).sum(axis=1));fill=np.maximum(0,n@np.array([.2,.9,.35])/np.linalg.norm([.2,.9,.35]))
 colors=np.array([x[3] for x in scene])[ids[valid]]
 rgb[valid]=colors*(.52+.24*fill[:,None]+.34*lam[:,None]*np.where(shadow,.25,1)[:,None])
 # Display gamma only; no photographic source pixels used.
 rgb=np.clip(rgb,0,1)**(1/1.7)
 return Image.fromarray(np.uint8(rgb.reshape(h,w,3)*255)),ids.reshape(h,w)
main,idmap=render(p)
font='/System/Library/Fonts/Supplemental/Arial.ttf'
canvas=Image.new('RGB',(1200,775),'#f8f6f0');canvas.paste(main,(0,55));d=ImageDraw.Draw(canvas)
d.text((24,14),'Fixed-geometry kitchen study — estimated camera match',font=ImageFont.truetype(font,26),fill='#263b3e')
d.text((24,742),'36" × 70" fridge • 35.7" depth + 1" rear gap • 43.5" enclosure • 13.5" adjacent base',font=ImageFont.truetype(font,18),fill='#263b3e')
canvas.save(OUT/'kitchen-fixed-geometry-camera-v1.png')
# Unoccluded diagnostic uses same camera and geometry, removes only foreground walls/counter.
exclude={'foreground left wall','foreground right wall','opening header','bar wall','bar cap','sink-side counter mass'}
cut,_=render(p,scene=[x for x in boxes if x[0] not in exclude]);cut.save(OUT/'kitchen-fixed-geometry-cutaway-v1.png')
# Oblique diagnostic: separate viewpoint solely to inspect fixed volume.
op=p.copy();op[:3]=[130,140,67];v=np.array([30,24,42])-op[:3];op[3]=math.atan2(v[0],-v[1]);op[4]=math.atan2(v[2],math.hypot(v[0],v[1]));op[5]=1800
vol,_=render(op,scene=[x for x in boxes if x[0] not in exclude]);vol.save(OUT/'kitchen-fixed-geometry-volume-v1.png')
# Determine lowest visible rear-fridge elevation along its centerline by ray occlusion.
zs=np.linspace(0,70,701);line=np.column_stack([np.full(len(zs),24.375),np.full(len(zs),34.301),zs]);eye=basis(p)[0];dv=line-eye;distance=np.linalg.norm(dv,axis=1);di=dv/distance[:,None];t,ids,norm=hit(eye,di,boxes)
vis=(t>=distance-.1);minz=float(zs[vis].min()) if vis.any() else None
receipt={'date':'2026-10-10','source_image':'outputs/keyframes/apartment-continuity-v8.png','source_image_edited':False,'coordinate_system':'x north-to-south along cooking run; y rear wall toward living; z AFF; inches','camera_parameters':dict(zip(['eye_x','eye_y','eye_z','yaw_radians','pitch_radians','focal_px_at2688','opening_width_estimate','opening_center_x'],map(float,p))),'anchor_targets_px':target.tolist(),'projected_anchors_px':proj.tolist(),'anchor_errors_px':errs.tolist(),'mean_anchor_error_px':float(errs.mean()),'maximum_anchor_error_px':float(errs.max()),'fridge_front_lowest_visible_z_in':minz,'door_handle_z_range_in':[33,61],'freezer_handle_z_in':17,'bar_height_in':43,'front_wall_y':105,'rear_counter_depth':25.5,'installed_handle_depth':36.7,'camera_constraints':'Eye height40–66 inches; rear-wall distance135–262 inches, bounded by nominal157-inch living span beyond105-inch kitchen', 'limits':['Manual approximate anchors on generated v8, not surveyed/calibrated photograph','Opening width fitted to image and conflicts with nominal66-inch bar schedule; not approved new dimension','Camera match is estimated and not unique; manufacturer fridge dimensions kept fixed','Primitive box geometry omits hinges/curves/trim; no full door-sweep or installation certification','No source image compositing, AI generation or provider calls']}
(OUT/'kitchen-fixed-geometry-camera.json').write_text(json.dumps(receipt,indent=2)+'\n')
# Export all boxes as OBJ for a conventional DCC renderer, inches units.
lines=[];idx=1
for name,lo,hi,col in boxes:
 x,y,z=lo;X,Y,Z=hi;verts=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)]
 lines.append('o '+name.replace(' ','_'))
 for v in verts:lines.append('v '+' '.join(map(str,v)))
 for f in [(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0)]:lines.append('f '+' '.join(str(idx+j) for j in f))
 idx+=8
(OUT/'kitchen-fixed-geometry-scene.obj').write_text('\n'.join(lines)+'\n')
print(json.dumps({'camera':receipt['camera_parameters'],'mean_anchor_error_px':float(errs.mean()),'lowest_visible_fridge_z':minz,'paid_spend':0},indent=2))
