#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 18-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "18-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Mistral Le Chat Enterprise 2 Arabic · Perplexity Pages 3 Arabic · "
    "Twilio AI Assistants 4 Arabic · Writer AI HQ 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Mistral Le Chat Enterprise 2 Arabic، Perplexity Pages 3 Arabic، Twilio AI Assistants 4 Arabic، Writer AI HQ 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 18 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Mistral Le Chat Enterprise 2 Arabic الذي يُجيب عن سياسات الامتثال الأوروبية ووثائقك الداخلية بالعربية مع استشهادات قبل أن ينام فريقك القانوني، إلى Perplexity Pages 3 Arabic الذي يُحوّل سؤالًا ليليًا عن السوق إلى تقرير بيع جاهز بالفصحى، ومن Twilio AI Assistants 4 Arabic الذي يُجيب مكالمات وواتساب بلهجة الخليج ويُحوّل المهتم إلى موعد، إلى Writer AI HQ 3 Arabic الذي يُصقل نبرة العلامة في كل رسالة بيع ودعم واتحادية — أربع قصص ليلية في 18 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ قبل شروق الشمس!</h1>
      <p class="hero-sub">ليلةٌ لرواد الأعمال والوكالات وفرق الدعم: المساعد يفهم العربية والامتثال، التقرير يُباع قبل الصباح، الصوت يُغلق الصفقات، والنبرة تبقى موحّدة عبر مئات الرسائل. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من اللحظة الأولى.</p>
      <div class="hero-meta">
        <span>📅 18 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Mistral Le Chat Enterprise 2 Arabic: مساعد مؤسسي أوروبي — بحث، وكلاء، وحوكمة بالعربية</h2>
      <p class="article-lead">«البنك يريد نموذجًا أوروبيًا يفهم العقود العربية ولا يُرسل بياناتنا خارج الاتحاد دون ضوابط». في 18 نوفمبر 2026، أطلقت <strong>Mistral</strong> <strong>Le Chat Enterprise 2 Arabic</strong>: منصة محادثة مؤسسية تفهم الفصحى ولهجات الخليج والمغرب العربي، تُفهرس مستندات داخل حدود الاستضافة الفرنسية، تُجيب مع اقتباسات صفحة، تُشغّل وكلاء مخصصين للموارد البشرية والمشتريات، تُطبّق سياسات عدم الاحتفاظ، وتتكامل مع Microsoft Teams وSlack وSharePoint — للبنوك والطيران والتعليم العالي في أوروبا والشرق الأوسط.</p>
      <p>المشكلة التي حلّتها: الإصدار المؤسسي الأول كان يخلط بين مصادر قديمة أو يُجيب بلهجة أوروبية باردة عند الموضوعات الحساسة؛ Enterprise 2 يدعم مصادر موثوقة متعددة، موافقات بشرية قبل الإجراءات الحساسة، ذاكرة محادثة منفصلة لكل فرق، قوالب «عقود وتوريد» و«استفسارات عملاء VIP» و«امتثال GDPR»، تدريبًا على مصطلحات قانونية عربية، وبرنامج شريك «Mistral Enterprise MENA».</p>
      <p>القدرات الأساسية: بحث مؤسسي بالعربية؛ وكلاء متخصصون؛ استشهادات واضحة؛ حوكمة بيانات أوروبية؛ تكامل فرق العمل.</p>
      <p>للمبدعين العرب: عرض «مساعد امتثال جاهز في 14 يومًا» — من يُنشر 3 حلول مؤسسية شهريًا بـ3500–22000 دولار للتسليم يبيع ثقة قانونية بلغة العميل دون بناء نموذج من الصفر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Mistral Le Chat Enterprise 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Le Chat Enterprise وفهرسة معرفة عربية:</strong> 8–18 يومًا — 3500–22000 دولار.</li>
          <li><strong>صيانة سياسات ومصادر ووكلاء شهريًا:</strong> — 780–3400 دولار/عميل/شهر.</li>
          <li><strong>قوالب وكلاء قطاعية (بنوك، طيران، تعليم):</strong> — 88–380 دولار/حزمة.</li>
          <li><strong>ورش «من GDPR إلى محادثة آمنة بالعربية»:</strong> — 58–232 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Mistral</span>
        <span class="tag">Le Chat</span>
        <span class="tag">Enterprise</span>
        <span class="tag">GDPR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Perplexity Pages 3 Arabic: من سؤال ليلي إلى تقرير مُبيع — مصادر، مخططات، وهوية علامة</h2>
      <p class="article-lead">«العميل يريد دراسة سوق عن منتج جديد غدًا صباحًا — ولا وقت لفريق الأبحاث». في 18 نوفمبر 2026، أطلقت <strong>Perplexity</strong> <strong>Pages 3 Arabic</strong>: أداة تُحوّل استفسارًا بالفصحى أو اللهجة إلى صفحة تقرير تفاعلية مع مصادر موثّقة، مخططات وجداول باتجاه RTL، تلخيص تنفيذي، تصدير PDF وعرض تقديمي، إدراج شعار العميل، وروابط مشاركة آمنة — للاستشاريين ووكالات التسويق والمستثمرين في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: Pages 2 كان يُهمل اتجاه النص في الجداول أو يخلط مصادر عربية وإنجليزية بلا ترتيب؛ الإصدار 3 يدعم فلاتر مصادر حسب اللغة والقطاع، تحديثًا تلقائيًا للبيانات الرقمية، قوالب «تحليل منافسين» و«خريطة فرص الاستثمار» و«ملخص تنظيمي»، تعليقات فريق بالعربية داخل الصفحة، وبرنامج «Perplexity Research Partners Arabia».</p>
      <p>القدرات الأساسية: تقارير مدعومة بمصادر؛ مخططات RTL؛ تصدير متعدد؛ علامة تجارية؛ تعاون فريق.</p>
      <p>للمبدعين العرب: منتج «تقرير أسبوعي جاهز للبيع» — من يُسلّم 15 تقريرًا شهريًا بـ180–950 دولار للتقرير يبني مكتبة بحث تُدفع شهريًا من شركات لا تملك محللي أبحاث بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Pages 3 Arabic؟</h3>
        <ul>
          <li><strong>اشتراك تقارير أبحاث أسبوعية (سوق، منافسة، تنظيم):</strong> — 180–950 دولار/تقرير.</li>
          <li><strong>إعداد قوالب Pages وهوية علامة للعميل:</strong> 3–7 أيام — 900–4200 دولار.</li>
          <li><strong>حزم «دراسة جدوى سريعة» للمستثمرين:</strong> — 1200–6500 دولار/دراسة.</li>
          <li><strong>دورة «بيع المعرفة بـ Perplexity Pages بالعربية»:</strong> — 48–195 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Pages</span>
        <span class="tag">Research</span>
        <span class="tag">Reports</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Twilio AI Assistants 4 Arabic: مكالمات وواتساب ذكية — حجز، دعم، ومبيعات بلهجة MENA</h2>
      <p class="article-lead">«العملاء يتصلون بعد منتصف الليل ولا أحد يُجيب — أريد صوتًا عربيًا طبيعيًا يحجز المواعيد ويُحدّث النظام». في 18 نوفمبر 2026، أطلقت <strong>Twilio</strong> <strong>AI Assistants 4 Arabic</strong>: منصة مساعدين صوتية ونصية فوق Twilio Voice وWhatsApp وSMS، تفهم الخليجية والمصرية والشامية، تُجيب عن الأسئلة المتكررة، تُحوّل المهتمين إلى مواعيد في التقويم، تُنشئ تذاكر دعم، تُلخّص المحادثات بالفصحى للمشرف، وتدعم الامتثال للتسجيل والموافقة — لعيادات الرعاية الصحية والعقارات والتعليم والتجزئة في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 3 كان يقطع اللهجة عند الأرقام الطويلة أو يُخطئ في أسماء المدن؛ Assistants 4 يدعم تحويل الكلام إلى نص دقيق للعربية، تبديلًا سلسًا إلى موظف بشري، قوالب «تأكيد حجز» و«استرداد طلب» و«تأهيل عميل B2B»، اختبارًا قبل الإطلاق، تكامل Salesforce وHubSpot وZendesk، وبرنامج «Twilio Conversational MENA».</p>
      <p>القدرات الأساسية: صوت وواتساب بالعربية؛ حجز وتذاكر؛ تلخيص للمشرف؛ تكامل أنظمة العملاء؛ امتثال الاتصالات.</p>
      <p>للمبدعين العرب: باقة «خط ساخن ذكي في 10 أيام» — من ينشر 6 مساعدين شهريًا بـ2800–16500 دولار للمشروع + 520–2400 دولار/شهر للمراقبة يبيع وقتًا محفوظًا لشركات تخسر عملاء بسبب تأخر الرد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Twilio AI Assistants 4 Arabic؟</h3>
        <ul>
          <li><strong>بناء مساعد صوتي أو واتساب من سيناريو عربي:</strong> 6–14 يومًا — 2800–16500 دولار.</li>
          <li><strong>مراقبة وتحسين المحادثات شهريًا:</strong> — 520–2400 دولار/عميل/شهر.</li>
          <li><strong>قوالب سيناريوهات (صحة، عقار، تعليم):</strong> — 65–285 دولار/حزمة.</li>
          <li><strong>ورش «بوتات صوتية تحقق مبيعات بالعربية»:</strong> — 62–248 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Twilio</span>
        <span class="tag">Voice AI</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Contact Center</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Writer AI HQ 3 Arabic: مقر أسلوب العلامة — كل رسالة بنبرة واحدة موثوقة</h2>
      <p class="article-lead">«فريقنا يكتب بالعربية والإنجليزية وكل رسالة تبدو كأنها من شركة مختلفة — أريد دليلًا حيًا يُصحّح النبرة تلقائيًا». في 18 نوفمبر 2026، أطلقت <strong>Writer</strong> <strong>AI HQ 3 Arabic</strong>: طبقة أسلوب مؤسسي تتعلم من موادك المعتمدة، تُراجع البريد والعروض وصفحات المنتج بالفصحى، تُقترح بدائل تراعي لهجة الخليج أو مصر حسب الجمهور، تُحذّر من عبارات محظورة تنظيميًا، تتكامل مع Gmail وOutlook وSalesforce وServiceNow، وتُصدّر تقارير اتساق أسبوعية — للبنوك والاتصالات وسلاسل التجزئة والشركات التقنية متعددة الأسواق.</p>
      <p>المشكلة التي حلّتها: HQ 2 كان يُبالغ في الترجمة الآلية أو يُضعف أسلوب العلامة الرسمي؛ الإصدار 3 يدعم مستودع نبرة ثنائي اللغة، قواعد امتثال للقطاعات المنظّمة، اقتراحات سياقية داخل المحرر، قوالب «إشعار تنظيمي» و«عرض سعر» و«اعتذار خدمة»، تدريبًا على اختصارات القطاع، وبرنامج «Writer Brand Voice MENA».</p>
      <p>القدرات الأساسية: دليل نبرة حي؛ مراجعة عربية وإنجليزية؛ تنبيهات امتثال؛ تكامل بريد وأنظمة عمل؛ تقارير اتساق.</p>
      <p>للمبدعين العرب: خدمة «صوت علامة موحّد في 21 يومًا» — من يُدير 8 عملاء بـ450–2100 دولار/شهر لكل عميل + 1100–5800 دولار للإعداد الأولي يبيع احترافية لغوية لعلامات تتوسع دون توظيف محررين لكل قناة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Writer AI HQ 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء دليل نبرة وتفعيل HQ على قنوات العميل:</strong> 10–21 يومًا — 1100–5800 دولار.</li>
          <li><strong>إدارة نبرة وامتثال لغوي شهريًا:</strong> — 450–2100 دولار/عميل/شهر.</li>
          <li><strong>قوالب رسائل منظّمة (مالية، اتصالات، تجزئة):</strong> — 55–240 دولار/مجموعة.</li>
          <li><strong>دورة «هوية لغوية رقمية بالعربية»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Writer</span>
        <span class="tag">Brand Voice</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 18-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="18-11-2026 -- 12-AM.html">
          📰 18 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "18-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/18-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/18-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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