"""Reel 07 — Under 25 disoccupati ×4. Genera reel-07/index.html + reel-07/sfx.json"""
import json, os, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # cartella studio/
OUT = BASE + '/reel-07'
os.makedirs(OUT, exist_ok=True)
for f in ('gsap.min.js', 'hyperframes.json', 'package.json'):
    shutil.copy(f'{BASE}/template/{f}', OUT)
json.dump({"id": "reel-07", "name": "reel-07", "createdAt": "2026-11-20T09:20:00Z"}, open(OUT + '/meta.json', 'w'))

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

D = 53.4
AZ, BE, OR_, LI = '#4F7CAC', SALVIA, OCRA, '#9A98B0'
caps = []
def cap(i, s, e, top, size, html, style=''): caps.append((i, s, e, top, size, html, style))
cap('k0', 0.05, 4.6, 300, 72, 'Giulia prende il telefono di Gigi…')
cap('k1', 8.85, 11.45, 300, 72, 'Giulia gli tira una scarpa in faccia.')
cap('k2', 15.55, 20.3, 300, 62, '<b style="color:#4F7CAC">Azzurra</b> = le azioni. Un giorno ti ama, quello dopo <em>−30%</em>.')
cap('k3', 20.35, 24.1, 300, 62, '<b style="color:#5E8A69">Bea</b> = le obbligazioni. Noiosa, ma <em>ti paga puntuale</em>.')
cap('k4', 24.15, 27.65, 300, 62, '<b style="color:#B8892A">Orietta</b> = l&#39;oro. Quando va tutto male, <em>lei c&#39;è</em>.')
cap('k5', 27.7, 32.2, 300, 62, '<b style="color:#6E6C88">Lilli</b> = la liquidità. Non rende niente, ma è <em>sempre lì</em>.')
cap('k6', 32.25, 35.95, 300, 66, 'Tutti i soldi su una sola, e lei <em>ti lascia</em>:')
cap('k7', 36.0, 39.65, 300, 66, 'Soldi divisi in quattro, e una <em>ti tradisce</em>:')
cap('k8', 39.7, 45.4, 300, 66, 'Quattro ragazze <em>tutte uguali</em>? Non è diversificazione.')
cap('k9', 45.45, 47.8, 300, 72, 'Comunque Giulia l&#39;ha lasciato lo stesso.')
cap('k10', 47.84, 51.1, 300, 64, 'Salva il video. Prima che lo veda <em>la tua ragazza</em>.')
NOTTE = set()
capd = ''.join(f'<div id="{i}" class="cap clip{" nt" if i in NOTTE else ""}" data-start="{s}" data-duration="{round(e-s,2)}" data-track-index="{10+n}" style="top:{t}px;font-size:{sz}px;{st}">{h}</div>'
               for n, (i, s, e, t, sz, h, st) in enumerate(caps))
capjs = ''.join(f'tl.fromTo("#{i}",{{opacity:0,y:34}},{{opacity:1,y:0,duration:.35,ease:"power3.out"}},{s});tl.to("#{i}",{{opacity:0,y:-20,duration:.2,ease:"power2.in"}},{round(e-0.22,2)});'
                for (i, s, e, t, sz, h, st) in caps)

def gigi(x, y, s, idn):
    return (f'<g transform="translate({x} {y}) scale({s})"><g id="{idn}">'
            f'<path d="M-19,0 L-19,-24 Q-19,-40 0,-40 Q19,-40 19,-24 L19,0 Z" fill="{AZ}"/>'
            f'<circle cx="0" cy="-58" r="15" fill="{INK}"/><path d="M-6,-72 Q2,-90 12,-74" stroke="{INK}" stroke-width="5" fill="none"/></g></g>')
def giulia(x, y, s, idn):
    return (f'<g transform="translate({x} {y}) scale({s})"><g id="{idn}">'
            f'<path d="M-20,0 L-14,-26 Q-12,-40 0,-40 Q12,-40 14,-26 L20,0 Z" fill="{ROSA}"/>'
            f'<circle cx="13" cy="-66" r="8" fill="{INK}"/><circle cx="0" cy="-58" r="15" fill="{INK}"/></g></g>')
def girl(x, y, s, col, idn, cls='', ini=''):
    return (f'<g transform="translate({x} {y}) scale({s})"><g id="{idn}" class="{cls}">'
            f'<path d="M-20,0 L-14,-26 Q-12,-40 0,-40 Q12,-40 14,-26 L20,0 Z" fill="{col}"/>'
            f'<circle cx="-13" cy="-66" r="8" fill="{INK}"/><circle cx="0" cy="-58" r="15" fill="{INK}"/></g></g>')

