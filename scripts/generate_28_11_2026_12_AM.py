#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 28-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "28-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Zendesk AI Copilot 3 Arabic · Oracle Fusion Cloud AI 3 Arabic · "
    "Snowflake Cortex AI 3 Arabic · UiPath Autopilot 5 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Zendesk AI Copilot 3 Arabic، Oracle Fusion Cloud AI 3 Arabic، Snowflake Cortex AI 3 Arabic، UiPath Autopilot 5 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 28 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Zendesk AI Copilot 3 Arabic الذي يُغلق تذكرة الدعم ويُرسل ملخصًا بالفصحى قبل أن يرحل العميل غاضبًا، إلى Oracle Fusion Cloud AI 3 Arabic الذي يُجيب مسؤول الموارد البشرية عن سياسة الإجازات من بيانات الشركة الحقيقية، ومن Snowflake Cortex AI 3 Arabic الذي يُحوّل مستودع البيانات إلى محادثة عربية تُنتج تقارير دون SQL، إلى UiPath Autopilot 5 Arabic الذي يُشغّل روبوتًا يُنجز مهمة يدوية مملة بعد أمر واحد بالعربية — أربع قصص ليلية في 28 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء الساعة الصفراء!</h1>
      <p class="hero-sub">ليلة الدعم والموارد البشرية والبيانات والأتمتة: العملاء يشعرون بالاهتمام، القرارات تُستند إلى أنظمة موحدة، الأرقام تتكلّم بوضوح، والروبوتات تحرّر الفريق من التكرار. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 28 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Zendesk AI Copilot 3 Arabic: مركز الدعم يتحدث — إجابات، تصعيد، ورضا قبل أن يغلق العميل المحادثة!</h2>
      <p class="article-lead">«العميل ينتظر منذ عشرين دقيقة — والوكيل يبحث في تسع تبويبات ليجد سياسة الإرجاع». في 28 نوفمبر 2026، أطلقت <strong>Zendesk</strong> <strong>Zendesk AI Copilot 3 Arabic</strong>: مساعد ذكي داخل مركز الدعم يقرأ تذاكر العملاء وسجل المحادثات ومركز المساعدة، يُقترح ردودًا بالفصحى أو باللهجة المصرية أو الخليجية حسب إعدادات العلامة، يُلخّص سلسلة طويلة من الشكاوى إلى نقاط قابلة للحل، يُنفّذ إجراءات (إرجاع، ترقية خطة، إعادة إرسال فاتورة) ضمن صلاحيات محددة، يُصعّد للإنسان مع سياق عربي كامل، يتكامل Shopify وSalesforce وSlack، يُقيس رضا بعد كل تذكرة، ويُرسل «تقرير ليل الخدمة» لمدير العمليات — لتجارة إلكترونية وبنوك رقمية واتصالات وتعليم إلكتروني في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot 2 كان يخلط بين لهجتين في رسالة واحدة ويُسيء فهم أرقام الطلبات المحلية؛ الإصدار 3 يُثبت نبرة الرد، يقرأ التواريخ بصيغتها المحلية، يدعم قوالب «تتبع شحنة» و«تعديل اشتراك» و«شكوى فوترة»، يُنبّه عند سؤال يتطلّب موافقة قانونية، يُولّد ملخصات QA للتدريب الداخلي بالعربية، مسار شريك Zendesk MENA، وتدريب على حماية البيانات الشخصية في قطاع الدفع والصحة.</p>
      <p>القدرات الأساسية: اقتراح ردود عربية؛ إجراءات مؤتمتة؛ تصعيد ذكي؛ تكامل CRM وتجارة؛ تقارير ليلية للإدارة.</p>
      <p>للمبدعين العرب: استوديو «تجربة دعم ذكية» — من يُفعّل Copilot لفرق 15–120 وكيلًا بـ1580–11800 دولار إعدادًا + 395–1580 دولار/شهر للتحسين يخدم علامات تخسر عملاء بسبب بطء الدعم لا جودة المنتج.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zendesk AI Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مركز مساعدة + قوالب ردود + تدريب الوكلاء:</strong> 8–18 يومًا — 1580–11800 دولار/عميل.</li>
          <li><strong>مراجعة محادثات وتحسين نبرة العلامة شهريًا:</strong> — 395–1580 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 ماكرو عربي (إرجاع، اشتراك، فوترة، شحن):</strong> — 76–304 دولار/حزمة.</li>
          <li><strong>ورش «خدمة عملاء ذكية بالعربية مع Zendesk»:</strong> — 50–200 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zendesk</span>
        <span class="tag">Support</span>
        <span class="tag">CX</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Oracle Fusion Cloud AI 3 Arabic: ERP يُجيب — موارد بشرية، مالية، ومشتريات بلسان المؤسسة!</h2>
      <p class="article-lead">«موظف يسأل عن رصيد إجازته الساعة 11 مساءً — ولا أحد في الموارد البشرية متاح». في 28 نوفمبر 2026، أطلقت <strong>Oracle</strong> <strong>Oracle Fusion Cloud AI 3 Arabic</strong>: طبقة ذكاء فوق منصة Fusion تفهم أسئلة الموظفين والمديرين بالعربية، تُجيب عن سياسات الإجازات والبدلات وخطط التأمين من بيانات الشركة المخزنة، تُساعد المالية في مسودات تقارير وتفسير انحرافات الميزانية، تُسرّع إجراءات المشتريات (موافقة مورد، مقارنة عروض)، تُلخّص لوحات تنفيذية للإدارة، تحترم صلاحيات الوصول والامتثال المحلي، تتكامل مع أنظمة الحكومة الإلكترية حيث تتوفر، وتُصدّر «نشرة ليل العمليات» لرئيس المالية — للشركات الصناعية والتجزئة الكبرى والجهات الحكومية 500–50 ألف موظف في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُرجع إجابات عامة من دليل إنجليزي؛ الإصدار 3 يربط كل رد بسجل الموظف أو طلب الشراء الفعلي، يدعم تقويم هجري وعملات محلية، يُنبّه عند طلب يتجاوز حدّ الموافقة، يُولّد نماذج عربية جاهزة للتوقيع الداخلي، مسار شريك Oracle MENA للتنفيذ، وتدريب على فصل البيانات بين الفروع والشركات التابعة.</p>
      <p>القدرات الأساسية: أسئلة موارد بشرية عربية؛ تفسير مالي؛ مساعدة مشتريات؛ ملخصات تنفيذية؛ حوكمة وامتثال.</p>
      <p>للمبدعين العرب: شركاء تنفيذ Oracle — من يُطلق Fusion AI لقسم موارد بشرية أو مالية بـ4200–68000 دولار حسب الحجم + 880–4200 دولار/شهر للدعم يبني خط إيرادات طويل الأمد مع مؤسسات تغرق في تذاكر الداخلية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Oracle Fusion Cloud AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل وحدات AI + ربط سياسات + تدريب المستخدمين:</strong> 14–45 يومًا — 4200–68000 دولار/مشروع.</li>
          <li><strong>صيانة مطالبات وقوالب تقارير شهريًا:</strong> — 880–4200 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 سيناريو عربي (إجازة، سلفة، مصروف، أمر شراء):</strong> — 120–480 دولار/حزمة.</li>
          <li><strong>ورش «موظف ذكي داخل ERP بالعربية»:</strong> — 62–248 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Oracle</span>
        <span class="tag">ERP</span>
        <span class="tag">HR</span>
        <span class="tag">Finance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Snowflake Cortex AI 3 Arabic: مستودع البيانات يتكلّم — تقارير، تنبؤات، وتطبيقات ذكاء بلا SQL معقد!</h2>
      <p class="article-lead">«المدير يريد إجابة عن هامش الربح حسب المنطقة — والفريق يستعد لاجتماع ليلي مع جداول SQL». في 28 نوفمبر 2026، أطلقت <strong>Snowflake</strong> <strong>Snowflake Cortex AI 3 Arabic</strong>: منصة ذكاء داخل Snowflake تسمح بأسئلة عربية طبيعية على البيانات المخزنة، تُولّد استعلامات آمنة وتقارير مرئية، تُبني تطبيقات RAG فوق مستندات الشركة دون نقل البيانات خارج المنصة، تُدير نماذج متعددة ضمن سياسة تكلفة واحدة، تُترجم النتائج إلى لغة أعمال عربية للإدارة، تتكامل مع Tableau وPower BI وSlack، تحترم قواعد إخفاء الهوية والصلاحيات، وتُرسل «تنبيه ليل الأرقام» عند انحراف مؤشر حرج — للتجزئة والبنوك والاتصالات والرعاية الصحية التي تخزّن بياناتها على Snowflake في المنطقة.</p>
      <p>المشكلة التي حلّتها: Cortex 2 كان يُنتج رسومًا بلا شرح عربي واضح؛ الإصدار 3 يُرفق كل إجابة بمصادر الجداول المستخدمة، يُقترح خطوات تحقيق عند شذوذ، يدعم Arabic OCR في ملفات PDF المرفوعة، يُمكّن مسارات موافقة بشرية قبل إرسال تقارير حساسة، برنامج شريك Snowflake MENA، وتدريب فرق البيانات على prompt engineering بالعربية للمؤسسات.</p>
      <p>القدرات الأساسية: أسئلة عربية على البيانات؛ RAG آمن؛ حوكمة نماذج؛ تقارير تنفيذية؛ تكامل BI.</p>
      <p>للمبدعين العرب: استوديو «بيانات تُجيب» — من يُشغّل Cortex لتطبيق تحليلي أو لوحة CFO بـ2400–32000 دولار إطلاق + 520–2400 دولار/شهر للمراقبة يخدم شركات تملك البيانات ولا تملك الوقت لبناء فرق ذكاء من الصفر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم نموذج بيانات + تطبيق Cortex + تدريب المحللين:</strong> 10–28 يومًا — 2400–32000 دولار/مشروع.</li>
          <li><strong>تحسين استعلامات ومراقبة تكلفة النماذج شهريًا:</strong> — 520–2400 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 لوحات عربية جاهزة (مبيعات، مخزون، اشتراكات، مخاطر):</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «تحليلات محادثة بالعربية على Snowflake»:</strong> — 54–216 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Data</span>
        <span class="tag">RAG</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>UiPath Autopilot 5 Arabic: موظف رقمي من وصف واحد — أتمتة، موافقات، وتقارير بلا نقرات لا تنتهي!</h2>
      <p class="article-lead">«كل صباح نفس الخمسين خطوة: تنزيل تقرير، تنسيقه، إرساله لثلاثة مديرين، وانتظار الموافقة». في 28 نوفمبر 2026، أطلقت <strong>UiPath</strong> <strong>UiPath Autopilot 5 Arabic</strong>: مساعد أتمتة يفهم أوامرك بالعربية، يُنشئ روبوتات desktop وAPI ووثائق PDF ومراسلات بريد دون برمجة تقليدية، يُسجّل خطواتك ويُحوّلها إلى تدفق قابل لإعادة التشغيل، يتكامل SAP وOracle وMicrosoft 365 وGoogle Workspace، يدعم موافقات بشرية عند العمليات الحساسة، يُقيس توفير الساعات لكل قسم، يُولّد دليل تشغيل بالفصحى للموظفين الجدد، ويُرسل «ملخص ليل الأتمتة» لقائد التحول الرقمي — للبنوك والتأمين والخدمات المشتركة والجهات الحكومية التي لا تزال تغرق في العمل اليدوي.</p>
      <p>المشكلة التي حلّتها: Autopilot 4 كان يتعثر عند واجهات عربية RTL في تطبيقات قديمة؛ الإصدار 5 يتعرّف على عناصر الواجهة بالعربية، يُميّز بين نسخ ملف متشابهة، يُنبّه عند محاولة أتمتة عملية مخالفة للسياسة، يدعم تصدير سجل التدقيق للامتثال، مسار شريك UiPath MENA، وتدريب مراكز التميز على إدارة أسطول روبوتات متعدد اللغات.</p>
      <p>القدرات الأساسية: أوامر عربية؛ روبوتات هجينة؛ تكامل ERP؛ حوكمة؛ تقارير توفير وقت.</p>
      <p>للمبدعين العرب: مكتب «أتمتة بالعربية» — من يُسلّم ثلاثة روبوتات إنتاجية لقسم واحد بـ2800–24000 دولار + 620–2800 دولار/شهر للصيانة يحوّل UiPath إلى مصدر دخل متكرر لدى مؤسسات تدفع الآن لموظفين يكررون ما يمكن للآلة إنجازه.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من UiPath Autopilot 5 Arabic؟</h3>
        <ul>
          <li><strong>اكتشاف عمليات + بناء روبوتات + تسليم تشغيلي:</strong> 12–35 يومًا — 2800–24000 دولار/قسم.</li>
          <li><strong>مراقبة أداء وإصلاح تدفقات شهريًا:</strong> — 620–2800 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب عربية (فواتير، onboarding، تقارير، موافقات):</strong> — 96–384 دولار/حزمة.</li>
          <li><strong>ورش «موظف رقمي بالعربية مع UiPath Autopilot»:</strong> — 58–232 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">UiPath</span>
        <span class="tag">RPA</span>
        <span class="tag">Automation</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 28-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="28-11-2026 -- 12-AM.html">
          📰 28 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "28-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/28-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/28-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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