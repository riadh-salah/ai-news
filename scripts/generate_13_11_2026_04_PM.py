#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 13-11-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "13-11-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Databricks Genie 2 Arabic · IBM Microsoft Imagine Enterprise Arabic · "
    "Sysdig AI Defense Arabic · Expedient AI CTRL Platform 2 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Databricks Genie 2 Arabic، IBM Microsoft Imagine Enterprise Arabic، Sysdig AI Defense Arabic، Expedient AI CTRL Platform 2 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 13 نوفمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Databricks Genie 2 Arabic الذي يُدير مهامك المؤسسية بينما أنت بعيد عن المكتب ويُرسل لك ملخصًا عربيًا عند الخطر، إلى IBM Microsoft Imagine Enterprise Arabic الذي يُسلّم وكلاء قطاعية جاهزة مع حوكمة للبنوك والطاقة، ومن Sysdig AI Defense Arabic الذي يُوقف وكيلًا مخترقًا قبل أن يُغيّر البنية التحتية، إلى Expedient AI CTRL Platform 2 Arabic الذي يُوحّد نماذج الشركة وبياناتها ووكلائها في لوحة عربية واحدة — أربع قصص مسائية في 13 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء آخر ضوء في اليوم!</h1>
      <p class="hero-sub">مساءٌ لفرق البيانات والامتثال والعمليات: الوكلاء أصبحوا يعملون دون إشراف، والقطاعات المنظّمة تخاف من الفوضى، والأمن يريد رؤية كل action، والإدارة العليا تريد ميزانية واحدة لكل نموذج. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 13 نوفمبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Databricks Genie 2 Arabic: وكيل مؤسسي دائم التشغيل — inbox، بريد، وontology عربي!</h2>
      <p class="article-lead">«ضع هدف الربع على Genie واتركه يُتابع التوقعات ويُذكّرني عندما تنحرف الأرقام — بالعربية في البريد». في 13 نوفمبر 2026، أطلقت <strong>Databricks</strong> الجيل الثاني من <strong>Genie 2 Arabic</strong>: وكيل مؤسسي يعمل في الخلفية بشكل مستقل، يُفهم كيف تعمل شركتك عبر Genie Ontology (البيانات والأفراد والعمليات)، يُبحث في أكثر من 100 مصدر بما فيها lakehouse وGoogle Drive وJira وConfluence، يُفوّض لsubagents عند الحاجة، يُرسل inbox أولويات وتنبيهات بريد عندما تكون بعيدًا، ويُجيب بالفصحى واللهجات الخليجية في التقارير — لفرق المالية والتسويق ونجاح العملاء في MENA.</p>
      <p>المشكلة التي حلّتها: Genie الأول كان تفاعليًا فقط؛ Genie 2 يُشغّل autonomous mode على compute مخصص، يُدير مهام طويلة الأمد (مثل متابعة GEO أو أنماط استخدام العملاء أو ملخص إيرادات أسبوعي)، يُتابع المدخلات الناقصة، يُطلب قرار الإنسان عند الحدود، يُسجّل كل خطوة للحوكمة، ويُدعم واجهة عربية كاملة للأسئلة والملخصات.</p>
      <p>القدرات الأساسية: Priority Inbox؛ بريد تلقائي بالعربية؛ Genie Search موسّع؛ تكامل Unity Catalog؛ سياسات امتثال للبيانات الحساسة؛ برنامج شريك «MENA Genie Ops».</p>
      <p>للمبدعين العرب: شركاء Databricks واستوديوهات تحليل البيانات — «وكيل Genie عربي live في 10 أيام» للفرق التي تملك lakehouse. من يُشغّل 5 عمليات Genie 2/ربع بـ 4200–52000 دولار/تنفيذ + مراقبة 880–6200 دولار/شهر يحوّل البيانات إلى موظف رقمي لا ينام.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Databricks Genie 2 Arabic؟</h3>
        <ul>
          <li><strong>تصميم ontology وأهداف وكيل (مصادر، حدود، تقارير عربية):</strong> 7–22 يومًا — 4200–52000 دولار/عميل.</li>
          <li><strong>مراقبة أسبوعية وضبط subagents وتنبيهات:</strong> — 880–6200 دولار/شهر.</li>
          <li><strong>حزم قطاعية (طاقة، اتصالات، تجزئة):</strong> — 78–295 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء دائمي التشغيل مع Genie»:</strong> — 62–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Databricks</span>
        <span class="tag">Genie</span>
        <span class="tag">Agents</span>
        <span class="tag">Data</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>IBM Microsoft Imagine Enterprise Arabic: منصة وكلاء قطاعية — حوكمة، Azure، و6 آلاف أصل جاهز!</h2>
      <p class="article-lead">«نريد وكيلًا يفهم عملية الموافقة الائتمانية البنكية — لا نريد بناء كل شيء من صفر». في 10 نوفمبر 2026، أعلنت <strong>IBM</strong> و<strong>Microsoft</strong> عن <strong>Imagine Enterprise Arabic</strong>: منصة agentic لبناء وتشغيل ومراقبة وكلاء يُنفّذون عمليات قطاعية محددة، تجمع خبرة IBM Consulting مع أكثر من 6000 وكيل وأصل جاهز، وتقنيات Microsoft للذكاء والسحابة والأمن، مع دعم هندسي مُدمج للمشاريع المؤهلة — والواجهة والتوثيق والتدريب متاحة بالعربية للقطاعات المنظّمة في الخليج وأوروبا.</p>
      <p>المشكلة التي حلّتها: المشاريع المشتركة كانت بطيئة؛ Imagine يُوحّد build وrun وgovern في طبقة واحدة، يُربط الوكلاء ببيانات المؤسسة وعملياتها اليومية، يُقدّم controls وobservability ودعم compliance للذكاء، يُسرّع النشر في الطاقة والمالية والصحة، ويُشحن قوالب عربية لـ KYC وإدارة الحوادث وسلسلة التوريد.</p>
      <p>القدرات الأساسية: كتالوج وكلاء قطاعية؛ تكامل Azure OpenAI وCopilot؛ لوحة حوكمة؛ forward-deployed engineers؛ مسارات للصناعات المنظّمة.</p>
      <p>للمبدعين العرب: IBM Business Partners وMicrosoft integrators — «حزمة وكيل قطاعي معتمد في 21 يومًا». من يُغلق 4 عقود Imagine/ربع بـ 5500–78000 دولار/مشروع + retainer 1200–9500 دولار/شهر يبيع تحولًا منظّمًا لا تجارب عشوائية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من IBM Microsoft Imagine Enterprise Arabic؟</h3>
        <ul>
          <li><strong>تنفيذ منصة ووكلاء (اكتشاف، تخصيص، حوكمة، go-live):</strong> 14–45 يومًا — 5500–78000 دولار/مشروع.</li>
          <li><strong>امتثال ومراجعة سياسات وكلاء شهريًا:</strong> — 1200–9500 دولار/شهر.</li>
          <li><strong>حزم قوالب (بنوك، نفط، تأمين):</strong> — 95–340 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء منظّمة مع Imagine Enterprise»:</strong> — 68–275 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">IBM</span>
        <span class="tag">Microsoft</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Governance</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Sysdig AI Defense Arabic: أمان وقت التشغيل لكل action — Cursor، Copilot، MCP!</h2>
      <p class="article-lead">«وكيل المطور غيّر إعدادات Kubernetes بينما كنا في اجتماع — ولا أحد رأى ذلك يدويًا». في 13 نوفمبر 2026، أطلقت <strong>Sysdig</strong> <strong>AI Defense Arabic</strong> بحزمة واجهة عربية للفرق الأمنية في MENA: أمان وقت التشغيل لكل إجراء يتخذه الوكيل — من جهاز المطور إلى السحابة — يُحكم السياسة في اللحظة (سماح، تأكيد بشري، أو حظر)، يُرصد Cursor وClaude Code وGitHub Copilot وCodex، يُسجّل MCP servers وskills وplugins، يُوقف credentials الخطرة، ويُقدّم سجلًا لا يُمسّ للتدقيق — للشركات التي تُشغّل وكلاء إنتاج في الرياض ودبي وأوروبا.</p>
      <p>المشكلة التي حلّتها: الأمن كان يركز على النماذج؛ AI Defense يُرى كل جلسة action بaction، يُبني inventory حيًا للوكلاء والمسؤولين عنها، يُطبّق قوالب OWASP LLM، يبدأ بوضع alert ثم enforcement، يُظهر action graph حيًا، ويُوزّع تكلفة النماذج على الفريق والوكيل والشخص.</p>
      <p>القدرات الأساسية: Live Agent Inventory؛ Policy Templates؛ Block/Hold للإجراءات؛ Immutable Audit؛ AI Spend Attribution؛ لوحة تنبيهات عربية.</p>
      <p>للمبدعين العرب: MSSPs وفرق DevSecOps — «حزمة حوكمة وكلاء في 14 يومًا» للشركات التي تُسرّع AI coding. من يُبيع 9 تراخيص AI Defense مُعدّلة/ربع بـ 3100–28000 دولار + SIEM integration 700–3400 دولار/شهر يحوّل الخوف من الوكلاء إلى ثقة قابلة للإثبات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sysdig AI Defense Arabic؟</h3>
        <ul>
          <li><strong>نشر AI Defense (سياسات، تكامل SIEM، تدريب SOC):</strong> 8–18 يومًا — 3100–28000 دولار/منظمة.</li>
          <li><strong>مراجعة incidents وكلاء وتحديث سياسات:</strong> — 700–3400 دولار/شهر.</li>
          <li><strong>حزم قوالب (فينتك، SaaS، طاقة):</strong> — 55–220 دولار/حزمة.</li>
          <li><strong>دورات «أمان الوكلاء وقت التشغيل»:</strong> — 48–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sysdig</span>
        <span class="tag">Security</span>
        <span class="tag">Agents</span>
        <span class="tag">DevSecOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Expedient AI CTRL Platform 2 Arabic: حوكمة موحّدة — Secure Chat، RAG، وAgentic Workflow!</h2>
      <p class="article-lead">«كل قسم يستخدم نموذجًا مختلفًا — والمالية لا تعرف من أنفق ماذا، والامتثال يريد سجلًا واحدًا». في 12 نوفمبر 2026، وسّعت <strong>Expedient</strong> الجيل التالي من <strong>AI CTRL Platform 2 Arabic</strong>: طبقة حوكمة وإدارة موحّدة لتطبيقات ونماذج ووكلاء الذكاء الاصطناعي في المؤسسة، بواجهة ويب وسطح مكتب عربية، ثلاث طبقات خدمة (Secure Chat، Secure Chat + Knowledge، Agentic Workflow Engine)، SSO وRBAC وتدفق credits مشترك وسقف إنفاق — كل عميل في instance مخصص single-tenant على Expedient Cloud.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان محدود القنوات؛ Platform 2 يُضيف Smart Model Router، redaction للبيانات الشخصية قبل النموذج، connectors وMCP للمعرفة الداخلية، بناء workflows متعددة الخطوات، فصل صلاحيات builders عن المستخدمين، وتصدير audit لأدوات الأمن الحالية — مع دعم فريق عربي للإعداد والتدريب.</p>
      <p>القدرات الأساسية: ثلاث تسعيرات tiers؛ workspace عربي؛ audit request-level؛ شركاء تنفيذ للوكلاء؛ webinar تدريبي «Next Gen AI CTRL».</p>
      <p>للمبدعين العرب: MSPs واستشاريو AI governance — «بوابة AI مؤسسية عربية في أسبوعين» للشركات 200–5000 موظف. من يُنفّذ 7 منصات CTRL/ربع بـ 2800–24000 دولار/نشر + إدارة 520–2100 دولار/شهر يبيع راحة الإدارة العليا لا chatbot فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Expedient AI CTRL Platform 2 Arabic؟</h3>
        <ul>
          <li><strong>نشر منصة (tier، SSO، connectors، سياسات، تدريب):</strong> 9–24 يومًا — 2800–24000 دولار/عميل.</li>
          <li><strong>إدارة نماذج ومراجعة إنفاق وكلاء شهريًا:</strong> — 520–2100 دولار/شهر.</li>
          <li><strong>حزم Knowledge + RAG (مالية، قانون، عمليات):</strong> — 58–235 دولار/حزمة.</li>
          <li><strong>دورات «حوكمة AI مؤسسية بالعربية»:</strong> — 42–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Expedient</span>
        <span class="tag">Governance</span>
        <span class="tag">Enterprise</span>
        <span class="tag">RAG</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 13-11-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="13-11-2026 -- 04-PM.html">
          📰 13 نوفمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "13-11-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/13-11-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/13-11-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
    if "\u00fc" in text or "yü" in text:
        raise SystemExit("ERROR: Latin ü found — use Arabic يُ")
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
