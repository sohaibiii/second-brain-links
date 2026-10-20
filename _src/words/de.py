# -*- coding: utf-8 -*-
"""German (de). English is the fallback; k.* are the app's own labels."""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Support",
"nav.about": "Über die App",
"nav.privacy": "Datenschutz",
"nav.terms": "Nutzungsbedingungen",
"nav.data": "Deine Daten",

"ui.skip": "Zum Inhalt springen",
"ui.pages": "Seiten",
"ui.footer": "Fußzeile",
"ui.lang": "Sprache",
"ui.toc": "Auf dieser Seite",
"ui.rights": "Alle Rechte vorbehalten.",
"ui.store_soon": "Bald im App Store",
"ui.store_get": "Laden im App Store",
"ui.date": "16. Oktober 2026",
"ui.last_updated": "Zuletzt aktualisiert: {DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "Diese Übersetzung dient nur der besseren Verständlichkeit. Weicht sie von der englischen Fassung ab, gilt die englische Fassung.",

# The app's own words, copied from SecondBrain/Localizable.xcstrings. Do not retranslate.
"k.settings": "Einstellungen",
"k.cloud_choices": "Cloud-Synchronisierung und KI-Optionen",
"k.account": "Dein Account",
"k.delete_account": "Account und Bibliothek löschen",
"k.keep_account": "Account behalten",
"k.delete_local": "Alle lokalen Daten löschen",
"k.export": "Export vorbereiten",
"k.share_export": "Bibliotheksexport teilen",
"k.recently_deleted": "Zuletzt gelöscht",
"k.delete_permanently": "Endgültig löschen",
"k.data_handled": "So werden deine Daten verarbeitet",
"k.privacy_screen": "Deine Privatsphäre",
"k.sync": "Meine Bibliothek synchronisieren",
"k.sync_now": "Jetzt synchronisieren",
"k.luna": "Luna zum Organisieren und Antworten nutzen",
"k.on_device": "KI auf dem Gerät",
"k.language": "Sprache",
"k.restore": "Käufe wiederherstellen",
"k.manage": "Abo verwalten",
"k.sign_out": "Abmelden und Gastbibliothek öffnen",
"k.keep_recording": "Diese Aufnahme behalten",
"k.needs_review": "Zu prüfen",
"k.smart_org": "Smarte Organisation",
"k.smart_fill": "Smart Fill",
"k.quick": "Schnellmodus",
"k.ask": "Frag deine Notizen",
"k.calendars": "Kalender-App verbinden",
"k.morning": "Morgenüberblick",
"k.reminders": "Erinnerungsmitteilungen",
"k.spotlight": "Gespeicherte Einträge in Spotlight zeigen",
"k.device_only": "Nur auf diesem iPhone behalten",
"k.undo": "Widerrufen",
"k.widgets": "Titel in Widgets anzeigen",

"meta.support.title": "Second Brain: Voice Planner – Support",
"meta.support.desc": "Offizieller Support für Second Brain: wie Festhalten, Smart Fill und „Frag deine Notizen“ funktionieren, was die App braucht, Antworten auf häufige Fragen und wie du uns erreichst.",
"meta.about.title": "Second Brain: Voice Planner — Aufgaben & Notizen mit privater KI",
"meta.about.desc": "Second Brain macht aus dem, was du sagst oder tippst, Aufgaben, Termine, Notizen und Ideen, behält dein Original und beantwortet Fragen aus dem, was du gespeichert hast – zuerst mit KI auf dem Gerät.",
"meta.privacy.title": "Datenschutzerklärung – Second Brain: Voice Planner",
"meta.privacy.desc": "Was Second Brain auf deinem Gerät behält, was in iCloud landet, was unser Server speichert und wann genau deine Worte für Cloud-KI gesendet werden.",
"meta.terms.title": "Nutzungsbedingungen – Second Brain: Voice Planner",
"meta.terms.desc": "Nutzungsbedingungen (EULA) für Second Brain: deine Inhalte, die KI-Funktionen, Cloud-Kontingente und wie Light- und Pro-Abos abgerechnet werden.",
"meta.data.title": "Deine Daten löschen – Second Brain: Voice Planner",
"meta.data.desc": "So exportierst du deine Bibliothek, löschst sie von diesem Gerät und löschst deinen Account bei Second Brain samt allem, was er in iCloud und auf unserem Server enthält.",
"meta.nf.title": "Nicht gefunden – Second Brain: Voice Planner",
"meta.nf.desc": "Seite nicht gefunden.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Support",
"s.h1": "Hilfe zu Second Brain",
"s.sub": "Sag es oder tipp es, und Second Brain sortiert es in Aufgaben, Termine, Notizen und Ideen, behält dein Original und lässt dich jede Änderung widerrufen. Hier erfährst du, wie es funktioniert, was es braucht und wie du uns erreichst.",
"s.cta": "Häufige Fragen lesen",
"s.meta": 'Funktioniert ohne Account · zuerst KI auf dem Gerät · <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>',

"s.how.h": "So funktioniert Second Brain",
"s.how.b": """
<p class="lead">Bring es in Sekunden aus dem Kopf und finde es wieder, wenn es darauf ankommt.</p>
<p>Tippe auf das Mikrofon und sprich, wie du denkst – oder schreib. Second Brain speichert zuerst deine Worte, genau so, wie du sie gesagt hast, damit nichts verloren geht. Dann schlägt es vor, was darin steckt: eine Aufgabe mit Fälligkeitsdatum, ein Termin mit Uhrzeit, eine Notiz oder eine Idee, abgelegt im richtigen Projekt. Du prüfst jeden Vorschlag, bevor etwas erstellt wird, und jede Änderung lässt sich widerrufen.</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>Festhalten</b><span>Die Sprachaufnahme beginnt, sobald sie sich öffnet. Du kannst auch tippen, Text, Links, Fotos oder Dateien aus anderen Apps teilen oder sie an einen Gedanken anhängen.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>Smart Fill und Prüfen</b><span>Tippe auf „Fertig“, und Smart Fill entwirft Aufgaben, Termine, Notizen und Ideen samt Datum und Uhrzeit. Jedes Feld lässt sich bearbeiten, bevor du die Einträge erstellst. Alles, wobei sich Smart Fill nicht sicher ist, bleibt markiert oder landet unter {K_needs_review}.</span></div></li>
  <li><span class="tile">{chat}</span><div><b>Frag deine Notizen</b><span>Stell eine Frage in ganz normalen Worten. Antworten stammen nur aus dem, was du gespeichert hast, und die Quellen werden aufgelistet, damit du sie öffnen und prüfen kannst.</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>Heute und Kalender</b><span>Was fällig ist, was als Nächstes ansteht und was wichtig ist, dazu eine Wochenansicht mit deiner Kalender-App neben deinen Aufgaben. Optional mit Erinnerungen und einem Morgenüberblick.</span></div></li>
  <li><span class="tile">{undo}</span><div><b>Dein Original, immer</b><span>Die Worte, die du festgehalten hast, bleiben in deiner Bibliothek neben allem, was daraus entstanden ist. {K_undo} nimmt jedes Organisieren zurück, und gelöschte Einträge warten 30 Tage lang unter {K_recently_deleted}.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Privat von Anfang an</b><span>Organisieren und Antworten laufen mit Apples Modell auf deinem Gerät, wenn dein Gerät es unterstützt. Cloud-Synchronisierung und Cloud-KI bleiben aus, bis du dich dafür entscheidest. Siehe <a href="{BASE}{L}/privacy/">Datenschutz</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Voraussetzungen",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Gerät</th><td><strong>iPhone oder iPad</strong> mit <strong>iOS 18 oder iPadOS 18</strong> oder neuer.</td></tr>
<tr><th>KI auf dem Gerät</th><td>Ein Gerät, das <strong>Apple Intelligence</strong> unterstützt, mit iOS 26 oder iPadOS 26 oder neuer, eingeschalteter Apple Intelligence und heruntergeladenem Modell. Auf anderen Geräten kannst du trotzdem Gedanken festhalten, von Hand organisieren, suchen und Erinnerungen einstellen. Smart Fill und Antworten können dann Luna in der Cloud nutzen, wenn du dich anmeldest und es erlaubst.</td></tr>
<tr><th>Account</th><td><strong>Optional.</strong> Festhalten, Organisieren, Suche, Export und Löschen funktionieren ohne Account, und auch Light oder Pro kannst du ohne Account kaufen. „Mit Apple anmelden“ brauchst du, um mit iCloud zu synchronisieren, Luna zu nutzen oder Seitentext zu importieren.</td></tr>
<tr><th>Internet</th><td>Nicht nötig zum Festhalten, für KI auf dem Gerät, Suche oder Export. Nötig für die Anmeldung, Käufe, iCloud-Synchronisierung, Luna, den Seitenimport und den ersten Download von Apples Sprachdateien für deine Sprache.</td></tr>
<tr><th>Berechtigungen</th><td>Mikrofon und Spracherkennung für die Sprachaufnahme. Kamera oder Fotos nur, wenn du ein Bild anhängst. Kalender nur, wenn du die Kalender-App verbindest. Mitteilungen nur für Erinnerungen und den Morgenüberblick. Jede Berechtigung wird erst abgefragt, wenn du sie zum ersten Mal brauchst.</td></tr>
<tr><th>iCloud</th><td>Für die Synchronisierung ein iCloud-Account mit genug freiem Speicherplatz. Die Synchronisierung ist in Light und Pro enthalten.</td></tr>
<tr><th>Sprachen</th><td>Englisch, Deutsch, Spanisch, Französisch, Japanisch, Koreanisch, brasilianisches Portugiesisch und vereinfachtes Chinesisch. Die Sprachaufnahme hört in der Sprache der App zu. Du wählst sie unter {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Erste Schritte",
"s.start.b": """
<ol class="steps">
  <li><div><b>Öffne Second Brain.</b> Es gibt keine Registrierung. Deine Bibliothek liegt von der ersten Sekunde an auf deinem Gerät.</div></li>
  <li><div><b>Tippe auf das Mikrofon und sag, was dir durch den Kopf geht.</b> Erlaube Mikrofon und Spracherkennung, wenn iOS danach fragt. Oder schreib einfach.</div></li>
  <li><div><b>Tippe auf „Fertig“.</b> Smart Fill entwirft Aufgaben, Termine, Notizen und Ideen. Prüfe jedes Feld, ändere, was du willst, und erstelle dann die Einträge.</div></li>
  <li><div><b>Frag deine Notizen.</b> Frag „Was habe ich Sam versprochen?“ oder „Wann ist der Zahnarzttermin?“ und öffne die genannten Quellen, um nachzuprüfen.</div></li>
  <li><div><b>Optional:</b> Um mit iCloud zu synchronisieren oder Luna zu nutzen, öffne {K_settings} → {K_cloud_choices} und melde dich mit Apple an. Für beides gibt es einen eigenen Schalter.</div></li>
