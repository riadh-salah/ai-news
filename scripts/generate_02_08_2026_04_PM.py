#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 02-08-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "02-08-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Harmony، Enigma، Encore AI، hiloop، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 2 أغسطس 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من وكلاء Slack إلى روبوتات تُتحكّم بها من المتصفح — أربع ثورات تُعيد رسم خريطة AI في أغسطس 2026!</h1>
      <p class="hero-sub">Harmony يجمع 34 مليون دولار لتحويل Slack وTeams إلى مركز خدمات موظفين ذكي، Enigma يفتح 100 روبوت للعالم على robots.online بـ 71 مليون دولار، Encore AI يُعدين «تعدين التفاعلات» من مكالمات العملاء، وhiloop من Y Combinator يُهزم state-of-the-art بـ 4188 تجربة في يومين. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 2 أغسطس 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Harmony: 34 مليون دولار — وكيلك الجديد يعيش داخل Slack وMicrosoft Teams!</h2>
      <p class="article-lead">تخيّل أن تطلب إعادة تعيين كلمة مرور، أو طلب لابتوب، أو استفساراً عن سياسة HR — من نفس مكان محادثاتك اليومية، ويُنفَّذ الطلب خلال دقائق لا أيام. Harmony لا يبني بوابة جديدة؛ بل يُغرق Slack وTeams بوكلاء AI يفهمون دورك وصلاحياتك وتاريخ عملك. 34 مليون دولار seed من Lightspeed — والمؤسسان باعا Epsagon لـ Cisco بـ 500 مليون دولار.</p>
      <p>في 28 يوليو 2026، أعلنت <strong>Harmony</strong> عن <strong>جولة seed بقيمة 34 مليون دولار</strong> بقيادة <strong>Lightspeed Venture Partners</strong>، مع Hitachi Ventures وFin Capital وMercer Ventures وOperator Partners، وملائكة من فريق تأسيس Wiz بقيادة Assaf Rappaport. المؤسسان <strong>Nitzan Shapira</strong> (CEO) و<strong>Ran Ribenzaft</strong> (CTO) — co-founders لـ Epsagon التي استحوذت عليها Cisco مقابل 500 مليون دولار في 2021.</p>
      <p>المنصة تُوفّر <strong>أكثر من 100 وكيل AI جاهز</strong> يُنشر خلال أيام لا أشهر، عبر IT وHR والمالية والمشتريات والقانون والأمن وDevOps. Harmony يربط هوية الموظف وأجهزته وتطبيقاته وصلاحياته — ويُحقّق <strong>70% no-touch resolution rate</strong>. الموظف يكتب طلبه في Slack أو Teams؛ الوكيل يُنفّذ عبر الأنظمة المتصلة — مع إمكانية موافقة بشرية قبل أي إجراء حساس.</p>
      <p>Business Insider وصف Harmony كـ «employee experience powered by AI». الفرق عن chatbots تقليدية: Harmony <strong>يتصرّف</strong> لا يُجيب فقط — onboarding، provisioning، password resets، approvals. للمبدعين العرب: كل مؤسسة MENA بـ Microsoft 365 أو Slack تحتاج implementation partner — consulting وcustom agents وtraining للـ IT teams فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Harmony وثورة employee AI agents؟</h3>
        <ul>
          <li><strong>Harmony implementation partner:</strong> نشر وربط وكلاء للشركات — 8000–45000 دولار/مشروع.</li>
          <li><strong>Custom agent development:</strong> بناء وكلاء HR/IT مخصّصين للـ MENA — 5000–25000 دولار.</li>
          <li><strong>دورات «Employee AI Agents»:</strong> workshop للـ IT وHR — 199–899 دولار.</li>
          <li><strong>Managed employee support retainer:</strong> صيانة وتحسين الوكلاء — 2000–12000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Harmony</span>
        <span class="tag">Slack Agents</span>
        <span class="tag">Microsoft Teams</span>
        <span class="tag">Employee Experience</span>
        <span class="tag">$34M Seed</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Enigma: 71 مليون دولار — 100 روبوت AI مفتوحة للعالم على robots.online!</h2>
      <p class="article-lead">معظم شركات الروبوتات تُغلق demos خلف NDA. Enigma فعل العكس: في يوم الإطلاق، فتح أكثر من 100 ذراع روبوتية للتحكم من أي متصفح — رسم بالفرشاة، مبارزات بالسيف، تجارب كيميائية. الهدف ليس entertainment فقط — بل جمع بيانات عن كيف يُوجّه البشر الآلات بشكل طبيعي. 71 مليون دولار seed من Index Ventures وRibbit Capital.</p>
      <p>في 27 يوليو 2026، خرجت <strong>Enigma</strong> من stealth بـ <strong>71 مليون دولار seed</strong> بقيادة <strong>Index Ventures</strong> و<strong>Ribbit Capital</strong>، مع Conviction Partners وقادة من OpenAI وAnthropic وDeepMind وxAI وCognition وWiz. المؤسسان <strong>Jonathan Jacobi</strong> (CEO) و<strong>Gal Niv</strong> (CTO) — أقل من سنة عمر الشركة.</p>
      <p>الفلسفة: <strong>الواجهة هي عنق الزجاجة</strong> — لا القدرات الخام. Enigma يبني foundation models للروبوتات + interfaces بديهية «مثل ضبط صوت السيارة». المنصة <strong>robots.online</strong> تسمح لأي شخص بالتحكم بروبوتات حقيقية في hangars بإسرائيل وكاليفورnia — لجمع insights عن human-robot interaction. Enigma يُطوّر الذراعات والنماذج من الصفر.</p>
      <p>TechCrunch وصف Enigma كـ «controlling a robot as easy as adjusting the volume». الشراكات الأولية: healthcare وlogistics وentertainment وretail. للمبدعين العرب: content creators يمكنهم بث تجارب robots.online، وconsultants في physical AI، ودورات «Human-Robot Interaction» — robotics economy تبدأ من UX لا hardware فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Enigma وثورة Physical AI؟</h3>
        <ul>
          <li><strong>Robotics UX consulting:</strong> تصميم interfaces للـ industrial robots — 10000–60000 دولار/مشروع.</li>
          <li><strong>Content &amp; streaming:</strong> بث تجارب robots.online — monetization عبر ads وsponsorships.</li>
          <li><strong>Physical AI training:</strong> دورات «Robotics + AI» للمهندسين — 249–1299 دولار.</li>
          <li><strong>MENA robotics integration:</strong> pilot deployments للـ logistics وhealthcare — 15000–80000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Enigma</span>
        <span class="tag">Physical AI</span>
        <span class="tag">robots.online</span>
        <span class="tag">Foundation Models</span>
        <span class="tag">$71M Seed</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Encore AI: 30 مليون دولار — «تعدين التفاعلات» يُحوّل مكالمات العملاء إلى وكلاء أذكياء!</h2>
      <p class="article-lead">كل مكالمة sales أو support تحمل gold mine من البيانات — لكن معظم الشركات تُهدرها. Encore AI يُحلّل آلاف المحادثات (calls، emails، texts) ويربطها بالـ CRM لاكتشاف: أي جملة أغلقت الصفقة؟ أي tactic فشل؟ ثم يُدرّب وكلاء voice/text على «interaction mining». 30 مليون دولار Series A من Team8 — وبنوك ومؤمّنون استثمروا بعد استخدام المنتج.</p>
      <p>في 29 يوليو 2026، أعلنت <strong>Encore AI</strong> (formerly Insait IO) عن <strong>Series A بقيمة 30 مليون دولار</strong> بقيادة <strong>Team8</strong>، مع Planven وLukatz وGarage — وبعض البنوك والمؤمّنين شاركوا بعد pilot. CEO <strong>Dvir Ginzburg</strong> بدأ 2022 بـ recommendation software للـ financial advisers، ثم pivot إلى platform تحلّل customer interactions.</p>
      <p>العملية: <strong>interaction mining</strong> — جمع recordings وemails وtexts، ربط CRM، تقسيم المحادثات لمراحل، وتحديد ما نجح وما فشل. الوكلاء يتواصلون بالصوت أو النص مع العملاء، أو يعملون <strong>assistants للموظفين</strong> — يُقترحون responses وtactics أثناء المكالمة live. Encore يُحدّد أيضاً friction points في processes الحالية.</p>
      <p>TechCrunch وصف Encore كـ «AI agents that learn from customer calls». Focus: financial institutions وlarge enterprises. للمبدعين العرب: كل bank وinsurance وtelco في MENA لديه call centers — consulting لـ interaction mining، voice agent deployment، وtraining datasets عربية فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Encore AI وثورة interaction mining؟</h3>
        <ul>
          <li><strong>Call center AI consulting:</strong> تحليل وتدريب وكلاء من recordings — 10000–50000 دولار/مشروع.</li>
          <li><strong>Arabic voice agent deployment:</strong> وكلاء صوت عربية للـ banks وe-commerce — 8000–40000 دولار.</li>
          <li><strong>Sales playbook automation:</strong> تحويل best practices لـ AI assistants — 5000–30000 دولار.</li>
          <li><strong>دورات «Customer Interaction AI»:</strong> bootcamp للـ sales وsupport teams — 199–999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Encore AI</span>
        <span class="tag">Interaction Mining</span>
        <span class="tag">Voice Agents</span>
        <span class="tag">Customer Calls</span>
        <span class="tag">$30M Series A</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>hiloop: Y Combinator S26 — 4188 تجربة في يومين تُهزم state-of-the-art!</h2>
      <p class="article-lead">تدريب agents على مهام صعبة يستهلك شهوراً من trial-and-error. hiloop يُ automate «autoresearch»: أعطِ مهمة، model/agent حالي، وevaluation — والمنصة تُشغّل آلاف التجارب عبر data وSFT وprompts وtools، وتُرجع أفضل improvement مُ verified إحصائياً. Karan وThomas — ex-DynamoAI — أعطيا agentين 50 B200 GPUs: 4188 experiment في يومين، وbeat Recursive's SOTA على Karpathy benchmark.</p>
      <p><strong>hiloop</strong> من batch <strong>Y Combinator Summer 2026</strong> يبني infrastructure لـ <strong>recursive self-improvement</strong>. المؤسسان <strong>Karan</strong> (ex-ML infra lead DynamoAI) و<strong>Thomas</strong> — يُوفّران: persistent memory، full experiment lineage، compute orchestration، وstatistical verification.</p>
      <p>النتائج: على Karpathy's autoresearch benchmark، وصلت recipe النهائية إلى <strong>0.9016 val_bpb</strong> — أفضل من Recursive's 0.9109. على NanoGPT speedrun: <strong>12.54% lower runtime</strong> من best known result. hiloop يعمل hosted أو in your cloud — starting with agent/model training، SFT، post-training، continual learning.</p>
      <p>الفلسفة: «Give us a hard task, your current agent, and evaluation — we return the best verified improvement.» للمبدعين العرب: consulting لـ model optimization، autoresearch campaigns للـ startups، ودورات «AI Experiment Automation» — كل team يبني agents custom يحتاج هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من hiloop وثورة autoresearch؟</h3>
        <ul>
          <li><strong>Model optimization consulting:</strong> autoresearch campaigns للعملاء — 15000–80000 دولار/مشروع.</li>
          <li><strong>Agent fine-tuning services:</strong> SFT وcontinual learning للـ Arabic models — 8000–50000 دولار.</li>
          <li><strong>دورات «Autoresearch &amp; AI Training»:</strong> bootcamp للـ ML engineers — 299–1499 دولار.</li>
          <li><strong>MLOps retainer:</strong> experiment orchestration وverification — 3000–15000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">hiloop</span>
        <span class="tag">Y Combinator</span>
        <span class="tag">Autoresearch</span>
        <span class="tag">Agent Training</span>
        <span class="tag">Self-Improvement</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 02-08-2026 -- 04-PM</p>
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
