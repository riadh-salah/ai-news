#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 18-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "18-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google NotebookLM 3 Arabic · Anthropic Claude for Work 2 Arabic · "
    "HubSpot Breeze Intelligence 2 Arabic · Runway Gen-4 Turbo Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google NotebookLM 3 Arabic، Anthropic Claude for Work 2 Arabic، HubSpot Breeze Intelligence 2 Arabic، Runway Gen-4 Turbo Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 18 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Google NotebookLM 3 Arabic الذي يُحوّل تقاريرك الطويلة إلى بودكاست عربي تستمع له أثناء تنقلك، إلى Anthropic Claude for Work 2 Arabic الذي يُنسّق مشاريع الفريق ويُحلّل العقود بالفصحى مع استشهادات، ومن HubSpot Breeze Intelligence 2 Arabic الذي يُكتشف العملاء المحتملين ويُصيغ رسائل بيع بلهجة مناسبة لكل سوق، إلى Runway Gen-4 Turbo Arabic الذي يُنتج إعلانات فيديو احترافية بنص عربي متحرك خلال دقائق — أربع قصص صباحية في 18 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ مع أول قهوة!</h1>
      <p class="hero-sub">صباحُ رواد الأعمال والمبدعين والمسوقين: المعرفة تُسمع لا تُقرأ فقط، الفريق يفكر بلغة واحدة، المبيعات تتحرك ذاتيًا، والفيديو لا ينتظر استوديو. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 18 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google NotebookLM 3 Arabic: من ملفات مُبعثرة إلى بودكاست وملخصات — تعلّم وبيع بالعربية</h2>
      <p class="article-lead">«لديّ مئات الصفحات عن استراتيجية السوق ولا وقت لقراءتها قبل الاجتماع». في 18 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>NotebookLM 3 Arabic</strong>: مساعد بحث يقرأ PDF وعروض Google Slides ومقاطع YouTube، يُولّد ملخصات تنفيذية بالفصحى، يُنشئ «نظرة صوتية» بودكاست ثنائية بالعربية الطبيعية، يُجيب عن أسئلة مع اقتباس من المصدر، يدعم لهجات الخليج والمصرية في الشرح، ويشارك دفاتر ملاحظات آمنة مع الفريق — للمدربين والمحامين والاستشاريين في العالم العربي.</p>
      <p>المشكلة التي حلّتها: الإصدار السابق كان يُحوّل العربية إلى صوت روبوتي أو يُهمل اتجاه النص في المخططات؛ NotebookLM 3 يدعم فهرسة مستندات ثنائية اللغة، تلخيصًا مقارنًا بين نسختين من العقد، قوالب «دورة تدريبية» و«ملخص جلسة محكمة» و«تحضير مكالمة مبيعات»، تصدير ملفات صوتية MP3 للبيع، تكامل Google Drive وGmail، وبرنامج شريك «NotebookLM Creators MENA».</p>
      <p>القدرات الأساسية: بودكاست عربي من المستندات؛ أسئلة وأجوبة مع مصدر؛ ملخصات تنفيذية؛ تعاون فريق؛ تصدير صوتي.</p>
      <p>للمبدعين العرب: منتج «حزمة معرفة صوتية أسبوعية» — من يُسلّم 12 بودكاستًا مخصصًا شهريًا بـ220–1200 دولار للعميل يبيع وقت التعلم لرجال أعمال لا يقرؤون لكنهم يستمعون بفارغ الصباح.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google NotebookLM 3 Arabic؟</h3>
        <ul>
          <li><strong>تحويل مكتبة عميل إلى بودكاست وملخصات شهرية:</strong> — 220–1200 دولار/شهر.</li>
          <li><strong>إعداد دفتر NotebookLM ومصادر منظمة:</strong> 4–9 أيام — 750–3800 دولار.</li>
          <li><strong>قوالب قطاعية (قانون، تعليم، عقار):</strong> — 45–210 دولار/حزمة.</li>
          <li><strong>ورش «بيع المعرفة الصوتية بالعربية»:</strong> — 55–220 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">NotebookLM</span>
        <span class="tag">Audio</span>
        <span class="tag">Research</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Anthropic Claude for Work 2 Arabic: مشاريع الفريق، تحليل وثائق، وحوكمة بيانات</h2>
      <p class="article-lead">«نحتاج مساعدًا يفهم عقودنا العربية ولا يُسرّبها خارج الشركة». في 18 نوفمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude for Work 2 Arabic</strong>: بيئة عمل للفرق تجمع محادثات مشتركة، مشاريع بملفات مرفقة، تحليل جداول وعقود PDF بالفصحى مع اقتباسات فقرة، سياسات احتفاظ وصلاحيات حسب الدور، تكامل Slack وMicrosoft 365 وNotion، ووضع «امتثال مالي» يرفض نصائح استثمارية غير مصرح بها — للبنوك وشركات التأمين والاستشارات في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يخلط بين مشاريع أو يُخطئ في الأرقام العربية الهندية؛ for Work 2 يدعم ذاكرة مشروع معزولة، مقارنة نسخ العقد، قوالب «مراجعة سياسة» و«تحليل مخاطر» و«صياغة رد تنظيمي»، تدقيقًا لغويًا رسميًا، تصدير تقارير Word بالاتجاه الصحيح، وبرنامج «Claude Enterprise Partners Gulf».</p>
      <p>القدرات الأساسية: مشاريع فريق؛ تحليل وثائق عربية؛ اقتباسات دقيقة؛ صلاحيات وحوكمة؛ تكامل أدوات العمل.</p>
      <p>للمبدعين العرب: باقة «مكتب Claude مؤسسي في 12 يومًا» — من ينفذ 5 إعدادات شهريًا بـ3200–18500 دولار للمشروع + 680–2900 دولار/شهر للإدارة يبيع ذكاءً آمنًا لشركات تُمنع من استخدام أدوات استهلاكية عادية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude for Work 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Claude for Work ومشاريع وصلاحيات:</strong> 8–16 يومًا — 3200–18500 دولار.</li>
          <li><strong>إدارة سياسات وقوالب تحليل شهريًا:</strong> — 680–2900 دولار/عميل/شهر.</li>
          <li><strong>قوالب قطاع منظّم (مالي، طبي، حكومي):</strong> — 72–310 دولار/مجموعة.</li>
          <li><strong>دورة «فرق العمل الآمنة مع Claude بالعربية»:</strong> — 60–240 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Documents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>HubSpot Breeze Intelligence 2 Arabic: اكتشاف عملاء، رسائل بيع، وتنبؤات إيراد</h2>
      <p class="article-lead">«فريق المبيعات يكتب رسائل cold بالإنجليزية والعميل الخليجي لا يرد». في 18 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze Intelligence 2 Arabic</strong>: طبقة ذكاء فوق CRM تُحلّل سجل التصفح والبريد، تُقترح عملاء محتملين بدرجات ملاءمة، تُولّد رسائل مبيعات بالفصحى أو لهجة الخليج حسب القطاع، تُلخّص مكالمات المبيعات، تُتنبأ بإغلاق الصفقة، وتتزامن مع WhatsApp Business وLinkedIn — لوكالات التسويق وشركات SaaS والعقارات في العالم العربي.</p>
      <p>المشكلة التي حلّتها: Breeze الأول كان يُكرر عبارات بيعية عامة أو يخلط بين عملاء من أسواق مختلفة؛ الإصدار 2 يدعم قواعد نبرة حسب الدولة، تخصيصًا جماعيًا لحملات، تكامل بيانات إعلانات ميتا، قوالب «عقار فاخر» و«برنامج تدريب شركات» و«اشتراك برمجي»، تنبيهات عندما يبرد العميل، وبرنامج «HubSpot Breeze MENA Agency».</p>
      <p>القدرات الأساسية: تسجيل عملاء ذكي؛ رسائل عربية مخصصة؛ تلخيص مكالمات؛ تنبؤات صفقات؛ تكامل قنوات.</p>
      <p>للمبدعين العرب: خدمة «خط أنابيب مبيعات ذكي» — من يُدير 10 عملاء HubSpot بـ550–2600 دولار/شهر لكل عميل يحوّل أداة CRM إلى آلة إيراد دون توظيف محللي بيانات بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze Intelligence 2 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل Breeze وقواعد نبرة عربية على HubSpot:</strong> 5–12 يومًا — 1400–7200 دولار.</li>
          <li><strong>إدارة خط أنابيب ورسائل وحملات شهريًا:</strong> — 550–2600 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب قطاع (عقار، تعليم، SaaS):</strong> — 58–265 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات عربية مدعومة بالذكاء الاصطناعي»:</strong> — 58–235 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Breeze</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Runway Gen-4 Turbo Arabic: إعلانات فيديو سريعة — نص عربي، حركة كاميرا، وعلامة تجارية</h2>
      <p class="article-lead">«العميل يريد ثلاث نسخ إعلانية بالعربية قبل نهاية الأسبوع ولا ميزانية لطاقم تصوير». في 18 نوفمبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Turbo Arabic</strong>: مولّد فيديو يفهم أوامر بالفصحى واللهجة، يُنتج مشاهد 5–15 ثانية بحركة كاميرا سينمائية، يُدرج نصًا عربيًا متحركًا قابلًا للقراءة، يحافظ على هوية الشخصية بين اللقطات، يدعم صور منتج كمرجع، ويُصدّر بصيغ إعلانات Reels وTikTok وYouTube Shorts — لوكالات المحتوى والتجارة الإلكترونية والمؤثرين في المنطقة.</p>
      <p>المشكلة التي حلّتها: Gen-3 كان يُشوّه الحروف العربية أو يُنتج حركة بطيئة؛ Turbo Arabic يدعم خطوط عربية واضحة في الفيديو، توليدًا متوازيًا لعشرات المقاطع، قوالب «إطلاق منتج» و«عرض خصم رمضان» و«شهادة عميل»، تحريرًا سريعًا داخل المشروع، مكتبة موسيقى مرخصة، وبرنامج «Runway Creator Studio Arabia».</p>
      <p>القدرات الأساسية: فيديو من نص عربي؛ نص متحرك مقروء؛ اتساق شخصيات؛ سرعة إنتاج؛ صيغ منصات قصيرة.</p>
      <p>للمبدعين العرب: استوديو «إعلانات أسبوعية جاهزة» — من يُسلّم 20 مقطعًا شهريًا بـ85–420 دولار للمقطع أو 1800–7500 دولار باقة شهرية يخدم متاجرًا تستهلك مئات الإعلانات دون استوديو تقليدي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Turbo Arabic؟</h3>
        <ul>
          <li><strong>باقة إعلانات فيديو عربية شهرية (8–25 مقطعًا):</strong> — 1800–7500 دولار/شهر.</li>
          <li><strong>مقطع إعلاني مخصص بعلامة العميل:</strong> — 85–420 دولار/مقطع.</li>
          <li><strong>إعداد قوالب Runway وهوية بصرية:</strong> 3–8 أيام — 950–4800 دولار.</li>
          <li><strong>دورة «منتج فيديو إعلاني بالذكاء الاصطناعي بالعربية»:</strong> — 52–210 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video AI</span>
        <span class="tag">Ads</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 18-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="18-11-2026 -- 08-AM.html">
          📰 18 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "18-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/18-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/18-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
        f"(4 أخبار + أفكار ربح من AI)"
    )
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "أحدث إصدار" in line and "news/" in line:
            if new in line:
                print(f"README already points to latest: {README}")
                return
            lines[i] = new_line
            break
    else:
        raise SystemExit("ERROR: could not find README latest edition line")
    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Written: {README}")


