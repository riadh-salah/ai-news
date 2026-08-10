#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 10-08-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "10-08-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — HappyRobot، Zenity، Sapiom، Naïve، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 10 أغسطس 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من يونيكورن العمليات إلى شركات تُدار بالكامل من الوكلاء — أغسطس 2026 يُعيد تعريف اقتصاد الذكاء الاصطناعي!</h1>
      <p class="hero-sub">HappyRobot يدخل نادي المليار دولار بـ 150 مليون دولار لتوسيع وكلاء العمليات، Zenity يجمع 125 مليون دولار لحماية مليار وكيل، Sapiom يُخفّض تكلفة الاستدلال بنسبة 75% عبر Router ذكي، وNaïve يُمكّن 30 ألف مطوّر من تأسيس شركات حقيقية عبر API واحد. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 10 أغسطس 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>HappyRobot: 150 مليون دولار — يونيكورن وكلاء العمليات يُهزم التنسيق اليدوي في المؤسسات!</h2>
      <p class="article-lead">تخيّل أن مكالمة شحن متأخرة، أو مطالبة تأمين معقدة، أو تنسيق صيانة طاقة — تُدار بالكامل عبر وكيل AI يفهم أنظمتك ويتعلّم من كل تفاعل. HappyRobot لا يُجيب على أسئلة فقط؛ بل ينفّذ workflows عبر الصوت والبريد والمستندات والويب. 150 مليون دولار Series C بقيادة Prysm Capital — وتقييم 1.2 مليار دولار.</p>
      <p>في 4 أغسطس 2026، أعلنت <strong>HappyRobot</strong> عن <strong>جولة Series C بقيمة 150 مليون دولار</strong> بقيادة <strong>Prysm Capital</strong> و<strong>Eurazeo</strong>، مع عودة a16z وBase10 وY Combinator، واستثمار استراتيجي من Koch Disruptive Technologies وOrange وT.Capital (Deutsche Telekom) وBankinter وEndeavor Catalyst. إجمالي التمويل يتجاوز 200 مليون دولار — والتقييم post-money: <strong>1.2 مليار دولار</strong>.</p>
      <p>المؤسسان الثلاثة الإسبان بدأوا 2022 بعد إيقاف startup للرؤية الحاسوبية — وركّزوا على <strong>agentic AI للعمليات</strong>. المنصة تُمكّن المؤسسات من بناء ونشر وإدارة وكلاء AI يُ automaten workflows معقدة عبر voice وemail وdocuments وweb — مع تعلّم مستمر من كل execution. بدأوا في logistics — أصعب صناعة تشغيلياً — ثم توسّعوا إلى insurance وenergy وtelecom وairlines.</p>
      <p>Tech.eu وصف HappyRobot كـ «agentic AI for enterprise operations». الفرق عن chatbots: الوكلاء <strong>يُنفّذون</strong> و<strong>يُفكّرون</strong> داخل أنظمة المؤسسة — capture operational knowledge، streamline information exchange، real-time visibility. للمبدعين العرب: كل telco وlogistics وairline في MENA يحتاج deployment partner — consulting وcustom agents وtraining للـ operations teams فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HappyRobot وثورة operational AI agents؟</h3>
        <ul>
          <li><strong>HappyRobot implementation partner:</strong> نشر وكلاء للـ logistics وtelco — 15000–80000 دولار/مشروع.</li>
          <li><strong>Voice agent customization:</strong> وكلاء صوت عربية للـ call centers — 10000–50000 دولار.</li>
          <li><strong>Operations AI consulting:</strong> تحليل workflows وautomation roadmap — 8000–40000 دولار.</li>
          <li><strong>دورات «Enterprise Agentic AI»:</strong> bootcamp للـ operations managers — 249–1299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HappyRobot</span>
        <span class="tag">Agentic AI</span>
        <span class="tag">Enterprise Operations</span>
        <span class="tag">Unicorn</span>
        <span class="tag">$150M Series C</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Zenity: 125 مليون دولار — درع الأمان الذي يحمي عصر مليار وكيل AI!</h2>
      <p class="article-lead">كل مؤسسة تُسرّع نشر وكلاء AI — لكن السؤال الحقيقي: ماذا لو «انحرف» وكيل وسرّب بيانات أو نفّذ أمراً خطيراً؟ Zenity بنت أول منصة أمن وحوكمة مُخصّصة للوكلاء — من discovery إلى inline prevention في runtime. 125 مليون دولار Series C من Norwest — وإجمالي التمويل 185 مليون دولار.</p>
      <p>في 3 أغسطس 2026، أعلنت <strong>Zenity</strong> عن <strong>Series C بقيمة 125 مليون دولار</strong> بقيادة <strong>Norwest Venture Partners</strong>، مع SoftBank Vision Fund 2 وQumra Capital وHitachi Ventures وLG Technology Ventures، واستمرار Vertex وThird Point وDTCP وIntel Capital. المؤسسان <strong>Ben Kliger</strong> (CEO) و<strong>Michael Bargury</strong> (CTO) — veterans من Unit 8200 وMicrosoft.</p>
      <p>المنصة تُغطي lifecycle كامل: <strong>agent discovery</strong>، posture management، real-time detection، <strong>inline prevention</strong>، وresponse. Zenity يراقب كيف يتصرّف الوكيل — ما يصل إليه، أي tools يستدعي — عبر SaaS وcloud وendpoint. شراكة Microsoft Foundry: runtime security controls تمنع misuse قبل تنفيذ أي أمر.</p>
      <p>SiliconANGLE وصف Zenity كـ «security layer for 1 billion AI agents». الشركة تخدم Fortune 500 — أكثر من 230 موظفاً، R&amp;D في Tel Aviv وgo-to-market من New York. للمبدعين العرب: كل bank وgovernment وenterprise في MENA يُسرّع agent adoption — consulting لـ AI agent security وcompliance وZenity deployment فرصة ذهبية قبل أن تُصبح mandatory.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zenity وثورة AI agent security؟</h3>
        <ul>
          <li><strong>AI security consulting:</strong> تقييم ونشر Zenity للمؤسسات — 12000–60000 دولار/مشروع.</li>
          <li><strong>Agent governance frameworks:</strong> سياسات وضوابط للـ MENA regulators — 8000–35000 دولار.</li>
          <li><strong>Managed security retainer:</strong> مراقبة وagents posture — 3000–15000 دولار/شهر.</li>
          <li><strong>دورات «AI Agent Security»:</strong> للـ CISOs وsecurity teams — 299–1499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zenity</span>
        <span class="tag">AI Security</span>
        <span class="tag">Agent Governance</span>
        <span class="tag">Inline Prevention</span>
        <span class="tag">$125M Series C</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Sapiom: 35 مليون دولار — Router ذكي يُخفّض فاتورة Claude من 1.2 مليون إلى 100 ألف دولار!</h2>
      <p class="article-lead">معظم فرق AI تُشغّل كل طلب على أغلى model — ثم تُفاجأ بفاتورة astronomical. Sapiom يجلس بين الوكلاء والنماذج ويُوجّه كل call للـ model الأنسب والأرخص. Anthropic نفسها مستثمرة — لأن الهدف ليس تدمير revenue بل تمكين trillion agents. 35 مليون دولار Series A من Dragonfly — و270 مليون transaction في 6 أشهر.</p>
      <p>في 5 أغسطس 2026، أعلنت <strong>Sapiom</strong> عن <strong>Series A بقيمة 35 مليون دولار</strong> بقيادة <strong>Dragonfly</strong>، مع Accel وGradient وCoinbase Ventures وAnthropic وOkta Ventures وMenlo Ventures — إجمالي التمويل 50 مليون دولار في 11 شهراً من التأسيس. المؤسس <strong>Ilan Zerbib</strong> من San Francisco.</p>
      <p>ثلاثة منتجات أُطلقت مع الجولة: <strong>Sapiom Router</strong> — endpoint متوافق مع OpenAI API يختار الـ model الأكفأ لكل request؛ <strong>Agent Studio</strong> — بيئة محلية لبناء واختبار ونشر agents بأمر واحد؛ <strong>Sapiom Runtime</strong> — infrastructure مُدارة مع sandboxes وmemory وsecrets وتسجيل cost لكل step. Polsia cut monthly Anthropic bill من 1.2 مليون إلى ~100 ألف دولار — reduction ~10x.</p>
      <p>LinkedIn post من Sapiom: أكثر من 100 ألف agent run يومياً — وcustomer واحد خفّض inference costs بنسبة 75%. Gartner يتوقع إلغاء &gt;40% من agentic projects بحلول 2027 بسبب التكلفة. للمبدعين العرب: كل startup وagency يبني agents يحتاج cost optimization — Sapiom consulting وArabic agent deployment فرصة عملية فورية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sapiom وثورة agent cost optimization؟</h3>
        <ul>
          <li><strong>Sapiom integration consulting:</strong> نشر Router وRuntime للعملاء — 8000–45000 دولار/مشروع.</li>
          <li><strong>Cost audit services:</strong> تحليل فواتير LLM وتقليلها — 3000–20000 دولار.</li>
          <li><strong>Agent Studio training:</strong> workshops للفرق الهندسية — 199–999 دولار.</li>
          <li><strong>Managed agent ops retainer:</strong> صيانة وmonitoring للـ production agents — 2500–12000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sapiom</span>
        <span class="tag">Model Router</span>
        <span class="tag">Agent Studio</span>
        <span class="tag">Cost Optimization</span>
        <span class="tag">$35M Series A</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Naïve: 28.5 مليون دولار — API واحد يُؤسّس شركتك ويُشغّلها عبر وكلاء AI!</h2>
      <p class="article-lead">بعد vibe coding، السؤال التالي: كيف تُأسّس LLC أمريكية، وتفتح حساب دفع، وتُنشئ email وphone وcloud — دون أسبوع من paperwork؟ Naïve يُجمّع كل ذلك خلف API واحد يستدعيه Cursor أو Claude Code. 30 ألف مطوّر سجّلوا في أشهر — وARR نما 10x في 6 أشهر. 28.5 مليون دولار Series A من Nexus Venture Partners.</p>
      <p>في 6 أغسطس 2026، أعلنت <strong>Naïve</strong> عن <strong>Series A بقيمة 28.5 مليون دولار</strong> بقيادة <strong>Nexus Venture Partners</strong>، مع Y Combinator وZetta وLiquid 2 وملائكة من Amazon وDocuSign وCodecademy. المؤسسان <strong>Sean Dorje</strong> و<strong>Dennis Zax</strong> — UC Berkeley dropouts عملا معاً منذ عمر 14.</p>
      <p>المنصة تُوفّر: <strong>LLC incorporation</strong>، virtual cards، business email، phone numbers، cloud وstorage، و<strong>governance gateway</strong> — budgets وapprovals وcapacity policies. Agents تُشغَّل في serverless JavaScript runtime — تدفع فقط عند التنفيط لا VM دائمة. Model router + memory system + multi-agent orchestrator يُقلّلون token costs.</p>
      <p>TechCrunch وصف Naïve كـ «infrastructure for autonomous companies». المطور يكتب config file؛ coding agent يستدعي API؛ Naïve يُ provision كل infrastructure. للمبدعين العرب: agencies تبني «AI-native businesses» للعملاء، consulting لـ Naïve setup، ودورات «Launch a Company with AI Agents» — كل freelancer يريد LLC أمريكية + payments بدون friction.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Naïve وثورة autonomous companies؟</h3>
        <ul>
          <li><strong>Naïve setup services:</strong> تأسيس شركات AI-native للعملاء — 2000–15000 دولار/مشروع.</li>
          <li><strong>Agent business templates:</strong> packs جاهزة (SaaS، agency، e-commerce) — 499–2999 دولار.</li>
          <li><strong>Compliance consulting:</strong> KYC/KYB وgovernance للـ MENA founders — 3000–18000 دولار.</li>
          <li><strong>دورات «AI Company Builder»:</strong> من فكرة إلى LLC + payments — 149–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Naïve</span>
        <span class="tag">Autonomous Companies</span>
        <span class="tag">Agent Infrastructure</span>
        <span class="tag">Serverless Runtime</span>
        <span class="tag">$28.5M Series A</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 10-08-2026 -- 08-AM</p>
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
