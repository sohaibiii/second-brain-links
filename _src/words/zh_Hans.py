# -*- coding: utf-8 -*-
"""Simplified Chinese (zh-Hans). English is the fallback; k.* are the app's own labels."""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "支持",
"nav.about": "关于",
"nav.privacy": "隐私",
"nav.terms": "条款",
"nav.data": "你的数据",

"ui.skip": "跳至主要内容",
"ui.pages": "页面",
"ui.footer": "页脚",
"ui.lang": "语言",
"ui.toc": "本页内容",
"ui.rights": "保留所有权利。",
"ui.store_soon": "即将登陆 App Store",
"ui.store_get": "在 App Store 下载",
"ui.date": "2026年10月14日",
"ui.last_updated": "最后更新：{DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "本译文仅为方便阅读而提供。如与英文版本有任何不一致，以英文版本为准。",

# The app's own words, copied from SecondBrain/Localizable.xcstrings. Do not retranslate.
"k.settings": "设置",
"k.cloud_choices": "云端同步与 AI 选项",
"k.account": "你的账户",
"k.delete_account": "删除账户和资料库",
"k.keep_account": "保留账户",
"k.delete_local": "删除所有本地数据",
"k.export": "准备导出",
"k.share_export": "共享资料库导出文件",
"k.recently_deleted": "最近删除",
"k.delete_permanently": "永久删除",
"k.data_handled": "你的数据如何处理",
"k.privacy_screen": "你的隐私",
"k.sync": "同步我的资料库",
"k.sync_now": "立即同步",
"k.luna": "使用 Luna 整理和回答",
"k.on_device": "设备端 AI",
"k.language": "语言",
"k.restore": "恢复购买",
"k.manage": "管理订阅",
"k.sign_out": "退出登录并打开访客资料库",
"k.keep_recording": "保留这段录音",
"k.needs_review": "待确认",
"k.smart_org": "智能整理",
"k.smart_fill": "智能填写",
"k.quick": "快速模式",
"k.ask": "问问你的大脑",
"k.calendars": "连接“日历”App",
"k.morning": "晨间摘要",
"k.reminders": "提醒通知",
"k.spotlight": "在 Spotlight 中显示已保存的条目",
"k.device_only": "仅保留在这台 iPhone 上",
"k.undo": "撤销",
"k.widgets": "在小组件中显示标题",

"meta.support.title": "Second Brain — 支持",
"meta.support.desc": "Second Brain 官方支持：记录、智能填写和“问问你的大脑”如何运作，App 需要什么，常见问题解答，以及如何联系我们。",
"meta.about.title": "Second Brain — 只管说出来，我们来整理。",
"meta.about.desc": "Second Brain 会把你说的话或输入的文字变成任务、日程、笔记和灵感，保留你的原始记录，并根据你保存的内容回答问题，优先使用设备端 AI。",
"meta.privacy.title": "隐私政策 — Second Brain",
"meta.privacy.desc": "Second Brain 在你的设备上保存什么、什么会进入 iCloud、我们的服务器保存什么，以及你的文字究竟在何时会被发送给云端 AI。",
"meta.terms.title": "使用条款 — Second Brain",
"meta.terms.desc": "Second Brain 使用条款（EULA）：你的内容、AI 功能、云端额度，以及 Light 和 Pro 订阅如何计费。",
"meta.data.title": "删除你的数据 — Second Brain",
"meta.data.desc": "如何导出你的资料库、将它从这台设备上删除，以及删除你的 Second Brain 账户及其在 iCloud 和我们服务器上保存的全部内容。",
"meta.nf.title": "未找到页面 — Second Brain",
"meta.nf.desc": "未找到该页面。",

# --- support --------------------------------------------------------------
"s.eyebrow": "支持",
"s.h1": "Second Brain 使用帮助",
"s.sub": "说出来或打出来，Second Brain 就会把它整理成任务、日程、笔记和灵感，保留你的原始记录，而且任何更改都可以撤销。本页介绍它如何运作、需要什么，以及如何联系我们。",
"s.cta": "阅读常见问题",
"s.meta": '无需账户即可使用 · 优先使用设备端 AI · <a href="{BASE}{L}/privacy/">隐私政策</a>',

"s.how.h": "Second Brain 如何运作",
"s.how.b": """
<p class="lead">几秒钟就把脑中的事记下来，需要时再轻松找回。</p>
<p>点按麦克风，想到什么就说什么，也可以直接输入。Second Brain 会先一字不差地保存你的原话，因此什么都不会丢失。然后它会建议其中包含的内容：带截止日期的任务、带时间的日程、一条笔记或一个灵感，并归入合适的项目。在创建任何内容之前，你都会逐一检查每条建议，而且每项更改都可以撤销。</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>记录</b><span>语音记录一打开就会开始录音。你也可以直接输入，从其他 App 共享文字、链接、照片或文件，或者将它们附加到一条记录中。</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>智能填写与确认</b><span>点按“完成”，智能填写就会起草任务、日程、笔记和灵感，并填好日期和时间。在点按“创建”之前，每个字段都可以编辑。它不确定的内容会保持高亮，或进入{K_needs_review}。</span></div></li>
  <li><span class="tile">{chat}</span><div><b>问问你的大脑</b><span>用平常的话提一个问题。回答只来自你保存的内容，并会列出来源，方便你打开核对。</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>“今天”与“日历”</b><span>哪些事到期、接下来做什么、什么最重要，一目了然；另有周视图，把“日历”App 中的日程显示在你的任务旁边。还可选择开启提醒和晨间摘要。</span></div></li>
  <li><span class="tile">{undo}</span><div><b>原始记录，始终保留</b><span>你记录下的原话会留在资料库中，就在由它生成的内容旁边。使用{K_undo}可以还原任何整理操作，删除的条目会在{K_recently_deleted}中保留 30 天。</span></div></li>
  <li><span class="tile">{lock}</span><div><b>默认私密</b><span>如果你的设备支持，整理和回答都会在你的设备上通过 Apple 的设备端模型运行。云端同步和云端 AI 在你选择开启之前都保持关闭。请参阅<a href="{BASE}{L}/privacy/">隐私</a>。</span></div></li>
</ul>
""",

