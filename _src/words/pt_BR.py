# -*- coding: utf-8 -*-
"""Brazilian Portuguese (pt-BR). English is the fallback; k.* are the app's own labels."""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Suporte",
"nav.about": "Sobre",
"nav.privacy": "Privacidade",
"nav.terms": "Termos",
"nav.data": "Seus dados",

"ui.skip": "Pular para o conteúdo",
"ui.pages": "Páginas",
"ui.footer": "Rodapé",
"ui.lang": "Idioma",
"ui.toc": "Nesta página",
"ui.rights": "Todos os direitos reservados.",
"ui.store_soon": "Em breve na App Store",
"ui.store_get": "Baixar na App Store",
"ui.date": "16 de outubro de 2026",
"ui.last_updated": "Última atualização: {DATE}",
# Shown only on translated Privacy and Terms pages.
"ui.prevails": "Esta tradução é oferecida por conveniência. Se houver diferença em relação à versão em inglês, prevalece a versão em inglês.",

# The app's own words, copied from SecondBrain/Localizable.xcstrings. Do not retranslate.
"k.settings": "Ajustes",
"k.cloud_choices": "Escolhas de sincronização e IA na nuvem",
"k.account": "Sua conta",
"k.delete_account": "Apagar conta e biblioteca",
"k.keep_account": "Manter conta",
"k.delete_local": "Apagar todos os dados locais",
"k.export": "Preparar uma exportação",
"k.share_export": "Compartilhar exportação da biblioteca",
"k.recently_deleted": "Apagados recentemente",
"k.delete_permanently": "Apagar permanentemente",
"k.data_handled": "Como seus dados são tratados",
"k.privacy_screen": "Sua privacidade",
"k.sync": "Sincronizar minha biblioteca",
"k.sync_now": "Sincronizar agora",
"k.luna": "Usar a Luna para organizar e responder",
"k.on_device": "IA no aparelho",
"k.language": "Idioma",
"k.restore": "Restaurar compras",
"k.manage": "Gerenciar assinatura",
"k.sign_out": "Sair e abrir a biblioteca de convidado",
"k.keep_recording": "Manter esta gravação",
"k.needs_review": "Para revisar",
"k.smart_org": "Organização inteligente",
"k.smart_fill": "Preenchimento inteligente",
"k.quick": "Modo rápido",
"k.ask": "Pergunte ao seu Cérebro",
"k.calendars": "Conectar o Calendário da Apple",
"k.morning": "Resumo da manhã",
"k.reminders": "Notificações de lembretes",
"k.spotlight": "Mostrar itens salvos no Spotlight",
"k.device_only": "Manter só neste iPhone",
"k.undo": "Desfazer",
"k.widgets": "Mostrar títulos nos widgets",

"meta.support.title": "Second Brain — Suporte",
"meta.support.desc": "Suporte oficial do Second Brain: como funcionam a captura, o Preenchimento inteligente e o Pergunte ao seu Cérebro, do que o app precisa, respostas às perguntas mais comuns e como falar com a gente.",
"meta.about.title": "Second Brain — É só falar. A gente organiza.",
"meta.about.desc": "O Second Brain transforma o que você fala ou digita em tarefas, eventos, notas e ideias, guarda o seu original e responde perguntas a partir do que você salvou, com a IA no aparelho em primeiro lugar.",
"meta.privacy.title": "Política de Privacidade — Second Brain",
"meta.privacy.desc": "O que o Second Brain guarda no seu aparelho, o que vai para o iCloud, o que o nosso servidor mantém e exatamente quando as suas palavras são enviadas para a IA na nuvem.",
"meta.terms.title": "Termos de Uso — Second Brain",
"meta.terms.desc": "Termos de Uso (EULA) do Second Brain: o seu conteúdo, os recursos de IA, as cotas na nuvem e como as assinaturas Light e Pro são cobradas.",
"meta.data.title": "Apague seus dados — Second Brain",
"meta.data.desc": "Como exportar a sua biblioteca, apagá-la deste aparelho e apagar a sua conta do Second Brain e tudo o que ela guarda no iCloud e no nosso servidor.",
"meta.nf.title": "Página não encontrada — Second Brain",
"meta.nf.desc": "Página não encontrada.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Suporte",
"s.h1": "Ajuda com o Second Brain",
"s.sub": "Fale ou digite, e o Second Brain organiza tudo em tarefas, eventos, notas e ideias, guarda o seu original e permite desfazer qualquer alteração. Esta página explica como ele funciona, do que ele precisa e como falar com a gente.",
"s.cta": "Ler as perguntas frequentes",
"s.meta": 'Funciona sem conta · IA no aparelho em primeiro lugar · <a href="{BASE}{L}/privacy/">Política de Privacidade</a>',

"s.how.h": "Como o Second Brain funciona",
"s.how.b": """
<p class="lead">Tire da cabeça em segundos e encontre de novo quando fizer diferença.</p>
<p>Toque no microfone e fale do jeito que você pensa, ou digite. O Second Brain salva primeiro as suas palavras, exatamente como você as disse, para que nada se perca. Depois, ele sugere o que elas contêm: uma tarefa com prazo, um evento com horário, uma nota ou uma ideia, no projeto certo. Você confere cada sugestão antes de qualquer coisa ser criada, e toda alteração pode ser desfeita.</p>
<ul class="rows">
  <li><span class="tile">{mic}</span><div><b>Captura</b><span>A captura por voz começa a gravar assim que abre. Você também pode digitar, compartilhar textos, links, fotos ou arquivos de outros apps, ou anexá-los a uma captura.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>Preenchimento inteligente e revisão</b><span>Toque em Concluído e o Preenchimento inteligente prepara tarefas, eventos, notas e ideias com as datas e os horários. Cada campo pode ser editado antes de você tocar em Criar. Tudo de que ele não tiver certeza fica destacado ou vai para {K_needs_review}.</span></div></li>
  <li><span class="tile">{chat}</span><div><b>Pergunte ao seu Cérebro</b><span>Faça uma pergunta com palavras simples. As respostas vêm só do que você salvou, com as fontes listadas para você abrir e conferir.</span></div></li>
  <li><span class="tile">{calendar}</span><div><b>Hoje e Calendário</b><span>O que vence, o que vem a seguir e o que importa, além de uma visão da semana com o seu Calendário da Apple ao lado das suas tarefas. Lembretes e resumo da manhã opcionais.</span></div></li>
  <li><span class="tile">{undo}</span><div><b>O seu original, sempre</b><span>As palavras que você capturou ficam na sua biblioteca ao lado do que foi criado a partir delas. {K_undo} reverte qualquer organização, e os itens apagados ficam em {K_recently_deleted} por 30 dias.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Privado por padrão</b><span>A organização e as respostas rodam no seu aparelho com o modelo da Apple que funciona no próprio aparelho, quando ele é compatível. A sincronização e a IA na nuvem ficam desativadas até você escolher usá-las. Veja <a href="{BASE}{L}/privacy/">Privacidade</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Requisitos",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Aparelho</th><td><strong>iPhone ou iPad</strong> com <strong>iOS 18 ou iPadOS 18</strong> ou posterior.</td></tr>
<tr><th>IA no aparelho</th><td>Um aparelho compatível com a <strong>Apple Intelligence</strong>, com iOS 26 ou iPadOS 26 ou posterior, a Apple Intelligence ativada e o modelo dela baixado. Em outros aparelhos, você ainda pode capturar, organizar manualmente, buscar e definir lembretes. Nesse caso, o Preenchimento inteligente e as respostas podem usar a Luna na nuvem, se você entrar na sua conta e permitir.</td></tr>
<tr><th>Conta</th><td><strong>Opcional.</strong> Captura, organização, busca, exportação e exclusão funcionam sem conta, e você também pode comprar o Light ou o Pro sem ela. É preciso usar o Iniciar sessão com a Apple para sincronizar com o iCloud, usar a Luna ou importar o texto de páginas.</td></tr>
<tr><th>Internet</th><td>Não é necessária para capturar, para a IA no aparelho, para buscar nem para exportar. É necessária para entrar na conta, fazer compras, sincronizar com o iCloud, usar a Luna, importar páginas e baixar pela primeira vez os arquivos de fala da Apple para o seu idioma.</td></tr>
<tr><th>Permissões</th><td>Microfone e Reconhecimento de Fala para a captura por voz. Câmera ou Fotos só quando você anexa uma imagem. Calendários só se você conectar o Calendário da Apple. Notificações só para lembretes e o resumo da manhã. Cada uma é pedida na primeira vez que você usa o recurso.</td></tr>
<tr><th>iCloud</th><td>Para sincronizar, uma conta do iCloud com espaço livre suficiente. A sincronização está incluída no Light e no Pro.</td></tr>
<tr><th>Idiomas</th><td>Inglês, alemão, espanhol, francês, japonês, coreano, português do Brasil e chinês simplificado. A captura por voz ouve no idioma do app. Escolha o idioma em {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Primeiros passos",
"s.start.b": """
<ol class="steps">
  <li><div><b>Abra o Second Brain.</b> Não há cadastro. A sua biblioteca fica no seu aparelho desde o primeiro segundo.</div></li>
  <li><div><b>Toque no microfone e diga o que está na sua cabeça.</b> Permita o microfone e o reconhecimento de fala quando o iOS pedir. Ou digite.</div></li>
  <li><div><b>Toque em Concluído.</b> O Preenchimento inteligente prepara tarefas, eventos, notas e ideias. Confira cada campo, altere o que quiser e toque em Criar.</div></li>
  <li><div><b>Pergunte ao seu Cérebro.</b> Pergunte “o que eu prometi para o Sam?” ou “quando é o dentista?” e abra as fontes citadas para conferir.</div></li>
  <li><div><b>Opcional:</b> para sincronizar com o iCloud ou usar a Luna, abra {K_settings} → {K_cloud_choices} e use o Iniciar sessão com a Apple. Cada opção é ativada separadamente.</div></li>
