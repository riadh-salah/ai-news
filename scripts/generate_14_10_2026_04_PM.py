#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 14-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "14-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Atlassian Rovo AI 4 Arabic، GitHub Copilot Workspace 4 Arabic، Klaviyo K:AI Marketing 4 Arabic، Databricks AI/BI Genie 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 14 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Atlassian Rovo AI 4 Arabic الذي يُحوّل سؤالك في Slack إلى ticket مُ assign وصفحة Confluence مُحدّثة قبل أن تُغلق laptop، إلى GitHub Copilot Workspace 4 Arabic الذي يُحوّل «أصلح bug الدفع بالعربية» إلى branch وtests وpull request جاهز للمراجعة، ومن Klaviyo K:AI Marketing 4 Arabic الذي يُ personalizes مليون email وSMS بلهجة خليجية ومصرية من سلوك الشراء الحي، إلى Databricks AI/BI Genie 4 Arabic الذي يُجيب CFO «لماذا هبط margin؟» من warehouse دون SQL — أربع قصص مسائية في 14 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء مع آخر ضوء!</h1>
      <p class="hero-sub">مساءٌ للفرق والمطورين والتسويق والبيانات: Jira مزدحم، backlog يتأخر، حملات email generic، ولوحات BI لا تُ narrate. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 14 أكتوبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Atlassian Rovo AI 4 Arabic: Jira وConfluence وLoom — search وagents وautomation بلسان فريقك!</h2>
      <p class="article-lead">«أين وصلنا في sprint؟ — والمدير ينتظر قبل اجتماع 5 مساءً». في 14 أكتوبر 2026، أطلقت <strong>Atlassian</strong> <strong>Rovo AI 4 Arabic</strong>: طبقة team intelligence فوق Jira وConfluence وBitbucket وLoom، تُ answer بالعربية عن status وblockers وowners، تُ create وupdate issues من natural language، تُ draft specs وmeeting notes RTL، تُ run cross-tool actions (Slack notify، assign، transition)، تُ respect project permissions وaudit — لل software وops وmarketing teams في MENA.</p>
      <p>المشكلة التي حلّتها: Rovo 3 كان يُ confuse بين dialects في comment threads؛ الإصدار 4 يُ semantic search على Arabic attachments، يُ benchmark −47% وقت weekly status prep في fintech دبي، يُ human-in-the-loop لل destructive changes، يُ integration Microsoft Teams وGoogle Chat، يُ custom agents per squad (QA، PM، support)، ويُ analytics على adoption وtime saved.</p>
      <p>القدرات الأساسية: Rovo Chat في browser وmobile; agent templates (incident، release، hiring); Confluence page generator من bullet list عربي; Jira bulk edit آمن; Loom transcript summaries لل standups; API لل internal portals.</p>
      <p>للمبدعين العرب: Atlassian partners — «Rovo AI 4 Arabic team cockpit in 8 days» لل orgs 30–2000 seats. من يُ deploy 7 cockpits/ربع بـ 3200–54000 دولار + care 220–1750 دولار/شهر يبني «مكتب Atlassian AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlassian Rovo AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة team cockpit (Rovo، agents، governance RTL):</strong> 6–14 يومًا — 3200–54000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل agents وknowledge hygiene:</strong> — 220–1750 دولار/شهر.</li>
          <li><strong>Vertical workflow packs (fintech، gaming، gov digital):</strong> — 48–205 دولار/pack.</li>
          <li><strong>دورات «فرق ذكية بـ Atlassian Rovo بالعربية»:</strong> — 44–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atlassian</span>
        <span class="tag">Rovo AI</span>
        <span class="tag">Jira</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>GitHub Copilot Workspace 4 Arabic: من issue إلى merge — planning وcoding وreview بلسان المهندس!</h2>
      <p class="article-lead">«Ticket بالعربية — والـ PR بالإنجليزية فقط». في 14 أكتوبر 2026، أطلقت <strong>GitHub</strong> <strong>Copilot Workspace 4 Arabic</strong>: بيئة agentic dev تُ ingest issue وrepo context، تُ plan steps بالعربية أو الإنجليزية، تُ generate code وtests وdocs، تُ run CI previews، تُ open pull request مع summary RTL لل reviewers، تُ iterate من comments في PR — لل startups وenterprises وagencies في المنطقة.</p>
      <p>المشكلة التي حلّتها: Workspace 3 كان يُ drift على legacy monoliths؛ الإصدار 4 يُ repo map وdependency graph، يُ benchmark −36% cycle time في payments startup قاهرة، يُ policy gates (secrets scan، license check)، يُ integration Jira وLinear وAzure DevOps، يُ Arabic commit messages وrelease notes، ويُ sandbox لل risky migrations.</p>
      <p>القدرات الأساسية: Multi-file edits مع diff review; test generation pytest/Jest; security fix suggestions; migration assistants (Node، Python); team playbooks قابلة للمشاركة; Enterprise SSO وaudit logs.</p>
      <p>للمبدعين العرب: dev shops — «Copilot Workspace 4 Arabic velocity pack in 5 days» لل teams 5–80 engineers. من يُ onboard 9 packs/ربع بـ 2800–48000 دولار + retainer 190–1550 دولار/شهر يبني «استوديو GitHub AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitHub Copilot Workspace 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة velocity pack (Workspace، playbooks، training RTL):</strong> 4–11 يومًا — 2800–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل guardrails وprompt libraries:</strong> — 190–1550 دولار/شهر.</li>
          <li><strong>Stack starter kits (Next.js، Laravel، mobile):</strong> — 55–230 دولار/kit.</li>
          <li><strong>دورات «تطوير agentic بـ Copilot Workspace بالعربية»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitHub</span>
        <span class="tag">Copilot Workspace</span>
        <span class="tag">DevTools</span>
        <span class="tag">Engineering</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Klaviyo K:AI Marketing 4 Arabic: email وSMS وpush — personalization وflows بلهجة عميلك!</h2>
      <p class="article-lead">«حملة Ramadan — ونفس النص لكل مدينة». في 14 أكتوبر 2026، أطلقت <strong>Klaviyo</strong> <strong>K:AI Marketing 4 Arabic</strong>: marketing AI فوق CDP يُ segment بالعربية (MSA، خليجي، مصري)، يُ generate subject lines وbody copy RTL، يُ predict send time per user، يُ build flows (cart abandon، win-back، VIP) من prompt، يُ sync Shopify وSalla وWooCommerce وcustom APIs — لل D2C وretail وsubscription brands في MENA.</p>
      <p>المشكلة التي حلّتها: K:AI 2 كان يُ break على mixed RTL/LTR product names؛ الإصدار 4 يُ bidi-safe templates، يُ benchmark +31% revenue per recipient في beauty e-commerce سعودي، يُ A/B multivariate auto-optimize، يُ WhatsApp وRCS hooks (where enabled)، يُ compliance unsubscribe وconsent Arabic، ويُ analyst chat «لماذا تراجع open rate؟».</p>
      <p>القدرات الأساسية: Campaign brief-to-send في دقائق; predictive CLV; influencer coupon attribution; image variants من catalog; API لل agencies; deliverability monitoring MENA ISPs.</p>
      <p>للمبدعين العرب: email agencies — «K:AI 4 Arabic revenue engine in 7 days» لل stores 10k–2M profiles. من يُ launch 10 engines/ربع بـ 1800–32000 دولار + ops 160–1300 دولار/شهر يبني «غرفة Klaviyo AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Klaviyo K:AI Marketing 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue engine (K:AI، flows، templates RTL):</strong> 5–13 يومًا — 1800–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل campaigns وsegment tuning:</strong> — 160–1300 دولار/شهر.</li>
          <li><strong>Seasonal playbooks (Ramadan، White Friday، National Day):</strong> — 42–185 دولار/playbook.</li>
          <li><strong>دورات «تسويق lifecycle ذكي بـ Klaviyo K:AI بالعربية»:</strong> — 40–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Klaviyo</span>
        <span class="tag">K:AI</span>
        <span class="tag">Email</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Databricks AI/BI Genie 4 Arabic: أسئلة CFO بالعربية — SQL وcharts وforecasts من warehouse!</h2>
      <p class="article-lead">«لماذا هبط gross margin في Q3؟ — والمحلل مشغول حتى الغد». في 14 أكتوبر 2026، أطلقت <strong>Databricks</strong> <strong>AI/BI Genie 4 Arabic</strong>: conversational analytics فوق Unity Catalog يُ parse أسئلة finance وops وsales بالعربية، يُ generate governed SQL، يُ produce dashboards وnarratives RTL، يُ run what-if scenarios، يُ alert anomalies إلى Slack وTeams، يُ keep data in-place (no export shadow) — لل retail وlogistics وtelecom في المنطقة.</p>
      <p>المشكلة التي حلّتها: Genie 3 كان يُ hallucinate على Arabic column aliases؛ الإصدار 4 يُ semantic layer MENA، يُ benchmark −44% وقت board prep في logistics UAE، يُ row-level security Arabic labels، يُ integration Power BI وTableau embed، يُ certified metrics library، ويُ mobile voice ask لل executives.</p>
      <p>القدرات الأساسية: Genie spaces per department; certified answers; lineage explanations; scheduled briefs صباحية; API لل internal copilots; Delta Live Tables awareness.</p>
      <p>للمبدعين العرب: data consultancies — «Genie 4 Arabic insights fabric in 12 days» لل orgs 5–500 TB. من يُ deliver 5 fabrics/ربع بـ 5200–85000 دولار + managed 350–2700 دولار/شهر يبني «ممارسة Databricks AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Databricks AI/BI Genie 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة insights fabric (Genie، semantic layer، training RTL):</strong> 9–20 يومًا — 5200–85000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل metrics وgovernance:</strong> — 350–2700 دولار/شهر.</li>
          <li><strong>Industry metric packs (CPG، telco، healthcare):</strong> — 72–295 دولار/pack.</li>
          <li><strong>دورات «تحليل ذكي بـ Databricks Genie بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Databricks</span>
        <span class="tag">Genie</span>
        <span class="tag">Analytics</span>
        <span class="tag">Data</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 14-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="14-10-2026 -- 04-PM.html">
          📰 14 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Atlassian Rovo AI 4 Arabic · GitHub Copilot Workspace 4 Arabic · Klaviyo K:AI Marketing 4 Arabic · Databricks AI/BI Genie 4 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/14-10-2026 -- 04-PM.html`](news/14-10-2026%20--%2004-PM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "14-10-2026 -- 04-PM.html" not in content:
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
    if new_content == content and "14-10-2026 -- 04-PM.html" not in content:
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
    if data[:2] == b"\xff\xfe" or data[:2] == b"\xfe\xff":
        raise SystemExit("ERROR: UTF-16 BOM detected")
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
        "Arbs:",
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
        "traduce",
        "oktober",
        "Oktober",
        "mezclar",
        "إنجlizi",
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
