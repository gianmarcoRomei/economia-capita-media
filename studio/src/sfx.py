import numpy as np, wave
SR=48000
rng=np.random.default_rng(7)
def t(d): return np.arange(int(SR*d))/SR
def env(n,a=0.003,dec=0.1):
    x=np.arange(n)/SR; e=np.minimum(x/a,1)*np.exp(-x/dec); return e
def lp(x,fc):
    a=np.exp(-2*np.pi*fc/SR); y=np.zeros_like(x); s=0
    for i,v in enumerate(x): s=(1-a)*v+a*s; y[i]=s
    return y
def hp(x,fc): return x-lp(x,fc)
def bp(x,lo,hi): return hp(lp(x,hi),lo)
def norm(x,peak): return x/np.max(np.abs(x))*peak
def stamp():
    tt=t(0.35); f=70*np.exp(-tt*6)+42
    thump=np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(tt),0.002,0.09)
    n=rng.standard_normal(len(tt)); slap=bp(n,900,5000)*env(len(tt),0.001,0.018)
    knock=np.sin(2*np.pi*260*tt)*env(len(tt),0.001,0.03)
    return norm(thump*1.0+slap*0.9+knock*0.4,0.9)
def whoosh(d=0.6):
    tt=t(d); n=rng.standard_normal(len(tt)); x=np.zeros_like(n)
    # sweep via chunked bandpass
    seg=len(n)//12
    for k in range(12):
        c=300+k*250; s=slice(k*seg,(k+1)*seg if k<11 else len(n)); x[s]=bp(n[s],c*0.5,c*2)
    e=np.sin(np.pi*np.linspace(0,1,len(tt)))**2
    return norm(lp(x,6000)*e,0.5)
def pop(f0=520):
    tt=t(0.07); f=f0+500*tt/0.07
    return norm(np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(tt),0.002,0.018),0.45)
def tick():
    tt=t(0.04); n=rng.standard_normal(len(tt))
    return norm(bp(n,2000,7000)*env(len(tt),0.0005,0.006),0.35)
def rise(d=0.9):
    tt=t(d); f=220+500*(tt/d)**1.5
    s=np.sin(2*np.pi*np.cumsum(f)/SR)+0.3*np.sin(4*np.pi*np.cumsum(f)/SR)
    e=(tt/d)**1.2*np.exp(-np.maximum(tt-d*0.85,0)*30)
    return norm(s*e,0.32)
def drop(d=1.0):
    tt=t(d); f=520*np.exp(-tt*2.2)+90
    s=np.sin(2*np.pi*np.cumsum(f)/SR)
    return norm(s*np.minimum(tt/0.02,1)*np.exp(-tt*1.5),0.38)
def ching():
    tt=t(0.9); s=sum(np.sin(2*np.pi*f*tt)*np.exp(-tt*k) for f,k in [(2093,5),(2637,6),(3136,7),(4186,9)])
    n=rng.standard_normal(len(tt)); click=bp(n,3000,9000)*env(len(tt),0.0005,0.01)
    return norm(s*np.minimum(tt/0.003,1)+click*2,0.35)
def rumble(d=1.6):
    tt=t(d); n=rng.standard_normal(len(tt)); x=lp(n,140)
    boom=np.sin(2*np.pi*np.cumsum(55*np.exp(-tt*1.2)+30)/SR)
    e=np.minimum(tt/0.01,1)*np.exp(-tt*1.8)
    return norm((x*3+boom)*e,0.7)
def rattle(d=0.35):
    tt=t(d); n=rng.standard_normal(len(tt)); x=bp(n,400,2500)
    am=(np.sin(2*np.pi*28*tt)>0.2).astype(float)
    return norm(x*am*np.exp(-tt*6),0.3)
def note(fr,d=0.5,g=1.0):
    tt=t(d); s=np.sin(2*np.pi*fr*tt)+0.35*np.sin(2*np.pi*fr*2*tt)*np.exp(-tt*6)+0.15*np.sin(2*np.pi*fr*3*tt)*np.exp(-tt*10)
    return s*np.minimum(tt/0.004,1)*np.exp(-tt*5.5)*g
def jingle(seq,step=0.19,tail=1.2):
    out=np.zeros(int(SR*(len(seq)*step+tail)))
    for i,fr in enumerate(seq):
        n=note(fr,0.9 if i==len(seq)-1 else 0.5); j=int(i*step*SR); out[j:j+len(n)]+=n
    return norm(out,0.5)
A4=440.0
def hz(semi): return A4*2**(semi/12)
lib=dict(jingle=jingle([hz(-7),hz(-9),hz(-2),hz(-5),hz(0),hz(-2),hz(3),hz(5),hz(3),hz(7),hz(12)],0.17),jingle_out=jingle([hz(12),hz(7),hz(3),hz(5),hz(0),hz(-5)],0.22,1.8),stamp=stamp(),whoosh=whoosh(),pop=pop(),tick=tick(),rise=rise(),drop=drop(),ching=ching(),rumble=rumble(),rattle=rattle())
def save(path,x):
    x=np.clip(x,-1,1); w=wave.open(path,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def place(length,events,gain_db=0):
    out=np.zeros(int(SR*length)+SR)
    for name,time,g in events:
        s=lib[name]*10**((g+gain_db)/20); i=int(time*SR); out[i:i+len(s)]+=s[:len(out)-i]
    return out[:int(SR*length)]
