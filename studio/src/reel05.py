"""Reel 05 — Under 25 disoccupati ×4. Genera reel-05/index.html + reel-05/sfx.json"""
import json, os, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # cartella studio/
OUT = BASE + '/reel-05'
os.makedirs(OUT, exist_ok=True)
for f in ('gsap.min.js', 'hyperframes.json', 'package.json'):
    shutil.copy(f'{BASE}/template/{f}', OUT)
json.dump({"id": "reel-05", "name": "reel-05", "createdAt": "2026-11-17T17:20:00Z"}, open(OUT + '/meta.json', 'w'))

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
def cap(i, s, e, top, size, html, style=''): caps.append((i, s, e, top, size, html, style))
L = 'font-family:var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--tenue)'
cap('k0', 5.2, 8.8, 300, 84, 'Non lo dico io.')
cap('k1', 8.85, 14.0, 300, 62, 'In Italia un under 25 resta senza lavoro quasi <em>4 volte</em> più di un adulto.')
cap('k2', 14.08, 15.88, 300, 80, '<em>Perché?</em> Pensa alla discoteca.')
cap('k3', 15.92, 19.0, 300, 72, 'Il locale è pieno. Arriva il buttafuori…')
cap('k4', 19.05, 21.1, 300, 72, '…e chi caccia? Quello <em>appena entrato</em>.')
cap('k5', 21.16, 26.15, 300, 64, 'Quando le aziende tagliano, mandano via chi costa meno mandare via.')
cap('k6', 26.2, 28.5, 300, 64, 'E il contratto a termine ce l&#39;ha <em>quasi 1 giovane su 3</em>.')
cap('k7', 28.56, 31.25, 300, 84, 'Il tempo pieno?')
cap('k8', 31.32, 34.75, 300, 62, '<em>6 su 10</em> fanno part-time solo perché il full-time non lo trovano.')
cap('k9', 34.85, 41.7, 300, 64, 'In 10 anni sono partiti <em>367.000</em> ragazzi tra i 25 e i 34 anni.')
cap('k10', 41.8, 46.25, 300, 64, 'Di questi, <em>146.000</em> erano laureati. Ne sono tornati 49.000.')
cap('k11', 46.33, 49.6, 300, 66, 'Praticamente l&#39;università l&#39;abbiamo pagata <em>alla Germania</em>.')
cap('k12', 49.68, 53.3, 300, 64, 'Nel prossimo: perché all&#39;estero ti pagano di più.')
cap('k13', 53.36, 55.45, 300, 64, 'E no, non è perché i tedeschi sono più bravi.')
NOTTE = {'k9', 'k10'}
capd = ''.join(f'<div id="{i}" class="cap clip{" nt" if i in NOTTE else ""}" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="{10+n}" style="top:{t}px;font-size:{sz}px;{st}">{h}</div>'
               for n, (i, s, e, t, sz, h, st) in enumerate(caps))
capjs = ''
for (i, s, e, t, sz, h, st) in caps:
    capjs += f'tl.fromTo("#{i}",{{opacity:0,y:34}},{{opacity:1,y:0,duration:.35,ease:"power3.out"}},{s});'
    capjs += f'tl.to("#{i}",{{opacity:0,y:-20,duration:.2,ease:"power2.in"}},{round(e-0.22,2)});'

# ---------- scena 2: barre ----------
bars = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
        f'<line x1="150" y1="1400" x2="930" y2="1400" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="bA" x="230" y="1270" width="200" height="130" fill="{SALVIA}" stroke="{INK}" stroke-width="5"/>'
        f'<rect id="bY" x="620" y="1270" width="200" height="130" fill="{ROSA}" stroke="{INK}" stroke-width="5"/>'
        + P(330, 1530, 1.6, INK, 'pA') + P(720, 1530, 1.25, TIMBRO, 'pY') +
        '</svg>'
        '<div class="ml" id="lA" style="left:230px;top:1545px;width:200px;text-align:center">adulto</div>'
        '<div class="ml" id="lY" style="left:620px;top:1545px;width:200px;text-align:center">under 25</div>'
        '<div class="ml" id="src" style="left:150px;top:640px">fonte · Organizzazione<br/>Internazionale del Lavoro</div>'
        '<div class="stamp big" id="x4" style="left:170px;top:860px">×4</div>')

