import re,math
from collections import defaultdict
D="/mnt/SSD/SteamLibrary/steamapps/common/Factorio/data"
PLAYER={"crafting","hand-crafting"}
REC={}
for f in ["/base/prototypes/recipe.lua","/space-age/prototypes/recipe.lua"]:
    s=open(D+f,encoding='utf8',errors='ignore').read()
    for blk in s.split('type = "recipe"')[1:]:
        nm=re.search(r'name\s*=\s*"([^"]+)"',blk)
        if not nm: continue
        name=nm.group(1)
        cat=re.search(r'\bcategory\s*=\s*"([^"]+)"',blk)
        cats=re.search(r'categories\s*=\s*\{([^}]*)\}',blk)
        c=set()
        if cat: c.add(cat.group(1))
        if cats: c|=set(re.findall(r'"([^"]+)"',cats.group(1)))
        if not c: c={"crafting"}
        ib=re.search(r'ingredients\s*=\s*\n?\s*\{(.*?)\n?\s*\}\s*,\s*\n\s*results',blk,re.S)
        rb=re.search(r'results\s*=\s*\{(.*?)\}\s*[,\n]',blk,re.S)
        if not ib or not rb: continue
        ing=[(m.group(1),int(m.group(2))) for m in re.finditer(
            r'type\s*=\s*"item",\s*name\s*=\s*"([^"]+)",\s*amount\s*=\s*(\d+)',ib.group(1))]
        res=[(m.group(1),int(m.group(2))) for m in re.finditer(
            r'type\s*=\s*"item",\s*name\s*=\s*"([^"]+)",\s*amount\s*=\s*(\d+)',rb.group(1))]
        if not res or name!=res[0][0] or name in REC: continue
        REC[name]={"cats":c,"ing":ing,"out":res[0][1],"fluid":"fluid" in ib.group(1)}

def hc(i):
    r=REC.get(i); return bool(r) and bool(r["cats"]&PLAYER) and not r["fluid"]

LISTA=[("burner-mining-drill",1),("stone-furnace",1),("boiler",1),("steam-engine",1),
       ("offshore-pump",1),("small-electric-pole",1),("lab",1),
       ("automation-science-pack",10),("assembling-machine-1",1)]

def custo(pool_sobras):
    sobra=defaultdict(int); feitos=defaultdict(int); total=0
    def obter(item,qty):
        nonlocal total
        if not hc(item): return          # minerado ou fundido: nao conta
        if pool_sobras:
            usa=min(sobra[item],qty); sobra[item]-=usa; qty-=usa
        if qty<=0: return
        r=REC[item]
        crafts=math.ceil(qty/r["out"]); feito=crafts*r["out"]
        for ing,amt in r["ing"]: obter(ing,amt*crafts)
        total+=feito; feitos[item]+=feito
        if pool_sobras: sobra[item]+=feito-qty
    for it,q in LISTA: obter(it,q)
    return total,feitos

for pool in (False,True):
    t,f=custo(pool)
    rot="com reaproveitamento de sobras" if pool else "sem reaproveitar sobras"
    print(f"\n=== {rot}: TOTAL {t}  (limite 111, folga {111-t}) ===")
    for k,v in sorted(f.items(),key=lambda x:-x[1]): print(f"   {k:26} {v:4}")

print("\n\n########## VARIANTES ##########")
VAR={
 "A) original do texto": LISTA,
 "B) sem as 10 ciencias na mao": [x for x in LISTA if x[0]!="automation-science-pack"],
 "C) sem ciencia e sem lab (assembler faz o lab)":
     [x for x in LISTA if x[0] not in ("automation-science-pack","lab")],
 "D) sem ciencia, lab sim, 2 brocas a queimador":
     [x for x in LISTA if x[0]!="automation-science-pack"]+[("burner-mining-drill",1)],
 "E) so o basico ate o assembler (sem lab, sem ciencia, 2 fornalhas extras)":
     [("burner-mining-drill",2),("stone-furnace",2),("boiler",1),("steam-engine",1),
      ("offshore-pump",1),("small-electric-pole",1),("assembling-machine-1",1)],
 "F) E + lab": [("burner-mining-drill",2),("stone-furnace",2),("boiler",1),("steam-engine",1),
      ("offshore-pump",1),("small-electric-pole",1),("assembling-machine-1",1),("lab",1)],
}
import copy
for nome,lst in VAR.items():
    LISTA=lst
    t,f=custo(True)
    flag="OK " if t<=111 else "NAO"
    print(f"{flag} {nome:52} {t:4} crafts   folga {111-t:+d}")
