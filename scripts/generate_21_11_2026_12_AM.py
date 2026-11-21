#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "21-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 2 Arabic · Canva AI Brand Studio 2 Arabic · "
    "Stripe AI Revenue Radar Arabic · Notion AI Meeting Hub 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 2 Arabic، Canva AI Brand Studio 2 Arabic، Stripe AI Revenue Radar Arabic، Notion AI Meeting Hub 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 2 Arabic الذي يُحوّل جملة عربية إلى موظف رقمي يُجيب عملاءك ويُدير طلباتك دون برمجة معقدة، إلى Canva AI Brand Studio 2 Arabic الذي يُبني هوية بصرية كاملة — شعار، ألوان، منشورات — من وصف قصير بالعربية، ومن Stripe AI Revenue Radar Arabic الذي يُرصد تسرب الإيرادات ويُقترح تسعيرًا ذكيًا قبل أن تفقد ألف عميل، إلى Notion AI Meeting Hub 3 Arabic الذي يُحوّل اجتماعاتك المسجّلة إلى قرارات ومهام مُسندة بالاسم — أربع قصص ليلية في 21 نوفمبر 2026 لروّاد الأعمال والمبدعين الذين يريدون أدوات عالمية ودخلًا يُضيء أول ساعات الصباح!</h1>
      <p class="hero-sub">ليلةٌ لأصحاب المتاجر والوكالات والشركات الناشئة: وكيلك يُبنى بالعربية، علامتك التجارية تُولَد في دقائق، الإيرادات تُراقب ذاتيًا، والاجتماعات لا تموت في التسجيلات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 21 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 2 Arabic: من فكرة عربية إلى وكيل ذكي — دعم ومبيعات بلا كود معقد</h2>
      <p class="article-lead">«أريد مساعدًا يفهم أسئلة العملاء بالعربية، يُجيب من سياسة الإرجاع، يُنشئ تذكرة دعم، ويُبلغ المدير إذا غضب العميل». في 21 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 2 Arabic</strong>: منصة لبناء وكلاء ذكاء اصطناعي تفهم الأوامر والمحادثات بالفصحى واللهجات الخليجية والمصرية والشامية، تربط SharePoint وDynamics وبوابات الويب، تُنشئ تدفقات موافقة، تلتزم بسياسات الامتثال للمؤسسات، تُصدّر الوكيل إلى Teams وموقعك وقنوات البريد — للشركات الصغيرة والمتوسطة التي تعجز عن توظيف فريق دعم كامل الليل.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يتطلب إنجليزية في معظم القوالب؛ Studio 2 يدعم محرّرًا عربيًا للأسئلة الشائعة، قوالب «متجر إلكتروني» و«عيادة» و«تعليم عن بُعد»، اختبارات محادثة قبل النشر، مراقبة جودة الردود، تكامل Power Automate، حماية من تسريب بيانات حساسة، وبرنامج «Copilot Partners MENA» للمطبّقين المعتمدين.</p>
      <p>القدرات الأساسية: بناء وكيل بالعربية؛ ربط أنظمة Microsoft والويب؛ تدفقات موافقة وتصعيد؛ نشر متعدد القنوات؛ قوالب قطاعية جاهزة.</p>
      <p>للمبدعين العرب: مختبر «موظف رقمي لكل عميل» — من يُسلّم وكيلًا مخصصًا بـ2800–14500 دولار للمشروع + 450–1900 دولار/شهر للصيانة يخدم مؤسسات تريد دعمًا ليليًا دون تضخيم الرواتب.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 2 Arabic؟</h3>
        <ul>
          <li><strong>وكيل دعم أو مبيعات عربي كامل (مع تكاملات):</strong> 8–18 يومًا — 2800–14500 دولار.</li>
          <li><strong>صيانة وتحسين ردود شهريًا:</strong> — 450–1900 دولار/عميل/شهر.</li>
          <li><strong>حزمة 5 وكلاء جاهزة لقطاع واحد:</strong> — 1200–4800 دولار.</li>
          <li><strong>ورش «ابنِ وكيلك بالعربية في Copilot Studio»:</strong> — 48–195 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot Studio</span>
        <span class="tag">Agents</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva AI Brand Studio 2 Arabic: هوية تجارية كاملة من جملة — شعار، ألوان، ومحتوى متسق</h2>
      <p class="article-lead">«علامتنا جديدة: مقهى عربي عصري يستهدف الشباب، أريد شعارًا وبطاقات وقوالب إنستغرام بنفس الروح خلال ساعة». في 21 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>AI Brand Studio 2 Arabic</strong>: استوديو ذكاء اصطناعي داخل Canva يقرأ وصفًا بالعربية، يُولّد هوية بصرية متناسقة، يقترح شعارات قابلة للتعديل، يُنشئ لوحة ألوان وخطوط عربية جميلة، يُنتج قوالب منشورات وستوري وعروض تقديمية، يحافظ على اتساق العلامة عبر الفريق، ويُصدّر دليل استخدام للموردين — لروّاد الأعمال والوكالات التي تخسر أسابيع في التنسيق بين المصمم والناسخ.</p>
      <p>المشكلة التي حلّتها: Brand Studio الأول كان يخلط بين أساليب متعارضة؛ الإصدار 2 يفهم سياقًا ثقافيًا عربيًا أفضل، يدعم RTL في كل القوالب، قوالب «مطاعم» و«تجميل» و«تقنية» و«تعليم»، تكامل Canva Teams، إصدارات Brand Kit للطباعة الرقمية، حماية حقوق الاستخدام التجاري، وبرنامج «Canva Brand Creators Arabia» للمنشئين المعتمدين.</p>
      <p>القدرات الأساسية: هوية من وصف عربي؛ شعارات وقوالب متسقة؛ دليل علامة؛ تعاون فريق؛ تصدير طباعة وويب.</p>
      <p>للمبدعين العرب: وكالة «هوية في يوم واحد» — من يُسلّم حزمة علامة كاملة بـ350–2200 دولار للعميل + اشتراكات Canva Pro جماعية يستهدف المشاريع الناشئة التي لا تملك ميزانية وكالة تقليدية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva AI Brand Studio 2 Arabic؟</h3>
        <ul>
          <li><strong>هوية بصرية كاملة (شعار + 30 قالبًا):</strong> 2–5 أيام — 350–2200 دولار.</li>
          <li><strong>تحديث موسمي وقوالب شهرية:</strong> — 120–480 دولار/شهر.</li>
          <li><strong>حزمة إعادة بناء علامة لـ10 عملاء صغار:</strong> — 2800–9800 دولار.</li>
          <li><strong>دورة «علامة تجارية بالذكاء الاصطناعي مع Canva»:</strong> — 42–175 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Branding</span>
        <span class="tag">Design</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Stripe AI Revenue Radar Arabic: رادار إيرادات ذكي — اكتشف التسرب واضبط التسعير قبل أن يفوت الأوان</h2>
      <p class="article-lead">«اشتراكاتنا تنمو لكن الإيراد الصافي يتذبذب: أين يختفي المال؟». في 21 نوفمبر 2026، أطلقت <strong>Stripe</strong> <strong>AI Revenue Radar Arabic</strong>: طبقة تحليل ذكاء اصطناعي فوق Stripe Billing تُترجم لوحات التحكم إلى تقارير عربية واضحة، تكتشف إلغاءات مبكرة وانخفاض استخدام قبل فوات الأوان، تقترح تسعيرًا وتجارب A/B للخطط، تُنبّه عند فشل دفع متكرر، تُولّد رسائل استرداد اشتراك بالعربية، وتربط محاسبة وتقارير ضريبية للأسواق الإقليمية — لشركات SaaS والمتاجر الرقمية التي تبيع بالدولار والعملات المحلية.</p>
      <p>المشكلة التي حلّتها: الرادار السابق كان بالإنجليزية وموجّهًا للسوق الأمريكي؛ Revenue Radar Arabic يدعم تقارير بالفصحى، قوالب «اشتراكات» و«سوق إلكتروني» و«تطبيقات جوال»، توافقًا مع فوترة VAT في الخليج ومصر والمغرب، تكامل HubSpot وSlack، تنبيهات للمدير المالي، وبرنامج «Stripe Revenue Advisors MENA».</p>
      <p>القدرات الأساسية: تحليل إيرادات بالعربية؛ تنبؤ إلغاء؛ اقتراح تسعير؛ رسائل استرداد؛ تقارير ضريبية.</p>
      <p>للمبدعين العرب: استشارة «إيرادات لا تهرب» — من يُدقّق 15 عميلًا Stripe شهريًا بـ600–2800 دولار/عميل يخدم مؤسسات لا تملك محلل بيانات ماليًا بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe AI Revenue Radar Arabic؟</h3>
        <ul>
          <li><strong>تدقيق إيرادات وخطة تحسين (مرة واحدة):</strong> 5–10 أيام — 1800–9500 دولار.</li>
          <li><strong>مراقبة وتحسين اشتراكات شهريًا:</strong> — 600–2800 دولار/عميل/شهر.</li>
          <li><strong>حزمة تقارير CFO عربية ربع سنوية:</strong> — 450–1800 دولار/ربع.</li>
          <li><strong>ورش «احتفظ بعملائك وارفع ARPU مع Stripe AI»:</strong> — 55–210 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Revenue</span>
        <span class="tag">SaaS</span>
        <span class="tag">Billing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Notion AI Meeting Hub 3 Arabic: اجتماعك لا يموت في التسجيل — قرارات، مهام، ومتابعة بالعربية</h2>
      <p class="article-lead">«ساعة اجتماع ولا أحد يتذكر ماذا اتُفق: نريد ملخصًا عربيًا، مهامًا بأسماء المسؤولين، وموعد متابعة تلقائي». في 21 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>AI Meeting Hub 3 Arabic</strong>: مركز اجتماعات ذكي داخل Notion يلتقط الصوت والفيديو أو يربط Zoom وGoogle Meet، يُفرّق المتحدثين، يُلخّص بالفصحى أو لهجة مختارة، يُستخرج قرارات ومهام بتواريخ، يُنشئ صفحة اجتماع مرتبطة بمشروعك، يُرسل تذكيرات في Slack وEmail، ويقترح نقاطًا للاجتماع القادم — للفرق البعيدة والوكالات التي تعيش على الاجتماعات المتتالية.</p>
      <p>المشكلة التي حلّتها: Meeting Hub 2 كان يخطئ في الأسماء العربية؛ الإصدار 3 يحسّن التعرف على اللهجات، قوالب «مجلس إدارة» و«سبرنت تقني» و«عرض عميل»، ربطًا مع تقويم Google وOutlook، أرشفة بحث عربي، صلاحيات خصوصية للمؤسسات، وبرنامج «Notion Workflow Partners» للمنطقة.</p>
      <p>القدرات الأساسية: تلخيص اجتماع عربي؛ استخراج مهام وقرارات؛ صفحات مرتبطة بالمشاريع؛ تذكيرات تلقائية؛ قوالب اجتماع.</p>
      <p>للمبدعين العرب: خدمة «اجتماعك يصبح نظامًا» — من يُطبّق Hub على 6 فرق بـ1200–6800 دولار للإعداد + 380–1500 دولار/شهر للتشغيل يبيع للشركات التي تضيع ساعات في إعادة شرح ما قيل أمس.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Meeting Hub 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مركز اجتماعات لفريق كامل:</strong> 4–9 أيام — 1200–6800 دولار.</li>
          <li><strong>تشغيل وتدقيق جودة ملخصات شهريًا:</strong> — 380–1500 دولار/فريق/شهر.</li>
          <li><strong>قوالب اجتماع جاهزة (12 نوعًا):</strong> — 85–340 دولار/مجموعة.</li>
          <li><strong>ورش «اجتماعات منتجة بالعربية مع Notion AI»:</strong> — 44–180 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Meetings</span>
        <span class="tag">Productivity</span>
        <span class="tag">Team</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="21-11-2026 -- 12-AM.html">
          📰 21 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "21-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/21-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/21-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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