#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-08-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "08-08-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Decade، Obsidian Security، Delightree، Lemma، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 أغسطس 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من ثروة AI في أمريكا اللاتينية إلى أمن الوكلاء — أربع ثورات تُعيد تشكيل اقتصاد الذكاء الاصطناعي!</h1>
      <p class="hero-sub">Decade يجمع 85 مليون دولار لإنشاء جيل جديد من المليونيرات عبر استشارات ثروة مدعومة بالذكاء الاصطناعي، Obsidian Security يُؤمّن وكلاء AI بـ 85 مليون دولار وvaluation 1.1 مليار، Delightree يبني نظام تشغيل agentic لـ 6000+ موقع franchise، وLemma من Y Combinator يكشف «الفشل الصامت» للوكلاء في الإنتاج. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 8 أغسطس 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Decade: 85 مليون دولار — أكبر seed في تاريخ أمريكا اللاتينية لثروة AI!</h2>
      <p class="article-lead">ماذا لو حصلت على مستشار مالي خاص — مدعوم بذكاء اصطناعي يُحلّل كل حساباتك واستثماراتك وعقاراتك — بـ 200 ريال برازيلي شهرياً؟ Decade لا يبني بنكاً آخر؛ بل يُنشئ فئة جديدة: استشارات ثروة AI-native تجمع Open Finance البرازيلي مع خبراء بشرية. 85 مليون دولار seed من Greenoaks وBenchmark — أكبر seed في تاريخ startups أمريكا اللاتينية.</p>
      <p>في 4 أغسطس 2026، خرجت <strong>Decade</strong> من stealth بـ <strong>85 مليون دولار seed</strong> — بقيادة <strong>Greenoaks</strong> و<strong>Benchmark</strong> و<strong>Diffusion</strong>. المؤسسان <strong>Vitor Olivier</strong> (CEO، ex-CTO لـ Nubank — أكبر بنك رقمي في العالم بـ 100 مليون+ عميل) و<strong>Felipe Meneses</strong> (Head of AI، مؤسس Hyperplane التي استحوذت عليها Nubank).</p>
      <p>النموذج: كل عميل يحصل على <strong>مستشار مالي خبير + برمجيات AI proprietary</strong>. لا حاجة لنقل استثماراتك — تربط حساباتك عبر <strong>Open Finance البرازيلي</strong>، تُضيف عقارات ومعاشات واستثمارات دولية، وAI يُحلّل الصورة الكاملة. الخدمة Decade Intelligence: <strong>200 ريال برازيلي/شهر</strong> (~54 دولار كندي) على الخطة السنوية — قائمة انتظار حالياً.</p>
      <p>الطموح: «إنشاء جيل جديد من المليونيرات» — intelligence مالي كان محجوزاً للأثرياء وفرق كبيرة، الآن accessible بالـ AI. Morningstar وBusiness Wire وصفا Decade كـ «largest seed round in Latin American history». للمبدعين العرب: fintech MENA يمكنه بناء نموذج مشابه مع open banking — consulting، content، وwhite-label wealth AI فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Decade وثورة AI wealth advisory؟</h3>
        <ul>
          <li><strong>Wealth AI consulting MENA:</strong> تصميم منصات استشارات ثروة AI-native — 15000–80000 دولار/مشروع.</li>
          <li><strong>Open banking integration:</strong> ربط حسابات متعددة لـ consolidated view — 8000–40000 دولار.</li>
          <li><strong>دورات «AI + Wealth Management»:</strong> bootcamp للـ financial advisors — 249–1299 دولار.</li>
          <li><strong>Content &amp; newsletter:</strong> تحليل trends fintech LATAM/MENA — monetization عبر subscriptions.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Decade</span>
        <span class="tag">AI Wealth</span>
        <span class="tag">Open Finance</span>
        <span class="tag">Nubank</span>
        <span class="tag">$85M Seed</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Obsidian Security: 85 مليون دولار — حارس الوكلاء الذكية بvaluation 1.1 مليار!</h2>
      <p class="article-lead">كل enterprise تُ deploy وكلاء AI على Claude وChatGPT وCopilot Studio — لكن من يُراقب ماذا يفعلون داخل Salesforce وWorkday وSlack؟ Obsidian Security لا يُؤمّن models — بل يُحكم <strong>non-human identities</strong> وagent activity داخل third-party apps. 85 مليون دولار Series D، valuation 1.1 مليار، و60 من Fortune 500 يثقون بها.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>Obsidian Security</strong> عن <strong>Series D بقيمة 85 مليون دولار</strong> بقيادة <strong>Crescent Cove Advisors</strong>، مع Greylock وMenlo Ventures وNorwest وIVP وGV وWing. CEO <strong>Hasan Imam</strong> في exclusive interview مع SiliconANGLE: «AI agents create cybersecurity's next major attack surface».</p>
      <p>المنصة تُوفّر: <strong>visibility</strong> لما متصل، <strong>controls</strong> لما مسموح، و<strong>runtime context</strong> لحوكمة AI قبل أن يسبب damage. أكثر من <strong>100 عميل</strong> ينفقون 100 ألف+ دولار سنوياً، و<strong>14 عميل</strong> ينفقون أكثر من مليون دولار. Obsidian يُ secure agents داخل critical business systems — ليس perimeter فقط.</p>
      <p>SiliconANGLE وصف Obsidian كـ «securing autonomous agents accessing cloud applications». عندما frontier models تستغل vulnerabilities في third-party apps، Obsidian يُ position كـ «AI-first enterprise security». للمبدعين العرب: كل bank وtelco وenterprise MENA يُ deploy Copilot — consulting لـ agent security governance، training للـ CISO teams، وmanaged security retainer فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Obsidian Security وثورة agent security؟</h3>
        <ul>
          <li><strong>Agent security consulting:</strong> تقييم ونشر governance للـ enterprises — 12000–60000 دولار/مشروع.</li>
          <li><strong>Non-human identity audit:</strong> mapping وكلاء AI وصلاحياتهم — 8000–35000 دولار.</li>
          <li><strong>دورات «AI Agent Security»:</strong> workshop للـ security teams — 299–1499 دولار.</li>
          <li><strong>Managed security retainer:</strong> مراقبة agent activity مستمرة — 3000–18000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Obsidian Security</span>
        <span class="tag">Agent Security</span>
        <span class="tag">Non-Human Identity</span>
        <span class="tag">Fortune 500</span>
        <span class="tag">$85M Series D</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Delightree: 25 مليون دولار — نظام التشغيل Agentic لـ 6000+ موقع franchise!</h2>
      <p class="article-lead">50 مليون أمريكي يعملون في restaurants وfitness وretail وhealthcare — لكن Main Street لم يستفد من AI. Delightree يُ unify training وcompliance وaudits وcommunications في <strong>AI operating system واحد</strong> للـ franchise brands. 25 مليون دولار Series B، revenue نما 20x، و6000+ location nationwide.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>Delightree</strong> (Denver) عن <strong>25 مليون دولار funding</strong> من <strong>Innovius</strong> و<strong>Accel</strong> و<strong>Timber Grove Ventures</strong> و<strong>Emergent</strong>. المؤسسان <strong>Tushar Mishra</strong> (CEO) و<strong>Madhulika Mukherjee</strong> — platform أُطلقت قبل أكثر من سنتين.</p>
      <p><strong>Delightree AI</strong> يعرف SOPs وroles وpermissions وlocations وtasks وaudits وtraining. <strong>AI Search</strong> يُجيب أسئلة franchisees من محتوى approved. <strong>Delphi</strong> يُجيب operational questions scoped للـ hierarchy. <strong>Astra</strong> (early access) يحوّل operating signals إلى recommended actions. العملاء: solidcore، Dunn Brothers Coffee، JETSET، MOOYAH Burgers، Beem Light Sauna.</p>
      <p>PR Newswire وصف Delightree كـ «agentic operating system for franchise and multi-unit brands». الفلسفة: standard → training → assigned work → verification → remediation — loop واحد. للمبدعين العرب: كل franchise chain في MENA (مطاعم، fitness، retail) يحتاج operational AI — implementation، custom SOP digitization، وtraining للـ operators فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Delightree وثورة franchise AI OS؟</h3>
        <ul>
          <li><strong>Franchise AI implementation:</strong> نشر Delightree أو منصة مشابهة — 10000–50000 دولار/شبكة.</li>
          <li><strong>SOP digitization:</strong> تحويل procedures لـ AI-ready content — 5000–25000 دولار.</li>
          <li><strong>دورات «Multi-Unit Operations AI»:</strong> training للـ franchise managers — 199–999 دولار.</li>
          <li><strong>White-label franchise OS:</strong> بناء حل MENA-localized — SaaS recurring revenue.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Delightree</span>
        <span class="tag">Franchise AI</span>
        <span class="tag">Agentic OS</span>
        <span class="tag">Multi-Unit</span>
        <span class="tag">$25M Series B</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Lemma: 2.3 مليون دولار — يكشف «الفشل الصامت» للوكلاء في الإنتاج!</h2>
      <p class="article-lead">أخطر bug في AI agents ليس crash — بل success وهمي: الوكيل يُنهي المهمة، يُرسل ✅، والنتيجة خاطئة. Lemma من Y Combinator Fall 2025 يبني monitoring infrastructure لاكتشاف هذه «silent failures». 2.3 مليون دولار pre-seed، أكثر من مليون agent trace مُعالَج، وMCP server يُدمج مع Cursor وClaude Desktop.</p>
      <p>أعلنت <strong>Lemma</strong> عن <strong>pre-seed بقيمة 2.3 مليون دولار</strong> من Matrix وY Combinator وLiquid 2 وVermilion Cliffs وIrregular Expressions وCervin وComma Capital وPosition Ventures وEight Capital — وملائكة من OpenAI وxAI وMeta وDoorDash. المؤسسان <strong>Jerry Zhang</strong> و<strong>Cole Gawin</strong>.</p>
      <p>المنصة تُ monitor production agents وتكشف: الوكيل <strong>يبدو أنه نجح</strong> لكن output خاطئ semantically. Lemma يُ extend workflow إلى dev environments عبر <strong>Model Context Protocol (MCP) server</strong> — developers يستعلمون من Cursor وClaude Desktop وClaude Code مباشرة. Focus أولي: startups تشغّل agents في production already.</p>
      <p>Unite.AI وصف Lemma كـ «tackle silent AI agent failures in production». عندما organizations تُ deploy agents عبر workflows معقدة، monitoring semantic failures يصبح standard operating procedure. للمبدعين العرب: consulting لـ agent reliability، integration Lemma/similar tools، ودورات «Production Agent Monitoring» — كل team يبني agents custom يحتاج هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Lemma وثورة agent reliability؟</h3>
        <ul>
          <li><strong>Agent monitoring setup:</strong> نشر Lemma وtracing للعملاء — 5000–30000 دولار/مشروع.</li>
          <li><strong>Silent failure audit:</strong> تحليل agent traces وإصلاح semantic bugs — 8000–40000 دولار.</li>
          <li><strong>دورات «Production Agent Reliability»:</strong> bootcamp للـ ML engineers — 249–1199 دولار.</li>
          <li><strong>MCP integration services:</strong> ربط monitoring بـ Cursor/Claude workflows — 3000–15000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Lemma</span>
        <span class="tag">Agent Monitoring</span>
        <span class="tag">Silent Failures</span>
        <span class="tag">Y Combinator</span>
        <span class="tag">$2.3M Pre-Seed</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-08-2026 -- 04-PM</p>
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
