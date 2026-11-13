# ProcessWheel

A roda de 4 etapas da referência ("Custom Skincare Mapped To Your Unique Profile"), usada para o "Como funciona" da clínica.

## Anatomia
- Círculo dividido em 4 quadrantes por hairlines `line`; o quadrante da etapa atual fica em `blush` (era o amarelo).
- Miolo `grafite` com 3 frases curtas em que a palavra final fica `rosa-claro` ("Sem tabu. Com escuta. No seu tempo.").
- Números 01 a 04 em círculo sobre o anel; o da etapa ativa fica `rosa`.
- Fotos redondas fora do anel (WhatsApp, avaliação, procedimento, retorno) e `.cr-circle-btn` ‹ › para avançar as etapas.
- Acima: `.cr-manifesto` + `.cr-subtitle` + botão `.cr-btn-dark.cr-btn-sm`.

## Etapas
01 Fale com a gente (WhatsApp ou consulta online grátis) → 02 Avaliação individual → 03 Seu protocolo → 04 Acompanhamento.

## Regras
- Sempre 4 etapas, título de 1 a 3 palavras e descrição de no máximo 3.
- No celular, troque a roda por uma lista vertical 01 a 04 com o mesmo destaque `blush` na etapa ativa.
- O SVG leva `role="img"` e um `aria-label` com as 4 etapas.