</ol>
""",

"s.faq.h": "Häufige Fragen",
"s.faq.b": """
<dl class="faq">
<dt>Brauche ich einen Account?</dt>
<dd>Nein. Festhalten, Organisieren, Suche, Erinnerungen, Export und Löschen funktionieren alle ohne Account auf deinem Gerät. Einen Account brauchst du nur, um mit iCloud zu synchronisieren, Luna in der Cloud zu nutzen oder Seitentext zu importieren. Einen Plan kannst du auch ohne Account kaufen. Beim Anmelden wird deine bestehende Gastbibliothek nie hochgeladen. Du wählst selbst, welche Gedanken du in den Account kopierst.</dd>
<dt>Was ist kostenlos?</dt>
<dd>Getippte Gedanken, Aufgaben und Projekte, lokale Suche, Transkription auf dem Gerät, Erinnerungen, Bearbeiten, Export und Löschen sind kostenlos und unbegrenzt. Außerdem enthält die kostenlose Nutzung <strong>pro Monat 20 Sprachaufnahmen, 40 Smart Fills und 5 Fragen über {K_ask}</strong>, gezählt auf jedem Gerät und am Monatsersten zurückgesetzt. Speichern wird nie blockiert: Ist ein Limit erreicht, kannst du weiterhin tippen und speichern. Ein angemeldeter Account, der Cloud-KI erlaubt, erhält außerdem einmalig ein Probekontingent von 10 Cloud-KI-Aufnahmen und 5 Antworten.</dd>
<dt>Was bieten Light und Pro zusätzlich?</dt>
<dd><strong>Light</strong> hebt die monatlichen Limits für Sprachaufnahmen, Smart Fill und „Frag deine Notizen“ auf, bietet den {K_quick} und private iCloud-Synchronisierung und enthält pro Monat 300 Cloud-KI-Aufnahmen und 100 Cloud-Antworten. <strong>Pro</strong> bietet pro Monat 700 Cloud-KI-Aufnahmen und 250 Cloud-Antworten, eine Cloud-Tageszusammenfassung und den Import des Texts einer Webseite. Light wird monatlich abgerechnet. Pro gibt es monatlich oder jährlich, und das Jahresabo beginnt für berechtigte Neuabonnenten mit 7 kostenlosen Tagen. Die Preise für dein Land siehst du in der App und im App Store, und die Abrechnung übernimmt Apple.</dd>
<dt>Was ist der Unterschied zwischen KI auf dem Gerät und Luna?</dt>
<dd>KI auf dem Gerät ist Apples Modell, das auf deinem Gerät läuft. Nichts, was du schreibst, verlässt es. Luna ist ein Cloud-Modell von OpenAI, das über unseren Server läuft. Es wird nur genutzt, wenn du dich anmeldest und {K_luna} einschaltest, und nur im Rahmen des Cloud-Kontingents deines Plans. KI auf dem Gerät kommt zuerst. Luna springt ein, wenn dein Gerät nicht weiterhelfen kann. Mit Light und Pro kannst du unter {K_settings} Luna als Haupt-Engine wählen. Gedanken mit {K_device_only} gehen nie an Luna, egal welche Engine du wählst.</dd>
<dt>Was bewirkt „{K_device_only}“?</dt>
<dd>Dieser Gedanke und alles, was daraus entsteht, wird nie mit iCloud synchronisiert und nie für Cloud-KI gesendet. Die KI auf dem Gerät kann ihn trotzdem organisieren.</dd>
<dt>Kann ich den Antworten vertrauen?</dt>
<dd>Antworten entstehen nur aus dem, was du gespeichert hast, und jede Antwort nennt ihre Quellen, damit du sie öffnen kannst. KI kann trotzdem etwas falsch verstehen oder übersehen. Prüfe also die Quellen, bevor du dich bei etwas Wichtigem auf eine Antwort verlässt.</dd>
<dt>Was passiert mit meinen Aufnahmen?</dt>
<dd>Sie werden auf deinem Gerät transkribiert und dafür weder an Apple noch an uns gesendet. Sobald ein Transkript fertig ist, wird das Audio nach 7 Tagen gelöscht, außer du tippst auf {K_keep_recording}. Schlägt ein Transkript fehl, bleibt das Audio erhalten, bis du es löschst, damit du es erneut versuchen kannst. Transkripte bleiben erhalten, auch wenn das Audio gelöscht ist.</dd>
<dt>Wird zwischen meinem iPhone und iPad synchronisiert?</dt>
<dd>Ja, mit Light oder Pro. Melde dich auf beiden Geräten mit demselben Apple Account an und schalte {K_sync} ein. Deine Bibliothek wird über deinen eigenen privaten iCloud-Speicher synchronisiert, den wir nicht lesen können.</dd>
<dt>Was passiert, wenn mein Abo endet?</dt>
<dd>Nichts, was du gespeichert hast, wird entfernt. Lesen, Bearbeiten, Suche, Export und Löschen funktionieren weiter, und die kostenlosen Monatslimits gelten wieder. Synchronisierung und Cloud-Kontingente stehen erst wieder zur Verfügung, wenn du erneut ein Abo abschließt.</dd>
<dt>Wie stelle ich einen Kauf auf einem neuen Gerät wieder her?</dt>
<dd>Verwende auf dem neuen Gerät denselben Apple Account, mit dem du das Abo abgeschlossen hast, und tippe im Bildschirm „Pläne“ auf {K_restore}. Die Funktionen deines Plans auf diesem iPhone sind sofort aktiv. Ist der Plan mit deinem Account bei Second Brain verknüpft, melde dich zusätzlich mit Apple an, um iCloud-Synchronisierung und dein Cloud-Kontingent zurückzubekommen.</dd>
<dt>Kann ich die App in meiner Sprache nutzen?</dt>
<dd>Second Brain spricht acht Sprachen und folgt der Sprache deines Geräts. Um eine andere zu wählen, ohne sonst etwas zu ändern, öffne {K_settings} → {K_language}. Die Sprachaufnahme hört dann in dieser Sprache zu.</dd>
<dt>Wie bekomme ich meine Daten heraus oder lösche sie?</dt>
<dd>Unter {EXPORT} erstellst du eine ZIP-Datei deiner gesamten Bibliothek samt Originaldateien. Unter {DELETE_ACCOUNT} löschst du deinen Account, seine iCloud-Kopie und alles, was unser Server dazu speichert. Details findest du auf der Seite <a href="{BASE}{L}/delete-data/">Deine Daten</a>.</dd>
</dl>
""",

"s.trouble.h": "Fehlerbehebung",
"s.trouble.b": """
<h3>Smart Fill oder Antworten sind nicht verfügbar</h3>
<ul>
  <li>KI auf dem Gerät braucht ein Gerät, das Apple Intelligence unterstützt, iOS 26 oder neuer, eingeschaltete Apple Intelligence in den iOS-Einstellungen und ein vollständig heruntergeladenes Modell. Nach dem ersten Einschalten kann der Download eine Weile dauern.</li>
  <li>Wenn dein Gerät sie nicht ausführen kann, melde dich an und schalte {K_luna} unter {K_settings} → {K_cloud_choices} ein, oder organisiere weiter von Hand. Dein Gedanke wird so oder so gespeichert.</li>
  <li>Wenn du eine Limit-Meldung siehst, hast du die kostenlosen Sprachaufnahmen, Smart Fills oder Fragen dieses Monats auf diesem Gerät aufgebraucht. Sie werden am Monatsersten zurückgesetzt, und Speichern funktioniert weiterhin.</li>
