# -*- coding: utf-8 -*-
"""English — the development language, and the fallback behind all seven others.

A key missing from another catalogue renders as the English here, never as an
identifier. That is the same rule the app follows (docs/LOCALIZATION.md).

Every value is an HTML fragment. `{name}` placeholders are filled by
`gen.context()`: `{BASE}` and `{L}` build an in-language link, `{MAIL}` is the
support address, `{DELETE_ACCOUNT}`, `{DELETE_LOCAL}` and `{EXPORT}` are the
app's own Settings paths, `{K_*}` are single app labels in a <kbd>, `{DATE}` is
the localised date, and the rest are icons.

The `k.*` values are the app's own labels, copied from
SecondBrain/Localizable.xcstrings in the app repo. Change them only when the
app's label changes.
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Support",
"nav.about": "About",
"nav.privacy": "Privacy",
"nav.terms": "Terms",
"nav.data": "Your data",

"ui.skip": "Skip to content",
"ui.pages": "Pages",
"ui.footer": "Footer",
"ui.lang": "Language",
"ui.toc": "On this page",
"ui.rights": "All rights reserved.",
"ui.store_soon": "Coming soon to the App Store",
"ui.store_get": "Download on the App Store",
"ui.date": "16 October 2026",
"ui.last_updated": "Last updated: {DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "This translation is provided for convenience. If it differs from the English version, the English version applies.",

# The app's own words, so this site names a screen the way the screen does.
"k.settings": "Settings",
"k.cloud_choices": "Cloud sync and AI choices",
"k.account": "Your account",
"k.delete_account": "Delete account and library",
"k.keep_account": "Keep account",
"k.delete_local": "Delete all local data",
"k.export": "Prepare an export",
"k.share_export": "Share library export",
"k.recently_deleted": "Recently deleted",
"k.delete_permanently": "Delete permanently",
"k.data_handled": "How your data is handled",
"k.privacy_screen": "Your privacy",
"k.sync": "Sync my library",
"k.sync_now": "Sync now",
"k.luna": "Use Luna to organize and answer",
"k.on_device": "On-device AI",
"k.language": "Language",
"k.restore": "Restore purchases",
"k.manage": "Manage subscription",
"k.sign_out": "Sign out and open guest library",
"k.keep_recording": "Keep this recording",
"k.needs_review": "Needs review",
"k.smart_org": "Smart organization",
"k.smart_fill": "Smart fill",
"k.quick": "Quick mode",
"k.ask": "Ask your Brain",
"k.calendars": "Connect Apple Calendar",
"k.morning": "Morning summary",
"k.reminders": "Reminder notifications",
"k.spotlight": "Show saved items in Spotlight",
"k.device_only": "Keep only on this iPhone",
"k.undo": "Undo",
"k.widgets": "Show titles in widgets",

"meta.support.title": "Second Brain — Support",
"meta.support.desc": "Official support for Second Brain: how capture, Smart fill and Ask your Brain work, what the app needs, answers to common questions, and how to reach us.",
"meta.about.title": "Second Brain — Just say it. We'll sort it out.",
"meta.about.desc": "Second Brain turns what you say or type into tasks, events, notes and ideas, keeps your original, and answers questions from what you saved, with on-device AI first.",
"meta.privacy.title": "Privacy Policy — Second Brain",
"meta.privacy.desc": "What Second Brain keeps on your device, what reaches iCloud, what our server holds, and exactly when your words are sent for cloud AI.",
"meta.terms.title": "Terms of Use — Second Brain",
"meta.terms.desc": "Terms of Use (EULA) for Second Brain: your content, the AI features, cloud allowances, and how Light and Pro subscriptions are billed.",
"meta.data.title": "Delete your data — Second Brain",
"meta.data.desc": "How to export your library, delete it from this device, and delete your Second Brain account and everything it holds in iCloud and on our server.",
"meta.nf.title": "Not found — Second Brain",
"meta.nf.desc": "Page not found.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Support",
"s.h1": "Help with Second Brain",
"s.sub": "Say it or type it, and Second Brain sorts it into tasks, events, notes and ideas, keeps your original, and lets you undo any change. This page covers how it works, what it needs, and how to reach us.",
"s.cta": "Read the FAQ",
"s.meta": 'Works without an account · on-device AI first · <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"s.how.h": "How Second Brain works",
"s.how.b": """
<p class="lead">Get it out of your head in seconds, and find it again when it matters.</p>
<p>Tap the microphone and talk the way you think, or type. Second Brain saves your words first, exactly as you said them, so nothing is lost. Then it suggests what they contain: a task with a due date, an event with a time, a note or an idea, filed under the right project. You check each suggestion before anything is created, and every change can be undone.</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>Capture</b><span>Voice capture starts recording as soon as it opens. You can also type, share text, links, photos or files from other apps, or attach them to a capture.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>Smart fill and review</b><span>Tap Done and Smart fill drafts tasks, events, notes and ideas with their dates and times. Every field can be edited before you tap Create. Anything it isn't sure about stays highlighted, or goes to {K_needs_review}.</span></div></li>
  <li><span class="tile">{chat}</span><div><b>Ask your Brain</b><span>Ask a question in plain words. Answers come only from what you saved, with the sources listed so you can open and check them.</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>Today and Calendar</b><span>What's due, what's next and what matters, plus a week view with your Apple Calendar beside your tasks. Optional reminders and a morning summary.</span></div></li>
  <li><span class="tile">{undo}</span><div><b>Your original, always</b><span>The words you captured stay in your library next to what was made from them. {K_undo} reverses any organizing, and deleted items wait in {K_recently_deleted} for 30 days.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Private by default</b><span>Organizing and answers run on your device with Apple's on-device model when your device supports it. Cloud sync and cloud AI stay off until you choose them. See <a href="{BASE}{L}/privacy/">Privacy</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Requirements",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Device</th><td><strong>iPhone or iPad</strong> with <strong>iOS 18 or iPadOS 18</strong> or later.</td></tr>
