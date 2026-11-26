"""Reel 08 — Perché le aziende italiane non crescono (senza voce: solo testo, effetti e base musicale).
Genera reel-08/index.html + reel-08/sfx.json"""
import json, os, shutil, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # cartella studio/
OUT = BASE + '/reel-08'
os.makedirs(OUT, exist_ok=True)
for f in ('gsap.min.js', 'hyperframes.json', 'package.json'):
    shutil.copy(f'{BASE}/template/{f}', OUT)
json.dump({"id": "reel-08", "name": "reel-08", "createdAt": "2026-11-26T14:40:00Z"}, open(OUT + '/meta.json', 'w'))

D = 57.0
INK, CARTA, TIMBRO, ROSA, SALVIA, OCRA, TENUE = '#2B2A4C', '#EDE6D3', '#A8463B', '#C96F62', '#8FAE95', '#E3B23C', '#4A4966'
BLU = '#4F7CAC'

def P(x, y, s=1.0, fill=INK, idn='', cls='', glasses=False):
    """omino con i piedi in (x,y)"""
    g = (f'<circle cx="0" cy="-58" r="15" fill="{fill}"/>'
         f'<path d="M-19,0 L-19,-24 Q-19,-40 0,-40 Q19,-40 19,-24 L19,0 Z" fill="{fill}"/>')
    if glasses:
        g += '<rect x="-14" y="-63" width="28" height="7" rx="2" fill="#111"/>'
    i = f' id="{idn}"' if idn else ''
    c = f' class="{cls}"' if cls else ''
    return f'<g transform="translate({x} {y}) scale({s})"><g{i}{c}>{g}</g></g>'

# ---------- didascalie ----------
caps = []
def cap(i, s, e, top, size, html, style=''): caps.append((i, s, e, top, size, html, style))
cap('k1', 3.75, 6.6, 300, 72, 'Su <em>100</em> aziende italiane…')
cap('k2', 6.65, 10.55, 300, 72, '…quasi <em>85</em> sono di famiglia.')
cap('k3', 10.65, 13.1, 300, 66, 'E quelle guidate da un <em>manager esterno</em>?')
cap('k4', 13.15, 15.5, 300, 72, '<em>1,6</em> su 100.')
cap('k5', 15.7, 17.6, 300, 80, 'Comanda <em>papà</em>.')
cap('k6', 17.65, 19.3, 300, 80, 'Poi il <em>figlio</em>.')
cap('k7', 19.35, 20.95, 300, 80, 'Poi il <em>nipote</em>.')
cap('k8', 21.1, 23.45, 300, 70, 'Papà il controllo <em>non lo molla</em>.')
cap('k9', 23.5, 26.35, 300, 62, 'Un socio? Un fondo? Un manager <em>più bravo di lui</em>?')
cap('k10', 28.5, 31.2, 300, 64, 'Niente soldi nuovi. Niente competenze nuove.')
cap('k11', 31.25, 33.2, 300, 70, '…e l&#39;azienda <em>resta piccola</em>.')
cap('k12', 33.25, 35.5, 300, 64, '<em>3 su 4</em> hanno meno di 10 persone.')
cap('k13', 35.75, 38.2, 300, 64, 'Attenzione: le aziende di famiglia <em>non sono il male</em>.')
cap('k14', 38.25, 42.3, 300, 62, 'Però crescono poco. E producono meno <em>per ogni persona</em>.')
cap('k15', 42.5, 44.8, 300, 72, 'Sai quando crescono <em>davvero</em>?')
cap('k16', 44.85, 47.5, 300, 68, 'Quando entra un <em>socio da fuori</em>.')
cap('k17', 47.7, 49.3, 300, 70, 'Non è che non possono crescere.')
cap('k18', 49.35, 51.3, 300, 80, 'È che <em>papà non vuole</em>.')
NOTTE = {'k13', 'k14'}
capd = ''.join(f'<div id="{i}" class="cap clip{" nt" if i in NOTTE else ""}" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="{10+n}" style="top:{t}px;font-size:{sz}px;{st}">{h}</div>'
               for n, (i, s, e, t, sz, h, st) in enumerate(caps))
