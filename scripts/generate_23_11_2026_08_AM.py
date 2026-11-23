#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "23-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Linear AI 3 Arabic · Buffer AI Assistant 3 Arabic · "
    "New Relic Grok 2 Arabic · Amplitude AI Analyst 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Linear AI 3 Arabic، Buffer AI Assistant 3 Arabic، New Relic Grok 2 Arabic، Amplitude AI Analyst 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Linear AI 3 Arabic الذي يُحوّل فكرة المنتج إلى خارطة مهام وسبرنتات وتحديثات للمدير بلغة الفريق قبل أن تبرد قهوتك، إلى Buffer AI Assistant 3 Arabic الذي يُخطّط تقويمًا للسوشيال ويكتب منشورات بصوت علامتك للخليج ومصر، ومن New Relic Grok 2 Arabic الذي يُفسّر تنبيهات الإنتاج ويُقترح خطوات الإصلاح بلهجة مهندس على-call، إلى Amplitude AI Analyst 3 Arabic الذي يُجيب «لماذا هبط الاحتفاظ؟» من بيانات التطبيق دون جداول معقدة — أربع قصص صباحية في 23 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباح المنتج والمحتوى والمراقبة والتحليل: المهام تُرتَّب، المنشورات تُجهَّز، الحوادث تُفهم، والمقاييس تُروى بالعربية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 23 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Linear AI 3 Arabic: من الفكرة إلى السبرنت — مهام، أولويات، وملخص للمدير بأمر عربي واحد!</h2>
      <p class="article-lead">«الفريق يضيع ساعات في توزيع المهام وكتابة التحديثات — والإصدار يتأخر كل أسبوع». في 23 نوفمبر 2026، أطلقت <strong>Linear</strong> <strong>Linear AI 3 Arabic</strong>: طبقة ذكاء داخل Linear تفهم وصف الميزة بالفصحى والعامية المكتبية، تُقسّم العمل إلى مهام وعلاقات تبعية، تُقترح تقديرات زمنية واقعية، تُولّد أوصاف واضحة للمطورين والمصممين، تُنشئ تحديثات أسبوعية للإدارة بالعربية، تُربط GitHub وFigma وSlack، تُصنّف الأخطاء حسب الخطورة، وتُقترح مالكًا لكل تذكرة — لفرق المنتج والتقنية في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يخلط بين المراحل العربية والإنجليزية في لوحة واحدة؛ الإصدار 3 يدعم قوالب «إطلاق ميزة» و«إصلاح عاجل» و«تجربة مستخدم»، تسميات دورات سبرنت بالعربية، تنبيهات تأخير، تكامل Notion للمواصفات، لوحات متعددة اللغات للفرق المختلطة، وبرنامج «Linear Partners AI MENA» للاستشاريين المعتمدين.</p>
      <p>القدرات الأساسية: مهام من وصف عربي؛ تبعيات وأولويات؛ ملخصات إدارية؛ تكامل أدوات التطوير؛ قوالب قطاعية.</p>
      <p>للمبدعين العرب: استوديو «تشغيل منتج ذكي» — من يُهيّئ Linear AI لفرق 8–45 عضوًا بـ1600–9800 دولار للإطلاق + 380–1750 دولار/شهر للتحسين يبيع للشركات التي تريد سرعة إصدار دون اجتماعات لا تنتهي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Linear AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وتفعيل workspace منتج (قوالب، أتمتة، تدريب فريق):</strong> 5–14 يومًا — 1600–9800 دولار.</li>
          <li><strong>إدارة لوحات وتحديثات إدارية شهريًا:</strong> — 380–1750 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 قوالب دورات سبرنت عربية (SaaS، تجارة، تعليم):</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «إدارة منتج ذكية بالعربية مع Linear»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Linear</span>
        <span class="tag">Product</span>
        <span class="tag">Engineering</span>
        <span class="tag">Sprint</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Buffer AI Assistant 3 Arabic: تقويم سوشيال ذكي — منشورات، ردود، وصوت علامة للخليج ومصر!</h2>
      <p class="article-lead">«خمس قنوات وعشرون منشورًا أسبوعيًا — والفريق ينسخ نفس النبرة الإنجليزية على جمهور عربي». في 23 نوفمبر 2026، أطلقت <strong>Buffer</strong> <strong>Buffer AI Assistant 3 Arabic</strong>: مساعد داخل Buffer يُخطّط تقويمًا أسبوعيًا وشهريًا، يكتب منشورات Instagram وLinkedIn وX وFacebook بالفصحى واللهجات التجارية، يُقترح أوقات النشر حسب نشاط الجمهور في MENA، يُلخّص التعليقات ويقترح ردودًا بصوت العلامة، يُعيد صياغة المحتوى الطويل إلى ثريدات وستوري، يُحلّل أداء المنشورات ويقترح تجارب A/B، ويتكامل مع Canva وتصاميم RTL — للوكالات والعلامات والمؤثرين في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُنتج نصوصًا جافة أو يتجاهل أيام الجمعة والعطل المحلية؛ الإصدار 3 يحترم تقويم المناسبات العربية، قوالب «عرض منتج» و«توظيف» و«تعليم سريع»، حدودًا لعدد المنشورات اليومية، تكاملًا مع Google Analytics للربط مع التحويلات، وبرنامج «Buffer Experts AI Arabia» للمنفّذين.</p>
      <p>القدرات الأساسية: تقويم ذكي؛ نصوص RTL؛ أوقات نشر؛ ردود تعليقات؛ تحليل أداء.</p>
      <p>للمبدعين العرب: خدمة «سوشيال يدير نفسه» — من يُشغّل Buffer AI لعلامة أو 8 عملاء بـ520–3400 دولار للإعداد + 220–980 دولار/شهر للتشغيل يبني دخلًا متكررًا من الوكالات الصغيرة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Buffer AI Assistant 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد تقويم وصوت علامة + تدريب فريق (3–8 قنوات):</strong> 4–10 أيام — 520–3400 دولار.</li>
          <li><strong>تشغيل وتحسين محتوى شهريًا لكل عميل:</strong> — 220–980 دولار/عميل/شهر.</li>
          <li><strong>حزمة 60 قالب منشور عربي (قطاعات متعددة):</strong> — 95–380 دولار/حزمة.</li>
          <li><strong>ورش «محتوى سوشيال ذكي بالعربية مع Buffer»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Buffer</span>
        <span class="tag">Social</span>
        <span class="tag">Marketing</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>New Relic Grok 2 Arabic: مراقبة تُفكّر — من التنبيه إلى السبب الجذري وخطة الإصلاح!</h2>
      <p class="article-lead">«الصفحة حمراء والفريق يبحث في آلاف السجلات — والعميل ينتظر». في 23 نوفمبر 2026، أطلقت <strong>New Relic</strong> <strong>New Relic Grok 2 Arabic</strong>: مساعد ذكاء فوق منصة المراقبة يُلخّص الحوادث بالفصحى التقنية الواضحة، يربط بين السجلات والتتبعات والمقاييس، يُقترح أسبابًا جذرية محتملة مرتبة بالاحتمال، يُولّد خطوات استكشاف وإصلاح، يكتب ملخص ما بعد الحادث للإدارة، يُرسل تحديثات إلى Slack وPagerDuty وJira، يحترم سياسات عدم الكشف عن البيانات الحساسة، ويدعم فرق on-call في السعودية والإمارات ومصر.</p>
      <p>المشكلة التي حلّتها: Grok 1 كان يُطيل الشرح أو يُغفل السياق المحلي لساعات الذروة؛ الإصدار 2 يدعم قوالب «تباطؤ API» و«ذاكرة تسرب» و«فشل دفع»، تكامل Kubernetes وAWS وAzure، تنبيهات بالعربية للمدير غير التقني، سجل تدقيق للامتثال، وبرنامج «New Relic AI Partners MENA».</p>
      <p>القدرات أساسية: تلخيص حوادث؛ سبب جذري مقترح؛ خطوات إصلاح؛ تكامل on-call؛ تقارير إدارية.</p>
      <p>للمبدعين العرب: مكتب «موثوقية ذكية» — من يُفعّل New Relic Grok لمنصة SaaS أو بنك رقمي بـ2800–16800 دولار للإطلاق + 480–2200 دولار/شهر للصيانة يخدم الشركات التي تدفع غرامات توقف مكلفة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من New Relic Grok 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مراقبة + Grok + runbooks عربية + تكامل on-call:</strong> 8–18 يومًا — 2800–16800 دولار.</li>
          <li><strong>صيانة وتحسين تنبيهات وتقارير شهريًا:</strong> — 480–2200 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 runbook عربي جاهز (API، قاعدة بيانات، CDN):</strong> — 140–560 دولار/حزمة.</li>
          <li><strong>ورش «مراقبة وإنتاجية موثوقة بالعربية مع New Relic»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">New Relic</span>
        <span class="tag">Observability</span>
        <span class="tag">SRE</span>
        <span class="tag">DevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Amplitude AI Analyst 3 Arabic: تحليل منتج يتكلم — احتفاظ، قنوات، وتجارب مقترحة للفريق!</h2>
      <p class="article-lead">«لوحة التحليلات مليئة بالرسوم — ولا أحد يعرف لماذا ترك المستخدمون التطبيق». في 23 نوفمبر 2026، أطلقت <strong>Amplitude</strong> <strong>Amplitude AI Analyst 3 Arabic</strong>: محلل ذكاء فوق بيانات المنتج يُجيب أسئلة بالعربية الطبيعية، يُفسّر انخفاض الاحتفاظ ومسارات التحويل، يُقترح تجارب A/B مرتبة بالأثر المتوقع، يُلخّص سلوك الشرائح في MENA، يُنشئ تقارير للمديرين بلغة أعمال واضحة، يُربط الأحداث بالحملات التسويقية، يحترم صلاحيات الفرق، ويتكامل مع Slack وNotion — لتطبيقات التجارة والتعليم والخدمات المالية في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُعيد أرقامًا دون سياق؛ الإصدار 3 يُضيف رواية «ماذا حدث ولماذا»، يدعم مقارنات أسبوعية تلقائية، تكامل Experiments لتشغيل الاختبارات، تنبيهات عند شذوذ المقاييس، قوالب «انطلاق ميزة» و«تسعير» و«onboarding»، وبرنامج «Amplitude Growth Partners Arabia».</p>
      <p>القدرات الأساسية: أسئلة عربية طبيعية؛ تفسير احتفاظ؛ تجارب مقترحة؛ تقارير إدارية؛ تكامل أدوات الفريق.</p>
      <p>للمبدعين العرب: استوديو «نمو مدفوع بالبيانات» — من يُشغّل Amplitude AI Analyst لمنتج 50 ألف–3 مليون مستخدم نشط بـ2200–13500 دولار للإطلاق + 420–1900 دولار/شهر للتحليل المستمر يخدم الشركات النامية في MENA.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Amplitude AI Analyst 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد تحليلات + أحداث + لوحة ذكاء عربية:</strong> 7–16 يومًا — 2200–13500 دولار.</li>
          <li><strong>تحليل أسبوعي وتجارب نمو شهريًا:</strong> — 420–1900 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 تقارير إدارية عربية جاهزة (قطاعات SaaS وتجزئة):</strong> — 98–392 دولار/حزمة.</li>
          <li><strong>ورش «نمو منتج بالعربية مع Amplitude AI»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Amplitude</span>
        <span class="tag">Analytics</span>
        <span class="tag">Growth</span>
        <span class="tag">Product</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="23-11-2026 -- 08-AM.html">
          📰 23 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "23-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/23-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/23-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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