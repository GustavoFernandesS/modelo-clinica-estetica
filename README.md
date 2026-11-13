# Modelo de site · Clínica de estética e saúde íntima

Site demonstrativo da [Codetrax](https://codetraxgf.com), com 9 páginas, para uma clínica de estética, saúde íntima e fisioterapia pélvica. A "Clínica Lívia Andrade", a equipe, os registros, o endereço e os depoimentos são **fictícios**. As fotos são do Unsplash ([CREDITOS.md](CREDITOS.md)).

Todos os botões de WhatsApp e os formulários abrem uma conversa com a Codetrax, para que nenhum número fictício caia no WhatsApp de uma pessoa real.

## Como funciona
- `design-system/`: tokens (JSON e CSS, tema claro e escuro) e 10 componentes com preview.
- `gerar-site.py`: lê o design system e gera todas as páginas em `site/`.
- `site/`: o site publicado (HTML, CSS e JS puros, sem dependências).

```bash
python gerar-site.py site          # gera as páginas
python -m http.server 5182 --directory site
```

## Segurança
`site/vercel.json` define CSP, nosniff, Referrer-Policy, Permissions-Policy, HSTS e bloqueio de iframe. Também envia `noindex`, para o modelo não aparecer em buscas como se fosse uma clínica real.
