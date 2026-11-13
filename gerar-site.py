# Gera as páginas do modelo de site da Clínica Lívia Andrade (marca fictícia, projeto demonstrativo da Codetrax) seguindo o design system em ./design-system/
# (tokens.css, components/bundle.css e a estrutura HTML dos preview.html, prefixo cr-).
# Uso: python gerar-site.py site
import os, sys, json

OUT = sys.argv[1] if len(sys.argv) > 1 else "site"

# ================================================================ ícones e peças
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 11.5l7-7M5.5 4.5h6v6"/></svg>'
PREV = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 3.5L5.5 8l4.5 4.5"/></svg>'
NEXT = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3.5L10.5 8 6 12.5"/></svg>'

ICONS = {  # traço fino 1,4px em viewBox 16 (como nos previews)
    "heart": '<path d="M8 13.5S2.5 10 2.5 6.3A2.8 2.8 0 0 1 8 5a2.8 2.8 0 0 1 5.5 1.3C13.5 10 8 13.5 8 13.5z"/>',
    "steth": '<path d="M4 2.5v3.5a3 3 0 0 0 6 0V2.5M7 9v1.5a3.5 3.5 0 0 0 7 0V9"/><circle cx="14" cy="7.5" r="1.3"/>',
    "wave": '<path d="M2 8h3l1.5-3.5 3 7L11 8h3"/>',
    "cal": '<rect x="2.5" y="3.5" width="11" height="10" rx="1.5"/><path d="M2.5 6.5h11M5.5 2v3M10.5 2v3"/>',
    "zap": '<path d="M9 1.5L3.5 9h4L7 14.5 12.5 7h-4z"/>',
    "lock": '<rect x="3.5" y="7" width="9" height="7" rx="1.5"/><path d="M5.5 7V5a2.5 2.5 0 0 1 5 0v2"/>',
    "car": '<path d="M3 11h10M4 11v2M12 11v2M2.8 11l1-4A1.5 1.5 0 0 1 5.3 6h5.4a1.5 1.5 0 0 1 1.5 1l1 4z"/>',
    "tv": '<rect x="2" y="3" width="12" height="8.5" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/>',
    "mic": '<rect x="6" y="1.5" width="4" height="7.5" rx="2"/><path d="M3.5 7.5a4.5 4.5 0 0 0 9 0M8 12v2.5"/>',
    "grad": '<path d="M1.5 6L8 3l6.5 3L8 9z"/><path d="M4.5 7.5v3c2 1.5 5 1.5 7 0v-3"/>',
    "insta": '<rect x="2.5" y="2.5" width="11" height="11" rx="3.2"/><circle cx="8" cy="8" r="2.6"/><circle cx="11.3" cy="4.7" r=".5"/>',
    "pin": '<path d="M8 14s-4.5-3.8-4.5-7.5a4.5 4.5 0 0 1 9 0C12.5 10.2 8 14 8 14z"/><circle cx="8" cy="6.5" r="1.6"/>',
    "phone": '<path d="M3.5 2.5h2l1.3 3.2-1.6 1a7 7 0 0 0 4 4l1-1.6 3.3 1.4v2a1.4 1.4 0 0 1-1.4 1.4A10.5 10.5 0 0 1 2 3.9a1.4 1.4 0 0 1 1.5-1.4z"/>',
    "msg": '<path d="M2.5 3.5h11v7H6l-3.5 3z"/>',
    "spark": '<path d="M8 2v3M8 11v3M2 8h3M11 8h3M4 4l2 2M10 10l2 2M4 12l2-2M10 6l2-2"/>',
    "snow": '<path d="M8 2v12M2.8 5l10.4 6M2.8 11l10.4-6"/>',
    "sun": '<circle cx="8" cy="8" r="2.8"/><path d="M8 1.5v1.5M8 13v1.5M1.5 8H3M13 8h1.5M3.4 3.4l1 1M11.6 11.6l1 1M3.4 12.6l1-1M11.6 4.4l1-1"/>',
    "drop": '<path d="M8 2s4 4.3 4 7.3a4 4 0 0 1-8 0C4 6.3 8 2 8 2z"/>',
    "hand": '<path d="M5.5 8.5V3.5a1 1 0 0 1 2 0v4M7.5 7V3a1 1 0 0 1 2 0v4.5M9.5 7.5v-3a1 1 0 0 1 2 0v5a4.5 4.5 0 0 1-4.5 4.5H6.5a4 4 0 0 1-3.3-1.8L2 10a1 1 0 0 1 1.6-1.2l1.9 1.7"/>',
    "flame": '<path d="M8 1.5c1.5 2 3.5 3.5 3.5 6.5a3.5 3.5 0 0 1-7 0c0-1.5.7-2.2 1.4-3 0 1.4.7 2 1.4 2 0-2-.7-3.5.7-5.5z"/>',
    "game": '<rect x="1.5" y="4.5" width="13" height="7" rx="3.5"/><path d="M4.8 7v2.5M3.5 8.2h2.6"/><circle cx="10.5" cy="7.5" r=".6"/><circle cx="12" cy="9" r=".6"/>',
    "menu": '<path d="M2.5 5h11M2.5 8h11M2.5 11h11"/>',
}

def ico(name):
    return f'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def feat_icon(name):
    return f'<span class="cr-feature-icon">{ico(name)}</span>'

USER = ('<svg viewBox="0 0 120 120" fill="currentColor" aria-hidden="true"><circle cx="60" cy="44" r="22"/>'
        '<path d="M18 112c4-24 22-38 42-38s38 14 42 38"/></svg>')

def person(label, chip="", sq=False):
    c = f'<span class="cr-chip">{chip}</span>' if chip else ""
    return f'<div class="person{" sq" if sq else ""}" role="img" aria-label="{label}">{USER}<span>({label})</span>{c}</div>'

# Fotos (baixadas pelo images/baixar-imagens.ps1). WebP com JPG de reserva.
# Fotos livres do Unsplash (créditos em CREDITOS.md). WebP com JPG de reserva.
FOTO = {
    "hero": ("hero-rosto", "Rosto de mulher com pele natural, iluminado por luz suave"),
    "intimo": ("card-laser-intimo", "Paciente deitada recebendo procedimento estético no rosto, com touca e luvas"),
    "pisom": ("card-laser-pisom", "Paciente recebendo aplicação de aparelho no rosto, de olhos fechados"),
    "fisio": ("card-fisioterapia-pelvica", "Fisioterapeuta avaliando o ombro de uma paciente com as mãos"),
    "faq": ("faq-toalha", "Toalha enrolada, frasco de creme e tulipas sobre uma bancada clara"),
    "cta": ("cta-serum-maos", "Mão segurando um frasco de sérum com conta-gotas"),
    "livia": ("dra-livia-retrato", "Dra. Lívia Andrade, de jaleco branco e estetoscópio, sorrindo ao ar livre"),
}

def ph(key, lazy=True, pos="center"):
    f, alt = FOTO[key]
    return (f'<picture class="ph"><source srcset="assets/img/{f}.webp" type="image/webp">'
            f'<img src="assets/img/{f}.jpg" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} decoding="async" style="object-position:{pos}"></picture>')

def retrato(chip="", sq=False, pos="50% 30%"):
    c = f'<span class="cr-chip">{chip}</span>' if chip else ""
    return f'<div class="person has-photo{" sq" if sq else ""}">{ph("livia", pos=pos)}{c}</div>'

def btn(label, kind="dark", wa=None, href=None, size="", arrow=True):
    attrs = f'href="{href}"' if href is not None else f'href="#" data-wa="{wa or ""}"'
    return f'<a class="cr-btn cr-btn-{kind} {size}" {attrs}>{label}{" " + ARROW if arrow else ""}</a>'

def line_link(label, href, accent=False):
    return f'<a class="cr-line-link{" is-accent" if accent else ""}" href="{href}">{label} {ARROW}</a>'

def statement_row(text, btn_html):
    return f'<div class="cr-statement-row"><h2 class="cr-statement">{text}</h2>{btn_html}</div>'

# ================================================================ moldura
NAV = [("index.html", "Início"), ("tratamentos.html", "Tratamentos"), ("laser-intimo.html", "Saúde Íntima"), ("resultados.html", "Resultados"), ("sobre.html", "A Clínica")]

def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a href="{h}">{t} {ARROW}</a>' for h, t in NAV + [("duvidas.html", "Dúvidas"), ("contato.html", "Contato")])
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <nav class="cr-nav" aria-label="Principal">
    <a class="cr-logo" href="index.html" aria-label="Lívia Andrade, página inicial">Lívia Andrade</a>
    <div class="cr-nav-links">{links}</div>
    <div class="nav-actions">
      <a class="cr-btn cr-btn-pastel cr-btn-sm" href="#" data-wa="">Agendar</a>
      <button class="cr-circle-btn nav-toggle" type="button" aria-label="Abrir menu" aria-expanded="false">{ico("menu")}</button>
    </div>
  </nav>
  <div class="mobile-menu">{mlinks}<a class="cr-btn cr-btn-pastel" href="#" data-wa="">Agendar pelo WhatsApp {ARROW}</a></div>
