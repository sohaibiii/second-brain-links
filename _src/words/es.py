# -*- coding: utf-8 -*-
"""Spanish (es). English is the fallback; k.* are the app's own labels."""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Soporte",
"nav.about": "Acerca de",
"nav.privacy": "Privacidad",
"nav.terms": "Términos",
"nav.data": "Tus datos",

"ui.skip": "Saltar al contenido",
"ui.pages": "Páginas",
"ui.footer": "Pie de página",
"ui.lang": "Idioma",
"ui.toc": "En esta página",
"ui.rights": "Todos los derechos reservados.",
"ui.store_soon": "Próximamente en el App Store",
"ui.store_get": "Descárgalo en el App Store",
"ui.date": "16 de octubre de 2026",
"ui.last_updated": "Última actualización: {DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "Esta traducción se ofrece para tu comodidad. Si difiere de la versión en inglés, prevalece la versión en inglés.",

# The app's own words, copied from SecondBrain/Localizable.xcstrings. Do not retranslate.
"k.settings": "Ajustes",
"k.cloud_choices": "Opciones de sincronización e IA en la nube",
"k.account": "Tu cuenta",
"k.delete_account": "Eliminar cuenta y biblioteca",
"k.keep_account": "Conservar cuenta",
"k.delete_local": "Eliminar todos los datos locales",
"k.export": "Preparar una exportación",
"k.share_export": "Compartir exportación de la biblioteca",
"k.recently_deleted": "Eliminado recientemente",
"k.delete_permanently": "Eliminar definitivamente",
"k.data_handled": "Cómo se tratan tus datos",
"k.privacy_screen": "Tu privacidad",
"k.sync": "Sincronizar mi biblioteca",
"k.sync_now": "Sincronizar ahora",
"k.luna": "Usar Luna para organizar y responder",
"k.on_device": "IA en el dispositivo",
"k.language": "Idioma",
"k.restore": "Restaurar compras",
"k.manage": "Gestionar suscripción",
"k.sign_out": "Cerrar sesión y abrir la biblioteca de invitado",
"k.keep_recording": "Conservar esta grabación",
"k.needs_review": "Por revisar",
"k.smart_org": "Organización inteligente",
"k.smart_fill": "Relleno inteligente",
"k.quick": "Modo rápido",
"k.ask": "Pregunta a tu cerebro",
"k.calendars": "Conectar el Calendario de Apple",
"k.morning": "Resumen matutino",
"k.reminders": "Notificaciones de recordatorios",
"k.spotlight": "Mostrar elementos guardados en Spotlight",
"k.device_only": "Guardar solo en este iPhone",
"k.undo": "Deshacer",
"k.widgets": "Mostrar títulos en los widgets",

"meta.support.title": "Second Brain — Soporte",
"meta.support.desc": "Soporte oficial de Second Brain: cómo funcionan la captura, el Relleno inteligente y «Pregunta a tu cerebro», qué necesita la app, respuestas a preguntas frecuentes y cómo contactarnos.",
"meta.about.title": "Second Brain — Solo dilo. Nosotros lo ordenamos.",
"meta.about.desc": "Second Brain convierte lo que dices o escribes en tareas, eventos, notas e ideas, conserva tu original y responde preguntas a partir de lo que has guardado, con la IA en el dispositivo como primera opción.",
"meta.privacy.title": "Política de privacidad — Second Brain",
"meta.privacy.desc": "Qué guarda Second Brain en tu dispositivo, qué llega a iCloud, qué conserva nuestro servidor y cuándo exactamente se envían tus palabras a la IA en la nube.",
"meta.terms.title": "Términos de uso — Second Brain",
"meta.terms.desc": "Términos de uso (EULA) de Second Brain: tu contenido, las funciones de IA, los cupos en la nube y cómo se facturan las suscripciones Light y Pro.",
"meta.data.title": "Elimina tus datos — Second Brain",
"meta.data.desc": "Cómo exportar tu biblioteca, eliminarla de este dispositivo y eliminar tu cuenta de Second Brain y todo lo que contiene en iCloud y en nuestro servidor.",
"meta.nf.title": "Página no encontrada — Second Brain",
"meta.nf.desc": "No se ha encontrado la página.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Soporte",
"s.h1": "Ayuda con Second Brain",
"s.sub": "Dilo o escríbelo, y Second Brain lo ordena en tareas, eventos, notas e ideas, conserva tu original y te permite deshacer cualquier cambio. Esta página explica cómo funciona, qué necesita y cómo contactarnos.",
"s.cta": "Leer las preguntas frecuentes",
"s.meta": 'Funciona sin cuenta · IA en el dispositivo primero · <a href="{BASE}{L}/privacy/">Política de privacidad</a>',

"s.how.h": "Cómo funciona Second Brain",
"s.how.b": """
<p class="lead">Sácalo de tu cabeza en segundos y vuelve a encontrarlo cuando importe.</p>
<p>Toca el micrófono y habla como piensas, o escribe. Second Brain guarda primero tus palabras, tal como las dijiste, para que no se pierda nada. Después sugiere lo que contienen: una tarea con fecha límite, un evento con hora, una nota o una idea, archivados en el proyecto adecuado. Revisas cada sugerencia antes de que se cree nada, y cualquier cambio se puede deshacer.</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>Captura</b><span>La captura de voz empieza a grabar en cuanto se abre. También puedes escribir, compartir texto, enlaces, fotos o archivos desde otras apps, o adjuntarlos a una captura.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>Relleno inteligente y revisión</b><span>Toca Listo y el Relleno inteligente prepara borradores de tareas, eventos, notas e ideas con sus fechas y horas. Puedes editar cada campo antes de tocar Crear. Lo que no tenga claro queda resaltado o va a {K_needs_review}.</span></div></li>
  <li><span class="tile">{chat}</span><div><b>Pregunta a tu cerebro</b><span>Haz una pregunta con tus propias palabras. Las respuestas salen solo de lo que has guardado, con las fuentes indicadas para que puedas abrirlas y comprobarlas.</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>Hoy y Calendario</b><span>Lo que vence, lo que viene y lo que importa, además de una vista semanal con tu Calendario de Apple junto a tus tareas. Recordatorios opcionales y un resumen matutino.</span></div></li>
  <li><span class="tile">{undo}</span><div><b>Tu original, siempre</b><span>Las palabras que capturaste se quedan en tu biblioteca junto a lo que se creó a partir de ellas. {K_undo} revierte cualquier organización, y los elementos eliminados esperan en {K_recently_deleted} durante 30 días.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Privado por defecto</b><span>La organización y las respuestas se generan en tu dispositivo con el modelo integrado de Apple, si tu dispositivo es compatible. La sincronización en la nube y la IA en la nube permanecen desactivadas hasta que tú las elijas. Consulta <a href="{BASE}{L}/privacy/">Privacidad</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Requisitos",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Dispositivo</th><td><strong>iPhone o iPad</strong> con <strong>iOS 18 o iPadOS 18</strong> o posterior.</td></tr>
<tr><th>IA en el dispositivo</th><td>Un dispositivo compatible con <strong>Apple Intelligence</strong>, con iOS 26 o iPadOS 26 o posterior, Apple Intelligence activado y su modelo descargado. En otros dispositivos puedes seguir capturando, organizando a mano, buscando y creando recordatorios. En ese caso, el Relleno inteligente y las respuestas pueden usar Luna en la nube, si inicias sesión y lo permites.</td></tr>
<tr><th>Cuenta</th><td><strong>Opcional.</strong> La captura, la organización, la búsqueda, la exportación y la eliminación funcionan sin cuenta, y también puedes comprar Light o Pro sin ella. Necesitas Iniciar sesión con Apple para sincronizar con iCloud, usar Luna o importar el texto de páginas.</td></tr>
<tr><th>Conexión a internet</th><td>No es necesaria para capturar, usar la IA en el dispositivo, buscar ni exportar. Sí lo es para iniciar sesión, hacer compras, sincronizar con iCloud, usar Luna, importar páginas y descargar por primera vez los archivos de voz de Apple para tu idioma.</td></tr>
<tr><th>Permisos</th><td>Micrófono y Reconocimiento de voz para la captura de voz. Cámara o Fotos solo cuando adjuntas una imagen. Calendarios solo si conectas el Calendario de Apple. Notificaciones solo para los recordatorios y el resumen matutino. Cada permiso se pide la primera vez que lo usas.</td></tr>
<tr><th>iCloud</th><td>Para sincronizar, una cuenta de iCloud con suficiente espacio libre. La sincronización está incluida en Light y Pro.</td></tr>
<tr><th>Idiomas</th><td>Inglés, alemán, español, francés, japonés, coreano, portugués de Brasil y chino simplificado. La captura de voz escucha en el idioma de la app. Elígelo en {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Primeros pasos",
"s.start.b": """
<ol class="steps">
  <li><div><b>Abre Second Brain.</b> No hace falta registrarse. Tu biblioteca está en tu dispositivo desde el primer segundo.</div></li>
  <li><div><b>Toca el micrófono y di lo que tienes en mente.</b> Permite el acceso al micrófono y al reconocimiento de voz cuando iOS te lo pida. O escribe.</div></li>
  <li><div><b>Toca Listo.</b> El Relleno inteligente prepara borradores de tareas, eventos, notas e ideas. Revisa cada campo, cambia lo que quieras y toca Crear.</div></li>
  <li><div><b>Pregunta a tu cerebro.</b> Pregunta «¿qué le prometí a Sam?» o «¿cuándo es el dentista?» y abre las fuentes citadas para comprobarlo.</div></li>
  <li><div><b>Opcional:</b> para sincronizar con iCloud o usar Luna, abre {K_settings} → {K_cloud_choices} e inicia sesión con Apple. Cada opción tiene su propio interruptor.</div></li>
