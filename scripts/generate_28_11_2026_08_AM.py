#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 28-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "28-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Wix Astro 2 Arabic · Gong Engage AI 4 Arabic · "
    "Typeform AI Insights 3 Arabic · Calendly AI Scheduling 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Wix Astro 2 Arabic، Gong Engage AI 4 Arabic، Typeform AI Insights 3 Arabic، Calendly AI Scheduling 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 28 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Wix Astro 2 Arabic الذي يُحوّل وصفًا عربيًا لعلامتك إلى موقعًا ومتجرًا ومقاطع ترويجية قبل أن تبرد قهوتك، إلى Gong Engage AI 4 Arabic الذي يُراجع مكالمات المبيعات ويُكتب متابعات بالفصحى تُفتح، ومن Typeform AI Insights 3 Arabic الذي يُترجم آلاف إجابات الاستبيان إلى قرارات منتج وعروض باللغة التي يفهمها الفريق، إلى Calendly AI Scheduling 3 Arabic الذي يُملأ تقويمك ويُرسل دعوات عربية ويُقيس أي موعد يُغلق الصفقة — أربع قصص صباحية في 28 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباح المواقع والمبيعات والبيانات والمواعيد: حضورك الرقمي يُبنى، الصفقات تتحرك، العملاء يُسمَعون، والتقويم يعمل كبائع صامت. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 28 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Wix Astro 2 Arabic: موقعك ومتجرك من جملة عربية — صفحات، SEO، وحملة قبل أن ينتهي اجتماع الصباح!</h2>
      <p class="article-lead">«العميل يريد موقعًا ومتجرًا يعملان غدًا — والفريق لا يزال يختار القالب المناسب». في 28 نوفمبر 2026، أطلقت <strong>Wix</strong> <strong>Wix Astro 2 Arabic</strong>: مساعد ذكاء داخل Wix يفهم وصفك بالعربية، يُبني هيكل موقع RTL بصفحات (من نحن، خدمات، اتصل بنا، مدونة)، يُصمم متجرًا إلكترونيًا مع فئات ومنتجات وعربة دفع، يُولّد نصوص SEO وعناوين جذابة، يُنشئ مقاطع ترويجية قصيرة وهوية بصرية متسقة، يتكامل مع Google Analytics وMeta Pixel وSalla وZapier، يدعم الدفع المحلي وواتساب للتجارة، ويُصدّر قائمة مهام للمطور عند الحاجة — للمطاعم والعيادات والمدربين والوكالات الصغيرة في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُنتج نصوصًا عامة بلا نبرة علامة؛ Astro 2 يقرأ ملف brand kit الخاص بك، يُميّز بين الفصحى واللهجة التجارية، يدعم قوالب «حجز موعد» و«بطاقة طعام» و«دورة رقمية»، يُنبّه عند ادعاء تسويقي يحتاج مراجعة قانونية، مسار شركاء Wix MENA، وتدريب على ربط النطاق والدفع والشحن المحلي.</p>
      <p>القدرات الأساسية: بناء موقع عربي؛ متجر جاهز؛ SEO ومحتوى؛ فيديو ترويجي؛ تكامل تسويق.</p>
      <p>للمبدعين العرب: استوديو «أطلق خلال أسبوع» — من يُسلّم موقعًا ومتجرًا كاملين بـ720–8900 دولار حسب التعقيد + 180–720 دولار/شهر للتحديثات يخدم آلاف المشاريع التي تبدأ متأخرة لأن التصميم يستهلك الوقت.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Wix Astro 2 Arabic؟</h3>
        <ul>
          <li><strong>جلسة اكتشاف + بناء موقع/متجر + تدريب العميل:</strong> 5–14 يومًا — 720–8900 دولار/مشروع.</li>
          <li><strong>صيانة محتوى وتحسين تحويل شهريًا:</strong> — 180–720 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 صفحة عربية جاهزة (خدمة، عرض، شهادات، مدونة):</strong> — 68–272 دولار/حزمة.</li>
          <li><strong>ورش «موقعك الأول بالعربية مع Wix Astro»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Wix</span>
        <span class="tag">Website</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Gong Engage AI 4 Arabic: مكالمات المبيعات تُترجم لقرار — متابعات، ملخصات، وتنبيهات قبل الاجتماع التالي!</h2>
      <p class="article-lead">«مدير المبيعات يسمع عشرين مكالمة يوميًا — ولا يعرف أيها يستحق متابعة عربية قوية». في 28 نوفمبر 2026، أطلقت <strong>Gong</strong> <strong>Gong Engage AI 4 Arabic</strong>: ذكاء داخل منصة Gong يُحلّل مكالمات الفيديو والصوت بالعربية والإنجليزية، يُلخّص نقاط الاعتراض والفرص وخطوة الإغلاق التالية، يُكتب متابعات بريد ورسائل LinkedIn بصوت فريقك، يُقارن أداء المندوبين حسب اللهجة والقطاع، يتكامل Salesforce وHubSpot وMicrosoft Dynamics، يُنبّه عند ذكر منافس أو مخاطر امتثال، يُولّد بطاقة اجتماع عربية قبل كل demo، ويُرسل «نشرة صباح المبيعات» لرئيس الإيرادات — لشركات SaaS والخدمات المهنية والتعليم B2B في المنطقة.</p>
      <p>المشكلة التي حلّتها: Engage 3 كان يُخطئ في المصطلحات المحلية ولا يفصل بين الفصحى واللهجة في رسالة واحدة؛ الإصدار 4 يثبت لهجة كل مندوب، يدعم تسجيلات WhatsApp voice حيث يسمح الامتثال، يُقترح playbooks عربية جاهزة لقطاعات (تعليم، عقار، لوجستيات)، برنامج شريك Gong MENA، وتدريب على حماية بيانات العملاء في المكالمات المسجّلة.</p>
      <p>القدرات الأساسية: تفريغ وتحليل عربي؛ متابعات تلقائية؛ رؤى فريق؛ تكامل CRM؛ تنبيهات مخاطر.</p>
      <p>للمبدعين العرب: مكتب «مبيعات مدعومة بالذكاء» — من يُفعّل Gong لفرق 8–60 مندوبًا بـ1900–16500 دولار إعدادًا + 480–1950 دولار/شهر للتحسين يخدم شركات تخسر صفقات بسبب متابعات ضعيفة لا بسبب المنتج.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gong Engage AI 4 Arabic؟</h3>
        <ul>
          <li><strong>ربط CRM + تفعيل التسجيل + قوالب متابعة عربية:</strong> 7–21 يومًا — 1900–16500 دولار/عميل.</li>
          <li><strong>مراجعة مكالمات وتحسين playbooks شهريًا:</strong> — 480–1950 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 سيناريو اعتراض عربي (سعر، توقيت، منافس، موافقة):</strong> — 82–328 دولار/حزمة.</li>
          <li><strong>ورش «إغلاق أسرع بالعربية مع Gong Engage»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gong</span>
        <span class="tag">Sales</span>
        <span class="tag">Revenue</span>
        <span class="tag">Coaching</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Typeform AI Insights 3 Arabic: الاستبيان يتحدث — قرارات منتج وعروض من آلاف الإجابات بلسان بسيط!</h2>
      <p class="article-lead">«أرسلنا استبيانًا لخمسة آلاف عميل — والنتائج عالقة في جداول لا يقرأها أحد قبل اجتماع المنتج». في 28 نوفمبر 2026، أطلقت <strong>Typeform</strong> <strong>Typeform AI Insights 3 Arabic</strong>: طبقة ذكاء فوق نماذج Typeform تقرأ الإجابات المفتوحة والمقياسية، تُلخّص المشاعر والطلبات بالفصحى، تُقترح ميزات وتحسينات بناءً على أنماط متكررة، تُولّد تقارير تنفيذية بجمل قصيرة للإدارة، تقسم النتائج حسب البلد واللغة والقناة، تتكامل Slack وNotion وHubSpot وGoogle Sheets، تُنبّه عند تراجع مؤشر رضا مفاجئ، وتُصدّر «ملخص صباح العميل» أسبوعيًا — للشركات الناشئة والتجزئة والتعليم والخدمات التي تعتمد على ملاحظات الجمهور.</p>
      <p>المشكلة التي حلّتها: Insights 2 كان يُجمّع أرقامًا بلا سياق لهجات عربية متعددة في نفس الاستبيان؛ الإصدار 3 يُصنّف الردود بلهجة كتابة المتجاوب، يدعم RTL في العرض التلقائي، يُولّد أسئلة متابعة ذكية للجولة الثانية، مسار شركاء Typeform للوكالات، وتدريب على تصميم استبيانات لا تحيز النتائج.</p>
      <p>القدرات الأساسية: تحليل نصوص عربية؛ تقارير تنفيذية؛ تكامل أدوات العمل؛ تنبيهات؛ اقتراح أسئلة.</p>
      <p>للمبدعين العرب: استوديو «صوت العميل» — من يُصمّم مسار استبيان + لوحة insights بـ580–6200 دولار + 145–580 دولار/شهر للمراجعة يخدم شركات تدفع لاستشارات بلا بيانات منظمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Typeform AI Insights 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم استبيان + تفعيل Insights + ورشة قراءة نتائج:</strong> 4–12 يومًا — 580–6200 دولار/مشروع.</li>
          <li><strong>مراجعة شهريّة وتحديث أسئلة المتابعة:</strong> — 145–580 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب استبيان عربي (رضا، NPS، ما قبل الإطلاق، تسعير):</strong> — 58–232 دولار/حزمة.</li>
          <li><strong>ورش «قرارات من بيانات العملاء بالعربية»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Typeform</span>
        <span class="tag">Surveys</span>
        <span class="tag">Product</span>
        <span class="tag">Insights</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Calendly AI Scheduling 3 Arabic: تقويم يبيع — دعوات عربية، أوقات ذكية، ومتابعة تلقائية بعد كل اجتماع!</h2>
      <p class="article-lead">«المستشار يضيع ساعات في رسائل «متى يناسبك؟» — والصفقة تبرد قبل أن يُحدَّد الموعد». في 28 نوفمبر 2026، أطلقت <strong>Calendly</strong> <strong>Calendly AI Scheduling 3 Arabic</strong>: مساعد جدولة يفهم تعليماتك بالعربية، يُكتب دعوات بريد ورسائل واتساب بصوت مهني، يُقترح أوقاتًا حسب منطقة العميل وسلوك الإلغاء السابق، يُوجّه الاجتماع للمندوب المناسب حسب اللغة والقطاع، يتكامل Salesforce وHubSpot وZoom وGoogle Calendar، يُرسل تذكيرات وتعليمات ما قبل الاجتماع، يُلخّص النتائج أسبوعيًا لمدير المبيعات، ويُقيس أي قالب عربي يحقق حضورًا أعلى — للمستشارين والوكالات والعيادات والمدربين الذين يبيعون بالمواعيد.</p>
      <p>المشكلة التي حلّتها: Scheduling 2 كان يُرسل نصوصًا مترجمة بلا احترام السياق الثقافي؛ الإصدار 3 يدعم تهنئة رسمية وصياغة خليجية ومصرية، يتعامل مع تقويم هجري للتنبيهات حسب الحاجة، يُنبّه عند تعارض مع إجازة الفريق، مسار شركاء Calendly للوكالات، وتدريب على ربط الدفع بعد الاجتماع لمقدمي الخدمات.</p>
      <p>القدرات الأساسية: دعوات عربية؛ توجيه ذكي؛ تذكيرات؛ تكامل CRM؛ تحليل أداء.</p>
      <p>للمبدعين العرب: خدمة «تقويم يُغلق» — من يُبني مسار حجز كامل بـ650–4800 دولار + 165–780 دولار/شهر للتحسين يخدم مئات المستقلين الذين يخسرون عملاء بسبب بطء التنسيق.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Calendly AI Scheduling 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد أنواع اجتماعات + قوالب عربية + ربط CRM:</strong> 3–10 أيام — 650–4800 دولار/عميل.</li>
          <li><strong>اختبار عناوين وتوقيت وتحسين التحويل شهريًا:</strong> — 165–780 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 قالب دعوة (استشارة، عرض، متابعة، إعادة حجز):</strong> — 55–220 دولار/حزمة.</li>
          <li><strong>ورش «املأ تقويمك بالعربية مع Calendly AI»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Calendly</span>
        <span class="tag">Scheduling</span>
        <span class="tag">Sales</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 28-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="28-11-2026 -- 08-AM.html">
          📰 28 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "28-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/28-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/28-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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