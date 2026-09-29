#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI o3 Enterprise Arabic، Workday Illuminate AI 3 Arabic، Cisco Webex AI Agent 3 Arabic، MongoDB Atlas AI Applications 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من OpenAI o3 Enterprise Arabic الذي يُحلّل عقودًا ولوائح ونماذج مالية بخطوات reasoning شفافة، إلى Workday Illuminate AI 3 Arabic الذي يُجيب الموظفين عن HR وpayroll من policies بالعربية، ومن Cisco Webex AI Agent 3 Arabic الذي يُلخّص اجتماعات ويُنفّذ follow-ups عبر Teams وSlack، إلى MongoDB Atlas AI Applications 3 Arabic الذي يُبني RAG وagents فوق بياناتك دون مغادرة cluster — أربع قصص ليلية في 29 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للقادة والمُنفّذين: CFOs يطلبون reasoning enterprise بلغة عربية، CHROs يريدون Illuminate يفهم leave policies باللهجة، IT leaders يحلمون بـ Webex agent يُغلق action items، وCTOs يبحثون عن MongoDB يُ ship agents في أيام لا أشهر. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 29 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI o3 Enterprise Arabic: reasoning مؤسسي — عقود، compliance، وmodels مالية بخطوات تُ audit!</h2>
      <p class="article-lead">«السؤال معقّد: قارن بنود العقد مع PDPL وSAMA — والرد السطحي خطر». في 29 سبتمبر 2026، أطلقت <strong>OpenAI</strong> <strong>o3 Enterprise Arabic</strong>: نموذج reasoning للمؤسسات عبر ChatGPT Enterprise وAPI يُ parse مستندات RTL، يُ chain-of-thought مع citations، يُ simulate scenarios مالية وlegal، يُ integrate Microsoft 365 وSharePoint وBox، يُ enforce data residency EU/US/GCC options، يُ red-team classifiers للمحتوى الحساس — للbanks وlaw firms وholding groups في MENA.</p>
      <p>المشكلة التي حلّتها: GPT-4.1 enterprise كان سريعًا لكن shallow على multi-step Arabic legal؛ o3 Enterprise Arabic يُ extended thinking budget per task، يُ Arabic numerals and date parsing (هجري/ميلادي)، يُ compare clause versions side-by-side، يُ export reasoning traces لـ compliance، يُ SOC2 Type II وHIPAA BAA، يُ benchmark يتفوق على Claude Opus على Arabic contract QA.</p>
      <p>القدرات الأساسية: Projects with shared Arabic prompts؛ batch API للdue diligence؛ plugins Salesforce وSAP؛ admin usage caps؛ watermarking للoutputs الحساسة.</p>
      <p>للمبدعين العرب: legal tech boutiques وrisk consultancies — «o3 Enterprise Arabic diligence sprint in 6 days» لل deals 1M–500M. من يُ deliver 5 engagements/ربع بـ 4800–92000 دولار + retainer model governance 620–5800 دولار/شهر يركب «Arabic reasoning desk».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI o3 Enterprise Arabic؟</h3>
        <ul>
          <li><strong>o3 Enterprise rollout (policies، Arabic prompt library، audit trails):</strong> 7–21 يومًا — 4500–95000 دولار/عميل.</li>
          <li><strong>Monthly reasoning QA and compliance regression:</strong> — 580–5600 دولار/شهر.</li>
          <li><strong>Vertical playbooks (M&amp;A، insurance، real estate):</strong> — 52–248 دولار/حزمة.</li>
          <li><strong>دورات «Enterprise Arabic Reasoning with o3»:</strong> — 47–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">o3</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Reasoning</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Workday Illuminate AI 3 Arabic: HR وpayroll وtalent — answers من policies بلهجة الموظف!</h2>
      <p class="article-lead">«موظف يسأل: كم رصيد إجازتي؟ — وHR تفتح 4 أنظمة». في 29 سبتمبر 2026، أطلقت <strong>Workday</strong> <strong>Illuminate AI 3 Arabic</strong>: copilot عبر HCM وFinancials وTalent يُ answer بالعربية من employee handbook وbenefits وlocal labor rules، يُ draft job descriptions RTL، يُ suggest learning paths، يُ manager nudges للreviews، يُ integrate Slack وTeams وmobile — للenterprises 2000–200000 موظف في GCC وNorth Africa.</p>
      <p>المشكلة التي حلّتها: Illuminate 2 كان English-first وweak على Gulf labor law nuances؛ الإصدار 3 يُ Khaleeji and Egyptian NLU، يُ multi-country policy routing (KSA vs UAE vs Egypt)، يُ payroll anomaly explain «لماذا اختلف الراتب؟»، يُ anonymized analytics للCHRO، يُ partner ecosystem مع regional SI في Riyadh وCairo.</p>
      <p>القدرات الأساسية: Illuminate Skills marketplace؛ custom connectors؛ audit who-asked-what؛ seasonal hiring Arabic packs؛ migration from legacy FAQ portals.</p>
      <p>للمبدعين العرب: Workday partners وHR transformation shops — «Illuminate 3 Arabic employee experience in 10 days» لل orgs rolling HCM. من يُ ship 4 programs/ربع بـ 5200–78000 دولار + content refresh 490–4500 دولار/شهر ي monetize «Arabic HR brain».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Workday Illuminate AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Illuminate 3 enablement (Arabic corpus، RBAC، change mgmt):</strong> 8–22 يومًا — 5000–82000 دولار/عميل.</li>
          <li><strong>Monthly policy updates and dialect tuning:</strong> — 460–4200 دولار/شهر.</li>
          <li><strong>Department kits (onboarding، benefits، performance):</strong> — 44–210 دولار/حزمة.</li>
          <li><strong>دورات «Arabic HR Copilot on Workday Illuminate»:</strong> — 43–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Workday</span>
        <span class="tag">Illuminate</span>
        <span class="tag">HR</span>
        <span class="tag">HCM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Cisco Webex AI Agent 3 Arabic: اجتماعات تُنتج actions — summaries، tasks، وCRM updates بلمسة واحدة!</h2>
      <p class="article-lead">«الاجتماع انتهى — ولا أحد يعرف من يفعل ماذا». في 29 سبتمبر 2026، أطلقت <strong>Cisco</strong> <strong>Webex AI Agent 3 Arabic</strong>: agent عبر Webex Suite وCalling وContact Center يُ transcribe Arabic dialects، يُ generate structured minutes RTL، يُ assign tasks في Asana وJira وMonday، يُ update Salesforce opportunities من commitments spoken، يُ real-time assist للagents في call center — للtelco وBPO وenterprise IT في MENA.</p>
      <p>المشكلة التي حلّتها: Webex AI Companion 2 كان summaries فقط؛ Agent 3 يُ proactive follow-up emails Arabic، يُ sentiment and escalation hints، يُ hybrid meeting room device integration، يُ compliance recording policies KSA/UAE، يُ ThousandEyes tie-in لـ network-aware quality، يُ pricing bundles for 500–50000 seats.</p>
      <p>القدرات الأساسية: Custom vocabulary per industry؛ role-based redaction؛ API webhooks؛ Copilot parity with Microsoft for mixed estates؛ migration from legacy UC.</p>
      <p>للمبدعين العرب: Cisco partners وcollaboration consultancies — «Webex AI Agent 3 Arabic productivity pilot in 9 days» لل orgs 300–30000 users. من يُ sell 7 rollouts/ربع بـ 3400–68000 دولار/each + adoption coaching 410–3800 دولار/شهر يركب «meetings that close loops».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cisco Webex AI Agent 3 Arabic؟</h3>
        <ul>
          <li><strong>Webex Agent 3 deployment (integrations، Arabic ASR tuning، UAT):</strong> 6–18 يومًا — 3200–72000 دولار/عميل.</li>
          <li><strong>Monthly workflow optimization and template library:</strong> — 390–3600 دولار/شهر.</li>
          <li><strong>Contact center starter packs (retention، sales، support):</strong> — 40–195 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Meeting Agents with Webex AI»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cisco</span>
        <span class="tag">Webex</span>
        <span class="tag">Collaboration</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>MongoDB Atlas AI Applications 3 Arabic: RAG وagents على بياناتك — vector search، tools، وMENA regions!</h2>
      <p class="article-lead">«البيانات في Mongo — لكن AI team يريد Postgres منفصل للvectors». في 29 سبتمبر 2026، أطلقت <strong>MongoDB</strong> <strong>Atlas AI Applications 3 Arabic</strong>: حزمة فوق Atlas Vector Search وStream Processing تُ ingest Arabic PDFs وchat logs، يُ deploy agents with function calling، يُ sync embeddings with change streams، يُ host في AWS Bahrain وUAE وFrankfurt، يُ observability وcost caps — للfintech وmarketplaces وSaaS في MENA.</p>
      <p>المشكلة التي حلّتها: DIY RAG on Mongo كان brittle؛ AI Applications 3 يُ Arabic OCR pipeline built-in، يُ multi-tenant app templates (support bot، catalog search)، يُ LangChain and Vercel AI SDK starters، يُ encryption at rest PDPL-friendly، يُ benchmark latency under 400ms P95 على Arabic queries at scale.</p>
      <p>القدرات الأساسية: Atlas Triggers for agent workflows؛ hybrid search lexical+vector؛ admin Arabic analytics dashboard؛ partner credits for startups؛ migration from Atlas Search v1.</p>
      <p>للمبدعين العرب: MongoDB partners وfull-stack agencies — «Atlas AI Applications 3 Arabic MVP in 11 days» لل products 10K–2M users. من يُ deliver 6 builds/ربع بـ 2800–58000 دولار + managed vector ops 330–3100 دولار/شهر يركب «Arabic data-native agents».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من MongoDB Atlas AI Applications 3 Arabic؟</h3>
        <ul>
          <li><strong>Atlas AI Applications build (schema، RAG، agents، Arabic eval):</strong> 8–24 يومًا — 2600–62000 دولار/عميل.</li>
          <li><strong>Monthly embedding refresh and Arabic query tuning:</strong> — 310–2900 دولار/شهر.</li>
          <li><strong>Industry templates (e-commerce، logistics، edtech):</strong> — 38–185 دولار/حزمة.</li>
          <li><strong>دورات «Arabic RAG on MongoDB Atlas AI Applications»:</strong> — 40–192 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">MongoDB</span>
        <span class="tag">Atlas</span>
        <span class="tag">RAG</span>
        <span class="tag">Vector</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-09-2026 -- 12-AM.html">
          📰 29 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">OpenAI o3 Enterprise Arabic · Workday Illuminate AI 3 Arabic · Cisco Webex AI Agent 3 Arabic · MongoDB Atlas AI Applications 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/29-09-2026 -- 12-AM.html`](news/29-09-2026%20--%2012-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-09-2026 -- 12-AM.html" not in content:
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
    if new_content == content and "29-09-2026 -- 12-AM.html" not in content:
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