</ul>
<h3>Die Sprachaufnahme transkribiert nicht</h3>
<ul>
  <li>Prüfe in iOS unter {K_settings} → Second Brain die Einstellungen für Mikrofon und Spracherkennung.</li>
  <li>Wenn du eine Sprache zum ersten Mal nutzt, brauchen Apples Sprachdateien eine Internetverbindung zum Herunterladen.</li>
  <li>Schlägt ein Transkript fehl, bleibt die Aufnahme erhalten, damit du es erneut versuchen oder den Text selbst eingeben kannst.</li>
</ul>
<h3>Die Synchronisierung aktualisiert nicht</h3>
<ul>
  <li>Die Synchronisierung braucht Light oder Pro und einen angemeldeten Account, und {K_sync} muss unter {K_settings} → {K_cloud_choices} eingeschaltet sein.</li>
  <li>Achte darauf, dass das Gerät bei iCloud angemeldet ist und freien iCloud-Speicher hat, und tippe dann auf {K_sync_now}.</li>
  <li>Wurde derselbe Eintrag auf zwei Geräten geändert, fragt dich die App, welche Version du behalten möchtest. Dein ursprünglicher Gedanke bleibt immer erhalten.</li>
</ul>
<h3>Erinnerungen kommen nicht an</h3>
<p>In den {K_settings} siehst du, ob {K_reminders} eingeschaltet sind. Wurden sie ausgeschaltet, tippe auf die Zeile, um die iOS-Einstellungen zu öffnen, und erlaube sie dort.</p>
<h3>Mein Plan wird nicht erkannt</h3>
<p>Achte darauf, dass dein iPhone denselben Apple Account verwendet, mit dem du das Abo abgeschlossen hast, und tippe dann auf {K_restore}. Ist der Plan mit deinem Account bei Second Brain verknüpft, melde dich zusätzlich mit Apple an. Erstattungen und Fragen zur Abrechnung bearbeitet Apple über den <a href="https://support.apple.com/billing">Apple Support</a>.</p>
<h3>Die App ist in der falschen Sprache</h3>
<p>Öffne {K_settings} → {K_language} und wähle die gewünschte Sprache. Die App, ihre Widgets und das Teilen-Menü wechseln sofort mit.</p>
""",

"s.contact.h": "Kontakt",
"s.contact.b": """
<p>Fragen, ein Fehler oder etwas, das funktionieren sollte, aber nicht funktioniert? Schreib uns, und ein Mensch antwortet dir.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Nenn uns dein Gerätemodell, die iOS-Version, die App-Version (ganz unten in den {K_settings}) und was du erwartet hast. Bitte schick uns deine Gedanken oder Aufnahmen nur, wenn wir darum bitten. Wir brauchen sie selten.</span></div></div>
<p style="margin-top:16px" class="small">Abrechnung, Erstattungen und Abo-Änderungen übernimmt Apple: <a href="https://apps.apple.com/account/subscriptions">Abos verwalten</a> · <a href="https://support.apple.com/billing">Erstattung anfordern</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Second Brain: Voice Planner",
"a.h1": "Sag es einfach. Wir sortieren es für dich.",
"a.sub": "Sprich, wie du denkst. Second Brain macht daraus Aufgaben, Termine, Notizen und Ideen, behält dein Original und findet es wieder, wenn du fragst.",
"a.cta": "Support",
"a.meta": "Aufgaben & Notizen mit privater KI · iPhone und iPad · iOS 18+ · acht Sprachen · funktioniert ohne Account",
"a.lead": "Second Brain ist ein ruhiger Ort für alles, was dich beschäftigt. Halte es in Sekunden per Sprache oder Text fest, prüfe, was Smart Fill daraus gemacht hat, und frag deine Notizen, wenn du es wieder brauchst – mit Quellen, die du öffnen und prüfen kannst.",

"a.f1.h": "Sag es einfach.",
"a.f1.p": "Die Sprachaufnahme hört zu, sobald sie sich öffnet, in acht Sprachen. Jede Aufgabe, jeder Plan und jede Idee wird beim Sprechen festgehalten, und das Original bleibt erhalten.",
"a.f2.h": "Ein Satz. Drei Dinge erledigt.",
"a.f2.p": "Smart Fill macht aus dem, was du gesagt hast, Aufgaben, Termine und Notizen mit eingetragenem Datum und Uhrzeit. Du prüfst jedes Feld, bevor etwas erstellt wird.",
"a.f3.h": "Frag alles.",
"a.f3.p": "Antworten stammen nur aus dem, was du gespeichert hast, und die Quellen werden aufgelistet, damit du sie öffnen und prüfen kannst.",
"a.f4.h": "Dein Tag und deine Woche.",
"a.f4.p": "Was fällig ist und was als Nächstes kommt, auf einem ruhigen Bildschirm – mit deiner Kalender-App neben deinen Aufgaben, Erinnerungen und einem optionalen Morgenüberblick.",
"a.f5.h": "Nichts geht verloren.",
"a.f5.p": "Deine ursprünglichen Worte bleiben neben allem, was daraus entstanden ist. Jedes Organisieren lässt sich widerrufen, und du kannst deine ganze Bibliothek jederzeit exportieren.",
"a.f6.h": "Privat von Anfang an.",
"a.f6.p": 'Zuerst KI auf dem Gerät, keine Werbung und kein Tracking. Cloud-Synchronisierung und Cloud-KI warten jeweils auf dein Ja, und jeder Gedanke kann ausschließlich auf diesem iPhone bleiben. <a href="{BASE}{L}/privacy/">So funktioniert das.</a>',

"a.price.h": "Pläne",
"a.price.b": """
<p>Second Brain ist kostenlos nutzbar, und Speichern wird nie blockiert. Light und Pro heben die monatlichen Limits auf und bieten Synchronisierung und Cloud-KI.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Kostenlos</div><div class="price">0 $</div><ul><li>Unbegrenzt: getippte Gedanken, Aufgaben, Projekte, Suche, Erinnerungen und Export</li><li>20 Sprachaufnahmen, 40 Smart Fills und 5 Fragen pro Monat</li><li>KI auf dem Gerät auf unterstützten Geräten</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">Monatlich</div><ul><li>Unbegrenzte Sprachaufnahmen, Smart Fill und Fragen</li><li>Schnellmodus</li><li>Private iCloud-Synchronisierung</li><li>300 Cloud-KI-Aufnahmen und 100 Cloud-Antworten pro Monat</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">Monatlich · Jährlich</div><ul><li>Alles aus Light</li><li>700 Cloud-KI-Aufnahmen und 250 Cloud-Antworten pro Monat</li><li>Eine Cloud-Tageszusammenfassung</li><li>Text einer Webseite importieren</li><li>Jahresabo beginnt mit 7 kostenlosen Tagen</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Die Preise für dein Land siehst du in der App und im App Store. Die Abrechnung übernimmt Apple. <a href="{BASE}{L}/terms/#subscriptions">Abo-Bedingungen.</a></p>
""",

"a.platform.h": "Gemacht für Apple-Geräte",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone und iPad</b><span>iOS 18 oder iPadOS 18 und neuer. KI auf dem Gerät auf Geräten, die Apple Intelligence unterstützen.</span></div></li>
  <li><span class="tile">{share}</span><div><b>Überall, wo du bist</b><span>Sichern aus jeder App über das Teilen-Menü, Widgets für den Home-Bildschirm, Siri und Kurzbefehle sowie optional die Spotlight-Suche.</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>Deine iCloud, nicht unsere</b><span>Die Synchronisierung läuft über deinen eigenen privaten iCloud-Speicher, deshalb haben wir nie eine Kopie deiner Bibliothek.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Acht Sprachen</b><span>Englisch, Deutsch, Spanisch, Französisch, Japanisch, Koreanisch, brasilianisches Portugiesisch und vereinfachtes Chinesisch – auch für die Sprachaufnahme. Wähle eine unter {K_settings} → {K_language}.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Datenschutzerklärung",
"p.h1": "Deine Gedanken bleiben deine.",
"p.sub": "Second Brain behält deine Bibliothek auf deinem Gerät. Cloud-Synchronisierung und Cloud-KI warten jeweils auf dein Ja. Diese Seite erklärt genau, was dein Gerät verlässt, wann es das tut und wer es erhält.",
"p.meta": "Gültig ab {DATE} · gilt für die App Second Brain für iPhone und iPad und für diese Website",

