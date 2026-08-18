# Session Summary — Marathi Bhasha Bhed

Last updated: 10 Aug 2026

## Project Overview
- Marathi language education website (मराठी भाषा भेद, इयत्ता ११ वी)
- Location: `C:\Users\manoh\Downloads\ULS\marathi-bhasha-bhed\`
- GitHub repo: `https://github.com/coderm046-stack/ULS` (branch `main`, HTTPS remote)
- gh CLI authenticated as `coderm046-stack`

## File Structure
- `index.html` — main page (sections: home, comparison, poems, quiz, map, boli, qr — in that order; QR moved to last)
- `css/styles.css` — all styles (~1210 lines)
- `js/app.js` — section toggle, map clicks, quiz, QR generation
- `data/dialects.json` — dialect word data for comparison/quiz
- `README.md`
- `varli.html`, `ahirani.html`, `vaidarbhi.html`, `konkani.html` — standalone dialect detail pages (hero, anchor nav, 8 sections each, cross-linked, share `css/styles.css`)
- `audio\` — generated audio (50 MP3 files: marathi/warli/ahirani/vaidarbhi/konkani × 10 sentences)
- `gen_audio.py` — edge-tts generation script (kept in project)

## What Was Done This Session
1. **Real Maharashtra map** — replaced fake SVG polygon with real state boundary from India topo data (Mercator projection, viewBox `0 0 500 420`). 8 dialect markers at real geographic positions.
2. **District boundaries** — added all 35 district outlines to the map SVG (`<path class="district-boundary">`), using `udit-001/india-maps-data` topojson (2011 census, includes Mumbai & Palghar). CSS: `fill:none; stroke:var(--secondary); opacity:0.4; width:0.75; pointer-events:none`. Dialect points recomputed to match new projection.
3. **QR section moved to last** — reordered sections so QR comes after बोलीभाषा परिचय (boli).
4. **Audio generation** — created 10 sample sentences in Marathi + 4 dialects (warli, ahirani, vaidarbhi, konkani). Generated with `edge-tts`:
   - Marathi: female voice `mr-IN-AarohiNeural`
   - Dialects: male voice `mr-IN-ManoharNeural`
   - **Caveat**: no dialect TTS voices exist; dialect audio spoken with standard Marathi accent (approximate)

## Commits Made
- `e16d9f9` — real Maharashtra map
- `d0e7ba6` — district boundaries added
- `0a9926c` — QR section moved to last

## Pending / Next Steps (for tomorrow)
- **User will record proper dialect audio** (native speaker recordings) to replace TTS previews
- User to save recordings as `audio\<dialect>\s01.mp3` … `s10.mp3` (same naming as now)
- Then upload/add audio files to the website (e.g., QR codes pointing to audio, or play buttons)
- User may still confirm/correct dialect sentence spellings in `gen_audio.py`

## Technical Notes
- TTS: `py -m edge_tts --list-voices` shows only `mr-IN-AarohiNeural` and `mr-IN-ManoharNeural`
- To re-run TTS generation: `py gen_audio.py` (set `$env:PYTHONIOENCODING="utf-8"` first — Windows console errors otherwise)
- Map data scripts kept in `C:\Users\manoh\AppData\Local\Temp\opencode\mh-map\` (`extract.js`, `extract-districts.js`, `gen-svg.js`, `mh-districts.topo.json`, `districts.svg.html`)
- Git: LF→CRLF warnings on `git add` are expected/harmless
- Deleted leftover `india.topo.json` from project folder (unused data file)
- TTS preview files NOT yet committed to git (user may still want to keep or delete them)
