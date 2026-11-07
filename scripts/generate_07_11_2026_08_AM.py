#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 07-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "07-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Harvey Legal Copilot 3 Arabic · Deel AI Workforce 3 Arabic · "
    "Brex Empower AI 3 Arabic · Gusto AI Payroll 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Harvey Legal Copilot 3 Arabic، Deel AI Workforce 3 Arabic، Brex Empower AI 3 Arabic، Gusto AI Payroll 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 7 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌅 نشرة AI العالمية</span>
      <h1>من Harvey Legal Copilot 3 Arabic الذي يُحوّل عقدًا ضخمًا إلى ملخص risks وclauses بالعربية قبل أن يبرد فنجان القهوة، إلى Deel AI Workforce 3 Arabic الذي يُ orchestrate توظيفًا عابرًا للحدود وpayroll بلهجة HR محلية، ومن Brex Empower AI 3 Arabic الذي يُ catch مصروفات مشبوهة ويُ forecast cash بلسان CFO، إلى Gusto AI Payroll 3 Arabic الذي يُ reconcile رواتب SMB ويُ answer موظفين بالفصحى واللهجات — أربع قصص صباحية في 7 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء بداية اليوم!</h1>
      <p class="hero-sub">صباحٌ لفرق legal وHR وfinance وops: عقود تتراكم، payroll عابر للحدود يتعقّد، burn يهرب من التقارير، وموظفون يسألون «متى الراتب؟». أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 7 نوفمبر 2026</span>
        <span>🌄 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Harvey Legal Copilot 3 Arabic: محامٍ copilot — عقود، due diligence، وmemos بلسان legal عربي!</h2>
      <p class="article-lead">«مائة صفحة SPA — والصفقة تُغلق غدًا». في 7 نوفمبر 2026، أطلقت <strong>Harvey</strong> <strong>Legal Copilot 3 Arabic</strong>: copilot قانوني يُ ingest contracts وdata rooms وregulatory PDFs، يُ summarize clauses وflag risks بالفصحى واللهجات المختارة، يُ compare against playbooks وprecedents، يُ draft NDAs وamendments وboard memos RTL، يُ cite sources مع page anchors، يُ bilingual redlines EN↔AR، يُ privilege-aware vaults وSSO، يُ workflow approvals لل partners — لل law firms وin-house legal وM&amp;A وfintech في MENA.</p>
      <p>المشكلة التي حلّتها: Legal Copilot 2 كان يُ miss Arabic OCR في scanned exhibits؛ الإصدار 3 يُ enhanced Arabic legal NER، يُ benchmark −52% وقت first-pass review في مكتب دبي، يُ integration iManage وNetDocuments، يُ jurisdiction packs (UAE، KSA، Egypt)، يُ audit logs لـ regulators، ويُ partner certifications لل regional boutiques.</p>
      <p>القدرات الأساسية: Contract summarization; Risk flagging RTL; Precedent compare; Memo drafting; Bilingual redlines; Enterprise vaults.</p>
      <p>للمبدعين العرب: legal ops boutiques — «Harvey Legal Copilot 3 Arabic deal desk in 10 days» لل firms 5–120 lawyers. من يُ deploy 5 desks/ربع بـ 4200–78000 دولار + managed 280–2200 دولار/شهر يبني «مكتب Harvey AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Harvey Legal Copilot 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة legal AI (playbooks، migrations، training، pilot على صفقة حقيقية):</strong> 8–18 يومًا — 4200–78000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ template hygiene وmatter analytics:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Vertical packs (fintech، real estate، employment):</strong> — 65–290 دولار/pack.</li>
          <li><strong>دورات «عمليات قانونية بـ Harvey Legal Copilot بالعربية»:</strong> — 55–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Harvey</span>
        <span class="tag">Legal</span>
        <span class="tag">Contracts</span>
        <span class="tag">M&amp;A</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Deel AI Workforce 3 Arabic: توظيف عالمي — offers، compliance، وonboarding بأمر عربي!</h2>
      <p class="article-lead">«نُوظّف في 6 دول — وكل دولة له قواعد مختلفة». في 7 نوفمبر 2026، أطلقت <strong>Deel</strong> <strong>AI Workforce 3 Arabic</strong>: copilot فوق Employer of Record يُ answer policy questions بالعربية، يُ draft localized offer letters وcontracts RTL، يُ check visa وtax compliance per country، يُ orchestrate onboarding (equipment، accounts، training paths)، يُ detect misclassification risks، يُ payroll anomaly alerts، يُ manager dashboards لل headcount وcost، يُ integrate Slack وHRIS وaccounting — لل remote-first وscale-ups في MENA وعالميًا.</p>
      <p>المشكلة التي حلّتها: Workforce 2 كان tone رسمي جامد في employee comms؛ الإصدار 3 يُ MENA HR tone packs، يُ benchmark −41% وقت «hire to productive day» في startup الرياض، يُ contractor vs employee classifier، يُ bulk offboarding checklists، يُ API لل staffing agencies، ويُ reseller enablement في Cairo وCasablanca.</p>
      <p>القدرات الأساسية: Localized offers; Compliance Q&amp;A; Onboarding orchestration; Classification checks; Payroll insights; HRIS sync.</p>
      <p>للمبدعين العرب: global HR consultancies — «Deel AI Workforce 3 Arabic expansion kit in 7 days» لل orgs 20–2000 contractors. من يُ run 8 kits/ربع بـ 2400–45000 دولار + care 190–1450 دولار/شهر يبني «مركز Deel AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Deel AI Workforce 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة global hiring (entity mapping، templates، pilot country):</strong> 5–14 يومًا — 2400–45000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ compliance updates وemployee Q&amp;A tuning:</strong> — 190–1450 دولار/شهر.</li>
          <li><strong>Country starter kits (UAE، KSA، Egypt، Jordan):</strong> — 58–265 دولار/kit.</li>
          <li><strong>دورات «توظيف عالمي ذكي بـ Deel AI بالعربية»:</strong> — 42–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Deel</span>
        <span class="tag">EOR</span>
        <span class="tag">HR</span>
        <span class="tag">Remote</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Brex Empower AI 3 Arabic: مصروفات وtreasury — policy، fraud، وnarratives للإدارة!</h2>
      <p class="article-lead">«بطاقة موظف في دبي — ومصروف في مدينة لم يزرها». في 7 نوفمبر 2026، أطلقت <strong>Brex</strong> <strong>Empower AI 3 Arabic</strong>: copilot فوق corporate cards وtreasury يُ narrate spend trends بالعربية، يُ enforce policies وauto-decline outliers، يُ detect duplicate SaaS وunused seats، يُ draft month-end memos لل CFO RTL، يُ forecast runway scenarios، يُ suggest vendor negotiations، يُ connect NetSuite وQuickBooks وSAP، يُ mobile approvals مع context cards — لل startups وmid-market في MENA.</p>
      <p>المشكلة التي حلّتها: Empower 2 كان reports إنجليزية فقط؛ الإصدار 3 يُ Arabic exec summaries، يُ benchmark −36% وقت monthly close narrative في fintech أبوظبي، يُ multi-entity FX explanations، يُ per-diem packs لل travel Gulf، يُ Slack digest RTL، ويُ partner path لل accounting firms.</p>
      <p>القدرات الأساسية: Spend narration; Policy enforcement; SaaS waste detection; CFO memos RTL; Runway forecasts; ERP sync.</p>
      <p>للمبدعين العرب: fractional CFO shops — «Brex Empower AI 3 Arabic finance cockpit in 6 days» لل companies 15–500 cards. من يُ deliver 10 cockpits/ربع بـ 1600–32000 دولار + tuning 125–980 دولار/شهر يبني «استوديو Brex AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Brex Empower AI 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة spend AI (policy design، integrations، training، 30-day review):</strong> 4–12 يومًا — 1600–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ anomaly reviews وCFO narratives:</strong> — 125–980 دولار/شهر.</li>
          <li><strong>Industry playbooks (SaaS، logistics، agencies):</strong> — 48–210 دولار/playbook.</li>
          <li><strong>دورات «ذكاء مالي بـ Brex Empower بالعربية»:</strong> — 38–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Brex</span>
        <span class="tag">Finance</span>
        <span class="tag">Spend</span>
        <span class="tag">Treasury</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Gusto AI Payroll 3 Arabic: رواتب SMB — runs، tax، وموظف يسأل copilot!</h2>
      <p class="article-lead">«يوم 28 — وثلاثة موظفين يسألون عن خصومات مختلفة». في 7 نوفمبر 2026، أطلقت <strong>Gusto</strong> <strong>AI Payroll 3 Arabic</strong>: copilot payroll للشركات الصغيرة يُ answer employee FAQs بالفصحى واللهجات، يُ preview payroll runs وflag errors، يُ explain tax وbenefits deductions، يُ draft HR notices RTL، يُ automate PTO accruals وovertime rules، يُ sync time tracking وaccounting، يُ year-end W-2 وlocal equivalent guidance، يُ manager digest لل labor cost — لل SMB وrestaurants وclinics في diaspora وMENA affiliates.</p>
      <p>المشكلة التي حلّتها: Payroll 2 كان يُ struggle مع bilingual pay stubs؛ الإصدار 3 يُ RTL payslip layout، يُ benchmark −44% payroll support tickets في clinic أردني، يُ contractor vs W-2 hints، يُ state compliance nudges US، يُ Arabic help center generation، ويُ accountant partner tier.</p>
      <p>القدرات الأساسية: Employee FAQ bot; Payroll previews; Deduction explainers; HR notices RTL; PTO automation; Accountant sync.</p>
      <p>للمبدعين العرب: bookkeeping agencies — «Gusto AI Payroll 3 Arabic SMB stack in 5 days» لل clients 5–120 employees. من يُ onboard 15 stacks/ربع بـ 900–16500 دولار + support 75–620 دولار/شهر يبني «خط Gusto AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gusto AI Payroll 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة payroll AI (migration، rules، employee comms، first run supervised):</strong> 3–10 أيام — 900–16500 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ FAQ tuning وcompliance nudges:</strong> — 75–620 دولار/شهر.</li>
          <li><strong>Vertical kits (restaurants، clinics، agencies):</strong> — 35–155 دولار/kit.</li>
          <li><strong>دورات «رواتب ذكية بـ Gusto AI بالعربية»:</strong> — 32–148 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gusto</span>
        <span class="tag">Payroll</span>
        <span class="tag">SMB</span>
        <span class="tag">HR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 07-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="07-11-2026 -- 08-AM.html">
          📰 7 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "07-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/07-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/07-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
