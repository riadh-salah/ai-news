#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-07-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "23-07-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Atoms، Meshy، Arrakis، HeyMilo، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 يوليو 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من 1.7 مليار دولار لـ Industrial AI إلى 400 مليون لـ 3D — الذكاء الاصطناعي يُعيد تشكيل المصانع والروبوتات والتوظيف!</h1>
      <p class="hero-sub">Atoms يجمع 1.7 مليار دولار لـ «wheelbase للروبوتات»، Meshy يُصبح أول يونيكورn AI 3D بـ 400 مليون دولار، Arrakis يبني نظام تشغيل agentic للصناعة الثقيلة، وHeyMilo يُطلق agentic recruiting بـ 6 ملايين دولار. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 23 يوليو 2026</span>
        <span>🕓 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Atoms: 1.7 مليار دولار من a16z وUber — Travis Kalanick يبني «Industrial AI» لتحويل التعدين والنقل والطعام!</h2>
      <p class="article-lead">بعد Uber وCloudKitchens، Travis Kalanick يعود بـ vision أكبر: «bits-to-atoms» — فهم العالم المادي، التنبؤ به، والتحكم فيه بالبرمجيات. Atoms ليست startup روبوتات عادية؛ إنها محاولة لبناء wheelbase للآلات التي ستُعيد تشغيل اقتصادات ثقيلة عمرها قرون.</p>
      <p>في 22 يوليو 2026، أعلنت <strong>Atoms</strong> — شركة <strong>Travis Kalanick</strong> للروبوتات والـ Industrial AI — عن جولة تمويل بقيمة <strong>1.7 مليار دولار</strong> بقيادة <strong>Andreessen Horowitz</strong>، مع مشاركة <strong>Bain Capital</strong> و<strong>Fifth Wall</strong> و<strong>Uber</strong> — إعادة اتصال Kalanick بشركته الأولى بعد سنوات. <strong>Ben Horowitz</strong> ينضم للـ board.</p>
      <p>الشركة تبني <strong>Industrial AI</strong>: مزيج من software وsensors وrobotics وAI لأتمتة عمليات في <strong>mining</strong> و<strong>construction</strong> و<strong>heavy transport</strong> و<strong>food production</strong>. Kalanick يقول: «أغلى شيء يمكن فعله بالـ AI والروبوتات هو تكرار ما فعله Uber للنقل — جعل كل شيء وكل شخص أكثر إنتاجية». Atoms استحوذت أيضاً على <strong>Pronto</strong> — startup للقيادة الذاتية — لتعزيز قدراتها.</p>
      <p>الرؤية: «atoms-based computers» حيث CPU هو التصنيع، storage هو real estate، وnetwork هو النقل. التمويل equity + debt يُمكّن Atoms من توسيع deployments وmanufacturing simultaneously. للمبدعين العرب: consulting لـ industrial automation MENA، integration partners للـ logistics/mining، ودورات «Physical AI للصناعة» — عصر البرمجيات ينتقل من الشاشة إلى المصنع.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Atoms وموجة Industrial AI؟</h3>
        <ul>
          <li><strong>Industrial automation consulting:</strong> ساعد مصانع وlogistics MENA على roadmap للـ physical AI — مشروع 25000–150000 دولار.</li>
          <li><strong>Sensor + AI integration:</strong> اربط IoT sensors بـ agentic workflows للصناعة — 15000–80000 دولار.</li>
          <li><strong>دورات «Physical AI للمؤسسات»:</strong> workshop للـ operations managers — 299–1499 دولار.</li>
          <li><strong>MENA deployment partner:</strong> كن reseller/integrator لحلول robotics في mining وtransport — retainer 5000–30000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Atoms</span>
        <span class="tag">Industrial AI</span>
        <span class="tag">Travis Kalanick</span>
        <span class="tag">Robotics</span>
        <span class="tag">$1.7B</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Meshy: 400 مليون دولار وvaluation 1.5 مليار — أكبر جولة AI 3D في التاريخ و12 مليون مستخدم!</h2>
      <p class="article-lead">النص والصورة أصبحا يُولّدان فيديوهات وصوراً — لكن العالم ثلاثي الأبعاد ظلّ bottleneck: modeling يدوي، أدوات معقدة، وأسابيع من العمل. Meshy يقول: 3D يجب أن يُولَّد مثل النص — foundation models تحوّل prompt إلى asset جاهز للألعاب والطباعة والتصنيع.</p>
      <p>في 21 يوليو 2026، أعلنت <strong>Meshy</strong> — من Silicon Valley، مؤسسة <strong>Ethan Hu</strong> (MIT PhD) — عن <strong>Series B بقيمة ~400 مليون دولار</strong> بvaluation <strong>1.5 مليار دولار</strong> — أكبر جولة تمويل لشركة AI 3D على الإطلاق. كل المستثمرين السابقين عادوا؛ هذه أول valuation مُعلنة للشركة.</p>
      <p>الأرقام مذهلة: <strong>12 مليون+</strong> مستخدم مسجّل، <strong>100 مليون</strong> model مُولَّد، و<strong>ARR نما 12×</strong> سنوياً. منتجات جديدة: <strong>3D Agent</strong> — وكيل يُولّد ويُحسّن assets؛ <strong>Auto Split</strong> — تقسيم mesh تلقائي؛ <strong>Smart Topology</strong> — topology نظيف للـ game engines. عملاء: <strong>Nexon</strong> و<strong>NetEase</strong> (gaming) و<strong>Bambu Lab</strong> و<strong>Creality</strong> (3D printing).</p>
      <p>التمويل يذهب لـ R&D وglobal expansion. Meshy mission: «جعل 3D creation accessible للجميع». للمبدعين العرب: sell 3D assets للألعاب والـ metaverse، offer «text-to-3D» services للـ e-commerce، ودورات «AI 3D للمبدعين» — سوق game assets وrapid prototyping ينمو مع كل studio يُسرّع production.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meshy وثورة AI 3D؟</h3>
        <ul>
          <li><strong>3D asset marketplace:</strong> بِع models مُولَّدة بالـ AI للألعاب وAR — 500–5000 دولار/شهر passive.</li>
          <li><strong>Product visualization service:</strong> حوّل صور منتجات e-commerce إلى 3D — 200–1500 دولار/منتج.</li>
          <li><strong>دورات «Text-to-3D للمبدعين»:</strong> bootcamp عربي — 99–499 دولار.</li>
          <li><strong>Game studio pipeline:</strong> accelerate prototyping للـ indie studios MENA — retainer 3000–15000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meshy</span>
        <span class="tag">AI 3D</span>
        <span class="tag">Generative 3D</span>
        <span class="tag">Gaming</span>
        <span class="tag">$1.5B Valuation</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Arrakis: 38 مليون دولار — نظام تشغيل agentic AI للطيران والطاقة والتصنيع يُنافس Palantir!</h2>
      <p class="article-lead">معظم AI يركز على office work — emails، slides، code. Arrakis يقول: أكبر عائد AI في factories وsupply chains وenergy grids — ليس في chatbots. فريق Palantir alumni يبني «AI operating system» للصناعة: design، build، scale agents في بيئات regulated وheavy-duty.</p>
      <p>في 22 يوليو 2026، خرجت <strong>Arrakis</strong> من stealth بـ <strong>38 مليون دولار</strong> إجمالي تمويل — <strong>Series A بـ 30 مليون</strong> بقيادة <strong>Blossom Capital</strong> فوق seed بـ 7.5 مليون من <strong>Accel</strong> — valuation <strong>140 مليون دولار</strong>. المؤسس <strong>Rafael Quintanilla</strong> (ex-Accel VP) مع <strong>Haroun Beltaifa</strong> و<strong>Romain Fouilland</strong> (ex-Palantir) و<strong>Mikhail Galkov</strong> (ex-Delivery Hero).</p>
      <p>Arrakis تُساعد شركات industrial على <strong>design وbuild وscale AI agents</strong> في aerospace وenergy وlogistics وmanufacturing وconstruction وtelecom. thesis: Palantir legacy player قابل للـ disruption — Arrakis أسرع وأكثر flexibility، وconsulting firms تُفوتر بالـ headcount لا بالـ outcomes. angels: <strong>Olivier Pomel</strong> (Datadog CEO) و<strong>Olivier Godement</strong> (OpenAI head of business products) و<strong>Junaid Hussain</strong> (Cambridge Aerospace founder).</p>
      <p>الخطة: triple headcount من ~15، offices في New York والشرق الأوسط، customers من NYSE-listed enterprises في energy وlogistics. للمبدعين العرب: consulting لـ industrial agent deployment، MENA expansion partner، ودورات «Agentic AI للصناعة» — كل مصنع في المنطقة يبحث عن efficiency بعد ارتفاع تكاليف الطاقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Arrakis وAI الصناعي؟</h3>
        <ul>
          <li><strong>Industrial agent consulting:</strong> نشر agents لـ supply chain وmaintenance — مشروع 20000–120000 دولار.</li>
          <li><strong>MENA expansion partner:</strong> كن local implementer لـ Arrakis-style deployments — retainer 4000–25000 دولار/شهر.</li>
          <li><strong>دورات «Agentic AI للمصانع»:</strong> workshop للـ plant managers — 249–1299 دولار.</li>
          <li><strong>Outcome-based automation:</strong> pricing بالـ KPIs لا بالساعات — نموذج consulting جديد للعرب.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Arrakis</span>
        <span class="tag">Industrial AI</span>
        <span class="tag">Agentic AI</span>
        <span class="tag">Palantir Alternative</span>
        <span class="tag">Aerospace</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>HeyMilo: 6 ملايين دولار — agentic recruiting يُقيّم المرشحين بسيناريوهات حية لا بـ CV keywords!</h2>
      <p class="article-lead">التوظيف high-volume كابوس: آلاف applicants، screening يدوي، وCVs مليئة keywords فارغة. HeyMilo يبني agentic recruiting pipeline — من inbound screening إلى scenario assessment وtalent pool mining وnotetaker للمقابلات البشرية. التقييم على القدرة الفعلية، لا على polish.</p>
      <p>في يونيو 2026، أعلنت <strong>HeyMilo AI</strong> من New York عن <strong>6 ملايين دولار</strong> إجمالي تمويل — بقيادة <strong>Category Ventures</strong> مع <strong>Canaan Partners</strong> و<strong>Alumni Ventures</strong> و<strong>Remarkable Ventures</strong>. المؤسسان <strong>Sabashan Ragavan</strong> و<strong>Ramie Raufdeen</strong> (ex-Instagram, Microsoft, Salesforce).</p>
      <p>ثلاثة agents جديدة: <strong>AI Scenario Assessment</strong> — تمارين live مع AI assistant تُقيّم problem-solving؛ <strong>Candidate Recommendations</strong> — يبحث talent pool الحالي ويُعيد surface مرشحين strong لأدوار جديدة؛ <strong>Notetaker</strong> — يلتقط structured notes أثناء human-led interviews. traction بين corporate recruiters وstaffing agencies وBPO firms — خصوصاً multilingual high-volume pipelines.</p>
      <p>الرؤية: «agentic recruiting» — agents تُدير workflow كامل من sourcing إلى assessment. للمبدعين العرب: HR tech consulting، Arabic voice screening agents، ودورات «AI Recruiting للـ HR» — سوق BPO وremote hiring في MENA ضخم ويحتاج automation ذكي لا robotic filters.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HeyMilo وagentic recruiting؟</h3>
        <ul>
          <li><strong>HR tech setup consulting:</strong> نشر agentic recruiting للشركات العربية — مشروع 8000–45000 دولار.</li>
          <li><strong>Arabic assessment scenarios:</strong> ابنِ scenario libraries للـ roles المحلية — 3000–20000 دولار.</li>
          <li><strong>دورات «AI Recruiting للـ HR»:</strong> bootcamp للـ talent teams — 149–799 دولار.</li>
          <li><strong>BPO automation retainer:</strong> automate screening لـ staffing agencies — 2000–12000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HeyMilo</span>
        <span class="tag">Agentic Recruiting</span>
        <span class="tag">HR Tech</span>
        <span class="tag">High-Volume Hiring</span>
        <span class="tag">AI Assessment</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-07-2026 -- 04-PM</p>
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
