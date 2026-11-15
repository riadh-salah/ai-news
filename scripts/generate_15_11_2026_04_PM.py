#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 15-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "15-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Anthropic Claude Cowork 2 Arabic · Salesforce Agentforce 3 Arabic · "
    "Figma Make 2 Arabic · ElevenLabs Dubbing Studio 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Anthropic Claude Cowork 2 Arabic، Salesforce Agentforce 3 Arabic، Figma Make 2 Arabic، ElevenLabs Dubbing Studio 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 15 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Anthropic Claude Cowork 2 Arabic الذي يُشغّل فريقًا افتراضيًا يكتب ويحلل ويُراجع عقودًا بالفصحى قبل انتهاء اجتماعك، إلى Salesforce Agentforce 3 Arabic الذي يُجيب عملاءك ويُحدّث الصفقات ويُرسل عروضًا بالعربية ليلًا دون تدخل، ومن Figma Make 2 Arabic الذي يُحوّل إطار التصميم إلى تطبيق يعمل من وصف عربي، إلى ElevenLabs Dubbing Studio 2 Arabic الذي يُضاعف فيديوهاتك بأصوات عربية طبيعية لعشرة أسواق — أربع قصص مسائية في 15 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ لقادة الفرق والتجار ومطوري المنتجات وصناع المحتوى: التعاون أصبح وكيلًا، المبيعات أصبحت أتمتة ذكية، التصميم أصبح كودًا، والترجمة أصبحت إنتاجًا بالجملة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 15 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Anthropic Claude Cowork 2 Arabic: مكتب افتراضي يُنفّذ مهام الفريق — بحث، صياغة، ومراجعة!</h2>
      <p class="article-lead">«ثلاثة تقارير قانونية وملخص مجلس إدارة بالعربية قبل الساعة السادسة — والفريق منشغل في مكالمات العملاء». في 15 نوفمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude Cowork 2 Arabic</strong>: بيئة تعاون يُشغّل فيها عدة وكلاء Claude مهامًا متوازية — قراءة مستندات، استخراج بنود، صياغة ردود رسمية، مقارنة إصدارات، تلخيص اجتماعات مسجّلة — مع لوحة موافقات بالفصحى، سجل تدقيق، وحدود صلاحيات لكل دور، وتكامل Slack وGoogle Drive وMicrosoft 365 — للمحامين وفرق الامتثال وإدارات الاستشارات.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُكرر المهام أو يخلط بين مصادر؛ Cowork 2 يُوزّع العمل على وكلاء متخصصين (باحث، كاتب، مدقق)، يُوقف التنفيذ عند البيانات الحساسة، يُحسّن الفصحى الإدارية والمصطلحات القانونية العربية، يُدعم قوالب «عقد» و«مذكرة مجلس» و«رد رسمي على شكوى»، وبرنامج شريك «Cowork Professional Services MENA».</p>
      <p>القدرات الأساسية: Arabic multi-agent workflows؛ مراجعة ثنائية البشر والآلة؛ تصدير Word وPDF؛ سياسات احتفاظ بالبيانات؛ وضع مؤسسي مع SSO.</p>
      <p>للمبدعين العرب: خدمة «مكتب معرفة مؤتمت» للشركات الصغيرة — من يُدير 12 عميلًا باشتراك 250–890 دولار/شهر + إعداد سير عمل 600–3200 دولار يبيع قدرة تنفيذية بلا توظيف محللين بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude Cowork 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم سير عمل (امتثال، عقود، تقارير):</strong> 4–10 أيام — 600–3200 دولار/عميل.</li>
          <li><strong>اشتراك تشغيل ومراجعة شهرية:</strong> — 250–890 دولار/شهر.</li>
          <li><strong>حزم قطاعية (قانون، تعليم، رعاية صحية):</strong> — 75–310 دولار/حزمة.</li>
          <li><strong>ورش «فرق تعاون ذكية بالعربية»:</strong> — 60–240 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Cowork</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Salesforce Agentforce 3 Arabic: وكلاء مبيعات وخدمة يعملون 24/7 — صفقات، دعم، وولاء!</h2>
      <p class="article-lead">«عميل كتب بالعربية الساعة 11 ليلًا — يريد عرض أسعار وتعديل عقد والرد خلال ساعة». في 15 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 3 Arabic</strong>: منصة وكلاء ترتبط بـCRM، تفهم اللهجات الخليجية والمصرية والشامية في سياق احترافي، تُجيب على الاستفسارات، تُحدّث المراحل، تُنشئ عروض PDF بالفصحى، تُحوّل المحادثة إلى إنسان عند الحاجة، تُحترم حدود الخصم والموافقات — للتجارة الإلكترونية والعقارات والتعليم والتأمين في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُخطئ في الأرقام والعملات أو يُكرر ردودًا جامدة؛ Agentforce 3 يُربط بكتالوج المنتجات الحي، يُطبّق قواعد التسعير، يُسجّل كل تفاعل للمراجعة، يتكامل مع WhatsApp Business وInstagram ومواقع الويب العربية، يُشغّل وضع «مستشار مبيعات» و«موظف خدمة» و«مُجمّع تقييمات»، وشهادة «Agentforce Partner Gulf».</p>
      <p>القدرات الأساسية: Arabic omnichannel agents؛ تلخيص محادثات للمديرين؛ توقع احتمال الإغلاق؛ حملات متابعة آلية؛ لوحة امتثال للتشريعات المحلية.</p>
      <p>للمبدعين العرب: وكالة «وكلاء مبيعات عربية جاهزة خلال أسبوع». من يبيع 8 شركات بـ2200–12000 دولار/إعداد + 350–1400 دولار/شهر للصيانة يحوّل CRM من سجل بيانات إلى محرّك إيرادات ليلي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 3 Arabic؟</h3>
        <ul>
          <li><strong>إطلاق وكيل مبيعات/خدمة متكامل:</strong> 7–21 يومًا — 2200–12000 دولار/مشروع.</li>
          <li><strong>صيانة وتحسين المحادثات والقواعد:</strong> — 350–1400 دولار/شهر.</li>
          <li><strong>حزم قوالب (عقارات، متاجر، أكاديميات):</strong> — 90–380 دولار/قطاع.</li>
          <li><strong>تدريب فرق المبيعات على الإشراف على الوكلاء:</strong> — 70–280 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Agentforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Figma Make 2 Arabic: من التصميم إلى تطبيق حي — واجهات، نماذج، واختبار سريع!</h2>
      <p class="article-lead">«العميل أعجبه التصميم العربي لكنه يريد نقرًا على الزرين وتسجيل دخول تجريبي قبل نهاية الأسبوع». في 15 نوفمبر 2026، أطلقت <strong>Figma</strong> <strong>Make 2 Arabic</strong>: طبقة ذكاء داخل Figma تُقرأ الإطارات RTL، تُولّد مكونات تفاعلية، تُربط بقواعد بيانات تجريبية، تُصدّر كود React أو Flutter مع دعم اتجاه النص، تُتيح مشاركة رابط تجريبي للعميل، وتُزامن مع Design System للفرق — للوكالات الرقمية والشركات الناشئة ومدارس ريادة الأعمال.</p>
      <p>المشكلة التي حلّتها: Make 1 كان يُهمل محاذاة العربية والأيقونات؛ الإصدار 2 يُحترم tokens ومتغيرات العلامة، يُولّد نماذج دخول ودفع ولوحات تحكم بالفصحى، يُدمج مع Supabase وFirebase للنماذج الأولية، يُصدّر Storybook للفرق الهندسية، وبرنامج «Figma Make Partner Studio MENA».</p>
      <p>القدرات الأساسية: Arabic RTL code export؛ نماذج أولية ببيانات وهمية؛ تعليقات العميل مترجمة؛ قوالب SaaS وتجارة إلكترونية؛ فحص وصول أساسي.</p>
      <p>للمبدعين العرب: عرض «من Figma إلى MVP في 72 ساعة». من ينفّذ 6 مشاريع شهريًا بـ1800–9500 دولار للمشروع يقلّص دورة البيع بين المصمم والمطور إلى أيام.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Figma Make 2 Arabic؟</h3>
        <ul>
          <li><strong>نموذج أولي تفاعلي من تصميم جاهز:</strong> 3–7 أيام — 1800–9500 دولار/مشروع.</li>
          <li><strong>اشتراك تحويل تصاميم أسبوعية للفرق:</strong> — 400–1600 دولار/شهر.</li>
          <li><strong>مكتبة مكونات عربية جاهزة للبيع:</strong> — 50–220 دولار/حزمة.</li>
          <li><strong>معسكر «تصميم يتحول إلى كود» للطلاب:</strong> — 45–180 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Figma</span>
        <span class="tag">Make</span>
        <span class="tag">Design</span>
        <span class="tag">Prototype</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ElevenLabs Dubbing Studio 2 Arabic: دبلجة ذكية لعشرة أسواق — يوتيوب، دورات، وإعلانات!</h2>
      <p class="article-lead">«فيديو تدريبي إنجليزي مدته 40 دقيقة — أريد نسخة عربية فصحى ونسخة خليجية ونشرها غدًا على المنصات». في 15 نوفمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 2 Arabic</strong>: استوديو يُفصل الصوت عن الفيديو، يُترجم بسياق احترافي، يُولّد أصواتًا عربية متعددة الأنماط، يُزامن حركة الشفاه تقريبيًا، يُحافظ على موسيقى الخلفية، يُصدّر ترجمات SRT بالعربية، ويتكامل مع YouTube وVimeo ومنصات التعلم — للمدربين والعلامات العالمية والمؤثرين الذين يستهدفون MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُخلط الأصوات المتداخلة أو يُسيء ترجمة المصطلحات التقنية؛ Dubbing Studio 2 يُتيح قاموس مصطلحات لكل عميل، يُراجع النطق بالتشكيل الاختياري، يُشغّل وضع «حلقة بودكاست مرئية» و«إعلان 30 ثانية»، يُدعم دفعات عشرات الفيديوهات، وAPI للوكالات التي تبيع توطينًا سريعًا.</p>
      <p>القدرات الأساسية: Arabic multi-dialect voices؛ تحكم بنبرة وجنس الصوت؛ علامة مائية للمسودات؛ تحليلات مشاهدة حسب اللغة؛ شريك «ElevenLabs Localization MENA».</p>
      <p>للمبدعين العرب: خدمة «قناة ثنائية اللغة في أسبوع». من يدير 25 عميلًا بـ150–900 دولار/فيديو أو 500–2800 دولار/شهر للباقات يحوّل التوطين من شهر عمل إلى يوم إنتاج.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 2 Arabic؟</h3>
        <ul>
          <li><strong>دبلجة وتحرير فيديو تعليمي/تسويقي:</strong> — 150–900 دولار/فيديو حسب الطول.</li>
          <li><strong>باقة شهرية لقناة أو أكاديمية:</strong> — 500–2800 دولار/شهر.</li>
          <li><strong>قاموس مصطلحات وصوت علامة مخصص:</strong> 2–5 أيام — 400–2100 دولار.</li>
          <li><strong>دورات «توطين محتوى بالذكاء الاصطناعي»:</strong> — 42–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Voice</span>
        <span class="tag">Localization</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 15-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="15-11-2026 -- 04-PM.html">
          📰 15 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "15-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/15-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/15-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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