</ol>
""",

"s.faq.h": "Preguntas frecuentes",
"s.faq.b": """
<dl class="faq">
<dt>¿Necesito una cuenta?</dt>
<dd>No. La captura, la organización, la búsqueda, los recordatorios, la exportación y la eliminación funcionan sin cuenta, en tu dispositivo. Solo necesitas una cuenta para sincronizar con iCloud, usar Luna en la nube o importar el texto de páginas. Puedes comprar un plan sin ella. Iniciar sesión nunca sube tu biblioteca de invitado existente. Tú eliges qué pensamientos copiar en la cuenta.</dd>
<dt>¿Qué es gratis?</dt>
<dd>La captura escrita, las tareas y los proyectos, la búsqueda local, la transcripción en el dispositivo, los recordatorios, la edición, la exportación y la eliminación son gratis e ilimitados. El plan Gratis también incluye <strong>20 capturas de voz, 40 usos de Relleno inteligente y 5 preguntas en {K_ask} al mes</strong>, contados en cada dispositivo y restablecidos el día 1 de cada mes. Guardar nunca se bloquea: cuando llegas a un límite, puedes seguir escribiendo y guardando. Una cuenta con sesión iniciada que permita la IA en la nube también recibe una muestra única de 10 capturas con IA en la nube y 5 respuestas.</dd>
<dt>¿Qué añaden Light y Pro?</dt>
<dd><strong>Light</strong> elimina los límites mensuales de captura de voz, Relleno inteligente y «Pregunta a tu cerebro», añade el {K_quick} y la sincronización privada con iCloud, e incluye 300 capturas con IA en la nube y 100 respuestas en la nube al mes. <strong>Pro</strong> ofrece 700 capturas con IA en la nube y 250 respuestas en la nube al mes, un resumen diario en la nube y la importación del texto de páginas web. Light se factura cada mes. Pro puede ser mensual o anual, y el plan anual empieza con 7 días gratis para nuevos suscriptores que cumplan los requisitos. Los precios se muestran en la app y en el App Store para tu país, y Apple gestiona la facturación.</dd>
<dt>¿En qué se diferencian la IA en el dispositivo y Luna?</dt>
<dd>La IA en el dispositivo es el modelo de Apple que funciona en tu dispositivo. Nada de lo que escribes sale de él. Luna es un modelo en la nube de OpenAI que funciona a través de nuestro servidor. Solo se usa si inicias sesión y activas {K_luna}, y solo dentro del cupo en la nube de tu plan. La IA en el dispositivo va primero. Luna se encarga cuando tu dispositivo no puede. Light y Pro pueden elegir Luna como motor principal en {K_settings}. Las capturas marcadas con {K_device_only} nunca van a Luna, elijas el motor que elijas.</dd>
<dt>¿Qué hace «{K_device_only}»?</dt>
<dd>Esa captura, y todo lo que se crea a partir de ella, nunca se sincroniza con iCloud ni se envía a la IA en la nube. La IA en el dispositivo puede seguir organizándola.</dd>
<dt>¿Puedo fiarme de las respuestas?</dt>
<dd>Las respuestas se basan solo en lo que has guardado, y cada respuesta indica sus fuentes para que puedas abrirlas. Aun así, la IA puede malinterpretar u omitir cosas, así que comprueba las fuentes antes de fiarte de una respuesta para algo importante.</dd>
<dt>¿Qué pasa con mis grabaciones de voz?</dt>
<dd>Se transcriben en tu dispositivo y no se envían a Apple ni a nosotros para transcribirlas. Cuando la transcripción está completa, el audio se elimina a los 7 días, salvo que toques {K_keep_recording}. Si una transcripción falla, el audio se conserva hasta que lo elimines, para que puedas volver a intentarlo. Las transcripciones se conservan aunque su audio ya no esté.</dd>
<dt>¿Se sincroniza entre mi iPhone y mi iPad?</dt>
<dd>Sí, con Light o Pro. Inicia sesión con la misma Cuenta de Apple en ambos y activa {K_sync}. Tu biblioteca se sincroniza a través de tu propio almacenamiento privado de iCloud, que nosotros no podemos leer.</dd>
<dt>¿Qué pasa si termina mi suscripción?</dt>
<dd>No se elimina nada de lo que guardaste. La lectura, la edición, la búsqueda, la exportación y la eliminación siguen funcionando, y vuelven a aplicarse los límites mensuales gratuitos. La sincronización y los cupos en la nube se detienen hasta que vuelvas a suscribirte.</dd>
<dt>¿Cómo restauro una compra en un dispositivo nuevo?</dt>
<dd>En el dispositivo nuevo, usa la misma Cuenta de Apple con la que te suscribiste y toca {K_restore} en la pantalla de planes. Las funciones del plan en ese iPhone se activan al momento. Si el plan está vinculado a tu cuenta de Second Brain, inicia sesión también con Apple para recuperar la sincronización con iCloud y tu cupo en la nube.</dd>
<dt>¿Puedo usar la app en mi idioma?</dt>
<dd>Second Brain habla ocho idiomas y sigue el idioma de tu dispositivo. Para elegir otro sin cambiar nada más, abre {K_settings} → {K_language}. A partir de entonces, la captura de voz escucha en ese idioma.</dd>
<dt>¿Cómo saco mis datos o los elimino?</dt>
<dd>{EXPORT} crea un ZIP con toda tu biblioteca y tus archivos originales. {DELETE_ACCOUNT} elimina tu cuenta, su copia en iCloud y lo que conserva nuestro servidor. Tienes los detalles en la página <a href="{BASE}{L}/delete-data/">Tus datos</a>.</dd>
</dl>
""",

"s.trouble.h": "Solución de problemas",
"s.trouble.b": """
<h3>El Relleno inteligente o las respuestas no están disponibles</h3>
<ul>
  <li>La IA en el dispositivo necesita un dispositivo compatible con Apple Intelligence, iOS 26 o posterior, Apple Intelligence activado en los Ajustes de iOS y su modelo completamente descargado. La descarga puede tardar un rato después de activarlo por primera vez.</li>
  <li>Si tu dispositivo no puede usarla, inicia sesión y activa {K_luna} en {K_settings} → {K_cloud_choices}, o sigue organizando a mano. Tu captura se guarda en cualquier caso.</li>
  <li>Si ves un mensaje de límite, has agotado las capturas de voz, los usos de Relleno inteligente o las preguntas gratis de este mes en este dispositivo. Se restablecen el día 1 de cada mes, y guardar sigue funcionando.</li>
