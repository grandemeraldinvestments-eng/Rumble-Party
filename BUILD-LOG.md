# Rumble Party: build log

Everything built so far, in the order it happened. The game is one file, `index.html`, plus three music tracks. It runs in a browser with Three.js and has no build step.

Last updated: 11 November 2026.

## What the game is

A 3D party board game for 2 to 4 players. Players roll a dice, move around a 60-space board, win tickets in mini games, and trade 20 tickets for a pearl at the pearl stall. Most pearls after the last round wins. Each player uses their own phone and joins with a code, or one person plays solo against computer players.

## Current contents

| Area | What is in the game |
|---|---|
| Maps | Island, Carnival, Farm, Volcano |
| Board | 45-space loop plus a 15-space bridge shortcut, 3 shops, 5 fixed pearl stall spots |
| Mini games | 19, chosen each round by a 10-second vote between three |
| Players | 2 to 4, any mix of people and computer players |
| Game length | 5, 10 or 15 rounds |
| Items | Twin Dice, Magnet, Kite |
| Music | Lobby, board and mini-game tracks, with separate music and sound switches |
| Controls | Touch, keyboard, game controller |
| Graphics | Smooth (default) or sharp, in Settings |

## Build history

### 1. First playable version
- Board game with a dice, tickets, pearls and a set of mini games.
- Moved to 3D graphics with original blocky characters (Otto, Pip, Juno, Moss). No designs from other games are used.
- Economy tuned after test games: lap bonus of 10 tickets, an underdog gift before the final round, two bonus pearls at the end.

### 2. Mini games and the rules guide
- Added five 3D mini games played on a shared deck.
- Added an optional intro guide that explains the rules and what every space does.

### 3. Retro look and online play
- Pixel-art characters on a smooth 3D world.
- Each player on their own phone, joining with a code. One phone hosts and runs the rules; the others show what the host sends.

### 4. Interface
- Player cards show each character's face and name, with a border on whoever's turn it is.
- Map view: tap any space to read what it does.
- Drag to pan the board; a Center button returns to the player whose turn it is.
- The action window can be hidden, and hides itself once your turn ends.
- A menu button at the top right opens Settings, with the Leave option inside.
- Readable font for numbers; round number centred at the top.

### 5. Bigger boards and more maps
- Boards grew to 60 spaces with a 15-space bridge.
- Shops became spaces you pass on the board.
- Added the Carnival and Farm maps, then five more mini games.
- Chance spaces got a reveal animation.

### 6. Voting
- Each round, players get 10 seconds to vote between three mini games. Tapping a game shows a summary of it.

### 7. Special spaces and the Volcano map
- Ten special spaces per map, some unique to that map, each with its own animation.
- Island: high tide, pickpocket, cannon, jackpot, storm.
- Carnival: big wheel, duel, spring, prize wheel, festival.
- Farm: harvest, trap, mud slide, bank, pearl shuffle.
- Volcano: eruption, trade winds, lava tube, mystery box.
- Volcano eruptions burn a stretch of the board and push back anyone standing on it.

### 8. Pearl stall, music and transitions
- The pearl stall moves between 5 fixed spots per map and never stays where it was.
- Three music tracks added: lobby and main menu, board (half speed, quiet), mini games (60% speed).
- A camera fly-over with a title card plays when a game starts.
- Item spaces show the item won, with its own icon and a description.

### 9. Name, repository and sharing
- Renamed from Pier Party to Rumble Party.
- Put on GitHub and shared with a collaborator.

### 10. Walk-around mini games reworked
- Knocked-out players disappear from the deck.
- The game ends when one player is left standing.
- Every deck is a random irregular shape, the same on every phone.
- Walking off the edge knocks you out.
- Walking into another player shoves them, with a bump sound and a knock-back.

### 11. Irregular board maps
- Each map's path has its own outline in place of an oval:
  - Island: a kidney shape with a cove.
  - Carnival: a round with a wedge-shaped mouth.
  - Farm: a peanut shape, pinched in the middle.
  - Volcano: a horseshoe with the crater in the centre and a bridge across the open mouth.
- Island and Volcano coastlines follow the path, so coves are real water.
- Scenery places itself around the path and keeps clear of the spaces.

### 12. Mini game and map fixes from testing
- Crate Stack allows two misses; Ring Toss has five throws.
- The Carnival bridge winds through the middle of the board.
- The Volcano has a third burn zone on its outer ring.
- Map view fits between the player cards and the action window.
- Item reveal cards stay up for about 5 seconds.

### 13. Island flood and Volcano lava
- The flood is one smooth river the same blue as the sea, running coast to coast with sandy banks.
- Shortcut spaces are fully covered until the flood drains.
- A footbridge appears over the river at each end and carries the main path. It is only there during a flood.
- A pearl stall caught on the shortcut moves to dry land.
- Volcano lava is drawn as winding streams and bands beside the burned stretch, never over a space.

