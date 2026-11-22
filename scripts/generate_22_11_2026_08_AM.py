#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 22-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "22-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "HubSpot Breeze AI 2 Arabic · Shopify Sidekick 3 Arabic · "
    "Intercom Fin 3 Arabic · Atlassian Rovo 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HubSpot Breeze AI 2 Arabic، Shopify Sidekick 3 Arabic، Intercom Fin 3 Arabic، Atlassian Rovo 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 22 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من HubSpot Breeze AI 2 Arabic الذي يكتب لك رسائل مبيعات بالفصحى ويُسجّل كل تفاعل في الـCRM قبل أن تنقر «إرسال»، إلى Shopify Sidekick 3 Arabic الذي يُصمّم متجرك ويُعدّ حملة إعلانية وتلميحات استهداف قبل أن يُطلع شريكك على السلة، ومن Intercom Fin 3 Arabic الذي يُجيب عملاءك بالعربية ويُحوّل المحادثة الصعبة إلى تذكرة مدفوعة لخبير بك، إلى Atlassian Rovo 2 Arabic الذي يبحث في Jira وConfluence وSlack بسؤال عربي واحد ويُلخّص أسبوع الفريق — أربع قصص صباحية في 22 نوفمبر 2026 لروّاد التجارة الإلكترونية والمبيعات والدعم والتقنية الذين يريدون دخلًا يبدأ مع أول ضوء!</h1>
      <p class="hero-sub">صباح التحوّل الرقمي في المنطقة: قمع المبيعات يتحدث عربيًا، المتاجر تُبنى بالذكاء، الدعم يُدرّ الأموال بينما تنام، ومشاريع التقنية تُدار بلا بحث عشوائي. أربع أخبار عالمية وصندوق ذهبي لكل منها — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 22 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HubSpot Breeze AI 2 Arabic: مساعد مبيعات وتسويق بالعربية — محتوى، قمع، وتنبؤات في لوحة واحدة</h2>
      <p class="article-lead">«عندنا ألف عميل محتمل والفريق يكتب نفس رسالة البريد بثلاث لهجات مختلفة — والمدير يريد تقريرًا بالعربية قبل اجتماع التسعيرة». في 22 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze AI 2 Arabic</strong>: طبقة ذكاء داخل منصة HubSpot تفهم أوامرك بالفصحى، تُولّد رسائل بريد وصفحات هبوط ومنشورات اجتماعية RTL، تُخصّص النبرة لكل قطاع، تُقترح خطوات تالية لكل صفقة، تُلخّص مكالمات وتُسجّلها في سجل الاتصال، تتنبأ باحتمال الإغلاق بناءً على سلوك عربي محلي، وتتكامل مع WhatsApp Business وGoogle Ads — للوكالات وفرق نمو التجارة في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Breeze الأول كان يُنتج جملًا ركيكة أو يخلط التذكير بين الألفاظ الرسمية والدعائية؛ الإصدار 2 يدعم قوالب «عقار» و«تجميل» و«تقنية مالية» و«تعليم»، يحترم علامتك التجارية، يُنشئ تقارير أسبوعية للإدارة بالفصحى، تكاملًا مع Salesforce للفرق المختلطة، امتثالًا لتفضيلات الخصوصية في المنطقة، وبرنامج «HubSpot Solutions Partners MENA AI» للمستشارين المعتمدين.</p>
      <p>القدرات الأساسية: أوامر عربية؛ محتوى تسويقي RTL؛ تنبؤ صفقات؛ ملخصات مكالمات؛ تكامل قنوات محلية.</p>
      <p>للمبدعين العرب: استوديو «نمو مدعوم بالذكاء» — من يُطبّق Breeze على قمع 3–5 مراحل بـ2100–11800 دولار للإطلاق + 450–2200 دولار/شهر للتحسين يخدم شركات تبيع B2B وB2C وتريد فريق تسويق صغيرًا بقوة كبيرة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze AI 2 Arabic؟</h3>
        <ul>
          <li><strong>بناء قمع مبيعات ذكي (قوالب، أتمتة، تدريب):</strong> 8–18 يومًا — 2100–11800 دولار.</li>
          <li><strong>تحسين محتوى وتنبؤ صفقات شهريًا:</strong> — 450–2200 دولار/عميل/شهر.</li>
          <li><strong>حزمة 20 قالب بريد وصفحة هبوط عربية:</strong> — 180–720 دولار.</li>
          <li><strong>ورش «مبيعات ذكية بالعربية مع HubSpot Breeze»:</strong> — 55–220 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">CRM</span>
        <span class="tag">Marketing</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick 3 Arabic: شريك متجرك الذكي — وصفات منتجات، حملات، وتحليل سلة بالعربية</h2>
      <p class="article-lead">«متجري جديد، الصور ضعيفة، والوصف بالإنجليزية — والزوار من السعودية يريدون شراء الآن». في 22 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: مساعد داخل لوحة تحكم Shopify يتحدث معك بالفصحى واللهجات الشائعة في التجارة الإلكترونية، يُعيد كتابة أوصاف منتجات بأسلوب يبيع، يُقترح صورًا وعناوين SEO عربية، يُعدّ حملات Meta وSnap وTikTok بميزانيات مقترحة، يُحلّل سلة التخلي ويقترح رسائل استعادة بالعربية، يقارنك بمتاجر مشابهة في المنطقة، ويتكامل مع بوابات الدفع المحلية — لروّاد التجارة والموردين الذين يبيعون عبر Shopify في MENA.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان يتجاهل العملات المحلية والمناسبات الإسلامية في الترويج؛ الإصدار 3 يدعم تقويمًا للعروض الموسمية، قواعد خصم ذكية، تكامل مع تطبيقات الشحن الإقليمية، وضع «متعدد المتاجر» للعلامات الإقليمية، حماية من وعود مضللة في النصوص التسويقية، وبرنامج «Shopify Partners AI Arabia».</p>
      <p>القدرات الأساسية: أوصاف وSEO عربي؛ حملات إعلانية؛ تحليل تخلي سلة؛ مقارنة سوقية؛ متاجر متعددة.</p>
      <p>للمبدعين العرب: خدمة «متجر جاهز في 14 يومًا» — من يُسلّم Sidekick مُهيّأ + 50 منتج مُوصوفًا عربيًا بـ1500–6800 دولار يجذب التجار الذين يريدون بيعًا فوريًا دون توظيف فريق محتوى كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>إطلاق متجر ذكي (هيكلة، منتجات، حملات أولى):</strong> 7–14 يومًا — 1500–6800 دولار.</li>
          <li><strong>تشغيل وتحسين حملات ومحتوى شهريًا:</strong> — 320–1450 دولار/متجر/شهر.</li>
          <li><strong>حزمة 30 وصف منتج + 10 إعلانات جاهزة:</strong> — 95–380 دولار.</li>
          <li><strong>دورات «تجارة إلكترونية عربية مع Sidekick»:</strong> — 42–168 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Retail</span>
        <span class="tag">Ads</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Intercom Fin 3 Arabic: وكيل دعم يتحدث العربية — يحلّ، يُصعّد، ويُدرّ الإيرادات</h2>
      <p class="article-lead">«مائتا تذكرة يوميًا، نصفها أسئلة متكررة بالعربية، والفريق ينام بعد منتصف الليل وما زال العميل ينتظر». في 22 نوفمبر 2026، أطلقت <strong>Intercom</strong> <strong>Fin 3 Arabic</strong>: وكيل ذكاء اصطناعي داخل Intercom يفهم الفصحى واللهجات الشائعة في الدعم، يجيب من قاعدة معرفة عربية، يُنفّذ إجراءات مثل تغيير عنوان الشحن أو استرداد مبلغ بصلاحيات محددة، يُصعّد للإنسان مع ملخص كامل بالعربية، يقترح ترقيات مدفوعة في اللحظة المناسبة، يقيس رضا العملاء، ويتكامل مع Zendesk وHubSpot عند الحاجة — لشركات SaaS والتجارة والخدمات الرقمية التي تخدم جمهورًا عربيًا واسعًا.</p>
      <p>المشكلة التي حلّتها: Fin 2 كان يُكرر الإجابات أو يُغلق المحادثة مبكرًا؛ الإصدار 3 يحسّن فهم السياق متعدد الرسائل، يدعم وضع «تعليمي» لتدريب الموظفين الجدد، تحليلًا لأسباب التصعيد، قوالب قطاعية للبنوك والتأمين والسفر، امتثالًا لسجلات المحادثات، وبرنامج «Intercom AI Partners Gulf».</p>
      <p>القدرات الأساسية: دعم عربي حي؛ إجراءات آلية؛ تصعيد ذكي؛ اقتراح بيع؛ تحليل رضا.</p>
      <p>للمبدعين العرب: مكتب «دعم يدفع ثمنه» — من يُبني قاعدة معرفة + Fin لشركة بـ2400–13500 دولار للإعداد + 520–2400 دولار/شهر للصيانة يُقلّل تكلفة مقعد الدعم ويُحوّل المحادثة إلى فرصة بيع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 3 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Fin كامل (معرفة، سياسات، تكاملات):</strong> 10–22 يومًا — 2400–13500 دولار.</li>
          <li><strong>صيانة وتحسين دقة الإجابات شهريًا:</strong> — 520–2400 دولار/شركة/شهر.</li>
          <li><strong>حزمة 100 سؤال وجواب عربي جاهز:</strong> — 140–560 دولار.</li>
          <li><strong>ورش «دعم عملاء عربي ذكي مع Intercom Fin»:</strong> — 48–192 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Support</span>
        <span class="tag">CX</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Atlassian Rovo 2 Arabic: بحث ذكي عبر Jira وConfluence — سؤال عربي واحد وإجابة من كل أدوات الفريق</h2>
      <p class="article-lead">«أين وثيقة المتطلبات التي كتبها أحمد قبل شهرين؟ بحثت في Slack وConfluence وJira — وضاعت الساعة». في 22 نوفمبر 2026، أطلقت <strong>Atlassian</strong> <strong>Rovo 2 Arabic</strong>: مساعد مؤسسي يفهم أسئلتك بالعربية، يبحث عبر Jira وConfluence وTrello وSlack والمرفقات، يُلخّص المستندات الطويلة بفقرات واضحة، يُقترح مهامًا ومستندات مرتبطة، يُجيب «من المسؤول عن…؟» و«ما حالة…؟» من بيانات حية، يُولّد مسودات specs بالفصحى التقنية السليمة، يحترم صلاحيات كل مستخدم، ويدعم فرق موزعة بين دبي والقاهرة ومراكش — لشركات البرمجيات والخدمات المالية والهندسة التي تعمل بمنهجيات أجايل.</p>
      <p>المشكلة التي حلّتها: Rovo الأول كان يُرجع نتائج إنجليزية رغم سؤال عربي؛ الإصدار 2 يُفهرس محتوى RTL، يدعم استعلامات بأسماء عربية، قوالب «مراجعة ربع سنوية» و«تسليم sprint» و«امتثال»، تكاملًا مع Microsoft 365، سجل تدقيق للاستعلامات الحساسة، وبرنامج «Atlassian Partners MENA Rovo».</p>
      <p>القدرات الأساسية: بحث مؤسسي عربي؛ تلخيص مستندات؛ اقتراح مهام؛ مسودات تقنية؛ امتثال صلاحيات.</p>
      <p>للمبدعين العرب: استشارة «معرفة الشركة في يد الفريق» — من يُنظّم Confluence ويُفعّل Rovo لـ200 مستخدم بـ3200–16800 دولار للمشروع + 580–2600 دولار/شهر للحوكمة يبيع لجهات تفقد ملايين الدقائق في البحث اليدوي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlassian Rovo 2 Arabic؟</h3>
        <ul>
          <li><strong>تنظيف معرفة وتفعيل Rovo (فهرسة، سياسات، تدريب):</strong> 12–28 يومًا — 3200–16800 دولار.</li>
          <li><strong>حوكمة وتحسين استعلامات شهريًا:</strong> — 580–2600 دولار/مؤسسة/شهر.</li>
          <li><strong>قوالب Confluence جاهزة (12 مجلدًا قطاعيًا):</strong> — 220–880 دولار.</li>
          <li><strong>ورش «إنتاجية فرق عربية مع Atlassian Rovo»:</strong> — 50–200 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atlassian</span>
        <span class="tag">Rovo</span>
        <span class="tag">Jira</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 22-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="22-11-2026 -- 08-AM.html">
          📰 22 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "22-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/22-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/22-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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