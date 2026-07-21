#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 21-07-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "21-07-2026 -- 08-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Fugu-Cyber، Squirro Agent Catalog، Coasty، Agent Steward، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 21 يوليو 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من أمن سيبراني بـ 86.9% دقة إلى وكيل يملك مشكلة العميل بالكامل — الذكاء الاصطناعي يتحوّل إلى «قوة تنفيذية» لا مجرد محادثة!</h1>
      <p class="hero-sub">Sakana AI تُطلق Fugu-Cyber اليوم ليُنسّق فرق agents أمنية بـ 86.9% على CyberGym، Squirro تُنهي «البداية من الصفر» بـ 13 agent جاهز للمؤسسات المنظّمة، Coasty من YC S26 يفتح API لوكلاء يتحكمون بالكمبيوتر، وDelight.ai يُقدّم Agent Steward — أول وكيل يملك حل مشاكل العملاء end-to-end. أربع ثورات عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 21 يوليو 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Fugu-Cyber من Sakana AI: orchestration model يُحقّق 86.9% على CyberGym — أمن سيبراني multi-agent بـ endpoint واحد!</h2>
      <p class="article-lead">الدفاع السيبراني لم يعد «نموذجاً واحداً يُجيب على prompts». المعركة الحقيقية multi-step: تحليل، استكشاف، تحقق، إصلاح. Fugu-Cyber يتصرّف كنموذج واحد — لكنه يُنسّق pool من agents متخصصين ديناميكياً.</p>
      <p>في 21 يوليو 2026، أعلنت <strong>Sakana AI</strong> — المختبر الياباني الذي يُعيد تعريف AI orchestration — عن إطلاق <strong>Fugu-Cyber</strong> كـ API endpoint جديد. النتائج على benchmarks الصناعية الأصعب: <strong>86.9%</strong> على CyberGym و<strong>72.1%</strong> على CTI-REALM — أداء comparable لـ GPT-5.5-Cyber وMythos-Preview.</p>
      <p>الفكرة الجوهرية: <strong>multi-agent system يتصرّف كنموذج واحد</strong>. تُرسل request لـ endpoint واحد، والنظام يُنسّق agents متخصصين لمهام multi-step معقدة — بدون vendor lock-in على lab واحد. Sakana تعمل مع مؤسسات يابانية كبرى لبناء harnesses وworkflows production-ready: automated vulnerability verification، threat intelligence، incident response.</p>
      <p>متاح اليوم على <strong>sakana.ai/fugu</strong> ضمن Token Plan. للمبدعين العرب في cybersecurity وMENA fintech: فرصة لبناء «Fugu-Cyber integration services»، consulting لـ SOC automation، ودورات «أمن AI multi-agent» — قبل أن تُصبح orchestration standard في كل bank وtelco خليجي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Fugu-Cyber؟</h3>
        <ul>
          <li><strong>SOC automation consulting:</strong> ادمج Fugu-Cyber في workflows أمنية للبنوك والحكومات — مشروع 5000–35000 دولار.</li>
          <li><strong>Threat intel pipelines:</strong> ابنِ pipelines CTI-REALM مخصّصة للشركات MENA — 3000–18000 دولار.</li>
          <li><strong>دورات «أمن AI Orchestration»:</strong> bootcamp لـ SecOps teams — 149–699 دولار.</li>
          <li><strong>Managed cyber agents:</strong> شغّل Fugu-Cyber لعملاء SMB — retainer 1500–8000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sakana AI</span>
        <span class="tag">Fugu-Cyber</span>
        <span class="tag">Cybersecurity</span>
        <span class="tag">Multi-Agent</span>
        <span class="tag">Orchestration</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Squirro Agent Catalog: 13 وكيل جاهز للمؤسسات — الوكيل الثاني لا يبدأ من الصفر!</h2>
      <p class="article-lead">أكبر عائق أمام AI في المؤسسات ليس التقنية — بل «البداية من الصفر» في كل مشروع. Squirro تُنهي هذه المعضلة: Agent Catalog يُورّث connections وdata وapprovals من agent لآخر.</p>
      <p>في 20 يوليو 2026، أعلنت <strong>Squirro</strong> — منصة enterprise AI بعملاء مثل <strong>Deutsche Bundesbank</strong> و<strong>Henkel</strong> و<strong>European Central Bank</strong> — عن general availability لـ <strong>Agent Catalog</strong>: أكثر من <strong>13 agent</strong> جاهز للإنتاج في finance وHR وlegal وsales وoperations وIT.</p>
      <p>المنطق الذكي: <strong>الوكيل الأول يُنجز compliance review</strong> — كل agent يليه يبني عليه. Instaquote Agent يحوّل طلبات العملاء إلى quotations SAP مع confidence score على كل خطوة. Sales Enablement Knowledge Hub Agent يرتّب المحتوى حسب deal stage وindustry وcompetitor. HR Compliance Agent يُجيب على أسئلة labor law مع citation trail كامل.</p>
      <p>كل agent يُجيب من verified enterprise data — الحالات الروتينية تُحلّ تلقائياً، والغامض يُوجّه لإنسان مع full context. للمبدعين العرب في regulated industries: فرصة لبناء «Squirro implementation» للبنوك والتأمين، customization لـ agents عربية، ودورات «AI للمؤسسات المنظّمة» — Squirro HQ في Zurich مع teams في Singapore وUSA.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Squirro Agent Catalog؟</h3>
        <ul>
          <li><strong>Enterprise agent deployment:</strong> نشر agents Squirro للبنوك والتأمين MENA — مشروع 8000–45000 دولار.</li>
          <li><strong>Arabic agent customization:</strong> طوّر agents HR وlegal بالعربية — 4000–20000 دولار.</li>
          <li><strong>Compliance consulting:</strong> ساعد مؤسسات تُجتاز أول compliance review — 3000–15000 دولار.</li>
          <li><strong>دورات «AI Agents للمؤسسات»:</strong> workshop للـ CIO teams — 199–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Squirro</span>
        <span class="tag">Agent Catalog</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">Regulated Industries</span>
        <span class="tag">Compliance</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Coasty من YC S26: API لوكلاء يتحكمون بالكمبيوتر — أتمتة المهام الرقمية المعقدة!</h2>
      <p class="article-lead">Computer-use agents — وكلاء يُحرّكون الماوس، يملؤون forms، يتصفحون apps — كانت حكراً على labs كبرى. Coasty يفتح API عاماً لبناء agents تعمل عبر أي software environment.</p>
      <p>في يوليو 2026، أطلقت <strong>Coasty</strong> — startup من <strong>YC S26</strong> بقيادة <strong>Nitish</strong> و<strong>Prateek</strong> — API لبناء <strong>computer-use agents</strong>. المنصة تُمكّن developers من إنشاء agents تُنفّذ مهام رقمية معقدة: data management، web automation، digital interactions — عبر environments مختلفة.</p>
      <p>Coasty يُؤكّد: agents مصمّمة للمرونة — automation في personal وenterprise contexts. الهدف: <strong>تقليل manual effort وزيادة productivity</strong> عبر AI-driven automation. API متاح publicly، early adopters يختبرون capabilities — roadmap يشمل integrations موسّعة وcommunity developer.</p>
      <p>للمبدعين العرب في automation وRPA: فرصة لبناء «Coasty agencies» لـ SMBs، consulting لـ workflow automation، ودورات «Computer-use Agents للمطورين» — السوق ينمو مع agentic AI وكل شركة تريد أتمتة tasks بدون API integration.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Coasty؟</h3>
        <ul>
          <li><strong>Workflow automation agency:</strong> ابنِ agents Coasty لـ SMBs عربية — مشروع 2000–12000 دولار.</li>
          <li><strong>RPA replacement consulting:</strong> استبدل RPA تقليدي بـ computer-use agents — 4000–25000 دولار.</li>
          <li><strong>دورات «Computer-use Agents»:</strong> bootcamp للمطورين — 99–449 دولار.</li>
          <li><strong>Managed automation:</strong> شغّل agents لعملاء — retainer 800–5000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Coasty</span>
        <span class="tag">YC S26</span>
        <span class="tag">Computer-Use Agents</span>
        <span class="tag">Automation</span>
        <span class="tag">API</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Agent Steward من Delight.ai: أول وكيل AI يملك مشكلة العميل end-to-end — عبر أنظمة وفرق وقنوات!</h2>
      <p class="article-lead">chatbots تُجيب على السؤال وتنتهي. Agent Steward يأخذ ownership كاملاً: يُنسّق عبر أنظمة، يُتخذ قرارات ضمن guardrails، ويتابع العميل wherever they are — حتى لو استغرق الحل ساعات.</p>
      <p>في يوليو 2026، أعلنت <strong>Delight.ai</strong> عن <strong>Agent Steward</strong> — «أول fully autonomous AI agent يأخذ ownership لمشاكل العملاء المعقدة ويحلّها end-to-end». Steward لا يُجيب فقط — يُنسّق عبر systems وteams وchannels، يُتخذ decisions ضمن guardrails، ويتابع العميل على أي قناة.</p>
      <p>الحالة المثالية: عميل يحتاج <strong>ثلاثة أشياء عبر أربعة أنظمة وطرفين ثالثين</strong> — ما يأخذ أفضل agent ساعات. Steward يحلّها live مع data العميل في fraction من الوقت. generally available اليوم — Delight تدعو teams لاختبار use cases «المدفونة في coordination work».</p>
      <p>للمبدعين العرب في customer experience وBPO: فرصة لبناء «Steward implementation» للشركات MENA، consulting لـ complex case automation، ودورات «AI Customer Ownership» — CX automation سوق ضخم في Gulf retail وbanking.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Agent Steward؟</h3>
        <ul>
          <li><strong>CX automation consulting:</strong> نشر Steward للـ retail وbanking MENA — مشروع 6000–40000 دولار.</li>
          <li><strong>Complex case workflows:</strong> صمّم guardrails وworkflows لـ use cases محلية — 3500–20000 دولار.</li>
          <li><strong>دورات «AI Customer Ownership»:</strong> bootcamp لـ CX teams — 149–649 دولار.</li>
          <li><strong>Managed Steward ops:</strong> شغّل Steward لعملاء — retainer 2000–10000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Delight.ai</span>
        <span class="tag">Agent Steward</span>
        <span class="tag">Customer Experience</span>
        <span class="tag">Autonomous Agents</span>
        <span class="tag">CX Automation</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 21-07-2026 -- 08-AM</p>
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
