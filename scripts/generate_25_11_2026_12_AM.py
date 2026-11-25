#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "PayPal AI Checkout 2 Arabic · Plaid AI Insights 2 Arabic · "
    "BambooHR AI Answers 2 Arabic · LinkedIn Sales Navigator AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — PayPal AI Checkout 2 Arabic، Plaid AI Insights 2 Arabic، BambooHR AI Answers 2 Arabic، LinkedIn Sales Navigator AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من PayPal AI Checkout 2 Arabic الذي يُحوّل زيارة المتجر الإلكتروني إلى دفع مُكمَل بلهجة عربية قبل أن يُغلق العميل التبويب، إلى Plaid AI Insights 2 Arabic الذي يُفسّر حركة الحسابات البنكية ويُنبّهك على انحرافات التدفق النقدي بجملة واحدة بالفصحى، ومن BambooHR AI Answers 2 Arabic الذي يُجيب الموظف عن الإجازة والتأمين والسياسات من دليل شركتك دون تذكرة HR، إلى LinkedIn Sales Navigator AI 3 Arabic الذي يُختصر البحث عن عملاء B2B ويُكتب متابعة مبيعات عربية تُفتح — أربع قصص ليلية في 25 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء الساعة الصفراء!</h1>
      <p class="hero-sub">ليلة الدفع والمالية والموارد البشرية والمبيعات: السلات تُكمَل، الأرقام تتكلّم، السياسات تُشرح، والفرص تُرسل. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 25 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>PayPal AI Checkout 2 Arabic: دفع ذكي — سلة، تقسيط، وثقة قبل أن يهجر العميل الشراء!</h2>
      <p class="article-lead">«العميل وصل لصفحة الدفع ثم اختفى — والسلة كانت بقيمة مئات الدولارات». في 25 نوفمبر 2026، أطلقت <strong>PayPal</strong> <strong>PayPal AI Checkout 2 Arabic</strong>: طبقة ذكاء فوق PayPal Commerce تُحلّل سلوك المتصفح والجهاز والمنطقة، تُقترح طريقة دفع مفضّلة (محفظة، بطاقة محلية، تقسيط Pay Later)، تُكتب رسائل طمأنة بالعربية عند رسوم إضافية أو عملة أجنبية، تُختبر عناوين زر «إتمام الشراء» لرفع التحويل، تُفعّل حماية من الاحتيال دون حظر مشتريات شرعية في MENA، تتكامل Shopify وWooCommerce وMagento، وتُرسل للتاجر تقريرًا أسبوعيًا بأين تتسرّب المبيعات — لمتاجر الإلكترونيات والأزياء والخدمات الرقمية في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُحسّن الحقول الإنجليزية فقط؛ الإصدار 2 يدعم واجهة RTL كاملة، رسائل SMS تأكيد بالعربية، تذكير سلة متروكة عبر واتساب Business المعتمد، توصيات تقسيط مُهيّأة لضوابط Sharia حيث ينطبق، لوحة للتاجر تشرح «لماذا انخفض التحويل هذا الأسبوع»، وبرنامج «PayPal Partners MENA Checkout» للوكالات التي تبيع الإعداد كحزمة.</p>
      <p>القدرات الأساسية: تحسين تحويل الدفع؛ تقسيم ذكي؛ رسائل طمأنة عربية؛ تكامل منصات تجارة؛ تقارير تسرّب مبيعات.</p>
      <p>للمبدعين العرب: استوديو «سلة لا تُهجر» — من يُفعّل PayPal AI Checkout لمتجر 50 ألف–2 مليون زيارة شهريًا بـ1400–9800 دولار للمشروع + 320–1450 دولار/شهر للتحسين المستمر يخدم تجّارًا يخسرون الإيراد في آخر خطوة لا في الإعلانات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من PayPal AI Checkout 2 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل Checkout AI وربط المتجر + اختبار A/B:</strong> 5–12 يومًا — 1400–9800 دولار.</li>
          <li><strong>تحسين تحويل ورسائل سلة متروكة شهريًا:</strong> — 320–1450 دولار/متجر/شهر.</li>
          <li><strong>حزمة 5 قوالب رسائل عربية (ثقة، تقسيط، تأكيد):</strong> — 85–340 دولار/حزمة.</li>
          <li><strong>ورش «دفع ذكي بالعربية مع PayPal AI Checkout»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">PayPal</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Payments</span>
        <span class="tag">Conversion</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Plaid AI Insights 2 Arabic: مالية واضحة — تدفق نقدي، فئات، وتنبيهات بلسان المحاسب!</h2>
      <p class="article-lead">«الميزانية تبدو سليمة حتى يُفاجئك انسحاب كبير من حساب الشركة دون تفسير». في 25 نوفمبر 2026، أطلقت <strong>Plaid</strong> <strong>Plaid AI Insights 2 Arabic</strong>: محرك تحليل فوق Plaid Link يقرأ حسابات بنكية وبطاقات مربوطة، يُصنّف المعاملات بالعربية (رواتب، اشتراكات، مشتريات موردين)، يُلخّص التدفق النقدي أسبوعيًا بجملة تنفيذية للمدير، يُنبّه عند رسوم غير متوقعة أو تكرار اشتراك مُلغى، يُقارن إنفاق الفروع، يتكامل مع QuickBooks وXero وبرمجيات محلية عبر واجهات API، ويحترم عدم تخزين بيانات حساسة خارج سياسة العميل — للشركات الناشئة والوكالات والمحاسبين الذين يخدمون 20–500 حسابًا في المنطقة.</p>
      <p>المشكلة التي حلّتها: Insights 1 كان ملخصات إنجليزية عامة؛ الإصدار 2 يدعم بنوك MENA الشائعة عبر شركاء ربط، تقارير PDF عربية للمجالس، أسئلة محادثة «كم صرفنا على التسويق هذا الربع؟»، تصدير لجدول Excel RTL، قواعد تنبيه مخصّصة للمؤسس، ومسار تصعيد لمحاسب بشري عند استثناءات ضريبية.</p>
      <p>القدرات الأساسية: تصنيف معاملات عربي؛ ملخص تدفق نقدي؛ تنبيهات انحراف؛ تكامل محاسبة؛ أسئلة محادثة مالية.</p>
      <p>للمبدعين العرب: مكتب «مالية تُفهم قبل الإقفال» — من يُسلّم لوحة Plaid AI لعشرة عملاء محاسبة بـ950–6800 دولار للإطلاق + 280–1200 دولار/شهر للصيانة يبني دخلًا متكررًا مع شركات تنمو أسرع من قدرتها على قراءة البنوك يدويًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Plaid AI Insights 2 Arabic؟</h3>
        <ul>
          <li><strong>ربط حسابات + قواعد تنبيه + تدريب المحاسب:</strong> 4–9 أيام — 950–6800 دولار/عميل.</li>
          <li><strong>مراجعة تصنيفات وتقارير مجلس شهريًا:</strong> — 280–1200 دولار/عميل/شهر.</li>
          <li><strong>حزمة 6 قوالب تقارير عربية (تدفق، مصروف، اشتراكات):</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «قراءة البنوك بالذكاء الاصطناعي مع Plaid»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Plaid</span>
        <span class="tag">Fintech</span>
        <span class="tag">Cash flow</span>
        <span class="tag">Accounting</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>BambooHR AI Answers 2 Arabic: موارد بشرية لحظية — سياسات، إجازات، ومزايا بلا تذاكر معلّقة!</h2>
      <p class="article-lead">«موظف يسأل عن عدد أيام الإجازة المتبقية في الساعة الحادية عشرة مساءً — وفريق HR نائم». في 25 نوفمبر 2026، أطلقت <strong>BambooHR</strong> <strong>BambooHR AI Answers 2 Arabic</strong>: مساعد داخل BambooHR يقرأ دليل الموظف وسياسات الشركة المعتمدة، يُجيب عن الإجازات والتأمين الصحي والاستئذان والعمل عن بُعد بالفصحى، يُرشد المدير لخطوات الموافقة داخل النظام، يُلخّص تغييرات سياسة جديدة ببريد عربي موجز، يُقترح نماذج رسائل للموظف والمدير، يتكامل Time Off والتعويضات والتقييمات، ويُصعّد للموارد البشرية عند حالات حساسة — للشركات 50–3000 موظفًا في السعودية والإمارات ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يخطئ في تفاصيل محلية؛ الإصدار 2 يدعم قوالب قانون عمل محلية كمرجع فقط مع تنبيه «راجع مستشارًا»، واجهة موظف بالعربية، تحليل أسئلة شائعة لتحسين الدليل، تكامل Slack وTeams، حماية خصوصية بيانات الرواتب، وبرنامج شريك للمستشارات HR العربية.</p>
      <p>القدرات الأساسية: إجابات سياسات؛ إرشاد موافقات؛ ملخصات تغييرات؛ تحليل أسئلة؛ تكامل إجازات ورواتب.</p>
      <p>للمبدعين العرب: خدمة «HR يُجيب قبل الفجر» — من يُرفع دليل الموظف العربي ويُفعّل AI لشركة 80–600 موظفًا بـ1650–11200 دولار + 360–1480 دولار/شهر يخفف ضغط تذاكر HR على الفرق الصغيرة النامية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من BambooHR AI Answers 2 Arabic؟</h3>
        <ul>
          <li><strong>ترجمة ورفع دليل + تفعيل AI + تدريب:</strong> 6–14 يومًا — 1650–11200 دولار.</li>
          <li><strong>تحديث سياسات ومراجعة إجابات شهريًا:</strong> — 360–1480 دولار/شركة/شهر.</li>
          <li><strong>حزمة 10 قوالب FAQ عربية (إجازة، تأمين، سفر عمل):</strong> — 68–272 دولار/حزمة.</li>
          <li><strong>ورش «موارد بشرية ذكية بالعربية مع BambooHR»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">BambooHR</span>
        <span class="tag">HR</span>
        <span class="tag">Policies</span>
        <span class="tag">Employee experience</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>LinkedIn Sales Navigator AI 3 Arabic: مبيعات B2B — leads دقيقة، رسائل تُفتح، وخط أنابيب أوضح!</h2>
      <p class="article-lead">«ساعات من البحث عن مدير مشتريات في قطاع اللوجستيات — ورسالة المتابعة الأولى تُهمَل». في 25 نوفمبر 2026، أطلقت <strong>LinkedIn</strong> <strong>LinkedIn Sales Navigator AI 3 Arabic</strong>: ذكاء داخل Sales Navigator يُحلّل ملفات الشركات والمناصب والنشاط الأخير، يُقترح قوائم leads تطابق ICP عربيًا (حجم، قطاع، موقع)، يُكتب رسائل InMail وطلبات اتصال بلهجة مهنية مناسبة لسوق الخليج ومصر، يُلخّص أخبار الشركة قبل المكالمة، يُرتّب الحسابات حسب نية الشراء، يتكامل CRM (Salesforce، HubSpot، Dynamics)، ويُقيس أي قوالب عربية تحقق ردودًا — للوكالات والشركات SaaS والخدمات الاستشارية التي تبيع B2B في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُترجم حرفيًا من الإنجليزية؛ الإصدار 3 يميّز الفصحى المؤسسية واللهجة الخليجية في نبرة الرسالة، يقترح زمن إرسال حسب المنطقة الزمنية، يُنبّه عند تغيير منصب contact حرج، يُولّد نقاط حديث للمكالمة، يحترم حدود LinkedIn وخصوصية البيانات، وبرنامج تدريب «Navigator AI Arabic Sellers» للفرق.</p>
      <p>القدرات الأساسية: قوائم leads ذكية؛ رسائل عربية مهنية؛ ملخصات حسابات؛ ترتيب نية شراء؛ تكامل CRM.</p>
      <p>للمبدعين العرب: وكالة «خط أنابيب B2B بالعربية» — من يُبني حزمة 4 حملات Navigator + قوالب رسائل + تقرير أسبوعي لعميل مبيعات بـ1200–8900 دولار للمشروع + 290–1380 دولار/شهر يبيع وقتًا بدلًا من الاجتهاد العشوائي في الرسائل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LinkedIn Sales Navigator AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد ICP + قوالب InMail + تدريب فريق مبيعات:</strong> 5–11 يومًا — 1200–8900 دولار.</li>
          <li><strong>تحسين قوالب وقوائم leads شهريًا:</strong> — 290–1380 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 رسالة عربية جاهزة (تعريف، متابعة، اجتماع):</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات B2B بالعربية مع Sales Navigator AI»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LinkedIn</span>
        <span class="tag">B2B</span>
        <span class="tag">Sales</span>
        <span class="tag">Lead gen</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="25-11-2026 -- 12-AM.html">
          📰 25 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/25-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/25-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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