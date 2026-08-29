#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-08-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-08-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Almanac، Hy4 Preview، Lightfield، Cohere Parse، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 أغسطس 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من وكيل بـ «دماغ ثانٍ» يُصحّح wiki تلقائياً إلى نموذج Tencent مفتوح 770B بسياق مليون token، ومن CRM يُبرمج نفسه بـ Python إلى Parse الذي يُحوّل ملايين الصفحات بـ 1.50 دولار — أربع ثورات تُعيد تعريف الذاكرة والبرمجة والمبيعات والمستندات في 29 أغسطس 2026!</h1>
      <p class="hero-sub">Almanac يبني دماغاً شخصياً وشركاتياً ذاتياً التحديث ويعمل في Slack وiMessage بكمبيوتر حقيقي، Hy4 Preview من Tencent يُطلق 770B MoE مفتوح المصدر بسياق 1M token على Vercel AI Gateway، Lightfield يُعطي وكيل CRM أداة تنفيذ كود Python على كل تفاعلات العملاء، وCohere Parse يُحلّل المستندات المعقدة بأفضل سعر/أداء مقارنة بـ AWS Textract وGoogle Document AI. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 29 أغسطس 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Almanac: الوكيل بـ «الدماغ الثاني» — wiki ذاتي التحديث، كمبيوتر حقيقي، وعمل استباقي يُصحّح نفسه قبل أن يُفسد الذاكرة!</h2>
      <p class="article-lead">«الذاكرة لا تُلصق لاحقاً — يجب أن تُجمَع مسبقاً بـ compute حقيقي». في 28 أغسطس 2026، احتل <strong>Almanac</strong> المركز السابع على Product Hunt بـ 144 upvote — <strong>وكيل AI يعرف شركتك</strong> يبني «دماغاً ثانياً» ذاتياً التحديث من Gmail وCalendar وGitHub وPostHog وGranola، ثم يعيش في Slack وiMessage ويُنجز مهاماً حقيقية بكمبيوتر سحابي خاص.</p>
      <p>المشكلة التي حلّتها: كل فريق يُريد وكيلاً واحداً يعرف سياق الشركة كاملاً — لكن OAuth لكل connector وhosting وmemory management يُضيّع أسابيع. Almanac يُجمّع connectors بنقرة واحدة (حسابات شخصية أو مشتركة)، يُولّد wiki شخصياً (تفضيلاتك وعلاقاتك) وwiki شركاتياً (roadmap وblockers)، ويُراجع كل تحديث قبل أن يُ landing — صفحة جديدة أم تعديل أم تناقض يجب حله. هذا يمنع «rotting memory» التي تُفسد كل وكلاء RAG.</p>
      <p>القدرات الأساسية: كمبيوتر حقيقي (browser + terminal) — للأدوات بلا API يُسجّل الدخول وينقر كما تفعل أنت، ويتوقف عند login أو payment أو قرار كبير ويُسلّمك المتصفح الحي. background worker يُقترح مهاماً استباقياً («صغّرت deck التمويل، تريد مراجعته؟»). CLI موحّد يمكن Codex وClaude Code استخدامه. خبرة بناء wikis لـ Harvard وNASA. Product Hunt #7 يوم 28 أغسطس، hunted by Garry Tan، trial 7 أيام على usealmanac.com.</p>
      <p>للمبدعين العرب: كل startup وagency وremote team في MENA يُعاني من context fragmentation — Almanac setup packages وArabic company brain design وmanaged agent memory retainers فرصة premium B2B. «Compiled upfront memory» vertical ينمو — Almanac تُكافئ teams التي تُفوّض multi-step work مع governance.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Almanac وثورة الدماغ الثاني؟</h3>
        <ul>
          <li><strong>Company brain setup packages:</strong> إعداد Almanac مع connectors وwikis — 2000–20000 دولار/شركة.</li>
          <li><strong>Arabic wiki architecture design:</strong> تصميم ذاكرة شركاتية بالعربية — 1500–12000 دولار/مشروع.</li>
          <li><strong>Managed agent memory retainers:</strong> صيانة wiki وworkflows شهرياً — 2500–25000 دولار/شهر.</li>
          <li><strong>دورات «Deploy Your Second Brain with Almanac»:</strong> bootcamp للفرق الناشئة — 59–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Almanac</span>
        <span class="tag">Second Brain</span>
        <span class="tag">Company Wiki</span>
        <span class="tag">Agent Memory</span>
        <span class="tag">Product Hunt</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Hy4 Preview: Tencent تُطلق 770B MoE مفتوح المصدر — 49B active، سياق 1M token، وبرمجة طويلة الأمد على Vercel AI Gateway!</h2>
      <p class="article-lead">«النماذج المغلقة تُحدّ من الابتكار — Hy4 preview يُعيد frontier للمجتمع». في 27–28 أغسطس 2026، أطلقت Tencent Hy Team <strong>Hy4 Preview</strong> — نموذج <strong>Mixture-of-Experts</strong> بـ 770B parameter إجمالي و49B active لكل token، 78 طبقة مع 256 expert مُوجّه + shared expert (top-8)، و<strong>سياق 1M token</strong>، متاح على Hugging Face وModelScope وVercel AI Gateway.</p>
      <p>المشكلة التي حلّتها: المطوّرون يحتاجون نموذجاً قوياً للبرمجة طويلة الأمد وتحليل المستندات الضخمة وتطوير الألعاب والاستدلال العلمي — لكن معظم frontier models مغلقة أو باهظة. Hy4 preview يُقدّم أقوى pre-training في open-source frontier مع native MTP layer (10B) للـ speculative decoding، ونسخة FP8 للنشر الفعّال.</p>
      <p>القدرات الأساسية: استخدام فوري عبر Vercel AI Gateway (`model: 'tencent/hy4-preview'`)، تكامل مع Claude Code وCodex وOpenCode وCursor وPi، أوزان مفتوحة على Hugging Face وGitCode وCNB، تركيز على long-horizon coding وdocument analysis وgame development وscientific reasoning. Vercel AI Gateway: unified API، failover، Zero Data Retention، بدون markup على أسعار المزود.</p>
      <p>للمبدعين العرب: كل AI agency وdev shop وSaaS builder في MENA يُريد نموذجاً قوياً بتكلفة منخفضة — Hy4 integration packages وArabic coding agent workflows وmanaged inference retainers فرصة infrastructure. «Open frontier MoE» vertical ينمو — Hy4 تُكافئ builders الذين يبنون على open weights.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hy4 Preview وثورة النماذج المفتوحة؟</h3>
        <ul>
          <li><strong>Hy4 agent integration packages:</strong> ربط Hy4 بـ workflows العملاء — 1500–15000 دولار/مشروع.</li>
          <li><strong>Arabic long-context coding workflows:</strong> pipelines برمجة وتحليل مستندات بالعربية — 1000–10000 دولار/workflow.</li>
          <li><strong>Managed inference retainers:</strong> إدارة Gateway وrouting وcost optimization — 2000–20000 دولار/شهر.</li>
          <li><strong>دورات «Build with Hy4 on Vercel AI Gateway»:</strong> bootcamp للمطوّرين — 49–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hy4 Preview</span>
        <span class="tag">Tencent Hunyuan</span>
        <span class="tag">Open Source MoE</span>
        <span class="tag">1M Context</span>
        <span class="tag">Vercel AI Gateway</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Lightfield: CRM أصلي بالذكاء الاصطناعي يُبرمج نفسه — وكيل Python يُحلّل pipeline ويُولّد تقارير من كل مكالمة وبريد دون workflow builder!</h2>
      <p class="article-lead">«CRM التقليدي يعتمد على إدخال يدوي — Lightfield يُلتقط كل تفاعل ويُبرمج workflows بلغة طبيعية». <strong>Lightfield</strong> هو <strong>AI-native CRM</strong> لـ 2500+ شركة ناشئة — يبني نموذجاً حياً لكل عميل من المكالمات والبريد والاجتماعات، والآن يُعطي الوكيل <strong>code execution</strong> لكتابة وتشغيل Python على كل سياق CRM.</p>
      <p>المشكلة التي حلّتها: workflow builders تتطلب سحب صناديق أو كتابة كود — وCRM data scattered في emails وmeetings. Lightfield agent يُخطّط approach، يكتب Python script، يُشغّله في sandbox، ويُقيّم النتائج ويُكرّر. عندما يحتاج context غير مُستخرج، يُرسل sub-agents لقراءة histories فردية وinterpret tone — ثم يُعالج على scale.</p>
      <p>القدرات الأساسية: migration agent يُنقل HubSpot في ساعة واحدة مع relationship preservation، auto-capture calls/emails/meetings، agent SDK وAPI documentation أصلية، Skills وKnowledge وAutomations blocks، Sequences مع LinkedIn DMs، Sonnet 5 في workflows، Slack agent integration. Code execution يُنتج reports وscorecards وCSV exports — foundation لـ GTM workflows defined in natural language.</p>
      <p>للمبدعين العرب: كل B2B startup وsales team وagency في MENA يُعاني من CRM manual entry — Lightfield setup packages وArabic sales intelligence workflows وmanaged CRM agent retainers فرصة revenue ops premium. «Agent that programs your CRM» vertical ينمو — Lightfield تُكافئ teams التي تُفوّض analytics وoutbound.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lightfield وثورة CRM البرمجي؟</h3>
        <ul>
          <li><strong>Lightfield CRM migration packages:</strong> نقل من HubSpot/Salesforce — 2000–20000 دولار/مشروع.</li>
          <li><strong>Arabic sales agent workflows:</strong> pipelines pipeline analytics وoutbound بالعربية — 1500–15000 دولار/workflow.</li>
          <li><strong>Managed GTM agent retainers:</strong> صيانة automations وreports شهرياً — 3000–30000 دولار/شهر.</li>
          <li><strong>دورات «Program Your CRM with Lightfield Agents»:</strong> bootcamp لفرق المبيعات — 69–449 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lightfield</span>
        <span class="tag">AI-Native CRM</span>
        <span class="tag">Code Execution</span>
        <span class="tag">Sales Intelligence</span>
        <span class="tag">CRM Migration</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Cohere Parse: ذكاء المستندات للمؤسسات — 1.50 دولار/1000 صفحة، +20 نقطة على AWS Textract، وParse-v5 جاهز للـ RAG والوكلاء!</h2>
      <p class="article-lead">«تحليل المستندات على scale كان مكلفاً وغير دقيق — Parse يُغيّر المعادلة». أطلقت Cohere <strong>Parse</strong> — <strong>vision language model</strong> لتحويل PDFs وslides وملفات multimodal معقدة إلى Markdown structured للـ indexing وRAG وagentic retrieval — بـ <strong>1.50 دولار لكل 1000 صفحة</strong> عبر Cohere API، مع Model Vault للـ single-tenant inference.</p>
      <p>المشكلة التي حلّتها: hyperscaler document AI (AWS Textract، Google Document AI) باهظة وأقل دقة — وfrontier LLMs general-purpose مكلفة جداً للـ high-volume. Parse يُقدّم أقوى price-performance tradeoff: يتفوق على specialized parsing solutions، و+20 نقطة improvement على Textract وDocument AI، ويُنافس GPT-5.5 وOpus 4.8 وGemini 3.5 Flash في evaluations.</p>
      <p>القدرات الأساسية: model `parse-v5` عبر Cohere API وModel Vault وMicrosoft Foundry وAWS SageMaker، throughput عالي للإنتاج (مئات آلاف إلى ملايين الصفحات)، Model Vault savings 23% عند 50% GPU utilization و61% عند full utilization، deployment آمن للصناعات المنظّمة. GA متاح الآن — ideal لـ enterprise knowledge bases وcompliance archives.</p>
      <p>للمبدعين العرب: كل legal tech وinsurance وgovernment digitization project في MENA يحتاج document parsing على scale — Parse integration packages وArabic document pipelines وmanaged parsing retainers فرصة enterprise ضخمة. «Cost-effective document intelligence» vertical ينمو — Parse تُكافئ high-volume workloads.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cohere Parse وثورة تحليل المستندات؟</h3>
        <ul>
          <li><strong>Document parsing integration packages:</strong> ربط Parse بـ RAG pipelines — 2500–25000 دولار/مشروع.</li>
          <li><strong>Arabic document digitization workflows:</strong> pipelines OCR وstructuring للوثائق العربية — 2000–20000 دولار/workflow.</li>
          <li><strong>Managed parsing retainers:</strong> معالجة millions of pages شهرياً — 3000–30000 دولار/شهر.</li>
          <li><strong>دورات «Build Enterprise RAG with Cohere Parse»:</strong> bootcamp للمحللين — 79–499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cohere Parse</span>
        <span class="tag">Document Intelligence</span>
        <span class="tag">Enterprise RAG</span>
        <span class="tag">Parse-v5</span>
        <span class="tag">Vision Language Model</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-08-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-08-2026 -- 08-AM.html">
          📰 29 أغسطس 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Almanac · Hy4 Preview · Lightfield · Cohere Parse</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-08-2026 -- 08-AM.html" not in content:
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
