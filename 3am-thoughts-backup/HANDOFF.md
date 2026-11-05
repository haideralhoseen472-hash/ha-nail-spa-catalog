# 3AM Thoughts — ملخص كامل للمشروع (للجلسة الجديدة)

> **إلى Claude بالجلسة الجديدة:** اقرأ هذا الملف كامل قبل ما تبدي.
> هو ملخص لكل الشغل اللي صار على قناة اليوتيوب **3AM Thoughts**، وفيه الأوامر والإعدادات
> حتى تكمل المونتاج بدون ما تسأل المستخدم عن شي معروف.
> المستخدم يحچي **عراقي**، فجاوبه بالعراقي وبجمل بسيطة.

---

## 1. شنو صار باختصار

1. سوّينا قناة يوتيوب Shorts اسمها **3AM Thoughts**، والـ handle مالها **@the3amthoughtsx**.
2. فكرة القناة: ريلز بيها أغاني حزينة ولقطة سياقة بالليل والمطر (night drive)، ويا كرت موسيقى بالشاشة.
3. سوّينا أول ريل لأغنية **Apocalypse** (لـ Cigarettes After Sex)، من الدقيقة 23:00 بالفيديو المصدر.
4. بعدين سوّينا وجبة الأسبوع الأول: **14 ريل**، كل ريل **60 ثانية**، بمعدل ريلين باليوم لسبع أيام.
5. كتبنا جدول نشر فيه العنوان والوصف والتاغات والحقوق لكل ريل.
6. **الهارد مال حاسبة المستخدم تلف** وراحت كل الملفات اللي على الحاسبة:
   الفيديوهات، والسكربتات، وصورة البروفايل، والغلاف.
7. رجّعنا السكربتات والجدول من سجل الجلسة القديمة، وحفظناها على GitHub
   (التفاصيل بالقسم 2).
8. المستخدم نزّل فيديو مصدر **جديد** لفولدر على سطح المكتب، والمطلوب نسوي الريلز منه من جديد.

---

## 2. وين الملفات المحفوظة

- **GitHub repo:** `haideralhoseen472-hash/ha-nail-spa-catalog`
- **الفرع:** `claude/youtube-channel-videos-qk7xhs`
- **المجلد:** `3am-thoughts-backup/`

| الملف | شنو بيه |
|---|---|
| `build.py` | يسوي ريل واحد (60 ثانية، 1080×1920، بدون صوت) |
| `batch.py` | يسوي كل الريلز اللي بملف TSV، 3 بنفس الوقت |
| `week1.tsv` | الـ 14 أغنية: رقم، دقيقة البداية، الأغنية، الفنان، الحقوق |
| `week1_schedule.md` | جدول النشر: العناوين، والوصف، والتاغات، والتعليق المثبّت |
| `project-3am-thoughts.md` | ملخص هوية القناة وطريقة الشغل |
| `HANDOFF.md` | هذا الملف |

لتنزيلها على حاسبة المستخدم:

```bash
git clone -b claude/youtube-channel-videos-qk7xhs https://github.com/haideralhoseen472-hash/ha-nail-spa-catalog.git
```

أو من موقع GitHub: افتح الفرع ← مجلد `3am-thoughts-backup` ← نزّل الملفات.

