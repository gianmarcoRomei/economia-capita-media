import subprocess, os
OUT='instagram/carosello-sconti'; os.makedirs(OUT, exist_ok=True)
CSS=open('/tmp/css_base.txt').read()+'''
.date{position:absolute;left:100px;top:150px;font-family:"IBM Plex Mono",monospace;font-size:32px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.big{position:absolute;left:92px;font-family:"IBM Plex Mono",monospace;font-weight:500;letter-spacing:-.05em;line-height:1;white-space:nowrap}
.say{position:absolute;left:100px;right:80px;font-size:60px;line-height:1.08}
.tease{position:absolute;right:80px;bottom:120px;font-size:48px;font-style:italic;color:var(--acc)}
.tl{position:absolute;left:100px;right:80px;top:110px;height:8px;background:var(--rule)}
.tl i{position:absolute;left:0;top:0;bottom:0;background:var(--acc)}
.tag{position:absolute;background:#F6F1E4;border:6px solid #2B2A4C;border-radius:18px;padding:40px 50px}
.strike{text-decoration:line-through;text-decoration-thickness:8px;text-decoration-color:#A8463B;color:#4A4966}
'''
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,500;0,600;1,500&family=IBM+Plex+Mono:wght@500&display=swap">'
def shot(name, html, w=1080):
    p=f'/tmp/sc-{name}.html'; open(p,'w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=4000',
                    f'--screenshot={OUT}/{name}.png',f'--window-size={w},1350','file://'+p],capture_output=True)
def page(theme, prog, body, w=1080, foot=True):
    f='<div class="foot"><span class="wm">economia <i>capita</i></span><span class="sw"></span></div>' if foot else ''
    return (f'<html><head>{FONTS}<style>{CSS} body{{width:{w}px}}</style></head><body class="{theme}">'
            f'<div class="tl"><i style="width:{prog}%"></i></div>{body}{f}</body></html>')
# 1 cover: il cartellino
b=('<div class="a" style="left:0;top:0;width:1080px;height:520px;background:#E3B23C"></div>'
   '<div class="date" style="color:#2B2A4C">black friday · 27 novembre</div>'
   '<div class="a" style="left:92px;top:200px;font-size:150px;line-height:1;font-weight:600;letter-spacing:-.03em;color:#2B2A4C">Affare o<br/>fregatura?</div>'
   '<div class="tag" style="left:150px;top:600px;transform:rotate(-4deg);width:780px">'
   '<div class="lab">cuffie wireless · offerta</div>'
   '<div style="font-family:IBM Plex Mono;font-size:70px;margin-top:20px" class="strike">139 £</div>'
   '<div style="font-family:IBM Plex Mono;font-size:150px;font-weight:500;line-height:1;color:#A8463B">119 £</div></div>'
   '<div class="a" style="left:610px;top:975px;transform:rotate(6deg)"><span class="stamp" style="font-size:80px;background:#EDE6D3">−14%</span></div>'
   '<div class="a lab" style="left:100px;top:1115px;color:var(--acc)">alla fine: il trucco per beccarli in 5 secondi</div>'
   '<div class="tease">scorri: guardiamo i mesi prima →</div>')