"s.requirements.h": "使用要求",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>设备</th><td>装有 <strong>iOS 18 或 iPadOS 18</strong> 或更高版本的 <strong>iPhone 或 iPad</strong>。</td></tr>
<tr><th>设备端 AI</th><td>支持 <strong>Apple Intelligence</strong> 的设备，运行 iOS 26 或 iPadOS 26 或更高版本，并已打开 Apple Intelligence 且下载了其模型。在其他设备上，你仍然可以记录、手动整理、搜索和设置提醒。届时，如果你登录并允许，智能填写和回答可以使用云端的 Luna。</td></tr>
<tr><th>账户</th><td><strong>可选。</strong>记录、整理、搜索、导出和删除都无需账户。购买 Light 或 Pro、通过 iCloud 同步、使用 Luna 或导入网页文字时，需要通过 Apple 登录。</td></tr>
<tr><th>网络</th><td>记录、设备端 AI、搜索和导出无需联网。登录、购买、iCloud 同步、Luna、网页导入，以及首次下载你所用语言的 Apple 语音文件时需要联网。</td></tr>
<tr><th>权限</th><td>语音记录需要麦克风和语音识别权限。仅在你附加图片时才需要相机或照片权限。仅在你连接“日历”App 时才需要日历权限。仅在使用提醒和晨间摘要时才需要通知权限。每项权限都会在你首次使用相应功能时询问。</td></tr>
<tr><th>iCloud</th><td>同步需要一个有足够可用空间的 iCloud 账户。Light 和 Pro 均包含同步功能。</td></tr>
<tr><th>语言</th><td>英语、德语、西班牙语、法语、日语、韩语、巴西葡萄牙语和简体中文。语音记录会使用 App 的语言进行识别。可在{K_settings} → {K_language}中选择。</td></tr>
</table></div>
""",

"s.start.h": "快速上手",
"s.start.b": """
<ol class="steps">
  <li><div><b>打开 Second Brain。</b>无需注册。从第一秒起，你的资料库就保存在你的设备上。</div></li>
  <li><div><b>点按麦克风，说出你在想的事。</b>iOS 询问时，请允许使用麦克风和语音识别。也可以直接输入。</div></li>
  <li><div><b>点按“完成”。</b>智能填写会起草任务、日程、笔记和灵感。检查每个字段，修改任何内容，然后点按“创建”。</div></li>
  <li><div><b>问问你的大脑。</b>问一句“我答应过 Sam 什么？”或“牙医预约是什么时候？”，然后打开引用的来源进行核对。</div></li>
  <li><div><b>可选：</b>如需通过 iCloud 同步或使用 Luna，请打开{K_settings} → {K_cloud_choices}，然后通过 Apple 登录。每项功能都有单独的开关。</div></li>
</ol>
""",

"s.faq.h": "常见问题",
"s.faq.b": """
<dl class="faq">
<dt>我需要账户吗？</dt>
<dd>不需要。记录、整理、搜索、提醒、导出和删除都无需账户，在你的设备上即可使用。只有在购买方案、通过 iCloud 同步、使用云端的 Luna 或导入网页文字时才需要账户。登录绝不会上传你现有的访客资料库。你可以自行选择要将哪些想法复制到账户中。</dd>
<dt>哪些功能是免费的？</dt>
<dd>文字记录、任务和项目、本地搜索、设备端转写、提醒、编辑、导出和删除均免费且不限次数。免费版每月还包含 <strong>5 次语音记录、3 次智能填写和 5 次{K_ask}提问</strong>，在每台设备上分别计数，并于每月 1 日重置。保存永远不会被阻止：达到限制后，你仍然可以输入并保存。已登录且允许云端 AI 的账户还可获得一次性体验：10 次云端 AI 记录和 5 次回答。</dd>
<dt>Light 和 Pro 增加了什么？</dt>
<dd><strong>Light</strong> 取消语音记录、智能填写和“问问你的大脑”的每月限制，增加{K_quick}和私密的 iCloud 同步，并且每月包含 300 次云端 AI 记录和 100 次云端回答。<strong>Pro</strong> 提供每月 700 次云端 AI 记录和 250 次云端回答、云端每日摘要，以及网页文字导入。Light 按月计费。Pro 可按月或按年计费，年付方案为符合条件的新订阅者提供 7 天免费试用。价格会按你所在的国家或地区显示在 App 内和 App Store 中，计费由 Apple 处理。</dd>
<dt>设备端 AI 和 Luna 有什么区别？</dt>
<dd>设备端 AI 是在你的设备上运行的 Apple 模型。你写下的任何内容都不会离开设备。Luna 是 OpenAI 提供的云端模型，通过我们的服务器运行。只有当你登录并打开{K_luna}时才会使用它，而且仅在你方案的云端额度内使用。设备端 AI 优先运行，当你的设备无法处理时，由 Luna 接手。Light 和 Pro 可以在{K_settings}中将 Luna 选为主要引擎。无论你选择哪个引擎，标记为{K_device_only}的记录都绝不会发送给 Luna。</dd>
<dt>{K_device_only}有什么作用？</dt>
<dd>该条记录以及由它生成的所有内容，都绝不会同步到 iCloud，也绝不会发送给云端 AI。设备端 AI 仍然可以整理它。</dd>
<dt>回答可信吗？</dt>
<dd>回答只根据你保存的内容生成，每个回答都会列出来源，方便你打开查看。但 AI 仍可能误读或遗漏信息，因此在重要事项上依赖某个回答之前，请先核对来源。</dd>
<dt>我的语音录音会怎样处理？</dt>
<dd>录音在你的设备上转写，不会为了转写而发送给 Apple 或我们。转写完成后，音频会在 7 天后删除，除非你点按{K_keep_recording}。如果转写失败，音频会一直保留到你删除为止，方便你重试。音频删除后，转写文本仍会保留。</dd>
<dt>可以在 iPhone 和 iPad 之间同步吗？</dt>
<dd>可以，需要 Light 或 Pro。在两台设备上登录同一个 Apple 账户，并打开{K_sync}。你的资料库会通过你自己的私密 iCloud 存储空间同步，我们无法读取。</dd>
<dt>订阅结束后会怎样？</dt>
<dd>你保存的内容都不会被删除。阅读、编辑、搜索、导出和删除仍可正常使用，免费版的每月限制会重新生效。同步和云端额度会停止，直到你再次订阅。</dd>
<dt>如何在新设备上恢复购买？</dt>
<dd>使用订阅时所用的同一个 Apple 账户登录，然后在方案页面点按{K_restore}。方案属于你的 Second Brain 账户，而该账户与你的 Apple 账户相关联。</dd>
<dt>可以用我自己的语言使用 App 吗？</dt>
<dd>Second Brain 支持八种语言，并会跟随你设备的语言。如果只想换一种语言而不改动其他设置，请打开{K_settings} → {K_language}。之后语音记录也会使用该语言进行识别。</dd>
<dt>如何导出或删除我的数据？</dt>
<dd>通过{EXPORT}可以生成一个 ZIP 文件，包含你的整个资料库及原始文件。通过{DELETE_ACCOUNT}可以删除你的账户、它的 iCloud 副本以及我们服务器上保存的内容。详情请见<a href="{BASE}{L}/delete-data/">你的数据</a>页面。</dd>
</dl>
""",

"s.trouble.h": "故障排除",
"s.trouble.b": """
<h3>无法使用智能填写或回答</h3>
<ul>
  <li>设备端 AI 需要支持 Apple Intelligence 的设备、iOS 26 或更高版本、在 iOS“设置”中打开 Apple Intelligence，并完整下载其模型。首次打开后，下载可能需要一段时间。</li>
  <li>如果你的设备无法运行它，请登录并在{K_settings} → {K_cloud_choices}中打开{K_luna}，或者继续手动整理。无论哪种方式，你的记录都会被保存。</li>
  <li>如果你看到限制提示，说明你已用完这台设备本月的免费语音记录、智能填写或提问次数。它们会在每月 1 日重置，而且保存功能仍可正常使用。</li>