"p.summary.h": "Die Kurzfassung",
"p.summary.b": """
<p class="lead">Second Brain funktioniert ohne Account. <strong>Deine Bibliothek (Gedanken, Aufnahmen, Anhänge, Aufgaben, Notizen und alles, was daraus entstanden ist) wird auf deinem Gerät gespeichert.</strong> Ohne Account sendet die App uns überhaupt nichts.</p>
<p>Drei Dinge ändern das, und jedes davon erfordert deine Entscheidung:</p>
<ul>
  <li><strong>iCloud-Synchronisierung</strong> (Light und Pro) kopiert deine Bibliothek in <em>deinen eigenen</em> privaten iCloud-Speicher. Wir können ihn nicht lesen.</li>
  <li><strong>Cloud-KI („Luna“)</strong> sendet den Text, der für eine einzelne Anfrage nötig ist, über unseren Server an OpenAI – wenn die KI auf dem Gerät nicht weiterhelfen kann oder wenn du Luna wählst. Es wird nichts gesendet, solange du dich nicht anmeldest und sie einschaltest.</li>
  <li><strong>Ein Account</strong> („Mit Apple anmelden“) lässt unseren Server einen kleinen Datensatz speichern: eine Account-ID, die ein Einweg-Hash ist, deinen Plan, deine Einwilligungen und deine Nutzungszähler. Wir fragen Apple nie nach deinem Namen oder deiner E-Mail-Adresse.</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>Keine Werbung, keine Analyse, kein Tracking und keine SDKs von Drittanbietern in der App. Wir verkaufen oder teilen keine personenbezogenen Daten und nutzen deine Inhalte nie zum Training von KI-Modellen.</div></div>
<p style="margin-top:16px">Diese Erklärung gilt für die App Second Brain für iPhone und iPad und für diese Website, die beide von {COMPANY} („wir“, „uns“) veröffentlicht werden. Der Bildschirm {K_settings} → {K_data_handled} in der App sagt dasselbe in Kurzform.</p>
""",

"p.collect.h": "Was wir erheben",
"p.collect.b": """
<p>„Erheben“ bedeutet hier: Daten, die dein Gerät verlassen und an einem Ort gespeichert werden, an dem wir sie lesen können. Daten, die nur in deinen eigenen iCloud-Speicher gelangen, werden von uns nicht erhoben.</p>
<div class="table-wrap"><table>
<tr><th>Kategorie</th><th>Erhoben?</th><th>Was das bedeutet</th></tr>
<tr><td>Kontaktdaten</td><td>Nein</td><td>„Mit Apple anmelden“ ist so eingerichtet, dass weder dein Name noch deine E-Mail-Adresse mit uns geteilt werden. In der App gibt es kein E-Mail-Feld.</td></tr>
<tr><td>Kennungen</td><td><strong>Nur mit Account</strong></td><td>Eine Account-ID, die aus einem Einweg-Hash der Kennung entsteht, die Apple uns übermittelt, und der öffentliche Schlüssel, den Apples App Attest auf jedem deiner Geräte erzeugt. Es werden weder eine Werbe-ID noch eine Geräte-ID verwendet.</td></tr>
<tr><td>Nutzerinhalte</td><td><strong>Nur mit Cloud-KI</strong></td><td>Der Text, der für eine Anfrage an Luna nötig ist, und ihr Ergebnis, kurzzeitig gespeichert wie unten beschrieben. Deine Bibliothek selbst bleibt auf deinem Gerät und in deiner eigenen iCloud.</td></tr>
<tr><td>Käufe</td><td><strong>Nur wenn du ein Abo abschließt</strong></td><td>Die signierte Transaktion, die Apple für deinen Plan sendet: Produkt, Datumsangaben, Status von Testphase und Verlängerung. Zahlungsdaten sehen wir nie.</td></tr>
<tr><td>Nutzungsdaten</td><td><strong>Nur mit Account</strong></td><td>Anzahl und Umfang der Cloud-KI-Anfragen, damit das monatliche Kontingent angewendet werden kann. Keine Analyse und keine Aufzeichnung darüber, wie du die App nutzt.</td></tr>
<tr><td>Standort, Kontakte, Gesundheit, Browserverlauf, Suchverlauf, Diagnose</td><td>Nein</td><td>Die App fragt weder Standort noch Kontakte ab und enthält weder Absturzberichte noch Analysewerkzeuge.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> keines. Wir verknüpfen keine Daten über dich mit Daten anderer Unternehmen, zeigen keine Werbung und teilen nichts mit Datenhändlern. Die App zeigt nie Apples Tracking-Abfrage, weil sie nichts zu fragen hat.</p>
""",

"p.device.h": "Was auf deinem Gerät bleibt",
"p.device.b": """
<p>Second Brain speichert deine Bibliothek in einem eigenen privaten Speicher auf deinem Gerät, geschützt durch die Datensicherheit von iOS und deinen Gerätecode:</p>
<ul>
  <li><strong>Gedanken</strong>: was du gesagt oder getippt hast, genau so, wie du es gesagt hast, plus alle Korrekturen, die du daran vorgenommen hast.</li>
  <li><strong>Aufnahmen und Anhänge</strong>: Audio, Fotos, PDFs, Dateien und Links, die du hinzugefügt hast, und der Text, der auf deinem Gerät daraus gelesen wurde.</li>
  <li><strong>Was daraus entstanden ist</strong>: Aufgaben, Termine, Notizen, Ideen, Projekte sowie der Prüf- und Widerrufsverlauf.</li>
  <li><strong>Suchdaten</strong>: der bedeutungsbasierte Suchindex, der auf deinem Gerät mit Apples Sprachmodellen erstellt wird.</li>
  <li><strong>Einstellungen</strong>: Sprache, Erinnerungen, Widgets, KI-Optionen und die Kalender, die du ausgewählt hast.</li>
  <li><strong>Im iOS-Schlüsselbund</strong>: deine Anmeldesitzung und der monatliche Zähler für kostenlose Sprachaufnahmen, Smart Fills und Fragen. Der Zähler enthält nur Zahlen und bleibt auf diesem Gerät, auch wenn die App neu installiert wird.</li>
</ul>
<p>Eine Gastbibliothek und jeder angemeldete Account haben getrennte Speicher auf dem Gerät. Wenn du iCloud-Backup oder ein verschlüsseltes Backup auf einem Computer nutzt, kann Apple diese Daten unter deinem Apple Account in dieses Backup aufnehmen. Wir haben keinen Zugriff darauf.</p>
<p><strong>Widgets und Spotlight.</strong> Widgets zeigen Titel von Einträgen nur, wenn du {K_widgets} einschaltest. Gespeicherte Einträge erscheinen nur in Spotlight, wenn du {K_spotlight} einschaltest. Beides bleibt auf deinem Gerät.</p>
""",

"p.ai.h": "KI auf deinem Gerät und Luna in der Cloud",
"p.ai.b": """
<h3>KI auf dem Gerät</h3>
<p>Auf unterstützten Geräten laufen Smart Fill, Organisieren, Antworten und Zusammenfassungen mit Apples Modell auf dem Gerät. Was du schreibst, verlässt dein Gerät nicht, und die Nutzung auf dem Gerät wird nie auf ein Cloud-Kontingent angerechnet.</p>
<h3>Luna, unsere Cloud-KI</h3>
<p>Luna ist ein Modell von <strong>OpenAI</strong>, das wir über unseren eigenen Server aufrufen. Dein Gerät kontaktiert OpenAI nie direkt, und in der App befindet sich kein API-Schlüssel. Luna läuft nur, wenn du <strong>dich angemeldet und {K_luna} eingeschaltet hast</strong>. Luna wird genutzt, wenn die KI auf dem Gerät nicht verfügbar ist oder eine Anfrage nicht abschließen kann – oder zuerst, wenn du Light oder Pro hast und Luna als Engine gewählt hast. Wenn du den Schalter ausschaltest, werden ab sofort keine neuen Cloud-KI-Anfragen mehr gestellt.</p>
<p>Für jede Anfrage wird nur der dafür nötige Text gesendet:</p>
<ul>
  <li><strong>Organisieren und Smart Fill</strong>: der Text des Gedankens, der organisiert wird, einschließlich Text, der auf deinem Gerät aus einem angehängten Foto oder PDF gelesen wurde, deine Zeitzone und Sprache sowie die Namen und kurzen Zusammenfassungen von bis zu 30 deiner Projekte.</li>
  <li><strong>Frag deine Notizen</strong>: deine Frage und kurze Auszüge aus bis zu 12 gespeicherten Einträgen, die dein Gerät als relevant ausgewählt hat.</li>
  <li><strong>Aufräumen</strong> (Light und Pro): der Text der Notiz, die du aufräumen lassen wolltest.</li>
  <li><strong>Tageszusammenfassung</strong> (Pro): die Anzahl der fälligen Dinge und kurze Auszüge aus bis zu 10 deiner Einträge für diesen Tag.</li>
</ul>
<p><strong>Nie gesendet werden:</strong> Audio, Bilder oder Dateien selbst; Gedanken mit {K_device_only}; Termine aus deiner Kalender-App; dein Name oder deine E-Mail-Adresse (die haben wir nicht); jegliche Kennung, an der OpenAI erkennen könnte, wer du bist.</p>
<h3>Wie lange es gespeichert wird</h3>
<p>Unser Server speichert ein Ergebnis <strong>bis zu 24 Stunden</strong>, damit eine unterbrochene Anfrage abgeschlossen werden kann, ohne sie doppelt auszuführen oder dein Kontingent doppelt zu belasten. Danach wird der Text entfernt, und ein inhaltsfreier Beleg (ein Einweg-Hash der Anfrage, die IDs der verwendeten Einträge und der Zeitpunkt) wird bis zu einem Jahr für die Kontingentabrechnung aufbewahrt. Wenn du einen Eintrag endgültig löschst, werden auch alle daraus erzeugten Ergebnisse entfernt, und wenn du deinen Account löschst, werden sie alle entfernt.</p>
<p>Wir bitten OpenAI, keine Antworten zu speichern. Gemäß seinen API-Bedingungen nutzt OpenAI diese Daten nicht zum Training seiner Modelle. OpenAI kann Eingaben und Ausgaben für begrenzte Zeit aufbewahren, um Missbrauch zu erkennen, wie in seinen <a href="https://openai.com/enterprise-privacy/">API-Datenrichtlinien</a> beschrieben.</p>
<p>KI-generierte Vorschläge und Antworten können falsch sein. Deshalb lässt sich jedes Smart-Fill-Feld vor dem Speichern prüfen, und jede Antwort nennt ihre Quellen.</p>
""",

