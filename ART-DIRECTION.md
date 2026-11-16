# Rumble Party art direction

Working notes for the visual overhaul. Branch `visual-overhaul`, based on Build 60 (commit 5a9328b).

## The look: "boardwalk toybox"

Everything should look like a painted wooden toy from a seaside fairground.

- **Outline:** thick, uniform dark navy `#17304d` on every icon, button and card.
- **Palette:** sun `#ffc531`, coral `#ff4d4d`, sky `#2f8fff`, mint `#35c98a`, pink `#ff5fa8`, lavender `#c9a6ff`, cream `#fffaf0`. Player colours are unchanged.
- **Shading:** flat colour, one soft highlight and one darker band per shape. No realism, no heavy gradients.
- **Shapes:** chunky and rounded. Corners 10 to 22 px. Everything pressable sits on a hard navy drop edge and sinks when pressed.
- **Type:** Lilita One for titles, buttons and numbers; Rubik for body text. The pixel font is no longer used in the interface.
- **Icons:** slight 3/4 tilt, big silhouette, readable at 24 px, transparent background, no text inside the picture.

The game stays 3D (three.js). Painted 2D art is used where it is cheap and reads well on a phone: interface, icons, badges and the tops of board spaces. Characters and scenery stay as 3D models.

## Master prompt for new art

Paste this before the list of things to draw, in the same ChatGPT thread ("Create Game Icon Sheet") so the style stays matched:

> Same master style: chunky toy-like 2D cartoon vector look, thick uniform dark navy outline (#17304d), flat saturated candy colours (sun yellow #ffc531, coral red #ff4d4d, sky blue #2f8fff, mint green #35c98a, pink #ff5fa8, lavender #c9a6ff, cream white), exactly one soft highlight and one darker shade band per shape, rounded corners, slightly tilted 3/4 view, big readable silhouettes. Square 1024x1024, TRANSPARENT background, a clean N by N grid of separate icons, each centred in its cell with empty margin, nothing overlapping, no text, no letters, no numbers.

## Pipeline

1. Generate a sheet in the ChatGPT thread and save it in `art-source/`.
2. Process it with the tools in `tools/`:
   - **Icons and standees:** `python3 tools/slice.py sheet.png rows cols outdir name1,name2,... size [tight]`. Makes the art fully solid (generated sheets come out slightly see-through), finds each object and writes WebP. `tight` keeps the object's own shape for standees; without it each icon is centred in a square.
   - **Ground textures:** `python3 tools/tile.py sheet.png quarter out.webp [blend|planks|mirror] [size]`. Takes one quarter of a 2 by 2 sheet and makes it repeat without a visible join. Use `blend` for scattered patterns (sand, grass, rock, ice), `planks` for boards, `mirror` for regular patterns (carpet, soil).
3. Runtime files go in `assets/<group>/`. Add new files to the list in `sw.js` and raise the cache number so installed copies update.
4. `minigames.html` is `index.html` with the title and `PRAC_ONLY` changed; regenerate it after every edit.

## How painted art is used in the 3D world

- **Ground:** `gmat(name, colour, repeatX, repeatY)` gives a material that shows the plain colour until its texture loads. Used by `coast()`, the carnival boardwalk and carpet, the farm ground and fields, and mini game decks.
- **Standees:** `stand(name, x, z, height)` places a painted cut-out that always faces the camera, with a soft shadow. `scatter(inside, ring)` fills a board: `inside` goes wherever there is room within the loop, `ring` goes round the outside.
- **Mini game arenas:** every arena is built from three painted layers, all drawn as seen from straight above.
  - **Setting** (`set:'name'` in the game's settings; listed in `SETS`): a repeating floor that runs to the horizon plus one big painting of the place laid round the platform (`assets/arena/ground-<name>.webp`). Settings: `sea` lagoon (default), `theatre`, `night` harbour, `snow` frozen lake, `fair` plaza, `crater` volcano, `factory`. Pick the one that fits the game; never leave an indoor, night or ice game on `sea`.
  - **Platform top** (`top:'name'`): a painting made for that game (`assets/arena/top-<name>.webp`) on a solid body that stands on the ground, with a trim band and, at sea, a foam ring. Tops: ship, beach, stage, circus, rink, court (round); dojo, arcade (square).
  - **Plain floors** (`floor:'name'`): for games without a painted top, a repeating texture (stage, carpet, sand, grass, rock, soil), or planks if left out.
  - To add one: generate with the "platform tops" or "surroundings" prompts in the ChatGPT thread, then `python3 tools/tops.py sheet.png assets/arena name1,name2,name3,name4` or `python3 tools/ground.py painting.png assets/arena/ground-name.webp`.
  - **Under the platform** (`under:'name'`): a painting the platform stands on, such as the ship under Boom Hop (`assets/arena/under-<name>.webp`).
  - **Painted tiles** (`ttex('name')`): one tile picture shared by every tile of a floor and tinted by the tile's colour. `stone` for Hot Planks and Crumble Deck, `glaze` for Paint Fight; `tile-belt` is drawn under the arrows in Conveyor Chaos.
  - **Long courses** (`zs:[...]`): where along the course the setting painting repeats. Prepare that painting with `tools/ground.py ... 1024 sides` so only its left and right edges fade.
  - **Own-screen games and the vote:** `assets/arena/stall.webp`, a fairground stall seen from the front, sits behind them.
  - **Spotlight** carries a real lamp in each spotlight, so the stage can be dark and players light up as they step in.
  - Standing cut-outs are not used in arenas any more: seen from the arena camera they looked pasted on. They are for the boards only.
- **Shoreline:** a foam ribbon is built round every coast in `coast()` and drifts slowly.
- **Sky:** each map shows `assets/sky/<map>.webp` behind the 3D view.

## What exists now

| Group | Files | Used in |
|---|---|---|
| `assets/icons` | twin, magnet, kite, ticket, pearl, clam, mystery, shop, star, trophy | Item buttons, bags, shop, reveal cards; ticket and pearl counters in the HUD |
| `assets/maps` | island, carnival, farm, volcano | Lobby map picker |
| `assets/games` | g0 to g23, one per mini game in `GAMES` order | Practice list and vote buttons |
| `assets/spaces` | one per special space letter in `SP`, plus S for start | Painted on the board spaces and on the reveal card |
| `assets/tex` | sand, grass, planks, rock, carpet, ice, soil, stage, snow, nightsea, foam (lava and cobble made, not yet used) | Board ground, shoreline, mini game decks |
| `assets/props` | 9 each for island, carnival, farm, volcano and sea, plus 3 theatre and 6 snow (54) | Standees on the boards, floating scenery round boards and mini game decks |
| `assets/arena` | 8 platform tops, 6 surroundings | Mini game arenas |
| `assets/sky` | island, carnival, farm, volcano | Sky behind each board |
| root | icon-192, icon-512, apple-touch-icon | Home-screen icon |

Not yet used: icons clam, mystery, shop, star, trophy.

## Still to do

- **Characters:** left as the stock adventurers by decision. Re-colouring was tried and dropped.
- **Mini games:** every game now has a painted setting. Still plain inside the own-screen games: their buttons, bars and targets. Hedge Maze and Ghost Runner are dark by design and unchanged. Platform shapes and rules are unchanged; only looks have changed so far.
- **Board spaces:** the plain blue, red, question, item and shop spaces still use the drawn icons.
- **Paths:** the track between spaces is still a flat colour.
- **Results and award screens:** not restyled beyond the shared skin.
- **Effects:** hit, pickup and win effects are still simple dots.
- **Real phones:** not tested for frame rate with the added textures and standees.
