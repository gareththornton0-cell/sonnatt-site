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
