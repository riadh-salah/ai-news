#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 08-09-2026 -- 04-PM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "08-09-2026 -- 04-PM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Fuzzball 4.2 MCP لتشغيل HPC بالوكلاء، Outline وكيل CFO بـ 3 ملايين دولار، Gaia طبقة AI سيادية للمؤسسات السعودية، Sapiom بـ 35 مليون دولار لبنية agent rails، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 8 سبتمبر 2026 | 04 مساءً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Fuzzball 4.2 الذي يُمكّن أي وكيل MCP من إرسال ومراقبة مهام HPC دون queue ops، إلى Outline الذي يُحوّل Excel إلى وكيل CFO بـ 3 ملايين دولار، ومن Gaia — طبقة AI سيادية سعودية بـ 1.5 مليون دولار تحافظ على البيانات داخل المملكة، إلى Sapiom بـ 35 مليون دولار Series A لبناء «rails» تنفيذ الوكلاء — أربع ثورات تُعيد تشكيل البنية التحتية الحاسوبية والمالية والسيادية والتنفيذية في 8 سبتمبر 2026!</h1>
      <p class="hero-sub">CIQ تُسلّم Fuzzball 4.2 بـ MCP server أصلي لـ fine-tuning وbatch inference، Outline تجمع 3 ملايين دولار من Founders Future لوكيل CFO بـ 10 عملاء مدفوعين، Gaia تبني permission-aware search وagents للمؤسسات السعودية مع SEEDRA Ventures، وSapiom بقيادة Dragonfly تُموّل execution rails لـ «تريليون وكيل». أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 8 سبتمبر 2026</span>
        <span>🌆 04 مساءً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Fuzzball 4.2: أي وكيل MCP يُرسل ويراقب مهام HPC — fine-tuning وbatch inference بدون queue ops!</h2>
      <p class="article-lead">«الوكيل يحتاج GPU cluster — لكن ops team لا يرد قبل 48 ساعة». في 3 سبتمبر 2026، أطلقت <strong>CIQ</strong> <strong>Fuzzball 4.2</strong> مع <strong>MCP server أصلي</strong> — أي وكيل يتحدث Model Context Protocol (Claude، Cursor، أو أي أداة MCP-compatible) يستطيع الآن inspect وsubmit وmonitor مهام high-performance computing مباشرةً.</p>
      <p>المشكلة التي حلّتها: HPC compute تاريخياً inaccessible بدون معرفة Slurm وmodules وjob schedulers — حتى فرق ML تحتاج ops handoff لكل fine-tuning run. Fuzzball 4.2 يُغلق الفجوة: الوكيل يُرسل التشغيل، Fuzzball ينفّذه، والوكيل يراقبه حتى الاكتمال — كل ذلك عبر standard MCP tool calls.</p>
      <p>القدرات الأساسية: inspect ما يعمل على cluster، draft workflow definitions، submit jobs، monitor execution تحت operator-defined permissions؛ self-service credentials مُحقونة تلقائياً workflow-scoped — dynamic compute pipelines بدون secrets ثابتة؛ مع 78% من enterprise AI teams تُشغّل MCP agents في production (يوليو 2026) و6400+ server في registry — HPC أصبح first-class MCP endpoint لا dashboard button.</p>
      <p>للمبدعين العرب: كل AI lab وuniversity وfintech ML team في MENA يحتاج GPU access أسرع — Fuzzball MCP integration packages وArabic HPC agent playbooks وmanaged compute retainers فرصة MLOps premium. «Agentic HPC infrastructure» vertical ينمو — CIQ تُكافئ teams التي تُسلّم autonomous training pipelines لا ticket-chasing workflows.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Fuzzball 4.2 MCP وثورة HPC الوكيلية؟</h3>
        <ul>
          <li><strong>Fuzzball MCP integration packages:</strong> agent + cluster workflows — 6000–45000 دولار/مشروع.</li>
          <li><strong>HPC agent consulting:</strong> fine-tuning + batch inference automation — 4000–35000 دولار/عميل.</li>
          <li><strong>Managed compute agent retainers:</strong> job monitoring + cost optimization — 2500–22000 دولار/شهر.</li>
          <li><strong>دورات «Run HPC Jobs via MCP Agents»:</strong> bootcamp — 59–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Fuzzball 4.2</span>
        <span class="tag">CIQ</span>
        <span class="tag">MCP HPC</span>
        <span class="tag">Agentic Infrastructure</span>
        <span class="tag">Fine-Tuning</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Outline: 3 ملايين دولار لوكيل CFO يُستبدل Excel — 10 عملاء مدفوعين و10 آخرون في سبتمبر!</h2>
      <p class="article-lead">«الـ forecast في 47 spreadsheet — والـ board meeting بعد 3 أيام». في 8 سبتمبر 2026، أعلنت <strong>Outline</strong> — startup فرنسية بفريق من 3 أشخاص — عن <strong>3 ملايين دولار seed</strong> بقيادة <strong>Founders Future</strong>، لبناء <strong>AI agent للـ CFOs</strong> يُستبدل Excel forecasting بتحليلات وكيلية ذكية.</p>
      <p>المشكلة التي حلّتها: CFOs وfinance teams تقضي أسابيع في نماذج Excel متشعبة — تتغير assumptions يدوياً، تُنسى scenarios، ولا أحد يثق بالرقم النهائي. Outline يُقدّم وكيلاً يفهم business context، يُحدّث forecasts تلقائياً، ويُجيب على «ماذا لو» في محادثة طبيعية — لا pivot tables ولا macro hell.</p>
      <p>القدرات الأساسية: 10 paying customers عند الإعلان و10 additional expected في سبتمبر؛ angel investors من <strong>CEO Cegid</strong> و<strong>finance director Pennylane</strong> — إشارة قوية لـ product-market fit في European finance SaaS؛ فريق من alumni <strong>Alan</strong> و<strong>Spotify</strong> — خبرة scaling وproduct في markets عالية التنظيم.</p>
      <p>للمبدعين العرب: كل scale-up وfamily office وSME في MENA يعاني Excel finance chaos — Outline-inspired agent stacks وArabic FP&amp;A automation playbooks وmanaged CFO agent retainers فرصة finance premium. «Agentic FP&amp;A» vertical ينمو — Founders Future backing يُشير أن category definition بدأت الآن.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Outline وثورة وكيل CFO؟</h3>
        <ul>
          <li><strong>CFO agent stack packages:</strong> forecasting + scenario modeling — 5000–40000 دولار/مشروع.</li>
          <li><strong>FP&amp;A automation consulting:</strong> Excel migration + agent workflows — 3500–30000 دولار/عميل.</li>
          <li><strong>Managed finance agent retainers:</strong> monthly forecast updates + board prep — 2000–18000 دولار/شهر.</li>
          <li><strong>دورات «Build CFO Agents — Beyond Excel»:</strong> bootcamp — 49–249 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Outline</span>
        <span class="tag">AI Agent CFO</span>
        <span class="tag">Founders Future</span>
        <span class="tag">FP&amp;A Automation</span>
        <span class="tag">Seed Funding</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Gaia: 1.5 مليون دولار لطبقة AI سيادية سعودية — بياناتك تبقى داخل المملكة!</h2>
      <p class="article-lead">«الـ LLM يريد cloud أمريكي — لكن compliance يقول لا». في 8 سبتمبر 2026، أعلنت startup الرياض <strong>Gaia</strong> عن <strong>1.5 مليون دولار pre-seed</strong> بقيادة <strong>SEEDRA Ventures</strong> — لبناء <strong>permission-aware AI layer</strong> للمؤسسات السعودية، مع بيانات تُخزَّن وتُعالَج داخل المملكة أو on-premise بالكامل.</p>
      <p>المشكلة التي حلّتها: enterprise AI tools تُجبر الشركات على إرسال emails وfiles وbusiness systems إلى cloud خارجي — مخالف لـ data residency وsector regulations في السعودية. Gaia تربط internal files وemails وbusiness systems في طبقة AI واحدة: search عبرها، answers grounded في company data، وagents تُنفّذ tasks عبر applications — كل ذلك مع inherited access permissions.</p>
      <p>القدرات الأساسية: deployment في private cloud أو on-premise أو fully offline؛ data stored and processed inside Saudi؛ founders <strong>Badr Al-Malluh</strong> (CEO) و<strong>Mohammad Rababah</strong> (CPTO)؛ SEEDRA portfolio يشمل Tamara وZid وLucidya وZenHR — investor active في Saudi early-stage؛ already working with enterprises on operational use cases.</p>
      <p>للمبدعين العرب: Vision 2030 + data sovereignty = demand explosion — Gaia-style sovereign agent packages وArabic enterprise RAG playbooks وmanaged sovereign AI retainers فرصة enterprise premium في MENA. «Sovereign enterprise AI» vertical ينمو — SEEDRA backing يُسرّع adoption في Saudi corporates.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Gaia وثورة AI السيادية للمؤسسات؟</h3>
        <ul>
          <li><strong>Sovereign AI layer packages:</strong> on-premise RAG + agent deployment — 8000–60000 دولار/مشروع.</li>
          <li><strong>Enterprise AI residency consulting:</strong> compliance + permission-aware search — 5000–45000 دولار/عميل.</li>
          <li><strong>Managed sovereign AI retainers:</strong> internal knowledge + agent ops — 3500–28000 دولار/شهر.</li>
          <li><strong>دورات «Build Sovereign Enterprise AI for MENA»:</strong> bootcamp — 69–349 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Gaia</span>
        <span class="tag">SEEDRA Ventures</span>
        <span class="tag">Sovereign AI</span>
        <span class="tag">Saudi Enterprise</span>
        <span class="tag">Data Residency</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Sapiom: 35 مليون دولار Series A — Dragonfly تُموّل «rails» تنفيذ تريليون وكيل!</h2>
      <p class="article-lead">«الوكلاء كثيرة — لكن التنفيذ مكلف وبطيء». في 7 سبتمبر 2026، أعلنت <strong>Sapiom</strong> — منصة AI agent infrastructure — عن <strong>35 مليون دولار Series A</strong> بقيادة <strong>Dragonfly</strong>، لبناء execution rails تحت وكلاء الآخرين — picks-and-shovels play في عصر agentic AI.</p>
      <p>المشكلة التي حلّتها: كل startup تبني agents — لكن execution cost (latency، reliability، orchestration) يصبح binding constraint عند scale. Sapiom لا تُنافس على model layer؛ بل تُوفّر infrastructure layer: كيف ينفّذ agent actions بكفاءة، بأمان، وبcost predictable — «toll booth» على agent economy.</p>
      <p>القدرات الأساسية: Dragonfly thesis — execution cost = binding constraint وwhoever solves it early owns infrastructure؛ نفس الأسبوع: Wordsmith +14M legal AI extension (84M Series B tranche)، Ambrook 30M Series B لـ AI-native finance في agriculture/trucking — capital gravitates toward picks-and-shovels وclear labor-arbitrage stories؛ «trillion agents» framing aspirational لكن Series A size يُشير conviction حقيقية.</p>
      <p>للمبدعين العرب: كل AI agency وplatform builder في MENA يحتاج cheaper reliable execution — Sapiom-compatible agent architecture packages وArabic agent orchestration playbooks وmanaged agent infra retainers فرصة platform premium. «Agent execution infrastructure» vertical ينمو — Dragonfly backing يُشير أن category winner لم يُحدَّد بعد — window مفتوح للintegrators.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Sapiom وثورة agent execution rails؟</h3>
        <ul>
          <li><strong>Agent rails architecture packages:</strong> Sapiom integration + cost optimization — 7000–55000 دولار/مشروع.</li>
          <li><strong>Agent execution consulting:</strong> latency + reliability playbooks — 4500–40000 دولار/عميل.</li>
          <li><strong>Managed agent infra retainers:</strong> orchestration monitoring + scaling — 3000–25000 دولار/شهر.</li>
          <li><strong>دورات «Build on Agent Execution Rails»:</strong> bootcamp — 59–299 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Sapiom</span>
        <span class="tag">Dragonfly</span>
        <span class="tag">Agent Rails</span>
        <span class="tag">Series A</span>
        <span class="tag">Agent Infrastructure</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 08-09-2026 -- 04-PM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="08-09-2026 -- 04-PM.html">
          📰 8 سبتمبر 2026 — 04 مساءً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Fuzzball 4.2 MCP · Outline AI CFO · Gaia Sovereign AI · Sapiom Agent Rails</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "08-09-2026 -- 04-PM.html" not in content:
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
    bad_patterns = ["dollar", "mlions", "bringing", "الLlatin", "أفكar", "دolار"]
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
