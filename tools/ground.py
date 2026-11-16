# Prepare a painted arena surrounding: fade its edges to transparent so it melts into the repeating floor underneath.
# usage: ground.py painting.png out.webp [size] [sides]     sides: fade only the left and right edges, for a painting that repeats along a long course
import sys
import numpy as np
from PIL import Image
src,out=sys.argv[1],sys.argv[2]; size=int(sys.argv[3]) if len(sys.argv)>3 else 1024
im=Image.open(src).convert('RGB').resize((size,size),Image.LANCZOS); A=np.asarray(im)
a=np.abs(np.linspace(-1,1,size)); r=np.sqrt(np.add.outer(a**4,a**4))**.5
if len(sys.argv)>4 and sys.argv[4]=='sides': r=np.tile(a,(size,1))     # rounded-square distance: 0 in the middle, 1 at the edges
al=np.clip((1-r)/.16,0,1); al=al*al*(3-2*al)
Image.fromarray(np.dstack([A,(al*255).astype('uint8')])).save(out,quality=84,method=6); print(out,size)
