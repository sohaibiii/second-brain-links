# -*- coding: utf-8 -*-
"""French (fr). English is the fallback; k.* are the app's own labels."""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Assistance",
"nav.about": "À propos",
"nav.privacy": "Confidentialité",
"nav.terms": "Conditions",
"nav.data": "Vos données",

"ui.skip": "Aller au contenu",
"ui.pages": "Pages du site",
"ui.footer": "Pied de page",
"ui.lang": "Langue",
"ui.toc": "Sur cette page",
"ui.rights": "Tous droits réservés.",
"ui.store_soon": "Bientôt sur l’App Store",
"ui.store_get": "Télécharger dans l’App Store",
"ui.date": "16 octobre 2026",
"ui.last_updated": "Dernière mise à jour : {DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "Cette traduction est fournie pour votre commodité. En cas de divergence avec la version anglaise, la version anglaise prévaut.",

# The app's own words, copied from SecondBrain/Localizable.xcstrings. Do not retranslate.
"k.settings": "Réglages",
"k.cloud_choices": "Choix de synchronisation cloud et d’IA",
"k.account": "Votre compte",
"k.delete_account": "Supprimer le compte et la bibliothèque",
"k.keep_account": "Garder le compte",
"k.delete_local": "Supprimer toutes les données locales",
"k.export": "Préparer une exportation",
"k.share_export": "Partager l’exportation de la bibliothèque",
"k.recently_deleted": "Supprimés récemment",
"k.delete_permanently": "Supprimer définitivement",
"k.data_handled": "Comment vos données sont traitées",
"k.privacy_screen": "Votre confidentialité",
"k.sync": "Synchroniser ma bibliothèque",
"k.sync_now": "Synchroniser",
"k.luna": "Utiliser Luna pour organiser et répondre",
"k.on_device": "IA sur l’appareil",
"k.language": "Langue",
"k.restore": "Restaurer les achats",
"k.manage": "Gérer l’abonnement",
"k.sign_out": "Se déconnecter et ouvrir la bibliothèque invité",
"k.keep_recording": "Garder cet enregistrement",
"k.needs_review": "À vérifier",
"k.smart_org": "Organisation intelligente",
"k.smart_fill": "Remplissage intelligent",
"k.quick": "Mode rapide",
"k.ask": "Interroger votre Brain",
"k.calendars": "Connecter l’app Calendrier",
"k.morning": "Résumé du matin",
"k.reminders": "Notifications de rappel",
"k.spotlight": "Afficher les éléments enregistrés dans Spotlight",
"k.device_only": "Garder uniquement sur cet iPhone",
"k.undo": "Annuler",
"k.widgets": "Afficher les titres dans les widgets",

"meta.support.title": "Second Brain — Assistance",
"meta.support.desc": "Assistance officielle de Second Brain : fonctionnement de la capture, du Remplissage intelligent et d’Interroger votre Brain, ce dont l’app a besoin, réponses aux questions fréquentes et comment nous contacter.",
"meta.about.title": "Second Brain — Dites-le, tout simplement. On s’occupe du reste.",
"meta.about.desc": "Second Brain transforme ce que vous dites ou tapez en tâches, événements, notes et idées, conserve votre original et répond à vos questions à partir de ce que vous avez enregistré, avec l’IA sur l’appareil en priorité.",
"meta.privacy.title": "Politique de confidentialité — Second Brain",
"meta.privacy.desc": "Ce que Second Brain garde sur votre appareil, ce qui va dans iCloud, ce que conserve notre serveur, et quand exactement vos mots sont envoyés à l’IA cloud.",
"meta.terms.title": "Conditions d’utilisation — Second Brain",
"meta.terms.desc": "Conditions d’utilisation (CLUF) de Second Brain : votre contenu, les fonctionnalités d’IA, les quotas cloud et la facturation des abonnements Light et Pro.",
"meta.data.title": "Supprimer vos données — Second Brain",
"meta.data.desc": "Comment exporter votre bibliothèque, la supprimer de cet appareil, et supprimer votre compte Second Brain ainsi que tout ce qu’il contient dans iCloud et sur notre serveur.",
"meta.nf.title": "Page introuvable — Second Brain",
"meta.nf.desc": "Page introuvable.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Assistance",
"s.h1": "Aide pour Second Brain",
"s.sub": "Dites-le ou tapez-le : Second Brain le classe en tâches, événements, notes et idées, conserve votre original et vous permet d’annuler toute modification. Cette page explique comment l’app fonctionne, ce dont elle a besoin et comment nous contacter.",
"s.cta": "Lire la FAQ",
"s.meta": 'Fonctionne sans compte · IA sur l’appareil en priorité · <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>',

"s.how.h": "Comment fonctionne Second Brain",
"s.how.b": """
<p class="lead">Videz votre tête en quelques secondes, et retrouvez tout au moment où ça compte.</p>
<p>Touchez le micro et parlez comme vous pensez, ou tapez. Second Brain enregistre d’abord vos mots, exactement tels que vous les avez dits, pour que rien ne se perde. Ensuite, il suggère ce qu’ils contiennent : une tâche avec une échéance, un événement avec une heure, une note ou une idée, rangée dans le bon projet. Vous vérifiez chaque suggestion avant que quoi que ce soit ne soit créé, et chaque modification peut être annulée.</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>Capture</b><span>La capture vocale commence à enregistrer dès son ouverture. Vous pouvez aussi taper, partager du texte, des liens, des photos ou des fichiers depuis d’autres apps, ou les joindre à une capture.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>Remplissage intelligent et vérification</b><span>Touchez Terminé et le Remplissage intelligent prépare des tâches, des événements, des notes et des idées avec leurs dates et heures. Chaque champ peut être modifié avant que vous touchiez Créer. Tout ce dont il n’est pas sûr reste surligné, ou va dans {K_needs_review}.</span></div></li>
  <li><span class="tile">{chat}</span><div><b>Interroger votre Brain</b><span>Posez une question avec vos propres mots. Les réponses viennent uniquement de ce que vous avez enregistré, avec la liste des sources pour que vous puissiez les ouvrir et les vérifier.</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>Aujourd’hui et Calendrier</b><span>Ce qui est à faire, ce qui vient ensuite et ce qui compte, plus une vue de la semaine avec l’app Calendrier à côté de vos tâches. Rappels et résumé du matin facultatifs.</span></div></li>
  <li><span class="tile">{undo}</span><div><b>Votre original, toujours</b><span>Les mots que vous avez capturés restent dans votre bibliothèque, à côté de ce qui en a été tiré. {K_undo} annule toute organisation, et les éléments supprimés attendent 30 jours dans {K_recently_deleted}.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Privé par défaut</b><span>L’organisation et les réponses s’effectuent sur votre appareil avec le modèle sur l’appareil d’Apple, si votre appareil le prend en charge. La synchronisation cloud et l’IA cloud restent désactivées tant que vous ne les choisissez pas. Voir <a href="{BASE}{L}/privacy/">Confidentialité</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Configuration requise",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Appareil</th><td><strong>iPhone ou iPad</strong> avec <strong>iOS 18 ou iPadOS 18</strong> ou version ultérieure.</td></tr>
<tr><th>IA sur l’appareil</th><td>Un appareil compatible avec <strong>Apple Intelligence</strong>, sous iOS 26 ou iPadOS 26 ou version ultérieure, avec Apple Intelligence activée et son modèle téléchargé. Sur les autres appareils, vous pouvez quand même capturer, organiser à la main, rechercher et définir des rappels. Le Remplissage intelligent et les réponses peuvent alors utiliser Luna dans le cloud, si vous vous connectez et l’autorisez.</td></tr>
<tr><th>Compte</th><td><strong>Facultatif.</strong> La capture, l’organisation, la recherche, l’exportation et la suppression fonctionnent sans compte, tout comme l’achat de Light ou Pro. « Se connecter avec Apple » est nécessaire pour synchroniser avec iCloud, utiliser Luna ou importer le texte d’une page.</td></tr>
<tr><th>Connexion Internet</th><td>Inutile pour la capture, l’IA sur l’appareil, la recherche ou l’exportation. Nécessaire pour la connexion au compte, les achats, la synchronisation iCloud, Luna, l’import de pages et le premier téléchargement des ressources vocales d’Apple pour votre langue.</td></tr>
<tr><th>Autorisations</th><td>Micro et Reconnaissance vocale pour la capture vocale. Appareil photo ou Photos uniquement quand vous joignez une image. Calendriers uniquement si vous connectez l’app Calendrier. Notifications uniquement pour les rappels et le résumé du matin. Chaque autorisation est demandée la première fois que vous en avez besoin.</td></tr>
<tr><th>iCloud</th><td>Pour la synchronisation, un compte iCloud avec suffisamment d’espace libre. La synchronisation est incluse avec Light et Pro.</td></tr>
<tr><th>Langues</th><td>Anglais, allemand, espagnol, français, japonais, coréen, portugais (Brésil) et chinois simplifié. La capture vocale écoute dans la langue de l’app. Choisissez-la dans {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Premiers pas",
"s.start.b": """
<ol class="steps">
  <li><div><b>Ouvrez Second Brain.</b> Aucune inscription. Votre bibliothèque vit sur votre appareil dès la première seconde.</div></li>
  <li><div><b>Touchez le micro et dites ce qui vous passe par la tête.</b> Autorisez le micro et la reconnaissance vocale quand iOS vous le demande. Ou tapez.</div></li>
  <li><div><b>Touchez Terminé.</b> Le Remplissage intelligent prépare des tâches, des événements, des notes et des idées. Vérifiez chaque champ, modifiez ce que vous voulez, puis touchez Créer.</div></li>
  <li><div><b>Interrogez votre Brain.</b> Demandez « qu’ai-je promis à Sam ? » ou « quand ai-je rendez-vous chez le dentiste ? » et ouvrez les sources citées pour vérifier.</div></li>
  <li><div><b>Facultatif :</b> pour synchroniser avec iCloud ou utiliser Luna, ouvrez {K_settings} → {K_cloud_choices} et connectez-vous avec Apple. Chaque option a son propre bouton.</div></li>