</ul>
<h3>La captura de voz no transcribe</h3>
<ul>
  <li>Revisa {K_settings} de iOS → Second Brain → Micrófono y Reconocimiento de voz.</li>
  <li>La primera vez que usas un idioma, los archivos de voz de Apple necesitan conexión para descargarse.</li>
  <li>Si una transcripción falla, la grabación se conserva para que puedas reintentarlo o añadir el texto tú mismo.</li>
</ul>
<h3>La sincronización no se actualiza</h3>
<ul>
  <li>La sincronización requiere Light o Pro, una cuenta con sesión iniciada y {K_sync} activado en {K_settings} → {K_cloud_choices}.</li>
  <li>Asegúrate de que el dispositivo tiene una sesión iniciada en iCloud y espacio libre en iCloud, y toca {K_sync_now}.</li>
  <li>Si el mismo elemento cambió en dos dispositivos, la app te pregunta qué versión conservar. Tu captura original siempre se conserva.</li>
</ul>
<h3>No llegan los recordatorios</h3>
<p>{K_settings} muestra si las {K_reminders} están activadas. Si se desactivaron, toca la fila para abrir los Ajustes de iOS y permitirlas.</p>
<h3>No se reconoce mi plan</h3>
<p>Asegúrate de que tu iPhone usa la misma Cuenta de Apple con la que te suscribiste y toca {K_restore}. Si el plan está vinculado a tu cuenta de Second Brain, inicia sesión también con Apple. Los reembolsos y las dudas sobre facturación los gestiona Apple a través del <a href="https://support.apple.com/billing">Soporte técnico de Apple</a>.</p>
<h3>La app está en el idioma equivocado</h3>
<p>Abre {K_settings} → {K_language} y elige el que quieras. La app, sus widgets y su opción del menú Compartir cambian al instante.</p>
""",

"s.contact.h": "Contacto",
"s.contact.b": """
<p>¿Tienes una pregunta, has encontrado un error o algo que debería funcionar no funciona? Escríbenos y te responderá una persona.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Indica el modelo de tu dispositivo, la versión de iOS, la versión de la app (aparece al final de {K_settings}) y lo que esperabas que pasara. Por favor, no envíes tus capturas ni grabaciones salvo que te las pidamos. Rara vez las necesitamos.</span></div></div>
<p style="margin-top:16px" class="small">La facturación, los reembolsos y los cambios de suscripción los gestiona Apple: <a href="https://apps.apple.com/account/subscriptions">gestionar suscripciones</a> · <a href="https://support.apple.com/billing">solicitar un reembolso</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Acerca de Second Brain",
"a.h1": "Solo dilo. Nosotros lo ordenamos.",
"a.sub": "Habla como piensas. Second Brain lo convierte en tareas, eventos, notas e ideas, conserva tu original y lo vuelve a encontrar cuando preguntas.",
"a.cta": "Soporte",
"a.meta": "iPhone y iPad · iOS 18+ · ocho idiomas · funciona sin cuenta",
"a.lead": "Second Brain es un lugar tranquilo para todo lo que tienes en mente. Captúralo en segundos con la voz o por escrito, comprueba lo que el Relleno inteligente ha hecho con ello y pregunta a tu cerebro cuando lo necesites, con fuentes que puedes abrir y comprobar.",

"a.f1.icon": "mic",
"a.f1.h": "Solo dilo.",
"a.f1.p": "La captura de voz empieza a escuchar en cuanto se abre, en ocho idiomas. Cada tarea, plan e idea queda recogido mientras hablas, y se conserva el original.",
"a.f2.icon": "sparkle",
"a.f2.h": "Una frase. Tres cosas hechas.",
"a.f2.p": "El Relleno inteligente convierte lo que dijiste en tareas, eventos y notas con las fechas y horas ya puestas. Revisas cada campo antes de que se cree nada.",
"a.f3.icon": "chat",
"a.f3.h": "Pregunta lo que quieras.",
"a.f3.p": "Las respuestas salen solo de lo que has guardado, con las fuentes indicadas para que puedas abrirlas y comprobarlas.",
"a.f4.icon": "calendar",
"a.f4.h": "Tu día y tu semana.",
"a.f4.p": "Lo que vence y lo que viene en una sola pantalla tranquila, con tu Calendario de Apple junto a tus tareas, recordatorios y un resumen matutino opcional.",
"a.f5.icon": "undo",
"a.f5.h": "No se pierde nada.",
"a.f5.p": "Tus palabras originales se quedan junto a todo lo que se crea a partir de ellas. Cualquier organización se puede deshacer, y puedes exportar toda tu biblioteca cuando quieras.",
"a.f6.icon": "lock",
"a.f6.h": "Privado por defecto.",
"a.f6.p": 'IA en el dispositivo primero, sin anuncios y sin rastreo. La sincronización en la nube y la IA en la nube esperan cada una tu sí, y cualquier captura puede quedarse solo en este iPhone. <a href="{BASE}{L}/privacy/">Cómo funciona.</a>',

"a.price.h": "Planes",
"a.price.b": """
<p>Second Brain se puede usar gratis, y guardar nunca se bloquea. Light y Pro eliminan los límites mensuales y añaden sincronización e IA en la nube.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Gratis</div><div class="price">$0</div><ul><li>Captura escrita, tareas, proyectos, búsqueda, recordatorios y exportación ilimitados</li><li>20 capturas de voz, 40 usos de Relleno inteligente y 5 preguntas al mes</li><li>IA en el dispositivo en los dispositivos compatibles</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">Mensual</div><ul><li>Captura de voz, Relleno inteligente y preguntas ilimitados</li><li>Modo rápido</li><li>Sincronización privada con iCloud</li><li>300 capturas con IA en la nube y 100 respuestas en la nube al mes</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">Mensual · Anual</div><ul><li>Todo lo de Light</li><li>700 capturas con IA en la nube y 250 respuestas en la nube al mes</li><li>Un resumen diario en la nube</li><li>Importación del texto de páginas web</li><li>El plan anual empieza con 7 días gratis</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Los precios se muestran en la app y en el App Store para tu país. Apple gestiona la facturación. <a href="{BASE}{L}/terms/#subscriptions">Condiciones de la suscripción.</a></p>
""",

"a.platform.h": "Creada para dispositivos Apple",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone y iPad</b><span>iOS 18 o iPadOS 18 y posteriores. IA en el dispositivo en los dispositivos compatibles con Apple Intelligence.</span></div></li>
  <li><span class="tile">{share}</span><div><b>Allí donde estés</b><span>Una opción en el menú Compartir para guardar desde cualquier app, widgets en la pantalla de inicio, Siri y Atajos, y búsqueda opcional en Spotlight.</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>Tu iCloud, no el nuestro</b><span>La sincronización funciona a través de tu propio almacenamiento privado de iCloud, así que nunca guardamos una copia de tu biblioteca.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Ocho idiomas</b><span>Inglés, alemán, español, francés, japonés, coreano, portugués de Brasil y chino simplificado, también en la captura de voz. Elige uno en {K_settings} → {K_language}.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Política de privacidad",
"p.h1": "Tus pensamientos son solo tuyos.",
"p.sub": "Second Brain guarda tu biblioteca en tu dispositivo. La sincronización en la nube y la IA en la nube esperan cada una tu sí. Esta página explica exactamente qué sale de tu dispositivo, cuándo sale y quién lo recibe.",
"p.meta": "En vigor desde el {DATE} · se aplica a la app Second Brain para iPhone y iPad, y a este sitio web",