</ol>
""",

"s.faq.h": "Perguntas frequentes",
"s.faq.b": """
<dl class="faq">
<dt>Preciso de uma conta?</dt>
<dd>Não. Captura, organização, busca, lembretes, exportação e exclusão funcionam sem conta, no seu aparelho. Uma conta só é necessária para sincronizar com o iCloud, usar a Luna na nuvem ou importar o texto de páginas. Você pode comprar um plano sem ela. Entrar na conta nunca envia a sua biblioteca de convidado existente. Você escolhe quais pensamentos copiar para a conta.</dd>
<dt>O que é grátis?</dt>
<dd>Captura digitada, tarefas e projetos, busca local, transcrição no aparelho, lembretes, edição, exportação e exclusão são grátis e ilimitados. O plano Grátis também inclui <strong>20 capturas por voz, 40 Preenchimentos inteligentes e 5 perguntas em {K_ask} por mês</strong>, contados em cada aparelho e renovados no primeiro dia do mês. Salvar nunca é bloqueado: quando um limite é atingido, você ainda pode digitar e salvar. Uma conta conectada que permite a IA na nuvem também ganha uma amostra única de 10 capturas com IA na nuvem e 5 respostas.</dd>
<dt>O que o Light e o Pro acrescentam?</dt>
<dd>O <strong>Light</strong> remove os limites mensais de captura por voz, Preenchimento inteligente e Pergunte ao seu Cérebro, acrescenta o {K_quick} e a sincronização privada com o iCloud, e inclui 300 capturas com IA na nuvem e 100 respostas na nuvem por mês. O <strong>Pro</strong> traz 700 capturas com IA na nuvem e 250 respostas na nuvem por mês, um resumo diário na nuvem e a importação do texto de páginas da web. O Light é cobrado mensalmente. O Pro é mensal ou anual, e o plano anual começa com 7 dias grátis para novos assinantes elegíveis. Os preços aparecem no app e na App Store para o seu país, e a cobrança é feita pela Apple.</dd>
<dt>Qual é a diferença entre a IA no aparelho e a Luna?</dt>
<dd>A IA no aparelho é o modelo da Apple rodando no seu aparelho. Nada do que você escreve sai dele. A Luna é um modelo na nuvem da OpenAI que roda por meio do nosso servidor. Ela só é usada se você entrar na sua conta e ativar {K_luna}, e só dentro da cota na nuvem do seu plano. A IA no aparelho vem primeiro. A Luna entra quando o seu aparelho não consegue ajudar. No Light e no Pro, você pode escolher a Luna como mecanismo principal em {K_settings}. Capturas marcadas com {K_device_only} nunca vão para a Luna, seja qual for o mecanismo escolhido.</dd>
<dt>O que faz “{K_device_only}”?</dt>
<dd>Essa captura, e tudo o que for criado a partir dela, nunca é sincronizada com o iCloud nem enviada para a IA na nuvem. A IA no aparelho ainda pode organizá-la.</dd>
<dt>Posso confiar nas respostas?</dt>
<dd>As respostas são criadas só a partir do que você salvou, e cada resposta lista as fontes para você abrir. Mesmo assim, a IA pode interpretar algo errado ou deixar algo passar, então confira as fontes antes de confiar em uma resposta para qualquer coisa importante.</dd>
<dt>O que acontece com as minhas gravações de voz?</dt>
<dd>Elas são transcritas no seu aparelho e não são enviadas para a Apple nem para nós para transcrição. Depois que uma transcrição é concluída, o áudio é apagado após 7 dias, a menos que você toque em {K_keep_recording}. Se uma transcrição falhar, o áudio fica guardado até você apagá-lo, para que você possa tentar de novo. As transcrições continuam depois que o áudio é apagado.</dd>
<dt>O app sincroniza entre o meu iPhone e o meu iPad?</dt>
<dd>Sim, com o Light ou o Pro. Entre com a mesma Conta Apple nos dois e ative {K_sync}. A sua biblioteca é sincronizada pelo seu próprio armazenamento privado do iCloud, que nós não conseguimos ler.</dd>
<dt>O que acontece se a minha assinatura terminar?</dt>
<dd>Nada do que você salvou é removido. Leitura, edição, busca, exportação e exclusão continuam funcionando, e os limites mensais grátis voltam a valer. A sincronização e as cotas na nuvem param até você assinar de novo.</dd>
<dt>Como restauro uma compra em um aparelho novo?</dt>
<dd>No aparelho novo, use a mesma Conta Apple com que você assinou e toque em {K_restore} na tela de planos. Os recursos do plano nesse iPhone são ativados na hora. Se o plano estiver vinculado à sua conta do Second Brain, entre também com a Apple para recuperar a sincronização com o iCloud e a sua cota na nuvem.</dd>
<dt>Posso usar o app no meu idioma?</dt>
<dd>O Second Brain fala oito idiomas e segue o idioma do seu aparelho. Para escolher outro sem mudar mais nada, abra {K_settings} → {K_language}. A captura por voz passa a ouvir nesse idioma.</dd>
<dt>Como tiro os meus dados do app ou os apago?</dt>
<dd>Em {EXPORT}, você gera um ZIP de toda a sua biblioteca com os seus arquivos originais. Em {DELETE_ACCOUNT}, você apaga a sua conta, a cópia dela no iCloud e o que o nosso servidor guarda. Os detalhes estão na página <a href="{BASE}{L}/delete-data/">Seus dados</a>.</dd>
</dl>
""",

"s.trouble.h": "Solução de problemas",
"s.trouble.b": """
<h3>O Preenchimento inteligente ou as respostas não estão disponíveis</h3>
<ul>
  <li>A IA no aparelho precisa de um aparelho compatível com a Apple Intelligence, iOS 26 ou posterior, a Apple Intelligence ativada nos Ajustes do iOS e o modelo dela totalmente baixado. O download pode demorar um pouco depois que você a ativa pela primeira vez.</li>
  <li>Se o seu aparelho não consegue rodá-la, entre na sua conta e ative {K_luna} em {K_settings} → {K_cloud_choices}, ou continue organizando manualmente. A sua captura é salva de qualquer forma.</li>
  <li>Se aparecer uma mensagem de limite, você já usou as capturas por voz, os Preenchimentos inteligentes ou as perguntas grátis deste mês neste aparelho. Eles são renovados no primeiro dia do mês, e salvar continua funcionando.</li>
