#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 3 Arabic · Workday Illuminate AI 2 Arabic · "
    "Sprinklr AI+ 4 Arabic · Tableau Pulse AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 3 Arabic، Workday Illuminate AI 2 Arabic، Sprinklr AI+ 4 Arabic، Tableau Pulse AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 3 Arabic الذي يُبنّي وكيلًا يتحدث مع عملائك بالفصحى ويُنفّذ إجراءات في CRM قبل أن ينتهي اجتماع المبيعات، إلى Workday Illuminate AI 2 Arabic الذي يُترجم سياسات الموارد البشرية ويوصي بمسار ترقية مبني على بيانات حقيقية، ومن Sprinklr AI+ 4 Arabic الذي يُوحّد ردود واتساب وإنستغرام وتيك توك بصوت واحد متسق للعلامة، إلى Tableau Pulse AI 3 Arabic الذي يُرسل لمديرك ملخصًا عربيًا عن سبب انخفاض المبيعات قبل أن يغلق الفرع — أربع قصص مسائية في 27 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء ساعة الغروب!</h1>
      <p class="hero-sub">مساء الوكلاء والموارد البشرية والتسويق والتحليلات: المحادثات تُدار، القرارات تُستند إلى أرقام، العملاء يشعرون بالاهتمام، والتقارير تتكلّم العربية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 27 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 3 Arabic: ابنِ وكيلك الذي يفهم العربية — محادثة، إجراء، وامتثال في منصة واحدة!</h2>
      <p class="article-lead">«العميل يكتب بالعربية على Teams — والبوت يرد بالإنجليزية ثم يتوقف عند طلب فاتورة». في 27 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Microsoft Copilot Studio 3 Arabic</strong>: منصة بناء وكلاء مؤسسيين تفهم الفصحى واللهجات المهنية الشائعة في MENA، تربط Dynamics 365 وSharePoint وDataverse وPower Automate، تُنفّذ إجراءات (فتح تذكرة، تحديث عميل، حجز موعد) بعد تأكيد السياسة، تُولّد محتوى ردود متوافقًا مع دليل العلامة، تدعم قنوات Teams وWhatsApp ومواقع الويب، تحترم Azure AI Content Safety وسجلات التدقيق، تُمكّن مسار موافقة بشري للعمليات الحساسة، وتُصدّر تحليلات «محادثات مسائية» لقائد الخدمة — للبنوك والتجزئة والاتصالات 200–25 ألف موظف على منظومة Microsoft.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يخلط بين لهجات في جملة واحدة ويُسيء فهم الأرقام العربية الهندية؛ الإصدار 3 يثبت لهجة الرد، يقرأ التواريخ والمبالغ بصيغتها المحلية، يدعم قوالب «استفسار فاتورة» و«تتبع شحنة» و«طلب عرض سعر»، يُنبّه عند سؤال خارج نطاق الوكيل، يتكامل Semantic Kernel لربط أدوات خارجية، مسار شريك Microsoft MENA لبناء وكلاء جاهزين، وتدريب على حدود البيانات الشخصية في أنظمة الدفع.</p>
      <p>القدرات الأساسية: وكلاء عربية؛ إجراءات متصلة؛ قنوات متعددة؛ حوكمة؛ تحليلات مسائية.</p>
      <p>للمبدعين العرب: استوديو «وكيل الخدمة بالعربية» — من يُصمّم 3–6 وكلاء لعميل 500–5000 مستخدم بـ1920–14400 دولار إعدادًا + 480–1920 دولار/شهر للتحسين يخدم مؤسسات تغرق في محادثات متقطعة عبر قنوات مختلفة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وكلاء + ربط أنظمة + اختبار محادثات:</strong> 10–20 يومًا — 1920–14400 دولار.</li>
          <li><strong>مراجعة نية المستخدم وتحسين الردود شهريًا:</strong> — 480–1920 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب حوار عربي جاهزة (خدمة، مبيعات، موارد بشرية):</strong> — 92–368 دولار/حزمة.</li>
          <li><strong>ورش «وكلاء ذكيون بالعربية مع Copilot Studio»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot</span>
        <span class="tag">Agents</span>
        <span class="tag">Dynamics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Workday Illuminate AI 2 Arabic: موارد بشرية تنطق بلسان الموظف — سياسات، مسارات، وتنبيهات ذكية!</h2>
      <p class="article-lead">«الموظف يقرأ سياسة الإجازة الإنجليزية ثلاث مرات ولا يزال غير متأكد — وموارد بشرية تغرق في نفس السؤال». في 27 نوفمبر 2026، أطلقت <strong>Workday</strong> <strong>Workday Illuminate AI 2 Arabic</strong>: طبقة ذكاء فوق منصة Workday HCM تُجيب عن المزايا والإجراءات واللوائح من مستندات معتمدة بالعربية، تُلخّص تغييرات السياسة الجديدة في فقرة واضحة، تُقترح مسارات تعلم وتطوير مبنية على مهارات الموظف الفعلية، تُنبّه المدير بفجوات في التغطية قبل موعد إجازة جماعية، تتكامل مع Journeys وSkills Cloud وLearning، تحترم صلاحيات البيانات حسب الدولة، وتُرسل «نشرة مساء الموارد البشرية» للقيادة — لمؤسسات عابرة للحدود 1000–80 ألف موظف في الخليج وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: Illuminate 1 كان يعتمد على ترجمة آلية لنصوص قانونية؛ الإصدار 2 يستخدم معجمًا مصطلحيًا عربيًا للعمل، يفرّق بين إرشاد عام ونص ملزم، يدعم أسئلة صوتية قصيرة، يُصعّد الحالات التي تمس الإنهاء أو التأشيرات لخبير بشري، مسار شريك Workday للاستشارات، وقوالب «تأهيل مدير جديد» و«سياسة عمل مرن» جاهزة بالعربية.</p>
      <p>القدرات الأساسية: إجابات عربية موثّقة؛ ملخصات سياسات؛ توصيات مهارات؛ تنبيهات تغطية؛ تقارير قيادة.</p>
      <p>للمبدعين العرب: باقة «Illuminate للمؤسسة العربية» — من يرفع سياسات معتمدة ويُفعّل المساعد لشركة 800–6000 موظف بـ2050–16200 دولار + 512–2050 دولار/شهر للحوكمة يبيع وضوحًا لفرق كانت تخسر أيامًا في تفسير اللوائح.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Workday Illuminate AI 2 Arabic؟</h3>
        <ul>
          <li><strong>ترجمة سياسات + مسارات موافقة + تدريب مديرين:</strong> 12–24 يومًا — 2050–16200 دولار.</li>
          <li><strong>تدقيق إجابات وتحديث سياسات شهريًا:</strong> — 512–2050 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 سؤالًا شائعًا عربيًا جاهزة (إجازات، تعويضات، أداء):</strong> — 98–392 دولار/حزمة.</li>
          <li><strong>ورش «موارد بشرية ذكية بالعربية مع Workday Illuminate»:</strong> — 55–220 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Workday</span>
        <span class="tag">HCM</span>
        <span class="tag">HR</span>
        <span class="tag">Illuminate</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Sprinklr AI+ 4 Arabic: صوت واحد للعلامة على كل الشبكات — ردود، تحليل مشاعر، وحملات لحظية!</h2>
      <p class="article-lead">«تعليق غاضب على إنستغرام — ورد مختلف على تويتر — والعميل يشعر أنّ الشركة لا تسمعه». في 27 نوفمبر 2026، أطلقت <strong>Sprinklr</strong> <strong>Sprinklr AI+ 4 Arabic</strong>: طبقة ذكاء لإدارة التجربة الرقمية تفهم العربية واللهجات الشائعة في التعليقات والرسائل الخاصة، تُقترح ردودًا متسقة مع نبرة العلامة (رسمية، ودية، شبابية محكومة)، تُصنّف المشاعر والنوايا وتُصعّد الأزمات فورًا، تُولّد مسودات حملات قصيرة مرتبطة بحدث رياضي أو موسم تسوق، تتكامل مع مراكز الاتصال والإعلانات، تحترم جداول النشر والموافقات، وتُرسل «لوحة مساء السمعة» لمدير التسويق — لعلامات تجزئة واتصالات وسياحة 50–500 شخص في فرق التسويق والرعاية.</p>
      <p>المشكلة التي حلّتها: الإصدار 3 كان يُبالغ في الألفة أو يستخدم مصطلحات غير مناسبة للسوق الخليجي؛ الإصدار 4 يتيح ملفات نبرة حسب بلد، يكتشف تهديدات قانونية وإساءة، يدعم ردودًا شبه آلية مع موافقة لحملات الحساسية العالية، مسار «Sprinklr MENA Partners» للوكالات، وتدريب على أرشفة المحادثات للامتثال.</p>
      <p>القدرات الأساسية: ردود عربية موحّدة؛ تصنيف مشاعر؛ مسودات حملات؛ تصعيد أزمات؛ لوحة مسائية.</p>
      <p>للمبدعين العرب: وكالة «صوت العلامة بالعربية» — من يُعدّ دليل نبرة ويُفعّل AI+ لعلامة 5–20 قناة بـ1780–13600 دولار + 445–1780 دولار/شهر للمراقبة يخدم شركات تخسر ثقة العملاء بسبب ردود متناقضة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sprinklr AI+ 4 Arabic؟</h3>
        <ul>
          <li><strong>دليل نبرة + قواعد تصعيد + ربط قنوات:</strong> 8–18 يومًا — 1780–13600 دولار.</li>
          <li><strong>مراجعة ردود وتحليل أزمات شهريًا:</strong> — 445–1780 دولار/عميل/شهر.</li>
          <li><strong>حزمة 24 قالب رد عربي جاهز (شكوى، استفسار، مديح):</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «إدارة سمعة ذكية بالعربية مع Sprinklr»:</strong> — 50–200 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sprinklr</span>
        <span class="tag">CX</span>
        <span class="tag">Social</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Tableau Pulse AI 3 Arabic: أرقامك تتحدث معك — ملخصات عربية، تفسير، وتنبيه قبل المفاجأة!</h2>
      <p class="article-lead">«لوحة Tableau مليئة بالرسوم — والمدير يسأل: لماذا تراجعت المبيعات في جدة؟ ولا أحد يجيب قبل الاجتماع غدًا». في 27 نوفمبر 2026، أطلقت <strong>Tableau</strong> <strong>Tableau Pulse AI 3 Arabic</strong>: مساعد تحليلات يشرح المؤشرات بلغة عربية واضحة داخل بريدك وTeams، يُبرز التغييرات المهمة في الإيرادات والتكاليف والتحويل، يُقترح أسئلة متابعة («هل السبب خصم المنافس أم نقص مخزون؟»)، يربط التفسير بصفحة التصور المناسبة، يحترم صلاحيات كل مستخدم على البيانات، يدعم تقويمًا هجريًا وتقويمًا ميلاديًا في التقارير، ويُرسل «موجز مساء المؤشرات» لكل مدير فرع — لشركات تجزئة وتصنيع وخدمات 30–300 محلل بيانات في المنطقة.</p>
      <p>المشكلة التي حلّتها: Pulse 2 كان يُطيل الشرح أو يخلط بين العملات؛ الإصدار 3 يختصر إلى ثلاث نقاط قابلة للتنفيذ، يُوسم مستوى الثقة في كل استنتاج، يُنبّه عند بيانات ناقصة قد تُضلّل القرار، يتكامل Einstein Trust Layer، مسار Salesforce MENA للتنفيذ، وقوالب «مؤشرات متجر» و«مخزون» و«رضا عميل» بالعربية.</p>
      <p>القدرات الأساسية: شرح عربي؛ تنبيهات مؤشرات؛ أسئلة متابعة؛ روابط تصور؛ موجز مسائي.</p>
      <p>للمبدعين العرب: مكتب «تحليلات تُفهم بالعربية» — من يربط مصادر بيانات ويُفعّل Pulse لـ 15–80 مديرًا بـ1680–13200 دولار + 420–1680 دولار/شهر لضبط المؤشرات يبيع سرعة قرار لفرق كانت تنتظر أيامًا لترجمة الأرقام.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Tableau Pulse AI 3 Arabic؟</h3>
        <ul>
          <li><strong>ربط بيانات + تعريف مؤشرات + تدريب مديرين:</strong> 9–18 يومًا — 1680–13200 دولار.</li>
          <li><strong>مراجعة تفسيرات وضبط عتبات تنبيه شهريًا:</strong> — 420–1680 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 موجزات مؤشرات عربية جاهزة:</strong> — 90–360 دولار/حزمة.</li>
          <li><strong>ورش «قرارات أسرع بالعربية مع Tableau Pulse»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Tableau</span>
        <span class="tag">Analytics</span>
        <span class="tag">BI</span>
        <span class="tag">Salesforce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-11-2026 -- 04-PM.html">
          📰 27 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/27-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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