#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-07-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "23-07-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Atoms، Meshy، Arrakis، HeyMilo، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 يوليو 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من 1.7 مليار لروبوتات التعدين إلى 400 مليون لعوالم ثلاثية الأبعاد — الذكاء الاصطناعي يُحرّك المصانع والألعاب والتوظيف معاً!</h1>
      <p class="hero-sub">Atoms يُعيد Travis Kalanick إلى قصة bits-to-atoms بـ 1.7 مليار دولار، Meshy يُطلق 3D Agent لـ 12 مليون مستخدم، Arrakis يبني نظام تشغيل AI للمصانع بـ 38 مليون دولار، وHeyMilo يُغيّر التوظيف الجماعي بثلاثة agents جديدة. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 23 يوليو 2026</span>
        <span>🕗 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Atoms: 1.7 مليار دولار من a16z وUber — Travis Kalanick يُنهي قصة bits-to-atoms في التعدين والنقل والغذاء!</h2>
      <p class="article-lead">بعد Uber وCloudKitchens، يعود Travis Kalanick بفكرة أكبر: «wheelbase for robots» — منصة Industrial AI تجمع software وsensors وrobotics لتحويل الصناعات الثقيلة من mining إلى food production. a16z يقود 1.7 مليار دولار — وUber يعود للطاولة بعد 16 عاماً من رحلة digitize the physical world.</p>
      <p>في 22 يوليو 2026، أعلنت <strong>Atoms</strong> — شركة robotics وIndustrial AI التي أسسها <strong>Travis Kalanick</strong> — عن جولة تمويل بقيمة <strong>1.7 مليار دولار</strong> بقيادة <strong>Andreessen Horowitz (a16z)</strong>، مع Bain Capital وFifth Wall و<strong>Uber</strong> ضمن المستثمرين. <strong>Ben Horowitz</strong> ينضم لمجلس الإدارة.</p>
      <p>Kalanick يصف الجولة بـ «unfinished business»: «16 عاماً مضت وأنا أبدأ رحلة digitize the physical world — understand, predict and control the physical world with software». Atoms تبني ما تسميه <strong>Industrial AI</strong>: أتمتة physical operations في mining وconstruction وheavy transport وfood production — حيث CPU هو manufacturing وstorage هو real estate وnetwork هو transportation.</p>
      <p>الشركة استحوذت على <strong>Pronto</strong> — startup للقيادة الذاتية — لتعزيز قدراتها. Kalanick يقول: «أثمن شيء يمكن فعله بـ AI وrobotics هو تكرار ما فعله Uber للنقل — جعل كل شيء وكل شخص أكثر إنتاجية». التمويل equity وdebt — والشركة تدعو engineers وbuilders للانضمام. للمبدعين العرب: consulting لـ industrial automation MENA، integration لـ logistics وmining، ودورات «Physical AI للصناعات الثقيلة» — سوق industrial robotics يتجاوز 100 مليار دولار.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atoms وIndustrial AI؟</h3>
        <ul>
          <li><strong>Industrial automation consulting MENA:</strong> ساعد مصانع ومناجم محلية على تبني AI robotics — مشروع 25000–150000 دولار.</li>
          <li><strong>Logistics AI integration:</strong> اربط fleets وwarehouses بـ autonomous systems — 15000–80000 دولار.</li>
          <li><strong>دورات «Physical AI للصناعات»:</strong> bootcamp للمهندسين — 299–1499 دولار.</li>
          <li><strong>Arabic industrial AI content:</strong> newsletters عن automation في mining وfood — اشتراكات 12–59 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atoms</span>
        <span class="tag">Industrial AI</span>
        <span class="tag">Robotics</span>
        <span class="tag">Travis Kalanick</span>
        <span class="tag">a16z</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Meshy: 400 مليون دولار وvaluation 1.5 مليار — 3D Agent يُحوّل محادثة إلى نموذج جاهز للطباعة في دقيقة!</h2>
      <p class="article-lead">3D modeling كان يحتاج أياماً وspecialists باهظين. Meshy يقول: دقيقة واحدة وحوالي دولار — من text أو photo أو sketch إلى model print-ready. Series B بـ 400 مليون دولار — أكبر جولة AI 3D في التاريخ — و3D Agent يُغيّر game dev و3D printing وproduct design.</p>
      <p>في 21 يوليو 2026، أعلنت <strong>Meshy</strong> — من Silicon Valley — عن <strong>Series B بقيمة ~400 مليون دولار</strong> — valuation <strong>1.5 مليار دولار</strong> — أول valuation مُعلن للشركة. الجولة بقيادة <strong>IDG Capital</strong> و<strong>Matrix Partners China</strong> و<strong>Monolith Management</strong>، مع Granite Asia وHongShan وBAI Capital وSource Code Capital.</p>
      <p>الأرقام مذهلة: <strong>12 مليون مستخدم مسجل</strong>، ARR نما <strong>12× سنوياً</strong>، وأكثر من <strong>100 مليون model</strong> مُولّد. عملاء: <strong>Nexon</strong> و<strong>NetEase</strong> (gaming) و<strong>Bambu Lab</strong> و<strong>Creality</strong> (3D printing). المؤسس <strong>Ethan Hu</strong> (MIT PhD) يبني foundation models لـ AI-powered 3D generation.</p>
      <p><strong>Meshy 3D Agent</strong> — أول AI agent مخصص لـ 3D creation — يُحوّل conversation إلى FBX/OBJ/GLB/STL print-ready. يُ brainstorm ideas، يُولّد concepts في batches، ويُجيب أسئلة 3D عبر Q&A مدمج. slicer success rate حتى <strong>97%</strong> للطباعة؛ exports نظيفة لـ Unity وUnreal وBlender. منتجات جديدة: <strong>Auto Split</strong> (تقسيم للطباعة) و<strong>Smart Topology</strong> (mesh geometry). للمبدعين العرب: دورات 3D Agent، خدمات asset generation للألعاب العربية، وprint-on-demand stores — سوق AI 3D ينمو بسرعة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meshy وAI 3D؟</h3>
        <ul>
          <li><strong>Game asset generation services:</strong> أنشئ assets للألعاب العربية عبر Meshy 3D Agent — 500–5000 دولار/مشروع.</li>
          <li><strong>3D print-on-demand store:</strong> بع designs مُولّدة بـ AI — margin 30–70%.</li>
          <li><strong>دورات «من Chat إلى 3D Model»:</strong> workshop للمصممين — 99–499 دولار.</li>
          <li><strong>Product visualization consulting:</strong> حوّل sketches العملاء إلى models للـ e-commerce — 2000–12000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meshy</span>
        <span class="tag">3D Agent</span>
        <span class="tag">AI 3D</span>
        <span class="tag">Game Dev</span>
        <span class="tag">3D Printing</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Arrakis: 38 مليون دولار — نظام تشغيل AI للمصانع يُنشر agents في أسابيع لا سنوات!</h2>
      <p class="article-lead">معظم AI يذهب لـ chatbots في المكاتب. Arrakis يقول: أكبر عائد AI في factories وsupply chains — aerospace وenergy وlogistics وmanufacturing. Palantir alumni يبنون «operating system» model-agnostic يُنشر agents في weeks — valuation 140 مليون دولار بعد 7 أشهر فقط.</p>
      <p>في 22 يوليو 2026، خرجت <strong>Arrakis</strong> من stealth بـ <strong>38 مليون دولار</strong> إجمالي — <strong>Series A بـ 30 مليون</strong> بقيادة <strong>Blossom Capital</strong>، فوق seed بـ 7.5 مليون من <strong>Accel</strong>. Valuation <strong>140 مليون دولار post-money</strong>. المؤسس <strong>Rafael Quintanilla</strong> (ex-Accel VP) مع Haroun Beltaifa وRomain Fouilland (ex-Palantir) وMikhail Galkov (ex-Delivery Hero).</p>
      <p>Arrakis تُ deploy <strong>forward-deployed AI engineers</strong> داخل الشركات الصناعية — model-agnostic، تستخدم open-source من Mistral وغيرها. النتائج المُ claimed: <strong>2–4× improvement</strong> في output quality مع <strong>70% cut</strong> في token costs. عملاء NYSE-listed في energy وlogistics وindustrial sectors. استحوذت على <strong>Emmi</strong> لتعزيز industrial AI capabilities.</p>
      <p>مستثمرون angels: <strong>Olivier Pomel</strong> (Datadog CEO) و<strong>Olivier Godement</strong> (OpenAI head of business products) وJunaid Hussain (Cambridge Aerospace). التوسع المُخطّط: مكاتب في New York والشرق الأوسط. Quintanilla يقول: Palantir legacy player ripe for disruption — consulting firms تُ charge headcount لا outcomes. للمبدعين العرب: industrial AI deployment partner، training لـ manufacturing teams، وArabic content عن «AI في المصانع».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Arrakis وAI الصناعي؟</h3>
        <ul>
          <li><strong>Industrial AI deployment MENA:</strong> ساعد مصانع محلية على نشر agents — مشروع 20000–100000 دولار.</li>
          <li><strong>Supply chain AI consulting:</strong> optimize logistics وinventory بـ agentic AI — 15000–75000 دولار.</li>
          <li><strong>دورات «Agentic AI للمصانع»:</strong> workshop للـ operations managers — 249–1199 دولار.</li>
          <li><strong>Arabic industrial case studies:</strong> content عن AI في aerospace وenergy — اشتراكات 10–49 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Arrakis</span>
        <span class="tag">Industrial AI</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Manufacturing</span>
        <span class="tag">Palantir Alternative</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>HeyMilo: 6 مليون دولار — ثلاثة agents جديدة تُغيّر التوظيف الجماعي وتكشف من يُجيد استخدام AI!</h2>
      <p class="article-lead">السير الذاتية أصبحت مُولّدة بـ ChatGPT — والمقابلات generic لا تكشف المهارات الحقيقية. HeyMilo يبني agentic recruiting: AI Scenario Assessment يُختبر كيف يخطط المرشح ويُ prompt ويُقيّم output الـ AI؛ Candidate Recommendations يُعيد تفعيل applicants من ATS؛ Notetaker يُ capture structured notes.</p>
      <p>في يونيو 2026، أعلنت <strong>HeyMilo AI</strong> — من New York — عن إجمالي تمويل <strong>6 مليون دولار</strong> بقيادة <strong>Category Ventures</strong>، مع Canaan Partners وAlumni Ventures وERA. المؤسسان <strong>Sabashan Ragavan</strong> و<strong>Ramie Raufdeen</strong> (2023) يبنون platform لـ high-volume hiring.</p>
      <p>عملاء: <strong>Randstad</strong> و<strong>WilsonHCG</strong> و<strong>Neo Financial</strong> — staffing agencies وRPOs وenterprise employers. المنصة <strong>screened أكثر من مليون candidate</strong> في production عبر staffing وBPO وcorporate hiring. المشكلة التي تحلها: candidates يستخدمون generative AI لكتابة perfect resumes والتظاهر في initial screens.</p>
      <p><strong>AI Scenario Assessment</strong>: scenario حي مع AI assistant مدمج — rubric-scoring لـ planning وprompting وevaluating AI output. <strong>Candidate Recommendations</strong>: يُ dig في ATS ويُعيد ranked shortlists من cycles سابقة. <strong>Notetaker</strong>: structured notes موحّدة عبر live recruiter-led interviews. HeyMilo تُ expand engineering وoperations وتُ accelerate multilingual pipelines. للمبدعين العرب: HR tech consulting، Arabic recruiting automation، ودورات «AI Skills Assessment للموارد البشرية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HeyMilo وagentic recruiting؟</h3>
        <ul>
          <li><strong>HR tech implementation MENA:</strong> نشر HeyMilo أو similar للشركات الكبرى — مشروع 8000–40000 دولار.</li>
          <li><strong>AI skills assessment design:</strong> صمّم scenarios مخصصة للسوق العربي — 3000–15000 دولار.</li>
          <li><strong>دورات «Agentic Recruiting للـ HR»:</strong> bootcamp لـ talent acquisition teams — 149–699 دولار.</li>
          <li><strong>Staffing agency automation:</strong> retainer لـ high-volume hiring workflows — 2000–12000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HeyMilo</span>
        <span class="tag">Agentic Recruiting</span>
        <span class="tag">HR Tech</span>
        <span class="tag">AI Assessment</span>
        <span class="tag">High-Volume Hiring</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-07-2026 -- 08-AM</p>
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
