#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 14-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "14-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI ChatGPT Atlas 3 Arabic · Cursor Cloud Agents 2 Arabic · "
    "Runway Gen-4 Director Arabic · HubSpot Breeze Copilot 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI ChatGPT Atlas 3 Arabic، Cursor Cloud Agents 2 Arabic، Runway Gen-4 Director Arabic، HubSpot Breeze Copilot 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 14 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من OpenAI ChatGPT Atlas 3 Arabic الذي يُتصفح الويب نيابة عنك ويُرسل تقريرًا عربيًا عن منافسيك قبل أن تُنهي قهوتك، إلى Cursor Cloud Agents 2 Arabic الذي يُبرمج ميزتك ويُفتح طلب دمج بينما أنت في اجتماع، ومن Runway Gen-4 Director Arabic الذي يُحوّل سكربتًا عربيًا إلى إعلان سينمائي بثلاث لقطات في دقائق، إلى HubSpot Breeze Copilot 3 Arabic الذي يُكتب رسائل مبيعات بالفصحى ويُقدّر احتمال إغلاق كل صفقة — أربع قصص مسائية في 14 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ للمؤسسين والمسوقين ومطوري المنتجات: التصفح أصبح وكيلًا، الشيفرة تُكتب في السحابة، الفيديو أصبح إخراجًا، وخط المبيعات يريد ذكاءً يفهم اللغة العربية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 14 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI ChatGPT Atlas 3 Arabic: متصفح ذكي يعمل لك — بحث، تلخيص، وتقارير بالعربية!</h2>
      <p class="article-lead">«أريد كل أسعار المنافسين في السوق السعودي قبل اجتماع الغد — ولا وقت لقراءة عشرين موقعًا». في 14 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>ChatGPT Atlas 3 Arabic</strong>: متصفح مدمج مع ChatGPT يفتح عشرات الصفحات بالتوازي، يقرأ الجداول والأسعار والشروط، يُلخّص بالفصحى أو اللهجة التي تختارها، يُصدّر PDF وNotion وSlack، يحترم سياسات المؤسسة ولا يُدخل بيانات حساسة دون موافقة — للبحث التنافسي والمشتريات والصحافة الاستقصائية الرقمية.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يتوقف عند صفحات الدفع أو يُخطئ في الأرقام العربية؛ الإصدار 3 يُميّز بين الفاصلة العربية والإنجليزية، يُعيد المحاولة عند CAPTCHA بطرق معتمدة، يُسجّل مسار التصفح للمراجعة، يتكامل مع Enterprise SSO، ويُوفّر وضع «مراقب امتثال» لقطاعات مالية.</p>
      <p>القدرات الأساسية: Arabic competitive briefs؛ جدولة تقارير يومية؛ ربط مع Zapier وMake؛ حدود استعلام لكل فريق؛ برنامج شريك «Atlas Research MENA».</p>
      <p>للمبدعين العرب: مكتب أبحاث رقمي — «تقرير منافسين أسبوعي بالعربية في 24 ساعة». من يخدم 8 شركات ناشئة بـ450–3200 دولار/شهر + إعداد أولي 600–4200 دولار يبيع ذكاء تصفح دون توظيف محللين كاملين.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI ChatGPT Atlas 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Atlas (سياسات، قوالب تقارير، تدريب فرق):</strong> 3–9 أيام — 600–4200 دولار/عميل.</li>
          <li><strong>تقارير تنافسية أسبوعية بالعربية:</strong> — 450–3200 دولار/شهر.</li>
          <li><strong>حزم قطاعية (تجزئة، تعليم، صحة):</strong> — 55–230 دولار/حزمة.</li>
          <li><strong>دورات «أبحاث سوق بالعربية مع ChatGPT Atlas»:</strong> — 45–185 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">ChatGPT</span>
        <span class="tag">Atlas</span>
        <span class="tag">Research</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Cursor Cloud Agents 2 Arabic: وكلاء برمجة في السحابة — ميزات، إصلاحات، وطلبات دمج!</h2>
      <p class="article-lead">«فريقي في الدوحة والعميل في لندن — أريد ميزة تسجيل بالعربية قبل نهاية الأسبوع دون سهر ليلي». في 14 نوفمبر 2026، أطلقت <strong>Cursor</strong> <strong>Cloud Agents 2 Arabic</strong>: وكلاء يعملون على مستودعك في بيئة معزولة، يفهمون تعليقات المشروع بالعربية والإنجليزية، يُنفّذون مهام من GitHub Issues وSlack وLinear، يُنشئون فرعًا واختبارات وطلب دمج، يُرسلون ملخصًا بالعربية لصاحب القرار — للشركات الناشئة ووكالات التطوير وفرق المنتج في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يحتاج مراقبة دائمة؛ الإصدار 2 يُضيف بوابات جودة قبل الدمج، يُقارن مع معايير الكود الداخلية، يُحدّ من نطاق الملفات، يُدمج مع CI، يُدعم متغيرات بيئة آمنة، ولوحة مراقبة عربية للمدير التقني.</p>
      <p>القدرات الأساسية: Arabic task specs؛ تكامل GitHub وGitLab؛ سياسات أمان للبنوك؛ حدود تكلفة لكل sprint؛ برنامج «Cloud Agents Partner MENA».</p>
      <p>للمبدعين العرب: استوديو تطوير موزّع — «sprint وكيل أسبوعي لثلاثة عملاء». من يُدير 6 شركات بـ1800–12000 دولار/شهر + onboarding 900–5500 دولار يبيع سرعة تسليم دون تضخم الفريق.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cursor Cloud Agents 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد وكلاء سحابة (سياسات، CI، تدريب):</strong> 4–12 يومًا — 900–5500 دولار/عميل.</li>
          <li><strong>إدارة sprint وكلاء شهرية:</strong> — 1800–12000 دولار/شهر.</li>
          <li><strong>حزم أمان وامتثال (مراجعة، سجلات):</strong> — 70–295 دولار/حزمة.</li>
          <li><strong>دورات «تشغيل Cloud Agents للفرق العربية»:</strong> — 52–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cursor</span>
        <span class="tag">Cloud Agents</span>
        <span class="tag">DevOps</span>
        <span class="tag">GitHub</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Runway Gen-4 Director Arabic: إخراج فيديو بالذكاء الاصطناعي — سكربت عربي، لقطات، وموسيقى!</h2>
      <p class="article-lead">«العميل يريد إعلانًا لمنتج عطور بنبرة خليجية راقية — والميزانية لا تكفي طاقم تصوير». في 14 نوفمبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Director Arabic</strong>: وضع إخراج يقرأ سكربتك بالعربية، يُقسّم المشهد إلى لقطات، يُولّد صورًا وفيديو متسقًا للشخصيات، يُضبط الإضاءة والحجم، يُقترح موسيقى خالية من حقوق، يُصدّر بصيغ إعلانات Meta وTikTok وYouTube — للوكالات والمؤثرين وعلامات التجزئة.</p>
      <p>المشكلة التي حلّتها: أدوات الفيديو السابقة كانت تُشوّه الحروف في اللوحات النصية؛ Director يُولّد نصًا عربيًا صحيحًا على الشاشة، يحفظ هوية الوجه عبر اللقطات، يُمكّن مراجعة كل مشهد قبل التصدير، يدعم safe zones للهواتف، وAPI للوكالات الكبيرة.</p>
      <p>القدرات الأساسية: Arabic storyboard؛ مكتبة أنماط إعلانية MENA؛ تصدير 4K؛ علامة مائية للمراجعة الداخلية؛ شريك «Runway Director MENA».</p>
      <p>للمبدعين العرب: استوديو إعلانات سريع — «حملة 3 فيديوهات عربية في 5 أيام». من يُسلّم 5 حملات/ربع بـ2200–18000 دولار + retainer 650–4200 دولار/شهر يفتح سوقًا ضخمًا للعلامات التي تتخلف عن الفيديو.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Director Arabic؟</h3>
        <ul>
          <li><strong>إنتاج حملة فيديو (سكربت، لقطات، مراجعة، تصدير):</strong> 5–14 يومًا — 2200–18000 دولار/حملة.</li>
          <li><strong>اشتراك استوديو شهري (حصة دقائق + مراجعات):</strong> — 650–4200 دولار/شهر.</li>
          <li><strong>حزم قطاعية (عطور، عقارات، تعليم):</strong> — 58–240 دولار/حزمة.</li>
          <li><strong>دورات «إخراج فيديو عربي مع Gen-4 Director»:</strong> — 48–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video</span>
        <span class="tag">Advertising</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>HubSpot Breeze Copilot 3 Arabic: مبيعات وتسويق بالعربية — رسائل، تنبؤات، وخط أنابيب!</h2>
      <p class="article-lead">«فريق المبيعات يكتب رسائل مختلفة لنفس العميل — والإغلاق يتأخر». في 14 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze Copilot 3 Arabic</strong>: مساعد داخل CRM يُقترح رسائل بريد وواتساب بالفصحى أو لهجة الخليج حسب ملف العميل، يُقدّر احتمال الإغلاق، يُلخّص المكالمات بالعربية، يُولّد عروض أسعار من قوالب معتمدة، يُنبّه عند تأخر المتابعة — لشركات B2B وخدمات ومكاتب عقارية في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُترجم حرفيًا من الإنجليزية؛ الإصدار 3 يُفهم ألقابًا عربية ومواسم رمضان والعيد، يُزامن مع Marketing Hub، يحترم GDPR وقوانين الخصوصية المحلية، يُدمج مع LinkedIn Sales Navigator، ويُوفّر تقارير أداء بالعربية للمديرين.</p>
      <p>القدرات الأساسية: Arabic outreach sequences؛ تكامل WhatsApp Business؛ قوالب عقود وعروض RTL؛ تدريب داخلي للفرق؛ برنامج «Breeze Partner MENA».</p>
      <p>للمبدعين العرب: وكالة نمو — «Breeze Copilot كمدير مبيعات افتراضي لـ10 شركات». من يُدير 10 حسابات بـ380–2600 دولار/شهر + إعداد 500–3500 دولار يبيع انضباطًا في خط الأنابيب دون توظيف قائد مبيعات إضافي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Breeze (CRM، تسلسلات، تدريب مبيعات):</strong> 3–10 أيام — 500–3500 دولار/عميل.</li>
          <li><strong>إدارة خط أنابيب ورسائل شهرية:</strong> — 380–2600 دولار/شهر.</li>
          <li><strong>حزم مواسم (رمضان، معارض، نهاية سنة):</strong> — 42–175 دولار/حزمة.</li>
          <li><strong>دورات «مبيعات عربية ذكية مع HubSpot Breeze»:</strong> — 40–170 دولار.</li>
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

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 14-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="14-11-2026 -- 04-PM.html">
          📰 14 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "14-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/14-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/14-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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