# Card

Os dois cards da referência aplicados aos tratamentos: o card de foto escura numerado e a grade de diferenciais com hairlines e ícone em círculo.

## Card de foto: `.cr-pcard.cr-photo`
- Foto vertical (cerca de 3:4, `radius-photo` 6px) com véu `scrim`; use a foto real do procedimento ou do equipamento.
- **Topo:** nome do tratamento em `rosa-claro` (`h3` 18px, peso 400) e o número em círculo branco `.cr-num` (01, 02, 03).
- **Base:** dado em destaque `.cr-stat-value` (`stat` 30px, peso 300) com rótulo pequeno ao lado, como "45 minutes" e "5 ml" na referência. Aqui: "2 min · por aplicação", "CRM · parceria com ginecologista", "MioLink · com biofeedback". `.is-accent` deixa o dado em `rosa-claro`.
- **Rodapé:** `.cr-price-from` ("A partir de R$ 120", só quando a clínica autorizar; senão "Comece pela avaliação") e `.cr-btn-pastel.cr-btn-sm` "Agendar", separados por hairline translúcida.

## Diferenciais: `.cr-features` > `.cr-feature`
Colunas separadas por linhas verticais de 1px (`line`), ícone de traço fino num círculo contornado, respiro de 32px, título 18px e descrição 13px em `ink-muted`. Exemplos: acolhimento sem tabu, parceria com ginecologista, MioLink, Clube do Corpo. Abra a seção com `.cr-statement-row`.

## Regras
- Sem fundo branco, sem borda, sem sombra: o card é a foto.
- 3 cards por linha no desktop; carrossel com `.cr-circle-btn` no celular.
- Descrição de no máximo 2 linhas, dizendo para quem é. Nunca prometa resultado.
