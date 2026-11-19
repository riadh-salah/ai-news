#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 19-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "19-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Notion AI Agents 3 Arabic · Intercom Fin 3 Arabic · "
    "Stripe Revenue Intelligence 2 Arabic · ElevenLabs Dubbing Studio 3 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Notion AI Agents 3 Arabic، Intercom Fin 3 Arabic، Stripe Revenue Intelligence 2 Arabic، ElevenLabs Dubbing Studio 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 19 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Notion AI Agents 3 Arabic الذي يُنفّذ مهامك الليلية داخل قاعدة معرفتك ويُحدّث الجداول بالعربية قبل أن تستيقظ، إلى Intercom Fin 3 Arabic الذي يُجيب عملاءك على واتساب بلهجة الخليج ويُحوّل السؤال إلى اشتراك، ومن Stripe Revenue Intelligence 2 Arabic الذي يُترجم حركة المدفوعات إلى توقعات إيراد ورسائل استرداد بالفصحى، إلى ElevenLabs Dubbing Studio 3 Arabic الذي يُضاعف فيديوهاتك بصوت عربي طبيعي لعشر لغات في ساعة واحدة — أربع قصص ليلية في 19 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يبدأ قبل أول فنجان قهوة!</h1>
      <p class="hero-sub">ليلةٌ لأصحاب المنتجات والوكالات وفرق النمو: الوكيل ينفّذ داخل Notion، الدعم يبيع بالعربية، المدفوعات تُتكلّم مع المبيعات، والصوت يفتح أسواقًا جديدة دون استوديو. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يأسرك من أول سطر.</p>
      <div class="hero-meta">
        <span>📅 19 نوفمبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Notion AI Agents 3 Arabic: وكلاء داخل مساحة عملك — مهام، تقارير، ومتابعة بالعربية</h2>
      <p class="article-lead">«نريد مساعدًا يقرأ قاعدة المعرفة ويُحدّث قاعدة العملاء ويُرسل ملخصًا أسبوعيًا دون أن ننسخ البيانات يدويًا». في 19 نوفمبر 2026، أطلقت <strong>Notion</strong> <strong>AI Agents 3 Arabic</strong>: وكلاء داخل Notion يفهمون الصفحات والجداول وقواعد البيانات بالعربية، يُنفّذون مهامًا متعددة الخطوات مثل «اجمع ملاحظات الاجتماع ثم أنشئ مهامًا ووزّعها»، يُولّدون تقاريرًا أسبوعية بالفصحى، يتزامنون مع Slack وGmail وGoogle Drive، يحترمون صلاحيات كل عضو، ويسجّلون كل إجراء للمراجعة — لشركات الناشئة والوكالات والمؤسسات في العالم العربي التي تعتمد Notion كمركز عمليات.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُجيب أسئلة لكنه لا يُنفّذ سلسلة إجراءات؛ Agents 3 يدعم قوالب «إطلاق منتج» و«تتبع عملاء» و«محتوى أسبوعي»، جدولة مهام ليلية، ربطًا مع Zapier وMake، تعليمات نبرة باللهجة المختارة، تكامل مع التقويم، وبرنامج شركاء «Notion Agent Partners MENA».</p>
      <p>القدرات الأساسية: وكلاء عربية متعددة الخطوات؛ تحديث جداول تلقائي؛ تقارير مجدولة؛ صلاحيات وأمان؛ تكامل أدوات العمل.</p>
      <p>للمبدعين العرب: خدمة «غرفة عمليات ذكية» — من يُصمّم 6 مساحات عمل ربعيًا بـ2800–15000 دولار للمشروع + 420–1800 دولار/شهر للصيانة يبيع للفرق التي تعيش داخل Notion وتريد أتمتة دون كود معقد.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>بناء مساحة ووكلاء Notion مؤسسيين:</strong> 8–18 يومًا — 2800–15000 دولار.</li>
          <li><strong>صيانة وكلاء وتقارير شهريًا:</strong> — 420–1800 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب قطاع (وكالة، تعليم، تقنية):</strong> — 55–240 دولار/حزمة.</li>
          <li><strong>ورش «وكلاء Notion بالعربية دون برمجة»:</strong> — 48–195 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Productivity</span>
        <span class="tag">Workflow</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Intercom Fin 3 Arabic: دعم يبيع — محادثات عربية، تأهيل، وتفعيل اشتراك</h2>
      <p class="article-lead">«فريق الدعم ينام والعميل يكتب على الموقع الساعة الثانية صباحًا بالعربية». في 19 نوفمبر 2026، أطلقت <strong>Intercom</strong> <strong>Fin 3 Arabic</strong>: مساعد دعم ومبيعات يُجيب الفصحى ولهجات الخليج والمغرب، يبحث في مركز المساعدة وقاعدة المعرفة، يُقترح خططًا وأسعارًا، يُفعّل تجربة مجانية، يُحوّل المحادثة إلى بشري عند الحاجة، يتكامل مع Stripe وShopify، يُلخّص المحادثة في CRM، ويُرسل تقارير رضا بالعربية — لشركات البرمجيات كخدمة والتجارة والتعليم الرقمي في المنطقة.</p>
      <p>المشكلة التي حلّتها: Fin 2 كان يُجيب لكنه يتعثر في الأسعار المعقدة أو اللهجات؛ الإصدار 3 يدعم أسئلة تأهيل مسبقة، قواعد «لا تُخفض السعر دون موافقة»، ردود واتساب وMessenger، فهمًا لرمضان وساعات العمل المحلية، اختبارات A/B للنصوص العربية، قوالب «اشتراك شهري» و«دورة مدفوعة» و«متجر إلكتروني»، وبرنامج «Intercom Partner Gulf».</p>
      <p>القدرات الأساسية: دعم ومبيعات عربي؛ تأهيل ذكي؛ تفعيل تجارب؛ تكامل مدفوعات؛ تحويل لبشري عند الحاجة.</p>
      <p>للمبدعين العرب: باقة «دعم يُغلق اشتراكات» — من يُفعّل 8 عملاء بـ580–2600 دولار/شهر لكل عميل يخدم شركات تخسر مبيعات ليلية بسبب بطء الرد بالعربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Intercom Fin 3 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل Fin وقاعدة معرفة عربية:</strong> 10–22 يومًا — 3800–19500 دولار.</li>
          <li><strong>إدارة نصوص واختبارات وشرائح شهريًا:</strong> — 580–2600 دولار/عميل/شهر.</li>
          <li><strong>قوالب قطاع (SaaS، تجارة، تدريب):</strong> — 62–265 دولار/حزمة.</li>
          <li><strong>ورش «دعم عربي يبيع دون إرهاق الفريق»:</strong> — 52–210 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Intercom</span>
        <span class="tag">Fin</span>
        <span class="tag">Customer Support</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Stripe Revenue Intelligence 2 Arabic: مدفوعات تتكلّم — تنبؤات ورسائل استرداد بالعربية</h2>
      <p class="article-lead">«نعرف أن الإيراد ينخفض لكننا لا نعرف من سيلغي الاشتراك الأسبوع القادم ولا بأي جملة نستعيده». في 19 نوفمبر 2026، أطلقت <strong>Stripe</strong> <strong>Revenue Intelligence 2 Arabic</strong>: طبقة ذكاء فوق Billing وPayments تجمع سجل الدفع والتجارب والإلغاءات، تُتنبأ بالانسحاب والتوسع، تُولّد رسائل استرداد وعروض تجديد بالفصحى أو لهجة العميل، تُقترح توقيت الإرسال، تتزامن مع البريد وواتساب، وتعرض لوحات تنفيذية عربية — لشركات الاشتراك والتطبيقات والتجارة الإلكترونية في العالم العربي.</p>
      <p>المشكلة التي حلّتها: الإصدار الأول كان إنجليزيًا ويُهمل فشل البطاقات المحلية؛ Revenue Intelligence 2 يدعم تفسيرًا لرفض الدفع في السعودية والإمارات ومصر، قواعد نبرة ودية رسمية، تفعيل عروض «خصم عودة» تلقائيًا، تقارير أسبوعية للمؤسسين بالعربية، تكامل HubSpot وSegment، قوالب «تطبيق» و«صندوق اشتراك» و«سوق إلكتروني»، وبرنامج «Stripe Revenue Partners MENA».</p>
      <p>القدرات الأساسية: تنبؤ إلغاء وتوسع؛ رسائل استرداد عربية؛ فهم فشل دفع محلي؛ لوحات عربية؛ تكامل نمو.</p>
      <p>للمبدعين العرب: خدمة «إنقاذ الإيراد المتكرر» — من يُدير 6 عملاء بـ720–3200 دولار/شهر يحوّل بيانات Stripe إلى حملات استرداد دون توظيف محلل بيانات بدوام كامل.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Stripe Revenue Intelligence 2 Arabic؟</h3>
        <ul>
          <li><strong>تفعيل Revenue Intelligence وقواعد رسائل:</strong> 12–28 يومًا — 4500–24000 دولار.</li>
          <li><strong>إدارة حملات استرداد وتقارير شهريًا:</strong> — 720–3200 دولار/عميل/شهر.</li>
          <li><strong>حزم قوالب قطاع (SaaS، اشتراك، سوق):</strong> — 58–250 دولار/حزمة.</li>
          <li><strong>ورش «إنقاذ اشتراكات بالذكاء والعربية»:</strong> — 55–220 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Stripe</span>
        <span class="tag">Revenue</span>
        <span class="tag">Billing</span>
        <span class="tag">Retention</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>ElevenLabs Dubbing Studio 3 Arabic: دبلجة ذكية — صوتك العربي يصل لعشر لغات بسرعة البرق</h2>
      <p class="article-lead">«لدينا دورة بالعربية ونريد نسخًا إنجليزية وفرنسية وتركية قبل موسم التسجيل». في 19 نوفمبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 3 Arabic</strong>: استوديو دبلجة يفصل الصوت عن الموسيقى، يُترجم النص ويُولّد أصواتًا طبيعية بالعربية وإليها، يُزامن الحركة مع الشفاه قدر الإمكان، يحافظ على نبرة المقدّم بين اللغات، يدعم تصديرًا ليوتيوب ونيتفليكس ومنصات التعليم، ويُتيح مراجعة بشرية سريعة — للمؤثرين ومنصات التعليم والوكالات الإعلامية في المنطقة.</p>
      <p>المشكلة التي حلّتها: الإصدار 2 كان يُشوّه بعض الحروف أو يطيل الإنتاج؛ Dubbing Studio 3 يدعم لهجات عربية متعددة، توليدًا دفعيًا لحلقات كاملة، قوالب «دورة تدريبية» و«بودكاست» و«إعلان»، حقوق استخدام تجاري واضحة، مكتبة أصوات مرخّصة، تكامل مع Descript وAdobe Premiere، وبرنامج «ElevenLabs Creator Arabia».</p>
      <p>القدرات الأساسية: دبلجة عربية ثنائية الاتجاه؛ فصل صوت وموسيقى؛ أصوات طبيعية؛ إصدارات متعددة اللغات؛ تصدير منصات.</p>
      <p>للمبدعين العرب: استوديو «محتوى عالمي من مقر واحد» — من يُسلّم 4 مشاريع دبلجة شهريًا بـ2200–12000 دولار للمشروع يخدم مدربين ومؤسسات تريد توسعًا دوليًا دون فرق تسجيل ضخمة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 3 Arabic؟</h3>
        <ul>
          <li><strong>دبلجة دورة أو مسلسل قصير متعدد اللغات:</strong> — 2200–12000 دولار/مشروع.</li>
          <li><strong>باقة دبلجة شهرية (حلقات أو إعلانات):</strong> — 1400–6500 دولار/شهر.</li>
          <li><strong>إعداد هوية صوتية وقوالب ElevenLabs:</strong> 5–12 يومًا — 950–4800 دولار.</li>
          <li><strong>دورة «دبلجة ومحتوى عالمي بالعربية»:</strong> — 58–235 دولار/مقعد.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 19-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="19-11-2026 -- 12-AM.html">
          📰 19 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "19-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/19-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/19-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
    print(f"Written: {README}")


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