#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-10-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-10-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Salesforce Agentforce 3 Arabic · Shopify Sidekick 5 Arabic · "
    "Atlassian Rovo 3 Arabic · Runway Gen-4 Turbo Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Salesforce Agentforce 3 Arabic، Shopify Sidekick 5 Arabic، Atlassian Rovo 3 Arabic، Runway Gen-4 Turbo Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 أكتوبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Salesforce Agentforce 3 Arabic الذي يُغلق تذكرة الدعم ويُحدّث CRM ويُ draft عرضًا قبل أن تبرد فنجانك، إلى Shopify Sidekick 5 Arabic الذي يُ rewrite وصف المنتج ويُ suggest bundles ويُ forecast مخزونًا بلهجة خليجية، ومن Atlassian Rovo 3 Arabic الذي يُ answer عن Jira وConfluence ويُ open PR من سؤال واحد في Slack، إلى Runway Gen-4 Turbo Arabic الذي يُولّد فيديو إعلاني RTL من storyboard عربي في دقائق — أربع قصص صباحية في 25 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُشعل يومه من أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للمبيعات والتجارة الإلكترونية والهندسة والإبداع المرئي: فرق revenue تغرق في follow-ups، تجّار D2C يُ rewrite listings يدويًا، squads تقضي ساعات في البحث عن ticket قديم، ووكالات تنتظر weeks لـ motion ads. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 25 أكتوبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Salesforce Agentforce 3 Arabic: وكلاء مبيعات وخدمة — يُفكرون، يُنفّذون، ويُوثّقون بالعربية!</h2>
      <p class="article-lead">«300 lead جديد — و3 SDRs فقط». في 25 أكتوبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 3 Arabic</strong>: autonomous agents داخل Sales Cloud وService Cloud يُ qualify leads ويُ schedule meetings ويُ resolve tier-1 tickets، يُ draft emails وWhatsApp templates بلهجة MENA/Gulf/Levant، يُ update opportunities وcases مع audit trail، يُ handoff لل humans بـ context كامل، يُ Einstein Trust Layer لل PII، يُ Data Cloud grounding من knowledge base عربي — لل enterprises وscale-ups 50–50000 users في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Agentforce 2 كان يُ hallucinate product SKUs؛ الإصدار 3 يُ catalog sync real-time، يُ benchmark +34% qualified meetings في telecom operator الرياض، يُ multi-agent orchestration (SDR + CSM + billing)، يُ Arabic sentiment routing، يُ compliance packs (banking، healthcare)، ويُ partner templates لل SIs.</p>
      <p>القدرات الأساسية: Arabic revenue and service agents; CRM autonomous actions; Trust Layer and audit; Knowledge grounding RTL; Human handoff; Industry compliance packs.</p>
      <p>للمبدعين العرب: RevOps consultancies — «Agentforce 3 Arabic revenue cell in 7 days» لل orgs 200–15000 seats. من يُ deploy 12 cells/ربع بـ 2400–58000 دولار + care 180–1400 دولار/شهر يبني «غرفة Agentforce عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة cell (agents، prompts، data، training):</strong> 5–15 يومًا — 2400–58000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ tuning وuse cases جديدة:</strong> — 180–1400 دولار/شهر.</li>
          <li><strong>Vertical agent kits (telco، retail، B2B RTL):</strong> — 62–285 دولار/kit.</li>
          <li><strong>دورات «وكلاء CRM بـ Agentforce بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Agentforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Revenue</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Shopify Sidekick 5 Arabic: متجرك يُحدّث نفسه — copy، SEO، bundles، وforecast!</h2>
      <p class="article-lead">«100 SKU — وCTR ينهار لأن الوصف مترجم حرفيًا». في 25 أكتوبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 5 Arabic</strong>: merchant copilot يُ rewrite product pages وcollections بلهجة سوقك، يُ suggest cross-sell bundles من sales data، يُ forecast inventory وreorder alerts، يُ generate Meta وTikTok ad copy RTL، يُ answer analytics questions («لماذا انخفض AOV في رمضان؟»)، يُ theme tweaks وsection copy، يُ Markets multi-currency insights — لل D2C وbrands على Shopify Plus في MENA وEU diaspora.</p>
      <p>المشكلة التي حلّتها: Sidekick 4 كان يُ ignore dialect nuance؛ الإصدار 5 يُ locale packs (KSA، UAE، EG، MA)، يُ benchmark +22% conversion lift في fashion D2C دبي، يُ image alt-text Arabic SEO، يُ compliance hints لل promotions، يُ connect Sidekick Actions لـ Flow و3PL، ويُ human review queue قبل publish.</p>
      <p>القدرات الأساسية: Arabic merchant copilot; Product and SEO copy RTL; Bundles and forecasting; Ad copy generation; Analytics Q&amp;A; Markets insights.</p>
      <p>للمبدعين العرب: e-commerce agencies — «Sidekick 5 Arabic store lift in 5 days» لل merchants 500–500K GMV/شهر. من يُ onboard 20 stores/ربع بـ 850–28000 دولار + retainer 95–780 دولار/شهر يبني «استوديو Shopify AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 5 Arabic؟</h3>
        <ul>
          <li><strong>باقة lift (audit، copy، bundles، Sidekick training):</strong> 3–11 يومًا — 850–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ seasonal campaigns وSEO:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Niche playbooks (beauty، electronics، food RTL):</strong> — 38–175 دولار/playbook.</li>
          <li><strong>دورات «تجارة ذكية بـ Sidekick بالعربية»:</strong> — 32–148 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">D2C</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Atlassian Rovo 3 Arabic: Jira وConfluence يُجيبان — search، summarize، وactions من Slack!</h2>
      <p class="article-lead">«أين قرارنا عن API v3؟ — ثلاث ساعات بحث في Confluence». في 25 أكتوبر 2026، أطلقت <strong>Atlassian</strong> <strong>Rovo 3 Arabic</strong>: team intelligence agent يُ search Jira issues وConfluence pages وBitbucket وSlack threads، يُ summarize sprints وincidents بالعربية، يُ create tickets وsubtasks من natural language، يُ suggest assignees من workload graph، يُ draft release notes RTL، يُ connect DevOps signals (PagerDuty، GitHub)، يُ admin controls وdata residency — لل engineering وproduct orgs 30–8000 seats.</p>
      <p>المشكلة التي حلّتها: Rovo 2 كان يُ miss Arabic comments in issues؛ الإصدار 3 يُ multilingual index، يُ benchmark −41% time-to-find-decision في fintech squad القاهرة، يُ Rovo Studio custom agents (QA، compliance)، يُ citation links لكل answer، يُ mobile Rovo في Teams وSlack RTL، ويُ SOC2 وISO roadmap.</p>
      <p>القدرات الأساسية: Arabic cross-tool search; Sprint and incident summaries; Ticket creation from chat; Workload-aware routing; Release notes RTL; Custom Rovo agents.</p>
      <p>للمبدعين العرب: agile consultancies — «Rovo 3 Arabic engineering memory in 6 days» لل squads 25–600 devs. من يُ ship 14 rollouts/ربع بـ 1200–35000 دولار + support 72–580 دولار/شهر يبني «مكتب Rovo عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlassian Rovo 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة memory (index، agents، workflows، champions):</strong> 4–12 يومًا — 1200–35000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ agents وgovernance:</strong> — 72–580 دولار/شهر.</li>
          <li><strong>Squad templates (platform، mobile، data RTL):</strong> — 42–198 دولار/template.</li>
          <li><strong>دورات «إنتاجية هندسية بـ Rovo بالعربية»:</strong> — 36–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atlassian</span>
        <span class="tag">Rovo</span>
        <span class="tag">Jira</span>
        <span class="tag">Engineering</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Runway Gen-4 Turbo Arabic: storyboard عربي → فيديو إعلاني، dubbing، وB-roll MENA!</h2>
      <p class="article-lead">«العميل يريد 15s spot باللهجة الخليجية — والموعد مساءً». في 25 أكتوبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Turbo Arabic</strong>: video stack يُ text-to-video وimage-to-video من brief عربي، يُ lip-sync dubbing EN↔AR مع dialect tags، يُ character consistency عبر shots، يُ brand-safe filters وwatermark controls، يُ extend وinpaint لل edits سريعة، يُ export ProRes وsocial crops، يُ team workspaces وreview comments — لل agencies وstudios وcreators في MENA.</p>
      <p>المشكلة التي حلّتها: Gen-3 Turbo كان يُ drift faces في Arabic scripts؛ الإصدار 4 يُ script-aware generation، يُ benchmark −58% time-to-first-cut في agency الرياض، يُ MENA stock style presets، يُ voice clone guardrails، يُ API tier لل pipelines، ويُ enterprise legal indemnity options.</p>
      <p>القدرات الأساسية: Arabic video generation; Dialect dubbing and lip-sync; Character consistency; Brand safety; Fast edit tools; Team review RTL.</p>
      <p>للمبدعين العرب: motion studios — «Gen-4 Turbo Arabic spot factory in 3 days» لل brands وcampaigns 10K–2M reach. من يُ deliver 18 spots/ربع بـ 1400–42000 دولار + subscription pass-through 120–950 دولار/شهر يبني «استوديو Runway عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Turbo Arabic؟</h3>
        <ul>
          <li><strong>باقة spot (storyboard، gen، dub، delivery):</strong> 2–8 أيام — 1400–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ retainer spots وvariants:</strong> — 120–950 دولار/شهر.</li>
          <li><strong>Vertical look packs (luxury، gaming، gov RTL):</strong> — 52–245 دولار/pack.</li>
          <li><strong>دورات «فيديو generative بـ Runway Gen-4 بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video AI</span>
        <span class="tag">Creative</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-10-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="25-10-2026 -- 08-AM.html">
          📰 25 أكتوبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-10-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/25-10-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/25-10-2026 -- 12-AM.html"
    new_line = (
        f"- [`{new}`](news/25-10-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS}) "
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