# --- S0/S1 telefono
rows = [('Azzurra', AZ, 'ieri ti amavo. oggi boh.', 'rA'), ('Bea', BE, 'ti ho mandato la cedola', 'rB'),
        ('Orietta', OR_, 'se crolla tutto chiamami', 'rO'), ('Lilli', LI, 'ci sono. sempre.', 'rL')]
rowh = ''.join(f'<div class="row" id="{rid}" style="top:{150 + k*150}px"><div class="av" style="background:{c}">{n[0]}</div>'
               f'<div><div class="rn">{n}</div><div class="rp">{p}</div></div><div class="rt">{("23:4"+str(k))}</div></div>'
               for k, (n, c, p, rid) in enumerate(rows))
phone = (f'<div id="ph"><div id="scr"><div id="lock">Gigi<br/><span>tocca per aprire</span><div id="notif">4 nuovi messaggi</div></div>'
         f'<div id="chats"><div class="ch">Chat</div>{rowh}</div></div></div>'
         f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{giulia(190, 1560, 2.4, "gj0")}</svg>'
         '<div class="bub" id="bq" style="left:120px;top:1230px">?!</div>'
         '<div class="stamp big" id="q4" style="left:300px;top:1450px;font-size:120px">4 RAGAZZE</div>')
# --- S2 scarpa
shoe = f'<g id="shoe"><path d="M-40,10 L-40,-14 Q-30,-22 -10,-14 L30,0 Q44,4 44,14 L44,18 L-40,18 Z" fill="{OCRA}" stroke="{INK}" stroke-width="5"/></g>'
fight = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{giulia(270, 1350, 3.2, "gj1")}{gigi(800, 1350, 3.2, "gg1")}'
         f'<g transform="translate(330 1130)">{shoe}</g></svg>'
         '<div class="stamp mid" id="bam" style="left:690px;top:900px">BAM.</div>'
         '<div class="bub r" id="b1" style="left:520px;top:620px">Amore, aspetta!</div>'
         '<div class="bub r" id="b2" style="left:470px;top:760px">Non ti tradisco.</div>'
         '<div class="stamp big" id="div" style="left:120px;top:1450px;font-size:112px">DIVERSIFICO!</div>')
# --- S3 le quattro
def card(x, y, name, lab, col, cid, path, extra=''):
    return (f'<div class="gc" id="{cid}" style="left:{x}px;top:{y}px;border-color:{col}">'
            f'<div class="gl">{lab}</div><div class="gn" style="color:{col}">{name}</div>'
            f'<svg width="360" height="170" viewBox="0 0 360 170" aria-hidden="true"><path class="ln" id="{cid}l" d="{path}" fill="none" stroke="{col}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>{extra}</svg></div>')
four = (card(110, 600, 'Azzurra', 'azioni', AZ, 'cA', 'M10,120 L50,60 L90,95 L130,30 L170,70 L210,20 L250,50 L290,40 L320,150')
        + card(560, 600, 'Bea', 'obbligazioni', '#5E8A69', 'cB', 'M10,120 L80,112 L150,104 L220,96 L290,88 L350,80')
        + card(110, 1060, 'Orietta', 'oro', '#B8892A', 'cO', 'M10,110 L80,100 L150,108 L220,70 L290,40 L350,30')
        + card(560, 1060, 'Lilli', 'liquidità', '#6E6C88', 'cL', 'M10,90 L350,90')
        + '<div class="stamp mid" id="m30" style="left:300px;top:930px;font-size:52px">−30%</div>'
        + '<div class="coin" id="cedola" style="left:880px;top:800px">€</div>'
        + '<div class="stamp mid ocra2" id="oc" style="left:330px;top:1400px;font-size:46px;color:#B8892A;border-color:#B8892A">lei c&#39;è</div>'
        + '<div class="stamp mid" id="sub" style="left:760px;top:1400px;font-size:46px;color:#6E6C88;border-color:#6E6C88">subito</div>')
