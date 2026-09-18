#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 18-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "18-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — OpenAI ChatGPT Pulse for Business 2، HubSpot AI Breeze Prospecting 3، Lovable Arabic App Builder 2، Teachable AI Course Factory 3، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 18 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من OpenAI ChatGPT Pulse for Business 2 الذي يرسل لك كل صباح «ماذا تفعل اليوم لزيادة دخلك»، إلى HubSpot AI Breeze Prospecting 3 الذي يكتب رسائل بيع بالعربية ويُجدول المتابعات، ومن Lovable Arabic App Builder 2 الذي يحوّل فكرة تطبيقك إلى MVP جاهز للنشر، إلى Teachable AI Course Factory 3 الذي يُبني دورتك وصفحات البيع والاختبارات في عطلة نهاية واحدة — أربع قصص مسائية في 18 سبتمبر 2026 لمن يريد أدوات AI حقيقية ودخلًا ملموسًا!</h1>
      <p class="hero-sub">مساءٌ للمُنفّذين: أصحاب المشاريع يريدون قرارات يومية ذكية، فرق المبيعات تريد leads دافئة بلا copywriter، المطوّرون والمبتكرون يريدون تطبيقات بلا شهر برمجة، والمدرّبون يريدون دورات تُباع قبل أن ينتهي الأسبوع. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 18 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>OpenAI ChatGPT Pulse for Business 2: موجز يومي بالعربية — فرص، مهام، وتنبيهات إيرادات!</h2>
      <p class="article-lead">«أفتح عشر تبويبات وأنسى ما كان مهمًا». في 18 سبتمبر 2026، أطلقت <strong>OpenAI</strong> <strong>ChatGPT Pulse for Business 2</strong>: يربط بريدك، تقويمك، Shopify أو Stripe، وSlack، فيُرسل كل صباح ملخصًا بالعربية: deals معلّقة، عملاء يحتاجون ردًا، trends في مجالك، و3 مهام revenue-first — مع أزرار «نفّذ الآن» تُطلق workflows جاهزة.</p>
      <p>المشكلة التي حلّتها: founders يغرقون في noise؛ Pulse 2 يُ prioritize حسب هامش الربح، يُ detect churn signals، يُ suggest pricing tweaks، يُ draft replies للمراجعات السلبية، ويُ sync مع فريقك دون تسريب بيانات حساسة (SOC2، data residency للخليج اختياري).</p>
      <p>القدرات الأساسية: custom «playbooks» (launch، Ramadan campaign، B2B outreach)؛ voice brief على الجوال؛ weekly CEO letter auto-draft؛ integrations مع Notion وHubSpot؛ API للوكالات التي تُ manage عشرات العملاء.</p>
      <p>للمبدعين العرب: business coaches وvirtual COOs — «90-day Pulse setup» للمتاجر وال SaaS الصغيرة. من يُ sell 5 retainer/شهر (إعداد + tuning) بـ 1200–6500 دولار + 400–1800 دولار/شهر يبني خط استشارات AI operations.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ChatGPT Pulse for Business 2؟</h3>
        <ul>
          <li><strong>Pulse onboarding for SMBs:</strong> 5–12 يومًا — 1500–12000 دولار/عميل.</li>
          <li><strong>Monthly playbook optimization:</strong> — 500–4200 دولار/شهر.</li>
          <li><strong>Industry morning brief templates (e-commerce، clinics، agencies):</strong> — 69–299 دولار/حزمة.</li>
          <li><strong>دورات «Arabic CEO Daily with Pulse 2»:</strong> — 47–225 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenAI</span>
        <span class="tag">ChatGPT</span>
        <span class="tag">Productivity</span>
        <span class="tag">Founders</span>
        <span class="tag">Automation</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>HubSpot AI Breeze Prospecting 3: من قائمة leads إلى اجتماع محجوز — رسائل عربية، متابعة، وCRM!</h2>
      <p class="article-lead">«لدينا 2000 contact — ولا reply واحد». في 18 سبتمبر 2026، أطلقت <strong>HubSpot</strong> <strong>AI Breeze Prospecting 3</strong>: تُرفع ICP بالعربية، فيُ enrich emails، يُ write sequences شخصية (فصحى أو لهجة خليجية)، يُ suggest best send time، يُ book meetings عبر Calendly، ويُ log كل شيء في CRM — مع compliance لـ CAN-SPAM وGDPR.</p>
      <p>المشكلة التي حلّتها: SDR teams مكلفة وبطيئة؛ Breeze 3 يُ research company news، يُ personalize opening lines، يُ A/B subject lines، يُ pause عند reply، يُ handoff للبشر عند objection، ويُ report pipeline forecast بالعربية.</p>
      <p>القدرات الأساسية: LinkedIn Sales Navigator sync؛ WhatsApp Business templates (where allowed)؛ multi-inbox rotation؛ AI call prep sheets؛ partner tier للوكالات في MENA.</p>
      <p>للمبدعين العرب: B2B agencies وfreelance SDRs — «Outbound-in-a-box» لل SaaS والتعليم والعقارات. من يُ run 4 accounts بـ 2500–18000 دولار/شهر + success fee 5–12% على deals closed يبني machine مبيعات ذكية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Breeze Prospecting 3؟</h3>
        <ul>
          <li><strong>Done-for-you outbound campaigns:</strong> 14–45 يومًا — 3200–28000 دولار/عميل.</li>
          <li><strong>SDR-as-a-service retainers:</strong> — 1800–9500 دولار/شهر.</li>
          <li><strong>Arabic sequence libraries by vertical:</strong> — 89–449 دولار/حزمة.</li>
          <li><strong>دورات «B2B Arabic Outbound with HubSpot AI»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Sales</span>
        <span class="tag">B2B</span>
        <span class="tag">CRM</span>
        <span class="tag">Lead Gen</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Lovable Arabic App Builder 2: «أريد تطبيق حجز عيادة بالعربية» — واجهة، backend، ونشر!</h2>
      <p class="article-lead">«الفكرة واضحة — والميزانية لا تكفي فريقًا». في 18 سبتمبر 2026، أطلقت <strong>Lovable</strong> <strong>Arabic App Builder 2</strong>: تصف التطبيق بالعربية (RTL، payments، notifications)، فيُ generate React UI، Supabase backend، auth، admin panel، وdeploy على Vercel — مع iterates بالمحادثة («أضف تقييمات Google»).</p>
      <p>المشكلة التي حلّتها: no-code كان محدودًا للعربية؛ Builder 2 يُ support Hijri dates، SAR/AED checkout via Stripe، push via Firebase، accessibility RTL، وexport clean code للمطورين الذين يريدون ownership.</p>
      <p>القدرات الأساسية: templates (marketplace، booking، LMS lite)؛ one-click App Store checklist؛ team seats؛ GitHub sync؛ white-label للوكالات.</p>
      <p>للمبدعين العرب: indie hackers وdigital agencies — «MVP weekend» للمطاعم والصالونات والمدارس. من يُ deliver 2 apps/شهر بـ 4500–22000 دولار + maintenance 600–3500 دولار/شهر يجمع project fees + recurring.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lovable Arabic App Builder 2؟</h3>
        <ul>
          <li><strong>Custom MVP builds for local businesses:</strong> 7–21 يومًا — 3800–26000 دولار/مشروع.</li>
          <li><strong>App care plans (updates، features):</strong> — 650–4800 دولار/شهر.</li>
          <li><strong>Vertical starter kits (clinics، gyms، events):</strong> — 99–499 دولار/قالب.</li>
          <li><strong>دورات «Ship Arabic Apps with Lovable 2»:</strong> — 59–279 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lovable</span>
        <span class="tag">No-Code</span>
        <span class="tag">Apps</span>
        <span class="tag">Startups</span>
        <span class="tag">MENA</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Teachable AI Course Factory 3: من outline إلى دورة مدفوعة — فيديو، quizzes، وصفحة مبيعات!</h2>
      <p class="article-lead">«لدي خبرة 10 سنوات — لكن لا وقت لتصوير 40 درسًا». في 18 سبتمبر 2026، أطلقت <strong>Teachable</strong> <strong>AI Course Factory 3</strong>: تُلصق syllabus أو تتحدث بالعربية، فيُ structure modules، يُ script lessons، يُ suggest slides، يُ generate quizzes، يُ create sales page RTL، email launch sequence، وpricing tiers — مع optional AI avatar presenter (بموافقتك).</p>
      <p>المشكلة التي حلّتها: course creators يتوقفون عند production؛ Factory 3 يُ batch record guidance، يُ add captions، يُ drip schedule، يُ integrate payment (TeachablePay)، يُ recommend upsells (coaching، community)، وyields completion analytics.</p>
      <p>القدرات الأساسية: cohort mode؛ certificates بالعربية؛ affiliate hub؛ mobile app viewer؛ compliance hints للتعليم المهني في الخليج.</p>
      <p>للمبدعين العرب: coaches وconsultants — «Launch your course in 10 days» للتسويق والبرمجة واللغات. من يُ combine own catalog + done-for-you 2000–14000 دولار/دورة للعملاء يبني empire تعليم رقمي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Teachable AI Course Factory 3؟</h3>
        <ul>
          <li><strong>Full course production for experts:</strong> 10–30 يومًا — 2500–18000 دولار/دورة.</li>
          <li><strong>Launch marketing retainers:</strong> — 900–5500 دولار/شهر.</li>
          <li><strong>Own niche courses (AI for Arabic marketers، etc.):</strong> — 97–497 دولار/تسجيل recurring.</li>
          <li><strong>دورات «Monetize Knowledge with Teachable Factory 3»:</strong> — 41–199 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Teachable</span>
        <span class="tag">Courses</span>
        <span class="tag">EdTech</span>
        <span class="tag">Creators</span>
        <span class="tag">Passive Income</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 18-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="18-09-2026 -- 04-PM.html">
          📰 18 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">OpenAI ChatGPT Pulse for Business 2 · HubSpot AI Breeze Prospecting 3 · Lovable Arabic App Builder 2 · Teachable AI Course Factory 3</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "18-09-2026 -- 04-PM.html" not in content:
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
        "رobots",
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
