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
| Mini games | 22. A random shared-deck game ends each round; own-screen games are used for duels |
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

### 30. Hedge Maze from the inside
- Hedge Maze is played through the character's eyes. The hedges are too tall to see over, so nothing beyond the corridor you are in is visible.
- Controls in the maze: push up to walk forward, down to back up, left and right to turn.
- Leafy hedge texture, tiled floor and a light haze give a sense of depth. You start facing an open corridor.
- In landscape, Map and Hide are always in the right corner of the action bar, with the action buttons between them and the text.

### 31. Hedge Maze in third person with split controls
- The camera sits above and behind the character, inside the maze and below the top of the hedges, and moves in closer when a hedge is behind you.
- Touch: drag on the right half of the screen to move, drag on the left half to turn the view.
- Controller: right stick moves, left stick turns the view. Keyboard: W A S D or up/down to move, left/right arrows to turn.
- The maze is 50% bigger: corridors are half as wide again, the camera sits further back, and players run about 30% faster so the one-minute limit still works.

### 32. Swap shows both players; even ready cards
- Chance swap: the camera now shows both players. If they are close it frames both at once; if they are far apart it visits the rival, shows the swap landing, then visits where the rival ended up.
- Ready screen: every player card is the same size. Landscape shows three per row, portrait two per row, with any leftover cards centred.

### 33. Stopping dice, maze sticks and timer bar
- The die stops on the number rolled, face up and tipped toward the camera. With Twin Dice it stops on the first number, spins again, and stops on the second after the second hit.
- Hedge Maze has two on-screen sticks: the left one turns the view, the right one moves. The camera is near eye level, over the character's shoulder.
- The mini game timer bar is back at the bottom of the screen in landscape.

### 34. Two new mini games: Trap Doors and Ghost Runner
- Trap Doors: three rounds. Everyone walks into a door before the timer runs out; one door per round is a drop and anyone behind it is out. 5 doors, then 3, then 2. Anyone who has not chosen in time is pushed through the nearest door.
- Ghost Runner: a pitch-black square where every player has a torch. A ghost starts in the middle and hunts one player, marked with a red ring. If the hunted player touches someone, the ghost switches to them. The ghost only catches the player it is hunting, pauses after a catch, then picks someone new. It starts at 75% of player speed and reaches 90%.
- Both are shared-deck games in the end-of-round rotation, which now has 14 games. The game has 22 mini games in total.

### 35. Ghost Runner: closer and darker
- The camera is steeper and zoomed in so the deck fills the screen width in portrait and the height in landscape.
- The ghost no longer glows. It is only visible where a torch beam lands on it. The same goes for the red ring under the hunted player.
- The deck edge is no longer outlined, so you only see it when a torch reaches it.

### 36. Trap Doors: one per door and a view from behind
- Only one player fits in each door, and once inside there is no coming back out. A player who is too slow is put in the nearest empty door.
- Because each door holds one player, a round has 5, 3 and 2 doors, or one per player still in if that is more.
- For the reveal the camera swings round behind the doors, low enough to see underneath. The floor under the wrong door swings down and that player drops through.

### 37. Ghost Runner: torches and a bigger deck
- Each player carries a burning torch that lights a circle all the way round them, in place of a forward beam. The flame flickers.
- The deck is 20% bigger.

### 38. Ghost Runner: landscape zoom and a hunted banner
- In landscape the deck is zoomed to the full width of the screen and the camera slides along the deck with your character.
- A red banner at the top middle, "Boo is after You", shows while the ghost is hunting you.
- Torches are a little brighter and held higher so characters are easier to see.

### 39. Updates arrive straight away; build number
- The offline worker now always re-checks the page with the server, bypassing the browser's 10-minute cache. Before this, a phone could keep showing the previous version for up to 10 minutes after an update.
- The main menu and the practice list show a build number, which goes up with every published update.

### 40. Practice list fix and new menu text
- Fixed: the Practice mini games button and the mini game tester page stopped working in build 40. A comment added with the build number had swallowed the rest of its line. Every publish now runs an automatic check that the tester page opens on its list.
- New menu text: an invitation line and a caution line.

## Build 42

- Menu text now says "up to 5 friends" (the game holds 6 players in total).
- No change to the Rumble Party title. Test screenshots now load the game's real fonts, so they match what phones show.

## Build 43

- Ghost Runner: the camera now keeps your character in the middle of the screen. Landscape is zoomed out about 15%, and portrait uses the same close view.
- Hedge Maze: turning the view is 20% faster (touch stick, controller stick and keys).

## Build 44

- Ghost Runner: portrait now uses the same zoom level as landscape, so characters are the same size on screen both ways round.

## Build 45

- Trap Doors: every doorway now has a door that stands open and slams shut behind the player who walks in.
- Trap Doors: a fourth round with 2 doors (5, 3, 2, 2). The game now lasts up to 52 seconds.
- Hedge Maze: the camera sits further behind your character when there is room, and turning the view is 30% faster.

## Build 46

- Ghost Runner: anyone who touches a ghost is out, not only the hunted player.
- Ghost Runner: half way through (30 seconds) the ghost splits in two and each half hunts a different player. A player with both on them sees "2 Boos are after You"; touching someone passes on only one.
- Ghost Runner: platform 15% bigger.
- Trap Doors: one door fewer each round (5, 4, 3, 2), never fewer doors than players still in.
- All shared-platform mini games: the camera is refitted when the phone is turned or goes full screen after the game was set up. Before, a game set up in portrait stayed zoomed far out in landscape.

## Build 47

- Trap Doors: with 6 players there are 6 doors and 5 rounds (6, 5, 4, 3, 2). With fewer players it stays 5 doors and 4 rounds.
- Ghost Runner: the game is 80 seconds. At 40 seconds the ghost splits into one ghost for every player still in, each a different colour and each hunting its own player. Touching someone still passes one of your ghosts on.
- Mini games can now set their own length per match.

## Build 48

- Ghost Runner: the ghost colours now have a ranking: white, green, pink, cyan, red, purple. When two players touch, whoever holds the highest-ranked ghost of the two passes that ghost to the other player. One touch moves one ghost.

## Build 49

- Slippery Slope: the snowball now rolls straight across the deck from one side to the other, then sets off on a new random course. It still speeds up as the game goes on.

## Build 50

- Stomp: 5 jumps each, shown on the Jump button. When every player still in has used all of theirs, everyone gets 5 more.
- Stomp: a separate Stun button with one use, never topped up. It freezes the nearest player in reach for a moment (yellow halo), and the player who used it cannot jump until it wears off. It cannot be used in the air.
- Sumo Shove: 5 dashes each, shown on the Dash button, and each dash ends with a small kick backwards.
- Mini games can now send extra per-player state (jumps, stuns) between phones, and can have a second action button.