</ul>
<h3>A captura por voz não está transcrevendo</h3>
<ul>
  <li>Verifique em {K_settings} do iOS → Second Brain → Microfone e Reconhecimento de Fala.</li>
  <li>Na primeira vez que você usa um idioma, os arquivos de fala da Apple precisam de conexão para serem baixados.</li>
  <li>Se uma transcrição falhar, a gravação é mantida para você tentar de novo ou adicionar o texto por conta própria.</li>
</ul>
<h3>A sincronização não está atualizando</h3>
<ul>
  <li>A sincronização exige o Light ou o Pro, uma conta conectada e {K_sync} ativado em {K_settings} → {K_cloud_choices}.</li>
  <li>Verifique se o aparelho está conectado ao iCloud e tem espaço livre no iCloud, depois toque em {K_sync_now}.</li>
  <li>Se o mesmo item foi alterado em dois aparelhos, o app pergunta qual versão manter. A sua captura original é sempre preservada.</li>
</ul>
<h3>Os lembretes não chegam</h3>
<p>Em {K_settings}, você vê se as {K_reminders} estão ativadas. Se tiverem sido desativadas, toque na linha para abrir os Ajustes do iOS e permiti-las.</p>
<h3>O meu plano não é reconhecido</h3>
<p>Verifique se o seu iPhone usa a mesma Conta Apple usada na assinatura e toque em {K_restore}. Se o plano estiver vinculado à sua conta do Second Brain, entre também com a Apple. Reembolsos e dúvidas sobre cobrança são tratados pela Apple, pelo <a href="https://support.apple.com/billing">Suporte da Apple</a>.</p>
<h3>O app está no idioma errado</h3>
<p>Abra {K_settings} → {K_language} e escolha o idioma que você quer. O app, os widgets e a extensão de compartilhamento mudam na hora.</p>
""",

"s.contact.h": "Contato",
"s.contact.b": """
<p>Dúvidas, um bug ou algo que deveria funcionar e não funciona? Escreva para a gente e uma pessoa vai responder.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Informe o modelo do aparelho, a versão do iOS, a versão do app (mostrada no fim de {K_settings}) e o que você esperava que acontecesse. Não envie as suas capturas ou gravações, a menos que a gente peça. Raramente precisamos delas.</span></div></div>
<p style="margin-top:16px" class="small">Cobranças, reembolsos e mudanças de assinatura são tratados pela Apple: <a href="https://apps.apple.com/account/subscriptions">gerenciar assinaturas</a> · <a href="https://support.apple.com/billing">solicitar reembolso</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Sobre o Second Brain",
"a.h1": "É só falar. A gente organiza.",
"a.sub": "Fale do jeito que você pensa. O Second Brain transforma isso em tarefas, eventos, notas e ideias, guarda o seu original e encontra tudo de novo quando você pergunta.",
"a.cta": "Suporte",
"a.meta": "iPhone e iPad · iOS 18+ · oito idiomas · funciona sem conta",
"a.lead": "O Second Brain é um lugar tranquilo para tudo o que está na sua cabeça. Capture em segundos por voz ou texto, confira o que o Preenchimento inteligente fez com isso e pergunte ao seu Cérebro quando precisar de volta, com fontes que você pode abrir e conferir.",

"a.f1.h": "É só falar.",
"a.f1.p": "A captura por voz começa a ouvir assim que abre, em oito idiomas. Cada tarefa, plano e ideia é registrado enquanto você fala, e o original fica guardado.",
"a.f2.h": "Uma frase. Três coisas resolvidas.",
"a.f2.p": "O Preenchimento inteligente transforma o que você disse em tarefas, eventos e notas, com datas e horários já preenchidos. Você confere cada campo antes de qualquer coisa ser criada.",
"a.f3.h": "Pergunte o que quiser.",
"a.f3.p": "As respostas vêm só do que você salvou, com as fontes listadas para você abrir e conferir.",
"a.f4.h": "O seu dia e a sua semana.",
"a.f4.p": "O que vence e o que vem a seguir numa tela tranquila, com o seu Calendário da Apple ao lado das suas tarefas, lembretes e um resumo da manhã opcional.",
"a.f5.h": "Nada se perde.",
"a.f5.p": "As suas palavras originais ficam ao lado de tudo o que foi criado a partir delas. Qualquer organização pode ser desfeita, e você pode exportar toda a sua biblioteca quando quiser.",
"a.f6.h": "Privado por padrão.",
"a.f6.p": 'IA no aparelho em primeiro lugar, sem anúncios e sem rastreamento. A sincronização e a IA na nuvem esperam, cada uma, pelo seu sim, e qualquer captura pode ficar só neste iPhone. <a href="{BASE}{L}/privacy/">Como isso funciona.</a>',

"a.price.h": "Planos",
"a.price.b": """
<p>O Second Brain é grátis para usar, e salvar nunca é bloqueado. O Light e o Pro removem os limites mensais e acrescentam sincronização e IA na nuvem.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Grátis</div><div class="price">R$ 0</div><ul><li>Captura digitada, tarefas, projetos, busca, lembretes e exportação ilimitados</li><li>20 capturas por voz, 40 Preenchimentos inteligentes e 5 perguntas por mês</li><li>IA no aparelho nos aparelhos compatíveis</li></ul></div>
  <div class="tier"><div class="lbl">Light</div><div class="price">Mensal</div><ul><li>Captura por voz, Preenchimento inteligente e perguntas ilimitados</li><li>Modo rápido</li><li>Sincronização privada com o iCloud</li><li>300 capturas com IA na nuvem e 100 respostas na nuvem por mês</li></ul></div>
  <div class="tier pro"><div class="lbl">Pro</div><div class="price">Mensal · Anual</div><ul><li>Tudo do Light</li><li>700 capturas com IA na nuvem e 250 respostas na nuvem por mês</li><li>Um resumo diário na nuvem</li><li>Importação do texto de páginas da web</li><li>O anual começa com 7 dias grátis</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Os preços aparecem no app e na App Store para o seu país. A cobrança é feita pela Apple. <a href="{BASE}{L}/terms/#subscriptions">Termos da assinatura.</a></p>
""",

"a.platform.h": "Feito para aparelhos Apple",
"a.platform.b": """
<ul class="rows">
  <li><span class="tile">{phone}</span><div><b>iPhone e iPad</b><span>iOS 18 ou iPadOS 18 e posteriores. IA no aparelho nos aparelhos compatíveis com a Apple Intelligence.</span></div></li>
  <li><span class="tile">{share}</span><div><b>Onde você estiver</b><span>Uma extensão de compartilhamento para salvar de qualquer app, widgets na Tela de Início, Siri e Atalhos, e busca opcional no Spotlight.</span></div></li>
  <li><span class="tile">{cloud}</span><div><b>O seu iCloud, não o nosso</b><span>A sincronização passa pelo seu próprio armazenamento privado do iCloud, então nunca guardamos uma cópia da sua biblioteca.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Oito idiomas</b><span>Inglês, alemão, espanhol, francês, japonês, coreano, português do Brasil e chinês simplificado, inclusive na captura por voz. Escolha um em {K_settings} → {K_language}.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Política de Privacidade",
"p.h1": "Os seus pensamentos continuam seus.",
"p.sub": "O Second Brain guarda a sua biblioteca no seu aparelho. A sincronização e a IA na nuvem esperam, cada uma, pelo seu sim. Esta página explica exatamente o que sai do seu aparelho, quando sai e quem recebe.",
"p.meta": "Vigente a partir de {DATE} · aplica-se ao app Second Brain para iPhone e iPad e a este site",

"p.summary.h": "Em resumo",
"p.summary.b": """
<p class="lead">O Second Brain funciona sem conta. <strong>A sua biblioteca (capturas, gravações, anexos, tarefas, notas e tudo o que é criado a partir delas) fica armazenada no seu aparelho.</strong> Sem conta, o app não nos envia absolutamente nada.</p>
<p>Três coisas mudam isso, e cada uma depende de uma escolha sua:</p>
<ul>
  <li>A <strong>sincronização com o iCloud</strong> (Light e Pro) copia a sua biblioteca para o <em>seu próprio</em> armazenamento privado do iCloud. Nós não conseguimos lê-la.</li>
  <li>A <strong>IA na nuvem (“Luna”)</strong> envia o texto necessário para uma solicitação, por meio do nosso servidor, para a OpenAI, quando a IA no aparelho não consegue ajudar ou quando você escolhe a Luna. Nada é enviado a menos que você entre na sua conta e ative essa opção.</li>
  <li><strong>Uma conta</strong> (Iniciar sessão com a Apple) permite que o nosso servidor guarde um registro pequeno: um ID de conta que é um hash unidirecional, o seu plano, as suas escolhas de consentimento e as suas contagens de uso. Nunca pedimos à Apple o seu nome ou e-mail.</li>
