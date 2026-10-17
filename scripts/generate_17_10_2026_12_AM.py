#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 17-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "17-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Anthropic Claude Code Enterprise 4 Arabic",
    "Google Vids AI 4 Arabic",
    "Splunk AI Assistant 4 Arabic",
    "Make.com AI Agents 4 Arabic",
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Anthropic Claude Code Enterprise 4 Arabic، Google Vids AI 4 Arabic، Splunk AI Assistant 4 Arabic، Make.com AI Agents 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 17 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Anthropic Claude Code Enterprise 4 Arabic الذي يُصلّح legacy repo ويُكتب tests بلهجة فريقك قبل أن يُغلق آخر مطوّر اللابتوب، إلى Google Vids AI 4 Arabic الذي يُحوّل slide deck إلى فيديو training عربي بصوت طبيعي، ومن Splunk AI Assistant 4 Arabic الذي يُترجم سؤال SOC بالفصحى إلى SPL وplaybook قبل أن يُرنّ هاتف on-call، إلى Make.com AI Agents 4 Arabic الذي يُبني automation يُغلق leads وsync invoices بين ERP وWhatsApp — أربع قصص ليلية في 17 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للهندسة والتواصل والأمن والأتمتة: backlog يتراكم، onboarding يتأخر على فيديوهات، alerts تغرق غرف العمليات، وintegrations تُستهلك أيامًا. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 17 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Anthropic Claude Code Enterprise 4 Arabic: مهندس وكيل — refactor، tests، وPRs بلسان squad عربي!</h2>
      <p class="article-lead">«الـ migration موعدها الأسبوع القادم — وال coverage لا يزال 41%». في 17 أكتوبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude Code Enterprise 4 Arabic</strong>: بيئة coding agent للمؤسسات تُفهم monorepos وpolicies داخلية، تُ draft plans بالعربية لل review، تُ execute refactors عبر subagents، تُ generate tests وfix CI، تُ open pull requests مع summaries RTL، وتُ respect secrets scanning وaudit logs — لل banks وtelcos وgovtech في MENA.</p>
      <p>المشكلة التي حلّتها: Claude Code Enterprise 3 كان يُخلط اللهجات في commit messages؛ الإصدار 4 يُ MSA وGulf technical glossaries، يُ benchmark −44% وقت «feature to merge» في fintech سعودي، يُ parallel agents على modules، يُ integration GitHub/GitLab وJira، يُ VPC deploy options، ويُ partner enablement في Dubai Internet City.</p>
      <p>القدرات الأساسية: Plan mode بالعربية; Subagent orchestration; Test generation; Security review pass; IDE وterminal وweb; Admin quotas وSSO.</p>
      <p>للمبدعين العرب: dev shops وplatform engineers — «Claude Code Enterprise 4 Arabic migration sprint in 10 days» لل codebases 50k–2M LOC. من يُ deliver 5 sprints/ربع بـ 6200–98000 دولار + retainer 420–3400 دولار/شهر يبني «مركز Claude Code عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Anthropic Claude Code Enterprise 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة migration sprint (plan، refactor، tests، CI):</strong> 7–18 يومًا — 6200–98000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ agent governance وprompt libraries:</strong> — 420–3400 دولار/شهر.</li>
          <li><strong>Vertical playbooks (core banking، telecom OSS، gov portals):</strong> — 78–340 دولار/playbook.</li>
          <li><strong>دورات «هندسة برمجية بـ Claude Code Enterprise بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude Code</span>
        <span class="tag">Enterprise</span>
        <span class="tag">DevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Google Vids AI 4 Arabic: فيديو workspace — من slides إلى training وcomms RTL بصوت طبيعي!</h2>
      <p class="article-lead">«HR تريد onboarding بالعربية — والاستوديو مشغول شهرًا». في 17 أكتوبر 2026، أطلقت <strong>Google</strong> <strong>Vids AI 4 Arabic</strong>: تطبيق فيديو داخل Workspace يُ generate scripts MSA/dialect، يُ record screen وtalking head، يُ auto-chapters وcaptions RTL، يُ translate EN↔AR، يُ brand templates من Drive، ويُ publish إلى Sites وClassroom وChat — لل enterprises وuniversities وretail chains في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: Vids AI 3 كان voice-over robotic على Egyptian؛ الإصدار 4 يُ ElevenLabs-quality Arabic voices licensed، يُ benchmark −47% وقت «policy video go-live» في holding إماراتي، يُ AI b-roll من stock MENA، يُ DLP على scripts، يُ viewer analytics heatmaps، ويُ Meet embed لل async updates.</p>
      <p>القدرات الأساسية: Script gen من Docs; Avatar presenter RTL; Auto edit وmusic; Multi-speaker; Approval workflow; Admin retention policies.</p>
      <p>للمبدعين العرب: L&amp;D studios — «Vids AI 4 Arabic onboarding library in 6 days» لل orgs 5–80 videos/quarter. من يُ produce 12 libraries/سنة بـ 1800–42000 دولار + refresh 150–1200 دولار/شهر يبني «استوديو Vids عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Vids AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة video library (scripts، record، brand، publish):</strong> 4–14 يومًا — 1800–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لتحديث modules وanalytics:</strong> — 150–1200 دولار/شهر.</li>
          <li><strong>Template packs (compliance، sales، retail SOPs RTL):</strong> — 42–185 دولار/pack.</li>
          <li><strong>دورات «تواصل مؤسسي بـ Google Vids AI بالعربية»:</strong> — 38–182 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Vids AI</span>
        <span class="tag">Workspace</span>
        <span class="tag">L&amp;D</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Splunk AI Assistant 4 Arabic: SOC copilot — من alert storm إلى SPL وremediation بلغة فريقك!</h2>
      <p class="article-lead">«ثلاثمائة alert — والمحلل الجديد لا يعرف أي index يبحث». في 17 أكتوبر 2026، أطلقت <strong>Splunk</strong> <strong>AI Assistant 4 Arabic</strong>: copilot فوق Enterprise Security وITSI يُ parse أسئلة عربية إلى SPL آمن، يُ correlate incidents، يُ suggest playbooks MITRE-mapped، يُ draft post-incident reports RTL، يُ tune detections، ويُ handoff إلى ServiceNow وPagerDuty — لل telcos وbanks وcritical infra في MENA.</p>
      <p>المشكلة التي حلّتها: Assistant 3 كان read-only على بعض data models؛ الإصدار 4 يُ governed actions (isolate host staging)، يُ benchmark −38% MTTR في SOC قطر، يُ Arabic log parsing hints، يُ integration MCP لل threat intel feeds، يُ on-call voice briefings، ويُ residency options KSA/EU.</p>
      <p>القدرات الأساسية: NL to SPL; Investigation notebooks; Detection authoring; Executive dashboards Arabic; Role-based guardrails; Partner MSSP program.</p>
      <p>للمبدعين العرب: MSSPs وsecurity boutiques — «Splunk AI Assistant 4 Arabic SOC uplift in 14 days» لل orgs 50–500 GB/day. من يُ deploy 4 uplifts/ربع بـ 5400–88000 دولار + managed 360–2900 دولار/شهر يبني «مركز Splunk AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Splunk AI Assistant 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة SOC uplift (use cases، SPL library، training RTL):</strong> 10–24 يومًا — 5400–88000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ detection tuning وAI QA:</strong> — 360–2900 دولار/شهر.</li>
          <li><strong>Industry packs (finance fraud، OT/ICS، cloud):</strong> — 68–295 دولار/pack.</li>
          <li><strong>دورات «SOC ذكي بـ Splunk AI Assistant بالعربية»:</strong> — 55–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Splunk</span>
        <span class="tag">Security</span>
        <span class="tag">SOC</span>
        <span class="tag">SIEM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Make.com AI Agents 4 Arabic: صِف workflow بالعربية — فيُبنى agent يُ sync ERP وWhatsApp وCRM!</h2>
      <p class="article-lead">«نريد lead من Instagram يُ validate في ERP ويُ reply على WhatsApp — وال IT مشغول». في 17 أكتوبر 2026، أطلقت <strong>Make.com</strong> <strong>AI Agents 4 Arabic</strong>: orchestrator يُ translate brief عربي إلى scenarios multi-step، يُ choose apps (Shopify، Zoho، SAP B1، Meta، Twilio)، يُ add error handling وlogging، يُ monitor costs، يُ version scenarios كمنتجات، ويُ sell templates في marketplace — لل agencies وops freelancers وSMBs في MENA.</p>
      <p>المشكلة التي حلّتها: AI Scenarios 3 كان يُ break على Arabic variable names؛ الإصدار 4 يُ UTF-8 safe paths، يُ benchmark −52% وقت «POC to production» في logistics مصري، يُ human-in-the-loop approvals، يُ OAuth vault enterprise، يُ white-label partner portal، ويُ training cohorts Cairo/Riyadh.</p>
      <p>القدرات الأساسية: Natural language to scenario; Agent memory; Conditional routing; Webhooks وAPI; Observability dashboard; SOC2 وGDPR tooling.</p>
      <p>للمبدعين العرب: automation agencies — «Make.com AI Agents 4 Arabic revenue stack in 5 days» لل clients 3–15 workflows. من يُ ship 16 stacks/ربع بـ 1400–32000 دولار + care 120–950 دولار/شهر يبني «مكتب Make AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Make.com AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue stack (workflows، QA، handoff docs RTL):</strong> 3–12 يومًا — 1400–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لل monitoring وoptimizations:</strong> — 120–950 دولار/شهر.</li>
          <li><strong>Template packs (e-commerce، clinics، real estate leads):</strong> — 35–158 دولار/template.</li>
          <li><strong>دورات «أتمتة مدفوعة بـ Make AI Agents بالعربية»:</strong> — 34–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Make.com</span>
        <span class="tag">Automation</span>
        <span class="tag">Agents</span>
        <span class="tag">No-Code</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 17-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="17-10-2026 -- 12-AM.html">
          📰 17 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Anthropic Claude Code Enterprise 4 Arabic · Google Vids AI 4 Arabic · Splunk AI Assistant 4 Arabic · Make.com AI Agents 4 Arabic</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "17-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    old = "news/16-10-2026 -- 04-PM.html"
    new = "news/17-10-2026 -- 12-AM.html"
    topics = " · ".join(TOPICS)
    content = README.read_text(encoding="utf-8")
    if new not in content:
        content = content.replace(
            f"[`{old}`](news/16-10-2026%20--%2004-PM.html) — أحدث إصدار",
            f"[`{new}`](news/17-10-2026%20--%2012-AM.html) — أحدث إصدار ({topics})",
        )
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
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
        "yُ",
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