</ul>
<h3>语音记录没有转写</h3>
<ul>
  <li>请在 iOS {K_settings} → Second Brain 中检查“麦克风”和“语音识别”。</li>
  <li>首次使用某种语言时，需要联网下载 Apple 的语音文件。</li>
  <li>如果转写失败，录音会被保留，你可以重试或自行添加文字。</li>
</ul>
<h3>同步没有更新</h3>
<ul>
  <li>同步需要 Light 或 Pro、已登录的账户，并在{K_settings} → {K_cloud_choices}中打开{K_sync}。</li>
  <li>请确保设备已登录 iCloud 且有可用的 iCloud 存储空间，然后点按{K_sync_now}。</li>
  <li>如果同一个条目在两台设备上都被更改，App 会询问你要保留哪个版本。你的原始记录始终会被保留。</li>
</ul>
<h3>收不到提醒</h3>
<p>{K_settings}中会显示{K_reminders}是否已打开。如果已关闭，请点按该行以打开 iOS“设置”，然后允许通知。</p>
<h3>无法识别我的方案</h3>
<p>请确保你使用订阅时所用的同一个 Apple 账户登录了 Second Brain，然后点按{K_restore}。退款和账单问题由 Apple 通过 <a href="https://support.apple.com/billing">Apple 支持</a>处理。</p>
<h3>App 显示的语言不对</h3>
<p>打开{K_settings} → {K_language}，选择你想要的语言。App、它的小组件和共享表单会立即随之更改。</p>
""",

"s.contact.h": "联系我们",
"s.contact.b": """
<p>有疑问、发现错误，或者某项功能本该正常却没有？给我们写信，会有真人回复你。</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">请注明你的设备型号、iOS 版本、App 版本（显示在{K_settings}底部）以及你预期会发生什么。除非我们提出请求，否则请不要发送你的记录或录音。我们很少需要它们。</span></div></div>
<p style="margin-top:16px" class="small">账单、退款和订阅更改由 Apple 处理：<a href="https://apps.apple.com/account/subscriptions">管理订阅</a> · <a href="https://support.apple.com/billing">申请退款</a>。</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "关于 Second Brain",
"a.h1": "只管说出来，我们来整理。",
"a.sub": "想到什么就说什么。Second Brain 会把它变成任务、日程、笔记和灵感，保留你的原始记录，并在你提问时帮你找回。",
"a.cta": "支持",
"a.meta": "iPhone 和 iPad · iOS 18+ · 八种语言 · 无需账户即可使用",
"a.lead": "Second Brain 是一个安静的地方，用来存放你脑海中的一切。用语音或文字几秒钟就能记下，再检查智能填写整理出的结果；需要找回时就问问你的大脑，回答附有可以打开核对的来源。",

"a.f1.h": "只管说出来。",
"a.f1.p": "语音记录一打开就开始聆听，支持八种语言。你说话时，每个任务、计划和灵感都会被记下，原话也会保留。",
"a.f2.h": "一句话，搞定三件事。",
"a.f2.p": "智能填写会把你说的话变成任务、日程和笔记，并填好日期和时间。在创建任何内容之前，你都会检查每个字段。",
"a.f3.h": "想问什么就问什么。",
"a.f3.p": "回答只来自你保存的内容，并会列出来源，方便你打开核对。",
"a.f4.h": "你的一天，你的一周。",
"a.f4.p": "到期事项和接下来的安排集中在一个清爽的页面上，“日历”App 中的日程就显示在你的任务旁边，另有提醒和可选的晨间摘要。",
"a.f5.h": "什么都不会丢。",
"a.f5.p": "你的原话始终保留在由它生成的所有内容旁边。任何整理都可以撤销，你也可以随时导出整个资料库。",
"a.f6.h": "默认私密。",
"a.f6.p": '优先使用设备端 AI，没有广告，也没有追踪。云端同步和云端 AI 都要等你同意才会开启，任何记录都可以只保留在这台 iPhone 上。<a href="{BASE}{L}/privacy/">了解具体做法。</a>',

"a.price.h": "方案",
"a.price.b": """
<p>Second Brain 可免费使用，保存永远不会被阻止。Light 和 Pro 取消每月限制，并增加同步和云端 AI。</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">免费</div><div class="price">$0</div><ul><li>不限次数的文字记录、任务、项目、搜索、提醒和导出</li><li>每月 5 次语音记录、3 次智能填写和 5 次提问</li><li>在支持的设备上使用设备端 AI</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">月付</div><ul><li>不限次数的语音记录、智能填写和提问</li><li>快速模式</li><li>私密的 iCloud 同步</li><li>每月 300 次云端 AI 记录和 100 次云端回答</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">月付 · 年付</div><ul><li>包含 Light 的全部内容</li><li>每月 700 次云端 AI 记录和 250 次云端回答</li><li>云端每日摘要</li><li>导入网页文字</li><li>年付方案含 7 天免费试用</li></ul></div>
</div>
<p class="small" style="margin-top:14px">价格会按你所在的国家或地区显示在 App 内和 App Store 中。计费由 Apple 处理。<a href="{BASE}{L}/terms/#subscriptions">订阅条款。</a></p>
""",

"a.platform.h": "专为 Apple 设备打造",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone 和 iPad</b><span>iOS 18 或 iPadOS 18 及更高版本。在支持 Apple Intelligence 的设备上可使用设备端 AI。</span></div></li>
  <li><span class="tile">{share}</span><div><b>随时随地</b><span>可通过共享表单从任何 App 保存内容，还有主屏幕小组件、Siri 与快捷指令，以及可选的 Spotlight 搜索。</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>是你的 iCloud，不是我们的</b><span>同步通过你自己的私密 iCloud 存储空间进行，因此我们从不持有你资料库的副本。</span></div></li>
  <li><span class="tile">{globe}</span><div><b>八种语言</b><span>英语、德语、西班牙语、法语、日语、韩语、巴西葡萄牙语和简体中文，语音记录也同样支持。可在{K_settings} → {K_language}中选择。</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "隐私政策",
