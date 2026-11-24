#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 24-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "24-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "HubSpot AI Customer Agent 3 Arabic · Trello Inbox AI 3 Arabic · "
    "Power BI Copilot 3 Arabic · SurveyMonkey Genius 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HubSpot AI Customer Agent 3 Arabic، Trello Inbox AI 3 Arabic، Power BI Copilot 3 Arabic، SurveyMonkey Genius 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 24 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من HubSpot AI Customer Agent 3 Arabic الذي يُجيب زيارات موقعك ويب وواتساب في منتصف الليل كأن لديك فريق مبيعات ودعم لا ينام، إلى Trello Inbox AI 3 Arabic الذي يُحوّل رسائل البريد والملاحظات الصوتية إلى بطاقات منظّمة قبل أن تفتح عينيك، ومن Power BI Copilot 3 Arabic الذي يُترجم أرقام شركتك إلى قصة عربية يفهمها المدير العام في جملة واحدة، إلى SurveyMonkey Genius 2 Arabic الذي يَصنع استبيانًا ويُحلّل آلاف الإجابات ويُقترح قرارًا تسويقيًا من فكرة عربية بسيطة — أربع قصص ليلية في 24 نوفمبر 2026 لروّاد الأعمال والوكالات الذين يريدون أدوات عالمية ودخلًا يُضيء الساعة الصفراء!</h1>
      <p class="hero-sub">ليلة العملاء والمهام والبيانات والأصوات: الوكيل يرد، البطاقات تُرتّب، التقارير تتكلّم، والاستبيان يُفكّر. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول عنوان.</p>
      <div class="hero-meta">
        <span>📅 24 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HubSpot AI Customer Agent 3 Arabic: وكيل يبيع ويدعم — محادثات عربية على الموقع والواتساب والبريد!</h2>
      <p class="article-lead">«زائر سعودي يسأل عن الأسعار الساعة الثانية صباحًا — وفريقك نائم والصفقة تضيع». في 24 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>HubSpot AI Customer Agent 3 Arabic</strong>: وكيل ذكاء اصطناعي داخل CRM HubSpot يقرأ معرفة منتجك وعروضك بالفصحى واللهجات التجارية الشائعة، يُجيب على موقعك وصفحات الهبوط، يتحادث عبر واتساب Business API مع احترام ساعات العمل والتصعيد، يُؤهّل العملاء المحتملين ويُحدّث السجل تلقائيًا، يُقترح مواعيد للمستشارين، يُرسل متابعات بعد 24 ساعة، يُلخّص المحادثات للبائع البشري، يدمج مع Marketing Hub وService Hub، ويدعم امتثال GDPR وموافقات التسجيل — للشركات B2B والتجارة الإلكترونية والتعليم في الخليج ومصر وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يكرّر إجابات طويلة أو يخلط بين منتجات؛ الإصدار 3 يملك «بطاقة نبرة» لكل علامة، يفضّل المصادر العربية من قاعدة المعرفة، يكتشف نية الشراء والاعتراضات، يُوقف البوت عند كلمات تصعيد حرجة، يُجري اختبارات ردود تلقائية، يقترح مقالات مساعدة من مدونة HubSpot، ويُقدّم برنامج «HubSpot AI Partners MENA» للمكامِلين المعتمدين.</p>
      <p>القدرات الأساسية: محادثة عربية متعددة القنوات؛ تأهيل تلقائي؛ تكامل CRM؛ تصعيد ذكي؛ تقارير تحويل.</p>
      <p>للمبدعين العرب: خدمة «مبيعات ليلية حية» — من يُنشئ قاعدة معرفة عربية ويُفعّل الوكيل لشركة 10–200 موظف بـ2200–13800 دولار للإطلاق + 520–2100 دولار/شهر للتحسين يجذب الشركات التي تخسر leads خارج ساعات الدوام.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot AI Customer Agent 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد وكيل + قاعدة معرفة عربية (قنوات، تدريب، اختبار):</strong> 8–18 يومًا — 2200–13800 دولار.</li>
          <li><strong>تحسين ردود ومعدّل تحويل شهريًا:</strong> — 520–2100 دولار/عميل/شهر.</li>
          <li><strong>حزمة 15 سيناريو محادثة عربية جاهزة لقطاعات متعددة:</strong> — 92–368 دولار/حزمة.</li>
          <li><strong>ورش «مبيعات ودعم ذكي بالعربية مع HubSpot AI»:</strong> — 44–176 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">CRM</span>
        <span class="tag">Chatbot</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Trello Inbox AI 3 Arabic: صندوق وارد ذكي — من بريد وصوت ونسخة إلى بطاقات بأولويات!</h2>
      <p class="article-lead">«المؤسس يرسل أفكارًا في البريد والواتساب والملاحظات الصوتية — ولا أحد يحوّلها إلى مهام». في 24 نوفمبر 2026، أطلقت <strong>Atlassian</strong> <strong>Trello Inbox AI 3 Arabic</strong>: صندوق وارد ذكي داخل Trello يستقبل رسائل البريد الموجّهة للفريق، رسائل Slack المفلترة، ملاحظات صوتية عربية مُفهمَة، ولصق نص سريع، يُصنّف كل مدخل (ميزة، عطل، مبيعات، عاجل)، يُنشئ بطاقة بعنوان عربي واضح ووصف منظّم، يُقترح القائمة والأعضاء والموعد، يُربط بالمرفقات، يكتشف التكرار ويُدمج البطاقات، يُرسل تذكيرًا للمعنيين، ويُزامن مع Jira عند الحاجة — للشركات الناشئة والوكالات والفرق عن بُعد في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: Inbox 2 كان يُسقط التشكيل أو يُخطئ في أولوية «عاجل»؛ الإصدار 3 يدعم قوالب «طلب عميل» و«فكرة منتج» و«متابعة مالية»، يميّز الأسماء العربية في الإسناد، يحترم ساعات عدم الإزعاج، يُولّد checklist فرعية، يُحفظ مسار المصدر للمراجعة، ويُتاح عبر برنامج «Trello AI Coaches Arabia» للمستشارين.</p>
      <p>القدرات الأساسية: capture عربي متعدد المصادر؛ تصنيف تلقائي؛ إسناد ذكي؛ دمج تكرار؛ تكامل Jira.</p>
      <p>للمبدعين العرب: مكتب «نظافة عمليات» — من يُصمّم قوائم Trello وInbox وقواعد capture لفرق 5–80 شخص بـ880–6200 دولار + 260–1180 دولار/شهر للصيانة يخدم روّاد الأعمال المغرقين في الفوضى الرقمية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Trello Inbox AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم نظام Inbox + قوائم وقواعد capture:</strong> 4–12 يومًا — 880–6200 دولار.</li>
          <li><strong>مراجعة بطاقات وتحسين قواعد أسبوعيًا:</strong> — 260–1180 دولار/فريق/شهر.</li>
          <li><strong>حزمة 10 قوالب بطاقة عربية لقطاعات (وكالة، متجر، SaaS):</strong> — 78–312 دولار/حزمة.</li>
          <li><strong>ورش «إنتاجية الفريق بالعربية مع Trello Inbox AI»:</strong> — 38–152 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Trello</span>
        <span class="tag">Atlassian</span>
        <span class="tag">Productivity</span>
        <span class="tag">Inbox</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Power BI Copilot 3 Arabic: بيانات تتكلّم — تقارير، رسوم، وتفسير بالعربية من سؤال واحد!</h2>
      <p class="article-lead">«المدير يسأل: لماذا تراجعت المبيعات في الرياض الشهر الماضي؟ — والمحلل يحتاج يومين». في 24 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Power BI Copilot 3 Arabic</strong>: مساعد تحليلي داخل Power BI يفهم أسئلة الإدارة بالفصحى واللهجات المكتبية، يُنشئ تقارير ولوحات من وصف عربي، يُولّد مخططات مناسبة للبيانات، يشرح الاتجاهات والشذوذ بلغة غير تقنية، يُقترح مقاييس جديدة ومعادلات DAX مُعلَّقة بالعربية، يُلخّص لوحة كاملة لاجتماع صباحي، يحترم صلاحيات الصفوف الحساسة، يدعم التقويم الهجري في المحاور الزمنية، ويتكامل مع Excel وTeams وFabric — للتجزئة والخدمات اللوجستية والبنوك والتعليم في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot 2 كان يُخطئ في تسمية الأعمدة العربية أو يُنتج تفسيرات إنجليزية؛ الإصدار 3 يربط قاموس أعمال عربي للمصطلحات الداخلية، يدعم RTL في العناوين والجداول، يُصدّر ملخص PDF عربي، يُنبّه عند جودة بيانات ضعيفة، يقترح خطوات تحسين نموذج البيانات، ويُتاح عبر برنامج «Microsoft AI Data Partners MENA».</p>
      <p>القدرات الأساسية: أسئلة عربية طبيعية؛ تقارير من وصف؛ تفسير أرقام؛ اقتراح DAX؛ ملخصات إدارية.</p>
      <p>للمبدعين العرب: استشارات «ذكاء مالي ولوجستي» — من يُبني نموذج بيانات ولوحات Copilot لشركة 50–800 موظف بـ3200–19200 دولار + 480–1950 دولار/شهر للدعم يخدم CFOs الذين يريدون قرارات أسرع دون توظيف فريق تحليل كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Power BI Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>نموذج بيانات + لوحات Copilot (مصادر، أمان، تدريب):</strong> 10–22 يومًا — 3200–19200 دولار.</li>
          <li><strong>صيانة تقارير ودقة إجابات شهريًا:</strong> — 480–1950 دولار/مؤسسة/شهر.</li>
          <li><strong>حزمة 8 قوالب لوحة عربية لقطاعات (تجزئة، تعليم، لوجستيات):</strong> — 105–420 دولار/حزمة.</li>
          <li><strong>ورش «قرارات من البيانات بالعربية مع Power BI Copilot»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Power BI</span>
        <span class="tag">Analytics</span>
        <span class="tag">Copilot</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>SurveyMonkey Genius 2 Arabic: استبيان يفكر معك — أسئلة، تحليل، وتوصيات ربح من أمر عربي!</h2>
      <p class="article-lead">«نريد نعرف لماذا تتوقف العملاء عن الاشتراك — ولا نعرف كيف نصيغ السؤال». في 24 نوفمبر 2026، أطلقت <strong>SurveyMonkey</strong> <strong>SurveyMonkey Genius 2 Arabic</strong>: مولّد استبيانات ذكي يقرأ هدف البحث بالعربية، يُقترح أسئلة محايدة وخيارات إجابة RTL، يُصمّم تدفقًا منطقيًا للفروع، يكتب رسالة دعوة للمشاركة بلهجة العلامة، بعد الجمع يُجمّع الإجابات المفتوحة في موضوعات، يقيس رضا العملاء ومحركات التسرب، يُبرز اقتباسات للعرض التقديمي، يُقترح حملات retargeting وتحسينات منتج، يُرسل تنبيهات عند تغيّر NPS، ويتكامل مع HubSpot وMailchimp وGoogle Sheets — للشركات الناشئة والوكالات وأقسام التسويق في المنطقة.</p>
      <p>المشكلة التي حلّتها: Genius الأول كان يُنتج أسئلة إنجليزية أو يُهمل خيارات «لا أعرف» الثقافية؛ الإصدار 2 يدعم قوالب «رضا عميل» و«تسعير» و«موظفين»، تحققًا من طول الاستبيان، ترجمة ثنائية الاتجاه عند الحاجة، إخفاء بيانات شخصية تلقائيًا، وتقارير تنفيذية PDF عربية جاهزة للاجتماع.</p>
      <p>القدرات الأساسية: استبيان من وصف عربي؛ تحليل موضوعات؛ NPS ورضا؛ توصيات عمل؛ تكامل تسويق.</p>
      <p>للمبدعين العرب: خدمة «بحث سوق سريع» — من يُسلّم استبيانًا مع تحليل Genius وعرض قرار للإدارة خلال 7 أيام بـ650–4800 دولار للمشروع يجذب العلامات التي تُطلق منتجات جديدة دون ميزانية بحث تقليدية ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من SurveyMonkey Genius 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم استبيان + جمع + تقرير Genius (هدف، تحليل، عرض):</strong> 5–10 أيام — 650–4800 دولار.</li>
          <li><strong>متابعة NPS واستبيانات ربع سنوية:</strong> — 220–980 دولار/عميل/ربع.</li>
          <li><strong>حزمة 6 قوالب استبيان عربية لقطاعات (SaaS، تجزئة، تعليم):</strong> — 68–272 دولار/حزمة.</li>
          <li><strong>ورش «قرارات من الأصوات بالعربية مع SurveyMonkey Genius»:</strong> — 34–136 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">SurveyMonkey</span>
        <span class="tag">Research</span>
        <span class="tag">NPS</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 24-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="24-11-2026 -- 12-AM.html">
          📰 24 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "24-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/24-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/24-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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