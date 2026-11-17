#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 17-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "17-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 3 Arabic · Shopify Sidekick 2 Arabic · "
    "Canva Magic Studio 3 Arabic · Zapier Central 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 3 Arabic، Shopify Sidekick 2 Arabic، Canva Magic Studio 3 Arabic، Zapier Central 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 17 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 3 Arabic الذي يُبني وكلاء مؤسسات يفهمون سياسات شركتك بالعربية، إلى Shopify Sidekick 2 Arabic الذي يُدير متجرك ويُطلق حملات من محادثة واحدة، ومن Canva Magic Studio 3 Arabic الذي يُحوّل فكرة مسائية إلى هوية بصرية كاملة، إلى Zapier Central 2 Arabic الذي يُنسّق عشرات التطبيقات بوكيل ذكي — أربع قصص مسائية في 17 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يستمر بعد غروب الشمس!</h1>
      <p class="hero-sub">مساء عملٍ رقمي لا يتوقف: الوكلاء يخدمون الفرق، المتجر يبيع وحده، التصميم يولد من الجملة، والأتمتة تفكر نيابةً عنك. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 17 نوفمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 3 Arabic: وكلاء مؤسسات يفهمون السياسات الداخلية ويُجيبون الموظفين بالعربية</h2>
      <p class="article-lead">«لدينا مئات الوثائق والموظفون يسألون نفس الأسئلة يوميًا — أريد وكيلًا يعرف دليل الشركة ولا يخترع إجابات». في 17 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 3 Arabic</strong>: منصة بناء وكلاء مدمجة في Microsoft 365 وTeams وSharePoint، تقرأ سياسات المنشأة بالفصحى، تُجيب أسئلة الموارد البشرية والقانونية والمبيعات، تُنشئ مهامًا في Planner، تُحيل للإنسان عند الحساسية، وتلتزم بحدود البيانات داخل حدود المستأجر — للبنوك والطيران والاتصالات والحكومة الرقمية في العالم العربي.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يخلط بين وثائق قديمة أو يُجيب بإنجليزية عند المصطلحات التقنية؛ Studio 3 يدعم فهرسة متعددة اللغات، موافقات على الإجراءات الحساسة، تكامل Power Automate، قوالب «إجازات ورواتب» و«سياسة سفر» و«أسئلة مبيعات»، تدريبًا على لهجات الخليج والشام، وبرنامج شركاء «Copilot MENA Enterprise».</p>
      <p>القدرات الأساسية: وكلاء مخصصون بالعربية؛ ربط M365 وTeams؛ موافقات بشرية؛ أتمتة Power Platform؛ امتثال داخل المستأجر.</p>
      <p>للمبدعين العرب: عرض «وكيل موارد بشرية جاهز في أسبوعين» — من يُنفّذ 3 مشاريع شهريًا بـ3200–18500 دولار للتسليم يبيع كفاءة لمؤسسات تُقلّص زمن الاستجابة الداخلي من أيام إلى دقائق.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم ونشر وكلاء مؤسسات عربية (HR، قانونية، مبيعات):</strong> 10–22 يومًا — 3200–18500 دولار.</li>
          <li><strong>صيانة وتحسين المعرفة والمحادثات شهريًا:</strong> — 850–3900 دولار/عميل/شهر.</li>
          <li><strong>قوالب وكلاء قطاعية (طيران، اتصالات، بنك):</strong> — 95–420 دولار/حزمة.</li>
          <li><strong>ورش «من السياسة إلى وكيل يعمل» لفِرق التحول الرقمي:</strong> — 82–328 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick 2 Arabic: مدير متجر ذكي — تحليل، حملات، ونصوص بيع من محادثة عربية</h2>
      <p class="article-lead">«متجري يبيع ليلًا ونهارًا وأنا أنسى تحديث الوصف والعروض — أريد مساعدًا يفهم السوق العربي ويقترح خطوات واضحة». في 17 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 2 Arabic</strong>: مساعد تجارة إلكترونية داخل لوحة التحكم، يحلل المبيعات والمخزون، يُولّد أوصاف منتجات بالفصحى واللهجة المحلية، يُقترح حملات بريد وSMS، يُعدّ تقارير أسبوعية بالعربية، يتكامل مع Meta وGoogle Ads وWhatsApp Catalog — لتجار الأزياء والعطور والإلكترونيات والمنتجات الحرفية في المنطقة.</p>
      <p>المشكلة التي حلّتها: Sidekick الأول كان يترجم العناوين حرفيًا أو يُهمل RTL في القوالب؛ الإصدار 2 يدعم تسعيرًا موسميًا (رمضان، العيد، اليوم الوطني)، اقتراحات bundle، تنبيهات مخزون، قوالب «إطلاق مجموعة» و«تصفية موسمية» و«استرداد عربة»، وبرنامج «Shopify Arabia Growth Partners».</p>
      <p>القدرات الأساسية: تحليل مبيعات بالعربية؛ أوصاف وحملات؛ تكامل إعلانات؛ WhatsApp Catalog؛ تقارير أسبوعية.</p>
      <p>للمبدعين العرب: خدمة «متجر يبيع أكثر في 30 يومًا» — من يُدير 8 متاجر شهريًا بـ680–2800 دولار/شهر + 1200–4500 دولار لإعداد Sidekick يبيع نموًا لمشاريع لا تملك فريق تسويق كاملًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد وتدريب Sidekick لمتجر عربي:</strong> 5–12 يومًا — 1200–4500 دولار.</li>
          <li><strong>إدارة نمو المتجر وتحسين الحملات شهريًا:</strong> — 680–2800 دولار/متجر/شهر.</li>
          <li><strong>قوالب أوصاف وحملات موسمية (رمضان، عيد، صيف):</strong> — 45–195 دولار/مجموعة.</li>
          <li><strong>معسكر «من أول منتج إلى أول ألف طلب»:</strong> — 88–352 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">E-Commerce</span>
        <span class="tag">Sidekick</span>
        <span class="tag">Retail</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Canva Magic Studio 3 Arabic: استوديو تصميم بالذكاء الاصطناعي — هوية، فيديو، وعروض جاهزة للنشر</h2>
      <p class="article-lead">«العميل يريد هوية كاملة غدًا — الشعار والبوستات والعرض التقديمي كلها بالعربية». في 17 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 3 Arabic</strong>: مجموعة أدوات AI داخل Canva Pro، تُولّد شعارات ولوحات ألوان، تُحوّل نصًا إلى فيديو قصير بخطوط RTL، تُنشئ عروضًا تقديمية من مخطط عربي، تُحافظ على دليل العلامة، وتُصدّر حزمًا لإنستغرام وتيك توك ولينكدإن — للمؤثرين والوكالات الصغيرة والمدارس وفرق التسويق الداخلية.</p>
      <p>المشكلة التي حلّتها: Magic Studio 2 كان يُشوّه الحروف المتصلة أو يُهمل اتجاه النص في الفيديو؛ الإصدار 3 يدعم قوالب «مطعم» و«عيادة» و«تطبيق تقني»، تحريرًا جماعيًا، علامة Canva Shield للأمان، تكامل Brandfolder، وبرنامج «Canva Creators MENA».</p>
      <p>القدرات الأساسية: شعار وهوية من وصف عربي؛ فيديو وعروض RTL؛ حزم سوشيال؛ دليل علامة؛ تصدير سريع.</p>
      <p>للمبدعين العرب: استوديو «هوية في 72 ساعة» — من يُسلّم 12 حزمة شهريًا بـ420–2400 دولار للحزمة يبيع سرعة بصرية لعلامات تتنافس على الانتباه دون توظيف مصمم بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>حزم هوية بصرية كاملة (شعار + سوشيال + عرض):</strong> 2–5 أيام — 420–2400 دولار/حزمة.</li>
          <li><strong>اشتراك محتوى مرئي شهري (20–40 منشورًا):</strong> — 350–1650 دولار/عميل/شهر.</li>
          <li><strong>قوالب Canva عربية جاهزة (قطاع محدد):</strong> — 35–150 دولار/مجموعة.</li>
          <li><strong>دورة «Magic Studio للمسوقين غير المصممين»:</strong> — 55–220 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Design</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Branding</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zapier Central 2 Arabic: مركز أتمتة بذكاء اصطناعي — يُربط التطبيقات ويُنفّذ المهام من أمر عربي</h2>
      <p class="article-lead">«نستخدم عشرة تطبيقات والبيانات تتشتت — أريد أن أقول بالعربية: عندما يصل طلب جديد، أرسل إشعارًا وحدّث الجدول وردّ على العميل». في 17 نوفمبر 2026، أطلقت <strong>Zapier</strong> <strong>Central 2 Arabic</strong>: طبقة وكلاء فوق أكثر من 7000 تطبيق، تفهم الأوامر بالفصحى، تُنشئ مسارات Zap مع شروط وتحويلات، تُراقب الأخطاء وتُعيد المحاولة، تُلخص سجل التشغيل بالعربية، وتتكامل مع Slack وGmail وNotion وHubSpot وShopify — للشركات الناشئة والوكالات وفرق العمليات.</p>
      <p>المشكلة التي حلّتها: Central الأول كان يتطلب صياغة إنجليزية دقيقة للمشغلات؛ الإصدار 2 يدعم شرحًا تفاعليًا بالعربية، قوالب «تأهيل عميل» و«فواتير وتحصيل» و«تذكير اجتماع»، اختبارًا آمنًا قبل التفعيل، سجلات امتثال، وبرنامج «Zapier Automation Arabia».</p>
      <p>القدرات الأساسية: أوامر عربية إلى أتمتة؛ 7000+ تطبيق؛ مراقبة وإعادة محاولة؛ قوالب قطاعية؛ ملخصات تشغيل.</p>
      <p>للمبدعين العرب: عرض «عمليات خالية من النسخ في 21 يومًا» — من ينشر 4 أتمتة مؤسسية شهريًا بـ2400–14000 دولار للمشروع + 520–2100 دولار/شهر للصيانة يبيع وقتًا محفوظًا لفرق لا تملك مهندس تكامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zapier Central 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وتفعيل أتمتة مؤسسية من متطلبات عربية:</strong> 8–21 يومًا — 2400–14000 دولار.</li>
          <li><strong>مراقبة وتحسين المسارات شهريًا:</strong> — 520–2100 دولار/عميل/شهر.</li>
          <li><strong>قوالب Zap جاهزة (مبيعات، دعم، مالية):</strong> — 60–260 دولار/حزمة.</li>
          <li><strong>ورش «أتمتة بدون برمجة للمديرين»:</strong> — 68–272 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zapier</span>
        <span class="tag">Automation</span>
        <span class="tag">Integration</span>
        <span class="tag">Workflow</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 17-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="17-11-2026 -- 04-PM.html">
          📰 17 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "17-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/17-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/17-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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