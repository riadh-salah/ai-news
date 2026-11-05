#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 05-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "05-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Notion AI Q&amp;A 3 Arabic · Canva Magic Studio 4 Arabic · "
    "HubSpot Breeze AI 2 Arabic · Shopify Sidekick 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Notion AI Q&amp;A 3 Arabic، Canva Magic Studio 4 Arabic، HubSpot Breeze AI 2 Arabic، Shopify Sidekick 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 5 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Notion AI Q&amp;A 3 Arabic الذي يُجيب عن policies وSOPs بالعربية من wiki الشركة قبل أن يُنهي الموظف فنجان الشاي، إلى Canva Magic Studio 4 Arabic الذي يُ birth حملات visual وbrand kits من prompt واحد، ومن HubSpot Breeze AI 2 Arabic الذي يُ draft sequences ويُ score leads بلهجة sales في MENA، إلى Shopify Sidekick 3 Arabic الذي يُ suggest bundles ويُ write product copy لمتجرك بينما الطلبات تتدفق — أربع قصص ليلية في 5 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة لفرق ops وmarketing وe-commerce: knowledge مُتفرقة، creatives تتأخر، pipelines بلا personalization، ومتاجر online تخسر conversion لغياب copy ذكي. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 5 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Notion AI Q&amp;A 3 Arabic: wiki ذكي — policies، onboarding، وإجابات موثّقة!</h2>
      <p class="article-lead">«أين policy الإجازات؟ — والـ HR في meeting». في 5 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>Notion AI Q&amp;A 3 Arabic</strong>: enterprise knowledge layer يُ index pages وdatabases وSlack exports، يُ answer بالفصحى واللهجات المختارة مع citations وdeep links، يُ detect stale docs ويُ suggest updates، يُ restrict answers حسب permissions وSSO groups، يُ summarize meeting notes إلى tasks، يُ bilingual search بين English docs وArabic queries — لل startups وholdings وgov digital teams في MENA.</p>
      <p>المشكلة التي حلّتها: Q&amp;A 2 كان يُ hallucinate على PDFs scanned؛ الإصدار 3 يُ OCR عربي محسّن، يُ benchmark −44% time-to-answer في conglomerate الرياض، يُ connector packs لـ Confluence وGoogle Drive، يُ analytics لـ «أسئلة لا تُجاب»، ويُ partner enablement في Dubai وCasablanca.</p>
      <p>القدرات الأساسية: Arabic Q&amp;A with citations; Permission-aware retrieval; Stale doc detection; Meeting-to-task summaries; Bilingual search; Enterprise SSO.</p>
      <p>للمبدعين العرب: ops consultancies — «Notion Q&amp;A 3 Arabic wiki rollout in 8 days» لل orgs 50–5000 seats. من يُ deploy 6 workspaces/ربع بـ 1800–36000 دولار + managed 140–1050 دولار/شهر يبني «مكتب Notion عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Q&amp;A 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة wiki AI (taxonomy، migrations، permissions، pilot):</strong> 5–15 يومًا — 1800–36000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ KB hygiene وquestion analytics:</strong> — 140–1050 دولار/شهر.</li>
          <li><strong>Department playbooks (HR، legal، product):</strong> — 45–198 دولار/playbook.</li>
          <li><strong>دورات «معرفة مؤسسية بـ Notion Q&amp;A بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Q&amp;A</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva Magic Studio 4 Arabic: تصميم بالprompt — brand kits، video، وsocial packs!</h2>
      <p class="article-lead">«نحتاج 20 post للحملة — والمصمم overloaded». في 5 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 4 Arabic</strong>: creative AI suite يُ generate layouts وcopy وshort videos من brief عربي، يُ lock brand colors وfonts وvoice، يُ resize لـ Instagram وSnap وLinkedIn وOOH mockups، يُ translate campaigns مع RTL-safe typography، يُ batch export مع naming conventions، يُ team libraries وapproval flows — لل agencies وSMEs وcreators في المنطقة.</p>
      <p>المشكلة التي حلّتها: Magic Studio 3 كان weak في Arabic kerning في video captions؛ الإصدار 4 يُ MENA type presets، يُ benchmark +35% output per designer في agency دبي، يُ Magic Write لل headlines وCTAs، يُ background remove على product shots، ويُ reseller program لل regional partners.</p>
      <p>القدرات الأساسية: Arabic prompt to designs; Brand-locked generation; Multi-format resize; Video captions RTL; Batch export; Team approvals.</p>
      <p>للمبدعين العرب: creative studios — «Magic Studio 4 Arabic campaign factory in 6 days» لل brands 3–25 assets/week. من يُ ship 9 retainers/ربع بـ 1200–28000 دولار + care 110–880 دولار/شهر يبني «خط Canva AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة creative AI (brand kit، templates، 4-week content sprint):</strong> 4–12 يومًا — 1200–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ template refresh وQA:</strong> — 110–880 دولار/شهر.</li>
          <li><strong>Vertical packs (restaurants، real estate، fintech):</strong> — 38–175 دولار/pack.</li>
          <li><strong>دورات «حملات سريعة بـ Magic Studio بالعربية»:</strong> — 32–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Design</span>
        <span class="tag">Video</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>HubSpot Breeze AI 2 Arabic: sales وmarketing copilot — sequences، scoring، وCRM insights!</h2>
      <p class="article-lead">«الlead ساخن — لكن الemail generic». في 5 نوفمبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze AI 2 Arabic</strong>: revenue AI على CRM يُ draft outreach باللهجة Gulf/Levant/Egyptian، يُ personalize landing snippets، يُ score intent من email opens وweb visits، يُ summarize deal rooms وcall notes، يُ suggest next-best-action لل reps، يُ generate reports بالعربية لل leadership، يُ guard PII وopt-out compliance — لل B2B وSaaS وservices في MENA.</p>
      <p>المشكلة التي حلّتها: Breeze 1 كان tone mismatch في formal B2B Arabic؛ الإصدار 2 يُ industry tone packs، يُ benchmark +22% reply rate في SaaS القاهرة، يُ WhatsApp وSMS hooks، يُ integration مع LinkedIn Sales Navigator، ويُ partner certifications لل agencies.</p>
      <p>القدرات الأساسية: Dialect-aware outreach; Intent scoring; Deal summaries; Next-best-action; Arabic leadership reports; Compliance guards.</p>
      <p>للمبدعين العرب: growth agencies — «Breeze AI 2 Arabic GTM stack in 9 days» لل teams 5–80 reps. من يُ launch 7 hubs/ربع بـ 2400–48000 دولار + retainer 180–1400 دولار/شهر يبني «استوديو HubSpot AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze AI 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue AI (CRM cleanup، sequences، scoring، training):</strong> 6–18 يومًا — 2400–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ sequence tuning وreporting:</strong> — 180–1400 دولار/شهر.</li>
          <li><strong>Industry sequence libraries (SaaS، logistics، healthcare):</strong> — 52–225 دولار/library.</li>
          <li><strong>دورات «مبيعات ذكية بـ Breeze بالعربية»:</strong> — 42–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Breeze AI</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Shopify Sidekick 3 Arabic: متجرك يتكلم — bundles، SEO copy، وmerchant copilot!</h2>
      <p class="article-lead">«المنتج جديد — والوصف فارغ والـ SEO صفر». في 5 نوفمبر 2026، أطلقت <strong>Shopify</strong> <strong>Sidekick 3 Arabic</strong>: merchant AI داخل admin يُ write product descriptions وmeta tags بالعربية، يُ suggest cross-sell bundles من sales data، يُ answer «لماذا انخفض conversion؟» مع charts، يُ automate discount tests وA/B subject lines، يُ draft customer replies aligned مع brand tone، يُ sync مع Markets لل multi-currency MENA — لل D2C وmarketplaces وomni retailers.</p>
      <p>المشكلة التي حلّتها: Sidekick 2 كان weak في dialect في chat replies؛ الإصدار 3 يُ storefront-aware Arabic، يُ benchmark +19% AOV في fashion متجر الكويت، يُ image alt-text generation، يُ integration مع Meta وGoogle Merchant feeds، ويُ partner apps لل regional logistics.</p>
      <p>القدرات الأساسية: Arabic product and SEO copy; Bundle suggestions; Conversion diagnostics; A/B automation; Customer reply drafts; Markets sync.</p>
      <p>للمبدعين العرب: e-commerce agencies — «Sidekick 3 Arabic store uplift in 7 days» لل merchants 50–5000 SKUs. من يُ run 8 stores/ربع بـ 1500–32000 دولار + managed 125–980 دولار/شهر يبني «خط Shopify AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Shopify Sidekick 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة merchant AI (catalog cleanup، SEO، bundles، analytics):</strong> 5–14 يومًا — 1500–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ copy refresh وconversion reviews:</strong> — 125–980 دولار/شهر.</li>
          <li><strong>Category playbooks (beauty، electronics، food):</strong> — 40–185 دولار/playbook.</li>
          <li><strong>دورات «متاجر أذكى بـ Sidekick بالعربية»:</strong> — 34–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Shopify</span>
        <span class="tag">Sidekick</span>
        <span class="tag">E-commerce</span>
        <span class="tag">SEO</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 05-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="05-11-2026 -- 12-AM.html">
          📰 5 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "05-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/05-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/05-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
