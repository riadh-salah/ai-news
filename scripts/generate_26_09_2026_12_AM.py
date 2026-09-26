#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "26-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Vertex AI Agent Builder 3 Arabic، IBM watsonx Orchestrate 3 Arabic، Meta WhatsApp Business AI Agents 3 Arabic، Dropbox Dash 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Google Vertex AI Agent Builder 3 Arabic الذي يُحوّل prompt عربي إلى وكيل يُشغّل BigQuery وGmail وCalendar في دقائق، إلى IBM watsonx Orchestrate 3 Arabic الذي يُنسّق HR وfinance وprocurement كموظف رقمي واحد، ومن Meta WhatsApp Business AI Agents 3 Arabic الذي يُغلق مبيعات ودعمًا على واتساب باللهجات، إلى Dropbox Dash 3 Arabic الذي يُجيب «أين العقد؟» من كل ملفات شركتك — أربع قصص ليلية في 26 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للبناة: CTOs يريدون agents على GCP بـ data residency، CIOs يبحثون عن orchestration enterprise، تجّار e-commerce يطمحون لـ WhatsApp automation حقيقي، وفرق knowledge تريد search موحّد RTL. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 26 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Vertex AI Agent Builder 3 Arabic: من فكرة بالعربية إلى وكيل production — tools، guardrails، وMENA hosting!</h2>
      <p class="article-lead">«نريد وكيلًا يقرأ policy داخل Drive ويُفتح ticket في Jira — والفريق ينتظر integration شهرًا». في 26 سبتمبر 2026، أطلقت <strong>Google Cloud</strong> <strong>Vertex AI Agent Builder 3 Arabic</strong>: منصة low-code وpro-code لبناء agents يفهمون NL بالعربية (MSA وخليجي ومصري)، يُ connect BigQuery وCloud Storage وGmail وCalendar وSAP connectors، يُ run multi-step plans، يُ enforce IAM وVPC-SC، ويُ deploy في region Dammam/EU — للبنوك وretail groups وtelcos في MENA.</p>
      <p>المشكلة التي حلّتها: Agent Builder 2 كان English-first وassist-heavy؛ الإصدار 3 يُ act ضمن policies (query warehouse، send approved email، create Calendar hold، post summary Arabic في Chat)، يُ ground على corpus المصرّح، يُ integrate Gemini 2.5 Pro وClaude via Model Garden، يُ offer evaluation harness «Arabic hallucination score»، يُ log every tool call للaudit، ويُ ship partner accelerators للـ KSA PDPL وUAE data laws.</p>
      <p>القدرات الأساسية: Arabic Agent Designer UI؛ prebuilt templates (invoice chase، vendor onboarding، SOC triage lite)؛ MCP gateway managed؛ cost caps per agent؛ A/B routing بين models؛ white-label SDK للintegrators.</p>
      <p>للمبدعين العرب: GCP partners وAI studios — «Arabic production agent in 9 days» لل enterprises 500+ seats. من يُ deliver 4 Vertex Agent Builder 3 programs/ربع بـ 3800–48000 دولار + managed eval 720–5600 دولار/شهر يركب موجة cloud agents enterprise في المنطقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Vertex AI Agent Builder 3 Arabic؟</h3>
        <ul>
          <li><strong>Agent Builder 3 rollout (Arabic UX، tools، guardrails، go-live):</strong> 8–22 يومًا — 3500–52000 دولار/عميل.</li>
          <li><strong>Managed agent eval and prompt/tool tuning:</strong> — 680–5200 دولار/شهر.</li>
          <li><strong>Vertical agent kits (banking، logistics، healthcare):</strong> — 58–295 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Cloud Agents with Vertex AI»:</strong> — 48–238 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google Cloud</span>
        <span class="tag">Vertex AI</span>
        <span class="tag">Agents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>IBM watsonx Orchestrate 3 Arabic: موظف رقمي واحد — HR، finance، IT، وprocurement بconversation واحدة!</h2>
      <p class="article-lead">«موظف يسأل عن leave balance وexpense status وlaptop request — وثلاثة portals مختلفة». في 26 سبتمبر 2026، أطلقت <strong>IBM</strong> <strong>watsonx Orchestrate 3 Arabic</strong>: digital worker layer فوق Workday وSAP وServiceNow وMicrosoft 365 يُ understand intents بالعربية، يُ orchestrate skills عبر systems، يُ draft approvals، يُ escalate exceptions، يُ summarize «ما الذي تأخر هذا الأسبوع؟» للمدير — لـ holding companies وairlines وuniversities في الخليج.</p>
      <p>المشكلة التي حلّتها: Orchestrate 2 كان skill catalog محدود؛ الإصدار 3 يُ act (submit PTO، route PO، reset MFA، schedule interview panel)، يُ integrate watsonx.governance للbias وPII، يُ bilingual employee comms EN/AR، يُ offer on-prem option للقطاع الحساس، يُ scale 10k+ concurrent chats مع latency SLA، يُ partner packs government وenergy MENA.</p>
      <p>القدرات الأساسية: Arabic Digital Employee Builder؛ prebuilt skills library 400+؛ voice channel for call centers؛ analytics «hours returned to business»؛ IBM Consulting fast-start 21 days.</p>
      <p>للمبدعين العرب: IBM partners وHR tech consultancies — «Arabic digital worker in 12 days» لل groups 5000+ employees. من يُ sell 3 Orchestrate 3 estates/سنة بـ 5200–72000 دولار/each + care 980–7400 دولار/شهر يبني practice enterprise automation premium.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من IBM watsonx Orchestrate 3 Arabic؟</h3>
        <ul>
          <li><strong>Orchestrate 3 deployment (skills، Arabic NL، integrations، UAT):</strong> 10–28 يومًا — 4800–78000 دولار/مشروع.</li>
          <li><strong>Monthly skill hygiene and employee experience tuning:</strong> — 920–7100 دولار/شهر.</li>
          <li><strong>Department starter packs (HR، finance، IT):</strong> — 62–318 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Digital Workforce with watsonx»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">IBM</span>
        <span class="tag">watsonx</span>
        <span class="tag">Automation</span>
        <span class="tag">HR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Meta WhatsApp Business AI Agents 3 Arabic: متجرك على واتساب — qualify، sell، support، وcart recovery باللهجة!</h2>
      <p class="article-lead">«80% من leads الخليج يأتون واتساب — وردود copy-paste تُفقد الصفقة». في 26 سبتمبر 2026، أطلقت <strong>Meta</strong> <strong>WhatsApp Business AI Agents 3 Arabic</strong>: agents داخل WhatsApp Business Platform يُ qualify leads، يُ recommend products من catalog، يُ apply promo rules، يُ handoff human مع transcript Arabic، يُ recover abandoned carts، يُ collect COD confirmations — للـ D2C brands وclinics وreal estate في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 2 كان template-heavy؛ الإصدار 3 يُ understand voice notes Arabic، يُ integrate Shopify وSalla وZid وpayment links، يُ enforce Meta commerce policies، يُ dialect packs Gulf/Egypt/Levant، يُ analytics funnel per campaign، يُ transparent pricing per conversation tier للSMBs.</p>
      <p>القدرات الأساسية: Agent Studio Arabic prompts؛ catalog sync real-time؛ Click-to-WhatsApp ads hooks؛ human-in-the-loop approvals؛ partner certification «MENA Commerce Agent».</p>
      <p>للمبدعين العرب: Meta Business Partners وperformance agencies — «Arabic WhatsApp agent live in 5 days» لل merchants 1k+ chats/week. من يُ deploy 12 Agent 3 stacks/ربع بـ 1100–9800 دولار/each + optimization 220–1750 دولار/شهر ي capture أسرع قناة مبيعات في المنطقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meta WhatsApp Business AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>WhatsApp Agent 3 setup (catalog، Arabic tone، ads، training):</strong> 4–12 يومًا — 950–11500 دولار/عميل.</li>
          <li><strong>Monthly conversation tuning and campaign A/B:</strong> — 210–1680 دولار/شهر.</li>
          <li><strong>Vertical commerce kits (beauty، electronics، clinics):</strong> — 38–178 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Conversational Commerce on WhatsApp»:</strong> — 32–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meta</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Commerce</span>
        <span class="tag">SMB</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Dropbox Dash 3 Arabic: «أين نسخة العقد الموقّع؟» — search موحّد، answers، وactions عبر Drive وSlack وNotion!</h2>
      <p class="article-lead">«400 GB scattered — والمحامي ينتظر ساعة ليجد clause». في 26 سبتمبر 2026، أطلقت <strong>Dropbox</strong> <strong>Dash 3 Arabic</strong>: universal AI search وassistant فوق Dropbox وGoogle Drive وMicrosoft 365 وSlack وNotion وJira يُ answer questions بالعربية مع citations، يُ summarize folders، يُ draft replies from context، يُ suggest next actions (share link، request signature، schedule review) — للـ law firms وconsultancies وNGOs في MENA.</p>
      <p>المشكلة التي حلّتها: Dash 2 كان search-first English UI؛ الإصدار 3 يُ act ضمن permissions (create shared link، start Dropbox Sign flow، post Arabic summary في Slack)، يُ RTL preview للPDFs، يُ respect connector scopes، يُ enterprise SSO وaudit logs، يُ «project brain» mode يُ rebuild timeline من scattered docs.</p>
      <p>القدرات الأساسية: Arabic Dash Chat؛ connector packs legal وconsulting؛ mobile voice query Arabic؛ admin analytics «questions saved per week»؛ partner resale margins للVARs.</p>
      <p>للمبدعين العرب: productivity consultants وIT admins — «Arabic knowledge hub in 7 days» لل teams 50–800 users. من يُ onboard 8 Dash 3 workspaces/ربع بـ 1400–12000 دولار/each + hygiene retainer 280–2100 دولار/شهر ي monetize pain point «فوضى الملفات» في كل مكتب عربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dropbox Dash 3 Arabic؟</h3>
        <ul>
          <li><strong>Dash 3 rollout (connectors، Arabic Q&amp;A، permissions، training):</strong> 5–15 يومًا — 1200–14500 دولار/عميل.</li>
          <li><strong>Monthly knowledge cleanup and connector health:</strong> — 260–1950 دولار/شهر.</li>
          <li><strong>Industry packs (legal، audit، creative agencies):</strong> — 44–205 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Knowledge AI with Dropbox Dash»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dropbox</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Search</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="26-09-2026 -- 12-AM.html">
          📰 26 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Google Vertex AI Agent Builder 3 Arabic · IBM watsonx Orchestrate 3 Arabic · Meta WhatsApp Business AI Agents 3 Arabic · Dropbox Dash 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/26-09-2026 -- 12-AM.html`](news/26-09-2026%20--%2012-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "26-09-2026 -- 12-AM.html" not in content:
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
    if new_content == content and "26-09-2026 -- 12-AM.html" not in content:
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
