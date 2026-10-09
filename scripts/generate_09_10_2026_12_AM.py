#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 09-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "09-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Vercel v0 4 Arabic، Postman AI Agent Builder 3 Arabic، Cloudflare Workers AI Gateway 3 Arabic، Replit Agent 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 9 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Vercel v0 4 Arabic الذي يُحوّل wireframe إلى تطبيق React منشور قبل أن يبرد القهوة، إلى Postman AI Agent Builder 3 Arabic الذي يُبني ويُختبر APIs وكيليًا بلغة squad عربي، ومن Cloudflare Workers AI Gateway 3 Arabic الذي يُ govern مئات نماذج AI بسياسات وتكلفة واضحة، إلى Replit Agent 4 Arabic الذي يُ ship منتجًا كاملًا من فكرة Slack — أربع قصص ليلية في 9 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للمطورين ورواد المنتجات وفرق المنصات: واجهات تُعاد بناؤها يدويًا كل sprint، collections Postman تتعفّن دون tests، فواتير AI تتضاعف بلا رقابة، وMVPs تتأخر أسابيع. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 9 أكتوبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Vercel v0 4 Arabic: من sketch إلى production — واجهات RTL، components، وdeploy بضغطة!</h2>
      <p class="article-lead">«الـ landing مطلوبة غدًا — والـ frontend team مشغول». في 9 أكتوبر 2026، أطلقت <strong>Vercel</strong> <strong>v0 4 Arabic</strong>: مولّد واجهات وكيلي يُفهم briefs بالعربية والإنجليزية، يُ generate React/Next.js components بخطوط RTL صحيحة، يُ wire API stubs، يُ preview responsive، يُ sync design tokens من Figma، ويُ one-click deploy على Vercel مع analytics — لل startups وagencies في MENA.</p>
      <p>المشكلة التي حلّتها: v0 3 كان يُ mix اتجاه النص في forms معقدة؛ الإصدار 4 يُ Arabic numerals toggle، يُ benchmark −52% وقت من wireframe إلى live URL في fintech إماراتية، يُ accessibility checks WCAG، يُ image gen MENA-safe، ويُ human review diff قبل merge.</p>
      <p>القدرات الأساسية: Multi-page flows؛ shadcn/ui Arabic presets؛ integration Supabase auth؛ A/B variant generator؛ export إلى GitHub repo مع CI.</p>
      <p>للمبدعين العرب: indie hackers وdev shops — «v0 4 Arabic launch sprint in 3 days» لل products 1–8 screens. من يُ deliver 12 sprints/ربع بـ 1800–28000 دولار + retainer 120–920 دولار/شهر يبني «استوديو v0 عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Vercel v0 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة launch sprint (UI، deploy، analytics):</strong> 2–8 أيام — 1800–28000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل iterations والـ A/B:</strong> — 120–920 دولار/شهر.</li>
          <li><strong>حزم قطاعية (SaaS، marketplace، fintech):</strong> — 55–240 دولار/حزمة.</li>
          <li><strong>دورات «بناء واجهات أسرع بالعربية مع v0»:</strong> — 45–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Vercel</span>
        <span class="tag">v0</span>
        <span class="tag">Frontend</span>
        <span class="tag">Next.js</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Postman AI Agent Builder 3 Arabic: وكلاء APIs — specs، tests، mocks، وdocumentation RTL!</h2>
      <p class="article-lead">«الـ API تغيّر — والـ docs قديمة من شهر». في 9 أكتوبر 2026، أطلقت <strong>Postman</strong> <strong>AI Agent Builder 3 Arabic</strong>: منصة وكيلية داخل Postman تُ ingest OpenAPI وGraphQL schemas، تُ generate collections وtests وmocks، تُ explain endpoints بالفصحى، تُ detect breaking changes، تُ suggest versioning، وتُ publish developer portals RTL — لل banks وtelcos وSaaS في MENA.</p>
      <p>المشكلة التي حلّتها: Agent Builder 2 كان summaries إنجليزية فقط؛ الإصدار 3 يُ Arabic error messages في examples، يُ benchmark −41% وقت onboarding partner APIs في operator سعودي، يُ contract tests CI، يُ security scan OWASP، ويُ sync Jira tickets لل fixes.</p>
      <p>القدرات الأساسية: Natural language «build payment flow test»؛ synthetic data MENA (IBAN، mobile formats)؛ monitor uptime؛ integration GitHub Actions؛ rate-limit simulation.</p>
      <p>للمبدعين العرب: API consultants — «Postman Agent 3 Arabic platform kit in 7 days» لل orgs 5–200 services. من يُ roll out 8 kits/ربع بـ 2600–36000 دولار + governance 150–1100 دولار/شهر يبني «مكتب Postman AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Postman AI Agent Builder 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة platform kit (collections، tests، portal RTL):</strong> 5–14 يومًا — 2600–36000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل monitoring والـ compliance:</strong> — 150–1100 دولار/شهر.</li>
          <li><strong>Playbooks (open banking، marketplace، IoT):</strong> — 60–270 دولار/playbook.</li>
          <li><strong>دورات «APIs وكيلية بالعربية مع Postman»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Postman</span>
        <span class="tag">API</span>
        <span class="tag">DevTools</span>
        <span class="tag">Testing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Cloudflare Workers AI Gateway 3 Arabic: بوابة نماذج — routing، budgets، وpolicies بلغة CFO!</h2>
      <p class="article-lead">«كل team يستدعي model مختلف — والفاتورة مفاجأة». في 9 أكتوبر 2026، أطلقت <strong>Cloudflare</strong> <strong>Workers AI Gateway 3 Arabic</strong>: طبقة edge تُ unify OpenAI وAnthropic وGoogle وopen models، تُ route by latency/cost/quality، تُ enforce budgets per team، تُ cache prompts، تُ redact PII قبل upstream، تُ generate Arabic cost reports لل finance، وتُ block jailbreak patterns — لل enterprises وscale-ups في MENA.</p>
      <p>المشكلة التي حلّتها: Gateway 2 كان dashboards إنجليزية؛ الإصدار 3 يُ Arabic executive summaries، يُ benchmark −34% spend waste في edtech مصرية، يُ fallback chains، يُ observability traces، ويُ DPA-ready logs.</p>
      <p>القدرات الأساسية: Custom model aliases؛ A/B model routing؛ integration SSO؛ Workers binding one-liner؛ anomaly alerts Slack/Teams.</p>
      <p>للمبدعين العرب: platform engineers — «AI Gateway 3 Arabic finops stack in 6 days» لل orgs 10–500 developers. من يُ deploy 7 stacks/ربع بـ 2200–45000 دولار + managed 140–1050 دولار/شهر يبني «مكتب Cloudflare AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cloudflare Workers AI Gateway 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة finops stack (routing، policies، training):</strong> 4–12 يومًا — 2200–45000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل budgets والـ security:</strong> — 140–1050 دولار/شهر.</li>
          <li><strong>Reference architectures (RAG، agents، batch):</strong> — 58–265 دولار/architecture.</li>
          <li><strong>دورات «حوكمة AI على الـ edge بالعربية»:</strong> — 50–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cloudflare</span>
        <span class="tag">Workers</span>
        <span class="tag">FinOps</span>
        <span class="tag">Infrastructure</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Replit Agent 4 Arabic: من فكرة Slack إلى app منشور — backend، DB، وpayments!</h2>
      <p class="article-lead">«عندنا idea — بس ما عندنا وقت coding». في 9 أكتوبر 2026، أطلقت <strong>Replit</strong> <strong>Agent 4 Arabic</strong>: وكيل full-stack يُ parse product briefs بالعربية، يُ scaffold React أو Flutter، يُ provision Postgres وauth، يُ integrate Stripe وTap Payments MENA، يُ write tests، يُ deploy Replit أو export Docker، ويُ iterate من تعليقات voice note — لل founders وbootcamps في MENA.</p>
      <p>المشكلة التي حلّتها: Agent 3 كان يُ break على RTL layouts؛ الإصدار 4 يُ Arabic UI kit، يُ benchmark 72h من idea إلى paid beta في marketplace مغربي، يُ security review dependencies، يُ team collab roles، ويُ usage-based billing transparent.</p>
      <p>القدرات الأساسية: Multi-agent planning (PM + dev + QA)؛ integration GitHub sync؛ mobile preview؛ analytics hooks؛ template library (CRM، booking، LMS).</p>
      <p>للمبدعين العرب: no-code agencies — «Replit Agent 4 Arabic MVP factory in 5 days» لل clients 1–3 MVPs/ربع. من يُ ship 10 factories/سنة بـ 3500–55000 دولار + support 180–1400 دولار/شهر يبني «مصنع MVP عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Agent 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة MVP factory (build، deploy، handoff):</strong> 4–10 أيام — 3500–55000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل features والـ scaling:</strong> — 180–1400 دولار/شهر.</li>
          <li><strong>Vertical accelerators (food delivery، tutoring، B2B portal):</strong> — 75–320 دولار/accelerator.</li>
          <li><strong>دورات «من الفكرة إلى الإيراد بالعربية مع Replit Agent»:</strong> — 55–260 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Agent</span>
        <span class="tag">Full-stack</span>
        <span class="tag">Startups</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 09-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="09-10-2026 -- 12-AM.html">
          📰 9 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Vercel v0 4 Arabic · Postman AI Agent Builder 3 Arabic · Cloudflare Workers AI Gateway 3 Arabic · Replit Agent 4 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/09-10-2026 -- 12-AM.html`](news/09-10-2026%20--%2012-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "09-10-2026 -- 12-AM.html" not in content:
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
    if new_content == content and "09-10-2026 -- 12-AM.html" not in content:
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
        " y\u064f ",
        "yü ",
        "yü",
        "تü",
        "فيdeo",
        "montaje",
        "المشk problem",
        "أktober",
        "أktobar",
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