"p.summary.h": "La versión corta",
"p.summary.b": """
<p class="lead">Second Brain funciona sin cuenta. <strong>Tu biblioteca (capturas, grabaciones, archivos adjuntos, tareas, notas y todo lo que se crea a partir de ellos) se almacena en tu dispositivo.</strong> Sin cuenta, la app no nos envía absolutamente nada.</p>
<p>Hay tres cosas que cambian eso, y cada una requiere que tú lo elijas:</p>
<ul>
  <li><strong>La sincronización con iCloud</strong> (Light y Pro) copia tu biblioteca en <em>tu propio</em> almacenamiento privado de iCloud. Nosotros no podemos leerlo.</li>
  <li><strong>La IA en la nube («Luna»)</strong> envía a OpenAI, a través de nuestro servidor, el texto necesario para una solicitud, cuando la IA en el dispositivo no puede ayudar o cuando eliges Luna. No se envía nada a menos que inicies sesión y la actives.</li>
  <li><strong>Una cuenta</strong> (Iniciar sesión con Apple) permite que nuestro servidor guarde un registro reducido: un ID de cuenta que es un hash unidireccional, tu plan, tus decisiones de consentimiento y tus recuentos de uso. Nunca pedimos a Apple tu nombre ni tu correo electrónico.</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>Sin publicidad, sin analíticas, sin rastreo y sin SDK de terceros en la app. No vendemos ni compartimos datos personales, y nunca usamos tu contenido para entrenar modelos de IA.</div></div>
<p style="margin-top:16px">Esta política se aplica a la app Second Brain para iPhone y iPad y a este sitio web, ambos publicados por {COMPANY} («nosotros»). La pantalla {K_settings} → {K_data_handled} de la app dice lo mismo de forma más breve.</p>
""",

"p.collect.h": "Qué recopilamos",
"p.collect.b": """
<p>Aquí, «recopilar» se refiere a los datos que salen de tu dispositivo y se guardan en algún lugar donde podemos leerlos. Los datos que solo llegan a tu propio almacenamiento de iCloud no los recopilamos nosotros.</p>
<div class="table-wrap"><table>
<tr><th>Categoría</th><th>¿Se recopila?</th><th>Qué significa</th></tr>
<tr><td>Información de contacto</td><td>No</td><td>Iniciar sesión con Apple está configurado para no compartir con nosotros ningún nombre ni dirección de correo electrónico. La app no tiene ningún campo de correo electrónico.</td></tr>
<tr><td>Identificadores</td><td><strong>Solo con una cuenta</strong></td><td>Un ID de cuenta creado a partir de un hash unidireccional del identificador que nos da Apple, y la clave pública que App Attest de Apple crea en cada uno de tus dispositivos. No se usa ningún identificador publicitario ni ningún ID de dispositivo.</td></tr>
<tr><td>Contenido del usuario</td><td><strong>Solo con IA en la nube</strong></td><td>El texto necesario para una solicitud que haces a Luna, y su resultado, conservados brevemente como se describe más abajo. Tu biblioteca en sí se queda en tu dispositivo y en tu propio iCloud.</td></tr>
<tr><td>Compras</td><td><strong>Solo si te suscribes</strong></td><td>La transacción firmada que Apple envía para tu plan: producto, fechas, estado de la prueba y de la renovación. Nunca vemos los datos de pago.</td></tr>
<tr><td>Datos de uso</td><td><strong>Solo con una cuenta</strong></td><td>Recuentos de las solicitudes de IA en la nube y de su tamaño, para poder aplicar el cupo mensual. Sin analíticas ni registro de cómo usas la app.</td></tr>
<tr><td>Ubicación, contactos, salud, navegación, historial de búsqueda, diagnóstico</td><td>No</td><td>La app no solicita la ubicación ni los contactos y no contiene ningún sistema de informes de fallos ni de analíticas.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Rastreo:</strong> ninguno. No vinculamos datos sobre ti con datos de otras empresas, no mostramos anuncios y no compartimos nada con intermediarios de datos. La app nunca muestra el aviso de rastreo de Apple porque no tiene nada que pedir.</p>
""",

"p.device.h": "Qué se queda en tu dispositivo",
"p.device.b": """
<p>Second Brain almacena tu biblioteca en su propio almacenamiento privado en tu dispositivo, protegido por la protección de datos de iOS y tu código:</p>
<ul>
  <li><strong>Capturas</strong>: lo que dijiste o escribiste, tal como lo dijiste, más las correcciones que hayas hecho.</li>
  <li><strong>Grabaciones y archivos adjuntos</strong>: audio, fotos, PDF, archivos y enlaces que añadiste, y el texto extraído de ellos en tu dispositivo.</li>
  <li><strong>Lo que se creó a partir de ellos</strong>: tareas, eventos, notas, ideas, proyectos, historial de revisión e historial de deshacer.</li>
  <li><strong>Datos de búsqueda</strong>: el índice de búsqueda por significado, creado en tu dispositivo con los modelos de lenguaje de Apple.</li>
  <li><strong>Ajustes</strong>: idioma, recordatorios, widgets, opciones de IA y los calendarios que elegiste.</li>
  <li><strong>En el llavero de iOS</strong>: tu sesión iniciada y el recuento mensual de capturas de voz, usos de Relleno inteligente y preguntas gratis. El recuento solo contiene números y se queda en este dispositivo, aunque se reinstale la app.</li>
</ul>
<p>Una biblioteca de invitado y cada cuenta con sesión iniciada tienen almacenes separados en el dispositivo. Si usas la Copia de seguridad de iCloud o una copia de seguridad cifrada en un equipo, Apple puede incluir estos datos en esa copia de seguridad, vinculada a tu Cuenta de Apple. No tenemos acceso a ellos.</p>
<p><strong>Widgets y Spotlight.</strong> Los widgets muestran los títulos de los elementos solo si activas {K_widgets}. Los elementos guardados aparecen en Spotlight solo si activas {K_spotlight}. Ambos se quedan en tu dispositivo.</p>
""",

"p.ai.h": "IA en tu dispositivo, y Luna en la nube",
"p.ai.b": """
<h3>IA en el dispositivo</h3>
<p>En los dispositivos compatibles, el Relleno inteligente, la organización, las respuestas y los resúmenes se generan con el modelo de Apple en el dispositivo. Lo que escribes no sale de tu dispositivo, y el uso en el dispositivo nunca cuenta para ningún cupo en la nube.</p>
<h3>Luna, nuestra IA en la nube</h3>
<p>Luna es un modelo de <strong>OpenAI</strong> al que llamamos desde nuestro propio servidor. Tu dispositivo nunca contacta directamente con OpenAI, y la app no contiene ninguna clave de API. Luna solo funciona si has <strong>iniciado sesión y activado {K_luna}</strong>. Se usa cuando la IA en el dispositivo no está disponible o no puede completar una solicitud, o en primer lugar si tienes Light o Pro y elegiste Luna como motor. Al desactivar el interruptor, se detienen de inmediato las nuevas solicitudes de IA en la nube.</p>
<p>En cada solicitud solo se envía el texto necesario para ella:</p>
<ul>
  <li><strong>Organización y Relleno inteligente</strong>: el texto de la captura que se organiza, incluido el texto extraído en tu dispositivo de una foto o un PDF adjuntos, tu zona horaria y tu idioma, y los nombres y breves resúmenes de hasta 30 de tus proyectos.</li>
  <li><strong>Pregunta a tu cerebro</strong>: tu pregunta y breves fragmentos de hasta 12 elementos guardados que tu dispositivo eligió como relevantes.</li>
  <li><strong>Ordenar</strong> (Light y Pro): el texto de la nota que pediste ordenar.</li>
  <li><strong>Resumen diario</strong> (Pro): recuentos de lo que vence y breves fragmentos de hasta 10 de tus elementos de ese día.</li>
</ul>
<p><strong>Nunca se envía:</strong> el audio, las imágenes ni los archivos en sí; las capturas marcadas con {K_device_only}; tus eventos del Calendario de Apple; tu nombre ni tu correo electrónico (no los tenemos); ningún identificador que pudiera indicar a OpenAI quién eres.</p>
<h3>Cuánto tiempo se conserva</h3>
<p>Nuestro servidor conserva un resultado <strong>hasta 24 horas</strong>, para que una solicitud interrumpida pueda completarse sin ejecutarla dos veces ni descontarla dos veces de tu cupo. Después se elimina el texto, y se conserva hasta un año un comprobante sin contenido (un hash unidireccional de la solicitud, los ID de los elementos que usó y la hora) para la contabilidad del cupo. Eliminar definitivamente un elemento también elimina los resultados creados a partir de él, y eliminar tu cuenta los elimina todos.</p>
<p>Pedimos a OpenAI que no almacene las respuestas. Según las condiciones de su API, OpenAI no usa estos datos para entrenar sus modelos. Puede conservar las entradas y salidas durante un tiempo limitado para detectar abusos, como se describe en sus <a href="https://openai.com/enterprise-privacy/">políticas de datos de la API</a>.</p>
<p>Las sugerencias y respuestas generadas por IA pueden ser incorrectas. Por eso cada campo del Relleno inteligente se puede revisar antes de guardarse, y cada respuesta indica sus fuentes.</p>
""",

