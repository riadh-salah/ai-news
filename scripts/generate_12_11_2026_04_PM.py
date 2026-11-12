#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 12-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "12-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Meta Llama Enterprise 4 Arabic · Databricks Mosaic AI Agent Framework 2 Arabic · "
    "Klaviyo AI Email Architect 5 Arabic · Wix AI Site Builder 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Meta Llama Enterprise 4 Arabic، Databricks Mosaic AI Agent Framework 2 Arabic، Klaviyo AI Email Architect 5 Arabic، Wix AI Site Builder 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 12 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Meta Llama Enterprise 4 Arabic الذي يُشغّل وكلاءك على بياناتك الخاصة بلهجة الفريق قبل غروب الشمس، إلى Databricks Mosaic AI Agent Framework 2 Arabic الذي يُبني agent يُستعلم من lakehouse ويُنفّذ SQL وactions من أمر عربي واحد، ومن Klaviyo AI Email Architect 5 Arabic الذي يُصمّم سلاسل بريد RTL ويُحسّن معدلات الفتح من سلوك المشتركين في MENA، إلى Wix AI Site Builder 3 Arabic الذي يُطلق متجرًا ومدونة وصفحات هبوط بعربية أصيلة قبل أن تُطفأ مكتبك — أربع قصص مسائية في 12 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ لفرق البيانات والتجارة والمؤسسين الرقميين: النماذج تخاف من البيانات الحساسة، الوكلاء عالقون في POC، الحملات البريدية تموت في spam، والمواقع تتأخر أسابيع. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 12 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Meta Llama Enterprise 4 Arabic: نماذج Llama على أرضك — وكلاء آمنون بلهجات MENA!</h2>
      <p class="article-lead">«لا نرفع عقود العملاء إلى cloud عام — لكننا نريد agent يُجيب الفريق بالعربية». في 12 نوفمبر 2026، أطلقت <strong>Meta</strong> <strong>Llama Enterprise 4 Arabic</strong>: حزمة استضافة وfine-tuning وتشغيل لوكلاء مبنية على Llama 4 family على VPC خاص أو sovereign cloud، تُفهم الفصحى والخليجية والمصرية والمغاربية، تُ retrieve من SharePoint وS3 وOracle وPostgreSQL، تُ enforce no-training وaudit logs وrole-based tools، تُ deploy في UAE وSaudi وEU regions، وتُ ship connectors لـ WhatsApp Business وTeams — للبنوك والقانون والطاقة والhealth في MENA.</p>
      <p>المشكلة التي حلّتها: Llama Enterprise 3 كان يتطلب ضبطًا معقدًا للعربية في RAG؛ الإصدار 4 يُ Arabic tokenizer محسّن، يُ multi-agent orchestration (research → draft → legal review)، يُ guardrails للـ PII والفتوى والclaims طبية، يُ benchmark +39% دقة استرجاع في corpus قانوني خليجي، يُ act عبر plugins (generate memo، compare clauses، post summary)، ويُ partner program «MENA Llama Builder» في الرياض ودبي.</p>
      <p>القدرات الأساسية: Llama Stack runtime؛ catalog نماذج (8B–405B inference)؛ Arabic eval suite؛ on-prem appliance option؛ MCP وOpenAPI tool registry؛ تدريب LoRA داخل perimeter.</p>
      <p>للمبدعين العرب: integrators وAI boutiques — «Llama Enterprise 4 Arabic secure agents in 12 days» للمؤسسات 500+ مقعد. من يُسلّم 5 rollouts/ربع بـ 4800–72000 دولار + care 960–6400 دولار/شهر يبيع سيادة بيانات عربية مع أداء عالمي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meta Llama Enterprise 4 Arabic؟</h3>
        <ul>
          <li><strong>Llama Enterprise 4 deployment (VPC، RAG، agents، governance):</strong> 10–28 يومًا — 4800–72000 دولار/عميل.</li>
          <li><strong>ضبط نماذج ومراقبة وكلاء شهريًا:</strong> — 960–6400 دولار/شهر.</li>
          <li><strong>حزم قطاعات (legal، banking، energy، health):</strong> — 72–320 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء Llama آمنون بالعربية على بياناتك»:</strong> — 58–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meta</span>
        <span class="tag">Llama</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Sovereign</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Databricks Mosaic AI Agent Framework 2 Arabic: من lakehouse إلى قرار — وكيل يُفكر بالبيانات ويُنفّذ!</h2>
      <p class="article-lead">«الرقم موجود في الجداول — لكن الإدارة تنتظر تقريرًا بالعربية منذ أسبوع». في 12 نوفمبر 2026، أطلقت <strong>Databricks</strong> <strong>Mosaic AI Agent Framework 2 Arabic</strong>: إطار بناء وكلاء فوق Unity Catalog وDelta Lake يُ parse أسئلة NL بالعربية، يُ generate SQL وPython آمن، يُ visualize في dashboards، يُ trigger workflows (Snowflake export، Slack alert، ticket ServiceNow)، يُ cite tables وrows، يُ respect row-level security، ويُ integrate MLflow وvector search — لفرق data وanalytics وops في retail وtelecom وفintech MENA.</p>
      <p>المشكلة التي حلّتها: Agent Framework 1 كان يتعثر على أسماء أعمدة عربية ومزامنة schemas؛ الإصدار 2 يُ Arabic schema hints، يُ human approval لـ destructive queries، يُ multi-step planning مع ذاكرة جلسة، يُ benchmark −52% وقت «سؤال إدارة → رد موثّق» في مجموعة اتصالات خليجية، يُ Unity governance tags، ويُ ship industry accelerators (churn، fraud، inventory).</p>
      <p>القدرات الأساسية: Agent Designer UI؛ Arabic query templates؛ evaluation harness؛ تكامل Power BI وTableau؛ partner certifications في القاهرة وعمّان.</p>
      <p>للمبدعين العرب: data consultancies — «Arabic data agent live in 8 days» على Databricks workspace. من يُشغّل 9 عملاء Agent Framework 2/ربع بـ 5200–68000 دولار + tuning 780–4900 دولار/شهر يحوّل lakehouse إلى منتج قرار عربي premium.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Databricks Mosaic AI Agent Framework 2 Arabic؟</h3>
        <ul>
          <li><strong>Agent Framework 2 implementation (catalog، tools، agents، UAT):</strong> 6–18 يومًا — 5200–68000 دولار/عميل.</li>
          <li><strong>تحسين استعلامات وحوكمة شهريًا:</strong> — 780–4900 دولار/شهر.</li>
          <li><strong>حزم vertical (retail analytics، fraud، HR metrics):</strong> — 68–295 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء بيانات عربية على Databricks»:</strong> — 55–240 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Databricks</span>
        <span class="tag">Mosaic</span>
        <span class="tag">Data</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Klaviyo AI Email Architect 5 Arabic: حملات بريد RTL — من الفكرة إلى A/B قبل العشاء!</h2>
      <p class="article-lead">«حملة Ramadan تحتاج 12 إيميلًا بالعربية — والتصميم عالق عند المراجعة الثالثة». في 12 نوفمبر 2026، أطلقت <strong>Klaviyo</strong> <strong>AI Email Architect 5 Arabic</strong>: منصة تُ ingest product catalog وbehavior وsegments، تُ draft subject lines وbody RTL بفصحى تسويقية ولهجات خليجية، تُ personalize blocks حسب RFM، تُ generate images متوافقة brand، تُ schedule send-time محلي لكل مدينة، تُ run multivariate tests، وتُ sync revenue attribution — لـ DTC brands وmarketplaces وsubscription boxes في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Architect 4 كان يُ كسر mobile layout على نص عربي طويل؛ الإصدار 5 يُ Arabic line-breaking engine، يُ spam-score advisor، يُ benchmark +27% open rate في cohort 180 متجر إلكتروني سعودي، يُ WhatsApp handoff للسلة المهجورة، يُ compliance hints (opt-out، promos)، ويُ integrate Shopify وWooCommerce وcustom CDP.</p>
      <p>القدرات الأساسية: Flow Copilot عربي؛ template marketplace MENA؛ deliverability dashboard؛ creator affiliate program؛ شهادة «MENA Lifecycle Marketer».</p>
      <p>للمبدعين العرب: email agencies وgrowth freelancers — «Architect 5 Arabic flows in 4 days» لكل brand 5K–500K subscriber. من يُدير 18 عميل lifecycle/ربع بـ 1200–8500 دولار/عميل + retainer 280–1600 دولار/شهر يبني MRR تسويق عربي قابل للتوسع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Klaviyo AI Email Architect 5 Arabic؟</h3>
        <ul>
          <li><strong>Architect 5 setup (segments، flows، RTL templates، testing):</strong> 3–10 أيام — 1200–8500 دولار/عميل.</li>
          <li><strong>تحسين حملات وdeliverability شهريًا:</strong> — 280–1600 دولار/شهر/عميل.</li>
          <li><strong>حزم مواسم (Ramadan، Black Friday، العودة للمدارس):</strong> — 42–185 دولار/حزمة.</li>
          <li><strong>دورات «تسويق lifecycle عربي بـ Klaviyo AI»:</strong> — 38–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Klaviyo</span>
        <span class="tag">Email</span>
        <span class="tag">Marketing</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Wix AI Site Builder 3 Arabic: موقعك وحملتك ومتجرك — من فكرة عربية إلى نشر خلال ساعات!</h2>
      <p class="article-lead">«نريد landing page بالعربية لمنتج جديد — والمطور مشغول حتى الجمعة». في 12 نوفمبر 2026، أطلقت <strong>Wix</strong> <strong>AI Site Builder 3 Arabic</strong>: محرك generative فوق Wix Editor يُ interview المستخدم بالعربية (جمهور، عرض قيمة، ألوان، tone)، يُ generate pages وsections وcopy RTL، يُ wire ecommerce وbookings وblog، يُ optimize Core Web Vitals وSEO عربي، يُ create ad creatives متسقة، يُ publish مع domain وSSL، ويُ offer analytics copilot — للمؤسسين والعيادات والمدربين والوكالات الصغيرة في MENA.</p>
      <p>المشكلة التي حلّتها: Site Builder 2 كان generic templates؛ الإصدار 3 يُ Arabic brand voice profiles، يُ industry packs (clinic، course، restaurant، B2B services)، يُ benchmark 78% sites live بدون مطوّر في pilot 300 مستخدم مصري، يُ integrate Wix Payments وPOS، يُ multilingual toggle EN/AR، ويُ partner program لـ resellers في الخليج.</p>
      <p>القدرات الأساسية: AI Sections library؛ Media generation؛ CRM lite؛ automation (leads → email)؛ white-label للوكالات؛ شهادة «MENA Wix AI Partner».</p>
      <p>للمبدعين العرب: web agencies وsolopreneurs — «Wix AI 3 Arabic site in 48 hours» لكل عميل. من يُبني 30 موقعًا/ربع بـ 450–4200 دولار/موقع + care 75–320 دولار/شهر/موقع يحوّل السرعة إلى خط إنتاج digital عربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Wix AI Site Builder 3 Arabic؟</h3>
        <ul>
          <li><strong>Site Builder 3 delivery (brief، AI build، polish، go-live):</strong> 1–5 أيام — 450–4200 دولار/موقع.</li>
          <li><strong>صيانة محتوى وSEO وتحديثات شهريًا:</strong> — 75–320 دولار/شهر/موقع.</li>
          <li><strong>حزم قطاعات (عيادة، تدريب، مطعم، SaaS landing):</strong> — 35–155 دولار/حزمة.</li>
          <li><strong>دورات «بناء مواقع عربية بـ Wix AI بدون كود»:</strong> — 32–145 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Wix</span>
        <span class="tag">Website</span>
        <span class="tag">No-Code</span>
        <span class="tag">SMB</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 12-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="12-11-2026 -- 04-PM.html">
          📰 12 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "12-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/12-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/12-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
