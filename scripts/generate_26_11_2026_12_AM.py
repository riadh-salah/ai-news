#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "26-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "HubSpot Content AI 3 Arabic · Canva Magic Studio 4 Arabic · "
    "Intercom Fin 3 Arabic · DocuSign Agreement AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HubSpot Content AI 3 Arabic، Canva Magic Studio 4 Arabic، Intercom Fin 3 Arabic، DocuSign Agreement AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من HubSpot Content AI 3 Arabic الذي يُحوّل فكرة تسويقية نصف جاهزة إلى مدونة وصفحة هبوط وسلسلة بريد بالفصحى قبل أن يُطفأ ضوء مكتبك، إلى Canva Magic Studio 4 Arabic الذي يُولّد هوية بصرية ومقاطع قصيرة وعروض تقديمية بخط عربي أنيق في دقائق، ومن Intercom Fin 3 Arabic الذي يُجيب زوار موقعك ليلاً ويُغلق الشكوى دون انتظار وكيل، إلى DocuSign Agreement AI 3 Arabic الذي يُلخّص العقد ويُبرز البنود الخطرة بجملة عربية قبل التوقيع — أربع قصص ليلية في 26 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء الساعة الصفراء!</h1>
      <p class="hero-sub">ليلة المحتوى والتصميم والدعم والعقود: الكلمات تُكتب، العلامات تُرسم، العملاء يُطمأنون، والاتفاقيات تُفهم. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 26 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HubSpot Content AI 3 Arabic: محتوى يبيع — مدونات، صفحات، وبريد من فكرة واحدة بالعربية!</h2>
      <p class="article-lead">«فريق التسويق لديك ينشر مرة كل شهرين — والمنافس ينشر أسبوعيًا بخطافات عربية تُفتح». في 26 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>HubSpot Content AI 3 Arabic</strong>: مساعد إبداعي داخل Marketing Hub يقرأ شخصية العلامة وقاعدة العملاء والكلمات المفتاحية المستهدفة في MENA، يُحوّل نقاطًا مختصرة إلى مقالات SEO بالفصحى أو نبرة خليجية دافئة، يُبني صفحات هبوط RTL مع أزرار دعوة محلية، يُولّد سلاسل بريد تنشيط وولاء مرتبطة بمرحلة القمع، يُقترح عناوين مُحسّنة للبحث العربي، يتكامل مع CRM وSocial وGoogle Ads، ويُلخّص أداء المحتوى بجملة تنفيذية للمدير — للشركات الناشئة ووكالات النمو في السعودية والإمارات ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: الإصدار الثاني كان يُطيل النص دون هيكل؛ الإصدار 3 يدعم قوالب «مقال خبرة» و«دليل شراء» و«مقارنة منتجات»، يحترم أيام العطل والرمضان في الجدولة، يُنبّه عند تكرار نفس الخطاف، يُقترح إعادة صياغة لقطع قديمة بلا زيارات، يدعم اختبار عناوين متعددة، تكامل مع جدولة LinkedIn وX بالعربية، وبرنامج شركاء «HubSpot Content MENA» للوكالات التي تبيع حزم محتوى شهري.</p>
      <p>القدرات الأساسية: مقالات وصفحات عربية؛ سلاسل بريد؛ SEO محلي؛ تقارير تنفيذية؛ تكامل CRM.</p>
      <p>للمبدعين العرب: استوديو «محتوى ليلي لا ينام» — من يُدير Content AI لخمسة عملاء بنطاق 10–80 مقالًا شهريًا بـ1350–9600 دولار للإعداد + 420–1680 دولار/شهر لكل عميل يبني دخلًا متكررًا مع فرق تسويق تختنق من الفراغ الإبداعي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Content AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد نبرة العلامة + قوالب + تدريب الفريق:</strong> 6–14 يومًا — 1350–9600 دولار/عميل.</li>
          <li><strong>تحرير وتحسين ونشر محتوى شهريًا:</strong> — 420–1680 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 عنوانًا وخطافًا عربيًا جاهزًا (B2B، تجزئة، خدمات):</strong> — 95–380 دولار/حزمة.</li>
          <li><strong>ورش «تسويق محتوى ذكي بالعربية مع HubSpot Content AI»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Content</span>
        <span class="tag">Marketing</span>
        <span class="tag">SEO</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva Magic Studio 4 Arabic: استوديو بصري كامل — تصاميم، فيديو، وعروض بخط عربي مُبهر!</h2>
      <p class="article-lead">«العميل يريد حملة بصرية خلال 48 ساعة — والمصمم مشغول والخطوط العربية غير متسقة». في 26 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Canva Magic Studio 4 Arabic</strong>: مجموعة أدوات ذكية داخل Canva تُولّد شعارات ومنشورات وستوريات من وصف نصي بالعربية، تُحوّل نص المدير إلى عرض تقديمي من 12 شريحة بترتيب منطقي، تُنتج مقاطع قصيرة Reels وTikTok بترجمة وتعليق عربي، تُقترح لوحات ألوان من صورة المنتج، تُطبّق خطوطًا عربية مُعتمدة (Noto Kufi، Cairo، Tajawal)، تتكامل Brand Kit وTeams وطباعة محلية، وتُصدّر بصيغ جاهزة للوكالات — لصناع المحتوى والتجار ومدارس التدريب في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 3 كان يخلط الاتجاهات في نفس القالب؛ الإصدار 4 يفرض RTL تلقائيًا على النصوص، يُنبّه عند تداخل الحروف، يدعم قوالب «رمضان» و«اليوم الوطني» و«عروض الجمعة البيضاء»، يُولّد نسخ A/B لنفس الإعلان، يحترم حقوق العلامة عبر Brand Guard، مسار شريك للوكالات التي تبيع «هوية شهرية بالذكاء الاصطناعي»، وتدريب Canva Certified MENA.</p>
      <p>القدرات الأساسية: توليد تصميم وفيديو؛ عروض تلقائية؛ خطوط عربية؛ Brand Kit؛ تصدير متعدد.</p>
      <p>للمبدعين العرب: استوديو «هوية في ليلة واحدة» — من يقدّم حزمة Canva Magic لعشرة عملاء (شعار + 30 منشورًا شهريًا) بـ980–7200 دولار للإعداد + 280–1240 دولار/شهر لكل عميل يخدم سوقًا جائعًا لتصاميم سريعة لا رخيصة الشكل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>بناء Brand Kit + قوالب + تدريب فريق العميل:</strong> 4–9 أيام — 980–7200 دولار/عميل.</li>
          <li><strong>إنتاج منشورات وفيديوهات قصيرة شهريًا:</strong> — 280–1240 دولار/عميل/شهر.</li>
          <li><strong>حزمة 40 قالب Canva عربي (تجزئة، عيادات، تعليم):</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «تصميم ذكي بالعربية مع Canva Magic Studio»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Design</span>
        <span class="tag">Video</span>
        <span class="tag">Branding</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Intercom Fin 3 Arabic: دعم ليلي بلا انتظار — إجابات، تصعيد، ورضا قبل الفجر!</h2>
      <p class="article-lead">«الزائر يسأل عن الشحن الساعة 2 صباحًا — وتجربته تنتهي بلا رد حتى موظف الدعم يستيقظ». في 26 نوفمبر 2026، أطلقت <strong>Intercom</strong> <strong>Intercom Fin 3 Arabic</strong>: وكيل دعم ذكي يقرأ مركز المساعدة وسياسات الشحن والإرجاع والفوترة، يُجيب بالفصحى أو باللهجة المصرية أو الخليجية حسب إعداداتك، يُنفّذ إجراءات (تتبع طلب، تغيير موعد، إرسال فاتورة)، يُصعّد للبشر مع ملخص عربي كامل، يتكامل Shopify وStripe وZendesk، يُقيس رضًا بعد كل محادثة، ويُبلّغ الإدارة بثلاثة مواضيع تتكرر ليلًا — لتجارة إلكترونية واشتراكات SaaS وخدمات تعليم رقمي في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُعيد صياغة مقالات المساعدة حرفيًا؛ الإصدار 3 يفهم النية قبل النص، يحترم ساعات العمل المحلية، يُخفّي بيانات بطاقات في المحادثة، يدعم واتساب Business و Messenger ضمن نفس السياق، يُولّد تقارير «أسئلة ليلية خاسرة» بالعربية، مسار تدريب للفرق على تحسين قاعدة المعرفة، وبرنامج «Intercom Partners Arabic CX» للمستشارين.</p>
      <p>القدرات الأساسية: إجابات متعددة اللهجات؛ إجراءات تلقائية؛ تصعيد ذكي؛ تكامل تجارة؛ تقارير نوايا.</p>
      <p>للمبدعين العرب: خدمة «دعم ليلي يُغلق التذكرة» — من يُفعّل Fin لموقع بـ5 آلاف–120 ألف محادثة شهريًا بـ1480–11200 دولار + 360–1540 دولار/شهر للتحسين يخدم شركات تخسر مبيعات ليلية بسبب بطء الرد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء قاعدة معرفة + تدفقات + اختبار المحادثات:</strong> 7–16 يومًا — 1480–11200 دولار.</li>
          <li><strong>مراجعة محادثات وتحسين نوايا شهريًا:</strong> — 360–1540 دولار/عميل/شهر.</li>
          <li><strong>حزمة 25 إجابة جاهزة (شحن، إرجاع، اشتراك) بالعربية:</strong> — 82–328 دولار/حزمة.</li>
          <li><strong>ورش «تجربة عميل ذكية بالعربية مع Intercom Fin»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Support</span>
        <span class="tag">Chatbot</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>DocuSign Agreement AI 3 Arabic: عقود واضحة — تلخيص، مخاطر، وتوقيع بثقة!</h2>
      <p class="article-lead">«موظفك وقّع عقدًا بـ40 صفحة دون فهم بند الغرامة — والشركة تدفع السعر ليلًا». في 26 نوفمبر 2026، أطلقت <strong>DocuSign</strong> <strong>DocuSign Agreement AI 3 Arabic</strong>: طبقة ذكاء فوق Intelligent Agreement Management تُلخّص العقد إلى خمس نقاط عربية، تُبرز بنود المسؤولية والتجديد التلقائي والغرامات، تُقارن النسخة المُرسلة بقالب شركتك المعتمد، يُ draft تعليقات للمدير القانوني بالفصحى المؤسسية، تتكامل Salesforce وSAP وMicrosoft 365، تُحفظ سجل التغييرات للامتثال، وتُنبّه عند التوقيع خارج ساعات العمل — للشركات القانونية والتقنية والعقارية والاستشارية 50–5000 موظف في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُترجم إنجليزيًا حرفيًا؛ الإصدار 3 يدعم مصطلحات عقود عربية شائعة، يحترم متطلبات الهيئات المحلية حيث تُتاح، يُقترح أسئلة للطرف المُوقّع قبل الموافقة، يُولّد ملخصًا صوتيًا قصيرًا بالعربية، مسار موافقة متعدد المستويات مع تذكير واتساب للمفوضين، وبرنامج شريك للمكاتب القانونية التي تبيع «مراجعة عقد بالذكاء الاصطناعي».</p>
      <p>القدرات الأساسية: تلخيص عربي؛ كشف مخاطر؛ مقارنة قوالب؛ تعليقات قانونية؛ تكامل مؤسسي.</p>
      <p>للمبدعين العرب: استشارات «توقيع بلا مفاجآت» — من يُفعّل Agreement AI لمؤسسة 100–3000 عقد سنويًا بـ1720–13800 دولار + 450–1820 دولار/شهر للمراقبة يبيع طمأنينة للقيادات التي تخاف من البنود المختبئة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من DocuSign Agreement AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد قوالب + سياسات + تدريب فرق قانونية:</strong> 8–20 يومًا — 1720–13800 دولار.</li>
          <li><strong>مراجعة عقود حرجة وتقارير مخاطر شهريًا:</strong> — 450–1820 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب تعليق عقد عربي (تعديل، رفض، طلب توضيح):</strong> — 76–304 دولار/حزمة.</li>
          <li><strong>ورش «عقود ذكية بالعربية مع DocuSign Agreement AI»:</strong> — 50–200 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">DocuSign</span>
        <span class="tag">Legal</span>
        <span class="tag">Contracts</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="26-11-2026 -- 12-AM.html">
          📰 26 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "26-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/26-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/26-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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