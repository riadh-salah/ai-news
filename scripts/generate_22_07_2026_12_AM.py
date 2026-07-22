#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 22-07-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "22-07-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Natural، Fireworks AI، Chai Discovery، Block Buzz، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 22 يوليو 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من محافظ FDIC للوكلاء إلى يونيكورن بـ 17.5 مليار — الذكاء الاصطناعي يُعيد اختراع المال والعلاج والتعاون في ليلة واحدة!</h1>
      <p class="hero-sub">Natural تبني rails الدفع للوكلاء بـ 30 مليون دولار، Fireworks AI تُحقّق مليار دولار ARR بجولة 1.5 مليار، Chai Discovery تُبرمج جزيئات Lilly وPfizer بـ 400 مليون، وBlock تُطلق Buzz — workspace مفتوح حيث البشر والوكلاء يبنون معاً. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 22 يوليو 2026</span>
        <span>🕛 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Natural: 30 مليون دولار لبناء «Stripe للوكلاء» — محافظ FDIC، Vault، وPay جاهزة للاقتصاد machine-to-machine!</h2>
      <p class="article-lead">الوكيل الذي لا يستطيع الدفع… ليس وكيلاً — بل chatbot مُكلف. Natural من San Francisco يُعيد بناء البنية المالية من الصفر: ليس لإضافة زر checkout للـ AI، بل لجعل الوكلاء يتحركون ويخزّنون ويُحوّلون الأموال باستقلالية — agent-to-agent، business-to-agent، consumer-to-agent.</p>
      <p>في 21 يوليو 2026، أعلنت <strong>Natural</strong> إغلاق <strong>Series A بقيمة 30 مليون دولار</strong> بقيادة <strong>Forerunner</strong> — Kirsten Green قالت: «platform shift جديد، rails جديدة» — ليصل إجمالي التمويل إلى <strong>40 مليون دولار</strong> بعد seed بـ 9.8 مليون في سبتمبر 2025. المؤسسون: <strong>Ali Lalji</strong> (Ivella سابقاً)، <strong>Eric Wang</strong>، و<strong>Walt Leung</strong> (Nextdoor سابقاً).</p>
      <p>ستة منتجات خرجت إلى <strong>general availability</strong> فوراً: <strong>Wallets</strong> — محافظ FDIC-insured للوكلاء؛ <strong>Vault</strong> — حسابات one-way (أموال تدخل ولا تخرج إلا بpolicy)؛ <strong>Pay</strong> و<strong>Request</strong> للإرسال والتحصيل؛ <strong>Transfer</strong> بين حسابات داخلية وخارجية؛ و<strong>Connect</strong> لبناء marketplaces على Natural. Q4 2026: Charge (per-API-call billing)، Credit (خطوط ائتمان للوكلاء)، Direct (استدعاء payment rails وقت التشغيل)، وBilling (success-based).</p>
      <p>المنافسون: Stripe يُسرّع agentic commerce، وSkyfire يبني stablecoin rails — لكن Natural يدمج bank payments التقليدية + stablecoins. للمبدعين العرب في fintech وagent builders: فرصة لبناء «Natural integration layer» لـ SaaS MENA، consulting لـ agent wallets للبنوك، ودورات «Agentic Payments 101» — الاقتصاد القادم ليس human-to-human فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Natural وagentic payments؟</h3>
        <ul>
          <li><strong>Agent wallet integration:</strong> اربط SaaS أو marketplace محلي بـ Natural Wallets — مشروع 6000–28000 دولار.</li>
          <li><strong>Fintech compliance consulting:</strong> ساعد startups MENA تُصمّم Vault policies وagent spending limits — 4000–18000 دولار.</li>
          <li><strong>دورات «مدفوعات الوكلاء»:</strong> bootcamp للمطورين والـ product managers — 149–699 دولار.</li>
          <li><strong>Agent marketplace builder:</strong> استخدم Connect لبناء platform لوكلاء عربية متخصصة — retainer 2500–12000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Natural</span>
        <span class="tag">Agentic Payments</span>
        <span class="tag">Forerunner</span>
        <span class="tag">FDIC Wallets</span>
        <span class="tag">Fintech</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Fireworks AI: 1.5 مليار دولار وvaluation 17.5 مليار — 40 تريليون token يومياً و«Specialized Intelligence» تُهزم frontier models!</h2>
      <p class="article-lead">الشركات لا تريد GPT عاماً — تريد model يفهم contracts قانونيتها، code style فريقها، وsupport tickets عملائها. Fireworks — من فريق PyTorch سابقاً في Meta — يبني platform حيث 95% من tokens تأتي من models مُخصّصة على بيانات proprietary، بـ 5–10× تكلفة أقل من closed frontier equivalents.</p>
      <p>في 16 يوليو 2026، أعلنت <strong>Fireworks</strong> جولة <strong>Series D بقيمة 1.505 مليار دولار</strong> بvaluation <strong>17.5 مليار دولار</strong> — بقيادة <strong>Atreides Management</strong> و<strong>Index Ventures</strong> و<strong>TCV</strong>، مع <strong>NVIDIA</strong> وLightspeed وBessemer وMenlo وOntario Teachers' Pension Plan. ARR تجاوز <strong>مليار دولار</strong> — نمو 5× في سنة — وvolume: <strong>40+ trillion token</strong> يومياً (من 15 trillion).</p>
      <p>عملاء: <strong>Cursor</strong> (Composer model)، <strong>Harvey</strong> (legal AI)، <strong>Shopify</strong>، <strong>Uber</strong>، <strong>Revolut</strong>، <strong>Elastic</strong>، <strong>GitLab</strong>، <strong>MongoDB</strong>. CEO <strong>Lin Qiao</strong> تخطّط لمضاعفة الفريق من 200 إلى 600 بحلول نهاية 2026 — مع George Hu (Salesforce سابقاً) كـ president. SpaceX acquisition لـ Cursor ($60B) يُ diversification revenue لكن Fireworks يبقى backbone للـ specialized models.</p>
      <p>للمبدعين العرب: consulting لـ fine-tune models على Arabic legal/medical/e-commerce data، deployment على Fireworks بدلاً من OpenAI للتكلفة، ودورات «Specialized Intelligence للشركات» — open models + proprietary data = moat حقيقي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Fireworks وSpecialized Intelligence؟</h3>
        <ul>
          <li><strong>Arabic model fine-tuning:</strong> خصّص open models للقطاعات العربية (legal، medical، retail) — مشروع 8000–35000 دولار.</li>
          <li><strong>Migration consulting:</strong> انقل شركات من OpenAI API إلى Fireworks — توفير 60–80% — retainer 3000–15000 دولار/شهر.</li>
          <li><strong>دورات «Fine-tune بدون vendor lock-in»:</strong> bootcamp للـ ML engineers — 199–899 دولار.</li>
          <li><strong>Vertical AI products:</strong> ابنِ SaaS عربي على Fireworks inference — MRR 500–5000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Fireworks AI</span>
        <span class="tag">Specialized Intelligence</span>
        <span class="tag">Series D</span>
        <span class="tag">Open Models</span>
        <span class="tag">NVIDIA</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Chai Discovery: 400 مليون دولار وvaluation 3.8 مليار — Chai-3 يُبرمج جزيئات Lilly وPfizer وNovartis!</h2>
      <p class="article-lead">تصميم دواء جديد كان يستغرق سنوات ومليارات. Chai Discovery — عمرها سنتان — تقول: AI يتنبأ ويُعيد برمجة تفاعلات الجزيئات، وpartners من Big Pharma تدفع لأن Chai-3 يعمل في المختبر — ليس في PowerPoint.</p>
      <p>في يوليو 2026، أغلقت <strong>Chai Discovery</strong> من San Francisco جولة <strong>Series C بقيمة 400 مليون دولار</strong> بvaluation <strong>3.8 مليار دولار</strong> — بقيادة <strong>Index Ventures</strong> و<strong>Kleiner Perkins</strong> و<strong>Sequoia Capital</strong> و<strong>Dimension</strong>. إجمالي التمويل: <strong>600+ مليون دولار</strong> — ثالث جولة في أقل من سنة (seed 30M، A 70M، B 130M).</p>
      <p>النماذج: <strong>Chai-1</strong> (2024) → <strong>Chai-2</strong> (أغسطس 2025) → <strong>Chai-3</strong> (2026) — كل generation يتنبأ ويُ reprogram molecular interactions. deals مع <strong>Lilly</strong>، <strong>Pfizer</strong>، و<strong>Novartis</strong> — partners يستشهدون باستخدام real-world في drug discovery كسبب الاستثمار. Index وKleiner وSequoia: «leading drugmakers تستخدم Chai فعلاً».</p>
      <p>للمبدعين العرب في biotech وhealthtech: consulting لـ AI drug discovery workflows، partnership liaison مع pharma MENA، ودورات «AI للعلاج الجزيئي» — السوق $1T+ والمنطقة تستثمر heavily في life sciences (Saudi Vision 2030، UAE biotech hubs).</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Chai Discovery وAI drug design؟</h3>
        <ul>
          <li><strong>Biotech AI consulting:</strong> ساعد startups MENA تُقيّم Chai-style molecular AI — مشروع 12000–55000 دولار.</li>
          <li><strong>Pharma partnership liaison:</strong> كن bridge بين Chai وregional pharma — retainer 5000–25000 دولار/شهر.</li>
          <li><strong>دورات «AI للعلاج الجزيئي»:</strong> bootcamp للـ researchers وbiotech founders — 299–1299 دولار.</li>
          <li><strong>Regional biotech accelerator:</strong> قدّم Chai integration كـ value-add لـ portfolio — equity + fees.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Chai Discovery</span>
        <span class="tag">Chai-3</span>
        <span class="tag">Drug Discovery</span>
        <span class="tag">Big Pharma</span>
        <span class="tag">Series C</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Block Buzz: workspace مفتوح حيث البشر والوكلاء يبنون معاً — Apache 2.0، Nostr، وmodel-agnostic من Day One!</h2>
      <p class="article-lead">معظم أدوات AI تعامل الوكيل كـ assistant ينتظر أوامر. Block (Square/Cash App) تقول: الوكيل teammate — له identity cryptographique، permissions، ويُ review code ويشغّل automations بجانب البشر في workspace مشترك.</p>
      <p>في 21 يوليو 2026، أطلقت <strong>Block</strong> <strong>Buzz</strong> — منصة collaboration مفتوحة المصدر (<strong>Apache 2.0</strong>) حيث humans وAI agents يعملون في shared workspace. متاح على <strong>buzz.xyz</strong> و<strong>github.com/block/buzz</strong> — self-host أو Block-hosted community.</p>
      <p>Buzz <strong>model-agnostic</strong> و<strong>agent-agnostic</strong>: Claude Code، Codex، goose، أو agent مخصّص — الـ workspace لا يُحدّد ما خلف الوكيل. Built on <strong>Nostr protocol</strong> — decentralized identity. Git integration مبكر: vision حيث open source communities تستضيف projects، تناقش ideas، تُ review changes، وتعمل مع agents تكتب/test/maintain code — كل ذلك في مكان واحد.</p>
      <p>للمبدعين العرب: deploy Buzz self-hosted للفرق التقنية، build Arabic-speaking agents على Buzz، consulting لـ «human+agent workspace» للشركات، ودورات «Collaborative AI Teams» — future of work ليس human vs agent، بل human <em>with</em> agent.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Block Buzz وcollaborative agents؟</h3>
        <ul>
          <li><strong>Buzz self-hosted deployment:</strong> نصّب واضبط Buzz للشركات والـ dev teams MENA — مشروع 5000–22000 دولار.</li>
          <li><strong>Custom Arabic agents:</strong> ابنِ agents متخصصة (legal، code review، content) على Buzz — 3000–15000 دولار/agent.</li>
          <li><strong>دورات «فرق AI التعاونية»:</strong> workshop للـ engineering managers — 199–799 دولار.</li>
          <li><strong>Managed Buzz communities:</strong> قدّم hosted workspace + agent maintenance — retainer 2000–10000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Block Buzz</span>
        <span class="tag">Open Source</span>
        <span class="tag">Nostr</span>
        <span class="tag">Human+Agent</span>
        <span class="tag">Collaboration</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 22-07-2026 -- 12-AM</p>
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