"p.sync.h": "iCloud-Synchronisierung",
"p.sync.b": """
<p>Mit Light oder Pro kannst du {K_sync} einschalten. Deine Bibliothek, einschließlich Gedanken, Einträgen, Projekten, Korrekturen, Verlauf und Anhängen, wird dann in einer <strong>privaten CloudKit-Datenbank in deinem eigenen iCloud-Account</strong> gespeichert, damit deine Geräte auf demselben Stand bleiben. Apple speichert sie gemäß seiner eigenen <a href="https://www.apple.com/legal/privacy/">Datenschutzrichtlinie</a>. Wir als Entwickler können deine privaten iCloud-Daten nicht lesen, und unser Server erhält nie eine Kopie deiner Bibliothek.</p>
<p>Gedanken mit {K_device_only} werden nie synchronisiert. Wenn die Synchronisierung eingeschaltet ist, kann iOS stille Mitteilungen von Apples Push-Dienst zustellen, um der App mitzuteilen, dass sich etwas geändert hat. Es wird kein Push-Token an uns gesendet.</p>
""",

"p.account.h": "Dein Account und unser Server",
"p.account.b": """
<p>Ein Account ist optional. Wenn du dich mit Apple anmeldest, fordern wir <strong>weder Namen noch E-Mail-Adresse</strong> an. Unser Server, der bei <strong>Cloudflare</strong> läuft, speichert:</p>
<ul>
  <li><strong>Eine Account-ID</strong>: ein Einweg-Hash der Kennung, die Apple uns übermittelt. Die ursprüngliche Apple-Kennung wird nicht gespeichert.</li>
  <li><strong>Anmeldedaten</strong>: Sitzungen, die nur als Hashes gespeichert werden und nach 30 Tagen ablaufen, sowie Apples Anmelde-Token, verschlüsselt und nur dazu verwendet, es zu widerrufen, wenn du deinen Account löschst.</li>
  <li><strong>Geräteprüfung</strong>: der öffentliche Schlüssel, den Apples App Attest auf jedem Gerät erzeugt, auf dem du dich anmeldest (bis zu 20), damit der Server weiß, dass er mit einer echten Kopie von Second Brain kommuniziert.</li>
  <li><strong>Deine Entscheidungen und dein Plan</strong>: ob Synchronisierung und Cloud-KI eingeschaltet sind, dein Plan und seine Verlängerungsdaten sowie die Transaktionen, die Apple zur Bestätigung sendet.</li>
  <li><strong>Nutzungszähler</strong>: wie viel vom Cloud-Kontingent dieses Monats du verbraucht hast.</li>
  <li><strong>Cloud-KI-Ergebnisse</strong>, kurzzeitig gespeichert wie oben beschrieben.</li>
</ul>
<p>Um den Dienst vor Missbrauch zu schützen, speichert der Server kurzzeitig einen Einweg-Hash deiner IP-Adresse in Kombination mit der aktuellen Minute. Er wird innerhalb weniger Minuten gelöscht. Wir führen keine Anfrageprotokolle, und unser Server erhält nie deine Bibliothek.</p>
<p><strong>Seitenimport</strong> (Pro): Wenn du den Text einer Webseite importieren möchtest, ruft unser Server diese öffentliche Seite selbst ab und sendet ihren lesbaren Text an dein Gerät zurück. Adresse und Text der Seite werden weder gespeichert noch an Luna gesendet.</p>
""",

"p.voice.h": "Stimme, Spracherkennung und Aufnahmen",
"p.voice.b": """
<p>Die Sprachaufnahme nutzt das Mikrofon nur, während du aufnimmst. Gesprochenes wird <strong>auf deinem Gerät</strong> mit Apples Spracherkennung transkribiert. Deine Aufnahme wird für die Transkription weder an Apple noch an uns gesendet; bei der ersten Nutzung einer Sprache werden allerdings Apples Sprachdateien heruntergeladen.</p>
<p>Aufnahmen werden in deiner Bibliothek aufbewahrt. Sobald ein Transkript fertig ist, wird das Audio <strong>7 Tage</strong> nach dem Speichern gelöscht, außer du tippst auf {K_keep_recording}. Eine Aufnahme, deren Transkription fehlgeschlagen ist, bleibt erhalten, bis du sie löschst. Transkripte bleiben erhalten, auch wenn das Audio gelöscht ist.</p>
""",

"p.permissions.h": "Berechtigungen",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>Berechtigung</th><th>Verwendet für</th></tr>
<tr><td>Mikrofon, Spracherkennung</td><td>Sprachaufnahme und Transkription auf dem Gerät.</td></tr>
<tr><td>Kamera, Fotos</td><td>Ein Bild aufnehmen oder auswählen, um es anzuhängen. Gelesen werden nur die Bilder, die du auswählst.</td></tr>
<tr><td>Kalender</td><td>Wird nur abgefragt, wenn du auf {K_calendars} tippst. Die Kalender, die du auswählst, werden auf deinem Gerät gelesen, um sie neben deinen Aufgaben anzuzeigen, und nie hochgeladen. Ein neuer Termin wird nur über Apples eigenen Editor zur Kalender-App hinzugefügt, nachdem du ihn bestätigt hast.</td></tr>
<tr><td>Mitteilungen</td><td>Erinnerungen, der Morgenüberblick und eine Erinnerung, bevor eine kostenlose Testphase endet. Alle werden auf deinem Gerät geplant.</td></tr>
</table></div>
<p style="margin-top:14px">Du kannst all das in iOS unter {K_settings} → Second Brain ändern. Die App fragt nie nach deinem Standort oder deinen Kontakten.</p>
""",

"p.purchases.h": "Käufe",
"p.purchases.b": """
<p>Light und Pro werden über Apples App Store verkauft. Die Zahlung erfolgt zwischen dir und Apple gemäß der <a href="https://www.apple.com/legal/privacy/">Datenschutzrichtlinie von Apple</a>, und wir sehen deine Zahlungsdaten nie. Einen Plan kannst du ohne Account kaufen: Dein iPhone prüft die von Apple signierte Transaktion, und unser Server speichert nichts über den Kauf. Wenn du dich anmeldest, prüft unser Server diese Transaktion und speichert sie mit deinem Account, damit der Plan dir auf deine anderen Geräte folgen kann. Ein ohne Account getätigter Kauf wird mit dem ersten Account verknüpft, der ihn übermittelt. Unser Server erhält außerdem Apples Benachrichtigungen zu Verlängerungen, Erstattungen und Kündigungen und wendet sie nur auf Käufe an, die mit einem Account verknüpft sind, damit dein Plan stets korrekt ist.</p>
""",

"p.third.h": "Dienstleister",
"p.third.b": """
<p>Second Brain enthält <strong>keine SDKs von Drittanbietern</strong>: keine Analyse, keine Werbung und keine Absturzberichte. Diese Unternehmen verarbeiten Daten für uns, jeweils nur für den genannten Zweck:</p>
<ul>
  <li><strong>Apple</strong>: „Mit Apple anmelden“, App Attest, der App Store und Käufe, iCloud-Synchronisierung in deinem eigenen Account, Push-Zustellung für die Synchronisierung sowie die KI- und Sprachmodelle auf dem Gerät.</li>
  <li><strong>Cloudflare</strong>: hostet unseren Server und seine Datenbank und leitet Anfragen dorthin weiter.</li>
  <li><strong>OpenAI</strong>: betreibt Luna für die Cloud-KI-Anfragen, die du erlaubst, wie oben beschrieben.</li>
</ul>
<p>Wir verkaufen oder vermieten keine personenbezogenen Daten und teilen nichts mit Werbetreibenden oder Datenhändlern. Wir können Informationen offenlegen, wenn das Gesetz es verlangt. Da wir so wenig speichern, gibt es kaum etwas, das wir offenlegen könnten.</p>
""",

"p.retention.h": "Wie lange wir Daten aufbewahren",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>Daten</th><th>Aufbewahrt</th></tr>
<tr><td>Deine Bibliothek auf deinem Gerät</td><td>Bis du sie löschst. Gelöschte Einträge bleiben 30 Tage lang unter {K_recently_deleted}.</td></tr>
<tr><td>Sprachaufnahmen</td><td>7 Tage nach einem fertigen Transkript, außer du behältst sie. Bis du sie löschst, wenn die Transkription fehlgeschlagen ist.</td></tr>
<tr><td>Deine iCloud-Kopie</td><td>Bis du sie oder deinen Account löschst. Sie wird von Apple in deiner iCloud gespeichert.</td></tr>
<tr><td>Cloud-KI-Ergebnis</td><td>Bis zu 24 Stunden. Ein inhaltsfreier Beleg wird bis zu 1 Jahr aufbewahrt.</td></tr>
<tr><td>Anmeldesitzungen</td><td>30 Tage ab der letzten Aktualisierung</td></tr>
<tr><td>Account, Plan und Nutzungszähler</td><td>Solange dein Account besteht</td></tr>
<tr><td>Gehashte IP-Adresse zum Schutz vor Missbrauch</td><td>Wenige Minuten</td></tr>
<tr><td>Server-Backups</td><td>Die Datenbank-Backups unseres Hosting-Anbieters können gelöschte Daten bis zu 30 Tage lang enthalten, bevor sie ablaufen.</td></tr>
</table></div>
""",

