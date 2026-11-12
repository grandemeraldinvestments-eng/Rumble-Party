# Rumble Party

A 3D party board game for 2 to 4 players that runs in a web browser. Players run around a 60-space board, win tickets in mini games and trade them for pearls. Most pearls at the end wins.

## What's in it

- Four maps: Island, Carnival, Farm and Volcano
- Nineteen mini games, chosen each round by a 10-second player vote
- Items, shop spaces, chance spaces and special spaces that differ on every map
- Computer opponents

## Files

- `index.html` - the whole game: markup, styles and code in one file
- `music-board.wav`, `music-mini.wav`, `music-lobby.wav` - looping background tracks

The only outside dependency is three.js r128, loaded from cdnjs, plus two Google Fonts.

## Running it

Serve the folder with any static web server and open it in a browser, for example:

    python3 -m http.server 8000

then visit http://localhost:8000. Opening `index.html` directly from disk also works, but the music will not load without a server.

## Online play

Playing on separate phones with a join code depends on the realtime room service of the Claude artifact the game was built in. That service is not available to a copy served from this repository, so here the game runs in solo mode against computer players. The Host and Join buttons stay disabled.

## Credits

Scenery models by Kay Lousberg (KayKit, www.kaylousberg.com), CC0.
