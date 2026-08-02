#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 02-08-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "02-08-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Dili، Modus، Freehand، Harmony، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 2 أغسطس 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من امتثال بنية تحتية بملايين الدولارات إلى وكلاء يُديرون سلاسل التوريد — أربعة محركات AI تُعيد تشكيل اقتصاد 2026!</h1>
      <p class="hero-sub">Dili يجمع 21.7 مليون دولار لأتمتة امتثال مشاريع البنية التحتية، Modus يُطلق Context Warehouse لسياق الوكلاء، Freehand يُحقق 75 مليون دولار لإدارة نفقات سلاسل التوريد، وHarmony يُضمّن 100 وكيل داخل Slack وTeams. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 2 أغسطس 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Dili: 21.7 مليون دولار — عندما يصبح AI «مدقق امتثال» لـ 700 مشروع بنية تحتية!</h2>
      <p class="article-lead">بناء مراكز البيانات ومحطات الطاقة يعني آلاف الصفحات من قوانين Davis-Bacon وPWA وOSHA — وأي خطأ قد يكلّف ملايين الدولارات غرامات. Dili لا يُخمّن: AI يقرأ المستندات، ونظام حتمي يطبّق القواعد بدقة. 700 مشروعاً نشطاً، وKhosla Ventures يقود Series A بـ 15 مليون دولار.</p>
      <p>في 30 يوليو 2026، أعلنت <strong>Dili</strong> — شركة AI للامتثال من San Francisco — عن <strong>Series A بقيمة 15 مليون دولار</strong> بقيادة <strong>Khosla Ventures</strong>، مع Allianz وRebel Fund وDarren Bechtel (Brick and Mortar) وGarry Tan (YC). التمويل الإجمالي وصل إلى <strong>21.7 مليون دولار</strong> بعد seed بـ 6.7 مليون. الشركة من batch Y Combinator Summer 2023.</p>
      <p>المؤسس <strong>Anand Chaturvedi</strong> يُركّز على مشاريع البنية التحتية الأمريكية الممولة فيدرالياً: قوانين الأجور السائدة، متطلبات apprenticeship للطاقة النظيفة، ولوائح EPA وOSHA المتداخلة. المعمارية: LLMs في طبقة البيانات فقط — لتحويل مستندات غير منظمة إلى بيانات structured — ثم <strong>deterministic rules engine</strong> يطبّق القواعد بدون «fuzziness». مهمة تستغرق يوماً كاملاً تُنجَز في دقائق.</p>
      <p>المنصة تُستخدم في <strong>نحو 700 مشروعاً</strong> — من مصانع إلى data centers. نصف العملاء يستخدمون البرمجيات داخلياً، والنصف الآخر يُ outsource الامتثال بالكامل لـ Dili. Chaturvedi: «Software and AI are going to start eating professional services workflows». للمبدعين العرب: consulting لامتثال مشاريع infrastructure في MENA، تكامل ERP + compliance، ودورات «AI for Construction Compliance» — كل مشروع NEOM أو data center regional يحتاج هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dili وثورة امتثال البنية التحتية؟</h3>
        <ul>
          <li><strong>Infrastructure compliance consulting:</strong> نفّذ Dili للمقاولين — 8000–50000 دولار/مشروع.</li>
          <li><strong>Document automation agency:</strong> أتمتة مستندات construction + payroll — retainer 2000–12000 دولار/شهر.</li>
          <li><strong>دورات «AI Compliance for Projects»:</strong> bootcamp للمهندسين — 199–899 دولار.</li>
          <li><strong>MENA data center compliance:</strong> امتثال مشاريع AI infrastructure — 10000–60000 دولار/عقد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dili</span>
        <span class="tag">AI Compliance</span>
        <span class="tag">Infrastructure</span>
        <span class="tag">Khosla Ventures</span>
        <span class="tag">$21.7M Total</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Modus: 10 ملايين دولار — «Context Warehouse» يُعطي الوكلاء السياق الصحيح فقط!</h2>
      <p class="article-lead">الوكيل الذكي يملك access لكل بيانات الشركة — لكنه لا يعرف «أي» سياق يحتاجه الآن. Modus يبني طبقة infrastructure جديدة: Context Warehouse يرسم كيف تعمل المؤسسة فعلياً، ويُسلّم للوكيل شريحة authorized وrelevant فقط — يقلّل tokens بـ 10× ويُحسّن الدقة. 10 ملايين دولار seed من Insight Partners.</p>
      <p>في 29 يوليو 2026، خرجت <strong>Modus</strong> من Tel Aviv من stealth بـ <strong>10 ملايين دولار seed</strong> بقيادة <strong>Insight Partners</strong>، مع Soma Capital وBullet Ventures وEyal Kishon وNadav Abrahami (Wix/Dazl) ومؤسسي Cyera وEpsagon. المؤسسان: <strong>Daniel Shimoni</strong> (CEO، ex-VP Product Lusha) و<strong>Tomer Mesika</strong> (CTO، ex-Head of Architecture Cyera).</p>
      <p>المنتج <strong>Context Warehouse</strong>: infrastructure layer يتعلّم continuously من metadata وusage patterns عبر data warehouses وBI tools وcode repos وdocumentation — <strong>بدون centralizing sensitive data</strong>. Governance controls تُطبَّق قبل وصول أي context للنموذج. يعمل مع أي data warehouse أو AI model، ويدعم MCP (Model Context Protocol). Ganesh Bell (Insight): «Data warehouses became foundational for enterprise data — Modus defines the Context Warehouse for AI».</p>
      <p>النتيجة: accuracy أعلى، response times أسرع، token consumption أقل بـ <strong>حتى 10×</strong>، وgovernance at scale. Modus يُ addressing الـ «context gap» — الفجوة بين قدرة AI ومعرفة كيف تعمل الشركة فعلياً. للمبدعين العرب: implementation لـ enterprise context layers، consulting لـ AI agent governance، وproducts تربط ERP العربية بـ context warehouses — كل bank وtelco في الخليج يبني agents ويحتاج هذه الطبقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Modus وثورة Context Warehouse؟</h3>
        <ul>
          <li><strong>Context layer implementation:</strong> نفّذ Modus للمؤسسات — 12000–70000 دولار/مشروع.</li>
          <li><strong>Agent governance consulting:</strong> صمّم authorized context flows — 8000–45000 دولار.</li>
          <li><strong>دورات «Enterprise AI Context»:</strong> workshop للـ data teams — 299–1299 دولار.</li>
          <li><strong>MENA context integration retainer:</strong> ربط SAP/Oracle بـ AI agents — 3000–18000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Modus</span>
        <span class="tag">Context Warehouse</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">Insight Partners</span>
        <span class="tag">MCP</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Freehand: 75 مليون دولار — وكلاء AI يُديرون نفقات Meta وUnilever وJ&amp;J!</h2>
      <p class="article-lead">Ramp يُدير بطاقات الشركات — Freehand يُدير شيئاً أصعب: logistics، raw materials، MRO، وعقود suppliers معقدة. وكلاء autonomous يقرأون العقود، يُفاوضون الموردين، يكتشفون leakage، ويُغلقون procure-to-pay — Meta وUnilever وPfizer وDunkin' يثقون بهم. 75 مليون دولار Series B، Category Context Graph، و5–10% recovery في النفقات.</p>
      <p>في 29 يوليو 2026، أعلنت <strong>Freehand</strong> من San Francisco عن <strong>Series B بقيمة 75 مليون دولار</strong> بقيادة مشتركة من <strong>Battery Ventures</strong> و<strong>NewRoad Capital Partners</strong>، مع PSP Growth (Penny Pritzker) وNexus Venture Partners. التمويل الإجمالي <strong>100 مليون دولار</strong>. المؤسسان: <strong>Nitin Jayakrishnan</strong> و<strong>Abhijeet Manohar</strong> — co-founders سابقان لـ Pando (TMS/procure-to-pay) الذي باعوه.</p>
      <p>المنصة: <strong>autonomous AI agents</strong> لـ supply-chain spend — procurement، supplier management، invoicing، payments. Built on <strong>Category Context Graph</strong>: reasoning عبر structured وunstructured data، فهم contracts وpolicies، execution مباشرة في collaboration tools وERP (SAP، Oracle، Dynamics، Coupa). Customers: Meta، Unilever، Johnson &amp; Johnson، Pfizer، Dunkin'، Cardinal Health.</p>
      <p>النتائج المclaimed: <strong>5–10% spend recovery</strong>، workflows <strong>5–7× أسرع</strong>، procure-to-pay cycles <strong>أقل بـ 70%</strong>. Freehand يُ positioning كـ بديل لـ BPO وoutsourcing — خاصة مع ضغط tariffs وimmigration على نموذج outsourcing التقليدي. للمبدعين العرب: consulting لـ supply chain AI، implementation للـ logistics MENA، ودورات «AI Procurement Automation» — كل manufacturer وretailer في المنطقة يُ fight cost inflation.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Freehand وثورة supply-chain AI؟</h3>
        <ul>
          <li><strong>Procurement AI implementation:</strong> نفّذ Freehand agents — 15000–80000 دولار/مشروع.</li>
          <li><strong>Spend recovery audit:</strong> اكتشف leakage في عقود logistics — 10000–50000 دولار + % savings.</li>
          <li><strong>دورات «AI Supply Chain Ops»:</strong> bootcamp للـ procurement teams — 349–1499 دولار.</li>
          <li><strong>MENA logistics AI retainer:</strong> إدارة procure-to-pay للـ SMBs — 2500–15000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Freehand</span>
        <span class="tag">Supply Chain AI</span>
        <span class="tag">Procurement</span>
        <span class="tag">Battery Ventures</span>
        <span class="tag">$100M Total</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Harmony: 34 مليون دولار — 100 وكيل جاهز داخل Slack وTeams يُحرّر HR وIT من الطوفان!</h2>
      <p class="article-lead">موظف يسأل HR عن إجازة، IT عن password reset، Finance عن approval — وكل department غرق في tickets متكررة. Harmony لا يبني dashboard آخر — بل يضع agents حيث يعمل الناس: Slack وMicrosoft Teams. 100+ prebuilt agent، deployment في أيام لا أشهر، ومؤسسو Epsagon (بيعوا لـ Cisco بـ 500 مليون) يعودون. 34 مليون seed من Lightspeed!</p>
      <p>في يوليو 2026، أعلنت <strong>Harmony</strong> عن <strong>34 مليون دولار seed</strong> بقيادة <strong>Lightspeed Venture Partners</strong> — valuation seed غير مسبوق لمؤسسين repeat-exit. المؤسسان: <strong>Nitzan Shapira</strong> و<strong>Ran Ribenzaft</strong> — باعوا Epsagon (cloud observability) لـ Cisco بـ <strong>500 مليون دولار</strong> في 2021.</p>
      <p>المنصة: <strong>AI agents embedded</strong> في Slack وTeams للـ employee support. أكثر من <strong>100 prebuilt agent</strong>: onboarding، software access provisioning، password resets، approvals، policy questions — HR، IT، Finance، Legal. Claim: deployment في <strong>أيام</strong> لا أشهر. Investors: Hitachi Ventures، Fin Capital، Mercer Ventures، Operator Partners، وangels من Wiz founding team وAssaf Rappaport.</p>
      <p>الفلسفة: agents حيث employees already type — لا portal منفصل. Security-adjacent cap table (Wiz، Eon.io) يُ signal أن agents touching identity تحتاج CISO approval قبل HR budget. للمبدعين العرب: implementation لـ workplace AI agents، customization للـ policies المحلية، ودورات «Deploy HR/IT Agents in Slack» — كل company hybrid في MENA يُ drowning في internal requests.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Harmony وثورة workplace agents؟</h3>
        <ul>
          <li><strong>Workplace agent deployment:</strong> نفّذ Harmony للشركات — 6000–40000 دولار/مشروع.</li>
          <li><strong>Custom HR/IT agent building:</strong> agents مخصصة للسياسات العربية — 4000–25000 دولار.</li>
          <li><strong>دورات «Slack AI Agents for Ops»:</strong> workshop للـ IT teams — 199–799 دولار.</li>
          <li><strong>MENA employee support retainer:</strong> صيانة agents + policies — 1500–9000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Harmony</span>
        <span class="tag">Slack Agents</span>
        <span class="tag">Microsoft Teams</span>
        <span class="tag">Lightspeed</span>
        <span class="tag">Epsagon Founders</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 02-08-2026 -- 08-AM</p>
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