> **ملاحظة:** OneDrive ممكن بعده بيه الفيديوهات القديمة. كانت بمسار
> `C:\Users\Al_Reem\OneDrive\Desktop\كلاود ترى المادة هنا\reel-apocalypse\`
> وبعده مجلد `week1\`. إذا المستخدم لگاها هناك (أو بالـ Recycle bin)، ما نحتاج نعيد المونتاج.

---

## 3. هوية القناة (Branding)

- **اسم القناة:** 3AM Thoughts
- **الـ handle:** @the3amthoughtsx
- **الستايل:** سياقة بالليل، مطر على الجام، أضواء مضبّبة (bokeh)، ألوان باهتة شوية، وجو هادي وحزين.
- **صورة البروفايل:** كانت `pfp_B_window.png`، صورة شباك عليه مطر وأضواء مضبّبة.
  **ضاعت ويا الهارد**، فلازم تنسوّى وحدة جديدة بنفس الفكرة:
  صورة مربعة (أقل شي 800×800)، شباك سيارة أو غرفة عليه قطرات مطر، وأضواء مدينة bokeh، بألوان داكنة.
- **الغلاف (Banner):** كان `banner_2560x1440.jpg`، و**ضاع هم**. الحجم المطلوب 2560×1440،
  والكتابة لازم تبقى بالنص بمساحة 1546×423 حتى تطلع على الموبايل.
- **خطوط الغلاف:** Cormorant (للعنوان) و Josefin Sans (للكتابة الصغيرة)، من Google Fonts.
- **خطوط الريل نفسه:** خطوط ويندوز Segoe UI (موجودة بأي ويندوز، ما تحتاج تنزيل).
- المجلد اللي كانت بيه هاي الصور اسمه `3am-thoughts/`، وكان جنب مجلد `reel-apocalypse/`.

---

## 4. شكل الريل (التصميم)

كل ريل:
- **الحجم:** 1080×1920 (عمودي)، **30 فريم بالثانية**، **60 ثانية بالضبط**
- **بدون صوت.** المستخدم يضيف الأغنية من مكتبة يوتيوب (Add sound) حتى ما ينضرب بحقوق.
- **لقطة وحدة متواصلة بدون قطع.** المستخدم فضّل هذا على المونتاج المقطّع،
  لأن المشاهد يندمج ويحس كأنه هو اللي يسوق.

ترتيب الشاشة من فوق لجوه:

| العنصر | المكان (بالبكسل) | التفاصيل |
|---|---|---|
| صورة البروفايل | المركز (540, 190)، القطر 190 | دائرية، تتنفس شوية، ويا هالة بيضاء خفيفة |
| اسم القناة | y = 312 | "3AM Thoughts" بخط Segoe UI Bold حجم 60 |
| أعمدة موسيقى | يسار الاسم | 4 أعمدة بيض تتحرك (equalizer) |
| علامة توثيق | يمين الاسم | دائرة بيضاء مسننة بيها ✓، **عنصر تصميم بس، مو توثيق حقيقي** |
| الفيديو | من y = 430، ارتفاعه 820 | اللقطة مقصوصة من النص ومكبّرة لعرض 1080 |
| كرت الأغنية | من y = 1290 | مربع أيقونة بيه أعمدة، واسم الأغنية، والفنان، وشريط تقدّم، والوقت |
| سطر الحقوق | تحت شريط التقدم | ♪ الأغنية — الفنان · © الحقوق |

**قواعد مهمة تعلمناها:**
- كل شي لازم يبقى **فوق y ≈ 1530**. بأول رفع، واجهة Shorts (الكابشن والأزرار) غطّت الكرت اللي جوه.
- لازم نبتعد عن **الجهة اليمين** (من x ≈ 920 وطالع)، لأن بيها أزرار اللايك والتعليق والشير.
- الحواف: يسار 160، يمين 920.
- إذا اسم الأغنية طويل، السكربت يصغّر الخط تلقائياً (من 50 لحد 32).

**الحركة (Animation):**
- البروفايل يطلع بأول 0.9 ثانية، والاسم بعده بـ 0.3 ثانية، والكرت بعده بـ 0.7 ثانية.
- الفيديو يبين تدريجياً من 0.2 لحد 1.2 ثانية، ويختفي بآخر ثانية.
- كل العناصر تختفي بآخر 0.9 ثانية.
- شريط التقدم يمشي ويا الوقت، من 0:00 لحد 1:00.

**تعديل الألوان على اللقطة:**
`eq=contrast=1.06:saturation=0.85:gamma=0.97`، يعني تباين أكثر شوية، وألوان أبهت شوية، وأغمق شوية.

---

## 5. البرامج المطلوبة على حاسبة المستخدم (ويندوز)

| البرنامج | ليش | التنصيب |
|---|---|---|
| **Python 3.10+** | يشغّل السكربتات | python.org، وفعّل "Add to PATH" |
| **Pillow** | يرسم البروفايل والاسم والكرت | `pip install pillow` |
| **ffmpeg** | يقص الفيديو ويطلّع الـ mp4 | `winget install Gyan.FFmpeg` |
| **yt-dlp** | ينزّل الفيديو المصدر من يوتيوب (إذا لزم) | `pip install yt-dlp` |
| **Git** (اختياري) | ينزّل الملفات من GitHub | `winget install Git.Git` |
| **Claude ديسكتوب** | تفتح بيه جلسة Claude Code على الحاسبة | claude.ai/download |

للتأكد إن كلشي منصّب:

```powershell
python --version
ffmpeg -version
python -c "import PIL; print(PIL.__version__)"
```

> **مهم:** جلسة Claude بالكلاود **ما توصل** لحاسبة المستخدم، وكمان يوتيوب ممنوع بيها.
> فالمونتاج لازم يصير **بجلسة Claude Code مفتوحة على حاسبة المستخدم نفسها**، جوه الفولدر اللي على سطح المكتب.

---

## 6. ترتيب الفولدر المطلوب

`build.py` يدور على الملفات بهذا الترتيب بالضبط:

```
Desktop\
├── 3am-thoughts\
│   └── pfp_B_window.png        ← صورة البروفايل (لازم تنسوّى من جديد)
└── <فولدر الشغل>\               ← مثلاً "night though" أو "3AM Thoughts"
    ├── build.py
    ├── batch.py
    ├── week1.tsv
    ├── week1_schedule.md
    ├── src\
    │   └── source.mp4          ← الفيديو المصدر، لازم يكون بهذا الاسم
    ├── takes\                  ← السكربت يسويه بنفسه (اللقطات المقصوصة)
    └── week1\                  ← السكربت يسويه بنفسه (الريلز النهائية)
