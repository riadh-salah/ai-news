#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 14-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "14-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "OpenAI Operator 2 Arabic · Vercel v0 Enterprise 3 Arabic · "
    "Mistral Agents API 2 Arabic · Glean Assistant 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI Operator 2 Arabic، Vercel v0 Enterprise 3 Arabic، Mistral Agents API 2 Arabic، Glean Assistant 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 14 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من OpenAI Operator 2 Arabic الذي يُكمل حجوزات الطيران ويُرسل لك تأكيدًا بالعربية قبل أن تنهي غسل أسنانك، إلى Vercel v0 Enterprise 3 Arabic الذي يُحوّل وصفًا عربيًا لتطبيق SaaS إلى واجهة RTL مع backend جاهز، ومن Mistral Agents API 2 Arabic الذي يُشغّل وكلاء فرنسا والخليج على نفس البنية بتهجئة عربية دقيقة، إلى Glean Assistant 3 Arabic الذي يُجيب عن سياسة الشركة من Slack وDrive دون أن يختلق — أربع قصص ليلية في 14 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ للمؤسسات والمستقلين: المتصفح أصبح موظفًا، التصميم أصبح إنتاجًا، النماذج الأوروبية تريد وكلاءً عربيين، والبحث الداخلي ما زال يفشل. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 14 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI Operator 2 Arabic: وكيل متصفح يُنجز مهامك — حجوزات، نماذج، ومشتريات بإشراف!</h2>
      <p class="article-lead">«أريد تذكرة الرياض–باريس يوم الخميس بدرجة رجال الأعمال تحت 4200 ريال — وأنا نائم». في 14 نوفمبر 2026، أطلقت <strong>OpenAI</strong> <strong>Operator 2 Arabic</strong>: وكيل computer-use يتحكم بالمتصفح الحقيقي، يقرأ النماذج والقوائم المنسدلة، يملأ حقول الاسم والجواز بالعربية والإنجليزية، يُوقف قبل الدفع ويطلب موافقة بصريّة، يُسجّل فيديو لكل خطوة للتدقيق، يُدمج مع ChatGPT للتخطيط وOutlook للتقويم — للمسافرين والمحامين والمكاتب الإدارية في MENA.</p>
      <p>المشكلة التي حلّتها: Operator 1 كان بطيئًا ومحدود اللغة؛ الإصدار 2 يُسرّع التنفيذ بثلاث مرات، يُفهم لوحات عربية ومواقع حكومية إقليمية، يُحفظ بروفايلات دفع وعناوين بشكل مشفّر محليًا، يُدير multi-step workflows (تأشيرة + فندق + تأمين سفر)، يُرسل تقريرًا ليليًا بالفصحى، يُحترم allowlist للنطاقات في Enterprise، وSLA لفرق 50+ مقعد.</p>
      <p>القدرات الأساسية: Arabic task templates؛ موافقة قبل كل تحويل مالي؛ تكامل SAML؛ سجل امتثال SOC2؛ حزم «حجز مؤتمرات» و«تجديد تراخيص» و«متابعة مناقصات».</p>
      <p>للمبدعين العرب: automation boutiques — «Operator 2 Arabic concierge في 5 أيام» للعائلات والشركات الصغيرة. من يُشغّل 10 اشتراكات بإدارة شهرية 280–1600 دولار/عميل + onboarding 650–4800 دولار يبيع وقتًا نادرًا لمن يعمل ليلًا.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenAI Operator 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Operator 2 (قوالب عربية، سياسات موافقة، تدريب):</strong> 3–12 يومًا — 650–4800 دولار/عميل.</li>
          <li><strong>إدارة مهام شهرية (سفر، مشتريات، متابعة حكومية):</strong> — 280–1600 دولار/شهر.</li>
          <li><strong>حزم قطاعية (قانون، عقارات، تعليم):</strong> — 52–218 دولار/حزمة.</li>
          <li><strong>دورات «أتمتة متصفح آمنة بالعربية مع Operator»:</strong> — 48–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">Operator</span>
        <span class="tag">Automation</span>
        <span class="tag">Browser</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Vercel v0 Enterprise 3 Arabic: من فكرة عربية إلى منتج RTL — UI، API، وdeploy!</h2>
      <p class="article-lead">«العميل يريد landing عربية + لوحة تحكم للمشتركين — والموعد بعد أسبوع». في 14 نوفمبر 2026، أطلقت <strong>Vercel</strong> <strong>v0 Enterprise 3 Arabic</strong>: مولّد واجهات يفهم برومبتات بالفصحى واللهجة الخليجية، يُنتج React وNext.js مع typography RTL، يُقترح جداول Postgres وauth وStripe، يُرفع مباشرة إلى Vercel مع preview لكل فرع، يُربط design tokens لعلامة العميل، ويُ enforce سياسات أمان للمؤسسات — لوكالات وم startups في الشرق الأوسط.</p>
      <p>المشكلة التي حلّتها: v0 السابق كان prototype فقط؛ Enterprise 3 يُولّد routes كاملة، يُكتب tests أساسية، يُوثّق API بالعربية، يُدمج مع Supabase وPlanetScale، يُراجع accessibility WCAG للنص العربي، يُصدر mobile-responsive تلقائيًا، يُشترك SSO وRBAC، ويُوفر quota للفرق 25+ مقعد.</p>
      <p>القدرات الأساسية: Arabic design system import؛ مكتبة مكونات shadcn RTL؛ تكامل Figma؛ مراجعات فرق قبل merge؛ شهادة شريك «MENA v0 Studio».</p>
      <p>للمبدعين العرب: product studios — «MVP عربي على Vercel في 72 ساعة» للمستثمرين الأوائل. من يُسلّم 8 منتجات/ربع بـ 2400–28000 دولار + retainer صيانة 400–2200 دولار/شهر يحوّل v0 إلى خط إنتاج SaaS عربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Vercel v0 Enterprise 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء MVP عربي (واجهات، auth، دفع، deploy):</strong> 5–18 يومًا — 2400–28000 دولار/منتج.</li>
          <li><strong>صيانة وتطوير ميزات شهريًا:</strong> — 400–2200 دولار/شهر.</li>
          <li><strong>حزم قوالب (تعليم، عيادات، عقارات):</strong> — 58–240 دولار/حزمة.</li>
          <li><strong>دورات «بناء منتجات RTL مع v0 بالعربية»:</strong> — 44–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Vercel</span>
        <span class="tag">v0</span>
        <span class="tag">SaaS</span>
        <span class="tag">RTL</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Mistral Agents API 2 Arabic: وكلاء أوروبيون يتحدثون العربية — أدوات، ذاكرة، وحوكمة!</h2>
      <p class="article-lead">«بنك في باريس لديه فريق دعم بالعربية — ويريد نموذجًا أوروبيًا لا أمريكيًا». في 14 نوفمبر 2026، أطلقت <strong>Mistral</strong> <strong>Agents API 2 Arabic</strong>: إطار وكلاء فوق Mistral Large مع فهم morphological للعربية، يُسجّل أدوات HTTP وdatabases، يُدير ذاكرة محادثة ومستندات، يُشغّل multi-agent orchestration، يُطبّق GDPR واستضافة فرنسية، يُدعم لهجات خليجية ومصرية في الردود الصوتية — للبنوك والطيران والتعليم في أوروبا والخليج.</p>
      <p>المشكلة التي حلّتها: الإصدار 1 كان إنجليزيًا ثم يُترجم؛ الإصدار 2 يُفكر بالعربية في chain-of-thought داخلي، يُقلّل hallucination على أرقام عربية-هندية، يُوفّر dashboards استخدام tokens، يُكامل Azure وOVH، يُصدر eval sets لـ MENA، وpricing تنافسي لـ millions من calls شهريًا.</p>
      <p>القدرات الأساسية: Arabic tool calling؛ حماية prompt injection؛ BYOK؛ templates لوكلاء HR وIT وlegal؛ marketplace شركاء عرب.</p>
      <p>للمبدعين العرب: EU-MENA integrators — «Mistral agent عربي جاهز في 7 أيام». من يُنشر 6 حلول/ربع بـ 3800–45000 دولار + دعم 720–5400 دولار/شهر يبيع سيادة بيانات أوروبية بلغة العميل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Mistral Agents API 2 Arabic؟</h3>
        <ul>
          <li><strong>بناء وكيل Mistral عربي (أدوات، ذاكرة، اختبارات، go-live):</strong> 6–20 يومًا — 3800–45000 دولار/عميل.</li>
          <li><strong>مراقبة أداء وتحديث أدوات شهريًا:</strong> — 720–5400 دولار/شهر.</li>
          <li><strong>حزم امتثال (GDPR، PCI، طبية):</strong> — 72–310 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء Mistral بالعربية للمؤسسات»:</strong> — 55–230 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Mistral</span>
        <span class="tag">Agents</span>
        <span class="tag">API</span>
        <span class="tag">GDPR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Glean Assistant 3 Arabic: بحث مؤسسي يُجيب بالعربية — Slack، Drive، ومصادر موثّقة!</h2>
      <p class="article-lead">«موظف جديد يسأل: ما سياسة العمل عن بُعد لدينا؟ — والإجابة مدفونة في 12 أداة». في 14 نوفمبر 2026، أطلقت <strong>Glean</strong> <strong>Assistant 3 Arabic</strong>: مساعد معرفة يُفهرس Confluence وGoogle Workspace وSlack وJira وSalesforce، يُجيب بالفصحى مع اقتباس رابط وسطر، يُميّز بين سياسة قديمة وحديثة، يُقترح خبيرًا بشريًا عند الغموض، يُحترم أذونات المستخدم، يُعمل من sidebar في Teams وSlack — للشركات 500–50000 موظف في المنطقة.</p>
      <p>المشكلة التي حلّتها: Assistant 2 كان يُخطئ في المصطلحات العربية؛ الإصدار 3 يُحسّن semantic search ثنائي اللغة، يُلخّص threads طويلة بالعربية، يُولّد onboarding paths للموظفين الجدد، يُكامل مع DLP، يُقيس «time saved» لكل قسم، packs للمالية والقانون والهندسة، وresidency في Frankfurt وDubai.</p>
      <p>القدرات الأساسية: Arabic Q&amp;A مع citations؛ تنبيهات عند تغيّر سياسة؛ widgets في بوابة الموظف؛ API للبوتات الداخلية؛ برنامج شريك «Glean MENA».</p>
      <p>للمبدعين العرب: knowledge consultancies — «Glean Assistant 3 عربي live في 14 يومًا». من يُنفّذ 5 rollouts/ربع بـ 5200–62000 دولار + tuning 980–7200 دولار/شهر يحوّل الفوضى المؤسسية إلى إجابة واحدة موثوقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Glean Assistant 3 Arabic؟</h3>
        <ul>
          <li><strong>نشر Glean 3 (فهرسة، سياسات، تدريب، إطلاق):</strong> 10–24 يومًا — 5200–62000 دولار/عميل.</li>
          <li><strong>ضبط جودة إجابات ومصادر شهريًا:</strong> — 980–7200 دولار/شهر.</li>
          <li><strong>حزم أقسام (موارد بشرية، مبيعات، هندسة):</strong> — 65–278 دولار/حزمة.</li>
          <li><strong>دورات «معرفة مؤسسية عربية مع Glean»:</strong> — 52–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Glean</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Search</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 14-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="14-11-2026 -- 12-AM.html">
          📰 14 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "14-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/14-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/14-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
