// MovaCondo – service worker. Ao alterar o index.html, suba a versão V.
const V = 'mc-v3.0.0';
const SHELL = ['./', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(SHELL)).catch(() => {})); self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V && k !== 'ff-img').map(k => caches.delete(k))))); self.clients.claim(); });
const clean = r => r.redirected ? r.blob().then(b => new Response(b, {status: 200, headers: r.headers})) : r;
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.pathname.startsWith('/api/')) return;
  if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).then(clean).then(r => { if (r.ok && u.pathname === '/') { const c = r.clone(); caches.open(V).then(x => x.put('./', c)); } return r; })
      .catch(() => caches.match(u.pathname === '/' ? './' : e.request, {ignoreSearch: true}).then(h => h || caches.match('./'))));
    return;
  }
  if (u.hostname === 'cdn.jsdelivr.net' || u.pathname.includes('/fotos/')) {
    e.respondWith(caches.open('ff-img').then(c => c.match(e.request).then(hit => hit || fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; }))));
    return;
  }
  if (u.origin === location.origin) {
    e.respondWith(fetch(e.request).then(r => { if (r.ok) { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); } return r; })
      .catch(() => caches.match(e.request, {ignoreSearch: true})));
  }
});