</ol>
""",

"s.faq.h": "Questions fréquentes",
"s.faq.b": """
<dl class="faq">
<dt>Ai-je besoin d’un compte ?</dt>
<dd>Non. La capture, l’organisation, la recherche, les rappels, l’exportation et la suppression fonctionnent tous sans compte, sur votre appareil. Un compte n’est nécessaire que pour synchroniser avec iCloud, utiliser Luna dans le cloud ou importer le texte d’une page. Vous pouvez acheter une formule sans compte. Se connecter n’envoie jamais votre bibliothèque invité existante : vous choisissez quelles pensées copier dans le compte.</dd>
<dt>Qu’est-ce qui est gratuit ?</dt>
<dd>La capture écrite, les tâches et les projets, la recherche locale, la transcription sur l’appareil, les rappels, la modification, l’exportation et la suppression sont gratuits et illimités. La formule Gratuit inclut aussi <strong>20 captures vocales, 40 Remplissages intelligents et 5 questions dans {K_ask} chaque mois</strong>, comptés sur chaque appareil et renouvelés le 1er du mois. L’enregistrement n’est jamais bloqué : quand une limite est atteinte, vous pouvez toujours taper et enregistrer. Un compte connecté qui autorise l’IA cloud reçoit aussi un essai unique de 10 captures avec l’IA cloud et 5 réponses.</dd>
<dt>Qu’apportent Light et Pro ?</dt>
<dd><strong>Light</strong> supprime les limites mensuelles de la capture vocale, du Remplissage intelligent et d’Interroger votre Brain, ajoute le {K_quick} et la synchronisation iCloud privée, et inclut 300 captures IA cloud et 100 réponses cloud par mois. <strong>Pro</strong> porte ce quota à 700 captures IA cloud et 250 réponses cloud par mois, et ajoute un résumé quotidien cloud et l’import du texte d’une page web. Light est facturé tous les mois. Pro est mensuel ou annuel, et la formule annuelle commence par 7 jours gratuits pour les nouveaux abonnés éligibles. Les prix sont affichés dans l’app et sur l’App Store pour votre pays, et la facturation est gérée par Apple.</dd>
<dt>Quelle est la différence entre l’IA sur l’appareil et Luna ?</dt>
<dd>L’IA sur l’appareil est le modèle d’Apple qui s’exécute sur votre appareil. Rien de ce que vous écrivez n’en sort. Luna est un modèle cloud d’OpenAI qui passe par notre serveur. Elle n’est utilisée que si vous vous connectez et activez {K_luna}, et seulement dans la limite du quota cloud de votre formule. L’IA sur l’appareil passe en premier, et Luna prend le relais quand votre appareil ne peut pas aider. Light et Pro peuvent choisir Luna comme moteur principal dans {K_settings}. Les captures marquées {K_device_only} ne sont jamais envoyées à Luna, quel que soit le moteur choisi.</dd>
<dt>Que fait « {K_device_only} » ?</dt>
<dd>Cette capture et tout ce qui en est tiré ne sont jamais synchronisés avec iCloud ni envoyés à l’IA cloud. L’IA sur l’appareil peut quand même l’organiser.</dd>
<dt>Puis-je me fier aux réponses ?</dt>
<dd>Les réponses sont construites uniquement à partir de ce que vous avez enregistré, et chaque réponse indique ses sources pour que vous puissiez les ouvrir. L’IA peut tout de même mal interpréter ou manquer certaines choses : vérifiez donc les sources avant de vous fier à une réponse pour quoi que ce soit d’important.</dd>
<dt>Que deviennent mes enregistrements vocaux ?</dt>
<dd>Ils sont transcrits sur votre appareil et ne sont envoyés ni à Apple ni à nous pour la transcription. Une fois la transcription terminée, l’audio est supprimé au bout de 7 jours, sauf si vous touchez {K_keep_recording}. Si une transcription échoue, l’audio est conservé jusqu’à ce que vous le supprimiez, pour que vous puissiez réessayer. Les transcriptions restent après la suppression de leur audio.</dd>
<dt>La synchronisation fonctionne-t-elle entre mon iPhone et mon iPad ?</dt>
<dd>Oui, avec Light ou Pro. Connectez-vous avec le même compte Apple sur les deux appareils et activez {K_sync}. Votre bibliothèque se synchronise via votre propre stockage iCloud privé, que nous ne pouvons pas lire.</dd>
<dt>Que se passe-t-il si mon abonnement prend fin ?</dt>
<dd>Rien de ce que vous avez enregistré n’est supprimé. La lecture, la modification, la recherche, l’exportation et la suppression continuent de fonctionner, et les limites mensuelles gratuites s’appliquent de nouveau. La synchronisation et les quotas cloud s’arrêtent jusqu’à ce que vous vous réabonniez.</dd>
<dt>Comment restaurer un achat sur un nouvel appareil ?</dt>
<dd>Sur le nouvel appareil, utilisez le compte Apple avec lequel vous vous êtes abonné, puis touchez {K_restore} sur l’écran des formules. Les fonctions de votre formule sur cet iPhone s’activent aussitôt. Si la formule est liée à votre compte Second Brain, connectez-vous aussi avec Apple pour retrouver la synchronisation iCloud et votre quota cloud.</dd>
<dt>Puis-je utiliser l’app dans ma langue ?</dt>
<dd>Second Brain parle huit langues et suit la langue de votre appareil. Pour en choisir une autre sans rien changer d’autre, ouvrez {K_settings} → {K_language}. La capture vocale écoute alors dans cette langue.</dd>
<dt>Comment récupérer mes données, ou les supprimer ?</dt>
<dd>{EXPORT} crée un fichier ZIP de toute votre bibliothèque, avec vos fichiers d’origine. {DELETE_ACCOUNT} supprime votre compte, sa copie iCloud et ce que conserve notre serveur. Tous les détails se trouvent sur la page <a href="{BASE}{L}/delete-data/">Vos données</a>.</dd>
</dl>
""",

"s.trouble.h": "Dépannage",
"s.trouble.b": """
<h3>Le Remplissage intelligent ou les réponses ne sont pas disponibles</h3>
<ul>
  <li>L’IA sur l’appareil nécessite un appareil compatible avec Apple Intelligence, iOS 26 ou version ultérieure, Apple Intelligence activée dans les Réglages d’iOS, et son modèle entièrement téléchargé. Le téléchargement peut prendre un certain temps après la première activation.</li>
  <li>Si votre appareil ne peut pas l’exécuter, connectez-vous et activez {K_luna} dans {K_settings} → {K_cloud_choices}, ou continuez à organiser à la main. Votre capture est enregistrée dans tous les cas.</li>
  <li>Si un message de limite s’affiche, vous avez utilisé les captures vocales, Remplissages intelligents ou questions gratuits de ce mois sur cet appareil. Ils se renouvellent le 1er du mois, et l’enregistrement fonctionne toujours.</li>
