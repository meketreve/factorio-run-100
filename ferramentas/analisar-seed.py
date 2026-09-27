from PIL import Image
import math,sys,os
WATER={(51,83,95),(38,64,73)}; NEST=(255,25,25)
RES={"ferro":(106,134,148),"cobre":(205,99,55),"carvao":(0,0,0),"pedra":(176,156,109)}
C=256;SZ=512
def cls(p):
    if p in WATER: return "agua"
    if p==NEST: return "nest"
    r,g,b=p
    if g>r+6 and g>b+6: return "arvore"
    for k,c in RES.items():
        if abs(r-c[0])+abs(g-c[1])+abs(b-c[2])<45: return k
    return None
for f in sys.argv[1:]:
    im=Image.open(f).convert("RGB"); d=list(im.getdata())
    lut={c:cls(c) for n,c in im.getcolors(maxcolors=1<<22)}
    cnt={k:0 for k in list(RES)+["arvore"]}; mind={k:999.0 for k in RES}
    nest=999.0; t150=0; tot150=0
    for i,p in enumerate(d):
        k=lut[p]; x=i%SZ-C; y=i//SZ-C; dd=math.sqrt(x*x+y*y)
        if k=="nest":
            nest=min(nest,dd); continue
        if dd<=150:
            tot150+=1
            if k=="arvore": t150+=1
        if k is None or dd>220: continue
        if k in cnt: cnt[k]+=1
        if k in mind: mind[k]=min(mind[k],dd)
    ch=[]
    for R in (100,140,180):
        idx=[]
        for kk in range(720):
            a=kk*math.pi/360
            x=int(C+R*math.cos(a)); y=int(C+R*math.sin(a))
            if 0<=x<SZ and 0<=y<SZ: idx.append(y*SZ+x)
        ch.append(round(sum(1 for i in idx if lut[d[i]]=="agua")/len(idx),3))
    print(f"\n{os.path.basename(f)}")
    print(f"  arvore(r150) {100*t150/max(tot150,1):5.1f}%   ninho {nest:5.0f}   agua no perimetro {ch} media {sum(ch)/3:.3f}")
    print("  area:", {k:cnt[k] for k in RES}, " dist:", {k:round(v) for k,v in mind.items()})
