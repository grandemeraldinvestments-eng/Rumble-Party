# Turn one quarter of a 2x2 texture sheet into a seamless tile.
# usage: tile.py sheet.png quarter(0-3) out.webp [mode] [size]     mode: blend (default, for scattered patterns) | planks (boards running left to right) | mirror (for regular patterns)
import sys
import numpy as np
from PIL import Image
src,q,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]; mode=sys.argv[4] if len(sys.argv)>4 else 'blend'; size=int(sys.argv[5]) if len(sys.argv)>5 else 256
im=Image.open(src).convert('RGB'); W,H=im.size; w,h=W//2,H//2; x0,y0=(q%2)*w,(q//2)*h; pad=int(w*.05)
T=np.asarray(im.crop((x0+pad,y0+pad,x0+w-pad,y0+h-pad))).astype(float)
if mode=='planks':
    dark=T.mean(axis=(1,2)); thr=dark.mean()-1.2*dark.std(); rows=np.where(dark<thr)[0]      # the seams between boards are the darkest rows
    groups=np.split(rows,np.where(np.diff(rows)>3)[0]+1); mids=[int(g.mean()) for g in groups if len(g)]
    T=T[mids[0]:mids[-1]]                                                                    # whole boards only, seam to seam
    T=np.concatenate([T,T[:,::-1]],axis=1)                                                   # mirror left-right so the grain meets itself
    res=Image.fromarray(T.astype('uint8')).resize((size*2,size),Image.LANCZOS)
elif mode=='mirror':
    T=np.concatenate([T,T[:,::-1]],axis=1); T=np.concatenate([T,T[::-1]],axis=0)      # flipped copies meet edge to edge
    res=Image.fromarray(T.astype('uint8')).resize((size,size),Image.LANCZOS)
else:
    n=min(T.shape[0],T.shape[1]); T=T[:n,:n]; S=np.roll(T,(n//2,n//2),axis=(0,1))            # the same picture moved half a tile, so its middle sits on the edges
    a=np.abs(np.linspace(-1,1,n)); e=np.clip((1-a)/.3,0,1); e=e*e*(3-2*e); m=np.minimum.outer(e,e)[:,:,None]   # keep the original in the middle, fade to the moved copy at the edges
    res=Image.fromarray((T*m+S*(1-m)).astype('uint8')).resize((size,size),Image.LANCZOS)
res.save(out,quality=86,method=6); print(out,res.size)
