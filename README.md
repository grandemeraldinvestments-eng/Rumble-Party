# Rumble Party

A 3D party board game for 2 to 4 players that runs in a web browser. Players run around a 60-space board, win tickets in mini games and trade them for pearls. Most pearls at the end wins.

## What's in it

- Four maps: Island, Carnival, Farm and Volcano
- Twenty-seven mini games. Each round plays one of the shared-platform games or Drum Beater, picked at random
- Items, shop spaces, chance spaces and special spaces that differ on every map
- Computer opponents

## Files

- `index.html` - the whole game: markup, styles and code in one file
- `server.js`, `package.json` - the room server for online play, which also serves the game's files
- `music-board.mp3`, `music-mini1.mp3` to `music-mini3.mp3`, `music-lobby.wav` - looping background tracks

The only outside dependency is three.js r128, loaded from cdnjs, plus two Google Fonts.

## Running it

Serve the folder with any static web server and open it in a browser, for example:

    python3 -m http.server 8000

then visit http://localhost:8000. Opening `index.html` directly from disk also works, but the music will not load without a server.

## Online play

One person taps **Host a game** and shares the 4-letter code; everyone else opens the same page, taps **Join a game** and types it. Up to six players, with computer players filling any empty seats.

Online play needs the room server in this repository (`server.js`). It serves the game's files and runs the join-code rooms over a web socket:

    npm install
    npm start

then visit http://localhost:8080. Any host that runs Node works (Railway, Render, Fly and so on): it only needs `npm start` and the `PORT` it is given.

A copy of the page served without that server, such as GitHub Pages, plays solo only unless `RUMBLE_SERVER` near the top of the online code in `index.html` is set to a room server's address (for example `wss://your-app.up.railway.app/ws`).

How it works: the host's phone runs the rules and posts the game state to the room; the other phones post their answers and positions. The server only passes these posts along and keeps nothing. If the host leaves, the game ends for everyone; if another player leaves, a computer player takes their seat.

## Credits

Scenery and character models by Kay Lousberg (KayKit, www.kaylousberg.com), CC0.

## Play it as a home-screen app

Once GitHub Pages is switched on for this repository, the game is served at `https://grandemeraldinvestments-eng.github.io/Rumble-Party/`.

- **iPhone:** open the link in Safari, tap Share, then "Add to Home Screen".
- **Android:** open the link in Chrome, tap the menu, then "Add to Home screen" or "Install app".

It opens full screen from its own icon and works offline after the first visit. Outside Claude the game is solo against computer players; joining friends by code needs the Claude page.