<tr><th>On-device AI</th><td>A device that supports <strong>Apple Intelligence</strong>, running iOS 26 or iPadOS 26 or later, with Apple Intelligence turned on and its model downloaded. On other devices you can still capture, organize by hand, search and set reminders. Smart fill and answers can then use Luna in the cloud, if you sign in and allow it.</td></tr>
<tr><th>Account</th><td><strong>Optional.</strong> Capture, organizing, search, export and deletion work without one, and so does buying Light or Pro. Sign in with Apple is needed to sync with iCloud, use Luna, or import page text.</td></tr>
<tr><th>Internet</th><td>Not needed for capturing, on-device AI, search or export. Needed for signing in, purchases, iCloud sync, Luna, page import, and the first download of Apple's speech files for your language.</td></tr>
<tr><th>Permissions</th><td>Microphone and Speech Recognition for voice capture. Camera or Photos only when you attach a picture. Calendars only if you connect Apple Calendar. Notifications only for reminders and the morning summary. Each one is asked when you first use it.</td></tr>
<tr><th>iCloud</th><td>For sync, an iCloud account with enough free space. Sync is included with Light and Pro.</td></tr>
<tr><th>Languages</th><td>English, German, Spanish, French, Japanese, Korean, Brazilian Portuguese and Simplified Chinese. Voice capture listens in the app's language. Choose it in {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Getting started",
"s.start.b": """
<ol class="steps">
  <li><div><b>Open Second Brain.</b> There is no sign-up. Your library lives on your device from the first second.</div></li>
  <li><div><b>Tap the microphone and say what's on your mind.</b> Allow the microphone and speech recognition when iOS asks. Or type.</div></li>
  <li><div><b>Tap Done.</b> Smart fill drafts tasks, events, notes and ideas. Check each field, change anything, then tap Create.</div></li>
  <li><div><b>Ask your Brain.</b> Ask "what did I promise Sam?" or "when is the dentist?" and open the cited sources to check.</div></li>
  <li><div><b>Optional:</b> to sync with iCloud or use Luna, open {K_settings} → {K_cloud_choices} and sign in with Apple. Each one has its own switch.</div></li>
</ol>
""",

"s.faq.h": "Frequently asked questions",
"s.faq.b": """
<dl class="faq">
<dt>Do I need an account?</dt>
<dd>No. Capture, organizing, search, reminders, export and deletion all work without one, on your device. An account is only needed to sync with iCloud, use Luna in the cloud, or import page text. You can buy a plan without one. Signing in never uploads your existing guest library. You choose which thoughts to copy into the account.</dd>
<dt>What is free?</dt>
<dd>Typed capture, tasks and projects, local search, on-device transcription, reminders, editing, export and deletion are free and unlimited. Free also includes <strong>20 voice captures, 40 Smart fills and 5 questions to {K_ask} each month</strong>, counted on each device and reset on the first of the month. Saving is never blocked: when a limit is reached you can still type and save. A signed-in account that allows cloud AI also gets a one-time sample of 10 cloud AI captures and 5 answers.</dd>
<dt>What do Light and Pro add?</dt>
<dd><strong>Light</strong> removes the monthly limits on voice capture, Smart fill and Ask your Brain, adds {K_quick} and private iCloud sync, and includes 300 cloud AI captures and 100 cloud answers a month. <strong>Pro</strong> includes everything in Light, raises the cloud allowance to 700 cloud AI captures and 250 cloud answers a month, and adds a cloud daily summary and importing a web page's text. Light is billed monthly. Pro is monthly or yearly, and the yearly plan starts with 7 days free for eligible new subscribers. Prices are shown in the app and on the App Store for your country, and Apple handles billing.</dd>
<dt>What is the difference between on-device AI and Luna?</dt>
<dd>On-device AI is Apple's model running on your device. Nothing you write leaves it. Luna is a cloud model from OpenAI that runs through our server. It is used only if you sign in and turn on {K_luna}, and only within your plan's cloud allowance. On-device AI goes first. Luna covers when your device can't help. Light and Pro can choose Luna as their main engine in {K_settings}. Captures marked {K_device_only} never go to Luna, whichever engine you choose.</dd>
<dt>What does "{K_device_only}" do?</dt>
<dd>That capture, and everything made from it, is never synced to iCloud and never sent for cloud AI. On-device AI can still organize it.</dd>
<dt>Can I trust the answers?</dt>
<dd>Answers are built only from what you saved, and every answer lists its sources so you can open them. AI can still misread or miss things, so check the sources before you rely on an answer for anything important.</dd>
<dt>What happens to my voice recordings?</dt>
<dd>They are transcribed on your device and are not sent to Apple or to us for transcription. Once a transcript is complete, the audio is deleted after 7 days unless you tap {K_keep_recording}. If a transcript fails, the audio stays until you delete it, so you can try again. Transcripts stay after their audio is gone.</dd>
<dt>Does it sync between my iPhone and iPad?</dt>
<dd>Yes, with Light or Pro. Sign in with the same Apple Account on both and turn on {K_sync}. Your library syncs through your own private iCloud storage, which we cannot read.</dd>
<dt>What happens if my subscription ends?</dt>
<dd>Nothing you saved is removed. Reading, editing, search, export and deletion keep working, and the free monthly limits apply again. Sync and cloud allowances stop until you subscribe again.</dd>
<dt>How do I restore a purchase on a new device?</dt>
<dd>On the new device, use the same Apple Account you subscribed with and tap {K_restore} on the plans screen. The plan's features on that iPhone turn on straight away. If the plan is linked to your Second Brain account, also sign in with Apple to get iCloud sync and your cloud allowance back.</dd>
<dt>Can I use the app in my own language?</dt>
<dd>Second Brain speaks eight languages and follows your device's language. To pick a different one without changing anything else, open {K_settings} → {K_language}. Voice capture then listens in that language.</dd>
<dt>How do I get my data out, or delete it?</dt>
<dd>{EXPORT} makes a ZIP of your whole library with your original files. {DELETE_ACCOUNT} deletes your account, its iCloud copy and what our server holds. Details are on the <a href="{BASE}{L}/delete-data/">Your data</a> page.</dd>
</dl>
""",