"p.h1": "你的想法，只属于你。",
"p.sub": "Second Brain 将你的资料库保存在你的设备上。云端同步和云端 AI 都要等你同意才会开启。本页将确切说明哪些内容会离开你的设备、何时离开，以及由谁接收。",
"p.meta": "生效日期：{DATE} · 适用于 iPhone 和 iPad 版 Second Brain App 及本网站",

"p.summary.h": "简要说明",
"p.summary.b": """
<p class="lead">Second Brain 无需账户即可使用。<strong>你的资料库（记录、录音、附件、任务、笔记以及由它们生成的一切）都存储在你的设备上。</strong>没有账户时，App 不会向我们发送任何内容。</p>
<p>以下三种情况会改变这一点，而且每一种都需要你自行选择：</p>
<ul>
  <li><strong>iCloud 同步</strong>（Light 和 Pro）会将你的资料库复制到<em>你自己的</em>私密 iCloud 存储空间。我们无法读取。</li>
  <li><strong>云端 AI（“Luna”）</strong>会在设备端 AI 无法处理或你选择使用 Luna 时，将单次请求所需的文字经由我们的服务器发送给 OpenAI。除非你登录并将其打开，否则不会发送任何内容。</li>
  <li><strong>账户</strong>（通过 Apple 登录）会让我们的服务器保存少量记录：一个经过单向哈希处理的账户 ID、你的方案、你的同意选项以及你的用量计数。我们从不向 Apple 索取你的姓名或电子邮件地址。</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>App 中没有广告、没有分析、没有追踪，也没有第三方 SDK。我们不出售或共享个人数据，也绝不会使用你的内容训练 AI 模型。</div></div>
<p style="margin-top:16px">本政策适用于 iPhone 和 iPad 版 Second Brain App 以及本网站，二者均由 {COMPANY}（“我们”）发布。App 自身的{K_settings} → {K_data_handled}页面以更简短的形式说明了同样的内容。</p>
""",

"p.collect.h": "我们收集的信息",
"p.collect.b": """
<p>这里的“收集”是指离开你的设备、并保存在我们可以读取之处的数据。仅进入你自己 iCloud 存储空间的数据不属于我们收集的数据。</p>
<div class="table-wrap"><table>
<tr><th>类别</th><th>是否收集？</th><th>具体含义</th></tr>
<tr><td>联系信息</td><td>否</td><td>“通过 Apple 登录”已设置为不与我们共享姓名和电子邮件地址。App 中没有电子邮件字段。</td></tr>
<tr><td>标识符</td><td><strong>仅在有账户时</strong></td><td>一个账户 ID，由 Apple 提供给我们的标识符经单向哈希处理生成；以及 Apple 的 App Attest 在你的每台设备上创建的公钥。不使用广告标识符，也不使用设备 ID。</td></tr>
<tr><td>用户内容</td><td><strong>仅在使用云端 AI 时</strong></td><td>你向 Luna 发出的请求所需的文字及其结果，按下文所述短暂保存。你的资料库本身保留在你的设备上和你自己的 iCloud 中。</td></tr>
<tr><td>购买项目</td><td><strong>仅在你订阅时</strong></td><td>Apple 针对你的方案发送的已签名交易：产品、日期、试用和续订状态。我们从不会看到付款详情。</td></tr>
<tr><td>使用数据</td><td><strong>仅在有账户时</strong></td><td>云端 AI 请求的次数及其大小，用于计算每月额度。没有分析功能，也不记录你如何使用 App。</td></tr>
<tr><td>位置、通讯录、健康、浏览历史记录、搜索历史记录、诊断</td><td>否</td><td>App 不会请求位置或通讯录权限，也不包含崩溃报告工具或分析功能。</td></tr>
</table></div>
<p style="margin-top:14px"><strong>追踪：</strong>无。我们不会将与你有关的数据与其他公司的数据相关联，不展示广告，也不与数据经纪商共享任何内容。App 从不显示 Apple 的追踪提示，因为它没有需要请求的内容。</p>
""",

"p.device.h": "保留在你设备上的内容",
"p.device.b": """
<p>Second Brain 会将你的资料库存储在它在你设备上的私有存储空间中，受 iOS 数据保护和你的设备密码保护：</p>
<ul>
  <li><strong>记录</strong>：你说出或输入的内容，与你的原话完全一致，以及你对其所做的任何更正。</li>
  <li><strong>录音和附件</strong>：你添加的音频、照片、PDF、文件和链接，以及在你的设备上从中读取的文字。</li>
  <li><strong>由它们生成的内容</strong>：任务、日程、笔记、灵感、项目、确认历史和撤销历史。</li>
  <li><strong>搜索数据</strong>：基于语义的搜索索引，在你的设备上使用 Apple 的语言模型构建。</li>
  <li><strong>设置</strong>：语言、提醒、小组件、AI 选项，以及你选择的日历。</li>
  <li><strong>iOS 钥匙串中</strong>：你的登录会话，以及免费语音记录、智能填写和提问的每月计数。该计数只包含数字，并且只保留在这台设备上，即使重新安装 App 也是如此。</li>
</ul>
<p>访客资料库和每个已登录的账户在设备上分别使用独立的存储空间。如果你使用 iCloud 云备份或加密的电脑备份，Apple 可能会将这些数据包含在你 Apple 账户下的相应备份中。我们无法访问这些备份。</p>
<p><strong>小组件和 Spotlight。</strong>只有当你打开{K_widgets}时，小组件才会显示条目标题。只有当你打开{K_spotlight}时，已保存的条目才会出现在 Spotlight 中。两者都只保留在你的设备上。</p>
""",