"p.sync.h": "Sincronización con iCloud",
"p.sync.b": """
<p>Con Light o Pro, puedes activar {K_sync}. Tu biblioteca, incluidas las capturas, los elementos, los proyectos, las correcciones, el historial y los archivos adjuntos, se almacena entonces en una <strong>base de datos privada de CloudKit en tu propia cuenta de iCloud</strong>, para que tus dispositivos estén sincronizados. Apple la almacena según su propia <a href="https://www.apple.com/legal/privacy/">política de privacidad</a>. Nosotros, como desarrolladores, no podemos leer tus datos privados de iCloud, y nuestro servidor nunca recibe una copia de tu biblioteca.</p>
<p>Las capturas marcadas con {K_device_only} nunca se sincronizan. Cuando la sincronización está activada, iOS puede entregar notificaciones silenciosas del servicio push de Apple para avisar a la app de que algo ha cambiado. No se nos envía ningún token push.</p>
""",

"p.account.h": "Tu cuenta y nuestro servidor",
"p.account.b": """
<p>Tener una cuenta es opcional. Cuando inicias sesión con Apple, <strong>no pedimos ningún nombre ni correo electrónico</strong>. Nuestro servidor, que funciona en <strong>Cloudflare</strong>, conserva:</p>
<ul>
  <li><strong>Un ID de cuenta</strong>: un hash unidireccional del identificador que nos da Apple. El identificador original de Apple no se almacena.</li>
  <li><strong>Datos de inicio de sesión</strong>: las sesiones, almacenadas solo como hashes y que caducan a los 30 días, y el token de inicio de sesión de Apple, cifrado y usado solo para revocarlo cuando eliminas tu cuenta.</li>
  <li><strong>Comprobación del dispositivo</strong>: la clave pública que App Attest de Apple crea en cada dispositivo en el que inicias sesión (hasta 20), para que el servidor sepa que se comunica con una copia auténtica de Second Brain.</li>
  <li><strong>Tus decisiones y tu plan</strong>: si la sincronización y la IA en la nube están activadas, tu plan y sus fechas de renovación, y las transacciones que Apple envía para confirmarlo.</li>
  <li><strong>Recuentos de uso</strong>: cuánto has usado del cupo en la nube de este mes.</li>
  <li><strong>Resultados de la IA en la nube</strong>, conservados brevemente como se describe más arriba.</li>
</ul>
<p>Para proteger el servicio frente a abusos, el servidor conserva brevemente un hash unidireccional de tu dirección IP combinada con el minuto actual. Se elimina en cuestión de minutos. No guardamos registros de solicitudes, y nuestro servidor nunca recibe tu biblioteca.</p>
<p><strong>Importación de páginas</strong> (Pro): cuando pides importar el texto de una página web, nuestro propio servidor obtiene esa página pública y devuelve su texto legible a tu dispositivo. La dirección y el texto de la página no se almacenan ni se envían a Luna.</p>
""",

"p.voice.h": "Voz, reconocimiento de voz y grabaciones",
"p.voice.b": """
<p>La captura de voz usa el micrófono solo mientras grabas. Lo que dices se transcribe <strong>en tu dispositivo</strong> con el reconocimiento de voz de Apple. Tu grabación no se envía a Apple ni a nosotros para transcribirla, aunque el primer uso de un idioma descarga los archivos de voz de Apple.</p>
<p>Las grabaciones se conservan en tu biblioteca. Cuando la transcripción está completa, el audio se elimina <strong>7 días</strong> después de guardarse, salvo que toques {K_keep_recording}. Una grabación cuya transcripción falló se conserva hasta que la elimines. Las transcripciones se conservan aunque su audio ya no esté.</p>
""",

"p.permissions.h": "Permisos",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>Permiso</th><th>Para qué se usa</th></tr>
<tr><td>Micrófono, Reconocimiento de voz</td><td>Captura de voz y transcripción en el dispositivo.</td></tr>
<tr><td>Cámara, Fotos</td><td>Hacer o elegir una imagen para adjuntarla. Solo se leen las imágenes que eliges.</td></tr>
<tr><td>Calendarios</td><td>Solo se pide si tocas {K_calendars}. Los calendarios que eliges se leen en tu dispositivo para mostrarlos junto a tus tareas, y nunca se suben. Un evento nuevo solo se añade al Calendario de Apple a través del propio editor de Apple, después de que lo confirmes.</td></tr>
<tr><td>Notificaciones</td><td>Recordatorios, el resumen matutino y un aviso antes de que termine una prueba gratuita. Todo se programa en tu dispositivo.</td></tr>
</table></div>
<p style="margin-top:14px">Puedes cambiar cualquiera de estos permisos en {K_settings} de iOS → Second Brain. La app nunca pide tu ubicación ni tus contactos.</p>
""",

"p.purchases.h": "Compras",
"p.purchases.b": """
<p>Light y Pro se venden a través del App Store de Apple. El pago se realiza entre tú y Apple, según la <a href="https://www.apple.com/legal/privacy/">política de privacidad de Apple</a>, y nunca vemos tus datos de pago. Puedes comprar un plan sin cuenta: tu iPhone verifica la transacción que firma Apple y nuestro servidor no guarda nada sobre la compra. Si inicias sesión, nuestro servidor verifica esa transacción y la almacena con tu cuenta, de modo que el plan te acompañe en tus otros dispositivos. Una compra hecha sin cuenta se vincula a la primera cuenta que la envía. Nuestro servidor también recibe los avisos de Apple sobre renovaciones, reembolsos y cancelaciones y solo los aplica a compras vinculadas a una cuenta, para que tu plan esté siempre al día.</p>
""",

"p.third.h": "Proveedores de servicios",
"p.third.b": """
<p>Second Brain <strong>no contiene SDK de terceros</strong>: ni analíticas, ni publicidad, ni sistema de informes de fallos. Estas empresas tratan datos por cuenta nuestra, cada una solo para la finalidad indicada:</p>
<ul>
  <li><strong>Apple</strong>: Iniciar sesión con Apple, App Attest, el App Store y las compras, la sincronización con iCloud en tu propia cuenta, la entrega de notificaciones push para la sincronización, y los modelos de IA y de voz en el dispositivo.</li>
  <li><strong>Cloudflare</strong>: aloja nuestro servidor y su base de datos, y le dirige las solicitudes.</li>
  <li><strong>OpenAI</strong>: ejecuta Luna para las solicitudes de IA en la nube que permites, como se describe más arriba.</li>
