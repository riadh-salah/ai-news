#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 09-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "09-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Agentforce 2 Arabic · Snowflake Cortex Analyst 3 Arabic · "
    "Zendesk AI Agents 3 Arabic · Databricks Genie 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Agentforce 2 Arabic، Snowflake Cortex Analyst 3 Arabic، Zendesk AI Agents 3 Arabic، Databricks Genie 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 9 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌅 نشرة AI العالمية</span>
      <h1>من Salesforce Agentforce 2 Arabic الذي يُحوّل pipeline ميتًا إلى وكلاء مبيعات وخدمة يتحدثون فصحى ويُغلقون الفرص قبل قهوة الصباح، إلى Snowflake Cortex Analyst 3 Arabic الذي يُجيب أسئلة CFO عن البيانات بلهجة finance عربية دون كتابة SQL، ومن Zendesk AI Agents 3 Arabic الذي يُحل تذاكر دعم عربية من أول رسالة ويُصعّد فقط ما يستحق إنسانًا، إلى Databricks Genie 2 Arabic الذي يُبني لوحات ونماذج ML من وصف عربي في دقائق — أربع قصص صباحية في 9 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء بداية اليوم!</h1>
      <p class="hero-sub">صباحٌ لفرق revenue وdata وsupport: صفقات عالقة، تقارير تتأخر، تذاكر متراكمة، ومهندسو بيانات ينتظرون dashboards. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 9 نوفمبر 2026</span>
        <span>🌄 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Agentforce 2 Arabic: مبيعات وخدمة — وكلاء autonomous يُغلقون الصفقات بلسان فريقك!</h2>
      <p class="article-lead">«العميل سأل عن SLA بالعربية الساعة 6 صباحًا — ومندوب المبيعات لم يفتح هاتفه بعد». في 9 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 2 Arabic</strong>: منصة وكلاء ذكية فوق Sales Cloud وService Cloud وMarketing Cloud يُ orchestrate autonomous agents يُ qualify leads، يُ answer product questions بالفصحى واللهجات المختارة، يُ draft proposals وquotes RTL، يُ schedule meetings وhandoffs للبشر، يُ resolve tier-1 service cases مع citations من Knowledge، يُ respect Einstein Trust Layer وdata residency، يُ integrate WhatsApp Business وSlack وMuleSoft — لل B2B وtelco وretail banks وhospitality في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار 1 كان يُ over-escalate أو يُ hallucinate pricing؛ الإصدار 2 يُ grounding صارم على price books وcontracts، يُ benchmark +38% lead response speed و−41% tier-1 backlog في fintech خليجي 220 مقعدًا، يُ human-in-the-loop approvals للخصومات، يُ partner accelerators في الرياض ودبي والقاهرة، ويُ industry playbooks لـ insurance وreal estate.</p>
      <p>القدرات الأساسية: Multi-agent routing؛ Arabic sentiment وintent؛ CRM write-backs آمنة؛ audit trails لل regulators؛ sandbox لل solution architects.</p>
      <p>للمبدعين العرب: Salesforce SI partners — «Agentforce 2 Arabic revenue crew in 10 days» لل orgs 80–8000 users. من يُ launch 7 crews/ربع بـ 4200–85000 دولار + retainer 380–3200 دولار/شهر يبني «استوديو Agentforce عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 2 Arabic؟</h3>
        <ul>
          <li><strong>Agent deployment (data model، Arabic prompts، guardrails، UAT):</strong> 8–22 يومًا — 4200–85000 دولار/عميل.</li>
          <li><strong>Monthly agent tuning وconversion reviews:</strong> — 380–3200 دولار/شهر.</li>
          <li><strong>Vertical kits (banks، SaaS، healthcare CRM):</strong> — 58–265 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء مبيعات ذكية بـ Salesforce بالعربية»:</strong> — 55–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Agentforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Revenue</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Snowflake Cortex Analyst 3 Arabic: lakehouse يُجيب — metrics، trends، وforecasts بلسان CFO!</h2>
      <p class="article-lead">«ما سبب انخفاض margin في Q3 لفرع الرياض؟ — وثلاث ساعات حتى يرجع analyst بالرسم». في 9 نوفمبر 2026، أطلقت <strong>Snowflake</strong> <strong>Cortex Analyst 3 Arabic</strong>: مساعد تحليلي داخل Snowflake Intelligence يُ parse أسئلة finance وops وproduct بالفصحى، يُ generate SQL وsemantic queries مع row-level security، يُ explain variance وseasonality «لماذا قفزت CAC رغم ثبات الإنفاق؟»، يُ draft board slides RTL، يُ chart في Snowsight، يُ integrate dbt وFivetran lineage، يُ certify answers لل audit، يُ mobile voice في التطبيق — لل retail groups وtelecom وinsurance وgov analytics في MENA.</p>
      <p>المشكلة التي حلّتها: Analyst 2 كان يُ stumble على أسماء أعمدة عربية ومقاييس مركبة؛ الإصدار 3 يُ glossary مؤسسي ثنائي اللغة، يُ benchmark −46% وقت «سؤال → chart معتمد» في conglomerate إماراتي، يُ anomaly detection narratives، يُ partner certification في Gitex وLEAP، ويُ private link للبنوك.</p>
      <p>القدرات الأساسية: Trusted semantic layer؛ bilingual metric definitions؛ scheduled Arabic digests؛ Cortex Guard لل PII؛ API لل Slack CFO bots.</p>
      <p>للمبدعين العرب: Snowflake partners — «Cortex Analyst 3 Arabic insights desk in 7 days» لل warehouses 5–500 TB. من يُ stand 9 desks/ربع بـ 3600–72000 دولار + support 290–2400 دولار/شهر يبني «مكتب Snowflake AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex Analyst 3 Arabic؟</h3>
        <ul>
          <li><strong>Analyst enablement (semantic model، Arabic metrics، RBAC، training):</strong> 5–16 يومًا — 3600–72000 دولار/عميل.</li>
          <li><strong>Monthly metric hygiene وexecutive briefings:</strong> — 290–2400 دولار/شهر.</li>
          <li><strong>Industry packs (telco ARPU، retail shrink، gov KPIs):</strong> — 52–238 دولار/حزمة.</li>
          <li><strong>دورات «تحليل بيانات ذكي بـ Snowflake بالعربية»:</strong> — 48–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Cortex</span>
        <span class="tag">Analytics</span>
        <span class="tag">Data Cloud</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Zendesk AI Agents 3 Arabic: دعم العملاء — حل تذاكر، تعاطف، وتصعيد ذكي من المحادثة الأولى!</h2>
      <p class="article-lead">«أين طلبي؟ — والعميل كتب باللهجة المغربية والموظف مشغول بـ 200 تذكرة». في 9 نوفمبر 2026، أطلقت <strong>Zendesk</strong> <strong>AI Agents 3 Arabic</strong>: وكلاء دعم autonomous فوق Sunshine وmessaging يُ read order history وKB وmacros، يُ reply بالفصحى واللهجات الشمالية والخليجية المدعومة، يُ resolve refunds وshipping وaccount unlock بسياسات مؤسسية، يُ detect churn risk وoffer retention، يُ escalate مع ملخص RTL للبشري، يُ integrate Shopify وMagento وSAP، يُ QA scoring لل managers — لل e-commerce وtravel وfintech وpublic services في MENA.</p>
      <p>المشكلة التي حلّتها: AI Agents 2 كان يُ sound robotic في العربية؛ الإصدار 3 يُ tone-of-voice branding، يُ benchmark 72% auto-resolution في marketplace سعودي 1.8M tickets/سنة، يُ copilot لل agents live، يُ partner marketplace في المنطقة، ويُ compliance templates لـ PDPL.</p>
      <p>القدرات الأساسية: Omnichannel Arabic؛ knowledge grounding؛ sentiment-aware apologies؛ workforce forecasting hints؛ admin analytics بالعربية.</p>
      <p>للمبدعين العرب: CX consultancies — «AI Agents 3 Arabic support factory in 6 days» لل brands 50k–5M tickets/سنة. من يُ deploy 8 factories/ربع بـ 2800–55000 دولار + coaching 220–1850 دولار/شهر يبني «مركز Zendesk AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zendesk AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>Agent rollout (KB، Arabic tone، policies، A/B):</strong> 4–14 يومًا — 2800–55000 دولار/عميل.</li>
          <li><strong>Monthly CSAT tuning وescalation audits:</strong> — 220–1850 دولار/شهر.</li>
          <li><strong>Vertical playbooks (delivery apps، airlines، neobanks):</strong> — 44–205 دولار/حزمة.</li>
          <li><strong>دورات «دعم عملاء ذكي بـ Zendesk بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zendesk</span>
        <span class="tag">CX</span>
        <span class="tag">Support</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Databricks Genie 2 Arabic: بيانات وML — dashboards وmodels من سؤال عربي واحد!</h2>
      <p class="article-lead">«اريد churn forecast لعملاء الاشتراك الشهري مع شرح للمدير — والفريق ينتظر sprint كامل». في 9 نوفمبر 2026، أطلقت <strong>Databricks</strong> <strong>Genie 2 Arabic</strong>: conversational AI فوق Unity Catalog وLakehouse يُ understand data questions بالفصحى، يُ propose SQL وnotebooks وdashboards، يُ train baseline models مع MLflow guardrails، يُ explain features RTL «لماذا تصنّف هذه العينة high-risk؟»، يُ schedule jobs وalerts، يُ collaborate في Databricks One، يُ air-gap للبيانات الحساسة — لل digital banks وmedia وlogistics وsmart city في MENA.</p>
      <p>المشكلة التي حلّتها: Genie 1 كان يُ overfit على prompts إنجليزية؛ الإصدار 2 يُ Arabic entity linking، يُ benchmark −42% time-to-first-production dashboard في telecom مصري، يُ responsible AI reviews، يُ partner bootcamps في عمّان ودبي، ويُ certifications لـ system integrators.</p>
      <p>القدرات الأساسية: Natural language to pipeline؛ bilingual data docs؛ Genie Spaces للفرق؛ approval workflows؛ integration مع Power BI exports.</p>
      <p>للمبدعين العرب: lakehouse consultancies — «Genie 2 Arabic data studio in 9 days» لل workspaces 10–400 engineers. من يُ deliver 5 studios/ربع بـ 3400–68000 دولار + retainer 270–2250 دولار/شهر يبني «مكتب Databricks AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Databricks Genie 2 Arabic؟</h3>
        <ul>
          <li><strong>Genie studio setup (catalog، Arabic governance، use cases، handover):</strong> 7–20 يومًا — 3400–68000 دولار/عميل.</li>
          <li><strong>Monthly model reviews وexecutive explainers:</strong> — 270–2250 دولار/شهر.</li>
          <li><strong>Use-case kits (fraud، propensity، demand forecast):</strong> — 50–232 دولار/حزمة.</li>
          <li><strong>دورات «منصات Lakehouse ذكية بـ Databricks بالعربية»:</strong> — 52–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Databricks</span>
        <span class="tag">Genie</span>
        <span class="tag">ML</span>
        <span class="tag">Lakehouse</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 09-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="09-11-2026 -- 08-AM.html">
          📰 9 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "09-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/09-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/09-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
        f"(4 أخبار + أفكار ربح من AI)"
    )
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "أحدث إصدار" in line and "news/" in line:
            if new in line:
                print(f"README already points to latest: {README}")
                return
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
        "عArabية",
        "أكtober",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    if re.search(r"[yY][\u064B-\u0652\u0670]", text):
        raise SystemExit("ERROR: Latin y with Arabic diacritic found")
    if "\u00fc" in text:
        raise SystemExit("ERROR: Latin u-umlaut found — use Arabic يُ")
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
