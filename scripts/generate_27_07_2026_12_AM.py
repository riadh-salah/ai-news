#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-07-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "27-07-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Together AI، MGX، Browserbase Agents، OpenEvidence، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 يوليو 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من أبوظبي إلى كامبريدج — 49 مليار دولار، 800 مليون، ووكلاء يتصفّحون الويب نيابةً عنك: الذكاء الاصطناعي يُعيد رسم خريطة الثروة في 2026!</h1>
      <p class="hero-sub">Together AI يجمع 800 مليون دولار بقيادة Aramco Ventures، صندوق MGX الإماراتي يُغلق بـ 49 مليار دولار، Browserbase يُحوّل 35 مليون جلسة متصفح شهرياً إلى وكيل واحد بـ API call، وOpenEvidence يُضاعف valuation إلى 12 مليار دولار كـ «زميل طبيب» موثوق. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 27 يوليو 2026</span>
        <span>🕛 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Together AI: 800 مليون دولار وvaluation 8.3 مليار — Aramco Ventures يقود ثورة «Neocloud» للنماذج المفتوحة!</h2>
      <p class="article-lead">لماذا تدفع لـ OpenAI أو Anthropic بينما يمكنك تشغيل Llama وDeepSeek وQwen على GPU clusters مُحسّنة؟ Together AI — neocloud مُخصّص للـ AI — يجمع 800 مليون دولار بقيادة Aramco Ventures، valuation 8.3 مليار دولار، وbookings سنوية تتجاوز 1.15 مليار دولار. الخطة: توسيع السحابة 50× خلال 5 سنوات و500 ميجاوatt من قدرة الحوسبة.</p>
      <p>في 1 يوليو 2026، أعلنت <strong>Together AI</strong> — من San Francisco — عن <strong>Series C بقيمة 800 مليون دولار</strong> بـ valuation <strong>8.3 مليار دولار</strong>. الجولة بقيادة <strong>Aramco Ventures</strong> (ذراع استثمار Aramco)، مع <strong>Vista Equity Partners</strong>، <strong>General Catalyst</strong>، <strong>Emergence Capital</strong>، <strong>NVIDIA</strong>، <strong>March Capital</strong>، <strong>Pegatron</strong>، و<strong>S Ventures</strong> من SentinelOne.</p>
      <p>المنصة تُؤجّر <strong>NVIDIA GPU clusters</strong> وinfrastructure مُحسّنة لتدريب وتشغيل <strong>open-source models</strong> — بدلاً من dependency على frontier labs مغلقة. Series B قبل 16 شهراً كانت 305 مليون دولار بـ valuation 3.3 مليار — قفزة 2.5× مدفوعة بإيرادات حقيقية لا hype. التمويل يُموّل شراء infrastructure وتوسيع training وinference features.</p>
      <p>TechCrunch وSiliconANGLE وصفا Together AI كـ «AI-optimized public cloud» للنماذج المفتوحة. عندما data sovereignty وcost sensitivity يدفعان enterprises نحو open models، neoclouds مثل Together تصبح طبقة حاسمة. للمبدعين العرب: consulting لـ open-model deployment، fine-tuning services، ودورات «Run Your Own LLM» — سوق inference مفتوح ينفجر في 2026.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Together AI وثورة Neocloud؟</h3>
        <ul>
          <li><strong>Open-model deployment consulting:</strong> نفّذ LLMs مفتوحة للشركات — 8000–55000 دولار/مشروع.</li>
          <li><strong>Fine-tuning agency:</strong> درّب نماذج على بيانات العملاء عبر Together — 5000–35000 دولار/نموذج.</li>
          <li><strong>دورات «Neocloud للمطورين العرب»:</strong> bootcamp inference وtraining — 149–799 دولار.</li>
          <li><strong>MENA AI infrastructure retainer:</strong> أدر deployments open-source شهرياً — 2500–18000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Together AI</span>
        <span class="tag">Neocloud</span>
        <span class="tag">Aramco Ventures</span>
        <span class="tag">Open-Source LLM</span>
        <span class="tag">$8.3B Valuation</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>MGX أبوظبي: 49 مليار دولار — أكبر صندوق AI في التاريخ يُبني مستقبل الذكاء من الخليج إلى باريس!</h2>
      <p class="article-lead">عندما يُغلق صندوق AI بـ 49 مليار دولار — يتجاوز الهدف بـ 4 مليارات — فأنت لا تشهد «استثماراً» بل «إعادة توزيع ثروة». MGX من أبوظبي يستثمر في 14 شركة spanning semiconductors وAI infrastructure وplatforms، يبني أكبر campus AI في أوروبا قرب باريس بـ 3GW compute، ويُشارك في صفقة 40 مليار دولار لـ Aligned Data Centres.</p>
      <p>في 1 يوليو 2026، أعلنت <strong>MGX</strong> — شركة استثمار AI مقرها <strong>أبوظبي</strong> — إغلاق <strong>Fund I بقيمة 49 مليار دولار</strong>، متجاوزة هدفها البالغ 45 مليار دولار. المستثمرون من الخليج وأمريكا الشمالية وآسيا وأوروبا — institutional وprivate investors يُعيدون رسم خريطة capital flows في AI.</p>
      <p>الصندوق استثمر في <strong>14 شركة</strong> حتى الآن: من semiconductors إلى AI infrastructure إلى platforms. MGX تطوّر <strong>أكبر AI campus في أوروبا</strong> قرب باريس بقدرة <strong>3GW compute</strong> — sovereign AI infrastructure على نطاق continental. كما شاركت في acquisition <strong>Aligned Data Centres</strong> ضمن consortium بقيمة <strong>40 مليار دولار</strong>.</p>
      <p>MGX شاركت أيضاً في جولة OpenAI التاريخية بـ 122 مليار دولار — إثبات أن capital الخليجي أصبح player مركزي في frontier AI. للمبدعين العرب: فرص consulting لـ sovereign AI، partnerships مع MENA enterprises، وcontent عن «كيف تستفيد من موجة الاستثمار الخليجي في AI» — المنطقة تتحول من consumer إلى builder.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من موجة MGX والاستثمار الخليجي في AI؟</h3>
        <ul>
          <li><strong>Sovereign AI consulting MENA:</strong> صمّم strategies للشركات والحكومات — 15000–90000 دولار/مشروع.</li>
          <li><strong>AI infrastructure advisory:</strong> ربط startups بفرص funding وpartnerships — 5000–40000 دولار/تقرير.</li>
          <li><strong>دورات «AI Investment Landscape»:</strong> workshop للمستثمرين والمؤسسين — 399–1999 دولار/مشارك.</li>
          <li><strong>GCC AI ecosystem content:</strong> newsletter أو podcast عن deals — 2000–12000 دولار/شهر من sponsors.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">MGX</span>
        <span class="tag">Abu Dhabi</span>
        <span class="tag">$49B Fund</span>
        <span class="tag">Sovereign AI</span>
        <span class="tag">Gulf Capital</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Browserbase Agents: من 35 مليون جلسة شهرياً إلى وكيل واحد — API call واحد وstructured data من مئات المواقع!</h2>
      <p class="article-lead">«سكربت لكل موقع» لا يتوسّع. Browserbase — التي تُشغّل 35+ مليون جلسة متصفح شهرياً — أطلقت Browserbase Agents: تصفّح goal بلغة طبيعية، واستلم structured typed results من مئات portals دون Playwright scripts ولا infrastructure. KYC عبر 1500+ county sites، competitor monitoring، document retrieval — كلها بـ one API call.</p>
      <p>في 30 يونيو 2026، أطلقت <strong>Browserbase</strong> <strong>Browserbase Agents</strong> — managed browser agent يُنشأ من natural-language prompt ويُشغَّل عبر <strong>single API call</strong>. المؤسس <strong>Paul Klein IV</strong> بنى الشركة حول pain point واحد: browsers حقيقية reliable enough للإنتاج — والآن يُpackage الـ agent loop كاملاً.</p>
      <p>المنصة تبني على: <strong>Stagehand SDK</strong> (open-source)، <strong>Agent Identity</strong> للـ auth وanti-bot، <strong>Search وFetch APIs</strong>، live browser view، session replay، traces، و<strong>per-run cost breakdown</strong>. Use cases: price monitoring، KYC/KYB عبر portals، government وreal estate records، document retrieval، automated QA لـ coding agents. Dashboard يُقدّم <strong>Optimize</strong> tool يُحسّن Agent من runs سابقة — تسريع 30%+.</p>
      <p>RuntimeWire وصف Browserbase Agents كـ «packaging the agent loop itself». عندما web data يُغذّي agents وRAG وcompetitive intelligence، managed browser agents تصبح infrastructure layer. للمبدعين العرب: agency لـ web data extraction، KYC automation للـ fintech، وcontent عن «كيف تبني agents تتصفّح الويب» — سوق browser automation ينفجر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Browserbase Agents وثورة web agents؟</h3>
        <ul>
          <li><strong>Web data extraction agency:</strong> نفّذ competitor وprice monitoring — 2000–20000 دولار/مشروع.</li>
          <li><strong>KYC/KYB automation:</strong> أتمت التحقق عبر government portals — 5000–45000 دولار/عميل.</li>
          <li><strong>دورات «Browser Agents للمطورين»:</strong> bootcamp Stagehand وBrowserbase — 129–599 دولار.</li>
          <li><strong>MENA fintech data retainer:</strong> راقب portals وrecords شهرياً — 1500–10000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Browserbase</span>
        <span class="tag">Browser Agents</span>
        <span class="tag">Stagehand</span>
        <span class="tag">Web Automation</span>
        <span class="tag">35M Sessions</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>OpenEvidence: 250 مليون دولار وvaluation 12 مليار — «ممدّد العقل» الذي يثق به 700 ألف طبيب!</h2>
      <p class="article-lead">ChatGPT يُجيب عن كل شيء — لكن الطبيب لا يستطيع الثقة بإجابة عامة عند قرار حياة أو موت. OpenEvidence — AI مُدرَّب على peer-reviewed literature وclinical guidelines — يُستخدم من 700+ ألف طبيب. Series D بـ 250 مليون دولار يُضاعف valuation إلى 12 مليار دولار. Thrive Capital وDST Global يقودان — GV وSequoia وKleiner Perkins وCoatue يشاركون.</p>
      <p>أعلنت <strong>OpenEvidence</strong> — من Cambridge/Miami — عن <strong>Series D بقيمة 250 مليون دولار</strong> بـ valuation <strong>12 مليار دولار</strong> — ضعف Series C في أكتوبر (6 مليار). الجولة الرابعة في أقل من سنة — إجمالي التمويل يقترب من <strong>700 مليون دولار</strong> منذ 2021. Thrive Capital وDST Global co-led، مع GV وSequoia وKleiner Perkins وCoatue.</p>
      <p>المنتج: <strong>clinical decision-support</strong> evidence-based في point of care — ليس chatbot عاماً بل AI مُخصّص للطب. يُقدّم guidance real-time مبني على literature مراجع وguidelines سريرية. التمويل يُسرّع integrations مع hospital systems وتطوير modules لـ oncology وcardiology وsurgery — medical AI يدخل مرحلة institutional deployment.</p>
      <p>Crunchbase News وصف OpenEvidence كـ «AI Doctor's Most Trusted Colleague». عندما general-purpose AI يفشل في high-stakes domains، vertical medical AI يفوز. للمبدعين العرب: consulting لـ healthcare AI MENA، training للأطباء على AI tools، وcontent عن «كيف تبني AI موثوق في القطاع الصحي» — كل hospital system في المنطقة يبحث عن هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من OpenEvidence وثورة Medical AI؟</h3>
        <ul>
          <li><strong>Healthcare AI consulting:</strong> صمّم clinical AI workflows للمستشفيات — 10000–75000 دولار/مشروع.</li>
          <li><strong>Medical content localization:</strong> ترجم وadapt evidence-based content للعربية — 3000–25000 دولار/مشروع.</li>
          <li><strong>دورات «AI للأطباء العرب»:</strong> workshop clinical decision-support — 199–999 دولار/مشارك.</li>
          <li><strong>MENA health AI retainer:</strong> راقب compliance وintegrations شهرياً — 4000–22000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">OpenEvidence</span>
        <span class="tag">Medical AI</span>
        <span class="tag">Clinical AI</span>
        <span class="tag">700K Doctors</span>
        <span class="tag">$12B Valuation</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-07-2026 -- 12-AM</p>
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
