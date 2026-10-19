#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 19-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "19-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 4 Arabic · Coda AI Brain 4 Arabic · "
    "Amplitude AI Analyst 4 Arabic · Oracle OCI Generative AI Agents 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 4 Arabic، Coda AI Brain 4 Arabic، Amplitude AI Analyst 4 Arabic، Oracle OCI Generative AI Agents 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 19 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 4 Arabic الذي يُحوّل «أريد وكيلًا يُتابع طلبات التأشيرة» إلى agent يعمل على Teams وWhatsApp قبل أن تُطفأ شاشة المكتب، إلى Coda AI Brain 4 Arabic الذي يُحوّل جداول وdocs فوضوية إلى نظام تشغيل يُجيب بجملة عربية واحدة، ومن Amplitude AI Analyst 4 Arabic الذي يُ explain لماذا انهار retention ويُ suggest experiments قبل اجتماع product، إلى Oracle OCI Generative AI Agents 4 Arabic الذي يُشغّل وكلاء procurement وfinance فوق بياناتك في region الخليج دون export — أربع قصص ليلية في 19 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للوكلاء والمستندات والتحليلات والسحابة: IT يريد agents بدون months of code، ops teams تغرق في spreadsheets، product managers يطاردون «لماذا؟» بعد كل release، وCIOs يُ insist على data residency. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 19 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 4 Arabic: وكلاء مؤسسية بدون كود — من فكرة عربية إلى production على Teams!</h2>
      <p class="article-lead">«نريد bot يُجيب عن سياسات HR بالخليجي — والـ backlog ممتلئ لستة أشهر». في 19 أكتوبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 4 Arabic</strong>: منصة low-code لبناء agents تفهم الفصحى واللهجات، تُ connect SharePoint وDataverse وDynamics وSAP connectors، تُ orchestrate multi-step flows (approvals، tickets، notifications)، تُ deploy على Teams وMicrosoft 365 Copilot وWhatsApp Business، مع guardrails وaudit وEntra identity — لل governments وbanks وretail في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot Studio 3 كان يُ struggle مع Arabic slot-filling في voice؛ الإصدار 4 يُ dialect packs MENA، يُ benchmark −41% time-to-agent في telco pilot UAE، يُ generative answers مع citations من internal KB، يُ test harness لل regression على 500 utterances، يُ hybrid human handoff، ويُ partner program لل system integrators العرب.</p>
      <p>القدرات الأساسية: Agent designer RTL; Topic branching; Plugin actions; Knowledge grounding; Analytics on deflection; Multi-channel publish.</p>
      <p>للمبدعين العرب: Power Platform boutiques — «Copilot Studio 4 Arabic agent factory in 9 days» لل orgs 500–80K seats. من يُ ship 6 agents/ربع بـ 3800–72000 دولار + care 240–1950 دولار/شهر يبني «مصنع وكلاء Microsoft عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة agent (discovery، topics، KB، UAT، go-live):</strong> 7–18 يومًا — 3800–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ intent tuning وanalytics reviews:</strong> — 240–1950 دولار/شهر.</li>
          <li><strong>Vertical kits (visa، loan status، store locator bilingual):</strong> — 72–310 دولار/kit.</li>
          <li><strong>دورات «وكلاء مؤسسية بـ Copilot Studio بالعربية»:</strong> — 46–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot Studio</span>
        <span class="tag">Agents</span>
        <span class="tag">Low-Code</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Coda AI Brain 4 Arabic: doc واحد يُشغّل الشركة — automations، dashboards، وQ&amp;A فوق بياناتك!</h2>
      <p class="article-lead">«عشرة Notion pages وGoogle Sheet — ولا أحد يعرف الرقم الصحيح للـ runway». في 19 أكتوبر 2026، أطلقت <strong>Coda</strong> <strong>AI Brain 4 Arabic</strong>: intelligence layer فوق docs وtables وpacks، تُ answer أسئلة ops وfinance بالعربية، تُ generate automations من brief («عندما status = delayed أرسل Slack للمدير»)، تُ build dashboards وOKR views RTL، تُ sync Jira وSalesforce وSlack، وتُ maintain single source of truth — لل startups وagencies وdistributed teams في MENA.</p>
      <p>المشكلة التي حلّتها: AI Brain 3 كان يُ hallucinate على Arabic column headers؛ الإصدار 4 يُ structured schema hints، يُ benchmark −38% وقت weekly reporting في agency Cairo، يُ row-level permissions preserved في answers، يُ template gallery (fundraising، hiring، sprint)، يُ mobile Brain chat، ويُ export PDF board packs.</p>
      <p>القدرات الأساسية: Brain Q&amp;A RTL; Automation generator; Formula assist; Pack marketplace; Cross-doc search; Team rituals templates.</p>
      <p>للمبدعين العرب: ops consultants — «Coda AI Brain 4 Arabic operating system in 6 days» لل teams 15–400 users. من يُ deploy 9 brains/ربع بـ 2200–38000 دولار + ops 130–1050 دولار/شهر يبني «استوديو Coda عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Coda AI Brain 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة operating system (tables، automations، Brain، training):</strong> 5–14 يومًا — 2200–38000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ automation refresh وBrain tuning:</strong> — 130–1050 دولار/شهر.</li>
          <li><strong>Industry templates (agency P&amp;L، marketplace ops، NGO grants):</strong> — 55–240 دولار/template.</li>
          <li><strong>دورات «تشغيل الشركة بـ Coda AI Brain بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Coda</span>
        <span class="tag">AI Brain</span>
        <span class="tag">No-Code</span>
        <span class="tag">Ops</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Amplitude AI Analyst 4 Arabic: product intelligence — «لماذا هبط retention؟» بإجابة مُ cited!</h2>
      <p class="article-lead">«الـ dashboard يقول −12% — والمدير يسأل لماذا قبل breakfast». في 19 أكتوبر 2026، أطلقت <strong>Amplitude</strong> <strong>AI Analyst 4 Arabic</strong>: copilot فوق behavioral data يُ parse cohorts وfunnels بالعربية، يُ surface root causes (onboarding step، paywall copy، crash event)، يُ draft experiment hypotheses وsuccess metrics، يُ generate narrative summaries لل executives RTL، يُ link insights إلى Jira وLinear — لل super-apps وfintech وmedia في MENA.</p>
      <p>المشكلة التي حلّتها: AI Analyst 3 كان يُ overfit على English event names؛ الإصدار 4 يُ Arabic event taxonomy mapping، يُ benchmark +19% experiment win rate في neobank KSA بعد 8 أسابيع، يُ anomaly alerts Slack bilingual، يُ privacy-safe aggregation، يُ playbook «churn rescue» و«activation lift»، وبرنامج شريك لل growth consultancies.</p>
      <p>القدرات الأساسية: NL analytics RTL; Cohort explain; Experiment designer; Exec briefs; Integration catalog; Governed SQL export.</p>
      <p>للمبدعين العرب: growth agencies — «Amplitude AI Analyst 4 Arabic insight sprint in 5 days» لل products 50K–5M MAU. من يُ run 8 sprints/ربع بـ 2600–42000 دولار + retainer 150–1200 دولار/شهر يبني «مكتب Amplitude AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Amplitude AI Analyst 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة insight sprint (taxonomy، dashboards، Analyst prompts، workshops):</strong> 4–12 يومًا — 2600–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ experiment reviews وAnalyst tuning:</strong> — 150–1200 دولار/شهر.</li>
          <li><strong>Vertical playbooks (wallet، marketplace seller، streaming):</strong> — 48–225 دولار/playbook.</li>
          <li><strong>دورات «نمو منتج بـ Amplitude AI Analyst بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Amplitude</span>
        <span class="tag">Product Analytics</span>
        <span class="tag">AI Analyst</span>
        <span class="tag">Growth</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Oracle OCI Generative AI Agents 4 Arabic: وكلاء على بياناتك في السحابة — procurement وfinance بلا export!</h2>
      <p class="article-lead">«البيانات لا تغادر region — لكن الفريق يريد ChatGPT على ERP». في 19 أكتوبر 2026، أطلقت <strong>Oracle</strong> <strong>OCI Generative AI Agents 4 Arabic</strong>: agent framework على Oracle Cloud Infrastructure يُ ground على Fusion apps وAutonomous DB وobject storage، يُ answer procurement وAP وinventory بالفصحى واللهجات، يُ execute approved actions (PO create، vendor query، budget check)، يُ enforce policies وSOX controls، يُ deploy في UAE وKSA regions — لل enterprises وpublic sector في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 3 كان يُ require heavy custom RAG؛ الإصدار 4 يُ prebuilt connectors Fusion، يُ benchmark −44% cycle time على vendor onboarding في conglomerate Riyadh، يُ multi-agent orchestration (researcher + approver)، يُ Arabic document ingestion OCR، يُ observability tokens وcost caps، ويُ SI enablement لل partners المحليين.</p>
      <p>القدرات الأساسية: RAG on OCI; Tool use with guardrails; Fusion actions; Data residency; Audit logs; Agent marketplace templates.</p>
      <p>للمبدعين العرب: Oracle partners وERP consultancies — «OCI Generative AI Agents 4 Arabic go-live in 12 days» لل orgs 500–50K employees. من يُ deliver 4 programs/ربع بـ 5200–98000 دولار + managed 320–2600 دولار/شهر يبني «مركز Oracle AI Agents عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Oracle OCI Generative AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة agents (use cases، grounding، UAT، production rollout):</strong> 9–22 يومًا — 5200–98000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ policy updates وagent monitoring:</strong> — 320–2600 دولار/شهر.</li>
          <li><strong>Domain packs (procurement، treasury، HR helpdesk Arabic):</strong> — 85–340 دولار/pack.</li>
          <li><strong>دورات «وكلاء ERP على OCI بالعربية»:</strong> — 52–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Oracle</span>
        <span class="tag">OCI</span>
        <span class="tag">Generative AI Agents</span>
        <span class="tag">ERP</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 19-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="19-10-2026 -- 12-AM.html">
          📰 19 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "19-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/19-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    if new in content:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/18-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/19-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
