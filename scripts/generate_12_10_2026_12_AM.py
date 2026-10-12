#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 12-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "12-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Notion AI Agents 4 Arabic، Shopify Sidekick 4 Arabic، Zoom AI Companion 4 Arabic، Intercom Fin 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 12 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Notion AI Agents 4 Arabic الذي يُحوّل قاعدة المعرفة إلى فريق يعمل بينما أنت نائم، إلى Shopify Sidekick 4 Arabic الذي يُ draft متجرًا وcampaigns RTL قبل الفجر، ومن Zoom AI Companion 4 Arabic الذي يُلخّص اجتماعات متعددة اللغات إلى قرارات عربية، إلى Intercom Fin 4 Arabic الذي يُغلق تذاكر الدعم بثقة موثّقة — أربع قصص ليلية في 12 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء مع أول إشعار صباحي!</h1>
      <p class="hero-sub">ليلٌ للمبدعين والتجّار: وثائق مبعثرة، متاجر بلا conversion، اجتماعات بلا follow-up، ودعم عملاء يأكل الهامش. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 12 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Notion AI Agents 4 Arabic: وكلاء على قاعدة المعرفة — مهام، تقارير، وsync بلا copy-paste!</h2>
      <p class="article-lead">«ثلاثمئة صفحة SOP — ولا أحد يعرف أين آخر تحديث». في 12 أكتوبر 2026، أطلقت <strong>Notion</strong> <strong>AI Agents 4 Arabic</strong>: وكلاء autonomous يقرأون databases وwikis بالفصحى واللهجات، يُ draft PRDs وstatus reports RTL، يُ assign tasks في Notion Projects، يُ sync Slack وemail summaries، يُ answer أسئلة الفريق مع citations من الصفحات، ويُ handoff إلى human عند قرارات حساسة — لل agencies وproduct teams وremote orgs في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 3 كان يُ hallucinate على permissions معقدة؛ الإصدار 4 يُ grounded على workspace ACLs، يُ benchmark −44% وقت البحث عن معلومة في scale-up أردني، يُ Arabic tone presets، يُ audit log لكل تعديل، ويُ templates لـ OKRs وclient portals.</p>
      <p>القدرات الأساسية: Multi-agent workflows (research + writer + reviewer); scheduled digests بالعربية; integration Google Drive وFigma links; sandbox قبل production; export PDF RTL لل boards.</p>
      <p>للمبدعين العرب: Notion consultants — «AI Agents 4 Arabic knowledge ops in 5 days» لل teams 10–800 seats. من يُ deploy 10 workspaces/ربع بـ 1400–42000 دولار + retainer 180–980 دولار/شهر يبني «استوديو Notion AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة knowledge ops (structure، agents، training):</strong> 4–12 يومًا — 1400–42000 دولار/عميل.</li>
          <li><strong>رعاية شهرية لل templates والحوكمة:</strong> — 180–980 دولار/شهر.</li>
          <li><strong>حزم قطاعية (legal، HR، PMO):</strong> — 48–220 دولار/حزمة.</li>
          <li><strong>دورات «إدارة معرفة AI بالعربية على Notion»:</strong> — 42–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Agents</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick 4 Arabic: شريك متجر ذكي — themes، SEO، وcampaigns RTL في جلسة واحدة!</h2>
      <p class="article-lead">«السلة تُ abandon — والـ theme لا يُ convince». في 12 أكتوبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 4 Arabic</strong>: copilot داخل Admin يُ generate product descriptions باللهجات، يُ suggest bundles وupsells، يُ optimize collections لـ SEO عربي، يُ draft email وWhatsApp flows، يُ analyze analytics بلغة تاجر مفهومة، ويُ connect Markets وTranslate &amp; Adapt — لل DTC وmarketplaces وomni-channel في MENA.</p>
      <p>المشكلة التي حلّتها: Sidekick 3 كان يخلط اللهجات في CTAs؛ الإصدار 4 يُ brand voice من catalog history، يُ benchmark +31% add-to-cart في fashion خليجي، يُ image alt-text Arabic، يُ compliance hints لل VAT وreturns، ويُ A/B suggestions مع Shopify Functions.</p>
      <p>القدرات الأساسية: Theme section drafts RTL; inventory alerts narratives; influencer brief generator; integration Meta وTikTok ads copy; mobile merchant app voice queries.</p>
      <p>للمبدعين العرب: Shopify partners — «Sidekick 4 Arabic growth sprint in 6 days» لل stores 500–500K SKUs. من يُ launch 12 stores/ربع بـ 900–28000 دولار + managed 120–860 دولار/شهر يبني «وكالة Sidekick عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة growth sprint (catalog، Sidekick، ads hooks):</strong> 3–10 أيام — 900–28000 دولار/متجر.</li>
          <li><strong>تشغيل شهري لل SEO والحملات:</strong> — 120–860 دولار/شهر.</li>
          <li><strong>Playbooks vertical (beauty، electronics، food):</strong> — 38–175 دولار/playbook.</li>
          <li><strong>دورات «تجارة AI بالعربية مع Sidekick»:</strong> — 35–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Zoom AI Companion 4 Arabic: اجتماعات تُ translate نفسها — summaries، actions، وCRM sync!</h2>
      <p class="article-lead">«ساعتان Zoom — ولا أحد كتب المهام». في 12 أكتوبر 2026، أطلقت <strong>Zoom</strong> <strong>AI Companion 4 Arabic</strong>: suite موحّدة تُ transcribe عربي/إنجلizi/فرنسي mixed، تُ draft meeting summaries RTL، تُ extract action items مع owners، تُ suggest follow-up emails، تُ sync Salesforce وHubSpot، تُ coach presenters على clarity، وتُ power Zoom Rooms digital signage — لل sales وeducation وhealthcare telehealth في MENA.</p>
      <p>المشكلة التي حلّتها: Companion 3 كان يُ drop names عربية؛ الإصدار 4 يُ custom vocabulary وparticipant roster، يُ benchmark −52% وقت كتابة المحاضر في bank مغربي، يُ HIPAA-ready modes، يُ team analytics بالعربية، ويُ clip highlights لـ L&amp;D.</p>
      <p>القدرات الأساسية: Live translation captions RTL; async video chapters; integration Microsoft Teams cross-post; governance retention policies; API webhooks لل internal tools.</p>
      <p>للمبدعين العرب: AV integrators وL&amp;D shops — «Companion 4 Arabic meeting ops in 4 days» لل orgs 50–20000 licenses. من يُ roll out 8 accounts/ربع بـ 2200–48000 دولار + support 210–1450 دولار/شهر يبني «مركز Zoom AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoom AI Companion 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة meeting ops (Companion، CRM، training):</strong> 3–9 أيام — 2200–48000 دولار/عميل.</li>
          <li><strong>دعم شهري لل governance والتكاملات:</strong> — 210–1450 دولار/شهر.</li>
          <li><strong>Templates (sales، board، classroom):</strong> — 52–240 دولار/template.</li>
          <li><strong>دورات «اجتماعات ذكية بالعربية مع Zoom»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zoom</span>
        <span class="tag">AI Companion</span>
        <span class="tag">Meetings</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Intercom Fin 4 Arabic: وكيل دعم يُجيب بثقة — RAG، handoff، وCSAT يصعد!</h2>
      <p class="article-lead">«500 تذكرة — والـ queue لا ينام». في 12 أكتوبر 2026، أطلقت <strong>Intercom</strong> <strong>Fin 4 Arabic</strong>: AI agent يُ answer من help center وmacros وConversations history بالفصحى واللهجات، يُ cite sources inline RTL، يُ escalate إلى human مع full context، يُ suggest macros لل agents، يُ analyze CSAT root causes، ويُ connect WhatsApp وInstagram DMs — لل SaaS وfintech وtravel في MENA.</p>
      <p>المشكلة التي حلّتها: Fin 3 كان يُ over-promise refunds؛ الإصدار 4 يُ policy guardrails وapproval workflows، يُ benchmark +38% first-contact resolution في neobank إماراتي، يُ tone empathy presets، يُ multilingual routing، ويُ Fin Insights dashboards بالعربية.</p>
      <p>القدرات الأساسية: Custom Fin tasks (billing lookup، order status); proactive outbound messages; integration Stripe وShopify; simulation قبل go-live; SOC2 وdata residency options.</p>
      <p>للمبدعين العرب: CX agencies — «Fin 4 Arabic support transformation in 7 days» لل brands 5K–2M tickets/year. من يُ deliver 6 programs/ربع بـ 3200–72000 دولار + ops 260–2100 دولار/شهر يبني «مكتب Fin عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة support AI (content، Fin، QA):</strong> 5–14 يومًا — 3200–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل macros والتحليلات:</strong> — 260–2100 دولار/شهر.</li>
          <li><strong>Runbooks (billing، logistics، onboarding):</strong> — 62–285 دولار/runbook.</li>
          <li><strong>دورات «دعم AI بالعربية مع Fin»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Fin</span>
        <span class="tag">Support</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 12-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="12-10-2026 -- 12-AM.html">
          📰 12 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Notion AI Agents 4 Arabic · Shopify Sidekick 4 Arabic · Zoom AI Companion 4 Arabic · Intercom Fin 4 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/12-10-2026 -- 12-AM.html`](news/12-10-2026%20--%2012-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "12-10-2026 -- 12-AM.html" not in content:
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
    if new_content == content and "12-10-2026 -- 12-AM.html" not in content:
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
        "إنجليزي",
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
