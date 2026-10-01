#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 01-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "01-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Vercel v0 3 Arabic، Replit Agent 3 Arabic، Linear AI Projects 2 Arabic، Amplitude AI Analyst 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 1 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Vercel v0 3 Arabic الذي يُحوّل وصف المنتج بالعربية إلى واجهة React جاهزة للنشر قبل أن تبرد الشاي، إلى Replit Agent 3 Arabic الذي يُبني تطبيقًا كاملًا من فكرة في sandbox آمن، ومن Linear AI Projects 2 Arabic الذي يُ priority issues ويُ draft specs للفريق، إلى Amplitude AI Analyst 3 Arabic الذي يُ explain لماذا انخفض retention ويُ suggest experiments — أربع قصص مسائية في 1 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ للم builders: startups تريد v0 يفهم RTL وdesign tokens، مطورون solo يبحثون عن Replit Agent يُ ship MVP، product teams تطلب Linear يُ translate chaos إلى roadmap، وgrowth leads يريدون Amplitude يُ narrate البيانات بالعربية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 1 أكتوبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Vercel v0 3 Arabic: من prompt عربي إلى UI production — components، RTL، وdeploy بضغطة!</h2>
      <p class="article-lead">«الـ mockup متأخر — والـ sprint يبدأ غدًا». في 1 أكتوبر 2026، أطلقت <strong>Vercel</strong> <strong>v0 3 Arabic</strong>: generative UI داخل منصة Vercel يُ parse مواصفات المنتج بالعربية والإنجليزية المختلطة، يُ generate shadcn وTailwind components مع RTL mirroring، يُ sync design tokens من Figma، يُ preview على edge ويُ push إلى Git — لل startups وagencies وproduct squads في MENA.</p>
      <p>المشكلة التي حلّتها: v0 2 كان يُ misalign Arabic typography وspacing؛ الإصدار 3 يُ Cairo وNoto stacks، يُ accessibility checks WCAG RTL، يُ benchmark 4× أسرع من sketch إلى deployable PR في fintech onboarding team سعودي، يُ guardrails على secrets وAPI keys في generated code.</p>
      <p>القدرات الأساسية: Multi-page flows من conversation واحدة؛ integration مع Next.js App Router؛ AI-assisted refactors؛ preview sharing لل stakeholders؛ templates ل e-commerce وSaaS dashboards.</p>
      <p>للمبدعين العرب: frontend studios وVercel partners — «v0 3 Arabic sprint in 4 days» لل teams 3–40 مطور. من يُ deliver 8 builds/ربع بـ 2200–48000 دولار + maintenance retainer 260–2400 دولار/شهر يركب «Arabic generative frontend bureau».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Vercel v0 3 Arabic؟</h3>
        <ul>
          <li><strong>v0 rollout (tokens، RTL library، prompts، CI wiring):</strong> 3–10 أيام — 2200–48000 دولار/عميل.</li>
          <li><strong>Monthly UI velocity coaching and prompt libraries:</strong> — 260–2400 دولار/شهر.</li>
          <li><strong>Vertical starter kits (fintech، health، edtech):</strong> — 36–175 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Frontend with Vercel v0»:</strong> — 40–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Vercel</span>
        <span class="tag">v0</span>
        <span class="tag">Frontend</span>
        <span class="tag">Generative UI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Replit Agent 3 Arabic: مطوّر وكيلي في المتصفح — من فكرة إلى app live!</h2>
      <p class="article-lead">«لا وقت لإعداد بيئة — والفكرة تستحق اختبارًا سريعًا». في 1 أكتوبر 2026، أطلقت <strong>Replit</strong> <strong>Agent 3 Arabic</strong>: autonomous coding agent داخل Replit يُ understand Arabic product briefs، يُ scaffold full-stack apps (React، Node، Postgres)، يُ run tests وfix bugs iteratively، يُ deploy على Replit Cloud أو export إلى GitHub — لل founders وstudents وhackathon teams في MENA.</p>
      <p>المشكلة التي حلّتها: Agent 2 كان يتعثر على Arabic comments في requirements؛ الإصدار 3 يُ bilingual spec parsing، يُ security sandbox وdependency scanning، يُ benchmark MVP في 6–18 ساعة ل marketplace prototype إماراتي مقابل أسابيع يدويًا، يُ human review checkpoints.</p>
      <p>القدرات الأساسية: Database schema generation؛ API integration stubs (Stripe، Twilio)؛ mobile-responsive layouts RTL؛ collaboration rooms؛ usage-based billing transparency.</p>
      <p>للمبدعين العرب: no-code agencies وReplit educators — «Agent 3 Arabic MVP factory in 72 hours» لل clients 1–20K MRR ambition. من يُ sell 6 MVPs/ربع بـ 3500–65000 دولار + support 300–2700 دولار/شهر يركب «Arabic rapid app studio».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Agent 3 Arabic؟</h3>
        <ul>
          <li><strong>MVP builds (spec، agent supervision، deploy، handoff):</strong> 2–7 أيام — 3500–65000 دولار/مشروع.</li>
          <li><strong>Monthly iteration and feature sprints:</strong> — 300–2700 دولار/شهر.</li>
          <li><strong>Industry MVP templates (booking، marketplace، LMS):</strong> — 45–220 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Prototyping with Replit Agent»:</strong> — 43–208 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Agent</span>
        <span class="tag">MVP</span>
        <span class="tag">Full-stack</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Linear AI Projects 2 Arabic: product ops بلسان عربي — triage، specs، وstatus للمدير!</h2>
      <p class="article-lead">«Slack مليء — ولا أحد يعرف priority الحقيقي». في 1 أكتوبر 2026، أطلقت <strong>Linear</strong> <strong>AI Projects 2 Arabic</strong>: intelligence layer فوق Linear issues يُ summarize sprint health RTL، يُ auto-triage bugs من customer feedback Arabic، يُ draft PRDs وacceptance criteria، يُ sync GitHub وFigma links، يُ prepare standup digests — لل product-led startups وscale-ups في MENA.</p>
      <p>المشكلة التي حلّتها: Projects 1 كان English-centric على Arabic support tickets؛ الإصدار 2 يُ dialect-aware classification، يُ cycle time predictions، يُ benchmark −38% time-to-triage في gaming studio مصري، يُ privacy controls على customer PII في issue bodies.</p>
      <p>القدرات الأساسية: Roadmap scenario planning؛ integration مع Intercom وZendesk؛ custom views بالعربية؛ AI-suggested labels وestimates؛ executive weekly PDF summaries.</p>
      <p>للمبدعين العرب: product ops consultants — «Linear AI Projects 2 Arabic setup in 6 days» لل teams 15–200 engineers. من يُ deliver 5 rollouts/ربع بـ 2800–52000 دولار + ops retainer 275–2550 دولار/شهر يركب «Arabic product intelligence practice».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Linear AI Projects 2 Arabic؟</h3>
        <ul>
          <li><strong>Linear AI enablement (workflows، Arabic triage rules، training):</strong> 4–14 يومًا — 2800–52000 دولار/عميل.</li>
          <li><strong>Monthly sprint analytics and spec quality reviews:</strong> — 275–2550 دولار/شهر.</li>
          <li><strong>Team playbooks (mobile، platform، growth):</strong> — 38–185 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Product Ops with Linear AI»:</strong> — 41–200 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Linear</span>
        <span class="tag">Product</span>
        <span class="tag">PM</span>
        <span class="tag">Workflows</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Amplitude AI Analyst 3 Arabic: growth copilot — retention، funnels، وexperiments مفسّرة!</h2>
      <p class="article-lead">«الـ dashboard يقول انخفاض — لكن لماذا؟». في 1 أكتوبر 2026، أطلقت <strong>Amplitude</strong> <strong>AI Analyst 3 Arabic</strong>: analytics copilot يُ answer NL questions «لماذا تراجع activation في السعودية؟»، يُ root-cause cohort drops، يُ propose A/B tests مع sample size، يُ narrate board-ready insights RTL، يُ connect warehouse وCDP events — لل super-apps وe-commerce وsubscription products في MENA.</p>
      <p>المشكلة التي حلّتها: Analyst 2 كان يُ hallucinate على sparse Arabic event properties؛ الإصدار 3 يُ schema-aware grounding، يُ benchmark 2.5× faster insight cycles في food delivery platform خليجي، يُ role-based masking على revenue metrics، يُ export slides بالعربية.</p>
      <p>القدرات الأساسية: Predictive churn scores مع explanations؛ integration مع Experiment وSession Replay؛ anomaly alerts Slack بالعربية؛ templates ل onboarding وmonetization reviews.</p>
      <p>للمبدعين العرب: growth agencies وAmplitude partners — «AI Analyst 3 Arabic insights program in 10 days» لل products 100K–10M MAU. من يُ sell 4 programs/ربع بـ 3200–68000 دولار + analytics retainer 290–2800 دولار/شهر يركب «Arabic growth intelligence desk».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Amplitude AI Analyst 3 Arabic؟</h3>
        <ul>
          <li><strong>Analyst rollout (taxonomy، Arabic NL tuning، exec workshops):</strong> 7–21 يومًا — 3200–68000 دولار/عميل.</li>
          <li><strong>Monthly experiment design and narrative reporting:</strong> — 290–2800 دولار/شهر.</li>
          <li><strong>Vertical analytics kits (marketplace، SaaS، media):</strong> — 42–205 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Growth Analytics with Amplitude AI»:</strong> — 44–212 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Amplitude</span>
        <span class="tag">Analytics</span>
        <span class="tag">Growth</span>
        <span class="tag">Product</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 01-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="01-10-2026 -- 04-PM.html">
          📰 1 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Vercel v0 3 Arabic · Replit Agent 3 Arabic · Linear AI Projects 2 Arabic · Amplitude AI Analyst 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/01-10-2026 -- 04-PM.html`](news/01-10-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "01-10-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "01-10-2026 -- 04-PM.html" not in content:
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
        "أktobar",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "رobots",
        "despierta",
        "yú ",
        "yú",
        "tربح",
        " yُ ",
        "yü ",
        "yü",
        "تü",
        "أktober",
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