</header>'''

FOOTER = f'''<div class="site-footer">
  <footer class="cr-footer cr-on-dark">
    <div class="cr-footer-grid">
      <div>
        <h2 class="cr-slogan">Seu corpo merece cuidado,<br><span class="cr-accent">não vergonha.</span></h2>
        <p>Saúde íntima, fisioterapia pélvica e estética avançada no Savassi, em Belo Horizonte, desde 2014.</p>
        <form class="cr-line-input" data-wa-form="novidades" style="max-width:320px"><input name="whatsapp" inputmode="numeric" placeholder="Seu WhatsApp" aria-label="Seu WhatsApp para receber novidades"><button type="submit">Receber {ARROW}</button></form>
      </div>
      <div><h5>Tratamentos</h5><ul>
        <li><a href="laser-intimo.html">Saúde Íntima</a></li><li><a href="fisioterapia-pelvica.html">Fisioterapia Pélvica</a></li>
        <li><a href="tratamentos.html#rosto">Rosto e lasers</a></li><li><a href="clube-do-corpo.html">Corpo e Clube do Corpo</a></li>
        <li><a href="tratamentos.html#depilacao">Depilação a Laser</a></li></ul></div>
      <div><h5>A clínica</h5><ul>
        <li><a href="sobre.html">A Dra. Lívia</a></li><li><a href="resultados.html">Resultados</a></li>
        <li><a href="duvidas.html">Dúvidas</a></li><li><a href="contato.html#agenda">Dias especiais</a></li><li><a href="contato.html">Contato</a></li></ul></div>
      <div><h5>Contato</h5><ul>
        <li><a href="#" data-wa="">WhatsApp (31) 9 0000-0000</a></li>
        <li><span>@clinica.liviaandrade (fictício)</span></li>
        <li><a href="contato.html#mapa">Como chegar</a></li><li><a href="contato.html#privacidade">Política de privacidade</a></li></ul>
        <p class="hours-mini" style="margin-top:var(--space-5)">Seg a sex, 8h–19h30 · Sáb, 8h–12h</p></div>
    </div>
    <div class="cr-footer-legal">
      <span>Clínica Lívia Andrade (marca fictícia) · Rua das Acácias, 120, Savassi, Belo Horizonte - MG · Projeto demonstrativo da <a href="https://codetraxgs.com/projetos" target="_blank" rel="noopener noreferrer">Codetrax</a>: marca, pessoas e depoimentos são fictícios</span>
      <span>Responsável técnica: Dra. Lívia Andrade Moura (fictícia) · Não atendemos convênio · © <span data-year>2026</span></span>
    </div>
    <div class="cr-squares" aria-hidden="true"></div>
  </footer>
</div>
<div class="mobile-cta"><a class="cr-btn cr-btn-hot" href="#" data-wa="">Agendar pelo WhatsApp {ARROW}</a></div>
<script src="assets/js/site.js"></script>
</body>
</html>'''

def page(fname, title, desc, active, body):
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/design-system.css">
<link rel="stylesheet" href="assets/css/site.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Ccircle cx='16' cy='16' r='11' fill='%23FF90AB'/%3E%3Ccircle cx='32' cy='16' r='11' fill='%23FFCCD1'/%3E%3Ccircle cx='16' cy='32' r='11' fill='%23FFCCD1'/%3E%3Ccircle cx='32' cy='32' r='11' fill='%23FF90AB'/%3E%3Ccircle cx='24' cy='24' r='5' fill='%23F60069'/%3E%3C/svg%3E">
</head>
<body>
{header(active)}
<main id="conteudo">
{body}
</main>
{FOOTER}'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", fname)

# ================================================================ blocos
def hero_page(crumb, title_html, aside, photo, foot):
    return f'''<div class="frame-wrap"><section class="cr-hero cr-photo hero-page">
  {ph(photo, lazy=False)}
  <div class="cr-hero-body">
    <div><nav class="crumbs" aria-label="Você está em"><a href="index.html">Início</a><span>/</span>{crumb}</nav>
    <h1 class="cr-hero-title">{title_html}</h1></div>
    <p class="cr-hero-aside">{aside}</p>
  </div>
  <div class="cr-hero-foot">{foot}</div>
</section></div>'''

def pcard(n, title, photo, stat, stat_label, text, small, big, wa, href=None, accent=False, pos="center"):
    title_html = f'<a href="{href}" style="color:inherit;text-decoration:none">{title}</a>' if href else title
    return f'''<article class="cr-pcard cr-photo">
  {ph(photo, pos=pos)}
  <span class="cr-num">{n:02d}</span>
  <h3 class="cr-pcard-title">{title_html}</h3>
  <div class="cr-pcard-foot">
    <div class="cr-stat"><span class="cr-stat-value{" is-accent" if accent else ""}">{stat}</span><span class="cr-stat-label">{stat_label}</span></div>
    <p class="cr-pcard-text">{text}</p>
    <div class="cr-pcard-buy"><span class="cr-price-from"><small>{small}</small><span class="cr-price">{big}</span></span><a class="cr-btn cr-btn-pastel cr-btn-sm" href="#" data-wa="{wa}">Agendar</a></div>
  </div>
</article>'''

CARD_LASER = lambda n=1: pcard(n, "Laser Íntimo", "intimo", "CRM", "Parceria com<br>ginecologista", "Para incontinência urinária, ressecamento e flacidez íntima.", "Comece pela", "Avaliação", "Laser Íntimo", "laser-intimo.html")
CARD_PISOM = lambda n=2: pcard(n, "Laser PISOM", "pisom", "2 min", "Por<br>aplicação", "Uniformiza o tom, suaviza poros e linhas e devolve o viço.", "A partir de", "R$ 120", "Laser PISOM", "tratamentos.html#lasers", accent=True)
CARD_FISIO = lambda n=3: pcard(n, "Fisioterapia Pélvica", "fisio", "MioLink", "Com<br>biofeedback", "Fortalece o assoalho pélvico e mostra sua evolução, até jogando.", "Comece pela", "Avaliação", "Fisioterapia Pélvica", "fisioterapia-pelvica.html")

def features(items):
    return '<div class="cr-features">' + "".join(f'<div class="cr-feature">{feat_icon(i)}<h4>{t}</h4><p>{d}</p></div>' for i, t, d in items) + "</div>"

def faq_list(items, open_first=True):
    return '<div class="cr-faq">' + "".join(
        f'<details{" open" if (k == 0 and open_first) else ""}><summary>{q}</summary><p>{a}</p></details>' for k, (q, a) in enumerate(items)) + "</div>"

def faq_wrap(title, intro, items, photo="faq", extra=""):
    return f'''<div class="cr-faq-wrap">
  <div>
    <h2 class="cr-statement" style="font-size:36px;line-height:40px">{title}</h2>
    <p class="cr-subtitle" style="margin-top:var(--space-3);max-width:340px">{intro}</p>
    {faq_list(items)}
    {extra}
  </div>
  <div class="cr-faq-photo cr-photo">{ph(photo)}</div>
</div>'''

REVIEWS = [
    ("Acompanho e sou cliente há vários anos. A clínica transmite o cuidado já na recepção, com profissionalismo e delicadeza.", "Paciente há vários anos", "Avaliação no Google"),
    ("Fiz laser íntimo e em duas sessões mudou minha vida e minha saúde pélvica.", "Paciente de laser íntimo", "Comentário no Instagram"),
    ("Simplesmente a melhor clínica de estética que já fui em BH. Parabéns pelo trabalho.", "Paciente", "Comentário no Instagram"),
    ("Foi um excelente atendimento, a profissional foi super atenciosa e tirou todas as minhas dúvidas.", "Paciente", "Avaliação no Google"),
    ("Fiz preenchimento e botox e estou me sentindo simplesmente bela, com a autoestima elevada.", "Paciente de harmonização facial", "Feedback no WhatsApp"),
    ("Hoje fiz procedimento e fui muito bem atendida. As meninas que trabalham na clínica são ótimas.", "Paciente", "Feedback no Instagram"),
]

def quotes(items):
    return '<div class="quotes">' + "".join(
        f'<figure><span class="stars" aria-label="5 estrelas">★★★★★</span><blockquote>“{q}”</blockquote><figcaption><b>{who}</b>{src}</figcaption></figure>' for q, who, src in items) + "</div>"

def cta_final(title_html, text, wa=""):
    return f'''<div class="frame-wrap"><section class="cta-photo cr-photo" aria-label="Agende sua avaliação">
  {ph("cta", pos="70% center")}
  <div class="stack-6">
    <span class="cr-subtitle" style="color:#FFFFFFCC">Agende sua avaliação</span>
    <h2 class="cta-title">{title_html}</h2>
  </div>
  <div class="cta-foot">
    <div class="stack-6">
      <p>{text}</p>
      <div class="chips"><span class="cr-chip">★ 4,9 no Google · 98 avaliações</span><span class="cr-chip">12 anos de clínica</span><span class="cr-chip">PIX ou cartão em até 12x</span><span class="cr-chip">Estacionamento próprio</span></div>
    </div>
    <div class="cta-actions">{btn("Agendar avaliação", "hot", wa=wa, size="cr-btn-lg")}{btn("Quero minha consulta online", "pastel", href="contato.html#consulta-online", size="cr-btn-lg")}</div>
  </div>
