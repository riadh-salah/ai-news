#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 13-08-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "news" / "13-08-2026 -- 04-PM.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — LangChain Deep Agents، ImagineArt Fashion Studio، HappyRobot، Zed Delta، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 13 أغسطس 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من وكلاء LangChain إلى أزياء AI وعمليات المليار دولار — أربع ثورات تُعيد رسم خريطة الذكاء الاصطناعي في أغسطس 2026!</h1>
      <p class="hero-sub">LangChain تُطلق Managed Deep Agents للإنتاج الفوري، ImagineArt يُلغي استوديوهات التصوير بالأزياء، HappyRobot يُصبح يونيكورن بـ 150 مليون دولار، وZed تُطلق Delta — بيئة متعددة اللاعبين لمراجعة كود الوكلاء. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 13 أغسطس 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>LangChain Managed Deep Agents: من النموذج الأول إلى الإنتاج بأمر واحد — والسحابة الخاصة أصبحت جاهزة!</h2>
      <p class="article-lead">بناء وكيل ذكاء اصطناعي أصبح سهلاً — لكن نشره في الإنتاج مع الذاكرة والتقييم والأمان ظلّ كابوساً للمطورين. LangChain أغلقت هذه الفجوة بـ Managed Deep Agents: من Python أو TypeScript إلى runtime مُدار بأمر واحد، مع LangSmith BYOC على AWS في توفر عام.</p>
      <p>في 13 أغسطس 2026، أعلنت <strong>LangChain</strong> عن <strong>Managed Deep Agents</strong> في معاينة عامة — منصة تُبسّط بناء وتشغيل ونشر Deep Agents دون إدارة البنية التحتية يدوياً. المنصة تُوفّر runtime مدمجاً، بثاً مباشراً (streaming)، sandboxes آمنة، أدوات تقييم (evals)، ذاكرة دائمة، ومصادقة (auth) — كل ما يحتاجه المطور للانتقال من prototype إلى production scale.</p>
      <p>سير العمل بسيط: اكتب وكيلك بـ Python أو TypeScript، اختبره محلياً، ثم انشره بأمر CLI واحد. LangSmith يتولى runtime وmemory mounts وskill loading — بينما تركّز أنت على منطق الوكيل. المعاينة العامة متاحة في منطقة LangSmith Cloud الأمريكية، مع CLI-first بينما يُستكمل API الرسمي.</p>
      <p>بالتوازي، وصل <strong>LangSmith Bring Your Own Cloud (BYOC)</strong> على <strong>Amazon Web Services</strong> إلى التوفر العام (GA) — مما يتيح للمؤسسات الكبرى observability وتقييم ونشر تطبيقات AI داخل VPC الخاص بها. للمبدعين العرب: كل شركة تريد وكلاء مخصّصين دون إرسال بياناتها للسحابة العامة — consulting وdeployment وtraining فرصة ذهبية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من LangChain Managed Deep Agents؟</h3>
        <ul>
          <li><strong>وكالة نشر وكلاء للإنتاج:</strong> انشر Deep Agents للشركات العربية — 8000–50000 دولار/مشروع.</li>
          <li><strong>LangSmith BYOC consulting:</strong> إعداد observability داخل VPC للمؤسسات — 15000–80000 دولار.</li>
          <li><strong>قوالب وكلاء جاهزة:</strong> بناء وبيع حزم agents لمجالات محددة (HR، مبيعات، دعم) — 49–499 دولار.</li>
          <li><strong>دورات «Deep Agents للإنتاج»:</strong> bootcamp للمطورين العرب — 199–999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">LangChain</span>
        <span class="tag">Deep Agents</span>
        <span class="tag">LangSmith</span>
        <span class="tag">BYOC</span>
        <span class="tag">Production AI</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>ImagineArt AI Fashion Studio: تصوير أزياء احترافي بلا عارضات ولا استوديو — من صورة إلى فيديو إعلان!</h2>
      <p class="article-lead">صناعة الأزياء تنفق مليارات على جلسات التصوير — عارضات، مصورون، استوديوهات، مونتاج. ImagineArt أطلقت AI Fashion Studio: أنشئ عارضة AI قابلة لإعادة الاستخدام، ارتدِها بملابس حقيقية، واحصل على صور وفيديوهات بجودة تحريرية — ثم حوّلها لإعلان TikTok أو فيلم سينمائي دون البدء من الصفر.</p>
      <p>في 13 أغسطس 2026، أعلنت <strong>ImagineArt</strong> من الولايات المتحدة عن <strong>AI Fashion Studio</strong> — أداة تُولّد تصوير أزياء بجودة كتالوج وتحريرية دون عارضة فعلية أو استوديو أو مصور. المنصة تسمح للعلامات التجارية ببناء <strong>عارضة AI قابلة لإعادة الاستخدام</strong>، ارتداءها بملابس حقيقية، وتوليد صور أو فيديو من سير عمل واحد.</p>
      <p>القوة الحقيقية في <strong>التكامل</strong>: جلسة Fashion Studio تنتقل تلقائياً إلى أدوات ImagineArt الأخرى. <strong>AI Ad Studio</strong> يحوّل نفس العارضة إلى فيديو إعلان (UGC، unboxing، virtual try-on) بمقاسات Meta وTikTok وYouTube. <strong>AI Film Studio</strong> يُضفي معالجة سينمائية مع تحكم بالكاميرا واستمرارية الشخصية. <strong>Audio Studio</strong> يُضيف تعليقاً صوتياً أو موسيقى أصلية — كل ذلك في نفس السير.</p>
      <p>للمبدعين العرب في التجارة الإلكترونية والأزياء والمحتوى: متاجر العباءات والحجاب وملابس الأطفال يمكنها الآن إنتاج كتالوجات كاملة بـ 10% من تكلفة التصوير التقليدي — مع إمكانية اختبار A/B لعشرات التصاميم يومياً.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ImagineArt AI Fashion Studio؟</h3>
        <ul>
          <li><strong>استوديو تصوير أزياء AI:</strong> قدّم جلسات كتالوج للمتاجر الإلكترونية — 200–1500 دولار/جلسة.</li>
          <li><strong>إعلانات UGC للعلامات:</strong> حوّل صور المنتجات إلى فيديوهات TikTok/Instagram — 150–800 دولار/فيديو.</li>
          <li><strong>White-label للوكالات:</strong> اشترك في ImagineArt وأعد بيع الخدمة للعملاء — هامش 40–60%.</li>
          <li><strong>دورات «AI Fashion Marketing»:</strong> علّم أصحاب المتاجر العرب — 99–499 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ImagineArt</span>
        <span class="tag">Fashion AI</span>
        <span class="tag">AI Ad Studio</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Video Ads</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>HappyRobot: 150 مليون دولار — يونيكورن بقيمة 1.2 مليار دولار يُشغّل عمليات المؤسسات بالوكلاء!</h2>
      <p class="article-lead">الذكاء الاصطناعي لم يعد يُجيب على الأسئلة فقط — بل يُنجز العمل. HappyRobot جمع 150 مليون دولار Series C بقيمة 1.2 مليار دولار، و150+ عميل enterprise من DHL إلى Uber — وكلاء يُديرون مكالمات، إيميلات، مستندات، وعمليات معقدة عبر 4–12 أسبوعاً للنشر الأول.</p>
      <p>في أغسطس 2026، أعلنت <strong>HappyRobot</strong> — منصة عمليات AI-native — عن <strong>Series C بقيمة 150 مليون دولار</strong> بقيادة <strong>Prysm Capital</strong> و<strong>Eurazeo</strong>، مع مشاركة a16z وBase10 وY Combinator وKoch Disruptive Technologies وOrange وDeutsche Telekom T.Capital وBankinter. التمويل الإجمالي يتجاوز 200 مليون دولار.</p>
      <p>المنصة تُنشئ وكلاء AI يُنفّذون العمل داخل أنظمة المؤسسة الحالية — مكالمات هاتفية، إيميلات، مستندات، وعمليات منفصلة. في <strong>الخدمات المالية</strong>: وكلاء يُديرون مكالمات التحصيل، استفسارات الحسابات، جمع المستندات، وفحوصات KYC. في <strong>التأمين</strong>: جمع معلومات المطالبات، التحقق من البوليصات، متابعة المستندات الناقصة. الحالات المعقدة تُصعَّد للبشر.</p>
      <p>الشركة نمت <strong>5×</strong> منذ Series B، وتخدم DHL وKuehne + Nagel وNaturgy وRepsol وUber. للمبدعين العرب: كل بنك ومؤمّن وشركة لوجستics في MENA لديها مراكز اتصال وعمليات يدوية — استشارات نشر الوكلاء ووكلاء صوت عربية فرصة بملايين الدولارات.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HappyRobot وثورة agentic operations؟</h3>
        <ul>
          <li><strong>HappyRobot implementation partner:</strong> نشر وكلاء للبنوك والتأمين — 20000–100000 دولار/مشروع.</li>
          <li><strong>Arabic voice agent layer:</strong> طبقة عربية فوق المنصة للـ MENA — 10000–60000 دولار.</li>
          <li><strong>Operations AI audit:</strong> تحليل العمليات وتحديد فرص الأتمتة — 5000–30000 دولار.</li>
          <li><strong>دورات «Enterprise AI Agents»:</strong> workshop للمديرين التنفيذيين — 299–1999 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HappyRobot</span>
        <span class="tag">Agentic AI</span>
        <span class="tag">$150M Series C</span>
        <span class="tag">Unicorn</span>
        <span class="tag">Enterprise Ops</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Zed Delta: بيئة متعددة اللاعبين لمراجعة كود الوكلاء — البرمجة بالذكاء الاصطناعي أصبحت رياضة جماعية!</h2>
      <p class="article-lead">الوكلاء يكتبون آلاف الأسطر في ثوانٍ — لكن المراجعة تبقى فردية وبطيئة. Zed أطلقت Delta: تطبيق مستقل (ليس plugin) يُزامن المحادثة وشجرة العمل الكود في الوقت الفعلي — فريقك يراقب الوكيل، يُعلّق على السطر 40، ويوجّهه — والتعليق يبقى مربوطاً حتى مع إعادة الكتابة.</p>
      <p>في 12 أغسطس 2026، أعلنت <strong>Zed</strong> — صانعة أسرع محررات الكود (مبني بـ Rust) — عن <strong>Delta</strong>: بيئة multiplayer للبرمجة مع الوكلاء ومراجعة ما يبنونه. Delta ليس ميزة في Zed — بل تطبيق جديد بالكامل، لأن تجربة التعاون مع الوكلاء تتطلب paradigm مختلفاً: <strong>المحادثة في المركز لا المحرر</strong>.</p>
      <p>القلب هو <strong>DeltaDB</strong> — نظام CRDT يُزامن المحادثة وشجرة العمل معاً في الوقت الفعلي. كل تعديل مربوط بالمحادثة التي أنتجته. زملاؤك يدخلون المحادثة، يراقبون Claude Code يعمل، يُعلّقون على الكود أو المحادثة، ويوجّهون الوكيل — حتى في اليوم التالي مع سياق كامل. Delta يعمل على سطح المكتب والويب (WebAssembly + WebGL)، ويتصل بـ Claude Code من الطرفية.</p>
      <p>264 نقطة على Hacker News — أعلى إطلاق non-model في ذلك اليوم. Delta في معاينة خاصة مع دعوات تدريجية. للمبدعين العرب: agencies تقدّم «AI pair programming workshops»، consulting لـ team workflows، وcontent عن أفضل الممارسات — سوق تطوير AI جماعي يولد الآن.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Zed Delta وثورة collaborative AI coding؟</h3>
        <ul>
          <li><strong>AI code review as a service:</strong> فرق تُراجع كود الوكلاء للشركات — 3000–20000 دولار/شهر.</li>
          <li><strong>استشارات سير عمل Delta:</strong> إعداد محادثات الفريق وprocesses — 5000–35000 دولار/مشروع.</li>
          <li><strong>دورات «Team AI Development»:</strong> تدريب فرق الهندسة العربية — 199–1299 دولار.</li>
          <li><strong>محتوى ودروس:</strong> قنوات YouTube/Twitter عن سير عمل Delta — تحقيق دخل عبر الإعلانات والرعايات.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Zed</span>
        <span class="tag">Delta</span>
        <span class="tag">DeltaDB</span>
        <span class="tag">Multiplayer IDE</span>
        <span class="tag">AI Code Review</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 13-08-2026 -- 04-PM</p>
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