## Build 51

- Paint Fight: a colour bomb lands on a random tile every 10 seconds. Walk over it to pick it up, then tap the new Bomb button to paint a 4 by 4 block of tiles around you.
- View check of all 14 shared-platform games in portrait and landscape. Landscape platforms now stop short of the timer bar, and the Trap Doors wall fits inside the screen.

## Build 52

- Coconut Drop: coconuts are half the size and about 30% more of them fall.
- Coconut Drop: everyone has a stun gun with 3 shots for the game. The Shoot button (bottom right) fires the way you are facing; a hit freezes that player for a moment.
- Hot Planks: half way through (20 seconds) the 16 big tiles turn into 256 small ones, about the size of the Crumble Deck tiles. Same rules, same timing, same share of the floor each time.

## Build 53

- Coconut Drop: the stun now lasts 1.4 seconds, twice as long as before.

## Build 54

- Hedge Maze: first-person view again. The camera is your character's eyes and your own character is hidden.
- Hedge Maze: a marker in your colour is dropped on the floor every step or so, so you can backtrack and see which corridors you have already walked.

## Build 55

- Crumble Deck: players can jump.
- Coconut Drop: platform about 20% bigger.
- Ghost Runner: once you are out, the view pulls back to the whole platform so you can watch the others.
- Board popups: any player can close a card once it is revealed, on anyone's turn, by tapping the screen, pressing a key or a controller button.
- Mini Game Frenzy: the final round ends with three mini games. Whoever wins the most of the three takes a pearl and no tickets; everyone else keeps all the tickets they won across the three.
- Award ceremony at the end of the game: the characters walk on and line up, the stage goes dark, a spotlight finds each award winner, a pearl comes down, they take it and dance, and finally each player's block rises to match their place.
- Eight award rules, three drawn in secret at the start of each game: Mini game champ, Podium regular, Globetrotter, Big spender, Gadget fan, Lucky feet, Hard knocks, Chance taker.

## Build 56

- Award ceremony: the spotlight now searches for 2.5 seconds longer before each winner is shown, with a drum roll that builds up to the reveal.
- Crab Scramble: crabs are 10% slower.

## Build 57

- New mini game, Conveyor Chaos: a race across eight moving belts that run left, right, back or forward and change direction every few seconds (they flash before they change). Carried off the side and you go back to the start.
- New mini game, Lantern Match: six coloured lanterns light up in a sequence; walk over them in the same order. One more is added each round. The wrong lantern, or running out of time, puts you out.
- Hedge Maze: seen from above, following your character, but only the part your character can see is shown. Anything round a corner or behind a hedge is blacked out. One stick again; trail markers kept.
- Crab Scramble: crabs 10% slower again and 10% fewer of them.
- Ready screen: a live preview of the game, played by computer players, runs behind the ready panel. The written rules are behind a Rules button.
- Every mini game now opens with a big 3, 2, 1, GO! countdown.

## Build 58

- Hedge Maze: the unseen areas are now one soft-edged sheet of darkness that fades in and out smoothly and follows your character's real line of sight, instead of switching whole squares on and off. Your view also fades with distance.
- Hedge Maze: the exit flag no longer shows above the darkness before you can see the exit.

## Build 59

- Conveyor Chaos: the course is three times as long (24 belts instead of 8) and the camera follows you down it. The time limit is now 100 seconds.
- Conveyor Chaos: belt direction changes are staggered, so they no longer change in bunches early on.

## Build 60

- Conveyor Chaos: the belts in the second half of the course push twice as hard. They are a darker colour and their arrows move faster.
- Conveyor Chaos: computer players now line up before stepping on to a belt, so they can still finish.

## Build 61

- Lobby music: the page now tries to start it the moment it opens, and has the track loaded and waiting. Where the browser holds sound until the first touch, it starts on that touch.
- Special spaces: the painted icons are redrawn at twice the size and sharpened, fill more of each disc, have a thin dark outline, and stay sharp when the board is seen at a slant.

## Build 62

- Item shop: land exactly on the shop and you are given a random item for free. Passing the shop still lets you buy one.
- Computer players in mini games: their steering is eased, they turn smoothly instead of snapping round, and they no longer flick between running and standing.
- Hedge Maze: the darkness is drawn on a finer grid and blurred, so the edge between seen and unseen is a soft gradient.

## Build 63

- Hedge Maze: the maze is twice the size (16 by 16 tiles, up from 11 by 11), and the time limit is 100 seconds.
- Hedge Maze: there are now ten fixed mazes and one is picked at random each game. The game shows which one you are in. Their shortest routes run from 46 to 74 tiles, with the exit in a different place in each.

## Build 64
- **Online play has its own server.** `server.js` is a small Node server that serves the game and runs the join-code rooms over a web socket, so Host and Join work on any host that runs Node, not only inside the Claude artifact. The page uses the artifact's room service when it has one and the room server otherwise.
- Tested with three browsers in one room: two full rounds including two mini games, with identical game state on all three; a player leaving hands their seat to the computer; the host leaving ends the game for the others.

## Build 65
- **Three new mini games.** Hot Bomba and Musical Chairs are shared-platform games; Drum Beater is played on your own screen. All three are in the practice list, the mini game tester and the round rotation.
- **Hot Bomba.** Hot potato with a bomb. Everyone stands in a ring facing in and nobody walks. Tap anywhere, or the Pass button, to hand the bomb to the next player clockwise, after holding it for 0.4 seconds. The host picks a fuse of 5 to 15 seconds each round and never sends it; the phones only get the time gone by, which drives the ticking. Whoever holds it when it goes off is out, the ring closes up and a new bomb is lit. Each phone turns the ring so its own player stands nearest the camera.
- **Musical Chairs.** One chair fewer than the players left. While the music plays everyone is carried clockwise round the outside of a red line, so nobody can camp; crossing the line then puts you out at once. The host stops the music after 4 to 10 seconds and decides who reached each chair first. When it stops the track cuts out, the screen flashes and SIT! fills the screen.
- **Drum Beater.** Forty seconds, four lanes, four big buttons. Notes come from the shared seed, so everyone plays the same song. The drum beat is made in code at 120 beats a minute and booked on the audio clock, and the notes use the same clock, so they cannot drift apart. Perfect is within 65 ms (100 points), Good within 150 ms (50 points); every 10 in a row adds a quarter, up to double. Keyboard D F J K; controller d-pad left, d-pad right, X, B. In landscape the buttons sit in pairs at the two edges for the thumbs. Computer players get a random accuracy.
- **Drum Beater joins the round rotation.** Until now only shared-platform games came up in a round; the older own-screen games are still practice only.
- **Fixed, online:** a position left over from the previous mini game could make a player look knocked out on the other phones at the start of the next one. Positions and the host's game state now carry the number of the mini game they belong to. The host's game state can now be an object as well as a list.
- Every ready screen now has the Rules button, including the own-screen games.
- Three new game icons (g24 to g26), made in the same ChatGPT thread and style as the others.
- Tested: each new game in practice mode with computer players, landscape and portrait, to the results screen; the three games in a row online with three browsers in one room. Not tested: real phones, a real controller, and how the sound lines up by ear.

