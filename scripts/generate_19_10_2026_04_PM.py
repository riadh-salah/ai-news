#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 19-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "19-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "GitHub Copilot Workspace 4 Arabic · HubSpot Breeze AI 4 Arabic · "
    "ServiceNow Now Assist 4 Arabic · Zendesk AI Agents 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — GitHub Copilot Workspace 4 Arabic، HubSpot Breeze AI 4 Arabic، ServiceNow Now Assist 4 Arabic، Zendesk AI Agents 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 19 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من GitHub Copilot Workspace 4 Arabic الذي يُحوّل issue في Jira إلى خطة refactor وpull request قبل أن تُغلق تذكرة العميل، إلى HubSpot Breeze AI 4 Arabic الذي يُ draft sequences وdeals وcontent لسوق MENA من CRM حي، ومن ServiceNow Now Assist 4 Arabic الذي يُ resolve incidents وchange requests بلسان IT عربي، إلى Zendesk AI Agents 4 Arabic الذي يُغلق تذاكر support بلهجات متعددة مع handoff ذكي — أربع قصص مسائية في 19 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ للمطورين والمبيعات وIT والدعم: فرق تُ ship features تحت ضغط، revenue teams تطارد leads بلا copy متسق، NOCs تغرق في alerts، ومراكز خدمة العملاء تُ balance SLA مع empathy. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 19 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>GitHub Copilot Workspace 4 Arabic: من الفكرة إلى PR — plan، code، وtests في مسار واحد!</h2>
      <p class="article-lead">«الـ sprint ينتهي غدًا — والـ bug في production منذ الصباح». في 19 أكتوبر 2026، أطلقت <strong>GitHub</strong> <strong>Copilot Workspace 4 Arabic</strong>: بيئة agentic داخل GitHub تُ ingest issues وSlack threads وlogs، تُ draft implementation plan RTL، تُ propose file changes عبر repos متعددة، تُ generate tests وdocs بالعربية والإنجليزية، تُ open PR مع review checklist، وتُ respect org policies وsecret scanning — لل startups وenterprises وoutsourcing shops في MENA.</p>
      <p>المشكلة التي حلّتها: Workspace 3 كان يُ over-edit خارج نطاق الـ issue؛ الإصدار 4 يُ scoped diffs، يُ benchmark −38% «time to first PR» في fintech Cairo، يُ integration Azure DevOps وJira bidirectional، يُ Arabic commit messages وrelease notes، يُ Copilot code review suggestions MSA، ويُ enterprise audit trail لل regulated sectors.</p>
      <p>القدرات الأساسية: Issue-to-PR flow; Multi-repo planning; Test generation; Bilingual docs; Policy gates; Review assist RTL.</p>
      <p>للمبدعين العرب: DevOps boutiques — «Copilot Workspace 4 Arabic velocity pack in 7 days» لل teams 15–800 engineers. من يُ deploy 6 packs/ربع بـ 3800–72000 دولار + coaching 240–1950 دولار/شهر يبني «استوديو GitHub AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitHub Copilot Workspace 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة velocity (workflows، guardrails، training، pilot sprint):</strong> 5–14 يومًا — 3800–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ prompt patterns وmetrics reviews:</strong> — 240–1950 دولار/شهر.</li>
          <li><strong>Stack kits (Node، .NET، mobile Flutter، data pipelines):</strong> — 58–265 دولار/kit.</li>
          <li><strong>دورات «شحن أسرع بـ Copilot Workspace بالعربية»:</strong> — 46–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitHub</span>
        <span class="tag">Copilot Workspace</span>
        <span class="tag">DevOps</span>
        <span class="tag">Agentic Dev</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>HubSpot Breeze AI 4 Arabic: CRM يُ sell — leads، sequences، وreports بصوت علامتك!</h2>
      <p class="article-lead">«200 lead من معرض دبي — ولا email عربي يُ match brand guide». في 19 أكتوبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze AI 4 Arabic</strong>: طبقة AI عبر Marketing Hub وSales Hub وService Hub تُ enrich contacts MENA، تُ draft outreach MSA vs Khaleeji، تُ summarize deal rooms RTL، تُ predict close dates من engagement، تُ generate landing copy وblog outlines، تُ coach reps على objection handling بالعربية — لل SMBs وscale-ups وagencies في المنطقة.</p>
      <p>المشكلة التي حلّتها: Breeze 3 كان يُ generic tone على WhatsApp leads؛ الإصدار 4 يُ dialect profiles، يُ benchmark +27% reply rate في B2B SaaS UAE، يُ integration LinkedIn وMeta lead ads، يُ Smart CRM cleanup duplicates Arabic names، يُ compliance notes PDPL، ويُ partner marketplace templates لل real estate وeducation.</p>
      <p>القدرات الأساسية: Lead enrichment RTL; Sequence copilot; Deal summaries; Content studio; Rep coaching; Analytics narratives.</p>
      <p>للمبدعين العرب: HubSpot partners — «Breeze AI 4 Arabic revenue engine in 8 days» لل orgs 50–5000 contacts/month growth. من يُ launch 7 engines/ربع بـ 2600–48000 دولار + optimization 190–1520 دولار/شهر يبني «مكتب HubSpot AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue engine (CRM audit، sequences، content، training):</strong> 6–12 يومًا — 2600–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ sequence A/B وpipeline hygiene:</strong> — 190–1520 دولار/شهر.</li>
          <li><strong>Industry playbooks (proptech، edtech، clinics، logistics):</strong> — 54–238 دولار/playbook.</li>
          <li><strong>دورات «مبيعات automated بـ Breeze AI بالعربية»:</strong> — 40–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Breeze AI</span>
        <span class="tag">CRM</span>
        <span class="tag">RevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ServiceNow Now Assist 4 Arabic: IT يُ heal نفسه — incidents، changes، وknowledge بثقة!</h2>
      <p class="article-lead">«P1 بعد 5 دقائق من deploy — والـ runbook بالإنجليزية فقط». في 19 أكتوبر 2026، أطلقت <strong>ServiceNow</strong> <strong>Now Assist 4 Arabic</strong>: generative AI عبر ITSM وCSM وHRSD يُ summarize incidents RTL، يُ suggest resolution steps من knowledge base، يُ draft change requests وimpact analysis، يُ auto-categorize tickets، يُ generate employee-facing replies بالفصحى واللهجات، يُ virtual agent لل self-service — لل banks وtelcos وgovernment digital services في MENA.</p>
      <p>المشكلة التي حلّتها: Now Assist 3 كان يُ hallucinate CMDB links؛ الإصدار 4 يُ grounded retrieval، يُ benchmark −44% MTTR في utility Jordan، يُ integration Microsoft Entra وSplunk، يُ Arabic runbook authoring، يُ manager dashboards Arabic، ويُ data residency options UAE.</p>
      <p>القدرات الأساسية: Incident summarization RTL; Resolution assist; Change drafting; Virtual agent; KB generation; Executive briefs.</p>
      <p>للمبدعين العرب: ServiceNow SIs — «Now Assist 4 Arabic IT transformation in 16 days» لل orgs 500–50000 agents. من يُ deliver 4 programs/ربع بـ 7800–105000 دولار + managed 420–3200 دولار/شهر يبني «مركز ServiceNow AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ServiceNow Now Assist 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة Now Assist (KB migration، flows، UAT، change mgmt):</strong> 12–22 يومًا — 7800–105000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ model tuning وKB freshness:</strong> — 420–3200 دولار/شهر.</li>
          <li><strong>Domain packs (core banking، 5G NOC، e-government portal):</strong> — 95–365 دولار/pack.</li>
          <li><strong>دورات «ITSM ذكي بـ Now Assist بالعربية»:</strong> — 55–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ServiceNow</span>
        <span class="tag">Now Assist</span>
        <span class="tag">ITSM</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zendesk AI Agents 4 Arabic: support على autopilot — resolve، upsell، وempathy!</h2>
      <p class="article-lead">«3000 ticket/open — والعميل يريد إجابة باللهجة المصرية الآن». في 19 أكتوبر 2026، أطلقت <strong>Zendesk</strong> <strong>AI Agents 4 Arabic</strong>: autonomous agents فوق Sunshine وMessaging وVoice تُ understand intent RTL، تُ pull order data من Shopify وSAP، تُ offer refunds وreplacements ضمن policy، تُ escalate emotional cases لـ human مع full transcript، تُ suggest macros لل agents، تُ measure CSAT lift — لل e-commerce وtravel وfintech support في MENA.</p>
      <p>المشكلة التي حلّتها: AI Agents 3 كان يُ loop على shipping FAQs؛ الإصدار 4 يُ multi-intent routing، يُ benchmark 68% auto-resolution في fashion retailer KSA، يُ WhatsApp Business native، يُ brand tone profiles، يُ QA sampling Arabic، ويُ partner certifications لل BPOs.</p>
      <p>القدرات الأساسية: Autonomous resolution RTL; Omnichannel (chat، email، voice); Policy-bound actions; Agent assist; Analytics QA; Integration marketplace.</p>
      <p>للمبدعين العرب: Zendesk CX agencies — «AI Agents 4 Arabic support transformation in 10 days» لل brands 5K–500K tickets/year. من يُ go-live 5 programs/ربع بـ 3400–62000 دولار + care 210–1680 دولار/شهر يبني «استوديو Zendesk AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zendesk AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة support AI (intents، KB، integrations، pilot، rollout):</strong> 7–16 يومًا — 3400–62000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ intent tuning وQA dashboards:</strong> — 210–1680 دولار/شهر.</li>
          <li><strong>Channel kits (WhatsApp peak، Ramadan hours، voice IVR handoff):</strong> — 60–248 دولار/kit.</li>
          <li><strong>دورات «دعم ذكي بـ Zendesk AI Agents بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zendesk</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Customer Support</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 19-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="19-10-2026 -- 04-PM.html">
          📰 19 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "19-10-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/19-10-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    if new in content and "أحدث إصدار" in content.split(new)[0][-200:]:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/19-10-2026 -- 08-AM.html"
    new_line = (
        f"- [`{new}`](news/19-10-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS}) "
        f"(4 أخبار + أفكار ربح من AI)"
    )
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if old_marker in line and "أحدث إصدار" in line:
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
        "أفكar",
        "دolار",
        "البروtokol",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "y\u0650",
        "المشkلة",
        "mezclar",
        "وy\u0650",
        "prefe r",
        " t\u0650",
        " y\u0650",
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
    update_readme()


if __name__ == "__main__":
    main()