capjs = ''
for (i, s, e, t, sz, h, st) in caps:
    capjs += f'tl.fromTo("#{i}",{{opacity:0,y:34}},{{opacity:1,y:0,duration:.35,ease:"power3.out"}},{s});'
    capjs += f'tl.to("#{i}",{{opacity:0,y:-20,duration:.2,ease:"power2.in"}},{round(e-0.22,2)});'

# ---------- S1-S2: griglia 100 aziende ----------
NONFAM = {3, 17, 22, 38, 41, 56, 64, 79, 83, 95, 9, 48, 70, 27, 88}   # 15 non familiari
MGR = {48, 70}                                                        # ~1,6 su 100 con manager
om = ''
for k in range(100):
    x, y = 180 + (k % 10) * 80, 700 + (k // 10) * 78
    cls = 'om ' + ('mgr' if k in MGR else ('fam' if k not in NONFAM else 'nf'))
    om += P(x, y, 0.85, INK, f'g{k}', cls)
grid = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{om}</svg>'
        '<div class="ml" id="src1" style="left:120px;top:1440px">fonte · Istat, censimento imprese 2025</div>'
        '<div class="stamp big bgp" id="s85" style="left:250px;top:860px">84,6%</div>'
        '<div class="ml" id="lmg" style="left:120px;top:1440px;color:#B8892A">■ manager esterno</div>'
        '<div class="stamp big bgp" id="s16" style="left:290px;top:860px">1,6%</div>')

# ---------- S3: dinastia ----------
crown = f'<g id="crown"><path d="M-42,0 L-46,-46 L-22,-22 L0,-54 L22,-22 L46,-46 L42,0 Z" fill="{OCRA}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/></g>'
dyn = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
       f'<line x1="120" y1="1380" x2="960" y2="1380" stroke="{INK}" stroke-width="5"/>'
       + P(260, 1380, 3.2, INK, 'd0') + P(560, 1380, 2.6, TENUE, 'd1') + P(820, 1380, 2.0, ROSA, 'd2') + crown +
       '</svg>'
       '<div class="ml dl" id="dl0" style="left:160px">papà</div>'
       '<div class="ml dl" id="dl1" style="left:460px">figlio</div>'
       '<div class="ml dl" id="dl2" style="left:720px">nipote</div>')

# ---------- S4: la porta ----------
door = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
        f'<line x1="100" y1="1380" x2="980" y2="1380" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="dr" x="830" y="1050" width="140" height="330" fill="{INK}"/>'
        f'<rect x="820" y="1040" width="160" height="12" fill="{INK}"/>'
        + P(720, 1380, 3.0, INK, 'pp') + P(170, 1380, 2.3, SALVIA, 'v0') + P(340, 1380, 2.3, OCRA, 'v1')
        + P(510, 1380, 2.3, BLU, 'v2', glasses=True) +
        '</svg>'
        '<div class="ml vl" id="vl0" style="left:90px">socio</div>'
        '<div class="ml vl" id="vl1" style="left:260px">fondo</div>'
        '<div class="ml vl" id="vl2" style="left:430px">manager</div>'
        '<div class="coin" id="eur4" style="left:125px;top:1040px">€</div>'
        '<div class="stamp huge" id="cc">COL CAZZO.</div>')

# ---------- S5: resta piccola ----------
def house(x, s, col, idn, lab):
    return (f'<g transform="translate({x} 1380) scale({s})"><g id="{idn}" class="hs">'
            f'<path d="M-60,0 L-60,-80 L0,-130 L60,-80 L60,0 Z" fill="{col}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="-16" y="-42" width="32" height="42" fill="{INK}"/></g></g>')
small = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
         f'<line x1="100" y1="1380" x2="980" y2="1380" stroke="{INK}" stroke-width="5"/>'
         f'<rect id="bld" x="390" y="1180" width="300" height="200" fill="{ROSA}" stroke="{INK}" stroke-width="6"/>'
         + house(200, 1.2, ROSA, 'h0', '') + house(420, 1.2, ROSA, 'h1', '') + house(640, 1.2, ROSA, 'h2', '')
         + house(860, 1.7, SALVIA, 'h3', '') +
         '</svg>'
         '<div class="stamp mid" id="x1" style="left:130px;top:700px">✗ soldi</div>'
         '<div class="stamp mid" id="x2" style="left:520px;top:830px">✗ competenze</div>'
         '<div class="ml hl8" id="hl0" style="left:140px">&lt; 10</div><div class="ml hl8" id="hl1" style="left:360px">&lt; 10</div>'
         '<div class="ml hl8" id="hl2" style="left:580px">&lt; 10</div><div class="ml hl8" id="hl3" style="left:800px">10 +</div>'
         '<div class="stamp big bgp" id="s76" style="left:300px;top:720px">76%</div>')

# ---------- S6: non sono il male (notte) ----------
pros = ('<div class="pc ok" id="p0" style="left:120px;top:700px">+ più redditizie</div>'
        '<div class="pc ok" id="p1" style="left:120px;top:880px">+ chiudono meno</div>'
        '<div class="pc ko" id="p2" style="left:120px;top:1080px">− più piccole</div>'
        '<div class="pc ko" id="p3" style="left:120px;top:1260px">− meno produttive</div>'
        '<div class="ml" id="src6" style="left:120px;top:1440px;color:#cfc8b6">fonte · Banca d&#39;Italia, QEF n. 1068 (2026)</div>')

# ---------- S7: socio da fuori ----------
grow = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
        f'<line x1="100" y1="1380" x2="980" y2="1380" stroke="{INK}" stroke-width="5"/>'
        + P(230, 1380, 2.4, INK, 'p7') + P(400, 1380, 2.4, OCRA, 'o7') +
        f'<rect id="b71" x="580" y="1180" width="150" height="200" fill="{SALVIA}" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="b72" x="790" y="1180" width="150" height="200" fill="{SALVIA}" stroke="{INK}" stroke-width="5"/>'
        '</svg>'
        '<div class="ml" id="bl1" style="left:560px;top:1395px;width:190px;text-align:center;font-size:24px">occupati</div>'
        '<div class="ml" id="bl2" style="left:765px;top:1395px;width:200px;text-align:center;font-size:24px">produttività</div>'
        '<div class="ml" id="ol7" style="left:300px;top:1395px;width:200px;text-align:center;font-size:24px;color:#B8892A">socio esterno</div>'
        '<div class="stamp mid" id="up7" style="left:600px;top:640px;color:#5E8A69;border-color:#5E8A69">CRESCONO ↑</div>')

# ---------- S8: papà non vuole ----------
nope = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
        f'<line x1="100" y1="1400" x2="980" y2="1400" stroke="{INK}" stroke-width="5"/>'
        + P(330, 1400, 4.2, INK, 'p8') +
        '</svg>'
        '<div class="stamp big" id="no8" style="left:560px;top:820px;font-size:190px">NO.</div>')

# ---------- finale ----------
fin = ('<div class="stamp big" id="seg" style="left:120px;top:760px">SEGUIMI</div>'
       '<div class="ml" id="nx" style="left:120px;top:960px;font-size:34px">prossimo episodio →<br/><span style="color:#2B2A4C;font-family:var(--serif);font-size:64px;text-transform:none;letter-spacing:0">Cosa succede quando<br/>papà va in pensione</span></div>')