"p.ai.h": "设备端 AI 与云端的 Luna",
"p.ai.b": """
<h3>设备端 AI</h3>
<p>在支持的设备上，智能填写、整理、回答和摘要都在 Apple 的设备端模型上运行。你写下的内容不会离开你的设备，设备端使用也绝不会计入云端额度。</p>
<h3>Luna，我们的云端 AI</h3>
<p>Luna 是由 <strong>OpenAI</strong> 提供、由我们自己的服务器调用的模型。你的设备从不直接连接 OpenAI，App 中也没有 API 密钥。只有当你<strong>已登录并打开{K_luna}</strong>时，Luna 才会运行。当设备端 AI 不可用或无法完成请求时会使用它；如果你使用 Light 或 Pro 并选择 Luna 作为引擎，则会优先使用它。关闭该开关会立即停止新的云端 AI 请求。</p>
<p>每次请求只会发送该请求所需的文字：</p>
<ul>
  <li><strong>整理和智能填写</strong>：正在整理的记录文字（包括在你的设备上从附加的照片或 PDF 中读取的文字）、你的时区和语言，以及你最多 30 个项目的名称和简短摘要。</li>
  <li><strong>问问你的大脑</strong>：你的问题，以及你的设备挑选出的最多 12 个相关已保存条目的简短摘录。</li>
  <li><strong>整理笔记</strong>（Light 和 Pro）：你要求整理的那条笔记的文字。</li>
  <li><strong>每日摘要</strong>（Pro）：当天到期事项的数量，以及你当天最多 10 个条目的简短摘录。</li>
</ul>
<p><strong>绝不会发送：</strong>音频、图片或文件本身；标记为{K_device_only}的记录；你在“日历”App 中的日程；你的姓名或电子邮件地址（我们没有这些信息）；任何可能让 OpenAI 知道你是谁的标识符。</p>
<h3>保存多久</h3>
<p>我们的服务器会将结果保存<strong>最多 24 小时</strong>，这样中断的请求可以直接完成，而不会重复运行，也不会重复扣除你的额度。之后文字会被删除，仅保留一份不含内容的回执（请求的单向哈希值、它所用条目的 ID 以及时间），最长保存一年，用于额度核算。永久删除某个条目时，也会删除由它生成的所有结果；删除账户则会删除全部结果。</p>
<p>我们要求 OpenAI 不存储响应。根据其 API 条款，OpenAI 不会使用这些数据训练其模型。它可能会在有限时间内保留输入和输出，以监控滥用行为，详见其 <a href="https://openai.com/enterprise-privacy/">API 数据政策</a>。</p>
<p>AI 生成的建议和回答可能有误。正因如此，每个智能填写字段在保存前都可以检查，每个回答也都会列出来源。</p>
""",

"p.sync.h": "iCloud 同步",
"p.sync.b": """
<p>使用 Light 或 Pro 时，你可以打开{K_sync}。之后，你的资料库（包括记录、条目、项目、更正、历史和附件）会存储在<strong>你自己 iCloud 账户中的私有 CloudKit 数据库</strong>里，让你的各台设备保持同步。Apple 会依据其自身的<a href="https://www.apple.com/legal/privacy/">隐私政策</a>存储这些数据。我们作为开发者无法读取你的私密 iCloud 数据，我们的服务器也从不会收到你资料库的副本。</p>
<p>标记为{K_device_only}的记录绝不会同步。同步打开时，iOS 可能会通过 Apple 的推送服务传送静默通知，告知 App 有内容发生了变化。不会向我们发送任何推送令牌。</p>
""",

"p.account.h": "你的账户和我们的服务器",
"p.account.b": """
<p>账户是可选的。当你通过 Apple 登录时，我们<strong>不请求姓名，也不请求电子邮件地址</strong>。我们的服务器运行在 <strong>Cloudflare</strong> 上，会保存：</p>
<ul>
  <li><strong>账户 ID</strong>：Apple 提供给我们的标识符的单向哈希值。不存储原始的 Apple 标识符。</li>
  <li><strong>登录数据</strong>：会话（仅以哈希值存储，30 天后过期），以及 Apple 的登录令牌（经过加密，仅用于在你删除账户时将其撤销）。</li>
  <li><strong>设备验证</strong>：Apple 的 App Attest 在你登录的每台设备上（最多 20 台）创建的公钥，让服务器知道它正在与正版的 Second Brain 通信。</li>
  <li><strong>你的选择和方案</strong>：同步和云端 AI 是否打开、你的方案及其续订日期，以及 Apple 为确认方案而发送的交易。</li>
  <li><strong>用量计数</strong>：你本月已使用了多少云端额度。</li>
  <li><strong>云端 AI 结果</strong>，按上文所述短暂保存。</li>
</ul>
<p>为防止服务被滥用，服务器会短暂保存你的 IP 地址与当前分钟组合后的单向哈希值，并在几分钟内删除。我们不保留请求日志，我们的服务器也从不会收到你的资料库。</p>
<p><strong>网页导入</strong>（Pro）：当你要求导入某个网页的文字时，我们的服务器会自行获取该公开网页，并将其中可读的文字返回到你的设备。网页的地址和文字不会被存储，也不会发送给 Luna。</p>
""",

"p.voice.h": "语音、语音识别和录音",
"p.voice.b": """
<p>语音记录仅在你录音时使用麦克风。语音会通过 Apple 的语音识别<strong>在你的设备上</strong>转写。你的录音不会为了转写而发送给 Apple 或我们，不过首次使用某种语言时会下载 Apple 的语音文件。</p>
<p>录音保存在你的资料库中。转写完成后，音频会在保存 <strong>7 天</strong>后删除，除非你点按{K_keep_recording}。转写失败的录音会一直保留到你删除为止。音频删除后，转写文本仍会保留。</p>
""",

"p.permissions.h": "权限",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>权限</th><th>用途</th></tr>
<tr><td>麦克风、语音识别</td><td>语音记录和设备端转写。</td></tr>
<tr><td>相机、照片</td><td>拍摄或选择要附加的图片。只会读取你选择的图片。</td></tr>
<tr><td>日历</td><td>仅在你点按{K_calendars}时才会请求。你选择的日历会在你的设备上读取，用于显示在你的任务旁边，绝不会上传。新日程只会在你确认后，通过 Apple 自己的编辑器添加到“日历”App。</td></tr>
<tr><td>通知</td><td>提醒、晨间摘要，以及免费试用结束前的提醒。所有通知都在你的设备上安排。</td></tr>
</table></div>
<p style="margin-top:14px">你可以在 iOS {K_settings} → Second Brain 中更改其中任何一项。App 从不会请求你的位置或通讯录。</p>
""",

"p.purchases.h": "购买",
"p.purchases.b": """
<p>Light 和 Pro 通过 Apple 的 App Store 销售。付款在你与 Apple 之间进行，受 <a href="https://www.apple.com/legal/privacy/">Apple 的隐私政策</a>约束，我们从不会看到你的付款详情。购买方案需要 Second Brain 账户，这样方案才能跟随你到其他设备上。我们的服务器会验证 Apple 签名的交易，将其与你的账户一起存储，并接收 Apple 关于续订、退款和取消的通知，以确保你的方案状态正确。</p>
""",

"p.third.h": "服务提供商",
"p.third.b": """
<p>Second Brain <strong>不包含任何第三方 SDK</strong>：没有分析、没有广告，也没有崩溃报告工具。以下公司代表我们处理数据，且各自仅用于所列用途：</p>
<ul>
  <li><strong>Apple</strong>：通过 Apple 登录、App Attest、App Store 和购买、你自己账户中的 iCloud 同步、用于同步的推送传送，以及设备端 AI 和语音模型。</li>
  <li><strong>Cloudflare</strong>：托管我们的服务器及其数据库，并将请求路由到服务器。</li>
  <li><strong>OpenAI</strong>：按上文所述，为你允许的云端 AI 请求运行 Luna。</li>
