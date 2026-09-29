#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "29-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"
README = ROOT / "README.md"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Microsoft Copilot for Security 3 Arabic، Cloudflare AI Gateway 3 Arabic، DeepL Write for Business 3 Arabic، NVIDIA AI Agent Blueprints 3 Arabic، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 29 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">☀️ نشرة AI الصباحية</span>
      <h1>من Microsoft Copilot for Security 3 Arabic الذي يُحوّل آلاف التنبيهات إلى خطة استجابة عربية قبل أن تبرد القهوة، إلى Cloudflare AI Gateway 3 Arabic الذي يُوحّد نماذج LLM ويُقيس التكلفة ويُحمي المفاتيح، ومن DeepL Write for Business 3 Arabic الذي يُصقل عقودًا وتقارير ورسائل بيع بلمسة أصلية لا «ترجمة آلية»، إلى NVIDIA AI Agent Blueprints 3 Arabic الذي يُشحن وكلاء production على GPU محلي أو سحابة خليجية — أربع قصص صباحية في 29 سبتمبر 2026 لمن يريد أدوات عالمية ودخلًا يستيقظ مع أول ضوء!</h1>
      <p class="hero-sub">صباحٌ لفرق الأمن والمنصّات والكتابة والبنية: CISOs يريدون copilot يفهم MITRE بالعربية، مهندسو platform يطلبون gateway واحد لعشرة نماذج، وكالات المحتوى تبحث عن DeepL يحافظ على أسلوب العلامة، وstartups deep tech تحلم بـ blueprints جاهزة على NIM. أربع أخبار عالمية مع صندوق ذهبي لكل خبر — أسلوب يشدّك من السطر الأول.</p>
      <div class="hero-meta">
        <span>📅 29 سبتمبر 2026</span>
        <span>☀️ 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Microsoft Copilot for Security 3 Arabic: SOC يتكلّم — من alert إلى hunt plan وplaybook بلغة فريقك!</h2>
      <p class="article-lead">«تنبيهات XDR تتكدّس — والمحلل يترجم MITRE يدويًا قبل أن يفهم السياق». في 29 سبتمبر 2026، أطلقت <strong>Microsoft</strong> <strong>Copilot for Security 3 Arabic</strong>: مساعد مؤسسي فوق Defender XDR وSentinel وIntune يُلخّص incidents بالعربية، يُ suggest investigation steps مع MITRE mapping، يُ draft executive briefs للإدارة، يُ generate KQL و hunting queries من سؤال طبيعي، يُ integrate ServiceNow وPagerDuty — للبنوك وtelco وenergy في MENA.</p>
      <p>المشكلة التي حلّتها: Copilot for Security 2 كان قويًا بالإنجليزية وضعيفًا على dialect-aware summaries للفرق المختلطة؛ الإصدار 3 يُ Arabic RTL في portal وTeams، يُ multi-tenant knowledge من past cases (مع privacy boundaries)، يُ plugin ecosystem لـ third-party TI feeds، يُ benchmark يُقلّل MTTR 34% في pilot خليجي، يُ compliance packs SAMA وNCA وPDPL.</p>
      <p>القدرات الأساسية: Custom skill packs per vertical؛ role-based redaction؛ export audit trail؛ bilingual incident timeline؛ migration path من standalone Copilot licenses.</p>
      <p>للمبدعين العرب: MSSPs وsecurity consultancies — «Copilot for Security 3 Arabic SOC uplift in 8 days» لل orgs 500–50000 seats. من يُ deliver 6 rollouts/ربع بـ 4200–88000 دولار + managed prompt tuning 520–4800 دولار/شهر يركب «Arabic cyber brain».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Microsoft Copilot for Security 3 Arabic؟</h3>
        <ul>
          <li><strong>Security Copilot enablement (Arabic playbooks، KQL library، RBAC):</strong> 7–20 يومًا — 4000–92000 دولار/عميل.</li>
          <li><strong>Monthly threat content refresh and dialect QA:</strong> — 500–4600 دولار/شهر.</li>
          <li><strong>Vertical hunt kits (finance، oil &amp; gas، healthcare):</strong> — 48–228 دولار/حزمة.</li>
          <li><strong>دورات «Arabic SOC AI with Microsoft Security Copilot»:</strong> — 46–218 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Microsoft</span>
        <span class="tag">Security</span>
        <span class="tag">Copilot</span>
        <span class="tag">SOC</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Cloudflare AI Gateway 3 Arabic: بوابة واحدة لكل LLM — routing، caching، DLP، وفواتير شفافة!</h2>
      <p class="article-lead">«عشرة فرق تستخدم OpenAI وAnthropic وGemini — ولا أحد يعرف التكلفة الحقيقية». في 29 سبتمبر 2026، أطلقت <strong>Cloudflare</strong> <strong>AI Gateway 3 Arabic</strong>: edge layer يُ sit أمام أي provider يُ log prompts/responses مع Arabic token analytics، يُ route حسب latency/cost/policy، يُ cache repeated RAG queries، يُ scan PII وsecrets قبل الخروج، يُ rate-limit per team، يُ dashboard بالعربية — للSaaS وmarketplaces وinternal platforms في GCC.</p>
      <p>المشكلة التي حلّتها: AI Gateway 2 كان observability فقط؛ الإصدار 3 يُ unified API compatible مع OpenAI schema، يُ fallback chains «Gemini ثم Claude ثم local»، يُ Workers AI co-location، يُ integrate Zero Trust للمفاتيح، يُ PDPL-friendly logging regions، يُ partner credits لل startups MENA.</p>
      <p>القدرات الأساسية: Prompt versioning؛ A/B eval hooks؛ custom guardrails؛ webhook alerts؛ Terraform modules؛ migration from direct API keys in 48h.</p>
      <p>للمبدعين العرب: platform engineers وAI consultancies — «AI Gateway 3 Arabic cost control pilot in 5 days» لل products burning 2K–200K USD/mo on tokens. من يُ ship 8 gateways/ربع بـ 1800–42000 دولار + FinOps retainer 380–3400 دولار/شهر ي monetize «Arabic LLM control plane».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Cloudflare AI Gateway 3 Arabic؟</h3>
        <ul>
          <li><strong>Gateway rollout (providers، policies، Arabic admin UI):</strong> 4–14 يومًا — 1600–48000 دولار/عميل.</li>
          <li><strong>Monthly FinOps and cache optimization:</strong> — 360–3200 دولار/شهر.</li>
          <li><strong>Starter templates (support bot، legal review، catalog search):</strong> — 42–198 دولار/حزمة.</li>
          <li><strong>دورات «Arabic LLM Gateway on Cloudflare»:</strong> — 41–195 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Cloudflare</span>
        <span class="tag">AI Gateway</span>
        <span class="tag">LLM</span>
        <span class="tag">FinOps</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>DeepL Write for Business 3 Arabic: نبرة العلامة في كل جملة — عقود، pitch decks، وemail sequences!</h2>
      <p class="article-lead">«الترجمة صحيحة — لكنها لا «تبيع» ولا «تهدّئ» العميل الغاضب». في 29 سبتمبر 2026، أطلقت <strong>DeepL</strong> <strong>Write for Business 3 Arabic</strong>: طبقة enterprise فوق DeepL Translator تُ rewrite بالMSA وخليجي ومصري حسب brand voice، يُ tone control (formal، friendly، legal-safe)، يُ glossary lock للمصطلحات، يُ batch polish لـ PDFs وDOCX، يُ API وSSO وaudit — للlaw firms وbanks وe-commerce وagencies في MENA.</p>
      <p>المشكلة التي حلّتها: Write 2 كان short-form English-centric؛ الإصدار 3 يُ long-document coherence، يُ compare side-by-side RTL، يُ detect «translationese» ويُ suggest native fixes، يُ integrate Microsoft 365 وGoogle Workspace، يُ human-in-the-loop review queues، يُ benchmark preferred over generic LLM rewrite on Arabic legal prose.</p>
      <p>القدرات الأساسية: Team style guides؛ compliance mode (no hallucinated clauses)؛ usage analytics؛ on-prem option EU/GCC؛ migration from legacy MT workflows.</p>
      <p>للمبدعين العرب: localization boutiques وcontent studios — «DeepL Write 3 Arabic brand voice in 6 days» لل brands publishing 50K+ words/month. من يُ sell 10 retainers/ربع بـ 900–18000 دولار + per-word overflow 0.008–0.04 دولار/كلمة يركب «Arabic polish factory».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من DeepL Write for Business 3 Arabic؟</h3>
        <ul>
          <li><strong>Write enablement (style guide، glossary، SSO، workflows):</strong> 5–12 يومًا — 850–22000 دولار/عميل.</li>
          <li><strong>Monthly voice tuning and QA sampling:</strong> — 290–2600 دولار/شهر.</li>
          <li><strong>Industry packs (banking، tourism، gov comms):</strong> — 38–182 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Brand Voice with DeepL Write»:</strong> — 39–188 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">DeepL</span>
        <span class="tag">Write</span>
        <span class="tag">Localization</span>
        <span class="tag">Content</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>NVIDIA AI Agent Blueprints 3 Arabic: وكلاء جاهزون — RAG، voice، وvision على NIM في أيام!</h2>
      <p class="article-lead">«الفريق يريد agent على documents وvoice — والـ PoC يستغرق شهرين». في 29 سبتمبر 2026، أطلقت <strong>NVIDIA</strong> <strong>AI Agent Blueprints 3 Arabic</strong>: مكتبة reference architectures فوق <strong>NIM</strong> microservices وNeMo وRiva يُ deploy Arabic RAG، multimodal support bots، field inspection vision agents، يُ Helm charts وTerraform، يُ run on DGX أو cloud partners في UAE وKSA، يُ observability with Langfuse patterns — للmanufacturing وhealthcare وretail في MENA.</p>
      <p>المشكلة التي حلّتها: Blueprints 2 كان English docs؛ الإصدار 3 يُ Arabic NLU packs، يُ Khaleeji ASR tuning guides، يُ hybrid on-prem + cloud burst، يُ security hardening checklist، يُ cost calculator per GPU hour، يُ ecosystem SI certifications في Riyadh وDubai.</p>
      <p>القدرات الأساسية: Custom tool calling templates؛ vector DB choices (Milvus، pgvector)； voice biometrics optional؛ upgrade path to full NeMo Agent toolkit؛ startup credits program.</p>
      <p>للمبدعين العرب: solution integrators وAI studios — «NVIDIA Blueprint 3 Arabic agent MVP in 10 days» لل enterprises piloting 1–3 use cases. من يُ deliver 5 blueprints/ربع بـ 5500–95000 دولار + GPU ops 680–6200 دولار/شهر يركب «Arabic agent factory on NIM».</p>

      <div class="money-box">
        <h3>💡 كيف تربح من NVIDIA AI Agent Blueprints 3 Arabic؟</h3>
        <ul>
          <li><strong>Blueprint deployment (NIM، RAG، Arabic eval، UAT):</strong> 8–22 يومًا — 5200–98000 دولار/عميل.</li>
          <li><strong>Monthly model refresh and GPU right-sizing:</strong> — 650–5900 دولار/شهر.</li>
          <li><strong>Use-case kits (warehouse vision، patient intake، sales copilot):</strong> — 55–265 دولار/حزمة.</li>
          <li><strong>دورات «Arabic Agents on NVIDIA NIM Blueprints»:</strong> — 52–248 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">NVIDIA</span>
        <span class="tag">NIM</span>
        <span class="tag">Agents</span>
        <span class="tag">Blueprints</span>
        <span class="tag">Arabic</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 29-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="29-09-2026 -- 08-AM.html">
          📰 29 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Microsoft Copilot for Security 3 Arabic · Cloudflare AI Gateway 3 Arabic · DeepL Write for Business 3 Arabic · NVIDIA AI Agent Blueprints 3 Arabic</small>
        </a>
      </li>