css_base = open('/tmp/base_css.txt').read().replace('{{', '{').replace('}}', '}')
CSS = css_base + '''
.bgp{background:#F6F1E4}
.dl{top:1400px;width:200px;text-align:center}
.vl{top:1135px;width:160px;text-align:center}
.hl8{top:1400px;width:120px;text-align:center}
.coin{position:absolute;width:90px;height:90px;border-radius:50%;background:#E3B23C;border:6px solid #2B2A4C;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:48px;font-weight:600}
#bg6{position:absolute;inset:0;background:var(--ink)}
.pc{position:absolute;width:840px;height:140px;border-radius:14px;display:flex;align-items:center;padding:0 40px;font-size:76px;font-weight:500;border:6px solid}
.pc.ok{color:#8FAE95;border-color:#8FAE95}
.pc.ko{color:#E9B8AE;border-color:#C96F62}
'''
JS = r'''
const tl = gsap.timeline({ paused: true });
const shake=(t,a=8)=>tl.to("#root",{x:a,duration:.05,yoyo:true,repeat:3,ease:"none"},t);
const stamp=(sel,t,r)=>{tl.fromTo(sel,{opacity:0,scale:2.2,rotation:-14},{opacity:1,scale:1,rotation:r,duration:.24,ease:"power4.in"},t-0.24);shake(t);};
const rise=(sel,t,d=.35)=>tl.fromTo(sel,{opacity:0,y:30},{opacity:1,y:0,duration:d,ease:"power3.out"},t);
const popin=(sel,t,st=0)=>tl.fromTo(sel,{opacity:0,scale:0,transformOrigin:"50% 100%"},{opacity:1,scale:1,duration:.3,ease:"back.out(2.2)",stagger:st},t);
tl.fromTo("#prog",{scaleX:0},{scaleX:1,duration:DUR,ease:"none"},0);
// HOOK
rise("#h1",0.05,.3); rise("#h2",0.75,.3); stamp("#hx",1.7,-5);
tl.to("#hx",{scale:1.08,duration:.18,yoyo:true,repeat:1},2.1);
tl.to("#notte",{y:-1920,duration:.55,ease:"power3.inOut"},3.15);
// S1 griglia
tl.set(["#src1","#s85","#lmg","#s16"],{opacity:0},0);
popin(".om",3.9,.012); rise("#src1",4.6);
tl.to(".fam *, .mgr *",{attr:{fill:"#C96F62"},duration:.12,stagger:.008},6.9);
stamp("#s85",8.9,-6);
tl.to("#s85",{opacity:0,scale:.8,duration:.25},10.3);
// S2 manager
tl.to(".fam, .nf",{opacity:.15,duration:.4},11.3);
tl.to(".mgr *",{attr:{fill:"#E3B23C"},duration:.2},11.6);
tl.to(".mgr",{scale:1.8,transformOrigin:"50% 100%",duration:.35,ease:"back.out(2)"},11.6);
tl.to("#src1",{opacity:0,duration:.2},11.3); rise("#lmg",12.0);
stamp("#s16",13.4,-5);
// S3 dinastia
tl.set(["#d0","#d1","#d2","#crown",".dl"],{opacity:0},0);
popin("#d0",15.75); rise("#dl0",15.95);
tl.set("#crown",{x:260,y:1130},0);
tl.fromTo("#crown",{opacity:0,y:1030},{opacity:1,y:1130,duration:.35,ease:"bounce.out"},16.2);
popin("#d1",17.7); rise("#dl1",17.85);
tl.to("#crown",{x:560,y:1180,rotation:360,duration:.5,ease:"power2.inOut"},17.95);
popin("#d2",19.4); rise("#dl2",19.55);
tl.to("#crown",{x:820,y:1225,rotation:720,duration:.5,ease:"power2.inOut"},19.6);
tl.to("#crown",{scale:1.2,duration:.15,yoyo:true,repeat:1},20.15);
// S4 la porta
tl.set(["#pp","#v0","#v1","#v2",".vl","#eur4","#cc"],{opacity:0},0);
popin("#pp",21.2);
tl.to("#pp",{rotation:-6,transformOrigin:"50% 100%",duration:.25,yoyo:true,repeat:3,ease:"sine.inOut"},22.0);
tl.fromTo("#v0",{opacity:0,x:-300},{opacity:1,x:0,duration:.45,ease:"power3.out"},23.6); rise("#vl0",23.9); tl.fromTo("#eur4",{opacity:0,y:-40},{opacity:1,y:0,duration:.35,ease:"bounce.out"},24.0);
tl.fromTo("#v1",{opacity:0,x:-300},{opacity:1,x:0,duration:.45,ease:"power3.out"},24.4); rise("#vl1",24.7);
tl.fromTo("#v2",{opacity:0,x:-300},{opacity:1,x:0,duration:.45,ease:"power3.out"},25.2); rise("#vl2",25.5);
stamp("#cc",26.6,-5); shake(26.65,16);
tl.to(["#v0","#v1","#v2"],{x:-700,y:-400,rotation:-540,transformOrigin:"50% 50%",duration:.8,ease:"power2.in",stagger:.07},27.0);
tl.to([".vl","#eur4"],{opacity:0,duration:.2},27.0);
// S5 resta piccola
tl.set(["#x1","#x2",".hs",".hl8","#s76"],{opacity:0},0);
tl.fromTo("#bld",{attr:{y:1380,height:0}},{attr:{y:1180,height:200},duration:.4,ease:"power2.out"},28.6);
stamp("#x1",29.4,-6); stamp("#x2",30.3,4);
tl.to(["#x1","#x2"],{opacity:0,duration:.2},31.1);
tl.to("#bld",{attr:{y:760,height:620},duration:.55,ease:"power2.out"},31.35);
tl.to("#bld",{attr:{y:1220,height:160},duration:.7,ease:"elastic.out(1,.35)"},32.0);
tl.to("#bld",{opacity:0,duration:.25},33.05);
popin(".hs",33.3,.1); rise(".hl8",33.6);
tl.to(["#h0","#h1","#h2"],{y:-14,duration:.12,yoyo:true,repeat:1,stagger:.1},34.0);
stamp("#s76",34.5,-5);
// S6 notte
tl.set([".pc","#src6"],{opacity:0},0);
tl.fromTo("#bg6",{y:1920},{y:0,duration:.5,ease:"power3.inOut"},35.55);
tl.fromTo(["#p0","#p1"],{opacity:0,x:-60},{opacity:1,x:0,duration:.35,ease:"back.out(1.8)",stagger:.45},36.5);
rise("#src6",37.2);
tl.fromTo(["#p2","#p3"],{opacity:0,x:60},{opacity:1,x:0,duration:.35,ease:"back.out(1.8)",stagger:.9},38.6);
tl.to("#p3",{scale:1.05,duration:.18,yoyo:true,repeat:1},40.6);
tl.to("#bg6",{y:-1920,duration:.5,ease:"power3.inOut"},42.15);
tl.to([".pc","#src6"],{y:-1920,duration:.5,ease:"power3.inOut"},42.15);
// S7 socio da fuori
tl.set(["#p7","#o7","#b71","#b72","#bl1","#bl2","#ol7","#up7"],{opacity:0},0);
popin("#p7",42.6);
tl.fromTo("#o7",{opacity:1,x:-500},{x:0,duration:.6,ease:"power2.out"},44.9); rise("#ol7",45.3);
tl.set(["#b71","#b72"],{opacity:1},45.2); rise(["#bl1","#bl2"],45.3);
tl.fromTo("#b71",{attr:{y:1380,height:0}},{attr:{y:1180,height:200},duration:.3},45.2);
tl.fromTo("#b72",{attr:{y:1380,height:0}},{attr:{y:1180,height:200},duration:.3},45.2);
tl.to("#b71",{attr:{y:820,height:560},duration:.8,ease:"power3.out"},45.7);
tl.to("#b72",{attr:{y:760,height:620},duration:.8,ease:"power3.out"},45.85);
stamp("#up7",46.7,-4);
// S8 no
tl.set(["#p8","#no8"],{opacity:0},0);
popin("#p8",47.8);
tl.to("#p8",{rotation:-5,transformOrigin:"50% 100%",duration:.3,yoyo:true,repeat:3,ease:"sine.inOut"},48.2);
stamp("#no8",49.6,-8); shake(49.65,16);
// FINALE
tl.set(["#seg","#nx"],{opacity:0},0);
stamp("#seg",51.6,-4);
rise("#nx",52.2);
tl.to("#nx",{x:10,duration:.6,yoyo:true,repeat:1,ease:"sine.inOut"},52.9);
tl.to(["#seg","#nx"],{opacity:0,duration:.25},54.6);
tl.fromTo("#logo",{opacity:0,y:30},{opacity:1,y:0,duration:.45},54.9);
stamp("#lst",55.6,-4);
'''.replace('DUR', str(D))