</ul>
<p>我们不会出售或出租个人数据，也不与广告商或数据经纪商共享任何内容。如法律要求，我们可能会披露信息。由于我们掌握的信息极少，能够披露的内容也很少。</p>
""",

"p.retention.h": "保存期限",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>数据</th><th>保存期限</th></tr>
<tr><td>你设备上的资料库</td><td>直到你将其删除。你删除的条目会在{K_recently_deleted}中保留 30 天。</td></tr>
<tr><td>语音录音</td><td>转写完成后保留 7 天，除非你选择保留。如果转写失败，则保留到你将其删除为止。</td></tr>
<tr><td>你的 iCloud 副本</td><td>直到你删除它或删除你的账户。它由 Apple 存储在你的 iCloud 中。</td></tr>
<tr><td>云端 AI 结果</td><td>最多 24 小时。不含内容的回执最长保留 1 年。</td></tr>
<tr><td>登录会话</td><td>自上次刷新起 30 天</td></tr>
<tr><td>账户、方案和用量计数</td><td>在你的账户存续期间</td></tr>
<tr><td>用于防滥用的经哈希处理的 IP 地址</td><td>几分钟</td></tr>
<tr><td>服务器备份</td><td>我们托管服务商的数据库备份可能会将已删除的数据保留最多 30 天，之后过期。</td></tr>
</table></div>
""",

"p.delete.h": "导出和删除",
"p.delete.b": """
<p>一切都由你掌控，就在 App 中：</p>
<ul>
  <li><strong>导出</strong>：通过{EXPORT}可创建一个 ZIP 文件，其中包含你的整个资料库、你的原始文件，以及一份无法包含在内的项目清单。</li>
  <li><strong>从这台设备上删除</strong>：通过{DELETE_LOCAL}可移除这台设备上的资料库。这不会删除你的账户或其 iCloud 副本。</li>
  <li><strong>删除你的账户</strong>：通过{DELETE_ACCOUNT}可删除你的 iCloud 副本、我们服务器上与该账户有关的所有内容，以及这台设备上该账户的资料库，并撤销 Second Brain 的“通过 Apple 登录”访问权限。</li>
</ul>
<p>账户删除后，我们的服务器只会保留一个不含内容的标记：被标记为已删除的哈希账户 ID、其用量计数，以及其购买标识符和设备标识符的单向哈希值。这个标记能让中断的删除操作得以完成，并防止同一笔购买或免费云端体验被重复领取。它不包含任何内容、姓名或电子邮件地址。分步说明请见<a href="{BASE}{L}/delete-data/">你的数据</a>页面。</p>
""",

"p.rights.h": "你的权利",
"p.rights.b": """
<p>视你所在地区而定（包括根据 GDPR、英国 GDPR 以及加州 CCPA/CPRA），你有权访问、更正、导出、限制处理、反对处理和删除我们持有的与你相关的个人数据，有权随时撤回同意，并有权向你所在地的数据保护机构投诉。其中大部分权利已内置于 App 中：导出、删除，以及同步和云端 AI 开关。如有其他需要，请发送邮件至 {MAIL}，我们会在 30 天内回复。</p>
<p>在适用 GDPR 的情况下，我们依据以下法律基础：<strong>合同</strong>，用于提供你使用的功能和你购买的方案；<strong>同意</strong>，用于 iCloud 同步和云端 AI，你可以通过相应开关撤回同意；<strong>正当利益</strong>，用于保障服务安全并防止滥用（App Attest 和防滥用保护）；以及<strong>法律义务</strong>，用于购买记录。</p>
""",

"p.children.h": "儿童",
"p.children.b": """
<p>Second Brain 并非面向 13 岁以下或未达到你所在地数字同意年龄的儿童。我们不会在知情的情况下收集儿童的个人数据。如果你认为有儿童创建了账户，请发送邮件至 {MAIL}，我们会协助删除该账户。</p>
""",

"p.transfers.h": "数据的处理地点",
"p.transfers.b": """
<p>Cloudflare 在其全球网络上运行我们的服务器，OpenAI 和 Apple 可能会在美国及其他国家或地区处理数据。在法律要求的情况下，这些传输受服务提供商的数据处理条款（包括标准合同条款）保障。存储在你设备上的数据会留在你设备所在的地方。</p>
""",

"p.changes.h": "本政策的变更",
"p.changes.b": """
<p>如果 App 处理数据的方式发生变化，我们会更新本政策及顶部的日期。我们会在 App 的版本说明中提及重大变更，并在法律要求时再次征得你的同意。未经你重新选择，我们绝不会开始将你的内容发送到任何新的地方。</p>
""",

