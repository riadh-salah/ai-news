#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 12-11-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "12-11-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI ChatGPT Atlas 2 Arabic · Salesforce Agentforce 3 Arabic · "
    "Notion AI 3 Arabic · Zapier AI Actions 5 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI ChatGPT Atlas 2 Arabic، Salesforce Agentforce 3 Arabic، Notion AI 3 Arabic، Zapier AI Actions 5 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 12 نوفمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI العالمية</span>
      <h1>من OpenAI ChatGPT Atlas 2 Arabic الذي يُتصفّح الويب نيابةً عنك ويُجمّع تقريرًا عربيًا موثّقًا قبل أن تبرد قهوتك، إلى Salesforce Agentforce 3 Arabic الذي يُغلق صفقة ويُحدّث CRM من أمر صوتي بالخليجية، ومن Notion AI 3 Arabic الذي يُحوّل فوضى meeting notes إلى خطة مشروع وجداول متابعة بلهجة الفريق، إلى Zapier AI Actions 5 Arabic الذي يُشغّل مئات التطبيقات من جملة عربية واحدة — أربع قصص صباحية في 12 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُوقِظ الفرص مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ للباحثين والمبيعات وفرق المعرفة والمؤسسين: الويب واسع، الفرص تضيع في tabs، الملاحظات لا تتحول لعمل، والأتمتة عالقة عند التكاملات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 12 نوفمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI ChatGPT Atlas 2 Arabic: متصفّح ذكي يُعمل لأجلك — بحث، مقارنة، وتقارير RTL موثّقة!</h2>
      <p class="article-lead">«أحتاج مقارنة أسعار فنادق الرياض مع تقييمات آخر 90 يومًا — ولا وقت لعشرين tab». في 12 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>ChatGPT Atlas 2 Arabic</strong>: عميل تصفّح agentic يُفتح مواقع بإذن المستخدم، يُقرأ محتوى عربي وإنجليزي، يُستخرج جداول وأسعار، يُتحقق من المصادر المتعارضة، يُصدر تقرير PDF وdoc RTL مع footnotes، يُحفظ جلسات البحث، ويُrespect enterprise policy (no PII upload، audit trail) — للباحثين وconsultants وصنّاع المحتوى وفرق competitive intel في MENA.</p>
      <p>المشكلة التي حلّتها: Atlas 1 كان يتعثر على مواقع تسجّل دخولًا وJavaScript ثقيل؛ الإصدار 2 يُparallelize tabs مع حدود واضحة، يُcookie vault مشفّر للمؤسسات، يُintegrate Bing وperplexity-style verify، يُact (حجز demo، ملء نموذج، export لـ Sheets)، يُdialect tone في الملخص، يُbenchmark −61% وقت «تقرير سوق» في pilot وكالة دبي، ويُTeam Spaces لمشاركة مسارات بحث آمنة.</p>
      <p>القدرات الأساسية: Arabic Research Templates (سوق، تسعير، due diligence)؛ Computer-use guardrails؛ تكامل ChatGPT Enterprise؛ جدولة تقارير أسبوعية؛ شهادة «MENA Atlas Researcher» للشركاء.</p>
      <p>للمبدعين العرب: research boutiques وmedia labs — «Atlas research desk in 5 days» للفرق 8–40 باحثًا. من يُبيع 12 برنامج Atlas 2/ربع بـ 2400–36000 دولار + retainer 480–3200 دولار/شهر يحوّل تصفّح الويب إلى منتج معرفي عربي premium.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI ChatGPT Atlas 2 Arabic؟</h3>
        <ul>
          <li><strong>Atlas 2 rollout (سياسات، قوالب عربية، vault، تدريب):</strong> 4–14 يومًا — 2400–36000 دولار/عميل.</li>
          <li><strong>تقارير أسبوعية وضبط مسارات بحث شهريًا:</strong> — 480–3200 دولار/شهر.</li>
          <li><strong>حزم قطاعات (سياحة، عقار، fintech، retail):</strong> — 58–265 دولار/حزمة.</li>
          <li><strong>دورات «بحث سوق عربي بذكاء agentic»:</strong> — 46–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Atlas</span>
        <span class="tag">Research</span>
        <span class="tag">Browser</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Salesforce Agentforce 3 Arabic: وكلاء مبيعات وخدمة يُفكرون ويُنفّذون — من lead إلى deal بدون lag!</h2>
      <p class="article-lead">«العميل سأل بالعربية عن ترقية العقد — والـ SDR نائم في منطقة زمنية أخرى». في 12 نوفمبر 2026، أطلقت <strong>Salesforce</strong> <strong>Agentforce 3 Arabic</strong>: طبقة agents فوق Sales Cloud وService Cloud وData Cloud تُqualify leads بلهجات MENA، تُdraft عروض وemails RTL، تُschedule meetings، تُupdate opportunity stages، تُopen cases وتُresolve FAQs، تُescalate بذكاء للبشر مع ملخص عربي كامل — للـ B2B SaaS والبنوك والتجزئة الفاخرة في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Agentforce 2 كان strong على الإنجليزية؛ الإصدار 3 يُArabic reasoning على product catalog معقد، يُEinstein Trust Layer مع redaction، يُconnect WhatsApp Business وSlack وvoice، يُmulti-agent (SDR + AE + CSM handoff)، يُanalytics «ساعات وفّرناها» و«صفقات أنقذناها»، data residency في Frankfurt وUAE، وpacks للتأمين والعقار والتوزيع.</p>
      <p>القدرات الأساسية: Prompt Builder عربي؛ Agent Library (lead nurture، renewal، complaint)؛ تكامل Marketing Cloud؛ A/B على نبرة اللهجة؛ Partner accelerators في الرياض وجدة.</p>
      <p>للمبدعين العرب: Salesforce SI partners — «Agentforce 3 live in 10 days» للمنظمات 80+ مقعد مبيعات. من يُشغّل 8 تحولات Agentforce 3/ربع بـ 3200–52000 دولار + optimization 640–4100 دولار/شهر يبيع خط إنتاج إيرادات عربي على CRM عالمي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Salesforce Agentforce 3 Arabic؟</h3>
        <ul>
          <li><strong>Agentforce 3 implementation (data، agents، قنوات، UAT):</strong> 8–22 يومًا — 3200–52000 دولار/عميل.</li>
          <li><strong>تحسين conversion وCSAT شهريًا:</strong> — 640–4100 دولار/شهر.</li>
          <li><strong>حزم vertical (insurance، real estate، medtech):</strong> — 62–285 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء مبيعات عربية على Salesforce»:</strong> — 52–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Salesforce</span>
        <span class="tag">Agentforce</span>
        <span class="tag">CRM</span>
        <span class="tag">Revenue</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Notion AI 3 Arabic: من ملاحظة عربية فوضوية إلى wiki حيّ، مهام، وmeetings — ذاكرة الفريق بلغتها!</h2>
      <p class="article-lead">«كل القرارات في Notion — لكن أحدًا لا يجد آخر نسخة من خارطة الطريق». في 12 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>Notion AI 3 Arabic</strong>: طبقة ذكاء فوق databases وdocs تُsummarize pages طويلة بالفصحى والعامية المكتبية، تُgenerate قواعد وtemplates عربية، تُextract action items من transcripts، تُauto-link بين مشاريع، تُanswer «ماذا قررنا الأسبوع الماضي؟» مع block citations، تُrespect guest permissions — للـ startups وagencies وprogram offices في MENA التي تعمل بالعربية والإنجليزية معًا.</p>
      <p>المشكلة التي حلّتها: AI 2 كان translation-heavy؛ الإصدار 3 يُnative Arabic typography، يُQ&amp;A على جداول (OKRs، hiring، budgets)، يُmeeting agent يُpost ملخصًا لـ Slack، يُversion-aware diffs «ما الذي تغيّر في السياسة؟»، يُenterprise search مع connectors (Drive، GitHub)، يُbenchmark −48% وقت onboarding موظف جديد في scale-up كويتي.</p>
      <p>القدرات الأساسية: AI Blocks (ملخص، ترجمة مهنية، قرار log)؛ Custom Agents per workspace؛ offline-friendly mobile summaries؛ HIPAA وSOC2 tiers؛ Notion Consultants program MENA.</p>
      <p>للمبدعين العرب: ops freelancers وboutique PM shops — «Arabic knowledge OS in 7 days» للفرق 15–200 مستخدم. من يُسلّم 10 workspaces Notion AI 3/ربع بـ 1800–28000 دولار + care 360–2400 دولار/شهر يحوّل الفوضى المعرفية إلى أصل قابل للبيع للعميل التالي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI 3 Arabic؟</h3>
        <ul>
          <li><strong>Notion AI 3 workspace (هيكلة، agents، تدريب، migration):</strong> 5–16 يومًا — 1800–28000 دولار/عميل.</li>
          <li><strong>صيانة wiki وضبط agents شهريًا:</strong> — 360–2400 دولار/شهر.</li>
          <li><strong>حزم (agency OS، fundraising، product discovery):</strong> — 45–198 دولار/حزمة.</li>
          <li><strong>دورات «إدارة معرفة عربية مع Notion AI»:</strong> — 38–175 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Productivity</span>
        <span class="tag">Teams</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zapier AI Actions 5 Arabic: جملة عربية واحدة → مئات التطبيقات — أتمتة تُدرّ دخلًا من اليوم الأول!</h2>
      <p class="article-lead">«أريد: إذا وصل lead عربي من Typeform → أضفه HubSpot → أرسل واتساب ترحيبي → أنشئ مجلد Drive → أخبر الفريق في Telegram». في 12 نوفمبر 2026، أطلقت <strong>Zapier</strong> <strong>AI Actions 5 Arabic</strong>: محرك agentic فوق 8000+ تطبيق يُparse طلبات NL بالعربية، يُpropose زاب متعدد الخطوات مع شرح RTL، يُtest في sandbox، يُdeploy مع مراقبة أخطاء، يُsuggest تحسينات من analytics، يُbundle للـ SMBs وagencies — لمن يريد جني المال من الأتمتة دون كتابة كود.</p>
      <p>المشكلة التي حلّتها: Actions 4 كان يحتاج prompt إنجليزي دقيق؛ الإصدار 5 يُdialect-aware triggers، يُhuman-in-the-loop لخطوات حساسة، يُtables وpaths معقّدة (branching، loops)، يُCentral admin للوكالات متعددة العملاء، يُrevenue share marketplace للقوالب العربية، يُbenchmark 94% نجاح أول تشغيل في cohort 200 وكالة خليجية صغيرة.</p>
      <p>القدرات الأساسية: Arabic Zap Copilot؛ Template Store (ecommerce، clinics، courses)؛ MCP bridge؛ client billing dashboards للوكالات؛ شهادة «MENA Automation Architect».</p>
      <p>للمبدعين العرب: Zapier experts وno-code agencies — «Arabic automation stack in 3 days» لكل عميل SMB. من يُشغّل 25 زبائن Actions 5/ربع بـ 800–4500 دولار/زب + maintenance 120–680 دولار/شهر/زب يبني MRR أتمتة يتضاعف مع كل تطبيق جديد في السوق العربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zapier AI Actions 5 Arabic؟</h3>
        <ul>
          <li><strong>Actions 5 setup (زaps، اختبار، تسليم، تدريب):</strong> 2–8 أيام — 800–4500 دولار/عميل SMB.</li>
          <li><strong>رعاية أتمتة وأخطاء شهريًا:</strong> — 120–680 دولار/شهر/عميل.</li>
          <li><strong>بيع قوالب عربية في Marketplace (مرة + اشتراك):</strong> — 29–149 دولار/قالب.</li>
          <li><strong>دورات «وكالة أتمتة عربية بدون كود»:</strong> — 35–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zapier</span>
        <span class="tag">Automation</span>
        <span class="tag">No-Code</span>
        <span class="tag">Agency</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 12-11-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="12-11-2026 -- 08-AM.html">
          📰 12 نوفمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "12-11-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/12-11-2026 -- 08-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/12-11-2026%20--%2008-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