# --- S4 tutto su una / divise
alln = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{girl(540, 1150, 3.0, AZ, "solo")}{girl(200, 1500, 2.0, AZ, "q0")}{girl(420, 1500, 2.0, "#5E8A69", "q1")}{girl(640, 1500, 2.0, "#B8892A", "q2")}{girl(860, 1500, 2.0, "#6E6C88", "q3")}</svg>'
        '<div class="wal" id="w1" style="top:560px">100 €</div>'
        '<div class="wl" id="wl1" style="top:770px">tutto su Azzurra</div>'
        '<div class="stamp big" id="rov" style="left:180px;top:1250px;font-size:110px">−30 €</div>'
        '<div class="q4l" id="ql0" style="left:120px">25 €</div><div class="q4l" style="left:340px">25 €</div><div class="q4l" style="left:560px">25 €</div><div class="q4l" style="left:780px">25 €</div>'
        '<div class="wal" id="w2" style="top:560px">100 €</div><div class="wl" id="wl2" style="top:770px">25 € a testa</div>'
        '<div class="stamp mid ocra2" id="pied" style="left:560px;top:880px;color:#5E8A69;border-color:#5E8A69">solo −7,50 €</div>')
# --- S5 tutte uguali
clones = ''.join(girl(200 + k * 220, 1300, 2.4, AZ, f'cl{k}', 'cln') for k in range(4))
same = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{clones}</svg>'
        '<div class="ml" id="lab4" style="left:120px;top:800px">4 × azioni dello stesso settore</div>'
        '<div class="stamp big" id="cas" style="left:140px;top:1450px;font-size:120px">UN CASINO.</div>')
# --- S6 lasciato
left = (f'<svg class="g" viewBox="0 0 1080 1920" aria-hidden="true">{gigi(320, 1350, 3.2, "gg2")}{giulia(700, 1350, 3.2, "gj2")}'
        f'<rect id="val" x="770" y="1220" width="90" height="70" rx="10" fill="{ROSA}" stroke="{INK}" stroke-width="6"/></svg>'
        '<div class="stamp big" id="las" style="left:150px;top:760px;font-size:120px">LASCIATO.</div>')
fin = ('<div class="stamp big" id="seg" style="left:120px;top:700px">SEGUIMI</div>'
       '<div class="ml" id="nx" style="left:120px;top:930px;font-size:34px">salva il video ↓<br/><span style="color:#2B2A4C;font-family:var(--serif);font-size:64px;text-transform:none;letter-spacing:0">e mandalo a chi<br/>«ha tutto su una cosa sola»</span></div>')

