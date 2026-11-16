#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "16-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI Sora 2 Pro Arabic · Zoom AI Companion 3 Arabic · "
    "Jasper Marketing AI 3 Arabic · Lovable Dev AI 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI Sora 2 Pro Arabic، Zoom AI Companion 3 Arabic، Jasper Marketing AI 3 Arabic، Lovable Dev AI 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 16 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من OpenAI Sora 2 Pro Arabic الذي يُحوّل نصًا بالفصحى إلى فيديو سينمائي دقيق مع شعارات ووجوه متسقة خلال دقائق، إلى Zoom AI Companion 3 Arabic الذي يُلخص اجتماعاتك بالعربية ويُسجّل المهام ويُرسل متابعات تلقائية للفريق، ومن Jasper Marketing AI 3 Arabic الذي يُبني حملات كاملة بصوت علامتك التجارية بلهجات عربية متعددة، إلى Lovable Dev AI 2 Arabic الذي يُطلق تطبيقًا ويبًا يعمل من فكرة مكتوبة بالعربية دون كتابة كود يدويًا — أربع قصص مسائية في 16 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ لصناع المحتوى وروّاد الأعمال ومديري المشاريع وفرق التسويق: الفيديو صار كلمة، الاجتماعات صارت محاضرًا ذكية، التسويق صار لهجة ثابتة، والتطبيقات صارت محادثة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 16 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI Sora 2 Pro Arabic: فيديو احترافي من جملة عربية — إعلان، قصة، ومنتج!</h2>
      <p class="article-lead">«العميل يريد إعلانًا لمنتج جديد بنسخة خليجية ومصرية قبل عرض الغد — والاستوديو محجوز بالكامل». في 16 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>Sora 2 Pro Arabic</strong>: منصة فيديو تُولّد مشاهد واقعية من وصف بالفصحى أو لهجات مدعومة، تُحافظ على شخصيات متسقة عبر اللقطات، تُدمج شعارات ونصوص RTL، تُنتج نسخ 9:16 و16:9، وتُصدّر بجودة بث مباشر — لوكالات الإعلان والمتاجر الإلكترونية وقنوات اليوتيوب العربية والمؤثرين.</p>
      <p>المشكلة التي حلّتها: Sora الأول كان يُشوّه النصوص العربية أو يغيّر ملامح الوجوه بين المشاهد؛ الإصدار 2 Pro يُثبت الهوية البصرية، يدعم storyboard من نقاط عربية، يحترم قوائم الموافقة للمؤسسات، يتكامل مع ChatGPT لكتابة السيناريو، يُوفّر قوالب «إعلان منتج» و«شرح خدمة» و«افتتاحية بودكاست»، وبرنامج «Sora Creators MENA Pro».</p>
      <p>القدرات الأساسية: Arabic text-in-video؛ شخصيات متسقة؛ موسيقى خلفية مرخّصة؛ تحرير لقطة بلقطة؛ تخزين آمن للفرق.</p>
      <p>للمبدعين العرب: استوديو «إعلان ذكي خلال 48 ساعة» — من ينفّذ 10 مشاريع شهريًا بـ1200–6800 دولار للفيديو + 280–1100 دولار/شهر لاشتراك الإدارة يُحوّل الإنتاج المرئي إلى خط إنتاج سريع دون طاقم تصوير ضخم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI Sora 2 Pro Arabic؟</h3>
        <ul>
          <li><strong>إنتاج إعلانات ومنتجات قصيرة بالذكاء الاصطناعي:</strong> 2–6 أيام — 1200–6800 دولار/فيديو.</li>
          <li><strong>اشتراك إنتاج شهري للعلامات (4–12 فيديو):</strong> — 280–1100 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب سيناريو عربية (تجزئة، عقارات، تعليم):</strong> — 55–240 دولار/حزمة.</li>
          <li><strong>ورش «فيديو تسويقي بالذكاء الاصطناعي»:</strong> — 62–248 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Sora</span>
        <span class="tag">Video</span>
        <span class="tag">Creative</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Zoom AI Companion 3 Arabic: اجتماعك يُختصر ويُترجم — ملخص، مهام، ومتابعة!</h2>
      <p class="article-lead">«ساعتان من اجتماع بالخلطيط بين العربية والإنجليزية — أحتاج ملخصًا بالفصحى وقائمة مهام واضحة خلال خمس دقائق». في 16 نوفمبر 2026، أطلقت <strong>Zoom</strong> <strong>AI Companion 3 Arabic</strong>: مساعد اجتماعات يُسجّل ويُلخّص المحادثات بالعربية الفصحى أو لهجات مدعومة، يُستخرج القرارات والمواعيد، يُرسل متابعات عبر البريد وSlack، يُقترح ردودًا على أسئلة متكررة، ويُتيح بحثًا داخل أرشيف الاجتماعات — للشركات الموزعة ومراكز الاتصال والجامعات والمنظمات غير الحكومية في المنطقة.</p>
      <p>المشكلة التي حلّتها: Companion 2 كان يُفوّت أسماء عربية أو يُخلط بين المتحدثين؛ الإصدار 3 يُحسّن التعرف على الأسماء المحلية، يدعم تبديل اللغة أثناء الاجتماع، يُربط Zoom Docs لتوليد محاضر رسمية، يحترم سياسات التسجيل المحلية، يتكامل مع Salesforce وAsana، وبرنامج شريك «Zoom AI Partner MENA».</p>
      <p>القدرات الأساسية: Arabic live summary؛ استخراج مهام؛ قوالب محاضر؛ ترجمة فورية مختلطة؛ لوحة امتثال للتسجيل.</p>
      <p>للمبدعين العرب: باقة «اجتماعات منظمة» للشركات المتوسطة — من يخدم 15 عميلًا بـ420–1850 دولار/شهر يُبيع انضباطًا تشغيليًا يوفر ساعات أسبوعية على كل فريق إدارة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoom AI Companion 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Zoom AI وسياسات تسجيل للمؤسسات:</strong> 3–10 أيام — 900–5200 دولار.</li>
          <li><strong>صيانة قوالب محاضر ومهام شهرية:</strong> — 420–1850 دولار/عميل/شهر.</li>
          <li><strong>تدريب مديري المشاريع على الاجتماعات الذكية:</strong> — 58–235 دولار/مقعد.</li>
          <li><strong>تقارير إنتاجية ربع سنوية من أرشيف الاجتماعات:</strong> — 380–1650 دولار/تقرير.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zoom</span>
        <span class="tag">Companion</span>
        <span class="tag">Meetings</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Jasper Marketing AI 3 Arabic: حملات بصوت علامتك — بريد، إعلان، ومحتوى اجتماعي!</h2>
      <p class="article-lead">«كل منصة تريد لهجة مختلفة لكن العلامة واحدة — أريد نظامًا يكتب بالعربية دون أن أفقد هويتنا». في 16 نوفمبر 2026، أطلقت <strong>Jasper</strong> <strong>Marketing AI 3 Arabic</strong>: منصة محتوى تُعرّف «صوت العلامة» بالفصحى واللهجات التجارية، تُولّد حملات بريد وإعلانات ومنشورات متسقة، تُختبر عناوين، تُربط بيانات CRM لتخصيص الرسائل، وتُصدّر تقويم محتوى شهرًا كاملًا — لوكالات التسويق وفرق النمو في التجزئة والتطبيقات والخدمات المالية العربية.</p>
      <p>المشكلة التي حلّتها: Jasper 2 كان يُكرر العبارات أو يخلط بين اللهجات؛ الإصدار 3 يُثبت قاموسًا لمصطلحات العلامة، يدعم موافقات قانونية قبل النشر، يُحسّن SEO العربي، يتكامل مع HubSpot وMailchimp وGoogle Ads، يُوفّر قوالب «رمضان» و«يوم التأسيس» و«إطلاق منتج»، وبرنامج «Jasper Agency MENA».</p>
      <p>القدرات الأساسية: Arabic brand voice؛ حملات متعددة القنوات؛ اختبار عناوين؛ تقويم محتوى؛ تحليلات أداء أولية.</p>
      <p>للمبدعين العرب: اشتراك «كاتب علامة افتراضي» — من يدير 8 علامات بـ580–2900 دولار/شهر لكل علامة يبيع اتساقًا لغويًا دون توظيف فريق كتابة كامل لكل عميل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Jasper Marketing AI 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء صوت علامة وإطلاق حملة شهر أول:</strong> 5–12 يومًا — 1100–6200 دولار.</li>
          <li><strong>إدارة محتوى وتحسين شهري:</strong> — 580–2900 دولار/علامة/شهر.</li>
          <li><strong>حزم نصوص إعلانية جاهزة (قطاع محدد):</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>دورات «كتابة تسويقية بالذكاء الاصطناعي»:</strong> — 54–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Jasper</span>
        <span class="tag">Marketing</span>
        <span class="tag">Content</span>
        <span class="tag">Brand</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Lovable Dev AI 2 Arabic: تطبيق ويب من فكرة عربية — واجهة، قاعدة بيانات، ونشر!</h2>
      <p class="article-lead">«لدي فكرة منصة حجوزات للعيادات بالعربية — لا وقت لتوظيف مطورين ثلاثة أشهر». في 16 نوفمبر 2026، أطلقت <strong>Lovable</strong> <strong>Dev AI 2 Arabic</strong>: بيئة بناء تُحوّل وصفًا بالفصحى إلى تطبيق React كامل مع واجهة RTL، قاعدة بيانات، مصادقة مستخدمين، لوحة إدارة عربية، ونشر على Vercel أو سحابة محلية — لروّاد الأعمال والمدربين والجمعيات والمستشارين الذين يريدون MVP سريعًا في العالم العربي.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُنتج كودًا صعب التعديل أو يُهمل المحاذاة العربية؛ Dev AI 2 يُولّد مكونات قابلة للتحرير، يدعم Supabase وFirebase، يُضيف فحوصات أمان أساسية، يتكامل مع Stripe للمدفوعات المحلية، يُتيح تصدير GitHub، وبرنامج «Lovable Builders MENA».</p>
      <p>القدرات الأساسية: Arabic prompt-to-app؛ RTL UI؛ لوحة إدارة؛ دفع واشتراكات؛ مراجعة كود قبل النشر.</p>
      <p>للمبدعين العرب: خدمة «MVP في أسبوع» — من يسلّم 6 تطبيقات شهريًا بـ1800–12000 دولار للمشروع + 350–1600 دولار/شهر للصيانة يبيع سرعة وصول للسوق لشركات ناشئة لا تملك فريقًا هندسيًا داخليًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lovable Dev AI 2 Arabic؟</h3>
        <ul>
          <li><strong>بناء ونشر MVP مخصص:</strong> 5–18 يومًا — 1800–12000 دولار/مشروع.</li>
          <li><strong>صيانة وميزات جديدة شهرية:</strong> — 350–1600 دولار/عميل/شهر.</li>
          <li><strong>قوالب تطبيقات جاهزة (حجوزات، تعليم، عضويات):</strong> — 95–420 دولار/قالب.</li>
          <li><strong>معسكر «ابنِ تطبيقك بالعربية في 3 أيام»:</strong> — 120–480 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lovable</span>
        <span class="tag">No-Code</span>
        <span class="tag">Apps</span>
        <span class="tag">Startup</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 16-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="16-11-2026 -- 04-PM.html">
          📰 16 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "16-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/16-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/16-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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