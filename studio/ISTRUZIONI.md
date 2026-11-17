# Economia Capita — routine del reel quotidiano

Obiettivo: **un reel al giorno**, pronto per l'approvazione verso le 14, pubblicato su Instagram **alle 17:00 (Europe/Rome) solo dopo l'"ok" esplicito di Gianmarco nella sessione del giorno**.

## Regole fisse
- Lingua: italiano. Tono: divulgatore curioso, ma anche volgare e intrattenente come un amico. Il **gancio iniziale non è volgare**; dentro il video qualche parolaccia ci sta.
- **Mai nominare l'università o il corso di Gianmarco** (vedi l'attività programmata) nei video, nelle didascalie o nei copioni: i video sono per tutti.
- Niente "AI slop": animazioni con un'idea visiva per ogni frase, timbri, omini, grafici che si disegnano. Mai stock generico.
- Fatti verificati con ricerca web prima di scrivere; fonti nella didascalia. Niente cifre a memoria.
- Temi politici: spiegare come funziona, mai dire se è giusto o sbagliato.
- **Mai aprire, stampare o committare `.env.local`.** La chiave ElevenLabs si legge solo dall'ambiente.
- **Mai pubblicare senza l'"ok" di Gianmarco nella sessione.** Senza risposta: non si pubblica, si lascia tutto pronto.

## Cosa funziona (dati TikTok/Instagram)
- Il pubblico decide nei primi 2–3 secondi: gancio di 5–6 parole, provocatorio, in movimento subito.
- Durata ideale 40–55 s. Distanziare i post (uno al giorno, non di più).
- I migliori: reel 1 sul '29 (49% di permanenza a 2 s), il carosello su GTA 6.

## Brand
- Palette "Vecchia Lira": carta #EDE6D3, chiara #F6F1E4, inchiostro #2B2A4C, tenue #4A4966, timbro #A8463B, rosa #C96F62, salvia #8FAE95, ocra #E3B23C, linea #D8CFB8. Tema notte = fondo inchiostro con accento ocra.
- Font: EB Garamond (titoli), IBM Plex Sans (testo), IBM Plex Mono (etichette maiuscole).
- Firma visiva: foglio a righe con margine rosso, timbro che cade (0.24 s power4.in + scossa), barra di avanzamento rossa in basso, chiusura "Economia [Capita]" col timbro e jingle_out.
- Zona sicura reel: didascalie in alto (top 300), grafica tra y 600 e 1450; niente in basso sotto 1500 né a destra oltre x 960.

## Procedura (cartella `studio/`)
1. **Setup**: `pip install -r requirements.txt numpy --break-system-packages`. Chiave: con i tool del computer (`device_stage_files`) copia `/Users/gianmarcoromei/Desktop/economia-capita/.env.local` in `studio/.env.local` **senza aprirlo**. Se il computer non risponde, avvisa Gianmarco (push) e chiedigli di accenderlo/aprire l'app Claude.
2. **Argomento**: leggi `pubblicati.md`. Se c'è una promessa aperta ("nel prossimo…"), fai quella. Altrimenti cerca notizie economiche del giorno (Italia/giovani/soldi/tecnologia) o un caso storico folle. Niente doppioni.
3. **Copione** in `copioni/reelNN-titolo.txt`: ~120–150 parole, tag vocali tra parentesi quadre ([shouting], [laughs], [whispers], [serious]), finale con "Seguimi: nel prossimo…".
4. **Voce**: `python3 src/voce.py copioni/reelNN-titolo.txt reelNN` → `audio/voce-reelNN.mp3` + `audio/words-reelNN.json` (tempi parola per parola). Voce Brando (voce.json, modello eleven_v4, stabilità 0.5, somiglianza 0.75).
5. **Video**: copia `src/reel05.py` in `src/reelNN.py` e riscrivi didascalie, scene, animazioni ed effetti sui tempi delle parole. `python3 src/reelNN.py`, poi in `reel-NN/`: `npx --yes hyperframes@0.9.58 lint`, `npx --yes hyperframes@0.9.58 snapshot --at <tempi chiave> -o /tmp/sNN --no-end` e **guarda il contact sheet**: correggi sovrapposizioni e testi fuori dai bordi prima di renderizzare.
6. **Render e mix**: `npx --yes hyperframes@0.9.58 render -o /tmp/reelNN-video.mp4 --quiet` (≈3 min), poi `python3 src/mix.py NN /tmp/reelNN-video.mp4 ../reel/reel-NN-titolo.mp4`.
7. **Copertina**: copia `src/copertine/reel-05.html` in un progetto temporaneo con i file di `template/`, cambia testi, `snapshot --at 0.5`, converti in JPEG (`ffmpeg -i x.png -q:v 2 ../reel/copertina-reel-NN.jpg`).
8. **Didascalia**: 4 paragrafi brevi + fonti + 10 hashtag (#economia #economiacapita …).
9. **Approvazione**: manda a Gianmarco video, copertina e didascalia (SendUserFile) + notifica push "Reel di oggi pronto: ok per le 17?". Copia il video anche sul Desktop (`/Users/gianmarcoromei/Desktop/economia-capita/reel-NN/`) per TikTok.
10. **Dopo l'ok**: commit e push di `reel/` e `studio/` (MAI .env.local). URL pubblico: `https://cdn.jsdelivr.net/gh/gianmarcoRomei/economia-capita-media@<sha-commit>/reel/<file>` (usa lo sha, non @main, per evitare la cache). Alle 17:00 (se l'ok arriva prima, programma con send_later per le 17:00 in questa sessione; se arriva dopo, pubblica subito): Windsor `instagram` → `create_video_post` sull'account `17841479750081873`, con `video_url`, `cover_url`, `caption`, `share_to_feed: true`.
11. Aggiorna `pubblicati.md` (riga nuova + promessa per il prossimo) e fai push.