</ul>
<p>No vendemos ni alquilamos datos personales, y no compartimos nada con anunciantes ni intermediarios de datos. Podemos revelar información si la ley lo exige. Como conservamos tan poco, es poco lo que podríamos revelar.</p>
""",

"p.retention.h": "Cuánto tiempo los conservamos",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>Datos</th><th>Plazo de conservación</th></tr>
<tr><td>Tu biblioteca en tu dispositivo</td><td>Hasta que la elimines. Los elementos que eliminas permanecen en {K_recently_deleted} durante 30 días.</td></tr>
<tr><td>Grabaciones de voz</td><td>7 días después de completarse la transcripción, salvo que las conserves. Si la transcripción falló, hasta que las elimines.</td></tr>
<tr><td>Tu copia en iCloud</td><td>Hasta que la elimines o elimines tu cuenta. Apple la almacena en tu iCloud.</td></tr>
<tr><td>Resultado de la IA en la nube</td><td>Hasta 24 horas. Se conserva un comprobante sin contenido durante un máximo de 1 año.</td></tr>
<tr><td>Sesiones iniciadas</td><td>30 días desde la última renovación</td></tr>
<tr><td>Cuenta, plan y recuentos de uso</td><td>Mientras exista tu cuenta</td></tr>
<tr><td>Dirección IP con hash para la protección frente a abusos</td><td>Unos minutos</td></tr>
<tr><td>Copias de seguridad del servidor</td><td>Las copias de seguridad de la base de datos de nuestro proveedor de alojamiento pueden contener datos eliminados durante un máximo de 30 días antes de caducar.</td></tr>
</table></div>
""",

"p.delete.h": "Exportación y eliminación",
"p.delete.b": """
<p>Todo está en tus manos, dentro de la app:</p>
<ul>
  <li><strong>Exportar</strong>: {EXPORT} crea un ZIP con toda tu biblioteca, tus archivos originales y una lista de lo que no se pudo incluir.</li>
  <li><strong>Eliminar de este dispositivo</strong>: {DELETE_LOCAL} elimina la biblioteca de este dispositivo. No elimina tu cuenta ni su copia en iCloud.</li>
  <li><strong>Eliminar tu cuenta</strong>: {DELETE_ACCOUNT} elimina tu copia en iCloud, todo lo que nuestro servidor conserva sobre la cuenta y la biblioteca de la cuenta en este dispositivo, y revoca el acceso de Second Brain a Iniciar sesión con Apple.</li>
</ul>
<p>Una vez eliminada una cuenta, nuestro servidor solo conserva un marcador sin contenido: el ID de cuenta con hash marcado como eliminado, sus recuentos de uso y hashes unidireccionales de sus identificadores de compra y de dispositivo. Ese marcador permite terminar una eliminación interrumpida e impide que una compra o la muestra gratuita en la nube se reclamen dos veces. No incluye contenido, nombre ni correo electrónico. Tienes instrucciones paso a paso en la página <a href="{BASE}{L}/delete-data/">Tus datos</a>.</p>
""",

"p.rights.h": "Tus derechos",
"p.rights.b": """
<p>Según dónde vivas, incluso en virtud del RGPD, el RGPD del Reino Unido y la CCPA/CPRA de California, tienes derecho a acceder a los datos personales que conservamos sobre ti, rectificarlos, exportarlos, limitar su tratamiento, oponerte a él y suprimirlos, a retirar tu consentimiento en cualquier momento y a presentar una reclamación ante tu autoridad de protección de datos. La mayoría de estos derechos están integrados en la app: exportar, eliminar y los interruptores de sincronización y de IA en la nube. Para cualquier otra cosa, escribe a {MAIL} y te responderemos en un plazo de 30 días.</p>
<p>Cuando se aplica el RGPD, nos basamos en: el <strong>contrato</strong>, para ofrecer las funciones que usas y el plan que compraste; el <strong>consentimiento</strong>, para la sincronización con iCloud y la IA en la nube, que puedes retirar con sus interruptores; el <strong>interés legítimo</strong> en mantener el servicio seguro y prevenir abusos (App Attest y la protección frente a abusos); y la <strong>obligación legal</strong>, para los registros de compras.</p>
""",

"p.children.h": "Menores",
"p.children.b": """
<p>Second Brain no se dirige a menores de 13 años, ni a menores de la edad de consentimiento digital del lugar donde vives. No recopilamos a sabiendas datos personales de menores. Si crees que un menor ha creado una cuenta, escribe a {MAIL} y te ayudaremos a eliminarla.</p>
""",

"p.transfers.h": "Dónde se tratan los datos",
"p.transfers.b": """
<p>Cloudflare ejecuta nuestro servidor en su red global, y OpenAI y Apple pueden tratar datos en Estados Unidos y en otros países. Cuando la ley lo exige, estas transferencias están amparadas por las condiciones de tratamiento de datos de los proveedores, incluidas las cláusulas contractuales tipo. Los datos almacenados en tu dispositivo se quedan donde esté tu dispositivo.</p>
""",

"p.changes.h": "Cambios en esta política",
"p.changes.b": """
<p>Si la app cambia lo que hace con los datos, actualizaremos esta política y la fecha que aparece arriba. Mencionaremos los cambios importantes en las notas de la versión de la app y, cuando la ley lo exija, volveremos a pedir tu consentimiento. Nunca empezaremos a enviar tu contenido a ningún sitio nuevo sin que tú lo elijas de nuevo.</p>
""",

