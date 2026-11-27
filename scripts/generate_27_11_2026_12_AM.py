#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Notion AI 3 Arabic · Airtable AI Assistant 2 Arabic · "
    "ClickUp Brain 3 Arabic · Dropbox Dash 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Notion AI 3 Arabic، Airtable AI Assistant 2 Arabic، ClickUp Brain 3 Arabic، Dropbox Dash 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Notion AI 3 Arabic الذي يُحوّل مذكّرة فوضوية إلى خطة عمل ومقال وقاعدة معرفة بالفصحى قبل أن ينام فريقك، إلى Airtable AI Assistant 2 Arabic الذي يُبني قاعدة بيانات وتقارير وتنبيهات من جملة واحدة بالعربية، ومن ClickUp Brain 3 Arabic الذي يُجيب «ماذا نفعل غدًا؟» بجدول مهام واضح ويلخّص الاجتماعات الطويلة، إلى Dropbox Dash 2 Arabic الذي يُجد لك الملف الصحيح عبر آلاف المستندات ويُلخّصه قبل الموعد — أربع قصص ليلية في 27 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء الساعة الصفراء!</h1>
      <p class="hero-sub">ليلة المعرفة والبيانات والإنتاجية والملفات: الأفكار تُنظَّم، الجداول تُبنى، المهام تُحسم، والمستندات تُعثر عليها. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 27 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Notion AI 3 Arabic: فكرة إلى نظام — وثائق، مهام، وقاعدة معرفة بضغطة واحدة!</h2>
      <p class="article-lead">«ملاحظاتك مبعثرة بين الدردشة والبريد — ولا أحد يجد SOP التشغيل عند الحاجة». في 27 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>Notion AI 3 Arabic</strong>: طبقة ذكاء داخل Workspace تفهم وصفك بالعربية، تُحوّل نقاطًا مختلطة إلى صفحات منظمة بعناوين وقوائم وجداول، تُولّد قوالب «خطة إطلاق» و«دليل موظف» و«اجتماع أسبوعي»، تُلخّص مئات الصفحات إلى ملخص تنفيذي، تُترجم بين الفصحى واللهجة المهنية حسب إعدادات الفريق، يقترح روابط داخلية بين الوثائق ذات الصلة، يتكامل Slack وGmail وCalendar وJira، يدعم RTL في العناوين والجداول، ويُصدّر «نشرة ليل المعرفة» لمدير العمليات — للشركات الناشئة والوكالات والمؤسسات 10–800 عضو في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُكرر عناوين بلا منطق؛ الإصدار 3 يفهم اختصارات الفريق، يحترم صلاحيات الصفحات السرية، يُنبّه عند تعارض إجراء قديم مع سياسة جديدة، يُولّد أسئلة اختبار للتدريب الداخلي بالعربية، يدعم الأوامر الصوتية القصيرة، مسار شريك للوكالات التي تبني «مراكز معرفة» لعملائها، وتدريب Notion Ambassador MENA على قوالب AI.</p>
      <p>القدرات الأساسية: صفحات من جملة؛ تلخيص وثائق؛ قوالب عربية؛ روابط ذكية؛ تقارير تنفيذية ليلية.</p>
      <p>للمبدعين العرب: استوديو «Notion بالعربية لشركتك» — من يُصمّم workspace + قوالب AI لفرق 25–400 شخص بـ1680–12400 دولار إعدادًا + 420–1680 دولار/شهر للصيانة يخدم مؤسسات تغرق في الفوضى المعرفية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI 3 Arabic؟</h3>
        <ul>
          <li><strong>هيكلة workspace + قوالب + تدريب الفرق:</strong> 10–18 يومًا — 1680–12400 دولار/عميل.</li>
          <li><strong>مراجعة وثائق وتحسين تدفقات شهريًا:</strong> — 420–1680 دولار/عميل/شهر.</li>
          <li><strong>حزمة 12 قالبًا عربيًا (SOP، onboarding، اجتماع، OKR):</strong> — 84–336 دولار/حزمة.</li>
          <li><strong>ورش «معرفة الشركة الذكية بالعربية مع Notion»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Productivity</span>
        <span class="tag">Teams</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Airtable AI Assistant 2 Arabic: من سؤال إلى جدول — بيانات، تقارير، وتنبيهات بلا معادلات!</h2>
      <p class="article-lead">«المدير يريد تقرير مبيعات بالمنطقة واللون — والمحلل يقضي ساعتين في الصيغ». في 27 نوفمبر 2026، أطلقت <strong>Airtable</strong> <strong>Airtable AI Assistant 2 Arabic</strong>: مساعد مدمج في القاعدة يفهم طلبك بالعربية، يُنشئ حقولًا وعلاقات وطرق عرض منطقية، يُولّد تقارير مخططات ولوحات بصرية، يُكتب صيغ التنبيه عند تجاوز هدف أو تأخر تسليم، يُنظّف بيانات مكررة، يُقترح أتمتة (إشعار Telegram عند صف جديد، إرسال بريد عند موافقة)، يتكامل Salesforce وShopify وZapier، يدعم تسميات حقول عربية مع RTL في الواجهة، ويُرسل «ملخص ليل البيانات» لصاحب العمل — للوكالات والتجارة والتعليم والمنظمات 20–600 مستخدم.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يخلط التواريخ؛ الإصدار 2 يحترم تقويم الفريق والعملة المحلية، يدعم قوالب «مخزون» و«حملة» و«قبول طلاب» بالعربية، يُنبّه عند صيغة قد تُبطّئ القاعدة، يُحوّل ملف CSV فوضويًا إلى هيكل نظيف مع شرح بالعربية، برنامج شركاء Airtable MENA للمستشارين، وتدريب على حوكمة البيانات الحساسة.</p>
      <p>القدرات الأساسية: قواعد من جملة؛ تقارير؛ أتمتة؛ تنظيف بيانات؛ تكامل CRM وتجارة.</p>
      <p>للمبدعين العرب: خدمة «Airtable ذكي للعميل» — من يبني 3–8 قواعد مترابطة لشركة نمو بـ1520–11200 دولار + 380–1520 دولار/شهر للدعم يبيع وضوحًا لفرق تعيش في جداول Excel مكسورة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable AI Assistant 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم قاعدة + أتمتة + تدريب:</strong> 6–16 يومًا — 1520–11200 دولار/عميل.</li>
          <li><strong>صيانة صيغ وتقارير شهريًا:</strong> — 380–1520 دولار/عميل/شهر.</li>
          <li><strong>حزمة 6 قوالب قاعدة (مبيعات، محتوى، موارد بشرية، فعاليات):</strong> — 72–288 دولار/حزمة.</li>
          <li><strong>ورش «بيانات بدون برمجة بالعربية مع Airtable»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">Database</span>
        <span class="tag">Reports</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ClickUp Brain 3 Arabic: عقل الفريق — مهام، ملخصات اجتماعات، وإجابات فورية بالعربية!</h2>
      <p class="article-lead">«الاجتماع انتهى قبل قليل — ولا أحد متأكد ممن يملك المهمة الحرجة غدًا». في 27 نوفمبر 2026، أطلقت <strong>ClickUp</strong> <strong>ClickUp Brain 3 Arabic</strong>: مساعد إنتاجية يعمل عبر المساحة كاملة، يُلخّص Threads الطويلة وملاحظات المهام إلى نقاط عمل، يُجيب «ما حالة مشروع العميل X؟» بجملة عربية مع روابط للمهام، يُولّد قوائم مهام من بريد أو رسالة صوتية، يُقترح أولويات حسب الموعد والاعتماديات، يُكتب تحديثات حالة للعميل بنبرة مهنية خليجية أو مصرية حسب الإعداد، يتكامل Zoom وTeams وGmail، يدعم عرض Gantt ولوحات بالعربية، ويُرسل «نشرة إنتاجية ليلية» للمدير — لفرق تطوير وتسويق وخدمات 8–350 عضو.</p>
      <p>المشكلة التي حلّتها: Brain 2 كان يخلط المشاريع؛ الإصدار 3 يحترم مساحات العمل المنفصلة لكل عميل، يُنبّه عند مهمة بلا مالك، يُقترح إغلاق مهام مكررة، يُولّد قوالب Stand-up بالعربية، مسار شريك للوكالات التي تدير ClickUp لعشرات العلامات، وتدريب ClickUp Partner على حوكمة AI داخل فرق مختلطة اللغات.</p>
      <p>القدرات الأساسية: ملخصات؛ أسئلة طبيعية؛ مهام من بريد؛ أولويات؛ تحديثات عملاء عربية.</p>
      <p>للمبدعين العرب: باقة «ClickUp Brain لفرق الوكالة» — من يُفعّل Brain لـ6 عملاء (فرق 15–40 شخص لكل عميل) بـ1440–9800 دولار إعدادًا + 360–1440 دولار/شهر لكل عميل يبني دخلًا متكررًا مع مديرين يخسرون الليل في الملاحقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ClickUp Brain 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مساحات + تدفقات Brain + تدريب:</strong> 5–12 يومًا — 1440–9800 دولار/عميل.</li>
          <li><strong>مراجعة إنتاجية وتحسين قوالب شهريًا:</strong> — 360–1440 دولار/عميل/شهر.</li>
          <li><strong>حزمة 10 قوالب مشروع (وكالة، SaaS، متجر، تطبيق):</strong> — 80–320 دولار/حزمة.</li>
          <li><strong>ورش «إدارة عمل ذكية بالعربية مع ClickUp Brain»:</strong> — 46–184 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ClickUp</span>
        <span class="tag">Tasks</span>
        <span class="tag">Meetings</span>
        <span class="tag">Agencies</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Dropbox Dash 2 Arabic: ابحث، لخّص، نفّذ — كل ملفات شركتك تتكلّم العربية!</h2>
      <p class="article-lead">«العقد الموقّع موجود «في مكان ما» — والفريق يبحث ساعة قبل اجتماع المستثمر». في 27 نوفمبر 2026، أطلقت <strong>Dropbox</strong> <strong>Dropbox Dash 2 Arabic</strong>: مساعد بحث عالمي يفهرس Dropbox وGoogle Drive وSlack وNotion وOutlook، يُجيب أسئلة «أين آخر عرض أسعار للعميل؟» بروابط مباشرة، يُلخّص PDF وعروض PowerPoint وعقودًا طويلة إلى نقاط عربية، يُقترح إجراءات (مشاركة، طلب موافقة، أرشفة)، يحترم صلاحيات المجلدات، يدعم استعلامات باللهجة المهنية، يتكامل Microsoft 365 وSalesforce، يُولّد Stack مؤقتًا لملفات مشروع، ويُرسل «تقرير ليل المستندات الحرجة» — للشركات القانونية والاستشارية والهندسية والإعلام 30–3000 موظف.</p>
      <p>المشكلة التي حلّتها: Dash الأول كان يُرجع نتائج إنجليزية فقط؛ الإصدار 2 يفهم أسماء مجلدات عربية، يُميّز بين نسخ الملف، يُنبّه عند مشاركة خارجية خطرة، يدعم تلخيص صوتي قصير بالعربية، مسار امتثال للبنوك والحكومة، وبرنامج شريك «Dropbox Dash MENA» للمستشارين في الأرشفة الرقمية.</p>
      <p>القدرات الأساسية: بحث عبر التطبيقات؛ تلخيص مستندات؛ إجراءات سريعة؛ امتثال؛ تقارير ليلية.</p>
      <p>للمبدعين العرب: خدمة «مكتبة الشركة الذكية» — من يُفعّل Dash لمؤسسة 200–5000 موظف بـ1890–14200 دولار + 470–1890 دولار/شهر للحوكمة يبيع وقتًا ثمينًا لقيادات تغرق في البحث عن الملفات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dropbox Dash 2 Arabic؟</h3>
        <ul>
          <li><strong>فهرسة مصادر + سياسات وصول + تدريب:</strong> 8–22 يومًا — 1890–14200 دولار.</li>
          <li><strong>مراجعة مشاركات وتقارير امتثال شهريًا:</strong> — 470–1890 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 استعلامًا جاهزًا (عقود، عروض، موارد بشرية، مالية):</strong> — 90–360 دولار/حزمة.</li>
          <li><strong>ورش «بحث مؤسسي ذكي بالعربية مع Dropbox Dash»:</strong> — 52–208 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dropbox</span>
        <span class="tag">Search</span>
        <span class="tag">Documents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-11-2026 -- 12-AM.html">
          📰 27 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/27-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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