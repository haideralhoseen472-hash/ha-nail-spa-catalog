"""3AM Thoughts reel builder — one continuous 60s take, 1080x1920, silent (song added in-app).

usage: python build.py --start 23:00 --song "Apocalypse" --artist "Cigarettes After Sex" \
                       --credit "© 2017 Partisan Records" --out reels/apocalypse.mp4 [--still 20]
Layout keeps everything above y≈1530 and clear of the right-hand button rail (YouTube Shorts / Reels UI).
"""
import argparse, math, subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src", "source.mp4")
AVATAR = os.path.join(ROOT, "..", "3am-thoughts", "pfp_B_window.png")
W, H, FPS, DUR = 1080, 1920, 30, 60.0

ap = argparse.ArgumentParser()
ap.add_argument("--start", required=True)          # mm:ss in source
ap.add_argument("--song", required=True)
ap.add_argument("--artist", required=True)
ap.add_argument("--credit", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--still", type=float)
A = ap.parse_args()
mm, ss = A.start.split(":"); START = int(mm) * 60 + int(ss)

# ---- layout (safe zone) ----
AV_C, AV_D = (540, 190), 190
NAME_Y = 312
VID_Y, VID_H = 430, 820
CARD_Y = 1290
L, R = 160, 920

NAME = "3AM Thoughts"
F = "C:/Windows/Fonts/"
f_name = ImageFont.truetype(F + "segoeuib.ttf", 60)
f_artist = ImageFont.truetype(F + "segoeui.ttf", 34)
f_time = ImageFont.truetype(F + "segoeui.ttf", 26)
f_small = ImageFont.truetype(F + "segoeuisl.ttf", 24)
f_sym = ImageFont.truetype(F + "seguisym.ttf", 24)

# shrink long song titles to fit the card
song_size = 50
while ImageFont.truetype(F + "segoeuib.ttf", song_size).getlength(A.song) > (R - L - 110) and song_size > 32:
    song_size -= 2
f_song = ImageFont.truetype(F + "segoeuib.ttf", song_size)

# ---- 1. the take ----
take = os.path.join(ROOT, "takes", f"take_{START}.mp4")
os.makedirs(os.path.dirname(take), exist_ok=True)
if not os.path.exists(take):
    crop_w = round(1080 * W / VID_H / 2) * 2
    vf = (f"fps={FPS},crop={crop_w}:1080,scale={W}:{VID_H}:flags=lanczos,"
          f"eq=contrast=1.06:saturation=0.85:gamma=0.97,setsar=1,format=yuv420p")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(START), "-t", str(DUR), "-i", SRC,
                    "-vf", vf, "-an", "-c:v", "libx264", "-crf", "14", "-preset", "medium", take], check=True)

# ---- 2. static assets ----
av = Image.open(AVATAR).convert("RGB").resize((AV_D * 2, AV_D * 2), Image.LANCZOS)
mask = Image.new("L", av.size, 0); ImageDraw.Draw(mask).ellipse((0, 0, *av.size), fill=255)
av.putalpha(mask)

def make_badge(sz):
    k = 8; S2 = sz * k; c = S2 / 2
    im = Image.new("RGBA", (S2, S2)); d = ImageDraw.Draw(im)
    pts = []
    for i in range(32):
        a = math.pi * 2 * i / 32; rr = (S2 / 2) * (1.0 if i % 2 == 0 else 0.86)
        pts.append((c + rr * math.cos(a), c + rr * math.sin(a)))
    d.polygon(pts, fill=(235, 235, 240, 255))
    w = int(S2 * 0.09)
    d.line([(S2 * 0.30, S2 * 0.52), (S2 * 0.44, S2 * 0.66), (S2 * 0.71, S2 * 0.37)], fill=(10, 10, 14, 255), width=w, joint="curve")
    for p in [(S2 * 0.30, S2 * 0.52), (S2 * 0.71, S2 * 0.37)]:
        d.ellipse((p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2), fill=(10, 10, 14, 255))
    return im.resize((sz, sz), Image.LANCZOS)

BADGE, BARS_W = 42, 44
badge = make_badge(BADGE)
name_w = f_name.getlength(NAME)
name_x0 = (W - (BARS_W + 20 + name_w + 14 + BADGE)) / 2

def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def fmt(s):
    s = int(s); return f"{s // 60}:{s % 60:02d}"

def bars(d, x, y_mid, t, alpha, n=4, bw=9, gap=4, hmax=42, hmin=12):
    for i in range(n):
        ph = i * 1.7
        v = math.sin(t * 5.1 + ph) * 0.5 + math.sin(t * 8.3 + ph * 2.1) * 0.3 + math.sin(t * 2.2 + ph) * 0.2
        h = hmin + (hmax - hmin) * (0.5 + 0.5 * v)
        bx = x + i * (bw + gap)
        d.rounded_rectangle((bx, y_mid - h / 2, bx + bw, y_mid + h / 2), radius=bw / 2, fill=(255, 255, 255, int(255 * alpha)))