"p.contact.h": "联系我们",
"p.contact.b": """
<p>Second Brain 的发布者 {COMPANY} 是本政策所述个人数据的控制者。如有隐私问题或请求，请发送邮件至 {MAIL}。</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "使用条款",
"t.h1": "用平实的语言写成的协议。",
"t.sub": "Second Brain 能做什么，它的 AI 能承诺什么、不能承诺什么，你的内容会如何处理，以及 Light 和 Pro 如何计费。",
"t.meta": "生效日期：{DATE} · {COMPANY} 出品的 Second Brain",

"t.acceptance.h": "1. 接受条款",
"t.acceptance.b": """
<p>本使用条款（“条款”）是你与 iPhone 和 iPad 版 Second Brain App（“Second Brain”或“本 App”）及其相关在线服务的发布者 {COMPANY}（“我们”）之间的协议。安装或使用 Second Brain 即表示你接受本条款以及我们的<a href="{BASE}{L}/privacy/">隐私政策</a>。如果你不同意，请勿使用本 App。</p>
""",
"t.who.h": "2. 谁可以使用 Second Brain",
"t.who.b": """
<p>你必须年满 13 岁，或达到你所在地的数字同意年龄，才能使用 Second Brain。如果你未达到所在地的法定成年年龄，则需要获得父母或监护人的许可才能购买订阅。</p>
""",
"t.what.h": "3. Second Brain 是什么，不是什么",
"t.what.b": """
<p>Second Brain 是一款个人工具，用于通过语音或文字记录想法，并将其整理成任务、日程、笔记和灵感，同时提供提醒、搜索以及基于你所保存内容的回答。</p>
<p>Second Brain <strong>不是</strong>医疗、法律、财务或其他专业服务，它生成的任何内容都不构成专业建议。请勿将其作为记住关键事项的唯一方式，例如用药、法律期限或安全相关事项。提醒取决于 iOS、你的设置和你的设备，可能无法送达。如遇紧急情况，请联系当地紧急服务。</p>
""",
"t.account.h": "4. 你的账户",
"t.account.b": """
<p>账户是可选的，使用“通过 Apple 登录”。你需要对你的 Apple 账户、你的设备及其密码，以及你账户下的活动负责。每个账户仅供一人使用。你可以随时退出登录，也可以在 App 中删除你的账户，具体请见<a href="{BASE}{L}/delete-data/">你的数据</a>页面。</p>
""",
"t.content.h": "5. 你的内容",
"t.content.b": """
<p>你在 Second Brain 中记录、附加或写下的所有内容（“你的内容”）始终归你所有。我们不主张对其拥有任何所有权。你仅授予我们为提供你所选功能而处理你的内容所需的有限许可：例如，在你打开云端 AI 时将文字发送给 Luna，或获取你要求导入的网页。我们不会使用你的内容训练 AI 模型，也不会出售你的内容。</p>
<p>你需要对你的内容负责，并确保你有权记录、导入和存储这些内容，包括其中涉及他人的任何信息。你的资料库保存在你的设备上，如果你选择，也会保存在你自己的 iCloud 中。请自行保留导出副本。我们不持有你资料库的副本，如果你的设备和 iCloud 副本丢失，我们无法恢复。</p>
""",
"t.ai.h": "6. AI 功能",
"t.ai.b": """
<p>Second Brain 使用人工智能来建议如何整理你记录的内容、填写日期和时间等细节、根据你的资料库回答问题，以及撰写摘要。在可用时，它会使用 Apple 的设备端模型；如果你允许，还会使用 <strong>Luna</strong>，即由 OpenAI 提供、经由我们服务器运行的云端模型。</p>
<p><strong>AI 输出可能错误、不完整或已过时。</strong>它可能会误读日期、遗漏任务，或错误陈述来源的内容。请在创建之前检查建议，并在依赖回答之前核对其来源。如果你打开{K_quick}，条目会在不经过上述确认的情况下创建，这是你自己的选择。智能填写不确定的内容会进入{K_needs_review}，并且{K_undo}仍然可用。</p>
<p>你同意不使用 AI 功能生成违法、有害或侵权的内容，也不试图提取底层模型、其指令或我们服务的密钥。为保护服务，我们可能会更换所用的模型、调整限制或暂停某项功能。届时，App 的其余部分仍可正常使用，你已保存的内容不会受到影响。</p>
""",
"t.cloud.h": "7. 云端功能和额度",
"t.cloud.b": """
<p><strong>同步</strong>使用你自己的 iCloud 账户，并取决于 Apple 的服务、你的 iCloud 存储空间和你的网络连接。<strong>云端 AI</strong> 受你方案的每月额度限制：Light 每月包含 300 次云端 AI 记录和 100 次云端回答，Pro 包含 700 次和 250 次，已登录的免费账户可获得一次性体验额度。额度在每个自然月重置，未用完的部分不会结转。为保证服务公平，每月处理的文字总量也有上限。<strong>网页导入</strong>（Pro）仅获取公开网页，你需要确保自己有权使用所导入的内容。</p>
<p>我们会努力保持云端功能可用，但不保证其不会中断。没有云端功能时，设备端功能仍可正常使用。</p>
""",
"t.subscriptions.h": "8. 订阅和计费",
"t.subscriptions.b": """
<p>Second Brain 可免费下载和使用，但每台设备上的语音记录、智能填写和“问问你的大脑”有每月限制。保存你记录的内容永远不会被阻止。付费方案是通过 Apple 销售的自动续期订阅，价格以 App 内和 App Store 中针对你所在国家或地区显示的价格为准：</p>
<ul>
  <li><strong>Light 月付</strong>：按月计费。</li>
  <li><strong>Pro 月付</strong>：按月计费。</li>
  <li><strong>Pro 年付</strong>：按年计费，符合条件的新订阅者可先享受 <strong>7 天免费试用</strong>。</li>
</ul>
<p>订阅需要 Second Brain 账户（通过 Apple 登录）。确认购买时，费用将从你的 Apple 账户中扣除。除非你在免费试用结束前至少 24 小时取消，否则免费试用将转为付费订阅。除非在当前周期结束前至少 24 小时关闭自动续订，否则订阅将以相同的价格和周期自动续订。你的 Apple 账户将在当前周期结束前的 24 小时内被扣取续订费用。你可以在 <a href="https://apps.apple.com/account/subscriptions">App Store 订阅设置</a>中或通过 App 内的{K_manage}管理或取消订阅。取消将在当前周期结束时生效。退款由 Apple 根据其政策处理。使用{K_restore}可在另一台设备上恢复方案。订阅不支持通过家人共享来共享。</p>
<p><strong>如果订阅结束</strong>，你保存的内容都不会被删除。阅读、编辑、搜索、导出和删除仍可正常使用，免费版的每月限制将重新生效，同步和云端额度会停止。删除 App 或你的账户不会取消订阅，请通过 Apple 取消。我们可能会更改方案的价格或功能。按照 Apple 的规则要求，在涨价对你生效之前，Apple 会通知你。</p>
""",
"t.licence.h": "9. 许可和知识产权",
"t.licence.b": """
<p>我们授予你一项个人的、非排他的、不可转让的、可撤销的许可，允许你依据本条款和 App Store 的使用规则，在你拥有或控制的 Apple 设备上使用 Second Brain。Second Brain 及其名称、设计、美术作品（包括大脑角色）、文字和代码均归 {COMPANY} 所有，并受法律保护。除非法律明确允许，否则你不得复制、修改、分发、出售、租赁、反向工程本 App，或基于本 App 创作衍生作品。</p>
""",
"t.use.h": "10. 可接受的使用",
"t.use.b": """
<p>你同意不会：以违法方式使用 Second Brain，或用它存储你无权持有的内容；干扰我们的服务器、使其过载或对其进行探测；规避额度限制、App Attest 或 App Store 的购买系统；访问他人的账户；或使用本服务骚扰、伤害他人，或在未取得法律所要求的同意的情况下录制他人。</p>
""",
"t.termination.h": "11. 终止",
"t.termination.b": """
<p>你可以随时停止使用 Second Brain，也可以在 App 中删除你的账户。如果你严重或屡次违反本条款，或法律有此要求，我们可能会暂停或终止你对云端功能的访问。在可能的情况下，我们会事先通知你。你设备上的内容仍归你所有，可供你导出。第 5、6、9、12、13 和 15 条在终止后继续有效。</p>
""",
"t.warranty.h": "12. 保证和责任",
"t.warranty.b": """
<p>Second Brain 按“现状”和“现有”基础提供，不附带任何明示或默示的保证。我们不保证 AI 输出准确无误、提醒总能送达、同步或云端功能不会中断，或本 App 没有错误。在法律允许的最大范围内，对于因你使用或无法使用本 App 而产生的间接、附带、特殊、后果性或惩罚性损害，或数据、利润或机会的损失，包括 AI 功能生成的任何内容或未能送达的提醒，{COMPANY} 概不负责。在无法免除责任的情况下，责任以你在提出索赔前十二个月内为 Second Brain 支付的金额为限。本条款中的任何内容均不限制你作为消费者享有的、不可放弃的权利。</p>
""",
"t.apple.h": "13. Apple",
"t.apple.b": """
<p>Second Brain 通过 Apple App Store 分发。本条款是你与 {COMPANY} 之间的协议，而非你与 Apple 之间的协议。Apple 没有义务为本 App 提供任何维护或支持服务，也不负责处理与本 App 相关的任何索赔，包括产品责任、法律合规或知识产权方面的索赔。如果本 App 不符合任何适用的保证，你可以通知 Apple，Apple 将退还购买价款（如有）。在法律允许的最大范围内，Apple 对本 App 不承担任何其他保证义务。Apple 及其子公司是本条款的第三方受益人，可以向你强制执行本条款。对于本条款未作规定的事项，适用 Apple 的<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">许可应用程序最终用户许可协议</a>。你确认你不在受美国政府禁运的国家或地区，也不在美国政府的任何禁止或受限交易方名单上；你在使用本 App 时必须遵守任何适用的第三方条款。</p>
""",
"t.changes.h": "14. 本条款的变更",
"t.changes.b": """
<p>随着 Second Brain 的变化，我们可能会更新本条款。届时顶部的日期会随之更改，我们也会在 App 的版本说明中提及重大变更。更新后继续使用即表示你接受修订后的条款。如果你不接受，可以停止使用本 App 并删除你的账户。</p>
""",
"t.law.h": "15. 适用法律",
"t.law.b": """
<p>本条款受巴基斯坦法律管辖（{COMPANY} 在该国运营），不考虑法律冲突规则。如果你居住国的法律为你提供了不能通过合同排除的保护，这些保护仍然适用。</p>
""",
"t.contact.h": "16. 联系我们",
"t.contact.b": """
<p>关于本条款的问题，请发送邮件至 {MAIL}。</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "你的数据",
"d.h1": "导出或删除你的数据",
"d.sub": "你的资料库保存在你的设备上；如果你选择了同步，也会保存在你自己的 iCloud 中。下面介绍如何获取副本、从一台设备上删除，或删除你的账户及其保存的全部内容。",
"d.meta": '另请参阅<a href="{BASE}{L}/privacy/">隐私政策</a>',