"s.trouble.h": "Troubleshooting",
"s.trouble.b": """
<h3>Smart fill or answers aren't available</h3>
<ul>
  <li>On-device AI needs a device that supports Apple Intelligence, iOS 26 or later, Apple Intelligence turned on in iOS Settings, and its model fully downloaded. Downloading can take a while after you first turn it on.</li>
  <li>If your device can't run it, sign in and turn on {K_luna} in {K_settings} → {K_cloud_choices}, or keep organizing by hand. Your capture is saved either way.</li>
  <li>If you see a limit message, you have used this month's free voice captures, Smart fills or questions on this device. They reset on the first of the month, and saving still works.</li>
</ul>
<h3>Voice capture isn't transcribing</h3>
<ul>
  <li>Check iOS {K_settings} → Second Brain → Microphone and Speech Recognition.</li>
  <li>The first time you use a language, Apple's speech files need a connection to download.</li>
  <li>If a transcript fails, the recording is kept so you can retry or add the text yourself.</li>
</ul>
<h3>Sync isn't updating</h3>
<ul>
  <li>Sync needs Light or Pro, a signed-in account, and {K_sync} turned on in {K_settings} → {K_cloud_choices}.</li>
  <li>Make sure the device is signed in to iCloud and has free iCloud storage, then tap {K_sync_now}.</li>
  <li>If the same item changed on two devices, the app asks you which version to keep. Your original capture is always preserved.</li>
</ul>
<h3>Reminders don't arrive</h3>
<p>{K_settings} shows whether {K_reminders} are on. If they were turned off, tap the row to open iOS Settings and allow them.</p>
<h3>My plan isn't recognised</h3>
<p>Make sure your iPhone uses the same Apple Account you subscribed with, then tap {K_restore}. If the plan is linked to your Second Brain account, sign in with Apple as well. Refunds and billing questions are handled by Apple through <a href="https://support.apple.com/billing">Apple Support</a>.</p>
<h3>The app is in the wrong language</h3>
<p>Open {K_settings} → {K_language} and pick the one you want. The app, its widgets and the Share extension follow straight away.</p>
""",

"s.contact.h": "Contact",
"s.contact.b": """
<p>Questions, a bug, or something that should work and doesn't? Write to us and a person will reply.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Include your device model, the iOS version, the app version (shown at the bottom of {K_settings}) and what you expected to happen. Please don't send your captures or recordings unless we ask. We rarely need them.</span></div></div>
<p style="margin-top:16px" class="small">Billing, refunds and subscription changes are handled by Apple: <a href="https://apps.apple.com/account/subscriptions">manage subscriptions</a> · <a href="https://support.apple.com/billing">request a refund</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "About Second Brain",
"a.h1": "Just say it. We'll sort it out.",
"a.sub": "Talk the way you think. Second Brain turns it into tasks, events, notes and ideas, keeps your original, and finds it again when you ask.",
"a.cta": "Support",
"a.meta": "iPhone and iPad · iOS 18+ · eight languages · works without an account",
"a.lead": "Second Brain is a calm place for everything on your mind. Capture it in seconds by voice or text, check what Smart fill made of it, and ask your Brain when you need it back, with sources you can open and check.",

"a.f1.icon": "mic",
"a.f1.h": "Just say it.",
"a.f1.p": "Voice capture starts listening the moment it opens, in eight languages. Every task, plan and idea is caught as you speak, and the original is kept.",
"a.f2.icon": "sparkle",
"a.f2.h": "One sentence. Three things done.",
"a.f2.p": "Smart fill turns what you said into tasks, events and notes with dates and times filled in. You check every field before anything is created.",
"a.f3.icon": "chat",
"a.f3.h": "Ask anything.",
"a.f3.p": "Answers come only from what you saved, with the sources listed so you can open and check them.",
"a.f4.icon": "calendar",
"a.f4.h": "Your day, and your week.",
"a.f4.p": "What's due and what's next on one calm screen, with your Apple Calendar beside your tasks, reminders and an optional morning summary.",
"a.f5.icon": "undo",
"a.f5.h": "Nothing is lost.",
"a.f5.p": "Your original words stay next to everything made from them. Any organizing can be undone, and you can export your whole library at any time.",
"a.f6.icon": "lock",
"a.f6.h": "Private by default.",
"a.f6.p": 'On-device AI first, no ads and no tracking. Cloud sync and cloud AI each wait for your yes, and any capture can stay on this iPhone only. <a href="{BASE}{L}/privacy/">How that works.</a>',

"a.price.h": "Plans",
"a.price.b": """
<p>Second Brain is free to use, and saving is never blocked. Light and Pro remove the monthly limits and add sync and cloud AI.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Free</div><div class="price">$0</div><ul><li>Unlimited typed capture, tasks, projects, search, reminders and export</li><li>20 voice captures, 40 Smart fills and 5 questions a month</li><li>On-device AI on supported devices</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">Monthly</div><ul><li>Unlimited voice capture, Smart fill and questions</li><li>Quick mode</li><li>Private iCloud sync</li><li>300 cloud AI captures and 100 cloud answers a month</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">Monthly · Yearly</div><ul><li>Everything in Light</li><li>700 cloud AI captures and 250 cloud answers a month</li><li>A cloud daily summary</li><li>Import a web page's text</li><li>Yearly starts with 7 days free</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Prices are shown in the app and on the App Store for your country. Billing is handled by Apple. <a href="{BASE}{L}/terms/#subscriptions">Subscription terms.</a></p>
""",

"a.platform.h": "Built for Apple devices",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone and iPad</b><span>iOS 18 or iPadOS 18 and later. On-device AI on devices that support Apple Intelligence.</span></div></li>
  <li><span class="tile">{share}</span><div><b>Everywhere you are</b><span>A Share extension to save from any app, Home Screen widgets, Siri and Shortcuts, and optional Spotlight search.</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>Your iCloud, not ours</b><span>Sync runs through your own private iCloud storage, so we never hold a copy of your library.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Eight languages</b><span>English, German, Spanish, French, Japanese, Korean, Brazilian Portuguese and Simplified Chinese, including voice capture. Choose one in {K_settings} → {K_language}.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Privacy Policy",
"p.h1": "Your thoughts stay yours.",
"p.sub": "Second Brain keeps your library on your device. Cloud sync and cloud AI each wait for your yes. This page explains exactly what leaves your device, when it leaves, and who receives it.",
"p.meta": "Effective {DATE} · applies to the Second Brain app for iPhone and iPad, and to this site",

"p.summary.h": "The short version",
"p.summary.b": """
<p class="lead">Second Brain works without an account. <strong>Your library (captures, recordings, attachments, tasks, notes and everything made from them) is stored on your device.</strong> With no account, the app sends us nothing at all.</p>
<p>Three things change that, and each needs your choice:</p>
<ul>
  <li><strong>iCloud sync</strong> (Light and Pro) copies your library to <em>your own</em> private iCloud storage. We cannot read it.</li>
  <li><strong>Cloud AI ("Luna")</strong> sends the text needed for one request through our server to OpenAI, when on-device AI can't help or when you choose Luna. Nothing is sent unless you sign in and turn it on.</li>
  <li><strong>An account</strong> (Sign in with Apple) lets our server keep a small record: an account ID that is a one-way hash, your plan, your consent choices and your usage counts. We never ask Apple for your name or email.</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>No advertising, no analytics, no tracking, and no third-party SDKs in the app. We do not sell or share personal data, and we never use your content to train AI models.</div></div>
