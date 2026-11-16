# Cut a transparent grid sheet into square, centred, equal-sized icons. usage: slice.py sheet.png rows cols outdir name1,name2,... [size]
import sys, os
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage
src,rows,cols,out,names=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],sys.argv[5].split(',')
size=int(sys.argv[6]) if len(sys.argv)>6 else 256
tight=len(sys.argv)>7 and sys.argv[7]=='tight'   # tight: keep the object's own shape (for standees) instead of padding it to a square
im=Image.open(src).convert('RGBA'); W,H=im.size; A=np.array(im); a0=A[:,:,3].astype(float)
A[:,:,3]=np.clip((a0-20)/(210-20),0,1)*255; im=Image.fromarray(A); a=A[:,:,3]   # generated sheets come slightly see-through: stretch alpha so solid areas are fully solid
print('alpha hist: 0=%d 1-200=%d 201-254=%d 255=%d'%((a==0).sum(),((a>0)&(a<=200)).sum(),((a>200)&(a<255)).sum(),(a==255).sum()))
mask=a>24; lab,n=ndimage.label(mask); boxes={}
for i,sl in enumerate(ndimage.find_objects(lab),1):
    area=(lab[sl]==i).sum()
    if area<40: continue
    cy,cx=ndimage.center_of_mass(lab==i) if area>2000 else ((sl[0].start+sl[0].stop)/2,(sl[1].start+sl[1].stop)/2)
    key=(min(rows-1,int(cy*rows/H)),min(cols-1,int(cx*cols/W)))
    b=boxes.get(key); y0,y1,x0,x1=sl[0].start,sl[0].stop,sl[1].start,sl[1].stop
    boxes[key]=(y0,y1,x0,x1) if not b else (min(b[0],y0),max(b[1],y1),min(b[2],x0),max(b[3],x1))
os.makedirs(out,exist_ok=True)
for r in range(rows):
    for c in range(cols):
        k=r*cols+c
        if k>=len(names) or not names[k] or (r,c) not in boxes: continue
        y0,y1,x0,x1=boxes[(r,c)]; crop=im.crop((x0,y0,x1,y1)); w,h=crop.size; s=int(max(w,h)*1.06)
        if tight: f=size/max(w,h); sq=crop.resize((max(1,round(w*f)),max(1,round(h*f))),Image.LANCZOS)
        else:
            sq=Image.new('RGBA',(s,s),(0,0,0,0)); sq.paste(crop,((s-w)//2,(s-h)//2)); sq=sq.resize((size,size),Image.LANCZOS)
        sq.save(f'{out}/{names[k]}.png'); sq.save(f'{out}/{names[k]}.webp',quality=88,method=6)
        print(names[k],(w,h),os.path.getsize(f'{out}/{names[k]}.webp'))
