#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 23-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "23-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "ElevenLabs Dubbing Studio 4 Arabic · Make.com AI Agents 4 Arabic · "
    "HubSpot Breeze AI 4 Arabic · Runway Gen-4 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — ElevenLabs Dubbing Studio 4 Arabic، Make.com AI Agents 4 Arabic، HubSpot Breeze AI 4 Arabic، Runway Gen-4 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 23 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من ElevenLabs Dubbing Studio 4 Arabic الذي يُ dub فيديو YouTube من إنجليزي إلى خليجي ومصري في دقائق مع sync شفاه، إلى Make.com AI Agents 4 Arabic الذي يُ orchestrate CRM وWhatsApp وGoogle Sheets من prompt عربي، ومن HubSpot Breeze AI 4 Arabic الذي يُ summarize deals ويُ draft emails مبيعات بلهجة سوقك، إلى Runway Gen-4 Arabic الذي يُ produce إعلانات سينمائية من storyboard نصي RTL — أربع قصص ليلية في 23 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للمحتوى والأتمتة والمبيعات والإبداع البصري: creators ينتظرون مترجمين، ops teams تربط 12 SaaS يدويًا، reps يغرقون في CRM، وmarketers يدفعون آلاف الدولارات لـ production. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 23 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>ElevenLabs Dubbing Studio 4 Arabic: دبلجة فيديو — صوت، لهجة، وsync شفاه للعرب!</h2>
      <p class="article-lead">«القناة عربية — والضيف أجنبي يتحدث إنجليزيًا لساعة». في 23 أكتوبر 2026، أطلقت <strong>ElevenLabs</strong> <strong>Dubbing Studio 4 Arabic</strong>: منصة dubbing تُ ingest YouTube وMP4 وpodcasts، تُ transcribe multi-speaker، تُ translate إلى MSA أو Gulf أو Egyptian أو Levantine، تُ clone tone وemotion، تُ lip-sync optional لل talking-head، تُ export SRT وaudio stems وfull mix، تُ batch 50 فيديو/ليلة، ويُ rights workflow لل licensed voices — لل media houses وcreators وedtech في MENA.</p>
      <p>المشكلة التي حلّتها: Dubbing Studio 2 كان يُ flatten diacritics؛ الإصدار 4 يُ dialect classifier دقيق، يُ benchmark +38% watch-time على dubbed tutorials سعودية، يُ glossary per brand (أسماء منتجات، مدن)، يُ human review queue RTL، يُ API لـ CMS وLMS، ويُ watermark-free exports لل subscribers Pro.</p>
      <p>القدرات الأساسية: Arabic multi-dialect dubbing; Lip-sync engine; Batch processing; Brand glossaries; Review workflows; API and LMS hooks.</p>
      <p>للمبدعين العرب: localization studios — «Dubbing Studio 4 Arabic channel pack in 4 days» لل channels 20–800 فيديو. من يُ deliver 8 packs/ربع بـ 2200–48000 دولار + maintenance 175–1280 دولار/شهر يبني «استوديو دبلجة AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من ElevenLabs Dubbing Studio 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة dubbing قناة (glossary، batch، QC، delivery):</strong> 3–10 أيام — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ فيديوهات جديدة وdialect tuning:</strong> — 175–1280 دولار/شهر.</li>
          <li><strong>حزم vertical (دورات، بودكast، إعلانات RTL):</strong> — 45–210 دولار/حزمة.</li>
          <li><strong>دورات «دبلجة محتوى احترافية بـ ElevenLabs بالعربية»:</strong> — 52–235 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">ElevenLabs</span>
        <span class="tag">Dubbing</span>
        <span class="tag">Video</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Make.com AI Agents 4 Arabic: أتمتة ذكية — من «اربط WhatsApp بـ CRM» إلى scenario يعمل!</h2>
      <p class="article-lead">«كل lead من Instagram يدويًا في Excel — والفريق ينام 4 ساعات». في 23 أكتوبر 2026، أطلقت <strong>Make.com</strong> <strong>AI Agents 4 Arabic</strong>: layer فوق scenarios يُ understand natural language بالعربية، يُ design multi-step automations (webhooks، OpenAI، HubSpot، Shopify، WhatsApp Business)، يُ debug failed runs مع fix suggestions RTL، يُ generate data mappers JSON، يُ schedule وmonitor SLA، يُ template library (lead routing، invoice reminders، support triage)، ويُ enterprise vault لل secrets — لل agencies وSMEs في MENA.</p>
      <p>المشكلة التي حلّتها: AI Agents beta كان يُ over-connect modules؛ الإصدار 4 يُ constraint planner، يُ benchmark −52% time-to-first automation في logistics startup إماراتي، يُ cost estimator per operation، يُ version diff لل scenarios، يُ SSO وaudit logs، ويشارك read-only links لل clients.</p>
      <p>القدرات الأساسية: Arabic automation design; Multi-app orchestration; Debug copilot; Template marketplace; Monitoring and SLA; Enterprise security.</p>
      <p>للمبدعين العرب: automation consultants — «AI Agents 4 Arabic ops stack in 5 days» لل companies 5–200 employees. من يُ onboard 11 clients/ربع بـ 1900–42000 دولار + retainer 150–1100 دولار/شهر يبني «مكتب Make عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Make.com AI Agents 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة automation (discovery، scenarios، testing، handoff):</strong> 4–12 يومًا — 1900–42000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وnew flows:</strong> — 150–1100 دولار/شهر.</li>
          <li><strong>Industry scenario packs (e-commerce، clinics، HR RTL):</strong> — 40–185 دولار/pack.</li>
          <li><strong>دورات «أتمتة أعمال ذكية بـ Make AI بالعربية»:</strong> — 48–220 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Make.com</span>
        <span class="tag">Automation</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Ops</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>HubSpot Breeze AI 4 Arabic: CRM يفكر — deals، emails، وreports بلهجة فريقك!</h2>
      <p class="article-lead">«500 contact — ولا أحد يعرف من جاهز للشراء». في 23 أكتوبر 2026، أطلقت <strong>HubSpot</strong> <strong>Breeze AI 4 Arabic</strong>: suite داخل CRM تُ score leads بالعربية من emails وcalls notes، تُ draft follow-ups Gulf/Egyptian/MSA، تُ summarize deal rooms وmeeting transcripts RTL، تُ build dashboards من سؤال «ما أفضل vertical هذا الربع؟»، تُ suggest sequences وplaybooks، تُ sync Marketing Hub وService Hub، ويُ compliance GDPR وlocal data residency options — لل B2B sales teams في MENA.</p>
      <p>المشكلة التي حلّتها: Breeze 1 كان يُ generic Arabic؛ الإصدار 4 يُ tone learning per workspace، يُ benchmark +27% reply rate على outbound سعودي، يُ objection handling snippets، يُ forecast copilot، يُحوّل mobile voice notes إلى structured CRM fields، وتكامل Salesforce bi-directional optional.</p>
      <p>القدرات الأساسية: Arabic sales copilot; Lead scoring; Email and sequence drafts; Meeting summaries; Natural language reporting; Hub integrations.</p>
      <p>للمبدعين العرب: RevOps freelancers — «Breeze AI 4 Arabic CRM tune-up in 6 days» لل teams 3–80 reps. من يُ implement 9 hubs/ربع بـ 2100–45000 دولار + optimization 165–1250 دولار/شهر يبني «شريك HubSpot AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من HubSpot Breeze AI 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة CRM AI (data cleanup، Breeze setup، sequences، training):</strong> 5–14 يومًا — 2100–45000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ scoring tuning وcontent refresh:</strong> — 165–1250 دولار/شهر.</li>
          <li><strong>Vertical playbooks (SaaS، logistics، education RTL):</strong> — 42–198 دولار/playbook.</li>
          <li><strong>دورات «مبيعات ذكية بـ HubSpot Breeze بالعربية»:</strong> — 55–245 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">HubSpot</span>
        <span class="tag">Breeze AI</span>
        <span class="tag">CRM</span>
        <span class="tag">Sales</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Runway Gen-4 Arabic: فيديو إعلاني — من نص عربي إلى مشهد سينمائي في ساعات!</h2>
      <p class="article-lead">«الحملة Ramadan تبدأ الأسبوع القادم — والمخرج مشغول». في 23 أكتوبر 2026، أطلقت <strong>Runway</strong> <strong>Gen-4 Arabic</strong>: video generation يُ parse briefs بالعربية (منتج، mood، CTA)، يُ storyboard frames RTL-aware، يُ generate 4K clips مع consistent characters، يُ extend scenes وcamera moves، يُ audio bed suggestions، يُ brand safety filters، يُ export ProRes وsocial crops، ويُ team workspaces لل agencies — لل brands وproduction houses في الخليج ومصر.</p>
      <p>المشكلة التي حلّتها: Gen-3 كان يُ distort Arabic signage؛ الإصدار 4 يُ typography-safe regions، يُ benchmark −60% pre-production cost في FMCG teaser إماراتي، يُ reference image lock، يُ lip-sync لل Arabic VO optional، يُ API batch لل media buyers، ويُ rights metadata per asset.</p>
      <p>القدرات الأساسية: Arabic brief-to-video; Character consistency; Scene extension; Brand safety; Multi-format export; Agency workspaces.</p>
      <p>للمبدعين العرب: creative agencies — «Gen-4 Arabic campaign kit in 3 days» لل launches وseasonal ads. من يُ ship 12 kits/ربع بـ 2400–52000 دولار + retainer 180–1350 دولار/شهر يبني «استوديو Runway عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Runway Gen-4 Arabic؟</h3>
        <ul>
          <li><strong>باقة video campaign (brief، Gen-4، edits، deliverables):</strong> 2–8 أيام — 2400–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ variants وA/B creatives:</strong> — 180–1350 دولار/شهر.</li>
          <li><strong>Sector visual kits (F&amp;B، fintech، tourism RTL):</strong> — 50–228 دولار/kit.</li>
          <li><strong>دورات «إعلانات فيdeo بـ Runway Gen-4 بالعربية»:</strong> — 58–265 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Runway</span>
        <span class="tag">Gen-4</span>
        <span class="tag">Video AI</span>
        <span class="tag">Advertising</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 23-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="23-10-2026 -- 12-AM.html">
          📰 23 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "23-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/23-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/22-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/23-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
        "يبni",
        " y\u0650u",
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