<p style="margin-top:16px">This policy applies to the Second Brain app for iPhone and iPad and to this website, both published by {COMPANY} ("we", "us"). The app's own {K_settings} → {K_data_handled} screen says the same in shorter form.</p>
""",

"p.collect.h": "What we collect",
"p.collect.b": """
<p>"Collect" here means data that leaves your device and is kept somewhere we can read it. Data that only reaches your own iCloud storage is not collected by us.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Collected?</th><th>What that means</th></tr>
<tr><td>Contact info</td><td>No</td><td>Sign in with Apple is set up to share no name and no email address with us. There is no email field in the app.</td></tr>
<tr><td>Identifiers</td><td><strong>Only with an account</strong></td><td>An account ID made from a one-way hash of the identifier Apple gives us, and the public key Apple's App Attest creates on each of your devices. No advertising identifier and no device ID are used.</td></tr>
<tr><td>User content</td><td><strong>Only with cloud AI</strong></td><td>The text needed for a request you make to Luna, and its result, kept briefly as described below. Your library itself stays on your device and in your own iCloud.</td></tr>
<tr><td>Purchases</td><td><strong>Only if you subscribe</strong></td><td>The signed transaction Apple sends for your plan: product, dates, trial and renewal status. We never see payment details.</td></tr>
<tr><td>Usage data</td><td><strong>Only with an account</strong></td><td>Counts of cloud AI requests and their size, so the monthly allowance can be applied. No analytics and no record of how you use the app.</td></tr>
<tr><td>Location, contacts, health, browsing, search history, diagnostics</td><td>No</td><td>The app does not request location or contacts and contains no crash reporter or analytics.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> none. We do not link data about you with other companies' data, show ads, or share anything with data brokers. The app never shows Apple's tracking prompt because it has nothing to ask.</p>
""",

"p.device.h": "What stays on your device",
"p.device.b": """
<p>Second Brain stores your library in its own private storage on your device, protected by iOS data protection and your passcode:</p>
<ul>
  <li><strong>Captures</strong>: what you said or typed, exactly as you said it, plus any corrections you made to it.</li>
  <li><strong>Recordings and attachments</strong>: audio, photos, PDFs, files and links you added, and the text read from them on your device.</li>
  <li><strong>What was made from them</strong>: tasks, events, notes, ideas, projects, review history and undo history.</li>
  <li><strong>Search data</strong>: the meaning-based search index, built on your device with Apple's language models.</li>
  <li><strong>Settings</strong>: language, reminders, widgets, AI choices, and the calendars you picked.</li>
  <li><strong>In the iOS Keychain</strong>: your sign-in session and the monthly count of free voice captures, Smart fills and questions. The count only holds numbers and stays on this device, even if the app is reinstalled.</li>
</ul>
<p>A guest library and each signed-in account have separate stores on the device. If you use iCloud Backup or an encrypted computer backup, Apple may include this data in that backup under your Apple Account. We have no access to it.</p>
<p><strong>Widgets and Spotlight.</strong> Widgets show item titles only if you turn on {K_widgets}. Saved items appear in Spotlight only if you turn on {K_spotlight}. Both stay on your device.</p>
""",

"p.ai.h": "AI on your device, and Luna in the cloud",
"p.ai.b": """
<h3>On-device AI</h3>
<p>On supported devices, Smart fill, organizing, answers and summaries run on Apple's on-device model. What you write does not leave your device, and on-device use never counts against a cloud allowance.</p>
<h3>Luna, our cloud AI</h3>
<p>Luna is a model from <strong>OpenAI</strong> that we call from our own server. Your device never contacts OpenAI directly, and no API key is in the app. Luna runs only if you have <strong>signed in and turned on {K_luna}</strong>. It is used when on-device AI is unavailable or can't complete a request, or first if you have Light or Pro and chose Luna as your engine. Turning the switch off stops new cloud AI requests straight away.</p>
<p>For each request, only the text needed for it is sent:</p>
<ul>
  <li><strong>Organizing and Smart fill</strong>: the text of the capture being organized, including text read on your device from an attached photo or PDF, your time zone and language, and the names and short summaries of up to 30 of your projects.</li>
  <li><strong>Ask your Brain</strong>: your question and short excerpts from up to 12 saved items your device picked as relevant.</li>
  <li><strong>Tidy-up</strong> (Light and Pro): the text of the note you asked to tidy.</li>
  <li><strong>Daily summary</strong> (Pro): counts of what's due and short excerpts from up to 10 of your items for that day.</li>