</ul>
<h3>La capture vocale ne transcrit pas</h3>
<ul>
  <li>Vérifiez dans iOS : {K_settings} → Second Brain → Micro et Reconnaissance vocale.</li>
  <li>La première fois que vous utilisez une langue, les ressources vocales d’Apple ont besoin d’une connexion pour se télécharger.</li>
  <li>Si une transcription échoue, l’enregistrement est conservé pour que vous puissiez réessayer ou ajouter le texte vous-même.</li>
</ul>
<h3>La synchronisation ne se met pas à jour</h3>
<ul>
  <li>La synchronisation nécessite Light ou Pro, un compte connecté, et {K_sync} activé dans {K_settings} → {K_cloud_choices}.</li>
  <li>Vérifiez que l’appareil est connecté à iCloud et dispose d’espace de stockage iCloud libre, puis touchez {K_sync_now}.</li>
  <li>Si le même élément a été modifié sur deux appareils, l’app vous demande quelle version garder. Votre capture d’origine est toujours préservée.</li>
</ul>
<h3>Les rappels n’arrivent pas</h3>
<p>{K_settings} indique si les {K_reminders} sont activées. Si elles ont été désactivées, touchez la ligne pour ouvrir les Réglages d’iOS et les autoriser.</p>
<h3>Ma formule n’est pas reconnue</h3>
<p>Vérifiez que votre iPhone utilise le compte Apple avec lequel vous vous êtes abonné, puis touchez {K_restore}. Si la formule est liée à votre compte Second Brain, connectez-vous aussi avec Apple. Les remboursements et les questions de facturation sont traités par Apple via l’<a href="https://support.apple.com/billing">Assistance Apple</a>.</p>
<h3>L’app n’est pas dans la bonne langue</h3>
<p>Ouvrez {K_settings} → {K_language} et choisissez celle que vous voulez. L’app, ses widgets et l’extension de partage suivent immédiatement.</p>
""",

"s.contact.h": "Nous contacter",
"s.contact.b": """
<p>Une question, un bug, ou quelque chose qui devrait fonctionner et ne fonctionne pas ? Écrivez-nous : une vraie personne vous répondra.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Indiquez le modèle de votre appareil, la version d’iOS, la version de l’app (affichée en bas de {K_settings}) et ce que vous attendiez. Merci de ne pas nous envoyer vos captures ou enregistrements, sauf si nous vous les demandons. Nous en avons rarement besoin.</span></div></div>
<p style="margin-top:16px" class="small">La facturation, les remboursements et les modifications d’abonnement sont gérés par Apple : <a href="https://apps.apple.com/account/subscriptions">gérer les abonnements</a> · <a href="https://support.apple.com/billing">demander un remboursement</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "À propos de Second Brain",
"a.h1": "Dites-le, tout simplement. On s’occupe du reste.",
"a.sub": "Parlez comme vous pensez. Second Brain en fait des tâches, des événements, des notes et des idées, conserve votre original et le retrouve quand vous le demandez.",
"a.cta": "Assistance",
"a.meta": "iPhone et iPad · iOS 18+ · huit langues · fonctionne sans compte",
"a.lead": "Second Brain est un endroit serein pour tout ce que vous avez en tête. Capturez-le en quelques secondes, à la voix ou par écrit, vérifiez ce que le Remplissage intelligent en a fait, et interrogez votre Brain quand vous en avez besoin, avec des sources que vous pouvez ouvrir et vérifier.",

"a.f1.h": "Dites-le, tout simplement.",
"a.f1.p": "La capture vocale se met à écouter dès son ouverture, en huit langues. Chaque tâche, chaque projet, chaque idée est saisi au vol pendant que vous parlez, et l’original est conservé.",
"a.f2.h": "Une phrase. Trois choses réglées.",
"a.f2.p": "Le Remplissage intelligent transforme ce que vous avez dit en tâches, événements et notes, dates et heures comprises. Vous vérifiez chaque champ avant que quoi que ce soit ne soit créé.",
"a.f3.h": "Posez vos questions.",
"a.f3.p": "Les réponses viennent uniquement de ce que vous avez enregistré, avec la liste des sources pour que vous puissiez les ouvrir et les vérifier.",
"a.f4.h": "Votre journée, et votre semaine.",
"a.f4.p": "Ce qui est à faire et ce qui vient ensuite sur un seul écran serein, avec l’app Calendrier à côté de vos tâches, des rappels et un résumé du matin facultatif.",
"a.f5.h": "Rien ne se perd.",
"a.f5.p": "Vos mots d’origine restent à côté de tout ce qui en est tiré. Toute organisation peut être annulée, et vous pouvez exporter toute votre bibliothèque à tout moment.",
"a.f6.h": "Privé par défaut.",
"a.f6.p": 'L’IA sur l’appareil d’abord, sans publicité ni suivi. La synchronisation cloud et l’IA cloud attendent chacune votre accord, et toute capture peut rester uniquement sur cet iPhone. <a href="{BASE}{L}/privacy/">Comment ça marche.</a>',

"a.price.h": "Formules",
"a.price.b": """
<p>Second Brain est gratuit, et l’enregistrement n’est jamais bloqué. Light et Pro suppriment les limites mensuelles et ajoutent la synchronisation et l’IA cloud.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Gratuit</div><div class="price">0 $</div><ul><li>Capture écrite, tâches, projets, recherche, rappels et exportation illimités</li><li>20 captures vocales, 40 Remplissages intelligents et 5 questions par mois</li><li>IA sur l’appareil sur les appareils compatibles</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">Mensuel</div><ul><li>Capture vocale, Remplissage intelligent et questions illimités</li><li>Mode rapide</li><li>Synchronisation iCloud privée</li><li>300 captures IA cloud et 100 réponses cloud par mois</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">Mensuel · Annuel</div><ul><li>Tout Light</li><li>700 captures IA cloud et 250 réponses cloud par mois</li><li>Un résumé quotidien cloud</li><li>Import du texte d’une page web</li><li>L’annuel commence par 7 jours gratuits</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Les prix sont affichés dans l’app et sur l’App Store pour votre pays. La facturation est gérée par Apple. <a href="{BASE}{L}/terms/#subscriptions">Conditions d’abonnement.</a></p>
""",

"a.platform.h": "Conçu pour les appareils Apple",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone et iPad</b><span>iOS 18 ou iPadOS 18 et versions ultérieures. IA sur l’appareil sur les appareils compatibles avec Apple Intelligence.</span></div></li>
  <li><span class="tile">{share}</span><div><b>Partout où vous êtes</b><span>Une extension de partage pour enregistrer depuis n’importe quelle app, des widgets pour l’écran d’accueil, Siri et Raccourcis, et une recherche Spotlight facultative.</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>Votre iCloud, pas le nôtre</b><span>La synchronisation passe par votre propre stockage iCloud privé : nous ne détenons donc jamais de copie de votre bibliothèque.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Huit langues</b><span>Anglais, allemand, espagnol, français, japonais, coréen, portugais (Brésil) et chinois simplifié, y compris pour la capture vocale. Choisissez-en une dans {K_settings} → {K_language}.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Politique de confidentialité",
"p.h1": "Vos pensées restent les vôtres.",
"p.sub": "Second Brain garde votre bibliothèque sur votre appareil. La synchronisation cloud et l’IA cloud attendent chacune votre accord. Cette page explique exactement ce qui quitte votre appareil, à quel moment, et qui le reçoit.",
"p.meta": "En vigueur à compter du {DATE} · s’applique à l’app Second Brain pour iPhone et iPad, et à ce site",

