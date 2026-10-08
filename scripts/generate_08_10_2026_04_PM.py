#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "08-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Cursor Bugbot 2 Arabic، Gamma Presentations 4 Arabic، Mercury AI Treasury 3 Arabic، Writer Enterprise 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Cursor Bugbot 2 Arabic الذي يُراجع pull requests ويُترجم ملاحظات الأمان إلى عربية واضحة قبل أن ينتهي standup، إلى Gamma Presentations 4 Arabic الذي يُحوّل outline عربي إلى deck سينمائي خلال دقائق، ومن Mercury AI Treasury 3 Arabic الذي يُ forecast cash flow ويُنبّه CFO قبل أي أزمة سيولة، إلى Writer Enterprise 3 Arabic الذي يُوحّد brand voice لآلاف الصفحات والعقود — أربع قصص مسائية في 8 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء مع آخر ضوء!</h1>
      <p class="hero-sub">مساءٌ للمهندسين والمستشارين وفرق المالية والمحتوى: repos تتراكم فيها PRs دون مراجعة، pitch decks تُعاد تصميمها ليلًا، treasury teams تُفاجأ بفجوات نقدية، وenterprise marketing يُعيد كتابة نفس الجمل بعشر لهجات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 8 أكتوبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Cursor Bugbot 2 Arabic: مراجع آلي للكود — أمان، أداء، وملخصات PR بلسان squad عربي!</h2>
      <p class="article-lead">«الـ PR مفتوح منذ ثلاثة أيام — ولا أحد راجع الـ diff». في 8 أكتوبر 2026، أطلقت <strong>Cursor</strong> <strong>Bugbot 2 Arabic</strong>: وكيل مراجعة مدمج في Cursor Cloud يُ scan كل pull request تلقائيًا، يُ detect bugs وsecurity issues وperformance regressions، يُ suggest fixes مع snippets، يُ draft review comments بالعربية أو الإنجليزية، يُ prioritize حسب severity، ويُ sync مع GitHub وGitLab وLinear — لل startups وscale-ups في MENA.</p>
      <p>المشكلة التي حلّتها: Bugbot 1 كان comments إنجليزية فقط ويُفوّت dialect في commit messages؛ الإصدار 2 يُ Arabic RTL summaries لل managers، يُ benchmark −41% time-to-merge في SaaS أردنية، يُ OWASP وdependency CVE checks، يُ learn من rejections السابقة، ويُ respect team style guides.</p>
      <p>القدرات الأساسية: Auto-assign reviewers؛ flaky test hints؛ migration risk flags؛ integration Slack وTeams؛ audit trail لل compliance؛ custom rules per monorepo.</p>
      <p>للمبدعين العرب: dev agencies وfractional tech leads — «Bugbot 2 Arabic review cockpit in 5 days» لل teams 3–60 engineers. من يُ roll out 8 cockpits/ربع بـ 1800–32000 دولار + tuning 120–950 دولار/شهر يبني «مكتب Cursor review عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cursor Bugbot 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة review cockpit (rules، workflows، training):</strong> 4–10 أيام — 1800–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل policies والـ tuning:</strong> — 120–950 دولار/شهر.</li>
          <li><strong>Playbooks (security hardening، legacy modules، mobile):</strong> — 55–248 دولار/playbook.</li>
          <li><strong>دورات «مراجعات كود أسرع بالعربية مع Bugbot»:</strong> — 45–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cursor</span>
        <span class="tag">DevTools</span>
        <span class="tag">CodeReview</span>
        <span class="tag">Security</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Gamma Presentations 4 Arabic: عروض تُبهر — من prompt إلى slides، charts، وnarration RTL!</h2>
      <p class="article-lead">«العرض بعد ساعتين — والـ deck فارغ». في 8 أكتوبر 2026، أطلقت <strong>Gamma</strong> <strong>Presentations 4 Arabic</strong>: منصة عروض وكيلية تُ ingest brief أو PDF أو Notion page، تُ generate storyline بالفصحى أو اللهجة المختارة، تُ layout slides بخطوط عربية صحيحة، تُ embed charts وtables من CSV، تُ Magic Animate لل transitions، تُ export إلى PowerPoint وPDF وshare link، وتُ optional AI voiceover MENA — لل consultants وfounders وHR في المنطقة.</p>
      <p>المشكلة التي حلّتها: Presentations 3 كان charts RTL معكوسة أحيانًا؛ الإصدار 4 يُ Arabic numerals toggle، يُ benchmark −52% وقت إعداد pitch في VC مصري، يُ brand themes lock، يُ speaker notes ذكية، ويُ collaboration comments RTL real-time.</p>
      <p>القدرات الأساسية: Template library (fundraising، training، quarterly review)؛ image gen contextual؛ data refresh من Google Sheets؛ embed في websites؛ analytics من opened slides.</p>
      <p>للمبدعين العرب: presentation freelancers — «Gamma 4 Arabic pitch factory in 3 days» لل founders وteams 2–200 seats. من يُ deliver 14 factories/ربع بـ 850–15500 دولار + refresh 70–580 دولار/شهر يبني «استوديو Gamma عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gamma Presentations 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة pitch factory (story، design، export):</strong> 2–8 أيام — 850–15500 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل updates والـ branding:</strong> — 70–580 دولار/شهر.</li>
          <li><strong>Vertical kits (investor، sales، onboarding):</strong> — 38–175 دولار/kit.</li>
          <li><strong>دورات «عروض احترافية بالعربية مع Gamma AI»:</strong> — 35–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gamma</span>
        <span class="tag">Presentations</span>
        <span class="tag">Design</span>
        <span class="tag">Consulting</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Mercury AI Treasury 3 Arabic: خزينة ذكية — cash flow، scenarios، وتنبيهات CFO بالعربية!</h2>
      <p class="article-lead">«هل نستطيع دفع الرواتب الشهر القادم؟ — والجدول في Excel قديم». في 8 أكتوبر 2026، أطلقت <strong>Mercury</strong> <strong>AI Treasury 3 Arabic</strong>: طبقة treasury intelligence فوق حسابات Mercury وbank feeds، تُ forecast cash 13-week rolling، تُ model scenarios (تأخر AR، FX، hiring)، تُ alert slack لل CFO بالعربية، تُ suggest payment scheduling، تُ categorize burn drivers، وتُ generate board-ready treasury memo PDF RTL — لل startups US وMENA founders.</p>
      <p>المشكلة التي حلّتها: Treasury 2 كان reports إنجليزية فقط؛ الإصدار 3 يُ Gulf calendar awareness، يُ benchmark 89% forecast accuracy في fintech إماراتية، يُ multi-currency AED/SAR/EGP، يُ integration QuickBooks وXero، ويُ role-based access لل investors read-only.</p>
      <p>القدرات الأساسية: Runway simulator؛ vendor payment optimizer؛ debt covenant watch؛ API embed في founder dashboards؛ scheduled Arabic weekly brief.</p>
      <p>للمبدعين العرب: fractional CFOs — «Mercury Treasury 3 Arabic control tower in 7 days» لل companies 500K–50M ARR. من يُ launch 7 towers/ربع بـ 2100–38000 دولار + managed 110–880 دولار/شهر يبني «مكتب treasury AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Mercury AI Treasury 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة control tower (models، alerts، training):</strong> 5–12 يومًا — 2100–38000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل forecasts والـ reporting:</strong> — 110–880 دولار/شهر.</li>
          <li><strong>Scenario packs (fundraise، expansion، downturn):</strong> — 48–220 دولار/pack.</li>
          <li><strong>دورات «إدارة سيولة بالعربية مع Mercury AI»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Mercury</span>
        <span class="tag">Finance</span>
        <span class="tag">Treasury</span>
        <span class="tag">Startups</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Writer Enterprise 3 Arabic: محتوى مؤسسي — brand voice، compliance، وآلاف الصفحات RTL!</h2>
      <p class="article-lead">«كل فريق يكتب بأسلوب مختلف — والامتثال يرفض النشر». في 8 أكتوبر 2026، أطلقت <strong>Writer</strong> <strong>Enterprise 3 Arabic</strong>: منصة generative AI لل enterprises تُ enforce brand voice وterminology glossary عربي/إنجليزي، تُ generate marketing وsupport وlegal drafts، تُ compliance scan (claims، PII، regulated industries)، تُ translate مع tone preservation، تُ workflow approvals، وتُ analytics على quality scores — لل banks وtelcos وhealthcare في MENA.</p>
      <p>المشكلة التي حلّتها: Enterprise 2 كان Arabic morphology errors في legal text؛ الإصدار 3 يُ legal Arabic templates، يُ benchmark −38% revision cycles في insurer سعودي، يُ RAG على internal knowledge base، يُ red-team prompts، ويُ SSO وdata residency options.</p>
      <p>القدرات الأساسية: Snippets library؛ multi-model routing؛ integration Salesforce وServiceNow؛ API لل portals؛ human review queues؛ export audit logs.</p>
      <p>للمبدعين العرب: content ops consultants — «Writer Enterprise 3 Arabic governance stack in 10 days» لل orgs 200–5000 seats. من يُ deploy 5 stacks/ربع بـ 3200–55000 دولار + governance 150–1200 دولار/شهر يبني «مكتب Writer AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Writer Enterprise 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة governance stack (voice، workflows، training):</strong> 7–18 يومًا — 3200–55000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل glossaries والـ compliance:</strong> — 150–1200 دولار/شهر.</li>
          <li><strong>Industry accelerators (banking، telecom، pharma):</strong> — 65–295 دولار/accelerator.</li>
          <li><strong>دورات «محتوى مؤسسي آمن بالعربية مع Writer»:</strong> — 52–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Writer</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Content</span>
        <span class="tag">Compliance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="08-10-2026 -- 04-PM.html">
          📰 8 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Cursor Bugbot 2 Arabic · Gamma Presentations 4 Arabic · Mercury AI Treasury 3 Arabic · Writer Enterprise 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/08-10-2026 -- 04-PM.html`](news/08-10-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "08-10-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "08-10-2026 -- 04-PM.html" not in content:
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
        "المشk problem",
        "أktober",
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
