"""
Motor de programas Firenze Fit
Uso: python tools/motor.py 12 2026-11 2027-12
Gera data/gXX/{catalogo.json, index.json, AAAA-MM.json, status.json} usando SÓ os aparelhos do grupo.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from catalogo import X, EQUIP, GRUPOS, POOLS, SO_INT, MOB, MOBX

MESES = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
PORTATIL = {"halter_leve","halter","colchonete","bola_suica","caixote","banco"}

def D(id, nome, foco, mob, *slots): return dict(id=id, nome=nome, foco=foco, mob=mob, slots=[s.split(':') for s in slots])
FB3 = [D("A","Full body A","Pernas, peito, costas","geral","quad:C","peito:C","costas_v:C","post_iso:I","ombro_lat:I","core:K"),
       D("B","Full body B","Costas, ombros, posterior","geral","post:C","costas_h:C","ombro:C","quad_iso:I","peito_iso:I","core:K"),
       D("C","Full body C","Glúteo, braços, pernas","geral","uni:C","costas_v:C","peito_inc:C","gluteo:C","biceps:I","triceps:I","pant:I")]
SPLITS = {
 "hipertrofia": {
  "iniciante": [FB3],
  "intermediario": [
   [D("A","Peito e tríceps","Peito, tríceps","superior","peito:C","peito_inc:C","peito_iso:I","triceps:I","triceps:I"),
    D("B","Costas e bíceps","Costas, bíceps","superior","costas_v:C","costas_h:C","costas_h:C","costas_iso:I","biceps:I","biceps:I"),
    D("C","Pernas – quadríceps","Quadríceps, glúteo, panturrilha","inferior","quad:C","quad:C","uni:C","quad_iso:I","pant:I"),
    D("D","Ombros, posterior e glúteo","Ombros, posterior, glúteo","geral","ombro:C","ombro_lat:I","ombro_post:I","post:C","post_iso:I","gluteo:C")],
   [D("A","Superiores 1","Peito, costas, ombros","superior","peito:C","costas_v:C","ombro:C","costas_h:C","ombro_lat:I","triceps:I"),
    D("B","Inferiores 1","Quadríceps e panturrilha","inferior","quad:C","uni:C","quad_iso:I","post_iso:I","pant:I","core:K"),
    D("C","Superiores 2","Costas, peito, braços","superior","costas_h:C","peito_inc:C","costas_v:C","peito_iso:I","biceps:I","triceps:I"),
    D("D","Inferiores 2","Glúteo e posterior","inferior","gluteo:C","post:C","quad:C","post_iso:I","abdutor:I","core:K")]],
  "avancado": [
   [D("A","Push – empurrar","Peito, ombros, tríceps","superior","peito:C","peito_inc:C","ombro:C","ombro_lat:I","triceps:I","triceps:I"),
    D("B","Pull – puxar","Costas, bíceps, posterior de ombro","superior","costas_v:C","costas_h:C","costas_v:C","ombro_post:I","biceps:I","biceps:I"),
    D("C","Legs – pernas","Quadríceps, posterior, glúteo","inferior","quad:C","quad:C","post:C","quad_iso:I","post_iso:I","pant:I"),
    D("D","Upper – superiores","Peito, costas, braços","superior","peito:C","costas_h:C","peito_iso:I","costas_iso:I","biceps:I","triceps:I","core:K"),
    D("E","Lower – glúteo e posterior","Glúteo, posterior, adutores","inferior","gluteo:C","uni:C","post_iso:I","abdutor:I","adutor:I","pant:I")],
   [D("A","Peito","Peito e core","superior","peito:C","peito_inc:C","peito:C","peito_iso:I","core:K"),
    D("B","Costas","Costas e trapézio","superior","costas_v:C","costas_h:C","costas_v:C","costas_iso:I","trap:I"),
    D("C","Pernas","Quadríceps e posterior","inferior","quad:C","quad:C","uni:C","quad_iso:I","post_iso:I","pant:I"),
    D("D","Ombros","Ombros completos","superior","ombro:C","ombro_lat:I","ombro_post:I","ombro_lat:I","core:K"),
    D("E","Braços e glúteo","Bíceps, tríceps, glúteo","geral","gluteo:C","biceps:I","triceps:I","biceps:I","triceps:I","abdutor:I")]]},
 "emagrecimento": {
  "iniciante": [FB3],
  "intermediario": [
   [D("A","Superiores A","Peito, costas, braços","superior","peito:C","costas_h:C","peito_inc:C","costas_v:C","biceps:I","triceps:I","core:K"),
    D("B","Inferiores A","Pernas e glúteo","inferior","quad:C","post_iso:I","quad_iso:I","post:C","abdutor:I","adutor:I","core:K"),
    D("C","Superiores B","Ombros, costas, braços","superior","costas_v:C","ombro:C","peito_iso:I","ombro_post:I","triceps:I","biceps:I","core:K"),
    D("D","Inferiores B","Glúteo e posterior","inferior","quad:C","uni:C","gluteo:C","post_iso:I","pant:I","core:K")],
   [D("A","Empurrar","Peito, ombros, tríceps","superior","peito:C","ombro:C","peito_inc:C","ombro_lat:I","triceps:I","core:K"),
    D("B","Pernas","Quadríceps e glúteo","inferior","quad:C","uni:C","quad_iso:I","gluteo:C","pant:I","core:K"),
    D("C","Puxar","Costas, bíceps","superior","costas_v:C","costas_h:C","costas_iso:I","ombro_post:I","biceps:I","core:K"),
    D("D","Glúteo e posterior","Glúteo, posterior, adutores","inferior","post:C","gluteo:C","post_iso:I","abdutor:I","adutor:I","core:K")]],
  "avancado": [
   [D("A","Circuito superiores","Peito, costas, ombros","superior","peito:C","costas_h:C","ombro_lat:I","costas_v:C","costas_iso:I","ombro_post:I","core:K"),
    D("B","Circuito inferiores","Pernas e glúteo","inferior","quad:C","uni:C","uni:C","quad:C","pant:I","core:K"),
    D("C","Força – full body","Corpo inteiro (dia mais pesado)","geral","quad:C","peito:C","costas_h:C","post:C"),
    D("D","Ombros e braços","Ombros, bíceps, tríceps","superior","ombro:C","ombro_post:I","biceps:I","triceps:I","biceps:I","triceps:I","core:K"),
    D("E","Glúteo metabólico","Glúteo e posterior","inferior","gluteo:C","abdutor:I","adutor:I","post_iso:I","quad_iso:I","core:K")],
   [D("A","Superiores 1","Peito e costas","superior","peito:C","costas_v:C","peito_inc:C","costas_h:C","ombro_lat:I","core:K"),
    D("B","Inferiores 1","Quadríceps","inferior","quad:C","uni:C","quad_iso:I","post_iso:I","pant:I","core:K"),
    D("C","Full body força","Corpo inteiro","geral","quad:C","peito:C","costas_v:C","post:C"),
    D("D","Superiores 2","Ombros e braços","superior","ombro:C","costas_h:C","ombro_post:I","biceps:I","triceps:I","core:K"),
    D("E","Inferiores 2","Glúteo e posterior","inferior","gluteo:C","post:C","uni:C","abdutor:I","adutor:I","core:K")]]},
}
FREQ = {"iniciante":3,"intermediario":4,"avancado":5}
CICLO = {
 ("hipertrofia","iniciante"):["adapt","base","cadencia","progressao"],
 ("hipertrofia","intermediario"):["piramide","base","biset","drop","piramide_dec","cadencia"],
 ("hipertrofia","avancado"):["piramide+drop","biset","restpause","triset","piramide_dec+drop","forca"],
 ("emagrecimento","iniciante"):["adapt","biset","base","cadencia"],
 ("emagrecimento","intermediario"):["biset","triset","base","biset+drop"],
 ("emagrecimento","avancado"):["triset","biset","forca+triset","triset+drop"],
}
NOMES = {"adapt":"Adaptação","base":"Séries tradicionais","cadencia":"Cadência controlada","progressao":"Progressão de volume",
 "piramide":"Pirâmide crescente","piramide_dec":"Pirâmide decrescente","biset":"Bi-sets","triset":"Tri-sets","drop":"Drop-set",
 "restpause":"Rest-pause","forca":"Força"}
DESCR = {"adapt":"Mês de aprender os movimentos com carga confortável.","base":"Séries fixas e descanso regular para construir base.",
 "cadencia":"Mais tempo sob tensão: desça sempre em 3 segundos.","progressao":"Os exercícios principais ganham uma série a mais.",
 "piramide":"No principal, a carga sobe e as repetições caem a cada série.","piramide_dec":"Comece pesado no principal e alivie a carga a cada série.",
 "biset":"Dois exercícios seguidos, sem pausa; descanso só no fim da dupla.","triset":"Três exercícios seguidos, sem pausa; descanso no fim da volta.",
 "drop":"Na última série dos isoladores, reduza a carga e continue até a falha.","restpause":"No principal: faça as repetições, pause 15 s e continue mais duas vezes.",
 "forca":"Cargas altas e descanso longo nos exercícios principais."}
BASE = {
 ("hipertrofia","iniciante"):{"C":(3,"12",75),"I":(3,"12",60),"K":(3,"30s",45)},
 ("hipertrofia","intermediario"):{"C":(4,"10",90),"I":(3,"12",60),"K":(3,"40s",45)},
 ("hipertrofia","avancado"):{"C":(4,"8",120),"I":(3,"12",60),"K":(3,"15",45)},
 ("emagrecimento","iniciante"):{"C":(3,"15",45),"I":(3,"15",45),"K":(3,"30s",30)},
 ("emagrecimento","intermediario"):{"C":(3,"15",45),"I":(3,"15",40),"K":(3,"40s",30)},
 ("emagrecimento","avancado"):{"C":(4,"12",45),"I":(3,"15",30),"K":(3,"45s",30)},
}
CARDIO = {"hipertrofia":{"iniciante":10,"intermediario":12,"avancado":10},"emagrecimento":{"iniciante":20,"intermediario":22,"avancado":25}}

def compat(a, b):
    ea, eb = set(X[a]["equip"]), set(X[b]["equip"])
    return bool((ea & eb) - {"anilhas"}) or ea <= PORTATIL or eb <= PORTATIL

def mlist(ini, fim):
    y, m = map(int, ini.split('-')); out = []
    while f"{y}-{m:02d}" <= fim:
        out.append(f"{y}-{m:02d}"); m += 1
        if m > 12: y, m = y+1, 1
    return out

def build(g, mk, midx):
    eq = set(GRUPOS[g]["equip"]); disp = {k for k, e in X.items() if set(e["equip"]) <= eq}
    progs = {}
    for obj in SPLITS:
        progs[obj] = {}
        for lvl in SPLITS[obj]:
            variants = SPLITS[obj][lvl]; split = variants[(midx // 3) % len(variants)]
            ciclo = CICLO[(obj, lvl)]; met = ciclo[midx % len(ciclo)].split('+'); base = BASE[(obj, lvl)]; dias = []
            for di, d in enumerate(split):
                usados, items = set(), []
                for k, (pool, papel) in enumerate(d["slots"]):
                    cand = [e for e in POOLS[pool] if e in disp and (lvl != "iniciante" or e not in SO_INT)]
                    if not cand: continue
                    start = (midx + di*2 + k) % len(cand)
                    pick = next((cand[(start+j) % len(cand)] for j in range(len(cand)) if cand[(start+j) % len(cand)] not in usados), None)
                    if not pick: continue
                    usados.add(pick); s, r, ds = base[papel]
                    if "progressao" in met and papel == "C": s += 1
                    if "forca" in met and papel == "C": s, r, ds = 4, "6", (150 if obj == "hipertrofia" else 90)
                    items.append(dict(ex=pick, papel=papel, series=s, reps=r, desc=ds, tipo="normal"))
                c0 = next((it for it in items if it["papel"] == "C"), None)
                if c0 and "piramide" in met: c0.update(tipo="piramide", series=4, reps="12 / 10 / 8 / 6", obs="Suba a carga a cada série")
                if c0 and "piramide_dec" in met: c0.update(tipo="piramide", series=4, reps="6 / 8 / 10 / 12", obs="Comece pesado e alivie a carga a cada série")
                if c0 and "restpause" in met: c0.update(tipo="restpause", series=3, reps="8 + máx + máx", obs="Faça 8, pause 15 s, faça o máximo; pause 15 s e repita")
                if "cadencia" in met:
                    for it in items:
                        if it["papel"] != "K": it["obs"] = "Desça em 3 segundos"
                if "drop" in met:
                    for it in [i for i in items if i["papel"] == "I"][-2:]:
                        it.update(tipo="drop", reps=it["reps"] + " + drop", obs="Última série: reduza ~30% da carga e vá até a falha")
                n = 3 if "triset" in met else (2 if "biset" in met else 1)
                blocos, i = [], 0
                while i < len(items):
                    grp = [items[i]]
                    if n > 1 and items[i]["tipo"] == "normal":
                        j = i + 1
                        while j < len(items) and len(grp) < n and items[j]["tipo"] == "normal" and all(compat(items[j]["ex"], x["ex"]) for x in grp):
                            grp.append(items[j]); j += 1
                    if len(grp) > 1:
                        ser = max(x["series"] for x in grp)
                        for x in grp[:-1]: x["desc"] = 0
                        for x in grp: x["series"] = ser
                        grp[-1]["desc"] = max(grp[-1]["desc"], 60)
                    tipo = {1: grp[0]["tipo"], 2: "biset", 3: "triset"}[len(grp)]
                    blocos.append(dict(tipo=tipo, exs=[{k: v for k, v in x.items() if k in ("ex","series","reps","desc","obs")} for x in grp]))
                    i += len(grp)
                cmin = CARDIO[obj][lvl]; interv = obj == "emagrecimento" and lvl != "iniciante" and midx % 2 == 1
                cardio = dict(min=cmin, intens=("Intervalado: 1 min forte / 1 min leve" if interv else ["Leve (consegue conversar)","Moderado (fala com esforço)"][(midx+di) % 2]),
                              obs="Use o aparelho de cardio que estiver livre")
                ml = MOB[d["mob"]]; mob = [ml[(midx + t) % len(ml)] for t in range(4)]
                dias.append(dict(id=d["id"], nome=d["nome"], foco=d["foco"], mob=mob, blocos=blocos, cardio=cardio))
            progs[obj][lvl] = dict(dinamica=" + ".join(NOMES[x] for x in met), descricao=" ".join(DESCR[x] for x in met), freq=FREQ[lvl], dias=dias)
    y, m = mk.split('-')
    return dict(grupo=g, mes=mk, titulo=f"{MESES[int(m)-1]} {y}", programas=progs)

def estimate(d):
    s = 6*60 + d["cardio"]["min"]*60
    for b in d["blocos"]: s += b["exs"][0]["series"] * (len(b["exs"])*45 + b["exs"][-1]["desc"])
    return s/60

def catalogo_grupo(g):
    eq = set(GRUPOS[g]["equip"]); disp = {k: dict(e) for k, e in X.items() if set(e["equip"]) <= eq}
    for k, e in disp.items():
        alt = e["alt"] if e["alt"] in disp and set(disp[e["alt"]]["equip"]) != set(e["equip"]) else None
        if not alt:
            pool = next((p for p in POOLS.values() if k in p), [])
            alt = next((o for o in pool if o in disp and o != k and set(disp[o]["equip"]) != set(e["equip"])), None)
        e["alt"] = alt
    mob = {k: v for k, v in MOBX.items() if v["equip"] in eq}
    return disp, mob

def run(g, ini, fim):
    out = f"data/g{g}"; os.makedirs(out + "/fotos", exist_ok=True)
    cat, mob = catalogo_grupo(g); erros, avisos = [], []
    meses = mlist(ini, fim)
    for mk in meses:
        midx = (int(mk[:4])*12 + int(mk[5:])) - (2026*12 + 11)
        P = build(g, mk, midx)
        for obj, nv in P["programas"].items():
            for lvl, pr in nv.items():
                if len(pr["dias"]) != pr["freq"]: erros.append(f"{mk} {obj}/{lvl}: dias≠freq")
                for d in pr["dias"]:
                    ids = [x["ex"] for b in d["blocos"] for x in b["exs"]]
                    if len(ids) != len(set(ids)): erros.append(f"{mk} {obj}/{lvl}/{d['id']}: repetido")
                    if len(ids) < 4: erros.append(f"{mk} {obj}/{lvl}/{d['id']}: poucos exercícios")
                    for x in ids:
                        if x not in cat: erros.append(f"{mk}: {x} não existe no grupo")
                    for m in d["mob"]:
                        if m not in mob: erros.append(f"{mk}: mobilidade {m} sem equipamento")
                    if estimate(d) > 75: avisos.append(f"{mk} {obj}/{lvl}/{d['id']}: ~{estimate(d):.0f} min")
        json.dump(P, open(f"{out}/{mk}.json","w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
    for e in cat.values():
        if not e["alt"]: avisos.append(f"sem alternativo: {e['id']}")
    G = GRUPOS[g]
    existentes = sorted(f[:-5] for f in os.listdir(out) if len(f) == 12 and f[4] == '-' and f.endswith('.json'))
    json.dump(dict(versao=2, exercicios=cat, mobilidade=mob, equipamentos={k: EQUIP[k] for k in G["equip"]}, detalhes=G.get("detalhes",{})),
              open(f"{out}/catalogo.json","w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
    json.dump(dict(grupo=g, nome=G["nome"], torres=G["torres"], obs=G.get("obs",""), meses=existentes,
                   fotos=["capa","ambiente2","ambiente_cardio","grama","halter"]),
              open(f"{out}/index.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    if not os.path.exists(f"{out}/status.json"):
        json.dump(dict(manutencao=[], aviso=""), open(f"{out}/status.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    if erros: print("ERROS:\n" + "\n".join(erros)); sys.exit(1)
    print(f"Grupo {g}: {len(meses)} meses ({meses[0]} a {meses[-1]}), {len(cat)} exercícios, {len(mob)} de mobilidade. OK")
    if avisos: print("Avisos:\n" + "\n".join(sorted(set(avisos))))

if __name__ == "__main__":
    a = sys.argv + [None]*4
    run(a[1] or "12", a[2] or "2026-11", a[3] or "2027-12")
