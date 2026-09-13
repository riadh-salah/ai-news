#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 13-09-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "13-09-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Google AI Edge Gallery على Mac بنماذج Gemma-4 محلياً، NVIDIA Halos for Robotics لأمان الروبوتات البشرية، EasySpecs.ai لمراجعة المواصفات قبل توليد الكود، Chalk MCP Server وChalk Assistant للتعلم الآلي الوكيلي، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 13 سبتمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Google AI Edge Gallery الذي يُشغّل Gemma-4-12B متعدد الوسائط على Mac بـ16GB RAM دون سحابة، إلى NVIDIA Halos for Robotics — أول نظام أمان full-stack للروبوتات البشرية في المصانع، ومن EasySpecs.ai الذي ينقل بوابة الجودة من مراجعة الكود إلى مراجعة المواصفات قبل أي سطر، إلى Chalk MCP Server وChalk Assistant اللذان يُدخلان الوكلاء في حلقة تطوير ML الإنتاجية — أربع ثورات تُعيد تشكيل AI المحلي وأمان الروبوتات وهندسة البرمجيات الوكيلية والتعلم الآلي في 13 سبتمبر 2026!</h1>
      <p class="hero-sub">Google تُطلق Edge Gallery وEloquent للخصوصية الكاملة على Mac، NVIDIA تُوحّد أمان الروبوتات مع Agility وToyota، EasySpecs.ai يُغيّر قواعد AI coding عبر spec review، وChalk يُحوّل الوكلاء من «مساعدين جانبيين» إلى مشاركين في feature engineering. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 13 سبتمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Google AI Edge Gallery على Mac: Gemma-4-12B محلياً — نص وصورة وصوت بـ16GB RAM دون إنترنت!</h2>
      <p class="article-lead">«الخصوصية = لا سحابة = لا نماذج قوية». في 13 سبتمبر 2026، أطلقت <strong>Google</strong> تطبيقها التجريبي <strong>AI Edge Gallery</strong> على <strong>macOS</strong> — منصة متخصصة لتشغيل نماذج generative AI محلياً بالكامل: محادثة، معالجة صور، وتحليل دلالي — دون الاعتماد على خوادم سحابية.</p>
      <p>المشكلة التي حلّتها: أدوات مثل Ollama وLM Studio عامة — Google اتخذت نهجاً متخصصاً. Edge Gallery يدعم خمسة نماذج instruction-tuned من ecosystem Google المفتوح: <strong>Gemma-4-12B-it</strong> و<strong>Gemma-4-E2B-it</strong> و<strong>Gemma-4-E4B-it</strong> و<strong>Gemma-3n-E2B-it</strong> و<strong>Gemma-3n-E4B-it</strong> — كلها مُحسّنة بـ<strong>edge-side parameter offloading</strong>.</p>
      <p>القدرات الأساسية: <strong>Gemma-4-12B</strong> — 12 مليار parameter، يتعامل مع نص وصورة وصوت على Macs بـ<strong>16GB RAM</strong>؛ قدرات coding وlogic analysis محلية تُحوّل laptop خفيفاً إلى وكيل ذكي offline؛ <strong>Google AI Edge Eloquent</strong> — أداة صوت مجانية للـMac: transcription offline، إزالة filler words، وrefinement محلي؛ <strong>custom vocabulary</strong> — أسماء ومصطلحات صناعية مخصصة؛ كل المعالجة على شريحة Mac — بيانات لا تغادر الجهاز.</p>
      <p>للمبدعين العرب: كل legal firm وhealthcare provider وgovernment agency في MENA يحتاج AI محلي compliant — Edge Gallery deployment packages وArabic offline AI playbooks وmanaged on-device AI retainers فرصة privacy premium. «Offline multimodal on consumer hardware» = category جديد — consultants الذين يُصمّمون local-first workflows مبكراً يفوزون بعقود regulated industries.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google AI Edge Gallery وثورة AI المحلي على Mac؟</h3>
        <ul>
          <li><strong>Edge Gallery deployment packages:</strong> Gemma model setup + custom vocabulary + Arabic workflows — 4000–32000 دولار/مشروع.</li>
          <li><strong>Offline AI privacy consulting:</strong> compliance mapping + on-device architecture + Eloquent integration — 3500–28000 دولار/عميل.</li>
          <li><strong>Managed local AI retainers:</strong> model updates + vocabulary tuning + support — 2500–18000 دولار/شهر.</li>
          <li><strong>دورات «Build Offline AI with Google Edge Gallery»:</strong> bootcamp — 39–199 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">AI Edge Gallery</span>
        <span class="tag">Gemma-4</span>
        <span class="tag">Offline AI</span>
        <span class="tag">macOS</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>NVIDIA Halos for Robotics: أول نظام أمان full-stack للروبوتات البشرية — Agility وToyota يتبنّان المعيار!</h2>
      <p class="article-lead">«الروبوت البشري يعمل بجانبك — لكن من يضمن أنه لن يسقط صندوقاً على رأس زميلك؟». في 12 سبتمبر 2026، أعلنت <strong>NVIDIA</strong> عن <strong>Halos for Robotics</strong>: أول نظام أمان شامل full-stack مُصمّم خصيصاً للروبوتات و<strong>physical AI</strong> — يُبقي الآلات المستقلة آمنة في المصانع والمستودعات ومرافق اللوجستيات حيث يعمل البشر جنباً إلى جنب.</p>
      <p>المشكلة التي حلّتها: أمان physical AI كان ad hoc — كل تطبيق يبني logic خاصاً. Halos يُوحّد: <strong>NVIDIA IGX Thor compute</strong> + <strong>Holoscan Sensor Bridge</strong> + <strong>Halos OS</strong> + <strong>Halos AI Systems Inspection Lab</strong> — compute وsensors وsystem software وvalidation وinspection في stack واحد.</p>
      <p>القدرات الأساسية: يستند إلى أكثر من <strong>18600 سنة هندسية</strong> من خبرة NVIDIA في autonomous driving؛ <strong>Agility Robotics</strong> — أول شركة humanoid تستخدم Halos لبناء safety في Digit؛ <strong>Toyota Motor Manufacturing Canada</strong> كشريك deployment؛ <strong>Halos Blueprint</strong> — جزء من Halos Applications layer، متاح في early access؛ open robotics safety system — machines التي sense وdecide وact في العالم الحقيقي تحصل على architecture أمان مشتركة.</p>
      <p>للمبدعين العرب: كل smart factory وlogistics hub وconstruction site في MENA يستعد لـhumanoid robots — Halos integration packages وArabic robotics safety playbooks وmanaged physical AI retainers فرصة industrial premium. «Standardized robot safety stack» = prerequisite للتبني — integrators الذين يُصمّمون Halos-compliant deployments مبكراً يفوزون بعقود transformation ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من NVIDIA Halos for Robotics وثورة أمان الروبوتات؟</h3>
        <ul>
          <li><strong>Halos robotics safety packages:</strong> IGX Thor setup + sensor bridge + inspection lab — 15000–120000 دولار/مشروع.</li>
          <li><strong>Physical AI safety consulting:</strong> risk assessment + Halos Blueprint + compliance — 8000–65000 دولار/عميل.</li>
          <li><strong>Managed robot safety retainers:</strong> inspection ops + firmware updates + audit support — 6000–45000 دولار/شهر.</li>
          <li><strong>دورات «Robotics Safety with NVIDIA Halos»:</strong> bootcamp — 79–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">NVIDIA</span>
        <span class="tag">Halos for Robotics</span>
        <span class="tag">Humanoid Robots</span>
        <span class="tag">Physical AI</span>
        <span class="tag">Agility Robotics</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>EasySpecs.ai: مراجعة المواصفات قبل الكود — spec-driven development يُنقذ فرق الهندسة من AI code overload!</h2>
      <p class="article-lead">«وكيل AI يُنتج 500 سطر — لا أحد لديه وقت لقراءتها». في 12 سبتمبر 2026، فتحت <strong>EasySpecs.ai</strong> من <strong>Spaii Labs SL</strong> الوصول العام لمنصة <strong>spec review</strong>: تُوثّق codebases موجودة، ثم تُحوّل change requests إلى specs مع <strong>spec verification checks</strong> مدمجة — قبل أن يُولَّد أي سطر كود.</p>
      <p>المشكلة التي حلّتها: AI coding agents أغرقوا code review — الجودة تتدهور لأن البشر لا يستطيعون قراءة كل output. EasySpecs ينقل بوابة الجودة upstream: من code review إلى <strong>spec review</strong>. المنصة تفهم ما يفعله الكود فعلاً، وتُنتج specs يبني عليها coding agents — reviewed intent بدلاً من guesswork.</p>
      <p>القدرات الأساسية: <strong>Free tier</strong> — أي developer يُوصّل repository ويرى ما تجده المنصة؛ <strong>Workbench</strong> — 5 يورو/repository/شهر (launch pricing، عادة 10) مع BYOK من OpenAI وAnthropic وGoogle وOpenRouter؛ <strong>Factory</strong> — 150 يورو/شهر مع managed inference للمؤسسة؛ <strong>Enterprise</strong> — deployment داخل VPC أو private cloud مع migration harness مخصص؛ متاح على easyspecs.ai وProduct Hunt.</p>
      <p>للمبدعين العرب: كل software house وfintech وenterprise في MENA يُسرّع AI coding — EasySpecs integration packages وArabic spec review playbooks وmanaged spec-driven development retainers فرصة devtools premium. «Spec-before-code» = paradigm shift — consultants الذين يُصمّمون spec review workflows مبكراً يفوزون بعقود engineering transformation.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من EasySpecs.ai وثورة spec-driven development؟</h3>
        <ul>
          <li><strong>EasySpecs integration packages:</strong> repo onboarding + spec templates + agent workflows — 3500–30000 دولار/مشروع.</li>
          <li><strong>Spec-driven development consulting:</strong> process design + verification rules + Arabic documentation — 3000–25000 دولار/عميل.</li>
          <li><strong>Managed spec review retainers:</strong> spec maintenance + agent tuning + audit — 2500–20000 دولار/شهر.</li>
          <li><strong>دورات «Spec Review Before AI Code Generation»:</strong> bootcamp — 29–149 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">EasySpecs.ai</span>
        <span class="tag">Spec Review</span>
        <span class="tag">Spec-Driven Development</span>
        <span class="tag">AI Coding</span>
        <span class="tag">Spaii Labs</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Chalk MCP Server وChalk Assistant: التعلم الآلي الوكيلي — الوكلاء يُشاركون في feature engineering لا يُعلّقون من الخارج!</h2>
      <p class="article-lead">«الوكيل يُقترح feature — ثم تنسخه يدوياً إلى Chalk وتختبره». في 11 سبتمبر 2026، أعلنت <strong>Chalk</strong> عن <strong>Chalk MCP Server</strong> و<strong>Chalk Assistant</strong>: foundation للـ<strong>agentic machine learning</strong> — وكلاء لا يُساعدون من الخارج بل يشاركون في حلقة تطوير ML systems الإنتاجية.</p>
      <p>المشكلة التي حلّتها: agents في data/ML teams يجلسون خارج الأنظمة — context يُلصق في prompts، suggestions تُختبر يدوياً. Chalk MCP Server يُعرّض capabilities Chalk مباشرة للوكلاء: read feature/resolver definitions، run online queries، Chalk SQL للـresearch، engineer وbacktest features، inspect query errors — نفس primitives التي يستخدمها ML engineer.</p>
      <p>القدرات الأساسية: <strong>Chalk MCP Server</strong> — agent يُحقّق investigate → validate → ship changes؛ cycles feature/model development من weeks إلى days؛ agents تختبر changes proactively بدلاً من انتظار incidents؛ <strong>Chalk Assistant</strong> — agent داخل المنتج: BYOK، sidebar investigation، review reasoning وqueries وproposed changes دون مغادرة interface؛ يُكمّل Chalk strengths: unified training/serving، point-in-time correct datasets، observability.</p>
      <p>للمبدعين العرب: كل fintech وe-commerce وtelecom في MENA يبني ML production — Chalk MCP integration packages وArabic agentic ML playbooks وmanaged feature engineering retainers فرصة MLOps premium. «Agents in the ML loop» = next frontier — consultants الذين يُصمّمون agentic feature workflows مبكراً يفوزون بعقود data platform طويلة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Chalk MCP Server وثورة التعلم الآلي الوكيلي؟</h3>
        <ul>
          <li><strong>Chalk MCP integration packages:</strong> MCP Server setup + agent workflows + feature templates — 5000–42000 دولار/مشروع.</li>
          <li><strong>Agentic ML consulting:</strong> feature engineering automation + backtest pipelines + Arabic NLP features — 4000–35000 دولار/عميل.</li>
          <li><strong>Managed agentic ML retainers:</strong> model iteration ops + agent monitoring + performance tuning — 3500–28000 دولار/شهر.</li>
          <li><strong>دورات «Agentic Machine Learning with Chalk»:</strong> bootcamp — 49–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Chalk</span>
        <span class="tag">Chalk MCP Server</span>
        <span class="tag">Chalk Assistant</span>
        <span class="tag">Agentic ML</span>
        <span class="tag">Feature Engineering</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 13-09-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="13-09-2026 -- 12-AM.html">
          📰 13 سبتمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Google Edge Gallery · NVIDIA Halos Robotics · EasySpecs.ai · Chalk MCP</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "13-09-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def validate_output():
    data = OUTPUT.read_bytes()
    if b"\x00" in data:
        raise SystemExit("ERROR: null bytes found in output")
    text = OUTPUT.read_text(encoding="utf-8")
    if "article-4" not in text:
        raise SystemExit("ERROR: missing article-4")
    if text.count('class="article"') != 4:
        raise SystemExit(f"ERROR: expected 4 articles, found {text.count('class=\"article\"')}")
    if not text.startswith("<!DOCTYPE html>"):
        raise SystemExit("ERROR: invalid HTML start")
    if not text.rstrip().endswith("</html>"):
        raise SystemExit("ERROR: invalid HTML end")
    bad_patterns = ["dollar", "mlions", "bringing", "الLlatin", "أفكar", "دolار", "البروtokol"]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    print("Validation passed: UTF-8, no null bytes, 4 articles, valid HTML structure")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    validate_output()
    update_index()


if __name__ == "__main__":
    main()