## Build 66
Speed. Measured on a laptop with built-in Intel graphics, a board frame took about 20 ms, which is over the 16.7 ms a 60-frames-a-second screen allows, and lowering the resolution barely helped. The time was going on the number of separate things drawn, not on pixels.
- **Characters are one mesh each.** A character model arrived as six skinned pieces, and every copy gave each piece its own skeleton, so one character cost six draws and six sets of bones a frame. The pieces are welded into one as the model loads: four characters now cost 4 draws, not 24.
- **Still scenery is welded together.** When a board is built, every plain coloured piece that never moves is merged into one mesh with its colour stored per corner. Spaces, icons, boats, clouds and anything an event can move, recolour or hide are left alone. Checked by playing four rounds on each board and confirming that none of the merged pieces would have changed.
- **Leak fixed.** Each mini game, and each preview of one, left 24 small textures and about 18 shapes behind on the graphics chip; a long game piled up hundreds. Scenes now free exactly what they made, including each character's bone data, and keep what is shared.
- **Shared materials stay loaded.** Ending a mini game used to throw away shared materials and shapes as well, so the next scene had to send them to the graphics chip again.
- Characters in the scene that is not on screen are no longer animated.
- The mini game timer and bar only touch the page when the number shown changes.
- The automatic resolution drop now starts when the frame rate falls below about 52 a second, not 42.
- Draw calls in the opening view of a board: Island 138 to 95, Carnival 152 to 117, Farm 152 to 128, Volcano 151 to 125.

## Build 67
Six races, the first batch from the 25-game brief. They share a way of describing a course (a smooth line, with every position measured as distance along and distance to the side) and a chase camera. Each has its own way of moving; none of them uses the walk-around movement of the older games.
- **Rail Riders.** No steering. Swipe a lever up and down; each full swing adds speed, long even swings and a steady rhythm add more. Every bend has a top speed worked out from how sharply it curves. Tight bends are painted red and signposted, and a bar shows your speed against the limit ahead. Too fast for 0.18 seconds and the car leaves the rails: 1.7 seconds lost and all speed gone.
- **Tricycle Turbo.** Two pedals that only count in turn; an even rhythm is worth 30% more. Steering is by sliding either thumb sideways on its pedal. Turn harder than the speed allows and the wheels skid: it runs wide and slows. Toy blocks in the road, always with a way past.
- **Marble Mayhem.** The stick is a push, not a direction. The marble keeps its speed, takes room to turn and stop, and gains speed on slopes. Narrow bridges, wide overtaking stretches, sliding bars, and marbles that knock each other. Over the edge means back to the last flag.
- **Shortcut Circuit.** Three laps of a closed tabletop circuit. The cars accelerate by themselves; steering makes the nose turn at once while the direction of travel catches up, and the slide costs speed. Three boosts. A narrow ruler bridge cuts off a loop of road and a jump cuts a corner; both drop you off the table if you miss. Two checkpoints make sure a lap can only be cut at the shortcuts.
- **Soapbox Surfers.** Forward speed is automatic. Leaning takes hold late, sideways speed carries on, and bends throw you outwards. Ducks spin you; bubbles give a burst of speed during which the soap answers even later.
- **Rapid Rafts.** One tap is one stroke. A stroke pushes forward and swings the nose away from that side, so alternating goes straight and is worth more. The river has a fast channel with most of the rocks in it, and whirlpools that drag the raft round.
- **Computer players use the same controls.** They produce lever swings, pedal presses, steering and paddle strokes, and the same physics turns those into movement. Each has its own skill, and the bold ones derail, skid, fall and hit rocks.
- **Any number of players from 2 to 6.** Start lines and course widths grow with the number of players. A finished vehicle no longer blocks anyone still racing.
- **Controls.** New on-screen controls for these games (lever, pedals, steering bar, paddle buttons), each with keys and a controller mapping. They appear only when the countdown ends and are removed when the game ends, however it ends.
- The ready screen shows one line on the controls for games that have their own.
- The host will not accept a reported result better than the game allows.
- Anyone who has not finished when the game ends is ranked by how far they got.
- Nine new game icons (g27 to g35) from the same ChatGPT thread; the last three are for games still to come.
- Tested: each race to the results screen with computer players, with 2, 4 and 6 players, landscape and portrait; every touch control with real touch events; three races online with three browsers in one room. Not tested: real phones, real controllers, and how the races feel in the hand.

## Build 68
- **Ghost Runner is replaced by Ghost Hot Potato.** A ghost possesses one player at a time. The possessed player is 13% faster and hands the ghost on by touching someone; the player who passed it cannot be tagged back for 1.6 seconds. Nobody is knocked out: possession time adds up for 40 seconds and the least wins. The host decides every tag from the positions it sees and keeps every player's clock, and its numbers are the result for everyone. A fence runs round the yard so nobody can fall off (and nobody can win by leaving).
- **Crab Scramble is replaced by Cannonball Kickoff.** Creatures round a pitch wind up and kick footballs across it. A ball knocks you back and leaves you safe for a moment; being knocked off the pitch is what puts you out. Balls get faster and more frequent, and later ones bounce once off the far rim. Everyone still on the pitch at 45 seconds shares the win. The pitch grows with the number of players.
- **Vacuum Escape.** Everyone runs down a bedroom floor by themselves and only steers. Toys are solid and every row has a way through, dust slows you, balls rolling across knock you back. The vacuum starts 10 m behind, never stops speeding up, and pulls harder the closer it is. First through the door wins; otherwise whoever got furthest.
- Where the host keeps the score itself (Ghost Hot Potato), a phone's own report cannot overwrite it.
- Game icons are renumbered now that two games are gone: g0 to g33.
- The code for Crab Scramble and Ghost Runner is removed, not just hidden.
- Tested: each of the three to the results screen with computer players, with 4 and 6 players. Ghost Hot Potato and Vacuum Escape online with three browsers. Not tested: real phones.

## Build 69
Three new boards. Each keeps the 60-space layout (a 45-space loop and a 15-space short cut) so every existing rule, item and computer player still works, and adds its own economy and spaces.