</section></div>'''

STEPS = [("Fale com a gente", "WhatsApp ou online"), ("Avaliação", "Individual e sigilosa"), ("Seu protocolo", "Feito para você"), ("Acompanhamento", "Evolução medida")]

def wheel():
    # Mesma geometria do components/ProcessWheel/preview.html; bolinhas com a foto faq-toalha
    pos_txt = [(190, 134), (370, 134), (370, 262), (190, 262)]
    pos_num = [(174, 94), (386, 94), (386, 306), (174, 306)]
    t = "".join(f'<text class="s-t" data-step="{k}" data-on="s-on" x="{x}" y="{y}" text-anchor="middle">{a}</text>'
                f'<text class="s-d" data-step="{k}" data-on="s-on" x="{x}" y="{y + 17}" text-anchor="middle">{b}</text>' for k, ((a, b), (x, y)) in enumerate(zip(STEPS, pos_txt)))
    nums = "".join(f'<circle class="n-bg" data-step="{k}" data-on="on" cx="{x}" cy="{y}" r="16"/><text class="n-t" data-step="{k}" data-on="on" x="{x}" y="{y + 4}" text-anchor="middle">0{k + 1}</text>' for k, (x, y) in enumerate(pos_num))
    labels = json.dumps([f"{a}: {b}" for a, b in STEPS], ensure_ascii=False).replace('"', "&quot;")
    lis = "".join(f'<li><span class="n">0{k + 1}</span><div><strong>{a}</strong><span>{b}</span></div></li>' for k, (a, b) in enumerate(STEPS))
    return f'''<div class="wheel-box">
  <svg class="cr-wheel" viewBox="0 0 560 400" role="img" aria-label="Quatro passos: fale com a gente, avaliação individual, seu protocolo, acompanhamento" data-wheel data-steps="{labels}">
    <defs><pattern id="cr-ava" patternContentUnits="objectBoundingBox" width="1" height="1"><image href="assets/img/faq-toalha.webp" width="1" height="1" preserveAspectRatio="xMidYMid slice"/></pattern></defs>
    <path class="q-on" d="M280 200 L130 200 A150 150 0 0 1 280 50 Z"/>
    <circle class="ring" cx="280" cy="200" r="150"/>
    <line class="ring" x1="130" y1="200" x2="430" y2="200"/>
    <line class="ring" x1="280" y1="50" x2="280" y2="350"/>
    <circle class="core" cx="280" cy="200" r="64"/>
    <text class="core-t" x="280" y="182" text-anchor="middle">Sem <tspan class="core-a">tabu.</tspan></text>
    <text class="core-t" x="280" y="204" text-anchor="middle">Com <tspan class="core-a">escuta.</tspan></text>
    <text class="core-t" x="280" y="226" text-anchor="middle">No seu <tspan class="core-a">tempo.</tspan></text>
    {t}{nums}
    <circle class="ava" cx="84" cy="70" r="26"/><circle class="ava" cx="476" cy="70" r="26"/><circle class="ava" cx="476" cy="330" r="26"/><circle class="ava" cx="84" cy="330" r="26"/>
  </svg>
  <div class="wheel-nav"><button class="cr-circle-btn" type="button" aria-label="Passo anterior" data-wheel-go="-1">{PREV}</button><p class="wheel-caption" aria-live="polite"></p><button class="cr-circle-btn" type="button" aria-label="Próximo passo" data-wheel-go="1">{NEXT}</button></div>
  <ol class="steps-list">{lis}</ol>
</div>'''

def events_block(with_form=True):
    form = f'''<form class="waitlist" data-wa-form="espera" novalidate>
      <label class="cr-field cr-select" style="max-width:240px"><span class="cr-label">Dia especial</span><select class="cr-input" name="evento"><option>Dia do PISOM</option><option>Dia do Laser Íntimo</option><option>Lavieen Day</option></select></label>
      <div class="stack-4" style="flex:1;min-width:260px"><span class="cr-label">Lista de espera</span>
        <div class="cr-line-input" style="max-width:none"><input name="whatsapp" inputmode="numeric" placeholder="Seu WhatsApp" aria-label="Seu WhatsApp"><button type="submit">Entrar na lista {ARROW}</button></div>
        <span class="cr-help fone-help">Com DDD.</span>
        <label class="cr-check"><input type="checkbox" checked required> Autorizo o contato pelo WhatsApp. <a href="contato.html#privacidade">Política de privacidade</a></label>
      </div>
    </form>''' if with_form else ""
    return f'''<div class="wrap"><section class="dark-frame cr-on-dark" id="agenda">
  <div class="cr-statement-row"><div class="stack-4"><span class="cr-label">Agenda de dias especiais</span><h2 class="cr-statement">Datas que lotam rápido. Seja avisada primeiro.</h2></div></div>
  <div class="events">
    <article class="event"><span class="cr-chip cr-chip-promo">Todo mês</span><h3>Dia do PISOM</h3><p>O PISOM fica na clínica um dia por mês, com data divulgada antes. Face, pescoço, colo, mãos e região íntima externa. A partir de R$ 120 por região, ou 3 regiões por R$ 247.</p></article>
    <article class="event"><span class="cr-chip cr-chip-promo">21 de setembro</span><h3>Dia do Laser Íntimo</h3><p>No aniversário da clínica, quem faz o laser íntimo ganha uma avaliação pélvica com biofeedback MioLink.</p></article>
    <article class="event"><span class="cr-chip cr-chip-promo">Edições especiais</span><h3>Lavieen Day</h3><p>Condições especiais para o laser Lavieen: manchas, melasma, poros e cicatrizes de acne.</p></article>
  </div>
  {form}
</section></div>'''

# ================================================================ HOME (ordem do README)
home = f'''
<div class="frame-wrap"><section class="cr-hero cr-photo ph-hero hero-home" aria-label="Apresentação">
  <div class="cr-hero-body">
    <h1 class="cr-hero-title">Saúde íntima<br><em>sem tabu</em></h1>
    <p class="cr-hero-aside">Fisioterapia pélvica, laser íntimo e estética avançada com avaliação individual e parceria com ginecologista. Há 12 anos em Belo Horizonte.</p>
  </div>
  <div class="cr-hero-foot">
    <div class="hero-actions">{btn("Agendar avaliação", "hot", wa="")}{line_link("Ver tratamentos", "tratamentos.html", accent=True)}</div>
    <div class="chips"><span class="cr-chip">★ 4,9 no Google</span><span class="cr-chip">12 anos de clínica</span><span class="cr-chip">Parceria com ginecologista</span><span class="cr-chip" data-status>Seg a sex 8h–19h30</span></div>
  </div>
</section></div>

<section class="section"><div class="wrap cr-center" style="gap:var(--space-8)">
  <h2 class="cr-manifesto">Um lugar seguro <span class="cr-soft">para cuidar de você,</span> sem tabu <span class="cr-soft">e</span> sem julgamento</h2>
  <p class="cr-subtitle" style="max-width:460px">Incontinência, dor na relação, flacidez, manchas: aqui tudo é assunto de saúde, conversado com calma e sigilo.</p>
  {btn("Conhecer a Dra. Lívia", "dark", href="sobre.html", size="cr-btn-sm")}
  <div class="stats" style="margin-top:var(--space-8)">
    <div class="stat"><strong>4,9 ★</strong><span>Nota no Google, com 98 avaliações</span></div>
    <div class="stat"><strong>12 anos</strong><span>De clínica na Savassi, desde 2014</span></div>
    <div class="stat"><strong>22,8 mil</strong><span>Seguidoras acompanham o trabalho</span></div>
    <div class="stat"><strong>+18 anos</strong><span>De carreira da Dra. Lívia Andrade</span></div>
  </div>
</div></section>

<section class="section" id="tratamentos"><div class="wrap stack-8">
  {statement_row("Incontinência, dor na relação e flacidez têm tratamento.", btn("Ver todos os tratamentos", "dark", href="tratamentos.html", size="cr-btn-sm"))}
  <div class="cr-cards three">{CARD_LASER()}{CARD_PISOM()}{CARD_FISIO()}</div>
  <div class="more-links">{line_link("Rosto e lasers", "tratamentos.html#rosto")}{line_link("Corpo e Clube do Corpo", "clube-do-corpo.html")}{line_link("Depilação a laser", "tratamentos.html#depilacao")}</div>
</div></section>

<section class="section"><div class="wrap stack-8">
  {statement_row("Cuidado de verdade começa por ouvir você.", btn("Conhecer a clínica", "dark", href="sobre.html", size="cr-btn-sm"))}
  {features([("heart", "Acolhimento sem tabu", "Um lugar seguro para falar de saúde íntima, sem julgamento."),
             ("steth", "Parceria com ginecologista", "Procedimentos íntimos com acompanhamento médico (CRM)."),
             ("wave", "MioLink com biofeedback", "Fisioterapia pélvica que mostra sua evolução, até jogando."),
             ("cal", "Clube do Corpo", "Plano mensal com horário fixo, como numa academia.")])}
</div></section>

<section class="section" id="como-funciona"><div class="wrap cr-center" style="gap:var(--space-5)">
  <h2 class="cr-manifesto" style="font-size:36px;line-height:42px">Seu cuidado pensado <span class="cr-soft">do primeiro contato</span> ao acompanhamento</h2>
  <p class="cr-subtitle">Sua jornada na clínica em 4 passos</p>
  {btn("Começar pela consulta online", "dark", href="contato.html#consulta-online", size="cr-btn-sm")}
  {wheel()}
</div></section>

