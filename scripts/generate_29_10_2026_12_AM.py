#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "LangChain LangSmith Agents 2 Arabic · PayPal AI Commerce 3 Arabic · "
    "Gamma AI Presentations 3 Arabic · Todoist Ramble AI 3 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — LangChain LangSmith Agents 2 Arabic، PayPal AI Commerce 3 Arabic، Gamma AI Presentations 3 Arabic، Todoist Ramble AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من LangChain LangSmith Agents 2 Arabic الذي يُراقب وكلاء production ويُصلح سلاسل الأدوات قبل أن يُ desync البيانات، إلى PayPal AI Commerce 3 Arabic الذي يُ personalizes checkout ويُ fight fraud بلهجة العميل، ومن Gamma AI Presentations 3 Arabic الذي يُ birth deck استثماري RTL من brief عربي في دقائق، إلى Todoist Ramble AI 3 Arabic الذي يُحوّل همس صوتي «ذكّر الفريق غدًا» إلى tasks مُ assign ومُ prioritized — أربع قصص ليلية في 29 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمطورين والتجار والمستشارين والمشغّلين: traces تتكدّس بلا root cause، abandoned carts تُحرق MRR، founders يبنون pitch slides يدويًا، وteams تنسى follow-ups. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 29 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>LangChain LangSmith Agents 2 Arabic: مراقبة وكلاء — traces، evals، وإصلاح تلقائي!</h2>
      <p class="article-lead">«الوكيل أجاب العميل خطأ — ولا أحد يعرف أي tool كسر». في 29 أكتوبر 2026، أطلقت <strong>LangChain</strong> <strong>LangSmith Agents 2 Arabic</strong>: منصة observability لل agents في production تُ ingest traces من LangGraph وCrewAI وcustom stacks، تُ visualize chains بالعربية مع token وlatency breakdown، تُ run eval suites على dialect packs (Gulf، Egyptian، Levantine)، تُ detect regression بعد prompt change، تُ suggest fixes (retry، fallback model، guardrail)، تُ annotate human feedback RTL، تُ export dashboards لل compliance، ويُ SSO وRBAC — لل fintech وhealthtech وSI في MENA.</p>
      <p>المشكلة التي حلّتها: LangSmith 1 كان dashboards إنجليزية فقط؛ الإصدار 2 يُ Arabic incident summaries لل on-call، يُ benchmark −41% وقت «من bug report إلى patched prompt» في insuretech الرياض، يُ dataset curation من production logs (PII-safe)، يُ A/B prompts مع statistical significance، يُ webhook alerts لـ Slack وTeams، ويُ partner certification لل consultancies.</p>
      <p>القدرات الأساسية: Arabic agent observability; Eval suites per dialect; Regression detection; Human feedback loops; Compliance exports; Partner ecosystem.</p>
      <p>للمبدعين العرب: LangChain partners — «LangSmith Agents 2 Arabic reliability pod in 8 days» لل orgs 5–200 agents. من يُ run 7 pods/ربع بـ 3200–58000 دولار + retainer 280–2200 دولار/شهر يبني «مركز LangSmith عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LangChain LangSmith Agents 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة reliability pod (instrumentation، evals، runbooks، training):</strong> 6–18 يومًا — 3200–58000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ eval refresh وincident reviews:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Playbooks قطاعية (banking، logistics، govtech، retail bots):</strong> — 62–285 دولار/playbook.</li>
          <li><strong>دورات «وكلاء آمنة في production بـ LangSmith بالعربية»:</strong> — 52–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LangChain</span>
        <span class="tag">LangSmith</span>
        <span class="tag">Agents</span>
        <span class="tag">DevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>PayPal AI Commerce 3 Arabic: مدفوعات ذكية — checkout، offers، وanti-fraud!</h2>
      <p class="article-lead">«70% يتركون السلة — والـ coupon لا يُ translate للخليجي». في 29 أكتوبر 2026، أطلقت <strong>PayPal</strong> <strong>AI Commerce 3 Arabic</strong>: طبقة intelligence فوق PayPal Checkout وBraintree تُ personalize payment methods (installments، wallets، local rails)، تُ dynamic offers وupsell post-purchase بالعربية، تُ fraud scoring مع explainability لل merchants، تُ smart retry لل failed cards، تُ A/B checkout copy RTL، تُ reconcile payouts وchargebacks summaries لل CFO، تُ integrate Shopify وWooCommerce وcustom APIs — لل e-commerce وmarketplaces وsubscriptions في GCC ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Commerce 2 كان offers generic؛ الإصدار 3 يُ cohort by dialect وdevice وLTV، يُ benchmark +18% conversion في fashion marketplace دبي، يُ BNPL eligibility messaging عربي compliant، يُ merchant copilot «لماذا ارتفع chargeback؟»، يُ partner revenue share لل agencies، ويُ sandbox لل QA قبل Black Friday.</p>
      <p>القدرات الأساسية: Arabic checkout personalization; Dynamic offers; Fraud explainability; Smart retries; Merchant copilot; Platform integrations.</p>
      <p>للمبدعين العرب: PayPal partners — «AI Commerce 3 Arabic revenue lift in 7 days» لل merchants 50K–20M GMV/month. من يُ deploy 10 stacks/ربع بـ 1800–42000 دولار + optimization 160–1350 دولار/شهر يبني «مكتب PayPal AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من PayPal AI Commerce 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue lift (audit، offers، checkout tests، reporting):</strong> 4–14 يومًا — 1800–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ offer tuning وfraud tuning:</strong> — 160–1350 دولار/شهر.</li>
          <li><strong>حزم vertical (fashion، electronics، travel، digital goods):</strong> — 38–175 دولار/حزمة.</li>
          <li><strong>دورات «تحويل أعلى بـ PayPal AI Commerce بالعربية»:</strong> — 34–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">PayPal</span>
        <span class="tag">Commerce</span>
        <span class="tag">Payments</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Gamma AI Presentations 3 Arabic: عروض تُ birth — slides، charts، وbrand RTL!</h2>
      <p class="article-lead">«Pitch غدًا — والـ deck ما زال bullet points مترجمة». في 29 أكتوبر 2026، أطلقت <strong>Gamma</strong> <strong>AI Presentations 3 Arabic</strong>: مولّد decks يُ ingest brief أو Notion doc، يُ structure narrative (problem، solution، traction، ask)، يُ generate slides RTL مع typography عربية، يُ charts من CSV وGoogle Sheets، يُ image blocks brand-safe، يُ speaker notes بالفصحى واللهجات، يُ export PDF وPPT وweb link، يُ collaborate comments وversion history، يُ template marketplace لل investors وconsultants — لل founders وagencies وuniversities في المنطقة.</p>
      <p>المشكلة التي حلّتها: Gamma 2 كان يُ break numbering في slides RTL؛ الإصدار 3 يُ bidi-safe layouts، يُ benchmark −55% وقت «brief إلى deck 20 slide» في VC accelerator القاهرة، يُ data refresh من live metrics، يُ custom fonts (Cairo، Tajawal)، يُ team libraries، ويُ API لل bulk generation.</p>
      <p>القدرات الأساسية: Arabic deck generation; RTL layouts; Live data charts; Speaker notes; Multi-export; Team libraries.</p>
      <p>للمبدعين العرب: presentation studios — «Gamma 3 Arabic investor deck in 48 hours» لل startups وconsultancies. من يُ ship 15 decks/ربع بـ 650–18500 دولار + subscription margin 20% يبني «استوديو Gamma AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gamma AI Presentations 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة investor deck (research، narrative، design، rehearsal notes):</strong> 2–6 أيام — 650–18500 دولار/عميل.</li>
          <li><strong>اشتراك شهري لـ updates وquarterly refresh:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Template packs (SaaS، real estate، NGO، edtech):</strong> — 28–132 دولار/pack.</li>
          <li><strong>دورات «عروض احترافية بـ Gamma AI بالعربية»:</strong> — 32–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gamma</span>
        <span class="tag">Presentations</span>
        <span class="tag">Pitch</span>
        <span class="tag">Design</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Todoist Ramble AI 3 Arabic: مهام من صوت — capture، prioritize، وdelegate!</h2>
      <p class="article-lead">«فكرة brilliant في السيارة — وتُنسى قبل موقف البيت». في 29 أكتوبر 2026، أطلقت <strong>Todoist</strong> <strong>Ramble AI 3 Arabic</strong>: مساعد voice وtext يُ listen للفصحى والعامية، يُ parse «ذكّر سارة بمراجعة العقد يوم الأحد» إلى tasks مُ assign مع due dates، يُ prioritize حسب energy وdeadlines، يُ break مشاريع كبيرة إلى subtasks، يُ sync calendar وSlack reminders، يُ daily plan عربي صباحي، يُ team workload view لل managers، يُ offline capture على mobile — لل freelancers وSMBs وremote teams في MENA.</p>
      <p>المشكلة التي حلّتها: Ramble 2 كان يُ confuse أسماء عربية في multi-assignee؛ الإصدار 3 يُ contact graph من integrations، يُ benchmark −36% missed deadlines في agency عمّان، يُ natural language filters «ما الذي يخص العميل X؟»، يُ Karma gamification localized، يُ export weekly reports RTL، ويُ Business tier SSO.</p>
      <p>القدرات الأساسية: Arabic voice capture; Smart assign; Priority engine; Project breakdown; Team workload; Calendar sync.</p>
      <p>للمبدعين العرب: productivity coaches — «Ramble 3 Arabic team OS in 3 days» لل teams 5–120. من يُ onboard 12 teams/ربع بـ 480–9800 دولار + coaching 75–620 دولار/شهر يبني «خط Todoist AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Todoist Ramble AI 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة team OS (workflows، labels، training، templates):</strong> 2–8 أيام — 480–9800 دولار/عميل.</li>
          <li><strong>coaching شهري لـ adoption وweekly reviews:</strong> — 75–620 دولار/شهر.</li>
          <li><strong>Industry templates (agencies، clinics، construction، events):</strong> — 22–98 دولار/template.</li>
          <li><strong>دورات «إنتاجية صوتية بـ Todoist Ramble بالعربية»:</strong> — 28–138 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Todoist</span>
        <span class="tag">Ramble</span>
        <span class="tag">Productivity</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="29-10-2026 -- 12-AM.html">
          📰 29 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/29-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/28-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/29-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
