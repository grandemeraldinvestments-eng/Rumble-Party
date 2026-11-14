# Rumble Party: build log

Everything built so far, in the order it happened. The game is one file, `index.html`, plus three music tracks. It runs in a browser with Three.js and has no build step.

Last updated: 12 November 2026.

## What the game is

A 3D party board game for 2 to 6 players. Players roll a dice, move around a 60-space board, win tickets in mini games, and trade 20 tickets for a pearl at the pearl stall. Most pearls after the last round wins. Each player uses their own phone and joins with a code, or one person plays solo against computer players.

## Current contents

| Area | What is in the game |
|---|---|
| Maps | Island, Carnival, Farm, Volcano |
| Board | 45-space loop plus a 15-space bridge shortcut, 3 shops, 5 fixed pearl stall spots |
| Mini games | 20. A random shared-deck game ends each round; own-screen games are used for duels |
| Players | 2 to 6, any mix of people and computer players |
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

### 19. Animated characters, six players and a start platform
- The four block characters are replaced by six animated ones: Knight, Barbarian, Mage, Rogue, Ranger and Paladin. They walk, run, jump, idle and cheer, and their portraits appear on the player cards.
- Character files are `char-0.json` to `char-5.json` (about 650 KB each). If they fail to load, the game uses six block characters instead.
- Up to six players, any mix of people and computer players. With five or six, the player cards sit in two rows and mini game prizes are 10, 6, 4, 2 and 1 tickets.
- Players wait on a start platform beside the GO space and step onto the board on their first turn.

### 20. Home-screen web app
- Added a web app manifest, icons and an offline worker (`manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png`, `sw.js`), so the game can be added to a phone's home screen, open full screen and run offline after the first visit.
- Needs GitHub Pages switched on for the repository. Outside Claude the game is solo only.

### 21. Landscape layout, full screen and right-stick scrolling
- Sideways phones get their own layout: player cards in one row, the action window at the bottom right, two-column menus, and a compact mini game intro so the Ready button is always on screen.
- Full screen: on phones the game asks the browser for full screen when a game starts, and Settings has a full screen switch. iPhone browsers do not allow this; there the game must be opened from the Home Screen icon.
- Controller right stick scrolls menus and long screens, and pans the board during play. Pressing the right stick re-centres the camera.
- The menu now says 2 to 6 players.

### 22. Touch steering fix, map centring and practice mode
- Fixed: in sideways view, dragging to steer in the walk-around mini games did nothing, because the browser treated the drag as a page scroll. Checked with a simulated touch drag before and after.
- Map view is fitted to the real bounds of the board and centred in the free part of the screen, beside the action window when the phone is sideways.
- New Practice screen on the main menu: pick any of the 19 mini games and play it against 1, 3 or 5 computer players. Games already tried are marked.
- `minigames.html` is the same game opened straight on the practice list.

### 23. Slimmer player cards and fork preview
- Player cards are two lines: YOU, CPU or the rank sits under the name, and tickets, pearls and items share the second line.
- The menu button is smaller and the round label sits under it on two lines, so more of the board shows.
- Fork in the path: tapping an option turns it yellow and shows that route's distance to the pearl and the space you will land on, with a ring on that space and the camera leaning toward it. Tapping the yellow option again confirms.
- The Center button is inside the action window, between the player name and Map.

### 24. Landscape action bar, item previews and the clam
- Sideways, the action window is a bar along the bottom: player name and message on the left, buttons on the right.
- Items work like the fork: tap an item in the shop or in your bag to read what it does (it turns yellow), tap it again to buy or use it. Skip and Hit the dice act on the first tap.
- The pearl stall is an open clam with the pearl inside, sitting beside its space on the side clearest of the path.

### 25. No vote, game cycle and button-only controller
- The vote is gone. Each round ends with a random shared-deck game, and none repeats until all 11 have been played.
- Own-screen games are kept for duels (all of them except Balloon Pop, which needs touch aiming and is in Practice only).
- Controller: the on-screen pointer is removed. The left stick or d-pad moves a box between the buttons and A presses the boxed one. The box jumps to the main button when one appears.
- In the touch-only duel games the stick slides, the d-pad taps a side and A taps.

