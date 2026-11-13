#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 13-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "13-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google Gemini Enterprise 3 Arabic · Anthropic Claude for Work 5 Arabic · "
    "Canva Magic Studio 4 Arabic · Shopify Sidekick 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Gemini Enterprise 3 Arabic، Anthropic Claude for Work 5 Arabic، Canva Magic Studio 4 Arabic، Shopify Sidekick 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 13 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Google Gemini Enterprise 3 Arabic الذي يُحوّل مكتبة عقود بالعربية إلى إجابة مدققة بمصادر قبل أن ينتهي اجتماع المشتريات، إلى Anthropic Claude for Work 5 Arabic الذي يُراجع مسودة سياسة امتثال ويُقترح بنودًا ناقصة بلهجة مهنية، ومن Canva Magic Studio 4 Arabic الذي يُبني حملة إطلاق منتج RTL من برومبت واحد، إلى Shopify Sidekick 3 Arabic الذي يُحلّل مبيعات المتجر ويُوصي بتخفيض سعر ورسالة واتساب للعملاء في الخليج — أربع قصص ليلية في 13 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ لفرق التسويق والتجارة والامتثال: المحتوى يتأخر، السياسات تتراكم، والمبيعات تُفلت بين القنوات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 13 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Gemini Enterprise 3 Arabic: معرفة مؤسسية تُجيب بالعربية — grounding، workspaces، وامتثال!</h2>
      <p class="article-lead">«لدينا ثلاثة آلاف ملف PDF بالعربية — ولا أحد يثق في إجابة البحث الداخلي». في 13 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>Gemini Enterprise 3 Arabic</strong>: منصة RAG مؤسسية تفهم الفصحى واللهجات الخليجية والمصرية، تُفهرس Drive وGCS وSharePoint عبر connectors، تُجيب مع اقتباسات صفحة وسطر، تُ enforce VPC-SC وCMEK، تُ deploy في Dammam وDublin وSingapore — للبنوك والطاقة والتعليم في MENA.</p>
      <p>المشكلة التي حلّتها: Enterprise 2 كان يخلط المصادر؛ الإصدار 3 يُ rank مستندات عربية بـ multilingual embeddings، يُ detect تضارب بين نسختين من سياسة، يُ suggest تحديث Confluence تلقائيًا، يُ integrate Workspace side panel في Docs وGmail، يُ audit كل prompt إلى BigQuery، يُ eval «Arabic citation F1»، ويُ ship packs للعقود والموارد البشرية والشحن.</p>
      <p>القدرات الأساسية: Arabic Enterprise Search؛ agents مخصصة لكل قسم؛ Gemini Code Assist hooks؛ ميزانيات tokens لكل workspace؛ A/B بين models؛ شهادة شريك «MENA Gemini Grounding».</p>
      <p>للمبدعين العرب: Google Cloud partners وboutique data shops — «Arabic enterprise brain live in 10 days» للمؤسسات 500+ مقعد. من يُسلّم 5 rollouts Enterprise 3/ربع بـ 4200–52000 دولار + ضبط شهري 840–6200 دولار/شهر يبني خط إنتاج معرفة عربية على GCP.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Gemini Enterprise 3 Arabic؟</h3>
        <ul>
          <li><strong>Enterprise 3 rollout (فهرسة عربية، workspaces، policies، go-live):</strong> 8–22 يومًا — 4200–52000 دولار/عميل.</li>
          <li><strong>ضبط grounding وتقييم إجابات شهريًا:</strong> — 840–6200 دولار/شهر.</li>
          <li><strong>حزم قطاعات (نفط وغاز، تأمين، جامعات):</strong> — 68–295 دولار/حزمة.</li>
          <li><strong>دورات «بحث مؤسسي عربي مع Gemini»:</strong> — 55–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Gemini</span>
        <span class="tag">Enterprise</span>
        <span class="tag">RAG</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Anthropic Claude for Work 5 Arabic: مساعد امتثال يُفكر ببطء — artifacts، projects، وguardrails!</h2>
      <p class="article-lead">«محامي الامتثال يريد مسودة سياسة مكافحة الرشوة بالعربية — والموعد غدًا». في 13 نوفمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude for Work 5 Arabic</strong>: طبقة مؤسسية فوق Claude تُ parse لوائح وعقود عربية، تُ draft artifacts RTL قابلة للتصدير، تُ run extended thinking على تضارب بنود، تُ sync projects عبر فرق قانون ومالية، تُ enforce PII redaction وSOC2 logging — للمجموعات في الخليج وأوروبا التي تُكتب بالعربية والإنجليزية معًا.</p>
      <p>المشكلة التي حلّتها: Work 4 كان بلا ذاكرة مشروع قوية؛ الإصدار 5 يُ memory عبر quarters، يُ cite مصادر رفعها الفريق فقط، يُ integrate Slack وTeams وGoogle Drive، يُ suggest checklist امتثال قبل النشر، يُ respect data residency EU/US، SLA لفرق 200+ مقعد، وpacks للبنوك والصحة والطيران.</p>
      <p>القدرات الأساسية: Arabic Artifacts Editor؛ مقارنة نسخ سياسة؛ تعليقات داخلية على مسودات؛ API batch للمراجعة الليلية؛ برنامج شركاء للخليج.</p>
      <p>للمبدعين العرب: legal tech studios وGRC consultancies — «Arabic compliance workspace in 7 days» لمنظمات regulated. من يُبيع 6 deployments Work 5/ربع بـ 3100–38000 دولار + retainer 620–4500 دولار/شهر يحوّل Claude من chat إلى خط إنتاج امتثال.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude for Work 5 Arabic؟</h3>
        <ul>
          <li><strong>Work 5 adoption (projects عربية، guardrails، تدريب legal/HR):</strong> 5–16 يومًا — 3100–38000 دولار/عميل.</li>
          <li><strong>مراجعة مسودات وسياسات شهريًا:</strong> — 620–4500 دولار/شهر.</li>
          <li><strong>حزم (AML، خصوصية، مشتريات):</strong> — 60–255 دولار/حزمة.</li>
          <li><strong>دورات «امتثال ذكي بالعربية مع Claude»:</strong> — 50–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Compliance</span>
        <span class="tag">Legal</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Canva Magic Studio 4 Arabic: من فكرة حملة إلى فيديو وبوستات RTL — Brand Kit، AI video، وteams!</h2>
      <p class="article-lead">«المسوق طلب 40 أصلًا لإطلاق تطبيق توصيل — والمصمم في إجازة». في 13 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 4 Arabic</strong>: suite إبداعية تُ generate نصوص إعلان بالفصحى واللهجة المختارة، تُ layout قوالب RTL تلقائيًا، تُ produce مقاطع قصيرة من storyboard عربي، تُ respect Brand Kit وألوان الخط، تُ schedule للانستقرام وتيك توك ولينكدإن — لوكالات ومتاجر MENA.</p>
      <p>المشكلة التي حلّتها: Studio 3 كان فيديو محدود الجودة؛ الإصدار 4 يُ upscale footage، يُ voiceover عربي طبيعي، يُ translate EN↔AR مع حفظ نبرة العلامة، يُ collaborate live مع تعليقات RTL، يُ analytics أداء كل أصل، يُ integrate Meta Ads وGoogle Ads export، وتسعير teams للوكالات 15+ مقعد.</p>
      <p>القدرات الأساسية: Arabic Magic Write Pro؛ Resize للمنصات الخليجية؛ مكتبة خطوط عربية مرخصة؛ approvals للعميل النهائي؛ شهادة «Canva Agency AI» للشرق الأوسط.</p>
      <p>للمبدعين العرب: social agencies وfreelance collectives — «Arabic campaign pack in 48 hours» للعلامات الناشئة. من يُشغّل 12 retainers Studio 4/ربع بـ 900–4200 دولار/شهر لكل عميل + ورش 240–1800 دولار يحوّل Magic Studio إلى مصنع محتوى عربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>Studio 4 retainer (استراتيجية، قوالب، فيديو، جدولة):</strong> — 900–4200 دولار/شهر/عميل.</li>
          <li><strong>حملات إطلاق (40–120 أصلًا RTL):</strong> 3–10 أيام — 1800–15000 دولار/حملة.</li>
          <li><strong>حزم قوالب قطاعية (عقارات، مأكولات، تجميل):</strong> — 45–188 دولار/حزمة.</li>
          <li><strong>دورات «تسويق بصري عربي مع Canva AI»:</strong> — 38–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Marketing</span>
        <span class="tag">Design</span>
        <span class="tag">Video</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Shopify Sidekick 3 Arabic: مدير متجر يتحدث العربية — inventory، pricing، وWhatsApp growth!</h2>
      <p class="article-lead">«صاحب المتجر يسأل: لماذا انخفضت مبيعات العطور هذا الأسبوع؟ — ولوحة Shopify مليئة بالأرقام». في 13 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: مساعد تجاري داخل Admin يُ analyze طلبات ومخزون بالعربية، يُ suggest خصم على SKU راكد، يُ draft رسائل استرداد عملاء VIP، يُ plan bundle للمواسم الخليجية، يُ connect WhatsApp Business وemail — لتجار D2C في السعودية والإمارات ومصر.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان insights فقط؛ الإصدار 3 يُ act (update price، create discount code، tag customer)، يُ forecast موسم رمضان والعودة للمدارس، يُ respect multi-currency وتسوية ضريبة، يُ integrate TikTok Shop وAmazon MCF، يُ guard من تغييرات خطرة بموافقة، dashboard «دولار زِدناه هذا الأسبوع»، وpacks عطور وأزياء وإلكترونيات.</p>
      <p>القدرات الأساسية: Arabic Sidekick Chat؛ playbooks نمو؛ A/B على عروض؛ تدريب صوتي في تطبيق Shopify Mobile؛ شركاء Plus في المنطقة.</p>
      <p>للمبدعين العرب: Shopify experts وgrowth freelancers — «Arabic commerce copilot in 5 days» لمتاجر GMV 50k–2M دولار. من يُ onboard 15 متجر Sidekick 3/ربع بـ 1200–9500 دولار/كل + optimization 350–1400 دولار/شهر يبيع نموًا مدعومًا بالذكاء الاصطناعي لا بالتخمين.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>Sidekick 3 setup (تحليل، playbooks عربية، قنوات، تدريب):</strong> 4–14 يومًا — 1200–9500 دولار/متجر.</li>
          <li><strong>تحسين تسعير ومخزون شهريًا:</strong> — 350–1400 دولار/شهر.</li>
          <li><strong>حزم موسمية (رمضان، عيد، Back to School):</strong> — 55–210 دولار/حزمة.</li>
          <li><strong>دورات «تجارة إلكترونية ذكية بالعربية مع Shopify»:</strong> — 42–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Retail</span>
        <span class="tag">Growth</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 13-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="13-11-2026 -- 12-AM.html">
          📰 13 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "13-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/13-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/13-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