shot('slide-01', page('carta',5,b))
# 2-3 panorama: il grafico del prezzo
X=lambda m: 120+m*300   # mesi: 0=mag ... 6=nov
Y=lambda p: 1150-(p-90)*13
pts=[(0,105),(0.4,99),(0.8,109),(1.2,104),(1.6,99),(2.0,109),(2.4,105),(2.8,99),(3.2,104),(3.6,109),(4.15,109),(4.3,139),(5.0,139),(5.7,139),(6.1,139),(6.25,119),(6.6,119)]
path='M'+' L'.join(f'{X(m):.0f},{Y(p):.0f}' for m,p in pts)
months=['MAG','GIU','LUG','AGO','SET','OTT','NOV']
mlab=''.join(f'<text x="{X(i)}" y="1215" font-family="IBM Plex Mono" font-size="30" fill="#C4BFCF" text-anchor="middle">{m}</text>' for i,m in enumerate(months))
grid=''.join(f'<line x1="100" x2="2100" y1="{Y(p)}" y2="{Y(p)}" stroke="rgba(237,230,211,.12)" stroke-width="3" stroke-dasharray="10 12"/><text x="2110" y="{Y(p)+10}" font-family="IBM Plex Mono" font-size="28" fill="#C4BFCF" text-anchor="end"></text>' for p in (99,119,139))+''.join(f'<text x="1100" y="{Y(p)-14}" font-family="IBM Plex Mono" font-size="30" fill="#C4BFCF">{p} £</text>' for p in (119,))
svg=(f'<svg class="a" style="left:0;top:0" width="2160" height="1350" viewBox="0 0 2160 1350">{grid}{mlab}'
     f'<rect x="{X(0)-20}" y="{Y(109)-20}" width="{X(3.7)-X(0)+40}" height="{Y(99)-Y(109)+40}" rx="14" fill="rgba(143,174,149,.18)"/>'
     f'<path d="{path}" fill="none" stroke="#E3B23C" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>'
     f'<circle cx="{X(6.4)}" cy="{Y(119)}" r="22" fill="#C96F62" stroke="#EDE6D3" stroke-width="6"/></svg>')
pb=('<div class="date">un caso vero · regno unito · fonte: which?</div>'
    '<div class="say" style="top:220px;width:900px">Le stesse cuffie. Da maggio a settembre costavano:</div>'
    '<div class="big" style="top:400px;font-size:150px;color:#8FAE95">99–109 £</div>'
    '<div class="a" style="left:1190px;top:220px;font-size:60px;line-height:1.08;width:860px">A settembre il prezzo <em>sale</em> a 139 £.</div>'
    '<div class="a" style="left:1190px;top:380px;font-size:60px;line-height:1.08;width:860px">Poi arriva il Black Friday: <em>«sconto!»</em> 119 £.</div>'
    '<div class="a" style="left:1440px;top:880px;transform:rotate(-5deg)"><span class="stamp" style="font-size:54px;background:#2B2A4C">più caro che d&#39;estate</span></div>'
    + svg +
    '<div class="a" style="left:860px;top:1250px;font-size:44px;font-style:italic;color:#E3B23C">e poi? →</div>'
    '<div class="a" style="right:80px;top:1250px;font-size:44px;font-style:italic;color:#E3B23C">capita spesso? →</div>')
shot('pano', page('notte',100,pb,2160,foot=False), 2160)
for i,x in ((2,0),(3,1080)):
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'{OUT}/pano.png','-vf',f'crop=1080:1350:{x}:0',f'{OUT}/slide-{i:02d}.png'])
def stat(i, theme, prog, date, num, numcol, say, tease, src, extra=''):
    b=(f'<div class="date">{date}</div><div class="big" style="top:210px;font-size:250px;color:{numcol}">{num}</div>'
       f'<div class="say" style="top:520px">{say}</div>{extra}<div class="tease">{tease}</div>'
       f'<div class="a" style="left:100px;bottom:200px;font-family:IBM Plex Mono;font-size:22px;color:var(--mut)">fonte: {src}</div>')
    shot(f'slide-{i:02d}', page(theme,prog,b))
stat(4,'carta',40,'black friday 2024 · 175 prodotti','100%','var(--acc)',
     'delle offerte costavano <em>uguale o meno</em> in altri giorni, nei 6 mesi prima o dopo.','e in Italia? →','Which?, 2024')
stat(5,'carta',50,'italia · 208 negozi online','<span style="font-size:210px">6 su 10</span>','var(--acc)',
     'non mostravano lo sconto <em>come vuole la legge</em>, o non lo mostravano proprio.','quale legge? →','Altroconsumo, febbraio 2026')