- **Melody Mansion.** The price of a pearl is 5, then 10, 20, 30, then 5 again; it moves on one step every time a pearl is bought. The Golden Note (the pearl stall) does not move after a sale. Only the Metronome space moves it, and that also changes the price. Piano Express and Brass Blast carry you across the room, Musical Mischief drops you on a blue or a red space. The short cut runs across the keys.
- **Pinball Paradise.** The classic rules: a pearl costs 20 and moves after each sale. Wheel of Wonder: bet 5, 10 or 15 tickets, press STOP, and the host draws the wedge (lose, half back, keep, x2, x3, x5). The Launcher fires you 6 to 16 spaces on, or onto the ramp, the Jackpot Zone or the Doom Zone. Flipper Frenzy moves you 5 on and bats nearby rivals onto the ramp. The ramp is the short cut and holds the Jackpot Zone (20 tickets, an item and 10, or a pearl) and the Doom Zone (lose tickets, an item, or a pearl).
- **Temple of the Golden Titan.** The pearl merchant stays on the summit for the whole game and sells as many pearls as you can pay for in one visit: buy 1, buy 2, or buy the most you can afford. Barrel Barrage knocks every rival on the climb back 5 spaces, the Jungle Vine swings you 7 up, Crumbling Steps slide you 6 back, the Ancient Lift takes you near the top for 3 tickets. In the last rounds there is an even chance of a Golden Rush, which drops the price to 5 for the rest of the game.
- The price is shown on a chip at the top of the screen and on a marker above the stall whenever it is not the usual 20.
- Computer players know the boards: they wait when the Golden Note costs 30 if they are ahead, take the ramp when they are behind, save for the summit and buy the most they can afford.
- The map picker shows all seven boards with a line about the one chosen. Each new board opens with a sentence on its rules.
- Art: 14 space icons, 24 scenery pieces, 3 map badges and 3 backdrops, all drawn for these boards. The metronome, pop bumpers, flippers and barrels are built in code so that they can move.
- Tested: full games with computer players on each new board with 2, 4 and 6 players and no errors; the wheel, the bulk purchase, the barrels and the metronome one at a time. Not tested: these boards on real phones, or online with more than one phone (the host sends its whole state, price and wheel included, so the phones draw what the host decided).
- Known limits: the boards are flat, so the temple climb is a route across the island, not a real height change. The new boards share the existing board music.

## Build 70
Thirteen new mini games, which finishes the list of 25 (three were left out as too close to games already here: Domino Dash, Giant Slam and Treasure Tide).

**Nine own-screen games.** Everyone plays the same puzzle, built from the round's seed, on their own phone. A computer player is scored by playing that same puzzle with a skill level.
- **Critter Wrangler.** Draw a closed loop round wandering critters: 1 point each, 3 for a gold one. The ink runs out, so a loop cannot take in the whole garden.
- **Dress for Success.** Remember who is wearing what, then pick that outfit out of look-alikes. More characters, more cards and closer look-alikes as it goes on.
- **Candy Detective.** Find the exact sweet the shopkeeper asks for in a crowded jar.
- **Hedge Hustle.** Five hedges: swipe leaves away, rub ladybirds off, keep your finger away from the bees.
- **Chalkboard Drop.** Three falls on an elastic cord. One tap to brake; the cord takes room to stop you. Closest above the red line scores most.
- **Matchstick Marksman.** Pull a bow back, aim and let go. Big villains 100, small ones 20, friends cost 30.
- **Twist and Route.** Turn road tiles so a wind-up car can drive from the start to the flag. Every board can be solved.
- **Sky Shapes.** Steer a skydiver through the gate with the right shape and colour, five times.
- **Limelight Shuffle.** On each marked beat press Sun if a spotlight is on you and Moon if it is not. (The brief called it Spotlight Shuffle; there is already a game called Spotlight.)

**Four shared games.**
- **Snapshot Showdown.** A hedge maze where everyone has a camera. Hold another player in view until the camera has focused, then snap. First to photograph everyone wins.
- **Crater Crawl.** Tap to climb a volcano wall, change lane to dodge vents that erupt, squeeze past climbers who block you, and stay ahead of the rising lava.
- **Pixel Panic.** A race across tiles that vanish after anyone steps on them and grow back a few seconds later. A fall sends you back to the last checkpoint.
- **Clockwork Climb.** A side-on race up a clock: turning gears, sliding and retracting bars, pendulums. Every ledge can be jumped up through.

Also in this build
- All nine own-screen games are in the round rotation, which now has 39 games.
- The playfield of the older own-screen games (Ticket Catch, Pier Dash, Balloon Pop and the others) had collapsed to a thin line on a phone held sideways. It now takes the room there is.
- The ready screen of an own-screen game shows one sentence and the control hint; the full rules are behind the Rules button.
- Shuffles that decide a puzzle use the game's own seeded shuffle, because sorting with a random test gives different results in different browsers.
- Thirteen new game icons, g34 to g46.
- Tested: each of the thirteen to the results screen with computer players, in landscape and portrait. The own-screen games with a scripted player that used the real touch controls. The four shared games with 2, 4 and 6 players. Every Twist and Route board from 2,000 seeds checked for a solution. Online with three browsers: Twist and Route and Limelight Shuffle started with the same puzzle on every phone and were played through; the run was too slow here to collect the final tables for them. Not tested: real phones, sound, controllers.
- Known limits: own-screen races do not show the other players while you play. Snapshot Showdown does not use "fewer times photographed" to break ties. Sky Shapes and Limelight Shuffle have keyboard controls; the other new own-screen games are touch and mouse only.

## Build 71
Music and sound after leaving the browser and coming back.

- Before: leaving the page paused the sound and coming back asked for it once. If the phone was not ready at that instant, nothing asked again, and the only touches listened for were the start of a touch, which a phone does not count as permission to make sound. The music could stay off for the rest of the game.
- Now, while the page is showing, the game checks a few times a second that the sound clock is really moving. If the sound is suspended it asks again, about once a second. If that fails three times, or the sound says it is running while its clock stands still, the sound system is thrown away, a new one is built and the music starts again.
- The end of a touch, a click and a key press are listened for as well as the start of a touch, so where the browser insists on a touch, the first one after coming back is enough.
- Coming back is noticed three ways (the page becoming visible, the page being shown again, the window getting focus), because not every browser sends all three.
- Drum Beater and Limelight Shuffle keep time by the sound clock. If that clock stops in the middle of a song they carry on by the ordinary clock, so the game still ends.
- Tested in a desktop browser with the faults made on purpose: leave and return (music back at once), six quick leave-and-returns, a sound system that refuses to resume (music back in 3 seconds), a stuck clock (back in 5 seconds, or at the next touch), and the sound system replaced in the middle of Drum Beater (the game finished). Not tested: a real iPhone or Android phone, where this fault actually happens.

## Build 72
The board when playing online on phones.

