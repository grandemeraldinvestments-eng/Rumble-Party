# Cut a 2x2 sheet of platform tops (seen from above) into square textures that the platform shape fills edge to edge.
# usage: tops.py sheet.png outdir name1,name2,name3,name4 [size]
import sys,os,subprocess,tempfile
from PIL import Image
src,out,names=sys.argv[1],sys.argv[2],sys.argv[3]; size=int(sys.argv[4]) if len(sys.argv)>4 else 512
tmp=tempfile.mkdtemp(); here=os.path.dirname(os.path.abspath(__file__))
subprocess.check_call([sys.executable,'-I',os.path.join(here,'slice.py'),src,'2','2',tmp,names,'640','tight'],stdout=subprocess.DEVNULL)
os.makedirs(out,exist_ok=True)
for n in names.split(','):
    im=Image.open(f'{tmp}/{n}.png'); print(n,im.size); im.resize((size,size),Image.LANCZOS).save(f'{out}/top-{n}.webp',quality=88,method=6)
