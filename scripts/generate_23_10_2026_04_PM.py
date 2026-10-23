#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "23-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Airtable Omni 4 Arabic · Pipedrive AI Sales Assistant 4 Arabic · "
    "Tableau Pulse AI 4 Arabic · QuickBooks AI Bookkeeper 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Airtable Omni 4 Arabic، Pipedrive AI Sales Assistant 4 Arabic، Tableau Pulse AI 4 Arabic، QuickBooks AI Bookkeeper 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Airtable Omni 4 Arabic الذي يُحوّل جدول فوضوي إلى تطبيق تشغيلي وportals للعملاء من جملة عربية واحدة، إلى Pipedrive AI Sales Assistant 4 Arabic الذي يُ draft متابعات ويُ priority الصفقات الحارة قبل أن يُطفأ مكتب المبيعات، ومن Tableau Pulse AI 4 Arabic الذي يُ explain لماذا تراجع KPI أمس ويُ push insights للمدير على Slack، إلى QuickBooks AI Bookkeeper 4 Arabic الذي يُ reconcile فواتير MENA ويُ narrate cashflow للـ CFO بالعربية — أربع قصص مسائية في 23 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُشتعل مع الغروب!</h1>
      <p class="hero-sub">مساءٌ للعمليات والمبيعات والتحليل والمالية: فرق ops تغرق في spreadsheets، reps يكتبون نفس email مئة مرة، analysts ينتظرون BI، والمحاسبة تطارد فواتير PDF. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 23 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Airtable Omni 4 Arabic: من base إلى app — workflows، portals، وautomations بprompt واحد!</h2>
      <p class="article-lead">«عندنا 47 جدولًا — ولا أحد يعرف أين آخر نسخة العقد». في 23 أكتوبر 2026، أطلقت <strong>Airtable</strong> <strong>Omni 4 Arabic</strong>: copilot فوق bases يُ parse schemas وrelations، يُ generate interfaces RTL للفرق والعملاء، يُ build automations (Slack، email، webhooks)، يُ draft forms وsurveys باللهجة (MSA، Gulf، Egyptian)، يُ suggest field types وvalidations، يُ sync CRM وERP connectors، ويُ governance roles وaudit — لل agencies وlogistics وevents وNGOs في MENA.</p>
      <p>المشكلة التي حلّتها: Omni 2 كان يُ break linked records في Arabic labels؛ الإصدار 4 يُ unicode-safe keys، يُ benchmark −52% time-to-app في events company إماراتية، يُ natural language queries على millions rows، يُ template marketplace (CRM، inventory، hiring RTL)، يُ mobile-first portals، ويُ export to React optional لل dev handoff.</p>
      <p>القدرات الأساسية: Arabic ops copilot; App and portal generation; Automations and integrations; NL queries; Template marketplace; Mobile portals.</p>
      <p>للمبدعين العرب: no-code studios — «Omni 4 Arabic ops app in 6 days» لل teams 10–400 users. من يُ ship 14 apps/ربع بـ 1400–42000 دولار + care 120–920 دولار/شهر يبني «مصنع Airtable AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Airtable Omni 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة app (discovery، schema، Omni build، training، go-live):</strong> 5–12 يومًا — 1400–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ automations وdata hygiene:</strong> — 120–920 دولار/شهر.</li>
          <li><strong>Vertical kits (agencies، warehouses، schools RTL):</strong> — 48–220 دولار/kit.</li>
          <li><strong>دورات «تطبيقات تشغيل بـ Airtable Omni بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Airtable</span>
        <span class="tag">Omni</span>
        <span class="tag">No-code</span>
        <span class="tag">Ops</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Pipedrive AI Sales Assistant 4 Arabic: صفقات أذكى — emails، scoring، وnext-best-action!</h2>
      <p class="article-lead">«120 deal مفتوح — والمدير يسأل: ماذا نُغلق هذا الأسبوع؟». في 23 أكتوبر 2026، أطلقت <strong>Pipedrive</strong> <strong>AI Sales Assistant 4 Arabic</strong>: assistant داخل pipeline يُ draft follow-ups MSA/Gulf/Egyptian، يُ score deals من activity وemail sentiment، يُ suggest next-best-action وmeeting agendas، يُ summarize calls (مع Gong/Zoom integrations)، يُ enrich leads من LinkedIn وClearbit، يُ forecast revenue scenarios، ويُ coach reps على objection handling — لل SMB وmid-market B2B في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Assistant 3 كان يُ sound generic في Arabic closings؛ الإصدار 4 يُ tone profiles per brand، يُ benchmark +29% win-rate في SaaS startup سعودية، يُ WhatsApp thread ingest optional، يُ pipeline hygiene alerts، يُ manager digest RTL يومي، ويُ GDPR-ready data scopes.</p>
      <p>القدرات الأساسية: Arabic sales copilot; Deal scoring and forecast; Email and agenda drafts; Call summaries; Lead enrichment; Manager digests.</p>
      <p>للمبدعين العرب: RevOps freelancers — «Pipedrive AI 4 Arabic revenue desk in 5 days» لل teams 3–80 reps. من يُ deploy 12 desks/ربع بـ 1100–22000 دولار + tuning 95–780 دولار/شهر يبني «مكتب مبيعات AI عربي على Pipedrive».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Pipedrive AI Sales Assistant 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة desk (audit، pipeline، AI rules، playbooks، training):</strong> 4–10 أيام — 1100–22000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ sequences وforecast tuning:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Industry playbooks (real estate، IT services، clinics RTL):</strong> — 35–165 دولار/playbook.</li>
          <li><strong>دورات «مبيعات ذكية بـ Pipedrive AI بالعربية»:</strong> — 38–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Pipedrive</span>
        <span class="tag">Sales AI</span>
        <span class="tag">CRM</span>
        <span class="tag">RevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Tableau Pulse AI 4 Arabic: KPIs تُ speak — insights، anomalies، وSlack briefs للمدير!</h2>
      <p class="article-lead">«ال dashboard فيه 200 chart — ولا CFO يفهم لماذا هبط margin». في 23 أكتوبر 2026، أطلقت <strong>Salesforce</strong> <strong>Tableau Pulse AI 4 Arabic</strong>: layer فوق Tableau Cloud يُ monitor metrics المعرّفة، يُ generate narrative insights بالعربية (MSA formal أو Gulf executive tone)، يُ detect anomalies وseasonality، يُ push digests إلى Slack وTeams وemail، يُ answer follow-up questions grounded في data، يُ suggest actions (pricing، inventory، headcount)، ويُ embed في Salesforce CRM لل reps — لل retail وF&amp;B وtelco في MENA.</p>
      <p>المشكلة التي حلّتها: Pulse 2 كان يُ mistranslate currency labels؛ الإصدار 4 يُ locale SAR/AED/EGP، يُ benchmark −38% time-to-insight في grocery chain مصرية، يُ metric certification workflows، يُ mobile Pulse cards RTL، يُ export board-ready PDF summaries، ويُ row-level security preserved.</p>
      <p>القدرات الأساسية: Arabic metric narratives; Anomaly detection; Slack and Teams digests; Conversational follow-ups; Action suggestions; CRM embed.</p>
      <p>للمبدعين العرب: BI boutiques — «Tableau Pulse AI 4 Arabic executive layer in 8 days» لل orgs 50–5000 seats. من يُ launch 8 pulses/ربع بـ 2600–48000 دولار + retainer 180–1350 دولار/شهر يبني «غرفة Pulse عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Tableau Pulse AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة Pulse (metrics design، narratives، alerts، exec training):</strong> 6–14 يومًا — 2600–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ metric tuning وstory refresh:</strong> — 180–1350 دولار/شهر.</li>
          <li><strong>Sector metric packs (retail، logistics، healthcare RTL):</strong> — 55–250 دولار/pack.</li>
          <li><strong>دورات «قصص بيانات بـ Tableau Pulse بالعربية»:</strong> — 52–240 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Tableau</span>
        <span class="tag">Pulse AI</span>
        <span class="tag">BI</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>QuickBooks AI Bookkeeper 4 Arabic: محاسبة تُ narrate نفسها — reconcile، VAT، وcashflow!</h2>
      <p class="article-lead">«300 فاتورة PDF — والـ VAT return بعد 48 ساعة». في 23 أكتوبر 2026، أطلقت <strong>Intuit</strong> <strong>QuickBooks AI Bookkeeper 4 Arabic</strong>: copilot يُ ingest receipts وbank feeds، يُ categorize expenses MENA-aware، يُ reconcile mismatches ويُ flag duplicates، يُ draft VAT/GST reports للـ GCC ومصر، يُ explain cashflow وrunway لل founder بالعربية، يُ chase overdue invoices بemails polite بلهجة العميل، يُ sync Shopify وStripe وPayTabs، ويُ audit trail لل accountants — لل SMEs وaccounting firms في MENA.</p>
      <p>المشكلة التي حلّتها: Bookkeeper 3 كان يُ confuse Arabic vendor names؛ الإصدار 4 يُ entity resolution محسّن، يُ benchmark −44% month-close time في consultancy أردنية، يُ multi-currency hedging hints، يُ accountant collaboration mode، يُ ZATCA e-invoicing hooks، ويُ fraud pattern alerts.</p>
      <p>القدرات الأساسية: Arabic finance copilot; Auto-categorization; VAT and compliance drafts; Cashflow narratives; Invoice chasing; Accountant mode.</p>
      <p>للمبدعين العرب: accounting freelancers — «QuickBooks AI 4 Arabic month-close in 7 days» لل businesses 5–200 FTE. من يُ onboard 16 clients/ربع بـ 850–24000 دولار + bookkeeping care 75–620 دولار/شهر يبني «مكتب Bookkeeper AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من QuickBooks AI Bookkeeper 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة setup (chart، rules، Bookkeeper، VAT config، training):</strong> 4–11 يومًا — 850–24000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ reconcile وmonth-close:</strong> — 75–620 دولار/شهر.</li>
          <li><strong>Compliance packs (ZATCA، UAE VAT، Egypt e-invoice RTL):</strong> — 40–185 دولار/pack.</li>
          <li><strong>دورات «محاسبة ذكية بـ QuickBooks AI بالعربية»:</strong> — 32–150 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">QuickBooks</span>
        <span class="tag">Bookkeeper AI</span>
        <span class="tag">Finance</span>
        <span class="tag">SME</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="23-10-2026 -- 04-PM.html">
          📰 23 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "23-10-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/23-10-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/23-10-2026 -- 08-AM.html"
    new_line = (
        f"- [`{new}`](news/23-10-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS}) "
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
        "الإصrador",
        "يبni",
        " y\u0650u",
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
