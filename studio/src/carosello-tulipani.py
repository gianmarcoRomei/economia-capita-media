import subprocess, os
OUT='instagram/carosello-tulipani'; os.makedirs(OUT, exist_ok=True)
CSS=open('/tmp/css_base.txt').read()+'''
.date{position:absolute;top:150px;font-family:"IBM Plex Mono",monospace;font-size:32px;letter-spacing:.12em;text-transform:uppercase;opacity:.7}
.big{position:absolute;top:200px;font-family:"IBM Plex Mono",monospace;font-weight:500;letter-spacing:-.05em;line-height:1;white-space:nowrap}
.say{position:absolute;width:880px;font-size:56px;line-height:1.1}
.tease{position:absolute;bottom:120px;font-size:46px;font-style:italic}
.tl{position:absolute;left:100px;right:80px;top:110px;height:8px;background:var(--rule)}
.tl i{position:absolute;left:0;top:0;bottom:0;background:var(--acc)}
.unit{font-size:.3em;letter-spacing:0;margin-left:.12em;opacity:.7}
'''
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,500;0,600;1,500&family=IBM+Plex+Mono:wght@500&display=swap">'
def shot(name, html, w=1080):
    p=f'/tmp/tu-{name}.html'; open(p,'w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=4000',
                    f'--screenshot={OUT}/{name}.png',f'--window-size={w},1350','file://'+p],capture_output=True)
def page(theme, body, w=1080, prog=None, foot=True):
    f='<div class="foot"><span class="wm">economia <i>capita</i></span><span class="sw"></span></div>' if foot else ''
    t=f'<div class="tl"><i style="width:{prog}%"></i></div>' if prog is not None else ''
    return f'<html><head>{FONTS}<style>{CSS} body{{width:{w}px}}</style></head><body class="{theme}">{t}{body}{f}</body></html>'
def tulip(x,y,s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0,0 L0,90" stroke="#5E8A69" stroke-width="10"/>'
            '<path d="M0,60 Q-40,40 -46,10 Q-14,26 0,52" fill="#8FAE95"/>'
            '<path d="M-38,-60 Q-40,0 0,4 Q40,0 38,-60 L20,-30 L0,-70 L-20,-30 Z" fill="#F6F1E4" stroke="#2B2A4C" stroke-width="5"/>'
            '<path d="M-20,-30 L-14,-2 M0,-70 L0,2 M20,-30 L14,-2" stroke="#A8463B" stroke-width="7" stroke-linecap="round"/></g>')
# 1 copertina
b=('<div class="a" style="left:0;top:0;width:1080px;height:640px;background:#E3B23C"></div>'
   '<div class="date" style="left:100px;color:#2B2A4C;opacity:1">olanda · 1600</div>'
   '<div class="a" style="left:92px;top:200px;right:60px;font-size:116px;line-height:1;font-weight:600;letter-spacing:-.03em;color:#2B2A4C">Questo fiore costava quanto una casa.</div>'
   f'<svg class="a" style="left:0;top:0" width="1080" height="1350" viewBox="0 0 1080 1350">{tulip(800,820,3.2)}</svg>'
   '<div class="a" style="left:100px;top:720px;width:520px;font-size:54px;line-height:1.12">Ogni slide passano un po&#39; di anni. Guarda dove va il prezzo.</div>'
   '<div class="a lab" style="left:100px;top:1010px;color:var(--acc)">alla fine: il colpo di scena</div>'
   '<div class="tease" style="right:80px;color:var(--acc)">scorri →</div>')
shot('slide-01', page('carta', b, prog=5))
# 2–8 panorama 7 slide
W=1080*7
pts=[(540,1200),(1620,1130),(2700,980),(3780,760),(4860,720),(5940,700),(6500,705),(6900,1360)]
path='M0,1190 '+' '.join(f'L{x},{y}' for x,y in pts)
bg=f'<rect x="{1080*5}" y="0" width="2160" height="1350" fill="#2B2A4C"/>'
marks=''.join(tulip(x,y-20,0.6) for x,y in pts[:5])
svg=(f'<svg class="a" style="left:0;top:0" width="{W}" height="1350" viewBox="0 0 {W} 1350">{bg}'
     f'<path d="{path}" fill="none" stroke="#A8463B" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>{marks}</svg>')
