self.addEventListener("install", e => {
    e.waitUntil(
        caches.open("emma-cache").then(cache => {
            return cache.addAll([
                "/",
                "/static/style.css",
                "/static/app.js"
            ]);
        })
    );
});

self.addEventListener("fetch", e => {
    e.respondWith(
        caches.match(e.request).then(resp => resp || fetch(e.request))
    );
});
