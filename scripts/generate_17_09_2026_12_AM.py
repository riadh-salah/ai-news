#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 17-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "17-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google Gemini Deep Research 2، Figma Make 2، ElevenLabs Dubbing Studio 3، Kajabi AI Course Architect 2، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 17 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Google Gemini Deep Research 2 الذي يُنجز لك تقريرًا استراتيجيًا من 40 صفحة بينما تنام، إلى Figma Make 2 الذي يحوّل وصفًا عربيًا إلى واجهة جاهزة للتطوير، ومن ElevenLabs Dubbing Studio 3 الذي يُ dub محتواك العالمي بصوت خليجي أو مصري في ساعات، إلى Kajabi AI Course Architect 2 الذي يبني دورة كاملة وصفحة بيع ورسائل بريد — أربع شرارات ليلية في 17 سبتمبر 2026 لمن يريد دخلًا ذكيًا من الذكاء الاصطناعي!</h1>
      <p class="hero-sub">ليلةٌ للمبدعين والاستشاريين: الباحثون يريدون تقارير عميقة دون فريق تحليل، المصممون يريدون MVP بصريًا قبل نهاية الأسبوع، صناع المحتوى يريدون أسواقًا جديدة بلغتهم، والمدربون يريدون منتجًا رقميًا يُباع وهو نائم. أربع قصص عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 17 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google Gemini Deep Research 2: محلل استراتيجي يعمل ساعات — تقارير منافسين، SWOT، ومصادر موثّقة بالعربية!</h2>
      <p class="article-lead">«المدير يريد دراسة سوق الخليج للـ fintech — والموعد بعد 36 ساعة». في 17 سبتمبر 2026، أطلقت <strong>Google</strong> <strong>Gemini Deep Research 2</strong>: agent بحث يُ plan خطوات متعددة، يزور مئات المصادر، يُ synthesize findings، ويُ export PDF وGoogle Doc بالعربية مع footnotes وروابط — دون أن تُ lost في tab chaos.</p>
      <p>المشكلة التي حلّتها: Chatbots تُلخص سريعًا لكن shallow؛ Deep Research 2 يُ run sessions 15–90 دقيقة، يُ track contradictions بين مصادر، يُ flag outdated stats، ويُ respect Workspace policies — مثالي لـ strategy teams وinvestors في MENA.</p>
      <p>القدرات الأساسية: templates «market entry GCC»، «competitor teardown»، «regulatory scan»؛ تكامل Drive وSlides لتوليد deck تلقائي؛ shared team vault للتقارير؛ enterprise data residency؛ API preview للintegrators.</p>
      <p>للمبدعين العرب: مستشارون وanalysts مستقلون — «Deep Research sprint» أسبوعي لـ 3 عملاء. من يُ package تقرير 25–40 صفحة + executive summary عربي + 10-slide deck ويبيعه 3200–22000 دولار/مشروع يبني pipeline قبل big four.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gemini Deep Research 2؟</h3>
        <ul>
          <li><strong>Strategic research packages:</strong> قطاع واحد، 3–8 منافسين — 2800–24000 دولار/مشروع.</li>
          <li><strong>Monthly intelligence retainers:</strong> تقارير + Deep Research workflows — 1400–9800 دولار/شهر.</li>
          <li><strong>Industry prompt &amp; template libraries:</strong> retail، SaaS، logistics — 79–449 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Strategic Research with Gemini Deep Research 2»:</strong> — 55–269 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Gemini</span>
        <span class="tag">Deep Research</span>
        <span class="tag">Strategy</span>
        <span class="tag">Enterprise</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Figma Make 2: «صمّم لي تطبيق توصيل طعام عربي» — من prompt إلى frames، components، وhandoff!</h2>
      <p class="article-lead">«العميل يريد mockup قبل الاجتماع — والمصمم في إجازة». في 17 سبتمبر 2026، أطلقت <strong>Figma</strong> <strong>Make 2</strong>: مولّد واجهات داخل Figma يقرأ brief عربي أو إنجلizi، يُ produce multi-screen flows، auto-layout، design tokens، وvariants — جاهز لـ Dev Mode خلال دقائق.</p>
      <p>المشكلة التي حلّتها: AI خارج Figma يُ export صور static؛ Make 2 يُ edit layers حقيقية، يُ sync مع libraries الفريق، يُ apply brand kit، ويُ generate responsive breakpoints — مع revision history كامل.</p>
      <p>القدرات الأساسية: RTL-aware layouts للعربية؛ component mapping إلى React وSwiftUI snippets؛ accessibility checks WCAG؛ Org plans مع audit؛ Make API لـ embed في internal tools.</p>
      <p>للمبدعين العرب: freelancers وproduct studios — «Make sprint» 48 ساعة: 8–15 شاشة + design system lite. من يُ sell 5 packages/شهر بـ 1800–9500 دولار each يصل لـ 50K+ revenue مع margin عالٍ على وقت التعديل اليدوي فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Figma Make 2؟</h3>
        <ul>
          <li><strong>UI sprint packages:</strong> MVP mobile أو web — 1500–14000 دولار/مشروع.</li>
          <li><strong>Design system kickstarts:</strong> tokens + 20 components — 4000–28000 دولار.</li>
          <li><strong>Arabic brief &amp; pattern libraries:</strong> fintech، edtech، marketplace — 59–329 دولار/حزمة.</li>
          <li><strong>دورات «Ship Arabic UI Faster with Figma Make 2»:</strong> — 48–229 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Figma</span>
        <span class="tag">Make 2</span>
        <span class="tag">UI Design</span>
        <span class="tag">RTL</span>
        <span class="tag">Product</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ElevenLabs Dubbing Studio 3: حوّل podcast إنجليزي إلى نسخة عربية — صوت، إيقاع، وemotions متطابقة!</h2>
      <p class="article-lead">«لديك 200 حلقة podcast — وتريد penetrate السوق السعودي». في 17 سبتمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 3</strong>: pipeline dubbing يُ preserve timing، يُ match speaker voices، يُ translate contextually للعربية (MSA أو dialect target)، ويُ export video أو audio-only — batch لـ 50 ملف دفعة واحدة.</p>
      <p>المشكلة التي حلّتها: dubbing تقليدي expensive وبطيء؛ Studio 3 يُ offer human-in-the-loop QA dashboard، glossary per brand، lip-sync optional للـ talking head، وcompliance flags للمحتوى الحساس.</p>
      <p>القدرات الأساسية: voice clone licensed للbrands؛ studio API؛ revenue share للstudios MENA؛ CDN delivery؛ SSO للmedia enterprises.</p>
      <p>للمبدعين العرب: media houses وcourse creators — «Arabic dub factory»: 30 ساعة/شهر محتوى أجنبي → منتج محلي. من يُ retainer 3500–19000 دولار/شهر + pass-through API يبني recurring revenue قبل broadcasters.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 3؟</h3>
        <ul>
          <li><strong>Batch dubbing projects:</strong> 10–100 حلقة — 4200–65000 دولار/عقد.</li>
          <li><strong>Managed localization retainers:</strong> weekly drops + QA — 2200–14500 دولار/شهر.</li>
          <li><strong>Brand voice &amp; glossary setup:</strong> — 1200–8500 دولار/عميل.</li>
          <li><strong>دورات «Monetize Global Content in Arabic with Dubbing Studio 3»:</strong> — 62–289 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Localization</span>
        <span class="tag">Media</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Kajabi AI Course Architect 2: من فكرة إلى دورة، landing page، وemail funnel — بيع قبل تصوير الحلقة الأولى!</h2>
      <p class="article-lead">«تريد launch دورة «الذكاء الاصطناعي للمحامين» — ولا تعرف من أين تبدأ». في 17 سبتمبر 2026، أطلقت <strong>Kajabi</strong> <strong>AI Course Architect 2</strong>: suite يُ outline curriculum، يُ write scripts عربية، يُ generate slides وworksheets، يُ build sales page وcheckout، ويُ schedule 7-day email sequence — مع A/B على headlines.</p>
      <p>المشكلة التي حلّتها: creators يضيعون أشهر في structure؛ Architect 2 يُ ingest competitor URLs ويُ suggest differentiation، يُ price based on market signals، ويُ connect Stripe وTap للدفع المحلي — analytics على conversion per module.</p>
      <p>القدرات الأساسية: community space auto-setup؛ affiliate program templates؛ mobile app wrapper؛ compliance disclaimers للconsulting niches؛ partner tier للagencies building courses for clients.</p>
      <p>للمبدعين العرب: coaches وsubject experts — «done-for-you course launch»: 14 يوم من idea إلى live. من يُ charge 8000–45000 دولار setup + 15% rev share على launch يملأ calendar قبل solo creators.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Kajabi AI Course Architect 2؟</h3>
        <ul>
          <li><strong>Full course launch packages:</strong> outline → live funnel — 7500–48000 دولار/عميل.</li>
          <li><strong>Monthly creator ops retainers:</strong> updates + email + A/B — 1900–12000 دولار/شهر.</li>
          <li><strong>Niche playbook libraries (legal، HR، real estate AI):</strong> — 89–399 دولار/حزمة.</li>
          <li><strong>دورات «Launch Arabic Digital Products with Course Architect 2»:</strong> — 54–259 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Kajabi</span>
        <span class="tag">Course Architect</span>
        <span class="tag">EdTech</span>
        <span class="tag">Funnel</span>
        <span class="tag">Monetization</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 17-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="17-09-2026 -- 12-AM.html">
          📰 17 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Gemini Deep Research 2 · Figma Make 2 · ElevenLabs Dubbing Studio 3 · Kajabi Course Architect 2</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "17-09-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


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


if __name__ == "__main__":
    main()
