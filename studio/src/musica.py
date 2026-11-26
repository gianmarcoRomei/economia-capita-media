"""Base musicale sintetica per i reel senza voce.
Uso: python3 src/musica.py 57.0 audio/musica-reel08.wav
Beat leggero a 100 BPM (cassa, charleston, basso, accordi morbidi), Am-F-C-G.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx
from sfx import SR, t, lp, hp

D, out = float(sys.argv[1]), sys.argv[2]
BPM = 100; beat = 60 / BPM; bar = beat * 4
N = int(SR * D); mix = np.zeros(N + SR * 2)
rng = np.random.default_rng(3)

def add(sig, at, g):
    i = int(at * SR); j = min(len(mix), i + len(sig)); mix[i:j] += sig[:j - i] * g

def kick():
    tt = t(0.3); f = 110 * np.exp(-tt * 25) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 12)
def hat():
    tt = t(0.05); return hp(rng.standard_normal(len(tt)), 6000) * np.exp(-tt * 90)
def snare():
    tt = t(0.2); n = rng.standard_normal(len(tt))
    return (lp(n, 4000) * 0.7 + np.sin(2 * np.pi * 190 * tt) * 0.5) * np.exp(-tt * 22)
def bass(fr, d):
    tt = t(d); s = np.tanh(1.8 * np.sin(2 * np.pi * fr * tt))
    return lp(s, 500) * np.minimum(tt / 0.01, 1) * np.exp(-tt * 1.6)
def pad(frs, d):
    tt = t(d); s = sum(np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt) for f in frs)
    e = np.minimum(tt / 0.25, 1) * np.minimum((d - tt) / 0.4, 1)
    return s * e / len(frs)

hz = lambda m: 440 * 2 ** ((m - 69) / 12)
prog = [(45, [57, 60, 64]), (41, [57, 60, 65]), (48, [55, 60, 64]), (43, [55, 59, 62])]  # Am F C G
K, H, S = kick(), hat(), snare()
nb = int(D / bar) + 1
for b in range(nb):
    t0 = b * bar
    root, ch = prog[b % 4]
    add(pad([hz(m) for m in ch], bar), t0, 0.10)
    add(bass(hz(root), beat * 1.5), t0, 0.22); add(bass(hz(root), beat * 1.5), t0 + beat * 2, 0.18)
    add(bass(hz(root + 12), beat * 0.5), t0 + beat * 3.5, 0.12)
    if b == 0:  # intro: solo accordi
        continue
    for k in range(4):
        add(K, t0 + k * beat, 0.45 if k in (0, 2) else 0.0)
        add(H, t0 + k * beat + beat / 2, 0.10)
        if k in (1, 3):
            add(S, t0 + k * beat, 0.16)

m = mix[:N]
fade = int(SR * 2.0); m[-fade:] *= np.linspace(1, 0, fade)
m = m / np.max(np.abs(m)) * 0.5
sfx.save(out, m)
print('ok', out)
