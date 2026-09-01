#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 01-09-2026 -- 08-AM.html with proper UTF-8 encoding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "news" / "01-09-2026 -- 08-AM.html"
INDEX = ROOT / "news" / "index.html"

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="أحدث أخبار الذكاء الاصطناعي العالمية بالعربية — Hermes v0.21، AgentMinder، Dify New Agent، Revolte، وأفكار لتحقيق الدخل من AI">
  <title>أخبار الذكاء الاصطناعي — 1 سبتمبر 2026 | 08 صباحاً</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">

    <header class="hero">
      <span class="hero-badge">🔥 نشرة AI العالمية</span>
      <h1>من Pantheon Release يُحوّل وكلاء Hermes إلى مجتمع دردشة جماعي بذاكرة مستمرة، إلى AgentMinder الذي يُصادق كل tool call قبل أن يصل لمورد المؤسسة، ومن Dify New Agent الذي يُحوّل الوكيل إلى قدرة قابلة لإعادة الاستخدام عبر workflows، إلى Revolte الذي يُقود SDLC كاملاً بجلسات تفاعلية — أربع ثورات تُعيد تعريف multi-agent والحوكمة والبناء في 1 سبتمبر 2026!</h1>
      <p class="hero-sub">Hermes v0.21 يُطلق Bot Mode وhermes peer وcron jobs بذاكرة وMCP command center، Broadcom AgentMinder يُتحقق من هوية الوكيل ونية كل action في runtime، Dify يجعل Agent تطبيقاً مستقلاً بمصدر حقيقة واحد للـ prompt والskills، وRevolte يُخطّط ويُولّد ويُراجع ويُنشر عبر Interactive Sessions مع موافقة المهندس على القرارات الحاسمة. أربع قصص عالمية مع خريطة ذهبية للمبدعين العرب.</p>
      <div class="hero-meta">
        <span>📅 1 سبتمبر 2026</span>
        <span>🌅 08 صباحاً (UTC)</span>
        <span>📰 4 أخبار عالمية</span>
      </div>
    </header>

    <!-- المقال الأول -->
    <article class="article" id="article-1">
      <div class="article-number">الخبر الأول</div>
      <h2>Hermes Agent v0.21: Pantheon Release — Bot Mode يُحوّل وكلاءك إلى فريق دردشة جماعي بذاكرة وcron مستمر!</h2>
      <p class="article-lead">«v0.20.0 جعل Hermes رسولاً — v0.21.0 يُجمع الآلهة». في 31 أغسطس 2026، أطلقت <strong>Nous Research</strong> <strong>Hermes Agent v0.21.0</strong> — <strong>Pantheon Release</strong> يُحوّل multi-agent من plumbing تقني إلى تجربة Discord-style: وكلاء بأسماء ووجوه، group chats مشتركة، وDMs بين البوتات عبر <strong>hermes peer</strong>.</p>
      <p>المشكلة التي حلّتها: «multi-agent» كان يعني تكوين ملفات وgateways — لا تجربة فريق حقيقية. Bot Mode أصبح جزءاً مدمجاً في desktop app: كل profile يحصل على اسم وavatar deterministic، rooms بأسماء وصور، @-mention من composer، ومحادثات group حيث البوتات تتحدث مع بعضها ومعك. <strong>hermes peer</strong> يُمكّن أي وكيل من مراسلة آخر عبر handle — الردود تُحفظ في Bot Chat canonical، لا fire-and-forget.</p>
      <p>القدرات الأساسية: cron jobs بذاكرة persistent وcontinuity بين التشغيلات — briefing الساعة 9am يعرف ما قاله أمس؛ steer subagents mid-flight عبر delegate_task؛ MCP command center موحد مع health checks وتكلفة usage؛ الوكيل يقود in-app browser مباشرة؛ 6 providers جديدة (Meta Muse Spark، CommandCode، Nebius Token Factory وغيرها)؛ skills wave: competitor-news-monitor، email-inbox-triage، github-issue-to-pr. ~5800 commit و2475 merged PR منذ v0.20.0.</p>
      <p>للمبدعين العرب: كل agency وcommunity وfounder في MENA يريد «فريق وكلاء» لا toolbox — Hermes Bot Mode setup packages وArabic agent squad templates وmanaged multi-agent retainers فرصة automation premium. «Agent society as a product» vertical ينمو — Hermes v0.21 تُكافئ teams التي تُريد coworkers لا scripts.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Hermes v0.21 وثورة Bot Mode؟</h3>
        <ul>
          <li><strong>Hermes Bot Mode rollout packages:</strong> إعداد agent squads وgroup rooms للفرق — 2000–18000 دولار/فريق.</li>
          <li><strong>Multi-agent workflow design:</strong> تصميم hermes peer flows وcron routines — 1500–12000 دولار/workflow.</li>
          <li><strong>Managed agent society retainers:</strong> تشغيل وصيانة bot fleets شهرياً — 2500–22000 دولار/شهر.</li>
          <li><strong>دورات «Build Agent Teams with Hermes v0.21»:</strong> bootcamp للمطورين — 49–399 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Hermes Agent v0.21</span>
        <span class="tag">Bot Mode</span>
        <span class="tag">Multi-Agent</span>
        <span class="tag">Nous Research</span>
        <span class="tag">Open Source</span>
      </div>
    </article>

    <!-- المقال الثاني -->
    <article class="article" id="article-2">
      <div class="article-number">الخبر الثاني</div>
      <h2>Broadcom AgentMinder: مراقب حركة المؤسسة — يُصادق هوية كل وكيل ويُفوّض كل action قبل الوصول للبيانات!</h2>
      <p class="article-lead">«الوكلاء لم يعودوا يُولّدون محتوى — بل يُنفّذون عمليات». في 31 أغسطس 2026، خلال <strong>VMware Explore 2026</strong>، أعلنت <strong>Broadcom</strong> عن <strong>AgentMinder</strong> — <strong>traffic controller</strong> للوكلاء autonomous في المؤسسات: يُتحقق من الهوية ويُفوّض كل action مقابل mission وintent وcontext وrisk قبل أن يصل لمورد enterprise.</p>
      <p>المشكلة التي حلّتها: guardrails على model level وpermissions ثابتة لا تكفي عندما agent يصل للبيانات ويستدعي tools ويُكمل business processes. AgentMinder يُميّز بين من هو الوكيل، ماذا يحاول فعله، وما الذي يُسمح له بلمسه — ثلاثة محاور: agent identity verification، intent validation، runtime enforcement عبر cloud-native AI gateway يُصادق tokens ويوجّه traffic فقط لـ backends مُصرّح بها.</p>
      <p>القدرات الأساسية: policy engine ديناميكي يُقيّم context من user identity إلى intent؛ deployment مرن على VMware Kubernetes Service وGCP وKubernetes standards-based؛ multi-region active-active — Salesforce.com تشغّل AgentMinder على agentic pipeline مع ~36 مليون API call يومياً للعملاء و~7 مليون للقوى العاملة. Generally available اليوم على broadcom.com/agentminder.</p>
      <p>للمبدعين العرب: كل bank وtelco وenterprise في MENA تُطلق agents — AgentMinder integration packages وArabic agent governance SOPs وmanaged runtime-control retainers فرصة compliance premium. «Agent traffic controller» vertical ينمو مع agentic AI في production — AgentMinder تُكافئ orgs التي تُريد safety لا speed فقط.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من AgentMinder وثورة حوكمة الوكلاء المؤسسية؟</h3>
        <ul>
          <li><strong>AgentMinder integration packages:</strong> ربط gateway بـ agent stacks — 15000–120000 دولار/مؤسسة.</li>
          <li><strong>Agent governance consulting:</strong> policy design وintent validation — 8000–60000 دولار/audit.</li>
          <li><strong>Managed agent-security retainers:</strong> تشغيل runtime control شهرياً — 10000–80000 دولار/شهر.</li>
          <li><strong>دورات «Enterprise Agent Governance with AgentMinder»:</strong> bootcamp لفرق الأمن — 99–799 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">AgentMinder</span>
        <span class="tag">Broadcom</span>
        <span class="tag">Agent Governance</span>
        <span class="tag">Enterprise AI</span>
        <span class="tag">Runtime Control</span>
      </div>
    </article>

    <!-- المقال الثالث -->
    <article class="article" id="article-3">
      <div class="article-number">الخبر الثالث</div>
      <h2>Dify New Agent: وكيل مستقل قابل لإعادة الاستخدام — مصدر حقيقة واحد للـ prompt والskills عبر workflows!</h2>
      <p class="article-lead">«المشكلة ليست بناء وكيل واحد — بل إعادة استخدامه بأمان عبر المؤسسة». <strong>Dify</strong> أطلقت <strong>New Agent</strong> — <strong>standalone independent app</strong> أو reusable resource في workflow: كل agent له configuration وlifecycle خاص، تُبنى مرة وتُ refine وتُ publish كـ web app أو API أو تُ reuse عبر workflows متعددة.</p>
      <p>المشكلة التي حلّتها: نسخ agents عبر workflows تُنشئ duplicates — prompt وskills وtools settings تتفرّق وتصبح maintenance nightmare. Dify New Agent يُقدّم single source of truth: Agent page مركزي للبحث والإدارة بالstatus وcreator وupdate time؛ Agent Task في workflow nodes يُحدّد ماذا يفعل الوكيل في هذا السياق دون تعديل prompt core؛ architecture جديدة: Home Snapshots وWorkspaces وAgent Bindings وRuntime Leases — logical resources منفصلة عن physical backends (Local، E2B).</p>
      <p>القدرات الأساسية: Build — تحويل عمل حقيقي إلى reusable capability؛ Manage — agent واحد عبر workflows متعددة بclicks؛ Track — white-box observability عبر single-run tracing وlong-term monitoring؛ publish كـ web app أو API؛ flexible composition مع data processing وbusiness rules وhuman approval في نفس workflow. Agenton framework يُ orchestrate agent logic عبر LayerNode وgraph-based plan composition.</p>
      <p>للمبدعين العرب: كل enterprise وagency في MENA تبني agents متعددة — Dify agent library packages وArabic reusable-agent templates وmanaged agent-platform retainers فرصة platform premium. «One agent, many contexts» positioning ينمو — Dify New Agent تُكافئ teams التي تُريد governance وreuse لا copy-paste.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Dify New Agent وثورة الوكلاء القابلة لإعادة الاستخدام؟</h3>
        <ul>
          <li><strong>Dify agent library packages:</strong> بناء reusable agents للفرق — 3000–25000 دولار/مكتبة.</li>
          <li><strong>Agent platform architecture consulting:</strong> bindings وworkspaces design — 4000–30000 دولار/مشروع.</li>
          <li><strong>Managed Dify agent retainers:</strong> صيانة agents وworkflows شهرياً — 3500–28000 دولار/شهر.</li>
          <li><strong>دورات «Build Reusable Agents on Dify»:</strong> bootcamp لفرق المنتج — 59–449 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Dify New Agent</span>
        <span class="tag">Reusable Agents</span>
        <span class="tag">Agent Platform</span>
        <span class="tag">Workflow Automation</span>
        <span class="tag">Enterprise AI</span>
      </div>
    </article>

    <!-- المقال الرابع -->
    <article class="article" id="article-4">
      <div class="article-number">الخبر الرابع</div>
      <h2>Revolte Interactive Sessions: قُد SDLC كاملاً بجلسات AI تفاعلية — من intent إلى production بموافقة المهندس!</h2>
      <p class="article-lead">«الهندسة لا تحتاج agent يكتب أسطراً — بل agent يُنجز features كاملة ب governance». في 31 أغسطس 2026، أطلق <strong>Revolte</strong> على Product Hunt <strong>Interactive Sessions</strong> — <strong>SDLC platform</strong> للفرق الهندسية: agents تُخطّط وتُولّد وتُشغّل quality وsecurity checks وتُنشئ PRs وتُدعم deployment — والمهندس يُ approve القرارات الحاسمة.</p>
      <p>المشكلة التي حلّتها: coding agents تُسرّع typing لكن delivery pipeline يبقى fragmented — plan هنا، code هناك، review في مكان ثالث. Revolte يُحوّل intent إلى production-ready software step by step: agents plan changes، generate code، run quality/security checks، create PRs، support deployment، monitor runtime behavior، surface risks early — engineers approve important decisions، Revolte handles delivery heavy lifting.</p>
      <p>القدرات الأساسية: higher delivery throughput عبر SDLC كامل؛ stronger governance مع human-in-the-loop على القرارات؛ more value shipped per engineer؛ built for engineering teams لا solo vibe-coders؛ 265 upvote و85 comment على Product Hunt — engagement عالٍ يدل على pain point حقيقي. Use cases: feature delivery، security gates، deployment support، runtime monitoring في workspace واحد.</p>
      <p>للمبدعين العرب: كل software house وproduct team في MENA تُريد velocity مع control — Revolte session design packages وArabic SDLC agent SOPs وmanaged delivery retainers فرصة engineering-as-a-service premium. «Agentic SDLC with governance» vertical ينمو — Revolte تُكافئ teams التي تُريد throughput لا chaos.</p>

      <div class="money-box">
        <h3>💡 كيف تربح من Revolte وثورة الجلسات التفاعلية للـ SDLC؟</h3>
        <ul>
          <li><strong>Revolte team rollout packages:</strong> إعداد Interactive Sessions للفرق — 5000–40000 دولار/فريق.</li>
          <li><strong>Agentic SDLC consulting:</strong> governance gates وapproval flows — 4000–32000 دولار/مشروع.</li>
          <li><strong>Managed delivery retainers:</strong> تشغيل agent sessions شهرياً — 6000–45000 دولار/شهر.</li>
          <li><strong>دورات «Ship Features with Revolte Sessions»:</strong> bootcamp لفرق الهندسة — 79–549 دولار.</li>
        </ul>
      </div>

      <div class="tags">
        <span class="tag">Revolte</span>
        <span class="tag">Interactive Sessions</span>
        <span class="tag">Agentic SDLC</span>
        <span class="tag">Software Engineering</span>
        <span class="tag">Developer Tools</span>
      </div>
    </article>

    <footer class="site-footer">
      <p>نشرة أخبار الذكاء الاصطناعي العالمية — إصدار 01-09-2026 -- 08-AM</p>
      <p style="margin-top: 0.5rem;"><a href="index.html">← جميع الإصدارات</a></p>
    </footer>

  </div>

</body>
</html>
"""

INDEX_ENTRY = """      <li>
        <a href="01-09-2026 -- 08-AM.html">
          📰 1 سبتمبر 2026 — 08 صباحاً (UTC)
          <br>
          <small style="color: var(--text-muted); font-weight: 400;">Hermes v0.21 · AgentMinder · Dify New Agent · Revolte</small>
        </a>
      </li>
"""


def update_index():
    content = INDEX.read_text(encoding="utf-8")
    marker = '    <ul class="edition-list">\n'
    if "01-09-2026 -- 08-AM.html" not in content:
        content = content.replace(marker, marker + INDEX_ENTRY)
        with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated: {INDEX}")
    else:
        print(f"Index already contains entry: {INDEX}")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(HTML)
    print(f"Written: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    update_index()


if __name__ == "__main__":
    main()
