#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 15-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "15-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI Operator 2 Arabic · Google NotebookLM 3 Arabic · "
    "Replit Agent 3 Arabic · Descript Underlord 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI Operator 2 Arabic، Google NotebookLM 3 Arabic، Replit Agent 3 Arabic، Descript Underlord 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 15 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من OpenAI Operator 2 Arabic الذي يُنفّذ مهام المتصفح نيابةً عنك — حجز، شراء، ومتابعة فواتير بالعربية، إلى Google NotebookLM 3 Arabic الذي يُحوّل مكتبتك من PDF إلى بودكاست تعليمي وملخص امتحان، ومن Replit Agent 3 Arabic الذي يُبني تطبيقًا كاملًا من وصف عربي في ساعات، إلى Descript Underlord 2 Arabic الذي يُحرّر فيديوهاتك بالأوامر الصوتية ويُزيل الصمت ويُضيف ترجمة عربية — أربع قصص صباحية في 15 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ لرواد الأعمال والمدرّسين وصناع المحتوى: المتصفح أصبح موظفًا، المذاكرة أصبحت صوتًا، البرمجة أصبحت محادثة، والمونتاج أصبح أمرًا واحدًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 15 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI Operator 2 Arabic: وكيل متصفح يُنجز مهامك — حجوزات، تجارة، ومتابعة!</h2>
      <p class="article-lead">«أحتاج حجز تذاكر وفتح تذكرة دعم ومتابعة شحنة من ثلاثة مواقع — والساعة 8 صباحًا واجتماع خلال نصف ساعة». في 15 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>Operator 2 Arabic</strong>: وكيل يتحكم في متصفح آمن، يقرأ واجهات بالعربية، يُكمل نماذج الحجز، يُرسل تأكيدات بالفصحى، يتوقف عند الدفع لموافقتك، يُسجّل كل خطوة للمراجعة، يتكامل مع ChatGPT وEnterprise للفرق — للمسافرين والتجار وفرق المشتريات في الشرق الأوسط.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يتعثر مع المواقع العربية RTL أو يُعيد المحاولة بلا نهاية؛ الإصدار 2 يُحسّن التعرف على الحقول العربية، يُدعم مصادقة ثنائية بالتنبيه، يُشغّل قوالب مهام (تجديد اشتراك، مقارنة أسعار)، يُحترم حدود الاستخدام المؤسسي، يُوفّر وضع «مشتريات B2B» مع اعتماد المدير، وبرنامج شريك «Operator Workflows MENA».</p>
      <p>القدرات الأساسية: Arabic task recipes؛ جدولة مهام صباحية؛ تكامل Slack للتنبيهات؛ سجل تدقيق قانوني؛ حزم امتثال للقطاع المالي.</p>
      <p>للمبدعين العرب: خدمة «مساعد مشتريات وإدارة رقمية» — من يُدير 30 عميلًا باشتراك 120–480 دولار/شهر + إعداد مهام 400–2400 دولار يبيع وقتًا تنفيذيًا بلا توظيف إداري بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI Operator 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم مهام متكررة (حجوزات، فواتير، متابعة):</strong> 3–8 أيام — 400–2400 دولار/عميل.</li>
          <li><strong>اشتراك تشغيل أسبوعي للمهام:</strong> — 120–480 دولار/شهر.</li>
          <li><strong>حزم قطاعية (سياحة، تعليم، عقارات):</strong> — 65–280 دولار/حزمة.</li>
          <li><strong>دورات «أتمتة مهام المتصفح بالعربية»:</strong> — 55–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Operator</span>
        <span class="tag">Browser Agent</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Google NotebookLM 3 Arabic: مصادرك تصبح بودكاست وامتحان — تعليم، امتثال، ومبيعات!</h2>
      <p class="article-lead">«فريق المبيعات لا يقرأ دليل المنتج الطويل — ويخسرون الحجج أمام المنافس». في 15 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>NotebookLM 3 Arabic</strong>: منصة تُرفع عليها مستندات PDF وعروضًا وروابط، تُولّد ملخصات بالفصحى، تُنتج بودكاستًا تعليميًا بصوت عربي طبيعي، تُنشئ أسئلة اختبار تفاعلية، تُربط بـGoogle Drive وWorkspace، تُحترم صلاحيات المؤسسة — للجامعات ومراكز التدريب وفرق تمكين المبيعات.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان محدودًا في اللهجات والمصادر المختلطة؛ الإصدار 3 يُحسّن الاستشهاد بالصفحة، يُدعم فيديو YouTube كمصدر، يُصدّر بطاقات مراجعة، يُشغّل «استوديو صوت عربي» بأصوات متعددة، يُتزامن مع Classroom، وAPI للوكالات التي تبيع محتوى تدريبًا سريعًا.</p>
      <p>القدرات الأساسية: Arabic audio overviews؛ قوالب امتثال وتشريعات؛ مشاركة آمنة للفرق؛ تحليلات استماع؛ شهادة شريك «NotebookLM Edu MENA».</p>
      <p>للمبدعين العرب: منتج «دليل منتجك كبودكاست عربي في 48 ساعة». من يبيع 15 شركة بـ900–5500 دولار/مشروع + تحديثات 200–950 دولار/شهر يحوّل المعرفة الراكدة إلى أصول صوتية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google NotebookLM 3 Arabic؟</h3>
        <ul>
          <li><strong>تحويل مكتبة عميل إلى بودكاست واختبارات:</strong> 2–5 أيام — 900–5500 دولار/مشروع.</li>
          <li><strong>تحديث مصادر وإصدارات صوتية شهرية:</strong> — 200–950 دولار/شهر.</li>
          <li><strong>حزم قطاعية (صيدلة، قانون، تقنية):</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>دورات «تعلم صوتي بالعربية مع NotebookLM»:</strong> — 42–185 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">NotebookLM</span>
        <span class="tag">Podcast</span>
        <span class="tag">Learning</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Replit Agent 3 Arabic: من فكرة عربية إلى تطبيق منشور — واجهة، قاعدة بيانات، ودفع!</h2>
      <p class="article-lead">«لدي فكرة تطبيق توصيل محلي بالعربية — وليس لدي فريق تقني بمليون دولار». في 15 نوفمبر 2026، أطلق <strong>Replit</strong> <strong>Agent 3 Arabic</strong>: وكيل برمجة يفهم المتطلبات بالفصحى، يُنشئ واجهة RTL، يُربط Postgres وStripe وخرائط، يُنشر على نطاق فوري، يُصلح الأخطاء تلقائيًا، يُولّد اختبارات، يُحترم قوالب أمان — للمؤسسين المنفردين والوكالات وطلاب التكنولوجيا.</p>
      <p>المشكلة التي حلّتها: Agent 2 كان يتوقف عند التكاملات المعقدة؛ الإصدار 3 يُدعم تطبيقات متعددة المستأجرين، مصادقة عربية عبر OTP، لوحات إدارة بالعربية، تكامل WhatsApp Business API، مراجعة كود بشرية اختيارية، وبرنامج «Replit Agency MENA» للوكالات التي تبيع MVP سريعًا.</p>
      <p>القدرات الأساسية: Arabic product specs؛ قوالب SaaS ومتاجر؛ نشر سحابي؛ مراقبة أداء؛ شراكات دفع محلية عبر موصلات.</p>
      <p>للمبدعين العرب: استوديو «من BRD عربي إلى تطبيق حي في 10 أيام». من يُسلّم 8 مشاريع سنويًا بـ3500–28000 دولار + صيانة 350–2200 دولار/شهر يبيع سرعة دخول السوق دون توظيف فريق كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Agent 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء MVP (مواصفات، تطوير، نشر، تسليم):</strong> 7–14 يومًا — 3500–28000 دولار/مشروع.</li>
          <li><strong>صيانة وتطوير ميزات شهريًا:</strong> — 350–2200 دولار/شهر.</li>
          <li><strong>حزم قوالب (حجز، دليل، اشتراكات):</strong> — 75–320 دولار/حزمة.</li>
          <li><strong>دورات «ابنِ منتجك بالعربية مع Replit Agent»:</strong> — 58–240 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Agent</span>
        <span class="tag">No-Code</span>
        <span class="tag">Startup</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Descript Underlord 2 Arabic: مونتاج بالأمر الصوتي — بودكاست، ريلز، وترجمة!</h2>
      <p class="article-lead">«ساعة تسجيل بودكاست عربي — وأريد إزالة التكرار وإضافة موسيقى وترجمة إنجليزية قبل الظهر». في 15 نوفمبر 2026، أطلقت <strong>Descript</strong> <strong>Underlord 2 Arabic</strong>: مساعد تحرير يفهم الأوامر بالفصحى، يُنظّف الصوت، يُقطع الفواصل، يُولّد B-roll من الوصف، يُضيف ترجمة عربية وإنجليزية متزامنة، يُصدّر لـYouTube وSpotify وTikTok — للبودكاسترز والمدرّسين والوكالات الإبداعية.</p>
      <p>المشكلة التي حلّتها: Underlord 1 كان يُسيء فهم المصطلحات العربية في الأوامر؛ الإصدار 2 يُحسّن تفريغ الكلام العربي، يُطبّق قوالب «حلقة بودكاست» و«درس تعليمي»، يُزامن مع قوالب العلامة، يُدعم فرق المراجعة، تكامل Riverside وZoom، وAPI لمن يبيع إنتاجًا بالجملة.</p>
      <p>القدرات الأساسية: Arabic voice commands؛ Studio Sound للعربية؛ ترجمة ثنائية اللغة؛ قوالب ريلز؛ شريك «Descript Creator MENA».</p>
      <p>للمبدعين العرب: باقة «تحرير أسبوعي لقناة عربية». من يدير 20 قناة بـ180–1200 دولار/شهر + إعداد 280–1900 دولار يحوّل التحرير من عنق الزجاجة إلى خط إنتاج.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Descript Underlord 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد قناة (قوالب، علامة، سير عمل):</strong> 2–6 أيام — 280–1900 دولار/عميل.</li>
          <li><strong>تحرير وإخراج حلقات شهرية:</strong> — 180–1200 دولار/شهر.</li>
          <li><strong>حزم موسمية (رمضان، توجيهي، مؤتمرات):</strong> — 45–195 دولار/حزمة.</li>
          <li><strong>دورات «مونتاج صوتي بالعربية مع Underlord»:</strong> — 38–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Descript</span>
        <span class="tag">Underlord</span>
        <span class="tag">Video</span>
        <span class="tag">Podcast</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 15-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="15-11-2026 -- 08-AM.html">
          📰 15 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "15-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/15-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/15-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
    print(f"Updated: {README}")


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