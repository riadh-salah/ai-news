#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 04-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "04-08-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Design Arena، June، Zenity، Horizon3.ai، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 4 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من «ذوق بشري» يُدرّب النماذج إلى pentesting ذاتي بـ 250 مليون دولار — أربع ثورات تُعيد تعريف AI في أغسطس 2026!</h1>
      <p class="hero-sub">Design Arena يجمع 7.9 مليون دولار لتحويل تفضيلات 5.3 مليون مستخدم إلى بيانات تدريب للـ frontier labs، June من Marc Benioff يُحلّ مشكلة «نشر الوكلاء في المؤسسات» بـ 20 مليون دولار، Zenity يُجمّع 125 مليون دولار لحماية الوكلاء من SoftBank وHitachi وLG، وHorizon3.ai يُحقّق تقييماً يتجاوز 2 مليار دولار لاختبار اختراق ذاتي. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 4 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Design Arena: 7.9 مليون دولار — 5.3 مليون مستخدم يُعلّمون AI «الذوق»!</h2>
      <p class="article-lead">النماذج تُنتج صوراً ومواقع وتصاميم — لكن «هل هذا جميل؟» سؤال لا يُجيب عنه benchmark تقليدي. Grace Li ورفاقها من Stanford بنوا Design Arena: منصة A/B testing بشري لـ AI media، يستخدمها 5.3 مليون شخص حول العالم — وfrontier labs تدفع مقابل هذه البيانات. 7.9 مليون دولار seed من Index Ventures — والشركة الأم Intelligence تُحقّق 60 مليون دولار ARR.</p>
      <p>في 3 أغسطس 2026، أعلنت <strong>Intelligence</strong> — الشركة خلف <strong>Design Arena</strong> — عن <strong>جولة seed بقيمة 7.9 مليون دولار</strong> بقيادة <strong>Index Ventures</strong>، مع Conviction (Sarah Guo وMike Vernal) وA* وValkyrie وآخرين. المؤسسة Grace Li بدأت قبل أسابيع من التخرج في 2025 — عندما فشلت نماذج AI في صنع ألعاب «ممتعة» لا «تعمل فقط».</p>
      <p>التجربة للمستخدم العادي: نافذة ChatGPT-style، dropdowns للصور والمواقع والفيديو، ثم سلسلة اختيارات «A vs B» حتى تُرتّب النتائج. للمختبرات الكبرى: <strong>human-led evaluation data</strong> على نطاق ضخم — ما لا تستطيع benchmarks الآلية قياسه: الذوق، الجمال، الإحساس البصري. Li تقول إن أول deal كبير مع frontier lab جاء خلال أسبوع من الإطلاق.</p>
      <p>TechCrunch وصف Design Arena كـ «bringing taste to AI models». LM Arena — نظير نصي — جمع 150 مليون دولار Series A في يناير. للمبدعين العرب: UX designers وcontent creators يمكنهم المشاركة في التقييمات، وبناء خدمات «AI design evaluation» للوكالات المحلية — سوق الذوق البشري لا يُستبدل بالكامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Design Arena وثورة human evaluation؟</h3>
        <ul>
          <li><strong>AI design evaluation consulting:</strong> مساعدة الوكالات في اختبار outputs نماذج مختلفة — 3000–20000 دولار/مشروع.</li>
          <li><strong>Curated prompt libraries:</strong> بيع مجموعات prompts مُختبرة على Design Arena — 29–199 دولار.</li>
          <li><strong>دورات «AI Taste &amp; Design QA»:</strong> workshop للمصممين — 149–699 دولار.</li>
          <li><strong>Agency retainer:</strong> تقييم مستمر لـ brand assets مُولّدة بالـ AI — 1500–8000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Design Arena</span>
        <span class="tag">Human Evaluation</span>
        <span class="tag">AI Design</span>
        <span class="tag">Index Ventures</span>
        <span class="tag">$7.9M Seed</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>June: 20 مليون دولار من Marc Benioff — خريطة طريق تلقائية لنشر الوكلاء في المؤسسات!</h2>
      <p class="article-lead">«سأعود بـ 100 وكيل AI» — وعد Marc Benioff في Dreamforce. كثير من الشركات عالقة: Claude Code يعمل، لكن نشر وكيل enterprise حقيقي؟ أسابيع من الاجتماعات مع architects وFDEs بلا تقدم. June يمسح أنظمتك، يكتشف الاختناقات، يبني roadmap خطوة بخطوة، ثم ينقر «build» — والوكيل يُنشأ في المؤسسة. 20 مليون دولار pre-seed من Time Ventures — Michael Dell وAaron Levie وGeorge Kurtz في الصف.</p>
      <p>في 3 أغسطس 2026، خرجت <strong>June</strong> من stealth بـ <strong>20 مليون دولار pre-seed</strong> بقيادة <strong>Marc Benioff's Time Ventures</strong>، مع Michael Dell وAaron Levie (Box) وGeorge Kurtz (CrowdStrike). المؤسسة <strong>Shira Rapoport</strong> (CEO) مع Ohad Hen وBarak Goldstein وIdan Tsitiat — يركزون على «AI deployment problem» لا model quality.</p>
      <p>المنصة: <strong>scan → map → build</strong>. June يفحص أنظمة الشركة، يفهم business processes، يجد bottlenecks، ثم يُولّد processes محسّنة بـ agents — مع إشعارات عبر Slack/Teams. «Remove these duplicates. Connect to this data source.» — ثم click «build» على كل task. CMG chief strategy officer Akinmade انتقل لـ Claude Code بسرعة، لكن June أعطاه roadmap واضحاً قبل حتى kickoff call مع Salesforce.</p>
      <p>TechCrunch وصف June كـ «AI can solve the AI deployment problem». June يُكمّل FDEs لا يستبدلهم — لكن customers قد يُ attracted لأنه يقلّل الاعتماد على consultants. للمبدعين العرب: كل enterprise MENA يُريد agents — June implementation partner وprocess mapping consulting فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من June وثورة enterprise agent deployment؟</h3>
        <ul>
          <li><strong>June implementation partner:</strong> نشر وربط وكلاء للشركات — 10000–60000 دولار/مشروع.</li>
          <li><strong>Process mapping consulting:</strong> تحليل workflows قبل June deployment — 5000–35000 دولار.</li>
          <li><strong>دورات «Enterprise AI Agents»:</strong> bootcamp للـ IT وops teams — 249–1299 دولار.</li>
          <li><strong>Managed agent rollout retainer:</strong> صيانة وتحسين deployments — 3000–18000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">June</span>
        <span class="tag">Marc Benioff</span>
        <span class="tag">Agent Deployment</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">$20M Pre-Seed</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Zenity: 125 مليون دولار — SoftBank وHitachi وLG يُموّلون «شرطة الوكلاء»!</h2>
      <p class="article-lead">خطر AI لا يأتي من النموذج القوي — بل من الوكيل الذي يُترك يتصرّف بمفرده. Zenity من إسرائيل يبني cybersecurity لـ AI agents: من يُنفّذ ماذا؟ هل الوكيل يتجاوز صلاحياته؟ هل prompt injection يُحوّله لـ attacker؟ 125 مليون دولار Series C — SoftBank وHitachi وLG في الصف. الرهان: كل مؤسسة بنت agents تحتاج «police force» قبل أن تُسرّق البيانات.</p>
      <p>في 3 أغسطس 2026، أعلنت <strong>Zenity</strong> عن <strong>Series C بقيمة 125 مليون دولار</strong> — مع <strong>SoftBank</strong> و<strong>Hitachi</strong> و<strong>LG</strong> وinvestors آخرين. الشركة Israel-based تركز على <strong>AI agent security</strong> — ليس model safety فقط، بل runtime behavior للوكلاء في production.</p>
      <p>المنصة تراقب: agent actions، data access، tool usage، identity boundaries. Fortune وصف Zenity كـ «police AI agents». مع انتشار Copilot Studio وLangChain agents وcustom workflows — attack surface يتضاعف. Zenity يُكتشف misconfigurations قبل أن يستغلها attacker — أو قبل أن «يهلوس» الوكيل ويُرسل بيانات حساسة.</p>
      <p>للمبدعين العرب: كل bank وtelco وgovernment في MENA يبني agents — Zenity reseller وsecurity audit للـ agent deployments فرصة ذهبية. دورات «AI Agent Security» للـ CISO teams — demand هائل في 2026.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zenity وثورة AI agent security؟</h3>
        <ul>
          <li><strong>Agent security audit:</strong> تقييم deployments قبل production — 8000–45000 دولار/مشروع.</li>
          <li><strong>Zenity implementation partner:</strong> نشر ومراقبة للمؤسسات — 15000–80000 دولار/مشروع.</li>
          <li><strong>دورات «Securing AI Agents»:</strong> workshop للـ security teams — 299–1499 دولار.</li>
          <li><strong>Compliance retainer:</strong> مراقبة مستمرة للـ agent policies — 4000–20000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zenity</span>
        <span class="tag">AI Agent Security</span>
        <span class="tag">SoftBank</span>
        <span class="tag">Cybersecurity</span>
        <span class="tag">$125M Series C</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Horizon3.ai: 250 مليون دولار — NodeZero يُخترق شبكتك قبل المهاجم الحقيقي!</h2>
      <p class="article-lead">Penetration testing تقليدي: تقرير PDF يُنسى في drawer. Horizon3.ai NodeZero يُهاجم production networks مباشرة — weak credentials، misconfigurations، identity gaps — في attack path حقيقي كما يفعل intruder. ثم fix guidance + re-run للتأكد. 250 مليون دولار Series E — تقييم يتجاوز 2 مليار دولار. من 650 مليون دولار في Series D (يونيو 2025) إلى unicorn في 14 شهراً.</p>
      <p>في 3 أغسطس 2026، أعلنت <strong>Horizon3.ai</strong> عن <strong>Series E بقيمة 250 مليون دولار</strong> بتقييم <strong>أكثر من 2 مليار دولار</strong>. NightDragon وNEA co-led، مع Acrew وBlue Cloud وEDBI وPSG Equity وSapphire وreturning investors. Dave DeWalt (ex-FireEye، ex-McAfee) ينضم للـ board.</p>
      <p><strong>NodeZero</strong> platform: autonomous pentesting على live production — «nothing breaks» كما تُؤكد الشركة. single run يُسلسل credentials ضعيفة وmisconfigurations وidentity gaps في path واحد. Fix guidance مُرفق — ثم re-run للتأكد من إغلاق الثغرة. الجزء الجديد: <strong>autonomous blue-team agents</strong> — remediation بدون انتظار human. التوسع: Singapore وAustralia أولاً، ثم EMEA — بما فيها Middle East.</p>
      <p>SiliconANGLE وصف Horizon3 كـ «fundamentally reshaping how the world defends its data». Total funding: 428.5 مليون دولار. للمبدعين العرب: MENA expansion صريحة — reseller وpentest-as-a-service للـ banks وgovernment فرصة ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Horizon3.ai وثورة autonomous pentesting؟</h3>
        <ul>
          <li><strong>NodeZero reseller:</strong> بيع وإدارة pentests للعملاء — 15000–100000 دولار/مشروع.</li>
          <li><strong>Security remediation consulting:</strong> تنفيذ fix guidance من NodeZero — 10000–60000 دولار/مشروع.</li>
          <li><strong>دورات «Autonomous Pentesting»:</strong> bootcamp للـ red/blue teams — 399–1999 دولار.</li>
          <li><strong>Managed security retainer:</strong> pentest دوري + remediation — 5000–25000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Horizon3.ai</span>
        <span class="tag">NodeZero</span>
        <span class="tag">Autonomous Pentesting</span>
        <span class="tag">Cybersecurity</span>
        <span class="tag">$250M Series E</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 04-08-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
