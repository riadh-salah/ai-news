#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — CrowdStrike Charlotte AI 3 Arabic، UiPath Autopilot 3 Arabic، Oracle Fusion AI Agents 3 Arabic، Cisco AI Defense 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من CrowdStrike Charlotte AI 3 Arabic الذي يُترجم تهديدات SOC إلى قرارات عربية قبل أن تُغلق التذكرة، إلى UiPath Autopilot 3 Arabic الذي يُحوّل طلبات الموظفين إلى workflows RPA تعمل بذاتها، ومن Oracle Fusion AI Agents 3 Arabic الذي يُجيب CFO ومدير المشتريات من داخل ERP، إلى Cisco AI Defense 2 Arabic الذي يُوقف هجمات AI-generated phishing على الشبكة — أربع قصص صباحية في 25 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يُبنى على الثقة!</h1>
      <p class="hero-sub">صباحٌ للمُشغّلين: فرق الأمن تريد copilot يفهم MENA threats، مديرو العمليات يريدون automation بلا كود مع عربية، IT finance يبحث عن agents داخل Oracle، وnetwork teams يريدون دفاعًا ضد deepfake voice وLLM abuse. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 25 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>CrowdStrike Charlotte AI 3 Arabic: SOC copilot — من alert flood إلى hunt وresponse بلسان الفريق!</h2>
      <p class="article-lead">«12,000 alert في ساعة — ومحلل SOC يقرأ الثلاثمائة الأولى فقط». في 25 سبتمبر 2026، أطلقت <strong>CrowdStrike</strong> <strong>Charlotte AI 3 Arabic</strong>: مساعد AI فوق Falcon platform يقرأ detections وIOCs وthreat intel، يُلخّص بالعربية «هذا lateral movement من endpoint مالي — اقترح isolate وcontainment»، يُ draft hunt queries، يُ explain MITRE mapping، يُ generate incident report للإدارة، ويُ suggest playbooks Falcon Fusion — MSA enterprise للبنوك والحكومة.</p>
      <p>المشكلة التي حلّتها: Charlotte 2 كان English-first؛ الإصدار 3 يُ act (trigger workflow، assign analyst، open case، post Arabic timeline في Teams)، يُ ground على tenant data فقط، يُ integrate SIEM partners، يُ respect data residency، يُ localize threat actor names للفرق العربية، ويُ offer air-gapped briefing packs للقطاع الحساس.</p>
      <p>القدرات الأساسية: Charlotte Hunt Agent؛ Arabic NL في Falcon console؛ partner packs banking وenergy MENA؛ executive risk digest أسبوعي؛ LLM abuse detection for insider tools.</p>
      <p>للمبدعين العرب: MSSPs وcyber consultancies — «Arabic SOC copilot in 10 days» لل enterprises 500+ endpoints. من يُ deliver 4 Charlotte AI 3 rollouts/ربع بـ 4200–48000 دولار + managed tuning 820–6200 دولار/شهر يركب موجة security AI في المنطقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من CrowdStrike Charlotte AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Charlotte AI enablement (Arabic UX، playbooks، Fusion workflows، training):</strong> 9–22 يومًا — 4000–52000 دولار/عميل.</li>
          <li><strong>Managed threat narrative and hunt query updates:</strong> — 780–5900 دولار/شهر.</li>
          <li><strong>Vertical SOC kits (banking، telecom، gov):</strong> — 68–320 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Cyber AI with CrowdStrike Charlotte»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">CrowdStrike</span>
        <span class="tag">Cybersecurity</span>
        <span class="tag">SOC</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>UiPath Autopilot 3 Arabic: أتمتة وكيلية — من «أريد تقريرًا» إلى robot يُنجزه قبل الغداء!</h2>
      <p class="article-lead">«موظف HR يرسل: حدّث 400 سجل في SAP — والـ RPA team مشغول أسبوعين». في 25 سبتمبر 2026، أطلقت <strong>UiPath</strong> <strong>Autopilot 3 Arabic</strong>: copilot وagents فوق Automation Cloud يفهمون طلبات NL بالعربية، يُ discover processes من recordings، يُ generate workflows، يُ test في sandbox، يُ deploy مع governance، يُ monitor exceptions، ويُ explain «لماذا فشل الخطوة 7» — للـ shared services وBPOs في MENA.</p>
      <p>المشكلة التي حلّتها: Autopilot 2 كان assist على Studio؛ الإصدار 3 يُ act (create automation، schedule run، escalate human-in-loop، update queue)، يُ integrate SAP وOracle وMicrosoft 365، يُ enforce PII masking، يُ bilingual docs EN/AR، يُ offer Process Mining insights Arabic، ويُ scale agent catalog لل finance وprocurement.</p>
      <p>القدرات الأساسية: Autopilot for Everyone Arabic UI؛ Document Understanding 3 RTL؛ partner accelerators logistics وretail GCC؛ Test Suite AI-generated cases؛ ROI dashboard بالعربية للـ C-suite.</p>
      <p>للمبدعين العرب: RPA boutiques وsystem integrators — «Arabic agentic automation in 12 days» لل holdings وtelcos. من يُ sell 5 Autopilot 3 programs/سنة بـ 2800–38000 دولار/each + hypercare 450–3400 دولار/شهر يبني practice automation عالي الهامش.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من UiPath Autopilot 3 Arabic؟</h3>
        <ul>
          <li><strong>Autopilot 3 rollout (discovery، Arabic copilot، governance، go-live):</strong> 8–21 يومًا — 2600–42000 دولار/مشروع.</li>
          <li><strong>Monthly bot health and process optimization:</strong> — 420–3200 دولار/شهر.</li>
          <li><strong>Department starter packs (finance، HR، customer ops):</strong> — 55–275 دولار/حزمة.</li>
          <li><strong>دورات «Arabic RPA AI with UiPath Autopilot»:</strong> — 44–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">UiPath</span>
        <span class="tag">RPA</span>
        <span class="tag">Automation</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Oracle Fusion AI Agents 3 Arabic: ERP وكيلي — من سؤال CFO إلى journal وforecast داخل النظام!</h2>
      <p class="article-lead">«مجلس الإدارة يريد variance analysis — والمحاسب يصدّر 14 تقريرًا يدويًا». في 25 سبتمبر 2026، أطلقت <strong>Oracle</strong> <strong>Fusion AI Agents 3 Arabic</strong>: وكلاء داخل Cloud ERP وHCM وSCM يُ answer «ما تأثير تأخر shipment على margin الربع؟» بالعربية، يُ draft requisitions، يُ suggest payment runs، يُ simulate headcount، يُ route approvals، ويُ cite Fusion records — للـ multinationals في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: Agents 2 كان Q&amp;A؛ الإصدار 3 يُ act ضمن policy (create PR، post accrual draft for review، notify buyer)، يُ respect SOX segregation، يُ integrate OCI GenAI private، يُ localize VAT/ZATCA context، يُ generate Arabic board packs، ويُ offer industry agents retail وconstruction.</p>
      <p>القدرات الأساسية: Agent Studio Arabic prompts؛ Fusion Data Intelligence tie-in؛ mobile approve with AI summary؛ partner MENA tax packs؛ audit log every agent action.</p>
      <p>للمبدعين العرب: Oracle partners وERP consultancies — «Arabic Fusion agents in 14 days» لل groups 2000+ users. من يُ onboard 3 Fusion AI hubs/سنة بـ 5200–65000 دولار/each + agent care 680–5100 دولار/شهر يستهدف enterprise ERP niche مربح.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Oracle Fusion AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>Fusion AI Agents deployment (agents، Arabic NL، policies، UAT):</strong> 12–28 يومًا — 5000–72000 دولار/مشروع.</li>
          <li><strong>Monthly agent tuning and compliance reviews:</strong> — 650–4900 دولار/شهر.</li>
          <li><strong>Module packs (GL، procurement، payroll GCC):</strong> — 72–340 دولار/حزمة.</li>
          <li><strong>دورات «Arabic ERP AI with Oracle Fusion Agents»:</strong> — 58–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Oracle</span>
        <span class="tag">ERP</span>
        <span class="tag">Finance</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Cisco AI Defense 2 Arabic: شبكة تُقاتل AI — من deepfake voice إلى prompt injection على edge!</h2>
      <p class="article-lead">«مكالمة «CEO» تطلب wire transfer — والصوت مقنع جدًا». في 25 سبتمبر 2026، أطلقت <strong>Cisco</strong> <strong>AI Defense 2 Arabic</strong>: طبقة AI-native security عبر Meraki وCatalyst وUmbrella تُ detect synthetic media، LLM data exfil attempts، malicious copilot plugins، وAI-generated phishing pages، مع dashboards وalerts بالعربية وrecommended actions للـ NOC وSOC.</p>
      <p>المشكلة التي حلّتها: AI Defense 1 كان pilot؛ الإصدار 2 يُ act (block URL category، quarantine device، update ACL، notify Arabic playbook في Webex)، يُ integrate Splunk وCrowdStrike، يُ respect zero-trust policies، يُ offer GCC sovereign cloud telemetry option، يُ train on customer network baseline only، يُ generate executive «AI risk score» شهري.</p>
      <p>القدرات الأساسية: AI Threat Intel feed MENA؛ Arabic admin console؛ partner bundles education وhealthcare؛ Secure Access SSE AI policy wizard؛ voice deepfake detection for contact centers.</p>
      <p>للمبدعين العرب: network VARs وMSP — «Arabic AI network defense in 7 days» لل campuses وbanks. من يُ deploy 6 AI Defense 2 stacks/ربع بـ 1900–26000 دولار/each + monitoring 380–2900 دولار/شهر يُ scale security services على موجة AI abuse.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cisco AI Defense 2 Arabic؟</h3>
        <ul>
          <li><strong>AI Defense rollout (policies، Arabic alerts، integrations، runbooks):</strong> 5–16 يومًا — 1800–30000 دولار/مشروع.</li>
          <li><strong>Managed AI threat monitoring and policy updates:</strong> — 360–2800 دولار/شهر.</li>
          <li><strong>Vertical network kits (bank branches، universities، retail):</strong> — 48–225 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Network AI Security with Cisco»:</strong> — 36–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cisco</span>
        <span class="tag">Networking</span>
        <span class="tag">Security</span>
        <span class="tag">Zero Trust</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="25-09-2026 -- 08-AM.html">
          📰 25 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">CrowdStrike Charlotte AI 3 Arabic · UiPath Autopilot 3 Arabic · Oracle Fusion AI Agents 3 Arabic · Cisco AI Defense 2 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/25-09-2026 -- 08-AM.html`](news/25-09-2026%20--%2008-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-09-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    content = README.read_text(encoding="utf-8")
    import re

    new_content = re.sub(
        r"- \[`news/[^`]+`\]\([^)]+\) — أحدث إصدار \(4 أخبار \+ أفكار ربح من AI\)\n",
        README_LATEST,
        content,
        count=1,
    )
    if new_content == content and "25-09-2026 -- 08-AM.html" not in content:
        new_content = content.replace(
            "## المحتوى\n\n",
            "## المحتوى\n\n" + README_LATEST,
        )
    if new_content != content:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        print(f"Updated: {README}")
    else:
        print(f"README already up to date: {README}")


def validate_output():
    data = OUTPUT.read_bytes()
    if b"\x00" in data:
        raise SystemExit("ERROR: null bytes found in output")
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
        "bringing",
        "الLlatin",
        "أفكar",
        "دolار",
        "البروtokol",
        "سبtemبر",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "رobots",
        "despierta",
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
