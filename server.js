// Rumble Party server: serves the game's files and runs the join-code rooms that let friends play together on separate phones.
// A room is just a shared noticeboard. Each player posts their own small state ("presence") and everyone in the room sees everyone's.
// The game does the rest: the host's phone runs the rules and posts the game state, the others post their answers and positions.
const http = require('http'), fs = require('fs'), path = require('path');
const { WebSocketServer } = require('ws');

const PORT = process.env.PORT || 8080, ROOT = __dirname;
const MAX_ROOM = 8;                  // people in one room (6 players plus a little slack for rejoining)
const MAX_MSG = 512 * 1024;          // largest single message, bytes
const MAX_RATE = 120;                // messages per second from one phone before it is dropped
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.json': 'application/json', '.webmanifest': 'application/manifest+json',
  '.png': 'image/png', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.md': 'text/markdown; charset=utf-8' };
const PRIVATE = /^\/(server\.js|package(-lock)?\.json|node_modules|tools|art-source|\.)/;   // never served

const server = http.createServer((req, res) => {
  let p; try { p = decodeURIComponent(new URL(req.url, 'http://x').pathname); } catch (e) { res.writeHead(400); return res.end(); }
  if (p === '/health') { res.writeHead(200, { 'content-type': 'text/plain' }); return res.end('ok'); }
  if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405); return res.end(); }
  if (p.endsWith('/')) p += 'index.html';
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT + path.sep) || PRIVATE.test(p) || !TYPES[path.extname(file)]) { res.writeHead(404); return res.end('Not found'); }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) { res.writeHead(404); return res.end('Not found'); }
    const page = /\.(html|js|webmanifest)$/.test(file);   // the page and its worker are always re-checked, so an update shows at once; art and sound are kept for a day
    res.writeHead(200, { 'content-type': TYPES[path.extname(file)], 'content-length': st.size, 'cache-control': page ? 'no-cache' : 'public, max-age=86400' });
    if (req.method === 'HEAD') return res.end();
    fs.createReadStream(file).pipe(res);
  });
});

const rooms = new Map();   // room name -> Map(id -> socket)
let nextId = 1;
const send = (ws, o) => { if (ws.readyState === 1) ws.send(JSON.stringify(o)); };
function leave(ws) {
  const name = ws.room, r = rooms.get(name); if (!r) return;
  r.delete(ws.id); ws.room = null;
  if (!r.size) rooms.delete(name); else for (const o of r.values()) send(o, { t: 'l', id: ws.id });
}
const wss = new WebSocketServer({ server, path: '/ws', maxPayload: MAX_MSG });
wss.on('connection', ws => {
  ws.id = 'p' + (nextId++).toString(36) + Math.random().toString(36).slice(2, 6); ws.room = null; ws.pres = {}; ws.alive = true; ws.n = 0; ws.t = Date.now();
  ws.on('pong', () => { ws.alive = true; });
  ws.on('message', raw => {
    const now = Date.now(); if (now - ws.t > 1000) { ws.t = now; ws.n = 0; } if (++ws.n > MAX_RATE) return ws.close(1008, 'too fast');
    let m; try { m = JSON.parse(raw); } catch (e) { return; }
    if (!m || typeof m !== 'object') return;
    if (m.t === 'join') {
      if (ws.room || typeof m.room !== 'string' || !/^[a-z0-9-]{3,32}$/.test(m.room)) return send(ws, { t: 'err', m: 'bad room' });
      let r = rooms.get(m.room); if (!r) rooms.set(m.room, r = new Map());
      if (r.size >= MAX_ROOM) return send(ws, { t: 'err', m: 'full' });
      const peers = {}; for (const o of r.values()) peers[o.id] = o.pres;
      r.set(ws.id, ws); ws.room = m.room; ws.pres = {};
      send(ws, { t: 'in', me: ws.id, peers });
      for (const o of r.values()) if (o !== ws) send(o, { t: 'p', id: ws.id, d: {} });
    } else if (m.t === 'p') {
      const r = rooms.get(ws.room); if (!r || !m.d || typeof m.d !== 'object' || Array.isArray(m.d)) return;
      Object.assign(ws.pres, m.d);   // a post changes only the parts it names
      for (const o of r.values()) if (o !== ws) send(o, { t: 'p', id: ws.id, d: m.d });
    } else if (m.t === 'k') { send(ws, { t: 'k', n: m.n });   // a keep-awake from a phone: sent straight back, so the phone can time the round trip
    } else if (m.t === 'leave') leave(ws);
  });
  ws.on('close', () => leave(ws));
  ws.on('error', () => {});
});
// drop phones that have gone silent (closed lid, lost signal), so the others see them leave
setInterval(() => { for (const ws of wss.clients) { if (!ws.alive) { ws.terminate(); continue; } ws.alive = false; ws.ping(); } }, 15000);

server.listen(PORT, () => console.log('Rumble Party is running on port ' + PORT));
