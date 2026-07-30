#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 30-07-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "30-07-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — DataBahn، ChipAgents، Encore AI، Oak، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 30 يوليو 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من طبقة بيانات الوكلاء إلى رقائق أسرع ووكلاء صوتية تُدرّ أرباحاً — البنية التحتية التي تُشغّل AI في يوليو 2026!</h1>
      <p class="hero-sub">DataBahn يجمع 40 مليون دولار لبناء «Agentic Data Control Plane»، ChipAgents يُسرّع تصميم الرقائق بـ 60 مليون دولار إضافية، Encore AI يُعلّم الوكلاء الصوتية من نجوم المبيعات الحقيقيين بـ 30 مليون، وOak يُعيد بناء هوية المؤسسات لعصر AI Agents بـ 60 مليون seed. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 30 يوليو 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>DataBahn: 40 مليون دولار — طبقة البيانات الذكية التي تُغذّي كل وكيل AI في المؤسسة!</h2>
      <p class="article-lead">الوكلاء جائعون للسياق — لكن pipelines التقليدية تُغرقهم بـ logs خام وتكاليف تخزين فلكية. DataBahn لا «تنقل» البيانات فقط — بل تُقلّلها، تُثريها، تحكمها، وتُفعّلها في الوقت الفعلي عبر Agent Farm من وكلاء متخصصين. 40 مليون دولار Series B من Insight Partners — والإعلان في 30 يوليو 2026.</p>
      <p>في 30 يوليو 2026، أعلنت <strong>DataBahn</strong> من دallas عن إغلاق <strong>Series B بقيمة 40 مليون دولار</strong> بقيادة <strong>Insight Partners</strong>، مع Forgepoint وGTM Capital وS3 Ventures — إجمالي التمويل <strong>59 مليون دولار</strong>. المؤسس والـ CEO <strong>Nanda Santhana</strong> يُ positioning الشركة كـ «Agentic Data Control Plane» — فئة infrastructure جديدة بين telemetry enterprise وconsumers (SIEM، warehouses، analytics، وAI agents).</p>
      <p>المنصة تستقبل telemetry من <strong>600+ مصدر</strong> بـ neutrality كاملة: أي source، أي destination، أي model — بدون vendor lock-in. التقنية الجديدة <strong>AIDI</strong> (Autonomous In-Stream Data Intelligence) تُفسّر البيانات أثناء تدفّقها — لا بعد وصولها — وتُطبّق governance وenrichment قبل inference. <strong>DataBahn Agent Farm</strong> يُشغّل وكلاء متخصصين: Signal، Sentry، وغيرها — لبناء connectors، validation، gap detection، وحماية البيانات الحساسة in-stream.</p>
      <p>SiliconANGLE وصف DataBahn كـ «foundational to future security architecture» لدى Fortune 500. المشكلة: AI inference وcloud egress يتكلفان بـ volume — DataBahn يُقلّل volume ويُحسّن relevance. للمبدعين العرب: consulting لـ data pipeline modernization، implementation لـ SIEM cost reduction، وproducts على AIDI للـ MENA regulated industries — كل bank في الخليج يُغرق في telemetry costs.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من DataBahn وثورة Agentic Data Control Plane؟</h3>
        <ul>
          <li><strong>Data pipeline optimization:</strong> نفّذ DataBahn لخفض تكاليف SIEM وAI inference — 8000–50000 دولار/مشروع.</li>
          <li><strong>Agent context engineering:</strong> صمّم data feeds للـ AI agents — 5000–35000 دولار.</li>
          <li><strong>دورات «Enterprise Data for AI»:</strong> bootcamp للـ security وdata teams — 249–999 دولار.</li>
          <li><strong>MENA telemetry retainer:</strong> managed data control plane — 2500–15000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">DataBahn</span>
        <span class="tag">Agentic Data Control Plane</span>
        <span class="tag">AIDI</span>
        <span class="tag">Insight Partners</span>
        <span class="tag">$59M Total</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>ChipAgents: 60 مليون دولار إضافية — وكلاء AI يُصمّمون رقائق بـ Verilog جاهز للإنتاج!</h2>
      <p class="article-lead">تصميم رقاقة واحدة يكلّف مئات الملايين ويستغرق سنوات — لكن وكيل AI يُحوّل specification إلى RTL production-ready ويُشخّص bugs في 15 دقيقة بدلاً من أيام. ChipAgents جمع 60 مليون دولار Series A2 من Micron وMediaTek وB Capital — إجمالي 134 مليون — و120+ شركة semiconductor تستخدم المنصة.</p>
      <p>في 29 يوليو 2026، أعلنت <strong>ChipAgents</strong> من Santa Clara عن <strong>60 مليون دولار Series A2</strong> — توسيع Series A إلى <strong>134 مليون دولار</strong>. B Capital قاد الجولة الجديدة؛ Bessemer وMicron وMediaTek وEricsson وScOp شاركوا. المؤسس <strong>William Wang</strong> (أستاذ UC Santa Barbara، ex-Amazon Q) يبني autonomous agents داخل code editor تُخطّط وتُنفّذ chip design وverification independently.</p>
      <p>المنصة: domain-specific agents تُولّد <strong>Verilog وSystemVerilog</strong> production-ready، verification assets، وautomated root-cause analysis. نموذج <strong>Renoir</strong> المتخصص — بالشراكة مع <strong>NVIDIA</strong> — يُركّز على chip design. Whalechip case study: RCA من أيام إلى 15–60 دقيقة، 100% hit rate، منع 1–2 أسبوع تأخير. ARR نما <strong>6×</strong> في H1 2026 — deployment في 120+ semiconductor company.</p>
      <p>Reuters وصف ChipAgents كـ «Nvidia partner» يُسرّع chip design. SOC 2 Type II وon-premises deployment للـ IP sensitivity. للمبدعين العرب: consulting لـ semiconductor AI adoption (MENA chip ambitions)، دورات «AI for Chip Design»، وpartnership مع fabs وdesign houses — UAE وSaudi تستثمر بكثافة في semiconductors.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ChipAgents وثورة AI في تصميم الرقائق؟</h3>
        <ul>
          <li><strong>Semiconductor AI consulting:</strong> نفّذ ChipAgents للـ design houses — 15000–80000 دولار/مشروع.</li>
          <li><strong>Verification automation:</strong> RCA وdebug workflows — 10000–60000 دولار.</li>
          <li><strong>دورات «Agentic Chip Design»:</strong> bootcamp للمهندسين — 399–1999 دولار.</li>
          <li><strong>MENA chip AI liaison:</strong> bridge بين fabs وChipAgents — retainer 4000–25000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ChipAgents</span>
        <span class="tag">Semiconductor AI</span>
        <span class="tag">Verilog Agents</span>
        <span class="tag">NVIDIA Partner</span>
        <span class="tag">$134M Series A</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Encore AI: 30 مليون دولار — وكلاء صوتية تتعلّم من «نجوم المبيعات» لا من scripts جامدة!</h2>
      <p class="article-lead">معظم وكلاء call center تُصمّم لـ «تقليل المكالمات» — Encore AI بُنيت لـ «زيادة الإيرادات». Interaction Mining يُحلّل ملايين المكالمات والإيميلات، يستخرج ما يفعله أفضل 10% من الموظفين، ويُحوّله إلى agents صوتية ونصية autonomously — أو Wingman يُ assist البشر live. 10× ROI لعميل lending خلال أشهر.</p>
      <p>في 29 يوليو 2026، أعلنت <strong>Encore AI</strong> (formerly Insait IO) عن <strong>Series A بقيمة 30 مليون دولار</strong> بقيادة <strong>Team8</strong> وPlanven وThe Garage. المؤسس <strong>Dr. Dvir Ginzburg</strong> (CEO) بدأ 2022 بـ recommendation software للـ financial advisers — الآن platform enterprise كاملة. 40+ enterprise customer في banks وinsurance وhealthcare.</p>
      <p>التقنية <strong>Interaction Mining</strong> (patented): تجميع calls، chats، emails، CRM — تقسيم interactions لمراحل — تحديد ما يُحرّك conversion — deploy كـ autonomous agents أو <strong>Wingman</strong> real-time assistant. Channels: voice، chat، IVR، live form-fill — أي لغة — compliance للـ regulated environments. Go-live في <strong>أسابيع</strong> لا أشهر — لا tuning manual طويل.</p>
      <p>TechCrunch وصف Encore كـ «AI agents that learn from customer calls». Thesis: revenue-oriented لا cost-deflection. Ginzburg: «نركّز على كل interaction — نحلّل كيف يؤدّيها الممثلون اليوم ونبني agents أفضل». للمبدعين العرب: implementation لـ banks وinsurance MENA، consulting لـ Interaction Mining، وproducts «Arabic revenue agents» — call centers في الخليج ضخمة وتحتاج conversion لا deflection.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Encore AI وثورة Revenue Agents؟</h3>
        <ul>
          <li><strong>Revenue agent deployment:</strong> نفّذ Encore للـ banks وinsurance — 12000–70000 دولار/مشروع.</li>
          <li><strong>Interaction Mining consulting:</strong> استخرج top-performer patterns — 8000–45000 دولار.</li>
          <li><strong>دورات «AI Revenue Operations»:</strong> workshop للـ sales وCX teams — 299–1299 دولار.</li>
          <li><strong>Arabic voice agent studio:</strong> localized agents للـ MENA — retainer 3000–20000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Encore AI</span>
        <span class="tag">Interaction Mining</span>
        <span class="tag">Revenue Agents</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Team8</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Oak: 60 مليون دولار seed — نظام تشغيل الهوية الذي يُحكم البشر والآلات والوكلاء معاً!</h2>
      <p class="article-lead">AI agents تستخدم credentials موظفين حقيقيين — وidentity stacks المجزّأة لا تُميّز بين إنسان وmachine وagent. Shai Morag (3 exits بـ 500 مليون دولار) يبني Identity Operating System: live identity graph، risk decisions real-time، وremediation — لكل identity type في مؤسسة واحدة. 60 مليون seed — أكبر seed rounds في Israeli cyber.</p>
      <p>في 15 يوليو 2026، خرجت <strong>Oak</strong> من stealth بـ <strong>60 مليون دولار seed</strong> co-led من <strong>Accel</strong> و<strong>Greylock Partners</strong> و<strong>CRV</strong> — Hetz Ventures وAlphaDrive Ventures شاركوا. المؤسسان: <strong>Shai Morag</strong> (CEO، ex-Ermetic/Tenable CPO) و<strong>Tal Marom</strong> (CPO، ex-Tenable/Salesforce). ~50 موظفاً في Tel Aviv وSan Francisco — platform generally available مع enterprise customers.</p>
      <p>المنصة: <strong>AI connector framework</strong> يصل أي application (cloud، on-prem، SaaS، homegrown) — يبني <strong>live identity graph</strong> من raw evidence — يُ govern lifecycle لكل identity: employees، contractors، machines، <strong>AI agents</strong>. يُ mapping access held vs access used — AI-built risk decisions وroot-cause remediation. Morag تحدّث 100+ CISO: «too many tools، unable to see how access is used».</p>
      <p>TechCrunch: «fix the identity mess that AI agents are making worse». Accel's Brasoveanu: «identity is the biggest problem left standing». للمبدعين العرب: Oak implementation للـ enterprises MENA، consulting لـ non-human identity governance، ودورات «IAM for AI Agents» — كل government وbank في المنطقة يُ deploying agents بدون identity strategy.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Oak وثورة AI-Native Identity؟</h3>
        <ul>
          <li><strong>Identity OS implementation:</strong> نفّذ Oak للمؤسسات — 10000–60000 دولار/مشروع.</li>
          <li><strong>Agent identity audits:</strong> inventory وpolicies للـ AI agents — 5000–30000 دولار.</li>
          <li><strong>دورات «IAM for AI Era»:</strong> bootcamp للـ security teams — 349–1499 دولار.</li>
          <li><strong>MENA identity governance retainer:</strong> ongoing IAM + agent control — 3500–22000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Oak</span>
        <span class="tag">Identity OS</span>
        <span class="tag">AI Agents IAM</span>
        <span class="tag">Shai Morag</span>
        <span class="tag">$60M Seed</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 30-07-2026 -- 04-PM</p>
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