def validate_output():
    data = OUTPUT.read_bytes()
    if b"\x00" in data:
        raise SystemExit("ERROR: null bytes found in output")
    if data[:3] == b"\xef\xbb\xbf":
        raise SystemExit("ERROR: BOM found in output")
    text = OUTPUT.read_text(encoding="utf-8")
    if "article-4" not in text:
        raise SystemExit("ERROR: missing article-4")
    if text.count('class="article"') != 4:
        raise SystemExit(f"ERROR: expected 4 articles, found {text.count('class=\"article\"')}")
    if not text.startswith("<!DOCTYPE html>"):
        raise SystemExit("ERROR: invalid HTML start")
    if not text.rstrip().endswith("</html>"):
        raise SystemExit("ERROR: invalid HTML end")
    bad_patterns = [
        "dollar",
        "mlions",
        "millones",
        "bringing",
        "الLlatin",
        "أfكar",
        "دolار",
        "البروtokol",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "المشkلة",
        "mezclar",
        "prefe r",
        "الإصrador",
        "يبni",
        "عArabية",
        "أكtober",
        "ت TECH",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    if re.search(r"[yY][\u064B-\u0652\u0670]", text):
        raise SystemExit("ERROR: Latin y with Arabic diacritic found")
    if "\u00fc" in text or "yü" in text:
        raise SystemExit("ERROR: Latin ü found — use Arabic يُ")
    print("Validation passed: UTF-8, no null bytes, 4 articles, valid HTML structure")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    validate_output()
    update_index()
    update_readme()


if __name__ == "__main__":
    main()