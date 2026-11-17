#!/usr/bin/env python3
"""Copione -> voce ElevenLabs (+ tempi parola per parola).

Uso:
  python3 src/voce.py copioni/reel05.txt reel05
  -> audio/voce-reel05.mp3  e  audio/words-reel05.json  ([[inizio, fine, "parola"], ...])

La chiave viene letta da .env.local (ELEVENLABS_API_KEY), mai scritta nel codice.
Voce e impostazioni stanno in voce.json.
"""
import base64, json, os, re, subprocess, sys, tempfile

from dotenv import load_dotenv
from elevenlabs import ElevenLabs, VoiceSettings

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE, ".env.local"))

CFG = json.load(open(os.path.join(BASE, "voce.json")))
MAX_CHARS = 2500  # pezzi corti = meno derive su testi lunghi


def chunks(text):
    """Divide il copione per paragrafi senza superare MAX_CHARS."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    out, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) + 2 > MAX_CHARS:
            out.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        out.append(cur)
    return out


def words_from(al, offset):
    """Raggruppa l'allineamento per carattere in parole."""
    words, w, t0, t1 = [], "", None, None
    for ch, a, b in zip(al.characters, al.character_start_times_seconds,
                        al.character_end_times_seconds):
        if ch.isspace():
            if w:
                words.append([round(t0 + offset, 3), round(t1 + offset, 3), w])
            w, t0 = "", None
            continue
        if t0 is None:
            t0 = a
        w += ch
        t1 = b
    if w:
        words.append([round(t0 + offset, 3), round(t1 + offset, 3), w])
    return words


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, name = sys.argv[1], sys.argv[2]
    text = open(src, encoding="utf-8").read()
    parts = chunks(text)

    # l'SDK legge ELEVENLABS_API_KEY quando viene importato, prima di load_dotenv: la passiamo esplicitamente
    client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))
    settings = VoiceSettings(stability=CFG["stability"],
                             similarity_boost=CFG["similarity_boost"])
    tmp = tempfile.mkdtemp(prefix="voce-")
    files, words, offset, chars = [], [], 0.0, 0

    for i, part in enumerate(parts):
        res = client.text_to_speech.convert_with_timestamps(
            voice_id=CFG["voice_id"],
            text=part,
            model_id=CFG["model_id"],
            language_code=CFG.get("language_code"),
            voice_settings=settings,
            output_format="mp3_44100_128",
            previous_text=parts[i - 1] if i > 0 else None,
            next_text=parts[i + 1] if i + 1 < len(parts) else None,
        )
        f = os.path.join(tmp, f"p{i:03d}.mp3")
        with open(f, "wb") as fh:
            fh.write(base64.b64decode(res.audio_base_64))
        al = res.alignment or res.normalized_alignment
        words += words_from(al, offset)
        offset += duration(f)
        chars += len(part)
        files.append(f)
        print(f"  pezzo {i + 1}/{len(parts)} ok ({len(part)} caratteri)")

    out_mp3 = os.path.join(BASE, "audio", f"voce-{name}.mp3")
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{f}'\n" for f in files)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", out_mp3], check=True)

    out_words = os.path.join(BASE, "audio", f"words-{name}.json")
    json.dump(words, open(out_words, "w"), ensure_ascii=False)
    print(f"voce: {out_mp3} ({offset:.1f} s, {chars} caratteri)")
    print(f"parole: {out_words} ({len(words)})")


if __name__ == "__main__":
    main()
