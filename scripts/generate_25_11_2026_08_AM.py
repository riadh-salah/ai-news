#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Stripe Radar AI 2 Arabic · Klaviyo AI Email 2 Arabic · "
    "Twilio Flex AI 2 Arabic · Microsoft Viva Copilot 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Stripe Radar AI 2 Arabic، Klaviyo AI Email 2 Arabic، Twilio Flex AI 2 Arabic، Microsoft Viva Copilot 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Stripe Radar AI 2 Arabic الذي يُوقف الاحتيال قبل أن يُبرد قهوتك ويُشرح لك «لماذا رُفضت هذه البطاقة» بجملة عربية واضحة، إلى Klaviyo AI Email 2 Arabic الذي يُكتب سلاسل بريد ولاء وتنشيط بالفصحى تُفتح في الصباح، ومن Twilio Flex AI 2 Arabic الذي يُحوّل مكالمة دعم صباحية إلى حل مغلق عبر صوت وواتساب ورسائل نصية بلهجة العميل، إلى Microsoft Viva Copilot 2 Arabic الذي يُرتّب يومك واجتماعاتك وأولوياتك من داخل Teams قبل أن يبدأ أول اجتماع — أربع قصص صباحية في 25 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباح المدفوعات والتسويق ومراكز الاتصال والإنتاجية: المدفوعات تُحمى، الرسائل تُرسل، العملاء يُرضَون، واليوم يُخطَّط بذكاء. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 25 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Stripe Radar AI 2 Arabic: درع ذكي للمدفوعات — احتيال أقل، موافقات أسرع، وثقة العميل!</h2>
      <p class="article-lead">«متجرك رفض 40 طلبًا شرعيًا أمس بسبب قواعد احتيال قديمة — والعملاء غادروا إلى منافس يقبل بطاقاتهم». في 25 نوفمبر 2026، أطلقت <strong>Stripe</strong> <strong>Stripe Radar AI 2 Arabic</strong>: طبقة ذكاء فوق Radar وPayments تُحلّل مئات الإشارات (جهاز، IP، سلوك سلة، عملة، توقيت الشراء)، تُفرّق بين الاحتيال الحقيقي والعميل المسافر أو المشتري أول مرة، تُكتب ملخصًا عربيًا للتاجر عند كل رفض أو مراجعة يدوية، تُقترح قواعد مخصّصة لسوق MENA دون حظر الدفع المحلي، تُختبر عتبات المخاطر أسبوعيًا بالذكاء الاصطناعي، تتكامل Apple Pay ومدى والمحافظ الرقمية، وتُرسل تنبيهًا فوريًا عند موجة هجوم بطاقات مسروقة — لمتاجر التجزئة الإلكترونية والاشتراكات والسوق السعودية والإماراتية ومصر.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُفرط في الحذر على بطاقات عربية جديدة؛ الإصدار 2 يدعم تفسيرات RTL في لوحة Stripe، تقارير «خسائر بسبب الرفض الزائد» بالعربية، تكامل مع 3D Secure وتدفقات التحقق المحلية، تدريب نموذج على بيانات مجمّعة مشفّرة من تجّار المنطقة، مسار تصعيد لمراجع بشري مع توصية الذكاء الاصطناعي، وبرنامج شركاء «Stripe Radar MENA» للوكالات التي تبيع ضبط المخاطر كخدمة متكررة.</p>
      <p>القدرات الأساسية: كشف احتيال دقيق؛ تقليل الرفض الخاطئ؛ شروحات عربية؛ قواعد إقليمية؛ تقارير خسارة إيراد.</p>
      <p>للمبدعين العرب: مكتب «دفعات آمنة لا تخيف العميل» — من يُضبط Stripe Radar لمتجر بـ2–15 مليون دولار مبيعات سنوية بـ1250–9200 دولار للمشروع + 290–1350 دولار/شهر للمراقبة يخدم تجّارًا يخسرون مبيعات شرعية في خط الدفع الأخير.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe Radar AI 2 Arabic؟</h3>
        <ul>
          <li><strong>تدقيق قواعد Radar + تقليل الرفض الخاطئ + تدريب الفريق:</strong> 4–10 أيام — 1250–9200 دولار.</li>
          <li><strong>مراجعة أسبوعية للمخاطر وتقارير عربية:</strong> — 290–1350 دولار/متجر/شهر.</li>
          <li><strong>حزمة 8 قوالب رسائل عربية (رفض، مراجعة، تأكيد دفع):</strong> — 78–310 دولار/حزمة.</li>
          <li><strong>ورش «مدفوعات ذكية ومكافحة احتيال بالعربية مع Stripe Radar»:</strong> — 45–180 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Fraud</span>
        <span class="tag">Payments</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Klaviyo AI Email 2 Arabic: بريد يُفتح في الصباح — شخصنة، سلاسل ولاء، وتفعيل من سلوك الشراء!</h2>
      <p class="article-lead">«قائمة بريدية بـ80 ألف مشترك — ومعدل فتح 9% لأن الموضوع والمحتوى إنجليزيان على جمهور عربي». في 25 نوفمبر 2026، أطلقت <strong>Klaviyo</strong> <strong>Klaviyo AI Email 2 Arabic</strong>: مساعد تسويق داخل Klaviyo يقرأ سجل الشراء والتصفح والسلات المتروكة، يُقترح موضوعات بريد عربية بخطاف عاطفي ومنطقي، يُكتب نسخة كاملة RTL مع أزرار دعوة للإجراء محلية، يُبني سلاسل ترحيب وتنشيط وولاء (win-back)، يُختبر عناوين متعددة قبل الإرسال، يُ personalizes الكتل حسب المدينة واللغة والمنتج المفضّل، يتكامل Shopify وWooCommerce وMagento وقنوات SMS، ويُلخّص أداء الحملة بجملة تنفيذية للمدير بالعربية — لوكالات التجزئة والجمال والتقنية في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُنتج نصوصًا طويلة أو حرفية؛ الإصدار 2 يملك «نبرة علامة» (فصحى رسمية، خليجية دافئة، مصرية قريبة)، يحترم أيام العطل والرمضان في الجدولة، يُنبّه عند تكرار عروض يتعب منها المشتركون، يُقترح تقسيمات جديدة من سلوك الشراء، يدعم اختبار A/B تلقائي، ومسار شريك للوكالات التي تدير عشرات الحسابات.</p>
      <p>القدرات الأساسية: موضوعات ونصوص عربية؛ سلاسل ولاء؛ شخصنة سلوكية؛ اختبار عناوين؛ تقارير تنفيذية.</p>
      <p>للمبدعين العرب: استوديو «بريد صباحي يُحوّل» — من يُدير Klaviyo AI لخمسة متاجر بنطاق 30 ألف–400 ألف مشترك بـ1100–7800 دولار للإعداد + 340–1580 دولار/شهر لكل عميل يبني دخلًا متكررًا مع تجّار يريدون إيرادًا من القائمة لا من إعلانات باهظة فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Klaviyo AI Email 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد AI + سلاسل ترحيب وتنشيط + تقسيمات:</strong> 5–12 يومًا — 1100–7800 دولار/عميل.</li>
          <li><strong>تحسين حملات واختبارات عناوين شهريًا:</strong> — 340–1580 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 قالب بريد عربي (عروض، ولاء، سلة متروكة):</strong> — 92–368 دولار/حزمة.</li>
          <li><strong>ورش «تسويق بريد ذكي بالعربية مع Klaviyo AI»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Klaviyo</span>
        <span class="tag">Email</span>
        <span class="tag">Marketing</span>
        <span class="tag">Retention</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Twilio Flex AI 2 Arabic: مركز اتصال ذكي — صوت، واتساب، وردود تُغلق التذكرة قبل الظهر!</h2>
      <p class="article-lead">«طابور انتظار صباحي 25 دقيقة — والعميل يسأل عن شحن طلبه على واتساب وفيسبوك والهاتف دون إجابة موحّدة». في 25 نوفمبر 2026، أطلقت <strong>Twilio</strong> <strong>Twilio Flex AI 2 Arabic</strong>: طبقة ذكاء فوق Flex Contact Center تسمع المكالمات وتقرأ المحادثات النصية، تُصنّف النية (شحن، إرجاع، فوترة، شكوى)، تُقترح ردودًا بالفصحى أو باللهجة المصرية أو الخليجية حسب قناة العميل، تُلخّص المحادثة للوكيل البشري عند التصعيد، تُطلق مسارات IVR ذكية بالصوت العربي، تتكامل مع CRM وShopify وتذاكر Zendesk، وتُقيس رضا العميل بعد كل تفاعل — لشركات الاتصالات والتجارة الإلكترونية والخدمات المالية التي تخدم آلاف المحادثات يوميًا في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يخلط اللغات في نفس الرد؛ الإصدار 2 يحترم ساعات العمل المحلية، يُفعّل حماية بيانات بطاقات الدفع في المحادثات، يُولّد ملخصًا عربيًا لكل مكالمة تُحفظ في السجل، يُقترح macros للوكلاء، يدعم تكامل WhatsApp Business API والرسائل الصوتية القصيرة، وبرنامج تدريب «Flex AI Arabic Agents» لفرق مراكز الاتصال.</p>
      <p>القدرات الأساسية: تصنيف نوايا؛ ردود متعددة القنوات؛ ملخصات عربية؛ IVR صوتي؛ تكامل CRM.</p>
      <p>للمبدعين العرب: خدمة «دعم صباحي بلا طابور طويل» — من يُبني Flex AI لمركز 30–250 وكيلًا بـ1850–14200 دولار + 410–1680 دولار/شهر للتحسين يخدم شركات تدفع غرامات SLA وسمعة بسبب تأخر الرد الصباحي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Twilio Flex AI 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم مسارات + ربط قنوات + تدريب وكلاء:</strong> 8–18 يومًا — 1850–14200 دولار.</li>
          <li><strong>تحسين قوالب ونوايا ومراقبة جودة شهريًا:</strong> — 410–1680 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 ردًا جاهزًا (شحن، إرجاع، فوترة) بالعربية:</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «مراكز اتصال ذكية بالعربية مع Twilio Flex AI»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Twilio</span>
        <span class="tag">Contact center</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Microsoft Viva Copilot 2 Arabic: يومك يُرتب نفسه — أولويات، اجتماعات، وتعلم قبل أول Teams!</h2>
      <p class="article-lead">«مئة إشعار و15 اجتماعًا — وفريقك لا يعرف ما الأولوية حتى الساعة العاشرة». في 25 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Microsoft Viva Copilot 2 Arabic</strong>: مساعد موحّد عبر Viva Insights وGoals وLearning داخل Microsoft 365 وTeams يقرأ تقويمك ورسائلك ومهامك (ضمن صلاحياتك)، يُلخّص ما يجب إنجازه اليوم بثلاث نقاط عربية واضحة، يُحضّرك لكل اجتماع بملخص المحادثات السابقة والقرارات المعلّقة، يُقترح بلوكات تركيز بلا اجتماعات، يُرشدك لمسار تعلم من فجوة المهارات، يُ draft رسائل متابعة للمدير والفريق بالفصحى المؤسسية، يتكامل Outlook وPlanner وSharePoint، ويحترم سياسات الخصوصية الإقليمية — للشركات الهجينة والمؤسسات 200–8000 موظف في السعودية والإمارات ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان عامًا جدًا؛ الإصدار 2 يدعم لهجات مهنية للتواصل الداخلي، يُنبّه عند اجتماعات متداخلة لا طائل منها، يُقيس عبء الاجتماعات على الفريق بلوحة عربية للمدير، يُقترح إجراءات سريعة من Copilot Actions، تكامل قراءة فقط مع أنظمة موارد بشرية شائعة، وبرنامج شريك لتفعيل Viva في المؤسسات العربية.</p>
      <p>القدرات الأساسية: تخطيط يومي عربي؛ تحضير اجتماعات؛ بلوكات تركيز؛ مسارات تعلم؛ رسائل متابعة.</p>
      <p>للمبدعين العرب: استشارات «صباح منتج بلا فوضى» — من يُفعّل Viva Copilot لقسم أو شركة 150–2000 مستخدم بـ1550–11800 دولار + 380–1520 دولار/شهر للتبنّي المستمر يبيع وقتًا تنفيذيًا للقيادات المغرقة في الاجتماعات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Viva Copilot 2 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل Viva + سياسات + تدريب قادة وفرق:</strong> 6–16 يومًا — 1550–11800 دولار.</li>
          <li><strong>مراجعة إنتاجية واجتماعات ومسارات تعلم شهريًا:</strong> — 380–1520 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 قالب رسالة داخلية عربية (متابعة، توجيه، شكر):</strong> — 70–280 دولار/حزمة.</li>
          <li><strong>ورش «إنتاجية ذكية بالعربية مع Viva Copilot»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Viva</span>
        <span class="tag">Productivity</span>
        <span class="tag">Teams</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="25-11-2026 -- 08-AM.html">
          📰 25 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/25-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/25-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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