</ul>
<div class="callout"><span class="tile">{shield}</span><div>Sem publicidade, sem ferramentas de análise, sem rastreamento e sem SDKs de terceiros no app. Não vendemos nem compartilhamos dados pessoais, e nunca usamos o seu conteúdo para treinar modelos de IA.</div></div>
<p style="margin-top:16px">Esta política se aplica ao app Second Brain para iPhone e iPad e a este site, ambos publicados pela {COMPANY} (“nós”). A tela {K_settings} → {K_data_handled} do próprio app diz o mesmo de forma mais curta.</p>
""",

"p.collect.h": "O que coletamos",
"p.collect.b": """
<p>“Coletar”, aqui, significa dados que saem do seu aparelho e ficam guardados em algum lugar onde podemos lê-los. Dados que só chegam ao seu próprio armazenamento do iCloud não são coletados por nós.</p>
<div class="table-wrap"><table>
<tr><th>Categoria</th><th>Coletado?</th><th>O que isso significa</th></tr>
<tr><td>Informações de contato</td><td>Não</td><td>O Iniciar sessão com a Apple está configurado para não compartilhar nome nem endereço de e-mail conosco. Não há campo de e-mail no app.</td></tr>
<tr><td>Identificadores</td><td><strong>Só com uma conta</strong></td><td>Um ID de conta gerado a partir de um hash unidirecional do identificador que a Apple nos fornece, e a chave pública que o App Attest da Apple cria em cada um dos seus aparelhos. Nenhum identificador de publicidade nem ID de aparelho é usado.</td></tr>
<tr><td>Conteúdo do usuário</td><td><strong>Só com a IA na nuvem</strong></td><td>O texto necessário para uma solicitação que você faz à Luna, e o resultado dela, guardados por pouco tempo como descrito abaixo. A sua biblioteca em si fica no seu aparelho e no seu próprio iCloud.</td></tr>
<tr><td>Compras</td><td><strong>Só se você assinar</strong></td><td>A transação assinada que a Apple envia para o seu plano: produto, datas, status do teste e da renovação. Nunca vemos dados de pagamento.</td></tr>
<tr><td>Dados de uso</td><td><strong>Só com uma conta</strong></td><td>Contagens das solicitações de IA na nuvem e do tamanho delas, para aplicar a cota mensal. Sem ferramentas de análise e sem registro de como você usa o app.</td></tr>
<tr><td>Localização, contatos, saúde, navegação, histórico de busca, diagnósticos</td><td>Não</td><td>O app não pede localização nem contatos e não contém relatório de falhas nem ferramentas de análise.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Rastreamento:</strong> nenhum. Não vinculamos dados sobre você a dados de outras empresas, não exibimos anúncios e não compartilhamos nada com corretores de dados. O app nunca mostra o pedido de rastreamento da Apple porque não tem nada a pedir.</p>
""",

"p.device.h": "O que fica no seu aparelho",
"p.device.b": """
<p>O Second Brain guarda a sua biblioteca no armazenamento privado do próprio app no seu aparelho, protegido pela proteção de dados do iOS e pelo seu código:</p>
<ul>
  <li><strong>Capturas</strong>: o que você disse ou digitou, exatamente como disse, mais as correções que você fez.</li>
  <li><strong>Gravações e anexos</strong>: áudio, fotos, PDFs, arquivos e links que você adicionou, e o texto lido deles no seu aparelho.</li>
  <li><strong>O que foi criado a partir deles</strong>: tarefas, eventos, notas, ideias, projetos, histórico de revisão e histórico de desfazer.</li>
  <li><strong>Dados de busca</strong>: o índice de busca por significado, criado no seu aparelho com os modelos de linguagem da Apple.</li>
  <li><strong>Ajustes</strong>: idioma, lembretes, widgets, escolhas de IA e os calendários que você escolheu.</li>
  <li><strong>No Keychain do iOS</strong>: a sua sessão de login e a contagem mensal de capturas por voz, Preenchimentos inteligentes e perguntas grátis. A contagem guarda só números e fica neste aparelho, mesmo que o app seja reinstalado.</li>
</ul>
<p>Uma biblioteca de convidado e cada conta conectada têm armazenamentos separados no aparelho. Se você usa o Backup do iCloud ou um backup criptografado no computador, a Apple pode incluir esses dados nesse backup, na sua Conta Apple. Não temos acesso a eles.</p>
<p><strong>Widgets e Spotlight.</strong> Os widgets só mostram os títulos dos itens se você ativar {K_widgets}. Os itens salvos só aparecem no Spotlight se você ativar {K_spotlight}. Os dois ficam no seu aparelho.</p>
""",

"p.ai.h": "IA no seu aparelho, e a Luna na nuvem",
"p.ai.b": """
<h3>IA no aparelho</h3>
<p>Nos aparelhos compatíveis, o Preenchimento inteligente, a organização, as respostas e os resumos rodam no modelo da Apple que funciona no próprio aparelho. O que você escreve não sai do seu aparelho, e o uso no aparelho nunca conta para uma cota na nuvem.</p>
<h3>Luna, a nossa IA na nuvem</h3>
<p>A Luna é um modelo da <strong>OpenAI</strong> que acessamos pelo nosso próprio servidor. O seu aparelho nunca se conecta diretamente à OpenAI, e não há nenhuma chave de API no app. A Luna só roda se você tiver <strong>entrado na sua conta e ativado {K_luna}</strong>. Ela é usada quando a IA no aparelho não está disponível ou não consegue concluir uma solicitação, ou em primeiro lugar se você tem o Light ou o Pro e escolheu a Luna como seu mecanismo. Desativar essa opção interrompe novas solicitações de IA na nuvem na hora.</p>
<p>Em cada solicitação, só é enviado o texto necessário para ela:</p>
<ul>
  <li><strong>Organização e Preenchimento inteligente</strong>: o texto da captura que está sendo organizada, incluindo o texto lido no seu aparelho de uma foto ou PDF anexado, o seu fuso horário e idioma, e os nomes e resumos curtos de até 30 dos seus projetos.</li>
  <li><strong>Pergunte ao seu Cérebro</strong>: a sua pergunta e trechos curtos de até 12 itens salvos que o seu aparelho escolheu como relevantes.</li>
  <li><strong>Organizar notas</strong> (Light e Pro): o texto da nota que você pediu para organizar.</li>
  <li><strong>Resumo diário</strong> (Pro): contagens do que vence e trechos curtos de até 10 dos seus itens daquele dia.</li>