CSS = open('/tmp/r7_css.txt').read() + '''
#ph{position:absolute;left:290px;top:520px;width:500px;height:900px;background:#2B2A4C;border-radius:56px;padding:22px}
#scr{position:relative;width:100%;height:100%;background:#F6F1E4;border-radius:38px;overflow:hidden}
#lock{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:80px;font-weight:500;text-align:center;background:#2B2A4C;color:#EDE6D3}
#notif{margin-top:40px;background:#A8463B;color:#fff;font-family:var(--mono);font-size:30px;padding:10px 22px;border-radius:30px}
#lock span{font-family:var(--mono);font-size:24px;color:#cfc8b6;letter-spacing:.08em}
.ch{position:absolute;left:30px;top:50px;font-size:56px;font-weight:600}
.row{position:absolute;left:20px;right:20px;height:130px;display:flex;align-items:center;gap:18px;border-bottom:3px solid #D8CFB8;padding:0 8px}
.av{width:84px;height:84px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:44px;font-weight:600;flex:none}
.rn{font-size:40px;font-weight:600;line-height:1}
.rp{font-family:var(--mono);font-size:19px;color:#4A4966;margin-top:6px}
.rt{position:absolute;right:16px;top:20px;font-family:var(--mono);font-size:18px;color:#4A4966}
.bub{position:absolute;background:#F6F1E4;border:6px solid #2B2A4C;border-radius:30px;padding:10px 28px;font-size:60px;font-weight:600;white-space:nowrap}
.gc{position:absolute;width:410px;height:400px;border:7px solid;border-radius:20px;background:#F6F1E4;padding:20px 24px}
.gl{font-family:var(--mono);font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#4A4966}
.gn{font-size:72px;font-weight:600;line-height:1.05;margin-bottom:10px}
.coin{position:absolute;width:90px;height:90px;border-radius:50%;background:#E3B23C;border:6px solid #2B2A4C;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:48px;font-weight:600}
.wal{position:absolute;left:0;right:0;text-align:center;font-family:var(--mono);font-size:150px;font-weight:500;letter-spacing:-.04em}
.wl{position:absolute;left:0;right:0;text-align:center;font-family:var(--mono);font-size:32px;letter-spacing:.06em;text-transform:uppercase;color:#4A4966}
.q4l{position:absolute;top:1530px;width:160px;white-space:nowrap;text-align:center;font-family:var(--mono);font-size:34px;font-weight:500}
'''
JS = open('/tmp/r7_js.txt').read() + r'''
const lose=(sel,t)=>tl.to(sel,{x:600,y:-500,rotation:540,transformOrigin:"50% 50%",duration:.8,ease:"power2.in"},t);
// S0 telefono
tl.set(["#chats","#bq","#q4"],{opacity:0},0);
tl.fromTo("#ph",{y:80,opacity:0},{y:0,opacity:1,duration:.45,ease:"power3.out"},0.1);
popin("#gj0",0.6); rise("#bq",1.7); tl.fromTo("#notif",{scale:0},{scale:1,duration:.3,ease:"back.out(3)"},0.25); tl.to("#notif",{scale:1.15,duration:.25,yoyo:true,repeat:5,ease:"sine.inOut"},0.6);
tl.to("#lock",{opacity:0,duration:.25},2.5); tl.set("#chats",{opacity:1},2.5);
tl.fromTo(".row",{opacity:0,x:40},{opacity:1,x:0,duration:.25,stagger:.12},2.55);
tl.to("#ph",{scale:1.08,duration:1.0,ease:"power1.inOut"},3.7);
stamp("#q4",5.0,-6); shake(5.0,16);
tl.to("#ph",{scale:1,duration:.3},5.6);
["#rA","#rB","#rO","#rL"].forEach((r,i)=>{const t=[6.05,6.85,7.33,8.2][i];tl.to(r,{background:"#E9D9A6",duration:.12},t);tl.to(r,{background:"transparent",duration:.25},t+.45);});
// S2 scarpa
tl.set(["#bam","#b1","#b2","#div","#shoe"],{opacity:0},0);
popin(["#gj1","#gg1"],8.9,.12);
tl.set("#shoe",{opacity:1},10.2);
tl.fromTo("#shoe",{x:0,y:0,rotation:0},{x:430,y:-40,rotation:720,duration:.6,ease:"power1.in"},10.3);
tl.to("#gg1",{rotation:-18,transformOrigin:"50% 100%",duration:.08,yoyo:true,repeat:3},10.9);
stamp("#bam",10.95,-8);
tl.to("#shoe",{y:300,rotation:900,duration:.5,ease:"power2.in"},10.95);
tl.to("#bam",{opacity:0,duration:.2},11.9);
rise("#b1",12.1); rise("#b2",13.2);
stamp("#div",14.5,-4); shake(14.5,16);
// S3 le quattro
tl.set([".gc","#m30","#cedola","#oc","#sub"],{opacity:0},0);
document.querySelectorAll(".ln").forEach(p=>{const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L;});
const intro=(c,t)=>{tl.fromTo(c,{opacity:0,scale:.6,rotation:-6},{opacity:1,scale:1,rotation:0,duration:.35,ease:"back.out(1.8)"},t);tl.to(c+"l",{strokeDashoffset:0,duration:2.0,ease:"none"},t+.2);};
intro("#cA",15.6); stamp("#m30",19.5,-6);
intro("#cB",20.4); tl.fromTo("#cedola",{opacity:0,y:-60},{opacity:1,y:0,duration:.4,ease:"bounce.out"},23.0);
intro("#cO",24.2); stamp("#oc",26.5,-5);
intro("#cL",27.8); stamp("#sub",31.6,-5);
// S4
tl.set(["#w1","#wl1","#solo","#rov","#w2","#wl2",".q4l","#q0","#q1","#q2","#q3","#pied"],{opacity:0},0);
rise(["#w1","#wl1"],32.4); popin("#solo",32.7);
lose("#solo",34.45);
tl.to("#w1",{color:"#A8463B",duration:.1},34.9);
const c1={v:100};tl.to(c1,{v:70,duration:.5,onUpdate:()=>{document.getElementById("w1").textContent=Math.round(c1.v)+" €";}},34.9);
stamp("#rov",35.3,-6);
tl.to(["#w1","#wl1","#rov"],{opacity:0,duration:.2},35.85);
rise(["#w2","#wl2"],36.1); popin(["#q0","#q1","#q2","#q3"],36.3,.08); rise(".q4l",36.6);
lose("#q0",37.5);
const c2={v:100};tl.to(c2,{v:92.5,duration:.5,onUpdate:()=>{document.getElementById("w2").textContent=(c2.v%1?c2.v.toFixed(2):c2.v.toFixed(0)).replace(".",",")+" €";}},37.95);
stamp("#pied",38.9,-5); tl.call(()=>{document.getElementById("ql0").textContent="17,50 €";},null,37.95); tl.to("#ql0",{color:"#A8463B",duration:.1},37.95); tl.call(()=>{document.getElementById("ql0").textContent="25 €";},null,36.0);
// S5 cloni
tl.set([".cln","#lab4","#cas"],{opacity:0},0);
popin(".cln",40.8,.1); rise("#lab4",41.3);
tl.to(".cln",{x:600,y:-500,rotation:540,transformOrigin:"50% 50%",duration:.8,ease:"power2.in",stagger:.05},43.2);
stamp("#cas",44.75,-5); shake(44.8,14);
// S6 lasciato
tl.set(["#las"],{opacity:0},0);
popin(["#gg2","#gj2"],45.5,.1);
tl.to(["#gj2","#val"],{x:500,duration:1.4,ease:"power1.in"},46.2);
stamp("#las",47.05,-6);
// FINALE
tl.set(["#seg","#nx"],{opacity:0},0); stamp("#seg",48.0,-4); rise("#nx",48.7);
tl.to(["#seg","#nx"],{opacity:0,duration:.25},51.2);
tl.fromTo("#logo",{opacity:0,y:30},{opacity:1,y:0,duration:.45},51.45);
stamp("#lst",52.1,-4);
'''
html = f'''<!doctype html>
<html lang="it" data-resolution="portrait"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920">
<div id="righe" class="clip" data-start="0" data-duration="{D}" data-track-index="0"></div>
<div id="margine" class="clip" data-start="0" data-duration="{D}" data-track-index="1"></div>
<div id="sPh" class="sc clip" data-start="0" data-duration="8.85" data-track-index="2">{phone}</div>
<div id="sFi" class="sc clip" data-start="8.85" data-duration="6.7" data-track-index="3">{fight}</div>
<div id="sFo" class="sc clip" data-start="15.55" data-duration="16.65" data-track-index="4">{four}</div>
<div id="sAl" class="sc clip" data-start="32.2" data-duration="7.5" data-track-index="5">{alln}</div>
<div id="sSa" class="sc clip" data-start="39.7" data-duration="5.75" data-track-index="6">{same}</div>
<div id="sLe" class="sc clip" data-start="45.45" data-duration="2.4" data-track-index="7">{left}</div>
<div id="sFin" class="sc clip" data-start="47.85" data-duration="3.6" data-track-index="8">{fin}</div>
<div id="logo" class="clip" data-start="51.45" data-duration="{round(D-51.45,2)}" data-track-index="9">Economia <span id="lst" class="stamp">Capita</span></div>
{capd}
<div id="prog" class="clip" data-start="0" data-duration="{D}" data-track-index="60"></div>
</div>
<script>{JS.replace("DUR", str(D))}{capjs}
window.__timelines["main"] = tl; tl.seek(0);</script>
</body></html>'''
open(OUT + '/index.html', 'w').write(html)
fx = [('whoosh',0.1,-8),('pop',0.6,-6),('pop',1.7,-6),('tick',2.5,-4),('pop',2.55,-10),('pop',2.67,-10),('pop',2.79,-10),('pop',2.91,-10),('rise',3.7,-6),
      ('stamp',5.0,2),('rumble',5.0,-4),('tick',6.05,-4),('tick',6.85,-4),('tick',7.33,-4),('tick',8.2,-4),
      ('pop',8.9,-6),('whoosh',10.3,-2),('stamp',10.95,2),('drop',11.0,-6),('pop',12.1,-6),('pop',13.2,-6),('stamp',14.5,2),('rumble',14.5,-4),
      ('whoosh',15.55,-6),('pop',15.6,-6),('drop',18.9,-4),('stamp',19.5,0),('pop',20.4,-6),('ching',23.0,-2),('pop',24.2,-6),('stamp',26.5,0),('pop',27.8,-6),('stamp',31.6,-2),
      ('whoosh',32.2,-6),('pop',32.7,-6),('whoosh',34.45,0),('drop',34.9,-4),('stamp',35.3,0),('pop',36.3,-8),('pop',36.38,-8),('pop',36.46,-8),('pop',36.54,-8),('whoosh',37.5,-2),('stamp',38.9,0),
      ('pop',40.8,-8),('pop',40.9,-8),('pop',41.0,-8),('pop',41.1,-8),('whoosh',43.2,0),('stamp',44.75,2),('rumble',44.75,-4),
      ('pop',45.5,-6),('whoosh',46.2,-6),('stamp',47.05,0),('stamp',48.0,0),('whoosh',51.2,-8),('jingle_out',51.3,-3),('stamp',52.1,-2)]
json.dump(fx, open(OUT + '/sfx.json', 'w'))
print('ok', OUT)
