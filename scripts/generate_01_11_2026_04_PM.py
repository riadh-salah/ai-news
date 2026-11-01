#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 01-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "01-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Notion AI Q&amp;A Hub 3 Arabic · Shopify Sidekick 3 Arabic · "
    "Runway Gen-4 Turbo Arabic · HubSpot Breeze Agents 2 Arabic"
)

TOPICS_PLAIN = (
    "Notion AI Q&A Hub 3 Arabic · Shopify Sidekick 3 Arabic · "
    "Runway Gen-4 Turbo Arabic · HubSpot Breeze Agents 2 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Notion AI Q&amp;A Hub 3 Arabic، Shopify Sidekick 3 Arabic، Runway Gen-4 Turbo Arabic، HubSpot Breeze Agents 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 1 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Notion AI Q&amp;A Hub 3 Arabic الذي يُحوّل wiki الشركة إلى مساعد يُجيب بالفصحى قبل أن ينتهي اجتماع standup، إلى Shopify Sidekick 3 Arabic الذي يُ draft متاجر وcampaigns وproduct copy للخليج في دقائق، ومن Runway Gen-4 Turbo Arabic الذي يُ birth مشاهد فيديو cinematic من storyboard عربي، إلى HubSpot Breeze Agents 2 Arabic الذي يُ nurture leads ويُ book meetings بلسان sales team — أربع قصص مسائية في 1 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ لفرق المعرفة والتجارة الإلكترونية والإبداع والمبيعات: docs مبعثرة، conversion يتأخر، reels تنتظر editor، وCRM يغرق في follow-ups يدوية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 1 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Notion AI Q&amp;A Hub 3 Arabic: ذاكرة الشركة حية — أسئلة، ملخصات، وSOPs بفصحى واضحة!</h2>
      <p class="article-lead">«أين policy الإجازات المحدّثة؟ — والموظف ينتظر في Slack». في 1 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>AI Q&amp;A Hub 3 Arabic</strong>: طبقة knowledge داخل workspace يُ index pages وdatabases وPDFs وSlack exports، يُ answer بالعربية مع citations لكل block، يُ summarize meeting notes RTL، يُ suggest SOP updates عند drift، يُ permission-aware search (HR vs engineering)، يُ connect Google Drive وConfluence وGitHub wikis، يُ audit who asked what، ويُ enterprise SSO مع data residency — لل scale-ups وNGOs وuniversities في MENA.</p>
      <p>المشكلة التي حلّتها: Hub 2 كان يُ confuse بين MSA وdialect في HR policies؛ الإصدار 3 يُ bilingual glossary locks، يُ benchmark −44% وقت «سؤال إلى إجابة موثقة» في edtech القاهرة، يُ auto-archive stale pages، يُ copilot في Slack وTeams، يُ template packs (onboarding، compliance، product)، ويُ partner certifications لل consultants.</p>
      <p>القدرات الأساسية: Arabic grounded Q&amp;A; Cited answers; SOP drift detection; Permission-aware retrieval; Integrations hub; Enterprise governance.</p>
      <p>للمبدعين العرب: ops consultants — «Notion Q&amp;A Hub 3 Arabic knowledge sprint in 5 days» لل orgs 50–5000 seats. من يُ deliver 10 sprints/ربع بـ 1800–32000 دولار + retainer 150–1250 دولار/شهر يبني «مكتب Notion AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Q&amp;A Hub 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة knowledge sprint (taxonomy، connectors، UAT، training):</strong> 4–12 يومًا — 1800–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ corpus refresh وquality reviews:</strong> — 150–1250 دولار/شهر.</li>
          <li><strong>حزم قطاعية (HR، legal ops، product، customer support):</strong> — 38–175 دولار/حزمة.</li>
          <li><strong>دورات «بناء wiki ذكي بـ Notion Q&amp;A بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Knowledge</span>
        <span class="tag">RAG</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick 3 Arabic: شريك متجر ذكي — products، ads، وsupport بلهجة العميل!</h2>
      <p class="article-lead">«نريد launch collection رمضان — 120 SKU والفريق صغير». في 1 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: merchant copilot يُ draft product descriptions وSEO بالفصحى والخليجية، يُ generate theme sections وhero banners RTL، يُ suggest ad copy لـ Meta وSnap وTikTok، يُ answer merchant questions («لماذا انخفض conversion؟») مع analytics citations، يُ automate support macros لل dialects، يُ inventory alerts وreorder hints، يُ integrate Shopify Flow وMarkets multi-currency، ويُ Plus VPC لل enterprise brands في MENA.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان inconsistent في Arabic product titles؛ الإصدار 3 يُ brand voice lock، يُ benchmark −41% time-to-launch في fashion D2C الرياض، يُ Sharia-friendly promo checks optional، يُ A/B variant generator، يُ marketplace playbooks لل agencies، ويُ revenue share لل template authors.</p>
      <p>القدرات الأساسية: Arabic merchandising copy; Theme and creative drafts; Ads variants; Analytics Q&amp;A; Support automation; Markets and Flow.</p>
      <p>للمبدعين العرب: ecommerce agencies — «Sidekick 3 Arabic store accelerator in 6 days» لل merchants 500–50000 orders/month. من يُ run 14 accelerators/ربع بـ 2200–45000 دولار + ops 180–1500 دولار/شهر يبني «استوديو Shopify AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة store accelerator (voice، catalog، ads pilot، analytics):</strong> 5–16 يومًا — 2200–45000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ seasonal campaigns وcatalog tuning:</strong> — 180–1500 دولار/شهر.</li>
          <li><strong>Vertical packs (beauty، electronics، food، modest fashion):</strong> — 35–168 دولار/pack.</li>
          <li><strong>دورات «تجارة AI بـ Sidekick 3 بالعربية»:</strong> — 40–185 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Ecommerce</span>
        <span class="tag">Merchants</span>
        <span class="tag">Copilot</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Runway Gen-4 Turbo Arabic: فيديو سريع — scenes، motion، وcaptions RTL بجودة broadcast!</h2>
      <p class="article-lead">«العميل يريد spot 20 ثانية بالعربية — والdeadline قبل 24 ساعة». في 1 نوفمبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Turbo Arabic</strong>: video stack يُ generate clips من prompt أو reference image، يُ character lock عبر shots، يُ camera paths cinematic، يُ Arabic typography-safe overlays، يُ auto captions RTL وsafe zones، يُ extend وinpaint، يُ brand palette وLUT packs، يُ team seats لل agencies، يُ API batch لل catalogs، ويُ commercial tiers لل broadcast وsocial في MENA.</p>
      <p>المشكلة التي حلّتها: Gen-3 Turbo كان يُ drift في Gulf vs Egyptian lip-sync previews؛ Gen-4 Turbo يُ dialect-aware TTS pairing، يُ benchmark −58% cost per finished second في agency دبي، يُ moderation filters، يُ template packs (product hero، tourism، fintech explainer)، ويُ partner program لل MENA creators.</p>
      <p>القدرات الأساسية: Arabic text-to-video turbo; Character consistency; RTL captions; Brand controls; Agency workspaces; API scale.</p>
      <p>للمبدعين العرب: video studios — «Gen-4 Turbo Arabic sprint in 3 days» لل clients 6–60 assets/month. من يُ ship 18 sprints/ربع بـ 1100–28000 دولار + ops 130–1050 دولار/شهر يبني «استوديو Runway عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Turbo Arabic؟</h3>
        <ul>
          <li><strong>باقة video sprint (storyboard، brand kit، pilot renders، handoff):</strong> 2–8 أيام — 1100–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ variants وperformance tuning:</strong> — 130–1050 دولار/شهر.</li>
          <li><strong>Vertical packs (hospitality، gaming، real estate، NGOs):</strong> — 32–155 دولار/pack.</li>
          <li><strong>دورات «إنتاج فيديو AI بـ Gen-4 Turbo بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Video AI</span>
        <span class="tag">Creative</span>
        <span class="tag">Turbo</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>HubSpot Breeze Agents 2 Arabic: فريق مبيعات رقمي — prospect، nurture، وbook بلسان عربي!</h2>
      <p class="article-lead">«300 lead جديد — و3 SDRs فقط». في 1 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze Agents 2 Arabic</strong>: agents داخل CRM يُ research accounts بالعربية، يُ draft personalized emails وWhatsApp templates RTL، يُ score intent من website وemail engagement، يُ schedule meetings مع calendar rules، يُ summarize calls وnext steps، يُ sync Marketing Hub وService Hub، يُ compliance logs وopt-out respect، ويُ enterprise data residency — لل B2B SaaS وreal estate وeducation في MENA.</p>
      <p>المشكلة التي حلّتها: Breeze Agents 1 كان English-first في sequences؛ الإصدار 2 يُ bilingual sequence branching، يُ benchmark −37% time-to-first-meeting في SaaS عمّان، يُ Arabic objection handling playbooks، يُ human approval gates، يُ API لل BI، ويُ marketplace templates لل agencies.</p>
      <p>القدرات الأساسية: Arabic prospect research; Personalized outreach RTL; Intent scoring; Meeting automation; Call summaries; Hub integrations.</p>
      <p>للمبدعين العرب: RevOps consultants — «Breeze Agents 2 Arabic pipeline kit in 7 days» لل teams 5–200 reps. من يُ deliver 8 kits/ربع بـ 3400–62000 دولار + managed 280–2200 دولار/شهر يبني «غرفة HubSpot AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze Agents 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة pipeline kit (ICP، sequences، integrations، UAT):</strong> 5–18 يومًا — 3400–62000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ sequence tuning وQA:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Starter playbooks (SaaS، proptech، clinics، training centers):</strong> — 55–240 دولار/playbook.</li>
          <li><strong>دورات «مبيعات AI بـ Breeze Agents بالعربية»:</strong> — 48–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Sales AI</span>
        <span class="tag">CRM</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 01-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="01-11-2026 -- 04-PM.html">
          📰 1 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "01-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/01-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/01-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