"p.summary.h": "En bref",
"p.summary.b": """
<p class="lead">Second Brain fonctionne sans compte. <strong>Votre bibliothèque (captures, enregistrements, pièces jointes, tâches, notes et tout ce qui en est tiré) est stockée sur votre appareil.</strong> Sans compte, l’app ne nous envoie absolument rien.</p>
<p>Trois choses changent cela, et chacune nécessite votre choix :</p>
<ul>
  <li><strong>La synchronisation iCloud</strong> (Light et Pro) copie votre bibliothèque dans <em>votre propre</em> stockage iCloud privé. Nous ne pouvons pas la lire.</li>
  <li><strong>L’IA cloud (« Luna »)</strong> envoie à OpenAI, via notre serveur, le texte nécessaire à une requête, quand l’IA sur l’appareil ne peut pas aider ou quand vous choisissez Luna. Rien n’est envoyé si vous ne vous connectez pas et ne l’activez pas.</li>
  <li><strong>Un compte</strong> (« Se connecter avec Apple ») permet à notre serveur de conserver un dossier minimal : un identifiant de compte obtenu par hachage irréversible, votre formule, vos choix de consentement et vos compteurs d’utilisation. Nous ne demandons jamais votre nom ni votre adresse e-mail à Apple.</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>Pas de publicité, pas d’outils d’analyse, pas de suivi, et aucun SDK tiers dans l’app. Nous ne vendons ni ne partageons de données personnelles, et nous n’utilisons jamais votre contenu pour entraîner des modèles d’IA.</div></div>
<p style="margin-top:16px">Cette politique s’applique à l’app Second Brain pour iPhone et iPad et à ce site web, tous deux publiés par {COMPANY} (« nous »). L’écran {K_settings} → {K_data_handled} de l’app dit la même chose sous une forme plus courte.</p>
""",

"p.collect.h": "Ce que nous collectons",
"p.collect.b": """
<p>« Collecter » désigne ici les données qui quittent votre appareil et sont conservées à un endroit où nous pouvons les lire. Les données qui n’atteignent que votre propre stockage iCloud ne sont pas collectées par nous.</p>
<div class="table-wrap"><table>
<tr><th>Catégorie</th><th>Collectées ?</th><th>Ce que cela signifie</th></tr>
<tr><td>Coordonnées</td><td>Non</td><td>« Se connecter avec Apple » est configuré pour ne nous communiquer ni nom ni adresse e-mail. L’app ne contient aucun champ d’adresse e-mail.</td></tr>
<tr><td>Identifiants</td><td><strong>Uniquement avec un compte</strong></td><td>Un identifiant de compte obtenu par hachage irréversible de l’identifiant qu’Apple nous transmet, et la clé publique créée par App Attest d’Apple sur chacun de vos appareils. Aucun identifiant publicitaire ni identifiant d’appareil n’est utilisé.</td></tr>
<tr><td>Contenu utilisateur</td><td><strong>Uniquement avec l’IA cloud</strong></td><td>Le texte nécessaire à une requête que vous adressez à Luna, et son résultat, conservés brièvement comme décrit ci-dessous. Votre bibliothèque elle-même reste sur votre appareil et dans votre propre iCloud.</td></tr>
<tr><td>Achats</td><td><strong>Uniquement si vous vous abonnez</strong></td><td>La transaction signée qu’Apple envoie pour votre formule : produit, dates, statut de l’essai et du renouvellement. Nous ne voyons jamais vos informations de paiement.</td></tr>
<tr><td>Données d’utilisation</td><td><strong>Uniquement avec un compte</strong></td><td>Le nombre de requêtes à l’IA cloud et leur taille, pour pouvoir appliquer le quota mensuel. Aucun outil d’analyse et aucun relevé de la façon dont vous utilisez l’app.</td></tr>
<tr><td>Localisation, contacts, santé, navigation, historique de recherche, diagnostics</td><td>Non</td><td>L’app ne demande ni votre localisation ni vos contacts, et ne contient ni outil de rapport de plantage ni outil d’analyse.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Suivi :</strong> aucun. Nous ne relions pas les données vous concernant à celles d’autres entreprises, n’affichons pas de publicité et ne partageons rien avec des courtiers en données. L’app n’affiche jamais la demande d’autorisation de suivi d’Apple, car elle n’a rien à demander.</p>
""",

"p.device.h": "Ce qui reste sur votre appareil",
"p.device.b": """
<p>Second Brain stocke votre bibliothèque dans son propre espace de stockage privé sur votre appareil, protégé par la protection des données d’iOS et votre code d’accès :</p>
<ul>
  <li><strong>Captures</strong> : ce que vous avez dit ou tapé, exactement comme vous l’avez dit, ainsi que les corrections que vous y avez apportées.</li>
  <li><strong>Enregistrements et pièces jointes</strong> : les fichiers audio, photos, PDF, fichiers et liens que vous avez ajoutés, et le texte qui en est extrait sur votre appareil.</li>
  <li><strong>Ce qui en est tiré</strong> : tâches, événements, notes, idées, projets, historique des vérifications et historique d’annulation.</li>
  <li><strong>Données de recherche</strong> : l’index de recherche sémantique, construit sur votre appareil avec les modèles linguistiques d’Apple.</li>
  <li><strong>Réglages</strong> : langue, rappels, widgets, choix d’IA et calendriers que vous avez sélectionnés.</li>
  <li><strong>Dans le trousseau iOS</strong> : votre session de connexion et le compteur mensuel de captures vocales, Remplissages intelligents et questions gratuits. Ce compteur ne contient que des nombres et reste sur cet appareil, même si l’app est réinstallée.</li>
</ul>
<p>Une bibliothèque invité et chaque compte connecté disposent d’espaces de stockage distincts sur l’appareil. Si vous utilisez la Sauvegarde iCloud ou une sauvegarde chiffrée sur ordinateur, Apple peut inclure ces données dans cette sauvegarde, sous votre compte Apple. Nous n’y avons pas accès.</p>
<p><strong>Widgets et Spotlight.</strong> Les widgets n’affichent les titres des éléments que si vous activez {K_widgets}. Les éléments enregistrés n’apparaissent dans Spotlight que si vous activez {K_spotlight}. Dans les deux cas, tout reste sur votre appareil.</p>
""",

"p.ai.h": "L’IA sur votre appareil, et Luna dans le cloud",
"p.ai.b": """
<h3>IA sur l’appareil</h3>
<p>Sur les appareils compatibles, le Remplissage intelligent, l’organisation, les réponses et les résumés s’effectuent avec le modèle sur l’appareil d’Apple. Ce que vous écrivez ne quitte pas votre appareil, et l’utilisation sur l’appareil n’est jamais décomptée d’un quota cloud.</p>
<h3>Luna, notre IA cloud</h3>
<p>Luna est un modèle d’<strong>OpenAI</strong> que nous appelons depuis notre propre serveur. Votre appareil ne contacte jamais OpenAI directement, et l’app ne contient aucune clé d’API. Luna ne fonctionne que si vous vous êtes <strong>connecté et avez activé {K_luna}</strong>. Elle est utilisée quand l’IA sur l’appareil n’est pas disponible ou ne peut pas traiter une requête, ou en premier si vous avez Light ou Pro et avez choisi Luna comme moteur. Désactiver ce bouton arrête immédiatement toute nouvelle requête à l’IA cloud.</p>
<p>Pour chaque requête, seul le texte nécessaire est envoyé :</p>
<ul>
  <li><strong>Organisation et Remplissage intelligent</strong> : le texte de la capture à organiser, y compris le texte extrait sur votre appareil d’une photo ou d’un PDF joint, votre fuseau horaire et votre langue, ainsi que les noms et de courts résumés de 30 de vos projets au maximum.</li>
  <li><strong>Interroger votre Brain</strong> : votre question et de courts extraits de 12 éléments enregistrés au maximum, que votre appareil a jugés pertinents.</li>
  <li><strong>Rangement</strong> (Light et Pro) : le texte de la note que vous avez demandé de ranger.</li>
  <li><strong>Résumé quotidien</strong> (Pro) : le décompte de ce qui est à faire et de courts extraits de 10 de vos éléments au maximum pour ce jour-là.</li>
</ul>
<p><strong>Jamais envoyés :</strong> l’audio, les images ou les fichiers eux-mêmes ; les captures marquées {K_device_only} ; vos événements de l’app Calendrier ; votre nom ou votre adresse e-mail (nous ne les avons pas) ; tout identifiant qui permettrait à OpenAI de savoir qui vous êtes.</p>
<h3>Durée de conservation</h3>
<p>Notre serveur conserve un résultat <strong>jusqu’à 24 heures</strong>, afin qu’une requête interrompue puisse être terminée sans être exécutée deux fois, ni décomptée deux fois de votre quota. Ensuite, le texte est supprimé, et un reçu sans contenu (un hachage irréversible de la requête, les identifiants des éléments utilisés et l’heure) est conservé jusqu’à un an pour le suivi des quotas. Supprimer définitivement un élément supprime aussi tous les résultats qui en sont tirés, et supprimer votre compte les supprime tous.</p>
<p>Nous demandons à OpenAI de ne pas stocker les réponses. Selon les conditions de son API, OpenAI n’utilise pas ces données pour entraîner ses modèles. OpenAI peut conserver les entrées et les sorties pendant une durée limitée afin de détecter les abus, comme décrit dans ses <a href="https://openai.com/enterprise-privacy/">règles relatives aux données de l’API</a>.</p>
<p>Les suggestions et les réponses générées par l’IA peuvent être erronées. C’est pourquoi chaque champ du Remplissage intelligent peut être vérifié avant d’être enregistré, et chaque réponse indique ses sources.</p>
""",