```

- المستخدم سمّى فولدر على سطح المكتب **"night though"** ونزّل بيه الفيديو الجديد.
  أول شي، شوف شنو بيه بالضبط.
- **الفيديو لازم يتسمّى `source.mp4` وينحط جوه `src\`.**
- صورة البروفايل مسارها بالسكربت `..\3am-thoughts\pfp_B_window.png`، يعني فولدر جنب فولدر الشغل.
  إذا تريد تحطها بمكان ثاني، عدّل سطر `AVATAR` بـ `build.py`.

---

## 7. الفيديو المصدر

**الفيديو القديم (اللي سوّينا منه الأسبوع الأول):**
- فيديو "Sad Hours" على يوتيوب، رقمه `FnLF_cjO1KI`، طوله تقريباً ساعة.
- الدقايق اللي استخدمناها: من 03:00 لحد 44:00، ودقيقة 23:00 للـ Apocalypse.

**الفيديو الجديد (اللي دزه المستخدم بهاي المحادثة):**
- الرابط: https://youtu.be/pNphviNwFPY
- طوله: **ساعة و1 دقيقة** (3668 ثانية)
- المستخدم نزّله لفولدر على سطح المكتب.
- **الدقايق بـ `week1.tsv` مالت الفيديو القديم.** لازم تنختار دقايق جديدة تناسب هذا الفيديو (القسم 9).

إذا تحتاج تنزّله من جديد على الحاسبة:

```powershell
yt-dlp -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]" --merge-output-format mp4 -o "src/source.mp4" "https://youtu.be/pNphviNwFPY"
```

> **تحذير الحقوق:** الفيديو المصدر مال قناة ثانية، فممكن يجي claim. المستخدم يعرف وقبل بهذا.
> ذكّره مرة وحدة بس، ولا تعيدها كل مرة.
> الأحسن على المدى البعيد: لقطات night drive مجانية (royalty-free) من Pexels أو Pixabay.

---

## 8. أوامر المونتاج

كل الأوامر تنكتب جوه فولدر الشغل (PowerShell أو CMD).

### 8.1 ريل واحد

```powershell
python build.py --start 23:00 --song "Apocalypse" --artist "Cigarettes After Sex" --credit "© 2017 Partisan Records" --out reels/apocalypse.mp4
```

| الخيار | المعنى |
|---|---|
| `--start` | من وين تبدي اللقطة بالفيديو المصدر، بصيغة mm:ss |
| `--song` | اسم الأغنية اللي يطلع بالكرت |
| `--artist` | اسم الفنان |
| `--credit` | سطر الحقوق، مثل "© 2013 Columbia Records" |
| `--out` | وين ينحفظ الريل |
| `--still 20` | (اختياري) يطلّع صورة وحدة من الثانية 20 بدال الفيديو، للمعاينة السريعة |

### 8.2 معاينة قبل الرندر (أسرع بهواية)

```powershell
python build.py --start 12:00 --song "Test" --artist "Test" --credit "© Test" --out test/t.mp4 --still 20
```

يطلّع `test/t_still20.jpg`. افتحه وتأكد إن التصميم مضبوط قبل ما ترندر كلشي.

### 8.3 كل الريلز مرة وحدة

```powershell
python batch.py week1.tsv
```

- يقرأ كل سطر بـ `week1.tsv` ويشغّل `build.py` عليه.
- يشغّل **3 ريلز بنفس الوقت**.
- الريلز تنحفظ بفولدر اسمه مثل اسم الملف (`week1\`)، بأسماء مثل `02_sweater_weather.mp4`.
- إذا الريل موجود من قبل، يعبره (skip). فإذا وقف بالنص، شغّله مرة ثانية ويكمل.
- الوقت: تقريباً **25 دقيقة** للـ 14 ريل، حسب الحاسبة.

### 8.4 التأكد إن كل الريلز 60 ثانية

```powershell
Get-ChildItem week1\*.mp4 | ForEach-Object { $_.Name + "  " + (ffprobe -v error -show_entries format=duration -of csv=p=0 $_.FullName) }
```

### 8.5 ورقة فحص (Contact sheet) لكل الريلز

```powershell
mkdir qc -Force
Get-ChildItem week1\*.mp4 | ForEach-Object { ffmpeg -v error -y -ss 20 -i $_.FullName -frames:v 1 -vf scale=270:480 ("qc\" + $_.BaseName + ".jpg") }
ffmpeg -v error -y -pattern_type glob -i "qc/*.jpg" -vf tile=7x2 qc_sheet.jpg
```

> على ويندوز ممكن `-pattern_type glob` ما يشتغل. بديله:
> `ffmpeg -i qc\%02d.jpg ...` بعد ما تعيد تسمية الصور 01.jpg، 02.jpg، وهيج.

### 8.6 اختيار الدقايق من فيديو جديد (صور من كل دقيقة)

```powershell
mkdir cand -Force
foreach ($m in 3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57) {
  ffmpeg -v error -y -ss ($m*60) -i src\source.mp4 -frames:v 1 -vf scale=320:180 ("cand\m{0:D2}.jpg" -f $m)
}
```

بعدين شوف الصور، واختار الدقايق اللي بيها مطر وأضواء وسياقة حلوة.
تجنّب الدقايق اللي بيها كتابة، أو لوغو، أو انتقال (transition)، أو شاشة سودة.

---

## 9. ملف الأغاني (week1.tsv)

الصيغة: **5 أعمدة مفصولة بـ Tab**، وبدون سطر عناوين:

```
رقم	دقيقة_البداية	الأغنية	الفنان	الحقوق
```

المحتوى الحالي (الدقايق مالت الفيديو القديم، **لازم تتغير للفيديو الجديد**):

| # | البداية | الأغنية | الفنان | الحقوق |
|---|---|---|---|---|
| 01 | 03:00 | I Wanna Be Yours | Arctic Monkeys | © 2013 Domino Recording Co. |
| 02 | 06:00 | Sweater Weather | The Neighbourhood | © 2013 Columbia Records |
| 03 | 09:00 | Summertime Sadness | Lana Del Rey | © 2012 Polydor / Interscope |
| 04 | 12:00 | The Night We Met | Lord Huron | © 2015 IAMSOUND / Republic Records |
| 05 | 15:00 | Glimpse of Us | Joji | © 2022 88rising Music |
| 06 | 18:00 | Here With Me | d4vd | © 2022 Darkroom / Interscope |
| 07 | 20:30 | Wicked Game | Chris Isaak | © 1989 Reprise Records |
| 08 | 26:00 | No Surprises | Radiohead | © 1997 XL Recordings |
| 09 | 29:00 | Fade Into You | Mazzy Star | © 1993 Capitol Records |
| 10 | 32:00 | Call Out My Name | The Weeknd | © 2018 XO / Republic Records |
| 11 | 35:00 | Somebody Else | The 1975 | © 2016 Dirty Hit |
| 12 | 38:00 | Sweet | Cigarettes After Sex | © 2017 Partisan Records |
| 13 | 41:00 | Slow Dancing in the Dark | Joji | © 2018 88rising Music |
| 14 | 44:00 | Young and Beautiful | Lana Del Rey | © 2013 Interscope Records |

وكان أكو ريل إضافي قبل الأسبوع الأول:
- **Apocalypse** — Cigarettes After Sex — © 2017 Partisan Records — من الدقيقة 23:00.

**عدد الفيديوهات:**
- الأسبوع الأول: **14 ريل** (ريلين باليوم × 7 أيام)
- زائد ريل **Apocalypse** الأول = **15 ريل** بالمجموع
- كل ريل: **60 ثانية**، والفيديو الجديد طوله ساعة، فيكفي لحوالي **50 ريل** إذا ما كررنا دقيقة.
- خلّي فرق **3 دقايق على الأقل** بين كل ريل والثاني، حتى ما تتشابه اللقطات.

---

## 10. جدول النشر

**الأوقات (بتوقيت بغداد):**
- الريل الأول باليوم: **9:00 بالليل**
- الريل الثاني: **1:00 بعد نص الليل**

**طريقة الرفع بتطبيق يوتيوب:**
1. Upload ← اختار الفيديو
2. **Add sound** ← ابحث عن الأغنية ← اختار مقطع الكورس
3. اكتب العنوان والوصف والتاغات
4. Visibility ← **Schedule** ← اختار الوقت

| اليوم | # | العنوان |
|---|---|---|
| 1 | 01 | i wanna be yours 🌙 \| 3am night drive |
| 1 | 02 | sweater weather on a rainy night 🌧️ |
| 2 | 03 | summertime sadness hits different at 3am 🌙 |
| 2 | 04 | the night we met 🌧️ \| for the one you still miss |
| 3 | 05 | glimpse of us 🌙 \| pov: you still see them in everyone |
| 3 | 06 | here with me 🌧️ \| late night drive |
| 4 | 07 | wicked game 🌙 \| rain, road, and one song |
| 4 | 08 | no surprises 🌧️ \| a quiet night drive |
| 5 | 09 | fade into you 🌙 \| 3am thoughts |
| 5 | 10 | call out my name 🌧️ \| night drive |
| 6 | 11 | somebody else 🌙 \| pov: they moved on |
| 6 | 12 | sweet 🌧️ \| cigarettes after sex night drive |
| 7 | 13 | slow dancing in the dark 🌙 \| 3am drive |
| 7 | 14 | young and beautiful 🌧️ \| will you still love me |

**الـ call to action ويا العنوان** (طلبه المستخدم بهاي المحادثة):
- ضيف بآخر العنوان: `| subscribe for more 3am edits` أو `subscribe if this hits at 3am 🌙`
- خيارات ثانية: `| save this for your 3am drive`، `| tag someone you miss 🌙`
- **العنوان كله لازم يبقى أقل من 100 حرف.**

أمثلة جاهزة:
- `sweater weather on a rainy night 🌧️ subscribe if this hits at 3am 🌙`
- `summertime sadness hits different at 3am 🌙 | subscribe for more 3am edits`

---

## 11. قالب الوصف

```
it's 3am and this song is playing in your head. 🌙

🎵 [SONG] — [ARTIST]
[CREDIT]. all rights belong to the artist and label.

subscribe for more late night edits → @the3amthoughtsx

#3amthoughts #nightdrive #sadsongs #shorts
```

بدّل `[SONG]` و `[ARTIST]` و `[CREDIT]` من جدول القسم 9.

---

## 12. التاغات

**تاغات ثابتة (لكل ريل):**

```
night drive, rainy night drive, sad songs, aesthetic edit, late night vibes, 3am thoughts, slowed reverb, car edit, night drive music, shorts
```

**تاغات الأغنية (تنحط قبل الثابتة):**

| # | التاغات |
|---|---|
| 01 | i wanna be yours, arctic monkeys, i wanna be yours slowed |
| 02 | sweater weather, the neighbourhood, sweater weather slowed |
| 03 | summertime sadness, lana del rey, lana del rey edit |
| 04 | the night we met, lord huron, the night we met slowed |
| 05 | glimpse of us, joji, joji sad songs |
| 06 | here with me, d4vd, d4vd here with me |
| 07 | wicked game, chris isaak, wicked game slowed |
| 08 | no surprises, radiohead, radiohead edit |
| 09 | fade into you, mazzy star, mazzy star fade into you |
| 10 | call out my name, the weeknd, the weeknd sad songs |
| 11 | somebody else, the 1975, the 1975 somebody else |
| 12 | sweet, cigarettes after sex, cigarettes after sex sweet |
| 13 | slow dancing in the dark, joji, joji slowed |
| 14 | young and beautiful, lana del rey, young and beautiful slowed |

**التعليق المثبّت (لكل ريل):**

```
who are you thinking about right now? 🌙
```

---

## 13. وين وقفنا

- آخر شي سلّمته للمستخدم: الكابشن والوصف والتاغات للفيديو **03 (Summertime Sadness)**.
- الي بعده: الفيديو **04 (The Night We Met)**.
- بس هسه الفيديوهات القديمة ضاعت، فالأولوية إننا **نعيد سوايتها** من الفيديو الجديد.

---

## 14. الخطوات للجلسة الجديدة (بالترتيب)

1. **شوف الفولدر:** شنو بيه بسطح المكتب (`night though`؟)، ووين الفيديو اللي نزّله المستخدم، وشنو اسمه.
2. **تأكد من البرامج:** Python و Pillow و ffmpeg (القسم 5). إذا ناقص شي، نصّبه.
3. **نزّل الملفات من GitHub** (القسم 2) وحطها بفولدر الشغل.
4. **رتّب الفولدر** (القسم 6): الفيديو يصير `src\source.mp4`.
5. **سوّي صورة بروفايل جديدة** وحطها بـ `..\3am-thoughts\pfp_B_window.png`.
   أو اسأل المستخدم إذا عنده الصورة على الموبايل أو بقناة يوتيوب. تكدر تنزّلها من صفحة القناة.
6. **اختار دقايق جديدة** من الفيديو الجديد (القسم 8.6) وعدّل `week1.tsv`.
7. **سوّي معاينة** بـ `--still 20` (القسم 8.2) وراويها للمستخدم.
8. **إذا وافق، رندر الكل:** `python batch.py week1.tsv` (القسم 8.3).
9. **افحص النتيجة:** الطول 60 ثانية (8.4)، وورقة الفحص (8.5).
10. **سلّم الجدول:** العنوان ويا الـ call to action، والوصف، والتاغات، لكل فيديو.
11. **خذ نسخة احتياطية:** انسخ الريلز النهائية لـ OneDrive، حتى ما تضيع مرة ثانية.

---

## 15. ملاحظات عن المستخدم وطريقة الشغل

- يحچي عراقي ويحب الجواب يكون **قصير وواضح**.
- يفضّل **لقطة وحدة متواصلة** على المونتاج المقطّع.
- قبل الحقوق: الفيديوهات تطلع **بدون صوت**، وهو يضيف الأغنية من مكتبة يوتيوب.
- ما يحب نصرف **كردت** بدون ما نسأله. رفض ننزّل الفيديو بـ Creative Claw (298 كردت).
- يستخدم الموبايل هواية (أندرويد)، فالملفات اللي يحتاجها لازم توصله بطريقة يكدر يفتحها من الموبايل.
- واتساب وتلجرام **مو مربوطة**، فما نكدر ندز عليهم.
- علامة التوثيق بالريل **مجرد تصميم**. لا تگول إنها توثيق رسمي، وذكّره إن يوتيوب ممكن ما يحبها إذا القناة مو موثقة.

---

## 16. مشاكل ممكن تصير وحلّها

| المشكلة | الحل |
|---|---|
| `ffmpeg is not recognized` | نصّب ffmpeg وسكّر الـ terminal وافتحه من جديد |
| `cannot open resource` (خط) | الخطوط بمسار `C:/Windows/Fonts/`. على ماك أو لينكس غيّر المسار بـ `build.py` |
| `FileNotFoundError: pfp_B_window.png` | صورة البروفايل مو بمكانها (القسم 6) |
| `FileNotFoundError: source.mp4` | الفيديو مو بـ `src\source.mp4` |
| الريل أقصر من 60 ثانية | دقيقة البداية قريبة من آخر الفيديو. البداية لازم تكون قبل النهاية بدقيقة على الأقل |
| الرندر بطيء | قلّل التوازي بـ `batch.py`: غيّر `ThreadPoolExecutor(3)` لـ 2 |
| الكرت مغطى بيوتيوب | لا تنزّل أي عنصر تحت y ≈ 1530 |
| اسم أغنية طويل يطلع برة الكرت | السكربت يصغّره لحد 32. إذا بعده طويل، اختصر الاسم |

---

*آخر تحديث: 5 نوفمبر 2026*
