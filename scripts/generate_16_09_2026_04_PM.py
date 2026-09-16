#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "16-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Perplexity Comet 2، Shopify Sidekick Pro 3، Runway Gen-4.5 Turbo API، Intercom Fin 3 للدعم باللهجات العربية، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 16 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Perplexity Comet 2 الذي يتصفح الإنترنت نيابةً عنك ويُلخّص المنافسين قبل أن تُنهي قهوتك، إلى Shopify Sidekick Pro 3 الذي يُحوّل متجرك إلى محلل مبيعات يتحدث العربية، ومن Runway Gen-4.5 Turbo API الذي يُنتج إعلانات فيديو سينمائية من جملة واحدة، إلى Intercom Fin 3 الذي يُجيب زبائنك بالخليجية والمصرية والشامية دون انتظار — أربع موجات مسائية في 16 سبتمبر 2026 لمن يريد دخلًا ذكيًا من الذكاء الاصطناعي!</h1>
      <p class="hero-sub">مساءٌ مليء بالفرص: الباحثون يريدون intelligence فوري، التجار يريدون قرارات inventory قبل نفاد المخزون، المبدعون يريدون فيديو يُ sold out حملاتهم، وفرق الدعم تريد SLA ممتازًا دون توظيف مئة agent. أربع قصص عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 16 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Perplexity Comet 2: متصفحك يصبح محققًا رقميًا — بحث، مقارنة أسعار، وتقارير منافسين بالعربية!</h2>
      <p class="article-lead">«تحتاج تقريرًا عن 15 منافسًا في السعودية — والموعد غدًا». في 16 سبتمبر 2026، أطلقت <strong>Perplexity</strong> <strong>Comet 2</strong>: agent متصفح enterprise يفتح تبويبات حقيقية، يُجمع البيانات من مواقع live، يُصدّر جداول مقارنة، ويُلخّص بالعربية مع citations لكل claim — دون أن تُ copy-paste بين ChatGPT وGoogle.</p>
      <p>المشكلة التي حلّتها: أدوات البحث القديمة تُعطي snippets؛ Comet 2 يُنفّذ multi-step workflows (pricing scrape، review sentiment، LinkedIn headcount)، يُ respect robots.txt enterprise mode، ويُ archive snapshots للامتثال — مثالي لوكالات competitive intelligence وconsultants في MENA.</p>
      <p>القدرات الأساسية: دعم RTL في التقارير المُصدّرة؛ جدولة مهام يومية «راقب أسعار X»؛ تكامل Slack وNotion؛ SSO وSOC2؛ حدود concurrent sessions للفرق؛ API لـ embed Comet في dashboards داخلية.</p>
      <p>للمبدعين العرب: محللو أسواق وB2B researchers — «Comet intelligence sprint» أسبوعي للشركات الناشئة قبل fundraising. من يُ package 10 competitor briefs عربية + dashboard Notion ويبيعها 2500–15000 دولار/ربع يبني retainer قبل consultancies الكبرى.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Comet 2؟</h3>
        <ul>
          <li><strong>Competitive intelligence packages:</strong> 5–12 منافس — 2200–18000 دولار/مشروع.</li>
          <li><strong>Managed market monitoring retainers:</strong> تقارير أسبوعية + Comet workflows — 1100–8500 دولار/شهر.</li>
          <li><strong>Vertical brief templates (e-commerce، fintech، health):</strong> — 89–499 دولار/حزمة.</li>
          <li><strong>دورات «Arabic OSINT with Comet 2»:</strong> bootcamp — 49–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Comet</span>
        <span class="tag">Browser Agent</span>
        <span class="tag">Research</span>
        <span class="tag">Enterprise</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick Pro 3: «لماذا انخفضت مبيعات الرياض؟» — AI يُجيب ويُقترح حملات وإعادة تسعير!</h2>
      <p class="article-lead">«المخزون ممتلئ — والحملة لا تُ sold». في 16 سبتمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick Pro 3</strong>: مساعد merchant يقرأ analytics كاملًا، يُ correlate weather وevents محلية، ويُ suggest: خصم 12% على SKU معين، email segment للعملاء الذين abandon cart، أو bundle جديد للعيد — بالعربية في لوحة التحكم.</p>
      <p>المشكلة التي حلّتها: SMBs تدفع consultants لقراءة dashboards؛ Sidekick Pro 3 يُ execute actions مباشرة (create discount، draft Meta ad، reorder from supplier) بعد موافقة one-click — مع audit log لكل تغيير.</p>
      <p>القدرات الأساسية: sync مع Salla وZid عبر partners؛ forecasts 30/60/90 يوم؛ A/B على subject lines عربية؛ compliance VAT خليجي؛ Plus merchants فقط في Pro tier مع rollout لـ Advanced قريبًا.</p>
      <p>للمبدعين العرب: وكالات e-commerce — «Sidekick ops» شهرية للمتاجر 50K–500K GMV. من يُ manage 12 متجرًا بـ 1200–7500 دولار/شهر each يصل لـ 100K MRR مع playbook موحّد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick Pro 3؟</h3>
        <ul>
          <li><strong>Sidekick onboarding + playbook setup:</strong> — 1800–12000 دولار/متجر.</li>
          <li><strong>Monthly growth retainers:</strong> campaigns + inventory AI — 900–6800 دولار/شهر.</li>
          <li><strong>Arabic prompt libraries for merchants:</strong> — 39–229 دولار/حزمة.</li>
          <li><strong>دورات «Scale MENA Stores with Sidekick Pro»:</strong> — 45–219 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">MENA</span>
        <span class="tag">Analytics</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Runway Gen-4.5 Turbo API: من نص عربي إلى spot إعلاني 4K — motion control وbrand kit في دقائق!</h2>
      <p class="article-lead">«العميل يريد فيديو Ramadan قبل 48 ساعة — والميزانية لا تسمح بـ studio». في 16 سبتمبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4.5 Turbo API</strong>: نموذج فيديو يُ generate clips 4–10 ثوانٍ، يُ extend scenes، يُ lock character consistency عبر brand kit، ويُ accept prompts بالعربية مع lip-sync اختياري للـ UGC style.</p>
      <p>المشكلة التي حلّتها: agencies كانت تنتظر queues طويلة؛ Turbo API يُ promise p95 latency under 90s per clip، batch endpoints لـ 20 variant، وwatermark removal للخطط enterprise — integration في After Effects وDaVinci plugins.</p>
      <p>القدرات الأساسية: camera motion presets (dolly، orbit، handheld)； safety filters للمحتوى الإعلاني regional； usage-based pricing per second generated； partner program 15% على first-year API spend للintegrators.</p>
      <p>للمبدعين العرب: motion designers وperformance marketers — «Arabic ad factory»: 30 creatives/شهر لbrand واحد. من يُ sell retainer 4000–22000 دولار/شهر + pass-through API cost يبني margin 40–55% على volume.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4.5 Turbo API؟</h3>
        <ul>
          <li><strong>Video ad sprint packages:</strong> 10–40 clips — 3500–28000 دولار/حملة.</li>
          <li><strong>API integration for agencies:</strong> pipeline + brand kits — 5000–35000 دولار/عميل.</li>
          <li><strong>Managed creative retainers:</strong> weekly drops + A/B variants — 2500–18000 دولار/شهر.</li>
          <li><strong>دورات «Arabic Performance Video with Runway API»:</strong> — 59–279 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4.5</span>
        <span class="tag">Video AI</span>
        <span class="tag">API</span>
        <span class="tag">Advertising</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Intercom Fin 3: بوت دعم يفهم «وين طلبي؟» و«الفاتورة غلط» — حل 78% من التذاكر قبل human!</h2>
      <p class="article-lead">«فريق الدعم غرق في WhatsApp وemail — والزبون ينتظر ساعتين». في 16 سبتمبر 2026، أطلقت <strong>Intercom</strong> <strong>Fin 3</strong>: agent support يُ train على help center + past tickets، يُ detect dialect (خليجي، مصري، شامي، مغاربي)، يُ execute refunds وorder lookup عبر Shopify/Zendesk APIs، ويُ escalate بملخص عربي للموظف.</p>
      <p>المشكلة التي حلّتها: chatbots generic تُ frustrate users؛ Fin 3 يُ score confidence per reply، يُ ask clarifying questions باللهجة، ويُ comply GDPR + local data residency options في EU/GCC hosting.</p>
      <p>القدرات الأساسية: voice note transcription عربي； proactive messages «طلبك تأخر — نُ offer خصم»； Fin Insights يُ highlight gaps في documentation； pricing per resolved conversation + human seat.</p>
      <p>للمبدعين العرب: SaaS وmarketplaces في المنطقة — «Fin 3 launch in 10 days» للشركات 500–5000 tickets/شهر. من يُ package knowledge base Arabic rewrite + Fin tuning + weekly optimization يفرض 6000–45000 دولار setup + 2000–12000 دولار/شهر retainer.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 3؟</h3>
        <ul>
          <li><strong>Fin 3 implementation packages:</strong> KB + integrations + dialect tuning — 5500–42000 دولار/عميل.</li>
          <li><strong>Support optimization retainers:</strong> analytics + new intents — 1800–11500 دولار/شهر.</li>
          <li><strong>Arabic macro &amp; playbook libraries:</strong> — 69–389 دولار/قطاع.</li>
          <li><strong>دورات «Arabic CX Automation with Fin 3»:</strong> — 52–239 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Fin 3</span>
        <span class="tag">Customer Support</span>
        <span class="tag">Arabic Dialects</span>
        <span class="tag">SaaS</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 16-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="16-09-2026 -- 04-PM.html">
          📰 16 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Perplexity Comet 2 · Shopify Sidekick Pro 3 · Runway Gen-4.5 Turbo · Intercom Fin 3</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "16-09-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def validate_output():
    data = OUTPUT.read_bytes()
    if b"\x00" in data:
        raise SystemExit("ERROR: null bytes found in output")
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
        "bringing",
        "الLlatin",
        "أفكar",
        "دolار",
        "البروtokol",
        "سبtemبر",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    print("Validation passed: UTF-8, no null bytes, 4 articles, valid HTML structure")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    validate_output()
    update_index()


if __name__ == "__main__":
    main()