html = f'''<!doctype html>
<html lang="it" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="gsap.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920">
<div id="righe" class="clip" data-start="0" data-duration="{D}" data-track-index="0"></div>
<div id="margine" class="clip" data-start="0" data-duration="{D}" data-track-index="1"></div>

<div id="sGr" class="sc clip" data-start="3.6" data-duration="12.0" data-track-index="2">{grid}</div>
<div id="sDy" class="sc clip" data-start="15.6" data-duration="5.45" data-track-index="3">{dyn}</div>
<div id="sDo" class="sc clip" data-start="21.05" data-duration="7.4" data-track-index="4">{door}</div>
<div id="sSm" class="sc clip" data-start="28.45" data-duration="7.2" data-track-index="5">{small}</div>
<div id="sMa" class="sc clip" data-start="35.5" data-duration="7.2" data-track-index="6"><div id="bg6"></div>{pros}</div>
<div id="sGo" class="sc clip" data-start="42.4" data-duration="5.25" data-track-index="7">{grow}</div>
<div id="sNo" class="sc clip" data-start="47.65" data-duration="3.75" data-track-index="8">{nope}</div>
<div id="sFin" class="sc clip" data-start="51.4" data-duration="3.5" data-track-index="9">{fin}</div>
<div id="logo" class="clip" data-start="54.9" data-duration="{round(D-54.9,2)}" data-track-index="39">Economia <span id="lst" class="stamp">Capita</span></div>

{capd}

<div id="notte" class="clip" data-start="0" data-duration="3.7" data-track-index="40">
 <div id="hk">
  <div id="h1">In Italia</div>
  <div id="h2">il capo è</div>
  <div id="hx">PAPÀ.</div>
 </div>
</div>
<div id="prog" class="clip" data-start="0" data-duration="{D}" data-track-index="60"></div>
</div>
<script>
{JS}
{capjs}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>'''
html = html.replace('#hx4', '#hx')
open(OUT + '/index.html', 'w').write(html)

