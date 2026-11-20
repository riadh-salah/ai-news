#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 20-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "20-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Klarna AI Shopping Assistant 2 Arabic · GrammarlyGo for Business 2 Arabic · "
    "Semrush AI Content Toolkit 3 Arabic · Toast IQ for Restaurants 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Klarna AI Shopping Assistant 2 Arabic، GrammarlyGo for Business 2 Arabic، Semrush AI Content Toolkit 3 Arabic، Toast IQ for Restaurants 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 20 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Klarna AI Shopping Assistant 2 Arabic الذي يُقترح سلة شراء ويقارن الأسعار ويُقسّط الدفع بلهجة عربية طبيعية قبل أن يغلق العميل التطبيق، إلى GrammarlyGo for Business 2 Arabic الذي يُصقل رسائل البيع والعقود والبريد الرسمي بصوت علامتك لا نبرة مترجمة، ومن Semrush AI Content Toolkit 3 Arabic الذي يُحوّل كلمة مفتاحية واحدة إلى خطة محتوى ومواقع مقالات ولوحة SEO بالعربية، إلى Toast IQ for Restaurants 2 Arabic الذي يُتنبأ بحركة المطبخ ويوصي بقائمة اليوم ويُقلّل الهدر — أربع قصص مسائية في 20 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ للتجار الرقميين وصنّاع المحتوى وفرق التسويق وأصحاب المطاعم: الشراء يُغلق نفسه، الكتابة تُحافظ على هويتك، SEO يُصبح خطة أسبوعية جاهزة، والمطبخ يقرأ الطلب قبل وصوله. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 20 نوفمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Klarna AI Shopping Assistant 2 Arabic: تسوق ذكي — مقارنة، تقسيط، وإغلاق صفقة بلهجة عميلك!</h2>
      <p class="article-lead">«العميل يسأل: أي سماعة أرخص مع توصيل غدًا وتقسيط أربع دفعات؟ — والبوت يرد بإنجليزية جامدة». في 20 نوفمبر 2026، أطلقت <strong>Klarna</strong> <strong>AI Shopping Assistant 2 Arabic</strong>: مساعد تسوق مضمّن في تطبيق Klarna ولوحات التجار يقرأ كتالوج المتجر، يُقارن المنتجات حسب السعر والتقييم والتوفر، يُقترح بدائل أصلية ومستعملة، يُحسب التقسيط والرسوم بالعملات المحلية، يُجيب بالفصحى واللهجات الخليجية والمصرية المدعومة، يُتتبع الطلب ويُرسل تحديثات واتساب، يتكامل Shopify وMagento وواجهات مخصصة — للتجارة الإلكترونية والعلامات التي تبيع في المنطقة عبر Klarna Pay.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُكرر وصف المنتج دون فهم السؤال؛ Assistant 2 يفهم الاستفسارات المركبة «أرخص مع ضمان سنتين»، يحترم سياسات الإرجاع لكل دولة، يُنبّه عند نفاد المخزون ويقترح بديلًا فورًا، يدعم الموافقة على الدفع بنقرة واحدة، يُحلّل سبب ترك السلة ويُعيد جذب العميل برسالة عربية مخصصة، ويُقدّم برنامج «Klarna Merchant AI MENA» للشركات التي تريد رفع معدل التحويل دون تكديس فرق دعم.</p>
      <p>القدرات الأساسية: مقارنة منتجات؛ تقسيط شفاف؛ لهجات عربية؛ تكامل متاجر؛ استرداد السلات المتروكة.</p>
      <p>للمبدعين العرب: وكالة «سلة ذكية» — من يُفعّل المساعد لعشرة متاجر إلكترونية خلال أسبوعين بـ1500–9200 دولار للمشروع يبيع تجربة شراء عربية تُنافس العلامات العالمية دون مركز اتصال ضخم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Klarna AI Shopping Assistant 2 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل مساعد تسوق كامل (كتالوج، لهجة، واتساب، اختبار A/B):</strong> 7–18 يومًا — 1500–9200 دولار/متجر.</li>
          <li><strong>تحسين معدل التحويل شهريًا:</strong> — 520–2400 دولار/عميل/شهر.</li>
          <li><strong>حزم رسائل استرداد سلة جاهزة (تقنية، أزياء، منزل):</strong> — 45–195 دولار/حزمة.</li>
          <li><strong>ورش «تجارة تقسيط ذكية بالعربية»:</strong> — 46–188 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Klarna</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Shopping</span>
        <span class="tag">BNPL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>GrammarlyGo for Business 2 Arabic: كتابة علامتك — عقود، عروض، وبريد بلا أخطاء وبلا لهجة غريبة!</h2>
      <p class="article-lead">«أرسلنا عرضًا بالعربية — والعميل شعر أنه مُترجم آليًا وفقدنا الصفقة». في 20 نوفمبر 2026، أطلقت <strong>Grammarly</strong> <strong>GrammarlyGo for Business 2 Arabic</strong>: منصة كتابة مؤسسية تتعلّم نبرة شركتك من مستنداتك السابقة، تُصحح النحو والإملاء في الفصحى، تُقترح صياغات احترافية للعقود والعروض والرسائل التنفيذية، تُوحّد أسلوب الفريق عبر القوالب، تتحقق من الالتزام بسياسات العلامة، تتكامل Microsoft 365 وGoogle Workspace وSlack، وتحترم عدم تدريب النماذج على بيانات العميل — للبنوك والقانون والتقنية والاستشارات في المنطقة.</p>
      <p>المشكلة التي حلّتها: GrammarlyGo 1 كان قويًا بالإنجليزية وضعيفًا في التشابك العربي؛ الإصدار 2 يفهم أسلوب «رسمي خليجي» و«ودود مصري» و«قانوني فصيح»، يكتشف التناقض بين الفقراء، يُحذّر من عبارات قد تُسيء ثقافيًا، يقترح بدائل للمصطلحات التقنية، يُولّد ملخصات تنفيذية من تقارير طويلة، يدعم الموافقات قبل الإرسال، وبرنامج «Grammarly Brand Voice Arabia» للمؤسسات متعددة الفروع.</p>
      <p>القدرات الأساسية: نبرة علامة عربية؛ تصحيح وتلخيص؛ قوالب مؤسسية؛ تكامل مكتبي؛ خصوصية بيانات.</p>
      <p>للمبدعين العرب: استوديو «صوتك الرسمي» — من يُعرّف نبرة عشر علامات خلال شهر ويُدرّب الفرق بـ2200–14500 دولار للعميل يبيع ثقة لغوية لشركات تتوسع إقليميًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GrammarlyGo for Business 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد نبرة علامة وقوالب (عقود، عروض، بريد):</strong> 5–14 يومًا — 2200–14500 دولار/مؤسسة.</li>
          <li><strong>مراجعة وتحسين محتوى شهري:</strong> — 680–3100 دولار/عميل/شهر.</li>
          <li><strong>حزم رسائل مبيعات واستجابة اعتراضات:</strong> — 55–230 دولار/حزمة.</li>
          <li><strong>دورة «كتابة مؤسسية عربية بالذكاء الاصطناعي»:</strong> — 44–175 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Grammarly</span>
        <span class="tag">Writing</span>
        <span class="tag">Brand Voice</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Semrush AI Content Toolkit 3 Arabic: من كلمة مفتاحية إلى إمبراطورية محتوى — SEO يتحدث العربية!</h2>
      <p class="article-lead">«المنافس يتصدر جوجل على «تأمين سيارات الرياض» — وفريقنا يكتب مقالات عشوائية». في 20 نوفمبر 2026، أطلقت <strong>Semrush</strong> <strong>AI Content Toolkit 3 Arabic</strong>: حزمة ذكاء فوق منصة Semrush تُحلل الكلمات المفتاحية العربية والإنجليزية معًا، تُبني خريطة موضوعات للربع القادم، تُولّد outlines مقالات RTL مع نية البحث، تُقترح عناوين ووصفًا meta، تراقب ترتيب المنافسين يوميًا، تُكتشف فجوات المحتوى، تربط Google Search Console وWordPress وWebflow، وتُصدّر تقارير عربية للعملاء — لوكالات التسويق والناشرين وفرق النمو في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Toolkit 2 كان يُولّد نصوصًا عامة بلا سياق محلي؛ الإصدار 3 يميّز بين البحث بالفصحى واللهجة، يقترح روابط داخلية من موقعك، يحسب صعوبة الكلمة حسب السوق المحدد، يُنبّه عند تحديث خوارزمية جوجل، يدعم قوالب «مقال مقارنة» و«دليل شراء» و«FAQ منظّم»، يحافظ على إرشادات E-E-A-T، وبرنامج «Semrush Partner MENA Content» للوكالات المعتمدة.</p>
      <p>القدرات الأساسية: بحث كلمات عربي؛ خطة محتوى؛ outlines ذكية؛ تتبع ترتيب؛ تقارير عملاء.</p>
      <p>للمبدعين العرب: مكتب «SEO محتوى» — من ينجز 20 مقالًا مُحسّنًا شهريًا لخمسة عملاء بـ900–4800 دولار/عميل/شهر يحوّل Toolkit إلى خط إنتاج دخل متكرر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Semrush AI Content Toolkit 3 Arabic؟</h3>
        <ul>
          <li><strong>خطة SEO ومحتوى ربع سنوية (بحث + 12 outline + تتبع):</strong> 6–12 يومًا — 1800–9800 دولار/عميل.</li>
          <li><strong>إنتاج ونشر مقالات محسّنة شهريًا:</strong> — 900–4800 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب مقالات قطاعية (عقار، تعليم، صحة):</strong> — 38–165 دولار/حزمة.</li>
          <li><strong>ورش «SEO عربي عملي مع Semrush AI»:</strong> — 42–182 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Semrush</span>
        <span class="tag">SEO</span>
        <span class="tag">Content</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Toast IQ for Restaurants 2 Arabic: مطبخ يتنبأ — طلبات، هدر، وأرباح قبل ذروة العشاء!</h2>
      <p class="article-lead">«الجمعة مساءً والمخزون ينفد والطهاة في حيرة — من أمر الضعف الإضافي؟». في 20 نوفمبر 2026، أطلقت <strong>Toast</strong> <strong>Toast IQ for Restaurants 2 Arabic</strong>: ذكاء مدمج في نظام نقاط البيع Toast للمطاعم والمقاهي يقرأ تاريخ المبيعات والأحداث المحلية والطقس، يتنبأ بحجم الطلبات ساعة بساعة، يُقترح قائمة اليوم وأصنافًا للترويج، يُحسب كميات المكونات لتقليل الهدر، يُرسل تنبيهات للمدير بالفصحى، يتكامل مع الموردين والجرد، ويدعم فروعًا متعددة في الإمارات والسعودية ومصر والأردن — لسلاسل الضيافة والمطابخ السحابية والكافيهات السريعة النمو.</p>
      <p>المشكلة التي حلّتها: Toast IQ 1 كان تنبؤات عامة؛ الإصدار 2 يتعلّم أنماط رمضان والعيد والمباريات، يميّز بين الطلب الداخلي والتوصيل، يُقترح تعديلات أسعار ديناميكية ضمن سياسة العلامة، يُلخّص أداء الفروع مقارنةً ببعضها، يكتشف احتيالًا أو خصومات غير مصرح بها، يدعم تقارير مجلس إدارة بالعربية، وبرنامج «Toast Partner MENA IQ» للمُكاملين المحليين.</p>
      <p>القدرات الأساسية: تنبؤ طلب؛ إدارة هدر؛ قوائم ذكية؛ تقارير فروع؛ تكامل مخزون.</p>
      <p>للمبدعين العرب: استشارة «مطبخ ربحي» — من يربط Toast IQ لثمانية مطاعم بـ1100–7800 دولار إعدادًا + 350–1600 دولار/شهر للمتابعة يبيع هامشًا أعلى لأصحاب منافذ لم يعودوا يخمنون الطلب.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Toast IQ for Restaurants 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Toast IQ وتدريب الطاقم (تنبؤ، جرد، تقارير):</strong> 4–10 أيام — 1100–7800 دولار/مطعم.</li>
          <li><strong>متابعة أداء وتحسين قائمة شهريًا:</strong> — 350–1600 دولار/فرع/شهر.</li>
          <li><strong>نماذج تقارير امتياز وامتثال صحي:</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>ورش «إدارة مطبخ ذكية بالعربية»:</strong> — 40–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Toast</span>
        <span class="tag">Restaurants</span>
        <span class="tag">Hospitality</span>
        <span class="tag">Forecasting</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 20-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="20-11-2026 -- 04-PM.html">
          📰 20 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "20-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/20-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/20-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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