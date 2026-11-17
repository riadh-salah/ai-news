#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 17-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "17-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "GitHub Copilot Workspace 2 Arabic · Runway Gen-4 Arabic · "
    "Notion AI 3 Arabic · Hugging Face Inference Pro Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — GitHub Copilot Workspace 2 Arabic، Runway Gen-4 Arabic، Notion AI 3 Arabic، Hugging Face Inference Pro Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 17 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من GitHub Copilot Workspace 2 Arabic الذي يُحوّل تذكرة عربية في Jira إلى فرع كود كامل مع اختبارات وطلب سحب خلال ساعات، إلى Runway Gen-4 Arabic الذي يُنتج مشاهد سينمائية من قصة بالفصحى مع نصوص عربية دقيقة، ومن Notion AI 3 Arabic الذي يُبني قاعدة معرفة مؤسسية ووكلاء مهام يتحدثون العربية، إلى Hugging Face Inference Pro Arabic الذي يُشغّل نماذج مفتوحة المصدر بلهجات عربية لفرقك داخل منطقتك — أربع قصص ليلية في 17 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ قبل شروق الشمس!</h1>
      <p class="hero-sub">ليلةٌ لمطوري البرمجيات وصناع الفيديو ومديري المعرفة ومهندسي الذكاء الاصطناعي: الكود صار محادثة، الفيديو صار سيناريو، الوثائق صارت وكلاء، والنماذج المفتوحة صارت خدمة جاهزة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من اللحظة الأولى.</p>
      <div class="hero-meta">
        <span>📅 17 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>GitHub Copilot Workspace 2 Arabic: من التذكرة إلى الكود — فرع، اختبارات، وسحب!</h2>
      <p class="article-lead">«المطورون يقرؤون التذاكر بالإنجليزية والعميل يكتب بالعربية — أريد أن تبدأ المهمة من وصف عربي وتنتهي بطلب سحب جاهز». في 17 نوفمبر 2026، أطلقت <strong>GitHub</strong> <strong>Copilot Workspace 2 Arabic</strong>: بيئة تخطيط وتنفيذ تفهم المتطلبات بالفصحى، تُنشئ فرعًا جديدًا، تُقسّم العمل إلى مهام، تكتب الاختبارات، تراجع الأمان، وتُعدّ ملخص سحب بالعربية للمراجعين — لشركات البرمجيات والبنوك والتطبيقات الحكومية في المنطقة العربية.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان يُهمل تعليقات عربية في التذاكر أو يُنتج تعليقات commit بالإنجليزية فقط؛ Workspace 2 يُوحّد لغة التواصل مع الفريق، يتكامل مع Azure DevOps وGitLab، يحترم سياسات الكود الداخلية، يُبرز ثغرات OWASP شائعة قبل السحب، يدعم قوالب «إصلاح ثغرة» و«ميزة API» و«ترقية تبعية»، وبرنامج شريك «GitHub Copilot MENA Enterprise».</p>
      <p>القدرات الأساسية: Arabic issue-to-PR؛ تخطيط مهام مرئي؛ اختبارات وحدة تلقائية؛ مراجعة أمان؛ تعليقات سحب ثنائية اللغة.</p>
      <p>للمبدعين العرب: باقة «تسليم ميزات أسرع» للشركات الناشئة — من يُسلّم 4 دورات تطوير شهرية بـ2200–14500 دولار للدورة يبيع سرعة دون تضخيم فريق هندسي دائم.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من GitHub Copilot Workspace 2 Arabic؟</h3>
        <ul>
          <li><strong>إعداد Workspace وسياسات سحب للفرق:</strong> 4–12 يومًا — 1500–9200 دولار.</li>
          <li><strong>دورات تطوير مُسارَعة بالذكاء الاصطناعي (ميزة كاملة):</strong> — 2200–14500 دولار/دورة.</li>
          <li><strong>صيانة قوالب تذاكر ومراجعات شهرية:</strong> — 480–2100 دولار/عميل/شهر.</li>
          <li><strong>ورش «من المتطلب العربي إلى الإنتاج»:</strong> — 70–280 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">GitHub</span>
        <span class="tag">Copilot</span>
        <span class="tag">Dev</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Runway Gen-4 Arabic: قصة عربية تتحول لمشاهد — حركة، إضاءة، ونص!</h2>
      <p class="article-lead">«نريد إعلانًا يبدو كفيلم قصير — النص عربي والعلامة خليجية والميزانية لا تسمح بأسبوع تصوير». في 17 نوفمبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Arabic</strong>: مولّد فيديو يقرأ سيناريوًا بالفصحى، يُثبت الشخصيات والمنتجات عبر اللقطات، يُحسّن الإضاءة والحركة البشرية، يُدمج عناوين عربية بخطوط RTL، ويُصدّر بجودة حملات تلفزيونية رقمية — للعلامات والوكالات وقنوات المحتوى في العالم العربي.</p>
      <p>المشكلة التي حلّتها: Gen-3 كان يُشوّه الحروف المتحركة أو يقطع الجمل الطويلة؛ Gen-4 يدعم storyboard بالعربية، تحكمًا في الكاميرا بلغة طبيعية، مكتبة موسيقى مرخصة، تكاملًا مع Adobe Premiere، امتثالًا لحقوق الوجوه في الأسواق الخليجية، وبرنامج «Runway Creative MENA».</p>
      <p>القدرات الأساسية: Arabic script-to-video؛ اتساق الشخصيات؛ تحكم كاميرا؛ موسيقى مرخصة؛ تصدير متعدد الأبعاد.</p>
      <p>للمبدعين العرب: استوديو «حلقة إعلان في 72 ساعة» — من ينفّذ 8 مشاريع شهريًا بـ1400–7500 دولار للمشروع يحوّل الإنتاج إلى خط سريع للعلامات التي تتنافس على انتباه المشاهد العربي.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Arabic؟</h3>
        <ul>
          <li><strong>إنتاج إعلانات وقصص مصورة بالذكاء الاصطناعي:</strong> 3–7 أيام — 1400–7500 دولار/مشروع.</li>
          <li><strong>اشتراك إنتاج شهري (6–15 فيديو):</strong> — 320–1350 دولار/عميل/شهر.</li>
          <li><strong>حزم سيناريوهات عربية جاهزة (قطاع محدد):</strong> — 60–265 دولار/حزمة.</li>
          <li><strong>تدريب فرق إبداع على Gen-4:</strong> — 68–270 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video</span>
        <span class="tag">Creative</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Notion AI 3 Arabic: قاعدة معرفة ووكلاء مهام — محاضر، سياسات، ومتابعة!</h2>
      <p class="article-lead">«كل قسم يكتب سياساته بطريقة مختلفة — أريد عقلًا مؤسسيًا واحدًا يُجيب الموظفين بالعربية ويُحدّث الوثائق تلقائيًا». في 17 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>AI 3 Arabic</strong>: منصة تعرف تُفهرس مساحات العمل بالعربية، تُولّد محاضر اجتماعات، تُبني قواعد معرفة للموارد البشرية والقانون والتشغيل، تُنشئ وكلاء مهام يُرسلون تذكيرات ومتابعات، وتُربط Slack وGmail وZoom — للشركات المتوسطة والجامعات والمنظمات في المنطقة.</p>
      <p>المشكلة التي حلّتها: Notion AI 2 كان يُخطئ في المصطلحات القانونية العربية أو يُكرر فقرات؛ الإصدار 3 يدعم موافقات النشر، قواميس مصطلحات مخصصة، بحثًا دلاليًا عبر آلاف الصفحات، قوالب «سياسة داخلية» و«دليل موظف» و«خطة مشروع»، تكاملًا مع أنظمة HR المحلية، وبرنامج «Notion Partners MENA».</p>
      <p>القدرات الأساسية: Arabic knowledge base؛ وكلاء مهام؛ محاضر تلقائية؛ قوالب مؤسسية؛ تحليلات استخدام.</p>
      <p>للمبدعين العرب: خدمة «مكتب معرفة رقمي» — من يُدير 10 منظمات بـ550–2600 دولار/شهر لكل منظمة يبيع انضباطًا معلوماتيًا يوفر ساعات بحث أسبوعية على كل موظف.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء قاعدة معرفة ووكلاء مهام كاملة:</strong> 6–14 يومًا — 1200–6800 دولار.</li>
          <li><strong>إدارة وتحديث معرفة شهرية:</strong> — 550–2600 دولار/عميل/شهر.</li>
          <li><strong>قوالب سياسات ودلائل عربية (قطاع محدد):</strong> — 45–195 دولار/حزمة.</li>
          <li><strong>دورات «إدارة المعرفة بالذكاء الاصطناعي»:</strong> — 52–208 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Agents</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Hugging Face Inference Pro Arabic: نماذج مفتوحة بلايطة عربية — API، خصوصية، وتوسع!</h2>
      <p class="article-lead">«نريد نموذجًا يفهم اللهجات دون إرسال بيانات عملائنا إلى سحابة أجنبية — والفريق لا يملك أشهر بناء بنية تحتية». في 17 نوفمبر 2026، أطلقت <strong>Hugging Face</strong> <strong>Inference Pro Arabic</strong>: منصة استضافة تُشغّل نماذج Llama وMistral ونماذج عربية مخصصة على حواف الجغرافيا الإقليمية، تُقدّم واجهات API بلهجات عربية، تُراقب الأداء والتكلفة، تدعم ضبطًا دقيقًا ببيانات محلية، وتُصدّر تقارير امتثال للجهات المنظمة — للبنوك والتطبيقات والاتصالات والقطاع الصحي.</p>
      <p>المشكلة التي حلّتها: الاستضافة العامة كانت بطيئة على العربية أو مكلفة عند الذروة؛ Inference Pro يُوازن بين النماذج المفتوحة والمغلقة، يدعم GPU مشتركة ومخصصة، يتكامل مع Kubernetes المحلي، يُوفّر قوالب «دردشة دعم» و«تلخيص مستند» و«تصنيف بلاغ»، وبرنامج «HF Enterprise MENA».</p>
      <p>القدرات الأساسية: Arabic model hosting؛ API بلهجات؛ مراقبة تكلفة؛ ضبط دقيق آمن؛ تقارير امتثال.</p>
      <p>للمبدعين العرب: خدمة «نشر نموذج في أسبوع» — من يُسلّم 3 مشاريع استضافة شهريًا بـ3500–22000 دولار للمشروع + 650–3200 دولار/شهر للتشغيل يبيع قدرة ذكاء اصطناعي محلية لجهات لا تثق بالسحابة العامة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hugging Face Inference Pro Arabic؟</h3>
        <ul>
          <li><strong>نشر وضبط نموذج عربي مؤسسي:</strong> 10–25 يومًا — 3500–22000 دولار/مشروع.</li>
          <li><strong>تشغيل ومراقبة وتحسين شهري:</strong> — 650–3200 دولار/عميل/شهر.</li>
          <li><strong>تقييم أداء نماذج عربية (benchmark):</strong> — 420–1850 دولار/تقرير.</li>
          <li><strong>معسكر «من النموذج المفتوح إلى الإنتاج»:</strong> — 135–540 دولار/مشارك.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hugging Face</span>
        <span class="tag">Open Source</span>
        <span class="tag">API</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 17-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="17-11-2026 -- 12-AM.html">
          📰 17 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "17-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/17-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/17-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
        f"(4 أخبار + أفكار ربح من AI)"
    )
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "أحدث إصدار" in line and "news/" in line:
            if new in line:
                print(f"README already points to latest: {README}")
                return
            lines[i] = new_line
            break
    else:
        raise SystemExit("ERROR: could not find README latest edition line")
    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Updated: {README}")


