const CACHE_SHELL = "upanishad-shell-v13";
const CACHE_DATA = "upanishad-data-v4";

const SHELL_FILES = [
  "./",
  "./index.html",
  "./manifest.json",
  "./content/catalog.json"
];

self.addEventListener("install", event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_SHELL).then(cache => cache.addAll(SHELL_FILES))
  );
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key !== CACHE_SHELL && key !== CACHE_DATA)
          .map(key => caches.delete(key))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);

  if (url.pathname.includes('/content/') && url.pathname.endsWith('.json')) {
    event.respondWith(
      caches.open(CACHE_DATA).then(cache =>
        cache.match(event.request).then(cached => {
          if (cached) return cached;
          return fetch(event.request).then(response => {
            if (response.ok) cache.put(event.request, response.clone());
            return response;
          });
        })
      )
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});
