#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-08-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-08-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Enter Pro، Lenz، Traccia، Caddi، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 أغسطس 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من منصة AI-native تُطلق تطبيقات ووكلاء ومدفوعات في workspace واحد، إلى API يُفحص الحقائق بـ 8 نماذج، ومن control plane محايد يُحكم الوكلاء في الإنتاج إلى وكيل يبني وكلاء من screenshare واحد — أربع ثورات تُعيد تعريف البناء والمصداقية والحوكمة والأتمتة في 29 أغسطس 2026!</h1>
      <p class="hero-sub">Enter Pro يحوّل الفكرة إلى منتج حقيقي بقواعد بيانات ومصادقة واستضافة ومدفوعات مدمجة، Lenz يستخرج الادعاءات ويُجري مناظرة multi-model ويُعيد حكماً موثّقاً عبر API وMCP، Traccia يُراقب ويُقيّم ويُحكم الوكلاء المستقلّين بـ OpenTelemetry دون vendor lock-in، وCaddi يُحوّل narrated screenshare إلى وكيل إنتاجي يُنفّذ back-office work بمنطق AI وتنفيذ حتمي. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 29 أغسطس 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Enter Pro: المنصة AI-native التي تُطلق تطبيقات ومواقع ووكلاء مخصّصين — من الفكرة إلى الإنتاج في workspace واحد!</h2>
      <p class="article-lead">«بناء ما يُشغّل الأعمال يحتاج أكثر من كود — يحتاج منصة كاملة». في 27 أغسطس 2026، احتل <strong>Enter Pro</strong> المركز الثاني على Product Hunt بـ 385 upvote — <strong>منصة AI-native</strong> من Converge تحوّل الفكرة إلى منتج عامل: تخطيط، بناء، معاينة، إطلاق، وتوسّع لتطبيقات ومواقع ووكلاء AI مخصّصين في مساحة عمل متصلة واحدة.</p>
      <p>المشكلة التي حلّتها: المطوّرون والفرق الناشئة تُضيّع أسابيع في تجميع البنية التحتية — نماذج، قواعد بيانات، مصادقة، استضافة، مدفوعات، تحليلات، وترجمة. Enter Pro يُدمج كل ذلك: models وdatabases وauthentication وhosting وpayments وanalytics وlocalization مدمجة — لتُطلق software مبني لأعمال حقيقية وليس prototypes فقط.</p>
      <p>القدرات الأساسية: workspace متصل من التخطيط إلى التوسّع، custom AI agents داخل نفس المنصة، بنية تحتية جاهزة للإنتاج، تكامل مدفوعات وتحليلات، دعم localization للأسواق العالمية. Product Hunt #2 يوم 27 أغسطس، hunted by Rohan Chaubey، متاح على enter.converge.ai — يتنافس في Developer Tools وAI وNo-Code بـ 1M+ followers على Product Hunt.</p>
      <p>للمبدعين العرب: كل founder وagency وSaaS builder في MENA يُريد إطلاق منتج بسرعة دون DevOps — Enter Pro setup packages وArabic app/agent launch workflows وmanaged platform retainers فرصة premium. «AI-native full-stack platform» vertical ينمو — Enter Pro تُكافئ builders الذين يُطلقون revenue-generating products وليس demos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Enter Pro وثورة المنصات AI-native؟</h3>
        <ul>
          <li><strong>Enter Pro launch packages:</strong> بناء وإطلاق تطبيق أو وكيل كامل — 2500–25000 دولار/مشروع.</li>
          <li><strong>Arabic SaaS on Enter Pro:</strong> تطبيقات ووكلاء بالعربية مع payments وlocalization — 3000–30000 دولار/منتج.</li>
          <li><strong>Managed platform retainers:</strong> صيانة وتوسّع وagents شهرياً — 2000–20000 دولار/شهر.</li>
          <li><strong>دورات «Ship Revenue Apps with Enter Pro»:</strong> bootcamp للمؤسسين — 69–449 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Enter Pro</span>
        <span class="tag">AI-Native Platform</span>
        <span class="tag">No-Code</span>
        <span class="tag">Full-Stack</span>
        <span class="tag">Product Hunt</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Lenz: API فحص الحقائق multi-model — 63% من الادعاءات تُختلف عليها frontier models، وLenz يُعيد حكماً موثّقاً بـ 8 نماذج!</h2>
      <p class="article-lead">«معظم أدوات AI تُعطيك تخمين نموذج واحد من الذاكرة — Lenz يضمن أن blind spots نموذج واحد لا تُحدّد النتيجة». <strong>Lenz</strong> هو <strong>AI fact-checking API</strong> للمنتجات التي لا تستطيع تحمّل hallucinations — يستخرج claims قابلة للتحقق من أي نص، ثم يفحص كل claim: بحث في مصادر مستقلة، multi-model debate، وتوجيه عبر review panel — يُعيد verdict مُقيّماً مع كل مصدر وحجة وخطوة مرئية.</p>
      <p>المشكلة التي حلّتها: عندما وُضعت 1000 claim حقيقية أمام frontier models، اختلفت على 63% منها — أي تقريباً claimين من كل ثلاثة. أي نموذج منها قد يكون الذي تُطلقه. Lenz هو الفحص الذي يُوضع أمام pipeline: أرسل claim، استلم verdict موثّقاً وscore وcitations من 8 نماذج دفعة واحدة — pipeline ينشر أو يُوقف أو يُصعّد دون إيقاظ أحد.</p>
      <p>القدرات الأساسية: API وMCP جاهزان للتكامل، استخراج claims تلقائياً، multi-model debate مع review panel، scored verdict مع مصادر وarguments وsteps مرئية، trial مجاني على lenz.io/ph. Product Hunt يوم 27 أغسطس بـ 254 upvote — ideal لـ legal tech وjournalism وhealthcare وenterprise AI pipelines.</p>
      <p>للمبدعين العرب: كل media platform وlegal SaaS وhealth AI في MENA يحتاج fact-checking قبل النشر — Lenz integration packages وArabic claim verification workflows وmanaged truth-layer retainers فرصة compliance premium. «Trust layer for AI output» vertical ينمو — Lenz تُكافئ products التي لا تستطيع afford hallucinations.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lenz وثورة فحص الحقائق؟</h3>
        <ul>
          <li><strong>Lenz pipeline integration:</strong> ربط fact-checking بـ AI workflows — 1500–15000 دولار/مشروع.</li>
          <li><strong>Arabic claim verification workflows:</strong> pipelines تحقق بالعربية للإعلام والقانون — 2000–20000 دولار/workflow.</li>
          <li><strong>Managed truth-layer retainers:</strong> مراقبة وtuning شهرياً — 2500–25000 دولار/شهر.</li>
          <li><strong>دورات «Build Trustworthy AI with Lenz»:</strong> bootcamp للمطوّرين — 49–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lenz</span>
        <span class="tag">Fact-Checking API</span>
        <span class="tag">Multi-Model Debate</span>
        <span class="tag">AI Trust</span>
        <span class="tag">MCP</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Traccia: control plane محايد للوكلاء — observe وevaluate وgovern وaudit trail عبر OpenTelemetry دون vendor lock-in!</h2>
      <p class="article-lead">«الوكلاء في الإنتاج يحتاجون طبقة تحكم — لا observability bolted-on». <strong>Traccia</strong> هو <strong>vendor-neutral AI Agent Control Plane</strong> للفرق التي تشغّل autonomous agents في production — يُراقب سلوك الوكيل، يُقيّم الأداء، يُحكم الإجراءات بـ policies وruntime controls، ويحافظ على audit trail لما حدث.</p>
      <p>المشكلة التي حلّتها: كل vendor يُقدّم observability خاصة — teams عالقة في lock-in بينما agents تتعدّد عبر models وframeworks. Traccia مبني بـ open developer-first SDK وOpenTelemetry — يعمل عبر models وframeworks وobservability stacks موجودة. eval path كامل: prompts → datasets → scorers → experiments قبل promote. runtime governance: policies + evidence حتى «observe» لا يكون نهاية القصة.</p>
      <p>القدرات الأساسية: open-source SDK (Python وNode)، full traces عبر models/agent frameworks، eval pipeline قبل production promote، runtime policies مع evidence، OpenTelemetry-native integration. Product Hunt #6 يوم 27 أغسطس بـ 192 upvote، hunted by Vijay Poudel — متاح على traccia.ai.</p>
      <p>للمبدعين العرب: كل enterprise وAI agency وregulated industry في MENA يُطلق agents ويحتاج governance — Traccia deployment packages وArabic agent policy design وmanaged control plane retainers فرصة infrastructure premium. «Agent governance without lock-in» vertical ينمو — Traccia تُكافئ teams التي تُشغّل agents في production بمسؤولية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Traccia وثورة حوكمة الوكلاء؟</h3>
        <ul>
          <li><strong>Traccia deployment packages:</strong> إعداد control plane وpolicies — 3000–30000 دولار/مشروع.</li>
          <li><strong>Arabic agent policy design:</strong> تصميم policies وeval datasets بالعربية — 2000–18000 دولار/مشروع.</li>
          <li><strong>Managed control plane retainers:</strong> مراقبة وgovernance شهرياً — 3500–35000 دولار/شهر.</li>
          <li><strong>دورات «Govern Production Agents with Traccia»:</strong> bootcamp لفرق DevOps — 79–499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Traccia</span>
        <span class="tag">Agent Control Plane</span>
        <span class="tag">OpenTelemetry</span>
        <span class="tag">Agent Governance</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Caddi: وكيل يبني وكلاء — screenshare مُ narrated واحد يُحوّل back-office work إلى automation إنتاجي بتحديث بلغة طبيعية!</h2>
      <p class="article-lead">«أرِ المهمة مرة واحدة — Caddi يتعلّم العملية ويبني الأتمتة ويُحدّثها بالإنجليزية البسيطة». في 28 أغسطس 2026، احتل <strong>Caddi</strong> المركز الثاني على Product Hunt بـ 303 upvote — <strong>وكيل يبني وكلاء</strong> يُحوّل narrated screenshares إلى production agents تُشغّل back-office work عبر أدواتك الحقيقية.</p>
      <p>المشكلة التي حلّتها: RPA وworkflow builders تتطلب scoping ومطوّرين وإعداد خطوة بخطوة — وback-office tasks متكررة تُضيّع ساعات. Caddi يُجمع AI reasoning مع deterministic execution: كل run مُسجّل وكل permission مُحدّد النطاق. أرِ المهمة مرة، Caddi يتعلّم، يبني automation، وتُحدّثه بلغة طبيعية — what comes out reasons، what runs executes.</p>
      <p>القدرات الأساسية: تعلّم من screenshare مُ narrated، production agents عبر real tools، deterministic execution مع logging كامل، permission scoping، تحديث workflows بلغة طبيعية، تكامل Productivity وLegal وAI categories. Product Hunt #2 يوم 28 أغسطس، hunted by Ben Lang — ideal لـ finance ops وlegal back-office وadmin workflows.</p>
      <p>للمبدعين العرب: كل accounting firm وlegal office وoperations team في MENA يُعاني من repetitive back-office — Caddi agent building packages وArabic workflow capture services وmanaged automation retainers فرصة B2B ضخمة. «Show once, automate forever» vertical ينمو — Caddi تُكافئ teams التي تُفوّض deterministic back-office work.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Caddi وثورة الأتمتة من screenshare؟</h3>
        <ul>
          <li><strong>Caddi automation packages:</strong> capture وbuild وdeploy agents — 2000–20000 دولار/workflow.</li>
          <li><strong>Arabic back-office agent library:</strong> مكتبة workflows جاهزة بالعربية — 1500–15000 دولار/مجموعة.</li>
          <li><strong>Managed automation retainers:</strong> صيانة agents وpermissions شهرياً — 2500–25000 دولار/شهر.</li>
          <li><strong>دورات «Automate Back-Office with Caddi»:</strong> bootcamp لفرق العمليات — 59–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Caddi</span>
        <span class="tag">Agent Builder</span>
        <span class="tag">Screenshare Automation</span>
        <span class="tag">Back-Office AI</span>
        <span class="tag">Product Hunt</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-08-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-08-2026 -- 04-PM.html">
          📰 29 أغسطس 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Enter Pro · Lenz · Traccia · Caddi</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-08-2026 -- 04-PM.html" not in content:
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