# 6 la legge: calendario 30 giorni
cal=''
for k in range(30):
    x=100+(k%10)*88; y=760+(k//10)*88; mn=(k==11)
    cal+=f'<div class="a" style="left:{x}px;top:{y}px;width:76px;height:76px;border:4px solid var(--fg);border-radius:8px;background:{"#A8463B" if mn else "transparent"}"></div>'
b=('<div class="date">la regola · art. 17-bis codice del consumo</div>'
   '<div class="say" style="top:220px">Lo sconto si calcola sul <em>prezzo più basso degli ultimi 30 giorni</em>.</div>'
   '<div class="say" style="top:470px;font-size:46px;color:var(--mut)">Non sul prezzo «di listino». Non su quello che vogliono loro.</div>'
   + cal + '<div class="a lab" style="left:100px;top:1040px;color:var(--acc)">■ il giorno più economico = il prezzo da cui partire</div>'
   '<div class="tease">quindi? →</div>')
shot('slide-06', page('carta',60,b))
# 7 esempio
b=('<div class="date">esempio</div>'
   '<div class="say" style="top:220px">Cartellino: <span class="strike" style="font-family:IBM Plex Mono">60 €</span> → <b style="font-family:IBM Plex Mono">45 €</b></div>'
   '<div class="big" style="top:360px;font-size:200px;color:var(--mut)" ><span class="strike">−25%</span></div>'
   '<div class="say" style="top:620px">Ma 20 giorni fa costava <b>50 €</b>. Lo sconto vero è:</div>'
   '<div class="big" style="top:800px;font-size:250px;color:var(--acc)">−10%</div>'
   '<div class="tease">quanti lo sanno? →</div>')
shot('slide-07', page('carta',70,b))
stat(8,'notte',80,'italiani che conoscono questa regola','1,4%','var(--acc)',
     'Su 100 persone che faranno acquisti al Black Friday, una e mezza. <em>Ora ci sei anche tu.</em>','il metodo →','Altroconsumo, 2026')
# 9 metodo
steps=['Cerca la scritta <b>«prezzo più basso degli ultimi 30 giorni»</b>.','Rifai lo sconto partendo <em>da quel prezzo</em>.','Non c&#39;è? Il negozio sta sbagliando: puoi segnalarlo all&#39;<b>Antitrust</b>.','Per le cose costose guarda lo <b>storico dei prezzi</b>.']
lst=''.join(f'<div style="display:flex;gap:28px;margin-top:34px"><span class="ms" style="font-size:40px;padding:0 16px;height:fit-content">{n}</span><span class="p">{t}</span></div>' for n,t in enumerate(steps,1))
b=(f'<div class="date">il metodo in 5 secondi</div><div class="a" style="left:100px;right:80px;top:200px">{lst}</div><div class="tease">ultima cosa →</div>')
shot('slide-09', page('carta',90,b))
# 10 cta
b=('<div class="a" style="left:0;top:0;width:1080px;height:1350px;background:#E3B23C"></div>'
   '<div class="date" style="color:#2B2A4C">black friday · venerdì 27 novembre</div>'
   '<div class="a" style="left:92px;top:220px;right:80px;font-size:118px;line-height:1.02;font-weight:500;color:#2B2A4C">Il miglior sconto è <em style="color:#A8463B">non cascarci</em>.</div>'
   '<div class="a" style="left:100px;top:760px;right:80px;font-size:54px;line-height:1.15;color:#2B2A4C">Salvalo per il 27. E mandalo a quell&#39;amico che compra tutto perché «era scontato».</div>'
   '<div class="a" style="left:100px;bottom:56px;font-size:34px;color:#2B2A4C">economia <i style="color:#A8463B">capita</i></div>')
shot('slide-10', page('carta',100,b,foot=False))
print('ok')
