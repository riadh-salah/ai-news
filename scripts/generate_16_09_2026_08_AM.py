#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "16-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Anthropic Claude for Excel 2، Meta WhatsApp Flows AI Builder، Replit Deploy AI 3، ConvertKit Creator AI 2 للمبدعين العرب، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 16 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Anthropic Claude for Excel 2 الذي يُحوّل جداولك إلى محلل مالي يتحدث العربية، إلى Meta WhatsApp Flows AI Builder الذي يبني متجرًا محادثيًا في ساعة، ومن Replit Deploy AI 3 الذي يُطلق SaaS من فكرة واحدة، إلى ConvertKit Creator AI 2 الذي يكتب سلاسل بريد تبيع منتجاتك وأنت نائم — أربع موجات صباحية في 16 سبتمبر 2026 لمن يريد دخلًا ذكيًا من الذكاء الاصطناعي!</h1>
      <p class="hero-sub">صباحٌ مليء بالفرص: المحاسبون يريدون تقارير فورية، التجار يريدون مبيعات على واتساب دون مطور، المبرمجون يريدون deploy خلال دقائق، والكُتّاب يريدون newsletters تُ convert. أربع قصص عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 16 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Anthropic Claude for Excel 2: جدولك يصبح CFO ذكيًا — تحليل، توقعات، ولوحات بالعربية بلمسة واحدة!</h2>
      <p class="article-lead">«عندك 47 تبويبًا في Excel — والمدير يريد forecast قبل الاجتماع بساعة». في 16 سبتمبر 2026، أطلقت <strong>Anthropic</strong> <strong>Claude for Excel 2</strong>: إضافة enterprise تُ read كل المصنف، تُفهم الصيغ والماكرو، وتُ answer بالعربية: «ما هامش الربح في Q3؟»، «أعدّ scenario إذا انخفض الدولار 5%»، وتُ generate pivot charts جاهزة للعرض.</p>
      <p>المشكلة التي حلّتها: Copilots القديمة كانت تُ hallucinate أرقامًا؛ Excel 2 يُ anchor كل إجابة بـ cell references، يُ log audit trail للامتثال، ويُ refuse تعديلات خطيرة دون تأكيد — مثالي لبنوك وشركات family office في الخليج.</p>
      <p>القدرات الأساسية: دعم RTL في التعليقات والتقارير المُصدّرة؛ ربط Power BI وGoogle Sheets sync؛ templates جاهزة (P&amp;L، cash flow، inventory)؛ SSO وSOC2؛ pricing per seat مع حزم 50 مستخدم للمجموعات.</p>
      <p>للمبدعين العرب: محاسبون ومستشارون ماليون — «Excel AI audit» أسبوعي للشركات المتوسطة. من يُ package 5 dashboards عربية + تدريب 2 ساعة ويبيعها 1800–12000 دولار/ربع يبني retainer قبل Big Four.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Claude for Excel 2؟</h3>
        <ul>
          <li><strong>Financial modeling sprints:</strong> 3–10 أيام — 2200–18000 دولار/شركة.</li>
          <li><strong>Managed FP&amp;A retainers:</strong> تحديث نماذج + Claude prompts — 900–7500 دولار/شهر.</li>
          <li><strong>Template packs (retail، construction، NGOs):</strong> — 79–449 دولار/حزمة.</li>
          <li><strong>دورات «Arabic FP&amp;A with Claude Excel»:</strong> bootcamp — 49–239 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Anthropic</span>
        <span class="tag">Claude</span>
        <span class="tag">Excel</span>
        <span class="tag">Finance</span>
        <span class="tag">Enterprise</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Meta WhatsApp Flows AI Builder: متجر كامل داخل المحادثة — catalog، دفع، ودعم باللهجة المحلية!</h2>
      <p class="article-lead">«زبونك لا يريد تطبيقًا جديدًا — يريد يشتري من واتساب». في 16 سبتمبر 2026، أطلقت <strong>Meta</strong> <strong>WhatsApp Flows AI Builder</strong>: منشئ no-code يصف متجرك بالعربية، فيُ generate flows (browse، cart، checkout، tracking)، يُ connect Meta Pay وTap وPaymob، ويُ train bot على FAQ بالعامية الخليجية والمصرية.</p>
      <p>المشكلة التي حلّتها: SMBs في MENA تدفع آلاف الدولارات لمطورين؛ Builder يُ import من Salla وShopify CSV، يُ suggest upsells من سلوك المحادثة، ويُ A/B test رسائل الترحيب — launch في يوم واحد.</p>
      <p>القدرات الأساسية: catalog sync كل 15 دقيقة؛ order notifications للmerchant على WhatsApp؛ analytics conversion per flow؛ compliance templates للصحة والمال؛ partner program 20% rev share على setup fees.</p>
      <p>للمبدعين العرب: وكالات social commerce — «WhatsApp store in 48h» للمطاعم والعيادات والبوتiques. من يُ sell 8 packages/شهر بـ 999–4999 دولار يصل لـ 40K MRR مع فريق صغير.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من WhatsApp Flows AI Builder؟</h3>
        <ul>
          <li><strong>WhatsApp commerce setup:</strong> flows + payments + training — 1200–8500 دولار/متجر.</li>
          <li><strong>Monthly chat commerce retainers:</strong> optimization + campaigns — 700–6000 دولار/شهر.</li>
          <li><strong>Vertical flow templates (clinics، F&amp;B، fashion):</strong> — 49–299 دولار/قالب.</li>
          <li><strong>دورات «Sell on WhatsApp with Meta AI Builder»:</strong> — 39–189 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meta</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Commerce</span>
        <span class="tag">MENA</span>
        <span class="tag">No-Code</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Replit Deploy AI 3: من prompt إلى SaaS live — auth، billing، وdomain خلال 90 دقيقة!</h2>
      <p class="article-lead">«لديك فكرة micro-SaaS — لكن Stripe وOAuth يأكلان شهرًا». في 16 سبتمبر 2026، أطلقت <strong>Replit</strong> <strong>Deploy AI 3</strong>: agent يُ build full-stack (Next.js أو Flask)، يُ add login، Stripe subscriptions، admin panel، ويُ deploy على Replit Cloud مع custom domain — من وصف عربي أو إنجليزي.</p>
      <p>المشكلة التي حلّتها: vibe coders يتوقفون عند production؛ Deploy 3 يُ run security scan، env secrets، rate limits، وmonitoring — مع «fix loop» تلقائي عند فشل CI.</p>
      <p>القدرات الأساسية: Arabic UI generation مع RTL؛ one-click fork to GitHub؛ usage-based hosting tiers؛ marketplace لـ «Replit Apps» حيث تبيع قوالب جاهزة؛ team seats للوكالات.</p>
      <p>للمبدعين العرب: indie hackers وdev agencies — «SaaS factory»: 3 منتجات niche (HR leave tracker، invoice OCR عربي، booking للصالونات) وبيع أول 100 seat. من يُ white-label Deploy 3 للعملاء المحليين يفرض 5000–25000 دولار/مشروع + 15% maintenance.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Replit Deploy AI 3؟</h3>
        <ul>
          <li><strong>Micro-SaaS builds for clients:</strong> MVP to production — 3500–28000 دولار/منتج.</li>
          <li><strong>Replit template marketplace:</strong> sell forks — 29–199 دولار/قالب + recurring hosting margin.</li>
          <li><strong>Managed SaaS ops:</strong> updates + support — 800–6500 دولار/شهر/تطبيق.</li>
          <li><strong>دورات «Launch Arabic SaaS on Replit in One Weekend»:</strong> — 55–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Replit</span>
        <span class="tag">Deploy AI</span>
        <span class="tag">SaaS</span>
        <span class="tag">Indie</span>
        <span class="tag">Developers</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ConvertKit Creator AI 2: newsletters تبيع — sequences عربية، landing pages، وaffiliate في منصة واحدة!</h2>
      <p class="article-lead">«قائمتك 12 ألف مشترك — لكن open rate 14%». في 16 سبتمبر 2026، أطلقت <strong>ConvertKit</strong> <strong>Creator AI 2</strong>: suite تُ write subject lines A/B tested، body بالفصحى أو dialect toggle، landing pages من outline، و«Revenue sequences» تُ recommend منتجات affiliate أو digital products بناءً على clicks السابقة.</p>
      <p>المشكلة التي حلّتها: creators العرب يُ copy-paste prompts بين أدوات؛ Creator AI 2 يُ live في editor، يُ respect brand voice profile، يُ schedule Ramadan وseasonal campaigns، ويُ integrate Gumroad وTeachable وStripe.</p>
      <p>القدرات الأساسية: spam score checker للعربية؛ segmentation «مهتم بالتسويق / التقنية / الاستثمار»؛ referral program automation؛ analytics LTV per subscriber؛ Creator Pro بـ unlimited AI generations.</p>
      <p>للمبدعين العرب: coaches وnewsletter writers — «Done-for-you email engine» للخبراء الذين لديهم audience على LinkedIn وX. من يُ run 5 clients بـ 1500–7000 دولار/شهر each يبني agency خفيفة بدون موظفين كُثر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Creator AI 2؟</h3>
        <ul>
          <li><strong>Newsletter growth + monetization setup:</strong> — 1800–11000 دولار/عميل.</li>
          <li><strong>Monthly creator retainers:</strong> 4–8 emails + funnels — 900–5500 دولار/شهر.</li>
          <li><strong>Sequence template packs (courses، consulting، SaaS trials):</strong> — 59–349 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Newsletters that Pay with ConvertKit AI»:</strong> — 42–199 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ConvertKit</span>
        <span class="tag">Newsletter</span>
        <span class="tag">Creator Economy</span>
        <span class="tag">Email</span>
        <span class="tag">Monetization</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 16-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="16-09-2026 -- 08-AM.html">
          📰 16 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Claude for Excel 2 · WhatsApp Flows AI · Replit Deploy AI 3 · ConvertKit Creator AI 2</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "16-09-2026 -- 08-AM.html" not in content:
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
        "سبتمber",
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
