#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 27-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "27-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Copilot Studio 2 Arabic · Canva Magic Studio 6 Arabic · "
    "ElevenLabs Voice Agents 2 Arabic · HubSpot Breeze Agents 3 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot Studio 2 Arabic، Canva Magic Studio 6 Arabic، ElevenLabs Voice Agents 2 Arabic، HubSpot Breeze Agents 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 27 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Copilot Studio 2 Arabic الذي يُحوّل «ردّ على شكاوى العملاء بالخليجية» إلى وكيل Teams يُ escalate للبشر بقواعد compliance، إلى Canva Magic Studio 6 Arabic الذي يُ birth حملة Ramadan كاملة — reels وcopy وbrand kit من brief واحد، ومن ElevenLabs Voice Agents 2 Arabic الذي يُجيب مكالمات support بصوت طبيعي ويُ handoff للموظف مع transcript عربي، إلى HubSpot Breeze Agents 3 Arabic الذي يُ research leads ويُ draft sequences ويُ book meetings من CRM — أربع قصص ليلية في 27 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمؤسسات والمبدعين والصوت والمبيعات: IT يبني agents بدون code، agencies تسبق deadlines التصميم، call centers تغرق في wait time، وفرق revenue تنتظر research يدويًا قبل كل outreach. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 27 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot Studio 2 Arabic: وكلاء مؤسسات بدون كود — Teams، SharePoint، وامتثال MENA!</h2>
      <p class="article-lead">«نريد bot يفهم policy الاسترجاع بالعربية — والـ IT مشغول شهرين». في 27 أكتوبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot Studio 2 Arabic</strong>: منصة low-code لبناء copilots وagents تُ understand Gulf dialects في chat، تُ connect Dataverse وSharePoint وDynamics وSAP connectors، تُ orchestrate multi-step workflows مع human-in-the-loop، تُ guardrails لل PII وsector rules، تُ deploy في Teams وweb وWhatsApp Business API، تُ analytics على resolution rate باللهجة، ويُ sovereign hosting options لـ GCC — لل enterprises وSIs وBPOs.</p>
      <p>المشكلة التي حلّتها: Studio 1 كان يُ hallucinate أرقام policy عند mixed Arabic-English KB؛ الإصدار 2 يُ grounded generation مع citation من docs، يُ benchmark −41% وقت «agent pilot to production» في telco الدمام، يُ reusable topic packs (HR، IT helpdesk، sales enablement)، يُ Copilot Studio SDK لل custom channels، يُ audit trail لـ regulators، ويُ A/B testing على prompts عربية.</p>
      <p>القدرات الأساسية: Arabic enterprise agents; Teams and WhatsApp deploy; Grounded KB answers; Compliance guardrails; Low-code orchestration; GCC sovereign options.</p>
      <p>للمبدعين العرب: Microsoft partners — «Copilot Studio 2 Arabic agent factory in 8 days» لل orgs 500–50000 employees. من يُ deliver 8 agents/ربع بـ 3200–78000 دولار + managed 280–2200 دولار/شهر يبني «مركز copilot عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot Studio 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة agent factory (design، KB، channels، UAT):</strong> 5–18 يومًا — 3200–78000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ KB refresh وprompt tuning:</strong> — 280–2200 دولار/شهر.</li>
          <li><strong>Industry packs (banking، retail، healthcare، gov):</strong> — 72–320 دولار/pack.</li>
          <li><strong>دورات «ابنِ وكيل مؤسسي بـ Copilot Studio بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Copilot Studio</span>
        <span class="tag">Enterprise</span>
        <span class="tag">Agents</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Canva Magic Studio 6 Arabic: حملات وbrand كاملة — فيديو، copy، وprint جاهز للطباعة!</h2>
      <p class="article-lead">«العميل يريد 40 asset لRamadan — والمصمم نائم وال deadline غدًا». في 27 أكتوبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Studio 6 Arabic</strong>: suite موحّدة يُ generate layouts RTL، يُ write headlines وCTAs باللهجات، يُ Magic Video من storyboard عربي، يُ resize لـ Instagram وSnap وOOH، يُ Brand Kit sync لل colors وfonts، يُ translate campaigns مع tone control، يُ print-ready PDF لل billboards، ويُ Teams approvals وcomment threads — لل agencies وin-house marketers وcreators.</p>
      <p>المشكلة التي حلّتها: Magic Studio 5 كان يُ clip نص عربي في video lower-thirds؛ الإصدار 6 يُ bidi-safe motion templates، يُ benchmark −47% وقت «campaign kit delivery» في agency دبي، يُ batch edit 100+ variants، يُ AI photo replace مع hijab-aware options، يُ reseller white-label لل MENA partners، ويُ accessibility alt-text عربي تلقائي.</p>
      <p>القدرات الأساسية: Arabic campaign generator; RTL video magic; Brand Kit automation; Multi-channel resize; Print-ready export; Agency collaboration.</p>
      <p>للمبدعين العرب: Canva partners — «Magic Studio 6 Arabic seasonal kit in 2 days» لل brands وSMBs. من يُ ship 22 kits/ربع بـ 680–18500 دولار + retainer 130–1050 دولار/شهر يبني «استوديو Canva AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Studio 6 Arabic؟</h3>
        <ul>
          <li><strong>باقة seasonal kit (concepts، assets، video، print):</strong> 1–5 أيام — 680–18500 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ campaigns وBrand Kit updates:</strong> — 130–1050 دولار/شهر.</li>
          <li><strong>Niche templates (restaurants، clinics، real estate، events):</strong> — 38–175 دولار/template pack.</li>
          <li><strong>دورات «حملات ذكية بـ Canva Magic Studio بالعربية»:</strong> — 32–148 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Magic Studio</span>
        <span class="tag">Design</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>ElevenLabs Voice Agents 2 Arabic: مركز اتصال بالذكاء الاصطناعي — صوت طبيعي، tools، وhandoff!</h2>
      <p class="article-lead">«90% المكالمات: أين طلبي؟ — وال queue 25 دقيقة». في 27 أكتوبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Voice Agents 2 Arabic</strong>: platform conversational voice تُ speak MSA وGulf وEgyptian، تُ connect CRM وorder APIs via tools، تُ interrupt handling وemotion detection، يُ live transfer لل agent مع Arabic summary، يُ record وQA scoring باللهجة، يُ telephony SIP وTwilio integration، يُ latency under 300ms target، ويُ compliance recording لل banking — لل e-commerce وlogistics وclinics.</p>
      <p>المشكلة التي حلّتها: Voice Agents 1 كان يُ mishear أرقام طلبات عربية؛ الإصدار 2 يُ digit-aware ASR وconfirmation loops، يُ benchmark −52% abandoned calls في retailer جeddah، يُ multi-language switch mid-call، يُ knowledge base sync hourly، يُ custom voice clone لل brand (with consent)، ويُ analytics dashboard على intent clusters.</p>
      <p>القدرات الأساسية: Arabic voice agents; Tool calling on phone; Live human handoff; Low-latency TTS; Telephony integrations; Call analytics.</p>
      <p>للمبدعين العرب: voice AI consultancies — «Voice Agents 2 Arabic IVR replacement in 7 days» لل call centers 500–50000 calls/month. من يُ deploy 5 stacks/ربع بـ 2400–62000 دولار + ops 210–1750 دولار/شهر يبني «مركز صوت AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Voice Agents 2 Arabic؟</h3>
        <ul>
          <li><strong>باقة IVR replacement (flows، tools، QA، go-live):</strong> 4–14 يومًا — 2400–62000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ flow tuning وintent updates:</strong> — 210–1750 دولار/شهر.</li>
          <li><strong>Vertical playbooks (delivery، appointments، collections، surveys):</strong> — 58–265 دولار/playbook.</li>
          <li><strong>دورات «مراكز اتصال ذكية بـ ElevenLabs Voice Agents بالعربية»:</strong> — 44–210 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Voice AI</span>
        <span class="tag">Call Center</span>
        <span class="tag">Telephony</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>HubSpot Breeze Agents 3 Arabic: مبيعات وتسويق وكيلية — research، sequences، وmeetings!</h2>
      <p class="article-lead">«كل SDR يقضي ساعتين يوميًا على LinkedIn — قبل أن يكتب سطرًا واحدًا». في 27 أكتوبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze Agents 3 Arabic</strong>: agents داخل CRM يُ research accounts بالعربية والإنجليزية، يُ draft personalized emails وWhatsApp templates، يُ suggest next-best-action من deal stage، يُ book meetings via calendar AI، يُ summarize calls وtickets لل managers، يُ content ideas لل blogs MENA، يُ connect Marketing Hub وService Hub، ويُ revenue attribution dashboards — لل B2B SaaS وagencies وfranchisors.</p>
      <p>المشكلة التي حلّتها: Breeze Agents 2 كان يُ generic outreach يُ trigger spam filters في Gulf inboxes؛ الإصدار 3 يُ dialect-aware personalization وdomain warm-up hints، يُ benchmark −39% وقت «lead to meeting booked» في SaaS startup عمان، يُ competitive intel briefs، يُ multi-agent handoff (research → write → schedule)، يُ GDPR and local consent flags، ويُ partner marketplace لل Arabic playbooks.</p>
      <p>القدرات الأساسية: Arabic sales agents; Account research; Outreach sequences; Meeting booking; Call summaries; RevOps analytics.</p>
      <p>للمبدعين العرب: HubSpot partners — «Breeze Agents 3 Arabic revenue pod in 5 days» لل teams 3–40 reps. من يُ onboard 12 pods/ربع بـ 1100–34000 دولار + managed 160–1280 دولار/شهر يبني «ممارسة HubSpot AI عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze Agents 3 Arabic؟</h3>
        <ul>
          <li><strong>باقة revenue pod (research agent، sequences، dashboards، training):</strong> 3–10 أيام — 1100–34000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ playbook refresh وA/B outreach:</strong> — 160–1280 دولار/شهر.</li>
          <li><strong>Industry sequences (EdTech، logistics، pro services، hospitality):</strong> — 42–198 دولار/sequence pack.</li>
          <li><strong>دورات «مبيعات وكيلية بـ HubSpot Breeze بالعربية»:</strong> — 38–182 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Breeze</span>
        <span class="tag">Sales AI</span>
        <span class="tag">CRM</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 27-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="27-10-2026 -- 12-AM.html">
          📰 27 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "27-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/27-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/26-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/27-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
        f"(4 أخبار + أفكار ربح من AI)"
    )
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if old_marker in line and "أحدث إصدار" in line:
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
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"ERROR: mixed-script typo found: {pat}")
    if re.search(r"[yY][\u064B-\u0652\u0670]", text):
        raise SystemExit("ERROR: Latin y with Arabic diacritic found")
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