What was measured first
- On a laptop the game needs about 10 to 12 ms a frame, the same whether hosting, joined or playing solo. The slowness reported was on phones, on the board, in online games only.
- On the board a joined phone shows what the host's phone tells it, through the room server. From New York, one message from one phone to another through the server (which is in the US West region) took 92 ms. A tap on a joined phone therefore took about a quarter of a second to show: there and back through the server, plus up to 90 ms that the host waited before sending, plus a pause the dice roll has built in.
- Steps of a moving piece reached a joined phone unevenly, so the piece stopped and started. In a model with ordinary phone wifi, about half of all moves had at least one stop.

What changed
- The host sends each step of a move the moment it happens, sends at once after any phone's answer, and otherwise checks for changes every 45 ms, not every 90.
- A joined phone waits a moment at the start of a walk to have a step in hand, then walks at the host's pace and only hurries if it falls behind. In the same model, moves with a stop fall from about half to about one in eight. The legs keep moving through a short wait when more steps are known to be coming.
- Your own dice hit shows at once on a joined phone; the number follows when the host has rolled it.
- Every phone in a room sends a tiny message about seven times a second when it has nothing else to say. A phone that sends nothing lets its radio doze and then hears from the host late. The server sends the message straight back, which gives the delay.
- Settings now shows a line: frames a second, the slowest frame, and when online the delay to the server and back. It is there to tell a slow phone from a slow connection.

Not changed, and the biggest remaining cause: the room server is in the US West region. Moving it to a region near the players would cut each message from about 92 ms to roughly 20.

Tested: full board games solo; an online game with two browsers (host and joiner agreed on the board and finished with the same scores); the walking model with three kinds of connection. Not tested: real phones.

## Build 73
A new look for the boards, starting with Island: a small 3D model of a place, not pictures stood on a flat plane.

The standard
- Scenery is solid: rounded shapes with thickness, soft plastic and painted wood, no dark outlines and no flat cut-outs. Navy outlines stay on the scoreboard, icons and the selection ring.
- A warm low sun with soft shadows, a cool fill light, and every prop shaded darker where it meets the ground.
- The ground has height. Pieces, the dice, markers, effects and the camera all stand on it.
- Things move: palms and flags sway, the sea rolls in, boats and buoys bob, gulls circle, the pearl glows.

The kit (in index.html between the TOY3D markers; any board can use it)
- Shapes: rounded boxes, turned shapes, bent tubes, thick leaves, lumpy rocks, bevelled outlines.
- Kit: gathers any number of coloured pieces into one mesh, so a whole board's scenery is two or three draws. It shades the foot of each prop and marks the parts that sway.
- Materials: matte (wood, leaves, cloth), gloss (toy plastic with reflections from a small painted sky), land and sea.
- Ground: worked out from the board's own path, so it fits any loop. Beaches of uneven width, a plateau that lifts parts of the path, flat-topped hills with rounded cliffs, and on tide boards a sandy channel cut from sea to sea. Sand, grass and rock are chosen per pixel, so the edge of the grass is a clean line.
- Sea: one sheet coloured by the depth of the ground under it. Clear over the shallows, deep blue further out, foam riding in to every shore, bright lines drifting across.
- Models from Blender can replace any prop: toyGLB() loads a .glb once and hands out copies. See ART-DIRECTION.md.

Island
- Sand rising out of the sea to a grassy plateau on the west side, a two-level hill with a hut on top, a cove behind with two huts on stilts and a pier, a wide beach at the front with the start deck, umbrellas, towels, surfboards and a sandcastle.
- The path is a boardwalk that climbs and falls with the ground. The short cut runs down into a dry channel. When the tide comes in the channel fills with water from the sea and the main path crosses it on two rope bridges.
- Spaces are glossy buttons set in white rings, with their colour and picture printed on the cap. Pearl spaces have a lavender ring.
- Around it: seven small islands, a lighthouse, four sailing boats, buoys, gulls, shells and starfish on the sand, flowers on the grass, party flags.
- Tall props are placed so that, as the game camera sees them, they never cover a space.

Every board
- The pearl stall is a big pink clam with a glowing lavender pearl. It breathes, opens wide when the camera visits or a pearl is bought, and when it moves it snaps shut, vanishes in sparkles and pops open at the new space.
- The dice is a rounded die with pips. It bobs as it spins and lands with a bounce.
- Pieces stretch as they leap, squash as they land and kick up dust. Tickets fly between a piece and its card on the scoreboard, and the card bumps when they arrive. The card of the player whose turn it is glows.
- Tapping a space picks the one whose top the tap passes closest to, at any height, and the ring round it pulses.

Speed
- Island is about 150,000 triangles in under 100 draws. Shadows are drawn at half detail on phones. If the game is still slow at its lowest sharpness, real shadows switch off and the soft blobs come back.
- Smoothing of edges is on for ordinary desktop screens.
- Soft shadows read the shadow picture 9 times a pixel, not 17, and the sea reads its wave picture 3 times, not 6. Both look the same and are cheaper on laptop and phone graphics chips.

Not changed: rules, turns, dice, spaces, tickets, pearls, mini games, online play. The other six boards keep their old scenery for now, with the new clam, dice and effects.

Limits
- Colours are still drawn the old way (no gamma step), because changing it would alter every board and mini game at once.
- All scenery is built in code. It is rounded and shaded, but hand-made models would be richer.
- The sky is still the painted picture behind the scene.

Tested: Island built and viewed on a desktop screen and a phone screen; full four-round solo game with no errors; the tide; the other boards and two mini games still run. Not tested: real phones.

## Build 74
An introduction before the first turn on every board.

What players see (full length, about 11.5 seconds)
- A flight in over the board, with its name.
- The one rule that makes the board different, on a card, while the camera circles the place it happens. On Island the tide really comes in; on Carnival the wheel spins up; on Volcano it erupts. Each line was checked against the rules in the code.
- The first pearl: the camera goes to the stall's real space for this game, the clam opens, rings of light spread from the space, and the card gives the distance from the start and the price.
- The camera settles into the game's own view. There is no cut and no fade: it is the same camera.

How it is built
- Flown live through the real board, timed by the clock so a slow phone takes no longer. One entry per board in INTRO.boards.
- A board can name a recorded film for the first two parts. The film player is built and tested (plays over the scene, words stay in step, dissolves into the live scene, falls back to the live flight on any failure). No films have been made, so none is switched on. INTRO-VIDEOS.md has the specification, the shot plan and a tool that records a film from the game.
- Length is each player's choice in Settings: full, quick (about 5 seconds: the rule and the pearl) or skip. A Skip button ends your own introduction early.
- Settings also has Board overview, which replays the flight, the rule and where the pearl is now, at any time in a game.

