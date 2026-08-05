#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 05-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "05-08-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HappyRobot، Convex، Delightree، Zenity، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 5 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من مليار و200 مليون دولار لـ HappyRobot إلى أمان مليار وكيل — أربع انفجارات تُعيد كتابة قواعد AI في أغسطس 2026!</h1>
      <p class="hero-sub">HappyRobot يُصبح «يونicorn» بـ 150 مليون دولار لأتمتة عمليات المؤسسات، Convex يجمع 57 مليون دولار لبناء backend يتحمّل برمجيات الوكلاء، Delightree يُطلق نظام تشغيل agentic للامتيازات التجارية بـ 25 مليون دولار، وZenity يُؤمّن عصر «مليار وكيل» بـ 125 مليون دولار Series C. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 5 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HappyRobot: 150 مليون دولار — وكيلك الجديد يُدير اللوجستيات والتأمين والطيران!</h2>
      <p class="article-lead">تخيّل وكيل AI يتصل بالسائقين لملء جداول التسليم، يُتابع حالة الشحنات، يُنسّق مع المقاولين عند غياب موظف، ويُرسل تذكيرات للعملاء — كل ذلك عبر الهاتف والبريد والويب، دون أن ينتظر أحد. HappyRobot لا يكتفي بالإجابة؛ بل <strong>ينفّذ</strong> العمليات الحرجة التي تُشغّل المؤسسات يومياً. 150 مليون دولار Series C بقيادة Prysm Capital — وتقييم 1.2 مليار دولار!</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>HappyRobot</strong> عن <strong>جولة Series C بقيمة 150 مليون دولار</strong> بقيادة <strong>Prysm Capital</strong> و<strong>Eurazeo</strong>، مع a16z وBase10 وY Combinator وKoch Disruptive Technologies وOrange وT.Capital (Deutsche Telekom) وBankinter وEndeavor Catalyst. التقييم post-money: <strong>1.2 مليار دولار</strong> — إجمالي التمويل ~200 مليون دولار.</p>
      <p>المنصة تُمكّن المؤسسات من بناء ونشر وإدارة وكلاء AI يُ automates workflows معقدة عبر voice وemail وdocuments والويب. الوكلاء يتعلمون من كل تفاعل — ويُحوّلون المعرفة التشغيلية إلى visibility فورية. التوسع: logistics، insurance، energy، telecoms، airlines — أي صناعة تعتمد على مكالمات ووثائق وأنظمة منفصلة.</p>
      <p>SiliconANGLE وصف HappyRobot كـ «AI agents for critical enterprise work». الميزة: AI builder يُنشئ وكيلاً جديداً بمحادثة إنجليزية بسيطة — ما يحتاجه، أي أنظمة يؤثر عليها، أي عمل يُنفّذ. للمبدعين العرب: كل شركة logistics وtelco وairline في MENA تحتاج deployment partner — consulting وcustom agents وtraining للـ operations teams فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HappyRobot وثورة enterprise agentic AI؟</h3>
        <ul>
          <li><strong>HappyRobot implementation partner:</strong> نشر وكلاء للـ logistics وtelco — 12000–60000 دولار/مشروع.</li>
          <li><strong>Voice agent customization:</strong> وكلاء صوت عربية للـ supply chain — 8000–40000 دولار.</li>
          <li><strong>Operations AI consulting:</strong> تحليل workflows وautomation roadmap — 5000–35000 دولار.</li>
          <li><strong>دورات «Enterprise AI Agents»:</strong> bootcamp للـ operations managers — 249–1299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HappyRobot</span>
        <span class="tag">Enterprise Agents</span>
        <span class="tag">Supply Chain AI</span>
        <span class="tag">Unicorn</span>
        <span class="tag">$150M Series C</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Convex: 57 مليون دولار — الـ backend الذي يجعل برمجيات الوكلاء آمنة للإنتاج!</h2>
      <p class="article-lead">عندما يكتب coding agent تطبيقاً كاملاً، كيف تضمن أن البيانات لا تُفسد؟ أن أخطاء الـ hallucination تُكتشف قبل production؟ Convex — من مهندسي Dropbox السابقين — يبني backend مصمّم لعصر «agent-written software»: ACID transactions، TypeScript end-to-end، وConvex Components — وحدات sandboxed يفهمها الوكيل بالكامل دون كسر invariants. 57 مليون دولار Series B من Insight Partners.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>Convex</strong> عن <strong>Series B بقيمة 57 مليون دولار</strong> بقيادة <strong>Insight Partners</strong>، مع Etna Labs وSpark Capital وAndreessen Horowitz وJustin Kan. يُتابع Series A بـ 26 مليون دولار (2022).</p>
      <p>الفلسفة: <strong>correctness enforced by platform</strong> — لا بمهندسين يقرأون كل سطر. ACID transactions تمنع corrupt data عند concurrent writes. TypeScript end-to-end يُحوّل hallucinated field name إلى build error. Automatic sync وcaching يمنعان «glue code» الذي يتعفّن. <strong>Convex Components</strong>: building blocks مع schema وfunctions وdata خلف API صريح — context-window-sized unit يفهمها agent بالكامل.</p>
      <p>Unite.AI وصف Convex كـ «backend for agent-written software». Roadmap: reactive state graph، Components expansion، hiring عبر engineering وproduct وGTM. للمبدعين العرب: كل startup يبني agents custom يحتاج backend آمن — Convex consulting، migration services، ودورات «Agent-Safe Backend» فرصة للمطورين.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Convex وثورة agent-written software؟</h3>
        <ul>
          <li><strong>Convex migration consulting:</strong> نقل تطبيقات لـ agent-ready backend — 10000–55000 دولار/مشروع.</li>
          <li><strong>Component architecture design:</strong> تصميم Components للـ agents — 6000–30000 دولار.</li>
          <li><strong>Agent + backend integration:</strong> ربط coding agents بـ Convex — 8000–45000 دولار.</li>
          <li><strong>دورات «Convex for AI Developers»:</strong> bootcamp للـ full-stack — 199–999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Convex</span>
        <span class="tag">Agent-Written Software</span>
        <span class="tag">Backend Infrastructure</span>
        <span class="tag">TypeScript</span>
        <span class="tag">$57M Series B</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Delightree: 25 مليون دولار — نظام التشغيل الذكي للامتيازات والعلامات متعددة الفروع!</h2>
      <p class="article-lead">50 مليون أمريكي يعملون في restaurants وfitness وwellness وretail — لكن معظمهم لم يستفيدوا من AI. Delightree يُغيّر المعادلة: نظام تشغيل agentic للـ franchise وmulti-unit brands — training، compliance، audits، communications، وإطلاق فروع جديدة من منصة واحدة. 25 مليون دولار من Innovius وAccel وTimber Grove وEmergent.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>Delightree</strong> عن <strong>25 مليون دولار</strong> من <strong>Innovius</strong> و<strong>Accel</strong> و<strong>Timber Grove Ventures</strong> و<strong>Emergent</strong>. المنصة تُساعد operators على إدارة distributed teams — تقليل management overhead، إطلاق locations أسرع، consistency عبر الفروع، وinstant access للمعلومات للـ frontline employees.</p>
      <p>التحدي: multi-unit businesses تعمل بأنظمة fragmented — Delightree يُوحّد training وcompliance وaudits وcommunications. التوسع: restaurants، fitness، wellness، retail، healthcare، home services — «Main Street» التي لم تصلها موجة AI الأخيرة.</p>
      <p>PR Newswire وصف Delightree كـ «agentic operating system for franchise brands». للمبدعين العرب: كل chain مطاعم وصالات رياضية وعيادات في MENA franchise — Delightree implementation، Arabic content للـ training modules، وconsulting للـ compliance automation فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Delightree وثورة franchise AI؟</h3>
        <ul>
          <li><strong>Delightree implementation:</strong> نشر للـ restaurant وfitness chains — 8000–40000 دولار/مشروع.</li>
          <li><strong>Arabic training content:</strong> modules تدريبية عربية للـ frontline — 3000–20000 دولار.</li>
          <li><strong>Compliance automation consulting:</strong> audits وchecklists مُ automated — 5000–25000 دولار.</li>
          <li><strong>دورات «Franchise AI Operations»:</strong> workshop للـ operators — 149–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Delightree</span>
        <span class="tag">Franchise AI</span>
        <span class="tag">Multi-Unit Brands</span>
        <span class="tag">Main Street</span>
        <span class="tag">$25M Funding</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zenity: 125 مليون دولار — أمان «مليار وكيل» يُؤمّن Copilot وChatGPT Enterprise!</h2>
      <p class="article-lead">Microsoft Copilot، ChatGPT Enterprise، Claude، Codex، Bedrock AgentCore — المؤسسات تُ rebuild infrastructure بوكلاء يصلون لبيانات enterprise وtools وprocesses. لكن من يُؤمّنهم؟ Zenity — من Gartner frontrunner في AI agent governance — يُغلق 125 مليون دولار Series C لحماية عصر «1 billion agents». Norwest وSoftBank Vision Fund 2 وHitachi Ventures وLG Technology Ventures.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>Zenity</strong> عن <strong>Series C بقيمة 125 مليون دولار</strong> بقيادة <strong>Norwest</strong>، مع Qumra Capital وSoftBank Vision Fund 2 وHitachi Ventures وLG Technology Ventures وVertex Ventures وThird Point وDTCP وIntel Capital. أكثر من 230 موظف — R&D في Tel Aviv، commercial في New York.</p>
      <p>المنصة: agentic-centric architecture، intent-aware detection، Agent Layer protection — من Google Drive إلى enterprise tools. Zenity تُساهم في OWASP Top 10 وMITRE ATLAS. Gartner (أبريل 2026) صنّفها frontrunner في AI agent governance.</p>
      <p>Fintech Global وصف Zenity كـ «AI agent security race heats up». الرؤية: «As we enter the era of 1 billion agents» — cybersecurity يحتاج approach جديداً لأن software development لم يعد محصوراً بمهندسين highly skilled. للمبدعين العرب: كل enterprise في MENA تُ deploy Copilot أو custom agents — Zenity consulting، security audits، ودورات «AI Agent Governance» طلب متزايد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zenity وثورة AI agent security؟</h3>
        <ul>
          <li><strong>AI agent security audits:</strong> تقييم governance للـ Copilot وcustom agents — 10000–50000 دولار/مشروع.</li>
          <li><strong>Zenity deployment consulting:</strong> نشر وحماية enterprise agents — 15000–70000 دولار.</li>
          <li><strong>Compliance &amp; governance training:</strong> دورات OWASP وMITRE ATLAS — 299–1499 دولار.</li>
          <li><strong>Managed agent security retainer:</strong> مراقبة وحماية مستمرة — 3000–18000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zenity</span>
        <span class="tag">AI Agent Security</span>
        <span class="tag">Governance</span>
        <span class="tag">Enterprise Copilot</span>
        <span class="tag">$125M Series C</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 05-08-2026 -- 12-AM</p>
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
