#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "21-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI ChatGPT Advanced Voice 3 Arabic · Miro AI Workflows 3 Arabic · "
    "Coursera Coach AI 2 Arabic · Asana AI Teammates 5 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI ChatGPT Advanced Voice 3 Arabic، Miro AI Workflows 3 Arabic، Coursera Coach AI 2 Arabic، Asana AI Teammates 5 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من OpenAI ChatGPT Advanced Voice 3 Arabic الذي يُجيبك بصوت طبيعي بالفصحى ويُترجم مكالمتك مع شريك أجنبي لحظة بلحظة، إلى Miro AI Workflows 3 Arabic الذي يُحوّل ورشة عصف ذهني فوضوية إلى خطة تنفيذ ومهام في Jira قبل أن تبرد قهوتك، ومن Coursera Coach AI 2 Arabic الذي يُصمّم مسار تعلم مخصصًا ويُختبرك بأسئلة عربية كأن معك مدربًا خاصًا، إلى Asana AI Teammates 5 Arabic الذي يُوزّع المهام ويُلخص تقدّم مشروعك للمدير بأمر عربي واحد — أربع قصص صباحية في 21 نوفمبر 2026 لروّاد الأعمال والمبدعين الذين يريدون أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ لفرق المبيعات والتعليم وإدارة المشاريع: صوتك يتحدث بذكاء، اللوحة البيضاء تُنتج قرارات، التعلم يُصبح تجربة شخصية، والمشاريع تسير دون اجتماعات طويلة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 21 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI ChatGPT Advanced Voice 3 Arabic: محادثة صوتية حية بالعربية — ترجمة، سياق، وعمل في الوقت الفعلي</h2>
      <p class="article-lead">«أنا أقود السيارة والعميل يريد توضيحًا للعقد بالعربية بينما المستشار يتحدث الإنجليزية — لا وقت لإيقاف كل شيء». في 21 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>ChatGPT Advanced Voice 3 Arabic</strong>: تجربة صوتية ثنائية الاتجاه تفهم الفصحى واللهجات الخليجية والمصرية والشامية، تُترجم لحظيًا بين العربية والإنجليزية والفرنسية والألمانية، تُلخص المكالمة بعد انتهائها بملخص عربي موثّق، تُنفّذ مهامًا بسيطة مثل إرسال بريد أو جدولة موعد عبر تكاملات معتمدة، تُحترم سياسات الخصوصية للمؤسسات، وتدعم وضع «مترجم احترافي» للمفاوضات التجارية — لفرق المبيعات والاستشارات والتعليم عن بُعد في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يقطع الجمل الطويلة أو يخلط بين اللهجات؛ Advanced Voice 3 يحسّن التعرف على الأسماء العربية، يقلّل التأخير إلى أقل من ثانية في معظم المناطق، يدعم قواميس مصطلحات مخصّصة لكل عميل، وضعًا صامتًا للاجتماعات الحساسة، تكامل Teams وZoom عبر إضافات، حماية من تسجيل غير مصرّح، وبرنامج «OpenAI Voice Partners MENA» للمطبّقين المعتمدين.</p>
      <p>القدرات الأساسية: صوت عربي طبيعي؛ ترجمة فورية؛ ملخصات مكالمات؛ مهام عبر تكاملات؛ امتثال مؤسسي.</p>
      <p>للمبدعين العرب: استوديو «مكالمات ثنائية اللغة» — من يُسلّم إعداد Voice للفرق بـ580–4200 دولار للعميل + 180–1100 دولار/شهر للدعم يخدم شركات تصدّر وخدمات تُجري مكالمات يومية مع أسواق أجنبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI ChatGPT Advanced Voice 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد صوتي كامل (قواميس، سياسات، تدريب فرق):</strong> 3–8 أيام — 580–4200 دولار/عميل.</li>
          <li><strong>صيانة وتحسين جودة ترجمة شهريًا:</strong> — 180–1100 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 سيناريو صوتي جاهز (مبيعات، دعم، تعليم):</strong> — 95–380 دولار/حزمة.</li>
          <li><strong>ورش «مكالمات ذكية بالعربية مع ChatGPT Voice»:</strong> — 45–188 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Voice</span>
        <span class="tag">Translation</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Miro AI Workflows 3 Arabic: من لوحة فوضوية إلى خطة تنفيذ — ورش عمل، قرارات، وتذاكر جاهزة</h2>
      <p class="article-lead">«ساعتان ورشة عمل على اللوحة — والفريق ما زال يسأل: ماذا نفعل غدًا؟». في 21 نوفمبر 2026، أطلقت <strong>Miro</strong> <strong>AI Workflows 3 Arabic</strong>: طبقة ذكاء داخل لوحات Miro تقرأ الملاحظات والرسومات بالعربية، تُصنّف الأفكار حسب الأولوية، تُولّد خطة تنفيذ بجدول زمني، تُنشئ بطاقات Jira وAsana وLinear تلقائيًا، تُلخّص قرارات الاجتماع للمديرين الذين لم يحضروا، تُقترح خطوات تالية ومسؤولين، وتُصدّر عرضًا تقديميًا RTL للعميل — للوكالات وفرق المنتج والاستراتيجية التي تعتمد ورش العصف الذهني.</p>
      <p>المشكلة التي حلّتها: Workflows 2 كان يتجاهل التعليقات العربية المكتوبة بخط اليد الافتراضي أو يُكرر مهامًا مكررة؛ الإصدار 3 يفهم RTL في كل القوالب، قوالب «إطلاق منتج» و«حملة تسويق» و«تحول رقمي»، ربطًا مع Slack وMicrosoft Teams، مراجعة بشرية قبل إنشاء التذاكر، أرشفة بحث عربي، وبرنامج «Miro Solution Partners Arabia».</p>
      <p>القدرات الأساسية: تحليل لوحة عربية؛ خطط تنفيذ؛ تكامل مهام؛ ملخصات إدارية؛ قوالب قطاعية.</p>
      <p>للمبدعين العرب: استشارة «ورشة تُنتج قرارًا» — من يُدير 8 ورش شهريًا بـ1400–7500 دولار للعميل يختصر أسبوع تنسيق في يوم واحد دون مشرف مشاريع بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Miro AI Workflows 3 Arabic؟</h3>
        <ul>
          <li><strong>ورشة استراتيجية كاملة (لوحة + خطة + تذاكر):</strong> 2–5 أيام — 1400–7500 دولار/مشروع.</li>
          <li><strong>تشغيل قوالب ورش وتحسين شهريًا:</strong> — 420–1680 دولار/فريق/شهر.</li>
          <li><strong>حزمة 6 قوالب قطاعية جاهزة:</strong> — 280–1120 دولار/مجموعة.</li>
          <li><strong>دورات «ورش منتجة بالعربية مع Miro AI»:</strong> — 48–195 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Miro</span>
        <span class="tag">Workshops</span>
        <span class="tag">Planning</span>
        <span class="tag">Collaboration</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Coursera Coach AI 2 Arabic: مدرب تعلم شخصي بالعربية — مسارات، اختبارات، وشهادات بلا انتظار</h2>
      <p class="article-lead">«الموظفون يريدون تطوير مهاراتهم لكن لا أحد يتابع من أنهى الدورة ومن يحتاج دعمًا إضافيًا». في 21 نوفمبر 2026، أطلقت <strong>Coursera</strong> <strong>Coach AI 2 Arabic</strong>: مساعد تعلم داخل منصة Coursera for Business يقيّم مستوى المتعلم بالعربية، يُقترح مسارًا من دورات معتمدة، يُجري اختبارات تفاعلية ويُفسّر الإجابات بلهجة واضحة، يُذكّر بالمواعيد النهائية، يُولّد ملخصات دروس، يتكامل مع أنظمة الموارد البشرية الشائعة، ويُصدر تقارير تقدم للمدير بالفصحى — للشركات والجامعات وأكاديميات التدريب في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Coach الأول كان يخلط بين مصطلحات تقنية مترجمة حرفيًا؛ الإصدار 2 يستخدم عربية تعليمية سليمة، يدعم مسارات «ذكاء اصطناعي» و«إدارة مشاريع» و«تسويق رقمي» و«لغة إنجليزية مهنية»، تتبعًا للامتثال التدريبي في القطاعات المنظّمة، تكامل SAML وSSO، لوحة مدير عربية، وبرنامج «Coursera Learning Partners MENA».</p>
      <p>القدرات الأساسية: مسارات مخصصة؛ اختبارات تفاعلية؛ تذكيرات وتقارير؛ تكامل HR؛ محتوى معتمد عالميًا.</p>
      <p>للمبدعين العرب: خدمة «أكاديمية الشركة في 30 يومًا» — من يُصمّم مسارات وتشغيل Coach لـ200 موظف بـ3200–18500 دولار للإطلاق + 550–2400 دولار/شهر للمتابعة يبيع لجهات تريد تدريبًا قابلًا للقياس دون بناء منصة من الصفر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Coursera Coach AI 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم أكاديمية مؤسسية كاملة:</strong> 10–25 يومًا — 3200–18500 دولار.</li>
          <li><strong>متابعة تعلم وتحسين مسارات شهريًا:</strong> — 550–2400 دولار/مؤسسة/شهر.</li>
          <li><strong>حزمة 8 مسارات جاهزة حسب القطاع:</strong> — 680–2720 دولار.</li>
          <li><strong>ورش «بناء ثقافة تعلم بالعربية مع Coursera Coach»:</strong> — 52–210 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Coursera</span>
        <span class="tag">Learning</span>
        <span class="tag">HR</span>
        <span class="tag">Upskilling</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Asana AI Teammates 5 Arabic: زميل ذكي للمشاريع — توزيع مهام، ملخصات، ومتابعة بأمر عربي</h2>
      <p class="article-lead">«خمسون مهمة متأخرة والمدير يريد ملخصًا عربيًا قبل الاجتماع بنصف ساعة — والجميع مشغول بالتنفيذ». في 21 نوفمبر 2026، أطلقت <strong>Asana</strong> <strong>AI Teammates 5 Arabic</strong>: مساعد داخل Asana يفهم الأوامر بالفصحى، يُعيد توزيع المهام حسب الحمل والمهارات، يُنبّه عند تعارض المواعيد، يُلخّص تقدّم المشروع بفقرات عربية واضحة، يُقترح خطوات تالية، يربط Goals بالمهام اليومية، يتكامل مع Slack وGmail وTeams، ويُحترم صلاحيات الخصوصية للفرق — للوكالات وشركات التقنية والخدمات التي تدير عشرات المشاريع المتزامنة.</p>
      <p>المشكلة التي حلّتها: Teammates 4 كان يُنشئ مهامًا بعناوين إنجليزية رغم واجهة عربية؛ الإصدار 5 يُنتج أوصاف مهام RTL كاملة، قوالب «حملة إطلاق» و«تسليم عميل» و«موارد بشرية»، تنبؤًا بتأخر التسليم، تكامل تقويم ثنائي الاتجاه، تقارير أسبوعية للإدارة، وبرنامج «Asana Partners MENA AI».</p>
      <p>القدرات الأساسية: أوامر عربية؛ إعادة توزيع مهام؛ ملخصات إدارية؛ أهداف مرتبطة؛ تكامل قنوات العمل.</p>
      <p>للمبدعين العرب: مكتب «إدارة مشاريع مدعومة بالذكاء» — من يُطبّق Teammates على 10 فرق بـ1800–9200 دولار للإعداد + 380–1650 دولار/شهر للتشغيل يبيع للمؤسسات التي تضيع ساعات في اجتماعات الحالة الأسبوعية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Asana AI Teammates 5 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Teammates لفريق أو قسم كامل:</strong> 5–12 يومًا — 1800–9200 دولار.</li>
          <li><strong>تشغيل وتحسين توزيع مهام شهريًا:</strong> — 380–1650 دولار/فريق/شهر.</li>
          <li><strong>قوالب مشاريع جاهزة (15 نوعًا):</strong> — 120–480 دولار/مجموعة.</li>
          <li><strong>ورش «إدارة مشاريع عربية ذكية مع Asana AI»:</strong> — 46–185 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Asana</span>
        <span class="tag">PM</span>
        <span class="tag">Productivity</span>
        <span class="tag">Teams</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="21-11-2026 -- 08-AM.html">
          📰 21 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "21-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/21-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/21-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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