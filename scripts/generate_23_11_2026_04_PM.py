#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "23-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Figma AI Design 3 Arabic · Notion AI Q&A 3 Arabic · "
    "Airtable Omni 2 Arabic · Loom AI Workflows 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Figma AI Design 3 Arabic، Notion AI Q&A 3 Arabic، Airtable Omni 2 Arabic، Loom AI Workflows 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Figma AI Design 3 Arabic الذي يُحوّل وصفك العربي إلى شاشات ومكوّنات وتصميم نظام كامل قبل أن يطفئ فريقك شاشة المكتب، إلى Notion AI Q&amp;A 3 Arabic الذي يجيب عن سياساتك ومشاريعك من ذاكرة شركتك بلغة الفريق، ومن Airtable Omni 2 Arabic الذي يُبني قاعدة بيانات وتدفقات عمل من جملة بالفصحى، إلى Loom AI Workflows 2 Arabic الذي يُلخّص تسجيلاتك ويُحوّل التعليمات المرئية إلى مهام ومستندات — أربع قصص مسائية في 23 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء ساعة الغروب!</h1>
      <p class="hero-sub">مساء التصميم والمعرفة والبيانات والفيديو: الواجهات تُرسم، الوثائق تُجيب، الجداول تُبنى، والتسجيلات تُصبح خطة عمل. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 23 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Figma AI Design 3 Arabic: من الفكرة إلى واجهة RTL — شاشات، مكوّنات، ونظام تصميم بلغة واحدة!</h2>
      <p class="article-lead">«المصمم يكرّر نفس الهيكل ثماني مرات والمطور ينتظر — والإطلاق يضيع أسبوعًا». في 23 نوفمبر 2026، أطلقت <strong>Figma</strong> <strong>Figma AI Design 3 Arabic</strong>: طبقة ذكاء داخل Figma تفهم وصف المنتج بالفصحى والعامية المكتبية، تُولّد إطارات RTL جاهزة للهواتف والويب، تُقترح أنظمة ألوان وخطوط عربية، تُنشئ مكوّنات قابلة لإعادة الاستخدام مع حالات وتسميات عربية، تُحوّل رسمًا تخطيطيًا إلى واجهة منقّحة، تُصدّر مواصفات للمطورين بالعربية والإنجليزية، تُربط مكتبات Design System، وتتكامل مع Dev Mode وSlack — لفرق المنتج والتجارة الإلكترونية والتعليم في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُهمل محاذاة RTL في الجداول والنماذج؛ الإصدار 3 يدعم قوالب «تطبيق بنكي» و«متجر إلكتروني» و«لوحة إدارية»، تباين ألوان للوصولية، مكتبات خطوط عربية معتمدة، مراجعة تلقائية للمسافات بين الحروف، تعليقات ذكية للمراجعين، وبرنامج «Figma AI Partners MENA» للاستوديوهات المعتمدة.</p>
      <p>القدرات الأساسية: شاشات من وصف عربي؛ مكوّنات RTL؛ أنظمة ألوان؛ مواصفات للمطورين؛ قوالب قطاعية.</p>
      <p>للمبدعين العرب: استوديو «واجهات أسرع» — من يُشغّل Figma AI Design لفرق 5–30 مصممًا بـ1400–8600 دولار للإطلاق + 350–1680 دولار/شهر للتحسين يخدم الشركات التي تُطلق منتجات متعددة شهريًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Figma AI Design 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء نظام تصميم ذكي (مكتبات، قوالب، تدريب فريق):</strong> 5–12 يومًا — 1400–8600 دولار.</li>
          <li><strong>تحديث مكوّنات وشاشات عربية شهريًا:</strong> — 350–1680 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 شاشة جاهزة RTL (قطاعات تجارة وتعليم):</strong> — 88–352 دولار/حزمة.</li>
          <li><strong>ورش «تصميم منتج ذكي بالعربية مع Figma AI»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Figma</span>
        <span class="tag">Design</span>
        <span class="tag">UX</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Notion AI Q&amp;A 3 Arabic: شركتك تُجيب — أسئلة عربية من الوثائق والمشاريع والاجتماعات!</h2>
      <p class="article-lead">«الموظف الجديد يسأل نفس الأسئلة التي أجابنا عنها في Notion قبل ستة أشهر — والخبير مشغول دائمًا». في 23 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>Notion AI Q&amp;A 3 Arabic</strong>: محرك إجابات فوق workspace Notion يفهرس الصفحات والجداول والملفات المسموح بها، يُجيب بالفصحى واللهجات المكتبية الشائعة، يُرفق المصدر والفقرة الأصلية، يُلخّص السياسات والإجراءات، يقترح تحديثات عند تعارض الإصدارات، يُجيب من اجتماعات مربوطة في Calendar، يحترم صلاحيات كل فريق، ويدعم تكامل Slack وGoogle Drive — للشركات الناشئة والمؤسسات في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يخلط بين اللغات في الاقتباسات؛ الإصدار 3 يفضّل المصادر العربية عند توفرها، يدعم قوالب «سياسة موارد بشرية» و«دليل منتج» و«إجراءات مالية»، تنبيهات عند معلومات قديمة، وضع امتثال يخفي الحقول الحساسة، تدريبًا تفاعليًا للموظفين الجدد، وبرنامج «Notion AI Consultants Arabia».</p>
      <p>القدرات الأساسية: بحث ذكي عربي؛ إجابات بمصادر؛ تلخيص سياسات؛ امتثال صلاحيات؛ اقتراح تحديثات.</p>
      <p>للمبدعين العرب: خدمة «معرفة مؤسسية حية» — من يُهيكل workspace ويُفعّل Q&amp;A لشركة 40–600 موظف بـ1800–11400 دولار + 400–1850 دولار/شهر للصيانة يختصر أسئلة التكرار التي تُهدر ساعات يومية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Q&amp;A 3 Arabic؟</h3>
        <ul>
          <li><strong>هيكلة workspace + تفعيل Q&amp;A (فهرسة، سياسات، تدريب):</strong> 7–16 يومًا — 1800–11400 دولار.</li>
          <li><strong>تنظيف محتوى وتحسين دقة إجابات شهريًا:</strong> — 400–1850 دولار/مؤسسة/شهر.</li>
          <li><strong>حزمة 12 قالب صفحة عربية لقطاعات متعددة:</strong> — 76–304 دولار/حزمة.</li>
          <li><strong>ورش «إدارة معرفة ذكية بالعربية مع Notion»:</strong> — 40–160 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Wiki</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Airtable Omni 2 Arabic: جدول ذكي يفهمك — قواعد بيانات، أتمتة، ولوحات من أمر عربي!</h2>
      <p class="article-lead">«نحتاج تتبّع طلبات العملاء والمخزون والفواتير — ولا وقت لبناء ERP صغير من الصفر». في 23 نوفمبر 2026، أطلقت <strong>Airtable</strong> <strong>Airtable Omni 2 Arabic</strong>: مساعد بناء داخل Airtable يقرأ وصف العملية بالعربية، يُقترح جداول وحقول وعلاقات، يُنشئ نماذج إدخال RTL، يُبني أتمتة للإشعارات والموافقات، يُولّد لوحات عرض للإدارة، يُربط البريد وSlack وShopify عند الحاجة، يُصدّر تقارير أسبوعية بالفصحى، ويقترح تحسينات عند تكرار العمل اليدوي — للوكالات والمتاجر والمنظمات في MENA.</p>
      <p>المشكلة التي حلّتها: Omni الأول كان يُنشئ حقولًا إنجليزية فقط أو يتجاهل التقويم الهجري والعطل المحلية؛ الإصدار 2 يدعم قوالب «وكالة إبداعية» و«توريد وتجزئة» و«تطوع ومنح»، تحققًا من صحة أرقام الهواتف الإقليمية، أتمتة تذكير واتساب عبر تكاملات معتمدة، حدودًا لصلاحيات المشاهدين، وسجل تغييرات للمراجعة الداخلية.</p>
      <p>القدرات الأساسية: مخطط من وصف عربي؛ أتمتة إشعارات؛ نماذج RTL؛ لوحات إدارية؛ تكامل أدوات.</p>
      <p>للمبدعين العرب: مكتب «عمليات رقمية سريعة» — من يُسلّم نظام Airtable جاهز للتشغيل لعملية واحدة بـ950–5800 دولار + 280–1320 دولار/شهر للتوسع يجذب أصحاب الأعمال الذين يعانون من Excel المشتت.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable Omni 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم قاعدة عمل كاملة (جداول، أتمتة، تدريب):</strong> 4–11 يومًا — 950–5800 دولار.</li>
          <li><strong>توسيع وتحسين أتمتة وتقارير شهريًا:</strong> — 280–1320 دولار/عميل/شهر.</li>
          <li><strong>حزمة 8 قوالب عمليات عربية جاهزة:</strong> — 85–340 دولار/حزمة.</li>
          <li><strong>ورش «إدارة عمليات بالعربية مع Airtable Omni»:</strong> — 36–144 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">No-Code</span>
        <span class="tag">Ops</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Loom AI Workflows 2 Arabic: فيديو يعمل عنك — تلخيص، مهام، ومستندات من كل تسجيل!</h2>
      <p class="article-lead">«ساعة من التدريب مسجّلة — ولا أحد يعرف ماذا يفعل بعد المشاهدة». في 23 نوفمبر 2026، أطلقت <strong>Loom</strong> <strong>Loom AI Workflows 2 Arabic</strong>: ذكاء فوق تسجيلات Loom يُلخّص الشرح بالفصحى الواضحة، يُستخرج خطوات العمل والقرارات، يُنشئ مهامًا في Asana وNotion وJira، يكتب ملخصًا للفريق المفقود من الاجتماع، يُولّد مقالات مساعدة قصيرة، يُترجم المقاطع المهمة إلى نص عربي للبحث، يقترح مقاطع قصيرة للتدريب الداخلي، ويحترم سياسات عدم مشاركة المحتوى الحساس — لفرق التوزيع والمبيعات والدعم في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُنتج ملخصات إنجليزية طويلة؛ الإصدار 2 يدعم قوالب «تسليم مشروع» و«تدريب موظف جديد» و«مراجعة أسبوعية»، تمييز المتحدثين في الاجتماعات المدمجة، ربطًا بـ CRM لربط المكالمات بالصفقات، علامات تلقائية للموضوعات، وفهرسة عربية للبحث داخل المكتبة.</p>
      <p>القدرات الأساسية: تلخيص عربي؛ استخراج مهام؛ مقالات مساعدة؛ مقاطع تدريبية؛ تكامل أدوات الفريق.</p>
      <p>للمبدعين العرب: خدمة «مكتبة فيديو منتجة» — من يُنظّم أرشيف Loom لشركة أو وكالة ويُفعّل Workflows بـ680–4200 دولار للإعداد + 240–1080 دولار/شهر للتشغيل يحوّل ساعات الفيديو المنسية إلى أصول تدريب قابلة للبيع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Loom AI Workflows 2 Arabic؟</h3>
        <ul>
          <li><strong>تنظيم مكتبة Loom + Workflows (قوالب، تكامل، تدريب):</strong> 3–9 أيام — 680–4200 دولار.</li>
          <li><strong>تحويل تسجيلات أسبوعية إلى مهام ومساعدة شهريًا:</strong> — 240–1080 دولار/عميل/شهر.</li>
          <li><strong>حزمة 25 ملخصًا ودليلًا عربيًا من قوالب Loom:</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «تواصل غير متزامن ذكي بالعربية مع Loom»:</strong> — 34–136 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Loom</span>
        <span class="tag">Video</span>
        <span class="tag">Async</span>
        <span class="tag">Training</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="23-11-2026 -- 04-PM.html">
          📰 23 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "23-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/23-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/23-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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