<section class="section"><div class="wrap stack-8">
  <div class="about">
    {retrato(chip="Responsável técnica")}
    <div class="stack-6">
      <span class="cr-label">Quem vai cuidar de você</span>
      <h2 class="cr-statement">Dra. Lívia Andrade Moura</h2>
      <div class="chips"><span class="cr-chip cr-chip-outline">Fisioterapeuta</span><span class="cr-chip cr-chip-outline">Biomédica esteta</span><span class="cr-chip cr-chip-outline">Ozonioterapeuta</span></div>
      <p class="lead">Especialista em fisioterapia pélvica, com formação complementar em vaginismo, a Dra. Lívia une mais de 18 anos de carreira à escuta atenta. Ela também ministra cursos para outras profissionais e fala de saúde íntima sem tabu nas redes.</p>
      <p class="quote">“Cuidar da saúde íntima vai muito além da estética. É autoconhecimento, autoestima e qualidade de vida.”</p>
      <div>{line_link("Conhecer a história da clínica", "sobre.html")}</div>
    </div>
  </div>
</div></section>

<section class="section" id="depoimentos"><div class="wrap stack-8">
  {statement_row("O que as pacientes dizem.", '<span class="cr-chip cr-chip-outline">★ 4,9 · 98 avaliações no Google</span>')}
  {quotes(REVIEWS[:3])}
  <div>{line_link("Ver resultados e depoimentos", "resultados.html")}</div>
</div></section>

<section class="section">{events_block()}</section>

<section class="section" id="duvidas"><div class="wrap">
  {faq_wrap("Dúvidas frequentes", "Reunimos as perguntas que as pacientes mais fazem antes da primeira avaliação.", [
    ("Preciso passar por avaliação antes?", "Sim. Antes de qualquer procedimento fazemos uma avaliação individual para indicar o protocolo certo. Ela também pode começar pela consulta online gratuita."),
    ("O Laser PISOM dói?", "A sensibilidade varia de pessoa para pessoa, mas em geral é bem tolerado: o desconforto é leve e a aplicação dura cerca de 2 minutos."),
    ("Vocês atendem convênio?", "Não. Aceitamos PIX e cartão em até 12x, e temos pacotes e o plano mensal da Clube do Corpo."),
    ("Meu atendimento é sigiloso?", "Sim. Saúde íntima é tratada com discrição, do primeiro contato no WhatsApp até o acompanhamento."),
    ("Os procedimentos íntimos têm acompanhamento médico?", "Sim. A clínica tem parceria com a Dra. Marina Costa, ginecologista e cirurgiã, que atua junto com a Dra. Lívia nos casos íntimos."),
    ("Tem estacionamento?", "Sim, a clínica tem estacionamento próprio no Savassi, em Belo Horizonte."),
  ], extra=f'<div style="margin-top:var(--space-8)">{line_link("Ver todas as dúvidas", "duvidas.html")}</div>')}
</div></section>

{cta_final('Dê o primeiro passo.<br><em>Você merece esse cuidado.</em>', "Conte o que está sentindo pelo WhatsApp ou comece pela consulta online gratuita. A gente explica tudo, sem pressa e sem julgamento.")}
'''
page("index.html", "Clínica Lívia Andrade · Saúde íntima, fisioterapia pélvica e estética em Belo Horizonte",
     "Laser íntimo, fisioterapia pélvica, harmonização e estética avançada em Belo Horizonte. 12 anos de clínica, nota 4,9 no Google e parceria com ginecologista.",
     "index.html", home)

# ================================================================ TRATAMENTOS
def group(gid, statement, link_html, cards):
    return f'''<section class="section" id="{gid}"><div class="wrap stack-8">
  {statement_row(statement, link_html)}
  <div class="cr-cards three">{cards}</div>
</div></section>'''

trat = f'''
{hero_page("<span>Tratamentos</span>", "Todos os cuidados<br><em>em um só lugar</em>",
  "Do íntimo ao rosto e ao corpo. Todos os tratamentos começam por uma avaliação individual.", "pisom",
  f'<div class="hero-actions">{btn("Agendar avaliação", "hot", wa="")}{line_link("Consulta online grátis", "contato.html#consulta-online", accent=True)}</div><div class="chips"><span class="cr-chip">Avaliação individual</span><span class="cr-chip">PIX ou cartão em até 12x</span><span class="cr-chip">Não atendemos convênio</span></div>')}
<section class="section" style="padding-bottom:var(--space-16)"><div class="wrap"><nav class="more-links" style="margin:0" aria-label="Categorias">
  {line_link("Saúde íntima", "#intima")}{line_link("Fisioterapia pélvica", "#pelvica")}{line_link("Rosto", "#rosto")}{line_link("Lasers", "#lasers")}{line_link("Corpo", "#corpo")}{line_link("Depilação a laser", "#depilacao")}
</nav></div></section>
{group("intima", "Saúde íntima sem tabu, com parceria médica.", btn("Ver laser íntimo", "dark", href="laser-intimo.html", size="cr-btn-sm"),
  CARD_LASER(1) +
  pcard(2, "Harmonização Íntima", "faq", "100%", "Discreta e<br>sigilosa", "Preenchimento, bioestimulador e toxina, para mulheres e homens.", "Comece pela", "Avaliação", "Harmonização Íntima") +
  pcard(3, "Bioestimulador Autólogo", "cta", "Autólogo", "Do seu próprio<br>organismo", "Estímulo de colágeno íntimo com componentes do seu corpo.", "Comece pela", "Avaliação", "Bioestimulador Autólogo", accent=True))}
{group("pelvica", "Seu assoalho pélvico merece cuidado.", btn("Ver fisioterapia pélvica", "dark", href="fisioterapia-pelvica.html", size="cr-btn-sm"),
  CARD_FISIO(1) +
  pcard(2, "Vaginismo e Dor na Relação", "faq", "Especialista", "Formação em<br>vaginismo", "Abordagem multidisciplinar e acolhedora, no seu tempo.", "Comece pela", "Avaliação", "Vaginismo", "fisioterapia-pelvica.html#vaginismo") +
  pcard(3, "Pós-parto e Menopausa", "intimo", "MioLink", "Evolução<br>na tela", "Força, sensibilidade e confiança em cada fase.", "Comece pela", "Avaliação", "Fisioterapia Pélvica", "fisioterapia-pelvica.html", accent=True))}
{group("rosto", "Rosto: resultado natural, sem exageros.", btn("Ver resultados", "dark", href="resultados.html", size="cr-btn-sm"),
  pcard(1, "Botox", "hero", "Natural", "Leve e<br>descansado", "Suaviza linhas de expressão e previne rugas.", "Comece pela", "Avaliação", "Botox", pos="center 30%") +
  pcard(2, "Preenchimentos", "pisom", "1 ml", "Lábios, olheiras<br>e malar", "Ácido hialurônico para contorno e um olhar descansado.", "Comece pela", "Avaliação", "Preenchimento", accent=True) +
  pcard(3, "Bioestimuladores e Skinbooster", "cta", "Colágeno", "De dentro<br>para fora", "Sculptra, Radiesse, skinbooster e fios de PDO para firmeza e viço.", "Comece pela", "Avaliação", "Bioestimulador"))}
{group("lasers", "Lasers de última geração.", btn("Ver dias especiais", "dark", href="contato.html#agenda", size="cr-btn-sm"),
  CARD_PISOM(1) +
  pcard(2, "Laser CO₂ e Lavieen", "intimo", "Lavieen Day", "Condições<br>especiais", "Rejuvenescimento, manchas, melasma, poros e cicatrizes de acne.", "Comece pela", "Avaliação", "Laser CO2 / Lavieen") +
  pcard(3, "Laser Etherea", "hero", "Intraoral", "Colágeno por<br>dentro da boca", "Rejuvenescimento facial, rugas, textura e estrias.", "Comece pela", "Avaliação", "Laser Etherea", accent=True, pos="center 30%"))}
{group("corpo", "Corpo: contorno, firmeza e constância.", btn("Conhecer a Clube do Corpo", "dark", href="clube-do-corpo.html", size="cr-btn-sm"),
  pcard(1, "Clube do Corpo", "faq", "Mensal", "Horário fixo,<br>como um clube", "Criolipólise, radiofrequência, lipocavitação, ozonioterapia e mais.", "Plano", "Mensalidade", "Clube do Corpo", "clube-do-corpo.html", accent=True) +
  pcard(2, "Harmonização Glútea", "cta", "Volume", "Natural e<br>firme", "Preenchimento e bioestimulador para contorno e textura.", "Comece pela", "Avaliação", "Harmonização Glútea") +
  pcard(3, "Ozonioterapia", "fisio", "Ozônio", "Com a Dra.,<br>ozonioterapeuta", "Ozonioterapia estética e de bem-estar.", "Comece pela", "Avaliação", "Ozonioterapia"))}
{group("depilacao", "Depilação a laser: diga adeus à cera.", btn("Agendar pelo WhatsApp", "dark", wa="Depilação a Laser", size="cr-btn-sm"),
  pcard(1, "Depilação a Laser", "pisom", "10", "Sessões<br>por pacote", "Laser de diodo, pacotes por região ou combinados.", "Pague em", "Até 12x", "Depilação a Laser", accent=True) +
  pcard(2, "Axilas", "intimo", "10", "Sessões", "Promoções frequentes de pacote no PIX.", "Pacote", "No PIX", "Depilação a Laser — axilas") +
  pcard(3, "Corpo Completo", "cta", "10", "Sessões<br>completas", "Pacote completo, parcelado no cartão.", "Pague em", "Até 12x", "Depilação a Laser — corpo completo"))}
{cta_final('Não sabe qual é<br><em>o tratamento certo?</em>', "Conte o que você sente. Na avaliação, a Dra. Lívia indica o protocolo ideal para o seu caso.")}
'''
page("tratamentos.html", "Tratamentos · Clínica Lívia Andrade",
     "Laser íntimo, fisioterapia pélvica, harmonização íntima e facial, lasers, corpo e depilação a laser em Belo Horizonte.", "tratamentos.html", trat)

# ================================================================ PÁGINA DE TRATAMENTO
def treatment(fname, title, crumb, h1, aside_txt, photo, wa, chips, blocks, faqs, related, desc, aside_extra=""):
    body = f'''
{hero_page(f'<a href="tratamentos.html">Tratamentos</a><span>/</span><span>{crumb}</span>', h1, aside_txt, photo,
  f'<div class="hero-actions">{btn(f"Agendar {crumb.lower()}", "hot", wa=wa)}{line_link("Ver dúvidas", "#duvidas", accent=True)}</div><div class="chips">{chips}</div>')}
