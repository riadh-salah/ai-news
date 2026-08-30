#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 30-08-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "30-08-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Agnost AI، beafk.app، Firecrawl Developer Index، screenpipe، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 30 أغسطس 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من مراقبة تُكشف فشل الوكلاء الصامت الذي تُفوته الاختبارات، إلى workspace جوّال يُشغّل Claude Code وCodex من هاتفك، ومن فهرس 70 مليون مورد برمجي للوكلاء إلى ذاكرة محلية تُسجّل شاشتك وتُغذّي وكلاء MCP — أربع ثورات تُعيد تعريف المراقبة والتطوير والبحث والسياق في 30 أغسطس 2026!</h1>
      <p class="hero-sub">Agnost AI يقرأ كل محادثة إنتاج ويُحوّل الفشل الصامت وانحراف السلوك إلى evals وإصلاحات، beafk.app يُجمّع وكلاء الترميز الأصليين في crew واحد تُوجّهه من جوّالك مع بقاء الكود على جهازك، Firecrawl Developer Index يُفتّش 70+ مليون README وissue وPR عبر API وMCP، وscreenpipe يُسجّل شاشتك وصوتك ونشاطك محلياً ليُجيب وكلاء AI عن «ماذا حدث في ذلك الاجتماع؟» دون أن تتذكر. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 30 أغسطس 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Agnost AI: اكتشف فشل الوكلاء الذي تُفوته evals — فشل صامت، هلوسة، إحباط مستخدم، وإشارات churn من محادثات الإنتاج!</h2>
      <p class="article-lead">«لوحة المراقبة تقول 200 OK — لكن الوكيل ادّعى أنه أنهى مهمة لم ينفّذها». في 25 أغسطس 2026، احتل <strong>Agnost AI</strong> المركز الثالث Product of the Day على Product Hunt بـ 286 upvote — أداة تُحلّل محادثات المستخدمين مع وكلاء AI في الإنتاج وتكتشف: <strong>silent failures</strong>، انحراف سلوك الوكيل، هلوسة وروابط مُختلقة، إحباط المستخدم، طلبات ميزات مخفية، وإشارات churn.</p>
      <p>المشكلة التي حلّتها: evals تختبر مشاكل تعرفها مسبقاً — لا يمكنك كتابة eval لمشكلة لم تكتشفها بعد. dashboards التقليدية تُظهر «طلب ناجح» بينما الفشل الحقيقي يظهر فقط لمن يقرأ المحادثة كاملة. Agnost AI يقرأ كل محادثة chat وvoice في الإنتاج، يُجمّعها في أنماط متكررة، يُظهر المستخدمين والمحادثات الدقيقة خلف كل insight، ثم يُحوّلها إلى evals أو يطلب من coding agent تصحيح المشكلة.</p>
      <p>القدرات الأساسية: اتصال بثلاثة أسطر كود أو عبر OpenTelemetry، تحليل أكثر من مليون رسالة يومياً، grouping للفشل المتكرر وbehavior drift وhallucinated links وfrustration وfeature requests. Use cases: أي منتج يُشغّل user-facing agents في customer support أو sales أو onboarding — «اكتشف ما لا تعرف أنه يحدث قبل أن يصلك ticket دعم».</p>
      <p>للمبدعين العرب: كل AI agency وSaaS في MENA يُطلق agents للعملاء — Agnost AI integration packages وArabic conversation analysis dashboards وmanaged agent QA retainers فرصة trust-as-a-service premium. «Conversation intelligence for agents» vertical ينمو — Agnost AI تُكافئ teams التي تُ prioritizes production quality على demo magic.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Agnost AI وثورة مراقبة محادثات الوكلاء؟</h3>
        <ul>
          <li><strong>Agnost AI integration packages:</strong> ربط Agnost بـ production agents — 2500–22000 دولار/مشروع.</li>
          <li><strong>Arabic agent QA dashboards:</strong> لوحات تحليل محادثات بالعربية — 1800–16000 دولار/لوحة.</li>
          <li><strong>Managed agent monitoring retainers:</strong> مراقبة وتحسين agents شهرياً — 3000–28000 دولار/شهر.</li>
          <li><strong>دورات «Catch Silent Agent Failures»:</strong> bootcamp لفرق المنتج — 59–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Agnost AI</span>
        <span class="tag">Agent Monitoring</span>
        <span class="tag">Silent Failures</span>
        <span class="tag">OpenTelemetry</span>
        <span class="tag">Product Hunt</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>beafk.app: workspace جوّال لـ AI coding agents — Claude Code وCodex وGrok وKimi في crew واحد تُوجّهه من هاتفك!</h2>
      <p class="article-lead">«الوكلاء يعملون — لكنك ما زلت تُنظّم يومك حول المكتب». في 29 أغسطس 2026، أطلقت <strong>beafk.app</strong> على Product Hunt — <strong>mobile-first workspace</strong> لتشغيل وتنسيق native AI coding agents على جهازك التطويري، مع التوجيه من الجوّال دون أن يغادر الكود والاعتمادات جهازك.</p>
      <p>المشكلة التي حلّتها: Claude Code وCodex وGrok Build وKimi Code يعملون بشكل مستقل — لكن المطوّر يبقى قرب الحاسوب لبدء الجلسات والإجابة على أسئلة الوكيل والتبديل بين الأدوات. beafk يُشغّل agents الأصليين على machine المطوّر، يُجمّعهم في coding session واحدة، ويسمح للـ lead agent بتفويض أجزاء المهمة لوكلاء آخرين — نماذج مختلفة لمهام مختلفة دون ملء context الوكيل الرئيسي.</p>
      <p>القدرات الأساسية: اتصال مباشر عبر Tailscale network مع شهادات قصيرة العمر — الكود ومحادثات الوكلاء والاعتمادات تبقى على جهازك. مزامنة skills وMCP servers عبر CLIs، workspaces للفرق مع audit log موقّع، تسعير حسب machines لا seats. Bogdan بنى المنتج 37 يوماً من جوّاله باستخدام beafk نفسه — «أردت أن أكون AFK وكنت AFK فعلاً أثناء البناء».</p>
      <p>للمبدعين العرب: كل remote dev team وAI agency في MENA يُريد ship من أي مكان — beafk setup packages وArabic mobile dev workflows وmanaged multi-agent retainers فرصة developer-tools premium. «Mobile-first agent orchestration» vertical ينمو — beafk تُكافئ teams التي تُريد freedom من desk-bound development.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من beafk.app وثورة التطوير الجوّالي بالوكلاء؟</h3>
        <ul>
          <li><strong>beafk team setup packages:</strong> إعداد workspaces وagents للفرق — 1500–12000 دولار/فريق.</li>
          <li><strong>Multi-agent workflow design:</strong> تصميم crews لوكلاء متخصصين — 2000–18000 دولار/workflow.</li>
          <li><strong>Managed mobile dev retainers:</strong> إدارة جلسات agents شهرياً — 2500–22000 دولار/شهر.</li>
          <li><strong>دورات «Ship Code from Your Phone with beafk»:</strong> bootcamp للمطورين — 49–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">beafk.app</span>
        <span class="tag">Mobile Coding</span>
        <span class="tag">Claude Code</span>
        <span class="tag">Multi-Agent</span>
        <span class="tag">Tailscale</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Firecrawl Developer Index: فهرس 70+ مليون مورد برمجي — README وissues وPRs وdocs في API وCLI وMCP واحد!</h2>
      <p class="article-lead">«وكلاء الترميز يحتاجون مصادر موثوقة — لا Google عشوائي». في 28 أغسطس 2026، احتل <strong>Firecrawl Developer Index</strong> مكاناً بارزاً على Product Hunt بـ 164 upvote — <strong>فهرس مُنسّق لأكثر من 70 مليون مورد برمجي</strong>: README وissues وpull requests وdocumentation على GitHub، عبر واجهة واحدة مُحسّنة للترميز.</p>
      <p>المشكلة التي حلّتها: coding agents وRAG pipelines تبحث في web عام أو docs مُشتتة — retrieval rate منخفض وزمن ضائع. Firecrawl Developer Index يُفتّش 70M+ entry عبر endpoint واحد `/v2/search/developer` — API وCLI وMCP جاهزة للتكامل مع أدوات الترميز المفضلة. بدون API key للبدء، أعلى retrieval rate في فئة coding-specific indexes.</p>
      <p>القدرات الأساسية: بحث موحّد في GitHub READMEs وissues وPRs وdocs، integration مع coding agents عبر MCP، CLI للـ terminal workflows، real-time access. Use cases: AI coding assistants تحتاج context دقيق من repos، developer research، agent toolchains — «أعطِ وكيلك مكتبة برمجية بـ 70 مليون صفحة بدلاً من 10 روابط Google».</p>
      <p>للمبدعين العرب: كل AI dev tool builder وconsulting firm في MENA يبني RAG للكود — Firecrawl integration packages وArabic developer search wrappers وmanaged coding-agent retainers فرصة infrastructure. «Developer knowledge index for agents» vertical ينمو — Firecrawl تُكافئ builders التي تُريد accuracy على speed.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Firecrawl Developer Index وثورة فهرسة المعرفة البرمجية؟</h3>
        <ul>
          <li><strong>Firecrawl MCP integration:</strong> ربط الفهرس بـ coding agents — 1800–15000 دولار/مشروع.</li>
          <li><strong>Custom developer RAG pipelines:</strong> pipelines بحث مُخصّصة للفرق — 2500–20000 دولار/pipeline.</li>
          <li><strong>Managed coding-agent retainers:</strong> agents مُغذّاة بـ Firecrawl شهرياً — 3000–25000 دولار/شهر.</li>
          <li><strong>دورات «Supercharge Coding Agents with Firecrawl»:</strong> bootcamp للمطورين — 49–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Firecrawl</span>
        <span class="tag">Developer Index</span>
        <span class="tag">MCP</span>
        <span class="tag">Coding Agents</span>
        <span class="tag">GitHub Search</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>screenpipe: ذاكرة محلية لجهازك — سجّل الشاشة والصوت والنشاط واسأل وكلاء MCP «ماذا قال في ذلك الاجتماع؟»</h2>
      <p class="article-lead">«لا تتذكر ما ناقشته صباحاً — screenpipe يتذكر». في 28 أغسطس 2026، احتل <strong>screenpipe</strong> مكاناً بارزاً على Product Hunt بـ 127 upvote — AI يُسجّل <strong>شاشتك وصوتك ونشاطك على الحاسوب</strong> محلياً، ثم يُتيح لوكلاء MCP الوصول للسجل — اسأل عن مكالمة أو bug أو document دون أن تُعيد بناء يومك من الذاكرة.</p>
      <p>المشكلة التي حلّتها: knowledge workers يُضيّعون ساعات في «أين رأيت ذلك؟» — meeting notes ناقصة، context مُشتت عبر tabs. screenpipe يسجّل screen وaudio وactivity بشكل local-first (Mac وWindows وLinux)، ثم يُغذّي AI agents عبر MCP — «ما الذي قاله العميل عن الموعد النهائي؟» «أين كان ذلك الخطأ في الكود؟» بدون manual recall.</p>
      <p>القدرات الأساسية: تسجيل مستمر local-first، MCP integration للوكلاء، cross-platform (Mac/Windows/Linux)، source-available. Use cases: consultants وfounders وdevelopers يحتاجون personal knowledge base من عملهم اليومي — «second brain» مبني على ما فعلته فعلاً لا ما كتبته. عرض إطلاق: BUSINESS20 لخصم 20% على الخطة السنوية.</p>
      <p>للمبدعين العرب: كل consultant وknowledge worker في MENA يُريد capture workflow — screenpipe setup packages وArabic MCP agent wrappers وmanaged personal-AI retainers فرصة productivity premium. «Local-first work memory for agents» vertical ينمو — screenpipe تُكافئ early adopters التي تُريد privacy مع power.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من screenpipe وثورة الذاكرة المحلية للعمل؟</h3>
        <ul>
          <li><strong>screenpipe setup packages:</strong> إعداد تسجيل وMCP للفرق — 800–8000 دولار/مشروع.</li>
          <li><strong>Personal AI memory workflows:</strong> workflows استعلام مُخصّصة — 1200–10000 دولار/workflow.</li>
          <li><strong>Managed work-memory retainers:</strong> صيانة وتحسين pipelines شهرياً — 1500–12000 دولار/شهر.</li>
          <li><strong>دورات «Build Your Work Memory with screenpipe»:</strong> bootcamp للمحترفين — 39–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">screenpipe</span>
        <span class="tag">Local-First AI</span>
        <span class="tag">MCP</span>
        <span class="tag">Work Memory</span>
        <span class="tag">Screen Recording</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 30-08-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="30-08-2026 -- 08-AM.html">
          📰 30 أغسطس 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Agnost AI · beafk.app · Firecrawl Developer Index · screenpipe</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "30-08-2026 -- 08-AM.html" not in content:
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
