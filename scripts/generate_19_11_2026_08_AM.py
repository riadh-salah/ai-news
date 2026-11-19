#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 19-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "19-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 3 Arabic · Canva Magic Studio 4 Arabic · "
    "Zapier AI Actions 2 Arabic · Shopify Sidekick 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 3 Arabic، Canva Magic Studio 4 Arabic، Zapier AI Actions 2 Arabic، Shopify Sidekick 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 19 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 3 Arabic الذي يُبني وكلاء مؤسسية يتحدثون مع عملائك بالفصحى ولهجات الخليج داخل Teams وواتساب، إلى Canva Magic Studio 4 Arabic الذي يُحوّل فكرة إعلان واحدة إلى حملة مرئية كاملة بلهجتك، ومن Zapier AI Actions 2 Arabic الذي يُترجم طلبك الصوتي إلى تدفق عمل يربط مئات الأدوات دون سطر كود، إلى Shopify Sidekick 3 Arabic الذي يُدير مخزونك ويُكتب أوصاف منتجات تجذب الشراء قبل أن تفتح متجرك — أربع قصص صباحية في 19 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضاف إلى فنجان القهوة الأول!</h1>
      <p class="hero-sub">صباحُ أصحاب المتاجر والوكالات وفرق التحول الرقمي: الوكلاء يخدمون العملاء، التصميم يُسرّع المبيعات، الأتمتة تفهم العربية، والمتجر يفكر معك. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 19 نوفمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 3 Arabic: وكلاء مؤسسية — دعم، مبيعات، وموارد بشرية بالعربية</h2>
      <p class="article-lead">«نريد مساعدًا واحدًا يُجيب موظفينا عن السياسات الداخلية ويُساعد العملاء على تتبع الطلبات دون أن نبني فريق تطوير كاملًا». في 19 نوفمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 3 Arabic</strong>: منصة لبناء وكلاء ذكاء يفهمون الفصحى ولهجات عربية رئيسية، يتصلون بـSharePoint وDynamics 365 وAzure، يُجيبون في Teams وواتساب وواجهات الويب، يحترمون صلاحيات Active Directory، يُسجّلون كل محادثة للامتثال، ويُتيحون نشرًا متعدد القنوات من استوديو واحد — للبنوك والاتصالات والتجزئة في الشرق الأوسط وشمال أفريقيا.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يتعثر في المصطلحات القانونية أو يخلط بين لهجات في جملة واحدة؛ Copilot Studio 3 يدعم قوالب «بنك» و«اتصالات» و«تعليم»، تدريبًا على مستندات PDF العربية، حوارات متعددة الخطوات مع تأكيد قبل تنفيذ إجراء حساس، تكامل Power Automate، اختبارات محاكاة قبل الإطلاق، مركز تحكم لمراقبة الدقة، وبرنامج شركاء «Copilot MENA Builders».</p>
      <p>القدرات الأساسية: وكلاء عربية متعددة القنوات؛ ربط أنظمة مؤسسية؛ حوكمة وأمان؛ قوالب قطاعات؛ نشر Teams وواتساب.</p>
      <p>للمبدعين العرب: استشارة «وكيل مؤسسي في 30 يومًا» — من يُصمّم 5 وكلاء لعملاء كبار بـ6500–32000 دولار للمشروع يخدم مؤسسات تُنفق ملايين على مراكز اتصال وتريد خفض التكلفة مع رفع جودة الرد بالعربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء ونشر وكلاء Copilot مؤسسيين:</strong> 14–35 يومًا — 6500–32000 دولار.</li>
          <li><strong>صيانة معرفة وتحسين محادثات شهريًا:</strong> — 780–3400 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب قطاع (مالية، صحة، تجزئة):</strong> — 72–295 دولار/حزمة.</li>
          <li><strong>ورش «وكلاء Copilot بالعربية دون برمجة ثقيلة»:</strong> — 58–225 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot Studio</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva Magic Studio 4 Arabic: حملات مرئية من جملة واحدة — علامة تجارية وإعلانات بلهجتك</h2>
      <p class="article-lead">«نحتاج عشرة تصاميم لرمضان بلهجة خليجية قبل اجتماع العلامة بعد ساعة». في 19 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 4 Arabic</strong>: مجموعة أدوات إبداعية تجمع Magic Design وMagic Write وMagic Resize مع فهم عميق للعربية RTL، تُولّد سلاسل إنستغرام وإعلانات سناب وترويجات واتساب من وصف نصي، تحافظ على ألوان الخط وشعارك، تُقترح نصوصًا إقناعية بالفصحى أو اللهجة المختارة، وتُصدر مقاسات جميع المنصات دفعة واحدة — لعلامات التجزئة والمطاعم والعيادات والمؤثرين في العالم العربي.</p>
      <p>المشكلة التي حلّتها: Magic السابق كان يُشوّه الحروف المتصلة أو يُهمل اتجاه النص في القوالب المختلطة؛ الإصدار 4 يدعم خطوط عربية احترافية، توليد فيديو قصير 9:16 مع ترجمة نص متحرك، Brand Kit ذكيًا يتذكر شعارك ونبرتك، قوالب «عروض نهاية الأسبوع» و«افتتاح فرع» و«دورة أونلاين»، حقوق استخدام تجاري واضحة، تكامل Meta Ads وGoogle Ads للتصدير المباشر، وبرنامج «Canva Creators Arabia Pro».</p>
      <p>القدرات الأساسية: توليد حملات RTL كاملة؛ حفظ هوية بصرية؛ نصوص إعلانية عربية؛ فيديو قصير؛ تصدير منصات إعلانية.</p>
      <p>للمبدعين العرب: وكالة «حملة أسبوعية بالذكاء» — من يُسلّم 12 عميلًا باقة 8 تصاميم + نصوص بـ450–2200 دولار/شهر يحل مشكلة الفرق الصغيرة التي لا تستطيع توظيف مصمم بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة حملات شهرية (تصميم + نصوص + مقاسات):</strong> — 450–2200 دولار/عميل/شهر.</li>
          <li><strong>إعداد Brand Kit وقوالب Magic مؤسسية:</strong> 4–10 أيام — 1200–5800 دولار.</li>
          <li><strong>حزم موسمية (رمضان، العيد، التخفيضات):</strong> — 85–380 دولار/حزمة.</li>
          <li><strong>دورة «إعلانات عربية سريعة بـCanva Magic»:</strong> — 45–185 دولار/مقعد.</li>
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

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Zapier AI Actions 2 Arabic: أتمتة تفهم كلامك — من الفكرة إلى تدفق عمل في دقائق</h2>
      <p class="article-lead">«عندما يصل نموذج اتصال بالعربية أرسله إلى Slack وافتح مهمة في Asana وأرسل رسالة شكر باللهجة نفسها». في 19 نوفمبر 2026، أطلقت <strong>Zapier</strong> <strong>AI Actions 2 Arabic</strong>: طبقة ذكاء فوق أكثر من 7000 تطبيق تفهم الأوامر بالفصحى واللهجات الشائعة، تُبني Zaps متعددة الخطوات من وصف طبيعي، تُصلح الأخطاء وتُقترح بدائل عند انقطاع API، تُوثّق كل تدفق بالعربية للفريق، وتُفعّل مراقبة أمان قبل ربط حسابات حساسة — لشركات الناشئة والوكالات والمكاتب التي تعمل بأدوات سحابية متفرقة.</p>
      <p>المشكلة التي حلّتها: AI Actions الأول كان يُفسّر العربية حرفيًا ويفشل مع الاختصارات المحلية؛ الإصدار 2 يدعم قوالب «وكالة تسويق» و«عيادة» و«متجر إلكتروني»، ربطًا مع OpenAI وClaude داخل التدفق، جدولة مهام رمضان وساعات العمل المحلية، تنبيهات عند فشل خطوة مع شرح بالعربية، مكتبة أفضل الممارسات للامتثال، تكامل Tables وInterfaces، وبرنامج «Zapier Solution Partners Gulf».</p>
      <p>القدرات الأساسية: أوامر عربية طبيعية؛ بناء تدفقات متعددة التطبيقات؛ توثيق عربي؛ مراقبة وأمان؛ قوالب قطاعات.</p>
      <p>للمبدعين العرب: خدمة «مكتب أتمتة ذكي» — من يُدير 10 عملاء بـ380–1650 دولار/شهر لكل عميل يحوّل الفوضى بين الأدوات إلى خط إنتاج هادئ دون توظيف مطور تكامل بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zapier AI Actions 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم وتفعيل حزمة أتمتة (8–20 Zap):</strong> 5–14 يومًا — 1800–9500 دولار.</li>
          <li><strong>إدارة وتحسين تدفقات شهريًا:</strong> — 380–1650 دولار/عميل/شهر.</li>
          <li><strong>قوالب قطاع جاهزة (CRM، فوترة، محتوى):</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>ورش «أتمتة الأعمال بالعربية دون كود»:</strong> — 42–175 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zapier</span>
        <span class="tag">Automation</span>
        <span class="tag">AI Actions</span>
        <span class="tag">No-Code</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Shopify Sidekick 3 Arabic: شريك متجرك الذكي — مخزون، أوصاف، وحملات تبيع بالعربية</h2>
      <p class="article-lead">«لديّ مئات المنتجات ولا أعرف أيها يُعلّم اليوم ولا بأي جملة أكتب الوصف لجذب عميل سعودي». في 19 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: مساعد داخل لوحة التحكم يقرأ مبيعاتك ومخزونك ومراجعاتك، يُقترح إعادة طلبًا ذكيًا، يُكتب أوصاف منتجات SEO بالفصحى أو اللهجة المستهدفة، يُولّد إيميلات استرداد سلة متروكة، يُحلّل إعلانات Meta السابقة ويقترح نصوصًا جديدة، يُعدّ تقارير أسبوعية بالعربية للمؤسس، ويتكامل مع Shopify Payments المحلي — لتجار التجزئة والماركات الناشئة في المنطقة.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان يُنتج نصوصًا عامة لا تلائم ثقافة الشراء المحلية؛ الإصدار 3 يدعم فهم مواسم رمضان والعيد والعودة للمدارس، اقتراحات تسعير ديناميكي مع تحذيرات هامش ربح، قوالب «أزياء» و«عطور» و«إلكترونيات»، دعمًا للدفع عند الاستلام في النصوص الترويجية، ربطًا مع تطبيقات الشحن العربية، لوحة «فرص نمو» بلغة بسيطة، وبرنامج «Shopify Partners MENA Plus».</p>
      <p>القدرات الأساسية: أوصاف وSEO عربي؛ تنبؤ مخزون؛ استرداد سلات؛ نصوص إعلانات؛ تقارير تنفيذية عربية.</p>
      <p>للمبدعين العرب: باقة «متجر يفكر» — من يُدير 8 متاجر بـ520–2400 دولار/شهر يجمع بين Sidekick ومراجعة بشرية خفيفة لرفع معدل التحويل دون توظيف فريق تسويق كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Sidekick وتحسين كتالوج عربي:</strong> 7–18 يومًا — 2200–11500 دولار.</li>
          <li><strong>إدارة نصوص وحملات ومخزون شهريًا:</strong> — 520–2400 دولار/متجر/شهر.</li>
          <li><strong>حزم أوصاف موسمية (50 منتج):</strong> — 350–1400 دولار/حزمة.</li>
          <li><strong>ورش «متجر Shopify يبيع بالعربية مع الذكاء»:</strong> — 50–195 دولار/مقعد.</li>
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

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 19-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="19-11-2026 -- 08-AM.html">
          📰 19 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "19-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/19-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/19-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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