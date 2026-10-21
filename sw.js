// Service worker for Ordbua som app: gjør at spillet åpner uten nett etter at det er åpnet én gang med nett.
// Spillet hentes alltid fra nettet først, så elevene får nyeste utgave. Den lagrede kopien brukes når nettet er borte
// eller treigere enn GRENSE_MS. Endre VERSJON når ikonene eller lista under endres, så de lagres på nytt.
const VERSJON = "ordbua-1";
const SKRIFT = "ordbua-skrift"; // Google-skriftene, som hentes én gang og beholdes på tvers av versjoner
const SKRIFTVERTER = ["fonts.googleapis.com", "fonts.gstatic.com"];
const GRENSE_MS = 3000;
const FILER = [
  "./",
  "spill/ordbua.html",
  "manifest.webmanifest",
  "ikon/ordbua-192.png",
  "ikon/ordbua-512.png",
  "ikon/ordbua-maskable-192.png",
  "ikon/ordbua-maskable-512.png",
  "ikon/apple-touch-icon.png"
];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(VERSJON)
    .then((c) => c.addAll(FILER.map((f) => new Request(f, { cache: "reload" }))))
    .then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  // Alle GitHub Pages-sidene på kontoen deler ett lager i nettleseren, så bare Ordbuas egne gamle lagre (ordbua-…) slettes.
  // En annen app på kontoen må ha sitt eget navneprefiks og bare slette sine egne.
  e.waitUntil(caches.keys()
    .then((navn) => Promise.all(navn.filter((n) => n.startsWith("ordbua-") && n !== VERSJON && n !== SKRIFT).map((n) => caches.delete(n))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin === location.origin) {
    // Sider lagres uten ?-delen av adressen (for eksempel ?fbclid fra Facebook), så det bare finnes én kopi, og den er den nyeste
    const nokkel = req.mode === "navigate" ? url.origin + url.pathname : req;
    // no-cache spør serveren om fila er endret. En navigering kan ikke kopieres med nye innstillinger, så den hentes fra adressen.
    const nett = fetch(req.mode === "navigate" ? new Request(req.url, { cache: "no-cache", redirect: "manual" }) : new Request(req, { cache: "no-cache" }));
    // Kopien tas før svaret går videre til siden, ellers er innholdet allerede lest
    const kopi = nett.then((s) => (s.ok && !s.redirected ? s.clone() : null), () => null);
    e.waitUntil(kopi.then((k) => k && caches.open(VERSJON).then((c) => c.put(nokkel, k))).catch(() => {}));
    e.respondWith(nettEllerLagret(req, nokkel, nett));
  } else if (SKRIFTVERTER.includes(url.hostname)) {
    e.respondWith(lagretEllerNett(req, e));
  }
});

async function nettEllerLagret(req, nokkel, nett) {
  const forSeint = new Promise((ok) => setTimeout(ok, GRENSE_MS, "forSeint"));
  let svar = null;
  try {
    svar = await Promise.race([nett, forSeint]);
    // Et feilsvar fra serveren (for eksempel 503 når GitHub Pages har driftsproblemer) behandles som manglende nett
    if (svar !== "forSeint" && (svar.ok || svar.type === "opaqueredirect")) return svar;
  } catch {}
  return (await caches.match(nokkel)) || (await caches.match(req, { ignoreSearch: true })) || (svar && svar !== "forSeint" ? svar : nett);
}

async function lagretEllerNett(req, e) {
  const c = await caches.open(SKRIFT);
  const lagret = await c.match(req, { ignoreVary: true });
  if (lagret) return lagret;
  const svar = await fetch(req);
  if (svar.ok || svar.type === "opaque") e.waitUntil(c.put(req, svar.clone()).catch(() => {}));
  return svar;
}

// Siden sender adressen til stilarket for skriftene, som ble lastet før denne filen tok over. Stilarket og skriftfilene
// for latinske bokstaver (der æ, ø og å er med) lagres, så skriftene også finnes uten nett.
self.addEventListener("message", (e) => {
  const ark = (e.data && Array.isArray(e.data.skrift) ? e.data.skrift : []).filter((u) => {
    try { return new URL(u).hostname === "fonts.googleapis.com"; } catch { return false; }
  });
  e.waitUntil(caches.open(SKRIFT).then((c) => Promise.all(ark.map(async (u) => {
    try {
      const svar = await fetch(u);
      if (!svar.ok) return;
      const css = await svar.clone().text();
      await c.put(u, svar);
      let filer = [...css.matchAll(/\/\*\s*latin(?:-ext)?\s*\*\/\s*@font-face\s*{[^}]*?url\((https:\/\/fonts\.gstatic\.com\/[^)\s]+)\)/g)].map((m) => m[1]);
      if (!filer.length) filer = [...css.matchAll(/url\((https:\/\/fonts\.gstatic\.com\/[^)\s]+)\)/g)].map((m) => m[1]);
      await Promise.all([...new Set(filer)].map((f) => c.match(f, { ignoreVary: true })
        .then((har) => har || fetch(f).then((s) => s.ok && c.put(f, s))).catch(() => {})));
    } catch {}
  }))));
});