"p.sync.h": "Synchronisation iCloud",
"p.sync.b": """
<p>Avec Light ou Pro, vous pouvez activer {K_sync}. Votre bibliothèque, y compris les captures, éléments, projets, corrections, historique et pièces jointes, est alors stockée dans une <strong>base de données CloudKit privée de votre propre compte iCloud</strong>, pour que vos appareils restent synchronisés. Apple la stocke conformément à sa propre <a href="https://www.apple.com/legal/privacy/">politique de confidentialité</a>. Nous, le développeur, ne pouvons pas lire vos données iCloud privées, et notre serveur ne reçoit jamais de copie de votre bibliothèque.</p>
<p>Les captures marquées {K_device_only} ne sont jamais synchronisées. Lorsque la synchronisation est activée, iOS peut transmettre des notifications silencieuses du service de notifications push d’Apple pour signaler à l’app qu’un changement a eu lieu. Aucun jeton push ne nous est envoyé.</p>
""",

"p.account.h": "Votre compte et notre serveur",
"p.account.b": """
<p>Un compte est facultatif. Lorsque vous vous connectez avec Apple, nous ne demandons <strong>ni nom ni adresse e-mail</strong>. Notre serveur, qui fonctionne sur <strong>Cloudflare</strong>, conserve :</p>
<ul>
  <li><strong>Un identifiant de compte</strong> : un hachage irréversible de l’identifiant qu’Apple nous transmet. L’identifiant Apple d’origine n’est pas stocké.</li>
  <li><strong>Des données de connexion</strong> : les sessions, stockées uniquement sous forme de hachages et expirant au bout de 30 jours, et le jeton de connexion d’Apple, chiffré et utilisé uniquement pour le révoquer quand vous supprimez votre compte.</li>
  <li><strong>La vérification de l’appareil</strong> : la clé publique créée par App Attest d’Apple sur chaque appareil sur lequel vous vous connectez (jusqu’à 20), pour que le serveur sache qu’il communique avec une copie authentique de Second Brain.</li>
  <li><strong>Vos choix et votre formule</strong> : si la synchronisation et l’IA cloud sont activées, votre formule et ses dates de renouvellement, et les transactions qu’Apple envoie pour la confirmer.</li>
  <li><strong>Les compteurs d’utilisation</strong> : la part du quota cloud de ce mois que vous avez utilisée.</li>
  <li><strong>Les résultats de l’IA cloud</strong>, conservés brièvement comme décrit ci-dessus.</li>
</ul>
<p>Pour protéger le service contre les abus, le serveur conserve brièvement un hachage irréversible de votre adresse IP combinée à la minute en cours. Il est supprimé en quelques minutes. Nous ne conservons aucun journal des requêtes, et notre serveur ne reçoit jamais votre bibliothèque.</p>
<p><strong>Import de pages</strong> (Pro) : quand vous demandez à importer le texte d’une page web, notre serveur récupère lui-même cette page publique et renvoie son texte lisible à votre appareil. L’adresse et le texte de la page ne sont ni stockés ni envoyés à Luna.</p>
""",

"p.voice.h": "Voix, parole et enregistrements",
"p.voice.b": """
<p>La capture vocale n’utilise le micro que pendant l’enregistrement. La parole est transcrite <strong>sur votre appareil</strong> avec la reconnaissance vocale d’Apple. Votre enregistrement n’est envoyé ni à Apple ni à nous pour la transcription, mais la première utilisation d’une langue entraîne le téléchargement des ressources vocales d’Apple.</p>
<p>Les enregistrements sont conservés dans votre bibliothèque. Une fois la transcription terminée, l’audio est supprimé <strong>7 jours</strong> après l’enregistrement de la capture, sauf si vous touchez {K_keep_recording}. Un enregistrement dont la transcription a échoué est conservé jusqu’à ce que vous le supprimiez. Les transcriptions restent après la suppression de leur audio.</p>
""",

"p.permissions.h": "Autorisations",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>Autorisation</th><th>Utilisation</th></tr>
<tr><td>Micro, Reconnaissance vocale</td><td>La capture vocale et la transcription sur l’appareil.</td></tr>
<tr><td>Appareil photo, Photos</td><td>Prendre ou choisir une image à joindre. Seules les images que vous choisissez sont lues.</td></tr>
<tr><td>Calendriers</td><td>Demandée uniquement si vous touchez {K_calendars}. Les calendriers que vous choisissez sont lus sur votre appareil pour être affichés à côté de vos tâches, et ne sont jamais envoyés hors de l’appareil. Un nouvel événement n’est ajouté à l’app Calendrier que par l’éditeur d’Apple lui-même, après votre confirmation.</td></tr>
<tr><td>Notifications</td><td>Les rappels, le résumé du matin et un rappel avant la fin d’un essai gratuit. Tous sont programmés sur votre appareil.</td></tr>
</table></div>
<p style="margin-top:14px">Vous pouvez modifier chacune de ces autorisations dans iOS : {K_settings} → Second Brain. L’app ne demande jamais votre localisation ni vos contacts.</p>
""",

"p.purchases.h": "Achats",
"p.purchases.b": """
<p>Light et Pro sont vendus via l’App Store d’Apple. Le paiement se fait entre vous et Apple, conformément à la <a href="https://www.apple.com/legal/privacy/">politique de confidentialité d’Apple</a>, et nous ne voyons jamais vos informations de paiement. Vous pouvez acheter une formule sans compte : votre iPhone vérifie la transaction signée par Apple, et notre serveur ne conserve rien sur l’achat. Si vous vous connectez, notre serveur vérifie cette transaction et la stocke avec votre compte, pour que la formule vous suive sur vos autres appareils. Un achat fait sans compte est lié au premier compte qui l’envoie. Notre serveur reçoit aussi les avis d’Apple concernant les renouvellements, remboursements et résiliations, et ne les applique qu’aux achats liés à un compte, pour que votre formule reste à jour.</p>
""",

"p.third.h": "Prestataires de services",
"p.third.b": """
<p>Second Brain ne contient <strong>aucun SDK tiers</strong> : ni outil d’analyse, ni publicité, ni outil de rapport de plantage. Les entreprises suivantes traitent des données pour notre compte, chacune uniquement pour la finalité indiquée :</p>
<ul>
  <li><strong>Apple</strong> : « Se connecter avec Apple », App Attest, l’App Store et les achats, la synchronisation iCloud dans votre propre compte, l’envoi de notifications push pour la synchronisation, ainsi que les modèles d’IA et de reconnaissance vocale sur l’appareil.</li>
  <li><strong>Cloudflare</strong> : héberge notre serveur et sa base de données, et lui achemine les requêtes.</li>
  <li><strong>OpenAI</strong> : exécute Luna pour les requêtes à l’IA cloud que vous autorisez, comme décrit ci-dessus.</li>
</ul>
<p>Nous ne vendons ni ne louons de données personnelles, et nous ne partageons rien avec des annonceurs ou des courtiers en données. Nous pouvons divulguer des informations si la loi l’exige. Comme nous détenons très peu de données, il y a peu de choses que nous pourrions divulguer.</p>
""",

"p.retention.h": "Durée de conservation",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>Données</th><th>Conservation</th></tr>
<tr><td>Votre bibliothèque sur votre appareil</td><td>Jusqu’à ce que vous la supprimiez. Les éléments que vous supprimez restent 30 jours dans {K_recently_deleted}.</td></tr>
<tr><td>Enregistrements vocaux</td><td>7 jours après une transcription terminée, sauf si vous les gardez. Jusqu’à ce que vous les supprimiez si la transcription a échoué.</td></tr>
<tr><td>Votre copie iCloud</td><td>Jusqu’à ce que vous la supprimiez ou supprimiez votre compte. Elle est stockée par Apple dans votre iCloud.</td></tr>
<tr><td>Résultat de l’IA cloud</td><td>Jusqu’à 24 heures. Un reçu sans contenu est conservé jusqu’à 1 an.</td></tr>
<tr><td>Sessions de connexion</td><td>30 jours après la dernière actualisation</td></tr>
<tr><td>Compte, formule et compteurs d’utilisation</td><td>Tant que votre compte existe</td></tr>
<tr><td>Adresse IP hachée pour la protection contre les abus</td><td>Quelques minutes</td></tr>
<tr><td>Sauvegardes du serveur</td><td>Les sauvegardes de base de données de notre hébergeur peuvent contenir des données supprimées pendant 30 jours au maximum avant d’expirer.</td></tr>
</table></div>
""",