# ---------- scena 3: discoteca ----------
crowd = ''.join(P(330 + k * 95, 1330, 1.35, INK, f'c{k}', 'cr') for k in range(5))
disco = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
         f'<rect x="230" y="1010" width="560" height="350" rx="10" fill="#2B2A4C" opacity=".1" stroke="{INK}" stroke-width="5"/>'
         f'<rect id="door" x="790" y="1130" width="110" height="230" fill="{INK}"/>'
         f'<line x1="150" y1="1360" x2="980" y2="1360" stroke="{INK}" stroke-width="5"/>'
         + crowd + P(845, 1330, 1.35, OCRA, 'you') + P(940, 1360, 2.3, INK, 'bouncer', glasses=True) +
         '</svg>'
         '<div id="sign">DISCO <span id="pieno">PIENO</span></div>'
         '<div class="stamp big" id="tu" style="left:560px;top:700px">TU.</div>')

# ---------- scena 4: contratti ----------
contr = ('<div class="card" id="cI" style="left:130px;background:#8FAE95"><div class="ct">contratto</div><div class="cn">tempo<br/>indeterminato</div></div>'
         '<div class="card" id="cT" style="left:560px;background:#E9B8AE"><div class="ct">contratto</div><div class="cn">a termine</div>'
         '<div class="stamp mid" id="tag" style="left:30px;top:140px">TAGLIATO</div></div>'
         '<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">'
         + P(380, 1100, 1.8, INK, 'u0', 'uu') + P(540, 1100, 1.8, OCRA, 'u1', 'uu') + P(700, 1100, 1.8, INK, 'u2', 'uu') +
         '</svg><div class="ml" id="l13" style="left:0;right:0;top:1140px;text-align:center">1 su 3 · a termine</div>')

