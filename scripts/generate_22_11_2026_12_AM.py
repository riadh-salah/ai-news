#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 22-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "22-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Mailchimp Intuit Assist 3 Arabic · Hootsuite OwlyWriter AI 4 Arabic · "
    "Gong Engage AI 3 Arabic · QuickBooks AI Advisor 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Mailchimp Intuit Assist 3 Arabic، Hootsuite OwlyWriter AI 4 Arabic، Gong Engage AI 3 Arabic، QuickBooks AI Advisor 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 22 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Mailchimp Intuit Assist 3 Arabic الذي يُصمّم سلاسل بريد عربية تُفتح وتُحوّل قبل أن يستيقظ فريقك، إلى Hootsuite OwlyWriter AI 4 Arabic الذي يُخطّط شهرًا كاملًا من المنشورات بلهجة علامتك على كل منصة، ومن Gong Engage AI 3 Arabic الذي يُكتب متابعات المبيعات ويُحلّل المكالمات ويقترح الخطوة التالية بلسان مدير المبيعات، إلى QuickBooks AI Advisor 3 Arabic الذي يُفسّر التدفق النقدي ويُنبّهك على المصروفات الغريبة قبل إقفال الشهر — أربع قصص ليلية في 22 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يبدأ قبل شروق الشمس!</h1>
      <p class="hero-sub">ليلةٌ للتسويق والمبيعات والمحاسبة: البريد يبيع، السوشيال يُجدول نفسه، الصفقات تتحرك، والأرقام تُشرح بلغة بشرية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 22 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Mailchimp Intuit Assist 3 Arabic: بريدك يبيع ليلًا — سلاسل، تجزئة، وعناوين تجذب بالعربية!</h2>
      <p class="article-lead">«قائمتنا البريدية 80 ألف مشترك، لكن الفتح منخفض والنصوص تبدو مترجمة آلية — وأنا أكتب الحملات وحدي حتى منتصف الليل». في 22 نوفمبر 2026، أطلقت <strong>Mailchimp</strong> <strong>Intuit Assist 3 Arabic</strong>: مساعد ذكاء داخل Mailchimp يفهم جمهورك بالفصحى واللهجات التجارية، يُقترح عناوين بريد تزيد النقر، يُصمّم سلاسل ترحيب وتخليص سلة وإعادة شراء، يُجزّئ المشتركين حسب السلوك، يُكتب نصوصًا RTL متناسقة مع الهوية، يُحسّن وقت الإرسال حسب المنطقة الزمنية، يُولّد تقارير أسبوعية بالعربية، ويتكامل مع Shopify وSalla وواتساب — للمتاجر الإلكترونية والدورات الرقمية والمطاعم والوكالات في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Assist 2 كان يُطيل الرسائل أو يُهمل التشكيل في العناوين؛ الإصدار 3 يُثبت قاموسًا للعلامة، يدعم وضع «رمضان» و«بلاك فرايداي»، يختبر عناوين متعددة تلقائيًا، يربط Google Analytics ومحركات التجارة، يُنبّه عند انخفاض التسليم، ويُقدّم برنامج «Mailchimp AI Partners MENA» للمطبّقين المعتمدين.</p>
      <p>القدرات الأساسية: سلاسل بريد عربية؛ تجزئة ذكية؛ عناوين محسّنة؛ تقارير تفسيرية؛ تكامل متاجر.</p>
      <p>للمبدعين العرب: وكالة «بريد يُغلق صفقة» — من يُدير حملات لسبع علامات بـ420–1950 دولار/شهر للعلامة يحوّل قوائم خاملة إلى إيراد متكرر دون فريق كتابة داخلي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Mailchimp Intuit Assist 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد حساب و3 سلاسل بريد عربية:</strong> 5–12 يومًا — 1100–6800 دولار/علامة.</li>
          <li><strong>إدارة حملات وتحسين أسبوعي:</strong> — 420–1950 دولار/عميل/شهر.</li>
          <li><strong>حزمة 25 قالب بريد قطاعي (جمال، تقنية، تعليم):</strong> — 95–380 دولار/حزمة.</li>
          <li><strong>ورش «تسويق بريدي ذكي بالعربية مع Mailchimp»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Mailchimp</span>
        <span class="tag">Email</span>
        <span class="tag">Marketing</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Hootsuite OwlyWriter AI 4 Arabic: شهر سوشيال كامل من فكرة واحدة — خطافات، جدولة، ولهجة علامة!</h2>
      <p class="article-lead">«أدير 12 حسابًا لعملاء مختلفين — وكل ليلة أكتب منشورات من الصفر لأربع منصات». في 22 نوفمبر 2026، أطلقت <strong>Hootsuite</strong> <strong>OwlyWriter AI 4 Arabic</strong>: كاتب ذكاء داخل لوحة Hootsuite يفهم موجز الحملة بالعربية، يُولّد منشورات Instagram وLinkedIn وX وTikTok بنبرة مختلفة لكل منصة، يُقترح هاشتاقات محلية، يُلخّص مقالات طويلة إلى threads، يُجدول التقويم الشامل، يُحلّل أفضل أوقات النشر في MENA، يُعيد كتابة المنشور الفاشل تلقائيًا، ويُصدّر تقرير أداء بالعربية — لوكالات السوشيال ومؤثري المحتوى وفرق التسويب في الشركات المتوسطة.</p>
      <p>المشكلة التي حلّتها: OwlyWriter 3 كان يُنتج نصوصًا متشابهة بين المنصات؛ الإصدار 4 يحفظ «بطاقة صوت» لكل عميل، يدعم قوالب «إطلاق منتج» و«توظيف» و«فعالية»، يربط Canva للصور، يتحقق من طول النص لكل منصة، يُمكّن موافقة العميل قبل النشر، وبرنامج «Hootsuite Agency Partners Arabia».</p>
      <p>القدرات الأساسية: محتوى متعدد المنصات؛ جدولة ذكية؛ تحليل أداء؛ إعادة صياغة تلقائية؛ قوالب حملات.</p>
      <p>للمبدعين العرب: استوديو «30 يوم محتوى في 48 ساعة» — من يُسلّم تقويمًا كاملاً لعشر علامات بـ850–5200 دولار/شهر لكل علامة يختصر أيام كتابة في جلسة موجزة واحدة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hootsuite OwlyWriter AI 4 Arabic؟</h3>
        <ul>
          <li><strong>تقويم محتوى شهر كامل (4 منصات):</strong> 3–6 أيام — 650–3200 دولار/علامة.</li>
          <li><strong>إدارة نشر وتحسين شهريًا:</strong> — 380–1750 دولار/عميل/شهر.</li>
          <li><strong>حزمة 40 خطاف عربي جاهز (قطاعات متنوعة):</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «سوشيال ذكي بالعربية مع Hootsuite OwlyWriter»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hootsuite</span>
        <span class="tag">Social Media</span>
        <span class="tag">Content</span>
        <span class="tag">Scheduling</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Gong Engage AI 3 Arabic: مبيعات تتبع نفسها — رسائل، مكالمات، وخطوة تالية بالعربية!</h2>
      <p class="article-lead">«مئات الصفقات في CRM — والمناديب ينسون المتابعة أو يكتبون رسائل عامة لا تُجيب». في 22 نوفمبر 2026، أطلقت <strong>Gong</strong> <strong>Engage AI 3 Arabic</strong>: مساعد مبيعات يفهم مكالماتك ورسائلك بالفصحى واللهجات التجارية، يُولّد رسائل متابعة مخصصة لكل عميل، يُلخّص الاجتماعات ويُستخرج الاعتراضات، يُقترح أفضل وقت للاتصال، يُنبّه عند خطر فقدان الصفقة، يُكتب عروضًا قصيرة من ملاحظات المكالمة، ويربط Salesforce وHubSpot وPipedrive — لفرق B2B والعقارات والتقنية والخدمات الاستشارية في المنطقة.</p>
      <p>المشكلة التي حلّتها: Engage 2 كان يُترجم أسماء شركات عربية خطأً؛ الإصدار 3 يدعم قوالب «عرض سعر» و«تجديد عقد» و«تأهيل عميل»، يحلّل نبرة العميل في المكالمة، يُنشئ مهام تلقائية للمدير، يتكامل LinkedIn وOutlook، وبرنامج «Gong Revenue Partners MENA».</p>
      <p>القدرات الأساسية: رسائل متابعة عربية؛ تلخيص مكالمات؛ تنبيهات خطر؛ اقتراح إجراء؛ تكامل CRM.</p>
      <p>للمبدعين العرب: مكتب «إيراد منسّق» — من يُنفّذ Gong لفرق 8–40 مندوبًا بـ2800–16500 دولار للإطلاق + 480–2100 دولار/شهر للتحسين يبيع للشركات التي تخسر صفقات بسبب متابعة ضعيفة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gong Engage AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Gong وتكامل CRM وفريق مبيعات:</strong> 8–18 يومًا — 2800–16500 دولار.</li>
          <li><strong>تحسين رسائل وتحليل مكالمات شهريًا:</strong> — 480–2100 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 قالب متابعة عربية (قطاعات B2B):</strong> — 85–340 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات ذكية بالعربية مع Gong Engage»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gong</span>
        <span class="tag">Sales</span>
        <span class="tag">Engagement</span>
        <span class="tag">CRM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>QuickBooks AI Advisor 3 Arabic: محاسبك الافتراضي يشرح الأرقام — تدفق نقدي، فواتير، وتنبيهات!</h2>
      <p class="article-lead">«أنا صاحب متجر صغير — المحاسب يرسل لي أرقامًا لا أفهمها، ولا أعرف إن كان الشهر رابحًا حتى نهاية الشهر». في 22 نوفمبر 2026، أطلقت <strong>Intuit</strong> <strong>QuickBooks AI Advisor 3 Arabic</strong>: مستشار ذكاء داخل QuickBooks يتحدث بالفصحى البسيطة، يُفسّر قائمة الدخل والتدفق النقدي بجمل قصيرة، يُصنّف المصروفات تلقائيًا، يُنبّه على فواتير متأخرة ومبالغ مكررة، يُقترح ضبط المخزون، يُولّد تقريرًا أسبوعيًا للمالك على واتساب أو بريد، يُحضّر ملخصًا لمحاسب خارجي، ويدعم العملات الخليجية والمصرية — للمطاعم والعيادات والمتاجر وشركات الخدمات الصغيرة.</p>
      <p>المشكلة التي حلّتها: Advisor 2 كان يُخطئ في تصنيف الفواتير العربية الممسوحة ضوئيًا؛ الإصدار 3 يقرأ الفواتير بالعربية بدقة أعلى، يدعم قوالب «مطعم» و«عيادة» و«تجارة إلكترونية»، يربط البنوك المحلية، يُولّد تذكيرات ضريبية موسمية، وبرنامج «QuickBooks ProAdvisor AI MENA».</p>
      <p>القدرات الأساسية: تفسير مالي عربي؛ تصنيف ذكي؛ تنبيهات مصروفات؛ تقارير مجدولة؛ قوالب قطاع.</p>
      <p>للمبدعين العرب: خدمة «مالك يفهم أرقامه» — من يُدير QuickBooks لـ15 عميلًا صغيرًا بـ220–980 دولار/شهر للعميل يبني دخلًا مستقرًا من غرفة عمل مشتركة دون مكتب محاسبة ضخم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من QuickBooks AI Advisor 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد QuickBooks وتدريب المالك (أسبوعان):</strong> 4–10 أيام — 950–5800 دولار.</li>
          <li><strong>مراجعة شهريّة وتقارير Advisor:</strong> — 220–980 دولار/عميل/شهر.</li>
          <li><strong>حزمة سياسات محاسبة عربية (5 قطاعات):</strong> — 65–260 دولار/حزمة.</li>
          <li><strong>ورش «إدارة مالية ذكية بالعربية مع QuickBooks»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">QuickBooks</span>
        <span class="tag">Intuit</span>
        <span class="tag">Accounting</span>
        <span class="tag">SMB</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 22-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="22-11-2026 -- 12-AM.html">
          📰 22 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "22-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/22-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/22-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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