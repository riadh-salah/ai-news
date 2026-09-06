#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 06-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "06-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — CUA-Lite، Grok Imagine Video Agent، Okta MCP Server، Zoho Catalyst 3.0، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 6 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من CUA-Lite الذي يُوحّد 30 ألف مهمة و15 benchmark لوكلاء سطح المكتب والمتصفح والجوال في أمر واحد، إلى Grok Imagine Video 1.5 Agent الذي يُحوّل اللقطات المنفصلة إلى قصة متصلة بـ Image 2.0، ومن Okta Managed MCP Server الذي يُدير الهوية والصلاحيات بلغة طبيعية، إلى Zoho Catalyst 3.0 المنصة الكاملة من prompt إلى production — أربع ثورات تُعيد تشكيل computer-use agents والفيديو الوكيلي وIAM المحادثي والتطوير الوكيلي في 6 سبتمبر 2026!</h1>
      <p class="hero-sub">UC Berkeley تُطلق CUA-Lite بـ LiteSample وlite.gym وGRPO على Docker، xAI تُسلّم Grok Imagine Video Agent بـ 15 ثانية و1080p و0.05 دولار/ثانية، Okta MCP يُنفّذ bulk access وcampaign audits من Claude وCursor، وZoho Catalyst 3.0 يُوجّه Agent Skills وMCP وCLI بلا تدخل يدوي. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 6 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>CUA-Lite: UC Berkeley تُطلق منصة مفتوحة لوكلاء سطح المكتب — 30 ألف مهمة و15 benchmark في أمر rollout.py واحد!</h2>
      <p class="article-lead">«المشكلة ليست النموذج — المشكلة أن كل sandbox وdataset وeval في مستودع منفصل». في 5–6 سبتمبر 2026، أطلق باحثون من <strong>UC Berkeley</strong> <strong>CUA-Lite</strong> — منصة مفتوحة لوكلاء استخدام الحاسوب (Computer-Use Agents) تُوحّد agents وenvironments وtraces وtraining/evaluation خلف action space واحد وschema واحد وأمر واحد.</p>
      <p>المشكلة التي حلّتها: تدريب CUA يتطلب أربعة مكونات — agents، environments، traces، framework — كلها مجزّأة عبر repositories بinterfaces غير متوافقة. CUA-Lite يُقدّم <strong>LiteSample</strong> (schema موحّد parquet + images)، <strong>lite.gym</strong> (screenshots in، actions out)، و<strong>scripts/rollout.py</strong> حيث تبدّل <strong>--model-id</strong> و<strong>--env-id</strong> فقط.</p>
      <p>القدرات الأساسية: 10+ agents مدمجة (GPT، Claude، Gemini، Qwen3-VL، UI-TARS، Fara-7B، MAI-UI)؛ 15+ benchmarks (OSWorld، WebArena، AndroidWorld، ScreenSpot-Pro)؛ 30,000+ مهمة قابلة للتحقق؛ Lite.OSWorld وLite.Browser وLite.Mobile؛ datasets على Hugging Face (Aguvis، OpenCUA، ScaleCUA، GUI-360)؛ reinforcement learning عبر GRPO على Slime trainer؛ deployable على أي Docker host.</p>
      <p>للمبدعين العرب: كل فريق يبني computer-use agents — CUA-Lite sandbox setup packages وArabic benchmark playbooks وmanaged CUA training retainers فرصة research premium. «Unified CUA infrastructure» vertical ينمو — Berkeley تُكافئ teams التي تُسلّم reproducible rollouts لا one-off demos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من CUA-Lite وثورة computer-use agents؟</h3>
        <ul>
          <li><strong>CUA-Lite sandbox deployment packages:</strong> Docker + benchmark setup — 3000–28000 دولار/مشروع.</li>
          <li><strong>Custom CUA training pipelines:</strong> LiteSample distillation + GRPO — 5000–45000 دولار/عميل.</li>
          <li><strong>Vertical CUA agents:</strong> desktop/browser/mobile automation — 4000–40000 دولار/حل.</li>
          <li><strong>دورات «Build Computer-Use Agents with CUA-Lite»:</strong> bootcamp — 59–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">CUA-Lite</span>
        <span class="tag">UC Berkeley</span>
        <span class="tag">Computer-Use Agents</span>
        <span class="tag">LiteSample</span>
        <span class="tag">OSWorld</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Grok Imagine Video 1.5 Agent: xAI يُحوّل اللقطات المنفصلة إلى قصة متصلة — Image 2.0 و15 ثانية و0.05 دولار/ثانية!</h2>
      <p class="article-lead">«الفيديو التوليدي كان لقطات معزولة — الآن وكيل يُخطّط ويُربط المشاهد كمخرج حقيقي». في 5 سبتمبر 2026، أطلقت <strong>xAI</strong> <strong>Grok Imagine Video 1.5 Agent</strong> — طبقة orchestration تُستخدم <strong>Image 2.0</strong> لتخطيط وربط لقطات AI-generated باستمرارية أقوى وجودة بصرية أعلى.</p>
      <p>المشكلة التي حلّتها: generative video يُنتج clips منفصلة بلا continuity — صناع المحتوى يُعيد توليد كل shot يدوياً. Agent الجديد يُخطّط sequence كامل، يُربط المشاهد، ويُحافظ على visual consistency عبر character وscene references — كل ذلك فوق Video 1.5 الموجود لا استبدالاً له.</p>
      <p>القدرات الأساسية: clips حتى <strong>15 ثانية</strong> و<strong>1080p</strong> في workflows مدعومة؛ audio متزامن؛ text/image/character/scene/voice references؛ Fast mode (~25 ثانية للclip)؛ API بـ <strong>0.05 دولار/ثانية</strong> generated؛ Image 2.0 Quality Mode للtypography والediting والconsistency. Agent يُدمج كل هذه الطبقات في workflow واحد للscenes متصلة.</p>
      <p>للمبدعين العرب: كل creator وagency في MENA — Grok Imagine agent packages وArabic short-form video playbooks وmanaged AI video retainers فرصة content premium. «Agentic video storytelling» vertical ينمو — xAI تُكافئ teams التي تُسلّم connected narratives لا isolated clips.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Grok Imagine Video Agent وثورة الفيديو الوكيلي؟</h3>
        <ul>
          <li><strong>AI video agent packages:</strong> multi-shot storytelling workflows — 1500–15000 دولار/مشروع.</li>
          <li><strong>Short-form content retainers:</strong> TikTok/Reels/Shorts بـ Grok — 800–8000 دولار/شهر.</li>
          <li><strong>Brand video automation:</strong> character consistency + voice refs — 2500–25000 دولار/عميل.</li>
          <li><strong>دورات «Agentic Video with Grok Imagine 1.5»:</strong> bootcamp — 39–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Grok Imagine</span>
        <span class="tag">Video 1.5 Agent</span>
        <span class="tag">xAI Image 2.0</span>
        <span class="tag">AI Video</span>
        <span class="tag">Generative Video</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Okta Managed MCP Server: إدارة الهوية بلغة طبيعية — users وgroups وpolicies وaudit logs من Claude وCursor!</h2>
      <p class="article-lead">«لم يعد IAM يعني عشرات النقرات في Admin Console — اسأل وكيلك ونفّذ». في 3 سبتمبر 2026، أطلقت <strong>Okta</strong> <strong>Managed MCP Server</strong> في Early Access — اتصال MCP مُستضاف turnkey يُمكّن Claude Desktop وClaude Code وCursor وVS Code من إدارة Okta org بلغة طبيعية.</p>
      <p>المشكلة التي حلّتها: identity ops repetitive — account lookup يعني clicks متعددة، bulk assignment يعني scripts مؤقتة، audit logs يعني filters يدوية. Okta MCP: user/group management، app assignments، policy updates، system log queries، governance workflows — كلها عبر prompts بدلاً من consoles.</p>
      <p>القدرات الأساسية: hosted MCP بدون local servers ولا custom wrappers؛ conversational user/group lookup وbulk access changes؛ campaign audits وapproval workflows؛ integration مع Claude Desktop وClaude Code وCursor وVS Code؛ OAuth-managed secure access؛ Early Access مع demo use cases للidentity teams.</p>
      <p>للمبدعين العرب: كل enterprise وSaaS في MENA — Okta MCP setup packages وArabic IAM automation playbooks وmanaged identity ops retainers فرصة security premium. «Conversational IAM» vertical ينمو — Okta تُكافئ integrators التي تُسلّم natural-language identity workflows لا manual admin tasks.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Okta MCP Server وثورة IAM المحادثي؟</h3>
        <ul>
          <li><strong>Okta MCP integration packages:</strong> Claude/Cursor + IAM workflows — 3500–35000 دولار/مشروع.</li>
          <li><strong>Identity automation retainers:</strong> bulk access + audit automation — 2000–20000 دولار/شهر.</li>
          <li><strong>Enterprise IAM consulting:</strong> conversational governance playbooks — 5000–50000 دولار/عميل.</li>
          <li><strong>دورات «Conversational IAM with Okta MCP»:</strong> bootcamp — 49–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Okta MCP Server</span>
        <span class="tag">Conversational IAM</span>
        <span class="tag">Identity Management</span>
        <span class="tag">MCP Server</span>
        <span class="tag">Enterprise Security</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zoho Catalyst 3.0: من prompt إلى production — Agent Skills وMCP وCLI غير تفاعلي في منصة serverless واحدة!</h2>
      <p class="article-lead">«وكيلك يكتب الكود — لكن أين يُ deploy؟ Catalyst 3.0 يُغلق الحلقة من prompt إلى production». في 2 سبتمبر 2026، أطلقت <strong>Zoho</strong> <strong>Catalyst 3.0</strong> — منصة cloud full-stack agent-ready تُمكّن AI coding assistants من بناء وdeploy تطبيقات production-grade في بيئة serverless واحدة.</p>
      <p>المشكلة التي حلّتها: agentic coding assistants تُنتج code لكن deployment يبقى bottleneck — developers يُبدّلون بين IDE وcloud console وCLI. Catalyst 3.0: <strong>Agent Skills</strong> تُعلّم الوكيل Catalyst APIs، <strong>MCP support</strong> لإكمال actions من coding assistant، و<strong>non-interactive CLI</strong> ينفّذ tasks start-to-finish بلا manual input.</p>
      <p>القدرات الأساسية: orchestration layer يُوجّه requests عبر CLI أو MCP deterministically (ليس للنموذج أن يختار)؛ AI IDE integrations؛ AI-assisted development workflows؛ serverless full-stack (functions، databases، storage، cron)؛ SDKs وCLI محدّثة؛ Agent Skills تُولّد production-grade code مُخصّص لـ Catalyst APIs.</p>
      <p>للمبدعين العرب: كل startup وagency تبني SaaS — Catalyst 3.0 agent setup packages وArabic full-stack playbooks وmanaged agentic deployment retainers فرصة dev premium. «Agent-ready cloud platform» vertical ينمو — Zoho تُكافئ teams التي تُسلّم prompt-to-production pipelines لا prototype-only demos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zoho Catalyst 3.0 وثورة التطوير الوكيلي؟</h3>
        <ul>
          <li><strong>Catalyst 3.0 agent setup packages:</strong> Skills + MCP + CLI — 2500–25000 دولار/مشروع.</li>
          <li><strong>Prompt-to-production SaaS builds:</strong> agent-driven full-stack — 5000–50000 دولار/تطبيق.</li>
          <li><strong>Managed Catalyst retainers:</strong> deployment + monitoring — 1500–15000 دولار/شهر.</li>
          <li><strong>دورات «Build SaaS with Catalyst 3.0 Agents»:</strong> bootcamp — 39–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zoho Catalyst 3.0</span>
        <span class="tag">Agent Skills</span>
        <span class="tag">MCP Support</span>
        <span class="tag">Serverless</span>
        <span class="tag">Prompt to Production</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 06-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="06-09-2026 -- 04-PM.html">
          📰 6 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">CUA-Lite · Grok Imagine Video Agent · Okta MCP Server · Zoho Catalyst 3.0</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "06-09-2026 -- 04-PM.html" not in content:
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
    bad_patterns = ["dollar", "mlions", "bringing", "الLlatin", "أفكar"]
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