# ---------- scena 5: col cazzo + 6/10 ----------
ten = ''.join(P(240 + (k % 5) * 150, 1180 + (k // 5) * 200, 1.4, INK, f't{k}', 'tt') for k in range(10))
cazzo = ('<div class="stamp huge" id="cc">COL CAZZO.</div>'
         f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{ten}</svg>'
         '<div class="ml" id="l610" style="left:0;right:0;top:1420px;text-align:center"><b style="color:#A8463B">■</b> part-time per forza</div>')

# ---------- scena 6: fuga (notte) ----------
suit = ''.join(f'<div class="suit" id="s{k}" style="top:{1000 + (k % 4) * 90}px;left:{100 + (k * 37) % 200}px"></div>' for k in range(8))
fuga = ('<div id="cnt"><span id="cntn">0</span><div class="cl">giovani 25–34 anni partiti · 2014–2023</div></div>'
        + suit +
        '<div class="hb" style="top:1100px"><div class="hl">laureati partiti</div><div class="hbar" id="hP"></div><div class="hv" id="vP">146.000</div></div>'
        '<div class="hb" style="top:1280px"><div class="hl">laureati tornati</div><div class="hbar" id="hR"></div><div class="hv" id="vR">49.000</div></div>'
        '<div class="stamp mid ocra" id="m97" style="left:560px;top:1440px">−97.000</div>')

# ---------- scena 7: Germania ----------
germ = ('<div class="box" id="bIT" style="left:120px">IT</div><div class="box" id="bDE" style="left:740px">DE</div>'
        '<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true"><line x1="340" y1="1100" x2="740" y2="1100" stroke="#2B2A4C" stroke-width="5" stroke-dasharray="14 14"/></svg>'
        '<div id="capb"><svg width="150" height="120" viewBox="-75 -60 150 120" aria-hidden="true"><path d="M-70,-10 L0,-45 L70,-10 L0,25 Z" fill="#2B2A4C"/><path d="M-38,5 L-38,38 Q0,60 38,38 L38,5 L0,25 Z" fill="#2B2A4C"/><line x1="62" y1="-6" x2="62" y2="40" stroke="#E3B23C" stroke-width="6"/></svg><div id="eur">€€€</div></div>'
        '<div class="stamp big" id="danke" style="left:300px;top:1300px">DANKE.</div>')

# ---------- finale ----------
fin = ('<div class="stamp big" id="seg" style="left:120px;top:760px">SEGUIMI</div>'
       '<div class="ml" id="nx" style="left:120px;top:960px;font-size:34px">prossimo episodio →<br/><span style="color:#2B2A4C;font-family:var(--serif);font-size:64px;text-transform:none;letter-spacing:0">Perché all&#39;estero<br/>ti pagano di più</span></div>')

html = f'''<!doctype html>
<html lang="it" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="gsap.min.js"></script>
<style>
:root{{--carta:#EDE6D3;--ink:#2B2A4C;--tenue:#4A4966;--timbro:#A8463B;--rosa:#C96F62;--salvia:#8FAE95;--ocra:#E3B23C;--linea:#D8CFB8;
--serif:"EB Garamond",Georgia,serif;--mono:"IBM Plex Mono",monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--carta)}}
#root{{position:relative;width:100%;height:100%;font-family:var(--serif);color:var(--ink);overflow:hidden}}
#righe{{position:absolute;inset:0;background-image:repeating-linear-gradient(to bottom,transparent 0 63px,rgba(43,42,76,.08) 63px 64px)}}
#margine{{position:absolute;top:0;bottom:0;left:84px;width:2px;background:rgba(168,70,59,.35)}}
.cap{{position:absolute;left:120px;right:170px;line-height:1.06;font-weight:500;letter-spacing:-.01em;z-index:5}}
.cap.nt{{color:var(--carta)}} .cap.nt em{{color:var(--ocra)}}
em{{font-style:italic;color:var(--timbro)}}
.sc{{position:absolute;inset:0}}
svg.g{{position:absolute;inset:0;width:1080px;height:1920px}}
.ml{{position:absolute;font-family:var(--mono);font-size:30px;letter-spacing:.06em;text-transform:uppercase;color:var(--tenue);line-height:1.35}}
.stamp{{position:absolute;display:inline-block;color:var(--timbro);border:7px solid var(--timbro);border-radius:10px;padding:0 22px 8px;font-weight:600;line-height:1.05;white-space:nowrap}}
.stamp.big{{font-size:150px}} .stamp.mid{{font-size:64px;border-width:6px;padding:2px 18px 6px}}
.stamp.huge{{font-size:132px;left:110px;top:760px;border-width:9px}}
.stamp.ocra{{color:var(--ocra);border-color:var(--ocra)}}
#notte{{position:absolute;inset:0;background:var(--ink);color:var(--carta)}}
#notte em{{color:var(--ocra)}}
#hk{{position:absolute;left:120px;right:110px;top:520px;display:flex;flex-direction:column;gap:34px;font-size:118px;line-height:1.0;font-weight:500;letter-spacing:-.015em}}
#hx4{{display:inline-block;color:var(--ocra);border:9px solid var(--ocra);border-radius:10px;padding:0 26px 10px;font-weight:600;font-size:230px;width:fit-content;line-height:1}}
#sign{{position:absolute;left:330px;top:940px;font-family:var(--mono);font-size:54px;font-weight:500;letter-spacing:.14em;color:var(--ocra);background:var(--ink);padding:6px 22px;border-radius:8px}}
#pieno{{color:var(--rosa)}}
.card{{position:absolute;top:700px;width:390px;height:330px;border:6px solid var(--ink);border-radius:14px;padding:30px 30px}}
.card .ct{{font-family:var(--mono);font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:var(--tenue)}}
.card .cn{{font-size:52px;font-weight:500;line-height:1.02;margin-top:16px}}
#bg2{{position:absolute;inset:0;background:var(--ink)}}
#cnt{{position:absolute;left:120px;top:620px;color:var(--carta)}}
#cntn{{font-family:var(--mono);font-size:170px;font-weight:500;color:var(--ocra);letter-spacing:-.02em}}
.cl{{font-family:var(--mono);font-size:28px;letter-spacing:.06em;text-transform:uppercase;color:#cfc8b6;margin-top:6px}}
.suit{{position:absolute;width:110px;height:80px;background:var(--rosa);border:6px solid var(--carta);border-radius:12px}}
.suit:before{{content:"";position:absolute;left:28px;top:-26px;width:40px;height:22px;border:6px solid var(--carta);border-bottom:none;border-radius:8px 8px 0 0}}
.hb{{position:absolute;left:120px;width:840px}}
.hl{{font-family:var(--mono);font-size:30px;letter-spacing:.06em;text-transform:uppercase;color:#cfc8b6;margin-bottom:12px}}
.hbar{{height:84px;width:780px;transform-origin:0 50%}}
#hP{{background:var(--rosa)}} #hR{{background:var(--salvia)}}
.hv{{position:absolute;right:70px;top:58px;font-family:var(--mono);font-size:48px;font-weight:500;color:var(--ink)}}
#vR{{right:auto;left:290px;color:var(--carta)}}
.box{{position:absolute;top:1000px;width:220px;height:200px;border:7px solid var(--ink);border-radius:14px;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:90px;font-weight:500;background:#F6F1E4}}
#capb{{position:absolute;left:265px;top:880px;text-align:center}}
#eur{{font-family:var(--mono);font-size:40px;color:var(--timbro);font-weight:500}}
#logo{{position:absolute;left:0;right:0;top:880px;text-align:center;font-size:110px;font-weight:500}}
#logo .stamp{{position:relative;font-size:110px;border-width:7px;padding:0 22px 8px}}
#prog{{position:absolute;left:0;bottom:0;height:10px;width:1080px;background:var(--timbro);transform-origin:0 50%;z-index:50}}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920">
<div id="righe" class="clip" data-start="0" data-duration="{D}" data-track-index="0"></div>
<div id="margine" class="clip" data-start="0" data-duration="{D}" data-track-index="1"></div>

<div id="sBar" class="sc clip" data-start="5.0" data-duration="9.05" data-track-index="2">{bars}</div>
<div id="sDis" class="sc clip" data-start="14.0" data-duration="7.15" data-track-index="3">{disco}</div>
<div id="sCon" class="sc clip" data-start="21.1" data-duration="7.45" data-track-index="4">{contr}</div>
<div id="sCaz" class="sc clip" data-start="28.5" data-duration="6.3" data-track-index="5">{cazzo}</div>
<div id="sFug" class="sc clip" data-start="34.6" data-duration="11.75" data-track-index="6"><div id="bg2"></div>{fuga}</div>
<div id="sGer" class="sc clip" data-start="46.25" data-duration="3.4" data-track-index="7">{germ}</div>
<div id="sFin" class="sc clip" data-start="49.6" data-duration="5.85" data-track-index="8">{fin}</div>
<div id="logo" class="clip" data-start="55.4" data-duration="{round(D-55.4,2)}" data-track-index="9">Economia <span id="lst" class="stamp">Capita</span></div>

{capd}

<div id="notte" class="clip" data-start="0" data-duration="5.0" data-track-index="40">
 <div id="hk">
  <div id="h1">Hai meno di 25 anni?</div>
  <div id="h2">Sei <em>fregato.</em></div>
  <div id="hx4">×4</div>
 </div>
</div>
<div id="prog" class="clip" data-start="0" data-duration="{D}" data-track-index="60"></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
const shake=(t,a=8)=>tl.to("#root",{{x:a,duration:.05,yoyo:true,repeat:3,ease:"none"}},t);
const stamp=(sel,t,r)=>{{tl.fromTo(sel,{{opacity:0,scale:2.2,rotation:-14}},{{opacity:1,scale:1,rotation:r,duration:.24,ease:"power4.in"}},t-0.24);shake(t);}};
const rise=(sel,t,d=.35)=>tl.fromTo(sel,{{opacity:0,y:30}},{{opacity:1,y:0,duration:d,ease:"power3.out"}},t);
const popin=(sel,t,st=0)=>tl.fromTo(sel,{{opacity:0,scale:0,transformOrigin:"50% 100%"}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2.2)",stagger:st}},t);
tl.fromTo("#prog",{{scaleX:0}},{{scaleX:1,duration:{D},ease:"none"}},0);
// HOOK
rise("#h1",0.05,.3); rise("#h2",1.8,.3); stamp("#hx4",3.3,-5);
tl.to("#hx4",{{scale:1.08,duration:.18,yoyo:true,repeat:1}},3.6);
tl.to("#notte",{{y:-1920,duration:.55,ease:"power3.inOut"}},4.45);
// BARRE
tl.set(["#src","#x4","#lA","#lY","#bA","#bY","#pA","#pY"],{{opacity:0}},0);
rise("#src",6.5);
popin(["#pA","#pY"],7.0,.15); rise(["#lA","#lY"],7.2);
tl.fromTo(["#bA","#bY"],{{opacity:1,scaleY:0,transformOrigin:"50% 100%"}},{{scaleY:1,duration:.4,ease:"power2.out"}},9.6);
tl.to("#bY",{{attr:{{y:780,height:620}},duration:.9,ease:"power3.out"}},11.75);
tl.to("#pY",{{y:-4,duration:.08,yoyo:true,repeat:5}},11.8);
stamp("#x4",12.6,-6);
tl.to("#pA",{{y:-12,duration:.15,yoyo:true,repeat:1}},13.2);
// DISCOTECA
tl.set([".cr","#you","#bouncer","#sign","#tu","#pieno"],{{opacity:0}},0);
rise("#sign",14.6);
popin(".cr",15.9,.12);
tl.to("#pieno",{{opacity:1,duration:.1}},16.5); tl.fromTo("#pieno",{{scale:1.6}},{{scale:1,duration:.25}},16.5);
tl.fromTo("#you",{{opacity:0,x:120}},{{opacity:1,x:0,duration:.4,ease:"power2.out"}},16.2);
tl.fromTo("#bouncer",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.35,ease:"back.out(1.6)"}},17.25);
tl.to(".cr",{{y:-6,duration:.12,yoyo:true,repeat:9,stagger:.05}},17.6);
tl.to("#bouncer",{{x:-60,duration:.2,ease:"power2.in"}},19.4);
tl.to("#you",{{x:50,y:-430,rotation:720,transformOrigin:"50% 50%",duration:.75,ease:"power2.out"}},19.6);
stamp("#tu",20.4,-8);
// CONTRATTI
tl.set(["#cI","#cT","#tag",".uu","#l13"],{{opacity:0}},0);
tl.fromTo("#cI",{{opacity:0,x:-80,rotation:-6}},{{opacity:1,x:0,rotation:-3,duration:.4,ease:"back.out(1.8)"}},21.3);
tl.fromTo("#cT",{{opacity:0,x:80,rotation:6}},{{opacity:1,x:0,rotation:3,duration:.4,ease:"back.out(1.8)"}},21.5);
tl.to("#cT",{{scale:1.07,duration:.2,yoyo:true,repeat:1}},23.85);
stamp("#tag",25.2,-8);
tl.to("#cT",{{y:1500,rotation:28,duration:.7,ease:"power2.in"}},25.6);
tl.to("#cI",{{x:200,duration:.5,ease:"power2.inOut"}},25.7);
tl.to("#cI",{{opacity:0,duration:.3}},26.3);
popin(".uu",27.05,.18); rise("#l13",27.6);
tl.to("#u1",{{y:-30,duration:.15,yoyo:true,repeat:3}},27.9);
// COL CAZZO
tl.set(["#cc",".tt","#l610"],{{opacity:0}},0);
stamp("#cc",30.35,-5); shake(30.4,16);
tl.to("#cc",{{opacity:0,scale:.8,duration:.25}},31.1);
popin(".tt",31.3,.05);
tl.to(["#t0 *","#t1 *","#t2 *","#t3 *","#t4 *","#t5 *"],{{attr:{{fill:"#A8463B"}},duration:.15,stagger:.11}},31.6);
rise("#l610",32.8);
// FUGA
tl.set(["#cnt",".suit",".hb","#m97"],{{opacity:0}},0);
tl.fromTo("#bg2",{{y:1920}},{{y:0,duration:.5,ease:"power3.inOut"}},34.6);
rise("#cnt",35.9);
const cobj={{v:0}};
tl.to(cobj,{{v:367000,duration:1.5,ease:"power2.out",onUpdate:()=>{{document.getElementById("cntn").textContent=Math.round(cobj.v).toLocaleString("it-IT");}}}},36.7);
tl.set(".suit",{{opacity:1}},40.4);
tl.fromTo(".suit",{{x:0,rotation:0}},{{x:1300,y:(i)=>[-120,60,-200,140,-60,220,-260,100][i],rotation:(i)=>[25,-30,40,-20,35,-45,20,-25][i],duration:1.0,ease:"power2.in",stagger:.07}},40.6);
tl.to("#cnt",{{opacity:0,y:-30,duration:.3}},41.5);
tl.set(".hb",{{opacity:1}},41.8);
tl.set(["#vP","#vR"],{{opacity:0}},41.8);
tl.fromTo("#hP",{{scaleX:0}},{{scaleX:1,duration:.7,ease:"power3.out"}},41.85);
tl.to("#vP",{{opacity:1,duration:.2}},42.4);
tl.fromTo("#hR",{{scaleX:0}},{{scaleX:.336,duration:.6,ease:"power3.out"}},44.4);
tl.to("#vR",{{opacity:1,duration:.2}},44.9);
stamp("#m97",45.6,-6);
// GERMANIA
tl.set(["#bIT","#bDE","#capb","#danke"],{{opacity:0}},0);
popin(["#bIT","#bDE"],46.35,.12);
tl.fromTo("#capb",{{opacity:0,x:0,y:0}},{{opacity:1,duration:.2}},46.9);
tl.to("#capb",{{x:520,duration:1.3,ease:"power1.inOut"}},47.1);
tl.to("#capb",{{y:-40,duration:.32,yoyo:true,repeat:3,ease:"sine.inOut"}},47.1);
tl.to("#bDE",{{background:"#E3B23C",duration:.2}},48.45);
stamp("#danke",48.75,-6);
// FINALE
tl.set(["#seg","#nx"],{{opacity:0}},0);
stamp("#seg",49.85,-4);
rise("#nx",50.5);
tl.to("#nx",{{x:10,duration:.6,yoyo:true,repeat:3,ease:"sine.inOut"}},51.2);
tl.to(["#seg","#nx"],{{opacity:0,duration:.25}},53.2);
tl.fromTo("#logo",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45}},55.45);
stamp("#lst",56.15,-4);
{capjs}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>'''
open(OUT + '/index.html', 'w').write(html)

# ---------- effetti sonori (tempi assoluti) ----------
fx = [('whoosh', 0.0, -8), ('pop', 0.05, -6), ('pop', 1.8, -6), ('stamp', 3.3, 0),
      ('whoosh', 4.45, -4), ('tick', 6.5, -4), ('pop', 7.0, -6), ('pop', 7.15, -6), ('rise', 11.0, -2), ('stamp', 12.6, 0),
      ('whoosh', 14.0, -6), ('pop', 15.9, -8), ('pop', 16.02, -8), ('pop', 16.14, -8), ('pop', 16.26, -8), ('pop', 16.38, -8),
      ('rumble', 17.25, -8), ('whoosh', 19.55, 0), ('stamp', 20.4, 0),
      ('whoosh', 21.3, -6), ('tick', 23.85, -2), ('stamp', 25.2, 0), ('drop', 25.6, -2), ('pop', 27.05, -6), ('pop', 27.23, -6), ('pop', 27.41, -6),
      ('stamp', 30.35, 2), ('rumble', 30.35, -2), ('tick', 31.6, -6), ('tick', 31.82, -6), ('tick', 32.04, -6), ('tick', 32.26, -6), ('tick', 32.48, -6), ('tick', 32.7, -6),
      ('whoosh', 34.6, -4), ('rise', 36.7, -4), ('ching', 38.2, -4), ('whoosh', 40.6, -2), ('whoosh', 40.95, -6), ('rise', 41.85, -8), ('drop', 44.4, -6), ('stamp', 45.6, 0),
      ('pop', 46.35, -6), ('pop', 46.47, -6), ('whoosh', 47.1, -8), ('ching', 48.45, -4), ('stamp', 48.75, 0),
      ('stamp', 49.85, 0), ('whoosh', 53.2, -8), ('jingle_out', 55.2, -3), ('stamp', 56.15, -2)]
json.dump(fx, open(OUT + '/sfx.json', 'w'))
print('ok', OUT)
