#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 20-10-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "20-10-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Canva Magic Media 4 Arabic · Mistral Le Chat Enterprise 4 Arabic · "
    "Descript Underlord 4 Arabic · Make.com AI Scenarios 4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Canva Magic Media 4 Arabic، Mistral Le Chat Enterprise 4 Arabic، Descript Underlord 4 Arabic، Make.com AI Scenarios 4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 20 أكتوبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌆 نشرة AI العالمية</span>
      <h1>من Canva Magic Media 4 Arabic الذي يُحوّل brief حملة عربية إلى فيديو وصور وkits بصرية جاهزة للنشر قبل غروب الشمس، إلى Mistral Le Chat Enterprise 4 Arabic الذي يُشغّل مساعدًا أوروبيًا متوافقًا مع GDPR داخل شركتك بلهجة فريقك، ومن Descript Underlord 4 Arabic الذي يُ edit بودكast ساعتين بأمر واحد ويُ dub لهجات MENA، إلى Make.com AI Scenarios 4 Arabic الذي يُبني automations معقدة من جملة عربية ويُشغّل WhatsApp وCRM وNotion — أربع قصص مسائية في 20 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء الغروب!</h1>
      <p class="hero-sub">مساءٌ للإبداع والامتثال والمحتوى والأتمتة: مسوقون يطاردون deadlines بصرية، CIOs يريدون AI داخل EU residency، creators يغرقون في post-production، وops teams تُ copy-paste بين تطبيقات. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 20 أكتوبر 2026</span>
        <span>🌇 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Canva Magic Media 4 Arabic: فيديو وصور وbrand kits — من الفكرة إلى حملة RTL في دقائق!</h2>
      <p class="article-lead">«العميل يريد 12 creative لـ White Friday — والمصمم في إجازة». في 20 أكتوبر 2026، أطلقت <strong>Canva</strong> <strong>Magic Media 4 Arabic</strong>: طبقة media generation فوق Magic Studio تفهم briefs بالفصحى واللهجات، تُ produce short-form video وstatic ads وcarousel RTL، تُ respect Brand Kit (colors، fonts، logos)، تُ extend clips من B-roll library MENA، تُ generate captions وhashtag sets، تُ resize لـ Meta وTikTok وSnap وGoogle Ads، وتُ export إلى Campaign Manager — لل agencies وSMBs وfranchises في المنطقة.</p>
      <p>المشكلة التي حلّتها: Magic Studio 5 كان يُ struggle مع Arabic motion typography؛ الإصدار 4 Media يُ Cairo وTajawal motion presets، يُ benchmark −46% وقت first campaign draft في retail chain سعودي، يُ human review queue لل legal، يُ version history per brand، يُ API لل DAM integrations، ويُ credits metering لل enterprises.</p>
      <p>القدرات الأساسية: Text-to-video RTL; Image variations on-brand; Campaign kit bundles; Auto-resize ad formats; Arabic captions; Team approval workflows.</p>
      <p>للمبدعين العرب: creative agencies — «Magic Media 4 Arabic seasonal kit in 3 days» لل brands 8–40 assets/week. من يُ deliver 12 kits/ربع بـ 1600–28000 دولار + retainer 130–1050 دولار/شهر يبني «استوديو Canva Media عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Magic Media 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة seasonal kit (brief، assets، resize، handoff):</strong> 2–6 أيام — 1600–28000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ brand refresh وA/B variants:</strong> — 130–1050 دولار/شهر.</li>
          <li><strong>Vertical packs (F&amp;B، fashion، fintech ads):</strong> — 55–240 دولار/pack.</li>
          <li><strong>دورات «حملات بصرية ذكية بـ Canva Magic Media بالعربية»:</strong> — 36–168 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Magic Media</span>
        <span class="tag">Creative AI</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Mistral Le Chat Enterprise 4 Arabic: مساعد AI أوروبي — عربي، GDPR، وdata residency جاهزة!</h2>
      <p class="article-lead">«لا نريد بياناتنا تغادر EU — ونريد copilot يفهم العربية». في 20 أكتوبر 2026، أطلقت <strong>Mistral AI</strong> <strong>Le Chat Enterprise 4 Arabic</strong>: workspace للفرق يُ deploy في EU وGCC regions، يُ understand MSA وخليجي ومصري، يُ ingest SharePoint وGoogle Drive وConfluence، يُ cite sources RTL، يُ draft policies وcontracts وRFPs، يُ orchestrate agents على internal APIs، يُ SSO وSCIM وaudit logs، ويُ zero training على customer data — لل banks وinsurance وpublic sector في MENA/EU corridors.</p>
      <p>المشكلة التي حلّتها: Le Chat Enterprise 3 كان يُ weak على Arabic legal terminology؛ الإصدار 4 يُ legal Arabic lexicon packs، يُ benchmark −43% time-to-memo في law firm دبي، يُ on-prem hybrid connectors، يُ DLP redaction pipeline، يُ admin prompt libraries Arabic، ويُ partner program لل SIs العرب.</p>
      <p>القدرات الأساسية: Enterprise chat RTL; Document Q&amp;A with citations; Agent orchestration; EU/GCC residency; SSO and audit; Arabic legal packs.</p>
      <p>للمبدعين العرب: compliance-first consultancies — «Le Chat Enterprise 4 Arabic rollout in 10 days» لل orgs 200–15000 seats. من يُ deploy 5 rollouts/ربع بـ 4200–72000 دولار + managed 260–2100 دولار/شهر يبني «مكتب Mistral عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Mistral Le Chat Enterprise 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة enterprise rollout (connectors، governance، training):</strong> 7–18 يومًا — 4200–72000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ policy tuning وusage review:</strong> — 260–2100 دولار/شهر.</li>
          <li><strong>Industry packs (banking، insurance، public sector):</strong> — 88–395 دولار/pack.</li>
          <li><strong>دورات «AI مؤسسي متوافق بـ Le Chat Enterprise بالعربية»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Mistral</span>
        <span class="tag">Le Chat</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">GDPR</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Descript Underlord 4 Arabic: edit فيديو وبودكast — dubbing، filler removal، وpublish بأمر واحد!</h2>
      <p class="article-lead">«تسجيل ساعتين — والمونتاج يأخذ يومًا كاملًا». في 20 أكتوبر 2026، أطلقت <strong>Descript</strong> <strong>Underlord 4 Arabic</strong>: agent فوق Descript editor يُ transcribe Arabic dialects، يُ remove fillers وsilences، يُ rewrite sections بصوت clone brand-safe، يُ dub إلى MENA dialects مع lip-sync preview، يُ generate chapters وshow notes RTL، يُ export إلى YouTube وSpotify وLinkedIn، ويُ team review links — لل podcasters وcourse creators وcorporate comms في المنطقة.</p>
      <p>المشكلة التي حلّتها: Underlord 3 كان يُ mis-align diacritics في TTS؛ الإصدار 4 يُ Arabic prosody models، يُ benchmark −51% post-production hours في edtech studio القاهرة، يُ multi-speaker diarization، يُ glossary locks لل brand terms، يُ API batch لل catalogs، ويُ rights management لل voice clones.</p>
      <p>القدرات الأساسية: Arabic transcription dialects; AI edit by text; Voice dub MENA; Chapter and show notes RTL; Multi-platform export; Team review.</p>
      <p>للمبدعين العرب: post-production studios — «Underlord 4 Arabic catalog sprint in 5 days» لل clients 4–80 hours/month. من يُ onboard 9 clients/ربع بـ 1400–26000 دولار + per-hour overflow 18–95 دولار/ساعة يبني «استوديو Descript عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Descript Underlord 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة catalog sprint (edit، dub، chapters، publish):</strong> 3–9 أيام — 1400–26000 دولار/عميل.</li>
          <li><strong>Overflow editing per finished hour:</strong> — 18–95 دولار/ساعة.</li>
          <li><strong>Course and podcast templates (intro، CTA، ads):</strong> — 42–185 دولار/template.</li>
          <li><strong>دورات «إنتاج محتوى سريع بـ Descript Underlord بالعربية»:</strong> — 44–205 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Descript</span>
        <span class="tag">Underlord</span>
        <span class="tag">Video AI</span>
        <span class="tag">Podcast</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Make.com AI Scenarios 4 Arabic: أتمتة من جملة واحدة — WhatsApp، CRM، ERP، وNotion!</h2>
      <p class="article-lead">«نريد: طلب WhatsApp → CRM → فاتورة → Slack — والـ IT مشغول شهرين». في 20 أكتوبر 2026، أطلقت <strong>Make.com</strong> <strong>AI Scenarios 4 Arabic</strong>: builder يُ parse workflow descriptions بالفصحى واللهجات، يُ generate scenarios مع error handling، يُ map apps (HubSpot، Zoho، Salla، SAP B1، Notion، Twilio)، يُ suggest data transforms وfilters، يُ simulate runs sandbox، يُ document flows RTL لل ops teams، ويُ sell templates في marketplace — لل agencies وSIs وinternal ops في MENA.</p>
      <p>المشكلة التي حلّتها: AI Scenarios 2 كان يُ break على Arabic field names؛ الإصدار 4 يُ Unicode-safe mappings، يُ benchmark −49% time-to-first-production scenario في logistics SMB الأردن، يُ observability dashboards، يُ version control Git sync، يُ role-based sharing، ويُ white-label لل partners.</p>
      <p>القدرات الأساسية: NL-to-scenario RTL; App connector suggestions; Sandbox simulation; Arabic flow docs; Marketplace templates; Partner white-label.</p>
      <p>للمبدعين العرب: automation agencies — «AI Scenarios 4 Arabic ops stack in 6 days» لل orgs 5–500 employees. من يُ ship 10 stacks/ربع بـ 1100–22000 دولار + care 95–820 دولار/شهر يبني «مصنع Make.com عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Make.com AI Scenarios 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة ops stack (discovery، scenarios، docs، handoff):</strong> 4–12 يومًا — 1100–22000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وscenario updates:</strong> — 95–820 دولار/شهر.</li>
          <li><strong>Industry templates (e-commerce، HR onboarding، finance):</strong> — 38–175 دولار/template.</li>
          <li><strong>دورات «أتمتة ذكية بـ Make.com AI Scenarios بالعربية»:</strong> — 40–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Make.com</span>
        <span class="tag">Automation</span>
        <span class="tag">No-code</span>
        <span class="tag">Integrations</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 20-10-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="20-10-2026 -- 04-PM.html">
          📰 20 أكتوبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "20-10-2026 -- 04-PM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/20-10-2026 -- 04-PM.html"
    content = README.read_text(encoding="utf-8")
    if new in content and "أحدث إصدار" in content.split(new)[0][-200:]:
        print(f"README already contains entry: {README}")
        return
    old_marker = "news/20-10-2026 -- 08-AM.html"
    new_line = (
        f"- [`{new}`](news/20-10-2026%20--%2004-PM.html) — أحدث إصدار ({TOPICS}) "
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
        "أفكar",
        "دolار",
        "البروtokol",
        "أktober",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "y\u0650",
        "المشkلة",
        "mezclar",
        "وy\u0650",
        "prefe r",
        " t\u0650",
        " y\u0650",
        "الإصrador",
        "وy\u0650",
    ]
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
    update_readme()


if __name__ == "__main__":
    main()