<section class="section"><div class="wrap">
  <div class="treat">
    <div class="blocks">{blocks}</div>
    <aside class="treat-aside">
      <div class="aside-dark cr-on-dark">
        <span class="cr-label">Agende sua avaliação</span>
        <h3>{crumb}</h3>
        <p>Chame no WhatsApp com a mensagem pronta e escolha o melhor horário.</p>
        {btn("Agendar pelo WhatsApp", "pastel", wa=wa)}
        <span class="cr-chip" data-status>Seg a sex 8h–19h30 · sáb 8h–12h</span>
      </div>
      {aside_extra}
      <div class="aside-light"><span class="cr-label">Por que aqui</span>
        <ul class="ticks"><li>Avaliação individual antes de tudo</li><li>Parceria com ginecologista (CRM)</li><li>Atendimento sigiloso e sem julgamento</li><li>PIX ou cartão em até 12x</li></ul></div>
    </aside>
  </div>
</div></section>
<section class="section" id="duvidas"><div class="wrap">{faq_wrap(f"Dúvidas sobre {crumb.lower()}", "As perguntas mais feitas antes da primeira sessão.", faqs, photo="faq")}</div></section>
<section class="section"><div class="wrap stack-8">
  {statement_row("Tratamentos relacionados.", btn("Ver todos os tratamentos", "dark", href="tratamentos.html", size="cr-btn-sm"))}
  <div class="cr-cards three">{related}</div>
</div></section>
{cta_final(f'Pronta para cuidar de você?<br><em>Agende {crumb.lower()}.</em>', "Fale com a gente no WhatsApp. A primeira conversa já tira boa parte das suas dúvidas.", wa=wa)}
'''
    page(fname, title, desc, "laser-intimo.html", body)

def block(label, title, inner):
    return f'<section class="block"><span class="cr-label">{label}</span><h2 class="h2-light">{title}</h2>{inner}</section>'

def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def facts(items):
    return '<div class="facts">' + "".join(f'<div class="fact"><span class="cr-label">{a}</span><strong>{b}</strong><span>{c}</span></div>' for a, b, c in items) + "</div>"

def note(text, src, icon="msg"):
    return f'<div class="note">{feat_icon(icon)}<div><p>“{text}”</p><small>{src}</small></div></div>'

def video(photo, label):
    return f'<div class="photo-wide cr-photo">{ph(photo)}<div class="play"><span class="cr-btn cr-btn-pastel cr-btn-sm">Assistir {ARROW}</span>({label})</div></div>'

LI_BLOCKS = (
    block("Para quem é", "Você pode se beneficiar se sente…", ticks([
        "Escapes de urina ao tossir, espirrar, rir ou se exercitar (incontinência urinária de esforço)",
        "Ressecamento, ardência ou desconforto na região íntima",
        "Sensação de flacidez ou mudanças após o parto ou a menopausa",
        "Diminuição da sensibilidade e da qualidade da vida íntima",
        "Vontade de rejuvenescer a região com um procedimento sem cortes"])) +
    block("O que é", "Tecnologia a laser a favor da sua saúde íntima",
        '<p class="body-text">O laser íntimo usa tecnologia de CO₂ para estimular a produção de colágeno e melhorar a elasticidade da mucosa. É uma alternativa moderna e sem cortes para tratar a incontinência urinária e o ressecamento, devolvendo conforto e confiança.</p>'
        '<p class="body-text">Aqui, o laser íntimo é feito dentro de uma parceria entre a estética e a ginecologia: a Dra. Lívia, fisioterapeuta pélvica e biomédica esteta, atua junto com a Dra. Marina Costa, ginecologista e cirurgiã. Você recebe um olhar completo, funcional e estético.</p>') +
    block("Na prática", "O que você precisa saber", facts([
        ("Avaliação", "Sempre antes", "Consulta individual para indicar o protocolo."),
        ("Sessões", "Definidas na avaliação", "Conforme a sua queixa e a evolução."),
        ("Cortes", "Nenhum", "Procedimento não cirúrgico, feito na clínica."),
        ("Conforto", "Avaliado em cada sessão", "Tire suas dúvidas sobre sensibilidade na avaliação."),
        ("Parceria médica", "Ginecologista", "Dra. Marina Costa, CRM-MG 000000 (fictícia)."),
        ("Combina com", "Fisioterapia pélvica", "Avaliação com biofeedback MioLink.")])) +
    block("Benefícios", "O que muda na sua rotina", ticks([
        "Mais controle da bexiga e menos escapes", "Mais hidratação e conforto no dia a dia",
        "Melhora da firmeza e do aspecto da região", "Mais sensibilidade, autoestima e qualidade na vida íntima"]) +
        note("Fiz laser íntimo e em duas sessões mudou minha vida e minha saúde pélvica.", "Comentário de paciente no Instagram da clínica. Os resultados variam de pessoa para pessoa.")) +
    block("Veja a Dra. Lívia explicando", "Laser íntimo, sem tabu", video("intimo", "vídeo da Dra. Lívia sobre laser íntimo")) +
    block("Cuidados", "Antes e depois do procedimento",
        '<p class="body-text">As orientações de preparo, os cuidados nos dias seguintes e as contraindicações (como gestação ou infecções ativas) são explicados na avaliação, de acordo com o seu caso.</p>')
)
treatment("laser-intimo.html", "Laser Íntimo em Belo Horizonte · Clínica Lívia Andrade", "Laser íntimo",
  "Laser íntimo,<br><em>sem cortes</em>",
  "Incontinência urinária, ressecamento e flacidez íntima têm tratamento, com parceria entre a estética e a ginecologia.",
  "intimo", "Laser Íntimo",
  '<span class="cr-chip">Sem cortes</span><span class="cr-chip">Parceria com ginecologista</span><span class="cr-chip">Atendimento sigiloso</span>',
  LI_BLOCKS, [
    ("O laser íntimo trata incontinência urinária?", "Ele é uma alternativa moderna para a incontinência urinária de esforço. Na avaliação, vemos se ele é indicado sozinho ou junto com a fisioterapia pélvica."),
    ("Precisa de cirurgia ou corte?", "Não. É um procedimento não cirúrgico, feito na própria clínica."),
    ("Quantas sessões vou precisar?", "Depende da sua queixa e de como o seu corpo responde. O número de sessões é definido na avaliação individual."),
    ("Posso fazer no pós-parto ou na menopausa?", "São fases em que o laser íntimo costuma ser indicado. O momento certo é avaliado caso a caso."),
    ("Tem acompanhamento médico?", "Sim. A clínica trabalha em parceria com a Dra. Marina Costa, ginecologista e cirurgiã (CRM-MG 000000, fictícia)."),
    ("Quando é o Dia do Laser Íntimo?", "Em 21 de setembro, aniversário da clínica. Quem faz o laser nesse dia ganha uma avaliação pélvica com biofeedback MioLink."),
  ], CARD_FISIO(1) + pcard(2, "Harmonização Íntima", "faq", "100%", "Discreta e<br>sigilosa", "Preenchimento, bioestimulador autólogo e limpeza de pele íntima.", "Comece pela", "Avaliação", "Harmonização Íntima", "tratamentos.html#intima") + CARD_PISOM(3),
  "Laser íntimo em Belo Horizonte para incontinência urinária, ressecamento e flacidez íntima, com parceria com ginecologista.",
  aside_extra='<div class="aside-light"><span class="cr-chip cr-chip-promo" style="align-self:flex-start">21 de setembro</span><h3 class="h3-light">Dia do Laser Íntimo</h3><p class="small">No aniversário da clínica, quem faz o laser íntimo ganha uma avaliação pélvica com biofeedback MioLink.</p>' + line_link("Quero ser avisada", "contato.html#agenda") + "</div>")

FP_BLOCKS = (
    block("Para quem é", "A fisioterapia pélvica ajuda quem sente…", ticks([
        "Escapes de urina (incontinência urinária) ou de fezes", "Dor na relação ou dificuldade de penetração (vaginismo)",
        "Pouca sensibilidade ou dificuldade de chegar ao orgasmo", "Fraqueza do assoalho pélvico no pós-parto",
        "Mudanças na menopausa que afetam o conforto e a vida íntima"])) +
    block("Como funciona", "É como academia: o músculo certo, do jeito certo",
        '<p class="body-text">Na fisioterapia pélvica não basta fazer o exercício: é preciso exercitar o músculo certo, da maneira certa. Feitos de forma errada, os exercícios podem não dar resultado ou até piorar algumas disfunções.</p>'
        '<p class="body-text">A Dra. Lívia Andrade é fisioterapeuta pélvica, com formação complementar em vaginismo. Ela avalia cada paciente e orienta os exercícios de forma individual, identificando quais músculos precisam ser trabalhados.</p>') +
    block("Tecnologia", "Biofeedback MioLink e tratamento gamificado", features([
        ("wave", "Biofeedback MioLink", "Você vê a sua contração na tela e acompanha a evolução a cada sessão."),
        ("game", "Fisioterapia que você joga", "Os exercícios viram um jogo, e a sessão fica leve e motivadora."),
        ("steth", "Equipe multidisciplinar", "Fisioterapia pélvica e ginecologia juntas.")])) +
    f'<section class="block" id="vaginismo"><span class="cr-label">Vaginismo</span><h2 class="h2-light">Um olhar completo, acolhedor e especializado</h2><p class="body-text">O vaginismo é uma disfunção pélvica séria e tratável. O tratamento pede cuidado multidisciplinar, porque físico e emocional caminham juntos. Com formação específica em vaginismo, a Dra. Lívia acompanha cada etapa com técnica, paciência e acolhimento.</p></section>' +
    block("Na prática", "O que você precisa saber", facts([
        ("Primeiro passo", "Avaliação pélvica", "Com biofeedback, para entender a sua musculatura."),
        ("Sessões", "Plano individual", "A frequência é definida na avaliação."),
        ("Evolução", "Acompanhada na tela", "Você vê o seu progresso sessão a sessão."),
        ("Equipe", "Multidisciplinar", "Fisioterapia pélvica e ginecologia juntas."),
        ("Ambiente", "Sem julgamento", "Um lugar seguro para falar de tudo."),
        ("Combina com", "Laser íntimo", "Para um cuidado ainda mais completo.")])) +
    block("Relato", "Quem já fez", note("Ela relatou melhora na força e na sensibilidade, e até o namorado notou a diferença.", "Caso de reabilitação pélvica publicado pela clínica, com atendimento conjunto de ginecologista e fisioterapeuta pélvica.")) +
    block("Veja na prática", "O MioLink em ação", video("fisio", "vídeo do MioLink e do tratamento gamificado, dos reels da clínica"))
)
treatment("fisioterapia-pelvica.html", "Fisioterapia Pélvica em Belo Horizonte · Clínica Lívia Andrade", "Fisioterapia pélvica",
  "Fisioterapia pélvica<br><em>que acolhe</em>",
  "Incontinência, vaginismo, dor na relação, pós-parto e menopausa, com biofeedback MioLink e uma especialista que escuta você.",
  "fisio", "Fisioterapia Pélvica",
  '<span class="cr-chip">Biofeedback MioLink</span><span class="cr-chip">Especialista em vaginismo</span><span class="cr-chip">Tratamento gamificado</span>',
  FP_BLOCKS, [
    ("Incontinência urinária tem tratamento?", "Tem, sim. A fisioterapia pélvica fortalece e reeduca a musculatura do assoalho pélvico, e pode ser combinada com o laser íntimo."),
    ("Posso fazer os exercícios sozinha em casa?", "Sem orientação, é comum exercitar o músculo errado. Na clínica, o biofeedback mostra se você está contraindo do jeito certo."),
    ("Chá ou relaxamento resolvem o vaginismo?", "Podem ajudar a relaxar, mas o vaginismo é uma disfunção pélvica que precisa de fisioterapia especializada, acolhimento e técnicas específicas."),
    ("A fisioterapia pélvica precisa ser chata?", "Não. Com o MioLink, os exercícios viram um jogo, e você acompanha a sua evolução na tela."),
    ("Serve para o pós-parto?", "Sim. A fisioterapia pélvica ajuda a recuperar força, sensibilidade e controle depois do parto."),
  ], CARD_LASER(1) + pcard(2, "Harmonização Íntima", "faq", "100%", "Discreta e<br>sigilosa", "Preenchimento, bioestimulador autólogo e limpeza de pele íntima.", "Comece pela", "Avaliação", "Harmonização Íntima", "tratamentos.html#intima") + CARD_PISOM(3),
  "Fisioterapia pélvica em Belo Horizonte para incontinência urinária, vaginismo, dor na relação, pós-parto e menopausa, com biofeedback MioLink.")

# ================================================================ ACADEMIA DO CORPO
acad = f'''
{hero_page('<a href="tratamentos.html">Tratamentos</a><span>/</span><span>Clube do Corpo</span>', "Estética corporal<br><em>como academia</em>",
  "Você paga uma mensalidade e usa os tratamentos corporais com horário fixo. Chega de pagar estética por sessão.", "faq",
  f'<div class="hero-actions">{btn("Quero conhecer o plano", "hot", wa="Clube do Corpo")}{line_link("O que está incluso", "#incluso", accent=True)}</div><div class="chips"><span class="cr-chip cr-chip-hot">Novidade</span><span class="cr-chip">Mensalidade</span><span class="cr-chip">Horário fixo</span></div>')}