def validate_output():
    data = OUTPUT.read_bytes()
    if b"\x00" in data:
        raise SystemExit("ERROR: null bytes found in output")
    if data[:3] == b"\xef\xbb\xbf":
        raise SystemExit("ERROR: BOM found in output")
    text = OUTPUT.read_text(encoding="utf-8")
    if "article-4" not in text:
        raise SystemExit("ERROR: missing article-4")
    if text.count('class="article"') != 4:
        raise SystemExit(f"ERROR: expected 4 articles, found {text.count('class=\"article\"')}")
    if not text.startswith("<!DOCTYPE html>"):
        raise SystemExit("ERROR: invalid HTML start")
    if not text.rstrip().endswith("</html>"):
        raise SystemExit("ERROR: invalid HTML end")
    bad_patterns = [
        "dollar",
        "mlions",
        "millones",
        "bringing",
        "الLlatin",
        "أfكar",
        "دolار",
        "البروtokol",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "المشkلة",
        "mezclar",
        "prefe r",
        "الإصrador",
        "يبni",
        "عArabية",
        "أكtober",
        "ت TECH",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    if re.search(r"[yY][\u064B-\u0652\u0670]", text):
        raise SystemExit("ERROR: Latin y with Arabic diacritic found")
    if "\u00fc" in text or "yü" in text:
        raise SystemExit("ERROR: Latin ü found — use Arabic يُ")
    print("Validation passed: UTF-8, no null bytes, 4 articles, valid HTML structure")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    validate_output()
    update_index()
    update_readme()


if __name__ == "__main__":
    main()