</ul>
<p><strong>Nunca enviados:</strong> o áudio, as imagens ou os arquivos em si; capturas marcadas com {K_device_only}; os eventos do seu Calendário da Apple; o seu nome ou e-mail (nós não os temos); qualquer identificador que possa dizer à OpenAI quem você é.</p>
<h3>Por quanto tempo é guardado</h3>
<p>O nosso servidor guarda um resultado por <strong>até 24 horas</strong>, para que uma solicitação interrompida possa ser concluída sem rodar duas vezes nem descontar duas vezes da sua cota. Depois disso, o texto é removido, e um comprovante sem conteúdo (um hash unidirecional da solicitação, os IDs dos itens usados e o horário) é guardado por até um ano para a contabilização da cota. Apagar um item permanentemente também remove todos os resultados criados a partir dele, e apagar a sua conta remove todos eles.</p>
<p>Pedimos à OpenAI que não armazene as respostas. Pelos termos da API dela, a OpenAI não usa esses dados para treinar os seus modelos. Ela pode guardar entradas e saídas por um tempo limitado para monitorar abusos, como descrito nas <a href="https://openai.com/enterprise-privacy/">políticas de dados da API</a> dela.</p>
<p>Sugestões e respostas geradas por IA podem estar erradas. É por isso que cada campo do Preenchimento inteligente pode ser conferido antes de ser salvo, e cada resposta lista as suas fontes.</p>
""",

"p.sync.h": "Sincronização com o iCloud",
"p.sync.b": """
<p>Com o Light ou o Pro, você pode ativar {K_sync}. A sua biblioteca, incluindo capturas, itens, projetos, correções, histórico e anexos, passa a ser armazenada em um <strong>banco de dados privado do CloudKit na sua própria conta do iCloud</strong>, para que os seus aparelhos fiquem em sincronia. A Apple a armazena de acordo com a própria <a href="https://www.apple.com/legal/privacy/">política de privacidade</a>. Nós, o desenvolvedor, não conseguimos ler os seus dados privados do iCloud, e o nosso servidor nunca recebe uma cópia da sua biblioteca.</p>
<p>Capturas marcadas com {K_device_only} nunca são sincronizadas. Quando a sincronização está ativada, o iOS pode entregar notificações silenciosas do serviço de push da Apple para avisar o app de que algo mudou. Nenhum token de push é enviado para nós.</p>
""",

"p.account.h": "A sua conta e o nosso servidor",
"p.account.b": """
<p>A conta é opcional. Quando você usa o Iniciar sessão com a Apple, <strong>não pedimos nome nem e-mail</strong>. O nosso servidor, que roda na <strong>Cloudflare</strong>, guarda:</p>
<ul>
  <li><strong>Um ID de conta</strong>: um hash unidirecional do identificador que a Apple nos fornece. O identificador original da Apple não é armazenado.</li>
  <li><strong>Dados de login</strong>: sessões, armazenadas só como hashes e que expiram após 30 dias, e o token de login da Apple, criptografado e usado só para revogá-lo quando você apaga a sua conta.</li>
  <li><strong>Verificação do aparelho</strong>: a chave pública que o App Attest da Apple cria em cada aparelho em que você entra (até 20), para que o servidor saiba que está falando com uma cópia legítima do Second Brain.</li>
  <li><strong>As suas escolhas e o seu plano</strong>: se a sincronização e a IA na nuvem estão ativadas, o seu plano e as datas de renovação dele, e as transações que a Apple envia para confirmá-lo.</li>
  <li><strong>Contagens de uso</strong>: quanto da cota na nuvem deste mês você já usou.</li>
  <li><strong>Resultados da IA na nuvem</strong>, guardados por pouco tempo como descrito acima.</li>
</ul>
<p>Para proteger o serviço contra abusos, o servidor guarda por pouco tempo um hash unidirecional do seu endereço IP combinado com o minuto atual. Ele é apagado em questão de minutos. Não mantemos registros de solicitações, e o nosso servidor nunca recebe a sua biblioteca.</p>
<p><strong>Importação de páginas</strong> (Pro): quando você pede para importar o texto de uma página da web, o nosso próprio servidor busca essa página pública e devolve o texto legível dela ao seu aparelho. O endereço e o texto da página não são armazenados e não são enviados à Luna.</p>
""",

"p.voice.h": "Voz, fala e gravações",
"p.voice.b": """
<p>A captura por voz usa o microfone só enquanto você está gravando. A fala é transcrita <strong>no seu aparelho</strong> com o reconhecimento de fala da Apple. A sua gravação não é enviada para a Apple nem para nós para transcrição, embora o primeiro uso de um idioma baixe os arquivos de fala da Apple.</p>
<p>As gravações ficam na sua biblioteca. Depois que uma transcrição é concluída, o áudio é apagado <strong>7 dias</strong> depois de salvo, a menos que você toque em {K_keep_recording}. Uma gravação cuja transcrição falhou fica guardada até você apagá-la. As transcrições continuam depois que o áudio é apagado.</p>
""",

"p.permissions.h": "Permissões",
"p.permissions.b": """
<div class="table-wrap"><table>
<tr><th>Permissão</th><th>Usada para</th></tr>
<tr><td>Microfone, Reconhecimento de Fala</td><td>Captura por voz e transcrição no aparelho.</td></tr>
<tr><td>Câmera, Fotos</td><td>Tirar ou escolher uma foto para anexar. Só as fotos que você escolhe são lidas.</td></tr>
<tr><td>Calendários</td><td>Pedida só se você tocar em {K_calendars}. Os calendários que você escolhe são lidos no seu aparelho para aparecer ao lado das suas tarefas, e nunca são enviados. Um novo evento só é adicionado ao Calendário da Apple pelo próprio editor da Apple, depois que você o confirma.</td></tr>
<tr><td>Notificações</td><td>Lembretes, o resumo da manhã e um lembrete antes do fim de um teste grátis. Tudo é agendado no seu aparelho.</td></tr>
</table></div>
<p style="margin-top:14px">Você pode mudar qualquer uma delas em {K_settings} do iOS → Second Brain. O app nunca pede a sua localização nem os seus contatos.</p>
""",

"p.purchases.h": "Compras",
"p.purchases.b": """
<p>O Light e o Pro são vendidos pela App Store da Apple. O pagamento acontece entre você e a Apple, de acordo com a <a href="https://www.apple.com/legal/privacy/">política de privacidade da Apple</a>, e nunca vemos os seus dados de pagamento. Você pode comprar um plano sem conta: o seu iPhone verifica a transação que a Apple assina, e o nosso servidor não guarda nada sobre a compra. Se você entrar na conta, o nosso servidor verifica essa transação e a armazena com a sua conta, para que o plano acompanhe você nos seus outros aparelhos. Uma compra feita sem conta fica vinculada à primeira conta que a enviar. O nosso servidor também recebe os avisos da Apple sobre renovações, reembolsos e cancelamentos e só os aplica a compras vinculadas a uma conta, para que o seu plano fique sempre correto.</p>
""",

"p.third.h": "Prestadores de serviços",
"p.third.b": """
<p>O Second Brain <strong>não contém SDKs de terceiros</strong>: nada de ferramentas de análise, publicidade ou relatório de falhas. Estas empresas tratam dados para nós, cada uma só para a finalidade indicada:</p>
<ul>
  <li><strong>Apple</strong>: Iniciar sessão com a Apple, App Attest, a App Store e as compras, a sincronização com o iCloud na sua própria conta, a entrega de push para a sincronização e os modelos de IA e de fala no aparelho.</li>
  <li><strong>Cloudflare</strong>: hospeda o nosso servidor e o banco de dados dele e encaminha as solicitações até ele.</li>
  <li><strong>OpenAI</strong>: roda a Luna para as solicitações de IA na nuvem que você permite, como descrito acima.</li>