# ---------- effetti sonori (tempi assoluti) ----------
fx = [('whoosh', 0.0, -8), ('pop', 0.05, -6), ('pop', 0.75, -6), ('stamp', 1.7, 2), ('rumble', 1.7, -6),
      ('whoosh', 3.15, -4), ('rise', 3.9, -10), ('tick', 4.6, -6), ('rise', 6.9, -6), ('stamp', 8.9, 0),
      ('whoosh', 11.3, -8), ('ching', 11.6, -4), ('stamp', 13.4, 0),
      ('pop', 15.75, -4), ('drop', 16.2, -8), ('tick', 16.5, -2), ('pop', 17.7, -4), ('whoosh', 17.95, -6), ('pop', 19.4, -4), ('whoosh', 19.6, -6), ('ching', 20.15, -6),
      ('pop', 21.2, -6), ('whoosh', 23.6, -6), ('ching', 24.0, -6), ('whoosh', 24.4, -6), ('whoosh', 25.2, -6),
      ('stamp', 26.6, 2), ('rumble', 26.6, -2), ('whoosh', 27.0, 0),
      ('pop', 28.6, -6), ('stamp', 29.4, 0), ('stamp', 30.3, 0), ('rise', 31.35, -4), ('drop', 32.0, -2),
      ('pop', 33.3, -8), ('pop', 33.4, -8), ('pop', 33.5, -8), ('pop', 33.6, -8), ('stamp', 34.5, 0),
      ('whoosh', 35.55, -4), ('pop', 36.5, -6), ('pop', 36.95, -6), ('drop', 38.6, -8), ('drop', 39.5, -8),
      ('whoosh', 42.15, -4), ('pop', 42.6, -6), ('whoosh', 44.9, -4), ('rise', 45.6, -4), ('stamp', 46.7, 0),
      ('pop', 47.8, -6), ('stamp', 49.6, 2), ('rumble', 49.6, -4),
      ('stamp', 51.6, 0), ('whoosh', 54.6, -8), ('jingle_out', 54.8, -3), ('stamp', 55.6, -2)]
json.dump(fx, open(OUT + '/sfx.json', 'w'))
print('ok', OUT)
