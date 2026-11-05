"""Render every row of a TSV (id, start, song, artist, credit) with build.py, 3 at a time."""
import csv, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
tsv = sys.argv[1]
outdir = os.path.join(ROOT, os.path.splitext(os.path.basename(tsv))[0])
rows = list(csv.reader(open(tsv, encoding="utf-8"), delimiter="\t"))

def run(r):
    rid, start, song, artist, credit = r
    slug = re.sub(r"[^a-z0-9]+", "_", song.lower()).strip("_")
    out = os.path.join(outdir, f"{rid}_{slug}.mp4")
    if os.path.exists(out): return f"{rid} skip"
    res = subprocess.run([sys.executable, os.path.join(ROOT, "build.py"), "--start", start, "--song", song,
                          "--artist", artist, "--credit", credit, "--out", out], capture_output=True, text=True)
    return f"{rid} {'ok' if res.returncode == 0 else 'FAIL ' + res.stderr[-300:]}"

with ThreadPoolExecutor(3) as ex:
    for msg in ex.map(run, rows): print(msg, flush=True)
