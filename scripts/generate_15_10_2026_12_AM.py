#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 15-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "15-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Glean AI 4 Arabic، Workday Illuminate AI 4 Arabic، Stripe Billing AI Copilot 4 Arabic، ClickUp Brain 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 15 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Glean AI 4 Arabic الذي يُ hunt إجابة «أين policy الإجازات؟» عبر Slack وDrive وConfluence قبل أن تُطفأ شاشة المكتب، إلى Workday Illuminate AI 4 Arabic الذي يُفسر payroll وbenefits بلسان الموظف والمدير، ومن Stripe Billing AI Copilot 4 Arabic الذي يُ translate churn وdunning إلى cashflow واضح بلهجة CFO، إلى ClickUp Brain 4 Arabic الذي يُحوّل chaos الـ Slack إلى sprint plan وowners وdeadlines — أربع قصص ليلية في 15 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمعرفة والموارد البشرية والاشتراكات والمشاريع: docs مبعثرة، HR tickets متكررة، MRR يتسرب، والمهام تضيع في threads. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 15 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Glean AI 4 Arabic: بحث enterprise ذكي — إجابات موثّقة من Slack وDrive وNotion!</h2>
      <p class="article-lead">«الملف موجود في مكان ما — واجتماعك بعد ساعتين». في 15 أكتوبر 2026، أطلقت <strong>Glean</strong> <strong>AI 4 Arabic</strong>: طبقة knowledge intelligence تُ index docs وtickets وmessages وcode، تُ answer بالعربية مع citations وpermissions، تُ summarize threads طويلة، تُ suggest experts داخل الشركة، تُ respect SSO وDLP — لل enterprises وscale-ups في MENA التي تغرق في silos.</p>
      <p>المشكلة التي حلّتها: Glean 3 كان يُ miss Arabic PDFs الممسوحة؛ الإصدار 4 يُ OCR عربي محسّن، يُ benchmark −52% وقت «البحث عن policy» في telco الرياض، يُ personal results حسب role، يُ integration Microsoft 365 وGoogle Workspace وSalesforce وJira، يُ agents لل onboarding وIT FAQ، ويُ analytics على knowledge gaps.</p>
      <p>القدرات الأساسية: Glean Chat في browser وSlack; semantic search عبر 100+ connectors; Arabic snippet highlights RTL; expert finder; scheduled digests صباحية; API لل internal portals; audit logs enterprise.</p>
      <p>للمبدعين العرب: IT consultancies — «Glean AI 4 Arabic knowledge fabric in 10 days» لل orgs 500–50000 seats. من يُ deploy 6 fabrics/ربع بـ 4800–72000 دولار + care 280–2200 دولار/شهر يبني «مكتب Glean AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Glean AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة knowledge fabric (connectors، governance، training RTL):</strong> 8–18 يومًا — 4800–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل indexing وpermission hygiene:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Department starter packs (legal، HR، sales enablement):</strong> — 58–240 دولار/pack.</li>
          <li><strong>دورات «بحث مؤسسي ذكي بـ Glean بالعربية»:</strong> — 46–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Glean</span>
        <span class="tag">Enterprise Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Workday Illuminate AI 4 Arabic: HR وpayroll وtalent — copilot يُفهم policies بلهجة الموظف!</h2>
      <p class="article-lead">«كم رصيد إجازتي؟ — وHR نائمة». في 15 أكتوبر 2026، أطلقت <strong>Workday</strong> <strong>Illuminate AI 4 Arabic</strong>: مساعد workforce داخل HCM يُ answer عن leave وpay slips وbenefits وorg chart بالعربية (MSA، خليجي، مصري)، يُ draft job descriptions وperformance reviews RTL، يُ guide managers في compensation cycles، يُ automate case routing — لل multinationals وgov entities في المنطقة.</p>
      <p>المشكلة التي حلّتها: Illuminate 3 كان يُ confuse بين nationalities في visa policies؛ الإصدار 4 يُ country packs MENA، يُ benchmark −41% tickets HR tier-1 في banking دبي، يُ human escalation لل sensitive cases، يُ integration Slack وTeams وWhatsApp Business (where approved)، يُ manager nudges لل reviews، ويُ analytics على employee sentiment.</p>
      <p>القدرات الأساسية: Employee self-service chat; manager copilot لل headcount planning; Arabic offer letters; skills graph suggestions; compliance reminders; mobile voice ask.</p>
      <p>للمبدعين العرب: HR tech partners — «Illuminate AI 4 Arabic people stack in 14 days» لل orgs 2000–80000 workers. من يُ go-live 4 stacks/ربع بـ 6200–95000 دولار + managed 380–2900 دولار/شهر يبني «ممارسة Workday AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Workday Illuminate AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة people stack (Illuminate، policies RTL، change mgmt):</strong> 10–22 يومًا — 6200–95000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل content وpolicy updates:</strong> — 380–2900 دولار/شهر.</li>
          <li><strong>Country compliance kits (KSA، UAE، Egypt):</strong> — 85–320 دولار/kit.</li>
          <li><strong>دورات «HR copilot بـ Workday Illuminate بالعربية»:</strong> — 50–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Workday</span>
        <span class="tag">Illuminate</span>
        <span class="tag">HR</span>
        <span class="tag">HCM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Stripe Billing AI Copilot 4 Arabic: MRR وchurn وdunning — finance copilot لاشتراكات SaaS!</h2>
      <p class="article-lead">«الإيراد الشهري هبط — ولا أحد يعرف لماذا». في 15 أكتوبر 2026، أطلقت <strong>Stripe</strong> <strong>Billing AI Copilot 4 Arabic</strong>: طبقة revenue intelligence فوق Billing وRevenue Recognition، تُ explain MRR movements بالعربية، تُ recommend dunning وpricing experiments، تُ forecast cash وLTV، تُ draft customer emails RTL لل failed payments، تُ sync HubSpot وSalesforce — لل SaaS وmarketplaces وsubscription media في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot 2 كان يُ lag على multi-currency MENA; الإصدار 4 يُ SAR/AED/EGP native، يُ benchmark +27% recovery على failed cards في edtech قطر، يُ cohort analysis بالعربية، يُ alert anomalies إلى Slack، يُ scenario «ماذا لو رفعنا السعر 10%؟»، ويُ PCI-safe — no card data in prompts.</p>
      <p>القدرات الأساسية: Revenue narrative dashboards RTL; smart retries; coupon abuse detection; Arabic invoice footnotes; API لل finance copilots; Stripe Sigma queries بالعربية natural language.</p>
      <p>للمبدعين العرب: fintech agencies — «Billing AI Copilot 4 Arabic revenue cockpit in 6 days» لل SaaS 50k–20M ARR. من يُ launch 8 cockpits/ربع بـ 2400–42000 دولار + ops 200–1650 دولار/شهر يبني «غرفة Stripe AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe Billing AI Copilot 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue cockpit (Copilot، dunning، dashboards RTL):</strong> 4–12 يومًا — 2400–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل experiments وreporting:</strong> — 200–1650 دولار/شهر.</li>
          <li><strong>Vertical playbooks (SaaS، marketplace، media):</strong> — 45–195 دولار/playbook.</li>
          <li><strong>دورات «اشتراكات ذكية بـ Stripe Billing AI بالعربية»:</strong> — 42–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Billing</span>
        <span class="tag">SaaS</span>
        <span class="tag">Revenue</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ClickUp Brain 4 Arabic: عقل المشروع — من Slack chaos إلى sprint وdocs وgoals!</h2>
      <p class="article-lead">«200 رسالة — ولا task واضح». في 15 أكتوبر 2026، أطلقت <strong>ClickUp</strong> <strong>Brain 4 Arabic</strong>: AI layer فوق workspace يُ ingest chats وemails وdocs، يُ generate project plans وtasks بالعربية، يُ assign owners وdue dates، يُ write status reports RTL، يُ connect goals وOKRs، يُ standup summaries — لل agencies وproduct teams وops في المنطقة.</p>
      <p>المشكلة التي حلّتها: Brain 3 كان يُ over-create tasks; الإصدار 4 يُ dedupe وmerge، يُ benchmark −38% وقت weekly planning في creative agency بيروت، يُ templates MENA (Ramadan campaigns، gov RFPs)، يُ integration GitHub وFigma وGoogle Calendar، يُ voice capture mobile، ويُ privacy tiers per space.</p>
      <p>القدرات الأساسية: Brain Ask across spaces; auto-docs من meetings; risk flags على delayed milestones; Arabic Gantt narratives; client portal summaries; API لل automations.</p>
      <p>للمبدعين العرب: PM boutiques — «Brain 4 Arabic velocity workspace in 5 days» لل teams 10–400 users. من يُ onboard 12 workspaces/ربع بـ 1400–26000 دولار + ops 110–880 دولار/شهر يبني «استوديو ClickUp AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ClickUp Brain 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة velocity workspace (Brain، templates، training RTL):</strong> 3–10 أيام — 1400–26000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل workflows وhygiene:</strong> — 110–880 دولار/شهر.</li>
          <li><strong>Industry templates (agency، construction، ecommerce ops):</strong> — 38–168 دولار/template.</li>
          <li><strong>دورات «إدارة مشاريع بـ ClickUp Brain بالعربية»:</strong> — 36–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ClickUp</span>
        <span class="tag">Brain</span>
        <span class="tag">PM</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 15-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="15-10-2026 -- 12-AM.html">
          📰 15 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Glean AI 4 Arabic · Workday Illuminate AI 4 Arabic · Stripe Billing AI Copilot 4 Arabic · ClickUp Brain 4 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/15-10-2026 -- 12-AM.html`](news/15-10-2026%20--%2012-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "15-10-2026 -- 12-AM.html" not in content:
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
    if new_content == content and "15-10-2026 -- 12-AM.html" not in content:
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
