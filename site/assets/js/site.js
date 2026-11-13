// Clínica Lívia Andrade (modelo demonstrativo da Codetrax) — comportamento do site
(function () {
  // Site de demonstração: todo WhatsApp vai para a Codetrax, nunca para um número fictício
  // que poderia ser de uma pessoa real. O contexto do botão segue junto na mensagem.
  var WHATS = "5511947771128";
  function waLink(msg) {
    var texto = "Olá, Codetrax! Vi o modelo de site de clínica estética no portfólio e quero um site assim." +
      (msg ? "

(Botão que testei: " + msg + ")" : "");
    return "https://wa.me/" + WHATS + "?text=" + encodeURIComponent(texto);
  }

  // Links de WhatsApp com mensagem pronta: data-wa="Laser Íntimo"
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var t = el.getAttribute("data-wa");
    var msg = t ? "Olá! Vi no site e quero agendar uma avaliação de *" + t + "*." : "Olá! Vi no site e quero agendar uma avaliação.";
    el.setAttribute("href", waLink(msg));
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener noreferrer");
  });

  // Menu fixo: transparente sobre o hero, grafite depois dele
  var header = document.querySelector(".site-header");
  var hero = document.querySelector(".cr-hero");
  function onScroll() {
    if (!header) return;
    var limit = hero ? hero.offsetTop + hero.offsetHeight - header.offsetHeight - 24 : 40;
    header.classList.toggle("is-solid", window.scrollY > limit);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Menu do celular
  var toggle = document.querySelector(".nav-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    });
    header.querySelectorAll(".mobile-menu a").forEach(function (a) {
      a.addEventListener("click", function () { header.classList.remove("is-open"); toggle.setAttribute("aria-expanded", "false"); });
    });
  }

  // Chip de status no horário de Brasília (UTC-3): seg–sex 08:00–19:30 · sáb 08:00–12:00
  var status = document.querySelectorAll("[data-status]");
  if (status.length) {
    var now = new Date(Date.now() - 3 * 3600 * 1000);
    var d = now.getUTCDay(), m = now.getUTCHours() * 60 + now.getUTCMinutes();
    var open = (d >= 1 && d <= 5 && m >= 480 && m < 1170) || (d === 6 && m >= 480 && m < 720);
    status.forEach(function (el) {
      if (open) {
        el.classList.add("cr-chip-open");
        el.textContent = d === 6 ? "Atendendo agora · até 12h" : "Atendendo agora · até 19h30";
      } else {
        el.textContent = (d === 6 && m >= 720) || d === 0 ? "Abre segunda às 8h" : (m < 480 ? "Abre hoje às 8h" : "Abre amanhã às 8h");
      }
    });
  }

  // Roda de etapas: ‹ › troca a etapa ativa
  var wheel = document.querySelector("[data-wheel]");
  if (wheel) {
    var steps = JSON.parse(wheel.getAttribute("data-steps"));
    var quads = ["M280 200 L280 50 A150 150 0 0 1 430 200 Z", "M280 200 L430 200 A150 150 0 0 1 280 350 Z", "M280 200 L280 350 A150 150 0 0 1 130 200 Z", "M280 200 L130 200 A150 150 0 0 1 280 50 Z"];
    // ordem visual: 01 sup. esquerdo, 02 sup. direito, 03 inf. direito, 04 inf. esquerdo
    var quadFor = [3, 0, 1, 2];
    var cur = 0;
    var cap = document.querySelector(".wheel-caption");
    function show(i) {
      cur = (i + 4) % 4;
      wheel.querySelector(".q-on").setAttribute("d", quads[quadFor[cur]]);
      wheel.querySelectorAll("[data-step]").forEach(function (el) {
        el.classList.toggle(el.getAttribute("data-on"), +el.getAttribute("data-step") === cur);
      });
      if (cap) cap.textContent = "Passo " + (cur + 1) + " de 4 · " + steps[cur];
      document.querySelectorAll(".steps-list li").forEach(function (li, k) { li.classList.toggle("on", k === cur); });
    }
    document.querySelectorAll("[data-wheel-go]").forEach(function (b) {
      b.addEventListener("click", function () { show(cur + (+b.getAttribute("data-wheel-go"))); });
    });
    show(0);
  }

  // Formulários que viram mensagem de WhatsApp
  document.querySelectorAll("form[data-wa-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fone = form.querySelector("[name=whatsapp]");
      var digits = (fone && fone.value || "").replace(/\D/g, "");
      var help = form.querySelector(".fone-help");
      if (fone && digits.length < 10) {
        fone.setAttribute("aria-invalid", "true");
        if (help) { help.textContent = "Faltam dígitos: use DDD + número."; help.classList.add("cr-help-error"); }
        fone.focus();
        return;
      }
      if (fone) fone.removeAttribute("aria-invalid");
      if (help) { help.classList.remove("cr-help-error"); help.textContent = "Com DDD."; }
      var data = new FormData(form);
      var tipo = form.getAttribute("data-wa-form");
      var msg;
      if (tipo === "espera") msg = "Olá! Quero entrar na lista de espera do *" + (data.get("evento") || "próximo dia especial") + "*.";
      else if (tipo === "novidades") msg = "Olá! Quero receber as novidades e os dias especiais da clínica.";
      else msg = "Olá! Meu nome é " + (data.get("nome") || "") + ". Vi no site e quero agendar uma avaliação de *" + (data.get("tratamento") || "") + "*." + (data.get("horario") ? " Melhor horário: " + data.get("horario") + "." : "");
      window.open(waLink(msg), "_blank", "noopener,noreferrer");
    });
  });

  // Botão fixo do celular some quando outro "Agendar avaliação" já está na tela (no máximo um por tela)
  var bar = document.querySelector(".mobile-cta");
  if (bar && "IntersectionObserver" in window) {
    var visible = new Set();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) visible.add(en.target); else visible.delete(en.target); });
      bar.classList.toggle("is-hidden", visible.size > 0);
    });
    document.querySelectorAll("main .cr-btn-hot").forEach(function (b) { io.observe(b); });
  }

  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
