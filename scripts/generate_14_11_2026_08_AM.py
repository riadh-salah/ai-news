#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 14-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "14-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google Gemini Live 2 Arabic · Anthropic Claude Skills Arabic · "
    "Shopify Sidekick 3 Arabic · ElevenLabs Dubbing Studio 4 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Gemini Live 2 Arabic، Anthropic Claude Skills Arabic، Shopify Sidekick 3 Arabic، ElevenLabs Dubbing Studio 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 14 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Google Gemini Live 2 Arabic الذي يُجري محادثة صوتية حية بالفصحى ويُترجم بينك وبين عميل أجنبي أثناء الاجتماع، إلى Anthropic Claude Skills Arabic الذي يُحوّل خبرتك القانونية أو المحاسبية إلى مهارة جاهزة للبيع، ومن Shopify Sidekick 3 Arabic الذي يُقترح حملات تسويق ويُعد وصف منتجك بالعربية في دقيقتين، إلى ElevenLabs Dubbing Studio 4 Arabic الذي يُدبلج فيديوهاتك بلهجات عربية متعددة مع مزامنة شفاه — أربع قصص صباحية في 14 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للتجار والمبدعين والمستشارين: الصوت أصبح جسرًا، المهارات أصبحت منتجًا، المتاجر تحتاج ذكاءً يوميًا، والفيديو يريد عربية أصيلة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 14 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Gemini Live 2 Arabic: محادثة صوتية حية بالعربية — ترجمة فورية، سياق، وWorkspace!</h2>
      <p class="article-lead">«أنا في مكالمة مع مستثمر من سنغافورة والعميل يريدني أن أُوضّح العقد بالعربية — والوقت ينفد». في 14 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>Gemini Live 2 Arabic</strong>: تجربة صوتية ثنائية الاتجاه تفهم الفصحى واللهجات الخليجية والمصرية، تُترجم لحظيًا بين العربية والإنجليزية والفرنسية، تُلخص ما قيل بعد الاجتماع، تُربط بـGmail وCalendar وMeet وDrive، تُحترم سياسات المؤسسة في Workspace — للمبيعات والدعم والتعليم عن بُعد في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يقطع المتحدث أو يُشوّه المصطلحات التقنية؛ الإصدار 2 يُقلّل زمن الاستجابة إلى أقل من 400 مللي ثانية، يُميّز بين المتكلمين في الغرفة، يُعرّف على أسماء منتجات العميل، يُسجّل بموافقة صريحة فقط، يُدمج مع Vertex للفرق الكبيرة، ويُوفّر وضع «مترجم مؤتمرات» لوكلاء السفر والعقارات.</p>
      <p>القدرات الأساسية: Arabic live captions؛ مفردات مخصّصة لكل عميل؛ تكامل Android وPixel؛ حزم امتثال للبنوك؛ شهادة شريك «Gemini Live MENA».</p>
      <p>للمبدعين العرب: تجربة ما بعد البيع — «Gemini Live Arabic لفرق المبيعات في 3 أيام» مع قواميس مصطلحات واختبارات صوت. من يُشغّل 12 عميلًا باشتراك إعداد 520–4100 دولار + دعم شهري 190–1100 دولار يبيع لغةً حيةً لفرق تكسب بالصوت.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Gemini Live 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Gemini Live (قواميس، سياسات تسجيل، تدريب فرق):</strong> 3–10 أيام — 520–4100 دولار/عميل.</li>
          <li><strong>مراقبة جودة ترجمة وتحديث مصطلحات شهريًا:</strong> — 190–1100 دولار/شهر.</li>
          <li><strong>حزم قطاعية (سياحة، طب، لوجستيك):</strong> — 46–198 دولار/حزمة.</li>
          <li><strong>دورات «مكالمات ثنائية اللغة بالعربية مع Gemini Live»:</strong> — 42–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Gemini</span>
        <span class="tag">Voice</span>
        <span class="tag">Live</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Anthropic Claude Skills Arabic: حوّل خبرتك إلى مهارة AI — سوق، دمج، واشتراكات!</h2>
      <p class="article-lead">«محامٍ يكتب عقودًا كل يوم — ويريد أن يبيع «مهارة مراجعة عقد إيجار عربي» دون كتابة كود». في 14 نوفمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude Skills Arabic</strong>: طبقة فوق Claude تسمح بإنشاء حزم تعليمات وأدوات وملفات مرجعية بالعربية، نشرها في Skills Marketplace أو بيعها خاصًا، تشغيلها داخل Claude.ai وAPI وClaude Code — للمحامين والمحاسبين والمهندسين والمدربين في العالم العربي.</p>
      <p>المشكلة التي حلّتها: البرومبتات تتسرب وتُنسخ؛ Skills تُغلّف المعرفة كمنتج قابل للترخيص، تُحدّث نسخًا للمشتركين، تُسجّل استخدامًا عادلًا، تُدعم RTL في الوثائق، تُراجع المحتوى القانوني قبل النشر، وتتكامل مع Stripe للمدفوعات المتكررة.</p>
      <p>القدرات الأساسية: Arabic skill authoring؛ تقييم جودة آلي؛ نسخ تجريبية للمشترين؛ تكامل Notion وDrive كمصادر؛ برنامج «Skills Partner MENA».</p>
      <p>للمبدعين العرب: استوديو مهارات — «حزمة 5 Skills عربية لقطاعك في أسبوع». من يبني 3 مهارات رابحة ويبيعها لـ200 مشترك بـ29–149 دولار/شهر يحوّل خبرةً محلية إلى دخل متكرر عالمي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude Skills Arabic؟</h3>
        <ul>
          <li><strong>بناء مهارة عربية (بحث، اختبارات، نشر، تسويق):</strong> 5–14 يومًا — 800–6500 دولار/مهارة.</li>
          <li><strong>اشتراكات مهارات للفرق (ترخيص، تحديثات، دعم):</strong> — 29–149 دولار/مقعد/شهر.</li>
          <li><strong>تخصيص مهارات للمؤسسات (علامة بيضاء، SSO):</strong> — 3200–28000 دولار/عقد.</li>
          <li><strong>دورات «تصميم مهارات Claude بالعربية للبيع»:</strong> — 55–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Skills</span>
        <span class="tag">Marketplace</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Shopify Sidekick 3 Arabic: مدير متجر ذكي بالعربية — وصف، حملات، وتحليلات!</h2>
      <p class="article-lead">«متجري على Shopify والعميل يسأل: لماذا لا تُرسلون عروض رمضان مبكرًا؟ — وأنا وحدي». في 14 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: مساعد تاجر يفهم لوحة التحكم بالعربية، يُعيد صياغة أوصاف منتجات SEO-friendly، يُقترح حملات بريد وإعلانات Meta مرتبطة بالمخزون، يُحذّر من منتجات راكدة، يُولّد تقارير أسبوعية بالفصحى — لـSMB وD2C في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان يكتب إنجليزية ثم يُترجم بأسلوب ركيك؛ الإصدار 3 يُفهم مواسم عربية (عيد، رمضان، العودة للمدارس)، يُراعي ضريبة القيمة المضافة المحلية، يُربط بوكلاء الشحن الإقليميين، يُشغّل A/B على العناوين العربية، ويُتزامن مع Shop app وPOS.</p>
      <p>القدرات الأساسية: Arabic catalog optimizer؛ قوالب حملات WhatsApp Business؛ تكامل Klaviyo وGoogle Ads؛ تنبيهات مخزون بالعربية؛ شريك «Sidekick MENA Agency».</p>
      <p>للمبدعين العرب: وكالات تجارة إلكترونية — «Sidekick 3 Arabic كمدير متجر افتراضي». من يدير 15 متجرًا بـ350–2200 دولار/شهر + إعداد أولي 400–2800 دولار يبيع نموًا دون توظيف فريق تسويق كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Sidekick (كتالوج، حملات، تدريب تاجر):</strong> 2–7 أيام — 400–2800 دولار/متجر.</li>
          <li><strong>إدارة نمو شهرية (حملات، أوصاف، تقارير):</strong> — 350–2200 دولار/شهر.</li>
          <li><strong>حزم مواسم (رمضان، عيد، تخفيضات):</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>دورات «تشغيل Shopify Sidekick بالعربية للتجار»:</strong> — 38–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ElevenLabs Dubbing Studio 4 Arabic: دبلجة فيديو بلهجات عربية — صوت، شفاه، وتوزيع!</h2>
      <p class="article-lead">«قناة تعليمية عربية تريد نسخة خليجية ومصرية لنفس الكورس — والميزانية لا تسمح بفرق دبلجة». في 14 نوفمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 4 Arabic</strong>: استوديو يستنسخ نبرة المُدرّب، يُترجم السكربت مع مراجعة ثقافية، يُزامن الشفاه للوجوه الظاهرة، يُصدّر مسارات لـYouTube وTikTok ومنصات تعليم، يُحترم حقوق الصوت بعقود موقّعة — للمؤثرين والجامعات ودور النشر الرقمية.</p>
      <p>المشكلة التي حلّتها: الإصدار 3 كان يبدو «روبوتيًا» في الحروف العربية الثقيلة؛ الإصدار 4 يُحسّن تشديد وهمزة وtanween، يُقسّم المشاريع إلى workflows مراجعة بشرية، يُدعم لهجات خليجية ومصرية وشامية و مغربية، يُوفّر قياس MOS للجودة، وAPI للوكالات.</p>
      <p>القدرات الأساسية: Arabic dialect packs؛ مراجعة جماعية بالعربية؛ مكتبة أصوات مرخّصة؛ تصدير SRT وVTT؛ برنامج شريك «Dubbing MENA».</p>
      <p>للمبدعين العرب: استوديوهات محتوى — «دبلجة دورة كاملة بثلاث لهجات في 10 أيام». من يُسلّم 4 مشاريع/ربع بـ1800–15000 دولار + retainer 500–3800 دولار/شهر يفتح سوقًا ضخمًا للتعليم والإعلان بالعربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>دبلجة مشروع (ترجمة، صوت، مراجعة، تصدير):</strong> 6–16 يومًا — 1800–15000 دولار/مشروع.</li>
          <li><strong>اشتراك استوديو شهري (حصة دقائق + مراجعة):</strong> — 500–3800 دولار/شهر.</li>
          <li><strong>حزم لهجات إضافية (قانونية، طبية، أطفال):</strong> — 62–245 دولار/حزمة.</li>
          <li><strong>دورات «دبلجة عربية احترافية مع ElevenLabs»:</strong> — 50–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Video</span>
        <span class="tag">Voice</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 14-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="14-11-2026 -- 08-AM.html">
          📰 14 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "14-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/14-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/14-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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