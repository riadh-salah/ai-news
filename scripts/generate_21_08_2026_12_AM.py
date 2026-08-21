#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "21-08-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Zephyr TAP، Suplari Data Assistant، MiniMax Design، Dulo، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من مساحة عمل وكلاء متعددة على سطح المكتب إلى فيديو كامل بأمر واحد ونماذج أساسية لتصميم الأجهزة — أربع ثورات تُعيد تشكيل الإنتاج والمشتريات والإبداع في 21 أغسطس 2026!</h1>
      <p class="hero-sub">Zephyr يُطلق The AI Platform للتوافر العام — مساحة عمل desktop حيث البشر والوكلاء يتعاونون في قنوات مشتركة، Suplari يُطلق Data Assistant الذي يملك دورة حياة بيانات المشتريات بالكامل، MiniMax Design يُحوّل نموذج H3 إلى استوديو فيديو متكامل بأربعة وكلاء متخصصين، ومؤسس Waymo سيباستيان ثرون يكشف عن Dulo — startup stealth لنماذج أساسية لتصميم الأجهزة. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 21 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Zephyr TAP: مساحة عمل وكلاء متعددة على سطح المكتب — من فكرة إلى mini-app إنتاجي في دقائق!</h2>
      <p class="article-lead">«الذكاء الاصطناعي لم يعد نافذة chatbot منفصلة — بل مكان العمل نفسه». في 20 أغسطس 2026، أعلنت Zephyr عن <strong>general availability</strong> لـ <strong>The AI Platform (TAP)</strong>: تطبيق desktop حيث فرق كاملة تتعاون مع متخصصي AI في قنوات مشتركة — بعد خمسة أشهر من early access.</p>
      <p>المنصة مبنية على مفهومين: <strong>Channels</strong> — غرف على طراز Slack حيث البشر والوكلاء يعملون جنباً إلى جنب — و<strong>Specialists</strong> — وكلاء قابلون لإعادة الاستخدام مع أدوار وتعليمات وأدوات ومعرفة دائمة مدعومة بسجل benchmarks لا prompts مؤقتة. <strong>Model Router</strong> provider-agnostic يُوجّه عبر OpenRouter وOpenAI وAnthropic Claude وGoogle Gemini وAWS Bedrock وendpoints محلية — بدون vendor lock-in.</p>
      <p>الجوهر: <strong>Mini-App Builder</strong>. أي workflow أو تجربة تُبنى داخل TAP تصبح تطبيقاً AI-enabled يمكن للشركة تثبيته. Zephyr تستخدم Module Federation مفتوح المصدر — أكثر من <strong>49 مليون npm download شهرياً</strong> — لتشغيل mini-apps. عمليات المبيعات والمحتوى والجدولة في Zephyr نفسها تعمل كـ mini-apps على المنصة.</p>
      <p>TAP متاح اليوم على macOS وWindows وLinux على theaiplatform.app. للمبدعين العرب: كل agency وstartup SaaS في MENA تبني workflows مخصصة — TAP mini-app consulting وArabic specialist templates وModel Router optimization services فرصة قبل saturation. Zephyr CEO Zack Chapple يُؤكد: «لأول مرة، بنية تحتية production-grade متاحة مباشرة من workspace يُبني أي شيء».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zephyr TAP وثورة multi-agent workspace؟</h3>
        <ul>
          <li><strong>TAP deployment consulting:</strong> إعداد المنصة للفرق — 5000–35000 دولار/مشروع.</li>
          <li><strong>Custom mini-app development:</strong> بناء تطبيقات AI-enabled على TAP — 8000–50000 دولار.</li>
          <li><strong>Arabic specialist templates:</strong> وكلاء متخصصون بالعربية جاهزون — 39–179 دولار/شهر.</li>
          <li><strong>دورات «Multi-Agent Workspaces with TAP»:</strong> bootcamp للفرق — 149–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zephyr TAP</span>
        <span class="tag">Multi-Agent Workspace</span>
        <span class="tag">Mini-App Builder</span>
        <span class="tag">Model Router</span>
        <span class="tag">Module Federation</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Suplari Data Assistant: وكيل AI يملك دورة حياة بيانات المشتريات — ويُصلّح الموصلات عندما تنكسر!</h2>
      <p class="article-lead">«الموصلات تنكسر دائماً — وهذا بالضبط العمل الذي يتفوق فيه هذا الوكيل». في 20 أغسطس 2026، أطلقت Suplari <strong>Data Assistant</strong>: وكيل AI يملك دورة حياة ingestion وtransformation لبيانات المشتريات بالكامل — من القراءة إلى التصحيح إلى إصلاح الموصلات.</p>
      <p>الوكيل يقبل Excel وCSV وWord وPDF وzip archives — بما فيها مجموعات bulk من عقود PDF. البيانات تصل ثلاث طرق: إرسال مباشر، push عبر API integration، أو pull عبر Suplari connector من ERP أو P2P platform. الوكيل يُحدّد محتوى كل ملف ووجهته — <strong>بدون mapping template</strong>.</p>
      <p>عند خطأ أو drift أو handoff: الوكيل يُصلّح ما يستطيع. فقط الغموض الحقيقي يصل للإنسان — كسؤال محدد لا error code. كل إجابة يُطبّقها الوكيل على الدورات المستقبلية، فحجم التدخل <strong>ينخفض مع الوقت</strong>. الوكيل يراقب كل connector لـ data drift وتغيّر هيكلي — عند الانكسار يُصلّح ويُحدّث الموصل. Pipelines تبقى live عبر schema changes.</p>
      <p>CEO Jeff Gerber: «أتمتنا data ingestion لسنوات. ما اختلف الآن أن الوكيل يملك lifecycle كاملاً». للمبدعين العرب: كل شركة enterprise في MENA لديها procurement data mess — Suplari setup consulting وArabic procurement data playbooks وmanaged data pipeline retainers فرصة ضخمة في قطاعات oil & gas وretail وmanufacturing.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Suplari Data Assistant وثورة agentic procurement؟</h3>
        <ul>
          <li><strong>Procurement data setup:</strong> إعداد Suplari للمؤسسات — 10000–55000 دولار/مشروع.</li>
          <li><strong>Connector remediation services:</strong> صيانة pipelines بيانات المشتريات — 3000–20000 دولار/سنة.</li>
          <li><strong>Arabic procurement playbooks:</strong> أدلة أتمتة مشتريات بالعربية — 49–199 دولار/شهر.</li>
          <li><strong>دورات «AI Procurement Data Management»:</strong> bootcamp لفرق المشتريات — 199–899 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Suplari</span>
        <span class="tag">Data Assistant</span>
        <span class="tag">Procurement AI</span>
        <span class="tag">Agentic Data</span>
        <span class="tag">Connector Repair</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>MiniMax Design: من «تحريك البكسل» إلى «تحريك المعنى» — فيلم كامل بأربعة وكلاء ونموذج H3!</h2>
      <p class="article-lead">«لم تعد تحتاج تحرير frame بframe — فقط صف نيتك الإبداعية». في 20 أغسطس 2026، أطلقت MiniMax <strong>MiniMax Design</strong>: منصة إبداع AI-native مبنية على نموذج H3 متعدد الوسائط — تُحوّل intent بلغة طبيعية إلى فيديو كامل من script إلى storyboard إلى music إلى editing.</p>
      <p>التحول: من «manipulating pixels» إلى <strong>manipulating semantics</strong>. H3 يفهم سياق مشروع كامل — scripts وcharacter assets وإصدارات سابقة وتفضيلات style. أربعة وكلاء متخصصون ينطلقون بالتوازي: <strong>Copy Agent</strong> للنصوص، <strong>Image Agent</strong> للمرئيات، <strong>Video Agent</strong> للـ timeline، <strong>Audio Agent</strong> للتعليق الصوتي.</p>
      <p>ميزة <strong>Agent 3D Director</strong>: تصف المشهد ومتطلبات الكاميرا بلغة طبيعية — النظام يعرض composition وعلاقات الشخصيات في 3D قبل أن يُولّد H3 الفيديو. Trial-and-error ينتقل لمرحلة storyboard. H3 يُنتج clips حتى 15 ثانية — Design يُجمّعها في أفلام 42 ثانية أو دقيقة أو 3 دقائق مع consistency في الشخصيات والإضاءة والكاميرا.</p>
      <p>يدعم ComfyUI workflows محلية — Agent يُساعد في ضبط nodes وparameters. يستهدف brand TVC وe-commerce content وshort dramas وknowledge videos. للمبدعين العرب: كل agency إعلانية وcreator في MENA يحتاج video at scale — MiniMax Design setup consulting وArabic video production playbooks وmanaged content retainers فرصة قبل competition.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من MiniMax Design وثورة agentic video production؟</h3>
        <ul>
          <li><strong>AI video production agency:</strong> إنتاج فيديو تجاري بـ Design — 2000–25000 دولار/مشروع.</li>
          <li><strong>Brand content packages:</strong> حملات فيديو + posters + copy — 5000–40000 دولار/حملة.</li>
          <li><strong>Arabic video templates library:</strong> قوالب فيديو عربية جاهزة — 29–149 دولار/شهر.</li>
          <li><strong>دورات «AI Video Production with MiniMax Design»:</strong> bootcamp للمبدعين — 99–599 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">MiniMax Design</span>
        <span class="tag">H3 Model</span>
        <span class="tag">Agentic Video</span>
        <span class="tag">3D Director</span>
        <span class="tag">Multimodal AI</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Dulo: سيباستيان ثرون مؤسس Waymo يكشف startup stealth — نماذج أساسية لتصميم الأجهزة وتصنيع بسرعة الضوء!</h2>
      <p class="article-lead">«الموجة القادمة ليست software-only — بل AI يُصمّم الأجهزة نفسها». في 18 أغسطس 2026، كشف سيباستيان ثرون — مؤسس Google self-driving project وWaymo وUdacity — عن <strong>Dulo</strong> في نهاية keynote في مؤتمر Actuate للروبوتات في San Francisco: startup stealth صغير لكنه في قلب الروبوتات.</p>
      <p>الموقع الرسمي يصف Dulo ببناء <strong>foundation models for hardware design</strong> — الهدف: <strong>manufacturing at lightspeed</strong>. الفكرة: تطبيق نفس منطق foundation models التي حوّلت text وimages وcode على تصميم وإنتاج الآلات والمكونات الفيزيائية. العملاء: <strong>مصنّعو الآلات</strong> لا end users — positioning B2B يُميّز Dulo عن منافسين يركزون على humanoid robots.</p>
      <p>الفريق: قادة من Waymo وGoogle Brain وStanford Artificial Intelligence Laboratory (SAIL) الذي أدارها Thrun سابقاً. Thrun co-founded Google Brain وGoogle X — وقاد Stanford team لإكمال 132-mile autonomous desert course في 2005 قبل أن يُوظّفه Larry Page لقيادة مشروع القيادة الذاتية الذي أصبح Waymo.</p>
      <p>لا funding معلن ولا product timeline — لكن roster من veterans في AI والautonomy يجعل Dulo من أكثر stealth startups مراقبة في 2026. للمبدعين العرب: كل manufacturer وengineering firm في MENA يستكشف AI-assisted design — Dulo readiness consulting وArabic hardware design playbooks وmanufacturing AI strategy services فرصة مبكرة قبل product launch.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dulo وثورة AI hardware design؟</h3>
        <ul>
          <li><strong>Manufacturing AI strategy:</strong> استشارات تبنّي AI في التصميم — 8000–45000 دولار/مشروع.</li>
          <li><strong>Hardware design workflow audits:</strong> تقييم جاهزية CAD/CAE للـ AI — 5000–25000 دولار.</li>
          <li><strong>Arabic engineering AI guides:</strong> أدلة تصميم أجهزة بالذكاء الاصطناعي — 49–249 دولار/شهر.</li>
          <li><strong>دورات «AI for Hardware Design»:</strong> bootcamp للمهندسين — 199–999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dulo</span>
        <span class="tag">Sebastian Thrun</span>
        <span class="tag">Hardware Design</span>
        <span class="tag">Foundation Models</span>
        <span class="tag">Robotics</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-08-2026 -- 12-AM</p>
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
