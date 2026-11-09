const CACHE_NAME = 'space-suite-v2';
const ASSETS = ['index.html', 'style.css', 'Habitability.html']
  .map((asset) => new URL(asset, self.registration.scope).href);

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys
        .filter((key) => key.startsWith('space-suite-') && key !== CACHE_NAME)
        .map((key) => caches.delete(key))
    ))
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});