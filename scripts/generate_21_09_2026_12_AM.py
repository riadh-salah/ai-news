#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "21-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Teams Copilot Facilitator 3، Linear Product Intelligence 2، Supabase AI Edge Functions 2، Gumloop Workflow Marketplace 2، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Teams Copilot Facilitator 3 الذي يُدير اجتماعك بالعربية ويُغلق action items قبل أن تغادر الغرفة، إلى Linear Product Intelligence 2 الذي يُحوّل feedback العملاء إلى roadmap جاهز، ومن Supabase AI Edge Functions 2 الذي يُ launch backends ذكية في ثوانٍ، إلى Gumloop Workflow Marketplace 2 الذي يُ sell automations جاهزة كمنتجات — أربع قصص ليلية في 21 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يعمل حتى وأنت نائم!</h1>
      <p class="hero-sub">منتصف الليل للبنّائين: فرق MENA تريد meetings بلا فوضى، product managers يريدون قرارات مبنية على بيانات، المطورون يريدون AI APIs بلا DevOps معقد، والمستقلون يريدون workflows تُ sold مرة واحدة وتُ repeat للأبد. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 21 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Teams Copilot Facilitator 3: مدير اجتماعات ذكي — agenda، تلخيص عربي، ومهام تُ assign تلقائيًا!</h2>
      <p class="article-lead">«الاجتماع انتهى — ولا أحد يتذكر من وعد بماذا». في 21 سبتمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Teams Copilot Facilitator 3</strong>: copilot يُ join كـ «facilitator» (بإذن)، يُ build agenda من Teams chat وOutlook threads، يُ keep timeboxes، يُ capture decisions بالعربية والإنجليزية، يُ create Planner tasks وLoop components، ويُ send recap emails بلهجة MENA — مع compliance للقطاعات المنظّمة.</p>
      <p>المشكلة التي حلّتها: meeting fatigue في الشركات العربية؛ Facilitator 3 يُ detect off-topic drift، يُ suggest parking lot items، يُ pull metrics من Power BI أثناء Q&amp;A، يُ integrate Viva Engage للتغذية الراجعة، ويُ offer «silent mode» للاجتماعات الحساسة مع on-prem retention options.</p>
      <p>القدرات الأساسية: bilingual live captions (خليجي/مصري/فصحى)؛ conflict de-escalation prompts للمدراء؛ recurring meeting memory؛ templates للboard meetings وsales reviews؛ admin dashboard لـ ROI على وقت الاجتماعات.</p>
      <p>للمبدعين العرب: Microsoft 365 partners وcorporate trainers — «Facilitator rollout + Arabic meeting culture playbooks» للشركات 100–5000 موظف. من يُ deploy 5 tenants/ربع بـ 8500–72000 دولار + retainer 1600–9800 دولار/شهر يبني practice productivity enterprise في المنطقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Teams Copilot Facilitator 3؟</h3>
        <ul>
          <li><strong>Facilitator pilot + governance (DLP + retention):</strong> 7–16 يومًا — 7800–62000 دولار/مؤسسة.</li>
          <li><strong>Managed meeting ops (agenda design + recap QA):</strong> — 1700–11000 دولار/شهر.</li>
          <li><strong>Arabic executive meeting template packs (board، HR، sales):</strong> — 69–349 دولار/حزمة.</li>
          <li><strong>دورات «Arabic High-Impact Meetings with Copilot Facilitator»:</strong> — 54–268 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Teams</span>
        <span class="tag">Copilot</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Productivity</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Linear Product Intelligence 2: من تذاكر الدعم إلى roadmap — AI يُ rank الأولويات ويُ write specs!</h2>
      <p class="article-lead">«لدينا 400 feature request — والفريق يختار بالحدس». في 21 سبتمبر 2026، أطلقت <strong>Linear</strong> <strong>Product Intelligence 2</strong>: طبقة AI فوق issues وcycles تُ cluster feedback من Intercom وSlack وGitHub، تُ score impact vs effort، تُ draft PRDs بالعربية للفرق ثنائية اللغة، تُ propose sprint plans، وتُ alert عند drift عن OKRs — مع explainability لكل قرار.</p>
      <p>المشكلة التي حلّتها: product chaos في startups MENA؛ Intelligence 2 يُ link customer quotes إلى tickets، يُ simulate release scenarios، يُ generate release notes multilingual، يُ sync مع Notion وFigma links، ويُ respect role-based visibility للinvestors vs engineers.</p>
      <p>القدرات الأساسية: «Insight Digest» أسبوعي بالعربية؛ competitor mention tracking؛ API للcustom scoring models؛ templates لـ fintech وhealthtech compliance؛ offline export للboards.</p>
      <p>للمبدعين العرب: product ops consultants وstartup advisors — «Intelligence setup week» للSeries A–B. من يُ sell 7 engagements/ربع بـ 3200–18000 دولار + 900–5200 دولار/شهر tuning يحوّل Linear إلى product command center مربح.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Linear Product Intelligence 2؟</h3>
        <ul>
          <li><strong>Product intelligence audit + Linear workspace design:</strong> 5–12 يومًا — 2800–16500 دولار/شركة.</li>
          <li><strong>Monthly roadmap facilitation + AI tuning:</strong> — 750–4800 دولار/شهر.</li>
          <li><strong>Vertical scoring packs (e-commerce، SaaS B2B، govtech):</strong> — 45–225 دولار/قالب.</li>
          <li><strong>دورات «Arabic Product Ops with Linear Intelligence»:</strong> — 48–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Linear</span>
        <span class="tag">Product</span>
        <span class="tag">Roadmap</span>
        <span class="tag">Startups</span>
        <span class="tag">SaaS</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Supabase AI Edge Functions 2: backends ذكية على الحافة — RAG، chatbots عربية، وbilling جاهز!</h2>
      <p class="article-lead">«العميل يريد chatbot على موقعه — والـ backend سيأخذ شهرين». في 21 سبتمبر 2026، أطلقت <strong>Supabase</strong> <strong>AI Edge Functions 2</strong>: deploy functions قرب المستخدم (including MENA PoPs)، مع embeddings مدمجة، pgvector sync، streaming LLM routes (OpenAI، Anthropic، Mistral)، Arabic tokenization helpers، rate limits، وStripe metered billing hooks — كلها من dashboard واحد.</p>
      <p>المشكلة التي حلّتها: fragmented AI infra؛ Edge Functions 2 يُ ship «RAG-in-a-box» من PDFs عربية، يُ offer auth + row-level security patterns، يُ log prompts للaudit، يُ cold-start under 200ms، ويُ template WhatsApp webhook bots للتجار.</p>
      <p>القدرات الأساسية: one-click fork من marketplace (support bot، lead qualifier، internal wiki)؛ secrets rotation؛ branch previews؛ observability dashboards؛ partner rev-share للagencies.</p>
      <p>للمبدعين العرب: full-stack freelancers وdev shops — «48-hour AI backend» للSMEs. من يُ deliver 12 projects/ربع بـ 2200–14000 دولار + 400–2800 دولار/شهر hosting margin يبني studio Supabase AI متخصص في MENA.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Supabase AI Edge Functions 2؟</h3>
        <ul>
          <li><strong>Edge AI backend packages (RAG + auth + dashboard):</strong> 4–10 أيام — 1900–13500 دولار/مشروع.</li>
          <li><strong>Managed AI ops (monitoring + model swaps):</strong> — 500–3400 دولار/شهر.</li>
          <li><strong>Arabic RAG starter kits (legal، real estate، clinics):</strong> — 59–299 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Backends on Supabase Edge»:</strong> — 62–310 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Supabase</span>
        <span class="tag">Edge</span>
        <span class="tag">Developers</span>
        <span class="tag">RAG</span>
        <span class="tag">Backend</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Gumloop Workflow Marketplace 2: اشترِ automation جاهزة — أو بِع workflowsك للعالم!</h2>
      <p class="article-lead">«أنا أبني نفس Zap للعملاء كل أسبوع — وأريد passive income». في 21 سبتمبر 2026، أطلقت <strong>Gumloop</strong> <strong>Workflow Marketplace 2</strong>: سوق لـ AI workflows (visual + code nodes) يُ support Arabic prompts، payments عبر Stripe وPayTabs، licensing (one-time vs subscription)، white-label delivery للconsultants، وreviews verified — مع sandbox testing قبل الشراء.</p>
      <p>المشكلة التي حلّتها: automation IP لا يُ monetized؛ Marketplace 2 يُ let creators package «lead gen for clinics» أو «invoice chase for agencies»، يُ handle updates وversioning، يُ split revenue 70/30، يُ offer enterprise bundles للHR وCS teams، ويُ integrate Slack وHubSpot وGoogle Sheets out of the box.</p>
      <p>القدرات الأساسية: MENA payment rails؛ Arabic UI for buyer onboarding؛ affiliate program؛ compliance badges؛ API لembed workflows في client portals؛ analytics على conversion per workflow.</p>
      <p>للمبدعين العرب: no-code sellers وautomation influencers — «workflow product line» بدل hourly only. من يُ publish 8 workflows بـ 49–499 دولار/each ويُ sell 200 licenses/ربع + 6 enterprise deals بـ 3500–22000 دولار يحوّل Gumloop إلى digital product business.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gumloop Workflow Marketplace 2؟</h3>
        <ul>
          <li><strong>Custom workflow products (niche MENA verticals):</strong> 3–8 أيام build — 800–6500 دولار setup + recurring licenses.</li>
          <li><strong>Marketplace optimization (listing + demos + support):</strong> — 600–3800 دولار/شهر retainer.</li>
          <li><strong>Enterprise workflow bundles (10–50 seats):</strong> — 2400–28000 دولار/صفقة.</li>
          <li><strong>دورات «Sell Arabic AI Workflows on Gumloop»:</strong> — 46–228 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gumloop</span>
        <span class="tag">Marketplace</span>
        <span class="tag">Automation</span>
        <span class="tag">Passive Income</span>
        <span class="tag">No-Code</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="21-09-2026 -- 12-AM.html">
          📰 21 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Microsoft Teams Copilot Facilitator 3 · Linear Product Intelligence 2 · Supabase AI Edge Functions 2 · Gumloop Workflow Marketplace 2</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "21-09-2026 -- 12-AM.html" not in content:
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
        "رobots",
        "سبtember",
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