"p.delete.h": "Exportation et suppression",
"p.delete.b": """
<p>Tout est entre vos mains, dans l’app :</p>
<ul>
  <li><strong>Exporter</strong> : {EXPORT} crée un fichier ZIP contenant toute votre bibliothèque, vos fichiers d’origine et la liste de ce qui n’a pas pu être inclus.</li>
  <li><strong>Supprimer de cet appareil</strong> : {DELETE_LOCAL} supprime la bibliothèque de cet appareil. Cela ne supprime ni votre compte ni sa copie iCloud.</li>
  <li><strong>Supprimer votre compte</strong> : {DELETE_ACCOUNT} supprime votre copie iCloud, tout ce que notre serveur conserve sur le compte et la bibliothèque du compte sur cet appareil, et révoque l’accès de Second Brain via « Se connecter avec Apple ».</li>
</ul>
<p>Après la suppression d’un compte, notre serveur ne conserve qu’un marqueur sans contenu : l’identifiant de compte haché, signalé comme supprimé, ses compteurs d’utilisation, et des hachages irréversibles de ses identifiants d’achat et d’appareil. Ce marqueur permet de terminer une suppression interrompue et empêche qu’un achat ou l’essai cloud gratuit ne soit réclamé deux fois. Il ne contient ni contenu, ni nom, ni adresse e-mail. Les instructions détaillées se trouvent sur la page <a href="{BASE}{L}/delete-data/">Vos données</a>.</p>
""",

"p.rights.h": "Vos droits",
"p.rights.b": """
<p>Selon votre lieu de résidence, notamment en vertu du RGPD, du RGPD britannique (UK GDPR) et du CCPA/CPRA californien, vous avez le droit d’accéder aux données personnelles que nous détenons à votre sujet, de les rectifier, de les exporter, d’en limiter le traitement, de vous opposer à leur traitement et de les effacer, de retirer votre consentement à tout moment, et d’introduire une réclamation auprès de votre autorité de protection des données. La plupart de ces droits sont intégrés à l’app : l’exportation, la suppression, et les boutons de synchronisation et d’IA cloud. Pour toute autre demande, écrivez à {MAIL} et nous vous répondrons sous 30 jours.</p>
<p>Lorsque le RGPD s’applique, nous nous fondons sur : l’<strong>exécution du contrat</strong> pour fournir les fonctionnalités que vous utilisez et la formule que vous avez achetée ; le <strong>consentement</strong> pour la synchronisation iCloud et l’IA cloud, que vous pouvez retirer avec leurs boutons ; nos <strong>intérêts légitimes</strong> à assurer la sécurité du service et à prévenir les abus (App Attest et protection contre les abus) ; et une <strong>obligation légale</strong> pour les justificatifs d’achat.</p>
""",

"p.children.h": "Enfants",
"p.children.b": """
<p>Second Brain ne s’adresse pas aux enfants de moins de 13 ans, ni à ceux qui n’ont pas atteint l’âge du consentement numérique applicable là où vous vivez. Nous ne collectons pas sciemment de données personnelles auprès d’enfants. Si vous pensez qu’un enfant a créé un compte, écrivez à {MAIL} et nous vous aiderons à le supprimer.</p>
""",

"p.transfers.h": "Lieu de traitement des données",
"p.transfers.b": """
<p>Cloudflare exécute notre serveur sur son réseau mondial, et OpenAI et Apple peuvent traiter des données aux États-Unis et dans d’autres pays. Lorsque la loi l’exige, ces transferts sont encadrés par les conditions de traitement des données des prestataires, y compris des clauses contractuelles types. Les données stockées sur votre appareil restent là où se trouve votre appareil.</p>
""",

"p.changes.h": "Modifications de cette politique",
"p.changes.b": """
<p>Si l’app change ce qu’elle fait des données, nous mettrons à jour cette politique et la date indiquée en haut de page. Nous signalerons les changements importants dans les notes de version de l’app et, lorsque la loi l’exige, nous vous redemanderons votre consentement. Nous ne commencerons jamais à envoyer votre contenu vers une nouvelle destination sans un nouveau choix de votre part.</p>
""",

