#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 04-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "04-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Google Jules 2 Arabic · Tabnine Enterprise 3 Arabic · "
    "Sourcegraph Cody 5 Arabic · LangChain LangSmith Agents 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Jules 2 Arabic، Tabnine Enterprise 3 Arabic، Sourcegraph Cody 5 Arabic، LangChain LangSmith Agents 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 4 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Google Jules 2 Arabic الذي يُغلق issues في GitHub ويُرجع pull requests بينما الفريق نائم، إلى Tabnine Enterprise 3 Arabic الذي يُ completion الكود بلهجة squad عربي دون تسريب secrets، ومن Sourcegraph Cody 5 Arabic الذي يُ hunt عبر monorepo ضخم ويُ explain legacy modules بالفصحى، إلى LangChain LangSmith Agents 3 Arabic الذي يُ catch regressions في وكلاء production قبل أن يُ desync CRM — أربع قصص ليلية في 4 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة لفرق engineering وplatform وDevOps: backlog يتراكم، copilots تُ leak snippets حساسة، repos تبدو متاهة، وagents في production تُ hallucinate دون trace. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 4 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Jules 2 Arabic: وكيل كود ليلي — من issue عربي إلى PR وtests جاهزة!</h2>
      <p class="article-lead">«الـ bug في checkout RTL — والـ on-call نائم». في 4 نوفمبر 2026، أطلقت <strong>Google</strong> <strong>Jules 2 Arabic</strong>: coding agent سحابي يُ connect GitHub وGitLab وCloud Source Repositories، يُ read issues وSlack threads بالعربية والإنجليزية، يُ plan fix في sandbox معزول، يُ edit multi-file مع style guide awareness، يُ run tests وlinters، يُ open pull request مع summary RTL لل reviewers، يُ respect VPC-SC وIAM وsecret scanning، ويُ schedule overnight runs — لل startups وenterprises في MENA.</p>
      <p>المشكلة التي حلّتها: Jules 1 كان يُ misread Arabic variable names في PHP legacy؛ الإصدار 2 يُ bilingual code context، يُ benchmark −46% time-to-fix P1 في marketplace مصر، يُ parallel tasks لـ microservices، يُ human approval قبل merge to main، يُ integrate Cloud Build وArtifact Registry، ويُ partner playbooks لل fintech وgov digital.</p>
      <p>القدرات الأساسية: Arabic issue to PR; Isolated cloud sandbox; Multi-file agent; CI and test loops; Approval gates; Enterprise IAM.</p>
      <p>للمبدعين العرب: dev consultancies — «Jules 2 Arabic overnight delivery in 6 days» لل teams 4–80 engineers. من يُ run 9 programs/ربع بـ 2200–48000 دولار + managed 170–1400 دولار/شهر يبني «خط Jules عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Jules 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة Jules rollout (repos، policies، pilot sprint، training):</strong> 5–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ overnight queue وreview tuning:</strong> — 170–1400 دولار/شهر.</li>
          <li><strong>Vertical runbooks (payments RTL، ERP، mobile):</strong> — 45–195 دولار/runbook.</li>
          <li><strong>دورات «تسليم ليلي بـ Jules بالعربية»:</strong> — 46–215 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Jules</span>
        <span class="tag">Coding Agent</span>
        <span class="tag">DevOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Tabnine Enterprise 3 Arabic: copilot خاص — completion، chat، وzero data retention!</h2>
      <p class="article-lead">«المطور لصق customer PII في prompt — وال compliance يرتجف». في 4 نوفمبر 2026، أطلقت <strong>Tabnine</strong> <strong>Enterprise 3 Arabic</strong>: AI assistant لل IDE (VS Code، JetBrains، Visual Studio) يُ train على codebase داخل VPC، يُ suggest completions وrefactors بلهجة comments عربية، يُ chat عن architecture مع citations إلى files، يُ enforce zero retention وair-gapped options، يُ block secrets وlicense violations، يُ admin dashboards RTL، ويُ SSO وSCIM — لل banks وhealthtech وoutsourcing في MENA.</p>
      <p>المشكلة التي حلّتها: Enterprise 2 كان weak في Arabic identifiers في Kotlin وSwift؛ الإصدار 3 يُ MENA tokenizer، يُ benchmark +22% acceptance rate في telco الرياض، يُ team-specific context per squad، يُ policy packs لل PCI-style repos، ويُ partner certification في Dubai وCairo.</p>
      <p>القدرات الأساسية: Private model hosting; Arabic-aware completions; Repo-grounded chat; Secret and license guardrails; Admin analytics RTL; Air-gapped deploy.</p>
      <p>للمبدعين العرب: security-first dev shops — «Tabnine Enterprise 3 Arabic secure copilot in 8 days» لل orgs 20–2000 devs. من يُ deploy 7 stacks/ربع بـ 1900–42000 دولار + care 150–1250 دولار/شهر يبني «مكتب Tabnine عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Tabnine Enterprise 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة secure copilot (VPC، indexing، policies، enablement):</strong> 6–16 يومًا — 1900–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ policy refresh وusage reviews:</strong> — 150–1250 دولار/شهر.</li>
          <li><strong>Compliance kits (banking، health، gov):</strong> — 52–230 دولار/kit.</li>
          <li><strong>دورات «copilot آمن بـ Tabnine بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Tabnine</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Security</span>
        <span class="tag">IDE</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Sourcegraph Cody 5 Arabic: عقل monorepo — search، explain، وrefactor بأمر عربي!</h2>
      <p class="article-lead">«أين logic الدفع؟ — والـ repo 400GB». في 4 نوفمبر 2026، أطلقت <strong>Sourcegraph</strong> <strong>Cody 5 Arabic</strong>: AI layer فوق Sourcegraph code intelligence يُ semantic search في repos ضخمة، يُ explain modules وdependencies بالعربية مع links إلى symbols، يُ propose refactors وmigrations، يُ generate unit tests من specs RTL، يُ batch changes عبر Cody Agents، يُ respect ACLs وaudit logs، ويُ integrate GitHub Enterprise وGitLab وBitbucket — لل scale-ups وenterprises 500–50000 devs.</p>
      <p>المشكلة التي حلّتها: Cody 4 كان يُ confuse homographs في Arabic comments؛ الإصدار 5 يُ cross-repo context graph، يُ benchmark −39% onboarding time لل junior devs في conglomerate الخليج، يُ migration assistants (Java 8→21، Angular→React)، يُ security review mode لل OWASP hotspots، ويُ partner SKUs لل SI.</p>
      <p>القدرات الأساسية: Arabic code search; Symbol-cited explanations; Agentic refactors; Test generation RTL; ACL-aware access; Enterprise audit.</p>
      <p>للمبدعين العرب: platform engineering boutiques — «Cody 5 Arabic monorepo brain in 10 days» لل orgs 50–800 repos. من يُ deliver 6 brains/ربع بـ 2600–55000 دولار + retainer 190–1550 دولار/شهر يبني «استوديو Cody عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sourcegraph Cody 5 Arabic؟</h3>
        <ul>
          <li><strong>باقة monorepo brain (indexing، Cody tuning، pilot refactor):</strong> 7–18 يومًا — 2600–55000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ context refresh وagent QA:</strong> — 190–1550 دولار/شهر.</li>
          <li><strong>Migration playbooks (legacy، microservices، mobile):</strong> — 58–245 دولار/playbook.</li>
          <li><strong>دورات «فهم codebase بـ Cody بالعربية»:</strong> — 44–208 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sourcegraph</span>
        <span class="tag">Cody</span>
        <span class="tag">Code Search</span>
        <span class="tag">Platform</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>LangChain LangSmith Agents 3 Arabic: مراقبة وكلاء — traces، evals، وإصلاح قبل الفجر!</h2>
      <p class="article-lead">«الوكيل باع خصمًا 90% — ولا trace يُ explain لماذا». في 4 نوفمبر 2026، أطلقت <strong>LangChain</strong> <strong>LangSmith Agents 3 Arabic</strong>: observability suite لل agents في production تُ ingest traces من LangGraph وCrewAI وcustom stacks، تُ visualize tool chains بالعربية مع cost وlatency، تُ run eval suites على dialect packs (Gulf، Levant، Egyptian)، تُ auto-alert على regression بعد prompt deploy، تُ suggest guardrails وfallback models، تُ human annotation RTL، تُ export compliance reports، ويُ SSO وdata residency EU/Middle East — لل fintech وe-commerce وBPO في MENA.</p>
      <p>المشكلة التي حلّتها: LangSmith Agents 2 كان summaries إنجليزية فقط؛ الإصدار 3 يُ Arabic incident narratives لل on-call، يُ benchmark −44% MTTR في insuretech دبي، يُ dataset curation PII-safe من logs، يُ A/B prompts مع stats، يُ webhooks لـ Slack وTeams، ويُ partner certification لل consultancies.</p>
      <p>القدرات الأساسية: Arabic trace dashboards; Dialect eval packs; Regression alerts; Guardrail suggestions; Compliance exports; Partner certification.</p>
      <p>للمبدعين العرب: AI ops studios — «LangSmith Agents 3 Arabic reliability stack in 9 days» لل orgs 3–40 production agents. من يُ ship 10 stacks/ربع بـ 1800–38000 دولار + managed 140–1180 دولار/شهر يبني «مركز LangSmith عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LangChain LangSmith Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة reliability stack (tracing، evals، alerts، runbooks):</strong> 5–15 يومًا — 1800–38000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ eval refresh وincident reviews:</strong> — 140–1180 دولار/شهر.</li>
          <li><strong>Industry eval packs (banking، retail، travel):</strong> — 38–172 دولار/pack.</li>
          <li><strong>دورات «وكلاء production بـ LangSmith بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LangChain</span>
        <span class="tag">LangSmith</span>
        <span class="tag">Agents</span>
        <span class="tag">Observability</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 04-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="04-11-2026 -- 12-AM.html">
          📰 4 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "04-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/04-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/04-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
