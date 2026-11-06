#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 06-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "06-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Maze AI Research 3 Arabic · CircleCI AI Pipelines 3 Arabic · "
    "Hex Magic AI 3 Arabic · Looker Gemini 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Maze AI Research 3 Arabic، CircleCI AI Pipelines 3 Arabic، Hex Magic AI 3 Arabic، Looker Gemini 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 6 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Maze AI Research 3 Arabic الذي يُحوّل جلسات usability فوضوية إلى insights وتوصيات product بلهجة عربية قبل أن يُطفأ ضوء المكتب، إلى CircleCI AI Pipelines 3 Arabic الذي يُ repair builds ويُ suggest tests من log واحد، ومن Hex Magic AI 3 Arabic الذي يُ answer «لماذا هبط conversion؟» بcharts وSQL narrative للفريق، إلى Looker Gemini 3 Arabic الذي يُ birth dashboards وexplores من سؤال CFO بالفصحى — أربع قصص ليلية في 6 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة لفرق product وdata وplatform: research يتأخر، CI يحترق، notebooks بلا story، وBI dashboards تتقادم. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 6 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Maze AI Research 3 Arabic: usability يُ think — clips، heatmaps، وتوصيات product RTL!</h2>
      <p class="article-lead">«شاهدنا 40 recording — ولا أحد يعرف أين يتعثر المستخدم في checkout». في 6 نوفمبر 2026، أطلقت <strong>Maze</strong> <strong>AI Research 3 Arabic</strong>: طبقة research فوق unmoderated tests وprototype links تُ transcribe think-aloud بالعربية والإنجليزية، تُ cluster pain points وsuccess paths، تُ generate highlight reels مع captions RTL، تُ draft usability reports وJira-ready recommendations، تُ compare variants A/B ويُ quantify impact، تُ integrate Figma وFigJam وLinear وNotion — لل product وUX agencies وSaaS في MENA.</p>
      <p>المشكلة التي حلّتها: Research 2 كان يُ miss dialect nuance في open feedback؛ الإصدار 3 يُ MENA tone packs (خليجي، مصري، مغاربي)، يُ benchmark −46% وقت «study to decision» في fintech product الرياض، يُ bias checks على survey wording، يُ privacy blur PII في recordings، ويُ partner certifications في Dubai وCasablanca.</p>
      <p>القدرات الأساسية: Arabic transcription; Pain-point clustering; Highlight reels RTL; Report-to-Jira; Variant comparison; Figma and Linear sync.</p>
      <p>للمبدعين العرب: UX research boutiques — «Maze AI Research 3 Arabic sprint in 5 days» لل teams 3–25 studies/ربع. من يُ deliver 10 sprints/ربع بـ 1100–24000 دولار + insights retainer 95–780 دولار/شهر يبني «استوديو Maze AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Maze AI Research 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة research AI (study design، recruitment brief، analysis، workshop):</strong> 4–11 يومًا — 1100–24000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ continuous discovery وhighlight library:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Vertical playbooks (e-commerce، banking، health):</strong> — 38–175 دولار/playbook.</li>
          <li><strong>دورات «بحث مستخدم ذكي بـ Maze AI بالعربية»:</strong> — 34–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Maze</span>
        <span class="tag">UX Research</span>
        <span class="tag">Product</span>
        <span class="tag">Figma</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>CircleCI AI Pipelines 3 Arabic: CI/CD copilot — fix builds، tests، وdeploy notes!</h2>
      <p class="article-lead">«Pipeline أحمر — والمهندس يترجم logs يدويًا قبل standup». في 6 نوفمبر 2026، أطلقت <strong>CircleCI</strong> <strong>AI Pipelines 3 Arabic</strong>: copilot داخل pipelines يُ summarize failures بالعربية مع root-cause hints، يُ suggest config fixes وDockerfile patches، يُ generate missing tests من diff، يُ draft release notes RTL لل stakeholders، يُ optimize parallelism وcache keys، يُ policy guard secrets وcompliance gates، يُ integrate GitHub وGitLab وArgo — لل platform teams وfintech وgaming في MENA.</p>
      <p>المشكلة التي حلّتها: Pipelines 2 كان يُ hallucinate على flaky tests؛ الإصدار 3 يُ flake detection وretry policies، يُ benchmark −42% MTTR pipeline في SaaS القاهرة، يُ runbook links من internal wiki، يُ audit trail SOC2، ويُ reseller enablement لل regional DevOps shops.</p>
      <p>القدرات الأساسية: Failure summaries RTL; Config suggestions; Test generation; Release notes; Cache optimization; Compliance gates.</p>
      <p>للمبدعين العرب: DevOps consultancies — «CircleCI AI Pipelines 3 Arabic rescue in 6 days» لل orgs 5–80 repos. من يُ onboard 9 clients/ربع بـ 1800–42000 دولار + SRE retainer 130–1050 دولار/شهر يبني «مكتب CircleCI AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من CircleCI AI Pipelines 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة pipeline AI (audit، templates، flaky fixes، training):</strong> 4–12 يومًا — 1800–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ MTTR reviews وconfig hygiene:</strong> — 130–1050 دولار/شهر.</li>
          <li><strong>Starter orbs (mobile، microservices، data):</strong> — 45–210 دولار/orb pack.</li>
          <li><strong>دورات «CI/CD ذكي بـ CircleCI AI بالعربية»:</strong> — 40–190 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">CircleCI</span>
        <span class="tag">DevOps</span>
        <span class="tag">CI/CD</span>
        <span class="tag">Platform</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Hex Magic AI 3 Arabic: notebooks تُ narrate — SQL، charts، وexecutive story!</h2>
      <p class="article-lead">«التحليل جاهز — لكن المدير يريد «لماذا» لا جداول». في 6 نوفمبر 2026، أطلقت <strong>Hex</strong> <strong>Magic AI 3 Arabic</strong>: copilot داخل collaborative notebooks يُ answer business questions بالفصحى، يُ write SQL/Python مع lineage، يُ build interactive charts وforecast scenarios، يُ produce executive summaries RTL مع caveats، يُ connect Snowflake وBigQuery وdbt وLooker، يُ role-based sharing وaudit — لل analytics وgrowth وfinance في MENA.</p>
      <p>المشكلة التي حلّتها: Magic 2 كان يُ break on Arabic column names؛ الإصدار 3 يُ unicode-safe identifiers، يُ benchmark −39% وقت «question to board slide» في retail analytics دبي، يُ semantic layer hints، يُ scheduled narratives to Slack وEmail، ويُ partner tier لل consultancies.</p>
      <p>القدرات الأساسية: Arabic Q&amp;A; SQL and Python assist; Executive narratives RTL; Warehouse connectors; Scheduled insights; Team permissions.</p>
      <p>للمبدعين العرب: data studios — «Hex Magic AI 3 Arabic analytics hub in 7 days» لل teams 5–60 analysts. من يُ launch 8 hubs/ربع بـ 2200–48000 دولار + managed 160–1250 دولار/شهر يبني «استوديو Hex AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hex Magic AI 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة analytics hub (semantic layer، notebooks، training):</strong> 5–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ narrative refresh وdata quality:</strong> — 160–1250 دولار/شهر.</li>
          <li><strong>Department packs (marketing، finance، ops):</strong> — 42–198 دولار/pack.</li>
          <li><strong>دورات «تحليل تعاوني بـ Hex Magic بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hex</span>
        <span class="tag">Analytics</span>
        <span class="tag">Notebooks</span>
        <span class="tag">Data</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Looker Gemini 3 Arabic: BI يتكلّم — explores، dashboards، وforecasts من سؤال!</h2>
      <p class="article-lead">«أين revenue by city آخر 90 يومًا؟ — والمحلل في إجازة». في 6 نوفمبر 2026، أطلقت <strong>Google Cloud</strong> <strong>Looker Gemini 3 Arabic</strong>: طبقة generative BI فوق Looker وBigQuery تُ parse أسئلة business بالعربية، تُ generate explores وLookML-safe queries، تُ build dashboards RTL مع drill-downs، تُ explain metric definitions grounded في semantic model، تُ forecast scenarios وanomaly alerts، تُ embed في apps وSlack وSheets، تُ row-level security وVPC-SC — لل enterprises وretail chains في GCC ومصر.</p>
      <p>المشكلة التي حلّتها: Gemini 2 كان يُ over-fetch costly queries؛ الإصدار 3 يُ cost guardrails وquery explain، يُ benchmark −44% self-serve BI tickets في holding الرياض، يُ Arabic number وdate formatting، يُ migration assistants من legacy reports، ويُ Google Cloud partner credits في MENA.</p>
      <p>القدرات الأساسية: Natural-language explores; RTL dashboards; Grounded definitions; Forecasts and alerts; Embedded analytics; Enterprise security.</p>
      <p>للمبدعين العرب: Looker partners — «Looker Gemini 3 Arabic self-serve BI in 10 days» لل orgs 50–5000 users. من يُ deliver 6 programs/ربع بـ 3800–72000 دولار + optimization 240–1950 دولار/شهر يبني «مكتب Looker Gemini عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Looker Gemini 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة BI AI (semantic model، explores، training، governance):</strong> 7–18 يومًا — 3800–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ model hygiene وcost reviews:</strong> — 240–1950 دولار/شهر.</li>
          <li><strong>Industry templates (retail، telco، healthcare):</strong> — 55–260 دولار/template.</li>
          <li><strong>دورات «BI ذكي بـ Looker Gemini بالعربية»:</strong> — 46–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Looker</span>
        <span class="tag">Google Cloud</span>
        <span class="tag">BI</span>
        <span class="tag">BigQuery</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 06-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="06-11-2026 -- 12-AM.html">
          📰 6 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "06-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/06-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/06-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
