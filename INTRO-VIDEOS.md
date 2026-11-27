# Board introductions: films

Every board opens with an introduction (Build 74): a flight over the board with its name, the one rule that makes the board different,
the space where the first pearl is in this game, and a glide into the game's own camera. Today all of it is flown live through the
real 3D board. This page says how a recorded film can replace the first two parts, and what has to be made.

## What exists and what does not
- The player for films is built and tested: it plays a film over the scene, keeps the title and rule card in step with it, dissolves
  into the live scene, and carries on without the film if it cannot load, cannot autoplay, or the screen is upright and the film has
  no upright version.
- **No films have been made.** No board has a `video` entry, so every board uses the live flight.
- A film recorded from the game itself (the tool below) looks the same as the live flight and costs a 2 to 4 MB download, so it is not
  switched on. A film is only worth using when it shows more than the live board can: a render from Blender, extra animation, effects.

## Films still to be produced
One for each board: Island, Carnival, Farm, Volcano, Melody Mansion, Pinball Paradise, Temple of the Golden Titan. Optionally an upright
version of each for phones held upright (otherwise those phones use the live flight).

## Specification
- 16:9, 1920 x 1080 master, 30 frames a second, no sound (the board music keeps playing).
- Length: the first two parts of the full introduction, less the turn toward the pearl. Today that is 6.45 seconds
  (3.2 s flight in + 4.2 s rule - 0.95 s). The tool prints the exact number to put in `until`.
- Delivery: H.264 MP4, yuv420p, `+faststart`, about 2 to 4 Mbit/s; a 1280 x 720 copy is enough for phones. A JPEG of the first frame
  as the poster.
- Nothing that changes from game to game may be in the picture: no pieces, no pearl stall, no dice, no scores.
- No words in the picture. The title, the rule card and the Skip button are drawn over it by the game, so they can be changed or
  translated.
- The last 0.6 seconds are dissolved into the live scene, so the camera, light and colours of those frames must match the game's.
  The surest way is to render along the game's own camera path: `introPose(shot,u,I)` in index.html gives the position and target
  for any moment.
- The server must be able to send part of a file (phones ask for films in pieces). server.js does from Build 74; GitHub Pages does.

## Shot plan (the same for every board; numbers are for a sideways screen)
| Part | Seconds | Camera | Drawn over it |
|---|---|---|---|
| A. Flight in | 0 to 3.2 | High and wide, about twice the board's half-width away, sweeping 45 degrees round and dropping toward the board | Board name; rounds and players |
| B. The rule | 3.2 to 7.4 | Circles the board's landmark from about 13 units away and 9 up (Island: 17 away, 12 up, over the tidal channel) | Rule card with its picture |
| C. The pearl (always live) | 7.4 to 10.3 | Closes on the pearl stall of this game from 9 to 6.5 units | "The first pearl", distance from the start, price |
| D. To the start (always live) | 10.3 to 11.7 | Settles into the game camera over the start space | Nothing; the scoreboard appears |

What part B looks at, and what it shows happening:
- Island: the tidal channel; the tide comes in and floods the short cut.
- Carnival: the big wheel, turning fast.
- Farm: a harvest space.
- Volcano: the volcano, erupting.
- Melody Mansion: the metronome.
- Pinball Paradise: the centre of the table.
- Temple of the Golden Titan: the summit.

## Recording from the game
`python3 tools/record-intro.py island 1920 1080 30` steps the game frame by frame along that path with pieces, pearl and words hidden,
and writes `assets/intro/island.mp4` and `.jpg`. The same command always gives the same film. On a machine with a graphics card set
`SOFTWARE_GL=0`.

## Switching a film on
In `INTRO.boards` (index.html) add to the board's entry:
`video:{src:'assets/intro/island.mp4',poster:'assets/intro/island.jpg',until:6.45}` (and `portrait:'...'` for an upright version).
Do not add films to the list in sw.js; the browser keeps them itself.