### 26. Set platforms and reworked shared-deck games
- Every shared-deck game has its own fixed platform (a circle or a square) in place of the random blob, and the camera pulls back to fit it in portrait or landscape.
- Every mini game ends with a "Game Finished" banner.
- Crab Scramble: a small island twice the old width with grass and a palm tree, 3 lives, crabs that get faster and more frequent.
- Boom Hop: a round deck as wide as the boom. The boom speeds up and reverses, flashing yellow just before it turns back.
- Ticket Grab: a square twice the old width, one minute, tickets last 5 seconds, and in the last 15 seconds one in ten is red and costs a ticket.
- Hot Planks: a square of 16 tiles. Yellow tiles are safe until they turn red; more tiles go, with less warning, over time.
- Coconut Drop: deck 30% bigger. Stomp: 20% bigger.
- Spotlight: 90 seconds, deck 30% bigger, live scoreboard. A new yellow light every 30 seconds; old lights turn red and take points away; red and yellow overlap is neutral.
- Sumo Shove: a square 50% bigger. The red closes in around two safe circles, which then roam faster and faster. Touching red knocks you out.
- Hedge Maze replaces Musical Pads: the same random maze for everyone, run alone, one minute, fastest out wins.
- Paint Fight: a square twice the old width with a square hole in the middle.
- Crumble Deck: a square 30% bigger; tiles drop sooner as the game goes on.
- Slippery Slope (new): an ice rink where players slide, and a giant snowball knocks anyone it hits flying.
- Interface: the menu button is as wide as the round label, the repeated "tap again" lines are gone, and the landscape action bar is one thin row.

### 27. Ticket Grab shrink and item icon fix
- Ticket Grab: from 15 to 45 seconds the deck shrinks to half its size and the camera closes in with it. In the last 15 seconds half the tickets are red.
- The item icon on the reveal card is centred in its circle in landscape.
- The clam and pearl are half their previous size and sit closer to their space.
- Board music replaced with a new track (`music-board.mp3`, 2 min 20 s, looped).
- Hedge Maze: no overview. The camera stays close above your own character, the hedges are taller, and the exit is no longer pointed out.

### 28. Mini game songs
Three new songs, each cropped to 90 seconds (the longest mini game), replace the single mini game track:

| File | Used for |
|---|---|
| `music-mini1.mp3` | Dodge and survive: Crab Scramble, Boom Hop, Hot Planks, Coconut Drop, Crumble Deck, Slippery Slope |
| `music-mini2.mp3` | Player against player and collecting: Ticket Grab, Spotlight, Sumo Shove, Hedge Maze, Paint Fight, Stomp |
| `music-mini3.mp3` | Own-screen games (duels and practice): Bell Ringer, Ring Toss, Ticket Catch, Lighthouse, Crab Count, Pier Dash, Balloon Pop, Crate Stack |

### 29. Pearl celebration, two-roll Twin Dice and a smaller action window
- Buying or winning a pearl: the character holds the pearl overhead and dances for about two seconds, with a banner and a fanfare.
- Twin Dice: the player hits the dice twice, once for each roll.
- Pop-up cards can be closed early with a tap by the player whose turn it is, once the card has been revealed.
- Action window: the player name sits top left with the text directly under it, and Map and Hide to the right. In portrait the window is about 22% shorter; in landscape the text has the full width up to the Map button.
- Ready screen: player names are two per row (three rows for six players) and the rules no longer overlap the title.

## Mini games

**Shared deck (everyone on one deck at once)**
Crab Scramble, Boom Hop, Ticket Grab, Hot Planks, Coconut Drop, Spotlight, Sumo Shove, Hedge Maze, Paint Fight, Crumble Deck, Stomp, Slippery Slope.

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

Scenery and character models are by Kay Lousberg (KayKit: Medieval Hexagon Pack, Halloween Bits and Adventurers character pack, www.kaylousberg.com), released under Creative Commons Zero (CC0). They were taken from the KayKit-Game-Assets repositories on GitHub and converted to a compact format.

The board and mini game music was generated with Suno by the project owner.

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
