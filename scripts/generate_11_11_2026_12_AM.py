#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 11-11-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "11-11-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "AWS Bedrock Agents 4 Arabic · IBM watsonx Orchestrate 4 Arabic · "
    "Meta WhatsApp Business AI Agents 4 Arabic · Dropbox Dash 4 Arabic"
)

TOPICS_PLAIN = TOPICS.replace("&amp;", "&")

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — AWS Bedrock Agents 4 Arabic، IBM watsonx Orchestrate 4 Arabic، Meta WhatsApp Business AI Agents 4 Arabic، Dropbox Dash 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 11 نوفمبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من AWS Bedrock Agents 4 Arabic الذي يُحوّل جملة عربية إلى وكيل يُقرأ S3 ويُفتح ticket في Jira قبل أن تبرد قهوتك الليلية، إلى IBM watsonx Orchestrate 4 Arabic الذي يُنسّق إجازات ومصروفات وتذاكر IT في محادثة واحدة، ومن Meta WhatsApp Business AI Agents 4 Arabic الذي يُبيع ويُدعم على واتساب بلهجة الخليج والشام، إلى Dropbox Dash 4 Arabic الذي يُجيب «أين مسودة العقد؟» من Slack وDrive وNotion في ثوانٍ — أربع قصص ليلية في 11 نوفمبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلٌ لفرق cloud وHR وتجارة ومعرفة: الـ POCs تتعثر، الموظفون يضيعون بين portals، leads واتساب تبرد، والملفات تختبئ في عشر سحاب. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 11 نوفمبر 2026</span>
        <span>🌃 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>AWS Bedrock Agents 4 Arabic: من فكرة بالعربية إلى وكيل production — knowledge bases، tools، وmulti-agent!</h2>
      <p class="article-lead">«نريد وكيلًا يقرأ policy من S3 ويُفتح ticket في Jira — والفريق عالق في POC منذ شهر». في 11 نوفمبر 2026، أطلقت <strong>Amazon Web Services</strong> <strong>Bedrock Agents 4 Arabic</strong>: منصة لبناء agents يفهمون NL بالعربية (MSA وخليجي ومصري)، يُ retrieve من knowledge bases، يُ invoke action groups (Lambda، API Gateway، Step Functions)، يُ plan multi-step، يُ enforce guardrails وPII redaction، ويُ deploy في region Bahrain وFrankfurt — للبنوك وfintech وlogistics في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 3 كان orchestration محدودًا على سلاسل طويلة؛ الإصدار 4 يُ supervise وكلاء متعددين (research → approve → execute)، يُ act (query Aurora، update DynamoDB، send SES مع human gate، post ملخص عربي في Chime)، يُ integrate Claude 4.5 وNova 2 Pro وLlama 4 via Bedrock، يُ eval harness «Arabic faithfulness»، يُ log CloudTrail لكل invocation، ويُ ship accelerators KYC وvendor risk وhelpdesk.</p>
      <p>القدرات الأساسية: Arabic Agent Builder في console؛ templates جاهزة (invoice chase، onboarding، SOC triage)؛ MCP gateway؛ ميزانيات تكلفة لكل وكيل؛ A/B بين foundation models؛ SDK للـ integrators في الخليج.</p>
      <p>للمبدعين العرب: AWS partners وAI studios — «Arabic Bedrock agent in 7 days» لل enterprises 300+ مقعد. من يُسلّم 5 برامج Agents 4/ربع بـ 3400–52000 دولار + ضبط شهري 680–5100 دولار/شهر يبني ممارسة وكلاء cloud عربية.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من AWS Bedrock Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>Bedrock Agents 4 rollout (Arabic UX، KB، tools، guardrails، go-live):</strong> 6–18 يومًا — 3400–52000 دولار/عميل.</li>
          <li><strong>ضبط تقييم الوكلاء وprompts/tools:</strong> — 680–5100 دولار/شهر.</li>
          <li><strong>حزم vertical (banking، logistics، healthcare):</strong> — 58–295 دولار/حزمة.</li>
          <li><strong>دورات «وكلاء سحابة عربية مع Amazon Bedrock»:</strong> — 48–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">AWS</span>
        <span class="tag">Bedrock</span>
        <span class="tag">Agents</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>IBM watsonx Orchestrate 4 Arabic: موظف رقمي واحد — HR، finance، IT، وprocurement بمحادثة!</h2>
      <p class="article-lead">«موظف يسأل عن رصيد الإجازة وحالة المصروف وطلب laptop — وثلاثة portals مختلفة». في 11 نوفمبر 2026، أطلقت <strong>IBM</strong> <strong>watsonx Orchestrate 4 Arabic</strong>: طبقة digital worker فوق Workday وSAP وServiceNow وMicrosoft 365 يُ understand intents بالعربية، يُ orchestrate skills عبر الأنظمة، يُ draft موافقات، يُ escalate استثناءات، يُ summarize «ما الذي تأخر هذا الأسبوع؟» للمدير — لـ holding companies وairlines وجامعات في الخليج.</p>
      <p>المشكلة التي حلّتها: Orchestrate 3 كان يعتمد على catalog ثابت؛ الإصدار 4 يُ act (submit PTO، route PO، reset MFA، schedule panel)، يُ memory عبر جلسات الموظف، يُ integrate watsonx.governance للـ bias وPII، يُ comms ثنائية EN/AR، خيار on-prem للقطاع الحساس، SLA latency لـ 10k+ محادثة متزامنة، وpacks حكومة وطاقة MENA.</p>
      <p>القدرات الأساسية: Arabic Digital Employee Builder؛ مكتبة 450+ skill؛ قناة voice لمراكز الاتصال؛ تحليلات «ساعات أعيدت للأعمال»؛ fast-start IBM Consulting 18 يومًا.</p>
      <p>للمبدعين العرب: IBM partners وHR consultancies — «Arabic digital worker in 11 days» لل مجموعات 5000+ موظف. من يُبيع 3 estates Orchestrate 4/سنة بـ 5400–80000 دولار/كل + care 1000–7500 دولار/شهر يبني automation enterprise premium.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من IBM watsonx Orchestrate 4 Arabic؟</h3>
        <ul>
          <li><strong>Orchestrate 4 deployment (skills، Arabic NL، integrations، UAT):</strong> 9–26 يومًا — 5000–80000 دولار/مشروع.</li>
          <li><strong>صيانة skills وتجربة موظف شهرية:</strong> — 1000–7500 دولار/شهر.</li>
          <li><strong>حزم أقسام (HR، finance، IT):</strong> — 64–325 دولار/حزمة.</li>
          <li><strong>دورات «قوة عاملة رقمية عربية مع watsonx»:</strong> — 54–255 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">IBM</span>
        <span class="tag">watsonx</span>
        <span class="tag">Automation</span>
        <span class="tag">HR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Meta WhatsApp Business AI Agents 4 Arabic: بيع ودعم على واتساب — qualify، catalog، وcart recovery باللهجة!</h2>
      <p class="article-lead">«80% من leads الخليج تأتي واتساب — وردود copy-paste تُفقد الصفقة ليلًا». في 11 نوفمبر 2026، أطلقت <strong>Meta</strong> <strong>WhatsApp Business AI Agents 4 Arabic</strong>: agents داخل WhatsApp Business Platform يُ qualify leads، يُ recommend من catalog، يُ apply promo rules، يُ handoff للبشر مع transcript عربي، يُ recover سلات مهجورة، يُ confirm COD — للـ D2C وعيادات وعقارات في MENA.</p>
      <p>المشكلة التي حلّتها: Agents 3 كان template-heavy؛ الإصدار 4 يُ understand voice notes عربية، يُ integrate Shopify وSalla وZid وروابط دفع، يُ enforce سياسات commerce، dialect packs خليجي/مصري/شامي، analytics funnel لكل حملة، وتسعير شفاف per conversation للـ SMBs.</p>
      <p>القدرات الأساسية: Agent Studio prompts عربية؛ مزامنة catalog لحظية؛ Click-to-WhatsApp ads؛ human-in-the-loop؛ شهادة شريك «MENA Commerce Agent 4».</p>
      <p>للمبدعين العرب: Meta Business Partners وperformance agencies — «Arabic WhatsApp agent live in 4 days» لل تجار 1k+ محادثة/أسبوع. من يُشغّل 12 stack Agent 4/ربع بـ 1200–12500 دولار/كل + تحسين 240–1820 دولار/شهر يغلق أسرع قناة مبيعات في المنطقة.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Meta WhatsApp Business AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>WhatsApp Agent 4 setup (catalog، نبرة عربية، ads، تدريب):</strong> 3–11 يومًا — 1100–12500 دولار/عميل.</li>
          <li><strong>ضبط محادثات وA/B حملات شهريًا:</strong> — 240–1820 دولار/شهر.</li>
          <li><strong>حزم commerce (beauty، electronics، عيادات):</strong> — 40–185 دولار/حزمة.</li>
          <li><strong>دورات «تجارة محادثية عربية على واتساب»:</strong> — 34–165 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Meta</span>
        <span class="tag">WhatsApp</span>
        <span class="tag">Commerce</span>
        <span class="tag">SMB</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Dropbox Dash 4 Arabic: «أين العقد الموقّع؟» — search موحّد، إجابات، وactions عبر السحاب!</h2>
      <p class="article-lead">«400 GB متفرقة — والمحامي ينتظر ساعة ليجد clause». في 11 نوفمبر 2026، أطلقت <strong>Dropbox</strong> <strong>Dash 4 Arabic</strong>: universal AI search وassistant فوق Dropbox وGoogle Drive وMicrosoft 365 وSlack وNotion وJira يُ answer بالعربية مع citations، يُ summarize مجلدات، يُ draft ردود من السياق، يُ suggest actions (رابط مشاركة، توقيع، مراجعة) — للـ law firms وconsultancies وNGOs في MENA.</p>
      <p>المشكلة التي حلّتها: Dash 3 كان search-first؛ الإصدار 4 يُ act ضمن permissions (shared link، Dropbox Sign، ملخص عربي في Slack)، preview RTL للـ PDFs، احترام scopes، SSO وaudit، ووضع «project brain» يُ rebuild timeline من مستندات متناثرة.</p>
      <p>القدرات الأساسية: Dash Chat عربي؛ connectors legal وconsulting؛ voice query mobile؛ analytics «أسئلة وفّرت وقتًا»؛ هوامش إعادة بيع للـ VARs.</p>
      <p>للمبدعين العرب: productivity consultants — «Arabic knowledge hub in 6 days» لفرق 50–800 مستخدم. من يُ onboard 8 workspaces Dash 4/ربع بـ 1500–15000 دولار/كل + retainer 290–2150 دولار/شهر يحوّل فوضى الملفات إلى إيراد متكرر.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dropbox Dash 4 Arabic؟</h3>
        <ul>
          <li><strong>Dash 4 rollout (connectors، Q&amp;A عربية، permissions، تدريب):</strong> 4–14 يومًا — 1400–15000 دولار/عميل.</li>
          <li><strong>تنظيف معرفة وصحة connectors شهريًا:</strong> — 290–2150 دولار/شهر.</li>
          <li><strong>حزم قطاعات (legal، audit، وكالات إبداع):</strong> — 46–215 دولار/حزمة.</li>
          <li><strong>دورات «معرفة مؤسسية عربية مع Dropbox Dash»:</strong> — 38–178 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dropbox</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Search</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 11-11-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="11-11-2026 -- 12-AM.html">
          📰 11 نوفمبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "11-11-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/11-11-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    new_line = (
        f"- [`{new}`](news/11-11-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS_PLAIN}) "
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
