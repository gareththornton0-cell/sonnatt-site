/* Sonnatt.ai website assistant: the chatbot clients add to their own website with one line.
 *
 *   <script src="https://sonnattai.com/widget.js" data-sonnatt-widget="CLIENT-ID" async></script>
 *
 * CLIENT-ID is the client's row in the chat_widgets table (Supabase). That row holds the business name,
 * greeting, colour, booking link and the question-and-answer list the assistant answers from.
 * Answers are matched by keywords, not generated, so it only ever says what the client approved.
 * When a visitor leaves their details the lead is saved to website_leads (form "widget-lead"),
 * and the lead-alert function emails it to the client's alert address.
 * Everything renders inside a shadow root, so the client's own styles can't break it and it can't break theirs.
 */
(function(){
  'use strict';
  var me = document.currentScript || document.querySelector('script[data-sonnatt-widget]');
  if(!me || window.__sonnattWidget) return;
  var ID = (me.getAttribute('data-sonnatt-widget') || '').trim().toLowerCase();
  if(!/^[a-z0-9][a-z0-9-]{2,40}$/.test(ID)) return;
  window.__sonnattWidget = true;

  var SB_URL = 'https://hwhzjpnzsajsgrsaxvqo.supabase.co', SB_KEY = 'sb_publishable_udJhvp-StezoCvk-RfdsAA_nOgQiVcU';
  var HEAD = {'apikey': SB_KEY, 'Content-Type': 'application/json'};
  var EMAIL_RE = /[^\s@<>()]+@[^\s@<>()]+\.[a-z]{2,}/i, PHONE_RE = /(\+?\d[\d\s()-]{8,}\d)/;

  function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
  function words(s){ return String(s).toLowerCase().replace(/[^a-z0-9£'\s]/g, ' ').split(/\s+/).filter(Boolean); }

  fetch(SB_URL + '/rest/v1/chat_widgets?id=eq.' + encodeURIComponent(ID) + '&select=id,business,greeting,accent,faqs,booking_url', {headers: HEAD})
    .then(function(r){ return r.ok ? r.json() : []; })
    .then(function(rows){ if(rows && rows[0]) start(rows[0]); })
    .catch(function(){});

  function start(cfg){
    var accent = /^#[0-9a-f]{6}$/i.test(cfg.accent || '') ? cfg.accent : '#0095F7';
    var faqs = Array.isArray(cfg.faqs) ? cfg.faqs.filter(function(f){ return f && f.q && f.a; }).slice(0, 60) : [];
    var S = {name:'', email:'', phone:'', message:'', step:null, sent:false, transcript:[], opened:false};

    var host = document.createElement('div');
    host.setAttribute('data-sonnatt-widget-host', '');
    host.style.cssText = 'position:fixed;right:0;bottom:0;z-index:2147482000;';
    var root = host.attachShadow ? host.attachShadow({mode:'open'}) : host;
    root.innerHTML =
      '<style>' +
      ':host{all:initial}' +
      '*{box-sizing:border-box;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}' +
      '.launch{position:fixed;right:20px;bottom:20px;width:60px;height:60px;border-radius:50%;border:0;cursor:pointer;background:' + accent + ';color:#fff;box-shadow:0 10px 30px rgba(0,0,0,.25);display:grid;place-items:center}' +
      '.launch svg{width:28px;height:28px}' +
      '.panel{position:fixed;right:20px;bottom:92px;width:min(370px,calc(100vw - 24px));height:min(560px,calc(100vh - 120px));background:#fff;color:#14181f;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.28);display:none;flex-direction:column;overflow:hidden;font-size:15px;line-height:1.45}' +
      '.panel.open{display:flex}' +
      '.top{background:' + accent + ';color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px}' +
      '.top b{font-size:16px}.top small{display:block;opacity:.85;font-size:12px}' +
      '.x{background:transparent;border:0;color:#fff;font-size:24px;line-height:1;cursor:pointer;width:44px;height:44px;margin:-10px -10px -10px 0}' +
      '.log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:8px;background:#f5f7fa}' +
      '.m{max-width:86%;padding:9px 12px;border-radius:14px;white-space:pre-wrap;word-wrap:break-word}' +
      '.bot{background:#fff;border:1px solid #e3e7ed;align-self:flex-start;border-bottom-left-radius:4px}' +
      '.you{background:' + accent + ';color:#fff;align-self:flex-end;border-bottom-right-radius:4px}' +
      '.chips{display:flex;flex-wrap:wrap;gap:6px;padding:8px 14px;background:#f5f7fa;border-top:1px solid #e9edf2}' +
      '.chip{border:1px solid ' + accent + ';color:' + accent + ';background:#fff;border-radius:999px;padding:7px 12px;font-size:13px;cursor:pointer;min-height:34px}' +
      'a.chip{text-decoration:none;display:inline-flex;align-items:center}' +
      'form{display:flex;gap:8px;padding:10px;border-top:1px solid #e9edf2;background:#fff}' +
      'input{flex:1;min-width:0;border:1px solid #cfd6df;border-radius:10px;padding:10px 12px;font-size:16px;color:#14181f;background:#fff}' +
      'input:focus{outline:2px solid ' + accent + ';outline-offset:0;border-color:transparent}' +
      '.send{border:0;border-radius:10px;background:' + accent + ';color:#fff;padding:0 16px;font-weight:600;cursor:pointer;min-height:44px}' +
      '.foot{font-size:11px;text-align:center;color:#8a94a3;padding:0 0 8px;background:#fff}.foot a{color:#8a94a3}' +
      ':focus-visible{outline:2px solid ' + accent + ';outline-offset:2px}' +
      '@media (max-width:480px){.panel{right:12px;bottom:84px}.launch{right:12px;bottom:12px}}' +
      '</style>' +
      '<button class="launch" type="button" aria-label="Chat with ' + esc(cfg.business) + '" aria-expanded="false">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-8l-5 4v-4H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/></svg></button>' +
      '<div class="panel" role="dialog" aria-label="Chat with ' + esc(cfg.business) + '">' +
        '<div class="top"><div><b>' + esc(cfg.business) + '</b><small>Usually replies instantly</small></div><button class="x" type="button" aria-label="Close chat">×</button></div>' +
        '<div class="log" aria-live="polite"></div>' +
        '<div class="chips"></div>' +
        '<form><input type="text" autocomplete="off" aria-label="Type your message" placeholder="Type your question…" maxlength="1000"><button class="send" type="submit">Send</button></form>' +
        '<div class="foot">Assistant by <a href="https://sonnattai.com/website-chatbot/?ref=' + encodeURIComponent(ID) + '" target="_blank" rel="noopener">Sonnatt.ai</a></div>' +
      '</div>';
    document.body.appendChild(host);

    var q = function(sel){ return root.querySelector(sel); };
    var launch = q('.launch'), panel = q('.panel'), log = q('.log'), chipsEl = q('.chips'), form = q('form'), input = q('input');

    function say(text, who){
      var d = document.createElement('div');
      d.className = 'm ' + (who || 'bot');
      d.textContent = text;
      log.appendChild(d);
      log.scrollTop = log.scrollHeight;
      S.transcript.push((who === 'you' ? 'Visitor: ' : 'Assistant: ') + text);
    }
    function chips(list){
      chipsEl.innerHTML = '';
      list.forEach(function(c){
        var el;
        if(c.href){ el = document.createElement('a'); el.href = c.href; el.target = '_blank'; el.rel = 'noopener'; }
        else { el = document.createElement('button'); el.type = 'button'; el.addEventListener('click', function(){ handle(c.label); }); }
        el.className = 'chip'; el.textContent = c.label;
        chipsEl.appendChild(el);
      });
      chipsEl.style.display = list.length ? '' : 'none';
      log.scrollTop = log.scrollHeight;
    }
    var CONTACT = 'Leave my details';
    function menu(){
      var list = faqs.slice(0, 4).map(function(f){ return {label: f.q}; });
      if(cfg.booking_url && /^https:\/\//.test(cfg.booking_url)) list.push({label: 'Book online', href: cfg.booking_url});
      if(!S.sent) list.push({label: CONTACT});
      chips(list);
    }

    function best(text){
      var t = ' ' + words(text).join(' ') + ' ', top = null, topScore = 0;
      faqs.forEach(function(f){
        if(text.trim().toLowerCase() === String(f.q).toLowerCase()){ top = f; topScore = 99; return; }
        var score = 0;
        (Array.isArray(f.keys) ? f.keys : []).concat(words(f.q).filter(function(w){ return w.length > 3; })).forEach(function(k){
          k = String(k).toLowerCase().trim();
          if(k && t.indexOf(' ' + k + ' ') !== -1) score += k.indexOf(' ') !== -1 ? 2 : 1;
          else if(k.length > 4 && t.indexOf(k) !== -1) score += 0.5;
        });
        if(score > topScore){ topScore = score; top = f; }
      });
      return topScore >= 1 ? top : null;
    }

    function save(){
      S.sent = true;
      var row = {form_name: 'widget-lead', widget_id: ID, status: 'new', page: String(location.href).slice(0, 500),
        name: S.name.slice(0, 200), message: S.message.slice(0, 5000), transcript: S.transcript.join('\n').slice(-20000),
        interest: ('Chat on ' + cfg.business).slice(0, 500)};
      if(S.email) row.email = S.email.slice(0, 320);
      if(S.phone) row.phone = S.phone.slice(0, 60);
      return fetch(SB_URL + '/rest/v1/website_leads', {method: 'POST', headers: {'apikey': SB_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal'}, body: JSON.stringify(row)})
        .then(function(r){ return r.ok; }).catch(function(){ return false; });
    }

    function handle(raw){
      var text = String(raw || '').trim();
      if(!text) return;
      say(text, 'you');
      if(S.step === 'name'){
        S.name = text.replace(/^(my name is|i'm|i am|it's|its)\s+/i, '').slice(0, 80);
        S.step = 'contact';
        say('Thanks ' + S.name.split(' ')[0] + '. What\'s the best email or phone number to reach you on?');
        chips([]); return;
      }
      if(S.step === 'contact'){
        var em = text.match(EMAIL_RE), ph = text.match(PHONE_RE);
        if(!em && !ph){ say('That doesn\'t look like an email or phone number. Could you check it?'); return; }
        S.email = em ? em[0] : ''; S.phone = ph ? ph[1] : '';
        S.step = 'message';
        say('And what can we help you with?');
        return;
      }
      if(S.step === 'message'){
        S.message = text; S.step = null;
        say('Sending that to the team…');
        save().then(function(ok){
          say(ok ? 'Done. ' + cfg.business + ' has your details and will be in touch soon.' :
            'Sorry, that didn\'t send. Please try again in a moment.');
          if(!ok) S.sent = false;
          menu();
        });
        return;
      }
      if(text === CONTACT || /\b(call me|contact me|get in touch|speak to|talk to|human|person|someone)\b/i.test(text)){
        if(S.sent){ say('We already have your details, so the team will be in touch.'); return; }
        S.step = 'name';
        say('Of course. What\'s your name?');
        chips([]); return;
      }
      var hit = best(text);
      if(hit){ say(hit.a); if(!S.message) S.message = text; menu(); return; }
      if(!S.message) S.message = text;
      say('I\'m not sure about that one, but the team can help. Would you like to leave your details so they can get back to you?');
      chips([{label: CONTACT}].concat(faqs.slice(0, 3).map(function(f){ return {label: f.q}; })));
    }

    function open(){
      panel.classList.add('open'); launch.setAttribute('aria-expanded', 'true');
      if(!S.opened){ S.opened = true; say(cfg.greeting || ('Hi! How can ' + cfg.business + ' help today?')); menu(); }
      setTimeout(function(){ input.focus(); }, 50);
    }
    function close(){ panel.classList.remove('open'); launch.setAttribute('aria-expanded', 'false'); launch.focus(); }
    launch.addEventListener('click', function(){ panel.classList.contains('open') ? close() : open(); });
    q('.x').addEventListener('click', close);
    root.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
    form.addEventListener('submit', function(e){ e.preventDefault(); var v = input.value; input.value = ''; handle(v); });
    window.SonnattWidget = {open: open, close: close};
  }
})();
