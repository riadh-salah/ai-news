#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 20-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "20-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Lovable AI 4 Arabic · UiPath Autopilot 4 Arabic · "
    "ElevenLabs Dubbing Studio 4 Arabic · Cisco Webex AI Agent 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Lovable AI 4 Arabic، UiPath Autopilot 4 Arabic، ElevenLabs Dubbing Studio 4 Arabic، Cisco Webex AI Agent 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 20 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Lovable AI 4 Arabic الذي يُحوّل «أريد marketplace RTL للخدمات المنزلية» إلى تطبيق يُ deploy على Supabase قبل أن تُطفأ شاشة المكتب، إلى UiPath Autopilot 4 Arabic الذي يُحوّل طلب موظف بالعربية إلى robot يُنجز تقريرًا ويُرسله على Teams، ومن ElevenLabs Dubbing Studio 4 Arabic الذي يُ dub فيديو تدريبك إلى خليجي ومصري مع lip-sync جاهز للبث، إلى Cisco Webex AI Agent 4 Arabic الذي يُلخّص اجتماع board ويُفتح Jira tickets ويُحدّث CRM من transcript واحد — أربع قصص ليلية في 20 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للبناء والأتمتة والمحتوى والاجتماعات: founders يريدون MVP بلا فريق backend، ops تغرق في طلبات email، media teams تطارد localization، ومديرون يستيقظون على «ماذا قررنا؟» بلا notes. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 20 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Lovable AI 4 Arabic: من prompt عربي إلى SaaS RTL — frontend، backend، وdeploy في ساعات!</h2>
      <p class="article-lead">«العميل يريد portal للعملاء بالعربية — والـ sprint القادم ممتلئ». في 20 أكتوبر 2026، أطلقت <strong>Lovable</strong> <strong>AI 4 Arabic</strong>: منصة vibe-coding تفهم briefs بالفصحى واللهجات، تُ generate React/Next.js layouts RTL مع Cairo typography، تُ wire Supabase أو Firebase auth وdatabase، تُ add Stripe checkout وArabic emails، تُ iterate في chat مع preview حي، تُ export GitHub repo نظيف، وتُ respect component libraries لل franchises — لل founders وagencies وproduct studios في MENA.</p>
      <p>المشكلة التي حلّتها: Lovable 3 كان يُ struggle مع Arabic forms وRTL tables؛ الإصدار 4 يُ bidirectional CSS auto-fix، يُ benchmark −52% time-to-MVP في proptech pilot الرياض، يُ integration Figma import مع mirror layouts، يُ Knack وRetool MCP connectors لل compliance backends، يُ Arabic error messages وvalidation copy، ويُ team seats مع audit لل enterprise pilots.</p>
      <p>القدرات الأساسية: Prompt-to-app RTL; Supabase/Firebase scaffold; Stripe and auth templates; Git sync; Design system import; MCP backend plugins.</p>
      <p>للمبدعين العرب: no-code agencies — «Lovable AI 4 Arabic launch sprint in 5 days» لل startups 0–1 product. من يُ ship 8 MVPs/ربع بـ 2200–48000 دولار + care 160–1280 دولار/شهر يبني «استوديو Lovable عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lovable AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة launch sprint (discovery، build، deploy، handoff RTL):</strong> 4–10 أيام — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ iterations وbugfix وfeature drops:</strong> — 160–1280 دولار/شهر.</li>
          <li><strong>Vertical kits (clinics، real estate، courses، marketplaces):</strong> — 68–295 دولار/kit.</li>
          <li><strong>دورات «ابنِ SaaS عربي بـ Lovable AI في أسبوع»:</strong> — 45–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lovable</span>
        <span class="tag">Vibe Coding</span>
        <span class="tag">SaaS</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>UiPath Autopilot 4 Arabic: RPA وكيلي — من «أريد تقريرًا» إلى robot يُنجزه قبل الغداء!</h2>
      <p class="article-lead">«Finance يرسل 40 email يوميًا — وكل واحد يطلب نفس extract من SAP». في 20 أكتوبر 2026، أطلقت <strong>UiPath</strong> <strong>Autopilot 4 Arabic</strong>: copilot فوق Automation Cloud يُ understand requests بالفصحى واللهجات، يُ discover processes من screen recordings، يُ generate robots وAPI workflows، يُ orchestrate Document Understanding على فواتير عربية، يُ deploy إلى attended وunattended modes، يُ monitor exceptions مع human-in-the-loop RTL — لل banks وinsurance وshared services centers في MENA.</p>
      <p>المشكلة التي حلّتها: Autopilot 3 كان يُ misread Arabic OCR على فواتير ZATCA؛ الإصدار 4 يُ UAE/KSA invoice models، يُ benchmark −46% handling time في claims processor الكويت، يُ integration Microsoft 365 Copilot handoff، يُ Process Mining narratives Arabic، يُ governance center لل PII، ويُ partner certifications لل SIs العرب.</p>
      <p>القدرات الأساسية: Natural language automation design RTL; Process discovery; Document AI Arabic; Orchestration cloud; Exception queues; Compliance audit.</p>
      <p>للمبدعين العرب: RPA boutiques — «Autopilot 4 Arabic automation factory in 14 days» لل orgs 200–15000 FTE. من يُ deliver 5 factories/ربع بـ 6200–92000 دولار + managed 380–2900 دولار/شهر يبني «مصنع UiPath AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من UiPath Autopilot 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة automation factory (discovery، build، UAT، hypercare):</strong> 10–24 يومًا — 6200–92000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ bot maintenance وexception triage:</strong> — 380–2900 دولار/شهر.</li>
          <li><strong>Domain accelerators (KYC، payroll، procurement، claims):</strong> — 88–420 دولار/accelerator.</li>
          <li><strong>دورات «أتمتة ذكية بـ UiPath Autopilot بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">UiPath</span>
        <span class="tag">Autopilot</span>
        <span class="tag">RPA</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ElevenLabs Dubbing Studio 4 Arabic: دبلجة AI — لهجات، lip-sync، وOTT جاهز للبث!</h2>
      <p class="article-lead">«الدورة بالإنجليزية — والسوق يريدها خليجية ومصرية قبل Ramadan». في 20 أكتوبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 4 Arabic</strong>: studio يُ ingest video وaudio، يُ transcribe وtranslate مع dialect control، يُ clone voices brand-safe أو library MENA، يُ lip-sync وface-aware dubbing، يُ mix music وSFX، يُ export SRT/VTT RTL وbroadcast masters، يُ API لل LMS وstreaming platforms — لل edtech وmedia houses وadvertisers في المنطقة.</p>
      <p>المشكلة التي حلّتها: Dubbing Studio 3 كان lip-sync ضعيف على close-ups؛ الإصدار 4 يُ multi-speaker diarization، يُ benchmark −41% cost per minute في OTT catalog dubbing، يُ glossary locks لل brand terms، يُ human review queue Arabic، يُ watermarking لل previews، ويُ rights metadata لل music clearance.</p>
      <p>القدرات الأساسية: Dialect dubbing RTL; Lip-sync 4; Voice library MENA; Batch API; Review workflows; OTT export presets.</p>
      <p>للمبدعين العرب: localization studios — «Dubbing Studio 4 Arabic catalog sprint in 6 days» لل catalogs 10–500 minutes/month. من يُ onboard 9 clients/ربع بـ 1800–38000 دولار + per-minute overflow 2–18 دولار/دقيقة يبني «استوديو دبلجة AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة catalog sprint (glossary، pilot، QC، delivery):</strong> 5–12 يومًا — 1800–38000 دولار/عميل.</li>
          <li><strong>تسعير per-minute لل dubbing وreview:</strong> — 2–18 دولار/دقيقة حسب dialect وQC.</li>
          <li><strong>Channel packs (YouTube، Shahid-style OTT، corporate LMS):</strong> — 55–240 دولار/pack.</li>
          <li><strong>دورات «إنتاج محتوى مُ dubbed بـ ElevenLabs بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Media AI</span>
        <span class="tag">Voice</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Cisco Webex AI Agent 4 Arabic: اجتماعات تُنتج actions — summaries، tasks، وCRM updates بلمسة واحدة!</h2>
      <p class="article-lead">«اجتماع ساعتان — ولا أحد يتذكر من يُ own المهمة». في 20 أكتوبر 2026، أطلقت <strong>Cisco</strong> <strong>Webex AI Agent 4 Arabic</strong>: agent فوق Webex Suite وCalling وContact Center يُ transcribe meetings RTL، يُ extract decisions وowners وdeadlines، يُ create tasks في Asana وJira وMonday، يُ draft follow-up emails MSA، يُ update Salesforce وHubSpot من verbal commitments، يُ brief managers قبل 1:1s — لل hybrid enterprises وBPOs في MENA.</p>
      <p>المشكلة التي حلّتها: Webex AI Agent 3 كان يُ confuse Arabic names in attendee lists؛ الإصدار 4 يُ phonetic matching لل Arabic names، يُ benchmark −39% «meeting-to-action» latency في consulting firm دبي، يُ integration Microsoft Teams وGoogle Meet import، يُ compliance retention UAE، يُ sales coaching snippets Arabic، ويُ device edge processing لل sensitive rooms.</p>
      <p>القدرات الأساسية: Meeting intelligence RTL; Action item automation; CRM sync; Manager briefs; Contact center assist; Hybrid compliance.</p>
      <p>للمبدعين العرب: collaboration consultancies — «Webex AI Agent 4 Arabic productivity hub in 9 days» لل orgs 500–25000 seats. من يُ deploy 6 hubs/ربع بـ 3400–56000 دولار + care 220–1750 دولار/شهر يبني «مكتب Webex AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cisco Webex AI Agent 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة productivity hub (integrations، templates، training، rollout):</strong> 7–16 يومًا — 3400–56000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ workflow tuning وadoption analytics:</strong> — 220–1750 دولار/شهر.</li>
          <li><strong>Role playbooks (sales، PMO، HR all-hands، board):</strong> — 48–225 دولار/playbook.</li>
          <li><strong>دورات «اجتماعات ذكية بـ Webex AI Agent بالعربية»:</strong> — 40–192 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cisco</span>
        <span class="tag">Webex</span>
        <span class="tag">Meeting AI</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 20-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="20-10-2026 -- 12-AM.html">
          📰 20 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "20-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/20-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    if new in content and "أحدث إصدار" in content.split(new)[0][-200:]:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/19-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/20-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
        "أفكar",
        "دolار",
        "البروtokol",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "y\u0650",
        "المشkلة",
        "mezclar",
        "وy\u0650",
        "prefe r",
        " t\u0650",
        " y\u0650",
        "الإصrador",
        "y\u0650",
        "وy\u0650",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
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