"d.where.h": "什么数据存储在哪里",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>数据</th><th>存储位置</th><th>如何移除</th></tr>
<tr><td>记录、录音、附件、任务、笔记、项目、历史</td><td>你的设备</td><td>{DELETE_LOCAL}，或删除你的账户（见下文）</td></tr>
<tr><td>同一个资料库（如果你打开了同步）</td><td>你自己 iCloud 中的私有数据库</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>账户 ID、方案、同意选项、用量计数、设备密钥</td><td>我们的服务器（Cloudflare）</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>云端 AI 结果</td><td>我们的服务器，最多 24 小时</td><td>到期自动移除；你永久删除相关条目或删除账户时也会移除</td></tr>
<tr><td>每月免费使用计数</td><td>这台设备上的 iOS 钥匙串（仅数字）</td><td>每月重置。删除 App 后，iOS 可能仍会保留它</td></tr>
<tr><td>订阅</td><td>你的 Apple 账户</td><td>通过 Apple 取消（见下文）</td></tr>
</table></div>
""",
"d.export.h": "先保存一份副本",
"d.export.b": """
<ol class="steps">
  <li><div>打开 Second Brain，前往{K_settings}。</div></li>
  <li><div>点按{K_export}，然后点按{K_share_export}。</div></li>
  <li><div>将 ZIP 文件存储到“文件”App，或发送到你想要的地方。它包含你的资料库（JSON、Markdown 格式以及一个任务 CSV 文件）、你的原始文件，以及一份无法包含在内的项目清单。</div></li>
</ol>
""",
"d.local.h": "从这台设备上删除",
"d.local.b": """
<p>要删除单个条目，请先将其删除，然后在{K_settings} → {K_recently_deleted}中使用{K_delete_permanently}将其移除。否则，它会在 30 天后被自动移除。</p>
<p>要删除这台设备上的整个资料库，请使用{DELETE_LOCAL}。这<strong>不会</strong>删除你的账户、其 iCloud 副本或单独的访客资料库。删除 App 也会将其数据从设备上移除。</p>
""",
"d.account.h": "删除你的账户",
"d.account.b": """
<ol class="steps">
  <li><div>打开{K_settings} → {K_cloud_choices}。</div></li>
  <li><div>点按{K_delete_account}并确认。</div></li>
  <li><div>Second Brain 会删除该账户的 iCloud 副本、我们服务器上与该账户有关的所有内容（会话、方案、选项、用量计数、设备密钥和 AI 结果），以及这台设备上该账户的资料库。它还会撤销自身的“通过 Apple 登录”访问权限。你单独的访客资料库会保留在设备上。</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>如果你的登录已过期，App 会要求你使用同一个 Apple 账户重新登录以完成操作。如果你已不再拥有该设备，可以在任意 iPhone 或 iPad 上安装 Second Brain，使用同一个 Apple 账户登录，然后在那里删除。</div></div>
<p style="margin-top:16px">之后，我们的服务器只会保留一个不含内容的标记：被标记为已删除的哈希账户 ID、其用量计数，以及其购买标识符和设备标识符的单向哈希值。这能让中断的删除操作得以完成，并防止同一笔购买或免费体验被重复领取。我们托管服务商保存的数据库备份会在 30 天内过期。</p>
""",
"d.subscription.h": "你的订阅",
"d.subscription.b": """
<p>删除你的数据、账户或 App <strong>不会</strong>取消订阅。订阅属于你的 Apple 账户。请在 <a href="https://apps.apple.com/account/subscriptions">App Store 订阅设置</a>中取消，订阅会保持有效，直到当前周期结束。退款由 <a href="https://support.apple.com/billing">Apple 支持</a>处理。</p>
""",
"d.email.h": "向我们咨询",
"d.email.b": """
<p>如果你无法使用 App，或对你的数据有任何疑问，请发送邮件至 {MAIL}。我们会在 30 天内回复。我们没有你账户的姓名或电子邮件地址，因此会与你一起想办法找到它。最快的方式通常是在任意设备上登录并在那里删除。请不要向我们发送你的记录或录音，我们无需它们也能帮助你。</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "找不到这个页面。",
"nf.sub": "就算是第二大脑，偶尔也会忘掉一个链接。",
"nf.cta": "返回支持页面",
"nf.b": '这个页面不存在。试试<a href="{BASE}/">支持</a>、<a href="{BASE}/privacy/">隐私政策</a>或<a href="{BASE}/terms/">使用条款</a>。',

}
