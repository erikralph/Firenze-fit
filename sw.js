// Firenze Fit – service worker. Ao alterar o index.html, suba a versão V.
const V = 'ff-v2.1.0';
const SHELL = ['./', 'index.html', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(SHELL))); self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V && k !== 'ff-img').map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET') return;
  const img = u.hostname === 'cdn.jsdelivr.net' || u.pathname.includes('/fotos/');
  if (img) {   // fotos: cache permanente
    e.respondWith(caches.open('ff-img').then(c => c.match(e.request).then(hit => hit || fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; }))));
    return;
  }
  if (u.pathname.includes('/data/')) {   // treinos: rede primeiro (mês novo), cache se offline
    e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); return r; })
      .catch(() => caches.match(e.request, {ignoreSearch: true})));
    return;
  }
  if (u.origin === location.origin) {   // app: cache primeiro, atualiza em segundo plano
    e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(hit => {
      const net = fetch(e.request).then(r => { if (r.ok) { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); } return r; }).catch(() => hit);
      return hit || net;
    }));
  }
});
