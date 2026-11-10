#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 10-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "10-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "GitLab Duo Enterprise 3 Arabic · Coupa Navi AI 2 Arabic · "
    "Procore Copilot 3 Arabic · Informatica CLAIRE GPT 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — GitLab Duo Enterprise 3 Arabic، Coupa Navi AI 2 Arabic، Procore Copilot 3 Arabic، Informatica CLAIRE GPT 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 10 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من GitLab Duo Enterprise 3 Arabic الذي يُحوّل merge request فوضويًا إلى review وCI green قبل أن يُنهي المطور فنجان الشاي الليلي، إلى Coupa Navi AI 2 Arabic الذي يُجيب CFO «لماذا تجاوزنا الميزانية؟» من بيانات المشتريات، ومن Procore Copilot 3 Arabic الذي يُترجم مخططات الموقع وRFIs إلى قرارات عربية للمقاولين، إلى Informatica CLAIRE GPT 3 Arabic الذي يُ map البيانات المتشتتة ويُ draft quality rules بلهجة data steward — أربع قصص ليلية في 10 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ لفرق الهندسة والمالية والبناء والبيانات: الـ MRs تتراكم، المشتريات تُفاجئ الإدارة، مواقع البناء تتأخر بسبب أوراق مفقودة، وMDM يغرق في metadata. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 10 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>GitLab Duo Enterprise 3 Arabic: DevSecOps مؤسسي — MR reviews، vulnerabilities، وpipelines بلسان الفريق!</h2>
      <p class="article-lead">«الـ MR عليه 38 تعليقًا — والـ release غدًا صباحًا». في 10 نوفمبر 2026، أطلقت <strong>GitLab</strong> <strong>Duo Enterprise 3 Arabic</strong>: suite AI داخل GitLab Ultimate يُ summarize diffs ويوضح المخاطر بالفصحى، يُ suggest fixes لل SAST وdependency alerts مع تبرير RTL، يُ author pipelines وCI snippets من issue description عربية، يُ chat عبر MRs وepics مع citations لـ code وdocs، يُ generate release notes وsecurity advisories، يُ respect self-managed وdedicated SaaS وVPC، يُ integrate Jira وSlack وServiceNow — لل banks وtelco وgov digital وproduct orgs في MENA.</p>
      <p>المشكلة التي حلّتها: Duo Agentic 2 كان يركز على tasks منفردة؛ الإصدار 3 يُ orchestrate multi-step workflows (review → fix branch → re-run pipeline) مع human approval gates، يُ benchmark −47% وقت «MR open → merged» في fintech خليجي 600 devs، يُ Arabic glossaries لـ domain terms، يُ partner bootcamps في الرياض ودبي والقاهرة، ويُ purple-team scenarios لل CISOs.</p>
      <p>القدرات الأساسية: Duo Chat enterprise-wide؛ AI-powered code suggestions مع policy packs؛ vulnerability explanation RTL؛ automated changelog من milestones؛ audit trail كامل لل prompts.</p>
      <p>للمبدعين العرب: DevOps consultancies — «Duo Enterprise 3 Arabic delivery pipeline in 10 days» لل orgs 80–3000 repos. من يُ deploy 5 rollouts/ربع بـ 4200–78000 دولار + retainer 310–2650 دولار/شهر يبني «مكتب GitLab AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitLab Duo Enterprise 3 Arabic؟</h3>
        <ul>
          <li><strong>Enterprise Duo rollout (policies، Arabic KB، MR templates، security tuning):</strong> 8–22 يومًا — 4200–78000 دولار/عميل.</li>
          <li><strong>Monthly pipeline hygiene وvulnerability coaching:</strong> — 310–2650 دولار/شهر.</li>
          <li><strong>Vertical kits (regulated cloud، mobile banking، IoT firmware):</strong> — 58–265 دولار/حزمة.</li>
          <li><strong>دورات «DevSecOps ذكي بـ GitLab Duo بالعربية»:</strong> — 55–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitLab</span>
        <span class="tag">Duo</span>
        <span class="tag">DevSecOps</span>
        <span class="tag">CI/CD</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Coupa Navi AI 2 Arabic: مشتريات ذكية — spend، suppliers، وbudget guardrails بلسان المالية!</h2>
      <p class="article-lead">«طلب شراء عاجل — ولا أحد يعرف إن كان ضمن العقد الإطاري». في 10 نوفمبر 2026، أطلقت <strong>Coupa</strong> <strong>Navi AI 2 Arabic</strong>: copilot فوق Business Spend Management يُ answer أسئلة procurement بالفصحى، يُ explain variances «لماذا ارتفع spend على IT Q3؟»، يُ recommend suppliers من historical performance، يُ draft RFP sections وevaluation criteria RTL، يُ flag maverick spend وcontract expiries، يُ orchestrate approval chains مع escalation hints، يُ integrate SAP وOracle وNetSuite feeds، يُ export board-ready briefs — لل enterprises وholding groups وgov procurement في MENA.</p>
      <p>المشكلة التي حلّتها: Navi 1 كان summaries إنجليزية فقط؛ الإصدار 2 يُ Arabic narrative لل CFOs، يُ benchmark −42% cycle time لـ PR-to-PO في conglomerate إماراتي، يُ playbook libraries لـ direct وindirect categories، يُ partner certification في المنطقة، ويُ compliance pack لـ anti-corruption policies.</p>
      <p>القدرات الأساسية: Natural language spend analytics؛ supplier risk summaries؛ contract clause Q&amp;A؛ mobile voice queries؛ sandbox لل procurement academies.</p>
      <p>للمبدعين العرب: procurement boutiques — «Navi AI 2 Arabic spend cockpit in 9 days» لل orgs 200–40000 POs/سنة. من يُ roll 6 cockpits/ربع بـ 3600–68000 دولار + managed 280–2300 دولار/شهر يبني «غرفة Coupa AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Coupa Navi AI 2 Arabic؟</h3>
        <ul>
          <li><strong>Navi enablement (taxonomy، Arabic approvals، supplier data، UAT):</strong> 7–18 يومًا — 3600–68000 دولار/عميل.</li>
          <li><strong>Monthly spend reviews وcategory coaching:</strong> — 280–2300 دولار/شهر.</li>
          <li><strong>Industry kits (construction، pharma، retail supply):</strong> — 52–235 دولار/حزمة.</li>
          <li><strong>دورات «مشتريات ذكية بـ Coupa Navi بالعربية»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Coupa</span>
        <span class="tag">Procurement</span>
        <span class="tag">Spend</span>
        <span class="tag">Finance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Procore Copilot 3 Arabic: بناء ذكي — RFIs، submittals، وsafety بلسان مهندس الموقع!</h2>
      <p class="article-lead">«RFI رقم 412 معلّق — والعميل يسأل عن التأخير على WhatsApp». في 10 نوفمبر 2026، أطلقت <strong>Procore</strong> <strong>Copilot 3 Arabic</strong>: مساعد فوق construction management يُ read drawings وspecs وdaily logs، يُ draft RFI responses وsubmittal coversheets بالفصحى، يُ summarize field issues وsafety observations، يُ predict schedule slips من weather وmaterial delays، يُ generate owner reports وprogress photos narratives RTL، يُ sync ERP وaccounting وBIM exports، يُ mobile voice على site مع offline cache — لل general contractors وdevelopers وinfrastructure في الخليج ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: Copilot 2 كان يُ confuse Arabic abbreviations في specs؛ الإصدار 3 يُ OCR عربي محسّن لل as-built، يُ benchmark −38% وقت «RFI assigned → answered» في megaproject سعودي، يُ bilingual owner portals، يُ partner enablement في قطاع construction MENA، ويُ template library لـ NEC وFIDIC workflows.</p>
      <p>القدرات الأساسية: NL search across project docs؛ automated meeting minutes من voice؛ cost impact hints؛ permit tracking reminders؛ integration Autodesk وBluebeam.</p>
      <p>للمبدعين العرب: construction tech integrators — «Copilot 3 Arabic field brain in 12 days» لل projects 5–80 active jobs. من يُ deliver 4 brains/ربع بـ 4800–72000 دولار + retainer 350–2850 دولار/شهر يبني «مكتب Procore AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Procore Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>Copilot rollout (templates، Arabic SOPs، training، integrations):</strong> 9–24 يومًا — 4800–72000 دولار/عميل.</li>
          <li><strong>Monthly RFI queues وsafety digest coaching:</strong> — 350–2850 دولار/شهر.</li>
          <li><strong>Vertical packs (hospitality، healthcare builds، renewables):</strong> — 62–285 دولار/حزمة.</li>
          <li><strong>دورات «إدارة مشاريع بناء ذكية بـ Procore بالعربية»:</strong> — 58–270 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Procore</span>
        <span class="tag">Construction</span>
        <span class="tag">Field Ops</span>
        <span class="tag">RFI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Informatica CLAIRE GPT 3 Arabic: حوكمة بيانات — lineage، quality، وMDM بلسان steward!</h2>
      <p class="article-lead">«أين مصدر حقل العميل arabic_name؟ — وثلاث أنظمة تُعارض بعضها». في 10 نوفمبر 2026، أطلقت <strong>Informatica</strong> <strong>CLAIRE GPT 3 Arabic</strong>: generative layer فوق Intelligent Data Management Cloud يُ answer data catalog questions بالفصحى، يُ explain lineage graphs «ماذا يحدث إذا غيّرنا هذا mapping؟»، يُ draft data quality rules وprofiling jobs، يُ suggest MDM match rules لل Arabic names وaddresses، يُ generate policy docs لل GDPR وsovereignty، يُ integrate Snowflake وDatabricks وSAP، يُ govern prompts مع PII masking — لل banks وinsurers وtelco وnational data offices في MENA.</p>
      <p>المشكلة التي حلّتها: CLAIRE GPT 2 كان يُ hallucinate connections؛ الإصدار 3 يُ grounded على catalog IDs فقط، يُ benchmark −41% وقت «steward question → approved rule» في insurer خليجي، يُ Arabic synonym dictionaries، يُ partner accelerators في الرياض ودبي، ويُ certification لـ system integrators.</p>
      <p>القدرات الأساسية: Chat في catalog UI؛ auto-documentation لل pipelines؛ bilingual glossary management؛ impact analysis reports RTL؛ API لل data marketplace.</p>
      <p>للمبدعين العرب: data governance firms — «CLAIRE GPT 3 Arabic stewardship hub in 11 days» لل domains 50–2000 assets. من يُ deploy 5 hubs/ربع بـ 3900–74000 دولار + retainer 300–2450 دولار/شهر يبني «مركز Informatica AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Informatica CLAIRE GPT 3 Arabic؟</h3>
        <ul>
          <li><strong>CLAIRE enablement (catalog، Arabic business glossary، DQ rules، training):</strong> 8–21 يومًا — 3900–74000 دولار/عميل.</li>
          <li><strong>Monthly lineage reviews وMDM tuning:</strong> — 300–2450 دولار/شهر.</li>
          <li><strong>Regulatory packs (banking BCBS، health HIPAA-style، telecom):</strong> — 55–258 دولار/حزمة.</li>
          <li><strong>دورات «حوكمة بيانات ذكية بـ Informatica بالعربية»:</strong> — 52–242 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Informatica</span>
        <span class="tag">CLAIRE</span>
        <span class="tag">Data Governance</span>
        <span class="tag">MDM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 10-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="10-11-2026 -- 12-AM.html">
          📰 10 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "10-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/10-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/10-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
    if "\u00fc" in text or "yü" in text:
        raise SystemExit("ERROR: Latin ü found — use Arabic يُ")
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
