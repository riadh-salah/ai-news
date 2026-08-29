#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-08-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Skydive، PageIndex، OpenTag، Aramb، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من زميل سحابي يُوظّف وكلاء حقيقيين إلى RAG بلا vectors يُفكّر كالبشر، ومن coworker يعيش في Slack إلى نظام تشغيل يُطلق ويُربح من الوكلاء في 20 دقيقة — أربع ثورات تُعيد تعريف العمل والبيانات والتعاون والاقتصاد في 29 أغسطس 2026!</h1>
      <p class="hero-sub">Skydive يُوظّف وكلاء سحابيين بكمبيوتر خاص يتعلّمون ويتعاونون عبر أدواتك، PageIndex يُحلّل المستندات الطويلة بـ 98.7% دقة دون vector DB، OpenTag يعيش في Slack وTeams ويُحدّث wiki الشركة تلقائياً، وAramb يُجمّع runtime وmemory وbrowser وbilling في API واحد لبناء وإطلاق وتحقيق الدخل من الوكلاء في 20 دقيقة. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 29 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Skydive: «وظّف» زميلاً سحابياً في دقائق — وكلاء بكمبيوتر خاص يتعلّمون ويتعاونون ويُنجزون العمل عبر Slack وiMessage والويب!</h2>
      <p class="article-lead">«Chatbots تُجيب — Skydive يُنجز». في 27 أغسطس 2026، احتل <strong>Skydive</strong> المركز الأول Product of the Day على Product Hunt بـ 410 upvote — <strong>منصة وكلاء سحابيين</strong> يُوظّفون كزملاء حقيقيين: تُصف النتيجة المطلوبة، والوكيل يُنشأ في دقائق ويعمل عبر أدواتك دون كود أو prompt engineering.</p>
      <p>المشكلة التي حلّتها: الجميع يملك نفس نماذج AI — لكن chatbots تُجيب وتنسى، وworkflow builders تتطلب تصميم كل خطوة. Skydive يُقدّم الجيل الثالث: وكلاء بـ <strong>كمبيوتر سحابي خاص</strong> ينقر ويكتب ويسجّل الدخول ويُكمل المهام من البداية للنهاية، يعملون في Slack والبريد وiMessage والويب والـ terminal، ويتعاونون ويُمرّرون العمل تلقائياً بينهم.</p>
      <p>القدرات الأساسية: إنشاء وكيل في دقائق بوصف النتيجة فقط، كمبيوتر سحابي لكل وكيل (مواقع وتطبيقات وملفات)، ذاكرة دائمة تتحسّن مع كل تصحيح، automation لا ينام (monitoring وaction على مدار الساعة)، تكامل Slack وemail وiMessage وdesktop، وكلاء متخصصون يتشاركون السياق — مثل ChargeKnight لـ Stripe disputes وAlfie لـ affiliate fraud. Product Hunt #1 يوم 27 أغسطس بـ 410 upvote و105 تعليقاً.</p>
      <p>للمبدعين العرب: كل founder وoperator وagency في MENA يُريد فريقاً دون payroll — Skydive agent setup packages وArabic workflow agents وmanaged cloud coworker retainers فرصة premium B2B. «Cloud agent coworkers» vertical ينمو مع agent adoption — Skydive تُكافئ teams التي تُفوّض مسؤوليات حقيقية لا مهام chat.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Skydive وثورة الزملاء السحابيين؟</h3>
        <ul>
          <li><strong>Cloud agent setup packages:</strong> إعداد وكلاء Skydive مخصصين للعملاء — 2000–20000 دولار/عميل.</li>
          <li><strong>Arabic workflow agent design:</strong> بناء وكلاء للعمليات المتكررة بالعربية — 1000–10000 دولار/وكيل.</li>
          <li><strong>Managed cloud coworker retainers:</strong> صيانة وتحسين أسطول وكلاء شهرياً — 2500–25000 دولار/شهر.</li>
          <li><strong>دورات «Hire Your First Cloud Agent with Skydive»:</strong> bootcamp للمؤسسين — 59–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Skydive</span>
        <span class="tag">Cloud Agents</span>
        <span class="tag">Agent Coworkers</span>
        <span class="tag">Multi-Agent</span>
        <span class="tag">Product Hunt #1</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>PageIndex: RAG بلا vectors يُفكّر كالبشر — 98.7% دقة على FinanceBench مع مراجع صفحات دقيقة وقابلة للتدقيق!</h2>
      <p class="article-lead">«التشابه الدلالي ≠ الصلة — الصلة تحتاج تفكيراً». في 29 أغسطس 2026، يتصدر <strong>PageIndex</strong> المشهد كـ <strong>vectorless reasoning-based RAG engine</strong> — يُحوّل المستندات الطويلة إلى شجرة هرمية ويُجري LLM reasoning عليها كما يقرأ الخبير البشري، بـ <strong>98.7% دقة</strong> على FinanceBench دون embeddings أو chunking أو vector DB.</p>
      <p>المشكلة التي حلّتها: vector RAG يُرجع ما هو «مشابه» لا ما هو «ذو صلة» — ويفشل في التقارير المالية والعقود القانونية والوثائق التنظيمية التي تتطلب فهماً سياقياً وmulti-step reasoning. PageIndex يستبدل vector index بـ <strong>hierarchical tree index</strong>: يُولّد شجرة للمستند، ثم يبحث فيها agentically بـ LLM reasoning — كل إجابة تحمل مراجع صفحات/أقسام دقيقة قابلة للتدقيق.</p>
      <p>القدرات الأساسية: PageIndex SDK (`pip install pageindex`) مع local mode وcloud mode، PageIndex Flash لتوليد الشجرة في ثوانٍ، MCP server وREST API وPython SDK، دعم PDFs طويلة (تقارير مالية، SEC filings، عقود، وثائق طبية)، File System لملايين المستندات (cloud)، وProduct Hunt #1 يوم 29 أغسطس. مفتوح المصدر على GitHub مع 50%+ accuracy gain على FinanceBench.</p>
      <p>للمبدعين العرب: كل legal tech وfintech وcompliance consultant في MENA يُعاني من RAG غير دقيق — PageIndex integration packages وArabic document analysis workflows وmanaged document AI retainers فرصة enterprise premium. «Reasoning-based document AI» vertical ينمو مع regulatory demand — PageIndex تُكافئ domain-specific accuracy.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من PageIndex وثورة RAG بالتفكير؟</h3>
        <ul>
          <li><strong>Document AI integration packages:</strong> ربط PageIndex بأنظمة العملاء — 3000–30000 دولار/مشروع.</li>
          <li><strong>Arabic compliance analysis workflows:</strong> pipelines تحليل وثائق تنظيمية بالعربية — 1500–15000 دولار/workflow.</li>
          <li><strong>Managed document intelligence retainers:</strong> فهرسة وتحليل مستندات شهرياً — 2000–20000 دولار/شهر.</li>
          <li><strong>دورات «Build Auditable Document AI with PageIndex»:</strong> bootcamp للمحامين والمحللين — 79–499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">PageIndex</span>
        <span class="tag">Vectorless RAG</span>
        <span class="tag">Reasoning Retrieval</span>
        <span class="tag">FinanceBench</span>
        <span class="tag">Document AI</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>OpenTag: زميل AI يعيش في Slack وTeams — يُنجز العمل ويُحدّث wiki الشركة تلقائياً وmodel-agnostic يتحسّن مع كل نموذج جديد!</h2>
      <p class="article-lead">«Claude Tag واجهة صحيحة — OpenTag يجعلها multiplayer وmodel-agnostic». في 28 أغسطس 2026، أطلقت <strong>OpenTag</strong> من Y Combinator (Open Curiosity) كـ <strong>AI coworker</strong> يعيش في Slack وMicrosoft Teams — ليس chatbot في tab منفصل، بل زميل بـ <strong>machine sandboxed</strong> خاص يتعلّم كيف تُدار شركتك ويُنجز عملاً حقيقياً في الـ thread.</p>
      <p>المشكلة التي حلّتها: فرق distributed تُضيّع ساعات في follow-ups وتقارير وtriage — وwiki الشركة stale دائماً. OpenTag يُغيّر المعادلة: tag في channel، أعطِ مهمة، النتيجة تظهر في thread مع sources. يرى workflows متكررة ويُقترح automation. يكتب wiki «كيف تُدار الشركة فعلاً» من قرارات chat — company brain يتقوّى مع الوقت. model-agnostic: عندما يُطلق نموذج أفضل، زميلك يتحسّن فوراً.</p>
      <p>القدرات الأساسية: setup في دقيقتين (invite + connect tools + first job)، تكامل Stripe وGitHub وZendesk وNotion وdatabase و200+ أداة، approval gates للإجراءات الحساسة، invited channels only (لا يقرأ workspace كاملاً)، recurring reports وfollow-ups وtriage operations، seat واحد per workspace للفريق كاملاً، خصم 50% لشهرين للإطلاق.</p>
      <p>للمبدعين العرب: كل remote team وSaaS وagency في MENA يعمل في Slack — OpenTag setup packages وArabic workflow automation وmanaged AI coworker retainers فرصة productivity premium. «Ambient AI coworker in chat» vertical ينمو مع distributed work — OpenTag تُكافئ teams التي تُفوّض multi-step work.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenTag وثورة زميل AI في الدردشة؟</h3>
        <ul>
          <li><strong>OpenTag workspace setup:</strong> إعداد coworker مع tools وworkflows — 1500–15000 دولار/workspace.</li>
          <li><strong>Arabic automation playbook design:</strong> سيناريوهات تقارير ومتابعات بالعربية — 800–8000 دولار/playbook.</li>
          <li><strong>Managed AI coworker retainers:</strong> صيانة wiki وautomation شهرياً — 2000–20000 دولار/شهر.</li>
          <li><strong>دورات «Deploy Your AI Coworker with OpenTag»:</strong> bootcamp لفرق remote — 49–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenTag</span>
        <span class="tag">AI Coworker</span>
        <span class="tag">Slack AI</span>
        <span class="tag">Model Agnostic</span>
        <span class="tag">Company Wiki</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Aramb: نظام تشغيل الوكلاء — ابنِ وأطلق وحقّق الدخل في 20 دقيقة بـ API واحد لـ runtime وmemory وbrowser وbilling!</h2>
      <p class="article-lead">«إطلاق وكيل واحد كان يعني 9 منتجات و9 فواتير — Aramb يُجمّعها في سطر واحد». في 28 أغسطس 2026، أطلقت <strong>Aramb</strong> كـ <strong>operating system for AI agents</strong> — `npm install @aramb-ai/sdk` ووكيلك جاهز للإطلاق والتحقيق من الدخل في 20 دقيقة: runtime وmemory وbrowser infrastructure وtools وmodels وusage-based billing في API واحد.</p>
      <p>المشكلة التي حلّتها: builders يُضيّعون أسابيع في integration — model provider + voice API + browser vendor + sandbox + vector DB + integrations + metering + Stripe + Redis. Aramb يُحوّل كل ذلك إلى primitives: models من أي provider مع routing حسب السعر والlatency، billing جاهز (Stripe/Paddle/credits)، browser وsandbox مدمجان، memory وtools موحّدة — سطر واحد بدلاً من 9 SDKs.</p>
      <p>القدرات الأساسية: SDK واحد (`@aramb-ai/sdk`) للبناء والإطلاق، usage-based billing مع credit pools للفرق، model routing agnostic، browser infrastructure مدمجة، private beta مع أول 500 مطوّر في Studio مجاناً، Product Hunt #7 يوم 28 أغسطس بـ 121 upvote. «Hire AI agents or build your own» — marketplace + builder platform.</p>
      <p>للمبدعين العرب: كل indie hacker وAI agency وSaaS builder في MENA يُريد launch agent product بسرعة — Aramb agent launch packages وArabic monetization playbooks وmanaged agent platform retainers فرصة infrastructure premium. «Agent OS with built-in billing» vertical ينمو مع agent economy — Aramb تُكافئ builders الذين يريدون revenue من اليوم الأول.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Aramb وثورة نظام تشغيل الوكلاء؟</h3>
        <ul>
          <li><strong>Agent product launch packages:</strong> بناء وإطلاق agent product على Aramb — 3000–30000 دولار/منتج.</li>
          <li><strong>Arabic agent monetization playbooks:</strong> نماذج pricing وcredit pools للسوق العربي — 1000–10000 دولار/playbook.</li>
          <li><strong>Managed agent platform retainers:</strong> صيانة runtime وbilling شهرياً — 2500–25000 دولار/شهر.</li>
          <li><strong>دورات «Launch Your AI Agent Business with Aramb»:</strong> bootcamp للمطوّرين — 69–449 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Aramb</span>
        <span class="tag">Agent OS</span>
        <span class="tag">Agent Monetization</span>
        <span class="tag">Usage Billing</span>
        <span class="tag">Agent SDK</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-08-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-08-2026 -- 12-AM.html">
          📰 29 أغسطس 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Skydive · PageIndex · OpenTag · Aramb</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-08-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    update_index()


if __name__ == "__main__":
    main()
