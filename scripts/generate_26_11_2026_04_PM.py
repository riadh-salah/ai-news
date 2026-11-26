#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "26-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "ServiceNow Now Assist 3 Arabic · Monday.com AI Blocks 2 Arabic · "
    "Freshdesk Freddy AI 3 Arabic · Zoho CRM Zia 4 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — ServiceNow Now Assist 3 Arabic، Monday.com AI Blocks 2 Arabic، Freshdesk Freddy AI 3 Arabic، Zoho CRM Zia 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من ServiceNow Now Assist 3 Arabic الذي يُغلق تذكرة IT ويُرسل للموظف تعليمات إصلاح بالفصحى قبل أن يصل المدير للمكتب، إلى Monday.com AI Blocks 2 Arabic الذي يُحوّل جملة عربية واحدة إلى لوحة مشروع كاملة بمهام ومواعيد وألوان وتنبيهات، ومن Freshdesk Freddy AI 3 Arabic الذي يُجيب عميلك على واتساب والبريد في نفس السياق دون تكرار القصة، إلى Zoho CRM Zia 4 Arabic الذي يُنبّهك بأنّ صفقة كبرى على وشك البرد ويُقترح رسالة إقناع باللهجة المناسبة — أربع قصص مسائية في 26 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء ساعة الغروب!</h1>
      <p class="hero-sub">مساء العمليات والمشاريع والدعم والمبيعات: الأنظمة تُصلَح، الفرق تُنظَّم، العملاء يُطمئَنون، والصفقات تُنقَذ. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 26 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>ServiceNow Now Assist 3 Arabic: خدمة ذكية تتكلّم مع موظفيك — حلول IT وHR بالعربية في ثوانٍ!</h2>
      <p class="article-lead">«مئات طلبات الدعم الداخلية مفتوحة — والموظف لا يفهم التعليمات الإنجليزية ويتصل بالمساعد الشخصي للمدير». في 26 نوفمبر 2026، أطلقت <strong>ServiceNow</strong> <strong>ServiceNow Now Assist 3 Arabic</strong>: مساعد مؤسسي يعمل داخل منصة Now، يقرأ قواعد المعرفة وسياسات الشركة، يُجيب عن إجازات ورواتب وأعطال أجهزة بالفصحى أو بنبرة خليجية رسمية، يُنفّذ طلبات قياسية (إعادة تعيين كلمة مرور، حجز معدات، فتح تذكرة صيانة)، يُلخّص حالة طلبك عند التصعيد، يتكامل مع Microsoft Teams وSlack وEmployee Center، يحترم الصلاحيات والامتثال المحلي، ويُرسل «ملخص مساء العمليات» لقائد IT — للجهات الحكومية والبنوك والاتصالات والتعليم 500–30 ألف موظف في السعودية والإمارات ومصر.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يترجم مقالات المساعدة حرفيًا؛ الإصدار 3 يفهم المصطلحات الداخلية العربية، يدعم لهجات متعددة في واجهة موحدة، يُقترح حلولًا قبل فتح تذكرة جديدة، يُنبّه عند تعارض سياسة مع إجابة، يُولّد توثيقًا تلقائيًا لتغييرات الإجراءات، مسار اعتماد بشري للطلبات الحساسة، وبرنامج «ServiceNow MENA Partners» لتنفيذ مراكز خدمة بالعربية.</p>
      <p>القدرات الأساسية: إجابات HR وIT عربية؛ تنفيذ طلبات؛ تلخيص تصعيد؛ تكامل Teams؛ تقارير مسائية للعمليات.</p>
      <p>للمبدعين العرب: استشارات «مركز خدمة يفهم العربية» — من يُفعّل Now Assist لمؤسسة 800–12 ألف موظف بـ2100–13800 دولار للإعداد + 560–2140 دولار/شهر للتحسين يخدم قطاعات تغرق في الطلبات الداخلية بلغة غير مألوفة للموظف.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ServiceNow Now Assist 3 Arabic؟</h3>
        <ul>
          <li><strong>هيكلة قاعدة معرفة + تدفقات + اختبار اللهجات:</strong> 12–22 يومًا — 2100–13800 دولار.</li>
          <li><strong>مراقبة محادثات وتحسين سياسات شهريًا:</strong> — 560–2140 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 إجراءً جاهزًا (إجازة، عهدة، صيانة، وصول):</strong> — 92–368 دولار/حزمة.</li>
          <li><strong>ورش «خدمة موظف ذكية بالعربية مع ServiceNow»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ServiceNow</span>
        <span class="tag">ITSM</span>
        <span class="tag">HR</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Monday.com AI Blocks 2 Arabic: من فكرة إلى لوحة — مشروع كامل بجملة واحدة بالعربية!</h2>
      <p class="article-lead">«العميل يريد حملة إطلاق منتج خلال أسبوعين — والفريق يقضي يومين فقط في إنشاء الأعمدة والمهام على Monday». في 26 نوفمبر 2026، أطلقت <strong>monday.com</strong> <strong>Monday.com AI Blocks 2 Arabic</strong>: كتل ذكاء مدمجة في Work OS تفهم وصفك بالعربية، تُبني لوحة مشروع بأعمدة الحالة والمسؤول والموعد والأولوية، تُولّد قائمة مهام منطقية (تصميم، محتوى، إعلانات، QA)، تُقترح أتمتة (إشعار عند التأخير، نقل بطاقة عند الموافقة)، تُنسّق ألوانًا ووسومًا للفرق المختلطة، تتكامل مع Gmail وSlack وZoom وMake، يدعم RTL في أسماء المجموعات، ويُصدّر «نشرة تقدم مسائية» للمدير — للوكالات والشركات الناشئة والمؤسسات 15–500 عضو في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يخلط التواريخ الهجرية والميلادية بلا وعي؛ الإصدار 2 يحترم تقويم الفريق، يدعم قوالب «حملة تسويق» و«تطوير منتج» و«فعالية» بالعربية، يُنبّه عند تعارض موارد، يُحوّل صوتًا عربيًا إلى مخطط مهام، مسار شريك للوكالات التي تدير عشرات اللوحات لعملاء، وتدريب Monday Partner MENA على AI Blocks.</p>
      <p>القدرات الأساسية: لوحة من جملة؛ مهام وأتمتة؛ قوالب عربية؛ تقارير مسائية؛ تكامل بريد ومحادثات.</p>
      <p>للمبدعين العرب: استوديو «Monday بالعربية لعميلك» — من يُدير AI Blocks لـ10 عملاء (لوحتان نشطتان لكل عميل) بـ980–7200 دولار إعدادًا + 240–980 دولار/شهر لكل عميل يبني دخلًا متكررًا مع فرق تضيع وقتهم في الإعداد لا التنفيذ.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Monday.com AI Blocks 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم قوالب صناعة + أتمتة + تدريب الفريق:</strong> 4–9 أيام — 980–7200 دولار/عميل.</li>
          <li><strong>صيانة لوحات وتحسين تدفقات شهريًا:</strong> — 240–980 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب لوحة (وكالة، متجر، تطبيق، حدث):</strong> — 76–304 دولار/حزمة.</li>
          <li><strong>ورش «إدارة مشاريع ذكية بالعربية مع Monday»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Monday.com</span>
        <span class="tag">Project</span>
        <span class="tag">Workflow</span>
        <span class="tag">Agencies</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Freshdesk Freddy AI 3 Arabic: مساعد دعم يذكر كل شيء — واتساب وبريد وتذكرة في سياق واحد!</h2>
      <p class="article-lead">«العميل كتب على واتساب صباحًا والبريد ظهرًا — والوكيل أعاد السؤال نفسه ثلاث مرات وخسر ثقة العلامة». في 26 نوفمبر 2026، أطلقت <strong>Freshworks</strong> <strong>Freshdesk Freddy AI 3 Arabic</strong>: محرك دعم متعدد القنوات يجمع المحادثات في ملف عميل واحد، يُجيب بالفصحى أو باللهجة المصرية أو الشامية حسب إعداداتك، يُنفّذ إجراءات (تتبع شحنة، تجديد اشتراك، استرداد جزئي)، يُصعّد للبشر مع تاريخ كامل بالعربية، يتكامل مع Shopify وWooCommerce وStripe، يُقيس CSAT بعد كل جلسة، يُولّد «تقرير أسئلة المساء المتكررة»، ويُدرب نفسه على macros محسّنة — لشركات SaaS وتجارة وتعليم واتصالات 500–200 ألف تذكرة شهريًا.</p>
      <p>المشكلة التي حلّتها: Freddy 2 كان يفصل القنوات؛ الإصدار 3 يفهم النية عبر اللغات، يحترم ساعات الدعم المحلية، يُنبّه عند إجابة قد تُخالف ضمانًا أو قانون استهلاك، يدعم ردود صوتية قصيرة للعملاء كبار السن، مسار تدريب للفرق على تحسين المحتوى العربي، وبرنامج شركاء «Freshdesk Arabic CX» للوكالات في الخليج وشمال أفريقيا.</p>
      <p>القدرات الأساسية: سياق موحّد؛ إجراءات تلقائية؛ لهجات متعددة؛ تكامل تجارة؛ تقارير نوايا مسائية.</p>
      <p>للمبدعين العرب: خدمة «دعم عربي بلا تكرار» — من يُفعّل Freddy 3 لشركة 5 آلاف–60 ألف تذكرة شهريًا بـ1480–10200 دولار + 360–1480 دولار/شهر للمراقبة يخدم علامات تخسر عملاء بسبب تجربة دعم مجزأة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Freshdesk Freddy AI 3 Arabic؟</h3>
        <ul>
          <li><strong>ربط قنوات + قاعدة معرفة + اختبار لهجات:</strong> 6–14 يومًا — 1480–10200 دولار.</li>
          <li><strong>مراجعة تذاكر وتحسين macros شهريًا:</strong> — 360–1480 دولار/عميل/شهر.</li>
          <li><strong>حزمة 35 ردًا جاهزًا (شحن، فاتورة، اشتراك، ضمان) بالعربية:</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «تجربة عميل ذكية بالعربية مع Freshdesk»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Freshdesk</span>
        <span class="tag">Freddy</span>
        <span class="tag">Support</span>
        <span class="tag">Omnichannel</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zoho CRM Zia 4 Arabic: مندوب مبيعات خفي — ينبّهك قبل أن تبرد الصفقة ويكتب الرسالة المناسبة!</h2>
      <p class="article-lead">«صفقة بقيمة 180 ألف ريال لم تُتابَع منذ أسبوع — وزملاؤك ينتظرون تقريرًا يدويًا لا يصل». في 26 نوفمبر 2026، أطلقت <strong>Zoho</strong> <strong>Zoho CRM Zia 4 Arabic</strong>: مساعد مبيعات داخل Zoho CRM يحلل سجل المكالمات والبريد والاجتماعات، يُصنّف نوايا العملاء، يُنبّه بصفقات «معرضة للفقدان» مع سبب واضح بالعربية، يُقترح رسالة متابعة بنبرة مهنية مناسبة للخليج أو لمصر، يُلخّص مكالمة طويلة لخمس نقاط، يتنبأ بإغلاق محتمل ويوصي بالخصم أو العرض التالي، يتكامل مع Zoho Books وCampaigns وSign، يدعم واتساب Business API، ويُرسل «نشرة صفقات المساء» للمدير — لشركات B2B وتوزيع وعقارات وتعليم 20–800 مندوب في MENA.</p>
      <p>المشكلة التي حلّتها: Zia 3 كان يكتب إنجليزية ثم يترجم؛ الإصدار 4 يولّد عربية أصلية، يفهم مصطلحات «عقد إطار» و«دفعة مقدمة» و«فترة ضمان»، يُحترم قواعد الخصم الداخلية قبل اقتراح تخفيض، يُولّد تقريرًا صوتيًا قصيرًا للمدير المسافر، مسار موافقة بشرية قبل إرسال عروض حساسة، وبرنامج «Zoho Partners Arabic Revenue» للمستشارين.</p>
      <p>القدرات الأساسية: تنبيه صفقات؛ رسائل متابعة؛ تلخيص مكالمات؛ تنبؤ إغلاق؛ تكامل Zoho Suite.</p>
      <p>للمبدعين العرب: حزمة «CRM يتكلّم عربيًا» — من يُفعّل Zia 4 لشركة 40–350 مندوبًا بـ1320–9200 دولار + 310–1260 دولار/شهر للضبط يخدم قيادات تخسر إيرادًا بسبب بطء المتابعة والرسائل غير المناسبة ثقافيًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoho CRM Zia 4 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Zia + قوالب صناعة + تدريب المبيعات:</strong> 7–13 يومًا — 1320–9200 دولار.</li>
          <li><strong>مراجعة تنبيهات وتحسين نبرة شهريًا:</strong> — 310–1260 دولار/عميل/شهر.</li>
          <li><strong>حزمة 18 رسالة متابعة عربية (B2B، خدمات، توزيع):</strong> — 74–296 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات ذكية بالعربية مع Zoho Zia»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zoho</span>
        <span class="tag">CRM</span>
        <span class="tag">Zia</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="26-11-2026 -- 04-PM.html">
          📰 26 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "26-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/26-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/26-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
        "dolار",
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