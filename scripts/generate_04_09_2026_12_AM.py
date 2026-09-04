#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 04-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "04-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Atlas by World Labs، Tabbit AI، Lightfield، Grove، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 4 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Atlas by World Labs الذي يُحوّل النص والصور والفيديو ونماذج ثلاثية الأبعاد إلى فيديو HD بتحكم كامل بالكاميرا، إلى Tabbit AI المتصفح الذي يُنجز عملك عبر الويب ويُحوّله إلى Skills قابلة لإعادة التشغيل، ومن Lightfield الذي يبني CRM كاملاً من بريدك الإلكتروني دون إدخال يدوي، إلى Grove الذي يُوحّد أنت ووكيلك في terminal واحد — أربع ثورات تُعيد تشكيل الفيديو التوليدي والتصفح الذكي وإدارة العملاء والتطوير متعدد الوكلاء في 4 سبتمبر 2026!</h1>
      <p class="hero-sub">World Labs تُطلق omni world model بفيديو 1440p حتى دقيقة كاملة، Tabbit يُسلّم HTML وPDF وعروضاً تقديمية من مهام ويب مجدولة، Lightfield يملأ pipeline من محادثاتك الحقيقية، وGrove يُشغّل 10+ وكلاء برمجة بالتوازي عبر Git worktrees. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 4 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Atlas by World Labs: omni world model — من نص وصور وفيديو و3D إلى فيديو HD بتحكم كامل بالكاميرا!</h2>
      <p class="article-lead">«العالم لم يعد صورة ثابتة — أصبح مشهداً تُحرّكه الكاميرا». في 3 سبتمبر 2026، أُطلق <strong>Atlas</strong> من <strong>World Labs</strong> على Product Hunt — <strong>omni world model</strong> يأخذ نصاً أو صوراً أو فيديو أو نماذج ثلاثية الأبعاد ويُنتج فيديو بدقة 1440p حتى دقيقة كاملة مع تحكم كامل بحركة الكاميرا.</p>
      <p>المشكلة التي حلّتها: أدوات توليد الفيديو تُنتج لقطات قصيرة بزوايا عشوائية — لا يمكنك «توجيه» الكاميرا كما في إنتاج سينمائي حقيقي. Atlas يُعيد بناء المشاهد من بضع صور، يُحاكي space-time للروبوتات، ويُولّد فيديو camera-controlled — نفس المحرك الذي سيُشغّل Marble القادم من World Labs. الوصول المبكر متاح الآن للمبدعين والمطورين.</p>
      <p>القدرات الأساسية: text-to-video مع camera paths مخصصة؛ scene reconstruction من صور قليلة؛ تكامل 3D models؛ محاكاة space-time للتطبيقات الروبوتية؛ فيديو 1440p حتى 60 ثانية. Atlas ليس مجرد مولّد فيديو — إنه world model يفهم المكان والزمان ويُتيح لك «التجول» داخل المشهد كما تريد.</p>
      <p>للمبدعين العرب: كل استوديو إعلانات ووكالة تسويق وصانع محتوى في MENA يُريد فيديو product cinematic بلا تصوير ميداني — Atlas workflow packs وArabic prompt libraries وmanaged video production retainers فرصة creative premium. «Camera-controlled world models» vertical ينمو — World Labs تُكافئ creators التي تُسلّم scenes قابلة لإعادة الاستخدام لا clips عشوائية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atlas by World Labs وثورة world models؟</h3>
        <ul>
          <li><strong>Atlas cinematic packages:</strong> فيديو product وbrand بتحكم كاميرا — 2000–20000 دولار/مشروع.</li>
          <li><strong>3D-to-video pipelines:</strong> تحويل نماذج منتجات إلى فيديو ترويجي — 1500–12000 دولار/عميل.</li>
          <li><strong>Arabic prompt &amp; scene libraries:</strong> مكتبات جاهزة للأسواق العربية — 500–5000 دولار/pack.</li>
          <li><strong>دورات «Cinematic AI with Atlas»:</strong> bootcamp للمبدعين — 39–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">World Labs</span>
        <span class="tag">Atlas</span>
        <span class="tag">World Model</span>
        <span class="tag">Video AI</span>
        <span class="tag">3D</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Tabbit AI: المتصفح الذي يعرف ما تعمل عليه — وكيل ويب يُسلّم HTML وPDF وعروضاً تقديمية!</h2>
      <p class="article-lead">«المتصفح لم يعد نافذة — أصبح موظفاً». في 3 سبتمبر 2026، أُطلق <strong>Tabbit AI</strong> على Product Hunt — <strong>متصفح AI-native</strong> يعرف السياق الذي تعمل عليه: الصفحات المفتوحة، لقطات الشاشة، ملفات PDF والملفات المحلية — ويُشغّل Tabbit Agent عبر الويب الآن أو على schedule.</p>
      <p>المشكلة التي حلّتها: امتدادات AI على Chrome مجزّأة — تلخّص صفحة واحدة لكنها لا تُنجز مهاماً متعددة الخطوات عبر الويب. Tabbit يُدمج 10+ نماذج LLM (GPT-5.5، Claude 4.7، DeepSeek V4 وغيرها) في المتصفح نفسه، ويُسلّم HTML وPDF وpresentations جاهزة، ثم يحفظ workflow كـ Skill قابل لإعادة التشغيل. Agentic mode يخطّط البحث، يزور المواقع، يُصفّي المعلومات، ويُخرج تقريراً كاملاً من وصف بالعربية أو الإنجليزية.</p>
      <p>القدرات الأساسية: multi-agent workflows للبحث والكتابة والتحليل؛ @ references للتبويبات وPDF والملفات المحلية؛ skills marketplace لأتمتة المواقع الشائعة؛ on-device storage للخصوصية؛ استيراد من Chrome وEdge وSafari بنقرة واحدة؛ MCP tools وthird-party integrations. Tabbit V1.0 متاح مجاناً على Windows مع iOS وAndroid في beta.</p>
      <p>للمبدعين العرب: كل باحث ومحلل وصحفي ومسوّق في MENA يُريد research automation — Tabbit skill packs وArabic research workflows وmanaged browser automation retainers فرصة productivity premium. «AI browser that delivers» vertical ينمو — Tabbit تُكافئ builders التي تُحوّل Skills إلى خدمات قابلة للبيع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Tabbit AI وثورة المتصفح الذكي؟</h3>
        <ul>
          <li><strong>Tabbit Skill packs:</strong> workflows جاهزة للبحث والتقارير والتسويق — 800–8000 دولار/pack.</li>
          <li><strong>Research automation retainers:</strong> تقارير أسبوعية مجدولة — 1500–10000 دولار/شهر.</li>
          <li><strong>Arabic content intelligence:</strong> مراقبة مواقع وصحف عربية — 2000–15000 دولار/عميل.</li>
          <li><strong>دورات «Build Skills with Tabbit AI»:</strong> bootcamp — 29–199 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Tabbit AI</span>
        <span class="tag">AI Browser</span>
        <span class="tag">Agentic Web</span>
        <span class="tag">Skills</span>
        <span class="tag">Multi-LLM</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Lightfield: CRM يبني نفسه — من بريدك الإلكتروني إلى pipeline كامل دون إدخال يدوي!</h2>
      <p class="article-lead">«CRM الذي لا يُحدَّث يموت — Lightfield لا يطلب منك التحديث أبداً». في 3 سبتمبر 2026، أُطلق <strong>Lightfield</strong> على Product Hunt — <strong>CRM AI-native</strong> يبني ويُحدّث نفسه تلقائياً من emails وmeeting transcripts وcalendar data، بدون schema مسبق وبدون data entry.</p>
      <p>المشكلة التي حلّتها: 73% من فرق المبيعات تتخلى عن CRM خلال 90 يوماً — لأن إدخال البيانات يدوياً مملّ ومستحيل. Lightfield يقرأ inbox وcalendar وtranscripts، يستخرج contacts وdeal stages وcontext، ويبني pipeline كاملاً. اكتب «اذهب عبر بريدي واملأ opportunities» — وعد بعد دقائق لتجد pipeline مُعبّأ. schema-less: الحقول تظهر حسب ما تجده المحادثات، لا حسب ما تُعدّه مسبقاً.</p>
      <p>القدرات الأساسية: customer memory مستمرة من كل تفاعل؛ natural language queries بدل dashboards؛ draft follow-ups وboard decks وproposals بprompt واحد؛ import من CRM قديم عبر agent؛ 2400+ شركة مسجّلة. مؤسس Lightfield Keith Peiris — الذي بنى Instagram Direct إلى 500 مليون مستخدم وco-founded Tome (#1 على Product Hunt) — يُقدّم 3 أشهر مجاناً بكود PH3.</p>
      <p>للمبدعين العرب: كل founder-led sales team وstartup في MENA يُريد CRM يعمل فعلاً — Lightfield setup packages وArabic email parsing workflows وmanaged CRM retainers فرصة B2B premium. «Self-building CRM» vertical ينمو — Lightfield تُكافئ consultants التي تُسلّم pipelines حية لا spreadsheets فارغة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lightfield وثورة CRM الذاتي البناء؟</h3>
        <ul>
          <li><strong>Lightfield migration packages:</strong> نقل من HubSpot/Salesforce — 3000–25000 دولار/مشروع.</li>
          <li><strong>Founder sales CRM setup:</strong> inbox + pipeline + follow-up automation — 1500–12000 دولار/startup.</li>
          <li><strong>Managed CRM intelligence retainers:</strong> تقارير pipeline وdraft follow-ups — 2000–15000 دولار/شهر.</li>
          <li><strong>دورات «Zero-Entry CRM with Lightfield»:</strong> bootcamp لفرق المبيعات — 49–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lightfield</span>
        <span class="tag">AI CRM</span>
        <span class="tag">Self-Building</span>
        <span class="tag">Customer Memory</span>
        <span class="tag">Sales AI</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Grove: terminal واحد لك وللوكيل — 10+ وكلاء برمجة بالتوازي في workspace موحّد!</h2>
      <p class="article-lead">«لا تُبدّل بين 5 terminals — Grove يُوحّد أنت ووكيلك». في 3 سبتمبر 2026، أُطلق <strong>Grove</strong> على Product Hunt — <strong>workspace AI-native</strong> يُشغّل Claude Code وCodex وCursor وGemini وCopilot و8 وكلاء آخرين بالتوازي، كل task في Git worktree معزول، عبر terminal وweb IDE وnative GUI وvoice mobile.</p>
      <p>المشكلة التي حلّتها: developers يُشغّلون agents متعددة في terminals منفصلة — collisions وcontext leaks وno visibility. Grove يُوفّر Kanban-style TUI، Blitz view لمراقبة كل task نشط، Agent Graph (DAG من agents يتبادلون structured messages)، وMCP server يُتيح لأي agent إنشاء tasks وmerge branches وreply to reviews. Studio يُتيح لغير المبرمجين المشاركة عبر Sketch canvases وartifact review.</p>
      <p>القدرات الأساسية: 13 agent مدمج عبر ACP protocol؛ isolated Git worktrees لكل task؛ built-in MCP server (grove_create_task، grove_send_prompt، grove_complete_task)؛ skills marketplace بنقرة واحدة؛ single binary Rust (macOS/Windows/Linux)؛ voice walkie-talkie mode. Spec في Studio → dispatch لفريق agents → review بـ AI batch-fix → merge — workflow كامل في مكان واحد.</p>
      <p>للمبدعين العرب: كل dev shop وagency وfreelancer في MENA يُريد multi-agent productivity — Grove setup packages وArabic agent personas وmanaged dev workflow retainers فرصة developer premium. «Multi-agent IDE» vertical ينمو — Grove تُكافئ teams التي تُسلّم velocity لا chaos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Grove وثورة workspace متعدد الوكلاء؟</h3>
        <ul>
          <li><strong>Grove team setup packages:</strong> multi-agent workflows + MCP integration — 2500–20000 دولار/فريق.</li>
          <li><strong>Custom agent personas:</strong> reviewer وdoc writer وtest-first coder — 1000–8000 دولار/pack.</li>
          <li><strong>Managed multi-agent retainers:</strong> orchestration وvelocity reports — 3000–18000 دولار/شهر.</li>
          <li><strong>دورات «Ship Faster with Grove Multi-Agent IDE»:</strong> bootcamp — 59–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Grove</span>
        <span class="tag">Multi-Agent IDE</span>
        <span class="tag">ACP</span>
        <span class="tag">MCP</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 04-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="04-09-2026 -- 12-AM.html">
          📰 4 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Atlas by World Labs · Tabbit AI · Lightfield · Grove</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "04-09-2026 -- 12-AM.html" not in content:
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
