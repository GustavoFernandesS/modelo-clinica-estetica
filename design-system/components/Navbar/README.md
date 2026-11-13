# Navbar

Menu sobre a foto do hero: logo em caixa alta à esquerda, links agrupados dentro de UMA pílula contornada no centro e o botão pastel "Agendar" à direita, como na referência.

## Estrutura
`.cr-nav` > `.cr-logo` + `.cr-nav-links` (links; o atual com `aria-current="page"` ganha texto e contorno `blush`) + `.cr-btn.cr-btn-pastel.cr-btn-sm`.

## Regras
- No máximo 5 links: Tratamentos, Saúde Íntima, Resultados, A Clínica, Contato. "Tratamentos" pode abrir um menu com as categorias (Saúde Íntima, Fisioterapia Pélvica, Rosto, Corpo, Depilação).
- Fixo no topo ao rolar: quando sai do hero, ganha fundo `grafite`.
- Abaixo de 760px os links somem (vão para um menu) e ficam só o logo e "Agendar". No rodapé da tela aparece o botão fixo `.cr-btn-hot` "Agendar pelo WhatsApp" com `shadow-float`.
- Logo: a flor de 4 pétalas + "Lívia Andrade" quando houver o vetor; até lá, o nome em caixa alta, leve e com tracking aberto, em `blush`.
