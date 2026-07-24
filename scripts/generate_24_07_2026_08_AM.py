#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 24-07-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "24-07-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Etched، Meshy، Trooly، Natural، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 24 يوليو 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">⚡ نشرة AI العالمية</span>
      <h1>من رقائق inference بـ 10.3 مليار دولار إلى مدفوعات الوكلاء الذكية — AI يُعيد هندسة البنية التحتية والتجارة والبحث والإبداع ثلاثي الأبعاد!</h1>
      <p class="hero-sub">Etched يُضاعف valuation إلى 10.3 مليار دولار برقائق low-voltage inference، Meshy يُحوّل النص إلى نماذج 3D جاهزة للطباعة بـ 400 مليون دولار، Trooly يُجري مقابلات عميقة 45 دقيقة مع المستهلكين عبر voice agents، وNatural يبني طبقة مدفوعات للوكلاء الذكية بـ 30 مليون دولار. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 24 يوليو 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Etched: 300 مليون دولار وvaluation 10.3 مليار — رقائق inference منخفضة الجهد تُنافس Nvidia بسرعة «مستحيلة»!</h2>
      <p class="article-lead">كل ثانية تأخير في inference تُكلف الشركات ملايين الدولارات. Etched — ثلاثة خريجين Harvard تركوا الجامعة — بنوا رقائق مُخصّصة لـ prefill وdecode بـ low-voltage inference وcluster-scale memory. النتيجة: سرعة «dramatically» أعلى وتكلفة أقل — والسوق يُكافئها بأعلى valuation لـ Series C في تاريخ Sequoia.</p>
      <p>في 23 يوليو 2026، أعلنت <strong>Etched</strong> عن <strong>Series C بقيمة 300 مليون دولار</strong> — valuation <strong>10.3 مليار دولار</strong> — بقيادة <strong>Sequoia</strong>، مع Andreessen Horowitz وSK Hynix وJane Street وDiffusion Capital. المستثمرون السابقون: Peter Thiel وAndrej Karpathy وDylan Field وAmjad Masad.</p>
      <p>Etched <strong>ضاعفت valuation</strong> من 5 مليار في ديسمبر 2025 — بعد Series B بـ 500 مليون. الشركة أعلنت الشهر الماضي: رقائقها homegrown <strong>صُنعت بنجاح</strong>، أول أنظمة كاملة تُختبر لدى عملاء، و<strong>طلبات بقيمة مليار دولار</strong> محجوزة. الفريق: 400 موظف، data center بـ 2 megawatt، ومنشأة جديدة 80,000 قدم مربع بـ 10MW في Milpitas.</p>
      <p>السر: <strong>prefill chip</strong> يعمل بجهد أقل — حرارة أقل، transistors أكثر؛ و<strong>cluster-scale memory</strong> يربط رقائق متعددة بذاكرة مشتركة ultra-low latency للـ decode. للمبدعين العرب: consulting لـ inference optimization، دورات «AI Chip Economics»، وpartnerships مع data centers MENA — كل شركة AI production تحتاج inference أرخص.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Etched وثورة inference المتخصص؟</h3>
        <ul>
          <li><strong>Inference cost optimization consulting:</strong> قلّل تكلفة LLM inference للشركات العربية — مشروع 10000–60000 دولار.</li>
          <li><strong>Arabic AI infrastructure audits:</strong> حلّل stack inference واقترح specialized chips — 5000–25000 دولار.</li>
          <li><strong>دورات «Economics of AI Inference»:</strong> workshop للـ CTOs وplatform teams — 199–899 دولار.</li>
          <li><strong>MENA data center partnerships:</strong> وسّط بين Etched-like vendors وoperators محليين — commission 2–8%.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Etched</span>
        <span class="tag">AI Chips</span>
        <span class="tag">Low-Voltage Inference</span>
        <span class="tag">$10.3B Valuation</span>
        <span class="tag">Hardware AI</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Meshy: 400 مليون دولار وvaluation 1.5 مليار — من نص إلى نموذج 3D جاهز للطباعة في دقيقة واحدة!</h2>
      <p class="article-lead">صناعة 3D assets كانت تستغرق أسابيع وتحتاج فنانين متخصصين. Meshy — مؤسسها Ethan Hu من MIT — يقول: اكتب وصفاً، أو ارفع صورة، أو ارسم sketch — واحصل على model ثلاثي الأبعاد print-ready في ~60 ثانية بتكلفة ~دولار واحد. 12 مليون مستخدم و100 مليون model مُولَّد — والسوق يُكافئ بأكبر جولة تمويل لشركة AI 3D.</p>
      <p>في 23 يوليو 2026، أعلنت <strong>Meshy</strong> عن <strong>Series B بقيمة ~400 مليون دولار</strong> — valuation <strong>1.5 مليار دولار</strong> — بقيادة IDG Capital وMatrix Partners China وMonolith Management. Granite Asia وSequoia China وBAI Capital oversubscribed.</p>
      <p>المنصة: ARR ينمو <strong>~12× سنوياً</strong>؛ أكثر من <strong>12 مليون مستخدم</strong> و<strong>100 مليون 3D model</strong> مُولَّد. الإطلاقات الجديدة: <strong>Meshy 3D Agent</strong> — أول AI agent مُخصّص لـ 3D — success rate في slicer حتى <strong>97%</strong>؛ <strong>Auto Split</strong> لتقسيم الأجزاء بضغطة واحدة؛ <strong>Smart Topology</strong> — polygon count من 100 إلى 100,000 في ~10 ثوانٍ.</p>
      <p>الرؤية: 3D ليس endpoint — بل <strong>نقطة بداية لتجارب immersive</strong> يمكن «الخطو فيها والشعور بها». للمبدعين العرب: خدمات 3D generation للـ e-commerce، دورات «AI 3D للمبتدئين»، وagency لـ game assets وmetaverse — سوق creator economy ينفجر مع AI 3D.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meshy وثورة التوليد ثلاثي الأبعاد؟</h3>
        <ul>
          <li><strong>AI 3D asset services:</strong> أنشئ models للمتاجر والألعاب — 500–5000 دولار/مشروع.</li>
          <li><strong>Print-on-demand 3D shop:</strong> حوّل أوصاف العملاء إلى منتجات مطبوعة — هامش 30–60%.</li>
          <li><strong>دورات «من Prompt إلى 3D Print»:</strong> bootcamp للمصممين — 99–499 دولار.</li>
          <li><strong>Arabic 3D content agency:</strong> فيديوهات وvisuals 3D للعلامات التجارية — retainer 2000–15000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meshy</span>
        <span class="tag">3D Generation</span>
        <span class="tag">Meshy 3D Agent</span>
        <span class="tag">Creator Economy</span>
        <span class="tag">$1.5B Valuation</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Trooly: 20 مليون دولار — voice agent يُجري مقابلات 45 دقيقة عميقة مع المستهلكين حول العالم!</h2>
      <p class="article-lead">استطلاعات الـ 5 دقائق تعطيك surface answers. Trooly يفعل العكس: مقابلة واحدة، 45 دقيقة، follow-up engine يتكيّف مع كل إجابة — كأن senior researcher يجلس أمام المستهلك. AI-native user research — depth over volume — والسوق يُمول بـ 20 مليون seed.</p>
      <p>في 23 يوليو 2026، أطلقت <strong>Trooly</strong> من Wilmington منصة <strong>AI-native user research</strong> وفتحت <strong>public beta</strong> في North America — مدعومة بـ <strong>~20 مليون دولار seed</strong>. الشعار: <strong>Make User's Voice Heard</strong> — Ask, Find what's next.</p>
      <p>المنصة تُحسّن <strong>عمق كل مقابلة</strong> لا عددها — information density التي تحملها محادثة 45 دقيقة عندما يطرح المحاور السؤال التالي الصحيح. <strong>Multimodal voice-agent technology</strong> + global panel من المشاركين. التمويل يذهب لـ R&D على core product، بناء panel عالمي، والتوسع في شركات scaling عالمياً وindustries عالية المخاطر.</p>
      <p>لفرق product وresearch وgrowth: depth مقابلة senior researcher بـ <strong>جزء من الوقت والتكلفة</strong>. Beta متاح في North America — global rollout من trooly.ai. للمبدعين العرب: consulting لـ user research automation، Arabic voice research panels، ودورات «AI User Research للمنتجات» — كل startup يحتاج customer insights قبل burn rate.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Trooly وثورة البحث عن المستخدمين؟</h3>
        <ul>
          <li><strong>AI user research consulting:</strong> صمّم studies للشركات العربية — مشروع 3000–20000 دولار.</li>
          <li><strong>Arabic voice panel services:</strong> نظّم مقابلات Trooly-style بالعربية — 500–3000 دولار/دراسة.</li>
          <li><strong>Product insight reports:</strong> حوّل interviews إلى actionable briefs — 1500–8000 دولار.</li>
          <li><strong>دورات «AI User Research 101»:</strong> workshop لـ PMs — 149–699 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Trooly</span>
        <span class="tag">User Research</span>
        <span class="tag">Voice Agents</span>
        <span class="tag">Product Insights</span>
        <span class="tag">$20M Seed</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Natural: 30 مليون دولار — مدفوعات مُصمّمة للوكلاء الذكية تُنافس Stripe في عصر agentic commerce!</h2>
      <p class="article-lead">الوكلاء الذكية ستشتري، تبيع، وتُحوّل الأموال — لكن Stripe وPayPal بُنيت للبشر. Natural يعيد تصميم payments من الصفر: agents تدفع autonomously، تجمع funds، وتتعامل مع humans وagents أخرى. 193 يوماً من التأسيس إلى Series A — والمستثمرون من Notion وBrex وBrowserbase وForerunner يُؤمنون.</p>
      <p>في 20 يوليو 2026، أعلنت <strong>Natural</strong> من San Francisco عن <strong>Series A بقيمة 30 مليون دولار</strong> — بقيادة <strong>Kirsten Green</strong> من Forerunner — إجمالي التمويل <strong>أكثر من 40 مليون دولار</strong>. المستثمرون: Human Capital وAbstract وWischoff Ventures وAkshay Kothari (Notion) وPaul Klein IV (Browserbase) وDarragh Buckley (Increase) وArt Levy (Brex) وJake وLogan Paul (Antifund) وغيرهم.</p>
      <p>Natural يبني <strong>payments infrastructure for AI agents</strong> — ليس bolt-on على أنظمة legacy. التكامل يتيح للشركات: agents تُجري <strong>autonomous payments</strong>، تجمع funds، وتتعامل مع humans وagents. CEO <strong>Kahlil Lalji</strong> يقول: architectural decisions كافية الآن للمنافسة مع incumbents — وStripe نفسها تُسرّع redesign payments للـ agents.</p>
      <p>للمبدعين العرب: consulting لـ agentic commerce setup، integration services للـ fintech MENA، ودورات «Payments for AI Agents» — كل marketplace وSaaS سيحتاج agent payments خلال 18 شهراً. الفرصة: كن early integrator قبل أن يصبح standard.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Natural ومدفوعات الوكلاء الذكية؟</h3>
        <ul>
          <li><strong>Agentic commerce integration:</strong> اربط agents بـ payment rails — مشروع 8000–45000 دولار.</li>
          <li><strong>AI agent marketplace setup:</strong> ابنِ marketplaces حيث agents تشتري وتبيع — 15000–80000 دولار.</li>
          <li><strong>دورات «Payments for AI Agents»:</strong> bootcamp للـ fintech developers — 199–999 دولار.</li>
          <li><strong>MENA fintech consulting:</strong> ساعد banks على agent-ready payment APIs — retainer 5000–25000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Natural</span>
        <span class="tag">Agentic Commerce</span>
        <span class="tag">AI Payments</span>
        <span class="tag">Fintech</span>
        <span class="tag">$30M Series A</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 24-07-2026 -- 08-AM</p>
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
