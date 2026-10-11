/* Shared behaviour for Sonnatt.ai inner pages: menu, booking links, cookie choices. */
(function(){
  var nav = document.querySelector('.nav'), t = document.getElementById('navToggle'), m = document.getElementById('mnav');
  if(nav && t && m){
    var set = function(open){ nav.classList.toggle('open', open); t.setAttribute('aria-expanded', open ? 'true' : 'false'); t.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); };
    t.addEventListener('click', function(){ set(!nav.classList.contains('open')); });
    m.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ set(false); }); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') set(false); });
    document.addEventListener('click', function(e){ if(nav.classList.contains('open') && !nav.contains(e.target)) set(false); });
  }
  // Booking: when a Google Calendar booking link is set in the page's meta tag, "Book" buttons open it.
  var url = (document.querySelector('meta[name=sonnatt-booking]') || {}).content || '';
  document.querySelectorAll('a[data-book]').forEach(function(a){
    if(url){ a.href = url; a.target = '_blank'; a.rel = 'noopener'; }
    a.addEventListener('click', function(){ try{ gtag('event', url ? 'booking_click' : 'contact_click', { page_path: location.pathname }); }catch(e){} });
  });
  // Enquiry form: saved to the website_leads table, which emails the team. Same fields as the homepage form.
  var lf = document.getElementById('lf');
  if(lf){
    var note = document.getElementById('lnote'), btn = lf.querySelector('button[type="submit"]');
    var LIVE = /(^|\.)sonnattai\.com$|\.github\.io$/i.test(location.hostname);
    var SB_URL = 'https://hwhzjpnzsajsgrsaxvqo.supabase.co', SB_KEY = 'sb_publishable_udJhvp-StezoCvk-RfdsAA_nOgQiVcU';
    lf.addEventListener('submit', function(ev){
      ev.preventDefault();
      var req = ['l-name','l-biz','l-email'].map(function(id){ return document.getElementById(id); });
      var miss = req.filter(function(el){ return !el.value.trim(); })[0];
      if(miss){ note.textContent = 'Add your name, business and email so we can reply.'; miss.focus(); return; }
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(req[2].value.trim())){ note.textContent = 'That email address doesn’t look right. Check it and try again.'; req[2].focus(); return; }
      var d = {}; new FormData(lf).forEach(function(v, k){ d[k] = v; });
      if(d['bot-field']){ lf.reset(); note.textContent = 'Thanks, that’s with the team.'; return; }
      if(!LIVE){ note.textContent = 'This is a preview, so nothing was sent.'; return; }
      var row = { form_name: 'contact-request', page: location.href, interest: lf.getAttribute('data-interest') || '' };
      ['name','business','email','phone','message'].forEach(function(k){ if(d[k] && String(d[k]).trim()) row[k] = String(d[k]).slice(0, k === 'message' ? 5000 : 320); });
      btn.disabled = true; note.textContent = 'Sending…';
      fetch(SB_URL + '/rest/v1/website_leads', { method: 'POST', headers: { 'Content-Type': 'application/json', 'apikey': SB_KEY, 'Prefer': 'return=minimal' }, body: JSON.stringify(row) })
        .then(function(r){
          if(!r.ok) throw 0;
          lf.reset(); note.textContent = 'Thanks, that’s with the team. We’ll reply within one working day.';
          try{ gtag('event', 'generate_lead', { form: 'inner_page', page_path: location.pathname }); }catch(e){}
        })
        .catch(function(){ note.textContent = 'Sorry, that didn’t send. Please try again or email info@sonnattai.com.'; })
        .then(function(){ btn.disabled = false; });
    });
  }
  // Online signup for the self-serve plans (form id "sf"). The details are saved to website_leads as a
  // "plan-signup" lead first, so the team always has them. If a payment link for the chosen plan is set in
  // a <meta name="sonnatt-pay-PLAN"> tag (a Stripe Payment Link), the visitor then goes straight to pay;
  // until one is set, the team emails a payment link instead.
  var sf = document.getElementById('sf');
  if(sf){
    var snote = document.getElementById('snote'), sbtn = sf.querySelector('button[type="submit"]'), plan = document.getElementById('s-plan');
    var PLANS = { chat: 'Chatbot plan (£99 setup + £49/month)', starter: 'Starter plan (£299 setup + £149/month)', core: 'Core plan (£995 setup + £995/month)' };
    var want = (location.search.match(/[?&]plan=([a-z]+)/) || [])[1];
    if(plan && want && PLANS[want]) plan.value = want;
    document.querySelectorAll('a[data-plan]').forEach(function(a){
      a.addEventListener('click', function(){ if(plan && PLANS[a.getAttribute('data-plan')]) plan.value = a.getAttribute('data-plan'); });
    });
    var SLIVE = /(^|\.)sonnattai\.com$|\.github\.io$/i.test(location.hostname);
    var SURL = 'https://hwhzjpnzsajsgrsaxvqo.supabase.co', SKEY = 'sb_publishable_udJhvp-StezoCvk-RfdsAA_nOgQiVcU';
    sf.addEventListener('submit', function(ev){
      ev.preventDefault();
      var req = ['s-name','s-biz','s-email'].map(function(id){ return document.getElementById(id); });
      var miss = req.filter(function(el){ return !el.value.trim(); })[0];
      if(miss){ snote.textContent = 'Add your name, business and email to get started.'; miss.focus(); return; }
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(req[2].value.trim())){ snote.textContent = 'That email address doesn’t look right. Check it and try again.'; req[2].focus(); return; }
      var d = {}; new FormData(sf).forEach(function(v, k){ d[k] = v; });
      if(d['bot-field']){ sf.reset(); snote.textContent = 'Thanks, you’re signed up.'; return; }
      var key = PLANS[d.plan] ? d.plan : 'chat';
      if(!SLIVE){ snote.textContent = 'This is a preview, so nothing was sent.'; return; }
      var row = { form_name: 'plan-signup', page: location.href.slice(0, 500), interest: PLANS[key] };
      ['name','business','email','phone'].forEach(function(k){ if(d[k] && String(d[k]).trim()) row[k] = String(d[k]).trim().slice(0, 320); });
      var msg = [d.website ? 'Website: ' + d.website : '', d.message || ''].filter(Boolean).join('\n');
      if(msg) row.message = msg.slice(0, 5000);
      sbtn.disabled = true; snote.textContent = 'Saving…';
      fetch(SURL + '/rest/v1/website_leads', { method: 'POST', headers: { 'Content-Type': 'application/json', 'apikey': SKEY, 'Prefer': 'return=minimal' }, body: JSON.stringify(row) })
        .then(function(r){
          if(!r.ok) throw 0;
          try{ gtag('event', 'sign_up', { method: key, page_path: location.pathname }); }catch(e){}
          var pay = (document.querySelector('meta[name="sonnatt-pay-' + key + '"]') || {}).content || '';
          if(/^https:\/\/(buy\.stripe\.com|checkout\.stripe\.com)\//.test(pay)){
            snote.textContent = 'Taking you to secure payment…';
            location.href = pay + (pay.indexOf('?') === -1 ? '?' : '&') + 'prefilled_email=' + encodeURIComponent(row.email);
            return;
          }
          sf.reset(); if(plan) plan.value = key;
          snote.textContent = 'You’re signed up. We’ll email your secure payment link and next steps within one working day.';
        })
        .catch(function(){ snote.textContent = 'Sorry, that didn’t send. Please try again or email info@sonnattai.com.'; })
        .then(function(){ sbtn.disabled = false; });
    });
  }
  // Cookie choices (Google Analytics only runs after Accept).
  var KEY = 'sonnatt_cookie_consent', b = document.getElementById('ckBanner');
  if(b){
    var choose = function(v){ try{ localStorage.setItem(KEY, v); }catch(e){} b.hidden = true; try{ gtag('consent', 'update', { analytics_storage: v === 'granted' ? 'granted' : 'denied' }); }catch(e){} };
    var saved = null; try{ saved = localStorage.getItem(KEY); }catch(e){}
    if(!saved) b.hidden = false;
    document.getElementById('ckYes').addEventListener('click', function(){ choose('granted'); });
    document.getElementById('ckNo').addEventListener('click', function(){ choose('denied'); });
    document.querySelectorAll('[data-cookie-settings]').forEach(function(a){ a.addEventListener('click', function(e){ e.preventDefault(); b.hidden = false; }); });
  }
})();
