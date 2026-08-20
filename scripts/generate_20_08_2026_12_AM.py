#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 20-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "20-08-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Veeda AI، Codistry، Medly AI، Synthefy Nori، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 20 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من نماذج العالم الفيزيائي بـ 90 مليون دولار إلى Nori الذي يُغيّر قواعد الأرقام — أربع ثورات تُعيد تشكيل الذكاء والتعليم والبرمجة في 20 أغسطس 2026!</h1>
      <p class="hero-sub">Veeda AI يخرج من Stealth بـ 90 مليون دولار لبناء world models للذكاء الفيزيائي، Codistry يقطع تكلفة البرمجة بالذكاء الاصطناعي إلى النصف، Medly AI يجمع 8 ملايين دولار لتعليم مخصص لـ 400 ألف طالب، وSynthefy يُطلق Nori — أول foundation model مفتوح للبيانات الرقمية يُنافس XGBoost بدون تدريب. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 20 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Veeda AI: 90 مليون دولار من Stealth — نماذج العالم التي تُعلّم الروبوتات «فهم الواقع»!</h2>
      <p class="article-lead">تخيّل ذكاءً اصطناعياً لا يكتفي بقراءة النصوص — بل يبني نموذجاً حياً للعالم المادي: فيزياء، أجسام، حركة، سببية. في يونيو 2026، خرجت Veeda AI من الستائر بـ أكثر من 90 مليون دولار seed — من أكبر جولات Seed في تاريخ كندا — بقيادة Radical Ventures وKhosla Ventures.</p>
      <p>تأسست <strong>Veeda AI</strong> (قانونياً Veeda Innovation) على يد ثلاثة باحثين بارزين من NVIDIA: <strong>Sanja Fidler</strong> (CEO وأستاذة في University of Toronto)، <strong>Huan Ling</strong> (Chief Scientist)، و<strong>Zan Gojcic</strong> (CTO ومدير بحث سابق في NVIDIA Zurich). Fidler كانت من نجوم NVIDIA Toronto AI Lab — والآن تبني <strong>world models</strong> للذكاء الفيزيائي: روبوتات، سيارات ذاتية، محاكاة صناعية.</p>
      <p>الفكرة الجوهرية: بينما LLMs تفهم اللغة، <strong>world models</strong> تفهم <strong>الواقع</strong> — كيف تتحرك الأشياء، ماذا يحدث عند التصادم، كيف تتفاعل الأجسام في 3D. هذا ما يحتاجه أي نظام AI يتحرك في العالم الحقيقي: من humanoid robots إلى autonomous vehicles إلى digital twins للمصانع.</p>
      <p>الجولة أصدرت 60.6 مليون سهم بسعر دولار واحد — وRadical partner Tomi Poutanen وKhosla partner Sven Strohband انضما للمجلس. Veeda ينضم لموجة «neolabs» — باحثون نجوم يغادرون عمالقة التقنية لبناء foundation models خاصة. للمبدعين العرب: كل شركة robotics وlogistics وmanufacturing في MENA تبحث عن simulation وworld models — consulting وArabic physical AI reports وintegration services فرصة قبل أن تُغلق waitlist.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Veeda AI وثورة world models؟</h3>
        <ul>
          <li><strong>Physical AI consulting:</strong> تقييم وتخطيط world models للشركات الصناعية — 15000–75000 دولار/مشروع.</li>
          <li><strong>Simulation integration services:</strong> ربط world models بأنظمة robotics وlogistics — 10000–50000 دولار.</li>
          <li><strong>Arabic physical AI newsletter:</strong> نشرة أسبوعية عن robotics وworld models — 19–99 دولار/شهر.</li>
          <li><strong>دورات «World Models for Engineers»:</strong> bootcamp للمهندسين — 249–1299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Veeda AI</span>
        <span class="tag">World Models</span>
        <span class="tag">Sanja Fidler</span>
        <span class="tag">Physical AI</span>
        <span class="tag">$90M Seed</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Codistry: منصة برمجة AI تُقطع تكلفة التطوير إلى النصف — Context Engine يُغيّر قواعد اللعبة!</h2>
      <p class="article-lead">«المشكلة ليست في النموذج — بل في السياق». Adronite أطلقت Codistry في 19 أغسطس 2026: منصة برمجة AI للمؤسسات الكبيرة، تستخدم Context Engine (ACE) المُسجّل براءة اختراع — خريطة علاقية للكود تُحدّث نفسها تلقائياً وتُرسل للنموذج فقط ما يحتاجه المهمة.</p>
      <p>تأسست <strong>Adronite</strong> في Seattle 2023، وCEO الجديد <strong>Chris Colleran</strong> (ex-Impinj) قاد Series A بـ 5 ملايين دولار من Gatemore في فبراير. <strong>Codistry</strong> يستهدف enterprise codebases الضخمة — حيث Claude Code وCopilot يُغرقون النماذج بسياق غير ضروري.</p>
      <p>ACE يبني relational map للمستودع عند التثبيت — بدون تحضير مسبق. عند كل مهمة، النموذج يحصل فقط على الأجزاء ذات الصلة. Benchmarks داخلية: Codistry استخدم <strong>نصف tokens</strong> تقريباً مقارنة بـ Claude Code على مهام متطابقة (Claude Opus 4.8) — وتكلفة أقل بنسبة 48%. على مشروع PocketBase مفتوح المصدر: من 2.12 دولار إلى 1.10 دولار لكل مهمة.</p>
      <p>المنصة تدعم frontier models وopen-weight models على خوادم محلية — مهم للشركات التي لا تريد إرسال الكود لـ endpoints خارجية. Adronite تُطلق تحدي 72 ساعة للمطورين: بناء web app تفاعلي من token budget ثابت — الجائزة الأولى 5000 دولار. للمبدعين العرب: كل fintech وbank وenterprise في MENA يبحث عن AI coding آمن واقتصادي — Codistry setup consulting وArabic enterprise coding guides فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Codistry وثورة context-efficient coding؟</h3>
        <ul>
          <li><strong>Enterprise AI coding setup:</strong> نشر Codistry للفرق التقنية — 8000–40000 دولار/مشروع.</li>
          <li><strong>Context optimization audits:</strong> تحليل وتقليل token costs للشركات — 5000–25000 دولار.</li>
          <li><strong>Arabic enterprise coding guides:</strong> أدلة prompts عربية لـ Codistry — 49–199 دولار/شهر.</li>
          <li><strong>دورات «Efficient AI Coding for Teams»:</strong> bootcamp للمطورين — 149–699 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Codistry</span>
        <span class="tag">Adronite</span>
        <span class="tag">Context Engine</span>
        <span class="tag">Enterprise Coding</span>
        <span class="tag">48% Cost Cut</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Medly AI: 8 ملايين دولار — مُعلّم ذكي يُحضّر 400 ألف طالب للامتحانات بساعة يومياً!</h2>
      <p class="article-lead">«التعليم الشخصي لم يعد حكراً على الأثرياء». Medly AI جمعت 8 ملايين دولار seed في 19 أغسطس 2026 بقيادة Felix Capital — لتوسيع منصة تعليم امتحانات مدعومة بالذكاء الاصطناعي في UK والأسواق الدولية. من إطلاقها في فبراير 2025: أكثر من 400 ألف مستخدم، وساعة استخدام يومياً في المتوسط.</p>
      <p>أسسها خريجا UCL Medicine <strong>Dr Paul Jung</strong> و<strong>Dr Kavi Samra</strong>. <strong>Medly</strong> ليست chatbot عام — بل tutor متخصص في امتحانات GCSE وSAT وAP وACT. يستخدم مزيجاً من <strong>7 LLMs</strong> مع approaches من cognitive science وteaching theory — يتتبع نقاط ضعف الطالب وأنماط التعلم ويُكيّف الشرح accordingly.</p>
      <p>النتائج: طلاب GCSE الذين استخدموا المنصة حققوا تحسناً في النتائج — وتجربة جارية على أكثر من 1000 طالب لقياس الأثر على التحصيل. التوسع الدولي بدأ: SAT في US، وAP وACT بنهاية 2026. المستثمرون: Eka Ventures وAda Ventures وangels من InvestEngine وLearnLaunch وEpisode 1.</p>
      <p>السوق: edtech AI في ازدهار — من Khan Academy إلى Duolingo Max. Medly تركز على <strong>exam prep</strong> — niche عالي القيمة حيث الأهالي يدفعون premium. للمبدعين العرب: كل parent وschool في MENA يبحث عن دعم امتحانات — Arabic exam prep AI setup وlocalized tutoring content وpartnership مع مدارس فرصة ضخمة قبل saturation.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Medly AI وثورة AI tutoring؟</h3>
        <ul>
          <li><strong>Arabic exam prep platform:</strong> بناء tutor AI لامتحانات عربية (ثانوية، تحصيلي) — 5000–30000 دولار/مشروع.</li>
          <li><strong>School AI tutoring integration:</strong> ربط Medly-like solutions بالمدارس — 3000–20000 دولار.</li>
          <li><strong>Localized tutoring content:</strong> محتوى تعليمي عربي متوافق مع AI tutors — 99–499 دولار/شهر.</li>
          <li><strong>دورات «AI Tutoring for Educators»:</strong> bootcamp للمعلمين — 99–499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Medly AI</span>
        <span class="tag">AI Tutoring</span>
        <span class="tag">Exam Prep</span>
        <span class="tag">EdTech</span>
        <span class="tag">$8M Seed</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Synthefy Nori: 6.5 مليون دولار — foundation model للأرقام يُنافس XGBoost بدون تدريب!</h2>
      <p class="article-lead">«ماذا لو كان للأرقام ما فعلته LLMs للكلمات؟» Synthefy أعلنت في 18 أغسطس 2026 عن 6.5 مليون دولار seed بقيادة Wing Venture Capital — لبناء Structured Data Foundation Models (SDFMs) للبيانات الرقمية والجداول والمعاملات التي تُشغّل الاقتصاد الحقيقي.</p>
      <p>منتجها الرئيسي <strong>Nori</strong>: أول tabular foundation model مفتوح المصدر بالكامل — 6 ملايين parameters، <strong>zero training</strong>، و#1 mean R² على benchmark من 96 dataset للانحدار. بدلاً من بناء وتدريب model منفصل لكل مشكلة — تُعطي Nori بياناتك كـ context ويُنبئ. «Train nothing, predict anything».</p>
      <p>التحميلات تجاوزت <strong>600 ألف</strong> خلال أسابيع من الإطلاق. Nori Flash: نسخة MLP مُقطّرة تعمل على CPUs في microseconds — آلاف المرات أسرع وأرخص. Glass-box interpretability: استخراج reasoning من black-box model إلى model شفاف قابل للقراءة. المستثمرون: Haystack وSamsung Next وCanonical وLightscape — وangels من OpenAI وMicrosoft وMeta (Srinivas Narayanan، Aparna Chennapragada، Manohar Paluri).</p>
      <p>الفريق من Meta وNVIDIA وAdobe وUber. الرهان: 80% من بيانات المؤسسات structured/numerical — وليس نصاً. XGBoost وLightGBM dominated لعقود — Nori يُغيّر المعادلة. للمبدعين العرب: كل bank وretail وlogistics في MENA يملك tabular data — Nori integration consulting وArabic data science courses وSDFM adoption services فرصة قبل mainstream.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Synthefy Nori وثورة structured data AI؟</h3>
        <ul>
          <li><strong>Nori integration consulting:</strong> نشر Nori لتحليلات الشركات — 5000–35000 دولار/مشروع.</li>
          <li><strong>Tabular AI migration:</strong> استبدال XGBoost pipelines بـ Nori — 8000–45000 دولار.</li>
          <li><strong>Arabic data science courses:</strong> دورات Nori وSDFMs بالعربية — 49–299 دولار.</li>
          <li><strong>Industry SDFM reports:</strong> تقارير تطبيق Nori في finance وretail — 2000–15000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Synthefy</span>
        <span class="tag">Nori</span>
        <span class="tag">Structured Data</span>
        <span class="tag">Tabular AI</span>
        <span class="tag">$6.5M Seed</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 20-08-2026 -- 12-AM</p>
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
