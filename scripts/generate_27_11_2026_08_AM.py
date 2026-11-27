#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google Workspace Vids AI 2 Arabic · Elastic AI Assistant 4 Arabic · "
    "Glean AI 6 Arabic · Rippling AI Workforce 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Workspace Vids AI 2 Arabic، Elastic AI Assistant 4 Arabic، Glean AI 6 Arabic، Rippling AI Workforce 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Google Workspace Vids AI 2 Arabic الذي يُحوّل مذكرة واحدة إلى فيديو تدريبي عربي جاهز للنشر قبل أن تبرد قهوتك، إلى Elastic AI Assistant 4 Arabic الذي يُطارد الأخطاء في السجلات ويُصوغ دليل إصلاح بالفصحى بينما فريقك يراجع التقارير، ومن Glean AI 6 Arabic الذي يُعثر على القرار والملف والبريد عبر كل أنظمة الشركة في ثوانٍ، إلى Rippling AI Workforce 3 Arabic الذي يُجيب موظفيك عن السياسات ويُشغّل إجراءات الموارد البشرية بلهجة مهنية عربية — أربع قصص صباحية في 27 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباح الفيديو والعمليات والمعرفة والموارد البشرية: المحتوى يُنتج، الحوادث تُحلّ، المعلومات تُعثر عليها، والفرق تعرف حقوقها وواجباتها. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 27 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Workspace Vids AI 2 Arabic: من فكرة إلى فيديو شرح — سيناريو، صوت، ومقاطع في دقائق!</h2>
      <p class="article-lead">«المدير يريد فيديو onboarding عربيًا غدًا — والمونتير مشغول أسبوعًا». في 27 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>Google Workspace Vids AI 2 Arabic</strong>: أداة فيديو داخل Workspace تفهم وصفك بالعربية، تُولّد سيناريوًا بفصول وعناوين فرعية، تُقترح لقطات من مكتبة Google وأصول العلامة، تُولّد تعليقًا صوتيًا بلهجة مهنية (فصحى، خليجية، مصرية) مع ضبط الإيقاع، تُضيف ترجمة عربية تلقائية وRTL في الشاشة، تتكامل Drive وSlides وGmail وMeet، تحترم سياسات العلامة والخطوط المعتمدة، وتُصدّر نسخة قصيرة للسوشيال ونسخة طويلة للتدريب — للشركات والجامعات والوكالات 50–8000 موظف على Google Workspace في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُخرج نصوصًا عامة بلا سياق داخلي؛ الإصدار 2 يقرأ مستنداتك في Drive كمصادر موثّقة، يُنبّه عند ادعاء غير مدعوم بملف، يدعم قوالب «سياسة أمن معلومات» و«منتج جديد» و«تدريب مبيعات»، يُمكّن الموافقة البشرية قبل النشر، مسار شريك Google Cloud MENA للمستشارين، وتدريب على حقوق الموسيقى والصور التجارية.</p>
      <p>القدرات الأساسية: سيناريو عربي؛ صوت ولغة؛ فصول وملخص؛ تكامل Workspace؛ تصدير متعدد الصيغ.</p>
      <p>للمبدعين العرب: استوديو «فيديو الشركة بالعربية» — من يُعدّ مسار Vids لعميل 200–3000 موظف بـ1760–13800 دولار إعدادًا + 440–1760 دولار/شهر للقوالب يخدم مؤسسات تتعثر في إنتاج محتوى تدريبي بطيء.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Workspace Vids AI 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد قوالب فيديو + هوية بصرية + تدريب فرق:</strong> 7–16 يومًا — 1760–13800 دولار.</li>
          <li><strong>إنتاج فيديوهات شهرية (onboarding، منتج، امتثال):</strong> — 440–1760 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب سيناريو عربي جاهزة:</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «فيديو تدريبي ذكي بالعربية مع Workspace Vids»:</strong> — 50–200 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Video</span>
        <span class="tag">Workspace</span>
        <span class="tag">Training</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Elastic AI Assistant 4 Arabic: من إنذار إلى حل — سجلات، أسباب جذرية، ودليل تشغيل!</h2>
      <p class="article-lead">«النظام بطيء منذ الفجر — والمهندس يقلب ملايين السطور دون أن يعرف السبب». في 27 نوفمبر 2026، أطلقت <strong>Elastic</strong> <strong>Elastic AI Assistant 4 Arabic</strong>: مساعد أمن وعمليات داخل Elastic Stack يفهم استفسارك بالعربية، يُرابط بين logs وtraces وmetrics وSIEM alerts، يُقترح سلسلة أسباب محتملة مع مستوى ثقة، يُولّد runbook خطوة بخطوة للفريق الليلي، يُترجم تقارير تقنية إلى ملخص تنفيذي للمدير، يتكامل PagerDuty وSlack وJira وServiceNow، يحترم RBAC ولا يُظهر بيانات حساسة لغير المصرّحين، ويُرسل «نشرة صباحية للحوادث» — لشركات fintech واتصالات وتجارة إلكترونية 15–500 مهندس DevOps في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 3 كان يُبالغ في الربط بين أحداث غير مرتبطة؛ الإصدار 4 يُقيّم الأدلة قبل الاستنتاج، يدعم قوالب حوادث شائعة (دفع، تسجيل دخول، API latency)، يُنبّه عند فرضية تحتاج تحقيقًا يدويًا، يُحفظ سياق التحقيق للمراجعة اللاحقة، مسار شريك Elastic MENA، وتدريب امتثال على سجلات العملاء المحمية.</p>
      <p>القدرات الأساسية: تحقيق عربي؛ runbooks؛ ملخصات إدارية؛ تكامل on-call؛ حوكمة وصول.</p>
      <p>للمبدعين العرب: مكتب «عمليات ذكية» — من يُفعّل Assistant لمركز NOC/SOC صغير بـ1980–15200 دولار + 495–1980 دولار/شهر لتحسين القواعد يبيع راحة لفرق نائمة على الإنذارات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Elastic AI Assistant 4 Arabic؟</h3>
        <ul>
          <li><strong>ربط مصادر + قواعد كشف + تدريب on-call:</strong> 12–22 يومًا — 1980–15200 دولار.</li>
          <li><strong>مراجعة runbooks وتحسين تنبيهات شهريًا:</strong> — 495–1980 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 runbooks عربي جاهزة (أداء، أمن، تكامل):</strong> — 95–380 دولار/حزمة.</li>
          <li><strong>ورش «مراقبة ذكية بالعربية مع Elastic AI»:</strong> — 54–216 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Elastic</span>
        <span class="tag">DevOps</span>
        <span class="tag">Security</span>
        <span class="tag">Observability</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Glean AI 6 Arabic: ابحث في الشركة كأنك تملك الذاكرة — ملفات، قرارات، وبريد!</h2>
      <p class="article-lead">«من وافق على خصم العميل الكبير؟ الإجابة «في مكان ما» — والصفقة تنتظر». في 27 نوفمبر 2026، أطلقت <strong>Glean</strong> <strong>Glean AI 6 Arabic</strong>: محرك معرفة مؤسسي يفهرس Slack وGoogle وMicrosoft وSalesforce وJira وConfluence وZendesk وNotion، يُجيب أسئلة بالعربية مع اقتباسات من المصدر، يُميّز بين نسخ المستندات والإصدارات الرسمية، يُلخّص threads طويلة إلى قرار واحد، يُقترح خبراء داخليين لسؤالك، يحترم صلاحيات كل مستخدم، يدعم لهجات مهنية متعددة، يتكامل SSO وSCIM، ويُرسل «موجز صباح المعرفة» لكل مدير — لمؤسسات استشارية وتقنية وتصنيع 200–15000 موظف.</p>
      <p>المشكلة التي حلّتها: الإصدار 5 كان يُخلط بين مسودات وموافقات نهائية؛ الإصدار 6 يُوسم حالة المستند، يُنبّه عند تعارض سياسات قديمة وجديدة، يدعم استعلامات صوتية قصيرة بالعربية، مسار امتثال للقطاعات المنظمة، وبرنامج شريك «Glean Knowledge MENA» لوكالات التي تبني «مكتبات ذاكرة» لعملائها.</p>
      <p>القدرات الأساسية: بحث موثّق؛ تلخيص؛ خبراء داخليون؛ حوكمة؛ موجز صباحي.</p>
      <p>للمبدعين العرب: خدمة «ذاكرة الشركة» — من يربط 8–20 مصدرًا لعميل 500–8000 موظف بـ2100–16800 دولار + 525–2100 دولار/شهر للحوكمة يبيع ساعات باهظة كانت تُهدر في البحث عن القرارات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Glean AI 6 Arabic؟</h3>
        <ul>
          <li><strong>فهرسة مصادر + سياسات وصول + تدريب:</strong> 10–20 يومًا — 2100–16800 دولار.</li>
          <li><strong>تدقيق نتائج وتحسين استعلامات شهريًا:</strong> — 525–2100 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 سؤالًا مؤسسيًا عربيًا جاهزًا:</strong> — 100–400 دولار/حزمة.</li>
          <li><strong>ورش «بحث مؤسسي ذكي بالعربية مع Glean»:</strong> — 56–224 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Glean</span>
        <span class="tag">Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Rippling AI Workforce 3 Arabic: موارد بشرية تُجيب — إجازات، رواتب، وسياسات بلا طابور انتظار!</h2>
      <p class="article-lead">«موظف جديد يسأل عن رصيد الإجازة والتأمين — وقسم الموارد البشرية يرد بعد ساعتين». في 27 نوفمبر 2026، أطلقت <strong>Rippling</strong> <strong>Rippling AI Workforce 3 Arabic</strong>: مساعد موظفين ومديرين داخل منصة HR الموحدة، يُجيب عن السياسات والمزايا والإجراءات بالعربية من مستندات معتمدة، يُطلق طلبات إجازة وتعديل بيانات مع مسارات موافقة، يُلخّص كشوف الرواتب للموظف بلغة بسيطة، يُذكّر المدير بمراجعات الأداء الموعودة، يتكامل Payroll وIT وApps، يدعم قوانين عمل متعددة الدول في MENA، يحترم الخصوصية، ويُرسل تقرير «صباح الموارد البشرية» للقيادة — لشركات ناشئة ومتوسطة 30–2000 موظف بنوا Rippling كـ system of record.</p>
      <p>المشكلة التي حلّتها: Workforce 2 كان يُجيب نصوصًا إنجليزية مترجمة حرفيًا؛ الإصدار 3 يفهم لوائح محلية (عمل عن بُعد، نهاية خدمة، تأشيرات)، يُصعّد الحالات الحساسة لموظف بشري، يدعم قوالب «عقد عمل» و«سياسة سفر» عربية، مسار شريك للمستشارين في التوظيف، وتدريب مديري خط على حدود ما يجيب عنه الذكاء الاصطناعي.</p>
      <p>القدرات الأساسية: أسئلة عربية؛ طلبات وموافقات؛ ملخص رواتب؛ تذكيرات؛ تقارير قيادة.</p>
      <p>للمبدعين العرب: باقة «موارد بشرية ذكية» — من يُفعّل Workforce لشركة 80–600 موظفًا بـ1640–12800 دولار + 410–1640 دولار/شهر للتحديث يخدم مؤسسات تتوسع بسرعة وتغرق في أسئلة متكررة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Rippling AI Workforce 3 Arabic؟</h3>
        <ul>
          <li><strong>رفع سياسات + مسارات موافقة + تدريب:</strong> 8–18 يومًا — 1640–12800 دولار.</li>
          <li><strong>مراجعة إجابات وتحديث سياسات شهريًا:</strong> — 410–1640 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 سياسة عربية جاهزة (إجازات، سلوك، أمن معلومات):</strong> — 86–344 دولار/حزمة.</li>
          <li><strong>ورش «خدمة موظف ذكية بالعربية مع Rippling»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Rippling</span>
        <span class="tag">HR</span>
        <span class="tag">Payroll</span>
        <span class="tag">Workforce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-11-2026 -- 08-AM.html">
          📰 27 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/27-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
        "dolgar",
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