"p.delete.h": "Export und Löschung",
"p.delete.b": """
<p>Alles liegt in deiner Hand, direkt in der App:</p>
<ul>
  <li><strong>Export</strong>: Unter {EXPORT} erstellst du eine ZIP-Datei mit deiner ganzen Bibliothek, deinen Originaldateien und einer Liste von allem, was nicht aufgenommen werden konnte.</li>
  <li><strong>Von diesem Gerät löschen</strong>: Mit {DELETE_LOCAL} entfernst du die Bibliothek auf diesem Gerät. Dein Account und seine iCloud-Kopie werden dabei nicht gelöscht.</li>
  <li><strong>Deinen Account löschen</strong>: Über {DELETE_ACCOUNT} werden deine iCloud-Kopie, alles, was unser Server über den Account speichert, und die Bibliothek des Accounts auf diesem Gerät gelöscht, und der Zugriff von Second Brain über „Mit Apple anmelden“ wird widerrufen.</li>
</ul>
<p>Nach dem Löschen eines Accounts behält unser Server nur eine inhaltsfreie Markierung: die als gelöscht gekennzeichnete gehashte Account-ID, ihre Nutzungszähler und Einweg-Hashes ihrer Kauf- und Gerätekennungen. Mit dieser Markierung kann eine unterbrochene Löschung abgeschlossen werden, und sie verhindert, dass ein Kauf oder das kostenlose Cloud-Probekontingent doppelt beansprucht wird. Sie enthält keine Inhalte, keinen Namen und keine E-Mail-Adresse. Eine Schritt-für-Schritt-Anleitung findest du auf der Seite <a href="{BASE}{L}/delete-data/">Deine Daten</a>.</p>
""",

"p.rights.h": "Deine Rechte",
"p.rights.b": """
<p>Je nachdem, wo du lebst, unter anderem nach der DSGVO, der UK-DSGVO und dem kalifornischen CCPA/CPRA, hast du das Recht auf Auskunft, Berichtigung, Export, Einschränkung der Verarbeitung, Widerspruch und Löschung in Bezug auf personenbezogene Daten, die wir über dich speichern, das Recht, eine Einwilligung jederzeit zu widerrufen, und das Recht, dich bei deiner Datenschutzaufsichtsbehörde zu beschweren. Die meisten dieser Rechte sind direkt in die App eingebaut: Export, Löschen und die Schalter für Synchronisierung und Cloud-KI. Für alles andere schreib an {MAIL}, und wir antworten innerhalb von 30 Tagen.</p>
<p>Soweit die DSGVO gilt, stützen wir uns auf: <strong>Vertrag</strong>, um die Funktionen bereitzustellen, die du nutzt, und den Plan, den du gekauft hast; <strong>Einwilligung</strong> für iCloud-Synchronisierung und Cloud-KI, die du mit den jeweiligen Schaltern widerrufen kannst; <strong>berechtigte Interessen</strong> daran, den Dienst sicher zu halten und Missbrauch zu verhindern (App Attest und Missbrauchsschutz); und <strong>rechtliche Verpflichtung</strong> für Kaufbelege.</p>
""",

"p.children.h": "Kinder",
"p.children.b": """
<p>Second Brain richtet sich nicht an Kinder unter 13 Jahren oder unter dem Alter der digitalen Einwilligung, das dort gilt, wo du lebst. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Wenn du glaubst, dass ein Kind einen Account erstellt hat, schreib an {MAIL}, und wir helfen, ihn zu löschen.</p>
""",

"p.transfers.h": "Wo Daten verarbeitet werden",
"p.transfers.b": """
<p>Cloudflare betreibt unseren Server in seinem globalen Netzwerk, und OpenAI und Apple können Daten in den USA und anderen Ländern verarbeiten. Soweit gesetzlich erforderlich, sind diese Übermittlungen durch die Datenverarbeitungsbedingungen der Anbieter abgedeckt, einschließlich Standardvertragsklauseln. Daten, die auf deinem Gerät gespeichert sind, bleiben dort, wo dein Gerät ist.</p>
""",

"p.changes.h": "Änderungen dieser Erklärung",
"p.changes.b": """
<p>Wenn die App ändert, was sie mit Daten macht, aktualisieren wir diese Erklärung und das Datum oben. Wesentliche Änderungen erwähnen wir in den Versionshinweisen der App und bitten, wo gesetzlich erforderlich, erneut um deine Einwilligung. Wir werden deine Inhalte nie an einen neuen Ort senden, ohne dass du dich erneut dafür entschieden hast.</p>
""",

