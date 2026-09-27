#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Azure AI Foundry Agents 3 Arabic، GitHub Copilot Workspace 3 Arabic، ElevenLabs Conversational AI 3 Arabic، Stripe Revenue Autopilot 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI الصباحية</span>
      <h1>من Microsoft Azure AI Foundry Agents 3 Arabic الذي يُشغّل وكلاء مؤسسية على Azure OpenAI وPhi مع حوكمة عربية، إلى GitHub Copilot Workspace 3 Arabic الذي يُحوّل issue إلى pull request كامل بلغة طبيعية، ومن ElevenLabs Conversational AI 3 Arabic الذي يُجري مكالمات وWhatsApp voice بالخليجي والمصري، إلى Stripe Revenue Autopilot 3 Arabic الذي يُلاحق الفواتير ويُحسّن التسعير من داخل Dashboard — أربع قصص صباحية في 27 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يستيقظ مع القهوة!</h1>
      <p class="hero-sub">صباحٌ للمُؤسّسين والمُطوّرين: فرق platform تريد agents على Azure مع PDPL، engineering leads يريدون Copilot يُ finish الميزات، contact centers تبحث عن صوت عربي طبيعي، وSaaS founders يريدون Stripe يُ recover revenue تلقائيًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 27 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Azure AI Foundry Agents 3 Arabic: وكلاء مؤسسية — من prompt عربي إلى Azure OpenAI وPhi مع audit كامل!</h2>
      <p class="article-lead">«نريد agents تُ answer policy بالعربية — لكن compliance يمنع أي data leak». في 27 سبتمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Azure AI Foundry Agents 3 Arabic</strong>: منصة agentic فوق Azure AI Foundry تُ author flows بالعربية (MSA وخليجي ومصري)، تُ connect Azure OpenAI وPhi-4 وcustom models، تُ enforce Entra ID وPurview DLP وcontent safety Arabic classifiers، تُ deploy إلى Teams وweb وCopilot Studio مع shared memory — للbanks وtelco وgovernment في MENA.</p>
      <p>المشكلة التي حلّتها: Foundry Agents 2 كان English authoring؛ الإصدار 3 يُ Arabic-native prompt templates، يُ multi-agent graphs «Research Arabic + Action Arabic + Human approval»، يُ grounding على Azure AI Search مع Arabic analyzers، يُ sovereign region UAE/KSA، يُ observability «token cost per agent topic»، يُ marketplace packs للlegal وHR وprocurement.</p>
      <p>القدرات الأساسية: Agent Service SLA 99.95%؛ MCP وAzure Functions connectors؛ evaluation suite Arabic bias tests؛ BYOK encryption؛ migration wizard من LangChain prototypes.</p>
      <p>للمبدعين العرب: Azure SI partners وAI boutiques — «Foundry Agents 3 Arabic landing in 7 days» لل tenants 500–50000 users. من يُ deliver 6 rollouts/ربع بـ 3800–72000 دولار + managed ops 750–5800 دولار/شهر يركب موجة «sovereign agentic cloud» في الخليج.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Azure AI Foundry Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>Foundry Agents 3 deployment (Arabic flows، Search، Purview، UAT):</strong> 7–21 يومًا — 3600–75000 دولار/عميل.</li>
          <li><strong>Monthly agent governance and prompt regression:</strong> — 720–5900 دولار/شهر.</li>
          <li><strong>Vertical agent accelerators (banking، energy، retail):</strong> — 58–285 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Enterprise Agents on Azure Foundry»:</strong> — 46–228 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Azure AI Foundry</span>
        <span class="tag">Agents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>GitHub Copilot Workspace 3 Arabic: من issue عربي إلى branch وtests وPR — مهندس وكيلي بجانبك!</h2>
      <p class="article-lead">«الميزة واضحة في Jira — لكن sprint ممتلئ». في 27 سبتمبر 2026، أطلقت <strong>GitHub</strong> <strong>Copilot Workspace 3 Arabic</strong>: agentic dev environment يُ read issue/spec بالعربية أو English، يُ plan tasks، يُ edit multi-file repos، يُ run tests في Codespaces، يُ open PR مع description ثنائي اللغة — لل startups وoutsourcing shops في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot Workspace 2 كان plan-only؛ الإصدار 3 يُ execute (scaffold API، migrate DB، fix flaky tests)، يُ Arabic comments in code review، يُ respect org policies (secret scanning block)، يُ integrate Jira/Azure Boards Arabic fields، يُ workspace analytics «time saved per squad»، يُ enterprise air-gapped option preview.</p>
      <p>القدرات الأساسية: Multi-model routing GPT-5.2 وClaude؛ sandbox command allowlist؛ visual diff RTL-friendly؛ pair mode «human steers agent»؛ Copilot Metrics export for managers.</p>
      <p>للمبدعين العرب: dev agencies وfractional CTOs — «Copilot Workspace 3 Arabic sprint booster in 5 days» لل teams 8–120 engineers. من يُ sell 8 enablement packages/ربع بـ 2200–38000 دولار/each + retainer 420–3400 دولار/شهر ي monetize «ship faster with guardrails».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitHub Copilot Workspace 3 Arabic؟</h3>
        <ul>
          <li><strong>Workspace 3 rollout (policies، workflows، Arabic specs، training):</strong> 5–14 يومًا — 2100–42000 دولار/عميل.</li>
          <li><strong>Monthly agent-assisted sprint support:</strong> — 400–3200 دولار/شهر.</li>
          <li><strong>Stack starter kits (Next.js، .NET، mobile):</strong> — 35–175 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Agentic Development with Copilot Workspace»:</strong> — 40–185 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitHub</span>
        <span class="tag">Copilot Workspace</span>
        <span class="tag">Developers</span>
        <span class="tag">DevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ElevenLabs Conversational AI 3 Arabic: وكلاء صوت — مكالمات، WhatsApp voice، وIVR باللهجات!</h2>
      <p class="article-lead">«العميل يتصل — والرد الآلي بالإنجليزية يُزعج». في 27 سبتمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Conversational AI 3 Arabic</strong>: platform لوكلاء صوت وchat يُ speak Gulf وEgyptian وLevant وMSA، يُ integrate Twilio وGenesys وMeta WhatsApp calling، يُ low latency (&lt;800ms region edge Dubai)، يُ knowledge base Arabic OCR، يُ handoff للhuman مع sentiment score — للbanks وe-commerce وhealthcare في MENA.</p>
      <p>المشكلة التي حلّتها: Conversational AI 2 كان MSA-only voice؛ الإصدار 3 يُ dialect detection auto-switch، يُ act (book appointment، check order status، create ticket)، يُ PCI-aware payment phrases، يُ analytics «containment rate per dialect»، يُ partner program Cairo وRiyadh studios.</p>
      <p>القدرات الأساسية: Voice library 40 Arabic personas؛ real-time translation EN↔AR؛ batch call campaigns PDPL consent؛ SDK mobile in-app voice؛ red-team tested for social engineering.</p>
      <p>للمبدعين العرب: CX integrators وvoice studios — «Conversational AI 3 Arabic contact center in 6 days» لل queues 500–80000 calls/month. من يُ onboard 10 clients/ربع بـ 1800–42000 دولار/each + tuning 380–3100 دولار/شهر ي scale «Arabic voice that sells».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Conversational AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Conversational AI 3 setup (personas، KB، telephony، compliance):</strong> 5–16 يومًا — 1750–45000 دولار/مشروع.</li>
          <li><strong>Monthly voice tuning and script A/B:</strong> — 360–3050 دولار/شهر.</li>
          <li><strong>Industry playbooks (telecom، insurance، delivery):</strong> — 42–205 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Voice Agents with ElevenLabs»:</strong> — 38–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Contact Center</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Stripe Revenue Autopilot 3 Arabic: فواتير، dunning، وpricing experiments — من Dashboard واحد!</h2>
      <p class="article-lead">«MRR ينمو — لكن failed payments تسرق 8%». في 27 سبتمبر 2026، أطلقت <strong>Stripe</strong> <strong>Revenue Autopilot 3 Arabic</strong>: AI layer فوق Billing وInvoicing وRevenue Recognition يُ send Arabic dunning emails/SMS، يُ suggest retry windows per MENA card networks، يُ run pricing experiments with statistical guardrails، يُ forecast churn وexpansion ARR — للSaaS وmarketplaces وcreators في المنطقة.</p>
      <p>المشكلة التي حلّتها: Autopilot 2 كان English templates؛ الإصدار 3 يُ Arabic RTL invoices and customer portal، يُ act (apply coupon، pause subscription، upgrade tier) via approved playbooks، يُ integrate HubSpot/Salesforce Arabic fields، يُ tax hints GCC VAT، يُ CFO dashboard «recovered revenue in SAR/AED».</p>
      <p>القدرات الأساسية: Smart retries ML model MENA-calibrated؛ conversational billing support widget Arabic؛ usage-based pricing advisor؛ audit trail for finance teams؛ Stripe Sigma Arabic query snippets.</p>
      <p>للمبدعين العرب: SaaS consultants وfractional CFOs — «Revenue Autopilot 3 Arabic billing health in 4 days» لل companies 50K–20M ARR. من يُ deliver 12 optimizations/ربع بـ 1400–28000 دولار/each + monitoring 290–2400 دولار/شهر ي capture «recover cash without hiring» demand.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe Revenue Autopilot 3 Arabic؟</h3>
        <ul>
          <li><strong>Autopilot 3 activation (Arabic comms، retries، experiments، training):</strong> 4–11 يومًا — 1300–29500 دولار/عميل.</li>
          <li><strong>Monthly revenue ops and experiment review:</strong> — 280–2350 دولار/شهر.</li>
          <li><strong>Vertical billing kits (EdTech، B2B SaaS، creator):</strong> — 38–188 دولار/حزمة.</li>
          <li><strong>دورات «Arabic FinOps AI with Stripe Autopilot»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Billing</span>
        <span class="tag">SaaS</span>
        <span class="tag">FinOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="27-09-2026 -- 08-AM.html">
          📰 27 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Microsoft Azure AI Foundry Agents 3 Arabic · GitHub Copilot Workspace 3 Arabic · ElevenLabs Conversational AI 3 Arabic · Stripe Revenue Autopilot 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/27-09-2026 -- 08-AM.html`](news/27-09-2026%20--%2008-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-09-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    content = README.read_text(encoding="utf-8")
    import re

    new_content = re.sub(
        r"- \[`news/[^`]+`\]\([^)]+\) — أحدث إصدار \(4 أخبار \+ أفكار ربح من AI\)\n",
        README_LATEST,
        content,
        count=1,
    )
    if new_content == content and "27-09-2026 -- 08-AM.html" not in content:
        new_content = content.replace(
            "## المحتوى\n\n",
            "## المحتوى\n\n" + README_LATEST,
        )
    if new_content != content:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        print(f"Updated: {README}")
    else:
        print(f"README already up to date: {README}")


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
        "رobots",
        "despierta",
        "yú ",
        "yú",
        "yُ ",
        "yُ",
        "tربح",
        "القدrات",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"Mixed-script typo found: {pat}")
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
