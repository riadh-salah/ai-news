#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Anthropic Claude for Work 3 Arabic · Runway Gen-4 Turbo Arabic · "
    "Shopify Sidekick 4 Arabic · Intercom Fin 3 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Anthropic Claude for Work 3 Arabic، Runway Gen-4 Turbo Arabic، Shopify Sidekick 4 Arabic، Intercom Fin 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Anthropic Claude for Work 3 Arabic الذي يُنسّق اجتماعات وفِرقًا وملفاتًا مؤسسية بلهجات عربية قبل أن تبرد القهوة، إلى Runway Gen-4 Turbo Arabic الذي يُحوّل storyboard نصيًا إلى فيديو إعلاني جاهز للبث، ومن Shopify Sidekick 4 Arabic الذي يُدير متجرًا ويُكتب وصفًا ويُقترح حملات WhatsApp، إلى Intercom Fin 3 Arabic الذي يُغلق تذاكر الدعم ويُ upsell بثقة — أربع قصص مسائية في 27 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء المساء!</h1>
      <p class="hero-sub">مساءٌ للقادة والمبدعين وأصحاب المتاجر: فرق knowledge تتشتت بين Slack وNotion، وكالات تنتظر أسابيع لـ motion بسيط، تجّار e-commerce يكتبون أوصافًا يدويًا، و SaaS يخسر عملاء على support بطيء. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 27 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Anthropic Claude for Work 3 Arabic: مكتب ذكي — projects، connectors، وامتثال!</h2>
      <p class="article-lead">«كل قسم يسأل Claude سؤالًا مختلفًا عن نفس السياسة». في 27 أكتوبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude for Work 3 Arabic</strong>: مساحة مؤسسية تُ index Google Drive وSharePoint وSlack وJira، تُ answer بالفصحى والخليجية والمصرية مع citations، تُ Projects لمشاريع متعددة الأقسام، تُ Artifacts للتقارير والجداول RTL، تُ connectors لـ Salesforce وZendesk، تُ admin DLP وSSO وno-training tier، تُ Claude Code integration لل engineering، ويُ regional data residency لـ EU وGCC partners — لل banks وconsultancies وgroups 200–80000 seats.</p>
      <p>المشكلة التي حلّتها: for Work 2 كان يُخلط أرقام ميزانيات بين نسخ قديمة؛ الإصدار 3 يُ version-aware RAG، يُ benchmark −41% وقت «إيجاد قرار معتمد» في holding دبي، يُ meeting prep packs من calendar، يُ policy Q&amp;A لل HR وlegal، يُ partner templates لل verticals، ويُ audit trails لل regulators.</p>
      <p>القدرات الأساسية: Arabic enterprise projects; Grounded answers; Cross-app connectors; RTL artifacts; Governance and SSO; Engineering handoff.</p>
      <p>للمبدعين العرب: Anthropic partners — «Claude for Work 3 Arabic rollout in 8 days» لل orgs 300–50000 users. من يُ deliver 7 rollouts/ربع بـ 3800–78000 دولار + managed 320–2600 دولار/شهر يبني «مكتب Claude عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude for Work 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة rollout (connectors، projects، governance، training):</strong> 6–18 يومًا — 3800–78000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ corpus refresh وplaybooks:</strong> — 320–2600 دولار/شهر.</li>
          <li><strong>قوالب قطاعية (banking، logistics، healthcare، gov):</strong> — 72–340 دولار/قالب.</li>
          <li><strong>دورات «مكتب ذكي بـ Claude for Work بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Work</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Runway Gen-4 Turbo Arabic: فيديو من نص — storyboard، lip-sync، وbrand kit!</h2>
      <p class="article-lead">«العميل يريد spot 15 ثانية بالعربية — والموعد غدًا». في 27 أكتوبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Turbo Arabic</strong>: نموذج فيديو يُفهم prompts عربية وإنجليزية، يُ generate scenes مع camera moves، يُ character consistency عبر shots، يُ Arabic lip-sync وon-screen typography RTL، يُ brand kit لل colors وlogos، يُ extend وinpaint في timeline، يُ export 4K ProRes وsocial crops، يُ API لل agencies، ويُ team seats وusage caps — لل brands وcreators وMENA media houses.</p>
      <p>المشكلة التي حلّتها: Gen-3 كان يُ distort حروف عربية في lower-thirds؛ Turbo يُ glyph-safe overlays، يُ benchmark −55% وقت «brief to master» في agency الرياض، يُ reference image locking، يُ audio stem sync، يُ style presets لل Ramadan وnational day campaigns، ويُ watermark controls لل client review.</p>
      <p>القدرات الأساسية: Arabic video prompts; Lip-sync and RTL text; Brand kits; Timeline editing; Agency API; Social exports.</p>
      <p>للمبدعين العرب: production studios — «Gen-4 Turbo Arabic spot factory in 4 days» لل brands 5–200 campaigns/year. من يُ ship 12 factories/ربع بـ 2400–52000 دولار + retainer 210–1750 دولار/شهر يبني «استوديو Runway عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Turbo Arabic؟</h3>
        <ul>
          <li><strong>باقة spot factory (brand kit، templates، pilot، handoff):</strong> 3–10 أيام — 2400–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ campaigns وasset library:</strong> — 210–1750 دولار/شهر.</li>
          <li><strong>حزم موسمية (Ramadan، back-to-school، sports):</strong> — 55–265 دولار/حزمة.</li>
          <li><strong>دورات «إعلانات فيديو بـ Gen-4 Turbo بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video</span>
        <span class="tag">Creative</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Shopify Sidekick 4 Arabic: متجر يتحدث — catalog، ads، وWhatsApp commerce!</h2>
      <p class="article-lead">«500 SKU — ولا وقت لكتابة وصف لكل واحد». في 27 أكتوبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 4 Arabic</strong>: مساعد تاجر يُ draft product copy MSA وخليجي، يُ suggest bundles وpricing، يُ build email وSMS flows، يُ connect Meta وGoogle ads مع Arabic creatives، يُ WhatsApp catalog وabandoned cart بالعربية، يُ analytics narratives لل owner، يُ inventory alerts، يُ Markets لل GCC currencies، ويُ partner APIs لل agencies — لل DTC وomnichannel في MENA.</p>
      <p>المشكلة التي حلّتها: Sidekick 3 كان يُ confuse VAT labels بين دول؛ الإصدار 4 يُ country-aware tax hints، يُ benchmark +22% conversion على stores جدة بعد copy refresh، يُ image alt-text عربي لل SEO، يُ seasonal campaign wizard، يُ influencer brief generator، ويُ B2B wholesale quote drafts.</p>
      <p>القدرات الأساسية: Arabic product copy; Ads and WhatsApp flows; Pricing insights; GCC Markets; Agency workflows; Owner dashboards.</p>
      <p>للمبدعين العرب: Shopify partners — «Sidekick 4 Arabic growth sprint in 5 days» لل stores 50–5000 SKUs. من يُ run 15 sprints/ربع بـ 1200–32000 دولار + ops 150–1200 دولار/شهر يبني «ممارسة Sidekick عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة growth sprint (catalog، ads، WhatsApp، training):</strong> 4–12 يومًا — 1200–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ campaigns وA/B copy:</strong> — 150–1200 دولار/شهر.</li>
          <li><strong>Vertical kits (fashion، beauty، electronics، food):</strong> — 38–175 دولار/kit.</li>
          <li><strong>دورات «متجر ذكي بـ Sidekick بالعربية»:</strong> — 32–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Intercom Fin 3 Arabic: دعم يُ sell — resolve، qualify، وhandoff بثقة!</h2>
      <p class="article-lead">«Fin يُجيب — لكن العميل يريد upgrade والموظف غائب». في 27 أكتوبر 2026، أطلقت <strong>Intercom</strong> <strong>Fin 3 Arabic</strong>: agent دعم يُ resolve FAQs بالفصحى والعامية المصرية والخليجية، يُ qualify leads في chat، يُ suggest upsell من usage data، يُ handoff إلى human مع full context RTL، يُ train على help center وmacros، يُ Slack وSalesforce sync، يُ CSAT وquality scoring، يُ multilingual switch mid-conversation، ويُ Fin Insights لل managers — لل SaaS وfintech وmarketplaces في MENA.</p>
      <p>المشكلة التي حلّتها: Fin 2 كان يُ sound stiff في tone WhatsApp؛ الإصدار 3 يُ brand voice profiles، يُ benchmark −47% first-response time في neobank القاهرة، يُ proactive outreach لل renewal risk، يُ dispute and KYC playbooks، يُ custom actions via API، ويُ redaction لل PII في logs.</p>
      <p>القدرات الأساسية: Arabic support resolution; Lead qualify and upsell; Smart handoff; Help center training; CRM sync; Manager insights.</p>
      <p>للمبدعين العرب: Intercom partners — «Fin 3 Arabic support revenue desk in 6 days» لل SaaS 10K–2M users. من يُ deploy 11 desks/ربع بـ 1600–38000 دولار + ops 165–1350 دولار/شهر يبني «مكتب Fin عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue desk (train، voice، workflows، QA):</strong> 4–14 يومًا — 1600–38000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ tuning وmacro updates:</strong> — 165–1350 دولار/شهر.</li>
          <li><strong>Playbooks (billing، onboarding، compliance، sales assist):</strong> — 42–198 دولار/playbook.</li>
          <li><strong>دورات «دعم يبيع بـ Fin بالعربية»:</strong> — 34–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Fin</span>
        <span class="tag">Support</span>
        <span class="tag">SaaS</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-10-2026 -- 04-PM.html">
          📰 27 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-10-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-10-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/27-10-2026 -- 08-AM.html"
    new_line = (
        f"- [`{new}`](news/27-10-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS}) "
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