"p.contact.h": "Kontakt",
"p.contact.b": """
<p>{COMPANY}, der Herausgeber von Second Brain, ist der Verantwortliche für die hier beschriebenen personenbezogenen Daten. Für Fragen oder Anliegen zum Datenschutz schreib an {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Nutzungsbedingungen",
"t.h1": "Die Vereinbarung, in klaren Worten.",
"t.sub": "Was Second Brain tut, was seine KI versprechen kann und was nicht, wie mit deinen Inhalten umgegangen wird und wie Light und Pro abgerechnet werden.",
"t.meta": "Gültig ab {DATE} · Second Brain von {COMPANY}",

"t.acceptance.h": "1. Annahme der Bedingungen",
"t.acceptance.b": """
<p>Diese Nutzungsbedingungen („Bedingungen“) sind eine Vereinbarung zwischen dir und {COMPANY} („wir“, „uns“), dem Herausgeber der App Second Brain für iPhone und iPad („Second Brain“ oder „die App“) und der zugehörigen Online-Dienste. Indem du Second Brain installierst oder nutzt, akzeptierst du diese Bedingungen und unsere <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>. Wenn du nicht einverstanden bist, nutze die App nicht.</p>
""",
"t.who.h": "2. Wer Second Brain nutzen darf",
"t.who.b": """
<p>Um Second Brain zu nutzen, musst du mindestens 13 Jahre alt sein oder das Alter der digitalen Einwilligung erreicht haben, das dort gilt, wo du lebst. Bist du dort, wo du lebst, noch nicht volljährig, brauchst du die Erlaubnis eines Elternteils oder Erziehungsberechtigten, um ein Abo abzuschließen.</p>
""",
"t.what.h": "3. Was Second Brain ist und was nicht",
"t.what.b": """
<p>Second Brain ist ein persönliches Werkzeug, um Gedanken per Sprache oder Text festzuhalten und sie in Aufgaben, Termine, Notizen und Ideen zu ordnen, mit Erinnerungen, Suche und Antworten aus dem, was du gespeichert hast.</p>
<p>Second Brain ist <strong>kein</strong> medizinischer, rechtlicher, finanzieller oder sonstiger professioneller Dienst, und nichts, was es erzeugt, ist eine fachliche Beratung. Verlass dich nicht darauf als einzige Möglichkeit, dich an etwas Wichtiges zu erinnern, etwa an Medikamente, eine rechtliche Frist oder eine sicherheitsrelevante Angelegenheit. Erinnerungen hängen von iOS, deinen Einstellungen und deinem Gerät ab und kommen möglicherweise nicht an. Wende dich im Notfall an deinen örtlichen Notruf.</p>
""",
"t.account.h": "4. Dein Account",
"t.account.b": """
<p>Ein Account ist optional und nutzt „Mit Apple anmelden“. Du bist verantwortlich für deinen Apple Account, dein Gerät und dessen Code sowie für Aktivitäten unter deinem Account. Jeder Account ist für eine Person bestimmt. Du kannst dich jederzeit abmelden und deinen Account in der App löschen, wie auf der Seite <a href="{BASE}{L}/delete-data/">Deine Daten</a> beschrieben.</p>
""",
"t.content.h": "5. Deine Inhalte",
"t.content.b": """
<p>Alles, was du in Second Brain festhältst, anhängst oder schreibst („deine Inhalte“), bleibt deins. Wir beanspruchen kein Eigentum daran. Du räumst uns nur die eingeschränkte Erlaubnis ein, die nötig ist, um deine Inhalte zu verarbeiten und so die Funktionen bereitzustellen, die du wählst: zum Beispiel Text an Luna zu senden, wenn du Cloud-KI eingeschaltet hast, oder eine Webseite abzurufen, die du importieren wolltest. Wir nutzen deine Inhalte nicht zum Training von KI-Modellen und verkaufen sie nicht.</p>
<p>Du bist für deine Inhalte verantwortlich und dafür, dass du das Recht hast, sie festzuhalten, zu importieren und zu speichern, auch alles, was andere Menschen betrifft. Deine Bibliothek liegt auf deinem Gerät und, wenn du es wählst, in deiner eigenen iCloud. Bewahre eigene Exporte auf. Wir haben keine Kopie deiner Bibliothek und können sie nicht wiederherstellen, wenn die Kopien auf deinem Gerät und in iCloud verloren gehen.</p>
""",
"t.ai.h": "6. KI-Funktionen",
"t.ai.b": """
<p>Second Brain nutzt künstliche Intelligenz, um vorzuschlagen, wie du Festgehaltenes organisierst, um Details wie Datum und Uhrzeit auszufüllen, um Fragen aus deiner Bibliothek zu beantworten und um Zusammenfassungen zu schreiben. Es nutzt Apples Modell auf dem Gerät, wo verfügbar, und, wenn du es erlaubst, <strong>Luna</strong>, ein Cloud-Modell von OpenAI, das über unseren Server bereitgestellt wird.</p>
<p><strong>KI-Ergebnisse können falsch, unvollständig oder veraltet sein.</strong> Die KI kann ein Datum falsch lesen, eine Aufgabe übersehen oder falsch wiedergeben, was in einer Quelle steht. Prüfe Vorschläge, bevor du sie erstellst, und prüfe die Quellen einer Antwort, bevor du dich darauf verlässt. Wenn du den {K_quick} einschaltest, werden Einträge ohne diese Prüfung erstellt, und zwar nach deiner eigenen Entscheidung. Alles, wobei sich Smart Fill nicht sicher ist, landet unter {K_needs_review}, und {K_undo} bleibt verfügbar.</p>
<p>Du verpflichtest dich, die KI-Funktionen nicht zu nutzen, um rechtswidrige, schädliche oder rechtsverletzende Inhalte zu erzeugen, und nicht zu versuchen, die zugrunde liegenden Modelle, ihre Anweisungen oder die Schlüssel unseres Dienstes zu extrahieren. Wir können die verwendeten Modelle ändern, Limits anpassen oder eine Funktion pausieren, um den Dienst zu schützen. In diesem Fall funktioniert der Rest der App weiter, und deine gespeicherten Inhalte sind nicht betroffen.</p>
""",
"t.cloud.h": "7. Cloud-Funktionen und Kontingente",
"t.cloud.b": """
<p>Die <strong>Synchronisierung</strong> nutzt deinen eigenen iCloud-Account und hängt von Apples Dienst, deinem iCloud-Speicher und deiner Verbindung ab. <strong>Cloud-KI</strong> ist durch das monatliche Kontingent deines Plans begrenzt: Light enthält 300 Cloud-KI-Aufnahmen und 100 Cloud-Antworten pro Monat, Pro enthält 700 und 250, und ein angemeldeter kostenloser Account erhält ein einmaliges Probekontingent. Kontingente werden jeden Kalendermonat zurückgesetzt, und ungenutzte Mengen werden nicht übertragen. Damit der Dienst fair bleibt, gilt außerdem ein Limit für die Gesamtmenge an Text, die pro Monat verarbeitet wird. Der <strong>Seitenimport</strong> (Pro) ruft nur öffentliche Seiten ab, und du bist dafür verantwortlich, dass du das Recht hast, das Importierte zu nutzen.</p>
<p>Wir bemühen uns, Cloud-Funktionen verfügbar zu halten, garantieren aber nicht, dass sie unterbrechungsfrei sind. Funktionen auf dem Gerät arbeiten auch ohne sie weiter.</p>
""",
"t.subscriptions.h": "8. Abos und Abrechnung",
"t.subscriptions.b": """
<p>Second Brain kann kostenlos geladen und genutzt werden, mit monatlichen Limits für Sprachaufnahmen, Smart Fill und „Frag deine Notizen“ auf jedem Gerät. Das Speichern von Festgehaltenem wird nie blockiert. Bezahlte Pläne sind sich automatisch verlängernde Abos, die über Apple verkauft werden, zu dem Preis, der in der App und im App Store für dein Land angezeigt wird:</p>
<ul>
  <li><strong>Light Monatsabo</strong>: monatliche Abrechnung.</li>
  <li><strong>Pro Monatsabo</strong>: monatliche Abrechnung.</li>
  <li><strong>Pro Jahresabo</strong>: jährliche Abrechnung, beginnend mit einer <strong>7-tägigen kostenlosen Testphase</strong> für berechtigte Neuabonnenten.</li>
</ul>
<p>Ein Abo kannst du auch ohne Account bei Second Brain abschließen. Ohne Account funktionieren die Gerätefunktionen des Plans auf iPhones, die den Apple Account verwenden, mit dem du das Abo abgeschlossen hast. Mit „Mit Apple anmelden“ verknüpfst du den Plan mit deinem Account und erhältst seine Cloud-Funktionen. Die Zahlung wird deinem Apple Account belastet, wenn du den Kauf bestätigst. Eine kostenlose Testphase geht in ein bezahltes Abo über, sofern du nicht mindestens 24 Stunden vor ihrem Ende kündigst. Abos verlängern sich automatisch zum gleichen Preis und für den gleichen Zeitraum, sofern die automatische Verlängerung nicht mindestens 24 Stunden vor dem Ende des aktuellen Zeitraums ausgeschaltet wird. Die Verlängerung wird deinem Apple Account innerhalb der 24 Stunden vor dem Ende dieses Zeitraums belastet. Du kannst ein Abo in deinen <a href="https://apps.apple.com/account/subscriptions">Abo-Einstellungen im App Store</a> oder über {K_manage} in der App verwalten oder kündigen. Eine Kündigung wird zum Ende des aktuellen Zeitraums wirksam. Erstattungen bearbeitet Apple gemäß seinen Richtlinien. Mit {K_restore} stellst du einen Plan auf einem anderen Gerät wieder her. Abos werden nicht über die Familienfreigabe geteilt.</p>
<p><strong>Wenn ein Abo endet</strong>, wird nichts entfernt, was du gespeichert hast. Lesen, Bearbeiten, Suche, Export und Löschen funktionieren weiter, die kostenlosen Monatslimits gelten wieder, und Synchronisierung und Cloud-Kontingente enden. Wenn du die App oder deinen Account löschst, wird ein Abo nicht gekündigt. Kündige es bei Apple. Wir können Preise oder die Funktionen eines Plans ändern. Apple informiert dich, bevor eine Preiserhöhung für dich gilt, wie es seine Regeln verlangen.</p>
""",
"t.licence.h": "9. Lizenz und geistiges Eigentum",
"t.licence.b": """
<p>Wir gewähren dir eine persönliche, nicht exklusive, nicht übertragbare, widerrufliche Lizenz, Second Brain auf Apple-Geräten zu nutzen, die du besitzt oder kontrollierst, gemäß diesen Bedingungen und den Nutzungsregeln des App Store. Second Brain, sein Name, Design, Grafiken (einschließlich der Begleiter-Figur), Texte und Code gehören {COMPANY} und sind gesetzlich geschützt. Du darfst die App nicht kopieren, verändern, verbreiten, verkaufen, vermieten, zurückentwickeln (Reverse Engineering) oder abgeleitete Werke davon erstellen, außer soweit das Gesetz es ausdrücklich erlaubt.</p>
""",
"t.use.h": "10. Zulässige Nutzung",
"t.use.b": """
<p>Du verpflichtest dich, Second Brain nicht rechtswidrig zu nutzen oder darin Inhalte zu speichern, die du nicht besitzen darfst; unsere Server nicht zu stören, zu überlasten oder auszuforschen; Kontingente, App Attest oder das Kaufsystem des App Store nicht zu umgehen; nicht auf den Account einer anderen Person zuzugreifen; und den Dienst nicht zu nutzen, um Menschen zu belästigen, ihnen zu schaden oder sie ohne die gesetzlich erforderliche Einwilligung aufzunehmen.</p>
""",
"t.termination.h": "11. Beendigung",
"t.termination.b": """
<p>Du kannst die Nutzung von Second Brain jederzeit beenden und deinen Account in der App löschen. Wir können den Zugang zu Cloud-Funktionen aussetzen oder beenden, wenn du schwerwiegend oder wiederholt gegen diese Bedingungen verstößt oder wenn das Gesetz es verlangt. Wo möglich, informieren wir dich vorher. Deine Inhalte auf deinem Gerät bleiben deine, und du kannst sie exportieren. Die Abschnitte 5, 6, 9, 12, 13 und 15 gelten über die Beendigung hinaus fort.</p>
""",
"t.warranty.h": "12. Gewährleistung und Haftung",
"t.warranty.b": """
<p>Second Brain wird „wie besehen“ und „wie verfügbar“ bereitgestellt, ohne ausdrückliche oder stillschweigende Gewährleistungen jeglicher Art. Wir gewährleisten nicht, dass KI-Ergebnisse korrekt sind, dass Erinnerungen immer ankommen, dass Synchronisierung oder Cloud-Funktionen unterbrechungsfrei sind oder dass die App fehlerfrei ist. Im größtmöglichen gesetzlich zulässigen Umfang haftet {COMPANY} nicht für indirekte, beiläufige, besondere, Folge- oder Strafschäden oder für den Verlust von Daten, Gewinnen oder Chancen, die aus deiner Nutzung der App oder der Unmöglichkeit ihrer Nutzung entstehen, einschließlich allem, was eine KI-Funktion erzeugt hat, oder einer Erinnerung, die nicht angekommen ist. Wo die Haftung nicht ausgeschlossen werden kann, ist sie auf den Betrag beschränkt, den du in den zwölf Monaten vor dem Anspruch für Second Brain bezahlt hast. Nichts in diesen Bedingungen schränkt Rechte ein, die dir als Verbraucher zustehen und auf die nicht verzichtet werden kann.</p>
""",
"t.apple.h": "13. Apple",
"t.apple.b": """
<p>Second Brain wird über den Apple App Store vertrieben. Diese Bedingungen gelten zwischen dir und {COMPANY}, nicht zwischen dir und Apple. Apple ist nicht verpflichtet, Wartung oder Support für die App zu leisten, und ist nicht dafür verantwortlich, Ansprüche im Zusammenhang mit der App zu bearbeiten, einschließlich Ansprüchen aus Produkthaftung, zur Einhaltung gesetzlicher Vorschriften oder zu geistigem Eigentum. Entspricht die App einer anwendbaren Gewährleistung nicht, kannst du Apple benachrichtigen, und Apple erstattet dir den Kaufpreis, falls vorhanden. Im größtmöglichen gesetzlich zulässigen Umfang hat Apple keine weitere Gewährleistungspflicht für die App. Apple und seine Tochtergesellschaften sind begünstigte Dritte dieser Bedingungen und können sie dir gegenüber durchsetzen. Wo diese Bedingungen nichts regeln, gilt Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Endbenutzer-Lizenzvertrag für lizenzierte Anwendungen</a>. Du bestätigst, dass du dich nicht in einem Land befindest, das einem Embargo der US-Regierung unterliegt, und nicht auf einer US-Liste verbotener oder eingeschränkter Parteien stehst, und du musst bei der Nutzung der App alle anwendbaren Bedingungen Dritter einhalten.</p>
""",
"t.changes.h": "14. Änderungen dieser Bedingungen",
"t.changes.b": """
<p>Wir können diese Bedingungen aktualisieren, wenn sich Second Brain verändert. Dann ändert sich das Datum oben, und wesentliche Änderungen erwähnen wir in den Versionshinweisen der App. Wenn du die App nach einer Aktualisierung weiter nutzt, akzeptierst du die überarbeiteten Bedingungen. Wenn du nicht einverstanden bist, kannst du die Nutzung der App beenden und deinen Account löschen.</p>
""",
"t.law.h": "15. Anwendbares Recht",
"t.law.b": """
<p>Diese Bedingungen unterliegen dem Recht Pakistans, wo {COMPANY} tätig ist, unter Ausschluss der Kollisionsnormen. Gewährt dir das Recht deines Wohnsitzlandes Schutz, der vertraglich nicht ausgeschlossen werden kann, gilt dieser Schutz weiterhin.</p>
""",
"t.contact.h": "16. Kontakt",
"t.contact.b": """
<p>Fragen zu diesen Bedingungen: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Deine Daten",
"d.h1": "Deine Daten exportieren oder löschen",
"d.sub": "Deine Bibliothek liegt auf deinem Gerät und, wenn du die Synchronisierung gewählt hast, in deiner eigenen iCloud. So erstellst du eine Kopie, löschst sie von einem Gerät oder löschst deinen Account und alles, was er enthält.",
"d.meta": 'Siehe auch die <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>',

