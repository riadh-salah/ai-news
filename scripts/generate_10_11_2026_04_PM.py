#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 10-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "10-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Einstein Copilot 2 Arabic · Zendesk AI Agents 3 Arabic · "
    "Shopify Sidekick 3 Arabic · Snowflake Cortex Analyst 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Einstein Copilot 2 Arabic، Zendesk AI Agents 3 Arabic، Shopify Sidekick 3 Arabic، Snowflake Cortex Analyst 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 10 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Salesforce Einstein Copilot 2 Arabic الذي يُحوّل CRM من جدول بارد إلى شريك مبيعات يُلخّص الصفقات ويُ draft عروضًا بالعربية، إلى Zendesk AI Agents 3 Arabic الذي يُغلق تذاكر الدعم قبل أن يفتح العميل رسالة ثانية، ومن Shopify Sidekick 3 Arabic الذي يُنمو متجرك من تحليل سلة مهجورة إلى حملة RTL في دقائق، إلى Snowflake Cortex Analyst 2 Arabic الذي يُجيب أسئلة الإدارة من بياناتك بفصحى موثّقة — أربع قصص مسائية في 10 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء نهاية اليوم!</h1>
      <p class="hero-sub">مساءٌ لفرق المبيعات وخدمة العملاء والتجارة الإلكترونية وتحليل البيانات: الصفقات تبرد، الطوابير تطول، الحملات تنتظر copy، والمديرون يسألون عن أرقام بلا وقت للـ SQL. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 10 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Einstein Copilot 2 Arabic: CRM حيّ — ملخص صفقات، عروض، ومتابعات بلسان مبيعاتك!</h2>
      <p class="article-lead">«العميل كتب بالعربية: نريد تسعيرًا لتجديد العقد — والمندوب يبحث في خمس شاشات». في 10 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Einstein Copilot 2 Arabic</strong>: مساعد مدمج في Sales وService وMarketing Cloud يُ summarize accounts وopportunities بالفصحى، يُ draft emails وquotes RTL من تاريخ التعامل، يُ suggest next steps من playbooks محلية، يُ answer «لماذا تأخرت هذه الصفقة؟» من activities وcalls، يُ generate call prep من ملاحظات عربية، يُ respect field-level security وEinstein Trust Layer، يُ integrate Slack وOutlook وWhatsApp Business — لل B2B وdistribution وreal estate وtelco في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot 1 كان يُ generic بالإنجليزية؛ الإصدار 2 يُ Arabic NLU على أسماء شركات ومنتجات محلية، يُ benchmark +31% speed-to-quote في integrator سعودي 220 مقعدًا، يُ grounding على Knowledge وData Cloud، يُ partner enablement في دبي والرياض والقاهرة، ويُ templates لـ RFP responses وrenewal campaigns.</p>
      <p>القدرات الأساسية: Sales emails بالعربية؛ opportunity risk scoring؛ meeting follow-ups؛ Arabic prompts library؛ audit trails لل compliance؛ mobile voice summaries.</p>
      <p>للمبدعين العرب: Salesforce partners — «Einstein Copilot 2 Arabic revenue desk in 6 days» لل orgs 50–8000 users. من يُ launch 7 desks/ربع بـ 3500–68000 دولار + retainer 280–2200 دولار/شهر يبني «مكتب Einstein عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Einstein Copilot 2 Arabic؟</h3>
        <ul>
          <li><strong>Copilot rollout (prompts، Arabic playbooks، Data Cloud، UAT):</strong> 5–16 يومًا — 3500–68000 دولار/عميل.</li>
          <li><strong>Monthly pipeline tuning وgovernance reviews:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Vertical kits (construction، pharma، insurance brokers):</strong> — 52–218 دولار/حزمة.</li>
          <li><strong>دورات «مبيعات ذكية بـ Salesforce Copilot بالعربية»:</strong> — 48–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Einstein</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Zendesk AI Agents 3 Arabic: دعم العملاء — حلّ تذاكر، حماية NPS، وردود بلسان العلامة!</h2>
      <p class="article-lead">«العميل يسأل عن استرجاع الطلب باللهجة الخليجية — والبوت يرد بفصحى جامدة». في 10 نوفمبر 2026، أطلقت <strong>Zendesk</strong> <strong>AI Agents 3 Arabic</strong>: وكلاء أتمتة فوق Support وMessaging وVoice يُ resolve inquiries من KB وorders وpolicies بالعربية، يُ detect sentiment وescalate لل human مع ملخص RTL، يُ draft macros وhelp center articles من أعلى التذاكر المتكررة، يُ proactive outreach لتأخير شحن أو انقطاع خدمة، يُ integrate Shopify وSAP وJira وSunshine Conversations، يُ QA sampling لل tone وcompliance — لل e-commerce وairlines وbanks وedtech في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 2 كان يُ hallucinate refund policies؛ الإصدار 3 يُ strict citations من help center وCRM، يُ benchmark −48% وقت «first reply → resolved» في marketplace مصري، يُ dialect packs لخليجي ومصري ومغربي، يُ partner certifications في Gitex، ويُ COPC-ready reporting لل outsourcers.</p>
      <p>القدرات الأساسية: Omnichannel agents؛ knowledge gap detection؛ supervisor co-pilot؛ Arabic CSAT insights؛ sandbox لل CX leads؛ APIs لل custom actions.</p>
      <p>للمبدعين العرب: Zendesk partners وBPOs — «AI Agents 3 Arabic CX cell in 5 days» لل brands 20–500 agents. من يُ stand 9 cells/ربع بـ 2600–52000 دولار + support 220–1800 دولار/شهر يبني «مركز Zendesk AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zendesk AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>CX cell deploy (KB grounding، dialect tone، integrations، QA):</strong> 4–14 يومًا — 2600–52000 دولار/عميل.</li>
          <li><strong>Monthly deflection tuning وmacro refresh:</strong> — 220–1800 دولار/شهر.</li>
          <li><strong>Playbooks (returns، telecom، fintech KYC):</strong> — 45–198 دولار/حزمة.</li>
          <li><strong>دورات «دعم عملاء ذكي بـ Zendesk بالعربية»:</strong> — 42–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zendesk</span>
        <span class="tag">AI Agents</span>
        <span class="tag">CX</span>
        <span class="tag">Support</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Shopify Sidekick 3 Arabic: تجارتك الإلكترونية — من سلة مهجورة إلى حملة RTL قبل العشاء!</h2>
      <p class="article-lead">«المخزون راكد والإعلانات لا تُباع — وصاحب المتجر يريد خطة بالعربية لا جدول Excel». في 10 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: مساعد داخل Admin يُ analyze sales وinventory بالفصحى، يُ suggest bundles وdiscounts من سلوك العملاء المحليين، يُ write product descriptions وSEO RTL، يُ generate email وSMS campaigns وsocial hooks، يُ create landing sections من prompt عربي، يُ sync Meta وGoogle وTikTok Shop، يُ compliance hints لل VAT وconsumer law في الخليج — لل D2C وmodest fashion وelectronics وF&amp;B brands في MENA.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان يُ ignore seasonal peaks محلية؛ الإصدار 3 يُ Ramadan وWhite Friday calendars، يُ benchmark +27% recovery من abandoned carts في fashion label إماراتي، يُ image alt-text عربي لل accessibility، يُ partner Plus agencies في دبي والرياض وبيروت، ويُ wholesale B2B snippets.</p>
      <p>القدرات الأساسية: Natural language analytics؛ theme block generation؛ customer segments؛ Arabic A/B copy؛ mobile voice briefings؛ Markets multi-currency insights.</p>
      <p>للمبدعين العرب: Shopify partners — «Sidekick 3 Arabic growth sprint in 3 days» لل stores 500–500000 GMV/شهر. من يُ run 12 sprints/ربع بـ 900–28000 دولار + retainer 120–980 دولار/شهر يبني «وكالة Sidekick عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>Growth sprint (catalog، Sidekick prompts، campaigns، KPIs):</strong> 2–8 أيام — 900–28000 دولار/عميل.</li>
          <li><strong>Monthly promo calendars وcreative refresh:</strong> — 120–980 دولار/شهر.</li>
          <li><strong>Niche kits (perfume، abaya، gaming gear، gourmet):</strong> — 28–145 دولار/حزمة.</li>
          <li><strong>دورات «تجارة ذكية بـ Shopify Sidekick بالعربية»:</strong> — 35–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Growth</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Snowflake Cortex Analyst 2 Arabic: بياناتك تتكلم — أسئلة إدارية بفصحى موثّقة من warehouse!</h2>
      <p class="article-lead">«المدير يسأل: ما هامش الربح حسب الفرع في الربع؟ — والفريق يعدّ SQL حتى المساء». في 10 نوفمبر 2026، أطلقت <strong>Snowflake</strong> <strong>Cortex Analyst 2 Arabic</strong>: واجهة محادثة فوق Snowflake تُ translate أسئلة إدارية بالعربية إلى SQL آمن، يُ explain النتائج بجمل واضحة مع جداول وcharts، يُ suggest follow-up questions، يُ cite semantic models وrow-level policies، يُ schedule digest صباحي لل CFO بالفصحى، يُ integrate Streamlit وTableau وSigma، يُ private models وArabic fine-tunes على الحوكمة — لل retail chains وlogistics وhealthcare payers وgovernments في MENA.</p>
      <p>المشكلة التي حلّتها: Analyst 1 كان يُ leak columns محظورة؛ الإصدار 2 يُ policy-aware generation وhuman approval لل exports، يُ benchmark −55% وقت «سؤال → chart معتمد» في supermarket group سعودي، يُ bilingual glossaries لل KPIs، يُ partner data mesh في دبي وعمّان، ويُ sovereign region support.</p>
      <p>القدرات الأساسية: Semantic layer bindings؛ Arabic number and date formatting؛ anomaly narratives؛ collaboration threads؛ audit لكل سؤال وquery.</p>
      <p>للمبدعين العرب: Snowflake partners — «Cortex Analyst 2 Arabic insights studio in 7 days» لل accounts 5–500 TB. من يُ deliver 6 studios/ربع بـ 4200–72000 دولار + managed 320–2600 دولار/شهر يبني «استوديو Cortex عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex Analyst 2 Arabic؟</h3>
        <ul>
          <li><strong>Insights studio (semantic models، Arabic KPIs، RBAC، training):</strong> 6–18 يومًا — 4200–72000 دولار/عميل.</li>
          <li><strong>Monthly metric catalog وexecutive digests:</strong> — 320–2600 دولار/شهر.</li>
          <li><strong>Vertical packs (FMCG، telco churn، hospital ops):</strong> — 55–235 دولار/حزمة.</li>
          <li><strong>دورات «تحليلات محادثة بـ Snowflake Cortex بالعربية»:</strong> — 52–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Cortex</span>
        <span class="tag">Analytics</span>
        <span class="tag">Data</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 10-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="10-11-2026 -- 04-PM.html">
          📰 10 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "10-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/10-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/10-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