"p.contact.h": "Contacto",
"p.contact.b": """
<p>{COMPANY}, editor de Second Brain, es el responsable del tratamiento de los datos personales descritos aquí. Para preguntas o solicitudes sobre privacidad, escribe a {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Términos de uso",
"t.h1": "El acuerdo, en palabras sencillas.",
"t.sub": "Qué hace Second Brain, qué puede y qué no puede prometer su IA, cómo se trata tu contenido y cómo se facturan Light y Pro.",
"t.meta": "En vigor desde el {DATE} · Second Brain, de {COMPANY}",

"t.acceptance.h": "1. Aceptación de los Términos",
"t.acceptance.b": """
<p>Estos Términos de uso («Términos») constituyen un acuerdo entre tú y {COMPANY} («nosotros»), editor de la app Second Brain para iPhone y iPad («Second Brain» o «la app») y de sus servicios en línea relacionados. Al instalar o usar Second Brain, aceptas estos Términos y nuestra <a href="{BASE}{L}/privacy/">Política de privacidad</a>. Si no estás de acuerdo, no uses la app.</p>
""",
"t.who.h": "2. Quién puede usar Second Brain",
"t.who.b": """
<p>Para usar Second Brain debes tener al menos 13 años o la edad de consentimiento digital del lugar donde vives. Si no has alcanzado la mayoría de edad en el lugar donde vives, necesitas el permiso de uno de tus padres o de tu tutor legal para comprar una suscripción.</p>
""",
"t.what.h": "3. Qué es Second Brain y qué no es",
"t.what.b": """
<p>Second Brain es una herramienta personal para capturar pensamientos por voz o por texto y organizarlos en tareas, eventos, notas e ideas, con recordatorios, búsqueda y respuestas basadas en lo que has guardado.</p>
<p>Second Brain <strong>no</strong> es un servicio médico, jurídico, financiero ni de ningún otro tipo profesional, y nada de lo que genera constituye asesoramiento profesional. No confíes en Second Brain como única forma de recordar algo crítico, como una medicación, un plazo legal o una cuestión de seguridad. Los recordatorios dependen de iOS, de tus ajustes y de tu dispositivo, y es posible que no lleguen. En caso de emergencia, contacta con los servicios de emergencia de tu zona.</p>
""",
"t.account.h": "4. Tu cuenta",
"t.account.b": """
<p>La cuenta es opcional y se crea con Iniciar sesión con Apple. Eres responsable de tu Cuenta de Apple, de tu dispositivo y su código, y de la actividad que se realice con tu cuenta. Cada cuenta es para una sola persona. Puedes cerrar sesión en cualquier momento y puedes eliminar tu cuenta en la app, como se describe en la página <a href="{BASE}{L}/delete-data/">Tus datos</a>.</p>
""",
"t.content.h": "5. Tu contenido",
"t.content.b": """
<p>Todo lo que capturas, adjuntas o escribes en Second Brain («tu contenido») sigue siendo tuyo. No reclamamos ninguna propiedad sobre él. Solo nos concedes el permiso limitado necesario para procesar tu contenido y ofrecerte las funciones que elijas: por ejemplo, enviar texto a Luna cuando has activado la IA en la nube, u obtener una página web que pediste importar. No usamos tu contenido para entrenar modelos de IA ni lo vendemos.</p>
<p>Eres responsable de tu contenido y de tener derecho a capturarlo, importarlo y almacenarlo, incluido cualquier contenido sobre otras personas. Tu biblioteca está en tu dispositivo y, si así lo eliges, en tu propio iCloud. Guarda tus propias exportaciones. No conservamos ninguna copia de tu biblioteca y no podemos restaurarla si se pierden las copias de tu dispositivo y de iCloud.</p>
""",
"t.ai.h": "6. Funciones de IA",
"t.ai.b": """
<p>Second Brain usa inteligencia artificial para sugerir cómo organizar lo que capturas, completar detalles como fechas y horas, responder preguntas a partir de tu biblioteca y redactar resúmenes. Usa el modelo de Apple en el dispositivo cuando está disponible y, si lo permites, <strong>Luna</strong>, un modelo en la nube proporcionado por OpenAI a través de nuestro servidor.</p>
<p><strong>Los resultados de la IA pueden ser incorrectos, incompletos o estar desactualizados.</strong> La IA puede malinterpretar una fecha, omitir una tarea o tergiversar lo que dice una fuente. Revisa las sugerencias antes de crearlas y comprueba las fuentes de una respuesta antes de fiarte de ella. Si activas el {K_quick}, los elementos se crean sin esa revisión, por decisión tuya. Todo lo que el Relleno inteligente no tenga claro va a {K_needs_review}, y {K_undo} sigue disponible.</p>
<p>Aceptas no usar las funciones de IA para generar contenido ilícito, dañino o que infrinja derechos, ni para intentar extraer los modelos subyacentes, sus instrucciones o las claves de nuestro servicio. Podemos cambiar los modelos que usamos, ajustar los límites o pausar una función para proteger el servicio. Si lo hacemos, el resto de la app sigue funcionando y tu contenido guardado no se ve afectado.</p>
""",
"t.cloud.h": "7. Funciones en la nube y cupos",
"t.cloud.b": """
<p><strong>La sincronización</strong> usa tu propia cuenta de iCloud y depende del servicio de Apple, de tu almacenamiento de iCloud y de tu conexión. <strong>La IA en la nube</strong> está limitada por el cupo mensual de tu plan: Light incluye 300 capturas con IA en la nube y 100 respuestas en la nube al mes, Pro incluye 700 y 250, y una cuenta gratuita con sesión iniciada recibe una muestra única. Los cupos se restablecen cada mes natural y las cantidades no usadas no se acumulan. Para que el servicio sea justo, también hay un límite en la cantidad total de texto procesado cada mes. <strong>La importación de páginas</strong> (Pro) solo obtiene páginas públicas, y eres responsable de tener derecho a usar lo que importas.</p>
<p>Trabajamos para mantener disponibles las funciones en la nube, pero no garantizamos que funcionen sin interrupciones. Las funciones en el dispositivo siguen funcionando sin ellas.</p>
""",
"t.subscriptions.h": "8. Suscripciones y facturación",
"t.subscriptions.b": """
<p>Second Brain se puede descargar y usar gratis, con límites mensuales de captura de voz, Relleno inteligente y «Pregunta a tu cerebro» en cada dispositivo. Guardar lo que capturas nunca se bloquea. Los planes de pago son suscripciones con renovación automática que se venden a través de Apple, al precio que se muestra en la app y en el App Store para tu país:</p>
<ul>
  <li><strong>Light mensual</strong>: se factura cada mes.</li>
  <li><strong>Pro mensual</strong>: se factura cada mes.</li>
  <li><strong>Pro anual</strong>: se factura cada año y empieza con una <strong>prueba gratuita de 7 días</strong> para nuevos suscriptores que cumplan los requisitos.</li>
</ul>
<p>Puedes suscribirte sin una cuenta de Second Brain. Sin cuenta, las funciones del plan en el dispositivo funcionan en los iPhone que usan la Cuenta de Apple con la que te suscribiste. Iniciar sesión con Apple vincula el plan a tu cuenta y añade sus funciones en la nube. El pago se carga en tu Cuenta de Apple cuando confirmas la compra. Una prueba gratuita se convierte en una suscripción de pago a menos que la canceles al menos 24 horas antes de que termine. Las suscripciones se renuevan automáticamente al mismo precio y por el mismo periodo, a menos que se desactive la renovación automática al menos 24 horas antes del final del periodo actual. La renovación se cobra en tu Cuenta de Apple dentro de las 24 horas anteriores al final de ese periodo. Puedes gestionar o cancelar una suscripción en los <a href="https://apps.apple.com/account/subscriptions">ajustes de suscripciones del App Store</a> o desde {K_manage} en la app. La cancelación se hace efectiva al final del periodo actual. Apple gestiona los reembolsos según sus políticas. Usa {K_restore} para recuperar un plan en otro dispositivo. Las suscripciones no se comparten mediante En familia.</p>
<p><strong>Si una suscripción termina</strong>, no se elimina nada de lo que guardaste. La lectura, la edición, la búsqueda, la exportación y la eliminación siguen funcionando, vuelven a aplicarse los límites mensuales gratuitos, y la sincronización y los cupos en la nube se detienen. Eliminar la app o tu cuenta no cancela una suscripción. Cancélala con Apple. Podemos cambiar los precios o las funciones de un plan. Apple te avisará antes de que se te aplique una subida de precio, como exigen sus normas.</p>
""",
"t.licence.h": "9. Licencia y propiedad intelectual",
"t.licence.b": """
<p>Te concedemos una licencia personal, no exclusiva, intransferible y revocable para usar Second Brain en dispositivos Apple de tu propiedad o bajo tu control, conforme a estos Términos y a las Reglas de uso del App Store. Second Brain, su nombre, diseño, ilustraciones (incluido el personaje del cerebro), textos y código pertenecen a {COMPANY} y están protegidos por la ley. No puedes copiar, modificar, distribuir, vender, arrendar ni aplicar ingeniería inversa a la app, ni crear obras derivadas de ella, salvo cuando la ley lo permita expresamente.</p>
""",
"t.use.h": "10. Uso aceptable",
"t.use.b": """
<p>Aceptas no: usar Second Brain de forma ilícita ni para almacenar contenido que no tienes derecho a conservar; interferir con nuestros servidores, sobrecargarlos ni sondearlos; eludir los cupos, App Attest o el sistema de compras del App Store; acceder a la cuenta de otra persona; ni usar el servicio para acosar, perjudicar o grabar a personas sin el consentimiento que exige la ley.</p>
""",
"t.termination.h": "11. Terminación",
"t.termination.b": """
<p>Puedes dejar de usar Second Brain en cualquier momento y puedes eliminar tu cuenta en la app. Podemos suspender o cancelar el acceso a las funciones en la nube si incumples estos Términos de forma grave o reiterada, o si la ley lo exige. Cuando sea posible, te avisaremos antes. Tu contenido en tu dispositivo sigue siendo tuyo para exportarlo. Las secciones 5, 6, 9, 12, 13 y 15 siguen vigentes tras la terminación.</p>
""",
"t.warranty.h": "12. Garantías y responsabilidad",
"t.warranty.b": """
<p>Second Brain se ofrece «tal cual» y «según disponibilidad», sin garantías de ningún tipo, expresas o implícitas. No garantizamos que los resultados de la IA sean exactos, que los recordatorios lleguen siempre, que la sincronización o las funciones en la nube funcionen sin interrupciones ni que la app esté libre de errores. En la máxima medida permitida por la ley, {COMPANY} no será responsable de daños indirectos, incidentales, especiales, consecuentes o punitivos, ni de la pérdida de datos, beneficios u oportunidades, derivados del uso o de la imposibilidad de usar la app, incluido cualquier contenido generado por una función de IA o un recordatorio que no llegó. Cuando la responsabilidad no pueda excluirse, se limita al importe que hayas pagado por Second Brain en los doce meses anteriores a la reclamación. Nada de lo dispuesto en estos Términos limita los derechos que tengas como consumidor y que no puedan ser objeto de renuncia.</p>
""",
"t.apple.h": "13. Apple",
"t.apple.b": """
<p>Second Brain se distribuye a través del App Store de Apple. Estos Términos se celebran entre tú y {COMPANY}, no con Apple. Apple no tiene ninguna obligación de prestar servicios de mantenimiento o soporte para la app, y no es responsable de atender ninguna reclamación relacionada con ella, incluidas las reclamaciones por responsabilidad del producto, cumplimiento normativo o propiedad intelectual. Si la app no cumple alguna garantía aplicable, puedes notificarlo a Apple, y Apple te reembolsará el precio de compra, si lo hubiera. En la máxima medida permitida por la ley, Apple no tiene ninguna otra obligación de garantía respecto a la app. Apple y sus filiales son terceros beneficiarios de estos Términos y pueden hacerlos valer frente a ti. En lo que estos Términos no prevean, se aplica el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final de aplicaciones con licencia</a> de Apple. Confirmas que no te encuentras en un país sujeto a un embargo del Gobierno de EE. UU. ni figuras en ninguna lista de partes prohibidas o restringidas de EE. UU., y debes cumplir las condiciones de terceros aplicables al usar la app.</p>
""",
"t.changes.h": "14. Cambios en estos Términos",
"t.changes.b": """
<p>Podemos actualizar estos Términos a medida que Second Brain cambie. Cuando lo hagamos, cambiará la fecha que aparece arriba, y mencionaremos los cambios importantes en las notas de la versión de la app. Si sigues usando la app después de una actualización, aceptas los Términos revisados. Si no los aceptas, puedes dejar de usar la app y eliminar tu cuenta.</p>
""",
"t.law.h": "15. Legislación aplicable",
"t.law.b": """
<p>Estos Términos se rigen por las leyes de Pakistán, donde opera {COMPANY}, sin tener en cuenta las normas sobre conflicto de leyes. Si la ley de tu país de residencia te otorga protecciones que no pueden excluirse por contrato, esas protecciones siguen aplicándose.</p>
""",
"t.contact.h": "16. Contacto",
"t.contact.b": """
<p>Preguntas sobre estos Términos: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Tus datos",
"d.h1": "Exporta o elimina tus datos",
"d.sub": "Tu biblioteca está en tu dispositivo y, si elegiste sincronizar, en tu propio iCloud. Aquí te explicamos cómo hacer una copia, eliminarla de un dispositivo o eliminar tu cuenta y todo lo que contiene.",
"d.meta": 'Consulta también la <a href="{BASE}{L}/privacy/">Política de privacidad</a>',

