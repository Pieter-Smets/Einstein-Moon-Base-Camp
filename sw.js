const CACHE_NAME = 'space-suite-v1';
const ASSETS = [
  '/',
  'index.html',
  'style.css'
];

// Install the service worker and cache basic layouts
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

// Serve assets from cache or grab via network
self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});