def blk(i, date, big, size, say, tease, col='#2B2A4C', acc='#A8463B', extra=''):
    x=1080*i+100
    return (f'<div class="date" style="left:{x}px;color:{col}">{date}</div>'
            f'<div class="big" style="left:{x-8}px;font-size:{size}px;color:{acc}">{big}</div>'
            f'<div class="say" style="left:{x}px;top:470px;color:{col}">{say}</div>{extra}'
            f'<div class="tease" style="left:{1080*i+1080-80}px;transform:translateX(-100%);white-space:nowrap;color:{acc}">{tease}</div>')
body=svg
body+=blk(0,'1623 · un bulbo di semper augustus','1.000<span class="unit">fiorini</span>',220,'Un artigiano guadagnava <b>circa 300 fiorini all&#39;anno</b>. Già tanto, eh.','e poi? →')
body+=blk(1,'1625','2.000<span class="unit">fiorini</span>',220,'Raddoppia in due anni. Ne esistono <em>una dozzina</em>.','continua →')
body+=blk(2,'1633','5.500<span class="unit">fiorini</span>',220,'Ormai è roba da ricchi. Gli altri <em>guardano</em>.','aspetta →')
body+=blk(3,'inizio 1637','10.000<span class="unit">fiorini</span>',176,'Quanto una casa sui canali di Amsterdam, <em>con carrozza e giardino</em>. 33 anni di stipendio.','e i tulipani normali? →')
body+=blk(4,'31 dic 1636 → 1 feb 1637','×12<span class="unit">in un mese</span>',230,'Anche i bulbi «comuni» impazziscono: da 125 a <em>1.500 fiorini</em> a libbra.','3 febbraio 1637 →')
body+=blk(5,'haarlem · 3 febbraio 1637','?',260,'Un&#39;asta di tulipani, come tante. Il banditore parte col prezzo…','e… →',col='#EDE6D3',acc='#E3B23C',
          extra=f'<div class="a" style="left:{1080*5+100}px;top:900px;transform:rotate(-6deg)"><span class="stamp" style="font-size:96px;color:#E3B23C;border-color:#E3B23C">nessuno compra.</span></div>')
body+=blk(6,'febbraio 1637','CRASH',230,'I prezzi crollano. I contratti non vengono pagati. È la <em>prima bolla</em> della storia.','così dicono i libri. ma… →',col='#EDE6D3',acc='#E3B23C')
shot('pano', page('carta', body, w=W, foot=False), W)
for k in range(7):
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'{OUT}/pano.png','-vf',f'crop=1080:1350:{1080*k}:0',f'{OUT}/slide-{k+2:02d}.png'])
# 9 colpo di scena
b=('<div class="date" style="left:100px">il colpo di scena</div>'
   '<div class="a h1" style="left:100px;top:210px;right:80px">Ma è vero <em>solo a metà</em>.</div>'
   '<div class="a p" style="left:100px;top:470px;right:80px">La storica Anne Goldgar ha scavato negli archivi olandesi: nessuna crisi economica, pochissimi rovinati. Il mercato era piccolo, fatto di ricchi collezionisti.</div>'
   '<div class="a card" style="left:100px;top:880px;width:880px;padding:30px 40px"><div class="lab" style="color:var(--acc)">e allora perché la conosciamo così?</div><div class="p" style="margin-top:10px">Pamphlet moralisti dell&#39;epoca e un libro del 1841 che l&#39;ha <b>gonfiata</b>. Una bella storia vende più di quella vera.</div></div>')
shot('slide-09', page('carta', b, prog=95))
# 10 lezione + cta
b=('<div class="a" style="left:0;top:0;width:1080px;height:1350px;background:#E3B23C"></div>'
   '<div class="date" style="left:100px;color:#2B2A4C;opacity:1">la lezione</div>'
   '<div class="a" style="left:92px;top:210px;right:80px;font-size:96px;line-height:1.04;font-weight:500;color:#2B2A4C">Una bolla è quando compri qualcosa <em style="color:#A8463B">solo perché</em> pensi che domani qualcuno la pagherà di più.</div>'
   '<div class="a" style="left:100px;top:800px;right:80px;font-size:56px;line-height:1.15;color:#2B2A4C">Ti ricorda qualcosa? Scrivi nei commenti <b>la bolla di oggi</b> ↓</div>'
   '<div class="a" style="left:100px;bottom:56px;font-size:34px;color:#2B2A4C">economia <i style="color:#A8463B">capita</i></div>')
shot('slide-10', page('carta', b, foot=False))
print('ok')
