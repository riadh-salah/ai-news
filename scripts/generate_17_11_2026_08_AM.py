#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 17-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "17-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Agentforce 3 Arabic · Adobe Firefly Video 2 Arabic · "
    "Replit Agent 3 Arabic · ElevenLabs Conversational AI 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Agentforce 3 Arabic، Adobe Firefly Video 2 Arabic، Replit Agent 3 Arabic، ElevenLabs Conversational AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 17 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌅 نشرة AI العالمية</span>
      <h1>من Salesforce Agentforce 3 Arabic الذي يُغلق الصفقات ويُجيب العملاء باللهجة التي يفهمونها، إلى Adobe Firefly Video 2 Arabic الذي يُحوّل فكرة صباحية إلى حركة بصرية جاهزة للحملة، ومن Replit Agent 3 Arabic الذي يبني تطبيقًا كاملًا من وصف عربي، إلى ElevenLabs Conversational AI 3 Arabic الذي يُشغّل مركز اتصال ذكيًا بأصوات عربية طبيعية — أربع قصص صباحية في 17 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ مع أول قهوة!</h1>
      <p class="hero-sub">صباح يشبه لوحة تحكم للأعمال الرقمية: المبيعات تتحدث العربية، الفيديو يولد من النص، التطبيق يُنجز بخطوة واحدة، والصوت يصبح واجهة خدمة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 17 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Agentforce 3 Arabic: وكلاء مبيعات ودعم يتحدثون مع عملائك بالعربية</h2>
      <p class="article-lead">«فريق المبيعات مشغول والعميل يكتب بالعربية على واتساب — أريد وكيلًا يفهم السياق ويُكمّل الرحلة دون أن أضيع الصفقة». في 17 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 3 Arabic</strong>: طبقة وكلاء ذكية تُقرأ بيانات CRM، تُجيب استفسارات بالفصحى واللهجات الخليجية والمصرية والشامية، تُقترح عروضًا مخصصة، تُنشئ مهام متابعة للبشر، تُسجّل المحادثة في السجل الموحد، وتلتزم بسياسات الامتثال المحلية — للتجارة الإلكترونية والبنوك والعقارات والتعليم في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: Agentforce 2 كان يُبدّل بين العربية والإنجليزية في الجملة الواحدة أو يُجيب بشروط عامة؛ الإصدار 3 يدعم قواميس منتجات بالعربية، تكامل WhatsApp Business وInstagram، تلخيصًا آليًا للمكالمات، موافقات بشرية على الخصومات الكبيرة، قوالب «تأهيل عميل» و«متابعة عربة متروكة» و«تجديد اشتراك»، وبرنامج شركاء «Agentforce MENA Revenue».</p>
      <p>القدرات الأساسية: وكلاء مبيعات ودعم بالعربية؛ تكامل CRM؛ قنوات متعددة؛ موافقات بشرية؛ تقارير تحويل وإيراد.</p>
      <p>للمبدعين العرب: خدمة «وكيل مبيعات جاهز في 10 أيام» — من يُسلّم 4 تنفيذات شهريًا بـ2800–16000 دولار للمشروع يحوّل الذكاء الاصطناعي إلى خط إيرادات مباشر لشركات لا تملك فرق دعم ليلية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم ونشر وكلاء مبيعات ودعم عربية:</strong> 8–18 يومًا — 2800–16000 دولار.</li>
          <li><strong>إدارة وتحسين أداء الوكلاء شهريًا:</strong> — 720–3400 دولار/عميل/شهر.</li>
          <li><strong>قوالب محادثات قطاعية (عقارات، تعليم، تجزئة):</strong> — 85–380 دولار/حزمة.</li>
          <li><strong>ورش «من الرسالة الأولى إلى الإغلاق» لفِرق المبيعات:</strong> — 75–295 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Agents</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Adobe Firefly Video 2 Arabic: من فكرة تسويقية إلى فيديو — آمن تجاريًا وجاهز للحملة</h2>
      <p class="article-lead">«نحتاج فيديو قصيرًا لإطلاق المنتج غدًا — الفريق الإبداعي مكتوف والعلامة تطلب نصًا عربيًا واضحًا». في 17 نوفمبر 2026، أطلقت <strong>Adobe</strong> <strong>Firefly Video 2 Arabic</strong>: مولّد فيديو مدمج في Creative Cloud يقرأ موجزًا بالعربية، يُنتج لقطات منتجات وبيئات بحركة سلسة، يُضيف عناوين ومؤثرات بخطوط RTL، يحترم مكتبة أصول العلامة المرخصة فقط، ويُصدّر صيغًا جاهزة لمنصات الإعلانات والسوشيال — للوكالات وقِطاعات التجزئة والسياحة والفعاليات.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان محدودًا في طول النص العربي ولقطات الوجوه في بعض الأسواق؛ Video 2 يدعم storyboard تفاعليًا، تحكمًا في الإطار واللون بلغة طبيعية، تكامل Premiere وAfter Effects، علامة Content Credentials للشفافية، قوالب «إطلاق منتج» و«عرض موسمي» و«دعوة فعالية»، وبرنامج «Adobe Creative MENA Pro».</p>
      <p>القدرات الأساسية: نص عربي إلى فيديو؛ أصول آمنة تجاريًا؛ عناوين RTL؛ تكامل Adobe؛ تصدير إعلانات.</p>
      <p>للمبدعين العرب: استوديو «حزمة حملة في 48 ساعة» — من ينفّذ 10 حزم شهريًا بـ950–5200 دولار للحزمة يبيع سرعة إبداعية للعلامات التي تتنافس على انتباه المشاهد في رمضان والمواسم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Adobe Firefly Video 2 Arabic؟</h3>
        <ul>
          <li><strong>إنتاج فيديوهات حملات من موجز عربي:</strong> 2–6 أيام — 950–5200 دولار/حزمة.</li>
          <li><strong>اشتراك إنتاج فيديو شهري (8–20 مقطعًا):</strong> — 380–1650 دولار/عميل/شهر.</li>
          <li><strong>قوالب storyboard عربية جاهزة (قطاع محدد):</strong> — 55–240 دولار/مجموعة.</li>
          <li><strong>تدريب فرق تسويق على Firefly Video:</strong> — 62–248 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Adobe</span>
        <span class="tag">Firefly</span>
        <span class="tag">Video</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Replit Agent 3 Arabic: تطبيق ويب كامل من جملة عربية — قاعدة بيانات، واجهة، ونشر</h2>
      <p class="article-lead">«لديّ فكرة منصة حجز بالعربية — لا وقت لتوظيف مطورين ثلاثة أشهر». في 17 نوفمبر 2026، أطلقت <strong>Replit</strong> <strong>Agent 3 Arabic</strong>: وكيل بناء يفهم المتطلبات بالفصحى، يُصمّم واجهات RTL، يولّد API وقاعدة بيانات، يُضيف دفعًا ومصادقة، يُشغّل اختبارات، وينشر التطبيق على Replit أو Docker أو VPS — للمؤسسين المستقلين والمدارس الرقمية وشركات الخدمات السريعة النمو.</p>
      <p>المشكلة التي حلّتها: Agent 2 كان يتوقف عند واجهة بسيطة أو يُهمل العربية في الحقول؛ الإصدار 3 يدعم تعدد اللغات، تكامل Stripe وMoyasar، قوالب «منصة دورات» و«حجز مواعيد» و«كتالوج B2B»، مراجعة أمان تلقائية، تعليقات كود ثنائية اللغة، وبرنامج «Replit Builders Arabia».</p>
      <p>القدرات الأساسية: بناء تطبيق من وصف عربي؛ RTL؛ قاعدة بيانات وAPI؛ دفع ومصادقة؛ نشر فوري.</p>
      <p>للمبدعين العرب: عرض «MVP في أسبوع» — من يُسلّم 3 منتجات شهريًا بـ2200–12500 دولار للمنتج + 180–750 دولار/شهر للصيانة يبيع سرعة الإطلاق لرواد أعمال يتنافسون على السوق المحلي قبل المستثمرين الأجانب.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Agent 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء MVP كامل من متطلبات عربية:</strong> 5–12 يومًا — 2200–12500 دولار.</li>
          <li><strong>صيانة وتحسين التطبيق شهريًا:</strong> — 180–750 دولار/عميل/شهر.</li>
          <li><strong>قوالب تطبيقات عربية جاهزة (قطاع محدد):</strong> — 120–520 دولار/قالب.</li>
          <li><strong>معسكر «من الفكرة إلى النشر في 5 أيام»:</strong> — 95–380 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Agent</span>
        <span class="tag">No-Code</span>
        <span class="tag">MVP</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ElevenLabs Conversational AI 3 Arabic: مركز اتصال ذكي بأصوات عربية — رد، حجز، وتصعيد</h2>
      <p class="article-lead">«عملاؤنا يتصلون بالعربية ونريد ردًا فوريًا دون انتظار 20 دقيقة — مع الحفاظ على طابع بشري دافئ». في 17 نوفمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Conversational AI 3 Arabic</strong>: منصة صوت تُشغّل وكلاء هاتف وويب، تتعرف على اللهجات، تُلخص المكالمات، تحجز مواعيد، تُحوّل إلى إنسان عند الحاجة، تتكامل مع HubSpot وزوهو وتطبيقات مخصصة عبر API — للعيادات والتعليم والضيافة والتجارة الإلكترونية.</p>
      <p>المشكلة التي حلّتها: الإصدار السابق كان يقرأ الأرقام والتواريخ بطريقة أجنبية أو ينقطع في الضوضاء؛ Conversational AI 3 يدعم إلغاء الصدى، نبرات متعددة للعلامة، امتثال تسجيل المكالمات حسب البلد، تحليلات نية العميل، قوالب «استقبال عيادة» و«تأكيد طلب» و«استبيان رضا»، وبرنامج «ElevenLabs Voice MENA».</p>
      <p>القدرات الأساسية: صوت عربي طبيعي؛ وكلاء هاتف وويب؛ حجز وتصعيد؛ تكامل CRM؛ تحليلات المكالمات.</p>
      <p>للمبدعين العرب: خدمة «خط ساخن ذكي في 14 يومًا» — من ينشر 5 مراكز اتصال شهريًا بـ1900–11000 دولار للتنفيذ + 290–1400 دولار/شهر للتشغيل يبيع تجربة خدمة ليلية ونهارية دون تضخيم رواتب.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Conversational AI 3 Arabic؟</h3>
        <ul>
          <li><strong>تصميم ونشر مركز اتصال صوتي عربي:</strong> 10–20 يومًا — 1900–11000 دولار.</li>
          <li><strong>تشغيل وتحسين الوكلاء الصوتيين شهريًا:</strong> — 290–1400 دولار/عميل/شهر.</li>
          <li><strong>سكربتات مكالمات جاهزة (قطاع محدد):</strong> — 40–175 دولار/مجموعة.</li>
          <li><strong>ورش «صوت العلامة بالذكاء الاصطناعي»:</strong> — 58–232 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Voice</span>
        <span class="tag">Call Center</span>
        <span class="tag">Conversational</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 17-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="17-11-2026 -- 08-AM.html">
          📰 17 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "17-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/17-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/17-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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