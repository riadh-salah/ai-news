#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 25-10-2026 -- 12-AM.html with proper UTF-8 encoding."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "25-10-2026 -- 12-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

TOPICS = (
    "Microsoft Power Automate Copilot 4 Arabic · Google Gemini for Workspace 4 Arabic · "
    "Notion AI Meeting Notes 4 Arabic · Canva Visual Suite 6 Arabic"
)

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Power Automate Copilot 4 Arabic، Google Gemini for Workspace 4 Arabic، Notion AI Meeting Notes 4 Arabic، Canva Visual Suite 6 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 25 أكتوبر 2026 | 12 منتصف الليل</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🌙 نشرة AI العالمية</span>
      <h1>من Microsoft Power Automate Copilot 4 Arabic الذي يُحوّل «وافق على الإجازة ثم أرسل لـ HR» إلى flow كامل على Teams وSharePoint قبل أن تُطفأ شاشة المكتب، إلى Google Gemini for Workspace 4 Arabic الذي يُلخّص Gmail وDocs وSheets وMeetings بلسان مدير عربي، ومن Notion AI Meeting Notes 4 Arabic الذي يُحوّل تسجيل Zoom إلى tasks وwiki وdecisions دون فقدان سياق، إلى Canva Visual Suite 6 Arabic الذي يُ birth حملة RTL كاملة — فيديو، posts، وpresentations — من brief واحد — أربع قصص ليلية في 25 أكتوبر 2026 لمن يريد أدوات عالمية ودخلًا يُضيء منتصف الليل!</h1>
      <p class="hero-sub">ليلة للأتمتة والإنتاجية والمعرفة والإبداع: موظفون يغرقون في موافقات يدوية، executives يفتحون عشر تبويبات لقرار واحد، فرق remote تضيع action items بعد كل call، ووكالات تُ rebuild assets لكل منصة. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 25 أكتوبر 2026</span>
        <span>🌙 12 منتصف الليل (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Power Automate Copilot 4 Arabic: أتمتة تُسمعك — flows، approvals، وRPA من جملة عربية!</h2>
      <p class="article-lead">«كل طلب شراء يمر بـ 6 emails — والـ CFO ينتظر أسبوعًا». في 25 أكتوبر 2026، أطلقت <strong>Microsoft</strong> <strong>Power Automate Copilot 4 Arabic</strong>: copilot يُ build cloud flows وdesktop flows من natural language عربي (MSA، Gulf، Levantine)، يُ wire Teams وOutlook وSharePoint وDynamics وSAP connectors، يُ suggest error handling وretries، يُ generate documentation RTL، يُ test sandbox قبل production، يُ compliance templates للقطاعات المنظّمة، ويُ Copilot Studio handoff لل agents — لل IT وops وHR في enterprises وSMB MENA.</p>
      <p>المشكلة التي حلّتها: Copilot 3 كان يُ break على multi-branch Arabic؛ الإصدار 4 يُ intent graph محسّن، يُ benchmark −48% time-to-first-flow في bank shared services الرياض، يُ process mining suggestions من Power BI، يُ DLP-aware variable handling، يُ Arabic error messages مع fix hints، ويُ partner pack لل SIs العرب.</p>
      <p>القدرات الأساسية: Arabic flow copilot; Cloud and desktop RPA; Connector orchestration; Test and document RTL; Compliance templates; Copilot Studio bridge.</p>
      <p>للمبدعين العرب: automation boutiques — «Power Automate Copilot 4 Arabic approval factory in 6 days» لل orgs 100–8000 users. من يُ ship 14 factories/ربع بـ 1800–52000 دولار + care 140–1100 دولار/شهر يبني «مكتب Power Automate AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Power Automate Copilot 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة factory (discovery، flows، tests، training):</strong> 4–12 يومًا — 1800–52000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ monitoring وflows جديدة:</strong> — 140–1100 دولار/شهر.</li>
          <li><strong>Vertical kits (HR، procurement، finance RTL):</strong> — 55–265 دولار/kit.</li>
          <li><strong>دورات «أتمتة مؤسسية بـ Power Automate Copilot بالعربية»:</strong> — 42–198 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Power Automate</span>
        <span class="tag">RPA</span>
        <span class="tag">Automation</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Google Gemini for Workspace 4 Arabic: مكتبك يُفهمك — Gmail، Docs، Sheets، وMeet بلسان واحد!</h2>
      <p class="article-lead">«200 email غير مقروء — واجتماع board بعد ساعتين». في 25 أكتوبر 2026، أطلقت <strong>Google</strong> <strong>Gemini for Workspace 4 Arabic</strong>: assistant موحّد داخل Gmail وDocs وSheets وSlides وMeet وChat يُ summarize threads ويُ draft replies بلهجة فريقك، يُ analyze spreadsheets ويُ explain variances بالعربية، يُ build decks من outline RTL، يُ live notes وaction items في Meet مع speaker attribution، يُ search Drive وChat بـ grounded answers، يُ admin controls وDLP — لل teams على Google Workspace في MENA وEU.</p>
      <p>المشكلة التي حلّتها: Gemini Workspace 3 كان يُ mix dialects في replies؛ الإصدار 4 يُ tone lock per domain، يُ benchmark −39% inbox triage time في consulting firm دبي، يُ cross-app workflows («من هذا email أنشئ Sheet وارسل للقناة»)، يُ citation chips لكل claim، يُ Gemini side panel في mobile RTL، ويُ Vault retention aware.</p>
      <p>القدرات الأساسية: Arabic Workspace copilot; Email and doc drafting; Sheet analysis RTL; Meet notes and actions; Grounded search; Enterprise DLP.</p>
      <p>للمبدعين العرب: productivity consultancies — «Gemini for Workspace 4 Arabic rollout in 8 days» لل orgs 50–5000 seats. من يُ onboard 10 rollouts/ربع بـ 2200–48000 دولار + adoption 160–1250 دولار/شهر يبني «غرفة Gemini Workspace عربية».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Google Gemini for Workspace 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة rollout (policies، prompts، training، champions):</strong> 5–14 يومًا — 2200–48000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ adoption وuse-case expansion:</strong> — 160–1250 دولار/شهر.</li>
          <li><strong>Department playbooks (sales، legal، PMO RTL):</strong> — 48–228 دولار/playbook.</li>
          <li><strong>دورات «إنتاجية ذكية بـ Gemini Workspace بالعربية»:</strong> — 38–182 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Google</span>
        <span class="tag">Gemini</span>
        <span class="tag">Workspace</span>
        <span class="tag">Productivity</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Notion AI Meeting Notes 4 Arabic: اجتماعات تُ write نفسها — transcript، tasks، وwiki!</h2>
      <p class="article-lead">«انتهى الـ standup — ولا أحد يتذكر من يملك ماذا». في 25 أكتوبر 2026، أطلقت <strong>Notion</strong> <strong>AI Meeting Notes 4 Arabic</strong>: pipeline يُ ingest Zoom وTeams وGoogle Meet recordings، يُ transcribe Arabic multi-dialect مع diarization، يُ extract decisions وowners وdue dates، يُ push tasks إلى databases وprojects، يُ link related wiki pages وOKRs، يُ generate follow-up emails RTL، يُ highlight risks وopen questions، يُ search past meetings semantically — لل remote teams وagencies وproduct squads 10–2000 members.</p>
      <p>المشكلة التي حلّتها: Meeting Notes 3 كان يُ duplicate tasks؛ الإصدار 4 يُ dedupe across workspace، يُ benchmark −52% «meeting aftermath» hours في SaaS startup القاهرة، يُ template packs (sales، retro، board)، يُ privacy redaction لل PII، يُ export to Linear وJira optional، ويُ SOC2 controls.</p>
      <p>القدرات الأساسية: Arabic meeting transcription; Action and decision extraction; Wiki and task sync; Follow-up drafts RTL; Semantic meeting search; Integrations.</p>
      <p>للمبدعين العرب: ops freelancers — «Meeting Notes 4 Arabic knowledge loop in 5 days» لل teams 15–500 users. من يُ deploy 18 loops/ربع بـ 950–32000 دولار + tuning 78–620 دولار/شهر يبني «استوديو Notion AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Notion AI Meeting Notes 4 Arabic؟</h3>
        <ul>
          <li><strong>باقة loop (templates، databases، training، integrations):</strong> 3–10 أيام — 950–32000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ templates وquality review:</strong> — 78–620 دولار/شهر.</li>
          <li><strong>Meeting type packs (board، sales، engineering RTL):</strong> — 40–190 دولار/pack.</li>
          <li><strong>دورات «اجتماعات ذكية بـ Notion AI بالعربية»:</strong> — 34–162 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Notion</span>
        <span class="tag">Meeting AI</span>
        <span class="tag">Knowledge</span>
        <span class="tag">Remote</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Canva Visual Suite 6 Arabic: حملة واحدة — فيديو، social، print، وpresentations RTL!</h2>
      <p class="article-lead">«العميل يريد Reels وLinkedIn وbillboard — والموعد غدًا». في 25 أكتوبر 2026، أطلقت <strong>Canva</strong> <strong>Visual Suite 6 Arabic</strong>: suite موحّدة يُ ingest brand kit وcampaign brief عربي، يُ generate video shorts وcarousel وPDF ads وpitch decks متسقة، يُ Magic Resize لكل منصة MENA، يُ translate copy EN↔AR مع tone control، يُ client approval links وcomments، يُ Brand Guardrails لل fonts وcolors، يُ analytics per asset — لل agencies وD2C وpersonal brands في الخليج ومصر والمغرب.</p>
      <p>المشكلة التي حلّتها: Visual Suite 5 كان يُ drift colors بين formats؛ الإصدار 6 يُ locked design tokens، يُ benchmark +29% faster campaign ship في agency الكويت، يُ AI video B-roll من stock MENA، يُ bulk export لل print vendors، يُ team libraries shared، ويُ enterprise SSO.</p>
      <p>القدرات الأساسية: Arabic campaign generation; Multi-format visual suite; Brand guardrails; Approvals; Localization; Analytics.</p>
      <p>للمبدعين العرب: creative studios — «Visual Suite 6 Arabic 360° campaign in 4 days» لل brands 20K–3M followers. من يُ deliver 22 campaigns/ربع بـ 1100–38000 دولار + retainer 88–720 دولار/شهر يبني «استوديو Canva AI عربي».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Canva Visual Suite 6 Arabic؟</h3>
        <ul>
          <li><strong>باقة 360° (brief، assets، approvals، handoff):</strong> 3–9 أيام — 1100–38000 دولار/عميل.</li>
          <li><strong>تشغيل شهري لـ campaigns وbrand refresh:</strong> — 88–720 دولار/شهر.</li>
          <li><strong>Industry packs (F&amp;B، fashion، fintech RTL):</strong> — 46–218 دولار/pack.</li>
          <li><strong>دورات «حملات بصرية بـ Canva Visual Suite بالعربية»:</strong> — 36–172 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Canva</span>
        <span class="tag">Visual Suite</span>
        <span class="tag">Creative</span>
        <span class="tag">Marketing</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 25-10-2026 -- 12-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = f"""      <li>
        <a href="25-10-2026 -- 12-AM.html">
          📰 25 أكتوبر 2026 — 12 منتصف الليل (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">{TOPICS}</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "25-10-2026 -- 12-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    new = "news/25-10-2026 -- 12-AM.html"
    content = README.read_text(encoding="utf-8")
    old_marker = "news/24-10-2026 -- 04-PM.html"
    new_line = (
        f"- [`{new}`](news/25-10-2026%20--%2012-AM.html) — أحدث إصدار ({TOPICS}) "
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
