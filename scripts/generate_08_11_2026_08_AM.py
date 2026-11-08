#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "08-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "SAP Joule 3 Arabic · Palantir AIP 4 Arabic · "
    "Cisco AI Defense 2 Arabic · Airtable Cobuilder 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — SAP Joule 3 Arabic، Palantir AIP 4 Arabic، Cisco AI Defense 2 Arabic، Airtable Cobuilder 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌅 نشرة AI العالمية</span>
      <h1>من SAP Joule 3 Arabic الذي يُحوّل ERP صامتًا إلى محادثة finance وsupply بلهجة ops عربية قبل اجتماع الميزانية، إلى Palantir AIP 4 Arabic الذي يُربط قرارات القيادة ببيانات حية ويُ draft scenarios RTL، ومن Cisco AI Defense 2 Arabic الذي يُ hunt تهديدات models وprompts قبل أن تُخترق شبكتك، إلى Airtable Cobuilder 2 Arabic الذي يُ launch base عمليات كاملة من وصف عربي في ساعات — أربع قصص صباحية في 8 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء بداية اليوم!</h1>
      <p class="hero-sub">صباحٌ لفرق ERP وdefense وinternal ops: تقارير تتأخر، قرارات بلا سياق، نماذج AI تُستغل دون رادار، ولوحات تُبنى أسابيعًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 8 نوفمبر 2026</span>
        <span>🌄 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>SAP Joule 3 Arabic: ERP يُجيب — finance، procurement، وHR بلسان المؤسسة!</h2>
      <p class="article-lead">«أين variance الميزانية لفرع جدة؟ — وستة تقارير وثلاثة exports». في 8 نوفمبر 2026، أطلقت <strong>SAP</strong> <strong>Joule 3 Arabic</strong>: copilot موحّد عبر S/4HANA وSuccessFactors وAriba يُ parse أسئلة CFO وcontroller وbuyer بالفصحى واللهجات المختارة، يُ explain PO delays وGL postings، يُ draft approval narratives RTL، يُ suggest cost optimizations مع audit trail، يُ integrate Microsoft Teams وSAP Build، يُ enforce SoD وdata masking — لل manufacturing وretail وutilities وpublic sector في MENA.</p>
      <p>المشكلة التي حلّتها: Joule 2 كان يُ confuse Arabic vendor names وSKU mix؛ الإصدار 3 يُ entity resolution محسّن، يُ benchmark −44% وقت «سؤال → journal insight» في conglomerate سعودي، يُ agent workflows لـ month-end close، يُ partner packs في الرياض ودبي والقاهرة، ويُ certification لـ SAP consultancies.</p>
      <p>القدرات الأساسية: Natural language إلى Fiori actions؛ anomaly alerts لل boards؛ Arabic chart narratives؛ sandbox لل CFO workshops؛ migration assistant من ECC notes.</p>
      <p>للمبدعين العرب: ERP boutiques — «Joule 3 Arabic finance cockpit in 16 days» لل orgs على S/4 5k+ users. من يُ deliver 5 rollouts/ربع بـ 5200–92000 دولار + managed 340–2900 دولار/شهر يبني «استوديو SAP AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من SAP Joule 3 Arabic؟</h3>
        <ul>
          <li><strong>Joule rollout (roles، SoD، Arabic glossary، UAT):</strong> 12–28 يومًا — 5200–92000 دولار/عميل.</li>
          <li><strong>Monthly close automation وadoption reviews:</strong> — 340–2900 دولار/شهر.</li>
          <li><strong>Vertical kits (oil &amp; gas، pharma GxP، government budget):</strong> — 55–245 دولار/حزمة.</li>
          <li><strong>دورات «ERP ذكي بـ SAP Joule بالعربية»:</strong> — 58–268 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">SAP</span>
        <span class="tag">ERP</span>
        <span class="tag">Finance</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Palantir AIP 4 Arabic: قرارات القيادة — ontologies، agents، وscenarios بلسان strategy!</h2>
      <p class="article-lead">«اللوحة خضراء — والواقع على الأرض مختلف». في 8 نوفمبر 2026، أطلقت <strong>Palantir</strong> <strong>AIP 4 Arabic</strong>: منصة decision intelligence تُ connect ERP وIoT وCRM وOSINT، تُ answer «ما تأثير إغلاق الميناء على SLAs؟» بالعربية مع provenance، تُ simulate policy options RTL، تُ orchestrate agents على workflows حساسة، تُ draft executive briefs لل boards، تُ integrate Foundry وGotham pipelines، يُ respect classification وair-gapped deploy — لل defense وenergy وlogistics وbanking في MENA.</p>
      <p>المشكلة التي حلّتها: AIP 3 كان يُ struggle مع Arabic geospatial labels؛ الإصدار 4 يُ MENA map pack، يُ benchmark −36% وقت «question → actionable decision» في port operator إماراتي، يُ eval harness لل agents، يُ on-prem GPU options، ويُ partner enablement في Abu Dhabi وAmman.</p>
      <p>القدرات الأساسية: Bilingual ontologies؛ agent guardrails؛ scenario compare؛ audit-grade lineage؛ mobile commander digest بالعربية.</p>
      <p>للمبدعين العرب: decision labs — «AIP 4 Arabic command center in 21 days» لل programs classified وcommercial. من يُ ship 4 centers/ربع بـ 12000–180000 دولار + retainer 450–3800 دولار/شهر يبني «مختبر قرارات Palantir عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Palantir AIP 4 Arabic؟</h3>
        <ul>
          <li><strong>AIP deployment (ontology، pipelines، Arabic UX، red-team):</strong> 18–45 يومًا — 12000–180000 دولار/عميل.</li>
          <li><strong>Monthly scenario drills وagent tuning:</strong> — 450–3800 دولار/شهر.</li>
          <li><strong>Industry accelerators (ports، grid، fraud fusion):</strong> — 85–420 دولار/حزمة.</li>
          <li><strong>دورات «Decision AI مع AIP بالعربية»:</strong> — 95–385 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Palantir</span>
        <span class="tag">AIP</span>
        <span class="tag">Decision</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Cisco AI Defense 2 Arabic: أمان النماذج — posture، policies، وthreat intel بلسان SOC!</h2>
      <p class="article-lead">«الـ chatbot داخل الشبكة — ولا أحد يعرف ماذا يُرسل للـ API». في 8 نوفمبر 2026، أطلقت <strong>Cisco</strong> <strong>AI Defense 2 Arabic</strong>: طبقة حماية عبر Secure Access وHypershield وDuo تُ discover shadow AI apps، تُ block prompt injection وdata exfiltration، تُ classify sensitive Arabic PII في prompts، تُ policy packs لـ GCC residency، تُ integrate Splunk وMicrosoft Sentinel، تُ red-team reports RTL لل CISO، يُ benchmark −52% unauthorized model calls في bank خليجي — لل enterprises وtelco وgov في MENA.</p>
      <p>المشكلة التي حلّتها: AI Defense 1 كان alerts إنجليزية فقط؛ الإصدار 2 يُ Arabic incident summaries، يُ model inventory مع risk scores، يُ automated quarantine، يُ partner MSSP program في Dubai وRiyadh، ويُ compliance mapping لـ NCA وPDPL.</p>
      <p>القدرات الأساسية: Shadow AI discovery؛ inline guardrails؛ Arabic PII detection؛ SOC playbooks؛ executive dashboards؛ air-gap policy sync.</p>
      <p>للمبدعين العرب: MSSPs — «AI Defense 2 Arabic zero-trust lane in 9 days» لل orgs 2k–80k seats. من يُ deploy 7 lanes/ربع بـ 3800–68000 دولار + SOC retainer 280–2400 دولار/شهر يبني «مركز أمان AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cisco AI Defense 2 Arabic؟</h3>
        <ul>
          <li><strong>Defense rollout (discovery، policies، Arabic runbooks، purple-team):</strong> 7–20 يومًا — 3800–68000 دولار/عميل.</li>
          <li><strong>Monthly threat reviews وpolicy updates:</strong> — 280–2400 دولار/شهر.</li>
          <li><strong>Vertical kits (banking، healthcare، smart city OT):</strong> — 48–215 دولار/حزمة.</li>
          <li><strong>دورات «Securing GenAI مع Cisco بالعربية»:</strong> — 52–228 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cisco</span>
        <span class="tag">Security</span>
        <span class="tag">GenAI</span>
        <span class="tag">SOC</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Airtable Cobuilder 2 Arabic: ops بدقائق — bases، automations، وportals من prompt عربي!</h2>
      <p class="article-lead">«نحتاج tracker للعقود — والـ IT مشغول شهرين». في 8 نوفمبر 2026، أطلقت <strong>Airtable</strong> <strong>Cobuilder 2 Arabic</strong>: مساعد يُ parse وصف workflow بالفصحى واللهجات، يُ generate tables وviews وforms RTL، يُ wire automations إلى Slack وGmail وSalesforce، يُ suggest formulas وrollups، يُ publish interfaces للعملاء الداخليين، يُ permission templates وaudit logs، يُ benchmark −58% وقت «idea → live base» في proptech دبي — لل ops وHR وlegal وPMO في MENA.</p>
      <p>المشكلة التي حلّتها: Cobuilder 1 كان يُ break على Arabic field names؛ الإصدار 2 يُ Unicode-safe schema، يُ multimodal import من PDF وWhatsApp exports، يُ AI field types لل classification عربي، يُ enterprise SSO، ويُ solution marketplace MENA.</p>
      <p>القدرات الأساسية: Prompt-to-base؛ bilingual interfaces؛ automation debugger؛ sync packs؛ mobile approvals بالعربية.</p>
      <p>للمبدعين العرب: no-code studios — «Cobuilder 2 Arabic ops kit in 5 days» لل teams 20–2000 seats. من يُ sell 10 kits/ربع بـ 1800–42000 دولار + tuning 190–1650 دولار/شهر يبني «استوديو Airtable AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable Cobuilder 2 Arabic؟</h3>
        <ul>
          <li><strong>Cobuilder setup (schema، automations، Arabic UI، training):</strong> 3–12 يومًا — 1800–42000 دولار/عميل.</li>
          <li><strong>Monthly workflow tuning وnew interfaces:</strong> — 190–1650 دولار/شهر.</li>
          <li><strong>Function packs (procurement، recruiting، franchise ops):</strong> — 42–198 دولار/حزمة.</li>
          <li><strong>دورات «بناء ops بـ Airtable Cobuilder بالعربية»:</strong> — 46–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">No-code</span>
        <span class="tag">Ops</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="08-11-2026 -- 08-AM.html">
          📰 8 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "08-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/08-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/08-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
