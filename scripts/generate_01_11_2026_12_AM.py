#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 01-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "01-11-2026 -- 12-AM.html"
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
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Anthropic Claude for Excel 3 Arabic، Deepgram Voice Agent 2 Arabic، Retool AI Agents 3 Arabic، Linear AI Insights 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 1 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Anthropic Claude for Excel 3 Arabic الذي يُحوّل مصنف الميزانية إلى محلل مالي يُجيب بالعربية قبل أن يُطفأ ضوء المكتب، إلى Deepgram Voice Agent 2 Arabic الذي يُجيب مكالمات WhatsApp وIVR بصوت طبيعي بلهجات MENA، ومن Retool AI Agents 3 Arabic الذي يُبني لوحات ops ووكلاء داخليين من prompt واحد، إلى Linear AI Insights 3 Arabic الذي يُترجم chaos الـ backlog إلى خطة sprint واضحة — أربع قصص ليلية في 1 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمالية ومراكز الاتصال وفرق العمليات والمنتج: pivot tables تتأخر، queues تطول، dashboards تُبنى يدويًا، وstandups تغرق في «من يفعل ماذا؟». أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 1 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Anthropic Claude for Excel 3 Arabic: CFO رقمي — scenarios، narratives، وaudit trails بلسان عربي!</h2>
      <p class="article-lead">«أعطني variance نوفمبر للفروع الخليجية مع ثلاثة scenarios وملخص للمجلس — والاجتماع بعد 45 دقيقة». في 1 نوفمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude for Excel 3 Arabic</strong>: add-in enterprise يُ read workbooks ضخمة وlinked queries، يُ answer بالفصحى واللهجات («لماذا تراجع margin الدمام؟»)، يُ write formulas وpivot tables وPower Query steps آمنة، يُ generate Monte Carlo scenarios وwaterfall charts، يُ produce board-ready narratives RTL، يُ connect Snowflake وSAP وNetSuite exports، يُ cell-level audit وrollback، يُ policy guardrails لل PII، ويُ SSO مع data residency EU/US/GCC — لل FP&amp;A وconsulting وfamily offices في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُ slow على ملفات 200+ sheet؛ الإصدار 3 يُ incremental indexing، يُ benchmark −44% وقت «سؤال إلى deck» في conglomerate الرياض، يُ bilingual footnotes EN+AR، يُ template packs (retail، hospitality، logistics)، يُ copilot mode داخل Teams، ويُ partner certifications لل finance boutiques.</p>
      <p>القدرات الأساسية: Arabic financial Q&amp;A; Scenario modeling; Executive narratives RTL; ERP connectors; Audit and rollback; Enterprise governance.</p>
      <p>للمبدعين العرب: finance freelancers — «Claude for Excel 3 Arabic FP&amp;A sprint in 5 days» لل teams 8–120 analysts. من يُ deliver 10 sprints/ربع بـ 2400–52000 دولار + retainer 190–1750 دولار/شهر يبني «مكتب Claude Excel عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude for Excel 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة FP&amp;A sprint (templates، connectors، UAT، board pack):</strong> 4–16 يومًا — 2400–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ model refresh وvariance reviews:</strong> — 190–1750 دولار/شهر.</li>
          <li><strong>حزم قطاعية (F&amp;B، proptech، healthcare، logistics):</strong> — 55–265 دولار/حزمة.</li>
          <li><strong>دورات «تحليل مالي بـ Claude for Excel بالعربية»:</strong> — 48–228 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Excel</span>
        <span class="tag">Finance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Deepgram Voice Agent 2 Arabic: مركز اتصال ذكي — STT، TTS، وhandoff بلسان العميل!</h2>
      <p class="article-lead">«الطابور 900 مكالمة — والعميل يريد إجابة بالخليجية الآن». في 1 نوفمبر 2026، أطلقت <strong>Deepgram</strong> <strong>Voice Agent 2 Arabic</strong>: stack voice AI يُ combine streaming STT وneural TTS للهجات (Gulf، Egyptian، Levantine، MSA)، يُ run dialog policies وtool calls (CRM، booking، payments)، يُ barge-in طبيعي وlatency &lt;300ms، يُ warm transfer إلى human مع transcript RTL، يُ integrate Twilio وGenesys وAmazon Connect، يُ analytics لل intent وCSAT، يُ on-prem GPU option لل banks، ويُ marketplace prompts لل retail وhealthcare في MENA.</p>
      <p>المشكلة التي حلّتها: Voice Agent 1 كان يُ confuse similar Arabic phonemes في noisy lines؛ الإصدار 2 يُ dialect classifier live، يُ benchmark −38% AHT في telco pilot الكويت، يُ WhatsApp voice note replies، يُ PCI-safe payment flows، يُ compliance recordings، ويُ revenue share لل SI partners.</p>
      <p>القدرات الأساسية: Arabic STT/TTS; Real-time agents; CRM tool use; Human handoff; Contact center integrations; On-prem deploy.</p>
      <p>للمبدعين العرب: CX agencies — «Deepgram Voice Agent 2 Arabic IVR pilot in 8 days» لل orgs 50–8000 agents. من يُ ship 7 pilots/ربع بـ 3800–72000 دولار + ops 320–2800 دولار/شهر يبني «مركز Deepgram عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Deepgram Voice Agent 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة IVR pilot (flows، integrations، QA، go-live):</strong> 6–22 يومًا — 3800–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ prompt tuning وquality monitoring:</strong> — 320–2800 دولار/شهر.</li>
          <li><strong>Vertical packs (banking، delivery، clinics، government hotlines):</strong> — 62–290 دولار/pack.</li>
          <li><strong>دورات «بناء voice agents بـ Deepgram بالعربية»:</strong> — 54–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Deepgram</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Contact Center</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Retool AI Agents 3 Arabic: ops في أيام — internal tools، workflows، وRBAC من وصف عربي!</h2>
      <p class="article-lead">«نحتاج portal للموافقات يربط Oracle وSlack — والـ IT مشغول شهرين». في 1 نوفمبر 2026، أطلقت <strong>Retool</strong> <strong>AI Agents 3 Arabic</strong>: builder يُ generate apps وworkflows من prompt عربي («ابنِ لوحة موافقات procurement مع audit log»)، يُ wire databases وREST وSAP وGoogle Sheets، يُ AI steps (classify، summarize، draft emails RTL)، يُ RBAC وSSO وversion history، يُ mobile-friendly RTL layouts، يُ self-host وRetool Cloud، يُ catalog لل reusable modules، ويُ partner program لل SIs في MENA — لل ops وHR وfinance mid-market.</p>
      <p>المشكلة التي حلّتها: Agents 2 كان يُ hallucinate schema على Arabic column names؛ الإصدار 3 يُ schema introspection وconfirm steps، يُ benchmark −51% time-to-app في logistics operator جدة، يُ Arabic validation messages، يُ approval chains multi-level، ويُ export to Git لل enterprises.</p>
      <p>القدرات الأساسية: Prompt-to-app Arabic; Workflow automation; Enterprise connectors; AI enrichment steps; Governance RBAC; Self-host option.</p>
      <p>للمبدعين العرب: low-code studios — «Retool AI Agents 3 Arabic ops portal in 6 days» لل orgs 30–2000 staff. من يُ deliver 9 portals/ربع بـ 2100–46000 دولار + managed 175–1450 دولار/شهر يبني «استوديو Retool عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Retool AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة ops portal (discovery، build، training، handoff):</strong> 5–18 يومًا — 2100–46000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ enhancements وincident support:</strong> — 175–1450 دولار/شهر.</li>
          <li><strong>Module packs (HR onboarding، vendor mgmt، ticket triage، inventory):</strong> — 38–185 دولار/module.</li>
          <li><strong>دورات «أدوات داخلية بـ Retool AI بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Retool</span>
        <span class="tag">Low-code</span>
        <span class="tag">Internal Tools</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Linear AI Insights 3 Arabic: product velocity — triage، roadmaps، وstatus بلسان squad عربي!</h2>
      <p class="article-lead">«200 issue مفتوح — والمدير يريد roadmap قبل standup». في 1 نوفمبر 2026، أطلقت <strong>Linear</strong> <strong>AI Insights 3 Arabic</strong>: layer فوق Linear يُ ingest issues وcycles وGitHub PRs، يُ summarize sprint health بالعربية، يُ suggest prioritization وdependencies، يُ draft release notes وstakeholder updates RTL، يُ auto-triage inbound bugs من Slack وemail، يُ forecast delivery dates مع confidence bands، يُ integrate Notion وFigma links، يُ team insights لل managers، ويُ enterprise SSO — لل startups وscale-ups وproduct orgs في MENA.</p>
      <p>المشكلة التي حلّتها: Insights 2 كان English-only summaries؛ الإصدار 3 يُ bilingual updates، يُ benchmark −35% وقت weekly planning في fintech القاهرة، يُ Arabic label taxonomy، يُ custom rules per squad، يُ API لل BI dashboards، ويُ marketplace playbooks لل agencies.</p>
      <p>القدرات الأساسية: Arabic sprint summaries; Smart triage; Roadmap suggestions; Release comms RTL; Delivery forecasts; Integrations.</p>
      <p>للمبدعين العرب: product ops consultants — «Linear AI Insights 3 Arabic velocity kit in 4 days» لل teams 5–80 engineers. من يُ run 12 kits/ربع بـ 980–18500 دولار + coaching 85–720 دولار/شهر يبني «غرفة Linear AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Linear AI Insights 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة velocity kit (taxonomy، rules، training، first cycle):</strong> 3–12 يومًا — 980–18500 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ triage tuning وexec reporting:</strong> — 85–720 دولار/شهر.</li>
          <li><strong>Playbooks (mobile app squad، platform team، agency client portal):</strong> — 32–148 دولار/playbook.</li>
          <li><strong>دورات «إدارة منتج بـ Linear AI Insights بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Linear</span>
        <span class="tag">Product</span>
        <span class="tag">Engineering</span>
        <span class="tag">Roadmaps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 01-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="01-11-2026 -- 12-AM.html">
          📰 1 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "01-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/01-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/31-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/01-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
