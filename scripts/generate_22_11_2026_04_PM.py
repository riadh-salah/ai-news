#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 22-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "22-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Einstein Copilot 3 Arabic · Wix ADI 4 Arabic · "
    "Dropbox Dash 2 Arabic · Pendo AI Guides 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Einstein Copilot 3 Arabic، Wix ADI 4 Arabic، Dropbox Dash 2 Arabic، Pendo AI Guides 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 22 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Salesforce Einstein Copilot 3 Arabic الذي يُحوّل سؤالك بالعربية إلى صفقة محدّثة ورسالة متابعة قبل أن تُغلق نافذة المبيعات، إلى Wix ADI 4 Arabic الذي يُطلق موقعًا ومتجرًا وحملة بريد من فقرة بالفصحى بينما تغرب الشمس، ومن Dropbox Dash 2 Arabic الذي يجيب «أين العقد ومن وافق؟» عبر كل ملفاتك في ثوانٍ، إلى Pendo AI Guides 3 Arabic الذي يُعلّم مستخدمي منتجك الرقمي خطوة بخطوة بلهجة يفهمها عميلك الخليجي أو المصري — أربع قصص مسائية في 22 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساء التحوّل الرقمي: المبيعات تتحدث عربيًا داخل الـCRM، المواقع تُبنى بالذكاء دون أسابيع تصميم، المعرفة المؤسسية تُصبح بحثًا بجملة واحدة، وتجربة المنتج تتحول إلى مدرّب ذكي يُقلّل الانسحاب. أربع أخبار عالمية وصندوق ذهبي لكل منها — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 22 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Einstein Copilot 3 Arabic: مساعد مبيعات وخدمة داخل Salesforce — أوامر عربية، صفقات، وتقارير فورية</h2>
      <p class="article-lead">«المدير يريد تقريرًا عن الصفقات المتأخرة بالعربية، والفريق يضيع ساعة في التصفية والنسخ». في 22 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Einstein Copilot 3 Arabic</strong>: مساعد ذكاء داخل Sales Cloud وService Cloud يفهم الفصحى واللهجات التجارية الشائعة، يُجيب أسئلة عن البيانات الحية، يُحدّث السجلات ويُنشئ مهامًا بأمر واحد، يُولّد رسائل بريد ومقترحات أسعار بنبرة العلامة، يُلخّص سلاسل البريد والمكالمات، يقترح الخطوة التالية لكل صفقة، يشرح لماذا تراجعت احتمالية الإغلاق، ويتكامل مع Slack وWhatsApp Business وMarketing Cloud — للوكالات وفرق المؤسسات في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُنتج جملًا رسمية جافة أو يخلط بين اللهجات؛ الإصدار 3 يدعم قوالب قطاعية للعقار والتأمين والتقنية والتجزئة، يحترم حقول الامتثال المحلية، يُنشئ تقارير إدارية أسبوعية بالفصحى، تدفقات موافقة داخلية، تكاملًا مع Tableau للرسوم، سجل تدقيق للاستعلامات الحساسة، وبرنامج «Salesforce MENA AI Partners» للمستشارين المعتمدين.</p>
      <p>القدرات الأساسية: استعلام عربي عن CRM؛ تحديث سجلات ومهام؛ محتوى مبيعات RTL؛ تلخيص تفاعلات؛ تنبؤات صفقات.</p>
      <p>للمبدعين العرب: استوديو «مبيعات مدعومة بالذكاء» — من يُفعّل Einstein Copilot على عملية كاملة من الاكتشاف حتى الإغلاق بـ2300–12500 دولار للمشروع + 480–2350 دولار/شهر للتحسين يخدم شركات B2B التي تريد مندوبي مبيعات أسرع دون توظيف محللي بيانات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Einstein Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وتفعيل مسارات مبيعات وخدمة ذكية (حقول، أتمتة، تدريب):</strong> 9–20 يومًا — 2300–12500 دولار.</li>
          <li><strong>تحسين دقة الاستعلامات والمحتوى شهريًا:</strong> — 480–2350 دولار/عميل/شهر.</li>
          <li><strong>حزمة 25 قالب بريد وتقرير إداري عربي:</strong> — 195–780 دولار.</li>
          <li><strong>ورش «مبيعات ذكية داخل Salesforce بالعربية»:</strong> — 58–232 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Einstein</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Wix ADI 4 Arabic: مصمم المواقع الذكي — من فكرة عربية إلى موقع ومتجر وحملة في ساعات</h2>
      <p class="article-lead">«نحتاج موقعًا للمطعم وقائمة طعام وصفحة حجز — والميزانية لا تسمح بوكالة كاملة». في 22 نوفمبر 2026، أطلقت <strong>Wix</strong> <strong>ADI 4 Arabic</strong> (Artificial Design Intelligence): محرك داخل Wix يقرأ وصفًا بالفصحى أو اللهجات الشائعة في الأعمال المحلية، يُولّد هيكل موقعًا كاملًا RTL، يختار ألوانًا وخطوطًا مناسبة للقطاع، يكتب نصوصًا تسويقية مقنعة، يُعدّ نماذج تواصل وحجز ودفع، يربط متجر Wix بمنتجات وشحن محلي، يُنشئ حملة بريد ترحيبية، يُحسّن العناوين لمحركات البحث العربية، ويقترح تعديلات بعد أول أسبوع من الزيارات — للمطاعم والعيادات والمدربين والمتاجر الصغيرة في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: ADI 3 كان يتجاهل المناسبات المحلية وصياغات الخصوصية؛ الإصدار 4 يدعم تقويماً للعروض الموسمية، نصوص امتثال لسياسات الإعلان المحلية، تكامل مع بوابات الدفع الإقليمية، استيرادًا من Instagram وTikTok لمعارض المنتجات، وضع «علامات متعددة» لامتداد إقليمي، وبرنامج «Wix Partners AI Arabia» للمنفذين المحليين.</p>
      <p>القدرات الأساسية: موقع RTL من وصف؛ نصوص تسويقية؛ متجر ودفع؛ بريد ترحيبي؛ تحسين محركات بحث عربي.</p>
      <p>للمبدعين العرب: خدمة «حضور رقمي في 48 ساعة» — من يُسلّم موقعًا ADI مُهيّأ مع تدريب العميل بـ900–4200 دولار يجذب أصحاب المشاريع الذين يريدون إطلاقًا سريعًا قبل نهاية الأسبوع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Wix ADI 4 Arabic؟</h3>
        <ul>
          <li><strong>إطلاق موقع أو متجر ذكي (هيكلة، محتوى، تدريب):</strong> 2–7 أيام — 900–4200 دولار.</li>
          <li><strong>صيانة محتوى وحملات وتحسين زيارات شهريًا:</strong> — 280–1280 دولار/موقع/شهر.</li>
          <li><strong>حزمة 5 صفحات هبوط عربية لقطاع واحد:</strong> — 120–480 دولار.</li>
          <li><strong>دورات «مواقع أعمال عربية مع Wix ADI»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Wix</span>
        <span class="tag">Web</span>
        <span class="tag">SMB</span>
        <span class="tag">Design</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Dropbox Dash 2 Arabic: بحث مؤسسي عبر كل ملفاتك — سؤال عربي وإجابة من Slack وDrive وNotion</h2>
      <p class="article-lead">«أين العرض الذي أرسلناه للعميل قبل شهرين؟ بحثت في البريد والمجلدات المشتركة — ولا أحد يتذكر اسم الملف». في 22 نوفمبر 2026، أطلقت <strong>Dropbox</strong> <strong>Dash 2 Arabic</strong>: مساعد بحث مؤسسي يفهم أسئلتك بالعربية، يفهرس Dropbox وGoogle Drive وMicrosoft 365 وSlack وNotion وJira عند التفعيل، يُرجع المستند الصحيح مع مقتطف مترجم أو بالأصل، يُلخّص العقود والعروض الطويلة، يُجيب «من وافق على…؟» و«ما آخر نسخة…؟»، يقترح ملفات مرتبطة بالمشروع، يحترم صلاحيات كل مستخدم، ويدعم فرقًا موزعة بين دبي والرياض والقاهرة — للقانونية والمالية والاستشارات والهندسة.</p>
      <p>المشكلة التي حلّتها: Dash الأول كان يُرجع نتائج إنجليزية رغم سؤال عربي أو يتجاهل المرفقات الممسوحة ضوئيًا؛ الإصدار 2 يدعم OCR عربي محسّنًا، أسماء ملفات ومشاريع بالعربية، قوالب «عروض أسعار» و«عقود» و«سياسات»، تنبيهات عند تضارب إصدارات، تكاملًا مع Dropbox Sign لتتبع التوقيع، وسجل تدقيق للبحث في البيانات الحساسة.</p>
      <p>القدرات الأساسية: بحث موحّد عربي؛ تلخيص مستندات؛ تتبع إصدارات؛ امتثال صلاحيات؛ تكامل أدوات العمل.</p>
      <p>للمبدعين العرب: مشروع «مكتب بلا فوضى ملفات» — من يربط مصادر البيانات ويُدرّب الفريق على Dash لـ150–800 مستخدم بـ2800–14200 دولار + 520–2480 دولار/شهر للحوكمة يبيع لجهات تخسر ساعات يوميًا في البحث اليدوي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dropbox Dash 2 Arabic؟</h3>
        <ul>
          <li><strong>ربط مصادر وتفعيل بحث ذكي (فهرسة، سياسات، تدريب):</strong> 10–24 يومًا — 2800–14200 دولار.</li>
          <li><strong>حوكمة فهرسة وتحسين دقة الاستعلامات شهريًا:</strong> — 520–2480 دولار/مؤسسة/شهر.</li>
          <li><strong>دليل تشغيل عربي + 40 استعلامًا جاهزًا للقطاعات:</strong> — 165–660 دولار.</li>
          <li><strong>ورش «إنتاجية المعرفة مع Dropbox Dash بالعربية»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dropbox</span>
        <span class="tag">Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Pendo AI Guides 3 Arabic: مرشد ذكي داخل منتجك الرقمي — يُقلّل الانسحاب ويُسرّع التبنّي</h2>
      <p class="article-lead">«ثمانون بالمئة من المستخدمين الجدد لا يصلون للميزة الأساسية — وفريق الدعم يكرّر نفس الشرح في كل مكالمة». في 22 نوفمبر 2026، أطلقت <strong>Pendo</strong> <strong>AI Guides 3 Arabic</strong>: طبقة داخل تطبيقات الويب والجوال تُولّد جولات تفاعلية ونصائح سياقية بالفصحى واللهجات الشائعة في البرمجيات، تتعلم من سلوك المستخدم أين يتعثر، تُقترح خطوات إصلاح فورية، تُنشئ محتوى مساعدة من تذاكر الدعم المتكررة، تُقسّم الرسائل حسب الدور والقطاع، تقيس تأثير كل دليل على التفعيل والاحتفاظ، وتتكامل مع Intercom وZendesk وProduct analytics — لشركات SaaS والبنوك الرقمية والتعليم الإلكتروني في المنطقة.</p>
      <p>المشكلة التي حلّتها: Guides 2 كانت تتطلب كتابة يدوية طويلة ولا تتكيف مع تحديثات الواجهة؛ الإصدار 3 يُولّد مسارات من فيديو شاشة أو وثائق موجودة، يكتشف تغييرات الواجهة ويقترح تحديث النصوص، يدعم وضع الامتثال للقطاعات المنظمة، اختبارات A/B للرسائل العربية، تكاملًا مع مراكز التدريب الداخلية، وبرنامج «Pendo Partners MENA» للوكالات المتخصصة في نجاح العملاء.</p>
      <p>القدرات الأساسية: جولات عربية داخل المنتج؛ نصائح سياقية؛ تحليل انسحاب؛ مساعدة من تذاكر الدعم؛ قياس التفعيل.</p>
      <p>للمبدعين العرب: استوديو «منتج يُعلّم نفسه» — من يُبني خريطة رحلة مستخدم + أدلة Pendo لمنتج SaaS بـ2100–11200 دولار للإطلاق + 450–2100 دولار/شهر للتحسين يخدم شركات تكافح مع تبنّي بطيء رغم استثمار تسويقي كبير.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Pendo AI Guides 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم رحلة مستخدم وأدلة ذكية (تحليل، محتوى، قياس):</strong> 8–18 يومًا — 2100–11200 دولار.</li>
          <li><strong>تحسين نصوص ومسارات شهريًا بعد إصدارات المنتج:</strong> — 450–2100 دولار/منتج/شهر.</li>
          <li><strong>حزمة 15 دليلًا تفاعليًا عربيًا لقطاع FinTech أو EdTech:</strong> — 175–700 دولار.</li>
          <li><strong>ورش «نجاح العملاء بالذكاء الاصطناعي مع Pendo»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Pendo</span>
        <span class="tag">Product</span>
        <span class="tag">SaaS</span>
        <span class="tag">Onboarding</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 22-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="22-11-2026 -- 04-PM.html">
          📰 22 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "22-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/22-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/22-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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