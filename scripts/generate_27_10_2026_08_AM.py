#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-10-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-10-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google Gemini Enterprise 4 Arabic · OpenAI Codex CLI 2 Arabic · "
    "Perplexity Comet 3 Arabic · Stripe AI Billing Agents Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Gemini Enterprise 4 Arabic، OpenAI Codex CLI 2 Arabic، Perplexity Comet 3 Arabic، Stripe AI Billing Agents Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 أكتوبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Google Gemini Enterprise 4 Arabic الذي يُحوّل مئات آلاف المستندات في Drive إلى إجابات مُ cited بلهجات الخليج قبل أن ينتهي اجتماع الإدارة، إلى OpenAI Codex CLI 2 Arabic الذي يُ refactor repos ويُ ship pull requests من terminal بأوامر عربية، ومن Perplexity Comet 3 Arabic الذي يُ browse ويُ compare ويُ summarize مصادر عالمية ومحلية في نافذة واحدة، إلى Stripe AI Billing Agents Arabic الذي يُ recover failed payments ويُ draft dunning emails بالعربية — أربع قصص صباحية في 27 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُشعل يومه من أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للمؤسسات والمطورين والباحثين وفرق الإيرادات: knowledge workers يغرقون في search، engineering teams تنتظر sprints لـ bugfixes بسيطة، analysts يفتحون 40 tab قبل تقرير واحد، و SaaS يخسر MRR على بطاقات منتهية. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 27 أكتوبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Gemini Enterprise 4 Arabic: workspace ذكي — RAG، agents، وامتثال للمؤسسات!</h2>
      <p class="article-lead">«لدينا 12000 ملف في Drive — والموظف يسأل نفس السؤال كل أسبوع». في 27 أكتوبر 2026، أطلقت <strong>Google</strong> <strong>Gemini Enterprise 4 Arabic</strong>: منصة موحّدة داخل Workspace تُ index Gmail وDrive وMeet transcripts وSites، تُ answer بالعربية الفصحى والخليجية والمصرية مع citations، تُ deploy agents لـ HR وIT وlegal workflows، تُ connect BigQuery وSAP وSalesforce، تُ VPC-SC وDLP وno-train enterprise tier، تُ Gemini Live للاجتماعات مع live notes عربية، ويُ sovereign options لـ GCC partners — لل banks وtelcos وgroups 1000–200000 seats.</p>
      <p>المشكلة التي حلّتها: Enterprise 3 كان يُ confuse تواريخ هجرية وميلادية في policy docs؛ الإصدار 4 يُ calendar-aware RAG، يُ benchmark −44% وقت «العثور على إجابة معتمدة» في conglomerate الرياض، يُ multi-modal Q&amp;A على PDFs وslides وrecordings، يُ admin prompt libraries بالعربية، يُ partner marketplace لـ vertical packs، ويُ audit export لـ regulators.</p>
      <p>القدرات الأساسية: Arabic enterprise RAG; Workspace-native agents; Grounded citations; Compliance controls; Live meeting notes; GCC deployment options.</p>
      <p>للمبدعين العرب: Google Cloud partners — «Gemini Enterprise 4 Arabic knowledge hub in 10 days» لل orgs 500–100000 users. من يُ deliver 6 hubs/ربع بـ 4500–92000 دولار + managed 350–2800 دولار/شهر يبني «مركز Gemini عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Gemini Enterprise 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة knowledge hub (index، agents، governance، training):</strong> 7–21 يومًا — 4500–92000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ corpus refresh وprompt libraries:</strong> — 350–2800 دولار/شهر.</li>
          <li><strong>Vertical packs (oil &amp; gas، healthcare، retail، gov):</strong> — 85–380 دولار/pack.</li>
          <li><strong>دورات «Workspace ذكي بـ Gemini Enterprise بالعربية»:</strong> — 58–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Gemini</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Workspace</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>OpenAI Codex CLI 2 Arabic: مطور في الطرفية — refactor، tests، وPRs بلغة عربية!</h2>
      <p class="article-lead">«ال ticket: أصلح bug في checkout — والـ sprint ممتلئ». في 27 أكتوبر 2026، أطلقت <strong>OpenAI</strong> <strong>Codex CLI 2 Arabic</strong>: agent سطر أوامر يُفهم أوامر عربية وإنجليزية، يُ scan monorepos، يُ propose diffs مع explanations، يُ run tests وlinters في sandbox، يُ open PRs على GitHub وGitLab، يُ respect CODEOWNERS وbranch policies، يُ MCP servers لل Jira وDatadog، يُ model routing بين fast وreasoning tiers، ويُ enterprise SSO وaudit — لل product teams وagencies وSIs.</p>
      <p>المشكلة التي حلّتها: Codex CLI 1 كان يُ break RTL strings في UI components؛ الإصدار 2 يُ i18n-aware patches، يُ benchmark −38% وقت «ticket to merged PR» في fintech عمان، يُ parallel workers على tasks مستقلة، يُ secret scanning قبل push، يُ custom rules files بالعربية لل teams، ويُ offline mode لـ air-gapped labs.</p>
      <p>القدرات الأساسية: Arabic CLI commands; Safe repo editing; Automated PR workflow; Test and lint integration; MCP toolchains; Enterprise governance.</p>
      <p>للمبدعين العرب: dev consultancies — «Codex CLI 2 Arabic velocity pod in 5 days» لل teams 5–80 engineers. من يُ onboard 10 pods/ربع بـ 2200–48000 دولار + retainer 190–1550 دولار/شهر يبني «ممارسة Codex عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI Codex CLI 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة velocity pod (rules، workflows، pilot sprint، handoff):</strong> 4–12 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ rules tuning وincident playbooks:</strong> — 190–1550 دولار/شهر.</li>
          <li><strong>Stack templates (Next.js، Laravel، Flutter، data pipelines):</strong> — 48–220 دولار/template.</li>
          <li><strong>دورات «تطوير أسرع بـ Codex CLI بالعربية»:</strong> — 42–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Codex</span>
        <span class="tag">Developer</span>
        <span class="tag">CLI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Perplexity Comet 3 Arabic: متصفح البحث الذكي — compare، cite، وresearch بلمسة!</h2>
      <p class="article-lead">«أحتاج مقارنة 15 vendor قبل RFP — وال deadline بعد ساعتين». في 27 أكتوبر 2026، أطلقت <strong>Perplexity</strong> <strong>Comet 3 Arabic</strong>: متصفح agentic يُ browse مواقع EN/AR، يُ build comparison tables مع sources، يُ summarize earnings calls وnews وforums، يُ Spaces لل teams مع shared threads، يُ Pro Search deep mode لل due diligence، يُ export إلى Notion وGoogle Docs RTL-safe، يُ privacy controls وteam admin، ويُ API لل embedded research widgets — لل consultants وinvestors وjournalists وPMs.</p>
      <p>المشكلة التي حلّتها: Comet 2 كان يُ miss مصادر عربية في niche verticals؛ الإصدار 3 يُ bilingual source ranking، يُ benchmark −51% وقت «competitive landscape memo» في strategy firm دبي، يُ scheduled research monitors، يُ citation confidence scores، يُ browser actions مع human confirm، ويُ enterprise SSO وdata retention policies.</p>
      <p>القدرات الأساسية: Arabic research browser; Multi-source compare; Team Spaces; Deep Pro Search; RTL exports; Research monitors.</p>
      <p>للمبدعين العرب: research boutiques — «Comet 3 Arabic intel desk in 3 days» لل funds وcorporate strategy. من يُ run 18 desks/ربع بـ 900–28500 دولار + subscription margin 120–980 دولار/شهر يبني «مكتب أبحاث Comet عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Comet 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة intel desk (monitors، templates، training، SLA):</strong> 2–8 أيام — 900–28500 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitors وbriefings:</strong> — 120–980 دولار/شهر.</li>
          <li><strong>Sector playbooks (fintech، logistics، healthcare، energy):</strong> — 35–168 دولار/playbook.</li>
          <li><strong>دورات «بحث احترافي بـ Comet بالعربية»:</strong> — 28–135 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Comet</span>
        <span class="tag">Research</span>
        <span class="tag">Browser</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Stripe AI Billing Agents Arabic: إيرادات أذكى — recovery، dunning، وforecasting!</h2>
      <p class="article-lead">«12% من الاشتراكات تفشل بسبب بطاقة منتهية — ولا أحد يكتب email بالعربية». في 27 أكتوبر 2026، أطلقت <strong>Stripe</strong> <strong>AI Billing Agents Arabic</strong>: agents داخل Billing وRevenue Recognition يُ predict churn من payment patterns، يُ draft dunning sequences MSA وخليجي، يُ smart retries حسب issuer وtimezone، يُ summarize MRR movements لل CFO، يُ recommend pricing experiments، يُ connect Stripe Sigma وMetabase، يُ compliance templates لـ VAT ZATCA وEgypt e-invoice hints، ويُ partner dashboard لل agencies — لل SaaS وmarketplaces وsubscription boxes في MENA.</p>
      <p>المشكلة التي حلّتها: Billing agents v1 كان يُ sound robotic في WhatsApp recovery؛ الإصدار Arabic يُ tone-matched templates وA/B subject lines، يُ benchmark +18% recovered revenue في edtech Cairo، يُ multi-currency dunning، يُ dispute evidence packs auto-assembled، يُ webhook agents لـ CRM updates، ويُ revenue forecast narratives لل board decks.</p>
      <p>القدرات الأساسية: Arabic dunning copy; Smart payment retry; Churn prediction; CFO summaries; Pricing experiments; MENA tax hints.</p>
      <p>للمبدعين العرب: Stripe partners — «AI Billing Agents Arabic revenue rescue in 6 days» لل SaaS 50K–5M ARR. من يُ deploy 14 stacks/ربع بـ 1800–42000 دولار + ops 175–1400 دولار/شهر يبني «ممارسة Stripe AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe AI Billing Agents Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue rescue (audit، agents، dunning، dashboards):</strong> 4–14 يومًا — 1800–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ copy tests وretry tuning:</strong> — 175–1400 دولار/شهر.</li>
          <li><strong>Vertical dunning kits (B2B SaaS، consumer apps، marketplaces):</strong> — 45–210 دولار/kit.</li>
          <li><strong>دورات «إيرادات اشتراك بـ Stripe AI بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Billing</span>
        <span class="tag">Revenue</span>
        <span class="tag">SaaS</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-10-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-10-2026 -- 08-AM.html">
          📰 27 أكتوبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-10-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-10-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/27-10-2026 -- 12-AM.html"
    new_line = (
        f"- [`{new}`](news/27-10-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS}) "
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