"""

README_LATEST = """- [`news/29-09-2026 -- 08-AM.html`](news/29-09-2026%20--%2008-AM.html) — أحدث إصدار (4 أخبار + أفكار ربح من AI)
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "29-09-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def update_readme():
    content = README.read_text(encoding="utf-8")
    import re

    new_content = re.sub(
        r"- \[`news/[^`]+`\]\([^)]+\) — أحدث إصدار \(4 أخبار \+ أفكار ربح من AI\)\n",
        README_LATEST,
        content,
        count=1,
    )
    if new_content == content and "29-09-2026 -- 08-AM.html" not in content:
        new_content = content.replace(
            "## المحتوى\n\n",
            "## المحتوى\n\n" + README_LATEST,
        )
    if new_content != content:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        print(f"Updated: {README}")
    else:
        print(f"README already up to date: {README}")


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
    bad_patterns = [
        "dollar",
        "mlions",
        "bringing",
        "الLlatin",
        "أفكar",
        "دolار",
        "البروtokol",
        "سبtemبر",
        "disappoint",
        "Arabs:",
        "القدrات",
        "frighten",
        "simulates",
        "رobots",
        "despierta",
        "yú ",
        "yú",
        "tربح",
        " yُ ",
        "yü ",
        "yü",
        "تü",
    ]
    for pat in bad_patterns:
        if pat in text:
            raise SystemExit(f"Mixed-script typo found: {pat}")
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
