#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-08-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "08-08-2026 -- 12-AM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Acrab، Cloudflare Kitesurf، Meta Muse Code، Hark Handoff، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 أغسطس 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من رقائق Edge إلى متصفحات الوكلاء — أربع ثورات تُعيد رسم «البنية التحتية» لعصر AI في أغسطس 2026!</h1>
      <p class="hero-sub">Acrab يجمع 130 مليون دولار ويُطلق GΞLIX 1 وAgent Box لحوسبة الوكلاء على الحافة، Cloudflare يبني Kitesurf — متصفحاً سحابياً مُصمّماً للوكلاء لا للبشر، Meta Muse Code يُطلق وكيلاً يُدير مستودعات ضخمة بـ sub-agents متوازية، وHark Handoff يُحوّل أي موقع ويب إلى مهمة تُنجَز بضغطة واحدة. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 8 أغسطس 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Acrab: 130 مليون دولار — رقاقة GΞLIX 1 وAgent Box: الوكلاء على الحافة بين يديك!</h2>
      <p class="article-lead">معظم الوكلاء اليوم يعيشون في السحابة — بطيئون، مكلفون، ومنقطعون عن العالم الحقيقي. Acrab يبني العكس: منصة حوسبة كاملة — silicon مُخصّص، edge AI، وبرمجيات orchestration — تُشغّل وكلاء شخصيين على أجهزتك وبيئتك المحلية. 130 مليون دولار Series B و350 مليون دولار إجمالي — والإيرادات متوقعة هذا العام.</p>
      <p>في 6 أغسطس 2026، أعلنت <strong>Acrab</strong> عن <strong>Series B بقيمة 130 مليون دولار</strong> بمشاركة <strong>Vertex Ventures SEA &amp; India</strong> و<strong>Vertex Growth</strong> ومستثمرين مؤسسيين من أوروبا وجنوب شرق آسيا. الشركة — تأسست 2024 — خرجت من stealth بـ <strong>أكثر من 350 مليون دولار</strong> تمويل تراكمي.</p>
      <p>المنتجان المحوريان: <strong>GΞLIX 1</strong> — System-on-Chip مُصمّم خصيصاً لحوسبة الوكلاء على الحافة — و<strong>Agent Box</strong>، منصة متكاملة تُشغّل وكلاء AI شخصيين يُقدّمون مساعدة فورية وتنفيذاً real-time عبر بيئات edge متنوعة. Acrab يجمع بين silicon مُخصّص، نماذج edge AI، وبرمجيات orchestration full-stack.</p>
      <p>الرؤية: الوكلاء ليسوا chatbots في المتصفح — بل طبقة حوسبة جديدة تُجلب المساعدة والإبداع والفائدة إلى حياتك اليومية. التمويل الجديد يُسرّع توسّع المنتج والنظام البيئي والجيل التالي من منصة الحوسبة. للمبدعين العرب: استشارات edge AI، تكامل Agent Box للمنازل الذكية والتجزئة والرعاية الصحية، ودورات «Physical + Agentic AI» — فرصة قبل أن يُشبع السوق.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Acrab وثورة Edge Agentic AI؟</h3>
        <ul>
          <li><strong>Edge agent deployment:</strong> نشر Agent Box للـ retail وhealthcare وlogistics — 12000–70000 دولار/مشروع.</li>
          <li><strong>IoT + agent integration:</strong> ربط أجهزة smart home بـ edge agents — 8000–45000 دولار.</li>
          <li><strong>دورات «Edge AI &amp; Agent Compute»:</strong> bootcamp للمهندسين — 249–1299 دولار.</li>
          <li><strong>MENA pilot partnerships:</strong> deployments تجريبية مع Acrab ecosystem — 20000–100000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Acrab</span>
        <span class="tag">GELIX 1</span>
        <span class="tag">Agent Box</span>
        <span class="tag">Edge AI</span>
        <span class="tag">$130M Series B</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Cloudflare Kitesurf: متصفح سحابي مُبنى للوكلاء — وليس للبشر!</h2>
      <p class="article-lead">Chrome وSafari بُنيا للبشر: tabs، themes، extensions. الوكلاء لا يحتاجون أيّاً من ذلك — بل إدارة context windows، token costs، scalability، وحماية من prompt injection. Cloudflare بنى Kitesurf في 12 أسبوعاً فقط: متصفح headless سحابي يعمل على Workers، يستهلك ذاكرة أقل وtokens أقل — ومجاني في beta.</p>
      <p>في 7 أغسطس 2026، أعلنت <strong>Cloudflare</strong> عن <strong>Kitesurf</strong> — متصفح سحابي مُصمّم <strong>للوكلاء لا للبشر</strong>. الفكرة: بدلاً من أن يبني كل مطوّر browser infrastructure من الصفر، يستخدم Kitesurf عبر <strong>Browser Run</strong> للتحكم programmatically في headless browser instances على شبكة Cloudflare.</p>
      <p>التقنيات: rendering engine من Blitz، CSS parser Stylo من Firefox، وBoa JS — Rust ECMAScript engine. كل شيء يعمل داخل Cloudflare Workers. Kitesurf يجتاز <strong>215,000+ web platform tests</strong> ويُضيف المزيد أسبوعياً. Threat model مختلف: prompt injection، agent vulnerabilities، وcost exhaustion — كلها considerations مُدمجة.</p>
      <p>Cloudflare تقول: الوكلاء يتصفحون الويب بكفاءة أعلى واستهلاك compute أقل — مما يُخفّض التكاليف. للمبدعين العرب: بناء agent products على Kitesurf/Browser Run، consulting لـ browser automation، ودورات «Agent Web Navigation» — بدون إدارة infrastructure.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cloudflare Kitesurf؟</h3>
        <ul>
          <li><strong>Agent product development:</strong> بناء أدوات web automation على Kitesurf — 5000–40000 دولار/مشروع.</li>
          <li><strong>Browser agent consulting:</strong> تصميم workflows للـ e-commerce وresearch — 3000–25000 دولار.</li>
          <li><strong>دورات «Cloudflare Browser Run»:</strong> workshop للمطورين — 149–699 دولار.</li>
          <li><strong>Managed agent browsing:</strong> retainer لصيانة وكلاء web — 1500–8000 دولار/شهر.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cloudflare</span>
        <span class="tag">Kitesurf</span>
        <span class="tag">Browser Run</span>
        <span class="tag">Agent Browser</span>
        <span class="tag">Workers</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Meta Muse Code: وكيل برمجة يُدير مستودعات ضخمة — وworking copy لا يُمس أبداً!</h2>
      <p class="article-lead">Codex وClaude Code يتنافسان على المطورين. Meta تدخل السباق بـ Muse Code — وكيل terminal يُخطّط ويكتب ويُ validate عبر مستودعات ضخمة، ويُ launch sub-agents متوازية في worktrees معزولة. working copy الأصلي لا يُمس أبداً. مدعوم بـ Muse Spark — وMeta تُ pitch التكلفة كميزة تنافسية.</p>
      <p>في 5 أغسطس 2026، أطلقت <strong>Meta</strong> <strong>Muse Code</strong> في beta — وكيل terminal coding يُنجز «complete software engineering tasks across large repos». CEO <strong>Mark Zuckerberg</strong> قال: التخطيط، كتابة الكود، والتحقق من النتائج — كلها في agent واحد.</p>
      <p>التثبيت: أمر واحد. Muse Code يُ launch sub-agents تعمل <strong>simultaneously</strong> — كل واحد في isolated worktree. مثال: «build six features for a game» — ستة agents، ستة worktrees، working copy الأصلي intact. مدعوم بـ <strong>Muse Spark</strong> — coding model سابق الإطلاق.</p>
      <p>Alexandr Wang (Meta AI chief) لـ Wall Street Journal: «incredibly good option, especially from a cost perspective». Meta توسّعت في يونيو إلى enterprise AI agents للـ customer service. للمبدعين العرب: consulting لـ Muse Code adoption، دورات «Multi-Agent Code Development»، وmanaged refactoring services — Meta تُ compete على السعر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meta Muse Code؟</h3>
        <ul>
          <li><strong>Large repo refactoring:</strong> campaigns بـ Muse Code للشركات — 10000–60000 دولار/مشروع.</li>
          <li><strong>Multi-agent dev consulting:</strong> إعداد worktrees وworkflows — 5000–30000 دولار.</li>
          <li><strong>دورات «Muse Code &amp; Agentic Dev»:</strong> bootcamp للمطورين — 199–999 دولار.</li>
          <li><strong>Code migration services:</strong> legacy → modern stack بـ parallel agents — 15000–80000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meta</span>
        <span class="tag">Muse Code</span>
        <span class="tag">Muse Spark</span>
        <span class="tag">Coding Agent</span>
        <span class="tag">Multi-Agent</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Hark Handoff: 700 مليون دولار Series A — وكيل يُحجز طيرانك ويتسوّق ويُراسل LinkedIn!</h2>
      <p class="article-lead">معظم browser agents بطيئة ومكلفة. Hark — startup Brett Adcock بـ 700 مليون دولار Series A — أطلقت Handoff: computer use agent يتنقل على Target وWalmart وOpenTable وLinkedIn بدون APIs رسمية. يُ predict «next action» لا next token — أسرع وأرخص من GPT-5.5 وOpus 4.8. Waitlist مفتوح — الإطلاق نهاية الصيف.</p>
      <p>في 5 أغسطس 2026، أعلنت <strong>Hark</strong> عن <strong>Handoff</strong> — computer use agent (CUA) يُكمل مهام end-to-end: طلب طعام على DoorDash، حجز flights على United وDelta، messaging candidates على LinkedIn. CEO <strong>Brett Adcock</strong> (serial entrepreneur وroboticist) — Hark جمعت <strong>700 مليون دولار Series A</strong> في مايو 2026.</p>
      <p>التقنية: post-trained model الآن، pre-training لاحقاً هذا العام. Handoff ينظر إلى website structure وvisual data — clicks وkeyboard inputs. يتنقل على sites بدون official APIs. Hark claims: أسرع من المنافسين وأرخص بكثير. Demo: بناء bouquet بزهور مُحددة + «florist's choice» fuzzy terms.</p>
      <p>Sign-ups على hark.com — availability لاحقاً هذا الشهر. Security وprivacy «primary focus» — technical preview. للمبدعين العرب: automation consulting للـ e-commerce وtravel، content عن browser agents، ودورات «Computer Use Agents» — Hark يُ redefine ما يمكن للوكيل فعله على الويب المفتوح.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hark Handoff وثورة Computer Use Agents؟</h3>
        <ul>
          <li><strong>Web automation consulting:</strong> workflows للـ travel وshopping وHR — 8000–50000 دولار/مشروع.</li>
          <li><strong>Agent demo content:</strong> فيديوهات وtutorials — monetization عبر sponsorships.</li>
          <li><strong>دورات «Browser Use Agents»:</strong> bootcamp — 249–1299 دولار.</li>
          <li><strong>MENA e-commerce automation:</strong> Handoff-style agents للمتاجر المحلية — 10000–60000 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hark</span>
        <span class="tag">Handoff</span>
        <span class="tag">Computer Use Agent</span>
        <span class="tag">Browser Automation</span>
        <span class="tag">$700M Series A</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-08-2026 -- 12-AM</p>
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
