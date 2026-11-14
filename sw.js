// Rumble Party service worker: keeps the game playable offline once it has been opened online.
// The page itself is fetched fresh when there is a connection, so pushed updates arrive on the next launch.
const CACHE='rumble-party-v12';
const CORE=['./','index.html','manifest.webmanifest','icon-192.png','models.json','char-0.json','char-1.json','char-2.json','char-3.json','char-4.json','char-5.json','music-board.mp3','music-mini1.mp3','music-mini2.mp3','music-mini3.mp3','music-lobby.wav',
  'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js','https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js','https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/utils/SkeletonUtils.js'];
self.addEventListener('install',e=>{self.skipWaiting(); e.waitUntil(caches.open(CACHE).then(c=>Promise.all(CORE.map(u=>c.add(u).catch(()=>{})))));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
const keep=(req,res)=>{if(res&&(res.ok||res.type==='opaque')){const cp=res.clone(); caches.open(CACHE).then(c=>c.put(req,cp)).catch(()=>{});} return res;};
self.addEventListener('fetch',e=>{
  const req=e.request; if(req.method!=='GET')return; const url=new URL(req.url), same=url.origin===location.origin, page=req.mode==='navigate'||url.pathname.endsWith('/')||url.pathname.endsWith('index.html');
  if(same&&page){e.respondWith(fetch(req).then(r=>keep(req,r)).catch(()=>caches.match(req,{ignoreSearch:true}).then(h=>h||caches.match('index.html')))); return;}
  // everything else: answer from the cache at once when we have it, and refresh the copy in the background
  e.respondWith(caches.match(req,{ignoreSearch:same}).then(hit=>{const net=fetch(req).then(r=>keep(req,r)); if(hit){net.catch(()=>{}); return hit;} return net;}));
});