</ul>
<p>Não vendemos nem alugamos dados pessoais, e não compartilhamos nada com anunciantes ou corretores de dados. Podemos divulgar informações se a lei exigir. Como guardamos tão pouco, há pouco que poderíamos divulgar.</p>
""",

"p.retention.h": "Por quanto tempo guardamos",
"p.retention.b": """
<div class="table-wrap"><table>
<tr><th>Dados</th><th>Prazo</th></tr>
<tr><td>A sua biblioteca no seu aparelho</td><td>Até você apagá-la. Os itens que você apaga ficam em {K_recently_deleted} por 30 dias.</td></tr>
<tr><td>Gravações de voz</td><td>7 dias após uma transcrição concluída, a menos que você as mantenha. Até você apagá-las, se a transcrição falhou.</td></tr>
<tr><td>A sua cópia no iCloud</td><td>Até você apagá-la ou apagar a sua conta. Ela é armazenada pela Apple no seu iCloud.</td></tr>
<tr><td>Resultado da IA na nuvem</td><td>Até 24 horas. Um comprovante sem conteúdo é guardado por até 1 ano.</td></tr>
<tr><td>Sessões de login</td><td>30 dias desde a última renovação</td></tr>
<tr><td>Conta, plano e contagens de uso</td><td>Enquanto a sua conta existir</td></tr>
<tr><td>Endereço IP em hash para proteção contra abusos</td><td>Alguns minutos</td></tr>
<tr><td>Backups do servidor</td><td>Os backups do banco de dados do nosso provedor de hospedagem podem conter dados apagados por até 30 dias, até expirarem.</td></tr>
</table></div>
""",

"p.delete.h": "Exportação e exclusão",
"p.delete.b": """
<p>Tudo está nas suas mãos, dentro do app:</p>
<ul>
  <li><strong>Exportar</strong>: em {EXPORT}, você cria um ZIP com toda a sua biblioteca, os seus arquivos originais e uma lista de tudo o que não pôde ser incluído.</li>
  <li><strong>Apagar deste aparelho</strong>: em {DELETE_LOCAL}, você remove a biblioteca deste aparelho. Isso não apaga a sua conta nem a cópia dela no iCloud.</li>
  <li><strong>Apagar a sua conta</strong>: em {DELETE_ACCOUNT}, você apaga a sua cópia no iCloud, tudo o que o nosso servidor guarda sobre a conta e a biblioteca da conta neste aparelho, e o acesso do Second Brain pelo Iniciar sessão com a Apple é revogado.</li>
