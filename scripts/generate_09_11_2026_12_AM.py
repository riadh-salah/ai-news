#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 09-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "09-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Okta Identity Security AI 2 Arabic · Intuit QuickBooks Assist 3 Arabic · "
    "Confluent AI Assistance 3 Arabic · monday.com AI Docs 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Okta Identity Security AI 2 Arabic، Intuit QuickBooks Assist 3 Arabic، Confluent AI Assistance 3 Arabic، monday.com AI Docs 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 9 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Okta Identity Security AI 2 Arabic الذي يُحوّل تنبيهات MFA وprivilege anomalies إلى قرار أمني عربي واضح قبل أن يَطير الـ on-call من السرير، إلى Intuit QuickBooks Assist 3 Arabic الذي يُفسر cashflow ويُقترح فواتير وتحصيلًا من سؤال CFO واحد، ومن Confluent AI Assistance 3 Arabic الذي يُشرح lag في Kafka ويُ draft schema policies وأنت تتابع dashboard على الهاتف، إلى monday.com AI Docs 3 Arabic الذي يُحوّل updates الفوضوية إلى مستندات SOP وملخصات للفريق بفصحى تُفهم من أول سطر — أربع قصص ليلية في 9 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للفرق التي لا تنام: أمناء الهوية يطاردون محاولات دخول غامضة، أصحاب الأعمال يستيقظون على سؤال «أين ذهب الرصيد؟»، مهندسو البيانات يبحثون عن سبب تأخر streams، ومديرو العمليات يريدون توثيقًا يُقرأ لا يُنسى. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 9 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Okta Identity Security AI 2 Arabic: هوية وحوكمة — threats، MFA، وprivilege بلسان فريق الأمن!</h2>
      <p class="article-lead">«مستخدم VIP دخل من IP جديد — هل نُعطّل حسابه أم نُرسل challenge فقط؟». في 9 نوفمبر 2026، أطلقت <strong>Okta</strong> <strong>Identity Security AI 2 Arabic</strong>: طبقة AI فوق Okta Identity Cloud وIGA يُ ingest sign-in logs وdevice signals وHR changes، يُ summarize incidents بالفصحى مع MITRE-style mapping مبسّط، يُ recommend step-up auth أو session revoke مع تبرير RTL للـ CISO، يُ detect privilege drift وorphan accounts، يُ draft policy updates وaccess review tasks، يُ integrate CrowdStrike وMicrosoft Defender وServiceNow، يُ respect data residency وaudit exports — لل banks وtelco وgov وholding groups في MENA.</p>
      <p>المشكلة التي حلّتها: الإصدار 1 كان يُ overwhelm محللي IAM بملخصات إنجليزية طويلة؛ الإصدار 2 يُ Arabic executive briefs، يُ benchmark −44% وقت «alert → decision» في financial institution إماراتي 8000 seats، يُ playbooks لل phishing وMFA fatigue، يُ partner certification في دبي والرياض، ويُ purple-team scenarios لل boards.</p>
      <p>القدرات الأساسية: NL policy search؛ automated access certification summaries؛ risk scoring مع explainability؛ Slack وTeams alerts بالعربية؛ sandbox لل identity architects.</p>
      <p>للمبدعين العرب: IAM consultancies وMSSPs — «Identity Security AI 2 Arabic command center in 9 days» لل orgs 500–50000 users. من يُ deploy 5 centers/ربع بـ 3800–72000 دولار + retainer 340–2800 دولار/شهر يبني «مركز Okta AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Okta Identity Security AI 2 Arabic؟</h3>
        <ul>
          <li><strong>Identity AI rollout (connectors، Arabic playbooks، policy tuning، UAT):</strong> 7–20 يومًا — 3800–72000 دولار/عميل.</li>
          <li><strong>Monthly access reviews وincident coaching:</strong> — 340–2800 دولار/شهر.</li>
          <li><strong>Vertical kits (banking، healthcare، education SSO):</strong> — 55–248 دولار/حزمة.</li>
          <li><strong>دورات «أمن الهوية الذكي بـ Okta بالعربية»:</strong> — 52–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Okta</span>
        <span class="tag">IAM</span>
        <span class="tag">Security</span>
        <span class="tag">Zero Trust</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Intuit QuickBooks Assist 3 Arabic: محاسبة SMB — فواتير، تدفق نقدي، وCFO insights بلسان صاحب العمل!</h2>
      <p class="article-lead">«العميل لم يدفع منذ 45 يومًا — وماذا عن ضريبة الفاتورة الأخيرة؟». في 9 نوفمبر 2026، أطلقت <strong>Intuit</strong> <strong>QuickBooks Assist 3 Arabic</strong>: copilot داخل QuickBooks Online وEnterprise يُ answer أسئلة finance بالفصحى واللهجات المختارة، يُ explain P&amp;L وcash runway «لماذا انخفض الرصيد رغم مبيعات قوية؟»، يُ draft invoices وpayment reminders RTL، يُ categorize expenses وflag duplicates، يُ suggest collection workflows وlate-fee policies متوافقة مع MENA practices، يُ connect bank feeds وPayPal وStripe، يُ generate reports للمستثمرين والبنوك، يُ mobile voice queries — لل SMEs وfranchises وfamily businesses في الخليج ومصر والأردن.</p>
      <p>المشكلة التي حلّتها: Assist 2 كان يُ confuse Arabic vendor names في receipts؛ الإصدار 3 يُ OCR عربي محسّن، يُ benchmark −49% وقت «سؤال → actionable invoice» في retail سعودي 120 فروع، يُ accountant collaboration mode، يُ partner program في القاهرة ودبي، ويُ templates لـ e-invoicing ZATCA-ready.</p>
      <p>القدرات الأساسية: Natural language dashboards؛ automated reconciliation hints؛ bilingual client emails؛ tax category suggestions؛ audit-friendly chat logs.</p>
      <p>للمبدعين العرب: accounting boutiques — «QuickBooks Assist 3 Arabic books brain in 5 days» لل orgs 50–5000 transactions/شهر. من يُ roll 10 brains/ربع بـ 1600–42000 دولار + support 140–1180 دولار/شهر يبني «مكتب QuickBooks AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intuit QuickBooks Assist 3 Arabic؟</h3>
        <ul>
          <li><strong>Assist enablement (chart، Arabic vendors، workflows، training):</strong> 3–12 يومًا — 1600–42000 دولار/عميل.</li>
          <li><strong>Monthly close coaching وAR follow-up automation:</strong> — 140–1180 دولار/شهر.</li>
          <li><strong>Industry kits (restaurants، clinics، e-commerce):</strong> — 42–195 دولار/حزمة.</li>
          <li><strong>دورات «محاسبة SMB ذكية بـ QuickBooks بالعربية»:</strong> — 45–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intuit</span>
        <span class="tag">QuickBooks</span>
        <span class="tag">SMB</span>
        <span class="tag">Finance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Confluent AI Assistance 3 Arabic: بيانات متدفقة — Kafka health، schemas، وincidents بلسان platform team!</h2>
      <p class="article-lead">«consumer lag قفز 400% — والـ on-call يبحث في Grafana عن السبب». في 9 نوفمبر 2026، أطلقت <strong>Confluent</strong> <strong>AI Assistance 3 Arabic</strong>: مساعد فوق Confluent Cloud وon-prem يُ answer أسئلة SRE وdata platform بالفصحى، يُ explain topic lag وrebalance plans، يُ detect schema drift وbreaking changes، يُ draft Flink SQL وksqlDB snippets مع guardrails، يُ correlate alerts من Prometheus وDatadog، يُ summarize incident timelines RTL لل management، يُ suggest cost optimizations وtiering، يُ integrate Terraform وGitHub Actions، يُ air-gapped connectors لل regulated sectors — لل fintech وlogistics وgaming وgov digital في MENA.</p>
      <p>المشكلة التي حلّتها: Assistance 2 كان إنجليزيًا فقط؛ الإصدار 3 يُ Arabic runbooks وpostmortems، يُ benchmark −40% MTTR في payments platform خليجي، يُ policy templates لـ PII streams، يُ partner enablement في Dubai Tech Week، ويُ certification لـ system integrators.</p>
      <p>القدرات الأساسية: NL cluster diagnostics؛ automated schema documentation؛ chat في Confluent UI؛ API لل PagerDuty؛ RBAC-aware answers.</p>
      <p>للمبدعين العرب: data platform consultancies — «AI Assistance 3 Arabic streaming cockpit in 8 days» لل clusters 20–500 topics. من يُ deliver 6 cockpits/ربع بـ 3200–58000 دولار + retainer 260–2150 دولار/شهر يبني «مكتب Confluent AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Confluent AI Assistance 3 Arabic؟</h3>
        <ul>
          <li><strong>Streaming AI enablement (connectors، Arabic KB، playbooks، load tests):</strong> 6–18 يومًا — 3200–58000 دولار/عميل.</li>
          <li><strong>Monthly lag reviews وschema governance:</strong> — 260–2150 دولار/شهر.</li>
          <li><strong>Vertical packs (payments events، IoT telemetry، clickstream):</strong> — 48–220 دولار/حزمة.</li>
          <li><strong>دورات «منصات بيانات ذكية بـ Confluent بالعربية»:</strong> — 50–228 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Confluent</span>
        <span class="tag">Kafka</span>
        <span class="tag">Streaming</span>
        <span class="tag">Data Platform</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>monday.com AI Docs 3 Arabic: عمليات ومعرفة — SOPs، updates، وhandbooks من board واحد!</h2>
      <p class="article-lead">«الفريق يسأل نفس السؤال كل أسبوع — والإجابة مدفونة في 14 thread». في 9 نوفمبر 2026، أطلقت <strong>monday.com</strong> <strong>AI Docs 3 Arabic</strong>: layer داخل work management يُ read boards وitems وfiles وupdates، يُ generate SOPs وtraining docs وrelease notes بالفصحى، يُ summarize sprint status للمدير، يُ detect conflicting tasks وmissing owners، يُ translate briefs EN↔AR مع terminology lock، يُ publish إلى workdocs وGoogle Docs وNotion exports، يُ permission-aware citations، يُ automate weekly digests لـ Slack وTeams — لل ops وHR وagencies وscale-ups في MENA.</p>
      <p>المشكلة التي حلّتها: AI Docs 2 كان يُ hallucinate روابط؛ الإصدار 3 يُ grounded على item IDs وattachments فقط، يُ benchmark −43% وقت «chaos → published handbook» في marketing agency سعودية، يُ template gallery RTL، يُ enterprise SCIM وaudit، ويُ partner marketplace في المنطقة.</p>
      <p>القدرات الأساسية: One-click SOP from board؛ bilingual exec summaries؛ doc versioning؛ mobile approve-and-publish؛ integrations مع Jira وAsana imports.</p>
      <p>للمبدعين العرب: ops consultants — «AI Docs 3 Arabic knowledge factory in 4 days» لل teams 15–800 seats. من يُ run 11 factories/ربع بـ 1400–36000 دولار + subscription coaching 95–780 دولار/شهر يبني «استوديو monday AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من monday.com AI Docs 3 Arabic؟</h3>
        <ul>
          <li><strong>Docs factory setup (boards، templates، Arabic tone، adoption):</strong> 3–10 أيام — 1400–36000 دولار/عميل.</li>
          <li><strong>Monthly doc refresh وSOP audits:</strong> — 95–780 دولار/شهر.</li>
          <li><strong>Vertical playbooks (agencies، construction، retail ops):</strong> — 38–175 دولار/حزمة.</li>
          <li><strong>دورات «توثيق عمليات ذكي بـ monday بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">monday.com</span>
        <span class="tag">Work OS</span>
        <span class="tag">Documentation</span>
        <span class="tag">Ops</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 09-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="09-11-2026 -- 12-AM.html">
          📰 9 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "09-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/09-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/09-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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

