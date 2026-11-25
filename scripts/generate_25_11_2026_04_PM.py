#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Adobe Firefly Video 2 Arabic · Shopify Sidekick AI 3 Arabic · "
    "Zoom AI Companion 3 Arabic · Replit Agent 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Adobe Firefly Video 2 Arabic، Shopify Sidekick AI 3 Arabic، Zoom AI Companion 3 Arabic، Replit Agent 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Adobe Firefly Video 2 Arabic الذي يُحوّل فكرة مسائية واحدة إلى مشهد فيديو عربي مكتمل مع نصوص وحركة قبل غروب الشمس، إلى Shopify Sidekick AI 3 Arabic الذي يُجيب على أسئلة متجرك ويُقترح حملات ويُعدّل أوصاف المنتجات بالفصحى أثناء ما تتناول القهوة، ومن Zoom AI Companion 3 Arabic الذي يُلخّص الاجتماع ويُكتب متابعات عربية ويُعيد جدولة اللقاءات دون أن تفتح الملاحظات، إلى Replit Agent 2 Arabic الذي يبني تطبيقًا ويب من وصف عربي ويُنشره على رابط حي خلال ساعات — أربع قصص مسائية في 25 نوفمبر 2026 لصنّاع المحتوى والتجار والمستشارين الذين يريدون أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساء الإبداع والتجارة والاجتماعات والبرمجة: الفيديو يُنتَج، المتجر يُدار، الاجتماع يُختصر، والتطبيق يُبنى. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 25 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Adobe Firefly Video 2 Arabic: فيديو احترافي من وصف عربي — إعلانات، سوشيال، وقصص علامة!</h2>
      <p class="article-lead">«العميل يريد إعلان 15 ثانية بالعربية قبل نهاية اليوم — والمونتير مشغول ولا يوجد لقطات جاهزة». في 25 نوفمبر 2026، أطلقت <strong>Adobe</strong> <strong>Adobe Firefly Video 2 Arabic</strong>: طبقة فيديو داخل Creative Cloud تُولّد مشاهد من وصف نصي بالفصحى، تُضيف عناوين عربية متحركة، تُحافظ على ألوان العلامة عبر Brand Kit، تُدمج صورًا ومقاطع المستخدم مع مولّدات الذكاء الاصطناعي، تُصدّر قوالب 9:16 و16:9 و1:1 لإنستغرام وتيك توك ويوتيوب، وتتكامل Premiere Pro وAfter Effects لمراجعة بشرية — للوكالات الإبداعية والمؤثرين وفرق التسويق في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُحرف الحروف العربية في الشاشة أو يُولّد نصوصًا معكوسة؛ Firefly Video 2 يدعم RTL في الطبقات النصية، قاموس نطق للأسماء التجارية، وضع «إعلان منتج» و«قصة موظف» و«ترويج حدث»، ضوابط حقوق المحتوى التجاري، مكتبة مؤثرات صوتية خالية من الرسوم، تدريب على سيناريوهات MENA دون نمط كاريكاتوري عام، وبرنامج شركاء «Firefly Video Studio MENA».</p>
      <p>القدرات الأساسية: Arabic prompt-to-video؛ توليد B-roll ذكي؛ ترجمة تلقائية للمشاهد الإنجليزية إلى عناوين عربية؛ علامة مائية للمسودات؛ تصدير ProRes وH.264؛ لوحة موافقات للفرق.</p>
      <p>للمبدعين العرب: استوديو «فيديو سريع بالذكاء الاصطناعي» — من يُسلّم 20 عميلًا شهريًا بـ350–2200 دولار/فيديو أو باقة 1200–5800 دولار/شهر يحوّل الإنتاج من أيام إلى ساعات دون فريق تصوير دائم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Adobe Firefly Video 2 Arabic؟</h3>
        <ul>
          <li><strong>إعلانات وريلز من موجز عربي:</strong> 1–4 أيام — 350–2200 دولار/مقطع حسب التعقيد.</li>
          <li><strong>باقة شهرية لعلامة أو مطعم:</strong> — 1200–5800 دولار/شهر.</li>
          <li><strong>دليل أسلوب فيديو + Brand Kit للفريق:</strong> 2–6 أيام — 500–2800 دولار.</li>
          <li><strong>ورش «فيديو تسويقي بالذكاء الاصطناعي»:</strong> — 55–210 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Adobe</span>
        <span class="tag">Firefly</span>
        <span class="tag">Video</span>
        <span class="tag">Creative</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick AI 3 Arabic: مساعد متجر ذكي — مخزون، حملات، ودردشة عميل!</h2>
      <p class="article-lead">«لماذا تراجعت مبيعات العطور هذا الأسبوع؟ وما العنوان العربي الأفضل لمنتج جديد؟ وأين السلات المتروكة؟» — سؤال واحد في لوحة Shopify وستحصل على إجابة بالفصحى مع اقتراح تنفيذي. في 25 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick AI 3 Arabic</strong>: مساعد داخل لوحة التحكم يُحلّل المبيعات والزيارات والمخزون، يُكتب أوصاف منتجات محسّنة للبحث العربي، يُولّد رسائل استعادة سلة ورسائل ولاء، يُقترح خصومات مُحدودة بقواعد ربح، يُجيب على أسئلة التجار بلهجة مهنية واضحة، يتكامل Meta وGoogle وSnap للحملات، ويُحترم سياسات الدفع المحلية — للمتاجر في السعودية والإمارات ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان يُعطي نصائح عامة بالإنجليزية أو يُخطئ في تواريخ التخفيضات الإسلامية؛ الإصدار 3 يُفعّل وضع RTL في التقارير، تفسيرات «لماذا انخفض التحويل»، قوالب واتساب Business لاستعادة السلة، اقتراحات شحن وCOD لأسواق الخليج، مسار موافقة قبل نشر أي خصم كبير، تكامل مع Shopify Flow لتنفيذ تلقائي، وشهادة «Shopify Sidekick Partner Gulf».</p>
      <p>القدرات الأساسية: Arabic natural language analytics؛ توليد SEO عربي؛ حملات متعددة القنوات؛ تنبيهات مخزون ذكية؛ ملخص أسبوعي صوتي بالعربية (اختياري).</p>
      <p>للمبدعين العرب: خدمة «مدير متجر ذكي بالاشتراك». من يُدير 15 متجرًا بـ400–1800 دولار/شهر + إعداد أولي 800–4500 دولار يبيع خبرة تشغيل دون توظيف محلل بيانات بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick AI 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Sidekick وسياسات الخصم والرسائل:</strong> 5–12 يومًا — 800–4500 دولار/متجر.</li>
          <li><strong>تشغيل وتحسين أسبوعي (حملات + أوصاف):</strong> — 400–1800 دولار/شهر.</li>
          <li><strong>حزم قطاعية (عطور، أزياء، إلكترونيات):</strong> — 90–340 دولار/حزمة.</li>
          <li><strong>تدريب أصحاب المتاجر على الأوامر الصوتية العربية:</strong> — 50–195 دولار/جلسة.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Retail</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Zoom AI Companion 3 Arabic: اجتماعات أذكى — تلخيص، مهام، ومتابعة بالفصحى!</h2>
      <p class="article-lead">«اجتماع ساعة ونصف بالعربية والإنجليزية — والعميل ينتظر ملخصًا وخطوات تالية قبل المساء». في 25 نوفمبر 2026، أطلقت <strong>Zoom</strong> <strong>AI Companion 3 Arabic</strong>: مساعد اجتماع يُفرّق المتحدثين، يُلخّص النقاط والقرارات بالفصحى، يُستخرج مهامًا بأسماء المسؤولين والمواعيد، يُكتب رسائل متابعة للعملاء، يُقترح مواعيد لقاء قادم مع احترام المناطق الزمنية العربية، يُترجم أجزاء من الحوار للفريق الدولي، ويتكامل Zoom Team Chat وGoogle Calendar وOutlook — لشركات الاستشارات والعقارات والتعليم والتقنية في MENA.</p>
      <p>المشكلة التي حلّتها: Companion 2 كان يُهمل اللهجات أو يخلط بين المشاركين؛ الإصدار 3 يدعم ملخصات ثنائية اللغة، قوالب «عرض سعر بعد الاجتماع» و«محضر مجلس» و«تدريب موظف»، حذف تلقائي للمعلومات الحساسة قبل المشاركة، امتثال تسجيل حسب إعدادات الشركة، وضع «اجتماع مبيعات» يُبرز الاعتراضات والردود، وبرنامج «Zoom AI Partner MENA» للمستشارين.</p>
      <p>القدرات الأساسية: Arabic meeting intelligence؛ مهام تلقائية في Asana وMonday؛ اقتراح رد على بريد مرتبط بالاجتماع؛ تحليل مزاج عام (بدون أحكام شخصية)؛ تصدير PDF وWord بالعربية.</p>
      <p>للمبدعين العرب: باقة «اجتماعات منظمة للفرق الصغيرة». من يبيع 10 شركات بـ1500–7500 دولار إعداد + 300–1200 دولار/شهر للقوالب والتدريب يحوّل Zoom من مكالمة إلى نظام متابعة مبيعات ومشاريع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoom AI Companion 3 Arabic؟</h3>
        <ul>
          <li><strong>نشر قوالب اجتماعات وامتثال تسجيل:</strong> 4–14 يومًا — 1500–7500 دولار/مؤسسة.</li>
          <li><strong>صيانة قوالب ملخص ومتابعة شهرية:</strong> — 300–1200 دولار/شهر.</li>
          <li><strong>تدريب مديري المبيعات على مراجعة الملخصات:</strong> — 65–260 دولار/مقعد.</li>
          <li><strong>تكامل Zoom مع CRM عربي (مخصص):</strong> — 900–4200 دولار/مشروع.</li>
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

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Replit Agent 2 Arabic: من فكرة عربية إلى تطبيق منشور — ويب، API، ولوحة إدارة!</h2>
      <p class="article-lead">«أريد منصة حجز مواعيد عربية مع دفع وتذكير واتساب — وليس لدي فريق برمجة كامل». في 25 نوفمبر 2026، أطلقت <strong>Replit</strong> <strong>Agent 2 Arabic</strong>: وكيل تطوير داخل Replit يقرأ مواصفة بالفصحى أو باللهجة المهنية، يختار المكدس (React، Next.js، Flask)، يُنشئ قاعدة بيانات وتسجيل دخول، يبني لوحة إدارة RTL، يُصلّح الأخطاء تلقائيًا، يُشغّل اختبارات، يُنشر على Replit Hosting أو يُصدّر إلى GitHub، ويُوثّق API للعميل — لروّاد الأعمال والوكالات الرقمية وطلاب ريادة الأعمال في العالم العربي.</p>
      <p>المشكلة التي حلّتها: Agent 1 كان يتوقف عند واجهات عربية معقدة أو يُهمل الأمان؛ الإصدار 2 يُولّد ثيمات RTL جاهزة، يُفعّل rate limiting وتحقق من المدخلات، يدعم قوالب «سوق مصغّر» و«نظام حجز» و«بوابة دورات»، تكامل Stripe وTap وHyperPay عبر إرشادات إعداد، مراجعة كود قبل الإنتاج، وبرنامج «Replit Agent Partner Builders MENA».</p>
      <p>القدرات الأساسية: Arabic spec-to-app؛ نشر سحابي فوري؛ تعديلات محادثة مستمرة؛ فصل بيئات dev/prod؛ مشاركة رابط تجريبي للعميل خلال دقائق.</p>
      <p>للمبدعين العرب: عرض «MVP عربي في 72–120 ساعة». من ينفّذ 5 مشاريع شهريًا بـ2500–14000 دولار للمشروع يُقلّص تكلفة البداية على الشركات الناشئة ويبيع السرعة كميزة تنافسية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Agent 2 Arabic؟</h3>
        <ul>
          <li><strong>بناء MVP من مواصفة عربية مكتوبة:</strong> 3–10 أيام — 2500–14000 دولار/مشروع.</li>
          <li><strong>اشتراك صيانة وتطوير ميزات:</strong> — 450–2200 دولار/شهر.</li>
          <li><strong>قوالب جاهزة (حجز، متجر رقمي، عضويات):</strong> — 120–550 دولار/قالب مع تخصيص.</li>
          <li><strong>معسكر «ابنِ أول تطبيقك بالذكاء الاصطناعي»:</strong> — 48–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Agent</span>
        <span class="tag">Coding</span>
        <span class="tag">MVP</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="25-11-2026 -- 04-PM.html">
          📰 25 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/25-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/25-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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