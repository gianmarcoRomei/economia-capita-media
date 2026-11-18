import subprocess, os
OUT='instagram/carosello-pane'; os.makedirs(OUT, exist_ok=True)
CSS=open('/tmp/css_base.txt').read() if os.path.exists('/tmp/css_base.txt') else ''
CSS+='''
.date{position:absolute;left:100px;top:150px;font-family:"IBM Plex Mono",monospace;font-size:34px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.num{position:absolute;left:92px;top:205px;font-family:"IBM Plex Mono",monospace;font-weight:500;letter-spacing:-.05em;line-height:1;white-space:nowrap}
.unit{font-size:.28em;letter-spacing:0;margin-left:.15em;color:var(--mut)}
.say{position:absolute;left:100px;right:80px;top:560px;font-size:60px;line-height:1.08}
.tease{position:absolute;right:80px;bottom:120px;font-size:48px;font-style:italic;color:var(--acc)}
.badge{position:absolute;font-family:"IBM Plex Mono",monospace;font-weight:500;font-size:46px;color:var(--acc);border:5px solid var(--acc);border-radius:10px;padding:4px 18px;transform:rotate(-5deg)}
.tl{position:absolute;left:100px;right:80px;top:110px;height:8px;background:var(--rule)}
.tl i{position:absolute;left:0;top:0;bottom:0;background:var(--acc)}
'''
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,500;0,600;1,500&family=IBM+Plex+Mono:wght@500&display=swap">'
def shot(name, html, w=1080):
    p=f'/tmp/{name}.html'; open(p,'w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=4000',
                    f'--screenshot={OUT}/{name}.png',f'--window-size={w},1350','file://'+p],capture_output=True)
def bread(x,y,s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-150,40 Q-160,-70 -60,-95 Q0,-110 60,-95 Q160,-70 150,40 Z" fill="#C9955B" stroke="var(--fg)" stroke-width="6"/>'
            '<path d="M-80,-55 Q-60,-20 -70,15 M-15,-70 Q5,-30 -5,10 M50,-60 Q70,-25 60,12" stroke="var(--fg)" stroke-width="6" fill="none" stroke-linecap="round"/></g>')
def stack(x,base,n):
    g=''
    for k in range(n):
        dx=(k*37)%23-11
        g+=f'<g transform="translate({x+dx} {base-k*28})"><rect x="-120" y="-24" width="240" height="24" rx="3" fill="#8FAE95" stroke="var(--fg)" stroke-width="4"/><circle cx="0" cy="-12" r="7" fill="none" stroke="var(--fg)" stroke-width="3"/></g>'
    return g
def page(theme, prog, body, w=1080, foot=True):
    f=('<div class="foot"><span class="wm">economia <i>capita</i></span><span class="sw"></span></div>' if foot else '')
    return (f'<html><head>{FONTS}<style>{CSS} body{{width:{w}px}}</style></head><body class="{theme}">'
            f'<div class="tl"><i style="width:{prog}%"></i></div>{body}{f}</body></html>')

steps=[ # (data, prezzo, size, frase, teaser, badge, note, tema, progress%)
 ('dicembre 1918','0,50',300,'Un pane a Berlino. Normale. <em>Ricordati questo numero.</em>','scorri. ogni slide passa il tempo →',None,1,'carta',2),
 ('dicembre 1921','4',300,'Tre anni dopo. Un po&#39; caro, ma vabbè.','aspetta.','×8',2,'carta',20),
 ('dicembre 1922','163',300,'Quaranta volte in <em>un anno</em>.','eh. peggiora.','×41',3,'carta',38),
 ('giugno 1923','1.465',280,'Lo Stato spende <em>sette volte</em> quello che incassa.','tieniti forte.','×9',5,'carta',55),
 ('agosto 1923','69.000',250,'In due mesi. Il caffè costa di più <em>quando lo finisci</em> che quando lo ordini.','non è finita.','×47',8,'notte',70),
 ('settembre 1923','1.512.000',190,'Un milione e mezzo. Per <em>un pane</em>.','ok, ora è ridicolo.','×22',11,'notte',80),
 ('ottobre 1923','1.743.000.000',128,'Quasi due miliardi. Bruciano le banconote nella stufa: costano meno della legna.','il prossimo non ci sta in una slide →','×1.153',13,'notte',90),
]
for i,(d,p,sz,say,tease,badge,n,th,prog) in enumerate(steps,1):
    b=f'<div class="date">{d} · un pane, in marchi</div><div class="num" style="font-size:{sz}px">{p}</div>'
    b+=f'<div class="say">{say}</div>'
    b+=f'<svg class="a" style="left:0;top:0" width="1080" height="1350" viewBox="0 0 1080 1350">{bread(290,1060,1.25)}{stack(760,1150,n)}</svg>'
    if badge: b+=f'<div class="badge" style="left:150px;top:830px">{badge}</div>'
    b+=f'<div class="tease">{tease}</div>'
    if i==1: b+='<div class="a lab" style="left:100px;top:720px;color:var(--acc)">alla fine scopri chi è stato</div>'
    shot(f'slide-{i:02d}', page(th,prog,b))
# 8-9 panorama
pb=('<div class="date">novembre 1923 · un pane, in marchi</div>'
    '<div class="num" style="font-size:236px;top:300px;left:100px">201.000.000.000</div>'
    '<div class="a" style="left:110px;top:620px;font-size:76px;line-height:1.05;width:900px">Duecentouno <em>miliardi</em> di marchi.</div>'
    '<div class="a" style="left:1190px;top:600px;font-size:58px;line-height:1.1;width:880px">Per lo stesso pane di cinque anni prima. <br/>Prezzo moltiplicato per <em>400 miliardi</em>.</div>'
    f'<svg class="a" style="left:0;top:0" width="2160" height="1350" viewBox="0 0 2160 1350">{bread(300,1080,1.25)}{stack(760,1170,9)}{stack(1250,1170,9)}{stack(1700,1170,9)}</svg>'
    '<div class="a" style="right:80px;top:1200px;font-size:52px;font-style:italic;color:var(--acc)">chi è stato? →</div>')
shot('pano', page('notte',100,pb,2160,foot=False), 2160)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{OUT}/pano.png','-vf','crop=1080:1350:0:0',f'{OUT}/slide-08.png'])
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{OUT}/pano.png','-vf','crop=1080:1350:1080:0',f'{OUT}/slide-09.png'])
# 10 chi è stato
b=('<div class="date">chi è stato?</div>'
   '<div class="a h1" style="left:100px;top:210px;right:80px">Lo Stato. <em>Ha acceso la stampante.</em></div>'
   '<div class="a p" style="left:100px;top:480px;right:80px">Pieno di debiti di guerra, invece di tassare stampava banconote. Più soldi in giro, stesso pane da comprare: <b>ogni marco valeva meno</b>.</div>'
   '<div class="a card" style="left:100px;top:790px;width:880px;padding:30px 40px"><div class="lab" style="color:var(--acc)">come ne sono usciti</div><div class="p" style="margin-top:10px">Nuova moneta, novembre 1923: <b>1 marco nuovo = 1.000 miliardi di vecchi</b>. Hanno cancellato 12 zeri.</div></div>'
   '<div class="a" style="left:100px;top:1130px;font-size:40px;font-style:italic;color:var(--mut)">Mandalo a chi dice che oggi è tutto caro.</div>')
shot('slide-10', page('carta',100,b))
print('ok')
