#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "26-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Agentforce 2 Arabic · Zendesk AI Agents 3 Arabic · "
    "Shopify Sidekick 3 Arabic · Atlassian Rovo 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Agentforce 2 Arabic، Zendesk AI Agents 3 Arabic، Shopify Sidekick 3 Arabic، Atlassian Rovo 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Salesforce Agentforce 2 Arabic الذي يُغلق صفقة ويُرسل متابعة بالعربية قبل أن تبرد فنجان القهوة، إلى Zendesk AI Agents 3 Arabic الذي يُحل تذكرة الدعم الصباحية من أول رد بلهجة العميل، ومن Shopify Sidekick 3 Arabic الذي يُقترح وصف منتج وعرضًا ترويجيًا وردًا على مراجعة سلبية في متجرك خلال دقائق، إلى Atlassian Rovo 2 Arabic الذي يُلخّص المشروع ويبحث في Confluence وJira ويُعدّك لاجتماع الفريق من داخل Slack — أربع قصص صباحية في 26 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباح المبيعات والدعم والتجارة والإنتاجية: الصفقات تُغلق، التذاكر تُحلّ، المتاجر تُنمو، والفرق تعرف ماذا تفعل اليوم. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 26 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Agentforce 2 Arabic: وكلاء مبيعات يعملون لك — متابعة، عروض، وإغلاق بالفصحى!</h2>
      <p class="article-lead">«لديك 200 فرصة مفتوحة — والمتابعة العربية تتأخر أسبوعًا والعميل يذهب للمنافس». في 26 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Salesforce Agentforce 2 Arabic</strong>: وكلاء ذكيون داخل Sales Cloud يقرأون سجل CRM والبريد والمكالمات، يُرسلون رسائل متابعة بالفصحى أو بنبرة خليجية مهنية، يُلخّصون الاجتماع الأخير لمدير المبيعات، يُقترحون الخطوة التالية (عرض، تجربة، تخفيض محدود)، يتكاملون مع Einstein وSlack وWhatsApp Business، يحترمون ساعات العمل والعطل المحلية، ويُبلّغونك بثلاث فرص «ستموت اليوم» دون اتصال — لشركات B2B وتوزيع وتقنية 30–500 مندوب في السعودية والإمارات ومصر وقطر.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يكتب إنجليزيًا ثم يُترجم حرفيًا؛ الإصدار 2 يفهم مصطلحات مبيعات عربية («عرض سعر»، «مدة تجربة»، «شروط الدفع»)، يدعم قوالب صناعات (عقارات، SaaS، لوجستيات)، يُنبّه عند وعود غير منسقة مع السياسة، يُولّد ملخصًا صوتيًا قصيرًا للمدير بالعربية، مسار موافقة بشرية قبل إرسال عروض حساسة، وبرنامج شريك «Agentforce MENA» للمستشارين الذين يبيعون أتمتة CRM.</p>
      <p>القدرات الأساسية: متابعة عربية؛ تلخيص اجتماعات؛ اقتراح خطوات؛ تكامل Slack وWhatsApp؛ تقارير فرص حرجة.</p>
      <p>للمبدعين العرب: خدمة «مبيعات صباحية لا تتأخر» — من يُفعّل Agentforce لشركة 50–300 مندوبًا بـ1890–12400 دولار للإعداد + 520–1980 دولار/شهر للتحسين يخدم قيادات تخسر صفقات بسبب بطء المتابعة بالعربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد وكلاء + قوالب صناعة + تدريب فريق المبيعات:</strong> 10–18 يومًا — 1890–12400 دولار.</li>
          <li><strong>مراجعة محادثات وتحسين نبرة شهريًا:</strong> — 520–1980 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 رسالة متابعة عربية جاهزة (B2B، تجزئة، خدمات):</strong> — 98–392 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات ذكية بالعربية مع Agentforce»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Zendesk AI Agents 3 Arabic: دعم بلا طوابير — حل التذكرة من أول رد بلهجة العميل!</h2>
      <p class="article-lead">«صباح الاثنين: 400 تذكرة مفتوحة — والعميل العربي ينتظر ساعتين لرد بسيط». في 26 نوفمبر 2026، أطلقت <strong>Zendesk</strong> <strong>Zendesk AI Agents 3 Arabic</strong>: وكلاء دعم متعدد القنوات يقرأون مركز المساعدة وسياساتك، يُجيبون بالفصحى أو باللهجة المصرية أو الخليجية حسب إعدادات العلامة، يُنفّذون إجراءات (إعادة تعيين كلمة مرور، تحديث عنوان، استرداد)، يُصعّدون للبشر مع ملخص عربي كامل، يتكاملون مع Shopify وStripe وSunshine Conversations، يُقيسون الرضا بعد كل جلسة، ويُولّدون تقرير «أسئلة الصباح المتكررة» للمدير — لاشتراكات وتجارة إلكترونية واتصالات وتعليم رقمي في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُكرر مقالات المساعدة؛ الإصدار 3 يفهم النية قبل النص، يحترم GDPR والاحتفاظ بالبيانات حيث يُطبَّق، يدعم واتساب وMessenger والبريد في سياق واحد، يُنبّه عند إجابة قد تُسبب نزاعًا قانونيًا، مسار تدريب للفرق على تحسين macros عربية، وبرنامج «Zendesk Partners Arabic CX» للوكالات.</p>
      <p>القدرات الأساسية: إجابات متعددة اللهجات؛ إجراءات تلقائية؛ تصعيد ذكي؛ تكامل تجارة؛ تقارير نوايا صباحية.</p>
      <p>للمبدعين العرب: خدمة «صباح بلا طابور تذاكر» — من يُفعّل AI Agents لشركة 3 آلاف–80 ألف تذكرة شهريًا بـ1620–10800 دولار + 380–1560 دولار/شهر للمراقبة يخدم فرق دعم تغمرها الاستفسارات العربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zendesk AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء قاعدة معرفة + تدفقات + اختبار اللهجات:</strong> 7–15 يومًا — 1620–10800 دولار.</li>
          <li><strong>مراجعة تذاكر وتحسين macros شهريًا:</strong> — 380–1560 دولار/عميل/شهر.</li>
          <li><strong>حزمة 30 ردًا جاهزًا (شحن، فوترة، اشتراك) بالعربية:</strong> — 84–336 دولار/حزمة.</li>
          <li><strong>ورش «تجربة عميل ذكية بالعربية مع Zendesk AI»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zendesk</span>
        <span class="tag">Support</span>
        <span class="tag">Ticketing</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Shopify Sidekick 3 Arabic: مساعد متجرك — أوصاف، عروض، وردود على المراجعات بالعربية!</h2>
      <p class="article-lead">«منتجك الجديد ممتاز — لكن الوصف الإنجليزي لا يُقنع الزائر العربي والمبيعات الصباحية ضعيفة». في 26 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Shopify Sidekick 3 Arabic</strong>: مساعد تاجر ذكي داخل لوحة التحكم يُحوّل نقاطًا مختصرة إلى أوصاف منتجات SEO بالفصحى أو بنبرة خليجية دافئة، يُقترح عناوين وصور alt نص عربي، يُصمّم كوبونات وعروض «صباحية» لرمضان والأعياد، يُكتب ردودًا مهنية على مراجعات سلبية، يُحلّل مبيعات الأمس ويُقترح ثلاث إجراءات اليوم، يتكامل مع Markets وTranslate &amp; Adapt وEmail، ويُصدّر تقريرًا صباحيًا للمالك — لتجار D2C وعلامات محلية ومتعدد الفروع في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يخلط العملات والدول في النصوص؛ الإصدار 3 يحترم سوق كل متجر (ريال، درهم، جنيه)، يدعم RTL في وصف المنتج، يُنبّه عند ادعاءات صحية أو قانونية حساسة، يُولّد نسخ A/B لوصف واحد، مسار شريك للوكالات التي تدير عشرات المتاجر، وتدريب Shopify Partner MENA على Sidekick.</p>
      <p>القدرات الأساسية: أوصاف عربية؛ عروض وكوبونات؛ ردود مراجعات؛ تحليل مبيعات؛ تقارير صباحية.</p>
      <p>للمبدعين العرب: استوديو «متجر يتكلم عربيًا» — من يُدير Sidekick لـ12 تاجرًا (40 منتجًا/شهر لكل متجر) بـ1180–8400 دولار للإعداد + 290–1180 دولار/شهر لكل عميل يبني دخلًا متكررًا مع تجار يخسرون مبيعات بسبب ضعف المحتوى المحلي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد نبرة المتجر + قوالب + تدريب التاجر:</strong> 5–11 يومًا — 1180–8400 دولار/عميل.</li>
          <li><strong>تحسين منتجات وعروض ومراجعات شهريًا:</strong> — 290–1180 دولار/عميل/شهر.</li>
          <li><strong>حزمة 25 وصف منتج عربي (موضة، إلكترونيات، عناية):</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «تجارة ذكية بالعربية مع Shopify Sidekick»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Retail</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Atlassian Rovo 2 Arabic: زميل فريق ذكي — بحث، تلخيص، واستعداد للاجتماع من Slack!</h2>
      <p class="article-lead">«اجتماع الساعة 9 — والفريق لم يقرأ آخر 40 تعليقًا في Jira والقرار يُؤجل أسبوعًا». في 26 نوفمبر 2026، أطلقت <strong>Atlassian</strong> <strong>Atlassian Rovo 2 Arabic</strong>: مساعد معرفي داخل Jira وConfluence وTrello وSlack يبحث عبر المشاريع بلغة طبيعية عربية، يُلخّص خيط تعليقات طويل إلى خمس نقاط تنفيذية، يُعدّ أجندة اجتماع من حالة المهام المفتوحة، يُقترح مالكًا لكل بند متأخر، يتكامل مع Microsoft Teams وGoogle Drive عند الحاجة، يحترم صلاحيات الوصول، ويُرسل «نشرة صباح الفريق» للقناة — لشركات تقنية واستشارية وإعلام رقمي 50–2000 موظف في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُرجع روابط بلا سياق؛ الإصدار 2 يُركّب إجابة من عدة صفحات، يدعم مصطلحات agile عربية («سبرينت»، «باك لوج»، «ستوري»)، يُنبّه عند تضارب تواريخ، يُولّد مسودة قرار للمدير بالفصحى، مسار تدريب IT على حوكمة Rovo، وبرنامج شريك للمستشارين الذين يبيعون «إنتاجية معرفية بالعربية».</p>
      <p>القدرات الأساسية: بحث عربي؛ تلخيص threads؛ أجندة اجتماع؛ نشرة صباحية؛ تكامل Slack وTeams.</p>
      <p>للمبدعين العرب: استشارات «اجتماع بلا فوضى» — من يُفعّل Rovo لمؤسسة 80–800 مستخدم بـ1560–10200 دولار + 410–1640 دولار/شهر للصيانة يخدم قادة فرق يغرقون في التوثيق ولا يجدون وقت القرار.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlassian Rovo 2 Arabic؟</h3>
        <ul>
          <li><strong>ربط مصادر + سياسات وصول + تدريب الفرق:</strong> 8–16 يومًا — 1560–10200 دولار.</li>
          <li><strong>ضبط تلخيصات ونشرات صباحية شهريًا:</strong> — 410–1640 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 قوالب أجندة اجتماع عربي (تقنية، تسويق، عمليات):</strong> — 68–272 دولار/حزمة.</li>
          <li><strong>ورش «إنتاجية فرق بالعربية مع Atlassian Rovo»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atlassian</span>
        <span class="tag">Rovo</span>
        <span class="tag">Productivity</span>
        <span class="tag">Jira</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="26-11-2026 -- 08-AM.html">
          📰 26 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "26-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/26-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/26-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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