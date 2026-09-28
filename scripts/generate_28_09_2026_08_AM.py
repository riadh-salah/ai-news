#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 28-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "28-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI Sora 2 Enterprise Arabic، Snowflake Cortex Agents 3 Arabic، LinkedIn Talent AI 3 Arabic، TikTok Symphony AI 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 28 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI الصباحية</span>
      <h1>من OpenAI Sora 2 Enterprise Arabic الذي يُحوّل storyboard عربي إلى فيديو cinematic جاهز للحملات، إلى Snowflake Cortex Agents 3 Arabic الذي يُجيب عن أسئلة finance وops من داخل data cloud دون نسخ CSV، ومن LinkedIn Talent AI 3 Arabic الذي يُ shortlist مرشحين ويُ draft رسائل outreach باللهجة، إلى TikTok Symphony AI 3 Arabic الذي يُولّد hooks وscripts وcreatives لمتاجر MENA — أربع قصص صباحية في 28 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يستيقظ مع القهوة!</h1>
      <p class="hero-sub">صباحٌ للمُؤسّسين والمُسوّقين: creative directors يريدون Sora enterprise بحقوق واضحة، محللو البيانات يطلبون agents على Snowflake مع governance، فرق HR تبحث عن LinkedIn يُفهم سوق العمل العربي، ومتاجر e-commerce تحلم بـ TikTok يُ produce محتوى يبيع. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 28 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI Sora 2 Enterprise Arabic: من نص بالعربية إلى فيديو 1080p — licensing، watermark، وAPI للوكالات!</h2>
      <p class="article-lead">«الفكرة مرئية في رأس المدير — لكن الميزانية لا تسمح بـ shoot في دبي». في 28 سبتمبر 2026، أطلقت <strong>OpenAI</strong> <strong>Sora 2 Enterprise Arabic</strong>: منصة فيديو generative للمؤسسات تفهم prompts بالفصحى واللهجات الخليجية والمصرية، تُ generate scenes وproduct placements وtalking-head style مع Arabic typography overlays، تُ enforce usage rights وC2PA metadata، تُ offer API وbatch queue مع rate tiers — للagencies وretail وmedia في MENA.</p>
      <p>المشكلة التي حلّتها: Sora consumer كان waitlist وcreative-only؛ الإصدار Enterprise Arabic يُ SSO وadmin audit، يُ extend clips وstoryboard-to-timeline، يُ brand safety filters للGCC، يُ integration ChatGPT Enterprise وAdobe وCanva export، يُ dedicated support للcampaigns Ramadan وNational Day.</p>
      <p>القدرات الأساسية: Up to 60s 1080p؛ camera motion presets؛ Arabic subtitle tracks؛ private fine-tune on approved assets؛ SLA 99.5%؛ residency EU preview.</p>
      <p>للمبدعين العرب: production houses وperformance marketers — «Sora 2 Enterprise Arabic pilot in 3 days» لل brands 5–500 SKUs. من يُ deliver 10 video packs/ربع بـ 1400–32000 دولار/each + retainer 320–2600 دولار/شهر يركب «Arabic cinematic ads without crew».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI Sora 2 Enterprise Arabic؟</h3>
        <ul>
          <li><strong>Sora 2 Enterprise rollout (prompt library، rights workflow، API):</strong> 4–12 يومًا — 1300–35000 دولار/عميل.</li>
          <li><strong>Monthly campaign production and A/B variants:</strong> — 310–2500 دولار/شهر.</li>
          <li><strong>Vertical storyboard packs (luxury، FMCG، proptech):</strong> — 48–235 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Enterprise Video with Sora 2 API»:</strong> — 44–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Sora 2</span>
        <span class="tag">Video</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Snowflake Cortex Agents 3 Arabic: analyst رقمي — SQL، forecasts، وSlack answers من سؤال بالعربية!</h2>
      <p class="article-lead">«الرئيس يسأل: ما margin SKU X في السعودية؟ — والفريق يبني spreadsheet ليومين». في 28 سبتمبر 2026، أطلقت <strong>Snowflake</strong> <strong>Cortex Agents 3 Arabic</strong>: agents داخل Snowflake AI Data Cloud يُ parse questions بالعربية، يُ generate SQL وPython على tables محمية، يُ summarize results وcharts، يُ post answers إلى Slack وTeams وemail — للretail وfinance وlogistics في MENA.</p>
      <p>المشكلة التي حلّتها: Cortex Agents 2 كان English NLQ؛ الإصدار 3 يُ Arabic dialect routing، يُ multi-step planning «compare YoY GCC»، يُ guardrails PII masking، يُ Cortex Analyst + Search unified، يُ marketplace templates inventory وrevenue وcompliance، يُ cost attribution per business unit.</p>
      <p>القدرات الأساسية: Row access policies respected؛ scheduled morning Arabic briefings؛ export PDF RTL؛ integration dbt and Fivetran metadata؛ UAE region GA.</p>
      <p>للمبدعين العرب: analytics consultancies وdata engineers — «Cortex Agents 3 Arabic live in 10 days» لل warehouses 20TB–2PB. من يُ ship 5 deployments/ربع بـ 4800–88000 دولار + managed analytics 680–6200 دولار/شهر ي monetize «Arabic BI that never leaves Snowflake».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Snowflake Cortex Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>Cortex Agents 3 build (semantic layer، Arabic NLQ، UAT):</strong> 8–24 يومًا — 4600–92000 دولار/عميل.</li>
          <li><strong>Monthly semantic model and agent tuning:</strong> — 650–6100 دولار/شهر.</li>
          <li><strong>Industry KPI packs (CPG، telco، airlines):</strong> — 52–265 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Data Agents on Snowflake Cortex»:</strong> — 47–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Snowflake</span>
        <span class="tag">Cortex</span>
        <span class="tag">Agents</span>
        <span class="tag">Analytics</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>LinkedIn Talent AI 3 Arabic: sourcing، screening، وInMail — recruiter واحد يُ cover MENA!</h2>
      <p class="article-lead">«الوظيفة urgent — لكن inbox المرشحين فارغ». في 28 سبتمبر 2026، أطلقت <strong>LinkedIn</strong> <strong>Talent AI 3 Arabic</strong>: suite داخل Recruiter وHiring Assistant يُ understand job descriptions بالعربية، يُ rank candidates مع explainability، يُ draft personalized InMail (MSA وخليجي)، يُ schedule interviews وscore skills tests — للenterprises وRPOs في GCC وEgypt.</p>
      <p>المشكلة التي حلّتها: Talent AI 2 كان English templates؛ الإصدار 3 يُ Arabic boolean search hints، يُ bias reduction for gendered Arabic titles، يُ internal mobility suggestions، يُ integration Workday and SAP SuccessFactors Arabic fields، يُ compliance logs PDPL-ready، يُ talent pool heatmaps by city.</p>
      <p>القدرات الأساسية: AI-assisted screening rubrics؛ video intro analysis multilingual؛ recruiter copilot chat؛ bulk outreach with human approval؛ analytics time-to-hire Arabic reports.</p>
      <p>للمبدعين العرب: HR tech consultants وboutique recruiters — «Talent AI 3 Arabic go-live in 6 days» لل companies 200–20000 employees. من يُ sell 12 implementations/ربع بـ 1800–42000 دولار/each + training retainer 280–2400 دولار/شهر يركب «hire faster in Arabic markets».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LinkedIn Talent AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Talent AI 3 deployment (workflows، Arabic JD templates، ATS sync):</strong> 5–16 يومًا — 1700–45000 دولار/عميل.</li>
          <li><strong>Monthly recruiter enablement and rubric updates:</strong> — 260–2300 دولار/شهر.</li>
          <li><strong>Role-specific screening kits (engineering، sales، healthcare):</strong> — 38–188 دولار/حزمة.</li>
          <li><strong>دورات «Arabic AI Recruiting with LinkedIn Talent AI»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LinkedIn</span>
        <span class="tag">Talent AI</span>
        <span class="tag">HR</span>
        <span class="tag">Recruiting</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>TikTok Symphony AI 3 Arabic: scripts، avatars، وShop ads — من فكرة باللهجة إلى viral في ساعات!</h2>
      <p class="article-lead">«المتجر جاهز — لكن TikTok يحتاج 30 فيديو/أسبوع». في 28 سبتمبر 2026، أطلقت <strong>TikTok</strong> <strong>Symphony AI 3 Arabic</strong>: creative suite للadvertisers يُ generate hooks وvoiceovers بالخليجي والمصري، يُ produce UGC-style clips وproduct demos، يُ sync TikTok Shop catalogs، يُ optimize CTAs per audience segment — للDTC brands وaffiliates في MENA.</p>
      <p>المشكلة التي حلّتها: Symphony 2 كان English voice وgeneric templates؛ الإصدار 3 يُ dialect lip-sync avatars، يُ Ramadan and back-to-school playbooks، يُ Spark Ads integration، يُ brand safety Arabic keyword lists، يُ API for agencies، يُ performance learning loop from GMV data.</p>
      <p>القدرات الأساسية: Batch 20 variants per SKU؛ auto caption burn-in RTL؛ music library MENA-licensed؛ creator marketplace match؛ dashboard ROAS Arabic.</p>
      <p>للمبدعين العرب: social commerce agencies وinfluencer managers — «Symphony AI 3 Arabic content factory in 4 days» لل stores 50–5000 products. من يُ run 15 client retainers/ربع بـ 900–18500 دولار/each + rev-share on ad spend يركب «Arabic TikTok revenue machine».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من TikTok Symphony AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Symphony AI 3 studio setup (brand voice، catalog sync، workflows):</strong> 3–9 أيام — 850–22000 دولار/عميل.</li>
          <li><strong>Monthly creative sprints and Spark optimization:</strong> — 220–2100 دولار/شهر.</li>
          <li><strong>Niche hook libraries (beauty، gadgets، food delivery):</strong> — 35–168 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Social Commerce with TikTok Symphony»:</strong> — 38–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">TikTok</span>
        <span class="tag">Symphony AI</span>
        <span class="tag">Commerce</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 28-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="28-09-2026 -- 08-AM.html">
          📰 28 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">OpenAI Sora 2 Enterprise Arabic · Snowflake Cortex Agents 3 Arabic · LinkedIn Talent AI 3 Arabic · TikTok Symphony AI 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/28-09-2026 -- 08-AM.html`](news/28-09-2026%20--%2008-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "28-09-2026 -- 08-AM.html" not in content:
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
    if new_content == content and "28-09-2026 -- 08-AM.html" not in content:
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
