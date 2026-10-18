#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 18-10-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "18-10-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Dropbox Dash Enterprise 4 Arabic · Asana AI Teammates 4 Arabic · "
    "DocuSign Agreement AI 4 Arabic · Twilio CustomerAI 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Dropbox Dash Enterprise 4 Arabic، Asana AI Teammates 4 Arabic، DocuSign Agreement AI 4 Arabic، Twilio CustomerAI 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 18 أكتوبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من Dropbox Dash Enterprise 4 Arabic الذي يُجيب عن «أين العقد؟» من آلاف الملفات قبل أن تبرد فنجان القهوة، إلى Asana AI Teammates 4 Arabic الذي يُوزّع المهام ويُلخّص الاجتماعات بلهجة فريقك، ومن DocuSign Agreement AI 4 Arabic الذي يُراجع البنود ويُ draft ملاحق عربية compliant، إلى Twilio CustomerAI 4 Arabic الذي يُبني profiles موحّدة للعميل عبر SMS وWhatsApp والبريد — أربع قصص صباحية في 18 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ مع شروق اليوم!</h1>
      <p class="hero-sub">صباح للبحث والتنسيق والعقود و360° للعميل: مديرون يغرقون في Drive وSlack، PMs يطاردون owners للمهام، legal teams تنتظر redlines، وCX leaders يريدون رؤية واحدة للعميل. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 18 أكتوبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Dropbox Dash Enterprise 4 Arabic: بحث موحّد — ملفات، Slack، وemail بسؤال عربي واحد!</h2>
      <p class="article-lead">«العقد موقع في مكان ما بين Drive وOutlook — والاجتماع بعد 40 دقيقة». في 18 أكتوبر 2026، أطلقت <strong>Dropbox</strong> <strong>Dash Enterprise 4 Arabic</strong>: universal search layer تُ index PDFs وSlides وNotion وGmail threads، تُ answer questions RTL مع citations، تُ summarize folders لل boards، تُ respect DLP وregion residency، تُ connect Microsoft 365 وGoogle Workspace، وتُ offer admin controls لل MENA enterprises — لل legal وfinance وconsulting firms.</p>
      <p>المشكلة التي حلّتها: Dash 3 كان يُ weak على Arabic OCR في scanned contracts؛ الإصدار 4 يُ improved Arabic tokenization، يُ benchmark −58% وقت «find the clause» في law firm دبي، يُ semantic search على mixed EN/AR docs، يُ starter packs M&A due diligence، يُ audit logs Arabic، ويُ partner program لل IT integrators في Riyadh وCairo.</p>
      <p>القدرات الأساسية: NL Q&amp;A across apps; Smart collections; Meeting prep briefs; Permission-aware results; Connectors catalog; Mobile RTL search.</p>
      <p>للمبدعين العرب: productivity consultants — «Dash Enterprise 4 Arabic rollout in 7 days» لل orgs 200–15K seats. من يُ deploy 8 tenants/ربع بـ 3200–52000 دولار + care 180–1450 دولار/شهر يبني «استوديو Dash عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dropbox Dash Enterprise 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة rollout (connectors، indexing، training، governance):</strong> 5–14 يومًا — 3200–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل collections tuning وadmin reports:</strong> — 180–1450 دولار/شهر.</li>
          <li><strong>Vertical playbooks (legal discovery، audit prep، sales enablement):</strong> — 55–240 دولار/playbook.</li>
          <li><strong>دورات «بحث ذكي موحّد بـ Dash بالعربية»:</strong> — 38–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dropbox</span>
        <span class="tag">Dash</span>
        <span class="tag">Enterprise Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Asana AI Teammates 4 Arabic: زميل رقمي — يُ plan، يُ nudge، ويُ recap بالعربية!</h2>
      <p class="article-lead">«المشروع أحمر — ولا أحد يعرف من يملك المهمة التالية». في 18 أكتوبر 2026، أطلقت <strong>Asana</strong> <strong>AI Teammates 4 Arabic</strong>: virtual coworkers داخل workspaces تُ break down goals إلى tasks RTL، تُ assign owners حسب workload، تُ draft status updates لل stakeholders، تُ transcribe وsummarize standups MSA/Gulf، تُ flag risks قبل deadlines، وتُ sync Jira وSalesforce — لل product وmarketing وops teams في MENA scale-ups.</p>
      <p>المشكلة التي حلّتها: Teammates 3 كان status copy English-first؛ الإصدار 4 يُ dialect-aware nudges، يُ benchmark −41% overdue tasks في fintech Cairo بعد 6 أسابيع، يُ portfolio views لل VPs، يُ custom teammate personas (PM، Content، CS)، يُ privacy scopes per project، ويُ certification لل Agile coaches العرب.</p>
      <p>القدرات الأساسية: Goal decomposition; Smart assignments; Auto status; Meeting recaps; Risk alerts; Rules builder Arabic NL.</p>
      <p>للمبدعين العرب: PMO freelancers — «Asana AI Teammates 4 Arabic ops fix in 6 days» لل teams 15–400 users. من يُ onboard 10 workspaces/ربع بـ 2100–28000 دولار + tuning 95–780 دولار/شهر يبني «مكتب Teammates عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Asana AI Teammates 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة workspace (templates، teammates، rules، training):</strong> 4–12 يومًا — 2100–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ persona tuning وportfolio reviews:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Industry kits (product launch، event ops، agency retainer):</strong> — 45–195 دولار/kit.</li>
          <li><strong>دورات «إدارة مشاريع بـ AI Teammates بالعربية»:</strong> — 32–158 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Asana</span>
        <span class="tag">AI Teammates</span>
        <span class="tag">PMO</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>DocuSign Agreement AI 4 Arabic: عقود ذكية — review، redlines، وملاحق بضغطة!</h2>
      <p class="article-lead">«NDA عربي-إنجليزي — والطرف الثاني ينتظر قبل ظهر اليوم». في 18 أكتوبر 2026، أطلقت <strong>DocuSign</strong> <strong>Agreement AI 4 Arabic</strong>: CLM intelligence تُ extract obligations وdates من bilingual PDFs، تُ compare versions side-by-side RTL، تُ suggest fallback clauses MSA-compliant، تُ generate amendment drafts من instructions عربية، تُ route approvals حسب risk score، وتُ integrate Salesforce وSAP — لل procurement وreal estate وvendor management في الخليج.</p>
      <p>المشكلة التي حلّتها: Agreement AI 3 كان يُ miss Arabic diacritics in some scans؛ الإصدار 4 يُ enhanced OCR، يُ benchmark −44% cycle time في property developer KSA، يُ playbook library (employment، SaaS، distribution)، يُ eSignature chain unchanged، يُ analytics renewal Arabic، ويُ reseller enablement في Dubai Internet City.</p>
      <p>القدرات الأساسية: Clause extraction; Risk scoring; Redline assist; Amendment gen; Renewal alerts; Audit trail bilingual.</p>
      <p>للمبدعين العرب: legal ops consultants — «DocuSign Agreement AI 4 Arabic CLM in 10 days» لل orgs 500–50K agreements/year. من يُ implement 5 CLM/ربع بـ 5500–72000 دولار + support 220–1680 دولار/شهر يبني «استوديو Agreement AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من DocuSign Agreement AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة CLM (playbooks، workflows، integrations، go-live):</strong> 7–18 يومًا — 5500–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل playbook updates وrenewal ops:</strong> — 220–1680 دولار/شهر.</li>
          <li><strong>Template packs (vendor، lease، employment bilingual):</strong> — 72–310 دولار/pack.</li>
          <li><strong>دورات «إدارة عقود ذكية بـ DocuSign بالعربية»:</strong> — 48–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">DocuSign</span>
        <span class="tag">Agreement AI</span>
        <span class="tag">CLM</span>
        <span class="tag">Legal</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Twilio CustomerAI 4 Arabic: عميل واحد — كل القنوات، journeys، وinsights!</h2>
      <p class="article-lead">«العميل كتب على WhatsApp — والـ agent لا يرى آخر email». في 18 أكتوبر 2026، أطلقت <strong>Twilio</strong> <strong>CustomerAI 4 Arabic</strong>: unified customer layer تُ merge profiles من SMS وvoice وWhatsApp وemail، تُ predict next-best-action RTL، تُ orchestrate journeys من brief عربي، تُ power Fin-style bots على Segment CDP، تُ personalize offers Gulf/Egypt timezones، وتُ feed analytics لل CX وgrowth — لل retail وbanking وtelecom في MENA.</p>
      <p>المشكلة التي حلّتها: CustomerAI 3 كان segmentation weak على Arabic names؛ الإصدار 4 يُ normalized Arabic script variants، يُ benchmark +27% CSAT في ecommerce UAE pilot، يُ consent management GDPR-style Arabic، يُ prebuilt connectors Shopify وZendesk، يُ fraud signals on OTP flows، ويُ partner margins لل regional SIs.</p>
      <p>القدرات الأساسية: Identity resolution; Journey AI; Channel orchestration; Predictive segments; Real-time events; Privacy controls.</p>
      <p>للمبدعين العرب: CX integrators — «Twilio CustomerAI 4 Arabic 360 in 8 days» لل brands 50K–5M customers. من يُ launch 6 stacks/ربع بـ 3800–68000 دولار + optimization 140–1120 دولار/شهر يبني «مختبر CustomerAI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Twilio CustomerAI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة 360 (CDP، journeys، bots، QA channels):</strong> 6–16 يومًا — 3800–68000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل segments وjourney A/B:</strong> — 140–1120 دولار/شهر.</li>
          <li><strong>Use-case accelerators (abandoned cart، KYC reminders، loyalty):</strong> — 58–265 دولار/accelerator.</li>
          <li><strong>دورات «تجربة عميل موحّدة بـ CustomerAI بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Twilio</span>
        <span class="tag">CustomerAI</span>
        <span class="tag">CDP</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 18-10-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="18-10-2026 -- 08-AM.html">
          📰 18 أكتوبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "18-10-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/18-10-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    if new in content:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/18-10-2026 -- 12-AM.html"
    new_line = (
        f"- [`{new}`](news/18-10-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS}) "
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
        "وyُ",
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
