# Input

Campos "de linha": sem caixa, só um traço embaixo, na mesma linguagem do "Subscribe to our newsletter ↗" e dos links sublinhados da referência (que não mostra nenhum formulário de caixa).

## Variantes
- `.cr-field` > `.cr-label` + `.cr-input` + `.cr-help`, para nome, WhatsApp e e-mail. Linha de 1px `ink-soft` (3,3:1), texto 16px.
- `.cr-field.cr-select` envolvendo `select.cr-input`, para "Tratamento de interesse" e "Melhor horário".
- `.cr-line-input`: campo + pílula de envio na mesma linha, para "Lista de espera do Dia do PISOM" e "Receber novidades". Dentro de `.cr-on-dark` a linha fica `rosa-claro` e o botão `blush`.
- `.cr-check`: consentimento LGPD em uma linha, com link `rosa-texto` para a política de privacidade.

## Estados
- Foco: a linha engrossa para 2px em `rosa`.
- Erro: `aria-invalid="true"` (linha `rosa-texto`) + `.cr-help-error` dizendo como corrigir.

## Regras
- Rótulo sempre visível acima (12px), nunca só placeholder.
- Peça o mínimo: nome, WhatsApp e tratamento de interesse. Nada de dados de saúde no formulário; isso fica para a avaliação.
- `inputmode="numeric"` no telefone.
- Todo formulário tem o consentimento LGPD ("Autorizo o contato pelo WhatsApp").
