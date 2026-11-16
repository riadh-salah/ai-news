#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "16-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 3 Arabic · Canva Magic Studio 3 Arabic · "
    "Perplexity Comet 2 Arabic · Stripe Revenue AI 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 3 Arabic، Canva Magic Studio 3 Arabic، Perplexity Comet 2 Arabic، Stripe Revenue AI 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 16 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 3 Arabic الذي يُبني وكلاء مؤسسيين يتحدثون بالفصحى ويتصرفون داخل Teams وDynamics دون أن يكتب المبرمج سطرًا واحدًا، إلى Canva Magic Studio 3 Arabic الذي يُحوّل فكرة حملة واحدة إلى عشرات تصاميم RTL جاهزة للنشر، ومن Perplexity Comet 2 Arabic الذي يُصفّح الإنترنت نيابةً عنك ويُلخّص الأخبار ويُقارن الأسعار بالعربية، إلى Stripe Revenue AI 2 Arabic الذي يُتنبّأ بالاشتراكات المتأخرة ويُقترح عروضًا استردادًا ذكية قبل أن يغادر العميل — أربع قصص صباحية في 16 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ لقادة التحول الرقمي ووكالات التسويق وفرق النمو: الوكلاء صاروا موظفين عربيين، التصميم صار محادثة، البحث صار متصفحًا ذكيًا، والمدفوعات صارت محللًا تنبؤيًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 16 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 3 Arabic: وكلاء مؤسسيون يتحدثون العربية — دعم، مبيعات، وامتثال!</h2>
      <p class="article-lead">«فرق الدعم تتلقى ألف استفسار يوميًا — أريد وكيلًا يفهم سياسة الشركة بالعربية ويُصعّد الحالات الحساسة فقط». في 16 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 3 Arabic</strong>: منصة بناء وكلاء تربط SharePoint وDynamics 365 وServiceNow وقواعد المعرفة الداخلية، تفهم اللهجات المهنية العربية، تُجيب من مستندات معتمدة، تُنشئ تذاكر، تُحدّث CRM، تُرسل تقارير يومية للمديرين، وتدعم موافقات بشرية قبل أي إجراء مالي — للبنوك والاتصالات والتجزئة والجهات الحكومية في الشرق الأوسط.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُبالغ في الردود أو يتجاهل سياسات الخصوصية المحلية؛ Studio 3 يُعرّف حدودًا صارمة للمصادر، يدعم التشفير داخل المنطقة، يُحسّن الأسلوب الرسمي الخليجي والمصري، يتكامل مع Azure OpenAI وPhi المحلي، يُوفّر قوالب «دعم عملاء» و«موارد بشرية» و«مشتريات»، وبرنامج شريك «Copilot Studio Partner MENA».</p>
      <p>القدرات الأساسية: Arabic grounded answers؛ تدفقات موافقة متعددة المستويات؛ تحليلات استخدام؛ ربط واتساب للأعمال؛ اختبار محادثات قبل الإطلاق.</p>
      <p>للمبدعين العرب: استشارة «وكيل دعم عربي خلال عشرة أيام» — من يبيع 6 مشاريع شهريًا بـ2200–12500 دولار للمشروع + 550–2400 دولار/شهر للصيانة يُحوّل مراكز الاتصال إلى تشغيل ذكي دون توظيف مئات الجدد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم ونشر وكيل مؤسسي متكامل:</strong> 8–22 يومًا — 2200–12500 دولار/مشروع.</li>
          <li><strong>صيانة قواعد معرفة وتحسين ردود:</strong> — 550–2400 دولار/شهر.</li>
          <li><strong>حزم قوالب قطاعية (اتصالات، تأمين، تعليم):</strong> — 120–480 دولار/حزمة.</li>
          <li><strong>ورش «بناء الوكلاء للمدراء العرب»:</strong> — 75–310 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot</span>
        <span class="tag">Agents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva Magic Studio 3 Arabic: حملة كاملة من جملة واحدة — بوستر، فيديو، ومتجر!</h2>
      <p class="article-lead">«العميل يريد حملة رمضان بخمسة منصات قبل الظهر — والمصمم الوحيد في إجازة». في 16 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 3 Arabic</strong>: مجموعة أدوات تُحوّل موجزًا بالفصحى إلى مجموعة تصاميم متسقة، تُولّد نصوص إعلانات، تُنتج مقاطع قصيرة مع ترجمة عربية، تُضبط هوية بصرية RTL، تُصدّر لإنستغرام وتيك توك ولينكدإن، وتربط متاجر Shopify وSalla مباشرة — لوكالات التسويق والمتاجر الإلكترونية ومدرسي التصميم في العالم العربي.</p>
      <p>المشكلة التي حلّتها: Magic 2 كان يُكرر الخطوط أو يُهمل محاذاة النصوص العربية؛ الإصدار 3 يُحافظ على دليل العلامة، يدعم الخطوط العربية المرخّصة، يُنتج صيغ متعددة للاختبار، يتكامل مع Brandfetch، يُتيح موافقة الفريق قبل النشر، وبرنامج «Canva Creators MENA AI».</p>
      <p>القدرات الأساسية: Arabic campaign kits؛ توليد فيديو من صور؛ جدولة نشر؛ تحليل أداء أولي؛ مكتبة قوالب محلية.</p>
      <p>للمبدعين العرب: باقة «حملة شهرية بالذكاء الاصطناعي» — من يخدم 12 عميلًا بـ650–3200 دولار/شهر لكل عميل يبيع إنتاجًا بصريًا متسارعًا دون تضخم فريق التصميم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>اشتراك إنتاج حملات شهرية للشركات:</strong> — 650–3200 دولار/عميل/شهر.</li>
          <li><strong>إعداد هوية وتدفقات Canva مؤسسية:</strong> 4–9 أيام — 900–4800 دولار.</li>
          <li><strong>بيع حزم قوالب موسمية (رمضان، اليوم الوطني):</strong> — 45–220 دولار/حزمة.</li>
          <li><strong>دورات «تسويق بصري بالذكاء الاصطناعي»:</strong> — 52–210 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Marketing</span>
        <span class="tag">Design</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Perplexity Comet 2 Arabic: متصفح ذكي يتصفح عنك — بحث، مقارنة، وملخص أخبار!</h2>
      <p class="article-lead">«أحتاج مقارنة أسعار خمسة موردين وملخص تقارير السوق قبل اجتماع التسعير — ولا وقت لفتح عشرين تبويبًا». في 16 نوفمبر 2026، أطلقت <strong>Perplexity</strong> <strong>Comet 2 Arabic</strong>: متصفح مدعوم بالذكاء الاصطناعي يُنفّذ مهام متعددة الخطوات، يزور المواقع، يستخرج جداول الأسعار، يُلخّص الأخبار العالمية بالفصحى، يُرسل تقريرًا منظمًا إلى بريدك، ويحترم قوائم المواقع المسموحة للشركات — للباحثين ومديري المشتريات والصحفيين ومحللي الاستثمار العرب.</p>
      <p>المشكلة التي حلّتها: Comet 1 كان يتوقف عند صفحات الدفع أو يُخطئ في الأرقام؛ الإصدار 2 يُثبت المصادر، يدعم وضع «قراءة فقط» للمؤسسات، يُحسّن فهم الاقتباسات العربية، يتكامل مع Slack وGmail، يُتيح تشغيل مهام مجدولة صباحية، وبرنامج «Perplexity Pro Teams MENA».</p>
      <p>القدرات الأساسية: Arabic multi-step browsing؛ تصدير CSV وPDF؛ مراقبة أسعار؛ ملخصات إخبارية مخصصة؛ عزل بيانات للفرق.</p>
      <p>للمبدعين العرب: خدمة «مراقبة سوق أسبوعية» — من يبيع 25 اشتراكًا بـ180–750 دولار/شهر يُقدّم ذكاء سوقي آليا لشركات صغيرة لا تستطيع توظيف محللين بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Comet 2 Arabic؟</h3>
        <ul>
          <li><strong>تقارير مراقبة أسعار ومنافسين أسبوعية:</strong> — 180–750 دولار/عميل/شهر.</li>
          <li><strong>إعداد مهام متصفح مخصصة للفرق:</strong> 2–5 أيام — 500–2800 دولار.</li>
          <li><strong>ملخصات إخبارية قطاعية (طاقة، تقنية، تجزئة):</strong> — 35–150 دولار/إصدار.</li>
          <li><strong>تدريب «بحث احترافي بالذكاء الاصطناعي»:</strong> — 48–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Comet</span>
        <span class="tag">Browser</span>
        <span class="tag">Research</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Stripe Revenue AI 2 Arabic: مدفوعات ذكية تتنبأ بالتخلي — استرداد، عروض، ونمو!</h2>
      <p class="article-lead">«اشتراكاتنا تتراجع كل شهر — أريد معرفة من على وشك الإلغاء قبل أن يضغط الزر». في 16 نوفمبر 2026، أطلقت <strong>Stripe</strong> <strong>Revenue AI 2 Arabic</strong>: طبقة تحليل فوق المدفوعات والاشتراكات، تُتنبّأ باحتمال التخلي، تُقترح عروض استرداد بالعربية، تُختبر رسائل بريد مخصصة، تُربط بيانات الاستخدام من تطبيقك، وتُولّد لوحات نمو RTL للمؤسسين — لشركات SaaS والتطبيقات والمتاجر الرقمية في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُرسل عروضًا عامة؛ Revenue AI 2 يُقسّم الشرائح، يحترم لوائح الرسائل التسويقية، يدعم عملات الخليج ومصر والمغرب، يتكامل مع HubSpot وIntercom، يُتيح تجارب A/B آلية، وبرنامج «Stripe Partner Growth MENA».</p>
      <p>القدرات الأساسية: Arabic churn prediction؛ حملات استرداد آلية؛ تحليل قيمة العميل مدى الحياة؛ تنبيهات للفرق المالية؛ تصدير لتقارير المستثمرين.</p>
      <p>للمبدعين العرب: استشارة «إنقاذ اشتراكات خلال 30 يومًا» — من ينفّذ 8 عملاء بـ1500–8500 دولار للمشروع + 400–1800 دولار/شهر للمتابعة يبيع نموًا قابلًا للقياس لشركات برمجيات لديها بيانات مدفوعات جاهزة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe Revenue AI 2 Arabic؟</h3>
        <ul>
          <li><strong>تدقيق اشتراكات وإطلاق حملات استرداد:</strong> 3–14 يومًا — 1500–8500 دولار/عميل.</li>
          <li><strong>متابعة نمو وتحسين شهري:</strong> — 400–1800 دولار/شهر.</li>
          <li><strong>قوالب رسائل عربية لقطاعات مختلفة:</strong> — 70–290 دولار/حزمة.</li>
          <li><strong>ورش «الذكاء الاصطناعي للإيرادات المتكررة»:</strong> — 60–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Revenue</span>
        <span class="tag">SaaS</span>
        <span class="tag">Payments</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 16-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="16-11-2026 -- 08-AM.html">
          📰 16 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "16-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/16-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/16-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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