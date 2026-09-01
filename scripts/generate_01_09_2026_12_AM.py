#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 01-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "01-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Stagehand v4، Morph Apply، oMLX، Superagent، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 1 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من SDK يُبني وكلاء متصفح بـ act وextract وobserve ذاتية الإصلاح، إلى محرّك دمج ملفات متعددة يُبقي builders مستقرين، ومن inference محلي على Mac يُعيد KV cache من SSD في 5 ثوانٍ لا 90، إلى منزل سطح مكتب لوكيل Claude Code مع متصفح حقيقي وiOS Simulator — أربع ثورات تُعيد تعريف أتمتة الويب والبناء والتشغيل المحلي في 1 سبتمبر 2026!</h1>
      <p class="hero-sub">Stagehand v4 يُمزج Playwright-style APIs مع primitives ذكية للوكلاء الذين يحتاجون وصولاً موثوقاً للويب، Morph Apply يُثبت تعديلات multi-file داخل sandbox قبل النشر، oMLX يُخزّن KV cache على SSD ليُسرّع Claude Code وCursor محلياً، وSuperagent يُعطي وكيلك متصفحاً على جلساتك المسجّلة وSimulator وroutines مجدولة — كل ذلك open source ومحلي. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 1 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Stagehand v4: SDK وكلاء المتصفح — act وextract وobserve ذاتية الإصلاح فوق CDP بلا Playwright!</h2>
      <p class="article-lead">«Playwright بُني للاختبار — Stagehand بُني للوكلاء». في 22 أغسطس 2026، أطلقت <strong>Browserbase</strong> <strong>Stagehand v4</strong> — <strong>SDK لوكلاء المتصفح</strong> يُشغّل Chromium عبر Chrome DevTools Protocol مباشرة، بلا dependency على Playwright، مع primitives طبيعية اللغة تُعيد حلّ العناصر على الصفحة الحية.</p>
      <p>المشكلة التي حلّتها: selectors الهشّة تموت مع كل redesign — وagents تحتاج مزيجاً من خطوات حتمية وخطوات ذكية تتكيّف. Stagehand يُقدّم طبقتين: <strong>act</strong> لتنفيذ أوامر بلغة طبيعية، <strong>extract</strong> لاستخراج بيانات typed بschema، <strong>observe</strong> لفهم حالة الصفحة — إلى جانب APIs مألوفة: goto وclick وlocator وscreenshot. تُمزج في سكربت واحد: selector حيث يكفي، AI حيث يتعثّر الكود.</p>
      <p>القدرات الأساسية: runtime داخل المتصفح لسرعة remote comparable بـ local، SDKs رسمية لـ TypeScript وPython وGo، metrics مدمجة للtokens والtiming، تكامل مع LangChain وCrewAI وMastra، server-side caching يُزيل inference بعد استقرار flow، وModel Gateway على Browserbase. Migration guide من Playwright متاح — port as-is ثم swap selectors الأكثر كسراً بـ act().</p>
      <p>للمبدعين العرب: كل fintech وe-commerce وrecruitment platform في MENA يحتاج scraping وautomation موثوق — Stagehand agent packages وArabic browser workflow SOPs وmanaged web-agent retainers فرصة infrastructure premium. «Browser agent SDK» vertical ينمو — Stagehand تُكافئ teams التي تُريد control دقيقاً لا agent chaos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stagehand v4 وثورة أتمتة المتصفح للوكلاء؟</h3>
        <ul>
          <li><strong>Stagehand automation packages:</strong> بناء flows وeb scraping للعملاء — 2500–20000 دولار/مشروع.</li>
          <li><strong>Browser agent consulting:</strong> migration من Playwright وarchitecture — 3000–18000 دولار/audit.</li>
          <li><strong>Managed web-agent retainers:</strong> تشغيل وصيانة agents على Browserbase — 3500–28000 دولار/شهر.</li>
          <li><strong>دورات «Build Browser Agents with Stagehand»:</strong> bootcamp للمطورين — 59–449 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stagehand v4</span>
        <span class="tag">Browser Agents</span>
        <span class="tag">Browserbase</span>
        <span class="tag">Web Automation</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Morph Apply: دمج ملفات متعددة بثبات — AI app builders لا تكسر imports وtypes بعد كل prompt!</h2>
      <p class="article-lead">«App builders تموت على patching flaky — Morph Apply يُثبت multi-file edits». <strong>Morph Apply</strong> من <strong>Morph LLM</strong> — <strong>apply engine</strong> يُدمج تعديلات LLM عبر UI وAPI وdata layers في pass واحد، داخل sandbox، مع preview diff قبل الكتابة.</p>
      <p>المشكلة التي حلّتها: agents تُولّد snippets لكن merge يكسر imports وtypes وcross-file references — المستخدم يرى demo ثم chaos. Morph Apply يأخذ instruction + code + update snippet ويُرجع merged files reviewable: run inside E2B أو Fly.io machines أو containers، show diff في UI، execute tests/typechecks تلقائياً، publish merged output فقط بعد نجاح guardrails.</p>
      <p>القدرات الأساسية: multi-file reliability عبر طبقات التطبيق، sandbox-first flow قبل production، reviewable output مع diffs واضحة، تكامل مع AI application builders وcoding agents، payload صريح: instruction يوجّه، code يُحدّد السياق، update يُطبّق. Use cases: vibe coding platforms، internal app builders، agent harnesses تحتاج deterministic edits.</p>
      <p>للمبدعين العرب: كل no-code startup وdev agency في MENA تبني AI builder — Morph Apply integration packages وArabic builder SOPs وmanaged apply-layer retainers فرصة infrastructure-as-a-service. «Reliable apply layer» niche ينمو — Morph تُكافئ builders التي تُريد stability لا speed فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Morph Apply وثورة الدمج الموثوق للـ AI builders؟</h3>
        <ul>
          <li><strong>Morph Apply integration packages:</strong> ربط apply engine بـ builder — 4000–30000 دولار/منصة.</li>
          <li><strong>AI builder architecture consulting:</strong> sandbox loops وguardrails — 2500–20000 دولار/مشروع.</li>
          <li><strong>Managed builder retainers:</strong> صيانة apply pipeline شهرياً — 3000–25000 دولار/شهر.</li>
          <li><strong>دورات «Stable Multi-File Edits with Morph»:</strong> bootcamp لفرق المنتج — 49–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Morph Apply</span>
        <span class="tag">AI App Builder</span>
        <span class="tag">Multi-File Edits</span>
        <span class="tag">Sandbox</span>
        <span class="tag">Developer Tools</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>oMLX: inference محلي على Mac — KV cache على SSD يُعيد TTFT من 90 ثانية إلى 5 ثوانٍ!</h2>
      <p class="article-lead">«Coding agents تُبطل KV cache عشرات المرات في الجلسة — oMLX يُ persist كل block على SSD». <strong>oMLX</strong> — <strong>macOS-native MLX server</strong> مع continuous batching وtiered caching: hot blocks في RAM، cold blocks على SSD بـ LRU policy — Claude Code وOpenClaw وCursor يستجيبون في 5 ثوانٍ لا 90 على contexts طويلة.</p>
      <p>المشكلة التي حلّتها: Ollama وLM Studio يcache في memory — عند shift في context mid-session، كل cache يُبطل ويُعاد compute. oMLX يكتب blocks بصيغة safetensors على disk؛ prefixes سابقة تُستعاد عبر requests وrestarts — never recomputed. Two-tier architecture يُ balance بين سرعة وfootprint على Apple Silicon.</p>
      <p>القدرات الأساسية: OpenAI-compatible (/v1/chat/completions) وAnthropic-compatible (/v1/messages) endpoints، web dashboard مع one-click config generator لكل أداة، menu bar app لإدارة models، دعم text LLMs وVLM وOCR وembeddings وrerankers، models: Qwen وDeepSeek وMiniMax وGLM وغيرها، vision models من v0.2.0. Minimum 16GB RAM، sweet spot M-series Pro/Max.</p>
      <p>للمبدعين العرب: كل developer وprivacy-conscious team في MENA على Mac — oMLX setup packages وArabic local-AI workshops وmanaged on-device retainers فرصة sovereignty premium. «Mac-native local inference» vertical ينمو — oMLX تُكافئ teams التي تُريد speed محلي بدون cloud bills.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من oMLX وثورة inference المحلي على Apple Silicon؟</h3>
        <ul>
          <li><strong>oMLX deployment packages:</strong> إعداد server وmodels للفرق — 1500–12000 دولار/فريق.</li>
          <li><strong>Local AI consulting:</strong> model selection وcache tuning — 2000–15000 دولار/audit.</li>
          <li><strong>Managed local-inference retainers:</strong> صيانة وتحديث models شهرياً — 1800–14000 دولار/شهر.</li>
          <li><strong>دورات «Run Coding Agents Locally with oMLX»:</strong> bootcamp للمطورين — 39–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">oMLX</span>
        <span class="tag">Local LLM</span>
        <span class="tag">Apple Silicon</span>
        <span class="tag">KV Cache</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Superagent: منزل سطح مكتب لوكيل Claude Code — متصفح حقيقي وiOS Simulator وroutines بلا terminal!</h2>
      <p class="article-lead">«العمل مع coding agent يجب أن يشبه Mac app جيداً — لا terminal». في أغسطس 2026، أطلق <strong>Superagent</strong> على Product Hunt — <strong>desktop home for coding agents</strong> open source: chat persistent لكل مشروع، متصفح حقيقي على جلساتك المسجّلة، iOS Simulator في النافذة، وroutines مجدولة.</p>
      <p>المشكلة التي حلّتها: Claude Code قوي في terminal — لكن non-technical founders وcreators يريدون GUI، browser agent يستخدم logins حقيقية، وvisibility على ما يفعله الوكيل. Superagent يُعطي الوكيل «computer»: browser يقوده على sites أنت logged in، files يحرّرها، board يُتابعه، worktree منفصل لكل chat — nothing collides. iPhone app companion يُتابع المحادثة encrypted end-to-end.</p>
      <p>القدرات الأساسية: sidebar chats قابلة للgrouping تsurvive restarts، git worktree per chat، browser على sessions حقيقية لا headless generic، iOS Simulator streaming، routines on schedule، local على Mac بـ Claude subscription الموجود — no middleman server وno API key وno second bill. Codex وAntigravity قادمان. Stack: Electron + TypeScript + React، companion iOS SwiftUI.</p>
      <p>للمبدعين العرب: كل solo founder وagency في MENA على Mac — Superagent onboarding packages وArabic agent routine templates وmanaged desktop-agent retainers فرصة productivity premium. «Claude Code for the rest of us» positioning ينمو — Superagent تُكافئ users التي تُريد experience لا power-user terminal.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Superagent وثورة desktop agent experience؟</h3>
        <ul>
          <li><strong>Superagent setup packages:</strong> إعداد workflows وroutines للفرق — 800–8000 دولار/فريق.</li>
          <li><strong>Agent routine design:</strong> morning briefings وmonitoring templates — 500–5000 دولار/routine.</li>
          <li><strong>Managed desktop-agent retainers:</strong> تشغيل وتحسين agent workflows — 1200–10000 دولار/شهر.</li>
          <li><strong>دورات «Ship with Superagent on Mac»:</strong> bootcamp للمؤسسين — 29–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Superagent</span>
        <span class="tag">Claude Code</span>
        <span class="tag">Desktop Agent</span>
        <span class="tag">macOS</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 01-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="01-09-2026 -- 12-AM.html">
          📰 1 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Stagehand v4 · Morph Apply · oMLX · Superagent</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "01-09-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    update_index()


if __name__ == "__main__":
    main()