"p.contact.h": "Nous contacter",
"p.contact.b": """
<p>{COMPANY}, l’éditeur de Second Brain, est le responsable du traitement des données personnelles décrites ici. Pour toute question ou demande relative à la confidentialité, écrivez à {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Conditions d’utilisation",
"t.h1": "Le contrat, en termes simples.",
"t.sub": "Ce que fait Second Brain, ce que son IA peut et ne peut pas promettre, comment votre contenu est traité, et comment Light et Pro sont facturés.",
"t.meta": "En vigueur à compter du {DATE} · Second Brain par {COMPANY}",

"t.acceptance.h": "1. Acceptation des Conditions",
"t.acceptance.b": """
<p>Les présentes Conditions d’utilisation (les « Conditions ») constituent un accord entre vous et {COMPANY} (« nous »), l’éditeur de l’app Second Brain pour iPhone et iPad (« Second Brain » ou « l’app ») et des services en ligne associés. En installant ou en utilisant Second Brain, vous acceptez les présentes Conditions et notre <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>. Si vous ne les acceptez pas, n’utilisez pas l’app.</p>
""",
"t.who.h": "2. Qui peut utiliser Second Brain",
"t.who.b": """
<p>Vous devez avoir au moins 13 ans, ou l’âge du consentement numérique applicable là où vous vivez, pour utiliser Second Brain. Si vous n’avez pas atteint l’âge de la majorité là où vous vivez, vous devez obtenir l’autorisation d’un parent ou d’un tuteur pour souscrire un abonnement.</p>
""",
"t.what.h": "3. Ce qu’est Second Brain, et ce qu’il n’est pas",
"t.what.b": """
<p>Second Brain est un outil personnel qui permet de capturer des pensées à la voix ou par écrit et de les organiser en tâches, événements, notes et idées, avec des rappels, une recherche et des réponses tirées de ce que vous avez enregistré.</p>
<p>Second Brain n’est <strong>pas</strong> un service médical, juridique, financier ou autre service professionnel, et rien de ce qu’il produit ne constitue un conseil professionnel. Ne vous en servez pas comme seul moyen de vous souvenir de quelque chose de crucial, comme un médicament, une échéance légale ou une question de sécurité. Les rappels dépendent d’iOS, de vos réglages et de votre appareil, et peuvent ne pas arriver. En cas d’urgence, contactez les services d’urgence locaux.</p>
""",
"t.account.h": "4. Votre compte",
"t.account.b": """
<p>Un compte est facultatif et utilise « Se connecter avec Apple ». Vous êtes responsable de votre compte Apple, de votre appareil et de son code d’accès, ainsi que de l’activité effectuée avec votre compte. Chaque compte est destiné à une seule personne. Vous pouvez vous déconnecter à tout moment, et vous pouvez supprimer votre compte dans l’app, comme décrit sur la page <a href="{BASE}{L}/delete-data/">Vos données</a>.</p>
""",
"t.content.h": "5. Votre contenu",
"t.content.b": """
<p>Tout ce que vous capturez, joignez ou écrivez dans Second Brain (« votre contenu ») vous appartient. Nous n’en revendiquons aucunement la propriété. Vous nous accordez uniquement l’autorisation limitée nécessaire pour traiter votre contenu afin de fournir les fonctionnalités que vous choisissez : par exemple, envoyer du texte à Luna lorsque vous avez activé l’IA cloud, ou récupérer une page web que vous avez demandé à importer. Nous n’utilisons pas votre contenu pour entraîner des modèles d’IA, et nous ne le vendons pas.</p>
<p>Vous êtes responsable de votre contenu et devez disposer du droit de le capturer, de l’importer et de le stocker, y compris tout ce qui concerne d’autres personnes. Votre bibliothèque se trouve sur votre appareil et, si vous le choisissez, dans votre propre iCloud. Conservez vos propres exportations. Nous ne détenons pas de copie de votre bibliothèque et ne pouvons pas la restaurer si les copies de votre appareil et d’iCloud sont perdues.</p>
""",
"t.ai.h": "6. Fonctionnalités d’IA",
"t.ai.b": """
<p>Second Brain utilise l’intelligence artificielle pour suggérer comment organiser ce que vous capturez, compléter des détails comme les dates et les heures, répondre à des questions à partir de votre bibliothèque et rédiger des résumés. Il utilise le modèle sur l’appareil d’Apple lorsqu’il est disponible et, si vous l’autorisez, <strong>Luna</strong>, un modèle cloud fourni par OpenAI via notre serveur.</p>
<p><strong>Les résultats de l’IA peuvent être erronés, incomplets ou obsolètes.</strong> L’IA peut mal lire une date, manquer une tâche ou déformer ce que dit une source. Vérifiez les suggestions avant de les créer, et vérifiez les sources d’une réponse avant de vous y fier. Si vous activez le {K_quick}, les éléments sont créés sans cette vérification, par votre propre choix. Tout ce dont le Remplissage intelligent n’est pas sûr va dans {K_needs_review}, et {K_undo} reste disponible.</p>
<p>Vous vous engagez à ne pas utiliser les fonctionnalités d’IA pour produire des contenus illicites, préjudiciables ou contrefaisants, ni pour tenter d’extraire les modèles sous-jacents, leurs instructions ou les clés de notre service. Nous pouvons changer les modèles utilisés, ajuster les limites ou suspendre une fonctionnalité pour protéger le service. Dans ce cas, le reste de l’app continue de fonctionner et votre contenu enregistré n’est pas affecté.</p>
""",
"t.cloud.h": "7. Fonctionnalités cloud et quotas",
"t.cloud.b": """
<p>La <strong>synchronisation</strong> utilise votre propre compte iCloud et dépend du service d’Apple, de votre stockage iCloud et de votre connexion. L’<strong>IA cloud</strong> est limitée par le quota mensuel de votre formule : Light inclut 300 captures IA cloud et 100 réponses cloud par mois, Pro en inclut 700 et 250, et un compte gratuit connecté bénéficie d’un essai unique. Les quotas se renouvellent chaque mois civil et les quantités non utilisées ne sont pas reportées. Pour garantir un usage équitable du service, une limite s’applique également à la quantité totale de texte traitée chaque mois. L’<strong>import de pages</strong> (Pro) ne récupère que des pages publiques, et vous devez disposer du droit d’utiliser ce que vous importez.</p>
<p>Nous nous efforçons de maintenir les fonctionnalités cloud disponibles, mais nous ne garantissons pas qu’elles fonctionneront sans interruption. Les fonctionnalités sur l’appareil continuent de fonctionner sans elles.</p>
""",
"t.subscriptions.h": "8. Abonnements et facturation",
"t.subscriptions.b": """
<p>Second Brain est gratuit à télécharger et à utiliser, avec des limites mensuelles par appareil pour la capture vocale, le Remplissage intelligent et Interroger votre Brain. L’enregistrement de ce que vous capturez n’est jamais bloqué. Les formules payantes sont des abonnements à renouvellement automatique vendus par l’intermédiaire d’Apple, au prix affiché dans l’app et sur l’App Store pour votre pays :</p>
<ul>
  <li><strong>Light mensuel</strong> : facturé tous les mois.</li>
  <li><strong>Pro mensuel</strong> : facturé tous les mois.</li>
  <li><strong>Pro annuel</strong> : facturé tous les ans, en commençant par un <strong>essai gratuit de 7 jours</strong> pour les nouveaux abonnés éligibles.</li>
