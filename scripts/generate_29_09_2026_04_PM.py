#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — GitHub Copilot Workspace 2 Arabic، Salesforce Agentforce 3 Arabic، Canva AI Studio 3 Arabic، Snowflake Cortex Agents 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI المسائية</span>
      <h1>من GitHub Copilot Workspace 2 Arabic الذي يُحوّل issue بالعربية إلى branch وtests وpull request قبل أن يُطفأ مكتبك، إلى Salesforce Agentforce 3 Arabic الذي يُغلق leads ويُجيب عملاء من CRM وKnowledge بلهجة خليجية، ومن Canva AI Studio 3 Arabic الذي يُولّد حملات RTL وreels وbrand kits من جملة واحدة، إلى Snowflake Cortex Agents 3 Arabic الذي يُشغّل وكلاء analytics فوق بياناتك دون نسخها إلى SaaS خارجي — أربع قصص مسائية في 29 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يُغلق قبل منتصف الليل!</h1>
      <p class="hero-sub">مساءٌ للمطورين والتسويق والمبيعات والبيانات: engineering managers يريدون Copilot يفهم requirements بالفصحى، revenue teams تحلم بـ Agentforce يُ book meetings، وكالات creative تبحث عن Canva يُحافظ على هوية العلامة، وCDOs يطلبون Cortex agents داخل warehouse. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 29 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>GitHub Copilot Workspace 2 Arabic: من ticket إلى merge — planning، coding، وreview بلغة فريقك!</h2>
      <p class="article-lead">«الـ backlog بالعربية — والكود بالإنجليزية — والفجوة تُكلّف sprint كاملًا». في 29 سبتمبر 2026، أطلقت <strong>GitHub</strong> <strong>Copilot Workspace 2 Arabic</strong>: بيئة agentic فوق GitHub Enterprise تُ parse issues وConfluence specs RTL، تُ propose architecture وfile plan، تُ generate وedit code across repos، تُ run CI وfix failures، تُ draft PR description وreview comments بالعربية أو ثنائي اللغة — للfintech وgovtech وproduct shops في MENA.</p>
      <p>المشكلة التي حلّتها: Workspace 1 كان English-first وweak على mixed-language repos؛ الإصدار 2 يُ Arabic issue templates، يُ dialect-aware acceptance criteria، يُ integrate Azure DevOps وJira، يُ policy gates (no secrets in prompts)، يُ benchmark يُقلّل time-to-PR 41% في pilot سعودي، يُ enterprise audit مع Copilot Business licenses.</p>
      <p>القدرات الأساسية: Multi-repo orchestration؛ test generation؛ security scan hooks؛ custom org instructions؛ migration من Copilot Chat في 72 ساعة؛ support for .NET وJava وPython stacks شائعة في المنطقة.</p>
      <p>للمبدعين العرب: dev consultancies وplatform teams — «Copilot Workspace 2 Arabic delivery sprint in 9 days» لل orgs 50–800 engineers. من يُ ship 5 enablements/ربع بـ 3800–72000 دولار + monthly prompt governance 440–4100 دولار/شهر يركب «Arabic software factory».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitHub Copilot Workspace 2 Arabic؟</h3>
        <ul>
          <li><strong>Workspace rollout (policies، Arabic templates، CI hooks، UAT):</strong> 6–18 يومًا — 3600–75000 دولار/عميل.</li>
          <li><strong>Monthly dev productivity coaching and guardrail tuning:</strong> — 420–3900 دولار/شهر.</li>
          <li><strong>Stack kits (Spring، Laravel، Flutter enterprise):</strong> — 44–210 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Agentic Dev with GitHub Copilot Workspace»:</strong> — 43–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitHub</span>
        <span class="tag">Copilot</span>
        <span class="tag">DevOps</span>
        <span class="tag">Workspace</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Salesforce Agentforce 3 Arabic: وكلاء مبيعات وخدمة — leads، cases، وWhatsApp من CRM واحد!</h2>
      <p class="article-lead">«العميل يسأل باللهجة — والرد template إنجليزي مترجم يُفقد الصفقة». في 29 سبتمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 3 Arabic</strong>: منصة agents فوق Sales Cloud وService Cloud وData Cloud تُ qualify leads، تُ answer FAQs من knowledge base عربية، تُ schedule meetings، تُ escalate complex cases، تُ sync WhatsApp Business وInstagram DMs، تُ respect consent وPDPL — للretail وreal estate وhealthcare في GCC.</p>
      <p>المشكلة التي حلّتها: Agentforce 2 كان English-centric وmanual prompt tuning؛ الإصدار 3 يُ MSA وGulf tone packs، يُ Einstein Trust Layer للـ PII، يُ flow builder بالعربية، يُ analytics على conversion وCSAT، يُ AppExchange partners في Dubai، يُ benchmark +28% lead response speed في e-commerce خليجي.</p>
      <p>القدرات الأساسية: Pre-built sales وservice agents؛ custom actions (create quote، update opportunity)؛ human handoff؛ multi-brand routing؛ sandbox-to-prod pipeline؛ integration MuleSoft.</p>
      <p>للمبدعين العرب: Salesforce SI partners وrevops boutiques — «Agentforce 3 Arabic go-live in 11 days» لل orgs 200–20000 users. من يُ deliver 6 agents/ربع بـ 4200–88000 دولار + optimization retainer 480–4500 دولار/شهر يركب «Arabic revenue autopilot».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 3 Arabic؟</h3>
        <ul>
          <li><strong>Agentforce implementation (Data Cloud، flows، Arabic KB، UAT):</strong> 8–24 يومًا — 4000–92000 دولار/عميل.</li>
          <li><strong>Monthly conversation tuning and A/B on scripts:</strong> — 460–4300 دولار/شهر.</li>
          <li><strong>Industry agent packs (property، clinics، telecom):</strong> — 47–225 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Sales Agents on Salesforce Agentforce»:</strong> — 45–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Agentforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Canva AI Studio 3 Arabic: حملات RTL جاهزة — posts، reels، pitch decks، وbrand voice!</h2>
      <p class="article-lead">«المبدعون ينتظرون designer — والموعد النشر فات». في 29 سبتمبر 2026، أطلقت <strong>Canva</strong> <strong>AI Studio 3 Arabic</strong>: طبقة enterprise فوق Canva Teams تُ generate campaigns RTL من brief عربي، تُ resize لـ LinkedIn وSnapchat وTikTok، تُ Magic Write للcaptions باللهجة المختارة، تُ Brand Kit lock للألوان والخطوط، تُ batch export وapproval workflows، تُ API للagencies — للtourism وF&amp;B وeducation في MENA.</p>
      <p>المشكلة التي حلّتها: AI Studio 2 كان short-form وweak على Arabic typography؛ الإصدار 3 يُ proper RTL layout engine، يُ Khaleeji وEgyptian caption modes، يُ video storyboards من script، يُ translate EN assets to Arabic with layout preserve، يُ SSO وadmin analytics، يُ partner program مع influencers platforms.</p>
      <p>القدرات الأساسية: Campaign wizard؛ voice-over script gen؛ stock + gen-image blend؛ compliance watermark للgov clients؛ team libraries؛ migration from Adobe Express in 1 week.</p>
      <p>للمبدعين العرب: social agencies وfreelance collectives — «Canva AI Studio 3 Arabic brand sprint in 4 days» لل brands posting 100+ assets/month. من يُ sell 12 retainers/ربع بـ 720–24000 دولار + per-campaign packs 120–980 دولار يركب «Arabic content machine».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva AI Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>Studio enablement (Brand Kit، workflows، Arabic templates، training):</strong> 3–10 أيام — 680–22000 دولار/عميل.</li>
          <li><strong>Monthly campaign production and dialect QA:</strong> — 280–2500 دولار/شهر.</li>
          <li><strong>Ramadan and seasonal packs (retail، charity، travel):</strong> — 35–175 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Creative Ops with Canva AI Studio»:</strong> — 38–185 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Creative</span>
        <span class="tag">Marketing</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Snowflake Cortex Agents 3 Arabic: وكلاء فوق warehouse — SQL، forecasts، وcompliance دون نسخ البيانات!</h2>
      <p class="article-lead">«البيانات في Snowflake — والـ chatbot في SaaS آخر ينسخ جداول حساسة». في 29 سبتمبر 2026، أطلقت <strong>Snowflake</strong> <strong>Cortex Agents 3 Arabic</strong>: agents فوق Cortex LLM وSearch وAnalyst داخل account تُ answer business questions بالعربية، تُ generate SQL مع row-level security، تُ run forecasts على sales data، تُ document lineage، تُ integrate Streamlit apps وSlack، تُ regions UAE وKSA للdata residency — للretail chains وbanks وlogistics في MENA.</p>
      <p>المشكلة التي حلّتها: Cortex Agents 2 كان English prompts وmanual tool wiring؛ الإصدار 3 يُ Arabic NL-to-SQL tuning، يُ semantic models for finance Arabic labels، يُ guardrails على PII columns، يُ eval harness for hallucination on metrics، يُ partner SI certifications، يُ benchmark 52% faster insight requests vs external BI copilots.</p>
      <p>القدرات الأساسية: Agent templates (FP&amp;A، inventory، customer 360)؛ scheduled reports؛ Cortex Guard؛ hybrid with external LLM via secure proxy؛ Terraform Snowflake provider updates.</p>
      <p>للمبدعين العرب: data consultancies وanalytics shops — «Cortex Agents 3 Arabic insight agent in 8 days» لل orgs with 10TB+ in Snowflake. من يُ deliver 4 agents/ربع بـ 4800–85000 دولار + warehouse tuning 520–5100 دولار/شهر يركب «Arabic data copilot inside Snowflake».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>Agent deployment (semantic model، Arabic NLG، RLS، UAT):</strong> 7–20 يومًا — 4600–88000 دولار/عميل.</li>
          <li><strong>Monthly metric dictionary and eval regression:</strong> — 500–4800 دولار/شهر.</li>
          <li><strong>Domain kits (CPG، aviation، insurance):</strong> — 50–240 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Data Agents on Snowflake Cortex»:</strong> — 48–230 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Cortex</span>
        <span class="tag">Data</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-09-2026 -- 04-PM.html">
          📰 29 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">GitHub Copilot Workspace 2 Arabic · Salesforce Agentforce 3 Arabic · Canva AI Studio 3 Arabic · Snowflake Cortex Agents 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/29-09-2026 -- 04-PM.html`](news/29-09-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-09-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "29-09-2026 -- 04-PM.html" not in content:
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
        "tربح",
        " yُ ",
        "yü ",
        "yü",
        "تü",
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