"d.where.h": "Was wo gespeichert ist",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>Daten</th><th>Wo sie liegen</th><th>So entfernst du sie</th></tr>
<tr><td>Gedanken, Aufnahmen, Anhänge, Aufgaben, Notizen, Projekte, Verlauf</td><td>Dein Gerät</td><td>{DELETE_LOCAL} oder deinen Account löschen (siehe unten)</td></tr>
<tr><td>Dieselbe Bibliothek, wenn du die Synchronisierung eingeschaltet hast</td><td>Eine private Datenbank in deiner eigenen iCloud</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Account-ID, Plan, Einwilligungen, Nutzungszähler, Geräteschlüssel</td><td>Unser Server (Cloudflare)</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Cloud-KI-Ergebnisse</td><td>Unser Server, bis zu 24 Stunden</td><td>Werden von selbst entfernt, außerdem wenn du den Eintrag endgültig löschst oder deinen Account löschst</td></tr>
<tr><td>Monatlicher Zähler der kostenlosen Nutzung</td><td>Der iOS-Schlüsselbund auf diesem Gerät (nur Zahlen)</td><td>Wird jeden Monat zurückgesetzt. iOS behält ihn möglicherweise, nachdem die App gelöscht wurde</td></tr>
<tr><td>Abo</td><td>Dein Apple Account</td><td>Bei Apple kündigen (siehe unten)</td></tr>
</table></div>
""",
"d.export.h": "Erst eine Kopie erstellen",
"d.export.b": """
<ol class="steps">
  <li><div>Öffne Second Brain und geh zu den {K_settings}.</div></li>
  <li><div>Tippe auf {K_export} und dann auf {K_share_export}.</div></li>
  <li><div>Sichere die ZIP-Datei in der Dateien-App oder sende sie, wohin du möchtest. Sie enthält deine Bibliothek (als JSON, Markdown und eine CSV-Datei mit deinen Aufgaben), deine Originaldateien und eine Liste von allem, was nicht aufgenommen werden konnte.</div></li>
</ol>
""",
"d.local.h": "Von diesem Gerät löschen",
"d.local.b": """
<p>Um einen einzelnen Eintrag zu löschen, lösche ihn und entferne ihn dann unter {K_settings} → {K_recently_deleted} mit {K_delete_permanently}. Andernfalls wird er nach 30 Tagen automatisch entfernt.</p>
<p>Um die ganze Bibliothek auf diesem Gerät zu löschen, nutze {DELETE_LOCAL}. Dadurch werden dein Account, seine iCloud-Kopie und eine separate Gastbibliothek <strong>nicht</strong> gelöscht. Wenn du die App löschst, werden ihre Daten ebenfalls vom Gerät entfernt.</p>
""",
"d.account.h": "Deinen Account löschen",
"d.account.b": """
<ol class="steps">
  <li><div>Öffne {K_settings} → {K_cloud_choices}.</div></li>
  <li><div>Tippe auf {K_delete_account} und bestätige.</div></li>
  <li><div>Second Brain löscht die iCloud-Kopie des Accounts, alles, was unser Server über den Account speichert (Sitzungen, Plan, Entscheidungen, Nutzungszähler, Geräteschlüssel und KI-Ergebnisse), und die Bibliothek des Accounts auf diesem Gerät. Außerdem widerruft es seinen Zugriff über „Mit Apple anmelden“. Deine separate Gastbibliothek bleibt auf dem Gerät.</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>Wenn deine Anmeldung abgelaufen ist, bittet dich die App, dich erneut mit demselben Apple Account anzumelden, um den Vorgang abzuschließen. Wenn du das Gerät nicht mehr hast, installiere Second Brain auf einem beliebigen iPhone oder iPad, melde dich mit demselben Apple Account an und lösche den Account dort.</div></div>
<p style="margin-top:16px">Danach behält unser Server nur eine inhaltsfreie Markierung: die als gelöscht gekennzeichnete gehashte Account-ID, ihre Nutzungszähler und Einweg-Hashes ihrer Kauf- und Gerätekennungen. So kann eine unterbrochene Löschung abgeschlossen werden, und ein Kauf oder das kostenlose Probekontingent kann nicht doppelt beansprucht werden. Datenbank-Backups bei unserem Hosting-Anbieter laufen innerhalb von 30 Tagen ab.</p>
""",
"d.subscription.h": "Dein Abo",
"d.subscription.b": """
<p>Wenn du deine Daten, deinen Account oder die App löschst, wird ein Abo <strong>nicht</strong> gekündigt. Es gehört zu deinem Apple Account. Kündige es in deinen <a href="https://apps.apple.com/account/subscriptions">Abo-Einstellungen im App Store</a>; es bleibt bis zum Ende des aktuellen Zeitraums aktiv. Erstattungen bearbeitet der <a href="https://support.apple.com/billing">Apple Support</a>.</p>
""",
"d.email.h": "Frag uns",
"d.email.b": """
<p>Wenn du die App nicht nutzen kannst oder eine Frage zu deinen Daten hast, schreib an {MAIL}. Wir antworten innerhalb von 30 Tagen. Wir haben weder einen Namen noch eine E-Mail-Adresse zu deinem Account gespeichert, deshalb suchen wir ihn gemeinsam mit dir. Am schnellsten geht es meist, wenn du dich auf einem beliebigen Gerät anmeldest und dort löschst. Bitte schick uns keine Gedanken oder Aufnahmen. Wir brauchen sie nicht, um dir zu helfen.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Diese Seite haben wir nicht gefunden.",
"nf.sub": "Auch ein zweites Gehirn vergisst mal einen Link.",
"nf.cta": "Zurück zum Support",
"nf.b": 'Diese Seite gibt es hier nicht. Versuch es mit dem <a href="{BASE}/">Support</a>, der <a href="{BASE}/privacy/">Datenschutzerklärung</a> oder den <a href="{BASE}/terms/">Nutzungsbedingungen</a>.',

}