</ul>
<p>Vous pouvez vous abonner sans compte Second Brain. Sans compte, les fonctions de la formule sur l’appareil fonctionnent sur les iPhone qui utilisent le compte Apple avec lequel vous vous êtes abonné. Se connecter avec Apple lie la formule à votre compte et ajoute ses fonctions cloud. Le paiement est débité de votre compte Apple lorsque vous confirmez l’achat. Un essai gratuit se transforme en abonnement payant, sauf si vous l’annulez au moins 24 heures avant sa fin. Les abonnements se renouvellent automatiquement au même prix et pour la même durée, sauf si le renouvellement automatique est désactivé au moins 24 heures avant la fin de la période en cours. Le renouvellement est débité de votre compte Apple dans les 24 heures précédant la fin de cette période. Vous pouvez gérer ou résilier un abonnement dans les <a href="https://apps.apple.com/account/subscriptions">réglages d’abonnement de l’App Store</a> ou depuis {K_manage} dans l’app. La résiliation prend effet à la fin de la période en cours. Les remboursements sont gérés par Apple selon ses propres règles. Utilisez {K_restore} pour récupérer une formule sur un autre appareil. Les abonnements ne sont pas partagés via le Partage familial.</p>
<p><strong>Si un abonnement prend fin</strong>, rien de ce que vous avez enregistré n’est supprimé. La lecture, la modification, la recherche, l’exportation et la suppression continuent de fonctionner, les limites mensuelles gratuites s’appliquent de nouveau, et la synchronisation et les quotas cloud s’arrêtent. Supprimer l’app ou votre compte ne résilie pas un abonnement : résiliez-le auprès d’Apple. Nous pouvons modifier les prix ou les fonctionnalités d’une formule. Apple vous informera avant qu’une hausse de prix ne s’applique à vous, comme l’exigent ses règles.</p>
""",
"t.licence.h": "9. Licence et propriété intellectuelle",
"t.licence.b": """
<p>Nous vous accordons une licence personnelle, non exclusive, non transférable et révocable pour utiliser Second Brain sur les appareils Apple dont vous êtes propriétaire ou que vous contrôlez, conformément aux présentes Conditions et aux Règles d’utilisation de l’App Store. Second Brain, son nom, son design, ses illustrations (y compris le personnage du cerveau), ses textes et son code appartiennent à {COMPANY} et sont protégés par la loi. Vous ne pouvez pas copier, modifier, distribuer, vendre ou louer l’app, en faire de l’ingénierie inverse ni en créer des œuvres dérivées, sauf lorsque la loi l’autorise expressément.</p>
""",
"t.use.h": "10. Utilisation acceptable",
"t.use.b": """
<p>Vous vous engagez à ne pas : utiliser Second Brain de manière illicite ou pour stocker du contenu que vous n’avez pas le droit de détenir ; perturber, surcharger ou sonder nos serveurs ; contourner les quotas, App Attest ou le système d’achat de l’App Store ; accéder au compte d’une autre personne ; ou utiliser le service pour harceler des personnes, leur nuire ou les enregistrer sans le consentement exigé par la loi.</p>
""",
"t.termination.h": "11. Résiliation",
"t.termination.b": """
<p>Vous pouvez cesser d’utiliser Second Brain à tout moment, et vous pouvez supprimer votre compte dans l’app. Nous pouvons suspendre ou interrompre l’accès aux fonctionnalités cloud si vous enfreignez gravement ou de manière répétée les présentes Conditions, ou si la loi l’exige. Dans la mesure du possible, nous vous en informerons au préalable. Le contenu présent sur votre appareil reste le vôtre, et vous pouvez l’exporter. Les sections 5, 6, 9, 12, 13 et 15 restent en vigueur après la résiliation.</p>
""",
"t.warranty.h": "12. Garanties et responsabilité",
"t.warranty.b": """
<p>Second Brain est fourni « en l’état » et « selon disponibilité », sans garantie d’aucune sorte, expresse ou implicite. Nous ne garantissons pas que les résultats de l’IA seront exacts, que les rappels arriveront toujours, que la synchronisation ou les fonctionnalités cloud fonctionneront sans interruption, ni que l’app sera exempte d’erreurs. Dans toute la mesure permise par la loi, {COMPANY} n’est pas responsable des dommages indirects, accessoires, spéciaux, consécutifs ou punitifs, ni des pertes de données, de bénéfices ou d’opportunités, résultant de votre utilisation de l’app ou de l’impossibilité de l’utiliser, y compris de tout ce qu’une fonctionnalité d’IA a produit ou d’un rappel qui n’est pas arrivé. Lorsque la responsabilité ne peut pas être exclue, elle est limitée au montant que vous avez payé pour Second Brain au cours des douze mois précédant la réclamation. Rien dans les présentes Conditions ne limite les droits dont vous disposez en tant que consommateur et auxquels il ne peut être renoncé.</p>
""",
"t.apple.h": "13. Dispositions relatives à Apple",
"t.apple.b": """
<p>Second Brain est distribué via l’App Store d’Apple. Les présentes Conditions sont conclues entre vous et {COMPANY}, et non avec Apple. Apple n’a aucune obligation de fournir des services de maintenance ou d’assistance pour l’app, et n’est pas responsable du traitement des réclamations la concernant, y compris les réclamations relatives à la responsabilité du fait des produits, à la conformité légale ou à la propriété intellectuelle. Si l’app n’est pas conforme à une garantie applicable, vous pouvez en informer Apple, qui vous remboursera le prix d’achat éventuel. Dans toute la mesure permise par la loi, Apple n’a aucune autre obligation de garantie concernant l’app. Apple et ses filiales sont des tiers bénéficiaires des présentes Conditions et peuvent les faire valoir à votre encontre. Pour tout ce que les présentes Conditions ne prévoient pas, le <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrat de licence d’utilisateur final des applications sous licence</a> d’Apple s’applique. Vous confirmez que vous ne vous trouvez pas dans un pays soumis à un embargo du gouvernement des États-Unis et que vous ne figurez sur aucune liste américaine de personnes interdites ou faisant l’objet de restrictions, et vous devez respecter les conditions de tiers applicables lorsque vous utilisez l’app.</p>
""",
"t.changes.h": "14. Modifications des présentes Conditions",
"t.changes.b": """
<p>Nous pouvons mettre à jour les présentes Conditions à mesure que Second Brain évolue. La date indiquée en haut de page changera alors, et nous signalerons les changements importants dans les notes de version de l’app. Continuer à utiliser l’app après une mise à jour signifie que vous acceptez les Conditions révisées. Dans le cas contraire, vous pouvez cesser d’utiliser l’app et supprimer votre compte.</p>
""",
"t.law.h": "15. Droit applicable",
"t.law.b": """
<p>Les présentes Conditions sont régies par le droit du Pakistan, où {COMPANY} exerce ses activités, sans égard aux règles de conflit de lois. Si le droit de votre pays de résidence vous accorde des protections auxquelles il ne peut être dérogé par contrat, ces protections continuent de s’appliquer.</p>
""",
"t.contact.h": "16. Nous contacter",
"t.contact.b": """
<p>Pour toute question sur les présentes Conditions : {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Vos données",
"d.h1": "Exporter ou supprimer vos données",
"d.sub": "Votre bibliothèque se trouve sur votre appareil et, si vous avez choisi la synchronisation, dans votre propre iCloud. Voici comment en faire une copie, la supprimer d’un appareil, ou supprimer votre compte et tout ce qu’il contient.",
"d.meta": 'Voir aussi la <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>',

"d.where.h": "Où sont stockées vos données",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>Données</th><th>Emplacement</th><th>Comment les supprimer</th></tr>
<tr><td>Captures, enregistrements, pièces jointes, tâches, notes, projets, historique</td><td>Votre appareil</td><td>{DELETE_LOCAL}, ou supprimez votre compte (voir ci-dessous)</td></tr>
<tr><td>La même bibliothèque, si vous avez activé la synchronisation</td><td>Une base de données privée dans votre propre iCloud</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Identifiant de compte, formule, choix de consentement, compteurs d’utilisation, clés des appareils</td><td>Notre serveur (Cloudflare)</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Résultats de l’IA cloud</td><td>Notre serveur, jusqu’à 24 heures</td><td>Supprimés automatiquement, lorsque vous supprimez définitivement l’élément, ou lorsque vous supprimez votre compte</td></tr>
<tr><td>Compteur mensuel d’utilisation gratuite</td><td>Le trousseau iOS de cet appareil (nombres uniquement)</td><td>Remis à zéro chaque mois. iOS peut le conserver après la suppression de l’app</td></tr>
<tr><td>Abonnement</td><td>Votre compte Apple</td><td>Résiliez-le auprès d’Apple (voir ci-dessous)</td></tr>
</table></div>
""",
"d.export.h": "Faites d’abord une copie",
"d.export.b": """
<ol class="steps">
  <li><div>Ouvrez Second Brain et accédez à {K_settings}.</div></li>
  <li><div>Touchez {K_export}, puis {K_share_export}.</div></li>
  <li><div>Enregistrez le fichier ZIP dans Fichiers ou envoyez-le où vous voulez. Il contient votre bibliothèque (aux formats JSON et Markdown, plus un fichier CSV des tâches), vos fichiers d’origine et la liste de ce qui n’a pas pu être inclus.</div></li>
</ol>
""",
"d.local.h": "Supprimer de cet appareil",
"d.local.b": """
<p>Pour supprimer un élément, supprimez-le, puis retirez-le de {K_settings} → {K_recently_deleted} avec {K_delete_permanently}. Sinon, il est supprimé automatiquement au bout de 30 jours.</p>
<p>Pour supprimer toute la bibliothèque de cet appareil, utilisez {DELETE_LOCAL}. Cela ne supprime <strong>pas</strong> votre compte, sa copie iCloud ni une bibliothèque invité distincte. Supprimer l’app efface aussi ses données de l’appareil.</p>
""",
"d.account.h": "Supprimer votre compte",
"d.account.b": """
<ol class="steps">
  <li><div>Ouvrez {K_settings} → {K_cloud_choices}.</div></li>
  <li><div>Touchez {K_delete_account} et confirmez.</div></li>
  <li><div>Second Brain supprime la copie iCloud du compte, tout ce que notre serveur conserve sur le compte (sessions, formule, choix, compteurs d’utilisation, clés des appareils et résultats de l’IA) et la bibliothèque du compte sur cet appareil. Il révoque aussi son accès via « Se connecter avec Apple ». Votre bibliothèque invité distincte reste sur l’appareil.</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>Si votre connexion a expiré, l’app vous demande de vous reconnecter avec le même compte Apple pour terminer. Si vous n’avez plus l’appareil, installez Second Brain sur n’importe quel iPhone ou iPad, connectez-vous avec le même compte Apple et supprimez le compte depuis cet appareil.</div></div>
<p style="margin-top:16px">Ensuite, notre serveur ne conserve qu’un marqueur sans contenu : l’identifiant de compte haché, signalé comme supprimé, ses compteurs d’utilisation, et des hachages irréversibles de ses identifiants d’achat et d’appareil. Cela permet de terminer une suppression interrompue et empêche qu’un achat ou l’essai gratuit ne soit réclamé deux fois. Les sauvegardes de base de données conservées par notre hébergeur expirent sous 30 jours.</p>
""",
"d.subscription.h": "Votre abonnement",
"d.subscription.b": """
<p>Supprimer vos données, votre compte ou l’app ne résilie <strong>pas</strong> un abonnement. Celui-ci appartient à votre compte Apple. Résiliez-le dans les <a href="https://apps.apple.com/account/subscriptions">réglages d’abonnement de l’App Store</a> : il reste actif jusqu’à la fin de la période en cours. Les remboursements sont gérés par l’<a href="https://support.apple.com/billing">Assistance Apple</a>.</p>
""",
"d.email.h": "Écrivez-nous",
"d.email.b": """
<p>Si vous ne pouvez pas utiliser l’app, ou si vous avez une question sur vos données, écrivez à {MAIL}. Nous vous répondrons sous 30 jours. Nous ne détenons ni nom ni adresse e-mail pour votre compte : nous chercherons donc avec vous comment le retrouver. Le plus rapide est généralement de vous connecter sur n’importe quel appareil et de supprimer le compte depuis celui-ci. Merci de ne pas nous envoyer vos captures ou enregistrements. Nous n’en avons pas besoin pour vous aider.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "Erreur 404",
"nf.h1": "Impossible de trouver cette page.",
"nf.sub": "Même un second cerveau oublie un lien de temps en temps.",
"nf.cta": "Retour à l’assistance",
"nf.b": 'Cette page n’existe pas. Essayez l’<a href="{BASE}/">Assistance</a>, la <a href="{BASE}/privacy/">Politique de confidentialité</a> ou les <a href="{BASE}/terms/">Conditions d’utilisation</a>.',

}