def fade(im, k):
    if k >= 1: return im
    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda p: int(p * k))); return im

def frame(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out = 1 - ease((t - (DUR - 0.9)) / 0.9)

    # avatar
    a_in = ease(t / 0.9)
    breathe = 1 + 0.018 * math.sin(t * 2 * math.pi / 4.0)
    size = int(AV_D * (0.86 + 0.14 * a_in) * breathe)
    glow = Image.new("RGBA", (W, H)); gd = ImageDraw.Draw(glow)
    gr = size / 2 + 9
    ga = int((60 + 40 * math.sin(t * 2 * math.pi / 4.0)) * a_in * out)
    gd.ellipse((AV_C[0] - gr, AV_C[1] - gr, AV_C[0] + gr, AV_C[1] + gr), outline=(255, 255, 255, ga), width=3)
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(6)))
    im.alpha_composite(fade(av.resize((size, size), Image.LANCZOS), a_in * out), (AV_C[0] - size // 2, AV_C[1] - size // 2))
    d = ImageDraw.Draw(im)
    rr = size / 2 + 1
    d.ellipse((AV_C[0] - rr, AV_C[1] - rr, AV_C[0] + rr, AV_C[1] + rr), outline=(255, 255, 255, int(85 * a_in * out)), width=2)

    # name + bars + badge
    k = ease((t - 0.3) / 0.8); n_in = k * out
    y = NAME_Y + int(18 * (1 - k))
    bars(d, name_x0, y + 40, t, n_in)
    x = name_x0 + BARS_W + 20
    d.text((x, y), NAME, font=f_name, fill=(255, 255, 255, int(255 * n_in)))
    im.alpha_composite(fade(badge, n_in), (int(x + name_w + 14), int(y + 41 - BADGE / 2)))
    d = ImageDraw.Draw(im)

    # song card
    k = ease((t - 0.7) / 0.9); c_in = k * out
    cy0 = CARD_Y + int(30 * (1 - k)); wa = int(255 * c_in)
    bx, by = L, cy0 + 6
    d.rounded_rectangle((bx, by, bx + 80, by + 80), radius=18, fill=(255, 255, 255, int(28 * c_in)),
                        outline=(255, 255, 255, int(70 * c_in)), width=2)
    bars(d, bx + 21, by + 40, t + 0.4, c_in, n=4, bw=7, gap=4, hmax=38, hmin=10)
    tx = bx + 104
    d.text((tx, cy0 + (50 - song_size) // 2), A.song, font=f_song, fill=(255, 255, 255, wa))
    d.text((tx, cy0 + 60), A.artist, font=f_artist, fill=(190, 190, 190, wa))
    py = cy0 + 128
    d.rounded_rectangle((L, py, R, py + 6), radius=3, fill=(255, 255, 255, int(55 * c_in)))
    px = L + (R - L) * min(1.0, t / DUR)
    d.rounded_rectangle((L, py, max(L + 6, px), py + 6), radius=3, fill=(255, 255, 255, wa))
    d.ellipse((px - 10, py - 7, px + 10, py + 13), fill=(255, 255, 255, wa))
    d.text((L, py + 20), fmt(t), font=f_time, fill=(170, 170, 170, wa))
    rem = "-" + fmt(math.ceil(DUR - t))
    d.text((R - f_time.getlength(rem), py + 20), rem, font=f_time, fill=(170, 170, 170, wa))
    cr = f"{A.song} — {A.artist}  ·  {A.credit}"
    cx0 = (W - f_small.getlength(cr) - 32) / 2
    d.text((cx0, py + 70), "\u266A", font=f_sym, fill=(130, 130, 130, wa))
    d.text((cx0 + 32, py + 72), cr, font=f_small, fill=(130, 130, 130, wa))
    return im

if A.still is not None:
    t = A.still
    base = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    vf = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", take, "-frames:v", "1",
                         "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True).stdout
    base.alpha_composite(Image.frombytes("RGBA", (W, VID_H), vf), (0, VID_Y))
    base.alpha_composite(frame(t))
    base.convert("RGB").save(A.out.replace(".mp4", f"_still{t:g}.jpg"), quality=92)
    raise SystemExit

os.makedirs(os.path.dirname(os.path.abspath(A.out)), exist_ok=True)
fc = (f"color=black:s={W}x{H}:r={FPS}:d={DUR}[bg];"
      f"[0:v]fade=in:st=0.2:d=1.0,fade=out:st={DUR-1.0}:d=1.0[vid];"
      f"[bg][vid]overlay=0:{VID_Y}[b1];[b1][1:v]overlay=0:0:format=auto,format=yuv420p[out]")
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-i", take,
                      "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-filter_complex", fc, "-map", "[out]", "-t", str(DUR),
                      "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-profile:v", "high",
                      "-movflags", "+faststart", A.out], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    p.stdin.write(frame(i / FPS).tobytes())
p.stdin.close(); p.wait()
print("done")
