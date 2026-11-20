import subprocess, os
OUT='instagram/storie-20nov-v2'; os.makedirs(OUT, exist_ok=True)
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,500;0,600;1,500&family=IBM+Plex+Mono:wght@500&display=swap">'
CSS='''*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:"EB Garamond",Georgia,serif;position:relative}
.carta{background:#EDE6D3;color:#2B2A4C;background-image:repeating-linear-gradient(to bottom,transparent 0 63px,rgba(43,42,76,.08) 63px 64px)}
.notte{background:#2B2A4C;color:#EDE6D3}
.a{position:absolute}
.k{position:absolute;left:100px;top:270px;font-family:"IBM Plex Mono",monospace;font-size:32px;letter-spacing:.12em;text-transform:uppercase;opacity:.75}
.t{position:absolute;left:100px;right:90px;top:330px;font-size:104px;line-height:1.02;font-weight:500;letter-spacing:-.015em}
em{font-style:italic;color:#A8463B} .notte em{color:#E3B23C}
.stamp{display:inline-block;color:#A8463B;border:8px solid #A8463B;border-radius:12px;padding:0 26px 10px;font-weight:600;line-height:1.05;white-space:nowrap}
.notte .stamp{color:#E3B23C;border-color:#E3B23C}
.wm{position:absolute;left:100px;bottom:200px;font-size:40px} .wm i{color:#C96F62}
.card{position:absolute;width:410px;height:300px;border:7px solid;border-radius:22px;background:#F6F1E4;padding:22px 26px;color:#2B2A4C}
.cl{font-family:"IBM Plex Mono",monospace;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#4A4966}
.cn{font-size:76px;font-weight:600;line-height:1.05}
.cd{font-size:34px;line-height:1.15;margin-top:8px}
.mono{font-family:"IBM Plex Mono",monospace}
.tap{position:absolute;left:100px;right:90px;bottom:330px;font-size:58px;font-style:italic;color:#A8463B}.notte .tap{color:#E3B23C}
.hint{position:absolute;left:100px;right:90px;font-family:"IBM Plex Mono",monospace;font-size:30px;letter-spacing:.06em;opacity:.7}
'''
def shot(name, theme, body):
    p=f'/tmp/st-{name}.html'
    open(p,'w').write(f'<html><head>{FONTS}<style>{CSS}</style></head><body class="{theme}">{body}<div class="wm">economia <i>capita</i></div></body></html>')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=4000',
                    f'--screenshot={OUT}/{name}.png','--window-size=1080,1920','file://'+p],capture_output=True)
# 1 — Che ragazza di Gigi sei? (sondaggio a 4 opzioni / quiz)
cards=[(100,820,'#4F7CAC','azioni','Azzurra','ti fa sognare, poi ti molla'),(570,820,'#5E8A69','obbligazioni','Bea','noiosa ma puntuale'),
       (100,1160,'#B8892A','oro','Orietta','c&#39;è quando va tutto male'),(570,1160,'#6E6C88','liquidità','Lilli','zero sorprese, zero guadagni')]