"d.where.h": "Qué se almacena y dónde",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>Datos</th><th>Dónde están</th><th>Cómo eliminarlos</th></tr>
<tr><td>Capturas, grabaciones, archivos adjuntos, tareas, notas, proyectos, historial</td><td>Tu dispositivo</td><td>{DELETE_LOCAL}, o elimina tu cuenta (más abajo)</td></tr>
<tr><td>La misma biblioteca, si activaste la sincronización</td><td>Una base de datos privada en tu propio iCloud</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>ID de cuenta, plan, decisiones de consentimiento, recuentos de uso, claves de dispositivo</td><td>Nuestro servidor (Cloudflare)</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Resultados de la IA en la nube</td><td>Nuestro servidor, durante un máximo de 24 horas</td><td>Se eliminan solos, cuando eliminas definitivamente el elemento o cuando eliminas tu cuenta</td></tr>
<tr><td>Recuento mensual de uso gratuito</td><td>El llavero de iOS en este dispositivo (solo números)</td><td>Se restablece cada mes. iOS puede conservarlo después de eliminar la app</td></tr>
<tr><td>Suscripción</td><td>Tu Cuenta de Apple</td><td>Cancélala con Apple (más abajo)</td></tr>
</table></div>
""",
"d.export.h": "Haz antes una copia",
"d.export.b": """
<ol class="steps">
  <li><div>Abre Second Brain y ve a {K_settings}.</div></li>
  <li><div>Toca {K_export} y, después, {K_share_export}.</div></li>
  <li><div>Guarda el ZIP en Archivos o envíalo adonde quieras. Contiene tu biblioteca (en JSON, Markdown y un CSV de tareas), tus archivos originales y una lista de lo que no se pudo incluir.</div></li>
</ol>
""",
"d.local.h": "Eliminar de este dispositivo",
"d.local.b": """
<p>Para eliminar un elemento, elimínalo y después quítalo de {K_settings} → {K_recently_deleted} con {K_delete_permanently}. Si no, se elimina automáticamente a los 30 días.</p>
<p>Para eliminar toda la biblioteca de este dispositivo, usa {DELETE_LOCAL}. Esto <strong>no</strong> elimina tu cuenta, su copia en iCloud ni una biblioteca de invitado independiente. Eliminar la app también elimina sus datos del dispositivo.</p>
""",
"d.account.h": "Eliminar tu cuenta",
"d.account.b": """
<ol class="steps">
  <li><div>Abre {K_settings} → {K_cloud_choices}.</div></li>
  <li><div>Toca {K_delete_account} y confirma.</div></li>
  <li><div>Second Brain elimina la copia en iCloud de la cuenta, todo lo que nuestro servidor conserva sobre la cuenta (sesiones, plan, decisiones, recuentos de uso, claves de dispositivo y resultados de IA) y la biblioteca de la cuenta en este dispositivo. También revoca su acceso a Iniciar sesión con Apple. Tu biblioteca de invitado independiente se queda en el dispositivo.</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>Si tu sesión ha caducado, la app te pide que vuelvas a iniciar sesión con la misma Cuenta de Apple para terminar. Si ya no tienes el dispositivo, instala Second Brain en cualquier iPhone o iPad, inicia sesión con la misma Cuenta de Apple y elimina la cuenta desde ahí.</div></div>
<p style="margin-top:16px">Después, nuestro servidor solo conserva un marcador sin contenido: el ID de cuenta con hash marcado como eliminado, sus recuentos de uso y hashes unidireccionales de sus identificadores de compra y de dispositivo. Eso permite terminar una eliminación interrumpida e impide que una compra o la muestra gratuita se reclamen dos veces. Las copias de seguridad de la base de datos que conserva nuestro proveedor de alojamiento caducan en un plazo de 30 días.</p>
""",
"d.subscription.h": "Tu suscripción",
"d.subscription.b": """
<p>Eliminar tus datos, tu cuenta o la app <strong>no</strong> cancela una suscripción. La suscripción pertenece a tu Cuenta de Apple. Cancélala en los <a href="https://apps.apple.com/account/subscriptions">ajustes de suscripciones del App Store</a>; seguirá activa hasta el final del periodo actual. Los reembolsos los gestiona el <a href="https://support.apple.com/billing">Soporte técnico de Apple</a>.</p>
""",
"d.email.h": "Pregúntanos",
"d.email.b": """
<p>Si no puedes usar la app o tienes cualquier pregunta sobre tus datos, escribe a {MAIL}. Te responderemos en un plazo de 30 días. No tenemos ningún nombre ni correo electrónico asociado a tu cuenta, así que colaboraremos contigo para encontrarla. Normalmente, lo más rápido es iniciar sesión en cualquier dispositivo y eliminarla desde ahí. Por favor, no nos envíes tus capturas ni grabaciones. No las necesitamos para ayudarte.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "No hemos encontrado esa página.",
"nf.sub": "Hasta un segundo cerebro olvida un enlace de vez en cuando.",
"nf.cta": "Volver a Soporte",
"nf.b": 'Esa página no está aquí. Prueba con <a href="{BASE}/">Soporte</a>, la <a href="{BASE}/privacy/">Política de privacidad</a> o los <a href="{BASE}/terms/">Términos de uso</a>.',

}