Online
- Each phone plays its own introduction, then tells the host it is ready. The host starts the first turn when every player is ready, or after 21 seconds. Until then a phone that has finished shows who it is waiting for. One player skipping never pulls the others in early.
- The pearl's space comes from the host's game state, which every phone already had before the introduction, so all phones show the same space.
- A phone that arrives late and finds the game already begun jumps to the end of its introduction.
- The fixed wait of 6 to 7 seconds at the start of every game is gone.

Loading
- Nothing the board needs is fetched when a game starts: the board is built in code and the characters and props are fetched when the page opens. The introduction waits for the characters, the props (on boards that use them) and the fonts, and if they are late it holds its last shot with "Preparing the board…" for up to 7 seconds, then goes on with the stand-ins the game already has.
- server.js can now send part of a file, which phones need to play films.

Tested: the full, quick and skip lengths on Island on a desktop and a phone screen; the rule and pearl shots on Carnival and Volcano; an online game with a host who skips and a joiner on full, and the other way round (both waited, both saw the same pearl space); the film path with a test film and with a missing film; Board overview; a full solo game. Not tested: real phones.

## Build 75
Carnival rebuilt to the Island standard, and the kit made ready for boards that are not islands.

Kit
- A board can now stand on a deck: the planks are drawn by the floor's own material, so one slab is enough.
- Path styles: any colours for the planks of the main path and the short cut. The short cut is laid on boards without a tide.
- A fourth kind of piece: things that give light (bulbs, later lava and neon). They are unlit and twinkle out of step.
- Each board can tint its own sun and fill light.
- Where spaces change colour during play (the volcano's lava) each space has its own material, so the old rule code still works.

Carnival
- A fairground on a wooden pier in the shape of the path, standing on piles in the sea, with a rope rail and lamps strung with coloured bulbs.
- The big wheel is larger and keeps the ride exactly as it was (the ride is drawn from the wheel's own size and place). Bulbs round its rim, gondolas that stay upright.
- A carousel and a swing ride that turn, a helter-skelter, three striped show tents, prize stalls with bulbs and prizes, snack carts, a giant bear, benches, flower tubs, balloon bunches, boats, buoys and gulls.
- A red plank path with a yellow short cut. Rides stand on painted star mats that stay clear of the path.
- Golden evening light.

Tested: Carnival built and viewed on a desktop screen; game view; a full three-round solo game with no errors. Not tested: real phones.

## Build 76
Farm rebuilt to the Island standard.

Kit
- Ground that is not an island: land in every direction, with low hills rolling away to the horizon and trees on them. Ponds anywhere the ground is low. Each board names its own colours for soil, grass and rock.
- A smooth dirt track as a path style.

Farm
- Rolling countryside. The path is a dirt track that rises and falls; the short cut is a plank walk.
- A windmill whose sails turn stands behind the middle of the board, a red barn with a silo in its yard, a paddock with cows, fields of crops and pumpkins with a scarecrow, an orchard along the back, a duck pond at the front with ducks that paddle.
- Inside the path: fruit trees, a tractor, hay bales, a well, sheep and hens. A white rail fence follows the outside of the path, with flower meadows and bushes around.

Tested: Farm built and viewed on a desktop screen; game view; a full three-round solo game. Not tested: real phones.

## Build 77
Volcano rebuilt to the Island standard.

- A dark rock island in a bright sea. The path is dark stone, the short cut red stone on a spit of rock at the front.
- The hollow the path circles is a lake of lava: slow bright currents under a drifting dark crust. Lava pools use the same material.
- The volcano is larger, with lava running down its sides, smoke from the crater and a glow that lights the ground round it. Eruptions shake it, light it and throw lava exactly as before, and the lava that floods beside a burning stretch of path is unchanged.
- Old ruins (arches and columns), glowing crystals, smoking vents, dead trees and dark rocks, on the island and on the small islands out at sea.
- Dusk light: a low warm sun and a violet fill.
- Each space has its own material here, so a burning stretch still darkens and glows space by space.
- On every board the START board now stands on whichever edge of the start deck is nearest the camera, and the sparks of an eruption and the confetti are round and glowing, not square dots.

Tested: Volcano built and viewed on a desktop screen; a full three-round solo game. Not tested: real phones.

## Build 78
Melody Mansion rebuilt to the Island standard.

- The board is laid on a woven rug on the floor of a huge music room; to the players everything else is enormous. The floorboards are wider than a player.
- A grand piano with its lid propped open stands behind the board, with a light that hops from key to key as if someone were playing. Round the rug: a drum kit whose cymbals rock, two speaker stacks, a guitar on its stand, a xylophone, a gramophone, two trumpets, a piano stool, an armchair and a floor lamp.
- The room has walls: striped paper over panelling, a skirting board, a window with curtains, framed pictures, a wall socket and a mouse hole.
- The path is ivory boards. The short cut, 'Across the keys', is a keyboard with black keys along it.
- Small instruments lie on the rug inside the path: records, tambourines, bongos, maracas, a harmonica, triangles, drumsticks and guitar picks.
- The metronome is a 3D model. The rules still swing its arm, and it still races when it is about to move the Golden Note.
- The Golden Note beside the pearl is a glowing 3D note that turns, not a flat picture. Coloured notes hang in the air over the instruments.

Tested: Melody Mansion built and viewed on a desktop screen and a phone-sized screen; a full three-round solo game (Golden Note, metronome, Piano Express, Brass Blast all seen). Not tested: real phones.

## Build 79
Pinball Paradise rebuilt to the Island standard.

- The board is the playfield of a huge pinball machine: a lacquered blue board with a painted starburst, red cabinet walls with a chrome rail, a row of bulbs and two neon tubes, an arched top, an apron with score cards at the front, and a lit back box with the board's name.
- The centre ramp really is a ramp. The short cut climbs, runs level above the board and comes down again, on yellow boards with chrome wire rails, posts and neon edges. The Jackpot Zone and the Doom Zone each have an arch over the ramp with a lit name board.
- Pop bumpers and flippers are 3D models. The rules still make a bumper jump and the flippers snap exactly as before.
- A chrome ball sits on the plunger at the bottom right. The plunger draws back, fires it up the right-hand lane, and it rolls round the arch and down the left-hand lane into a hole, then comes back.
- A Wheel of Wonder stands at the top of the table and turns. Its wedges are the real wheel's wedges, in the same order and sizes.
- Chrome balls, drop targets, star posts, rollover lanes and lamps set into the board. Arrows of light run round the outside of the path in the direction of play.
- Round the machine: an arcade carpet far below, and other machines glowing in the dark.
- Night light: cool and violet, with the lamps doing the work.

Tested: Pinball Paradise built and viewed on a desktop screen; a full three-round solo game (Wheel of Wonder bets, flipper launches, Jackpot Zone and Doom Zone all seen). Not tested: real phones.

## Build 80
Temple of the Golden Titan rebuilt to the Island standard. All seven boards are now 3D toy models.

- A jungle island that really climbs: the path rises from the beach in the south to a paved summit terrace in the north, with rock shelves and ruins inside it.
- The Golden Titan stands behind the summit: chest and shoulders rising out of the rock, arms laid forward so the terrace sits between his hands, gold headdress, shoulder plates, wrist bands and chest medallion, moss and vines. His head turns slowly and his eyes glow. When Barrel Barrage is played his jaw drops and his head shakes while the barrels roll.
- A waterfall falls into a rock basin on each side of him, with spray.
- On the summit: a stone gate, torches, a treasure chest, heaps of gold, and a brazier burning in each of the Titan's hands.
- The loop is a stone path ('Stone stairs'). The short cut is a wooden walkway with rope rails ('Vine path').
- Beside the special spaces: barrels at Barrel Barrage, a vine at Jungle vine, a broken column at Crumbling steps, a golden idol at Golden idol.
- The barrels the rules roll down the climb are 3D and follow the slope.
- Palms, round trees, big-leaf plants, bushes, flowers, old columns, arches and broken walls, on the island and on small islands out at sea.
- The introduction camera now looks at the Titan over the summit on this board, and across the whole table on Pinball Paradise.

Tested: Temple built and viewed on a desktop screen; a full three-round solo game (Barrel Barrage with players knocked back, Jungle vine, Golden idol all seen). Not tested: real phones.

## Build 81
Mini games: real 3D scenery round the platform, and a results ceremony.

- Eighteen mini games that are played on a platform no longer stand on a flat painting. Each now has scenery built from the same kit as the boards, lit the same way, with soft shadows:
  - Boom Hop: the deck of a ship, with rails, cannons, barrels, crates, a coil of rope, a life ring, a mast with a striped sail and a bowsprit, on moving water.
  - Coconut Drop and Sumo Shove: a lagoon with sand bars, palms, a hut, rocks and buoys, and the platform on wooden piles.
  - Ticket Grab, Paint Fight, Stomp, Trap Doors, Cannonball Kickoff and Snapshot Showdown: the fairground, with tents, stalls, a high striker, a cart, lamps strung with bulbs, balloons, planters, benches and confetti.
  - Musical Chairs: a music room, on a rug, with a piano, drum kit, speakers, guitar, xylophone, gramophone and notes in the air.
  - Spotlight: a theatre, with curtains, lighting rigs, footlights and rows of seats.
  - Lantern Match and Ghost Hot Potato: a harbour at night, with lamp posts, boats carrying lanterns, lanterns afloat, fireflies and a lighthouse.
  - Slippery Slope: a frozen lake, with pines, snowmen, an igloo, snow banks, ice crystals and a sled.
  - Hot Planks, Crumble Deck and Hot Bomba: inside the volcano, on moving lava, with rocks, crystals and ruins.
- If the scenery for a game cannot be built, the game falls back to its old painted surround and plays as before.
- Mini game results: the rows pop in from first place to last, the winner's row glows gold, confetti falls and the fanfare plays.
- The introduction on the Temple board now frames the Titan's head.

Not changed in this build: the ten racing and climbing games that build their own course (Rail Riders, Tricycle Turbo, Marble Mayhem, Shortcut Circuit, Soapbox Surfers, Rapid Rafts, Vacuum Escape, Crater Crawl, Pixel Panic, Clockwork Climb), Conveyor Chaos and Hedge Maze, the eight tap-and-timing games (Bell Ringer, Ring Toss, Ticket Catch, Lighthouse, Crab Count, Pier Dash, Balloon Pop, Crate Stack), Drum Beater and the nine games with their own screens (Critter Wrangler to Limelight Shuffle). They play and look as before.

Tested: all eighteen games started in practice on a desktop screen with no errors and looked at; two on a phone-sized screen; one played to its results. Rules, scoring and controls are untouched. Not tested: real phones, online play.

## Build 82
The rest of the Full Game Visual Overhaul: every mini game now plays in a 3D scene, plus the award ceremony, the results and character reactions.

Course games (scenery down both sides of the course, never on it; rules, tracks and timing untouched)
- Rail Riders: big pines, snowmen, igloos, ice crystals and snow banks.
- Tricycle Turbo, Vacuum Escape and Shortcut Circuit: a playroom, with block towers, ring stacks, crayons, presents, balls, books, teddies and balloons.
- Marble Mayhem: the factory floor far below, with turning gear wheels, robot arms, pipes, crates and warning lamps.
- Soapbox Surfers: moving water, sand bars with palms, rocks, buoys and float rings.
- Rapid Rafts: trees, bushes, toadstools, rocks and flowers along the banks.
- Crater Crawl: crystals, broken columns, arches and dead trees beyond the boulders.
- Pixel Panic: neon arches over the grid, shapes turning in the dark, a grid of light far below and coloured stars.
- Clockwork Climb: brass wheels turning on the back wall, pipes, wall lamps and a clock face with moving hands at the top.
- Conveyor Chaos: the painted floor is replaced by a real factory floor with presents, block towers, crates, belts, pipes and robot arms.

Tap and timing games (the flat blue panel is gone; each is played in a scene that answers to the game)
- Bell Ringer: a fairground high striker. Every tap knocks the puck up the tower; tap fast enough and it rings the bell.
- Ring Toss: a stall with a peg on a table. A ring slides to and fro above it in step with the marker; Toss drops it where it is.
- Lighthouse: a lighthouse on a rock at night. Its lamp is dark until the signal, then it blazes and sweeps its beams.
- Crab Count: the crabs are 3D and run out onto a real beach, in exactly the places the game chose.
- Ticket Catch: the tickets, the red crates and the basket are 3D objects, placed exactly where the game puts them, in front of a stall.
- Pier Dash: moving water, sand bars with palms, buoys, rocks and pier posts.
- Balloon Pop: the fairground behind the balloons.
- Crate Stack: a wooden dock with crates and barrels, boats, a lighthouse and palms.

Own-screen games
- Drum Beater: sand bars with palms, speakers, a gramophone and notes round the drum island.
- Limelight Shuffle: theatre curtains, lighting rigs and footlights round the stage.
- Critter Wrangler, Hedge Hustle (meadow), Dress for Success (theatre), Candy Detective, Matchstick Marksman (fairground), Chalkboard Drop, Twist and Route (playroom) and Sky Shapes (clouds, floating islands and balloons): each is now set in a 3D scene in place of the painted stall. Their play areas are still the 2D drawings they were designed as.

Shared
- Platform games open with the camera sweeping in from the side during 3, 2, 1.
- The award ceremony is on a theatre stage: plank floor, red curtains with gold pelmets, lighting rigs, footlights, gold stars and balloons.
- Final results: rows pop in, the winner's row glows gold, confetti falls, the fanfare plays and the winner's piece cheers on the board.
- Characters use two animations they already carried but never played: they flinch when they lose tickets on the board or are knocked out of a platform game, and cheer when they win 8 or more tickets at once.
- If any scene cannot be built the game falls back to what it showed before and plays on.
- Online play: a phone that started slowly could find Host and Join greyed out for good, because the room connection was tried once, for four seconds. It now keeps trying for about half a minute and switches the buttons on when it gets through.

Hedge Maze is unchanged on purpose: the dark round the maze is its rule (you only see where you have been).

Tested: all 47 mini games started in practice on a desktop screen with no errors and looked at; four tap games at phone size; the award ceremony and final results played through; an online game on three phones with a computer player through four mini games (results and seed identical on every phone, no errors). Not tested: real phones.

## Build 83
Kite, pearl stall and mini game edges: rules fixed at the root, and the Kite gets its flight.

The Kite is rare now, and its rarity is set in one place
- Every way an item reaches a player now reads one table, `RARITY` (in the code under "ONE TABLE FOR EVERY ITEM"): item spaces, the free item for stopping at a shop, the Mystery Box, the Jackpot Zone and the shop shelf.
- What was found: an item space gave a Kite 15% of the time, the Mystery Box and the Jackpot Zone 40%, every shop always sold one for 15 tickets, and a computer player could buy one at the start of any turn from anywhere on the board.
- Now: item space 4%, shop gift 2%, Mystery Box 6%, Jackpot Zone 10%. The shop puts a single Kite on the shelf on about one round in four, for 25 tickets. A player can hold one Kite at a time. At most 1 Kite reaches the players in a 5-round game, 2 in a 10-round game and 3 in a 15-round game, counted across every source.
- The shop has a shelf that is refilled each round and shared by all three shops: 3 Twin Dice, 2 Magnets and, some rounds, 1 Kite.
- Computer players buy at the shop like everyone else. They no longer buy from anywhere.

The Kite flight
- Using a Kite is now a film in five parts: the kite sails down out of the sky with its string trailing; the player watches it, hops and catches the string, and the kite dips as it takes the weight; a gust lifts them; they fly over the board to wherever the pearl stall stands, swinging underneath, with the camera travelling alongside; they are set down by the stall with a bounce and a cheer while the kite flies off.
- The kite is a 3D toy: four bright cloth panels that flutter, a face, a tail of bows that streams behind it, a string that ripples while it hangs loose, and streaks of wind in flight.
- The path is worked out from where the player stands and where the stall stands at that moment, and it climbs over whatever ground lies between (the Temple statue, the Pinball ramp).
- It is safe by construction. The player's place changes the moment the Kite is used and the Kite leaves the bag at the same moment; the film is only a film. So nothing along the way is set off, a dropped connection or a skipped film cannot leave anyone between spaces or pay out twice, and the offer of a pearl is made after landing against the place the stall stands then.
- Every phone shows the same flight, each working it out from the host's one message. The flier (or the host, for a computer player) can tap Skip.
- The film runs by the clock, so a slow phone does not fall behind the game.

The pearl stall
- One function, `pearlStop`, now decides when a pearl is offered. Walking past the stall, stopping exactly on its space, arriving by cannon, pipe, wheel, piano, trumpet, flipper or Kite, and starting a turn while standing on its space all go through it.
- What was wrong: the offer was only made at the moment of arriving. A player who stopped on the stall's space without enough tickets, or who was standing there when the stall moved to them, was never asked again, even after winning tickets in the mini game. They had to walk away and come round again.
- Now a player standing on the stall's space who can pay is offered the pearl at the start of their turn. Nobody is asked twice in a turn, saying no is respected, and where the stall stays put (Melody Mansion, the Temple) buying once is all a visit allows.
- Not enough tickets: the player shakes their head, "Need 8 more" floats up, and the message says the price and what they hold. The stall only moves after a sale.
- A gold ring on the ground marks the one space the stall belongs to.

Mini game edges
- Every platform game now has a stated rule for its edge (`edgeRule`): fall, wall or none. A game that is not listed gets a wall, so no game is knocked out at the edge just for using the shared platform.
- What was wrong: one line in the shared platform code knocked out anyone who stepped past the rim, in every game that used it. That included Ticket Grab, Spotlight, Paint Fight and Ghost Hot Potato, whose own rules say nobody is knocked out.
- Wall (the rim stops you, and a hard shove into it bounces back): Boom Hop, Ticket Grab, Hot Planks, Coconut Drop, Spotlight, Sumo Shove, Paint Fight (the hole too), Stomp, Trap Doors, Lantern Match, Musical Chairs, Ghost Hot Potato.
- Fall (staying on is the game): Slippery Slope, Cannonball Kickoff, Crumble Deck. Even there nobody can fall in the first second, and being over the rim for a single stray frame no longer counts.
- Unchanged: the mazes and the bomb ring have no rim, and the course games already put you back at the last flag.

Checked
- Pearl stall, on Island, Melody Mansion and the Temple: passing, stopping exactly, not enough tickets, waiting on the space and then being able to pay, saying no, arriving by Kite, a skipped Kite.
- Kite odds measured over 40,000 draws per source; none past the cap; never a second one in the same bag.
- Two phones online: the joined player used a Kite and bought the pearl; both phones showed the flight and ended in the same state.
- Fifteen platform games: a player was walked straight at the rim. The twelve wall games held them; the three fall games dropped them.
- Screenshots of the flight on the Island (desktop) and the Temple (phone).

## Mini games

**Shared deck (everyone on one deck at once)**
Boom Hop, Ticket Grab, Hot Planks, Coconut Drop, Spotlight, Sumo Shove, Hedge Maze, Paint Fight, Crumble Deck, Stomp, Trap Doors, Slippery Slope, Conveyor Chaos, Lantern Match, Hot Bomba, Musical Chairs, Rail Riders, Tricycle Turbo, Marble Mayhem, Shortcut Circuit, Soapbox Surfers, Rapid Rafts, Ghost Hot Potato, Cannonball Kickoff, Vacuum Escape, Snapshot Showdown, Crater Crawl, Pixel Panic, Clockwork Climb.

**Own screen (everyone plays at the same time, separately)**
Bell Ringer, Ring Toss, Ticket Catch, Lighthouse, Crab Count, Pier Dash, Balloon Pop, Crate Stack, Drum Beater, Critter Wrangler, Dress for Success, Candy Detective, Hedge Hustle, Chalkboard Drop, Matchstick Marksman, Twist and Route, Sky Shapes, Limelight Shuffle.

## How it is tested

Tests run in a headless browser with no graphics chip:
- Every mini game is played to the end with random input.
- A full game with computer players is played on each of the seven maps.
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
