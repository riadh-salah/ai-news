#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 26-07-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "26-07-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Together AI، CopilotKit، Browserbase Agents، Harvey، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 26 يوليو 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من سحابة مفتوحة بـ 8.3 مليار دولار إلى وكلاء قانونيين بـ 11 مليار — أربع ثورات تُعيد رسم خريطة الثروة في AI!</h1>
      <p class="hero-sub">Together AI تجمع 800 مليون دولار لتُ democratize النماذج المفتوحة، CopilotKit يبني طبقة الواجهة للوكلاء بـ 27 مليون دولار وبروتوكول AG-UI، Browserbase يُطلق وكلاء متصفح بنداء API واحد فوق 35 مليون جلسة شهرياً، وHarvey تصل إلى 11 مليار دولار كإمبراطورية AI القانونية. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 26 يوليو 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Together AI: 800 مليون دولار — سحابة AI مفتوحة بـ 8.3 مليار دولار و1.15 مليار حجوزات!</h2>
      <p class="article-lead">النماذج المغلقة تُكلّف. Together AI يُثبت العكس: inference على DeepSeek وKimi وMiniMax بـ 6 إلى 60 ضعفاً أرخص — مع أداء يُنافس GPT وClaude. 800 مليون دولار Series C، valuation 8.3 مليار دولار، و500 ميجاواط compute capacity. Cursor وCognition وDecagon يبنون عليها — والسؤال: من يملك طبقة inference المفتوحة؟</p>
      <p>في 1 يوليو 2026، أعلنت <strong>Together AI</strong> عن <strong>Series C بقيمة 800 مليون دولار</strong> بقيادة <strong>Aramco Ventures</strong> — valuation <strong>8.3 مليار دولار</strong> (من 3.3 مليار في فبراير 2025). المشاركون: <strong>NVIDIA</strong>، <strong>Vista Equity Partners</strong>، <strong>General Catalyst</strong>، <strong>Emergence Capital</strong>، <strong>March Capital</strong>، <strong>Pegatron</strong>، <strong>S Ventures</strong> (SentinelOne)، <strong>Salesforce Ventures</strong>، و<strong>Lux Capital</strong>.</p>
      <p>الفلسفة: <strong>AI Native Cloud</strong> — لا foundation model proprietary، بل infrastructure لتشغيل open-source models بـ production scale. CEO <strong>Vipul Ved Prakash</strong> (مؤسس Cloudmark، بيعته لـ Proofpoint): «مستقبل AI لن يُملكه عدد قليل — بل ملايين المطورين والشركات، والنماذج المفتوحة تجعل ذلك ممكناً». Annual bookings تجاوزت <strong>1.15 مليار دولار</strong> — أكثر من مليون مطوّر على المنصة.</p>
      <p>المنصة تُقدّم: <strong>inference</strong>، <strong>training</strong>، <strong>reinforcement learning</strong>، و<strong>GPU clusters</strong> مُحسّنة. الخطة: توسيع compute capacity <strong>50 ضعفاً</strong> خلال 5 سنوات. TechCrunch وصف Together كـ «neocloud» — competitor لـ CoreWeave وLambda — لكن بـ thesis مفتوح المصدر. للمبدعين العرب: consulting لـ cost optimization، deployment لـ Arabic LLMs، وreseller/agency لـ MENA enterprises تُ preffer open models للـ compliance والتكلفة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Together AI وثورة inference المفتوح؟</h3>
        <ul>
          <li><strong>Open-model deployment:</strong> نفّذ inference pipelines للشركات — 5000–40000 دولار/مشروع.</li>
          <li><strong>Cost optimization consulting:</strong> قلّل فاتورة AI بـ 60× — retainer 2000–12000 دولار/شهر.</li>
          <li><strong>Arabic LLM hosting:</strong> شغّل نماذج عربية fine-tuned على Together — 3000–25000 دولار/مشروع.</li>
          <li><strong>دورات «Open-Source AI at Scale»:</strong> bootcamp للمطورين — 149–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Together AI</span>
        <span class="tag">Open Source</span>
        <span class="tag">Neocloud</span>
        <span class="tag">$8.3B Valuation</span>
        <span class="tag">Inference</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>CopilotKit: 27 مليون دولار — بروتوكول AG-UI يُصبح «طبقة الواجهة» لعصر الوكلاء!</h2>
      <p class="article-lead">الوكيل بدون واجهة = black box. CopilotKit يبني AG-UI — open standard يربط agents بـ React apps: streaming chat، front-end tool calls، state sharing، وhuman-in-the-loop. Google وMicrosoft وAmazon وOracle تتبنّاه. 27 مليون دولار Series A — ونصف Fortune 500 يستخدم أدواتهم.</p>
      <p>في 5 مايو 2026، أعلنت <strong>CopilotKit</strong> من Seattle عن <strong>Series A بقيمة 27 مليون دولار</strong> (20 مليون جديد + 7 مليون seed) بقيادة <strong>Glilot Capital</strong> و<strong>NFX</strong> و<strong>SignalFire</strong>. المؤسسان: الأخوان <strong>Atai Barkai</strong> و<strong>Uli Barkai</strong> — roots في Techstars Seattle. الشركة ~25 موظفاً — adoption عضويّة قبل أي pitch deck.</p>
      <p>المنتج: <strong>AG-UI protocol</strong> — lightweight، event-based، يعمل مع LangGraph وMastra وPydanticAI وAgno. يُكمّل MCP وA2A. Features: streaming responses، shared state بين frontend وagent، front-end tool calls. <strong>Enterprise Intelligence Platform</strong>: threads دائمة، persistence عبر devices، admin console، self-hosted Kubernetes — للشركات التي تريد CopilotKit كـ conversation layer.</p>
      <p>TechCrunch وصف CopilotKit كـ «vendor-neutral alternative» لـ Vercel AI SDK وOpenAI Apps SDK. Glilot: «timing deliberate — agentic era يحتاج UI layer جديد». للمبدعين Arabs: build copilots داخل SaaS عربية، consulting لـ AG-UI integration، ودورات «Agent UI for React» — كل product team يبني agents يحتاج هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من CopilotKit وطبقة واجهة الوكلاء؟</h3>
        <ul>
          <li><strong>Copilot integration:</strong> أدمج AG-UI في SaaS عملاء — 6000–35000 دولار/مشروع.</li>
          <li><strong>Arabic copilot products:</strong> ابنِ copilots عربية لـ HR، legal، e-commerce — SaaS 29–299 دولار/شهر.</li>
          <li><strong>Enterprise Intelligence setup:</strong> self-hosted deployment — 10000–50000 دولار.</li>
          <li><strong>دورات «Agent UI with CopilotKit»:</strong> workshop للفرق — 199–899 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">CopilotKit</span>
        <span class="tag">AG-UI</span>
        <span class="tag">Agent Frontend</span>
        <span class="tag">Glilot Capital</span>
        <span class="tag">Series A</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Browserbase Agents: نداء API واحد — وكيل متصفح يُتجول في مئات المواقع ويُعيد بيانات منظّمة!</h2>
      <p class="article-lead">«سكربت لكل موقع» لا يتوسّع. «وكيل واحد» يتوسّع. Browserbase — خلف 35 مليون+ جلسة متصفح شهرياً — يُطلق Agents: prompt بلغة طبيعية، API call واحد، ووكيل يُتجول عبر مئات portals ويُعيد structured data. بدون infrastructure، بدون selectors، بدون scripts.</p>
      <p>في 30 يونيو 2026، أعلنت <strong>Browserbase</strong> عن <strong>Browserbase Agents</strong> — managed browser agent يُنشأ من natural-language prompt ويُشغَّل عبر <strong>single API call</strong>. المؤسس <strong>Paul Klein IV</strong> (pk_iv) يبني منذ Series B (40 مليون دولار، يونيو 2025، valuation ~300 مليون) thesis: «real browser reliable enough for production AI».</p>
      <p>المنصة: <strong>real browsers</strong> مع logged-in profiles وproxies وlive view. <strong>Sandboxed workspace</strong> per agent — upload files، get files back، reuse environments. <strong>Conversations that continue</strong> — follow-up runs مع full context. Built on <strong>Stagehand</strong> (scripts + AI agents hybrid) و<strong>Director</strong> (natural language للـ business users). Partners: Julius (browser agent مجاني أسبوعاً)، ViDA (BrowserBC open-source).</p>
      <p>RuntimeWire: Browserbase يتنافس في crowded layer — لكن managed agent يُ elevate product فوق raw browser sessions. Build vs buy blog: building browser infra = $220K+/year senior engineers + SOC 2 + pentest — Browserbase يُ sell «buy» للـ POC والproduction. للمبدعين Arabs: web scraping agents للـ e-commerce وgovernment portals، RPA consulting، وproducts على structured web data — MENA يحتاج automation للـ fragmented Arabic web.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Browserbase Agents وأتمتة الويب؟</h3>
        <ul>
          <li><strong>Web data agents:</strong> ابنِ agents لجمع أسعار ومناقصات — 4000–30000 دولار/مشروع.</li>
          <li><strong>Browser automation agency:</strong> RPA للـ SMBs عربية — retainer 1500–10000 دولار/شهر.</li>
          <li><strong>Government portal bots:</strong> أتمتة إجراءات حكومية — 8000–50000 دولار/عقد.</li>
          <li><strong>دورات «Browser Agents for Business»:</strong> bootcamp — 149–699 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Browserbase</span>
        <span class="tag">Browser Agents</span>
        <span class="tag">Web Automation</span>
        <span class="tag">Stagehand</span>
        <span class="tag">35M Sessions</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Harvey: 200 مليون دولار — 11 مليار valuation و100,000 محامٍ يثقون بـ AI القانوني!</h2>
      <p class="article-lead">OpenAI وAnthropic يتوسّعان — لكن Harvey تقول: «لدينا كلمة». 200 مليون دولار fresh capital، valuation 11 مليار دولار (من 8 مليار في ديسمبر)، و100,000+ محامٍ في 1,300 مؤسسة. Contract analysis، compliance، due diligence، litigation — كلها agents تُنجز مهاماً مستقلة. Vertical AI يفوز.</p>
      <p>في 25 مارس 2026، أعلنت <strong>Harvey</strong> عن <strong>200 مليون دولار</strong> بvaluation <strong>11 مليار دولار</strong> — بقيادة <strong>GIC</strong> (Singapore) و<strong>Sequoia</strong> (الجولة الثالثة التي يقودها Sequoia — «ultimate sign of conviction» حسب Pat Grady). المؤسسان: <strong>Winston Weinberg</strong> (CEO، ex-lawyer) و<strong>Gabe Pereyra</strong> (ex-Google DeepMind وMeta). بدأوا بتجربة GPT-3 قبل ChatGPT.</p>
      <p>المنتجات: AI tools لـ <strong>legal وprofessional services</strong> — contract analysis، compliance، due diligence، litigation support. <strong>AI agents</strong> تُكمل مهاماً autonomously. Expansion: embedded legal engineering teams عالمياً. CNBC: Harvey يُثبت أن AI startups في industries متخصصة تحصل traction حتى مع توسّع OpenAI وAnthropic — depth beats breadth.</p>
      <p>Winston Weinberg angel في Prime Intellect — ecosystem يتشابك. للمبدعين Arabs: Harvey-style products للـ Sharia compliance وArabic contract review، legal AI consulting للمكاتب الخليجية، ودورات «Legal AI for MENA» — كل law firm في دبي والرياض يبحث عن AI — وHarvey يُ prove أن premium vertical AI = billions.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Harvey وثورة AI القانوني العمودي؟</h3>
        <ul>
          <li><strong>Arabic legal AI:</strong> ابنِ contract review للقانون العربي — SaaS 500–5000 دولار/شهر.</li>
          <li><strong>Sharia compliance agents:</strong> due diligence للـ Islamic finance — 15000–80000 دولار/مشروع.</li>
          <li><strong>Law firm AI consulting:</strong> نفّذ Harvey-style workflows — 10000–60000 دولار.</li>
          <li><strong>دورات «Legal AI for Professionals»:</strong> certification — 299–1499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Harvey</span>
        <span class="tag">Legal AI</span>
        <span class="tag">Vertical AI</span>
        <span class="tag">Sequoia</span>
        <span class="tag">$11B Valuation</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 26-07-2026 -- 04-PM</p>
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