b='<div class="k">dopo il reel di oggi</div><div class="t">Tu con chi staresti? <em>Sii onesto.</em></div>'
b+=''.join(f'<div class="card" style="left:{x}px;top:{y}px;border-color:{c}"><div class="cl">{l}</div><div class="cn" style="color:{c}">{n}</div><div class="cd">{d}</div></div>' for x,y,c,l,n,d in cards)
b+='<div class="a" style="left:100px;right:90px;top:1450px;font-size:50px;line-height:1.15">Scegline una. <b>Solo una.</b></div><div class="tap">poi tocca → e scopri che investitore sei</div>'
shot('a1-che-ragazza-sei','carta',b)
rows=[('#4F7CAC','Azzurra','Ami il rischio. Occhio ai crolli.'),('#5E8A69','Bea','Prudente. Dormi bene la notte.'),('#B8892A','Orietta','Pessimista di professione.'),('#6E6C88','Lilli','Tranquillo… ma l&#39;inflazione ti mangia.')]
b='<div class="k">che investitore sei</div>'+''.join(f'<div class="a" style="left:100px;right:90px;top:{330+i*230}px"><div style="font-size:84px;font-weight:600;color:{c};line-height:1">{n}</div><div style="font-size:54px;line-height:1.15;margin-top:6px">{d}</div></div>' for i,(c,n,d) in enumerate(rows))
b+='<div class="a" style="left:100px;top:1290px;transform:rotate(-4deg)"><span class="stamp" style="font-size:68px">la risposta giusta?</span></div><div class="a" style="left:100px;right:90px;top:1440px;font-size:66px;line-height:1.1">Un po&#39; di <em>tutte</em>. Si chiama diversificare: è nel reel di oggi.</div>'
shot('a2-che-investitore-sei','carta',b)
# 2a — Quiz sconto
b=('<div class="k">black friday · quiz</div><div class="t">«Da 100 € a <em>50 €</em>.»<br/>Ma 20 giorni fa costava 60 €.</div>'
   '<div class="a" style="left:100px;top:820px;right:90px;font-size:70px;line-height:1.1">Lo sconto <b>vero</b> qual è?</div>'
   '<div class="a mono" style="left:100px;top:960px;font-size:200px;font-weight:500;letter-spacing:-.04em;opacity:.12">−??%</div>')
b+='<div class="a" style="left:100px;top:1250px;font-size:60px;line-height:1.15">A) −50%<br/>B) −17%<br/>C) −33%</div><div class="tap">scegli. poi tocca →</div>'
shot('b1-quiz-sconto','notte',b)
# 2b — Risposta
b=('<div class="k">risposta B</div>'
   '<div class="a mono" style="left:90px;top:360px;font-size:330px;font-weight:500;letter-spacing:-.05em;color:#E3B23C;line-height:1">−17%</div>'
   '<div class="a" style="left:100px;right:90px;top:760px;font-size:68px;line-height:1.1">Lo sconto si calcola sul <em>prezzo più basso degli ultimi 30 giorni</em>: da 60 a 50.</div>'
   '<div class="a" style="left:100px;top:1170px;transform:rotate(-5deg)"><span class="stamp" style="font-size:96px">il resto è marketing</span></div>'
   '<div class="hint" style="top:1420px">tutta la regola nel carosello sul profilo</div>')
shot('b2-risposta-sconto','notte',b)
# 3a — Slider: quanto guadagna in più un tedesco
b=('<div class="k">scommettiamo?</div><div class="t">Quanto guadagna <em>in più</em> di un italiano un tedesco, ogni anno?</div>'
   '<div class="a" style="left:100px;right:90px;top:880px;font-size:54px;line-height:1.15;color:#4A4966">Stipendio medio lordo, tempo pieno. <b>Dilla ad alta voce.</b></div>')
b+='<div class="a mono" style="left:100px;top:1100px;font-size:190px;font-weight:500;letter-spacing:-.04em;opacity:.12">+??.000 €</div><div class="tap">detta? ora tocca →</div>'
shot('c1-stipendio-tedesco','carta',b)
# 3b — Risposta
b=('<div class="k">la risposta · eurostat 2025</div>'
   '<div class="a mono" style="left:90px;top:360px;font-size:170px;font-weight:500;letter-spacing:-.05em;color:#A8463B;line-height:1;white-space:nowrap">+22.000 €</div>'
   '<div class="a" style="left:100px;right:90px;top:640px;font-size:66px;line-height:1.12">Germania: oltre 56.000 €.<br/>Italia: 34.213 €.</div>'
   '<div class="a" style="left:100px;right:90px;top:900px;font-size:66px;line-height:1.12">E no, non perché sono <em>più bravi</em>.</div>'
   '<div class="a" style="left:100px;top:1160px;transform:rotate(-5deg)"><span class="stamp" style="font-size:84px">il perché è nel reel ↓</span></div>')
shot('c2-risposta-tedesco','carta',b)
print('ok')
