#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 09-08-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "09-08-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HappyRobot، Freehand، Omilia، Gravity، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 9 أغسطس 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من يونيكورن العمليات إلى إعلانات الشات بوت — أربع ثورات تُعيد تعريف اقتصاد AI في أغسطس 2026!</h1>
      <p class="hero-sub">HappyRobot يُصبح يونيكورن بـ 150 مليون دولار لأتمتة عمليات المؤسسات، Freehand يُحرّر 75 مليون دولار لإدارة مشتريات Fortune 500، Omilia يُطلق Lexis ويجمع 67 مليون دولار لخدمة العملاء الصوتية، وGravity يُبني أكبر قناة إعلانية جديدة داخل chatbots. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 9 أغسطس 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HappyRobot: 150 مليون دولار — يونيكورن جديد يُشغّل عمليات المؤسسات بالوكلاء الذكيين!</h2>
      <p class="article-lead">تخيّل أن مكالمات الشحن، رسائل التأمين، وثائق الطيران، ورسائل البريد الإلكتروني بين فرق العمل — كلها تُدار بوكلاء AI يفهمون سياق عملك ويُنفّذون فعلاً لا يُجيبون فقط. HappyRobot جمع 150 مليون دولار Series C بقيمة 1.2 مليار دولار، ليصبح أحد أسرع يونيكورنات agentic AI في العالم.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>HappyRobot</strong> عن <strong>جولة Series C بقيمة 150 مليون دولار</strong> بقيادة <strong>Prysm Capital</strong> و<strong>Eurazeo</strong>، مع مشاركة a16z وBase10 وY Combinator وKoch Disruptive Technologies وOrange وT.Capital (Deutsche Telekom) وBankinter وEndeavor Catalyst. إجمالي التمويل يتجاوز 200 مليون دولار — والتقييم post-money: <strong>1.2 مليار دولار</strong>.</p>
      <p>المشكلة التي يحلّها HappyRobot: المؤسسات الكبرى ما زالت تعتمد على ملايين المكالمات والرسائل والأنظمة المنفصلة يومياً. ChatGPT سهّل توليد المعلومات، لكن <strong>تنفيذ العمليات</strong> بقي يدوياً. HappyRobot يُنشر وكلاء AI عبر الصوت والبريد والوثائق والويب — يتعلمون من كل تفاعل، يُحسّنون workflows، ويُوفّرون رؤية real-time للعمليات.</p>
      <p>الشركة تتوسع من logistics إلى insurance وenergy وtelecoms وairlines — أي قطاع يعتمد على تنسيق عمليات معقّد. Tech.eu وصف HappyRobot كـ «agentic AI for enterprise operations». للمبدعين العرب: كل شركة logistics وطيران وتأمين في MENA تحتاج deployment partner — consulting وcustom agents وtraining فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HappyRobot وثورة enterprise agentic AI؟</h3>
        <ul>
          <li><strong>HappyRobot deployment partner:</strong> نشر وكلاء للـ logistics والطيران — 15000–80000 دولار/مشروع.</li>
          <li><strong>Operational workflow automation:</strong> تحليل وتصميم workflows للمؤسسات — 10000–50000 دولار.</li>
          <li><strong>دورات «Enterprise AI Agents»:</strong> bootcamp للـ operations teams — 299–1499 دولار.</li>
          <li><strong>Managed operations retainer:</strong> صيانة وتحسين الوكلاء — 5000–25000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HappyRobot</span>
        <span class="tag">Agentic AI</span>
        <span class="tag">Enterprise Operations</span>
        <span class="tag">Unicorn</span>
        <span class="tag">$150M Series C</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Freehand: 75 مليون دولار — وكلاء AI يُديرون مشتريات Fortune 500 ويُوفّرون 5–10% من الإنفاق!</h2>
      <p class="article-lead">Procurement ليس glamour — لكنه gold mine. Freehand يُشغّل وكلاء AI autonomously لإدارة supply-chain spend: قراءة العقود، التفاوض مع الموردين، معالجة الفواتير والمدفوعات. Meta وUnilever وJohnson &amp; Johnson وPfizer وDunkin وCardinal Health يستخدمونه — ويُسترد 5–10% من الإنفاق في فئات معقّدة.</p>
      <p>في 6 أغسطس 2026، أعلنت <strong>Freehand</strong> عن <strong>75 مليون دولار</strong> co-led من <strong>Battery Ventures</strong> و<strong>NewRoad Capital Partners</strong>، مع PSP Growth (Penny Pritzker) وNexus Venture Partners. الشركة خرجت من stealth ب deployments حقيقية — ليس pitch deck فقط.</p>
      <p>السر: <strong>Category Context Graph</strong> — graph يُوحّد structured وunstructured data (عقود، policies، invoices، emails). الوكلاء يُ reason عبر البيانات، يفهمون contracts، ويُنفّذون decisions مباشرة في collaboration tools وenterprise systems. النتائج: workflows أسرع 5–7x، procure-to-pay cycles أقل 70%، و savings قابلة للقياس — بدون headcount إضافي أو outsourcing contracts.</p>
      <p>Focus: logistics وdirect materials وMRO — فئات معقّدة حيث outsourcing تقليدي يُكلف مليارات. The AI Insider وصف Freehand كـ «AI teams managing supply chain spend». للمبدعين العرب: manufacturing وretail وhealthcare في MENA — consulting لـ procurement AI، Category Context Graph setup، وpilot deployments فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Freehand وثورة procurement AI؟</h3>
        <ul>
          <li><strong>Procurement AI consulting:</strong> تحليل spend وdeployment وكلاء — 20000–100000 دولار/مشروع.</li>
          <li><strong>Category Context Graph setup:</strong> بناء knowledge graphs للمؤسسات — 15000–60000 دولار.</li>
          <li><strong>دورات «AI Procurement»:</strong> workshop للـ finance وprocurement — 249–1299 دولار.</li>
          <li><strong>Savings-share model:</strong> نسبة من الـ 5–10% recovered — recurring revenue.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Freehand</span>
        <span class="tag">Procurement AI</span>
        <span class="tag">Supply Chain</span>
        <span class="tag">Category Context Graph</span>
        <span class="tag">$75M Funding</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Omilia: 67 مليون دولار — Lexis و1000+ Taco Bell drive-thru تُثبت أن voice AI جاهز للمؤسسات!</h2>
      <p class="article-lead">Voice AI في drive-thru كان joke — حتى Taco Bell. Omilia تُشغّل voice AI في أكثر من 1000 drive-thru عبر 38 ولاية أمريكية — order times أسرع، accuracy أعلى، staff retention أفضل. الآن Lexis: generative TTS model مُصمّم لـ contact centers enterprise. 67 مليون دولار Series B من Expedition Growth Capital.</p>
      <p>في 6 أغسطس 2026، أعلنت <strong>Omilia</strong> (Self-Learning Agentic CX) عن <strong>Series B بقيمة 67 مليون دولار</strong> بقيادة <strong>Expedition Growth Capital</strong>. الشركة trusted by world's largest enterprises — Gartner Visionary في Conversational AI Platforms Q2 2026.</p>
      <p>الإنجازات 2026: expanded agreement مع Taco Bell (1000+ drive-thrus)، إطلاق <strong>Lexis</strong> — generative text-to-speech built natively للـ contact centers، perform cost-effectively at scale. التمويل يدعم North America expansion، opening أول US office H2 2026، وsenior GTM hires (Nick Delis CRO، Ryan Kam CMO — ex-Five9، ARR $100M→$1B+).</p>
      <p>Omilia fit for highly regulated وsecurity-first organizations — voice-first platform scalable. للمبدعين العرب: QSR chains وbanks وtelcos في MENA — voice AI deployment، Lexis integration، وArabic TTS customization فرصة ضخمة. كل drive-thru وcall center يحتاج partner محلي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Omilia وثورة agentic CX؟</h3>
        <ul>
          <li><strong>Voice AI deployment:</strong> Taco Bell-style drive-thru وcall centers — 25000–120000 دولار/مشروع.</li>
          <li><strong>Arabic Lexis customization:</strong> TTS عربي للـ contact centers — 10000–50000 دولار.</li>
          <li><strong>QSR voice ordering:</strong> pilot للـ fast food chains MENA — 15000–80000 دولار.</li>
          <li><strong>دورات «Voice AI for CX»:</strong> bootcamp للـ customer experience — 199–999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Omilia</span>
        <span class="tag">Agentic CX</span>
        <span class="tag">Lexis TTS</span>
        <span class="tag">Taco Bell</span>
        <span class="tag">$67M Series B</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Gravity: 30.5 مليون دولار — إعلانات chatbots ستصبح أكبر قناة إعلانية في العالم!</h2>
      <p class="article-lead">Zach Oldham، cofounder Gravity، يؤمن: AI ads ستصبح world's largest advertising channel. ليس إعلانات للبشر فقط — بل إعلانات موجهة للـ AI bots themselves. Gravity جمع 30.5 مليون دولار Series A — full-stack ad platform: DSP للمعلنين، SSP للمطورين، exchange يربطهما. Lightspeed وCommitted Capital co-lead.</p>
      <p>في أغسطس 2026، أعلنت <strong>Gravity</strong> عن <strong>Series A بقيمة 30.5 مليون دولار</strong> co-led من <strong>Lightspeed Venture Partners</strong> و<strong>Committed Capital</strong>. إجمالي التمويل: 38.5 مليون دولار. Business Insider exclusive: «AI ads will eventually become the world's largest advertising channel.»</p>
      <p>المنصة: <strong>Demand-side platform</strong> — يساعد المعلنين وضع ads داخل AI chatbots وإلى agents. <strong>Supply-side platform</strong> — يساعد developers AI apps monetize عبر ads. <strong>Exchange</strong> يربط الطرفين. أدوات measurement وad creation. Text-based ads داخل chat interfaces — حيث attention ينتقل.</p>
      <p>الفرصة: كل ChatGPT وClaude وPerplexity وcustom agents — surfaces جديدة للإعلان. Gravity يبني infrastructure قبل flood. للمبدعين العرب: ad agencies تُ adapt campaigns لـ AI surfaces، developers يُ monetize chatbots، consultants في «AI ad strategy» — economy جديدة قبل mainstream.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gravity وثورة AI advertising؟</h3>
        <ul>
          <li><strong>AI ad strategy consulting:</strong> campaigns للمعلنين على chatbots — 5000–40000 دولار/مشروع.</li>
          <li><strong>Chatbot monetization setup:</strong> SSP integration للمطورين — 3000–25000 دولار.</li>
          <li><strong>Ad creative for AI surfaces:</strong> text ads optimized للـ agents — 2000–15000 دولار/campaign.</li>
          <li><strong>دورات «Monetize Your AI App»:</strong> workshop للمطورين — 149–699 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gravity</span>
        <span class="tag">AI Advertising</span>
        <span class="tag">Chatbot Monetization</span>
        <span class="tag">AdTech</span>
        <span class="tag">$30.5M Series A</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 09-08-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