</ul>
<p>Depois que uma conta é apagada, o nosso servidor guarda só um marcador sem conteúdo: o ID da conta em hash marcado como apagado, as contagens de uso dela e hashes unidirecionais dos identificadores de compra e de aparelho dela. Esse marcador permite que uma exclusão interrompida seja concluída e impede que uma compra ou a amostra grátis na nuvem seja usada duas vezes. Ele não contém conteúdo, nome nem e-mail. As instruções passo a passo estão na página <a href="{BASE}{L}/delete-data/">Seus dados</a>.</p>
""",

"p.rights.h": "Os seus direitos",
"p.rights.b": """
<p>Dependendo de onde você mora, inclusive pelo GDPR, pelo UK GDPR e pela CCPA/CPRA da Califórnia, você tem o direito de acessar, corrigir, exportar e apagar os dados pessoais que mantemos sobre você, de restringir o tratamento deles e de se opor a ele, de retirar o consentimento a qualquer momento e de apresentar uma reclamação à sua autoridade de proteção de dados. A maioria desses direitos está integrada ao app: exportar, apagar e as opções de sincronização e de IA na nuvem. Para qualquer outra coisa, escreva para {MAIL} e responderemos em até 30 dias.</p>
<p>Onde o GDPR se aplica, nos baseamos em: <strong>contrato</strong>, para oferecer os recursos que você usa e o plano que você comprou; <strong>consentimento</strong>, para a sincronização com o iCloud e a IA na nuvem, que você pode retirar desativando essas opções; <strong>interesses legítimos</strong>, para manter o serviço seguro e evitar abusos (App Attest e proteção contra abusos); e <strong>obrigação legal</strong>, para os registros de compras.</p>
""",

"p.children.h": "Crianças",
"p.children.b": """
<p>O Second Brain não é direcionado a crianças menores de 13 anos, ou abaixo da idade de consentimento digital no lugar onde você mora. Não coletamos intencionalmente dados pessoais de crianças. Se você acredita que uma criança criou uma conta, escreva para {MAIL} e vamos ajudar a apagá-la.</p>
""",

"p.transfers.h": "Onde os dados são tratados",
"p.transfers.b": """
<p>A Cloudflare roda o nosso servidor na rede global dela, e a OpenAI e a Apple podem tratar dados nos Estados Unidos e em outros países. Quando a lei exige, essas transferências são cobertas pelos termos de tratamento de dados dos prestadores, incluindo cláusulas contratuais padrão. Os dados armazenados no seu aparelho ficam onde o seu aparelho está.</p>
""",

"p.changes.h": "Alterações nesta política",
"p.changes.b": """
<p>Se o app mudar o que faz com os dados, atualizaremos esta política e a data no topo. Mencionaremos as alterações relevantes nas notas da versão do app e, quando a lei exigir, pediremos o seu consentimento novamente. Nunca começaremos a enviar o seu conteúdo para um lugar novo sem uma nova escolha sua.</p>
""",

"p.contact.h": "Contato",
"p.contact.b": """
<p>A {COMPANY}, que publica o Second Brain, é a controladora dos dados pessoais descritos aqui. Para dúvidas ou solicitações sobre privacidade, escreva para {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Termos de Uso",
"t.h1": "O acordo, em palavras simples.",
"t.sub": "O que o Second Brain faz, o que a IA dele pode e não pode prometer, como o seu conteúdo é tratado e como o Light e o Pro são cobrados.",
"t.meta": "Vigente a partir de {DATE} · Second Brain, da {COMPANY}",

"t.acceptance.h": "1. Aceitação dos Termos",
"t.acceptance.b": """
<p>Estes Termos de Uso (“Termos”) são um acordo entre você e a {COMPANY} (“nós”), que publica o app Second Brain para iPhone e iPad (“Second Brain” ou “o app”) e os serviços online relacionados a ele. Ao instalar ou usar o Second Brain, você aceita estes Termos e a nossa <a href="{BASE}{L}/privacy/">Política de Privacidade</a>. Se você não concordar, não use o app.</p>
""",
"t.who.h": "2. Quem pode usar o Second Brain",
"t.who.b": """
<p>Você precisa ter pelo menos 13 anos, ou a idade de consentimento digital no lugar onde mora, para usar o Second Brain. Se você ainda não tiver atingido a maioridade no lugar onde mora, precisa da permissão de um dos pais ou de um responsável para comprar uma assinatura.</p>
""",
"t.what.h": "3. O que o Second Brain é, e o que não é",
"t.what.b": """
<p>O Second Brain é uma ferramenta pessoal para capturar pensamentos por voz ou texto e organizá-los em tarefas, eventos, notas e ideias, com lembretes, busca e respostas tiradas do que você salvou.</p>
<p>O Second Brain <strong>não</strong> é um serviço médico, jurídico, financeiro ou de outra natureza profissional, e nada do que ele produz é aconselhamento profissional. Não dependa dele como a única forma de lembrar algo crítico, como um medicamento, um prazo legal ou uma questão de segurança. Os lembretes dependem do iOS, dos seus ajustes e do seu aparelho, e podem não chegar. Em uma emergência, entre em contato com os serviços de emergência locais.</p>
""",
"t.account.h": "4. A sua conta",
"t.account.b": """
<p>A conta é opcional e usa o Iniciar sessão com a Apple. Você é responsável pela sua Conta Apple, pelo seu aparelho e pelo código dele, e pela atividade na sua conta. Cada conta é para uma pessoa. Você pode sair a qualquer momento e pode apagar a sua conta no app, como descrito na página <a href="{BASE}{L}/delete-data/">Seus dados</a>.</p>
""",
"t.content.h": "5. O seu conteúdo",
"t.content.b": """
<p>Tudo o que você captura, anexa ou escreve no Second Brain (“o seu conteúdo”) continua sendo seu. Não reivindicamos nenhuma propriedade sobre ele. Você nos dá apenas a permissão limitada necessária para tratar o seu conteúdo a fim de oferecer os recursos que você escolhe: por exemplo, enviar texto à Luna quando você ativou a IA na nuvem, ou buscar uma página da web que você pediu para importar. Não usamos o seu conteúdo para treinar modelos de IA e não o vendemos.</p>
<p>Você é responsável pelo seu conteúdo e por ter o direito de capturá-lo, importá-lo e armazená-lo, incluindo qualquer coisa sobre outras pessoas. A sua biblioteca fica no seu aparelho e, se você quiser, no seu próprio iCloud. Guarde as suas próprias exportações. Não mantemos uma cópia da sua biblioteca e não podemos restaurá-la se as cópias no seu aparelho e no iCloud forem perdidas.</p>
""",
"t.ai.h": "6. Recursos de IA",
"t.ai.b": """
<p>O Second Brain usa inteligência artificial para sugerir como organizar o que você captura, preencher detalhes como datas e horários, responder perguntas a partir da sua biblioteca e escrever resumos. Ele usa o modelo da Apple no aparelho, quando disponível, e, se você permitir, a <strong>Luna</strong>, um modelo na nuvem fornecido pela OpenAI por meio do nosso servidor.</p>
<p><strong>O resultado da IA pode estar errado, incompleto ou desatualizado.</strong> Ela pode interpretar errado uma data, deixar passar uma tarefa ou relatar de forma incorreta o que uma fonte diz. Confira as sugestões antes de criá-las e confira as fontes de uma resposta antes de confiar nela. Se você ativar o {K_quick}, os itens são criados sem essa revisão, por sua própria escolha. Tudo de que o Preenchimento inteligente não tiver certeza vai para {K_needs_review}, e a opção {K_undo} continua disponível.</p>
<p>Você concorda em não usar os recursos de IA para produzir conteúdo ilegal, nocivo ou que viole direitos, nem para tentar extrair os modelos subjacentes, as instruções deles ou as chaves do nosso serviço. Podemos mudar os modelos que usamos, ajustar limites ou pausar um recurso para proteger o serviço. Quando fizermos isso, o resto do app continua funcionando e o seu conteúdo salvo não é afetado.</p>
""",
"t.cloud.h": "7. Recursos na nuvem e cotas",
"t.cloud.b": """
<p>A <strong>sincronização</strong> usa a sua própria conta do iCloud e depende do serviço da Apple, do seu armazenamento do iCloud e da sua conexão. A <strong>IA na nuvem</strong> é limitada pela cota mensal do seu plano: o Light inclui 300 capturas com IA na nuvem e 100 respostas na nuvem por mês, o Pro inclui 700 e 250, e uma conta grátis conectada recebe uma amostra única. As cotas são renovadas a cada mês do calendário, e o que não for usado não é acumulado. Para manter o serviço justo, também há um limite para a quantidade total de texto tratada a cada mês. A <strong>importação de páginas</strong> (Pro) só busca páginas públicas, e você é responsável por ter o direito de usar o que importar.</p>
<p>Trabalhamos para manter os recursos na nuvem disponíveis, mas não garantimos que funcionem sem interrupções. Os recursos no aparelho continuam funcionando sem eles.</p>
""",
"t.subscriptions.h": "8. Assinaturas e cobrança",
"t.subscriptions.b": """
<p>O Second Brain é grátis para baixar e usar, com limites mensais de captura por voz, Preenchimento inteligente e Pergunte ao seu Cérebro em cada aparelho. Salvar o que você captura nunca é bloqueado. Os planos pagos são assinaturas com renovação automática vendidas pela Apple, pelo preço mostrado no app e na App Store para o seu país:</p>
<ul>
  <li><strong>Light mensal</strong>: cobrado mensalmente.</li>
  <li><strong>Pro mensal</strong>: cobrado mensalmente.</li>
  <li><strong>Pro anual</strong>: cobrado anualmente, começando com um <strong>teste grátis de 7 dias</strong> para novos assinantes elegíveis.</li>
</ul>
<p>Você pode assinar sem uma conta do Second Brain. Sem conta, os recursos do plano no aparelho funcionam nos iPhones que usam a Conta Apple com que você assinou. Iniciar sessão com a Apple vincula o plano à sua conta e adiciona os recursos na nuvem. O pagamento é cobrado na sua Conta Apple quando você confirma a compra. Um teste grátis se converte em uma assinatura paga, a menos que você cancele pelo menos 24 horas antes do fim dele. As assinaturas são renovadas automaticamente pelo mesmo preço e período, a menos que a renovação automática seja desativada pelo menos 24 horas antes do fim do período atual. A renovação é cobrada na sua Conta Apple nas 24 horas anteriores ao fim desse período. Você pode gerenciar ou cancelar uma assinatura nos <a href="https://apps.apple.com/account/subscriptions">ajustes de assinatura da App Store</a> ou em {K_manage} no app. O cancelamento passa a valer no fim do período atual. Os reembolsos são tratados pela Apple de acordo com as políticas dela. Use {K_restore} para recuperar um plano em outro aparelho. As assinaturas não são compartilhadas pelo Compartilhamento Familiar.</p>
<p><strong>Se uma assinatura terminar</strong>, nada do que você salvou é removido. Leitura, edição, busca, exportação e exclusão continuam funcionando, os limites mensais grátis voltam a valer, e a sincronização e as cotas na nuvem param. Apagar o app ou a sua conta não cancela uma assinatura. Cancele-a com a Apple. Podemos mudar os preços ou os recursos de um plano. A Apple vai avisar você antes que um aumento de preço seja aplicado, como as regras dela exigem.</p>
""",
"t.licence.h": "9. Licença e propriedade intelectual",
"t.licence.b": """
<p>Concedemos a você uma licença pessoal, não exclusiva, intransferível e revogável para usar o Second Brain em aparelhos Apple que sejam seus ou que você controle, de acordo com estes Termos e as Regras de Uso da App Store. O Second Brain, o nome, o design, as ilustrações (incluindo o personagem do cérebro), os textos e o código dele pertencem à {COMPANY} e são protegidos por lei. Você não pode copiar, modificar, distribuir, vender, alugar, fazer engenharia reversa nem criar obras derivadas do app, exceto quando a lei permitir expressamente.</p>
""",
"t.use.h": "10. Uso aceitável",
"t.use.b": """
<p>Você concorda em não: usar o Second Brain de forma ilegal ou para armazenar conteúdo que você não tem o direito de manter; interferir nos nossos servidores, sobrecarregá-los ou sondá-los; burlar as cotas, o App Attest ou o sistema de compras da App Store; acessar a conta de outra pessoa; nem usar o serviço para assediar, prejudicar ou gravar pessoas sem o consentimento que a lei exige.</p>
""",
"t.termination.h": "11. Encerramento",
"t.termination.b": """
<p>Você pode parar de usar o Second Brain a qualquer momento e pode apagar a sua conta no app. Podemos suspender ou encerrar o acesso aos recursos na nuvem se você violar estes Termos de forma grave ou repetida, ou se a lei exigir. Sempre que possível, avisaremos você antes. O seu conteúdo no seu aparelho continua sendo seu para exportar. As seções 5, 6, 9, 12, 13 e 15 continuam valendo após o encerramento.</p>
""",
"t.warranty.h": "12. Garantias e responsabilidade",
"t.warranty.b": """
<p>O Second Brain é fornecido “no estado em que se encontra” e “conforme disponível”, sem garantias de qualquer tipo, expressas ou implícitas. Não garantimos que o resultado da IA seja preciso, que os lembretes sempre cheguem, que a sincronização ou os recursos na nuvem funcionem sem interrupções nem que o app esteja livre de erros. Na máxima extensão permitida por lei, a {COMPANY} não se responsabiliza por danos indiretos, incidentais, especiais, consequenciais ou punitivos, nem por perda de dados, lucros ou oportunidades, decorrentes do seu uso ou da impossibilidade de usar o app, incluindo qualquer coisa produzida por um recurso de IA ou um lembrete que não chegou. Quando a responsabilidade não puder ser excluída, ela fica limitada ao valor que você pagou pelo Second Brain nos doze meses anteriores à reclamação. Nada nestes Termos limita direitos que você tem como consumidor e que não podem ser renunciados.</p>
""",
"t.apple.h": "13. Apple",
"t.apple.b": """
<p>O Second Brain é distribuído pela App Store da Apple. Estes Termos são firmados entre você e a {COMPANY}, e não com a Apple. A Apple não tem nenhuma obrigação de oferecer manutenção ou suporte para o app e não é responsável por tratar qualquer reclamação relacionada a ele, incluindo reclamações de responsabilidade pelo produto, de conformidade legal ou de propriedade intelectual. Se o app não estiver em conformidade com qualquer garantia aplicável, você pode notificar a Apple, e a Apple reembolsará o preço de compra, se houver. Na máxima extensão permitida por lei, a Apple não tem nenhuma outra obrigação de garantia em relação ao app. A Apple e as suas subsidiárias são terceiras beneficiárias destes Termos e podem exigir o cumprimento deles contra você. Quando estes Termos forem omissos, aplica-se o <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de Licença de Usuário Final de Aplicativo Licenciado</a> da Apple. Você confirma que não está em um país sujeito a embargo do governo dos EUA nem em uma lista dos EUA de partes proibidas ou restritas, e deve cumprir quaisquer termos de terceiros aplicáveis ao usar o app.</p>
""",
"t.changes.h": "14. Alterações nestes Termos",
"t.changes.b": """
<p>Podemos atualizar estes Termos à medida que o Second Brain muda. A data no topo vai mudar quando fizermos isso, e mencionaremos as alterações relevantes nas notas da versão do app. Continuar usando o app depois de uma atualização significa que você aceita os Termos revisados. Se não aceitar, você pode parar de usar o app e apagar a sua conta.</p>
""",
"t.law.h": "15. Lei aplicável",
"t.law.b": """
<p>Estes Termos são regidos pelas leis do Paquistão, onde a {COMPANY} opera, sem considerar as regras de conflito de leis. Se a lei do seu país de residência der a você proteções que não podem ser afastadas por contrato, essas proteções continuam valendo.</p>
""",
"t.contact.h": "16. Contato",
"t.contact.b": """
<p>Dúvidas sobre estes Termos: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Seus dados",
"d.h1": "Exporte ou apague os seus dados",
"d.sub": "A sua biblioteca está no seu aparelho e, se você escolheu sincronizar, no seu próprio iCloud. Veja como fazer uma cópia, apagá-la de um aparelho ou apagar a sua conta e tudo o que ela guarda.",
"d.meta": 'Veja também a <a href="{BASE}{L}/privacy/">Política de Privacidade</a>',

"d.where.h": "O que fica armazenado onde",
"d.where.b": """
<div class="table-wrap"><table>
<tr><th>Dados</th><th>Onde ficam</th><th>Como remover</th></tr>
<tr><td>Capturas, gravações, anexos, tarefas, notas, projetos, histórico</td><td>O seu aparelho</td><td>{DELETE_LOCAL}, ou apague a sua conta (abaixo)</td></tr>
<tr><td>A mesma biblioteca, se você ativou a sincronização</td><td>Um banco de dados privado no seu próprio iCloud</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>ID da conta, plano, escolhas de consentimento, contagens de uso, chaves dos aparelhos</td><td>O nosso servidor (Cloudflare)</td><td>{DELETE_ACCOUNT}</td></tr>
<tr><td>Resultados da IA na nuvem</td><td>O nosso servidor, por até 24 horas</td><td>Removidos sozinhos, quando você apaga o item permanentemente ou quando apaga a sua conta</td></tr>
<tr><td>Contagem mensal de uso grátis</td><td>O Keychain do iOS neste aparelho (só números)</td><td>É renovada todo mês. O iOS pode mantê-la depois que o app é apagado</td></tr>
<tr><td>Assinatura</td><td>A sua Conta Apple</td><td>Cancele com a Apple (abaixo)</td></tr>
</table></div>
""",
"d.export.h": "Faça uma cópia antes",
"d.export.b": """
<ol class="steps">
  <li><div>Abra o Second Brain e vá para {K_settings}.</div></li>
  <li><div>Toque em {K_export} e depois em {K_share_export}.</div></li>
  <li><div>Salve o ZIP no app Arquivos ou envie para onde quiser. Ele contém a sua biblioteca (em JSON, Markdown e um CSV de tarefas), os seus arquivos originais e uma lista de tudo o que não pôde ser incluído.</div></li>
</ol>
""",
"d.local.h": "Apagar deste aparelho",
"d.local.b": """
<p>Para apagar um item, apague-o e depois remova-o em {K_settings} → {K_recently_deleted} com {K_delete_permanently}. Caso contrário, ele é removido automaticamente após 30 dias.</p>
<p>Para apagar toda a biblioteca deste aparelho, use {DELETE_LOCAL}. Isso <strong>não</strong> apaga a sua conta, a cópia dela no iCloud nem uma biblioteca de convidado separada. Apagar o app também remove os dados dele do aparelho.</p>
""",
"d.account.h": "Apagar a sua conta",
"d.account.b": """
<ol class="steps">
  <li><div>Abra {K_settings} → {K_cloud_choices}.</div></li>
  <li><div>Toque em {K_delete_account} e confirme.</div></li>
  <li><div>O Second Brain apaga a cópia da conta no iCloud, tudo o que o nosso servidor guarda sobre a conta (sessões, plano, escolhas, contagens de uso, chaves dos aparelhos e resultados de IA) e a biblioteca da conta neste aparelho. Ele também revoga o próprio acesso pelo Iniciar sessão com a Apple. A sua biblioteca de convidado, que é separada, continua no aparelho.</div></li>
</ol>
<div class="callout warm"><span class="tile">{info}</span><div>Se o seu login tiver expirado, o app pede que você entre de novo com a mesma Conta Apple para concluir. Se você não tiver mais o aparelho, instale o Second Brain em qualquer iPhone ou iPad, entre com a mesma Conta Apple e apague a conta por lá.</div></div>
<p style="margin-top:16px">Depois disso, o nosso servidor guarda só um marcador sem conteúdo: o ID da conta em hash marcado como apagado, as contagens de uso dela e hashes unidirecionais dos identificadores de compra e de aparelho dela. Isso permite que uma exclusão interrompida seja concluída e impede que uma compra ou a amostra grátis seja usada duas vezes. Os backups do banco de dados mantidos pelo nosso provedor de hospedagem expiram em até 30 dias.</p>
""",
"d.subscription.h": "A sua assinatura",
"d.subscription.b": """
<p>Apagar os seus dados, a sua conta ou o app <strong>não</strong> cancela uma assinatura. Ela pertence à sua Conta Apple. Cancele-a nos <a href="https://apps.apple.com/account/subscriptions">ajustes de assinatura da App Store</a>, e ela continua ativa até o fim do período atual. Os reembolsos são tratados pelo <a href="https://support.apple.com/billing">Suporte da Apple</a>.</p>
""",
"d.email.h": "Fale com a gente",
"d.email.b": """
<p>Se você não conseguir usar o app, ou tiver qualquer dúvida sobre os seus dados, escreva para {MAIL}. Responderemos em até 30 dias. Não guardamos nome nem e-mail da sua conta, então vamos trabalhar com você para encontrá-la. O caminho mais rápido costuma ser entrar em qualquer aparelho e apagar por lá. Não nos envie as suas capturas ou gravações. Não precisamos delas para ajudar.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Não encontramos essa página.",
"nf.sub": "Até um segundo cérebro esquece um link de vez em quando.",
"nf.cta": "Voltar ao Suporte",
"nf.b": 'Essa página não está aqui. Tente o <a href="{BASE}/">Suporte</a>, a <a href="{BASE}/privacy/">Política de Privacidade</a> ou os <a href="{BASE}/terms/">Termos de Uso</a>.',

}
