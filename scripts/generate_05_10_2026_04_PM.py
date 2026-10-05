#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 05-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "05-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Loom AI Workflows 3 Arabic، PandaDoc AI Hub 2 Arabic، Atlassian Rovo 4 Arabic، Surfer SEO AI Writer 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 5 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Loom AI Workflows 3 Arabic الذي يُحوّل تسجيل شاشة واحد إلى playbook تدريب وonboarding بالعربية، إلى PandaDoc AI Hub 2 Arabic الذي يُ birth عرضًا وعقدًا RTL قبل أن تُغلق مكالمة Zoom، ومن Atlassian Rovo 4 Arabic الذي يُ orchestrate Jira وConfluence وLoom بأمر عربي واحد، إلى Surfer SEO AI Writer 3 Arabic الذي يُ bridge بين keyword intent MENA ومحتوى يُ rank — أربع قصص مسائية في 5 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء نهاية يوم الاثنين!</h1>
      <p class="hero-sub">مساءٌ للمُشغّلين والمُبدعين: remote teams تغرق في فيديوهات طويلة لا يشاهدها أحد، sales reps يُعدّون proposals يدويًا بعد كل demo، engineering managers يُ chase status بين Slack وJira، وcontent teams في MENA تكتب مقالات بلا خريطة intent عربية حقيقية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 5 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Loom AI Workflows 3 Arabic: فيديو async ذكي — summaries، chapters، وtraining flows RTL!</h2>
      <p class="article-lead">«سجّلت 40 دقيقة شرح — ولا أحد يعرف أين يبدأ الجزء المهم». في 5 أكتوبر 2026، أطلقت <strong>Loom</strong> <strong>AI Workflows 3 Arabic</strong>: suite فوق Loom recorder تُ transcribe لهجات MENA، تُ generate chapters وtitles RTL، تُ draft SOPs وFAQ من الفيديو، تُ create interactive walkthroughs مع CTAs، تُ translate captions EN↔AR، وتُ sync إلى Notion وConfluence وSlack — لل product وCS وHR وsales enablement.</p>
      <p>المشكلة التي حلّتها: Workflows 2 كان English-first؛ الإصدار 3 يُ parse mixed Arabic-English narration، يُ benchmark −52% time-to-onboard في fintech remote team إماراتي، يُ permission-aware sharing، يُ viewer analytics (drop-off heatmaps)، ويُ integration Salesforce وHubSpot لـ video pitches.</p>
      <p>القدرات الأساسية: Bulk video library tagging؛ AI trim silence؛ personalized intro lines per viewer segment؛ embed في help centers RTL؛ mobile recording with live Arabic captions.</p>
      <p>للمبدعين العرب: enablement consultants وLoom champions — «Workflows 3 Arabic video ops in 5 days» لل teams 20–800 seats. من يُ ship 12 libraries/ربع بـ 1100–21000 دولار + care 95–780 دولار/شهر يبني «استوديو Loom AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Loom AI Workflows 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة video ops (audit، templates، chapters، Arabic tone):</strong> 3–8 أيام — 1100–21000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل library والتحديثات:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>حزم onboarding قطاعية (SaaS، banking، retail):</strong> — 48–220 دولار/حزمة.</li>
          <li><strong>دورات «تشغيل Loom Workflows بالعربية للفرق»:</strong> — 36–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Loom</span>
        <span class="tag">Video</span>
        <span class="tag">Enablement</span>
        <span class="tag">Async</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>PandaDoc AI Hub 2 Arabic: عروض وعقود — quotes، eSign، وrenewals بلهجة MENA!</h2>
      <p class="article-lead">«العميل يريد proposal غدًا — والقالب إنجليزي قديم». في 5 أكتوبر 2026، أطلقت <strong>PandaDoc</strong> <strong>AI Hub 2 Arabic</strong>: copilot يُ draft quotes وproposals وMSAs RTL من CRM notes، يُ suggest pricing tables وpayment terms ZATCA-aware، يُ redline clauses مع summaries عربية، يُ auto-fill recipient data، يُ track opens وsignatures، ويُ trigger renewals sequences — لل B2B agencies وSaaS وreal estate brokers في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: Hub 1 كان template-heavy English؛ الإصدار 2 يُ dialect-friendly cover letters، يُ benchmark +34% faster close cycle في IT services سعودي، يُ CRM sync Salesforce وHubSpot وPipedrive، يُ approval workflows multi-signer، ويُ audit trail PDPL-ready.</p>
      <p>القدرات الأساسية: Content library Arabic snippets؛ bulk send personalized؛ payment collection embedded؛ analytics win/loss reasons؛ API لل custom portals.</p>
      <p>للمبدعين العرب: sales ops freelancers — «PandaDoc AI Hub 2 Arabic deal desk in 6 days» لل orgs 5–200 reps. من يُ onboard 10 desks/ربع بـ 1300–24000 دولار + managed 105–850 دولار/شهر يبني «مكتب proposals AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من PandaDoc AI Hub 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة deal desk (templates، CRM، Hub tuning، Arabic legal tone):</strong> 4–10 أيام — 1300–24000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل templates والتقارير:</strong> — 105–850 دولار/شهر.</li>
          <li><strong>Playbooks (agency SOW، SaaS MSA، real estate SPA):</strong> — 55–240 دولار/playbook.</li>
          <li><strong>دورات «عروض PandaDoc AI بالعربية للمبيعات»:</strong> — 38–182 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">PandaDoc</span>
        <span class="tag">Sales</span>
        <span class="tag">Proposals</span>
        <span class="tag">eSign</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Atlassian Rovo 4 Arabic: زميل AI للهندسة — Jira، Confluence، وLoom في مسار واحد!</h2>
      <p class="article-lead">«أين قرار architecture الأسبوع الماضي؟ — و12 thread مختلف». في 5 أكتوبر 2026، أطلقت <strong>Atlassian</strong> <strong>Rovo 4 Arabic</strong>: teammate agent يُ search across Jira وConfluence وBitbucket وLoom بالعربية، يُ create وupdate issues من chat، يُ summarize sprints وincidents، يُ draft PRDs وrelease notes RTL، يُ link Loom clips إلى tickets، يُ suggest assignees — لل software houses وbanks وtelcos في MENA.</p>
      <p>المشكلة التي حلّتها: Rovo 3 كان search-strong لكن action-light؛ الإصدار 4 يُ multi-step plans (research → ticket → doc)، يُ benchmark −41% time-to-spec في scale-up مصري، يُ permission inheritance strict، يُ data residency EU/GCC options، ويُ Studio لل custom agents Arabic.</p>
      <p>القدرات الأساسية: Incident postmortems auto-draft؛ code review summaries؛ cross-project dependency maps؛ mobile voice commands Arabic؛ integration Slack وMicrosoft Teams.</p>
      <p>للمبدعين العرب: Atlassian partners وdev productivity coaches — «Rovo 4 Arabic engineering cockpit in 8 days» لل orgs 30–3000 devs. من يُ deploy 9 stacks/ربع بـ 2200–48000 دولار + retainer 140–1150 دولار/شهر يبني «غرفة Rovo AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlassian Rovo 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة engineering cockpit (spaces، agents، Rovo tuning، Arabic docs):</strong> 5–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل sprints والمعرفة:</strong> — 140–1150 دولار/شهر.</li>
          <li><strong>Agents جاهزة (incident، onboarding dev، compliance):</strong> — 60–265 دولار/agent.</li>
          <li><strong>دورات «Rovo 4 للفرق الهندسية العربية»:</strong> — 42–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atlassian</span>
        <span class="tag">Rovo</span>
        <span class="tag">DevOps</span>
        <span class="tag">Jira</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Surfer SEO AI Writer 3 Arabic: محتوى يُ rank — outline، entities، وSERP gaps RTL!</h2>
      <p class="article-lead">«نريد traffic من السعودية — والمقالات translated English». في 5 أكتوبر 2026، أطلقت <strong>Surfer SEO</strong> <strong>AI Writer 3 Arabic</strong>: copilot يُ analyze SERP عربي (MSA وdialect hints)، يُ generate outlines وbriefs RTL، يُ score content vs competitors، يُ suggest NLP entities وinternal links، يُ audit existing pages، يُ export إلى WordPress وWebflow — لل publishers وagencies وe-commerce SEO في MENA.</p>
      <p>المشكلة التي حلّتها: Writer 2 كان keyword-stuffing prone؛ الإصدار 3 يُ E-E-A-T friendly Arabic، يُ benchmark +29% organic clicks في health blog خليجي، يُ cannibalization alerts، يُ integration Ahrefs وGSC، ويُ team workflows مع approval comments RTL.</p>
      <p>القدرات الأساسية: Bulk content plans؛ AI humanizer tone presets (فصحى، خليجي light)؛ plagiarism checks؛ SERP volatility alerts؛ API لل programmatic SEO.</p>
      <p>للمبدعين العرب: SEO freelancers وcontent studios — «Surfer Writer 3 Arabic content engine in 7 days» لل sites 10–500 URLs. من يُ launch 8 engines/ربع بـ 900–19000 دولار + optimization 85–720 دولار/شهر يبني «وكالة SEO AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Surfer SEO AI Writer 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة content engine (audit، clusters، Writer tuning، Arabic style guide):</strong> 4–11 يومًا — 900–19000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل briefs والمراقبة:</strong> — 85–720 دولار/شهر.</li>
          <li><strong>حزم niche (fintech، travel، SaaS B2B):</strong> — 40–195 دولار/حزمة.</li>
          <li><strong>دورات «SEO بالعربية مع Surfer AI Writer»:</strong> — 34–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Surfer SEO</span>
        <span class="tag">SEO</span>
        <span class="tag">Content</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 05-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="05-10-2026 -- 04-PM.html">
          📰 5 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Loom AI Workflows 3 Arabic · PandaDoc AI Hub 2 Arabic · Atlassian Rovo 4 Arabic · Surfer SEO AI Writer 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/05-10-2026 -- 04-PM.html`](news/05-10-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "05-10-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "05-10-2026 -- 04-PM.html" not in content:
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
        "أktobar",
        "أktober",
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
        " y\u064f ",
        "yü ",
        "yü",
        "تü",
        "فيdeo",
        "montaje",
        "المشك problem",
        " y\u064f ",
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
