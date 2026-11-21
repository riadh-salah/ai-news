#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "21-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Freshworks Freddy AI 3 Arabic · Airtable Omni 2 Arabic · "
    "Squarespace Blueprint AI 2 Arabic · Adobe Express Brand Kit AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Freshworks Freddy AI 3 Arabic، Airtable Omni 2 Arabic، Squarespace Blueprint AI 2 Arabic، Adobe Express Brand Kit AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Freshworks Freddy AI 3 Arabic الذي يُغلق تذاكر الدعم ويُرتب المبيعات بلهجة العميل قبل أن يصل إشعار المساء، إلى Airtable Omni 2 Arabic الذي يُحوّل جداولك المشتتة إلى لوحات قرار ومهام بأمر عربي واحد، ومن Squarespace Blueprint AI 2 Arabic الذي يُطلق موقعًا ومتجرًا وحملة بريد من وصف بالفصحى قبل أن تُطفأ أضواء المكتب، إلى Adobe Express Brand Kit AI 3 Arabic الذي يُبقي شعارك وألوانك متسقة في كل منشور وستوري وفيديو — أربع قصص مسائية في 21 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ لفرق الدعم والعمليات والتجارة الإلكترونية والعلامات الصغيرة: الخدمة تُصبح محادثة ذكية، البيانات تُصبح قرارًا، الحضور الرقمي يُصبح ساعةً واحدة، والهوية البصرية تُصبح نظامًا لا مجرد ملف. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 21 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Freshworks Freddy AI 3 Arabic: دعم ومبيعات بلسان العميل — تذاكر، تأهيل، ومتابعات ذكية!</h2>
      <p class="article-lead">«التذاكر تتراكم والفريق يرد بنفس الرد الإنجليزي على عميل يكتب بالعربية — ودرجة الرضا تهبط كل أسبوع». في 21 نوفمبر 2026، أطلقت <strong>Freshworks</strong> <strong>Freddy AI 3 Arabic</strong>: طبقة ذكاء فوق Freshdesk وFreshsales تفهم الفصحى واللهجات الخليجية والمصرية والشامية، تُحلّ استفسارات الشحن والفوترة من أول رسالة، تُؤهّل العملاء المحتملين وتُلخص محادثات المبيعات، تُقترح ردودًا بصوت العلامة، تُصعّد للإنسان عند الغضب أو المبالغ المرتفعة، تُربط قاعدة المعرفة وواتساب والبريد، وتُحترم سياسات الخصوصية المحلية — للتجزئة الإلكترونية والاتصالات والتعليم والخدمات في المنطقة.</p>
      <p>المشكلة التي حلّتها: Freddy 2 كان يُكرر إجابات عامة أو يُخطئ في أرقام الطلبات العربية؛ الإصدار 3 يُثبت قاموس منتجات لكل عميل، يدعم وضع «تعاطف تجاري» للشكاوى، يُنشئ مهام متابعة تلقائية في CRM، يُولّد تقارير أسبوعية بالعربية للإدارة، يتكامل مع Slack وMicrosoft Teams، قوالب «ضمان» و«استرجاع» و«ترقية باقة»، وبرنامج «Freshworks AI Partners MENA» للمطبّقين المعتمدين.</p>
      <p>القدرات الأساسية: محادثات عربية متعددة القنوات؛ حل تذاكر ذاتي؛ تأهيل مبيعات؛ تصعيد ذكي؛ تقارير رضا عملاء.</p>
      <p>للمبدعين العرب: خلية «دعم ذكي في أسبوع» — من يُسلّم إعداد Freddy لثلاث علامات بـ2100–11500 دولار للإطلاق + 380–1750 دولار/شهر للتحسين يبيع للشركات التي تدفع موظفي ليل بسبب ذروة الرسائل المسائية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Freshworks Freddy AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Freddy وقاعدة معرفة عربية كاملة:</strong> 5–12 يومًا — 2100–11500 دولار/علامة.</li>
          <li><strong>صيانة ردود وتحليل شكاوى شهريًا:</strong> — 380–1750 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 سيناريو دعم جاهز (تجزئة، سفر، تعليم):</strong> — 95–420 دولار/حزمة.</li>
          <li><strong>ورش «خدمة عملاء ذكية بالعربية مع Freddy»:</strong> — 48–195 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Freshworks</span>
        <span class="tag">Freddy</span>
        <span class="tag">Support</span>
        <span class="tag">CRM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Airtable Omni 2 Arabic: من جداول فوضوية إلى قرارات — أوامر عربية، لوحات، وأتمتة!</h2>
      <p class="article-lead">«عشرون جدولًا لكل قسم — والمدير يريد رؤية واحدة لحالة المشاريع قبل اجتماع الغد». في 21 نوفمبر 2026، أطلقت <strong>Airtable</strong> <strong>Omni 2 Arabic</strong>: مساعد داخل قواعد Airtable يفهم الأوامر بالفصحى، يُنشئ حقولًا وviews ولوحات تحكم من وصف نصي، يُلخّص آلاف الصفوف بفقرات عربية، يُقترح أتمتة بين الجداول، يُولّد تقارير PDF للعملاء، يُربط Slack وGmail، يُحترم صلاحيات الفريق، ويُصدّر بيانات جاهزة للتحليل — للوكالات وشركات الأحداث والعقارات والخدمات التي تعتمد Airtable كعمود فقري للعمليات.</p>
      <p>المشكلة التي حلّتها: Omni الأول كان يُنشئ عناوين أعمدة بالإنجليزية رغم واجهة عربية؛ الإصدار 2 يُنتج تسميات RTL كاملة، قوالب «تتبع حملة» و«مخزون متجر» و«جدول فعاليات»، تنبيهات عند تأخر التسليم، تكامل مع Zapier وMake، مراجعة بشرية قبل حذف بيانات، وبرنامج «Airtable Solution Partners Arabia».</p>
      <p>القدرات الأساسية: أوامر عربية؛ لوحات فورية؛ أتمتة مقترحة؛ ملخصات تنفيذية؛ قوالب قطاعية.</p>
      <p>للمبدعين العرب: استوديو «نظام عمليات في 10 أيام» — من يبني قاعدة Airtable مع Omni لفرق 15–80 شخصًا بـ2800–14800 دولار يختصر شهور تنسيق يدوي في أسبوعين من الإعداد الذكي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable Omni 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم قاعدة عمليات كاملة مع Omni:</strong> 8–18 يومًا — 2800–14800 دولار/مؤسسة.</li>
          <li><strong>تشغيل أتمتة وتحسين لوحات شهريًا:</strong> — 420–2100 دولار/عميل/شهر.</li>
          <li><strong>مجموعة 8 قوالب عربية جاهزة (وكالة، عقار، تعليم):</strong> — 180–720 دولار/مجموعة.</li>
          <li><strong>دورات «إدارة بيانات ذكية بالعربية مع Airtable Omni»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">Omni</span>
        <span class="tag">Operations</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Squarespace Blueprint AI 2 Arabic: موقعك ومتجرك من فكرة عربية — صفحات، SEO، وحملة بريد!</h2>
      <p class="article-lead">«أريد حضورًا احترافيًا على الإنترنت لمتجري الصغير — لكن الميزانية لا تسمح بوكالة كاملة». في 21 نوفمبر 2026، أطلقت <strong>Squarespace</strong> <strong>Blueprint AI 2 Arabic</strong>: منشئ ذكي يقرأ وصف نشاطك بالفصحى أو لهجة تجارية، يُختار قالبًا RTL مناسبًا، يُكتب نصوص الصفحة الرئيسية و«من نحن» وصفحات المنتج بأسلوب مقنع، يُحسّن العناوين لمحركات البحث العربية، يُنشئ نموذج اشتراك بريد وسلسلة ترحيب، يُقترح صورًا من مكتبة مرخّصة، وينشر الموقع مع شهادة أمان — لمقدمي الخدمات والحرفيين والمتاجر الناشئة في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: Blueprint الأول كان يُنتج فقرات مكررة أو يُهمل اتجاه النص في الأزرار؛ الإصدار 2 يدعم خطوط عربية محلية، دفع Squarespace Payments ومناطق توصيل، تكامل Instagram Shopping، قوالب «استشارة» و«مطعم» و«تجميل» و«تدريب»، تحليلات زوار بالعربية، وبرنامج «Squarespace Creators MENA».</p>
      <p>القدرات الأساسية: مواقع RTL كاملة؛ نصوص SEO؛ بريد تسويقي؛ متجر إلكتروني؛ نشر سريع.</p>
      <p>للمبدعين العرب: باقة «إطلاق نهاية الأسبوع» — من يُسلّم موقعًا جاهزًا للتاجر خلال 48 ساعة بـ650–4200 دولار يخدم آلاف المشاريع الصغيرة التي تبحث عن حضور رقمي دون تعقيد تقني.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Squarespace Blueprint AI 2 Arabic؟</h3>
        <ul>
          <li><strong>موقع أو متجر كامل من مقابلة عربية واحدة:</strong> 2–5 أيام — 650–4200 دولار/مشروع.</li>
          <li><strong>صيانة محتوى وتحسين SEO شهريًا:</strong> — 180–880 دولار/موقع/شهر.</li>
          <li><strong>حزمة 5 صفحات هبوط قطاعية جاهزة:</strong> — 120–480 دولار/حزمة.</li>
          <li><strong>ورش «متجرك الأول بالعربية مع Squarespace Blueprint»:</strong> — 38–165 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Squarespace</span>
        <span class="tag">Blueprint</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Web</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Adobe Express Brand Kit AI 3 Arabic: هوية واحدة لكل منصة — منشورات، فيديو، وستوريات بلا فوضى!</h2>
      <p class="article-lead">«كل مصمم يخرج نسخة مختلفة من الشعار — والعميل يسأل: أين علامتنا الحقيقية؟». في 21 نوفمبر 2026، أطلقت <strong>Adobe</strong> <strong>Express Brand Kit AI 3 Arabic</strong>: نظام يخزّن شعارك وألوانك وخطوطك العربية المعتمدة، يُطبّقها تلقائيًا على قوالب Instagram وLinkedIn وTikTok وYouTube Shorts، يُولّد فيديوهات قصيرة بنص عربي متحرك، يُقترح عناوين حسب المنصة، يُتحقق من تباين الألوان لإمكانية القراءة، يتكامل مع Photoshop وIllustrator وCreative Cloud، ويُصدّر حزم حملات جاهزة للطباعة الرقمية — للوكالات الصغيرة والمؤثرين وفرق التسويق في الشركات المتوسطة.</p>
      <p>المشكلة التي حلّتها: Brand Kit 2 كان يُشوّه الحروف المتصلة في العناوين أو يستخدم خطوطًا لا تدعم التشكيل؛ الإصدار 3 يدعم خطوط عربية احترافية، قوالب «رمضان» و«يوم وطني» و«إطلاق منتج»، وضع موافقة الفريق قبل النشر، أرشفة إصدارات الهوية، تكامل Firefly للصور، وبرنامج «Adobe Express Partners MENA».</p>
      <p>القدرات الأساسية: هوية موحّدة؛ قوالب متعددة المنصات؛ فيديو قصير؛ تحقق جودة؛ تعاون فريق.</p>
      <p>للمبدعين العرب: اشتراك «مدير هوية رقمي» — من يدير Brand Kit لثماني علامات بـ520–2650 دولار/شهر لكل علامة يبيع اتساقًا بصريًا دون استوديو تصميم كامل لكل عميل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Adobe Express Brand Kit AI 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء Brand Kit وإطلاق حملة أولى (15 أصلًا):</strong> 4–10 أيام — 880–5800 دولار.</li>
          <li><strong>إدارة محتوى اجتماعي وتحديث قوالب شهريًا:</strong> — 520–2650 دولار/علامة/شهر.</li>
          <li><strong>حزمة 30 قالبًا قطاعيًا مع هوية العميل:</strong> — 240–980 دولار/حزمة.</li>
          <li><strong>ورش «هوية رقمية عربية مع Adobe Express»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Adobe</span>
        <span class="tag">Express</span>
        <span class="tag">Brand</span>
        <span class="tag">Social</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="21-11-2026 -- 04-PM.html">
          📰 21 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "21-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/21-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/21-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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