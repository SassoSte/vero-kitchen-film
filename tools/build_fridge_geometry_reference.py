"""Deterministic dimensional concept; never modifies original sources or calls a provider."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ROOT=Path(__file__).resolve().parents[1]
fig=plt.figure(figsize=(15,9),facecolor='#faf8f3')
ax=fig.add_axes([.03,.16,.59,.73],projection='3d')
all_faces=[];all_colors=[]
def box(x,y,z,w,d,h,color):
 p=[(x,y,z),(x+w,y,z),(x+w,y+d,z),(x,y+d,z),(x,y,z+h),(x+w,y,z+h),(x+w,y+d,z+h),(x,y+d,z+h)]
 faces=[[p[i] for i in ids] for ids in [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]]
 all_faces.extend(faces);all_colors.extend([color]*len(faces))
# All coordinates inches. Rear wall y=0; front projects toward positive y.
box(0,0,0,5.25,28.875,84,'#eee9df')
box(5.25,0,0,.75,28.875,84,'#e9e4d8')
box(42.75,0,0,.75,28.875,84,'#e9e4d8')
box(6,0,71,36.75,28.875,13,'#e9e4d8')
# Body; 1-inch rear gap. Outer doors36 wide; cabinet35.6 wide.
box(6.575,1,0,35.6,28.5,68.3,'#969fa4')
box(6.375,29.5,21,17.9,4.8,49,'#bdc4c7')
box(24.475,29.5,21,17.9,4.8,49,'#adb7bd')
box(6.375,29.5,0,36,4.8,20.6,'#a8b2b7')
box(22.6,34.3,33,.7,2.4,28,'#d6dbdc')
box(25.6,34.3,33,.7,2.4,28,'#d6dbdc')
box(9,34.3,17,30,2.4,.8,'#d6dbdc')
box(43.5,0,0,13.5,24,34.5,'#f1eee7');box(43.5,0,34.5,13.5,25.5,1.5,'#dad9d3')
box(57,0,0,30,27,36,'#a9afb1');box(87,0,0,36,24,34.5,'#f1eee7');box(87,0,34.5,36,25.5,1.5,'#dad9d3')
# Save actual geometric faces as an OBJ, then present unambiguous orthographic views.
obj=[];idx=1
for face in all_faces:
 for pt in face:obj.append('v '+' '.join(map(str,pt)))
 obj.append('f '+' '.join(str(idx+i) for i in range(len(face))));idx+=len(face)
(ROOT/'outputs/review/fridge-36-blockout.obj').write_text('\n'.join(obj)+'\n')
plt.close(fig)
fig=plt.figure(figsize=(15,8),facecolor='#faf8f3')
fig.text(.04,.94,'36-inch refrigerator: dimensioned installation concept',fontsize=21,weight='bold')
fig.text(.04,.90,'Product dimensions verified; room and cabinetry allocations provisional. Original drawings unchanged.',fontsize=11)
def panel(rect,title,xlim,ylim):
 a=fig.add_axes(rect);a.set_aspect('equal');a.set_xlim(*xlim);a.set_ylim(*ylim);a.set_title(title,fontsize=12);a.tick_params(labelsize=8);return a
def rect(a,x,y,w,h,c):a.add_patch(Rectangle((x,y),w,h,facecolor=c,edgecolor='#526066',linewidth=1))
a=panel([.04,.25,.43,.58],'Front elevation — range stays at its original start',(0,123),(0,96))
rect(a,0,0,43.5,84,'#e8e1d5');rect(a,6,0,36.75,71,'#777c7c');rect(a,6.375,0,36,20.6,'#a4afb5');rect(a,6.375,21,17.9,49,'#bec5c8');rect(a,24.475,21,17.9,49,'#bec5c8')
for x in [22.6,25.6]:rect(a,x,33,.7,28,'#56636b')
rect(a,9,17,30,.8,'#56636b');rect(a,43.5,0,13.5,36,'#f1eee7');rect(a,57,0,30,36,'#a4afb5');rect(a,87,0,36,36,'#f1eee7')
a.axhline(70,color='#9a552e',ls=':',lw=1);a.text(60,72,'Fridge top70"',fontsize=9);a.text(6,87,'43.5" enclosure',fontsize=9);a.set_xlabel('Distance from north end (inches)');a.set_ylabel('Height above floor (inches)')
a=panel([.50,.25,.19,.58],'Side section — real depth',(0,42),(0,96))
rect(a,0,0,28.875,84,'#e8e1d5');rect(a,1,0,28.5,68.3,'#a4afb5');rect(a,29.5,0,4.8,70,'#c0c7ca');rect(a,34.3,33,2.4,28,'#56636b');rect(a,34.3,17,2.4,.8,'#56636b');rect(a,0,71,28.875,13,'#e8e1d5');a.axvline(25.5,color='#9a552e',ls='--',lw=1);a.set_xlabel('Depth from rear wall (inches)')
a=panel([.75,.35,.22,.40],'Plan — enclosure and adjacent base',(0,87),(50,0))
rect(a,0,0,43.5,28.875,'#e8e1d5');rect(a,43.5,0,13.5,25.5,'#f1eee7');rect(a,57,0,30,25.5,'#a4afb5');rect(a,6.375,1,36,35.7,'#b1bcc1');a.axhline(25.5,color='#9a552e',ls='--',lw=1);a.set_xlabel('Along run (inches)')
fig.text(.04,.18,'Run: 43.5" fridge/enclosure + 13.5" base + 30" range + 36" base = 123". Counter front remains25.5".',fontsize=12)
fig.text(.04,.13,'Fridge36" W ×70" H ×35.7" D; rear gap1". Panels28 7/8" deep; upper cabinet underside71", top84".',fontsize=11)
fig.text(.04,.08,'Wall-side door sweep and full drawer access still need verification. Not a surveyed installation or matched-camera rendering.',fontsize=11,color='#8c482e')
out=ROOT/'outputs/review/fridge-36-geometry-reference.png';fig.savefig(out,dpi=140,facecolor=fig.get_facecolor());plt.close(fig);print(out)
