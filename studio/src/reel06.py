"""Reel 05 — Under 25 disoccupati ×4. Genera reel-06/index.html + reel-06/sfx.json"""
import json, os, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # cartella studio/
OUT = BASE + '/reel-06'
os.makedirs(OUT, exist_ok=True)
for f in ('gsap.min.js', 'hyperframes.json', 'package.json'):
    shutil.copy(f'{BASE}/template/{f}', OUT)
json.dump({"id": "reel-06", "name": "reel-06", "createdAt": "2026-11-18T18:10:00Z"}, open(OUT + '/meta.json', 'w'))

D = 57.4
INK, CARTA, TIMBRO, ROSA, SALVIA, OCRA, TENUE = '#2B2A4C', '#EDE6D3', '#A8463B', '#C96F62', '#8FAE95', '#E3B23C', '#4A4966'

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

D = 60.2
caps = []
def cap(i, s, e, top, size, html, style=''): caps.append((i, s, e, top, size, html, style))
cap('k0', 5.0, 11.45, 300, 62, 'Stipendio medio annuo, lordo, a tempo pieno.')
cap('k1', 11.55, 14.2, 300, 80, '«Eh, ma i tedeschi sono più bravi.»')
cap('k2', 15.3, 20.3, 300, 66, 'Stesso falegname. In Italia: bottega da 4, <em>un trapano</em>.')
cap('k3', 20.4, 23.45, 300, 66, 'In Germania: azienda da 100, <em>piena di macchine</em>.')
cap('k4', 23.5, 27.25, 300, 70, 'Chi fa più tavoli in un&#39;ora? <em>Quello con le macchine.</em>')
cap('k5', 27.3, 29.3, 300, 80, 'E lo stipendio <em>segue i tavoli</em>.')
cap('k6', 29.4, 33.5, 300, 64, 'In Italia il <em>95%</em> delle imprese ha meno di 10 addetti.')
cap('k7', 33.55, 37.6, 300, 64, 'Ci lavora quasi <em>1 lavoratore su 2</em>. In Germania, 1 su 5.')
cap('k8', 37.7, 42.95, 300, 64, 'Valore prodotto per addetto, all&#39;anno:')
cap('k9', 43.0, 51.0, 300, 64, 'Salari reali dal 1990 al 2020 (cioè tolta l&#39;inflazione):')
cap('k10', 51.1, 54.2, 300, 84, 'Non sei scarso.')
cap('k11', 54.28, 58.4, 300, 62, 'Nel prossimo: perché le aziende italiane <em>non crescono mai</em>.')
NOTTE = {'k6', 'k7', 'k8'}
capd = ''.join(f'<div id="{i}" class="cap clip{" nt" if i in NOTTE else ""}" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="{10+n}" style="top:{t}px;font-size:{sz}px;{st}">{h}</div>'
               for n, (i, s, e, t, sz, h, st) in enumerate(caps))
capjs = ''.join(f'tl.fromTo("#{i}",{{opacity:0,y:34}},{{opacity:1,y:0,duration:.35,ease:"power3.out"}},{s});tl.to("#{i}",{{opacity:0,y:-20,duration:.2,ease:"power2.in"}},{round(e-0.22,2)});'
                for (i, s, e, t, sz, h, st) in caps)

# --- scena barre stipendi
bars = ('<div class="ml" id="src" style="left:120px;top:600px">fonte · Eurostat, 2025</div>'
        f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true"><line x1="120" y1="1450" x2="960" y2="1450" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="bDE" x="200" y="750" width="260" height="700" fill="{SALVIA}" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="bIT" x="620" y="1022" width="260" height="428" fill="{ROSA}" stroke="{INK}" stroke-width="5"/></svg>'
        '<div class="ml" style="left:200px;top:1475px;width:260px;text-align:center">Germania</div>'
        '<div class="ml" style="left:620px;top:1475px;width:260px;text-align:center">Italia</div>'
        '<div class="val" id="vDE" style="left:110px;top:675px;width:440px">0</div>'
        '<div class="val" id="vIT" style="left:530px;top:947px;width:440px">0</div>'
        '<div class="stamp mid ocra2" id="gap" style="left:560px;top:700px">+22.000 €</div>')
