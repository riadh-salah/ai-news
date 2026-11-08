#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "08-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Genesys AI Studio 3 Arabic · Nutanix GPT Advisor 2 Arabic · "
    "Bill.com FinAgent 2 Arabic · Linear AI Projects 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Genesys AI Studio 3 Arabic، Nutanix GPT Advisor 2 Arabic، Bill.com FinAgent 2 Arabic، Linear AI Projects 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Genesys AI Studio 3 Arabic الذي يُحوّل «أريد وكيلًا يُجيب WhatsApp بالخليجية ويُرفع للبشر عند الغضب» إلى journey تعمل قبل غروب الشمس، إلى Nutanix GPT Advisor 2 Arabic الذي يُشرح لماذا cluster على وشك الانهيار ويُ draft runbook RTL وأنت في المترو، ومن Bill.com FinAgent 2 Arabic الذي يُ reconcile فواتير MENA ويُ narrate cashflow للـ CFO بجملة عربية واحدة، إلى Linear AI Projects 3 Arabic الذي يُ priority issues ويُ draft specs ويُ sync مع Slack قبل أن تُغلق اللابتوب — أربع قصص مسائية في 8 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء نهاية اليوم!</h1>
      <p class="hero-sub">مساءٌ لفرق CX وinfra وfinance وproduct: مراكز الاتصال تغرق في قنوات متشعبة، ops يطارد capacity غامضة، المحاسبة تتراكم والـ CFO يريد إجابة الآن، والـ backlog يبتلع الأولويات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 8 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Genesys AI Studio 3 Arabic: استوديو وكلاء CX — bots، voice، وجولات omnichannel بلسان عميلك!</h2>
      <p class="article-lead">«العميل يراسلنا على إنستغرام وواتساب والهاتف — وثلاثة أنظمة لا تتكلم». في 8 نوفمبر 2026، أطلقت <strong>Genesys</strong> <strong>AI Studio 3 Arabic</strong>: بيئة low-code لبناء agents تُ ingest policies وorder data وKB بالعربية، تُ reply بالفصحى أو لهجات (Gulf، Egyptian، Levantine)، تُ orchestrate voice وchat وemail وsocial في journey واحد، تُ handoff للـ human مع ملخص sentiment RTL، تُ integrate Salesforce وServiceNow وShopify، تُ analytics على containment وCSAT وrevenue recovery، تُ respect data residency وPCI — لل banks وretail وtelco وhealthcare في MENA.</p>
      <p>المشكلة التي حلّتها: Studio 2 كان يُ struggle مع code-switching في المحادثات؛ الإصدار 3 يُ dialect routing محسّن، يُ benchmark −47% وقت «brief → live agent» في contact center خليجي 1200 seats، يُ prompt sandbox لل QA، يُ partner certification في الرياض ودبي وعمّان، ويُ crisis playbook templates لل viral mentions.</p>
      <p>القدرات الأساسية: Visual flow builder RTL؛ knowledge sync من SharePoint؛ real-time translation EN↔AR؛ supervisor copilot؛ A/B على opening messages؛ export transcripts لل compliance.</p>
      <p>للمبدعين العرب: CX agencies — «AI Studio 3 Arabic journey launch in 8 days» لل orgs 50–5000 agents. من يُ deliver 6 launches/ربع بـ 4200–78000 دولار + managed 320–2700 دولار/شهر يبني «استوديو Genesys AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Genesys AI Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>Studio rollout (flows، KB، dialect tuning، UAT):</strong> 10–22 يومًا — 4200–78000 دولار/عميل.</li>
          <li><strong>Monthly containment tuning وcrisis drills:</strong> — 320–2700 دولار/شهر.</li>
          <li><strong>Vertical kits (banking KYC، ecommerce returns، telco billing):</strong> — 52–238 دولار/حزمة.</li>
          <li><strong>دورات «بناء وكلاء CX بـ Genesys AI Studio بالعربية»:</strong> — 55–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Genesys</span>
        <span class="tag">CX</span>
        <span class="tag">Contact Center</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Nutanix GPT Advisor 2 Arabic: infra copilot — capacity، incidents، وcost بلسان platform ops!</h2>
      <p class="article-lead">«الـ cluster أصفر — والمدير يسأل: هل نشتري nodes أم نُحسّن؟». في 8 نوفمبر 2026، أطلقت <strong>Nutanix</strong> <strong>GPT Advisor 2 Arabic</strong>: مساعد فوق NC2 وPrism يُ answer أسئلة SRE وplatform بالفصحى، يُ explain utilization spikes وnoisy neighbors، يُ suggest rightsizing وVM moves، يُ draft incident timelines RTL، يُ correlate alerts من Prometheus وvCenter، يُ estimate TCO scenarios، يُ integrate ServiceNow وPagerDuty، يُ on-prem أو hybrid GPU-aware — لل enterprises وcloud providers وgov DC في MENA.</p>
      <p>المشكلة التي حلّتها: Advisor 1 كان إنجليزيًا فقط؛ الإصدار 2 يُ Arabic runbooks وpostmortems، يُ benchmark −41% MTTR في telco إماراتي، يُ policy guard لـ admin actions، يُ partner enablement في Dubai وRiyadh، ويُ certification لـ MSPs.</p>
      <p>القدرات الأساسية: NL capacity planning؛ automated KB updates؛ chat في Prism UI؛ API لل Slack alerts؛ air-gapped mode لل classified workloads.</p>
      <p>للمبدعين العرب: infra MSPs — «GPT Advisor 2 Arabic ops brain in 7 days» لل clusters 50–5000 VMs. من يُ deploy 5 brains/ربع بـ 3600–65000 دولار + retainer 270–2200 دولار/شهر يبني «مكتب Nutanix AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Nutanix GPT Advisor 2 Arabic؟</h3>
        <ul>
          <li><strong>Advisor enablement (connectors، Arabic KB، playbooks، purple-team):</strong> 6–18 يومًا — 3600–65000 دولار/عميل.</li>
          <li><strong>Monthly capacity reviews وincident coaching:</strong> — 270–2200 دولار/شهر.</li>
          <li><strong>Vertical packs (VDI، databases، AI inference nodes):</strong> — 48–210 دولار/حزمة.</li>
          <li><strong>دورات «platform ops ذكي بـ Nutanix GPT Advisor بالعربية»:</strong> — 50–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Nutanix</span>
        <span class="tag">Infrastructure</span>
        <span class="tag">SRE</span>
        <span class="tag">Hybrid Cloud</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Bill.com FinAgent 2 Arabic: محاسبة وكيلية — AP، AR، وcashflow بلسان finance team!</h2>
      <p class="article-lead">«مئات الفواتير PDF عربية وإنجليزية — والإقفال بعد 48 ساعة». في 8 نوفمبر 2026، أطلقت <strong>Bill.com</strong> <strong>FinAgent 2 Arabic</strong>: agent فوق AP/AR يُ ingest invoices وreceipts وbank feeds، يُ extract vendors وamounts وVAT بنية MENA، يُ match POs وflag duplicates، يُ draft approval routes RTL، يُ narrate cashflow «لماذا تراجع الرصيد هذا الأسبوع؟»، يُ sync QuickBooks وNetSuite وXero، يُ WhatsApp reminders لل approvers، يُ audit trail لل boards — لل SMB وmid-market وfranchise groups في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: FinAgent 1 كان يُ confuse Arabic company names؛ الإصدار 2 يُ entity resolution محسّن، يُ benchmark −53% وقت «invoice → booked» في FMCG سعودي، يُ multi-currency SAR/AED/EGP، يُ partner program في القاهرة ودبي، ويُ templates لـ e-invoicing compliance.</p>
      <p>القدرات الأساسية: OCR عربي؛ anomaly detection؛ natural language dashboards؛ mobile approvals؛ sandbox لل CFO workshops.</p>
      <p>للمبدعين العرب: accounting boutiques — «FinAgent 2 Arabic books cockpit in 6 days» لل orgs 200–8000 bills/شهر. من يُ sell 8 cockpits/ربع بـ 2200–48000 دولار + bookkeeping 180–1500 دولار/شهر يبني «مكتب Bill.com AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Bill.com FinAgent 2 Arabic؟</h3>
        <ul>
          <li><strong>FinAgent setup (chart، workflows، Arabic vendors، training):</strong> 4–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>Monthly close support وexception handling:</strong> — 180–1500 دولار/شهر.</li>
          <li><strong>Industry kits (hospitality، construction، logistics):</strong> — 40–185 دولار/حزمة.</li>
          <li><strong>دورات «محاسبة ذكية بـ Bill.com FinAgent بالعربية»:</strong> — 44–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Bill.com</span>
        <span class="tag">Finance</span>
        <span class="tag">AP/AR</span>
        <span class="tag">SMB</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Linear AI Projects 3 Arabic: product velocity — specs، priorities، وupdates بلسان engineering!</h2>
      <p class="article-lead">«37 issue عاجلة — والـ PM يريد خطة قبل standup». في 8 نوفمبر 2026، أطلقت <strong>Linear</strong> <strong>AI Projects 3 Arabic</strong>: copilot داخل Linear يُ summarize sprint health بالعربية، يُ draft issue descriptions وacceptance criteria RTL، يُ suggest triage وassignees من history، يُ generate weekly status لل stakeholders، يُ sync GitHub وFigma وSlack، يُ detect scope creep وblockers، يُ respect team templates وworkflows — لل startups وscale-ups وproduct agencies في MENA.</p>
      <p>المشكلة التي حلّتها: Projects 2 كان summaries إنجليزية؛ الإصدار 3 يُ bilingual briefs، يُ benchmark −37% وقت «chaos → prioritized backlog» في fintech قطر، يُ agent mode يُ chain sub-tasks، يُ enterprise SSO، ويُ marketplace playbooks لل RTL apps.</p>
      <p>القدرات الأساسية: NL issue creation؛ auto-link duplicates؛ meeting notes → tickets؛ cycle analytics؛ mobile digest بالعربية.</p>
      <p>للمبدعين العرب: product consultants — «AI Projects 3 Arabic velocity kit in 3 days» لل teams 5–150 engineers. من يُ run 12 kits/ربع بـ 900–28000 دولار + coaching 85–720 دولار/شهر يبني «غرفة Linear AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Linear AI Projects 3 Arabic؟</h3>
        <ul>
          <li><strong>Velocity kit (templates، workflows، Arabic rituals، onboarding):</strong> 2–8 أيام — 900–28000 دولار/عميل.</li>
          <li><strong>Monthly backlog hygiene وstakeholder reporting:</strong> — 85–720 دولار/شهر.</li>
          <li><strong>Stack packs (mobile RTL، payments، marketplace):</strong> — 35–165 دولار/حزمة.</li>
          <li><strong>دورات «إدارة منتج بـ Linear AI Projects بالعربية»:</strong> — 38–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Linear</span>
        <span class="tag">Product</span>
        <span class="tag">Engineering</span>
        <span class="tag">Agile</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="08-11-2026 -- 04-PM.html">
          📰 8 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "08-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/08-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/08-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
