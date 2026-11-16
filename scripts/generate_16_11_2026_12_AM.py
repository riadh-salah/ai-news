#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "16-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "xAI Grok Workspace 2 Arabic · Airtable AI Omni 3 Arabic · "
    "Harvey AI Legal 2 Arabic · Spline AI 3D Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — xAI Grok Workspace 2 Arabic، Airtable AI Omni 3 Arabic، Harvey AI Legal 2 Arabic، Spline AI 3D Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 16 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من xAI Grok Workspace 2 Arabic الذي يُجمع بريدك وتقاويمك وملفاتك في غرفة عمل ذكية تُجيب بالفصحى قبل أن يرن المنبّه، إلى Airtable AI Omni 3 Arabic الذي يُحوّل جداولك المتناثرة إلى وكلاء يُنفّذون تقارير ومتابعات ليلًا، ومن Harvey AI Legal 2 Arabic الذي يُراجع عقودك ويُلخّص بنود المخاطر بلغة قانونية عربية واضحة، إلى Spline AI 3D Arabic الذي يُولّد مشاهد تفاعلية ثلاثية الأبعاد لمواقعك وتطبيقاتك من وصف عربي — أربع قصص ليلية في 16 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ لرواد الأعمال وفرق العمليات والمحامين والمصممين الرقميين: المكتب الذكي صار مترجمًا عربيًا، قواعد البيانات صارت فريقًا مستقلًا، القانون صار مساعدًا سريعًا، والتصميم ثلاثي الأبعاد صار نصًا واحدًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 16 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>xAI Grok Workspace 2 Arabic: مكتب ذكي يفهم بريدك وجدولك — تقارير، ردود، وتلخيص!</h2>
      <p class="article-lead">«مئتا رسالة بريد ومكالمة السابعة صباحًا — وأريد ملخصًا لما يخص العميل الكبير قبل أن أنهض من السرير». في 16 نوفمبر 2026، أطلقت <strong>xAI</strong> <strong>Grok Workspace 2 Arabic</strong>: مساحة عمل تربط Gmail وOutlook وGoogle Calendar وSlack وDrive في طبقة واحدة، تفهم أوامر بالفصحى واللهجات الخليجية والمصرية في سياق مهني، تُعدّ مسودات ردود رسمية، تُلخّص سلاسل طويلة، تُنبّهك بالتعارضات في المواعيد، وتُولّد تقريرًا صباحيًا جاهزًا للفريق — لمؤسسي الشركات ومديري المبيعات والاستشاريين في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُبالغ في الثقة أو يُهمل خصوصية الرسائل؛ Workspace 2 يُقسّم الصلاحيات بحسب الدور، يُخفي البيانات الحساسة من السجلات المشتركة، يُحسّن الأسلوب الإداري العربي، يدعم قوالب «إحاطة يومية» و«ملخص اجتماع» و«رد على استفسار عميل»، يتكامل مع Teams وNotion، وبرنامج شريك «Grok Workspace Partner MENA».</p>
      <p>القدرات الأساسية: Arabic unified inbox intelligence؛ جدولة ذكية مع اقتراح بدائل؛ تصدير PDF وWord؛ وضع مؤسسي مع تدقيق؛ اختصارات صوتية بالعربية.</p>
      <p>للمبدعين العرب: خدمة «مكتب تنفيذي مؤتمت» للشركات المتوسطة — من يُدير 15 عميلًا باشتراك 280–1100 دولار/شهر + إعداد سير عمل 700–3800 دولار يبيع وقتًا تنفيذيًا بلا توظيف مساعدين إضافيين.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من xAI Grok Workspace 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مكتب ذكي متكامل لكل شركة:</strong> 5–12 يومًا — 700–3800 دولار/عميل.</li>
          <li><strong>اشتراك تشغيل وتحسين أسبوعي:</strong> — 280–1100 دولار/شهر.</li>
          <li><strong>حزم قوالب (مبيعات، موارد بشرية، استشارات):</strong> — 80–340 دولار/حزمة.</li>
          <li><strong>ورش «إنتاجية المدير بالذكاء الاصطناعي»:</strong> — 55–230 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">xAI</span>
        <span class="tag">Grok</span>
        <span class="tag">Workspace</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Airtable AI Omni 3 Arabic: الجدول يُصبح فريق عمل — أتمتة، تقارير، ومتابعة!</h2>
      <p class="article-lead">«قاعدة بيانات المشاريع في خمس جداول — والمدير يريد تقرير حالة بالعربية كل ليلة دون أن أجلس ساعتين». في 16 نوفمبر 2026، أطلقت <strong>Airtable</strong> <strong>AI Omni 3 Arabic</strong>: طبقة وكلاء فوق القواعد والواجهات، تفهم الأوامر بالفصحى، تُحدّث السجلات، تُرسل تذكيرات واتساب وSlack، تُولّد لوحات عرض RTL، تُقارن إصدارات البيانات، وتُنفّذ سيناريوهات «إذا تأخر المورد فأرسل تنبيهًا للمدير» — لفرق العمليات والتوريد والتسويق والفعاليات في الشرق الأوسط.</p>
      <p>المشكلة التي حلّتها: Omni 2 كان يُخطئ في الحقول المترابطة أو يُكرر التنبيهات؛ الإصدار 3 يُعرّف سياسات موافقة قبل التعديلات الحساسة، يدعم مصطلحات عربية مخصصة لكل شركة، يتكامل مع Zapier وMake دون كسر التدفقات، يُشغّل وضع «مدير مشروع» و«محلل مبيعات» و«منسق فعاليات»، وبرنامج «Airtable AI Partner Gulf».</p>
      <p>القدرات الأساسية: Arabic natural-language automations؛ تقارير مجدولة بالفصحى؛ ربط CRM ومتاجر؛ سجل تدقيق؛ قوالب قطاعية جاهزة.</p>
      <p>للمبدعين العرب: وكالة «تحويل Excel إلى نظام حي خلال أسبوع». من يبيع 10 مشاريع شهريًا بـ1600–9200 دولار للمشروع + 320–1400 دولار/شهر للصيانة يحوّل جداول ميتة إلى محرّك تنفيذ ليلي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable AI Omni 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء نظام تشغيل مؤسسي على Airtable:</strong> 7–18 يومًا — 1600–9200 دولار/مشروع.</li>
          <li><strong>صيانة وكلاء ومتابعة شهرية:</strong> — 320–1400 دولار/شهر.</li>
          <li><strong>قوالب قطاع (عقارات، تعليم، لوجستيات):</strong> — 95–420 دولار/قالب.</li>
          <li><strong>تدريب فرق على الأتمتة الذكية بالعربية:</strong> — 65–270 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">Omni</span>
        <span class="tag">Automation</span>
        <span class="tag">Operations</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Harvey AI Legal 2 Arabic: مساعد قانوني يقرأ العقود — ملخص، مخاطر، ومقارنة!</h2>
      <p class="article-lead">«عقد إيجار تجاري بثلاثين صفحة — أحتاج قائمة بنود الخطر وصياغة ملاحظات للعميل قبل جلسة المحكمة». في 16 نوفمبر 2026، أطلقت <strong>Harvey</strong> <strong>AI Legal 2 Arabic</strong>: منصة للمحامين وفرق الامتثال تُحلّل مستندات PDF وWord، تُستخرج الالتزامات والمواعيد والغرامات، تُقارن إصدارات العقود، تُولّد ملخصات بالفصحى القانونية، تُقترح أسئلة تفاوض، وتُحترم سرية الملفات مع تشفير وعزل بيانات — لمكاتب المحاماة والشركات العقارية والتأمين والتقنية في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُسيء ترجمة المصطلحات أو يتجاهل أنظمة محلية؛ Legal 2 يتضمن قواميس لقوانين دول مجلس التعاون ومصر والأردن كمرجع إرشادي، يُميّز بين الفصحى القانونية والشرح للعميل، يدعم التعليقات التعاونية، يُصدّر تقارير جاهزة للطباعة، وبرنامج «Harvey Legal Partner MENA».</p>
      <p>القدرات الأساسية: Arabic contract intelligence؛ جدولة مراجعات دورية؛ قوالب NDA وتوظيف وشراكة؛ تكامل مع Microsoft 365؛ وضع تدقيق للمؤسسات.</p>
      <p>للمبدعين العرب: عرض «مراجعة عقد خلال 24 ساعة» مدعوم بأدوات Harvey — من يخدم 20 عميلًا شركة بـ400–2800 دولار/عقد أو اشتراك 500–2200 دولار/شهر يُسرّع الخدمة القانونية دون مضاعفة عدد المحامين المبتدئين.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Harvey AI Legal 2 Arabic؟</h3>
        <ul>
          <li><strong>مراجعة وتلخيص عقود مع تقرير مخاطر:</strong> — 400–2800 دولار/عقد حسب الحجم.</li>
          <li><strong>اشتراك امتثال لشركات متوسطة:</strong> — 500–2200 دولار/شهر.</li>
          <li><strong>قوالب بنود عربية معتمدة لقطاعك:</strong> 3–6 أيام — 600–3100 دولار.</li>
          <li><strong>دورات «الذكاء الاصطناعي للمحامين العرب»:</strong> — 70–290 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Harvey</span>
        <span class="tag">Legal</span>
        <span class="tag">Contracts</span>
        <span class="tag">Compliance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Spline AI 3D Arabic: مشاهد ثلاثية الأبعاد من وصف عربي — مواقع، تطبيقات، وإعلانات!</h2>
      <p class="article-lead">«العميل يريد صفحة هبوط فيها منتج يدور ثلاثي الأبعاد وزر شراء بالعربية — والموعد بعد يومين». في 16 نوفمبر 2026، أطلقت <strong>Spline</strong> <strong>AI 3D Arabic</strong>: مولّد داخل منصة Spline يفهم برومبتات بالفصحى، يُنشئ كائنات ومشاهد تفاعلية، يُضبط الإضاءة والحركة، يُصدّر كود embed خفيفًا لمواقع React وWordPress، يدعم اتجاه RTL في النصوص ثلاثية الأبعاد، ويتكامل مع Figma وWebflow — للوكالات الرقمية ومصممي المنتجات وصناع الإعلانات الذين يستهدفون جمهورًا عربيًا.</p>
      <p>المشكلة التي حلّتها: الإصدارات السابقة كانت تتطلب خبرة نمذجة يدوية؛ Spline AI 3D يُولّد نماذج أولية قابلة للتحرير، يُحسّن الأداء للهواتف، يُتيح أنماط «منتج تسويقي» و«خلفية هيرو» و«أيقونة تطبيق»، يدعم تصدير فيديو قصير للإعلانات، وبرنامج «Spline AI Partner Studio MENA».</p>
      <p>القدرات الأساسية: Arabic prompt-to-3D؛ تحكم بالمواد والألوان؛ معاينة فورية؛ مكتبة مشاهد للبيع؛ تحسين للويب والجوال.</p>
      <p>للمبدعين العرب: باقة «هيرو ثلاثي الأبعاد لموقعك خلال 48 ساعة». من ينفّذ 8 مشاريع شهريًا بـ1200–6800 دولار للمشروع يُميّز العلامات بمحتوى بصري نادر دون استوديو إنتاج تقليدي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Spline AI 3D Arabic؟</h3>
        <ul>
          <li><strong>مشهد تفاعلي لصفحة هبوط أو تطبيق:</strong> 2–5 أيام — 1200–6800 دولار/مشروع.</li>
          <li><strong>اشتراك إنتاج مشاهد شهرية للفرق:</strong> — 450–1800 دولار/شهر.</li>
          <li><strong>بيع حزم مشاهد جاهزة (تقنية، عقارات، تجزئة):</strong> — 60–280 دولار/حزمة.</li>
          <li><strong>معسكر «تصميم ثلاثي الأبعاد بالذكاء الاصطناعي»:</strong> — 48–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Spline</span>
        <span class="tag">3D</span>
        <span class="tag">Design</span>
        <span class="tag">Web</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 16-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="16-11-2026 -- 12-AM.html">
          📰 16 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "16-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/16-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/16-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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