### 14. Smoother play
- Characters walk in one continuous stride and no longer stop on every space.
- Island and Volcano coastlines are single shapes (they were about 180 overlapping discs), which roughly doubled drawing speed on those maps in testing.
- Cheaper shadows that refresh every other frame.
- The game lowers its sharpness in steps on phones that cannot hold a steady frame rate.

### 15. Player-versus-player games, ready-up and controllers
- Five new games:
  - Sumo Shove: the safe floor shrinks; shove the others into the red. Dash for a harder hit.
  - Musical Pads: one pad fewer than players; be on one when it turns red.
  - Paint Fight: tiles you walk over turn your colour; most tiles wins.
  - Crumble Deck: tiles drop after anyone steps on them and grow back later.
  - Stomp: jump and land on another player to knock them out.
- The memory game, Signal Flags, was removed.
- Every player taps Ready before each mini game and duel. Computer players are always ready, and the game starts anyway after 30 seconds.
- Game controller support:
  - Walk-around games: left stick or d-pad runs, A jumps or dashes.
  - Everywhere else: the stick moves a pointer and A presses what is under it. The d-pad hops between buttons, B opens the map, Start opens the menu.

### 16. Smoothness pass
- New Graphics setting, **smooth** by default: no live shadows, no edge smoothing, lower sharpness, and a soft blob under each character in place of its shadow. Switch to **sharp** in Settings to get the old look back.
- Path planks and space rims are baked into a few meshes (they were about 120 separate ones).
- In walk-around games, other players' movement is replayed a beat behind and glides between updates, so they no longer jerk toward each new position.
- On the test machine (no graphics chip) the board went from about 5 to about 40 frames a second.

### 17. Ready-made scenery models
- Added free 3D models for scenery: a beach hut, market stalls, a well, a farmhouse, a windmill, pine trees, fences, wheat fields, pond plants, boulders, dead trees, a mine, a ruin, sea crags, hills and clouds.
- The models are stored in `models.json` (52 models, about 1 MB). Everything placed on a map is baked into one mesh, so the extra drawing cost is small.
- If `models.json` is missing, the game falls back to the scenery it builds in code.
- The four characters, the ferris wheel, carousel, striped tents, lighthouse, palms and volcano are still built in code.

### 18. Scenery scale, Island village and more event spaces
- Scenery models are scaled to the characters: buildings stand clearly taller than a player, and barrels, crates and fences sit at waist height.
- The Island no longer has the ferris wheel, striped tent or balloons; those belong to the Carnival. It has a beach village instead: two houses, a market stall, a watchtower, a well and a canopy with cargo.
- Two more event spaces on every map. Island has 4 Storm spaces, Carnival 4 Festival, Farm 4 Pearl shuffle, and the Volcano, which had none, has 2 Storm.

## Mini games

**Shared deck (everyone on one deck at once)**
Crab Scramble, Boom Hop, Ticket Grab, Hot Planks, Coconut Drop, Spotlight, Sumo Shove, Musical Pads, Paint Fight, Crumble Deck, Stomp.

**Own screen (everyone plays at the same time, separately)**
Bell Ringer, Ring Toss, Ticket Catch, Lighthouse, Crab Count, Pier Dash, Balloon Pop, Crate Stack.

## How it is tested

Tests run in a headless browser with no graphics chip:
- Every mini game is played to the end with random input.
- A full game with computer players is played on each of the four maps.
- A two-device game is simulated in one browser and the final scores on both sides are compared.
- Controller input is checked with a simulated gamepad.
- Screenshots are taken of new visuals.

## Credits

Scenery models are by Kay Lousberg (KayKit: Medieval Hexagon Pack and Halloween Bits, www.kaylousberg.com), released under Creative Commons Zero (CC0). They were taken from the KayKit-Game-Assets repositories on GitHub and converted to a compact format.

## Known limits

- **Real phones:** play between real phones has not been tested here. Shoving and Stomp depend on each phone's view of the others and may feel slightly off on a slow connection.
- **Sound:** music and effects cannot be heard in testing.
- **Controllers:** not tested with a real controller. The Claude page may block controllers because it runs in a locked-down frame; a standalone copy would not have that limit.
- **Online play outside Claude:** joining by code uses the Claude page's room service. The copy in this repository runs solo against computer players only, unless the online layer is replaced.
- **Frame rate:** measured only on a machine with no graphics chip, so the numbers show relative change, not real phone speed.

## Open decisions

**Mobile app.** Not built. Three routes:
1. An app shell around this web game: solo play only, controllers work.
2. An app shell plus a replacement online service (for example Firebase), which needs an account.
3. A rebuild in a game engine such as Unity or Godot, for a real gain in smoothness and graphics.

**Other ideas not yet built**
- Let knocked-out players do something while they wait in long survival games.
- Real 3D models and animations made in a tool such as Blender.
