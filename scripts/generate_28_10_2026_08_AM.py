#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 28-10-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "28-10-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Amazon Q Developer 3 Arabic · Make.com AI Scenarios 2 Arabic · "
    "Figma AI Dev Mode 3 Arabic · Airtable Omni AI 2 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Amazon Q Developer 3 Arabic، Make.com AI Scenarios 2 Arabic، Figma AI Dev Mode 3 Arabic، Airtable Omni AI 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 28 أكتوبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Amazon Q Developer 3 Arabic الذي يُفهم repos ضخمة ويُصلح bugs من أوامر عربية قبل أن تبرد فنجان القهوة، إلى Make.com AI Scenarios 2 Arabic الذي يُبني تدفقات ربح بين ERP وWhatsApp وShopify بجملة واحدة، ومن Figma AI Dev Mode 3 Arabic الذي يُحوّل frames إلى React وSwiftUI مع tokens عربية RTL، إلى Airtable Omni AI 2 Arabic الذي يُشغّل bases كوكلاء مبيعات وعمليات — أربع قصص صباحية في 28 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُشعل يومه من أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للمطورين والمستقلين وفرق التصميم والعمليات: legacy code يبتلع sprint، integrations تتعطل عند كل حرف عربي في webhook، handoff design-to-dev يستغرق أيامًا، و spreadsheets تتحول إلى متاهة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 28 أكتوبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Amazon Q Developer 3 Arabic: مساعد كود enterprise — agents، security، وAWS native!</h2>
      <p class="article-lead">«الـ PR عالق منذ أسبوع — والـ on-call نائم». في 28 أكتوبر 2026، أطلقت <strong>Amazon</strong> <strong>Q Developer 3 Arabic</strong>: مساعد تطوير مدمج في IDE وCLI يُفهم prompts بالفصحى والعامية، يُ scan repos لل vulnerabilities وdebt، يُ generate unit tests وmigrations، يُ explain legacy modules مع diagrams، يُ integrate CodeCatalyst وCodeWhisperer lineage، يُ IAM-aware suggestions (لا secrets في chat)، يُ multi-repo agents لل microservices، يُ Jira وSlack handoffs، ويُ private VPC endpoints لل banks وgov — لل teams 20–50000 engineers في MENA وglobal.</p>
      <p>المشكلة التي حلّتها: Q Developer 2 كان يُ hallucinate أسماء AWS services بالعربية؛ الإصدار 3 يُ bilingual service catalog، يُ benchmark −41% وقت «فهم module غريب» في fintech دبي، يُ automated PR reviews RTL-friendly، يُ cost estimator لـ Lambda وRDS changes، يُ compliance packs (PCI، HIPAA hints)، ويُ partner training لل SI.</p>
      <p>القدرات الأساسية: Arabic dev chat; Security and debt scans; Test and migration gen; AWS-native workflows; Enterprise VPC; Multi-repo agents.</p>
      <p>للمبدعين العرب: AWS partners — «Q Developer 3 Arabic enablement sprint in 7 days» لل orgs 50–8000 devs. من يُ deliver 8 sprints/ربع بـ 3800–78000 دولار + retainer 280–2200 دولار/شهر يبني «ممارسة Q عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Amazon Q Developer 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة enablement (IDE rollout، guardrails، pilot repos، training):</strong> 5–18 يومًا — 3800–78000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ policy updates وusage reviews:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Vertical playbooks (fintech، telecom، gov cloud):</strong> — 72–320 دولار/playbook.</li>
          <li><strong>دورات «تطوير أسرع بـ Q Developer بالعربية»:</strong> — 54–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Amazon</span>
        <span class="tag">Q Developer</span>
        <span class="tag">AWS</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Make.com AI Scenarios 2 Arabic: أتمتة بصرية تفهم العربية — ERP، WhatsApp، revenue!</h2>
      <p class="article-lead">«Zapier جميل — لكننا نحتاج scenario معقدًا ومرئيًا». في 28 أكتوبر 2026، أطلقت <strong>Make</strong> <strong>AI Scenarios 2 Arabic</strong>: منصة automation تُ build flows من وصف طبيعي بالعربية، تُ connect 2000+ apps مع error branches، تُ parse Arabic JSON وwebhooks unicode-safe، تُ AI module لـ classify emails وroute tickets، يُ generate invoices وPO من Sheets، يُ WhatsApp Business وInstagram DM routing، يُ monitor SLA وalert ops، يُ white-label لل agencies، ويُ enterprise SSO — لل SMBs وintegrators وe-commerce في MENA.</p>
      <p>المشكلة التي حلّتها: Scenarios 1 كان يُ break عند RTL text في HTTP bodies؛ الإصدار 2 يُ encoding-aware parsers، يُ benchmark +22% order fulfillment speed في retailer الرياض، يُ template library «money scenarios» (lead nurture، stock sync، refund automation)، يُ AI copilot يُ suggest next modules، ويُ usage-based billing analytics لل consultants.</p>
      <p>القدرات الأساسية: Natural language scenario build; Arabic-safe integrations; AI classification modules; Commerce and ERP flows; Agency white-label; Revenue scenario packs.</p>
      <p>للمبدعين العرب: Make partners — «AI Scenarios 2 Arabic ops blueprint in 5 days» لل businesses 10–2000 staff. من يُ ship 15 blueprints/ربع بـ 1600–34000 دولار + ops 165–1350 دولار/شهر يبني «استوديو Make عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Make.com AI Scenarios 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة ops blueprint (audit، scenarios، testing، handoff):</strong> 4–12 يومًا — 1600–34000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وscenario tuning:</strong> — 165–1350 دولار/شهر.</li>
          <li><strong>حزم قطاعية (retail، clinics، logistics، education):</strong> — 38–175 دولار/حزمة.</li>
          <li><strong>دورات «أتمتة مرئية بـ Make AI بالعربية»:</strong> — 34–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Make.com</span>
        <span class="tag">Automation</span>
        <span class="tag">Integration</span>
        <span class="tag">Revenue</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Figma AI Dev Mode 3 Arabic: من تصميم إلى كود — React، tokens، وRTL!</h2>
      <p class="article-lead">«التصميم جاهز — والمطور يسأل عن spacing للمرة العاشرة». في 28 أكتوبر 2026، أطلقت <strong>Figma</strong> <strong>AI Dev Mode 3 Arabic</strong>: طبقة dev تُ generate component code من frames، يُ understand Arabic labels في designs، يُ export React وVue وSwiftUI مع design tokens، يُ RTL layout hints وmirroring rules، يُ sync variables مع Storybook وGitHub، يُ AI diff reviews بين design versions، يُ accessibility checks WCAG، يُ Jira وLinear specs auto، ويُ enterprise libraries لل groups — لل product teams وagencies وstartups MENA.</p>
      <p>المشكلة التي حلّتها: Dev Mode 2 كان يُ flatten Arabic typography layers؛ الإصدار 3 يُ glyph-preserving exports، يُ benchmark −48% وقت «design to first PR» في SaaS القاهرة، يُ component reuse scoring، يُ codegen style guides per brand، يُ MCP server لل Cursor وCopilot context، ويُ billing seats لل design+dev duos.</p>
      <p>القدرات الأساسية: Design-to-code Arabic; RTL token export; Multi-framework output; Version diff AI; Accessibility automation; MCP for IDEs.</p>
      <p>للمبدعين العرب: Figma partners — «Dev Mode 3 Arabic design system kit in 6 days» لل teams 8–400 people. من يُ run 12 kits/ربع بـ 2200–52000 دولار + ops 195–1650 دولار/شهر يبني «خط Figma-to-code عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Figma AI Dev Mode 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة design system kit (tokens، codegen، training، pilot):</strong> 4–14 يومًا — 2200–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ library sync وQA:</strong> — 195–1650 دولار/شهر.</li>
          <li><strong>Starter templates (e-commerce، dashboard، mobile app RTL):</strong> — 55–240 دولار/template.</li>
          <li><strong>دورات «من Figma إلى production بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Figma</span>
        <span class="tag">Dev Mode</span>
        <span class="tag">Design-to-code</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Airtable Omni AI 2 Arabic: bases ذكية — CRM، ops agents، ودخل متكرر!</h2>
      <p class="article-lead">«Excel انفجر — وCRM مكلف». في 28 أكتوبر 2026، أطلقت <strong>Airtable</strong> <strong>Omni AI 2 Arabic</strong>: طبقة AI فوق bases تُ answer questions بالعربية على records، يُ build interfaces وforms من prompt، يُ assign tasks وsend reminders WhatsApp وemail، يُ summarize pipelines وforecast revenue، يُ connect Salesforce وHubSpot وStripe، يُ custom agents per department (sales، HR، inventory)، يُ audit trail وpermissions granular، ويُ partner program لل implementers — لل agencies وSMBs وops teams في MENA.</p>
      <p>المشكلة التي حلّتها: Omni 1 كان يُ misread Arabic numerals في phone fields؛ الإصدار 2 يُ locale-aware parsing، يُ benchmark −37% وقت «weekly ops review» في logistics جدة، يُ AI-generated dashboards RTL، يُ marketplace interfaces عربية، يُ sync bidirectional مع Google Calendar عربي، ويُ usage insights لل consultants.</p>
      <p>القدرات الأساسية: Arabic base Q&amp;A; Prompt-built interfaces; Ops and sales agents; CRM connectors; RTL dashboards; Implementer marketplace.</p>
      <p>للمبدعين العرب: Airtable experts — «Omni AI 2 Arabic revenue base in 4 days» لل orgs 5–500 users. من يُ deploy 18 bases/ربع بـ 1200–28000 دولار + retainer 150–1200 دولار/شهر يبني «مكتب Airtable عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable Omni AI 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue base (schema، agents، interfaces، training):</strong> 3–10 أيام — 1200–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ automations وdata hygiene:</strong> — 150–1200 دولار/شهر.</li>
          <li><strong>Industry base packs (real estate، events، franchising، NGOs):</strong> — 35–165 دولار/pack.</li>
          <li><strong>دورات «تشغيل أعمال على Airtable Omni بالعربية»:</strong> — 30–145 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">Omni AI</span>
        <span class="tag">No-code</span>
        <span class="tag">CRM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 28-10-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="28-10-2026 -- 08-AM.html">
          📰 28 أكتوبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "28-10-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/28-10-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/28-10-2026 -- 12-AM.html"
    new_line = (
        f"- [`{new}`](news/28-10-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS}) "
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
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    if re.search(r"[yY][\u064B-\u0652\u0670]", text):
        raise SystemExit("ERROR: Latin y with Arabic diacritic found")
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
