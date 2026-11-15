#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 15-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "15-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 2 Arabic · Perplexity Comet 2 Arabic · "
    "Notion AI Agents Arabic · Canva Magic Studio 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 2 Arabic، Perplexity Comet 2 Arabic، Notion AI Agents Arabic، Canva Magic Studio 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 15 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 2 Arabic الذي يُبني وكيل دعم عربي يُجيب عن سياسات الشركة في Teams بينما أنت نائم، إلى Perplexity Comet 2 Arabic الذي يُتصفح عشرات المواقع ويُسلّم لك ملخصًا موثقًا بالعربية عن سوقك، ومن Notion AI Agents Arabic الذي يُحدّث قاعدة معرفتك ويُرسل تذكيرات مهام للفريق من صفحة واحدة، إلى Canva Magic Studio 3 Arabic الذي يُحوّل فكرة حملة رمضانية إلى سلسلة تصاميم RTL خلال دقائق — أربع قصص ليلية في 15 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للمديرين التنفيذيين ووكالات التسويق وفرق العمليات: الوكلاء صاروا جاهزين للمؤسسات، البحث العميق أصبح متصفحًا ذكيًا، قواعد المعرفة تدير نفسها، والتصميم يريد عربية أصيلة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 15 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 2 Arabic: وكلاء عرب في Teams وOutlook — سياسات، تكامل، وامتثال!</h2>
      <p class="article-lead">«العميل يسأل عن إرجاع المنتج الساعة 2 فجرًا — والموظفون نيام». في 15 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 2 Arabic</strong>: منصة بناء وكلاء تفهم الفصحى ولهجات الخليج والشام، تُجيب من مستندات SharePoint وDynamics وServiceNow، تُحترم صلاحيات Entra ID، تُسجّل المحادثات لمراجعة الامتثال، تُدمج في Teams وOutlook وWhatsApp Business عبر موصلات رسمية — للبنوك والاتصالات والتجزئة في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يختلق أحيانًا أو يُجيب بالإنجليزية؛ الإصدار 2 يُفرض «الإجابة من المصدر فقط»، يُحدّث المكتبة تلقائيًا عند تغيير السياسة، يُدعم أسئلة ثنائية اللغة، يُوفّر لوحة جودة بالعربية، يُتصل بـPower Automate لتصعيد التذكرة، ويشهادات SOC2 و HIPAA-ready للقطاعات الحساسة.</p>
      <p>القدرات الأساسية: Arabic topic authoring؛ قوالب وكلاء جاهزة (HR، IT، مبيعات)؛ تكامل Azure OpenAI؛ مراجعة بشرية قبل النشر؛ برنامج شريك «Copilot Studio MENA».</p>
      <p>للمبدعين العرب: استشارات تأسيس — «وكيل دعم عربي لفرق 500 موظف في 12 يومًا». من يُنفّذ 6 مشاريع سنويًا بعقود 8500–62000 دولار + صيانة 600–4500 دولار/شهر يبيع موثوقية ليلية دون توظيف مركز اتصال كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 2 Arabic؟</h3>
        <ul>
          <li><strong>بناء وكيل (محتوى، اختبارات، نشر، تدريب):</strong> 8–18 يومًا — 8500–62000 دولار/مشروع.</li>
          <li><strong>صيانة وتحديث سياسات شهريًا:</strong> — 600–4500 دولار/شهر.</li>
          <li><strong>حزم قطاعية (تأمين، لوجستيك، تعليم):</strong> — 55–240 دولار/حزمة.</li>
          <li><strong>دورات «تصميم وكلاء Copilot بالعربية للمؤسسات»:</strong> — 62–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot Studio</span>
        <span class="tag">Agents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Perplexity Comet 2 Arabic: متصفح ذكي يبحث نيابةً عنك — مصادر، تقارير، وأسواق!</h2>
      <p class="article-lead">«أريد تحليل أسعار منافسي التجارة الإلكترونية في ثلاث دول — وليس لدي وقت لفتح خمسين تبويبًا». في 15 نوفمبر 2026، أطلقت <strong>Perplexity</strong> <strong>Comet 2 Arabic</strong>: متصفح مدعوم بنماذج reasoning يُنفّذ مهام متعددة الخطوات، يقرأ المواقع العربية والإنجليزية، يُخرج تقارير PDF بالفصحى مع روابط موثقة، يُحفظ جلسات البحث للفرق، يُحترم حظر تسجيل الدخول التلقائي دون موافقة — للمحللين والاستشاريين ورواد الأعمال.</p>
      <p>المشكلة التي حلّتها: Comet 1 كان يتوقف عند CAPTCHA أو الصفحات الديناميكية؛ الإصدار 2 يُشغّل وضع «محقق أسواق» مع جداول مقارنة، يُلخص أخبار SEC و البورصات الخليجية، يُصدر CSV عربي RTL، يُتزامن مع Spaces للفرق، وAPI للوكالات التي تبيع «تقارير أسبوعية».</p>
      <p>القدرات الأساسية: Arabic report templates؛ جدولة مهام ليلية؛ تكامل Google Drive وNotion؛ حدود استخدام للمؤسسات؛ شريك «Comet Research MENA».</p>
      <p>للمبدعين العرب: منتج تقارير — «ملخص سوقك كل اثنين بالعربية». من يبيع 40 عميلًا باشتراك 79–399 دولار/شهر + إعداد 300–1800 دولار يحوّل بحثًا عميقًا إلى دخل متكرر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Comet 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد مساحات بحث (مواضيع، جداول، أتمتة):</strong> 2–6 أيام — 300–1800 دولار/عميل.</li>
          <li><strong>اشتراك تقارير أسبوعية (سوق، منافسون، تنظيمات):</strong> — 79–399 دولار/شهر.</li>
          <li><strong>تقارير لمرة واحدة (استحواذ، دخول سوق جديد):</strong> — 450–3200 دولار/تقرير.</li>
          <li><strong>دورات «بحث سوقي بالعربية مع Comet»:</strong> — 45–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Comet</span>
        <span class="tag">Browser</span>
        <span class="tag">Research</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Notion AI Agents Arabic: وكلاء يُديرون قاعدة المعرفة — مهام، تذكيرات، ومزامنة!</h2>
      <p class="article-lead">«ويكي الشركة فارغ لأن أحدًا لا يُحدّث صفحات الإجراءات — والمشاريع تتأخر». في 15 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>AI Agents Arabic</strong>: وكلاء يقرأون قواعد البيانات، يُحدّثون حالات المهام، يُولّدون ملخصات اجتماع بالفصحى، يُرسلون تذكيرات Slack، يُقترحون قوالب SOP جديدة من محادثات الفريق، يُحترمون أذونات الصفحة — للشركات الناشئة والوكالات والجامعات.</p>
      <p>المشكلة التي حلّتها: Notion AI السابق كان يكتب فقط؛ الوكلاء يُنفّذون: «بعد كل مكالمة مبيعات، أضف ملخصًا عربيًا واربطه بالفرصة». يدعم RTL في الجداول، تكامل CRM خفيف، سجل تدقيق، حدود تنفيذ آمنة، ومكتبة وكلاء جاهزة للموارد البشرية والتسويق.</p>
      <p>القدرات الأساسية: Arabic database queries؛ قوالب wiki للامتثال؛ تكامل Zapier وGitHub Issues؛ وضع «مدير مشروع ليلي»؛ برنامج شريك «Notion Agents MENA».</p>
      <p>للمبدعين العرب: باقات تأسيس — «نظام تشغيل شركة عربية على Notion في أسبوع». من يُسلّم 20 عميلًا بـ1200–7500 دولار + دعم 250–1600 دولار/شهر يبيع انضباطًا رقميًا دون تطبيق مخصّص.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Agents Arabic؟</h3>
        <ul>
          <li><strong>تأسيس workspace (قواعد بيانات، وكلاء، تدريب):</strong> 5–12 يومًا — 1200–7500 دولار/عميل.</li>
          <li><strong>دعم وتحسين وكلاء شهريًا:</strong> — 250–1600 دولار/شهر.</li>
          <li><strong>حزم قوالب (OKR، onboarding، محتوى):</strong> — 39–175 دولار/حزمة.</li>
          <li><strong>دورات «تشغيل وكلاء Notion بالعربية»:</strong> — 48–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Wiki</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Canva Magic Studio 3 Arabic: استوديو تصميم ذكي — حملات RTL، فيديو قصير، وعلامة!</h2>
      <p class="article-lead">«العميل يريد 30 بوستًا لحملة العودة للمدارس خلال يومين — والمصمم في إجازة». في 15 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 3 Arabic</strong>: مجموعة أدوات تُولّد نصوصًا إعلانية بالفصحى واللهجات المختارة، تُطبّق هوية بصرية من Brand Kit، تُنتج فيديوهات Reels بترجمة عربية، تُقيس تناسق الألوان RTL، تُصدّر لـMeta وSnap وTikTok — للمطاعم والعيادات والمتاجر الإلكترونية.</p>
      <p>المشكلة التي حلّتها: Magic Studio 2 كان يكرر نفس القوالب الإنجليزية؛ الإصدار 3 يُفهم اتجاه النص والخطوط العربية، يُقترح عناوين SEO للمتاجر، يُزامن مع Canva Sites للصفحات المقصودة، يُشغّل «حملة كاملة من وصف واحد»، ويُتيح مراجعة جماعية بالتعليقات العربية.</p>
      <p>القدرات الأساسية: Arabic copy variants؛ مكتبة خطوط عربية مرخّصة؛ resize ذكي للمنصات؛ تكامل Content Planner؛ شريك «Canva Agency MENA».</p>
      <p>للمبدعين العرب: وكالات محتوى — «حزمة حملة شهرية عربية بلا مصمم بدوام كامل». من يدير 25 عميلًا بـ280–1900 دولار/شهر + رسوم إعداد 350–2200 دولار يبيع سرعة وجودة بصريّة للسوق العربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Brand Kit وحملة أولى:</strong> 2–5 أيام — 350–2200 دولار/عميل.</li>
          <li><strong>إدارة محتوى شهري (تصاميم، فيديو، جدولة):</strong> — 280–1900 دولار/شهر.</li>
          <li><strong>حزم مواسم (رمضان، عيد، تخفيضات):</strong> — 52–225 دولار/حزمة.</li>
          <li><strong>دورات «حملات عربية سريعة مع Magic Studio»:</strong> — 40–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Design</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 15-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="15-11-2026 -- 12-AM.html">
          📰 15 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "15-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/15-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/15-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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