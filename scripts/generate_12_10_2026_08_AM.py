#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 12-10-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "12-10-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — LinkedIn Talent AI 4 Arabic، Box AI Hub 4 Arabic، ServiceNow Now Assist 4 Arabic، Datadog Bits AI 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 12 أكتوبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من LinkedIn Talent AI 4 Arabic الذي يُ shortlist مرشحين ويُ draft رسائل outreach بلهجة سوقك قبل أن ينتهي standup، إلى Box AI Hub 4 Arabic الذي يُ interrogate عقودًا ومستندات compliance بالعربية دون فتح مئة مجلد، ومن ServiceNow Now Assist 4 Arabic الذي يُحلّ incidents IT وHR من محادثة واحدة، إلى Datadog Bits AI 4 Arabic الذي يُحوّل تنبيهات production إلى root cause وplaybook — أربع قصص صباحية في 12 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُشعل يومه من أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للموارد البشرية والامتثال وIT ops والـ SRE: مرشحون ضائعون، عقود لا تُقرأ، tickets متراكمة، وincidents تُيقظ الفريق ليلاً. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 12 أكتوبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>LinkedIn Talent AI 4 Arabic: توظيف ذكي — sourcing، screening، ورسائل outreach RTL تُ open doors!</h2>
      <p class="article-lead">«مئتا applicant — ولا CV يُ match JD». في 12 أكتوبر 2026، أطلقت <strong>LinkedIn</strong> <strong>Talent AI 4 Arabic</strong>: suite موحّدة داخل Recruiter وHiring Manager تُ parse JDs بالفصحى واللهجات، تُ rank profiles مع explainability، تُ draft InMail وemail sequences RTL، تُ suggest interview kits، تُ flag bias risks، وتُ sync ATS (Workday، SAP SuccessFactors) — لل scale-ups وenterprises وRPOs في MENA.</p>
      <p>المشكلة التي حلّتها: Talent AI 3 كان يُ underrate bilingual talent؛ الإصدار 4 يُ Arabic skill graphs، يُ benchmark −41% time-to-shortlist في fintech دبي، يُ compliance GDPR وlocal labor hints، يُ talent pool insights بالعربية، ويُ human-in-the-loop قبل أي reject نهائي.</p>
      <p>القدرات الأساسية: Boolean-free search باللغة الطبيعية; pipeline analytics narratives; integration Microsoft Teams scheduling; employer brand copy generator; mobile approvals لل hiring managers.</p>
      <p>للمبدعين العرب: HR consultancies وrecruitment boutiques — «Talent AI 4 Arabic hiring sprint in 6 days» لل orgs 20–8000 headcount. من يُ deploy 7 programs/ربع بـ 2800–52000 دولار + retainer 220–1650 دولار/شهر يبني «مكتب توظيف AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LinkedIn Talent AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة hiring transformation (JD، AI، training):</strong> 4–11 يومًا — 2800–52000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل pipelines والتقارير:</strong> — 220–1650 دولار/شهر.</li>
          <li><strong>Playbooks قطاعية (tech، retail، healthcare):</strong> — 55–248 دولار/playbook.</li>
          <li><strong>دورات «توظيف AI بالعربية على LinkedIn»:</strong> — 45–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LinkedIn</span>
        <span class="tag">Talent AI</span>
        <span class="tag">HR</span>
        <span class="tag">Recruiting</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Box AI Hub 4 Arabic: مستودع ذكي — أسئلة على العقود، summaries، وaudit trails!</h2>
      <p class="article-lead">«عشرة آلاف PDF — والمحامي يسأل: أين بند الإنهاء؟». في 12 أكتوبر 2026، أطلقت <strong>Box</strong> <strong>AI Hub 4 Arabic</strong>: layer موحّدة على Content Cloud تُ index contracts وpolicies وfinancial packs، تُ answer أسئلة بالفصحى مع citations صفحة-صفحة RTL، تُ compare versions، تُ extract obligations وdates، تُ redact PII قبل share، وتُ connect e-signature workflows — لل legal وfinance وgov في MENA.</p>
      <p>المشكلة التي حلّتها: Box AI 3 كان يُ confuse similar clause numbers؛ الإصدار 4 يُ structured extraction لل Arabic OCR، يُ benchmark −48% وقت due diligence في acquisition سعودي، يُ retention policies enterprise، يُ multi-hub governance، ويُ export memo PDF لل boards.</p>
      <p>القدرات الأساسية: Multi-file Q&amp;A across folders; Box Sign integration; Microsoft 365 Copilot cross-links; admin analytics بالعربية; on-prem hybrid connectors.</p>
      <p>للمبدعين العرب: legal ops boutiques وBox partners — «AI Hub 4 Arabic content intelligence in 8 days» لل orgs 1K–500K files. من يُ deliver 5 hubs/ربع بـ 3500–68000 دولار + managed 280–2200 دولار/شهر يبني «استوديو Box AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Box AI Hub 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة content intelligence (taxonomy، AI Hub، training):</strong> 5–14 يومًا — 3500–68000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل governance والاستخراج:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Templates (M&amp;A، vendor، employment):</strong> — 68–295 دولار/template.</li>
          <li><strong>دورات «إدارة مستندات AI بالعربية على Box»:</strong> — 52–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Box</span>
        <span class="tag">AI Hub</span>
        <span class="tag">Legal</span>
        <span class="tag">Compliance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ServiceNow Now Assist 4 Arabic: IT وHR من chat واحد — incidents، approvals، وknowledge!</h2>
      <p class="article-lead">«VPN معطّل — والـ ticket رقم 8842 في الطابور». في 12 أكتوبر 2026، أطلقت <strong>ServiceNow</strong> <strong>Now Assist 4 Arabic</strong>: copilot عبر Virtual Agent وEmployee Center يُ troubleshoot باللهجات، يُ create وresolve incidents، يُ route approvals، يُ summarize change requests، يُ suggest KB articles RTL، ويُ automate catalog items — لل ITSM وHRSD وCSM في MENA.</p>
      <p>المشكلة التي حلّتها: Now Assist 3 كان يُ misroute Arabic intents؛ الإصدار 4 يُ intent packs MENA، يُ benchmark −37% MTTR في telco مصري، يُ integration Microsoft Entra وOkta، يُ flow designer prompts بالعربية، ويُ audit لل AI actions.</p>
      <p>القدرات الأساسية: Proactive outage comms; agent assist لل live chat; CMDB-aware answers; mobile push summaries; Now Platform store templates.</p>
      <p>للمبدعين العرب: ServiceNow partners — «Now Assist 4 Arabic employee experience in 10 days» لل enterprises 2K–120K seats. من يُ roll out 4 accounts/ربع بـ 4200–95000 دولار + support 320–2800 دولار/شهر يبني «مركز Now Assist عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ServiceNow Now Assist 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة employee experience (workflows، Now Assist، change):</strong> 6–16 يومًا — 4200–95000 دولار/عميل.</li>
          <li><strong>دعم شهري لل intents والـ KB:</strong> — 320–2800 دولار/شهر.</li>
          <li><strong>Industry packs (banking، aviation، retail):</strong> — 78–340 دولار/pack.</li>
          <li><strong>دورات «ServiceNow AI بالعربية لل IT وHR»:</strong> — 58–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ServiceNow</span>
        <span class="tag">Now Assist</span>
        <span class="tag">ITSM</span>
        <span class="tag">HR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Datadog Bits AI 4 Arabic: SRE copilot — من alert إلى root cause وremediation!</h2>
      <p class="article-lead">«PagerDuty يناديك — والـ dashboard sea of graphs». في 12 أكتوبر 2026، أطلقت <strong>Datadog</strong> <strong>Bits AI 4 Arabic</strong>: investigator يُ correlate logs وmetrics وtraces، يُ narrate incident timeline RTL، يُ suggest runbooks وTerraform fixes، يُ draft postmortems، يُ query natural language على observability stack، ويُ integrate Slack وJira وServiceNow — لل SaaS وfintech وgaming في MENA.</p>
      <p>المشكلة التي حلّتها: Bits 3 كان يُ overload engineers بنص مختلط؛ الإصدار 4 يُ Arabic on-call summaries، يُ benchmark −33% mean time to detect في neobank خليجي، يُ guardrails على destructive actions، يُ cost anomaly explanations، ويُ FinOps hints.</p>
      <p>القدرات الأساسية: Automated incident rooms; SLO breach narratives; integration PagerDuty escalation; notebook generation; API لل custom bots.</p>
      <p>للمبدعين العرب: DevOps consultancies — «Bits AI 4 Arabic observability ops in 7 days» لل teams 10–400 engineers. من يُ deploy 6 stacks/ربع بـ 3100–72000 دولار + retainer 240–2100 دولار/شهر يبني «مكتب Datadog AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Datadog Bits AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة observability AI (dashboards، Bits، runbooks):</strong> 5–12 يومًا — 3100–72000 دولار/عميل.</li>
          <li><strong>رعاية on-call شهرية لل playbooks:</strong> — 240–2100 دولار/شهر.</li>
          <li><strong>Runbooks (K8s، DB، payments):</strong> — 62–278 دولار/runbook.</li>
          <li><strong>دورات «SRE AI بالعربية مع Datadog»:</strong> — 48–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Datadog</span>
        <span class="tag">Bits AI</span>
        <span class="tag">SRE</span>
        <span class="tag">Observability</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 12-10-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="12-10-2026 -- 08-AM.html">
          📰 12 أكتوبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">LinkedIn Talent AI 4 Arabic · Box AI Hub 4 Arabic · ServiceNow Now Assist 4 Arabic · Datadog Bits AI 4 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/12-10-2026 -- 08-AM.html`](news/12-10-2026%20--%2008-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "12-10-2026 -- 08-AM.html" not in content:
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
    if new_content == content and "12-10-2026 -- 08-AM.html" not in content:
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
    if data[:2] == b"\xff\xfe" or data[:2] == b"\xfe\xff":
        raise SystemExit("ERROR: UTF-16 BOM detected")
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
        "traduce",
        "oktober",
        "Oktober",
        "mezclar",
        "إنجليزي",
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