</ul>
<p><strong>Never sent:</strong> audio, images or files themselves; captures marked {K_device_only}; your Apple Calendar events; your name or email (we don't have them); any identifier that could tell OpenAI who you are.</p>
<h3>How long it is kept</h3>
<p>Our server keeps a result for <strong>up to 24 hours</strong>, so a request that is interrupted can be finished without running it, or charging your allowance, twice. After that the text is removed, and a content-free receipt (a one-way hash of the request, the IDs of the items it used, and the time) is kept for up to a year for allowance accounting. Permanently deleting an item also removes any results made from it, and deleting your account removes them all.</p>
<p>We ask OpenAI not to store responses. Under its API terms, OpenAI does not use this data to train its models. It may keep inputs and outputs for a limited time to monitor for abuse, as described in its <a href="https://openai.com/enterprise-privacy/">API data policies</a>.</p>
<p>AI-generated suggestions and answers can be wrong. That is why every Smart fill field can be checked before it is saved, and every answer lists its sources.</p>
""",

"p.sync.h": "iCloud sync",
"p.sync.b": """
<p>With Light or Pro, you can turn on {K_sync}. Your library, including captures, items, projects, corrections, history and attachments, is then stored in a <strong>private CloudKit database in your own iCloud account</strong>, so your devices stay in step. Apple stores it under its own <a href="https://www.apple.com/legal/privacy/">privacy policy</a>. We, the developer, cannot read your private iCloud data, and our server never receives a copy of your library.</p>
<p>Captures marked {K_device_only} are never synced. When sync is on, iOS may deliver silent notifications from Apple's push service to tell the app that something changed. No push token is sent to us.</p>
""",

"p.account.h": "Your account and our server",
"p.account.b": """
<p>An account is optional. When you sign in with Apple, we request <strong>no name and no email</strong>. Our server, which runs on <strong>Cloudflare</strong>, keeps:</p>
<ul>
  <li><strong>An account ID</strong>: a one-way hash of the identifier Apple gives us. The original Apple identifier is not stored.</li>
  <li><strong>Sign-in data</strong>: sessions, stored only as hashes and expiring after 30 days, and Apple's sign-in token, encrypted and used only to revoke it when you delete your account.</li>
  <li><strong>Device check</strong>: the public key Apple's App Attest creates on each device you sign in on (up to 20), so the server knows it is talking to a genuine copy of Second Brain.</li>
  <li><strong>Your choices and plan</strong>: whether sync and cloud AI are on, your plan and its renewal dates, and the transactions Apple sends to confirm it.</li>
  <li><strong>Usage counts</strong>: how much of this month's cloud allowance you have used.</li>
  <li><strong>Cloud AI results</strong>, kept briefly as described above.</li>
</ul>
<p>To protect the service from abuse, the server briefly holds a one-way hash of your IP address combined with the current minute. It is deleted within minutes. We keep no request logs, and our server never receives your library.</p>
<p><strong>Page import</strong> (Pro): when you ask to import a web page's text, our server fetches that public page itself and returns its readable text to your device. The page's address and text are not stored and are not sent to Luna.</p>
""",

"p.voice.h": "Voice, speech and recordings",
"p.voice.b": """
<p>Voice capture uses the microphone only while you are recording. Speech is transcribed <strong>on your device</strong> with Apple's speech recognition. Your recording is not sent to Apple or to us for transcription, although the first use of a language downloads Apple's speech files.</p>
<p>Recordings are kept in your library. Once a transcript is complete, the audio is deleted <strong>7 days</strong> after saving unless you tap {K_keep_recording}. A recording whose transcript failed stays until you delete it. Transcripts stay after their audio is gone.</p>
""",

"p.permissions.h": "Permissions",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>Permission</th><th>Used for</th></tr>
<tr><td>Microphone, Speech Recognition</td><td>Voice capture and on-device transcription.</td></tr>
<tr><td>Camera, Photos</td><td>Taking or choosing a picture to attach. Only the pictures you pick are read.</td></tr>
<tr><td>Calendars</td><td>Asked only if you tap {K_calendars}. The calendars you choose are read on your device to show next to your tasks, and are never uploaded. A new event is added to Apple Calendar only through Apple's own editor, after you confirm it.</td></tr>
<tr><td>Notifications</td><td>Reminders, the morning summary and a reminder before a free trial ends. All are scheduled on your device.</td></tr>
</table></div>
<p style="margin-top:14px">You can change any of these in iOS {K_settings} → Second Brain. The app never asks for your location or contacts.</p>
""",

"p.purchases.h": "Purchases",
"p.purchases.b": """
<p>Light and Pro are sold through Apple's App Store. Payment happens between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>, and we never see your payment details. You can buy a plan without an account: your iPhone checks the transaction Apple signs, and our server keeps nothing about the purchase. If you sign in, our server checks that transaction and stores it with your account, so the plan can follow you to your other devices. A purchase made without an account is linked to the first account that sends it. Our server also receives Apple's notices about renewals, refunds and cancellations, and applies them only to purchases linked to an account, so your plan stays correct.</p>
""",

"p.third.h": "Service providers",
"p.third.b": """
<p>Second Brain contains <strong>no third-party SDKs</strong>: no analytics, no advertising and no crash reporter. These companies process data for us, each only for the purpose listed:</p>
<ul>
  <li><strong>Apple</strong>: Sign in with Apple, App Attest, the App Store and purchases, iCloud sync in your own account, push delivery for sync, and the on-device AI and speech models.</li>
  <li><strong>Cloudflare</strong>: hosts our server and its database, and routes requests to it.</li>
  <li><strong>OpenAI</strong>: runs Luna for the cloud AI requests you allow, as described above.</li>
</ul>
<p>We do not sell or rent personal data, and we share nothing with advertisers or data brokers. We may disclose information if the law requires it. Because we hold so little, there is little we could disclose.</p>
""",

"p.retention.h": "How long we keep it",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>Data</th><th>Kept</th></tr>
<tr><td>Your library on your device</td><td>Until you delete it. Items you delete stay in {K_recently_deleted} for 30 days.</td></tr>
<tr><td>Voice recordings</td><td>7 days after a completed transcript unless you keep them. Until you delete them if transcription failed.</td></tr>
<tr><td>Your iCloud copy</td><td>Until you delete it or your account. It is stored by Apple in your iCloud.</td></tr>
<tr><td>Cloud AI result</td><td>Up to 24 hours. A content-free receipt is kept for up to 1 year.</td></tr>
<tr><td>Sign-in sessions</td><td>30 days from last refresh</td></tr>
<tr><td>Account, plan and usage counts</td><td>While your account exists</td></tr>
<tr><td>Hashed IP address for abuse protection</td><td>A few minutes</td></tr>
<tr><td>Server backups</td><td>Our hosting provider's database backups may hold deleted data for up to 30 days before they expire.</td></tr>
</table></div>
""",

"p.delete.h": "Export and deletion",
"p.delete.b": """
<p>Everything is in your hands, inside the app:</p>
<ul>
  <li><strong>Export</strong>: {EXPORT} creates a ZIP with your whole library, your original files and a list of anything that couldn't be included.</li>
  <li><strong>Delete from this device</strong>: {DELETE_LOCAL} removes the library on this device. It does not delete your account or its iCloud copy.</li>
  <li><strong>Delete your account</strong>: {DELETE_ACCOUNT} deletes your iCloud copy, everything our server holds about the account, and the account's library on this device, and revokes Second Brain's Sign in with Apple access.</li>
</ul>
<p>After an account is deleted, our server keeps only a content-free marker: the hashed account ID flagged as deleted, its usage counts, and one-way hashes of its purchase and device identifiers. That marker lets an interrupted deletion finish and stops a purchase or the free cloud sample being claimed twice. It contains no content, name or email. Step-by-step instructions are on the <a href="{BASE}{L}/delete-data/">Your data</a> page.</p>
""",

"p.rights.h": "Your rights",
"p.rights.b": """
<p>Depending on where you live, including under the GDPR, the UK GDPR and California's CCPA/CPRA, you have the right to access, correct, export, restrict, object to and erase personal data we hold about you, to withdraw consent at any time, and to complain to your data protection authority. Most of these rights are built into the app: export, delete, and the sync and cloud AI switches. For anything else, write to {MAIL} and we will respond within 30 days.</p>
<p>Where the GDPR applies, we rely on: <strong>contract</strong> to provide the features you use and the plan you bought; <strong>consent</strong> for iCloud sync and cloud AI, which you can withdraw with their switches; <strong>legitimate interests</strong> in keeping the service secure and preventing abuse (App Attest and abuse protection); and <strong>legal obligation</strong> for purchase records.</p>
""",

"p.children.h": "Children",
"p.children.b": """
<p>Second Brain is not directed at children under 13, or under the age of digital consent where you live. We do not knowingly collect personal data from children. If you believe a child has created an account, write to {MAIL} and we will help delete it.</p>
""",

"p.transfers.h": "Where data is processed",
"p.transfers.b": """
<p>Cloudflare runs our server on its global network, and OpenAI and Apple may process data in the United States and other countries. Where the law requires it, these transfers are covered by the providers' data processing terms, including standard contractual clauses. Data stored on your device stays where your device is.</p>
""",

"p.changes.h": "Changes to this policy",
"p.changes.b": """
<p>If the app changes what it does with data, we will update this policy and the date at the top. We will mention material changes in the app's release notes and, where the law requires, ask for your consent again. We will never start sending your content anywhere new without a new choice from you.</p>
""",

"p.contact.h": "Contact",
"p.contact.b": """
<p>{COMPANY}, the publisher of Second Brain, is the controller of the personal data described here. For privacy questions or requests, write to {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Terms of Use",
"t.h1": "The agreement, in plain words.",
"t.sub": "What Second Brain does, what its AI can and can't promise, how your content is treated, and how Light and Pro are billed.",
"t.meta": "Effective {DATE} · Second Brain by {COMPANY}",

"t.acceptance.h": "1. Acceptance of Terms",
"t.acceptance.b": """
<p>These Terms of Use ("Terms") are an agreement between you and {COMPANY} ("we", "us"), the publisher of the Second Brain app for iPhone and iPad ("Second Brain" or "the app") and its related online services. By installing or using Second Brain you accept these Terms and our <a href="{BASE}{L}/privacy/">Privacy Policy</a>. If you do not agree, do not use the app.</p>
""",
"t.who.h": "2. Who may use Second Brain",
"t.who.b": """
<p>You must be at least 13 years old, or the age of digital consent where you live, to use Second Brain. If you are under the age of majority where you live, you need a parent's or guardian's permission to buy a subscription.</p>
""",
"t.what.h": "3. What Second Brain is, and is not",
"t.what.b": """
<p>Second Brain is a personal tool for capturing thoughts by voice or text and organizing them into tasks, events, notes and ideas, with reminders, search and answers drawn from what you saved.</p>
<p>Second Brain is <strong>not</strong> a medical, legal, financial or other professional service, and nothing it produces is professional advice. Do not rely on it as the only way to remember something critical, such as medication, a legal deadline or a safety matter. Reminders depend on iOS, your settings and your device, and may not arrive. In an emergency, contact your local emergency services.</p>
""",
"t.account.h": "4. Your account",
"t.account.b": """
<p>An account is optional and uses Sign in with Apple. You are responsible for your Apple Account, your device and its passcode, and for activity under your account. Each account is for one person. You can sign out at any time, and you can delete your account in the app, as described on the <a href="{BASE}{L}/delete-data/">Your data</a> page.</p>
""",
"t.content.h": "5. Your content",
"t.content.b": """
<p>Everything you capture, attach or write in Second Brain ("your content") remains yours. We claim no ownership of it. You give us only the limited permission needed to process your content to provide the features you choose: for example, to send text to Luna when you have turned cloud AI on, or to fetch a web page you asked to import. We do not use your content to train AI models, and we do not sell it.</p>
<p>You are responsible for your content and for having the right to capture, import and store it, including anything about other people. Your library lives on your device and, if you choose, in your own iCloud. Keep your own exports. We do not hold a copy of your library and cannot restore it if your device and iCloud copies are lost.</p>
""",
"t.ai.h": "6. AI features",
"t.ai.b": """
<p>Second Brain uses artificial intelligence to suggest how to organize what you capture, to fill in details such as dates and times, to answer questions from your library, and to write summaries. It uses Apple's on-device model where available and, if you allow it, <strong>Luna</strong>, a cloud model provided by OpenAI through our server.</p>
<p><strong>AI output can be wrong, incomplete or out of date.</strong> It may misread a date, miss a task or misstate what a source says. Check suggestions before you create them, and check an answer's sources before relying on it. If you turn on {K_quick}, items are created without that review, at your own choice. Anything Smart fill isn't sure about goes to {K_needs_review}, and {K_undo} remains available.</p>
<p>You agree not to use the AI features to produce unlawful, harmful or infringing content, or to try to extract the underlying models, their instructions or our service's keys. We may change the models we use, adjust limits, or pause a feature to protect the service. When we do, the rest of the app keeps working and your saved content is not affected.</p>
""",
"t.cloud.h": "7. Cloud features and allowances",
"t.cloud.b": """
<p><strong>Sync</strong> uses your own iCloud account and depends on Apple's service, your iCloud storage and your connection. <strong>Cloud AI</strong> is limited by your plan's monthly allowance: Light includes 300 cloud AI captures and 100 cloud answers a month, Pro includes 700 and 250, and a signed-in free account gets a one-time sample. Allowances reset each calendar month and unused amounts do not carry over. To keep the service fair, there is also a limit on the total amount of text processed each month. <strong>Page import</strong> (Pro) only fetches public pages, and you are responsible for having the right to use what you import.</p>
<p>We work to keep cloud features available, but we do not guarantee they will be uninterrupted. On-device features keep working without them.</p>
""",
"t.subscriptions.h": "8. Subscriptions and billing",
"t.subscriptions.b": """
<p>Second Brain is free to download and use, with monthly limits on voice capture, Smart fill and Ask your Brain on each device. Saving what you capture is never blocked. Paid plans are auto-renewing subscriptions sold through Apple, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Light Monthly</strong>: billed monthly.</li>
  <li><strong>Pro Monthly</strong>: billed monthly.</li>
  <li><strong>Pro Yearly</strong>: billed yearly, beginning with a <strong>7-day free trial</strong> for eligible new subscribers.</li>
</ul>
<p>You can subscribe without a Second Brain account. Without one, the plan's on-device features work on iPhones that use the Apple Account you subscribed with. Signing in with Apple links the plan to your account and adds its cloud features. Payment is charged to your Apple Account when you confirm the purchase. A free trial converts to a paid subscription unless you cancel at least 24 hours before it ends. Subscriptions renew automatically at the same price and period unless auto-renew is turned off at least 24 hours before the end of the current period. Your Apple Account is charged for renewal within the 24 hours before that period ends. You can manage or cancel a subscription in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a> or from {K_manage} in the app. Cancellation takes effect at the end of the current period. Refunds are handled by Apple under its policies. Use {K_restore} to recover a plan on another device. Subscriptions are not shared through Family Sharing.</p>
<p><strong>If a subscription ends</strong>, nothing you saved is removed. Reading, editing, search, export and deletion keep working, the free monthly limits apply again, and sync and cloud allowances stop. Deleting the app or your account does not cancel a subscription. Cancel it with Apple. We may change prices or the features of a plan. Apple will tell you before a price increase applies to you, as its rules require.</p>
""",
"t.licence.h": "9. Licence and intellectual property",
"t.licence.b": """
<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to use Second Brain on Apple devices you own or control, under these Terms and the App Store's Usage Rules. Second Brain, its name, design, artwork (including the brain character), text and code belong to {COMPANY} and are protected by law. You may not copy, modify, distribute, sell, lease, reverse-engineer or create derivative works of the app, except where the law expressly allows it.</p>
""",
"t.use.h": "10. Acceptable use",
"t.use.b": """
<p>You agree not to: use Second Brain unlawfully or to store content you have no right to hold; interfere with, overload or probe our servers; get around allowances, App Attest or the App Store's purchase system; access another person's account; or use the service to harass, harm or record people without the consent the law requires.</p>
""",
"t.termination.h": "11. Termination",
"t.termination.b": """
<p>You can stop using Second Brain at any time, and you can delete your account in the app. We may suspend or end access to cloud features if you seriously or repeatedly breach these Terms, or if the law requires it. Where we can, we will tell you first. Your content on your device stays yours to export. Sections 5, 6, 9, 12, 13 and 15 survive termination.</p>
""",
"t.warranty.h": "12. Warranties and liability",
"t.warranty.b": """
<p>Second Brain is provided "as is" and "as available", without warranties of any kind, express or implied. We do not warrant that AI output will be accurate, that reminders will always arrive, that sync or cloud features will be uninterrupted, or that the app will be error-free. To the fullest extent the law allows, {COMPANY} is not liable for indirect, incidental, special, consequential or punitive damages, or for loss of data, profits or opportunities, arising from your use of or inability to use the app, including anything an AI feature produced or a reminder that did not arrive. Where liability cannot be excluded, it is limited to the amount you paid for Second Brain in the twelve months before the claim. Nothing in these Terms limits rights you have as a consumer that cannot be waived.</p>
""",
"t.apple.h": "13. Apple",
"t.apple.b": """
<p>Second Brain is distributed through the Apple App Store. These Terms are between you and {COMPANY}, not Apple. Apple has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to it, including product-liability, legal-compliance or intellectual-property claims. If the app fails to conform to any applicable warranty, you may notify Apple, and Apple will refund the purchase price, if any. To the maximum extent the law allows, Apple has no other warranty obligation for the app. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them against you. Where these Terms are silent, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a> applies. You confirm that you are not in a country subject to a U.S. government embargo or on a U.S. list of prohibited or restricted parties, and you must comply with any applicable third-party terms when using the app.</p>
""",
"t.changes.h": "14. Changes to these Terms",
"t.changes.b": """
<p>We may update these Terms as Second Brain changes. The date at the top will change when we do, and we will mention material changes in the app's release notes. Continued use after an update means you accept the revised Terms. If you do not, you can stop using the app and delete your account.</p>
""",
"t.law.h": "15. Governing law",
"t.law.b": """
<p>These Terms are governed by the laws of Pakistan, where {COMPANY} operates, without regard to conflict-of-law rules. If the law of your country of residence gives you protections that cannot be contracted out of, those protections still apply.</p>
""",
"t.contact.h": "16. Contact",
"t.contact.b": """
<p>Questions about these Terms: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Your data",
"d.h1": "Export or delete your data",
"d.sub": "Your library is on your device and, if you chose sync, in your own iCloud. Here is how to take a copy, delete it from one device, or delete your account and everything it holds.",
"d.meta": 'See also the <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"d.where.h": "What is stored where",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Captures, recordings, attachments, tasks, notes, projects, history</td><td>Your device</td><td>{DELETE_LOCAL}, or delete your account (below)</td></tr>
<tr><td>The same library, if you turned on sync</td><td>A private database in your own iCloud</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Account ID, plan, consent choices, usage counts, device keys</td><td>Our server (Cloudflare)</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Cloud AI results</td><td>Our server, for up to 24 hours</td><td>Removed on their own, when you permanently delete the item, or when you delete your account</td></tr>
<tr><td>Monthly free-use count</td><td>The iOS Keychain on this device (numbers only)</td><td>Resets every month. iOS may keep it after the app is deleted</td></tr>
<tr><td>Subscription</td><td>Your Apple Account</td><td>Cancel with Apple (below)</td></tr>
</table></div>
""",
"d.export.h": "Take a copy first",
"d.export.b": """
<ol class="steps">
  <li><div>Open Second Brain and go to {K_settings}.</div></li>
  <li><div>Tap {K_export}, then {K_share_export}.</div></li>
  <li><div>Save the ZIP to Files or send it where you like. It contains your library (as JSON, Markdown and a tasks CSV), your original files, and a list of anything that couldn't be included.</div></li>
</ol>
""",
"d.local.h": "Delete from this device",
"d.local.b": """
<p>To delete one item, delete it and then remove it from {K_settings} → {K_recently_deleted} with {K_delete_permanently}. Otherwise it is removed automatically after 30 days.</p>
<p>To delete the whole library on this device, use {DELETE_LOCAL}. This does <strong>not</strong> delete your account, its iCloud copy, or a separate guest library. Deleting the app removes its data from the device, too.</p>
""",
"d.account.h": "Delete your account",
"d.account.b": """
<ol class="steps">
  <li><div>Open {K_settings} → {K_cloud_choices}.</div></li>
  <li><div>Tap {K_delete_account} and confirm.</div></li>
  <li><div>Second Brain deletes the account's iCloud copy, everything our server holds about the account (sessions, plan, choices, usage counts, device keys and AI results), and the account's library on this device. It also revokes its Sign in with Apple access. Your separate guest library stays on the device.</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>If your sign-in has expired, the app asks you to sign in again with the same Apple Account to finish. If you no longer have the device, install Second Brain on any iPhone or iPad, sign in with the same Apple Account and delete from there.</div></div>
<p style="margin-top:16px">Afterwards our server keeps only a content-free marker: the hashed account ID flagged as deleted, its usage counts, and one-way hashes of its purchase and device identifiers. That lets an interrupted deletion finish and stops a purchase or the free sample being claimed twice. Database backups held by our hosting provider expire within 30 days.</p>
""",
"d.subscription.h": "Your subscription",
"d.subscription.b": """
<p>Deleting your data, your account or the app does <strong>not</strong> cancel a subscription. It belongs to your Apple Account. Cancel it in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>, and it stays active until the end of the current period. Refunds are handled by <a href="https://support.apple.com/billing">Apple Support</a>.</p>
""",
"d.email.h": "Ask us",
"d.email.b": """
<p>If you can't use the app, or have any question about your data, write to {MAIL}. We will reply within 30 days. We hold no name or email for your account, so we will work with you to find it. The quickest route is usually signing in on any device and deleting there. Please don't send us your captures or recordings. We don't need them to help.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "We couldn't find that page.",
"nf.sub": "Even a second brain forgets a link now and then.",
"nf.cta": "Back to Support",
"nf.b": 'That page isn\'t here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.',

}
