#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 18-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "18-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "ElevenLabs Agents 4 Arabic · Pendo AI Guides 4 Arabic · "
    "Sentry Seer AI 4 Arabic · Deel AI Workforce 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — ElevenLabs Agents 4 Arabic، Pendo AI Guides 4 Arabic، Sentry Seer AI 4 Arabic، Deel AI Workforce 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 18 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من ElevenLabs Agents 4 Arabic الذي يُجيب عميلك بصوت بشري ولهجة خليجية أو مصرية قبل أن تُنهي مكالمة Zoom، إلى Pendo AI Guides 4 Arabic الذي يُكتشف أين يتعثر المستخدم في منتجك ويُبني onboarding تفاعليًا بالعربية، ومن Sentry Seer AI 4 Arabic الذي يُحوّل stack trace إلى إصلاح مقترح وPR draft، إلى Deel AI Workforce 4 Arabic الذي يُ automate عقود وتأشيرات وpayroll للموظفين عن بُعد — أربع قصص مسائية في 18 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ للصوت والمنتج والكود والموارد البشرية العالمية: call centers يريدون agents لا تُملّ، product teams تطارد friction في UX، مهندسون يُ tired من incidents متكررة، وHR يُدير فرقًا موزّعة عبر 40 دولة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 18 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>ElevenLabs Agents 4 Arabic: وكيل صوتي حيّ — يُ sell، يُ support، ويُ handoff بثقة!</h2>
      <p class="article-lead">«العميل يُفضّل الصوت على الشات — والانتظار 12 دقيقة». في 18 أكتوبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Agents 4 Arabic</strong>: منصة voice agents تُ stream محادثات RTL بزمن استجابة &lt;800ms، تُ clone brand voice أو تختار أصوات MSA/Gulf/Egypt/Levant، تُ integrate CRM وZendesk وShopify، تُ execute tools (book slot، check order، escalate)، تُ record transcripts bilingual لل compliance، وتُ deploy على phone وWhatsApp voice وweb widget — لل banking وhealthcare وe-commerce في المنطقة.</p>
      <p>المشكلة التي حلّتها: Agents 3 كان يُ stumble على أرقام عربية-هندية mixed؛ الإصدار 4 يُ normalized numerals، يُ benchmark +31% containment في telco pilot KSA، يُ emotion-aware pacing لل upset callers، يُ knowledge base RAG مع citations read-aloud، يُ latency edge nodes في Dubai، ويُ partner certification لل contact center SIs.</p>
      <p>القدرات الأساسية: Real-time voice RTL; Dialect packs; Tool calling; Human handoff; Analytics QA; SOC2-ready logging.</p>
      <p>للمبدعين العرب: CX voice studios — «ElevenLabs Agents 4 Arabic go-live in 9 days» لل brands 10K–2M calls/month. من يُ launch 5 agents/ربع بـ 4200–58000 دولار + tuning 165–1380 دولار/شهر يبني «استوديو voice AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة voice agent (persona، KB، integrations، UAT):</strong> 6–15 يومًا — 4200–58000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ prompt tuning وQA listening:</strong> — 165–1380 دولار/شهر.</li>
          <li><strong>Vertical kits (collections، appointment، order status bilingual):</strong> — 62–285 دولار/kit.</li>
          <li><strong>دورات «مراكز اتصال ذكية بـ ElevenLabs بالعربية»:</strong> — 44–208 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Agents</span>
        <span class="tag">CX</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Pendo AI Guides 4 Arabic: منتجك يُ teach نفسه — friction، tours، وNPS مرفوع!</h2>
      <p class="article-lead">«70% يُ drop عند خطوة KYC — ولا أحد يعرف لماذا». في 18 أكتوبر 2026، أطلقت <strong>Pendo</strong> <strong>AI Guides 4 Arabic</strong>: product intelligence تُ analyze session replays وevents، تُ detect friction clusters RTL، تُ generate in-app guides وtooltips من brief عربي، تُ personalize paths حسب plan وlocale، تُ A/B copy MSA vs dialect، تُ sync insights إلى Jira وSlack، وتُ measure lift على activation وretention — لل SaaS وfintech وmarketplaces في MENA.</p>
      <p>المشكلة التي حلّتها: Guides 3 كان copy suggestions English-first؛ الإصدار 4 يُ native Arabic UX writing، يُ benchmark +22% activation في neobank UAE بعد 5 أسابيع، يُ sentiment على in-app surveys Arabic، يُ playbook library (onboarding، upsell، churn save)، يُ privacy masking PII in replays، ويُ enablement لل product-led growth consultants.</p>
      <p>القدرات الأساسية: Friction AI; Guide generator RTL; Segment targeting; Experiment engine; Roadmap signals; Replay search Arabic NL.</p>
      <p>للمبدعين العرب: PLG agencies — «Pendo AI Guides 4 Arabic activation fix in 7 days» لل apps 5K–500K MAU. من يُ deploy 8 stacks/ربع بـ 2900–44000 دولار + optimization 120–980 دولار/شهر يبني «مكتب Pendo عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Pendo AI Guides 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة PLG (instrumentation، guides، experiments، training):</strong> 5–14 يومًا — 2900–44000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ guide refresh وfriction reports:</strong> — 120–980 دولار/شهر.</li>
          <li><strong>Industry playbooks (B2B SaaS، wallet، marketplace seller):</strong> — 48–215 دولار/playbook.</li>
          <li><strong>دورات «نمو منتج ذكي بـ Pendo بالعربية»:</strong> — 35–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Pendo</span>
        <span class="tag">Product Analytics</span>
        <span class="tag">In-App Guides</span>
        <span class="tag">PLG</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Sentry Seer AI 4 Arabic: من crash إلى fix — root cause، patch، وPR بلسان فريقك!</h2>
      <p class="article-lead">«نفس NullPointer كل جمعة — والـ on-call ينام 3 ساعات». في 18 أكtober 2026، أطلقت <strong>Sentry</strong> <strong>Seer AI 4 Arabic</strong>: dev copilot فوق errors وperformance يُ explain incidents RTL لل engineers وmanagers، يُ trace regressions عبر releases، يُ suggest code fixes مع diff previews، يُ draft GitHub/GitLab PR descriptions Arabic/EN، يُ link runbooks وSlack threads، يُ prioritize by user impact وrevenue — لل scale-ups وenterprises MENA.</p>
      <p>المشكلة التي حلّتها: Seer 3 كان summaries technical English-only؛ الإصدار 4 يُ bilingual postmortems، يُ benchmark −37% MTTR في ecommerce Cairo، يُ aut fix لل common patterns (config، i18n RTL layout)، يُ Seer chat في IDE plugins، يُ governance لـ auto-apply في staging only، ويُ partner program لل DevOps boutiques العرب.</p>
      <p>القدرات الأساسية: Root cause AI; Fix suggestions; PR drafts; Release health; Arabic exec summaries; Integration catalog.</p>
      <p>للمبدعين العرب: SRE freelancers — «Sentry Seer AI 4 Arabic reliability sprint in 6 days» لل teams 10–300 engineers. من يُ onboard 6 orgs/ربع بـ 2400–36000 دولار + retainer 95–820 دولار/شهر يبني «مختبر Seer عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sentry Seer AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة observability (Seer rules، dashboards، runbooks، training):</strong> 4–12 يومًا — 2400–36000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ incident reviews وSeer tuning:</strong> — 95–820 دولار/شهر.</li>
          <li><strong>Fix pattern libraries (mobile RTL، payment webhooks، auth):</strong> — 52–228 دولار/library.</li>
          <li><strong>دورات «موثوقية ذكية بـ Sentry Seer بالعربية»:</strong> — 38–182 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sentry</span>
        <span class="tag">Seer AI</span>
        <span class="tag">DevOps</span>
        <span class="tag">SRE</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Deel AI Workforce 4 Arabic: توظيف عالمي — عقود، compliance، وpayroll بأمر عربي!</h2>
      <p class="article-lead">«نريد موظفًا في تونس وآخر في أمريكا — والlegal يريد كل شيء compliant غدًا». في 18 أكtober 2026، أطلقت <strong>Deel</strong> <strong>AI Workforce 4 Arabic</strong>: HR platform copilot يُ draft employment contracts MSA-compliant حسب country، يُ answer policy questions RTL لل employees، يُ automate onboarding checklist وequipment، يُ flag visa وtax risks، يُ reconcile payroll anomalies، يُ generate executive workforce reports Arabic — لل remote-first companies وagencies في MENA hiring globally.</p>
      <p>المشكلة التي حلّتها: Workforce 3 كان chat English-centric؛ الإصدار 4 يُ dialect HR FAQs، يُ benchmark −48% time-to-hire paperwork في agency Dubai، يُ integration Workday وSlack وNotion، يُ contractor vs employee classifier AI، يُ audit trail bilingual لل regulators، ويُ reseller margins لل HR consultancies.</p>
      <p>القدرات الأساسية: Contract AI RTL; Policy Q&amp;A; Payroll assist; Compliance alerts; Workforce analytics; Employee self-service Arabic.</p>
      <p>للمبدعين العرب: global HR boutiques — «Deel AI Workforce 4 Arabic stack in 10 days» لل companies 20–5000 workers. من يُ implement 5 accounts/ربع بـ 3500–52000 دولار + care 180–1450 دولار/شهر يبني «استوديو Deel AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Deel AI Workforce 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة global HR (entities، contracts، payroll rules، go-live):</strong> 7–18 يومًا — 3500–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ compliance updates وworkforce reports:</strong> — 180–1450 دولار/شهر.</li>
          <li><strong>Country packs (Egypt، KSA، UAE، Morocco hiring):</strong> — 68–295 دولار/pack.</li>
          <li><strong>دورات «توظيف عالمي ذكي بـ Deel بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Deel</span>
        <span class="tag">Workforce AI</span>
        <span class="tag">HR</span>
        <span class="tag">Global Payroll</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 18-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="18-10-2026 -- 04-PM.html">
          📰 18 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "18-10-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/18-10-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    if new in content:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/18-10-2026 -- 08-AM.html"
    new_line = (
        f"- [`{new}`](news/18-10-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS}) "
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