# --- stronzate
stron = '<div class="stamp huge" id="str">STRONZATE.</div>'
# --- falegname
def table(x, y, idn):
    return f'<g id="{idn}" class="tb" transform="translate({x} {y})"><rect x="-38" y="-30" width="76" height="12" fill="{OCRA}" stroke="{INK}" stroke-width="4"/><line x1="-30" y1="-18" x2="-30" y2="8" stroke="{INK}" stroke-width="5"/><line x1="30" y1="-18" x2="30" y2="8" stroke="{INK}" stroke-width="5"/></g>'
itp = ''.join(P(170 + k * 80, 1000, 0.9, INK, f'i{k}', 'ip') for k in range(4))
dep = ''.join(P(600 + (k % 6) * 60, 940 + (k // 6) * 120, 0.62, INK, f'd{k}', 'dp') for k in range(18))
drill = f'<g id="drill" transform="translate(330 1120)"><rect x="-50" y="-22" width="80" height="40" rx="8" fill="{ROSA}" stroke="{INK}" stroke-width="5"/><rect x="30" y="-8" width="40" height="12" fill="{INK}"/><rect x="-40" y="18" width="30" height="50" rx="6" fill="{ROSA}" stroke="{INK}" stroke-width="5"/></g>'
gears = ''.join(f'<g class="gear" transform="translate({x} 1180)"><circle r="34" fill="none" stroke="{INK}" stroke-width="10" stroke-dasharray="14 9"/><circle r="12" fill="{INK}"/></g>' for x in (640, 740, 840, 940))
tabsIT = ''.join(table(190 + k * 110, 1350, f'ti{k}') for k in range(2))
tabsDE = ''.join(table(620 + (k % 4) * 100, 1290 + (k // 4) * 70, f'td{k}') for k in range(8))
fale = ('<div class="pan" style="left:110px">ITALIA · bottega da 4</div><div class="pan" style="left:570px">GERMANIA · azienda da 100</div>'
        f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true"><line x1="540" y1="820" x2="540" y2="1480" stroke="{INK}" stroke-width="4" stroke-dasharray="12 12"/>'
        f'{itp}{drill}{dep}{gears}{tabsIT}{tabsDE}</svg>'
        '<div class="cnt2" id="cIT" style="left:110px">2 tavoli</div><div class="cnt2" id="cDE" style="left:570px">8 tavoli</div>'
        '<div class="stamp mid" id="eIT" style="left:150px;top:1580px">€</div><div class="stamp mid" id="eDE" style="left:610px;top:1580px">€€€€</div>')
# --- micro imprese (notte)
row = lambda pref, n_on, y: ''.join(P(170 + k * 80, y, 0.75, '#4A4966', f'{pref}{k}', pref) for k in range(10))
micro = ('<div id="bg2"></div><div class="big2" id="n95">0%</div><div class="ml nt2" id="l95" style="left:120px;top:830px">delle imprese italiane: meno di 10 addetti</div>'
         f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{row("ri",5,1180)}{row("rd",2,1430)}</svg>'
         '<div class="ml nt2" id="lri" style="left:120px;top:1000px">Italia · lavoratori in microimprese</div>'
         '<div class="ml nt2" id="lrd" style="left:120px;top:1250px">Germania</div>'
         '<div class="hb2" id="hb1" style="top:620px"><div class="ml nt2">microimpresa</div><div class="hbar2" id="m1"></div><div class="hv2">30.000 €</div></div>'
         '<div class="hb2" id="hb2" style="top:860px"><div class="ml nt2">grande impresa</div><div class="hbar2" id="m2"></div><div class="hv2">72.680 €</div></div>'
         '<div class="stamp mid ocra2" id="x2" style="left:560px;top:1100px">più del doppio</div>'
         '<div class="ml nt2" id="srcm" style="left:120px;top:1560px">fonti · Istat, Prometeia, BNL</div>')
# --- salari reali: grafico
Xs = lambda y: 160 + (y - 1990) * 26
Yv = lambda v: 1200 - v * 14
it = [(1990, 0), (1995, -1), (2000, 2), (2005, 3), (2010, 2), (2015, -1), (2020, -2.9)]
de = [(1990, 0), (1995, 6), (2000, 11), (2005, 12), (2010, 17), (2015, 26), (2020, 33.4)]
pth = lambda pts: 'M' + ' L'.join(f'{Xs(y):.0f},{Yv(v):.0f}' for y, v in pts)
graf = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true"><line x1="140" y1="{Yv(0)}" x2="960" y2="{Yv(0)}" stroke="{INK}" stroke-width="4" stroke-dasharray="10 10"/>'
        f'<path id="lIT" d="{pth(it)}" fill="none" stroke="{ROSA}" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>'
        f'<path id="lDE" d="{pth(de)}" fill="none" stroke="{SALVIA}" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>'
        + ''.join(f'<text x="{Xs(y)}" y="1290" font-family="IBM Plex Mono" font-size="28" fill="#4A4966" text-anchor="middle">{y}</text>' for y in (1990, 2000, 2010, 2020)) +
        '</svg><div class="stamp mid" id="sIT" style="left:760px;top:1320px">−3%</div>'
        '<div class="stamp mid ocra2" id="sDE" style="left:740px;top:620px;color:#5E8A69;border-color:#5E8A69">+33%</div>'
        '<div class="ml" id="lgI" style="left:160px;top:1340px"><b style="color:#C96F62">■</b> Italia   <b style="color:#8FAE95">■</b> Germania</div>'
        '<div class="ml" style="left:160px;top:1400px;font-size:24px">fonte · OCSE</div>')
bott = '<div class="stamp big" id="bot" style="left:110px;top:760px;font-size:96px">SEI IN UNA<br/>BOTTEGA.</div>'
fin = ('<div class="stamp big" id="seg" style="left:120px;top:700px">SEGUIMI</div>'
       '<div class="ml" id="nx" style="left:120px;top:930px;font-size:34px">prossimo episodio →<br/><span style="color:#2B2A4C;font-family:var(--serif);font-size:64px;text-transform:none;letter-spacing:0">Perché le aziende<br/>italiane non crescono</span></div>')

head = open('/tmp/r5_head.txt').read() if False else None
CSS = '''
:root{--carta:#EDE6D3;--ink:#2B2A4C;--tenue:#4A4966;--timbro:#A8463B;--rosa:#C96F62;--salvia:#8FAE95;--ocra:#E3B23C;
--serif:"EB Garamond",Georgia,serif;--mono:"IBM Plex Mono",monospace}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--carta)}
#root{position:relative;width:100%;height:100%;font-family:var(--serif);color:var(--ink);overflow:hidden}
#righe{position:absolute;inset:0;background-image:repeating-linear-gradient(to bottom,transparent 0 63px,rgba(43,42,76,.08) 63px 64px)}
#margine{position:absolute;top:0;bottom:0;left:84px;width:2px;background:rgba(168,70,59,.35)}
.cap{position:absolute;left:120px;right:170px;line-height:1.06;font-weight:500;letter-spacing:-.01em;z-index:5}
.cap.nt{color:var(--carta)} .cap.nt em{color:var(--ocra)}
em{font-style:italic;color:var(--timbro)}
.sc{position:absolute;inset:0}
svg.g{position:absolute;inset:0;width:1080px;height:1920px}
.ml{position:absolute;font-family:var(--mono);font-size:30px;letter-spacing:.06em;text-transform:uppercase;color:var(--tenue);line-height:1.35}
.nt2{color:#cfc8b6}
.stamp{position:absolute;display:inline-block;color:var(--timbro);border:7px solid var(--timbro);border-radius:10px;padding:0 22px 8px;font-weight:600;line-height:1.05;white-space:nowrap}
.stamp.big{font-size:150px} .stamp.mid{font-size:64px;border-width:6px;padding:2px 18px 6px}
.stamp.huge{font-size:128px;left:110px;top:800px;border-width:9px}
.stamp.ocra2{color:var(--ocra);border-color:var(--ocra)}
#notte{position:absolute;inset:0;background:var(--ink);color:var(--carta)}
#notte em{color:var(--ocra)}
#hk{position:absolute;left:120px;right:110px;top:500px;display:flex;flex-direction:column;gap:34px;font-size:112px;line-height:1.0;font-weight:500;letter-spacing:-.015em}
#hx{display:inline-block;color:var(--ocra);border:9px solid var(--ocra);border-radius:10px;padding:0 26px 10px;font-weight:600;font-size:118px;width:fit-content;line-height:1;font-family:var(--mono);white-space:nowrap}
.val{position:absolute;font-family:var(--mono);font-size:54px;font-weight:500;text-align:center;white-space:nowrap}
.pan{position:absolute;top:700px;width:420px;font-family:var(--mono);font-size:28px;letter-spacing:.06em;color:var(--tenue)}
.cnt2{position:absolute;top:1420px;width:420px;font-family:var(--mono);font-size:48px;font-weight:500}
#bg2{position:absolute;inset:0;background:var(--ink)}
.big2{position:absolute;left:120px;top:540px;font-family:var(--mono);font-size:260px;font-weight:500;color:var(--ocra);letter-spacing:-.04em;line-height:1}
.hb2{position:absolute;left:120px;width:840px}
.hb2 .ml{position:static} .hbar2{height:90px;width:820px;transform-origin:0 50%;background:var(--ocra);margin-top:12px}
#m1{background:var(--rosa)}
.hv2{font-family:var(--mono);font-size:52px;font-weight:500;color:var(--carta);margin-top:10px}
#logo{position:absolute;left:0;right:0;top:880px;text-align:center;font-size:110px;font-weight:500}
#logo .stamp{position:relative;font-size:110px;border-width:7px;padding:0 22px 8px}
#prog{position:absolute;left:0;bottom:0;height:10px;width:1080px;background:var(--timbro);transform-origin:0 50%;z-index:50}
'''
JS = r'''
const tl = gsap.timeline({ paused: true });
const shake=(t,a=8)=>tl.to("#root",{x:a,duration:.05,yoyo:true,repeat:3,ease:"none"},t);
const stamp=(sel,t,r)=>{tl.fromTo(sel,{opacity:0,scale:2.2,rotation:-14},{opacity:1,scale:1,rotation:r,duration:.24,ease:"power4.in"},t-0.24);shake(t);};
const rise=(sel,t,d=.35)=>tl.fromTo(sel,{opacity:0,y:30},{opacity:1,y:0,duration:d,ease:"power3.out"},t);
const popin=(sel,t,st=0)=>tl.fromTo(sel,{opacity:0,scale:0,transformOrigin:"50% 100%"},{opacity:1,scale:1,duration:.3,ease:"back.out(2.2)",stagger:st},t);
const count=(sel,to,t,d,fmt)=>{const o={v:0};tl.to(o,{v:to,duration:d,ease:"power2.out",onUpdate:()=>{document.querySelector(sel).textContent=fmt(o.v);}},t);};
const eur=v=>Math.round(v).toLocaleString("it-IT")+" €";
tl.fromTo("#prog",{scaleX:0},{scaleX:1,duration:DUR,ease:"none"},0);
// HOOK
rise("#h1",0.05,.3); stamp("#hx",2.0,-4); rise("#h2",2.25,.3);
tl.fromTo("#h2 em",{opacity:0},{opacity:1,duration:.2},3.1);
tl.to("#notte",{y:-1920,duration:.55,ease:"power3.inOut"},4.3);
// BARRE
tl.set(["#src","#gap","#vDE","#vIT"],{opacity:0},0);
rise("#src",5.3);
tl.fromTo("#bDE",{scaleY:0,transformOrigin:"50% 100%"},{scaleY:1,duration:.9,ease:"power3.out"},7.0);
tl.set("#vDE",{opacity:1},7.2); count("#vDE",56000,7.2,1.6,v=>"> "+eur(v));
tl.fromTo("#bIT",{scaleY:0,transformOrigin:"50% 100%"},{scaleY:1,duration:.8,ease:"power3.out"},9.6);
tl.set("#vIT",{opacity:1},9.8); count("#vIT",34213,9.8,1.2,eur);
stamp("#gap",11.05,-6);
// STRONZATE
tl.set("#str",{opacity:0},0); stamp("#str",14.35,-5); shake(14.4,16);
// FALEGNAME
tl.set([".pan",".ip","#drill",".dp",".gear",".tb",".cnt2","#eIT","#eDE"],{opacity:0},0);
rise(".pan",15.45,.35);
popin(".ip",17.0,.1); popin("#drill",19.65);
popin(".dp",20.7,.03); popin(".gear",22.0,.08);
tl.to(".gear",{rotation:720,transformOrigin:"50% 50%",duration:6,ease:"none"},22.3);
popin("#ti0",24.3); popin("#ti1",25.6);
popin(["#td0","#td1","#td2","#td3","#td4","#td5","#td6","#td7"],24.0,.3);
rise(".cnt2",26.4);
stamp("#eIT",27.7,-5); stamp("#eDE",28.3,-5);
// MICRO
tl.set(["#n95","#l95",".ri",".rd","#lri","#lrd",".hb2","#x2","#srcm"],{opacity:0},0);
tl.fromTo("#bg2",{y:1920},{y:0,duration:.5,ease:"power3.inOut"},29.3);
tl.set("#n95",{opacity:1},30.1); count("#n95",95,30.1,.9,v=>Math.round(v)+"%");
rise("#l95",31.0);
tl.to(["#n95","#l95"],{opacity:0,duration:.25},33.4);
rise("#lri",33.6); popin(".ri",33.7,.04);
tl.to(["#ri0 *","#ri1 *","#ri2 *","#ri3 *","#ri4 *"],{attr:{fill:"#E3B23C"},duration:.12,stagger:.1},34.3);
rise("#lrd",35.8); popin(".rd",35.9,.04);
tl.to(["#rd0 *","#rd1 *"],{attr:{fill:"#E3B23C"},duration:.12,stagger:.1},36.7);
tl.to([".ri",".rd","#lri","#lrd"],{opacity:0,duration:.25},37.55);
tl.set("#hb1",{opacity:1},38.4); tl.fromTo("#m1",{scaleX:0},{scaleX:0.413,duration:.6,ease:"power3.out"},38.5);
tl.set("#hb2",{opacity:1},41.2); tl.fromTo("#m2",{scaleX:0},{scaleX:1,duration:.7,ease:"power3.out"},41.3);
stamp("#x2",42.3,-5); rise("#srcm",39.0);
// GRAFICO
tl.set(["#sIT","#sDE","#lgI"],{opacity:0},0);
rise("#lgI",43.6);
["#lIT","#lDE"].forEach(s=>{const p=document.querySelector(s);const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L;});
tl.to("#lIT",{strokeDashoffset:0,duration:3.6,ease:"none"},44.0);
stamp("#sIT",48.1,-5);
tl.to("#lDE",{strokeDashoffset:0,duration:1.8,ease:"power1.inOut"},48.6);
stamp("#sDE",50.45,-5);
// BOTTEGA
tl.set("#bot",{opacity:0},0); stamp("#bot",52.95,-4); shake(53.0,14);
// FINALE
tl.set(["#seg","#nx"],{opacity:0},0); stamp("#seg",54.5,-4); rise("#nx",55.1);
tl.to(["#seg","#nx"],{opacity:0,duration:.25},58.2);
tl.fromTo("#logo",{opacity:0,y:30},{opacity:1,y:0,duration:.45},58.45);
stamp("#lst",59.1,-4);
'''
html = f'''<!doctype html>
<html lang="it" data-resolution="portrait"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920">
<div id="righe" class="clip" data-start="0" data-duration="{D}" data-track-index="0"></div>
<div id="margine" class="clip" data-start="0" data-duration="{D}" data-track-index="1"></div>
<div id="sBar" class="sc clip" data-start="4.9" data-duration="6.6" data-track-index="2">{bars}</div>
<div id="sStr" class="sc clip" data-start="11.5" data-duration="3.75" data-track-index="3">{stron}</div>
<div id="sFal" class="sc clip" data-start="15.2" data-duration="14.1" data-track-index="4">{fale}</div>
<div id="sMic" class="sc clip" data-start="29.3" data-duration="13.7" data-track-index="5">{micro}</div>
<div id="sGra" class="sc clip" data-start="43.0" data-duration="8.1" data-track-index="6">{graf}</div>
<div id="sBot" class="sc clip" data-start="51.1" data-duration="3.1" data-track-index="7">{bott}</div>
<div id="sFin" class="sc clip" data-start="54.2" data-duration="4.25" data-track-index="8">{fin}</div>
<div id="logo" class="clip" data-start="58.45" data-duration="{round(D-58.45,2)}" data-track-index="9">Economia <span id="lst" class="stamp">Capita</span></div>
{capd}
<div id="notte" class="clip" data-start="0" data-duration="4.9" data-track-index="40">
 <div id="hk"><div id="h1">Un tedesco guadagna</div><div id="hx">+22.000 €</div><div id="h2">più di te. <em>Ogni anno.</em></div></div>
</div>
<div id="prog" class="clip" data-start="0" data-duration="{D}" data-track-index="60"></div>
</div>
<script>{JS.replace("DUR", str(D))}{capjs}
window.__timelines["main"] = tl; tl.seek(0);</script>
</body></html>'''
open(OUT + '/index.html', 'w').write(html)
fx = [('whoosh',0.0,-8),('pop',0.05,-6),('stamp',2.0,0),('pop',2.25,-6),('whoosh',4.3,-4),('tick',5.3,-4),
      ('rise',7.0,-4),('ching',8.8,-6),('rise',9.6,-6),('ching',10.9,-8),('stamp',11.05,0),
      ('stamp',14.35,2),('rumble',14.35,-2),('whoosh',15.2,-6),('pop',17.0,-8),('pop',17.1,-8),('pop',17.2,-8),('pop',17.3,-8),('pop',19.65,-4),
      ('rise',20.7,-8),('rumble',22.0,-8),('pop',24.0,-8),('pop',24.3,-8),('pop',24.6,-8),('pop',24.9,-8),('pop',25.2,-8),('pop',25.5,-8),('pop',25.6,-6),('pop',25.8,-8),('pop',26.1,-8),
      ('stamp',27.7,-2),('stamp',28.3,0),('whoosh',29.3,-4),('rise',30.1,-6),('tick',31.0,-6),('pop',33.7,-8),
      ('tick',34.3,-6),('tick',34.4,-6),('tick',34.5,-6),('tick',34.6,-6),('tick',34.7,-6),('pop',35.9,-8),('tick',36.7,-6),('tick',36.8,-6),
      ('whoosh',38.5,-6),('whoosh',41.3,-4),('stamp',42.3,0),('whoosh',43.0,-6),('drop',44.0,-8),('stamp',48.1,0),('rise',48.6,-4),('stamp',50.45,0),
      ('stamp',52.95,2),('rumble',52.95,-4),('stamp',54.5,0),('whoosh',58.2,-8),('jingle_out',58.3,-3),('stamp',59.1,-2)]
json.dump(fx, open(OUT + '/sfx.json', 'w'))
print('ok', OUT)