<section class="section" id="incluso"><div class="wrap stack-8">
  {statement_row("Tecnologias corporais em um só plano.", '<span class="cr-subtitle">E muito mais, combinado na avaliação.</span>')}
  {features([("wave", "Lipocavitação", "Ultrassom para gordura localizada."), ("drop", "Ozonioterapia estética", "Com a Dra. Lívia, ozonioterapeuta."),
             ("zap", "Corrente russa", "Estímulo e tonificação muscular."), ("sun", "Radiofrequência", "Firmeza e combate à flacidez.")])}
  {features([("snow", "Criolipólise", "Redução de gordura pelo frio."), ("flame", "Manta térmica", "Calor que potencializa os protocolos."),
             ("spark", "Enzimas localizadas", "Ação direta na gordura localizada."), ("hand", "Endermologia", "Celulite, drenagem e contorno.")])}
</div></section>
<section class="section"><div class="wrap stack-8">
  <div class="cr-center"><h2 class="cr-manifesto">Constância <span class="cr-soft">é o que</span> traz resultado</h2></div>
  <div class="compare">
    <div class="old"><span class="cr-label">Por sessão</span><h3 class="h2-light">Do jeito tradicional</h3>{ticks(["Você paga cada sessão separadamente", "Fica mais difícil manter a frequência", "Um tratamento de cada vez"])}</div>
    <div class="new cr-on-dark"><span class="cr-label">Clube do Corpo</span><h3 class="h2-light" style="color:var(--rosa-claro)">Como numa academia</h3>{ticks(["Uma mensalidade, vários tratamentos", "Horário fixo garantido na sua semana", "Protocolo combinado para o seu objetivo"])}{btn("Quero conhecer o plano", "pastel", wa="Clube do Corpo")}</div>
  </div>
</div></section>
<section class="section"><div class="wrap">{faq_wrap("Dúvidas sobre o plano", "Como funciona a Clube do Corpo.", [
    ("Como funciona a Clube do Corpo?", "É um plano mensal: você paga uma mensalidade e tem acesso a vários tratamentos corporais, com horário fixo, como numa academia."),
    ("Quais tratamentos posso fazer?", "Lipocavitação, ozonioterapia estética, corrente russa, radiofrequência, criolipólise, manta térmica, enzimas localizadas, endermologia e mais, combinados na avaliação."),
    ("Qual é o valor da mensalidade?", "Os planos são montados de acordo com o seu objetivo. Chame no WhatsApp para conhecer as opções."),
    ("Preciso de avaliação?", "Sim. Na avaliação definimos o protocolo, os tratamentos e a frequência ideais para você."),
  ])}</div></section>
{cta_final('Garanta o seu<br><em>horário fixo.</em>', "As vagas da Clube do Corpo são limitadas pelos horários da agenda. Fale com a gente e conheça o plano.", wa="Clube do Corpo")}
'''
page("clube-do-corpo.html", "Clube do Corpo · plano mensal de estética corporal · Clínica Lívia Andrade",
     "Plano mensal de tratamentos corporais em Belo Horizonte: criolipólise, radiofrequência, lipocavitação, ozonioterapia e mais, com horário fixo.", "tratamentos.html", acad)

# ================================================================ RESULTADOS
def ba_slot(title, sub):
    return f'<figure class="ba-slot" style="margin:0"><div class="halves"><span>Antes</span><span>Depois</span></div><figcaption><strong>{title}</strong><small>{sub}</small></figcaption></figure>'

res = f'''
{hero_page("<span>Resultados</span>", "Resultados naturais,<br><em>histórias reais</em>",
  "Cada resultado começa com uma avaliação individual. Os resultados variam de pessoa para pessoa.", "hero",
  f'<div class="hero-actions">{btn("Agendar avaliação", "hot", wa="")}{line_link("Ler depoimentos", "#depoimentos", accent=True)}</div><div class="chips"><span class="cr-chip">★ 4,9 no Google</span><span class="cr-chip">98 avaliações</span></div>')}
