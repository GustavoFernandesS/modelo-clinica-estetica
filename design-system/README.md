# Lívia Andrade

> Modelo de demonstração da Codetrax. A marca "Clínica Lívia Andrade" e as pessoas citadas são fictícias.

Design system da landing page e do site da **Clínica Lívia Andrade Estética Avançada** (Belo Horizonte, Savassi, desde 2014), referência em saúde íntima, fisioterapia pélvica e estética avançada.

O objetivo de cada tela é um só: fazer a paciente **tirar todas as dúvidas, confiar e agendar a avaliação**. A linguagem visual vem, peça por peça, da landing de referência (a clínica Lumina): editorial, leve, muita foto, títulos finos e enormes, botões em pílula com seta ↗. O tom é o da Dra. Lívia: **sem tabu, mas com acolhimento**.

## A referência, peça por peça

| Na referência | Na Lívia Andrade |
| --- | --- |
| Hero: foto escura numa moldura arredondada, título enorme e **leve** em 2 linhas, a 2ª em amarelo | `display` 76px peso 300: "Saúde íntima / **sem tabu**", 2ª linha em `rosa-claro` |
| Parágrafo curto alinhado **à direita** no hero | `.cr-hero-aside` |
| Link "Check Treatment Eligibility ↗" com sublinhado longo | `.cr-line-link` ("Ver tratamentos ↗") |
| Menu: logo em caixa alta + links dentro de **uma pílula contornada** + "Book Consultation" pastel | `.cr-nav`: mesmo arranjo, CTA "Agendar" em `blush` |
| Título central com palavras alternando **preto e cinza** | `.cr-manifesto` com `.cr-soft` (`ink-soft`) |
| Botão pílula escuro pequeno com ↗ solto | `.cr-btn-dark.cr-btn-sm` em `grafite` |
| Frase à esquerda + botão à direita | `.cr-statement-row` |
| Cards de tratamento com foto, número (01, 02, 03), título amarelo e "45 minutes / 5 ml" | `.cr-pcard`: título `rosa-claro`, dado em destaque ("2 min · por aplicação") e "a partir de" |
| Grade de 4 benefícios com linhas verticais e ícone em círculo | `.cr-features` |
| Roda de 4 etapas com quadrante amarelo e miolo preto | `ProcessWheel` "Como funciona": quadrante `blush`, miolo `grafite` |
| CTA com foto + selos claros em pílula | Chips de prova sobre a foto: "★ 4,7 no Google", "14 anos de clínica" |
| "Common Questions" com hairlines, + / − e foto ao lado | `FAQ` |
| Rodapé escuro com frase gigante, 2ª linha amarela, colunas e quadradinhos amarelos | `Footer`: "Seu corpo merece cuidado, **não vergonha.**", quadradinhos `rosa` |
| Nada de sombra, nada de negrito pesado | Mantido |

## O que é próprio da clínica (o toque novo)

1. **Paleta grafite + rosas** no lugar de preto + amarelo, com a mesma lógica de uso (pastel para botões sobre foto, tom médio para destaques em texto), ligada à flor rosa do logo.
2. **"Agendar avaliação" em rosa #F60069**: a única ação quente da página, que abre o WhatsApp com mensagem pronta citando o tratamento.
3. **Prova antes da venda:** chips de nota no Google, anos de clínica e parceria com ginecologista já no hero.
4. **Inputs de linha** (a referência não mostra formulário): derivados do link sublinhado, com consentimento LGPD.
5. **Usabilidade:** botões de 36–44px (na referência ~32px), corpo em 15px (lá ~13px), botão fixo de agendamento no celular, caixa de frase em português.

## Princípios de usabilidade

1. **Confiança antes da venda.** Toda tela mostra pelo menos uma prova: nota no Google (4,7 com 126 avaliações), 14 anos de clínica, parceria com ginecologista (CRM), antes e depois real ou depoimento. Assunto íntimo pede segurança.
2. **Uma ação principal, sempre à vista.** "Agendar avaliação" aparece no menu (pastel), no hero, no fim de cada página de tratamento (rosa) e num botão fixo no celular. A secundária ("Ver tratamentos", "Consulta online grátis") vai em `grafite`; a terciária ("Como chegar") é link de linha.
3. **Responder antes de a paciente perguntar.** Cada tratamento mostra para quem é, quantas sessões, se dói, quanto tempo dura, a recuperação e quando aparece o resultado. Horário, endereço, "não atendemos convênio" e "PIX ou cartão em até 12x" ficam em chips, não escondidos no rodapé.
4. **Sem tabu, sem constrangimento.** Palavras diretas (incontinência, vaginismo, orgasmo), sem gíria e sem imagem apelativa. Nada de corpo sexualizado: silhuetas, detalhes de pele, a Dra. explicando, equipamentos.
5. **Polegar manda.** Alvos de toque ≥ 44px, CTA fixo no rodapé da tela no celular.
6. **Contraste de verdade.** Texto pequeno sempre ≥ 4,5:1; cinza e rosas claros só em títulos grandes ou sobre grafite/foto.

## Cores

Paleta base: **#4D4A4B · #F60069 · #FF41A1 · #FF90AB · #FFCCD1**.

