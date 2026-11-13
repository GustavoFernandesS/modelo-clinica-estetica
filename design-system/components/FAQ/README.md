# FAQ

O "Common Questions" da referência: título grande à esquerda, intro curta, lista com hairlines e "+ / −" cinza à direita, e uma foto da clínica ao lado. Tira as dúvidas que impedem o agendamento (avaliação, dor, sessões, pagamento, sigilo, convênio).

## Estrutura
`.cr-faq-wrap` (2 colunas) > texto (`.cr-statement` + `.cr-subtitle` + `.cr-faq`) e `.cr-faq-photo` (`radius-photo`). Cada item é um `<details>` nativo: pergunta 15px peso 500, resposta 13px em `ink-muted`.

## Regras
- De 5 a 8 perguntas por bloco, as mais feitas primeiro. Use as perguntas reais das pacientes (dos destaques do Instagram), por exemplo "Dói?", "Quanto tempo leva?", "Posso fazer na região íntima?" e "Botox ou ácido hialurônico?".
- Respostas de 1 ou 2 frases, sem prometer resultado; se precisar de mais, link para a página do tratamento.
- Toda página de tratamento tem o seu FAQ; a página Dúvidas reúne as gerais.
- No celular a foto sobe para cima da lista. `<details>` nativo funciona com teclado e leitor de tela sem JavaScript.