<section class="section"><div class="wrap stack-8">
  {statement_row("Antes e depois, com autorização.", '<span class="cr-subtitle" style="max-width:340px">Espaços reservados para casos reais, sempre com autorização por escrito das pacientes e seguindo as regras dos conselhos.</span>')}
  <div class="ba-grid">
    {ba_slot("Preenchimento labial", "1 ml de ácido hialurônico")}{ba_slot("Preenchimento de olheiras", "Ácido hialurônico")}{ba_slot("Botox", "Testa e olhar")}
    {ba_slot("Bioestimulador de colágeno", "Após 15 dias")}{ba_slot("Harmonização glútea", "Bioestimulador")}{ba_slot("Laser Lavieen", "Manchas e melasma")}
  </div>
</div></section>
<section class="section" id="depoimentos"><div class="wrap stack-8">
  {statement_row("Quem viveu, recomenda.", '<span class="cr-chip cr-chip-outline">★ 4,9 · 98 avaliações no Google</span>')}
  {quotes(REVIEWS)}
  <p class="small">Depoimentos ilustrativos: este é um modelo de site e as pacientes citadas são fictícias.</p>
</div></section>
{cta_final('Seu cuidado<br><em>começa aqui.</em>', "Agende sua avaliação e descubra o protocolo ideal para você.")}
'''
page("resultados.html", "Resultados e depoimentos · Clínica Lívia Andrade",
     "Depoimentos de pacientes da Clínica Lívia Andrade em Belo Horizonte. Nota 4,9 no Google.", "resultados.html", res)

# ================================================================ SOBRE
sobre = f'''
{hero_page("<span>A clínica</span>", "Cuidado que começa<br><em>na recepção</em>",
  "Desde 2014 no Savassi, em Belo Horizonte, unindo fisioterapia, biomedicina estética e ginecologia para cuidar da mulher por inteiro.", "faq",
  f'<div class="hero-actions">{btn("Agendar avaliação", "hot", wa="")}{line_link("Conhecer a equipe", "#equipe", accent=True)}</div><div class="chips"><span class="cr-chip">Desde 2014</span><span class="cr-chip">Estacionamento próprio</span></div>')}
<section class="section"><div class="wrap">
  <div class="about">
    {retrato(chip="Fundadora")}
    <div class="stack-6">
      <span class="cr-label">A fundadora</span>
      <h2 class="cr-statement">Dra. Lívia Andrade Moura</h2>
      <div class="chips"><span class="cr-chip cr-chip-outline">Fisioterapeuta</span><span class="cr-chip cr-chip-outline">Biomédica esteta</span><span class="cr-chip cr-chip-outline">Ozonioterapeuta</span><span class="cr-chip cr-chip-promo">Especialista em fisioterapia pélvica</span></div>
      <p class="lead">Começou como esteticista e fisioterapeuta e hoje soma mais de 18 anos de carreira. Especialista em fisioterapia pélvica, com formação complementar em vaginismo.</p>
      <p class="quote">“Quero que cada paciente saia daqui entendendo o próprio corpo, e sem vergonha de perguntar.”</p>
      <p class="small">A Dra. Lívia fez da clínica um lugar onde saúde íntima é tratada sem tabu. Ministra cursos para profissionais da área e leva o tema a palestras e às redes.</p>
    </div>
  </div>
</div></section>
<section class="section"><div class="wrap stack-8">
  {statement_row("Uma história de dedicação.", "")}
  <div class="stats">
    <div class="stat"><strong>2014</strong><span>Nasce a clínica, em setembro, no Savassi.</span></div>
    <div class="stat"><strong>2018</strong><span>Primeiros cursos para profissionais da área, em Belo Horizonte.</span></div>
    <div class="stat"><strong>2019</strong><span>Fisioterapia pélvica e laser íntimo viram o coração da clínica.</span></div>
    <div class="stat"><strong>2026</strong><span>12 anos e referência em saúde íntima e pélvica.</span></div>
  </div>
</div></section>
<section class="section" id="equipe"><div class="wrap stack-8">
  {statement_row("Profissionais que trabalham juntos.", "")}
  <div class="team">
    <div class="stack-4">{retrato(sq=True, pos="50% 25%")}<h3 class="h3-light">Dra. Lívia Andrade</h3><p class="small">Fisioterapeuta pélvica e biomédica esteta. Responsável técnica.</p></div>
    <div class="stack-4">{person("foto da Dra. Marina Costa", sq=True)}<h3 class="h3-light">Dra. Marina Costa</h3><p class="small">Ginecologista e cirurgiã (CRM-MG 000000, fictícia), parceira nos procedimentos íntimos.</p></div>
    <div class="stack-4">{person("foto da equipe", sq=True)}<h3 class="h3-light">Equipe de estética</h3><p class="small">Profissionais treinadas pela Dra. Lívia.</p></div>
    <div class="stack-4">{person("foto da recepção", sq=True)}<h3 class="h3-light">Recepção</h3><p class="small">O cuidado começa aqui, desde o primeiro contato.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap stack-8">
  {statement_row("Um espaço pensado para o seu conforto.", line_link("Como chegar", "contato.html#mapa"))}
  <div class="cr-cards three">
    <div class="cr-pcard cr-photo" style="min-height:420px">{ph("intimo")}<h3 class="cr-pcard-title">Salas equipadas</h3><div class="cr-pcard-foot"><p class="cr-pcard-text">Aparelhos de alta tecnologia em ambiente climatizado.</p></div></div>
    <div class="cr-pcard cr-photo" style="min-height:420px">{ph("pisom")}<h3 class="cr-pcard-title">Procedimentos com cuidado</h3><div class="cr-pcard-foot"><p class="cr-pcard-text">Proteção, higiene e técnica em cada sessão.</p></div></div>
    <div class="cr-pcard cr-photo" style="min-height:420px">{ph("faq")}<h3 class="cr-pcard-title">Momento só seu</h3><div class="cr-pcard-foot"><p class="cr-pcard-text">Privacidade e acolhimento, com estacionamento próprio.</p></div></div>
  </div>
  <p class="small">Fotos ilustrativas. No site final entram as fotos reais da recepção, das salas e dos equipamentos.</p>
</div></section>
<section class="section"><div class="wrap stack-8">
  {statement_row("Saúde íntima sem tabu para mais mulheres.", "")}
  {features([("tv", "Em palestras", "Convidada de palestras e rodas de conversa sobre saúde da mulher."),
             ("mic", "Podcast", "Falou sobre prazer e saúde íntima feminina num trecho com mais de 1.700 comentários."),
             ("grad", "Cursos para profissionais", "Harmonização íntima, endolaser, glúteo, peelings e drenagem linfática."),
             ("insta", "Conteúdo educativo", "Dicas de saúde íntima e bem-estar nas redes da clínica.")])}
</div></section>
<section class="section"><div class="wrap stack-8">
  {statement_row("O carinho de quem já passou por aqui.", '<span class="cr-chip cr-chip-outline">★ 4,9 no Google</span>')}
  {quotes(REVIEWS[3:])}
