#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 30-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "30-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Asana AI Teammates 2 Arabic، Ramp Intelligence 2 Arabic، Rippling Intelligence 2 Arabic، Gong Revenue AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 30 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Asana AI Teammates 2 Arabic الذي يُوزّع المهام ويُلخص المشاريع بأمر عربي داخل workspace، إلى Ramp Intelligence 2 Arabic الذي يُ audit المصروفات ويُ catch anomalies قبل نهاية الشهر، ومن Rippling Intelligence 2 Arabic الذي يُ automate HR وpayroll policies بلهجات MENA، إلى Gong Revenue AI 3 Arabic الذي يُ decode مكالمات المبيعات ويُ coach الفريق بالعربية — أربع قصص مسائية في 30 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء مسارك بعد الظهر!</h1>
      <p class="hero-sub">مساءٌ للفرق الطموحة: مديرو المشاريع يطلبون teammates ذكية تفهم «نبي التسليم بكرة»، CFOs يبحثون عن Ramp يُ explain spend بالعربية، HR leaders يريدون Rippling يُ answer policy questions فورًا، وقادة revenue يحلمون بـ Gong يُ highlight objections في calls خليجية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 30 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Asana AI Teammates 2 Arabic: زميل ذكي للمشاريع — توزيع مهام، ملخصات، ومتابعة RTL بلا اجتماعات طويلة!</h2>
      <p class="article-lead">«المشروع متأخر — ولا أحد يعرف من يمسك المهمة». في 30 سبتمبر 2026، أطلقت <strong>Asana</strong> <strong>AI Teammates 2 Arabic</strong>: وكلاء داخل Work Graph يُ parse briefs عربية، يُ suggest assignees حسب skills، يُ draft status updates RTL، يُ summarize threads طويلة، يُ nudge deadlines via Slack وTeams — لل agencies وproduct teams وconstruction PMOs في MENA.</p>
      <p>المشكلة التي حلّتها: Teammates 1 كان English-centric وweak على Arabic comments؛ الإصدار 2 يُ MSA وGulf tone packs، يُ read PDFs وWhatsApp exports، يُ custom rules «لا task بدون owner»، يُ benchmark −22% meeting hours في fintech إماراتي، يُ admin controls على data residency EU وGCC options.</p>
      <p>القدرات الأساسية: Goals linking؛ portfolio dashboards بالعربية؛ approval workflows؛ API hooks إلى Jira migration kits؛ templates لل Ramadan campaign sprints.</p>
      <p>للمبدعين العرب: ops consultancies وAsana partners — «Teammates 2 Arabic rollout in 9 days» لل orgs 50–5000 seats. من يُ deliver 7 workspaces/ربع بـ 2400–52000 دولار + coaching retainer 290–2700 دولار/شهر يركب «Arabic project velocity studio».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Asana AI Teammates 2 Arabic؟</h3>
        <ul>
          <li><strong>Teammates deployment (taxonomy، rules، Arabic UX، training):</strong> 6–18 يومًا — 2400–52000 دولار/عميل.</li>
          <li><strong>Monthly workflow reviews and adoption analytics:</strong> — 290–2700 دولار/شهر.</li>
          <li><strong>Vertical playbooks (agency، real estate، events):</strong> — 38–190 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Project Ops on Asana»:</strong> — 41–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Asana</span>
        <span class="tag">PMO</span>
        <span class="tag">Productivity</span>
        <span class="tag">Teams</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Ramp Intelligence 2 Arabic: CFO copilot — مصروفات، سياسات، وتنبيهات fraud بلغة finance عربية!</h2>
      <p class="article-lead">«الفاتورة غريبة — والمحاسب ينام». في 30 سبتمبر 2026، أطلقت <strong>Ramp</strong> <strong>Intelligence 2 Arabic</strong>: طبقة AI فوق corporate cards وbill pay تُ categorize spend RTL، تُ explain anomalies «لماذا زاد marketing 18%»، تُ draft policy reminders، تُ negotiate vendor insights، تُ sync QuickBooks وNetSuite — لل startups وscale-ups وholding groups في MENA.</p>
      <p>المشكلة التي حلّتها: Intelligence 1 كان reports إنجليزية؛ الإصدار 2 يُ Arabic natural language queries، يُ multi-entity consolidation، يُ VAT-aware tagging للخليج، يُ benchmark 31% faster month-close في ecommerce سعودي، يُ SOC2 وlocal audit exports.</p>
      <p>القدرات الأساسية: Slack bot بالعربية؛ receipt OCR للفواتير اليدوية؛ budget guardrails؛ delegated approvers؛ sandbox للCFO workshops.</p>
      <p>للمبدعين العرب: finance ops boutiques — «Ramp Intelligence 2 Arabic in 5 days» لل companies 20–800 cards. من يُ sell 9 implementations/ربع بـ 1800–44000 دولار + advisory 240–2200 دولار/شهر يركب «Arabic spend intelligence desk».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Ramp Intelligence 2 Arabic؟</h3>
        <ul>
          <li><strong>Ramp Intelligence setup (policies، integrations، Arabic reporting):</strong> 4–12 يومًا — 1800–44000 دولار/عميل.</li>
          <li><strong>Monthly close support and anomaly playbooks:</strong> — 240–2200 دولار/شهر.</li>
          <li><strong>Industry kits (SaaS، retail، logistics fleets):</strong> — 32–168 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Finance Ops with Ramp»:</strong> — 37–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Ramp</span>
        <span class="tag">Finance</span>
        <span class="tag">Spend</span>
        <span class="tag">CFO</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Rippling Intelligence 2 Arabic: HR وpayroll agent — onboarding، policies، وcompliance بمحادثة واحدة!</h2>
      <p class="article-lead">«الموظف الجديد يسأل عن الإجازة — وHR مشغول». في 30 سبتمبر 2026، أطلقت <strong>Rippling</strong> <strong>Intelligence 2 Arabic</strong>: مساعد unified workforce platform يُ answer HR FAQs dialect-aware، يُ generate offer letters RTL، يُ route IT provisioning، يُ flag compliance gaps (iqama، contracts، benefits)، يُ integrate devices وapps — لل multinationals وfast-growing SMEs في MENA.</p>
      <p>المشكلة التي حلّتها: Intelligence 1 كان US payroll focus؛ الإصدار 2 يُ GCC leave rules، يُ Arabic employee handbook RAG، يُ manager coaching snippets، يُ benchmark −35% HR ticket volume في tech hub مصري، يُ partner legal review packs.</p>
      <p>القدرات الأساسية: Employee app chat بالعربية؛ workflow builder no-code؛ analytics على attrition signals؛ SSO وpermission mirroring؛ migration from legacy HRIS documented.</p>
      <p>للمبدعين العرب: HR tech implementers — «Rippling Intelligence 2 Arabic go-live in 16 days» لل headcount 100–10000. من يُ deliver 5 rollouts/ربع بـ 5200–88000 دولار + support 380–3600 دولار/شهر يركب «Arabic unified HR AI practice».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Rippling Intelligence 2 Arabic؟</h3>
        <ul>
          <li><strong>Rippling Intelligence rollout (HRIS، policies، Arabic KB، UAT):</strong> 12–28 يومًا — 5200–88000 دولار/عميل.</li>
          <li><strong>Monthly policy updates and employee adoption:</strong> — 380–3600 دولار/شهر.</li>
          <li><strong>Country packs (UAE، KSA، Egypt payroll nuances):</strong> — 55–265 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Workforce AI on Rippling»:</strong> — 44–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Rippling</span>
        <span class="tag">HR</span>
        <span class="tag">Payroll</span>
        <span class="tag">Workforce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Gong Revenue AI 3 Arabic: decode مكالمات المبيعات — objections، coaching، وforecast من صوت عربي!</h2>
      <p class="article-lead">«الصفقة ضاعت — ولا أحد سجل سبب الاعتراض». في 30 سبتمبر 2026، أطلقت <strong>Gong</strong> <strong>Revenue AI 3 Arabic</strong>: conversation intelligence upgrade يُ transcribe Gulf وLevant calls، يُ highlight pricing objections، يُ suggest follow-up emails RTL، يُ score talk tracks، يُ sync Salesforce وHubSpot — لل B2B sales orgs وchannel partners في MENA.</p>
      <p>المشكلة التي حلّتها: Revenue AI 2 كان weak code-switching؛ الإصدار 3 يُ diarization للmulti-party Zoom، يُ deal risk alerts «competitor mentioned twice»، يُ Arabic coaching clips للmanagers، يُ benchmark +19% win rate في cybersecurity vendor خليجي، يُ privacy controls للrecordings.</p>
      <p>القدرات الأساسية: Playbooks بالعربية؛ forecast roll-ups؛ integration مع Microsoft Teams وGoogle Meet؛ anonymized benchmarks؛ mobile rep digest صباحي.</p>
      <p>للمبدعين العرب: sales enablement agencies — «Gong Revenue AI 3 Arabic in 10 days» لل teams 15–400 reps. من يُ sell 8 programs/ربع بـ 3400–72000 دولار + tuning 310–2900 دولار/شهر يركب «Arabic revenue intelligence lab».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gong Revenue AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Gong Revenue AI setup (CRM sync، playbooks، Arabic QA، manager training):</strong> 7–21 يومًا — 3400–72000 دولار/عميل.</li>
          <li><strong>Monthly deal review rituals and talk-track tuning:</strong> — 310–2900 دولار/شهر.</li>
          <li><strong>Vertical libraries (cyber، logistics SaaS، proptech):</strong> — 40–195 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Conversation Intelligence with Gong»:</strong> — 42–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gong</span>
        <span class="tag">Sales</span>
        <span class="tag">Revenue</span>
        <span class="tag">Coaching</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 30-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="30-09-2026 -- 04-PM.html">
          📰 30 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Asana AI Teammates 2 Arabic · Ramp Intelligence 2 Arabic · Rippling Intelligence 2 Arabic · Gong Revenue AI 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/30-09-2026 -- 04-PM.html`](news/30-09-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "30-09-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "30-09-2026 -- 04-PM.html" not in content:
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
