#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 24-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "24-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "MuleSoft Composer AI 2 Arabic · Workiva AI Disclosure 2 Arabic · "
    "Deel HR AI 3 Arabic · PandaDoc Contract AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — MuleSoft Composer AI 2 Arabic، Workiva AI Disclosure 2 Arabic، Deel HR AI 3 Arabic، PandaDoc Contract AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 24 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من MuleSoft Composer AI 2 Arabic الذي يُحوّل فكرة التكامل بين أنظمتك إلى سير تدفق يعمل قبل أن يغلق فريق التقنية مكاتبهم، إلى Workiva AI Disclosure 2 Arabic الذي يُلخّص تقارير الامتثال ويُجهّز إفصاحات بالفصحى للجهات التنظيمية، ومن Deel HR AI 3 Arabic الذي يُجيب الموظفين العالميين عن العقود والرواتب والضرائب بلهجات مفهومة عبر المناطق الزمنية، إلى PandaDoc Contract AI 3 Arabic الذي يُحوّل مكالمة المبيعات إلى عقد جاهز للتوقيع RTL مع تتبّع كل مرحلة — أربع قصص مسائية في 24 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء ساعة الغروب!</h1>
      <p class="hero-sub">مساء التكامل والامتثال والموارد البشرية والعقود: الأنظمة تتكامل، التقارير تُفهم، الفرق العالمية تُدعَم، والصفقات تُغلق. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 24 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>MuleSoft Composer AI 2 Arabic: تكامل ذكي بلا كود — جملة عربية تربط Salesforce وSAP وShopify!</h2>
      <p class="article-lead">«عميل جديد يظهر في CRM لكن الطلب لا يُرسل للمستودع — والتكامل عالق عند المطور المشغول لأسبوعين». في 24 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>MuleSoft Composer AI 2 Arabic</strong>: منصة تكامل مدعومة بالذكاء تفهم طلبك بالعربية، تُقترح تدفقات بيانات بين التطبيقات السحابية والمحلية، تُبني connectors جاهزة لـ SAP وNetSuite وShopify وMicrosoft Dynamics، تُولّد تعيين حقول وتحويلات، تُختبر السيناريوهات قبل الإطلاق، تُنبّه عند فشل مزامنة حرجة، تُوثّق التدفق بلغة الأعمال لا بالكود فقط، وتتكامل مع Agentforce وEinstein — للشركات المتوسطة والمؤسسات في الخليج ومصر التي تنفق ثروات على ربط أنظمة يدويًا.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يحتاج إنجليزية تقنية؛ الإصدار 2 يدعم أوامر صوتية ونصية بالفصحى، قوالب «طلب جديد → مخزون → فاتورة» و«موظف جديد → IT → HR»، امتثال سجلات API، مراجعة أمنية قبل النشر، لوحة مراقبة بالعربية، وبرنامج «MuleSoft Partners MENA» للمكاملين المعتمدين.</p>
      <p>القدرات الأساسية: تدفقات من جملة عربية؛ connectors جاهزة؛ اختبار آلية؛ توثيق للأعمال؛ تكامل CRM وERP.</p>
      <p>للمبدعين العرب: مكتب «تكامل بلا ازدحام» — من يُسلّم 3–12 تدفق ذكي لشركة ناشئة أو مجموعة تجزئة بـ2200–14500 دولار للمشروع + 480–1920 دولار/شهر للصيانة يخدم قادة التقنية الذين لم يعودوا يقبلون مهلة ربط الأنظمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من MuleSoft Composer AI 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وتفعيل تدفقات Composer + تدريب فرق العمليات:</strong> 8–18 يومًا — 2200–14500 دولار.</li>
          <li><strong>مراقبة وتحسين تدفقات شهريًا:</strong> — 480–1920 دولار/عميل/شهر.</li>
          <li><strong>حزمة 6 قوالب تكامل عربية (مبيعات، مخزون، موارد بشرية):</strong> — 98–392 دولار/حزمة.</li>
          <li><strong>ورش «تكامل أنظمة ذكي بالعربية مع MuleSoft Composer»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">MuleSoft</span>
        <span class="tag">Integration</span>
        <span class="tag">Salesforce</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Workiva AI Disclosure 2 Arabic: امتثال وإفصاح — تقارير SEC وتقارير داخلية تُفهم قبل الموعد النهائي!</h2>
      <p class="article-lead">«لجنة المراجعة تطلب توضيحًا عن بند مخاطر في التقرير السنوي — والفريق يعيد صياغة الليلة كاملة». في 24 نوفمبر 2026، أطلقت <strong>Workiva</strong> <strong>Workiva AI Disclosure 2 Arabic</strong>: مساعد ذكاء داخل منصة Workiva يلخّص مسودات الإفصاح المالية والحوكمة، يُقارن إصدارات المستندات ويُبرز التغييرات الحرجة، يُترجم مقاطع تقنية إلى فصحى إدارية واضحة للمجالس، يُتحقق من تناسق الأرقام عبر الأقسام، يُقترح بنود امتثال ناقصة حسب معيار الإفصاح، يُجهّد ملخصات عربية للمستثمرين المحليين، يتكامل مع XBRL وSOC ومراجعات داخلية، ويحفظ مسار تدقيق كامل — للشركات المدرجة والبنوك وشركات التقنية في MENA ذات إفصاحات مزدوجة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُنتج ملخصات إنجليزية فقط؛ الإصدار 2 يدعم ثنائية اللغة في نفس المستند، قوالب «تقرير مجلس» و«مخاطر سيبرانية» و«حوكمة بيئية»، تنبيهات عند تعارض أرقام، تكامل مع Microsoft 365 وGoogle Workspace، ومسار تصعيد لمدقق بشري معتمد.</p>
      <p>القدرات الأساسية: تلخيص إفصاحات؛ مقارنة إصدارات؛ فصحى إدارية؛ فحص تناسق أرقام؛ مسار تدقيق.</p>
      <p>للمبدعين العرب: استشارات «امتثال يتكلم العربية» — من يُعد Workiva AI لقسم مراجعة 20–200 موظفًا بـ3100–22800 دولار للإطلاق + 520–2100 دولار/شهر للصيانة يجذب مكاتب التي تُجهّد تقارير ربع سنوية تحت ضغط المواعيد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Workiva AI Disclosure 2 Arabic؟</h3>
        <ul>
          <li><strong>رفع قوالب إفصاح + تفعيل AI + تدريب فريق المراجعة:</strong> 10–22 يومًا — 3100–22800 دولار.</li>
          <li><strong>مراجعة مواسم الإفصاح وتحسين القوالب:</strong> — 520–2100 دولار/مؤسسة/شهر.</li>
          <li><strong>حزمة 8 ملخصات إدارية عربية لقطاعات (بنوك، تقنية، طاقة):</strong> — 115–460 دولار/حزمة.</li>
          <li><strong>ورش «إفصاح ذكي بالعربية مع Workiva AI»:</strong> — 58–232 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Workiva</span>
        <span class="tag">Compliance</span>
        <span class="tag">Finance</span>
        <span class="tag">Disclosure</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Deel HR AI 3 Arabic: فرق موزّعة عالميًا — عقود، رواتب، وضرائب بإجابة عربية واحدة!</h2>
      <p class="article-lead">«مؤسسة توظّف في خمس دول — وكل سؤال عن عقد مصر أو ضريبة السعودية يتحول إلى سلسلة إيميلات طويلة». في 24 نوفمبر 2026، أطلقت <strong>Deel</strong> <strong>Deel HR AI 3 Arabic</strong>: مساعد موارد بشرية عالمي داخل منصة Deel يقرأ عقود العمل المصرح بها، يُجيب عن الإجازات والمكافآت ومواعيد الدفع بالفصحى أو بلهجة مكتبية مختارة، يُرشد الموظف والمدير لخطوات التوظيف عن بُعد، يُلخّص تغييرات قانون العمل في دول محددة بلغة مبسّطة، يُقترح وصف وظيفة ثنائي اللغة من مسمى إنجليزي، يتكامل Payroll والامتثال والفواتير، ويُنبّه عند تجاوز ميزانية headcount — للشركات الناشئة والوكالات ذات 30–5000 متعاقد في منطقة الشرق الأوسط وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُخطئ في تفاصيل ضريبية محلية؛ الإصدار 3 يدعم مصر والسعودية والإمارات والأردن والمغرب، قوالب FAQ للموظفين والمديرين، تصعيد للخبراء البشريين عند استثناءات، ترجمة سياسات الشركة الداخلية، ولوحة تحليل أسئلة شائعة لتحسين السياسات.</p>
      <p>القدرات الأساسية: إجابات عقود عالمية؛ إرشاد توظيف عن بُعد؛ ملخصات قانونية مبسّطة؛ أوصاف وظائف؛ تكامل رواتب وامتثال.</p>
      <p>للمبدعين العرب: خدمة «HR عالمي بدون تذاكر لا تنتهي» — من يُفعّل Deel HR AI لشركة 40–800 موظفًا موزّعين بـ1750–12800 دولار + 390–1580 دولار/شهر للصيانة يخدم المؤسسات التي تنمو أسرع من قدرتهم على توظيف أخصائي موارد بشرية في كل دولة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Deel HR AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تكوين عقود ودول + رفع سياسات + تدريب:</strong> 7–15 يومًا — 1750–12800 دولار.</li>
          <li><strong>صيانة FAQ وتحديثات قانونية شهريًا:</strong> — 390–1580 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 قالب إجابة عربية (إجازة، إنهاء، مكافأة، تأشيرة):</strong> — 78–312 دولار/حزمة.</li>
          <li><strong>ورش «توظيف عالمي ذكي بالعربية مع Deel HR AI»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Deel</span>
        <span class="tag">HR</span>
        <span class="tag">Remote</span>
        <span class="tag">Payroll</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>PandaDoc Contract AI 3 Arabic: من العرض إلى التوقيع — عقود RTL، تتبّع، وتحليلات إغلاق!</h2>
      <p class="article-lead">«المبيعات أغلقت verbally — والعقد يَتأخر لأن الصياغة تمرّ بثلاث جهات». في 24 نوفمبر 2026، أطلقت <strong>PandaDoc</strong> <strong>PandaDoc Contract AI 3 Arabic</strong>: محرك عقود ذكي داخل PandaDoc يحوّل ملخص الصفقة بالعربية إلى مسودة اتفاقية خدمات أو شراكة أو اشتراك SaaS، يُقترح بنود دفع وإنهاء وسرية مناسبة لسوق MENA، يُولّد ملحقات وشروط SLA، يُتابع من فتح العرض حتى التوقيع، يُرسل تذكيرات عربية عبر البريد وواتساب Business، يُحلّل أين تتوقف الصفقات في المسار، يتكامل CRM ودفع إلكتروني، ويحترم التواقيع الإلكترونية المعتمدة — للوكالات والشركات البرمجية والخدمات المهنية في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: PandaDoc AI Hub 4 ركّز على قوالب عامة؛ Contract AI 3 يخصّص نبرة العلامة، يميّز أنواع الصفقات بالعربية، يُقترح تسعيرًا شهريًا وسنويًا في جداول RTL، يُنبّه المدير عند تعديل العميل بنود حرجة، يُصدّر PDF عربي، وبرنامج «PandaDoc Revenue Partners Arabic» للوكالات التي تبيع الإعداد كحزمة.</p>
      <p>القدرات الأساسية: مسودات عقود عربية؛ تتبّع توقيع؛ تذكيرات ذكية؛ تحليل مسار الصفقة؛ تكامل CRM.</p>
      <p>للمبدعين العرب: استوديو «عقود تُغلق الصفقة» — من يُسلّم مكتبة 15 عقدًا ذكيًا + تدريب فريق مبيعات بـ980–7200 دولار للمشروع يجذب من يخسرون صفقات بسبب بطء الأوراق لا بسبب السعر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من PandaDoc Contract AI 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء مكتبة عقود + قواعد نبرة + ربط CRM:</strong> 4–11 يومًا — 980–7200 دولار.</li>
          <li><strong>تحسين معدل إغلاق وA/B للبنود شهريًا:</strong> — 260–1050 دولار/عميل/شهر.</li>
          <li><strong>حزمة 7 عقود عربية جاهزة (وكالة، SaaS، استشارات، NDA):</strong> — 92–368 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات تُوقّع أسرع بالعربية مع PandaDoc Contract AI»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">PandaDoc</span>
        <span class="tag">Contracts</span>
        <span class="tag">Sales</span>
        <span class="tag">eSign</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 24-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="24-11-2026 -- 04-PM.html">
          📰 24 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "24-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/24-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/24-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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