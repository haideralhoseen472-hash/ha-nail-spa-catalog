---
name: project-3am-thoughts
description: 3AM Thoughts YouTube Shorts channel (@the3amthoughtsx) — night-drive music edits, 2 reels/day, batch pipeline in reel-apocalypse/
metadata:
  type: project
---

YouTube channel **3AM Thoughts** (@the3amthoughtsx), started 2026-10-20. Aesthetic sad-song edits: one continuous 60s night-drive take + top bar (channel pfp, "3AM Thoughts", white badge, animated EQ bars) + music-player card with song/artist/credit. Goal: ~2 reels per day.

- Pipeline: `كلاود ترى المادة هنا/reel-apocalypse/` — `build.py` (one reel, args --start/--song/--artist/--credit/--out), `batch.py weekN.tsv` (renders TSV rows, 3 parallel), `weekN_schedule.md` (titles/tags).
- Footage: 1-hour "Sad Hours" YouTube video (FnLF_cjO1KI) in src/ — third-party, claim risk; user accepted. Minute 23 used for Apocalypse; week1 used 3–44 min.
- Branding: `3am-thoughts/` — pfp_B_window.png chosen (rainy window bokeh), banner_2560x1440.jpg, fonts Cormorant/Josefin.
- Videos exported SILENT; user adds the song from YouTube's sound library (licensed). Layout must stay above y≈1530 and clear of right rail (Shorts UI covered the first upload's bottom card).

**Why:** user wants a monetisable music-edit channel with consistent identity.
**How to apply:** reuse build.py/batch.py for new weeks; vary footage minutes and songs; suggest new royalty-free night-drive footage once the hour runs out. Related: [[user-profile]], [[feedback-design-workflow]]