</div></section>
{cta_final('Venha conhecer<br><em>a clínica.</em>', "Agende sua avaliação e conheça a Dra. Lívia, a equipe e o espaço.")}
'''
page("sobre.html", "A clínica e a Dra. Lívia Andrade · Clínica Lívia Andrade",
     "Conheça a Dra. Lívia Andrade Moura, fisioterapeuta e biomédica esteta, e a clínica fundada em 2014 em Belo Horizonte.", "sobre.html", sobre)

# ================================================================ DÚVIDAS
GROUPS = [
    ("geral", "Atendimento", [
        ("Preciso passar por avaliação antes?", "Sim. Antes de qualquer procedimento fazemos uma avaliação individual. Você também pode começar pela consulta online gratuita."),
        ("Como funciona a consulta online gratuita?", "É uma avaliação inicial personalizada pela internet: você tira dúvidas sem sair de casa, recebe um plano de tratamento e tem acompanhamento. As vagas são limitadas."),
        ("Meu atendimento é sigiloso?", "Sim, com total discrição, do primeiro contato até o acompanhamento."),
        ("Quem realiza os procedimentos?", "A Dra. Lívia Andrade (fisioterapeuta, biomédica esteta e ozonioterapeuta) e a equipe treinada por ela. Os procedimentos íntimos contam com a parceria da Dra. Marina Costa, ginecologista e cirurgiã."),
        ("Atendem homens?", "Sim: depilação a laser, botox, micropigmentação labial e harmonização íntima masculina."),
        ("Qual é o horário e onde fica a clínica?", 'Segunda a sexta, das 8h às 19h30, e sábado, das 8h às 12h. Rua das Acácias, 120, na Savassi, em Belo Horizonte (endereço fictício), com estacionamento próprio. <a href="contato.html#mapa">Ver mapa</a>.')]),
    ("pagamento", "Pagamento", [
        ("Aceitam convênio?", "Não atendemos convênio."),
        ("Quais são as formas de pagamento?", "PIX e cartão de crédito em até 12x. Temos pacotes de sessões e o plano mensal da Clube do Corpo."),
        ("Vocês divulgam os valores?", "Alguns valores de referência aparecem no site, como o PISOM a partir de R$ 120. Os demais são passados na avaliação, porque dependem do protocolo.")]),
    ("intima", "Saúde íntima", [
        ("Incontinência urinária tem tratamento?", 'Tem. Fisioterapia pélvica e laser íntimo são as principais opções. <a href="fisioterapia-pelvica.html">Saiba como funciona</a>.'),
        ("Os procedimentos íntimos têm acompanhamento médico?", "Sim, em parceria com a Dra. Marina Costa, ginecologista e cirurgiã (CRM-MG 000000, fictícia)."),
        ("Fisioterapia pélvica precisa ser chata?", "Não. Com o biofeedback MioLink, você faz os exercícios jogando e vê a sua evolução na tela."),
        ("Vaginismo tem tratamento?", "Sim. É uma disfunção pélvica tratável, com fisioterapia especializada e acolhimento. A Dra. Lívia tem formação específica em vaginismo.")]),
    ("rosto", "Rosto", [
        ("Qual a diferença entre botox e ácido hialurônico?", "O botox relaxa os músculos e suaviza as linhas de expressão. O ácido hialurônico preenche e devolve volume, como em lábios, olheiras e malar. Muitas vezes eles se complementam."),
        ("Colágeno (bioestimulador) ou preenchimento: qual é melhor para mim?", "O bioestimulador estimula o seu próprio colágeno e melhora a firmeza aos poucos. O preenchimento repõe volume na hora. A avaliação mostra o que o seu rosto precisa."),
        ("Botox aos 19 anos é necessário?", "Nem sempre. O botox preventivo é indicado de acordo com a sua expressão e a sua pele, não pela idade."),
        ("O resultado fica natural?", "Esse é o nosso compromisso: valorizar você sem exageros, respeitando a sua anatomia.")]),
    ("pisom", "Laser PISOM", [
        ("Quanto tempo leva?", "A aplicação dura cerca de 2 minutos. O atendimento todo, com avaliação e orientações, leva cerca de 20 minutos."),
        ("Dói?", "Depende da sensibilidade de cada pessoa, mas em geral é bem tolerado, com desconforto leve."),
        ("Pode fazer na região íntima?", "Sim, na região íntima externa, sempre com avaliação prévia."),
        ("Qualquer pessoa pode fazer?", "Sim, mas só depois de uma avaliação individual."),
        ("Tem horário amanhã?", 'O PISOM fica na clínica um dia por mês, com data divulgada antes. <a href="contato.html#agenda">Entre na lista de espera</a>.')]),
    ("depil", "Depilação a laser", [
        ("Posso fazer depilação a laser grávida?", "A recomendação é aguardar o fim da gestação. Converse com a gente para planejar o melhor momento."),
        ("Como são os pacotes?", "Pacotes de 10 sessões por região ou combinados, no PIX ou no cartão em até 12x.")]),
]
duv = f'''
{hero_page("<span>Dúvidas</span>", "Tudo o que você quer saber,<br><em>sem tabu</em>",
  "As perguntas que mais recebemos no WhatsApp e no Instagram. Ficou alguma dúvida? Chame a gente.", "fisio",
  f'<div class="hero-actions">{btn("Perguntar no WhatsApp", "hot", wa="")}</div><div class="chips"><span class="cr-chip">Resposta com sigilo</span></div>')}
<section class="section"><div class="wrap"><div class="faq-layout">
  <div class="faq-side">
    <h2 class="cr-statement" style="font-size:36px;line-height:40px">Dúvidas frequentes</h2>
    <p class="cr-subtitle">Escolha um assunto.</p>
    <nav class="side-links" aria-label="Assuntos">{"".join(f'<a href="#{g}">{t} {ARROW}</a>' for g, t, _ in GROUPS)}</nav>
  </div>
  <div class="faq-groups">{"".join(f'<section id="{g}"><h3 class="h2-light">{t}</h3>{faq_list(items, open_first=(k == 0))}</section>' for k, (g, t, items) in enumerate(GROUPS))}</div>
</div></div></section>
{cta_final('Ainda ficou<br><em>alguma dúvida?</em>', "Chame no WhatsApp. Respondemos com carinho, sigilo e sem julgamento.")}
'''
page("duvidas.html", "Dúvidas frequentes · Clínica Lívia Andrade",
     "Perguntas e respostas sobre avaliação, pagamento, saúde íntima, botox, preenchimento, PISOM e depilação a laser.", "", duv)

# ================================================================ CONTATO
cont = f'''
{hero_page("<span>Contato</span>", "Vamos conversar?<br><em>Estamos aqui</em>",
  "Agende sua avaliação, faça a consulta online gratuita ou entre na lista de espera dos dias especiais.", "cta",
  f'<div class="hero-actions">{btn("Agendar pelo WhatsApp", "hot", wa="")}{line_link("Como chegar", "#mapa", accent=True)}</div><div class="chips"><span class="cr-chip" data-status>Seg a sex 8h–19h30 · sáb 8h–12h</span></div>')}
<section class="section"><div class="wrap">
  <div class="contact">
    <div class="stack-8">
      <div class="stack-4"><span class="cr-label">Agende sua avaliação</span><h2 class="cr-statement">Mande seu pedido pelo WhatsApp.</h2>
      <p class="small" style="max-width:420px">Preencha e abrimos o WhatsApp com a mensagem pronta. Nada de dados de saúde aqui: isso fica para a avaliação.</p></div>
      <form class="form" data-wa-form="agendar" novalidate>
        <div class="row">
          <label class="cr-field"><span class="cr-label">Seu nome</span><input class="cr-input" name="nome" placeholder="Como podemos te chamar?" autocomplete="name" required></label>
          <label class="cr-field"><span class="cr-label">WhatsApp</span><input class="cr-input" name="whatsapp" inputmode="numeric" placeholder="(31) 9 0000-0000" autocomplete="tel" required><span class="cr-help fone-help">Com DDD.</span></label>
        </div>
        <div class="row">
          <label class="cr-field cr-select"><span class="cr-label">Tratamento de interesse</span><select class="cr-input" name="tratamento">
            <option>Laser Íntimo</option><option>Fisioterapia Pélvica</option><option>Harmonização Íntima</option><option>Botox</option><option>Preenchimento</option><option>Lasers</option><option>Clube do Corpo</option><option>Harmonização Glútea</option><option>Depilação a Laser</option><option>Ozonioterapia</option><option>Ainda não sei</option></select></label>
          <label class="cr-field cr-select"><span class="cr-label">Melhor horário</span><select class="cr-input" name="horario"><option>Manhã</option><option>Tarde</option><option>Fim da tarde (até 19h30)</option><option>Sábado de manhã</option></select></label>
        </div>
        <label class="cr-check" id="privacidade"><input type="checkbox" required checked> Autorizo o contato pelo WhatsApp. Usamos seus dados só para responder ao seu pedido.</label>
        <button class="cr-btn cr-btn-dark cr-btn-lg" type="submit">Enviar pelo WhatsApp {ARROW}</button>
      </form>
    </div>
    <div class="stack-6">
      <ul class="info">
        <li>{feat_icon("pin")}<div><strong>Endereço</strong><span>Rua das Acácias, 120 · Savassi · Belo Horizonte - MG (endereço fictício)</span></div></li>
        <li>{feat_icon("phone")}<div><strong>WhatsApp</strong><a href="#" data-wa="">(31) 9 0000-0000</a></div></li>
        <li>{feat_icon("car")}<div><strong>Estacionamento próprio</strong><span>Chegue com tranquilidade.</span></div></li>
        <li>{feat_icon("insta")}<div><strong>Instagram</strong><span>@clinica.liviaandrade (fictício)</span></div></li>
      </ul>
      <table class="hours"><tbody><tr><td>Segunda a sexta</td><td>08:00 – 19:30</td></tr><tr><td>Sábado</td><td>08:00 – 12:00</td></tr><tr><td>Domingo</td><td>Fechado</td></tr></tbody></table>
      <div class="chips"><span class="cr-chip cr-chip-outline">PIX ou cartão em até 12x</span><span class="cr-chip cr-chip-outline">Não atendemos convênio</span></div>
    </div>
  </div>
</div></section>
<section class="section" id="mapa"><div class="wrap stack-8">
  {statement_row("Como chegar.", line_link("Abrir no Google Maps", "https://www.google.com/maps/search/?api=1&query=Savassi%2C+Belo+Horizonte"))}
  <div class="map"><iframe title="Mapa: região da Savassi, Belo Horizonte" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Savassi%2C+Belo+Horizonte&output=embed"></iframe></div>
</div></section>
<section class="section" id="consulta-online"><div class="wrap"><div class="dark-frame cr-on-dark">
  <div class="about">
    <div class="stack-6">
      <span class="cr-label">Consulta online</span>
      <h2 class="cr-statement">Comece de casa, de graça.</h2>
      <p class="lead">O primeiro passo para quem quer entender o que tem, saber se o tratamento é para você ou mora longe de Belo Horizonte.</p>
      <ul class="ticks" style="border-top-color:#FFFFFF26">{"".join(f'<li style="border-bottom-color:#FFFFFF26">{i}</li>' for i in ["Avaliação inicial personalizada", "Tire suas dúvidas sem sair de casa", "Plano de tratamento exclusivo", "Acompanhamento do antes e depois"])}</ul>
      <div class="cta-actions">{btn("Quero minha consulta online", "pastel", wa="Consulta Online gratuita")}<span class="cr-chip cr-chip-promo">Vagas limitadas</span></div>
    </div>
    {retrato(chip="Consulta online")}
  </div>
</div></div></section>
<section class="section">{events_block()}</section>
'''
page("contato.html", "Contato, consulta online e agenda · Clínica Lívia Andrade",
     "Agende sua avaliação pelo WhatsApp (31) 9 0000-0000. Consulta online gratuita e lista de espera dos dias especiais. Savassi, Belo Horizonte.", "", cont)