- **Principal:** `fundo` #FFF5F6 · `ink`/`grafite` #4D4A4B · `rosa` #F60069 ("Agendar avaliação").
- **Secundária:** `blush` #FFCCD1 (botão pastel do menu e sobre fotos, etapa ativa, chip "Consulta online grátis") · `rosa-claro` #FF90AB (texto de destaque sobre foto/grafite) · `rosa-vivo` #FF41A1 (hover, detalhes da flor).
- **Suporte (derivados):** `ink-soft` #8C8889 (palavras cinzas dos títulos) · `ink-muted` #6E6A6B (texto pequeno) · `line` #EADCDF (hairlines) · `scrim` #1F1D1E a 60% (véu nas fotos) · `rosa-texto` #C8004F (erro, link de privacidade) · `status-ok` #2F7D3A (só "Atendendo agora").

Distribuição como na referência: muito fundo claro e foto escura, pastel só nos botões, cor de destaque só em 2ªs linhas de título e números, rosa intenso só no agendamento.

Contraste: ✅ `grafite` sobre `fundo`/`blush` (≥ 6:1), branco sobre `grafite` (8,9:1). ⚠️ Branco sobre `rosa` 4,1:1 → botão com 15px semibold. ⚠️ `ink-soft` (3,3:1) e `rosa-claro` sobre grafite (4,2:1) → só ≥ 18–24px. ❌ `rosa-claro`/`blush` como texto sobre fundo claro; verde para outra coisa que não seja status.

## Tipografia

Neo-grotesca em pesos leves, tracking fechado, quase sem negrito: calma e sofisticação clínica, como na referência.
- **Títulos:** Inter Tight 300–400 (pagas equivalentes: Helvetica Now Display, Neue Montreal, Aeonik).
- **Texto:** Inter 400–500.
- **Hierarquia:** `display` 76/74 peso 300 → `slogan` 60/60 300 → `h1` 42/50 400 → `h2` 32/38 400 → `stat` 30/32 300 → `h3` 18/23 400 → `lead` 16/24 → `body` 15/22 → `small` 13/19 → `button` 14/20 500 → `caption` 12/16.
- Celular: `display` 44, `slogan` 38, `h1` 30, `h2` 26. Nunca menos de 15px no corpo.
- Valores sempre como "A PARTIR DE R$ 120" e só quando a clínica autorizar publicar.

## Componentes

Hero · Navbar · Headline · Button · Chip · Input · Card · ProcessWheel · FAQ · Footer — cada um com prévia e regras próprias.

## Estética

- **Arredondamento:** fotos e cards de foto quase retos (`radius-photo` 6px); moldura de hero, CTA e rodapé `radius-frame` 20px; tudo clicável em pílula (`radius-full`). Nenhum outro raio.
- **Sombras:** nenhuma. Profundidade vem da foto com `scrim`. Exceções: `focus-ring` e `shadow-float` no botão fixo do celular.
- **Linhas:** hairlines de 1px (`line`) separam FAQ, colunas e links, em vez de caixas.
- **Espaçamento:** base 4px; seções com `space-28` (112px) no desktop e `space-16` (64px) no celular; blocos de texto estreitos (290–520px); container 1120px.

## Iconografia e fotos

- Ícones de traço fino (1,4px) dentro de círculos contornados de 30px; seta ↗ em todo link e botão.
- **Fotos reais da clínica**, nunca banco de imagem genérico: a Dra. Lívia de jaleco ou em frente ao painel "Lívia Andrade" da recepção, a equipe, as salas, os equipamentos (MioLink, lasers) e os procedimentos em plano fechado. Luz suave, sempre com véu `scrim` sob texto; um toque de rosa na cena (jaleco, flores, painel) amarra a foto à marca.
- **Antes e depois:** lado a lado, mesmo enquadramento e mesma luz, legenda em `small` com o procedimento e o tempo ("Preenchimento labial · 1 ml"), **só com autorização por escrito da paciente** e respeitando as regras dos conselhos (CREFITO/COFFITO, CRBM).
- **Logo:** flor de 4 pétalas rosa/lilás. Enquanto não houver o vetor, use "Lívia Andrade" em caixa alta, leve e com tracking aberto (como "LUMINA").

## Estrutura sugerida da landing (mesma ordem da referência)

1. **Hero** com menu: foto da Dra., "Saúde íntima / sem tabu", parágrafo à direita, "Ver tratamentos ↗" e chips de prova.
2. **Manifesto central** + foto: "Um lugar seguro para cuidar de você".
3. **Tratamentos**: frase + "Ver todos ↗" e cards de foto numerados (Saúde Íntima, Fisioterapia Pélvica, Rosto, Corpo, Depilação a Laser).
4. **Diferenciais**: grade com hairlines (acolhimento sem tabu, parceria com ginecologista, MioLink, Clube do Corpo).
5. **Como funciona**: roda de 4 etapas (contato → avaliação → protocolo → acompanhamento).
6. **Sobre a Dra. Lívia** e **resultados/depoimentos** em CTA com foto e chips.
7. **Agenda de dias especiais** (Dia do PISOM, Dia do Laser Íntimo, Lavieen Day) com lista de espera.
8. **FAQ** com foto, **CTA final** e **rodapé** com horários, CNPJ, responsável técnica e os 3 Instagrams.

## Voz

Acolhedora, direta e sem tabu, como a Dra. Lívia fala com as pacientes: "Incontinência urinária tem tratamento", "Um lugar seguro para ser ouvida", "Seu corpo merece cuidado, não vergonha". Verbos no imperativo nos botões ("Agendar avaliação", "Quero minha consulta online", "Entrar na lista de espera"); nada de "Saiba mais".

- **Use:** linguagem clara de saúde, segunda pessoa ("você"), "avaliação individual", "resultado natural".
- **Evite:** gírias das redes ("pamonha", "pepeka"), promessas ("resultado garantido", "sem riscos"), termos técnicos sem explicação e emojis no meio do texto do site.
