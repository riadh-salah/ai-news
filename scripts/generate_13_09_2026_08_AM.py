#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 13-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "13-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Abacus.AI Smaug Agentic وFlash وMini للوكلاء المفتوحة، Hugging Face ML Intern لتجارب ML من المحادثة، Leadpages MCP لبناء صفحات هبوط من Claude وChatGPT، Strands Agents مع LeRobot وStorage Buckets لحلقة روبوتات كاملة، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 13 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Abacus.AI Smaug الذي يُخفّض تكلفة حلقات الوكلاء 10–100× عبر أوزان مفتوحة على Kimi K3 وDeepSeek وQwen، إلى Hugging Face ML Intern — «متدرب ML» يُشغّل التدريب والتقارير من جملة عربية أو إنجليزية، ومن Leadpages MCP الذي يُنشر صفحة هبوط من هاتفك داخل Claude أو ChatGPT، إلى Strands Agents مع LeRobot وStorage Buckets — تسجيل وتدريب ونشر روبوت من مكان واحد — أربع ثورات تُعيد تشكيل الوكلاء المفتوحة والتسويق الوكيلي والروبوتات في 13 سبتمبر 2026!</h1>
      <p class="hero-sub">Smaug يُنافس Opus-class داخل VPC، ML Intern يُ democratize التجارب، Leadpages يُحوّل المحادثة إلى إيرادات فورية، وStrands يُغلق حلقة البيانات من الذراع الروبوتية إلى Hub. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 13 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Abacus.AI Smaug: ثلاثة نماذج open-weight للوكلاء — Agentic 2.8T وFlash وMini 27B بأداء أعلى 15–20%!</h2>
      <p class="article-lead">«حلقة وكيل طويلة = فاتورة Opus كل ساعة». في 10 سبتمبر 2026، أطلقت <strong>Abacus.AI</strong> عائلة <strong>Smaug</strong>: ثلاثة نماذج <strong>open-weight</strong> مُ fine-tuned لحلقات <strong>agentic</strong> طويلة — self-improving loops داخل VPC المؤسسة دون إرسال بيانات العملاء إلى APIs مغلقة.</p>
      <p>المشكلة التي حلّتها: الوكلاء المؤسسيون يكرّرون tool calls وسياقاً ضخماً — prompt caching ينكسر عبر فجوات زمنية، والنماذج المغلقة تُكلّف 10–100× أكثر. Smaug يجمع <strong>agentic traces</strong> حقيقية مع بيانات synthetic صعبة — methodology ترفع benchmarks الوكلاء 15–20% دون زيادة compute.</p>
      <p>القدرات الأساسية: <strong>Smaug Agentic</strong> — fine-tune على <strong>Kimi K3</strong> (2.8T MoE، 1M token context، MoonViT-V2)؛ بديل Opus-class للـcoding loops المعقّدة؛ على Hugging Face كـ<code>abacusai/Smaug-Agentic</code>؛ <strong>Smaug Flash</strong> — على <strong>DeepSeek V4 Flash 0731</strong>؛ وكيل شخصي يتصل WhatsApp وTelegram وSlack؛ LiveBench agentic coding 61.1 مقابل 46.8 للأساس؛ <strong>Smaug Mini</strong> — 27B على <strong>Qwen3.8</strong>؛ chatbots مؤسسية multimodal قابلة للـfine-tune؛ متاح أيضاً عبر <strong>RouteLLM API</strong> من Abacus.AI.</p>
      <p>للمبدعين العرب: كل بنك وtelco وe-commerce في MENA يريد وكلاء داخل السحابة الخاصة — Smaug hosting packages وArabic agent fine-tuning وmanaged RouteLLM deployments فرصة sovereignty premium. «Open-weight agent parity» = موجة 2026 — من يُسلّم VPC-ready agents مبكراً يفوز بعقود multi-year.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Abacus.AI Smaug وثورة الوكلاء open-weight؟</h3>
        <ul>
          <li><strong>Smaug VPC deployment packages:</strong> GPU cluster + Smaug Agentic/Flash + observability — 8000–75000 دولار/مشروع.</li>
          <li><strong>Agentic fine-tuning consulting:</strong> traces عربية + tool schemas + eval harness — 5000–45000 دولار/عميل.</li>
          <li><strong>Managed Smaug retainers:</strong> inference ops + model updates + cost caps — 4000–32000 دولار/شهر.</li>
          <li><strong>دورات «Deploy Enterprise Agents with Smaug»:</strong> bootcamp — 49–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Abacus.AI</span>
        <span class="tag">Smaug</span>
        <span class="tag">Open-Weight</span>
        <span class="tag">Agentic AI</span>
        <span class="tag">Hugging Face</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Hugging Face ML Intern: وصف فكرتك بالعربية — والوكيل يبحث ويُدرّب ويُرفع النموذج إلى Hub!</h2>
      <p class="article-lead">«أريد classifier للعربية — لكن ليس لدي فريق ML». في 9 سبتمبر 2026، أطلقت <strong>Hugging Face</strong> <strong>ML Intern</strong>: مساعد داخل واجهة المحادثة يحوّل وصفاً بلغة طبيعية إلى تجربة ML كاملة — من جمع البيانات إلى demo تفاعلي — بميزانية تُوافق عليها قبل أي GPU.</p>
      <p>المشكلة التي حلّتها: Hub غني بالنماذج والـdatasets لكن non-experts عالقون. ML Intern يُ automates البحث في Hub وGitHub والويب، يُقدّر التكلفة، ثم بعد موافقتك يُولّد datasets ويُشغّل training ويراقب jobs ويكتب تقارير ويبني demos — dashboard لكل run.</p>
      <p>القدرات الأساسية: workflow محادثة → اكتشاف → <strong>budget approval</strong> → تنفيذ مستقل؛ demo فيديو Hugging Face: run ~6 ساعات بتكلفة أقل من <strong>0.50 دولار</strong> (يختلف حسب الحجم)؛ رفع النتائج إلى Hub تلقائياً؛ يُكمّل رؤية HF «open AI for everyone» — نفس spirit الذي يُغذي Smaug وLeRobot ecosystem.</p>
      <p>للمبدعين العرب: كل startup edtech وmedia وgovtech يريد POC سريع — ML Intern guided packages وArabic dataset curation playbooks و«HF Hub launch» retainers فرصة democratization premium. «No-code ML that ships» = category killer — consultants الذين يُصمّمون budget-safe experiment pipelines يفوزون بعقود innovation labs.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hugging Face ML Intern وثورة تجارب ML من المحادثة؟</h3>
        <ul>
          <li><strong>ML Intern experiment packages:</strong> scoped ideas + budget governance + Hub publishing — 2500–22000 دولار/مشروع.</li>
          <li><strong>Arabic ML POC consulting:</strong> dataset design + eval + demo for stakeholders — 3000–28000 دولار/عميل.</li>
          <li><strong>Managed HF experimentation retainers:</strong> monthly experiment sprints + reports — 2000–16000 دولار/شهر.</li>
          <li><strong>دورات «Ship ML from Chat with ML Intern»:</strong> bootcamp — 29–149 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hugging Face</span>
        <span class="tag">ML Intern</span>
        <span class="tag">AutoML</span>
        <span class="tag">Hub</span>
        <span class="tag">Agentic ML</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Leadpages MCP: «ابنِ صفحة الهبوط من المحادثة» — Claude وChatGPT ينشرون Leadpages في 30 ثانية!</h2>
      <p class="article-lead">«الفكرة وُلدت في الاجتماع — والصفحة لا تزال فارغة». في 12 سبتمبر 2026، أعلنت <strong>Leadpages</strong> عن <strong>Leadpages MCP</strong> داخل <strong>Claude</strong> و<strong>ChatGPT</strong>: اتصال MCP آمن يُمكّن المساعد من إنشاء وتحرير ونشر صفحات Leadpages — دون فتح التطبيق، حتى من الهاتف.</p>
      <p>المشكلة التي حلّتها: AI assistants كانوا يُ explain كيف تبني landing page — لا يبنونها. MCP يُعرّف actions Leadpages نفسها: create page، edit، publish — بصلاحيات OAuth scoped مثل أي تكامل app-to-app.</p>
      <p>القدرات الأساسية: ربط الحساب ~30 ثانية؛ من prompt إلى صفحة جاهزة للنشر؛ ideal للفرق التي تستخدم Claude/ChatGPT يومياً — marketing velocity من conversation؛ security model MCP: المساعد يعمل ضمن permissions الممنوحة فقط؛ لا حاجة لمطوّر للإعداد.</p>
      <p>للمبدعين العرب: كل agency وcreator وSME في MENA يبيع عبر funnels — Leadpages MCP setup + Arabic copy workflows + «chat-to-campaign» retainers فرصة marketing premium. «Conversation is the CMS» = trend 2026 — من يُ package MCP landing playbooks يفوز ب retainers شهرية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Leadpages MCP وثورة التسويق من المحادثة؟</h3>
        <ul>
          <li><strong>Leadpages MCP onboarding packages:</strong> Claude/ChatGPT connect + templates + Arabic funnels — 1500–12000 دولار/عميل.</li>
          <li><strong>Chat-to-conversion consulting:</strong> offer design + A/B prompts + analytics — 2000–18000 دولار/مشروع.</li>
          <li><strong>Managed landing retainers:</strong> weekly pages from chat + optimization — 1200–9000 دولار/شهر.</li>
          <li><strong>دورات «Publish Landing Pages via MCP»:</strong> bootcamp — 19–99 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Leadpages</span>
        <span class="tag">MCP</span>
        <span class="tag">Claude</span>
        <span class="tag">ChatGPT</span>
        <span class="tag">Marketing AI</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Strands Agents + LeRobot + HF Storage Buckets: حلقة بيانات streaming — من تسجيل الذراع إلى policy على Hub!</h2>
      <p class="article-lead">«سجّلت demo — ثم انتظرت sync وdownload وtrain وdeploy». في 11 سبتمبر 2026، نشرت <strong>Hugging Face</strong> مع <strong>AWS Strands Agents</strong> و<strong>LeRobot</strong> حلقة <strong>streaming data loop</strong>: agent واحد يُسجّل demonstrations إلى <strong>Storage Buckets</strong>، يُدرّب بالـstream من Hub، ويُعيد policy إلى hardware — بنفس تنسيق LeRobot على القرص طوال المسار.</p>
      <p>المشكلة التي حلّتها: robot ML campaigns تتطلب قرارات يومية — أي episodes تُبقي؟ متى re-record؟ أي checkpoint يُستبدل على الذراع؟ Strands Robots SDK (Apache 2.0) يُ expose robot abstractions وsimulation وLeRobot كـ<strong>AgentTools</strong> في agent loop واحد.</p>
      <p>القدرات الأساسية: <strong>Storage Buckets</strong> — mutable Xet-backed repos في namespace <code>hf://</code>؛ sync incremental bytes فقط؛ train مباشرة من Hub دون download كامل؛ deploy بـkeyword argument واحد من sim إلى <strong>SO-101</strong> hardware؛ notebook companion <code>05_streaming_data_loop.ipynb</code>؛ يُكمّل post «Hub to hardware» — اليوم البيانات تعود من الذراع إلى policy عبر agent.</p>
      <p>للمبدعين العرب: كل factory automation lab وwarehouse robotics pilot في MENA — Strands integration packages وArabic robotics data playbooks وmanaged LeRobot retainers فرصة physical AI premium. «Closed-loop robot data agent» = moat — integrators الذين يُسلّمون streaming loops يفوزون ب pilot-to-production contracts.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Strands Agents وLeRobot وثورة حلقة الروبوتات؟</h3>
        <ul>
          <li><strong>Strands robot loop packages:</strong> sim + bucket + train pipeline + hardware deploy — 12000–95000 دولار/مشروع.</li>
          <li><strong>LeRobot consulting:</strong> dataset campaigns + policy selection + Hub governance — 7000–60000 دولار/عميل.</li>
          <li><strong>Managed robotics ML retainers:</strong> daily agent ops + retrain cycles — 5500–42000 دولار/شهر.</li>
          <li><strong>دورات «Streaming Robot Data with Strands»:</strong> bootcamp — 59–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Strands Agents</span>
        <span class="tag">LeRobot</span>
        <span class="tag">Hugging Face</span>
        <span class="tag">Robotics</span>
        <span class="tag">Storage Buckets</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 13-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="13-09-2026 -- 08-AM.html">
          📰 13 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Abacus Smaug · HF ML Intern · Leadpages MCP · Strands LeRobot</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "13-09-2026 -- 08-AM.html" not in content:
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
    bad_patterns = ["dollar", "mlions", "bringing", "الLlatin", "أفكar", "دolار", "البروtokol"]
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
