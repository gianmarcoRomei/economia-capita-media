"""Mixa voce + effetti sonori sul video renderizzato.

Uso: python3 src/mix.py 06 /tmp/reel06-video.mp4 out/reel-06.mp4
Legge audio/voce-reel06.mp3 e reel-06/sfx.json (lista di [nome, secondo, guadagno_db]).
"""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nn, video, out = sys.argv[1], sys.argv[2], sys.argv[3]
D = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', video],
                         capture_output=True, text=True).stdout)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{BASE}/audio/voce-reel{nn}.mp3', '-ar', '48000', '-ac', '1', '-f', 'f32le', '-'],
                     capture_output=True).stdout
v = np.frombuffer(raw, np.float32)
voice = np.zeros(int(sfx.SR * D)); voice[:min(len(v), len(voice))] = v[:len(voice)]
fx = sfx.place(D, [tuple(e) for e in json.load(open(f'{BASE}/reel-{nn}/sfx.json'))], gain_db=-7)
mix = np.tanh((voice + fx) * 1.1) / np.tanh(1.1)
wav = f'{BASE}/audio/reel{nn}-mix.wav'
sfx.save(wav, mix * 0.9)
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', video, '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', out], check=True)
print('ok', out)
