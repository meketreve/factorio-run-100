import json, zlib, base64
NORTH,EAST,SOUTH,WEST = 0,4,8,12
VER = 562949955649536
# direction do inserter = lado de ONDE ELE PEGA. Entrega no lado oposto.
FROM_W, FROM_E, FROM_N, FROM_S = WEST, EAST, NORTH, SOUTH

class B:
    def __init__(s): s.e=[]; s.n=0
    def add(s,name,x,y,d=None):
        s.n+=1; o={"entity_number":s.n,"name":name,"position":{"x":x,"y":y}}
        if d is not None and d!=0: o["direction"]=d
        s.e.append(o); return o
    def bp(s,label,icons,desc):
        return {"item":"blueprint","label":label,"description":desc,
                "icons":[{"signal":{"name":i},"index":k+1} for k,i in enumerate(icons)],
                "entities":s.e,"version":VER}

# 01 Coluna de fundicao
b=B()
for y in range(16):
    b.add("transport-belt",0.5,y+0.5,SOUTH)
    b.add("transport-belt",1.5,y+0.5,SOUTH)
    b.add("transport-belt",6.5,y+0.5,SOUTH)
for k in range(8):
    ya,yb=2*k+0.5,2*k+1.5
    b.add("inserter",2.5,ya,FROM_W)
    b.add("long-handed-inserter",2.5,yb,FROM_W)
    b.add("stone-furnace",4,2*k+1)
    b.add("inserter",5.5,ya,FROM_W)
for yb in (3.5,11.5): b.add("medium-electric-pole",5.5,yb)
smelt=b.bp("01 Coluna de fundicao 1:1",["stone-furnace","transport-belt"],
 "8 fornos. x0 carvao, x1 minerio, x6 placas.")

# 02 Mall
b=B()
for y in range(18): b.add("transport-belt",0.5,y+0.5,SOUTH)
for k in range(6):
    yc=3*k+1.5
    b.add("inserter",1.5,yc,FROM_W)
    b.add("assembling-machine-1",3.5,yc)
    b.add("inserter",5.5,yc,FROM_W)
    b.add("wooden-chest",6.5,yc)
for k in (0,3): b.add("medium-electric-pole",1.5,3*k+0.5)
mall=b.bp("02 Mall inicial",["assembling-machine-1","transport-belt"],
 "6 assemblers, saida em bau. Escolha a receita de cada um.")

# 03 Labs
b=B()
for y in range(18): b.add("transport-belt",0.5,y+0.5,SOUTH)
for k in range(6):
    yc=3*k+1.5
    b.add("inserter",1.5,yc,FROM_W)
    b.add("lab",3.5,yc)
for k in (0,3): b.add("medium-electric-pole",1.5,3*k+0.5)
labs=b.bp("03 Bloco de labs",["lab","automation-science-pack"],
 "6 labs, packs entram pela correia.")

# 04 Circuito verde 3:2
b=B()
for y in range(27):
    for x,d in ((0.5,SOUTH),(6.5,SOUTH),(12.5,SOUTH),(13.5,SOUTH)):
        b.add("transport-belt",x,y+0.5,d)
for k in range(9):
    yc=3*k+1.5
    b.add("inserter",1.5,yc,FROM_W)
    b.add("assembling-machine-1",3.5,yc)
    b.add("inserter",5.5,yc,FROM_W)
for k in range(6):
    yc=3*k+1.5
    b.add("inserter",7.5,yc,FROM_W)
    b.add("assembling-machine-1",9.5,yc)
    b.add("inserter",11.5,yc-1,FROM_E)
    b.add("long-handed-inserter",11.5,yc+1,FROM_W)
for y in (0.5,6.5,12.5,18.5,24.5):
    for x in (1.5,7.5,14.5): b.add("medium-electric-pole",x,y)
circ=b.bp("04 Circuito verde 3:2",["electronic-circuit","copper-cable"],
 "9 cabo : 6 circuito. x0 cobre, x6 cabo, x12 ferro, x13 saida.")

# 05 Muralha
b=B()
for x in range(16):
    b.add("stone-wall",x+0.5,0.5)
    b.add("transport-belt",x+0.5,4.5,EAST)
for xt in (2,6,10,14):
    b.add("gun-turret",xt,2)
    b.add("inserter",xt-0.5,3.5,FROM_S)
for x in (3.5,10.5): b.add("medium-electric-pole",x,5.5)
wall=b.bp("05 Muralha + gun turrets",["gun-turret","stone-wall"],
 "16 tiles de muro, 4 torres, municao por correia. Sem laser.")

def enc(o): return "0"+base64.b64encode(zlib.compress(json.dumps(o,separators=(',',':')).encode(),9)).decode()
allb=[smelt,mall,labs,circ,wall]
book={"blueprint_book":{"item":"blueprint-book","label":"Arranque - run 100%",
 "description":"Nauvis antes do foguete. Sem solar, sem laser, sem requester.",
 "icons":[{"signal":{"name":"stone-furnace"},"index":1}],
 "blueprints":[{"index":i,"blueprint":x} for i,x in enumerate(allb)],
 "active_index":0,"version":VER}}
names=["01-fundicao","02-mall","03-labs","04-circuito-verde","05-muralha"]
for nm,x in zip(names,allb):
    s=enc({"blueprint":x}); open(nm+".txt","w").write(s+"\n")
s=enc(book); open("00-livro-arranque.txt","w").write(s+"\n")

# validacao: nomes, sobreposicao e destino de cada inserter
import glob,re
D="/mnt/SSD/SteamLibrary/steamapps/common/Factorio/data"
src="".join(open(f,encoding='utf8',errors='ignore').read() for f in glob.glob(D+"/base/prototypes/**/*.lua",recursive=True))
SIZE={"transport-belt":(1,1),"inserter":(1,1),"long-handed-inserter":(1,1),"medium-electric-pole":(1,1),
      "assembling-machine-1":(3,3),"lab":(3,3),"stone-furnace":(2,2),"wooden-chest":(1,1),
      "stone-wall":(1,1),"gun-turret":(2,2)}
DV={NORTH:(0,-1),EAST:(1,0),SOUTH:(0,1),WEST:(-1,0)}
for x in allb:
    occ={};bad=[]
    for en in x["entities"]:
        nm=en["name"]
        if not re.search(r'name\s*=\s*"'+re.escape(nm)+r'"',src): bad.append("NOME "+nm)
        w,h=SIZE[nm];px,py=en["position"]["x"],en["position"]["y"]
        for dx in range(w):
            for dy in range(h):
                t=(int(px-w/2)+dx,int(py-h/2)+dy)
                if t in occ: bad.append(f"SOBREPOE {t}")
                occ[t]=nm
    for en in x["entities"]:
        if "inserter" not in en["name"]: continue
        r=2 if "long" in en["name"] else 1
        d=DV[en.get("direction",0)];px,py=en["position"]["x"],en["position"]["y"]
        pk=(int(px+d[0]*r),int(py+d[1]*r)); ins=(int(px-d[0]*r),int(py-d[1]*r))
        if occ.get(pk) is None or occ.get(ins) is None:
            bad.append(f"inserter {px},{py}: pega={occ.get(pk)} entrega={occ.get(ins)}")
    print(f"{x['label']:30} {len(x['entities']):3} ent  {'OK' if not bad else bad[:2]}")
print("\nlivro:",len(s),"chars")
