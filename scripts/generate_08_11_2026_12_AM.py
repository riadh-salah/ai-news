#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "08-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Databricks Assistant 3 Arabic، Elastic AI Assistant 3 Arabic، Glean AI 5 Arabic، Zoom AI Companion 5 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Databricks Assistant 3 Arabic الذي يُحوّل lakehouse صامتًا إلى محادثة analytics تجيب «لماذا انخفضت المبيعات في الرياض؟» قبل أن ينتهي اجتماع الطوارئ، إلى Elastic AI Assistant 3 Arabic الذي يُ hunt logs وtraces ويُ draft runbooks RTL بينما on-call يغمض عينيه، ومن Glean AI 5 Arabic الذي يُ find الملف والقرار والبريد في ثوانٍ عبر كل silos، إلى Zoom AI Companion 5 Arabic الذي يُلخّص اجتماعات متعددة اللغات ويُ push actions إلى CRM — أربع قصص ليلية في 8 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للفرق التي لا تنام: data engineers يبحثون عن إجابات فوق petabytes، SREs يطاردون alert storm، knowledge workers يغرقون في silos، ومديرو مبيعات يستيقظون على اجتماعات بلا ملخص. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 8 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Databricks Assistant 3 Arabic: محادثة فوق lakehouse — SQL، notebooks، وgovernance بلسان data team!</h2>
      <p class="article-lead">«الـ dashboard قديم — والمدير يسأل سؤالًا جديدًا كل ليلة». في 8 نوفمبر 2026، أطلقت <strong>Databricks</strong> <strong>Assistant 3 Arabic</strong>: copilot موحّد فوق Unity Catalog وnotebooks وSQL warehouses يُ parse أسئلة finance وops وproduct بالفصحى واللهجات المختارة، يُ generate SQL وPython آمن مع lineage، يُ explain metrics «لماذا CTR هبط بعد حملة رمضان»، يُ suggest feature engineering وtests، يُ draft data docs RTL، يُ enforce row-level policies وmasking، يُ integrate Slack وTeams للتنبيهات الليلية — لل retail وlogistics وfintech وtelco في MENA.</p>
      <p>المشكلة التي حلّتها: Assistant 2 كان يُ struggle مع Arabic entity names في CRM exports؛ الإصدار 3 يُ Unicode normalization محسّن، يُ benchmark −38% وقت «سؤال → SQL صحيح» في ecommerce خليجي، يُ agent mode يُ chain queries وvisualizations، يُ partner enablement في الرياض ودبي والقاهرة، ويُ certification لـ system integrators.</p>
      <p>القدرات الأساسية: Natural language إلى Spark وDelta؛ anomaly narratives لل boards؛ cost guardrails على clusters؛ Arabic glossary لأسماء الأعمدة؛ sandbox لل workshops التنفيذية.</p>
      <p>للمبدعين العرب: data consultancies — «Assistant 3 Arabic analytics cockpit in 14 days» لل orgs على Databricks 500TB+. من يُ deliver 6 cockpits/ربع بـ 4200–78000 دولار + managed 320–2800 دولار/شهر يبني «استوديو lakehouse عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Databricks Assistant 3 Arabic؟</h3>
        <ul>
          <li><strong>Assistant rollout (catalog، governance، Arabic glossary، UAT):</strong> 10–24 يومًا — 4200–78000 دولار/عميل.</li>
          <li><strong>Monthly query tuning وadoption analytics:</strong> — 320–2800 دولار/شهر.</li>
          <li><strong>Vertical playbooks (retail، telecom، healthcare FHIR):</strong> — 48–235 دولار/حزمة.</li>
          <li><strong>دورات «تحليلات AI على Databricks بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Databricks</span>
        <span class="tag">Lakehouse</span>
        <span class="tag">Analytics</span>
        <span class="tag">Data</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Elastic AI Assistant 3 Arabic: من alert إلى runbook — logs، APM، وsecurity بلسان SRE!</h2>
      <p class="article-lead">«الإنتاج أحمر — والفريق يتخبط بين Kibana وPagerDuty». في 8 نوفمبر 2026، أطلقت <strong>Elastic</strong> <strong>AI Assistant 3 Arabic</strong>: مساعد عبر Elasticsearch وObservability وSecurity يُ correlate logs وtraces وmetrics، يُ answer «ما سبب latency spike على API الدفع؟» بالعربية مع timeline، يُ draft remediation steps RTL، يُ suggest SIEM queries وdetection rules، يُ summarize incidents للمدير الصباحي، يُ integrate ServiceNow وJira وSlack، يُ respect RBAC وaudit trails — لل SaaS وbanks وgaming وmarketplaces في MENA.</p>
      <p>المشكلة التي حلّتها: Assistant 2 كان weak على code-switching في error messages؛ الإصدار 3 يُ Arabic+English log parsing، يُ benchmark −41% MTTR في fintech إماراتي، يُ GenAI over internal runbooks، يُ alert grouping يُ reduce noise 52%، ويُ SOC2 وdata residency EU/GCC.</p>
      <p>القدرات الأساسية: Conversational Kibana؛ playbooks auto-draft؛ threat hunting بالعربية؛ cost-aware index suggestions؛ mobile digest لل on-call.</p>
      <p>للمبدعين العرب: observability boutiques — «Elastic AI Assistant 3 Arabic war room in 7 days» لل clusters 1–500 nodes. من يُ deploy 8 war rooms/ربع بـ 2800–62000 دولار + retainer 260–2200 دولار/شهر يبني «مكتب SRE ذكي عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Elastic AI Assistant 3 Arabic؟</h3>
        <ul>
          <li><strong>Assistant setup (ingest، dashboards، Arabic runbooks، on-call rituals):</strong> 5–18 يومًا — 2800–62000 دولار/عميل.</li>
          <li><strong>Monthly incident reviews وrule tuning:</strong> — 260–2200 دولار/شهر.</li>
          <li><strong>Industry kits (payments، ecommerce peaks، Ramadan traffic):</strong> — 42–198 دولار/حزمة.</li>
          <li><strong>دورات «Observability AI مع Elastic بالعربية»:</strong> — 46–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Elastic</span>
        <span class="tag">Observability</span>
        <span class="tag">SRE</span>
        <span class="tag">Security</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Glean AI 5 Arabic: بحث enterprise يُفهم سؤالك — answers، actions، وcitations عبر كل التطبيقات!</h2>
      <p class="article-lead">«أين آخر عرض pricing للعميل السعودي؟ — وستة تطبيقات وثلاثة Slack threads». في 8 نوفمبر 2026، أطلقت <strong>Glean</strong> <strong>AI 5 Arabic</strong>: طبقة معرفة موحّدة تُ connect Slack وDrive وConfluence وSalesforce وZendesk وGitHub وBox، تُ answer بالفصحى واللهجات مع citations دقيقة، تُ draft emails وslides RTL، تُ trigger workflows (create ticket، schedule meeting)، تُ personalize حسب role وpermissions، تُ detect knowledge gaps ويُ suggest wiki updates، يُ benchmark −49% وقت البحث في holding الرياض — لل enterprises وscale-ups وconsultancies في MENA.</p>
      <p>المشكلة التي حلّتها: Glean AI 4 كان يُ duplicate answers عند Arabic OCR ضعيف؛ الإصدار 5 يُ MENA document pack، يُ multimodal charts وtables، يُ agents يُ chain internal APIs، يُ analytics لأسئلة بدون إجابة، ويُ partner program في دبي وعمّان.</p>
      <p>القدرات الأساسية: Enterprise graph؛ API لل custom apps؛ SSO وSCIM؛ Arabic Q&amp;A على English source docs؛ compliance exports.</p>
      <p>للمبدعين العرب: knowledge ops studios — «Glean AI 5 Arabic enterprise brain in 11 days» لل orgs 500–50000 seats. من يُ sell 7 brains/ربع بـ 3600–85000 دولار + managed 290–2450 دولار/شهر يبني «مركز معرفة Glean عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Glean AI 5 Arabic؟</h3>
        <ul>
          <li><strong>Glean deployment (connectors، taxonomy، Arabic tuning، training):</strong> 8–22 يومًا — 3600–85000 دولار/عميل.</li>
          <li><strong>Monthly knowledge health وgap remediation:</strong> — 290–2450 دولار/شهر.</li>
          <li><strong>Function packs (sales، legal، engineering onboarding):</strong> — 45–215 دولار/حزمة.</li>
          <li><strong>دورات «بحث enterprise بـ Glean بالعربية»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Glean</span>
        <span class="tag">Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zoom AI Companion 5 Arabic: اجتماعات تُترجم نفسها — summaries، decisions، وCRM sync بليلة واحدة!</h2>
      <p class="article-lead">«اجتماع ساعتين — ولا أحد يتذكر ماذا اتُفق». في 8 نوفمبر 2026، أطلقت <strong>Zoom</strong> <strong>AI Companion 5 Arabic</strong>: مساعد موحّد عبر Meetings وTeam Chat وPhone وMail يُ transcribe خليجي وشامي ومصري، يُ highlight decisions وaction items RTL، يُ draft follow-ups وproposals، يُ sync Salesforce وHubSpot وmonday.com، يُ coach managers على talk time وobjections، يُ cluster recurring topics عبر quarters، يُ privacy controls وretention — لل sales وCS وHR وboard meetings في MENA.</p>
      <p>المشكلة التي حلّتها: Companion 4 كان يُ lose names في code-switching؛ الإصدار 5 يُ speaker ID محسّن، يُ benchmark +24% completion rate على action items في B2B سعودي، يُ clip highlights للتدريب، يُ integration مع Microsoft 365 وGoogle Workspace، ويُ admin policies لل recordings.</p>
      <p>القدرات الأساسية: Smart chapters؛ bilingual summaries؛ automated task creation؛ deal risk signals من call patterns؛ mobile morning digest بالعربية.</p>
      <p>للمبدعين العرب: revenue ops agencies — «Companion 5 Arabic meeting OS in 6 days» لل orgs 50–5000 licenses. من يُ roll 9 programs/ربع بـ 2200–48000 دولار + tuning 210–1750 دولار/شهر يبني «استوديو اجتماعات ذكية عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoom AI Companion 5 Arabic؟</h3>
        <ul>
          <li><strong>Companion rollout (CRM sync، templates، Arabic coaching، adoption):</strong> 4–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>Monthly call reviews وplaybook updates:</strong> — 210–1750 دولار/شهر.</li>
          <li><strong>Vertical kits (real estate، insurance، government tenders):</strong> — 38–185 دولار/حزمة.</li>
          <li><strong>دورات «اجتماعات AI مع Zoom بالعربية»:</strong> — 44–208 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zoom</span>
        <span class="tag">Meetings</span>
        <span class="tag">Sales</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="08-11-2026 -- 12-AM.html">
          📰 8 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Databricks Assistant 3 Arabic · Elastic AI Assistant 3 Arabic · Glean AI 5 Arabic · Zoom AI Companion 5 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/08-11-2026 -- 12-AM.html`](news/08-11-2026%20--%2012-AM.html) — أحدث إصدار (Databricks Assistant 3 Arabic · Elastic AI Assistant 3 Arabic · Glean AI 5 Arabic · Zoom AI Companion 5 Arabic) (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "08-11-2026 -- 12-AM.html" not in content:
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
        r"- \[`news/[^`]+`\]\([^)]+\) — أحدث إصدار \([^)]+\) \(4 أخبار \+ أفكار ربح من AI\)\n",
        README_LATEST,
        content,
        count=1,
    )
    if new_content == content:
        new_content = re.sub(
            r"- \[`news/[^`]+`\]\([^)]+\) — أحدث إصدار \(4 أخبار \+ أفكار ربح من AI\)\n",
            README_LATEST,
            content,
            count=1,
        )
    if new_content == content and "08-11-2026 -- 12-AM.html" not in content:
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
    if data[:3] == b"\xef\xbb\xbf":
        raise SystemExit("ERROR: BOM found in output")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise SystemExit(f"ERROR: invalid UTF-8: {e}") from e
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
        "نوفمبرtemبر",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "رobots",
        "despierta",
        "mezclar",
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
