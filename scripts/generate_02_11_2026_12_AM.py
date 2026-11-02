#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 02-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "02-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Anthropic Claude for Excel 3 Arabic · Deepgram Voice Agent 2 Arabic · "
    "Retool AI Agents 3 Arabic · Linear AI Insights 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI GPT-5.1 Codex Workspace 2 Arabic، Perplexity Comet 2 Arabic، Canva Magic Studio 4 Arabic، Zapier Central 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 2 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من OpenAI GPT-5.1 Codex Workspace 2 Arabic الذي يُحوّل مستودع الكود إلى شريك هندسي يُجيب بالعربية قبل أن ينتهي merge request، إلى Perplexity Comet 2 Arabic الذي يُتصفّح الويب ويُلخّص مصادر موثوقة بلهجة الباحث العربي، ومن Canva Magic Studio 4 Arabic الذي يُ birth حملات visual كاملة RTL من brief واحد، إلى Zapier Central 3 Arabic الذي يُ orchestrate وكلاء عبر 7000+ تطبيق — أربع قصص ليلية في 2 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمهندسين والباحثين والمسوقين وفرق الأتمتة: bugs تتراكم، tabs تتكاثر، creatives تنتظر designer، وworkflows تتعطل بين Slack وCRM. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 2 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI GPT-5.1 Codex Workspace 2 Arabic: مهندس برمجيات في المتصفح — refactor، tests، وdocs بلسان الفريق!</h2>
      <p class="article-lead">«الـ PR فيه 40 ملفًا — والمراجع يريد ملخصًا بالعربية قبل midnight». في 2 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>GPT-5.1 Codex Workspace 2 Arabic</strong>: بيئة cloud IDE تُ index monorepos وGitHub/GitLab، تُ answer أسئلة architecture بالفصحى واللهجات، تُ propose patches وunit tests وmigration plans، تُ run sandboxes آمنة وCI previews، تُ generate ADRs وrunbooks RTL، تُ respect branch policies وsecret scanning، تُ integrate Jira وLinear وSlack، ويُ enterprise VPC لل fintech وgovtech في MENA.</p>
      <p>المشكلة التي حلّتها: Workspace 1 كان يُ slow على Arabic comments في legacy PHP؛ الإصدار 2 يُ bilingual code search، يُ benchmark −46% وقت «ticket إلى merged fix» في neobank الرياض، يُ pair programming voice mode، يُ template packs (React، Laravel، Flutter، data pipelines)، ويُ partner certifications لل dev shops.</p>
      <p>القدرات الأساسية: Arabic code Q&amp;A; Safe patch proposals; Test generation; Docs and ADRs RTL; CI sandbox; Enterprise VPC.</p>
      <p>للمبدعين العرب: freelance tech leads — «Codex Workspace 2 Arabic rescue sprint in 4 days» لل teams 3–60 engineers. من يُ deliver 11 sprints/ربع بـ 2800–58000 دولار + retainer 220–1850 دولار/شهر يبني «مكتب Codex عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI GPT-5.1 Codex Workspace 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة rescue sprint (audit، guardrails، pilot repos، training):</strong> 3–14 يومًا — 2800–58000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ policy tuning وquality reviews:</strong> — 220–1850 دولار/شهر.</li>
          <li><strong>حزم stack (mobile، backend، data، legacy modernization):</strong> — 58–275 دولار/حزمة.</li>
          <li><strong>دورات «هندسة AI بـ Codex Workspace بالعربية»:</strong> — 52–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Codex</span>
        <span class="tag">Developers</span>
        <span class="tag">IDE</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Perplexity Comet 2 Arabic: متصفح ذكي — research، citations، وbriefs بلهجة MENA!</h2>
      <p class="article-lead">«العميل يريد competitive landscape لـ 12 competitor — والموعد قبل 48 ساعة». في 2 نوفمبر 2026، أطلقت <strong>Perplexity</strong> <strong>Comet 2 Arabic</strong>: متصفح agentic يُ navigate sites وPDFs وpaywalls المسموحة، يُ synthesize answers بالعربية مع footnotes، يُ compare pricing وfeatures في جداول RTL، يُ save research spaces لل teams، يُ schedule monitoring alerts، يُ export إلى Notion وGoogle Docs، يُ enterprise SSO وaudit logs، ويُ on-device cache لل sensitive sectors — لل consultants وjournalists وstrategy teams في MENA.</p>
      <p>المشكلة التي حلّتها: Comet 1 كان يُ mix dialects في legal summaries؛ الإصدار 2 يُ MSA lock لل reports، يُ benchmark −42% وقت «brief إلى deck» في agency دبي، يُ Arabic OCR لل scanned filings، يُ team libraries مشتركة، ويُ revenue share لل research boutiques.</p>
      <p>القدرات الأساسية: Arabic agentic browsing; Cited synthesis; Competitive tables RTL; Team spaces; Monitoring; Enterprise audit.</p>
      <p>للمبدعين العرب: strategy freelancers — «Comet 2 Arabic insight sprint in 3 days» لل clients 4–40 reports/month. من يُ ship 15 sprints/ربع بـ 1200–24000 دولار + ops 140–1100 دولار/شهر يبني «مكتب Perplexity عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Perplexity Comet 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة insight sprint (scope، sources، deliverable deck، handoff):</strong> 2–9 أيام — 1200–24000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وbrief refresh:</strong> — 140–1100 دولار/شهر.</li>
          <li><strong>Vertical packs (fintech، healthcare، retail، energy):</strong> — 35–168 دولار/pack.</li>
          <li><strong>دورات «بحث استراتيجي بـ Comet بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Perplexity</span>
        <span class="tag">Browser</span>
        <span class="tag">Research</span>
        <span class="tag">Citations</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Canva Magic Studio 4 Arabic: استوديو إبداعي — brands، motion، وsocial kits من prompt عربي!</h2>
      <p class="article-lead">«نحتاج 30 post لرمضان — والـ brand book بالعربية والإنجليزية». في 2 نوفمبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 4 Arabic</strong>: suite يُ lock fonts وcolors وvoice، يُ generate carousels وstories وshort video RTL، يُ resize لـ Meta وSnap وLinkedIn وTikTok، يُ translate copy مع tone guard، يُ animate logos وproduct shots، يُ batch export مع naming rules، يُ team approvals وversion history، ويُ enterprise brand portal — لل SMEs وagencies وcreators في MENA.</p>
      <p>المشكلة التي حلّتها: Magic Studio 3 كان inconsistent في Arabic kerning؛ الإصدار 4 يُ typography engine جديد، يُ benchmark −49% time-to-campaign في beauty D2C الكويت، يُ Sharia-aware imagery filters optional، يُ template marketplace لل MENA designers، ويُ API batch لل catalogs.</p>
      <p>القدرات الأساسية: Arabic brand kits; Motion and video RTL; Multi-channel resize; Tone-safe translation; Approvals; Enterprise portal.</p>
      <p>للمبدعين العرب: social agencies — «Magic Studio 4 Arabic campaign factory in 5 days» لل brands 8–80 SKUs/season. من يُ run 13 factories/ربع بـ 1600–32000 دولار + ops 150–1250 دولار/شهر يبني «استوديو Canva AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة campaign factory (brand lock، templates، pilot season، training):</strong> 4–15 يومًا — 1600–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ seasonal drops وA/B variants:</strong> — 150–1250 دولار/شهر.</li>
          <li><strong>Industry packs (food، fashion، education، NGOs):</strong> — 38–178 دولار/pack.</li>
          <li><strong>دورات «تسويق visual بـ Magic Studio بالعربية»:</strong> — 42–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Design</span>
        <span class="tag">Social</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zapier Central 3 Arabic: غرفة تحكم للأتمتة — agents، triggers، وops بلسان عربي!</h2>
      <p class="article-lead">«كل lead يمر بـ 6 أدوات — ونصف الخطوات manual». في 2 نوفمبر 2026، أطلقت <strong>Zapier</strong> <strong>Central 3 Arabic</strong>: hub يُ describe workflows بالعربية («عند lead جديد، enrich، score، notify sales، open ticket»)، يُ deploy multi-step agents عبر 7000+ apps، يُ human-in-the-loop approvals RTL، يُ monitor failures وretry policies، يُ cost dashboards per team، يُ connect HubSpot وSalesforce وGoogle Workspace وWhatsApp Business، يُ SOC2 وdata residency options، — لل ops وRevOps وcustomer success في MENA.</p>
      <p>المشكلة التي حلّتها: Central 2 كان English-first في error messages؛ الإصدار 3 يُ bilingual runbooks، يُ benchmark −40% broken zaps في SaaS عمّان، يُ Arabic NLP لل inbound forms، يُ template marketplace لل agencies، ويُ certification program لل implementers.</p>
      <p>القدرات الأساسية: Arabic workflow design; Multi-app agents; Approvals RTL; Observability; WhatsApp and CRM; Enterprise compliance.</p>
      <p>للمبدعين العرب: automation consultants — «Central 3 Arabic ops mesh in 7 days» لل orgs 20–5000 seats. من يُ deliver 9 meshes/ربع بـ 2400–48000 دولار + managed 200–1650 دولار/شهر يبني «غرفة Zapier AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zapier Central 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة ops mesh (mapping، build، UAT، runbooks):</strong> 5–20 يومًا — 2400–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وoptimization:</strong> — 200–1650 دولار/شهر.</li>
          <li><strong>Starter meshes (sales، support، finance close، HR onboarding):</strong> — 45–210 دولار/mesh.</li>
          <li><strong>دورات «أتمتة AI بـ Zapier Central بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zapier</span>
        <span class="tag">Automation</span>
        <span class="tag">Agents</span>
        <span class="tag">RevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 02-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="02-11-2026 -- 12-AM.html">
          📰 2 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "02-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/02-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/01-11-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/02-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
