#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "26-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google NotebookLM 5 Arabic · Cohere North 4 Arabic · "
    "SAP Joule 5 Arabic · Snowflake Cortex Agents 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google NotebookLM 5 Arabic، Cohere North 4 Arabic، SAP Joule 5 Arabic، Snowflake Cortex Agents 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Google NotebookLM 5 Arabic الذي يُحوّل مئات PDF ومحاضرات إلى بودكast عربي وخطة امتحان قبل أن تُطفأ شاشة المكتب، إلى Cohere North 4 Arabic الذي يُجيب «أين آخر عرض pricing؟» من ERP وSlack وDrive مع citation واحد، ومن SAP Joule 5 Arabic الذي يُ approve purchase orders ويُ explain variance من داخل S/4HANA بلهجة CFO، إلى Snowflake Cortex Agents 4 Arabic الذي يُشغّل وكلاء analytics فوق warehouse دون تصدير CSV — أربع قصص ليلية في 26 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمعرفة والبحث المؤسسي والعمليات والبيانات: طلاب ومدربون يغرقون في ملفات، موظفون يضيعون ساعات في البحث عن مستند، فرق procurement تنتظر تقارير finance، وanalysts يُ copy-paste SQL قبل كل اجتماع board. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 26 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google NotebookLM 5 Arabic: مصادرك تُ narrate — بودكast، امتحانات، وteams بلسان عربي!</h2>
      <p class="article-lead">«120 slide للمقرر — والامتحان بعد 48 ساعة». في 26 أكتوبر 2026، أطلقت <strong>Google</strong> <strong>NotebookLM 5 Arabic</strong>: research companion يُ ingest PDFs وGoogle Docs وSlides وYouTube (Arabic captions) وDrive folders، يُ chat بالعربية مع citations لكل جملة، يُ generate Audio Overview بلهجات MSA وGulf وEgyptian preview، يُ build study guides وflashcards وmind maps RTL، يُ compare notebooks («قارن سياسة HR مع هذا العقد»)، يُ team workspaces مع roles وwatermarking، يُ export إلى Docs/Slides Arabic layout، ويُ API للEdTech — للuniversities وcorporate L&amp;D وconsultants في MENA.</p>
      <p>المشكلة التي حلّتها: NotebookLM 4 كان يُ stumble على المصطلحات المالية والقانونية العربية في audio؛ الإصدار 5 يُ pronunciation layer متخصص، يُ benchmark −41% وقت «إعداد review pack» في edtech سعودي، يُ multi-source timeline للresearch projects، يُ admin DLP وno-train enterprise، يُ offline audio download للcommuters، ويُ partner packs لل banking compliance training.</p>
      <p>القدرات الأساسية: Arabic research companion; Audio Overview dialects; Study guides RTL; Team notebooks; Compare sources; EdTech API.</p>
      <p>للمبدعين العرب: EdTech studios — «NotebookLM 5 Arabic academy hub in 4 days» لل cohorts 300–12000 learners. من يُ ship 14 hubs/ربع بـ 950–22000 دولار + refresh 260–2100 دولار/شهر يبني «مركز NotebookLM عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google NotebookLM 5 Arabic؟</h3>
        <ul>
          <li><strong>باقة academy (sources، audio عربي، governance، training):</strong> 3–12 يومًا — 950–22000 دولار/مشروع.</li>
          <li><strong>تشغيل شهري لـ notebooks موسمية وcontent refresh:</strong> — 260–2100 دولار/شهر.</li>
          <li><strong>Vertical kits (banking، legal، medical RTL):</strong> — 45–210 دولار/kit.</li>
          <li><strong>دورات «ادرس بذكاء بـ NotebookLM بالعربية»:</strong> — 36–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">NotebookLM</span>
        <span class="tag">EdTech</span>
        <span class="tag">Research</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Cohere North 4 Arabic: enterprise search وagents — من سؤال عربي إلى action في ERP!</h2>
      <p class="article-lead">«أين نسخة العقد الموقّع؟ — و15 نظامًا للبحث». في 26 أكتوبر 2026، أطلقت <strong>Cohere</strong> <strong>North 4 Arabic</strong>: enterprise AI platform يُ unify search عبر SharePoint وGoogle Drive وSlack وSalesforce وSAP connectors، يُ answer بالعربية مع citations وpermissions-aware، يُ deploy agents تُ draft emails وtickets وapprovals، يُ RAG على private data دون training على محتواك، يُ admin SSO وaudit logs وdata residency، يُ benchmark latency لل MENA regions، ويُ partner SDK لل SIs — لل enterprises 500–50000 seats.</p>
      <p>المشكلة التي حلّتها: North 3 كان يُ miss scanned Arabic PDFs في legal archives؛ الإصدار 4 يُ OCR RTL pipeline وtable extraction، يُ benchmark −44% وقت «العثور على مستند حاسم» في bank الرياض، يُ multi-step agents مع human-in-the-loop، يُ analytics «ما الأسئلة التي لا يُجيب عنها KB؟»، يُ Arabic-English code-switch handling، ويُ indemnity tier لل regulated industries.</p>
      <p>القدرات الأساسية: Arabic enterprise search; Permission-aware RAG; Workflow agents; OCR RTL; SSO and audit; MENA latency.</p>
      <p>للمبدعين العرب: knowledge consultancies — «North 4 Arabic search brain in 10 days» لل orgs 800–25000 users. من يُ deploy 8 brains/ربع بـ 2400–72000 دولار + managed 180–1500 دولار/شهر يبني «ممارسة Cohere North عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cohere North 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة brain (connectors، agents، governance، champions):</strong> 6–20 يومًا — 2400–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ connectors وtuning:</strong> — 180–1500 دولار/شهر.</li>
          <li><strong>Industry packs (banking، energy، public sector RTL):</strong> — 62–285 دولار/pack.</li>
          <li><strong>دورات «بحث مؤسسي ذكي بـ Cohere North بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cohere</span>
        <span class="tag">North</span>
        <span class="tag">Enterprise Search</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>SAP Joule 5 Arabic: ERP يتكلّم — procurement، finance، وHR من chat واحد!</h2>
      <p class="article-lead">«PO معلّق — وCFO يسأل عن variance قبل 6 صباحًا». في 26 أكتوبر 2026، أطلقت <strong>SAP</strong> <strong>Joule 5 Arabic</strong>: copilot عبر S/4HANA وSuccessFactors وAriba يُ answer بالعربية عن procurement وGL وheadcount، يُ draft purchase requisitions وapproval chains، يُ explain budget variance مع drill-down لـ cost centers، يُ summarize vendor performance، يُ HR policy answers RTL مع links لـ policies، يُ mobile وTeams integration، يُ role-based guardrails وaudit — لل manufacturing وretail وpublic sector 1000–100000 users في MENA.</p>
      <p>المشكلة التي حلّتها: Joule 4 كان يُ confuse Arabic vendor names مع transliterations؛ الإصدار 5 يُ master data grounding، يُ benchmark −39% وقت «إغلاق دورة procurement» في retail chain مصر، يُ multi-module orchestration (finance + HR + supply chain)، يُ citation لكل SAP transaction ID، يُ partner accelerators لل government وoil &amp; gas، ويُ offline cache للcritical FAQs في sites منخفضة الاتصال.</p>
      <p>القدرات الأساسية: Arabic ERP copilot; Procurement workflows; Finance variance explain; HR policy RTL; Multi-module agents; Enterprise guardrails.</p>
      <p>للمبدعين العرب: SAP partners — «Joule 5 Arabic ops cockpit in 14 days» لل orgs on Rise/GROW. من يُ deliver 6 cockpits/ربع بـ 4800–95000 دولار + care 280–2400 دولار/شهر يبني «مركز Joule عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من SAP Joule 5 Arabic؟</h3>
        <ul>
          <li><strong>باقة cockpit (KB، workflows، training، governance):</strong> 8–22 يومًا — 4800–95000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ use cases وmaster data:</strong> — 280–2400 دولار/شهر.</li>
          <li><strong>Vertical kits (retail، utilities، healthcare RTL):</strong> — 72–330 دولار/kit.</li>
          <li><strong>دورات «عمليات ذكية بـ SAP Joule بالعربية»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">SAP</span>
        <span class="tag">Joule</span>
        <span class="tag">ERP</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Snowflake Cortex Agents 4 Arabic: وكلاء فوق warehouse — SQL، forecasts، وSlack answers!</h2>
      <p class="article-lead">«board يريد forecast — وBI team نائم». في 26 أكتوبر 2026، أطلقت <strong>Snowflake</strong> <strong>Cortex Agents 4 Arabic</strong>: agentic layer على Snowflake Data Cloud يُ answer natural language بالعربية، يُ generate SQL وPython checks مع explain، يُ run forecasts وanomaly detection على revenue وinventory، يُ post summaries إلى Slack وTeams، يُ respect row-level security وcolumn masking، يُ multi-agent teams (analyst + compliance + finance)، يُ deploy في region الخليج EU options — لل data teams 50–5000 users.</p>
      <p>المشكلة التي حلّتها: Cortex Agents 3 كان يُ hallucinate على Arabic product names في catalogs؛ الإصدار 4 يُ semantic catalog grounding، يُ benchmark −46% وقت «إعداد board narrative» في fintech دبي، يُ citation لكل query result، يُ admin approval gates لل destructive SQL، يُ partner templates لل retail وtelco، ويُ Cortex Analyst merge في agent workflows.</p>
      <p>القدرات الأساسية: Arabic data agents; NL to SQL with explain; Forecasts and anomalies; Slack delivery; RLS aware; Multi-agent teams.</p>
      <p>للمبدعين العرب: analytics boutiques — «Cortex Agents 4 Arabic data brain in 9 days» لل orgs on Snowflake. من يُ ship 10 brains/ربع بـ 2100–58000 دولار + ops 160–1300 دولار/شهر يبني «استوديو Snowflake AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة brain (agents، semantic models، governance، training):</strong> 5–16 يومًا — 2100–58000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ models وseasonal dashboards:</strong> — 160–1300 دولار/شهر.</li>
          <li><strong>Industry semantic packs (e-commerce، banking، logistics RTL):</strong> — 58–265 دولار/pack.</li>
          <li><strong>دورات «وكلاء بيانات بـ Snowflake Cortex بالعربية»:</strong> — 46–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Cortex</span>
        <span class="tag">Data Agents</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="26-10-2026 -- 12-AM.html">
          📰 26 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "26-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/26-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/25-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/26-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
