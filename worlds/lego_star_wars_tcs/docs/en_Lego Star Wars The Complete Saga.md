# Lego Star Wars: The Complete Saga

This Archipelago randomizer implementation is playable, but is a work in progress. This notice will be removed once the
logic has been rewritten from scratch, into a format that is more suitable for Archipelago.

## What does randomization do to this game?

Story mode is skipped for Chapters within an Episode, which should always be played in Free Play.

To unlock a Chapter, all Story Mode characters for that Chapter must be acquired. Optionally, an Episode Unlock item
must also be acquired.

The player always starts with the items necessary to enter their starting Chapter.

## What items and locations get randomized?

### Items
Characters, Extras (that require a Power Brick) and Minikits are in the item pool.

Score Multiplier Extras are replaced with Progressive Score Multiplier items that unlock more Score Multiplier Extras
the more Progressive Score Multipliers are acquired.

Purple Stud items are added to the item pool to fill out the rest of the item pool.

### Locations

Making purchases from the Characters or Extras shop are locations to check.
The Extras that can be purchased without collecting a Power Brick are not currently location checks.

Completing an Episode Chapter in Free Play is a location to check. Additional checks can be sent for each Story mode
character that would have been unlocked if the Chapter had been completed in Story mode.

Completing the True Jedi for a Chapter is a location to check.

Every 1-10 number of Minikits collected in a Chapter is a check.

Completing Bonus levels and watching the Indiana Jones trailer can be locations to check.

## What other changes are made to the game?

Purchases in the Characters shop and Extras shop will not award their vanilla Characters/Extras.

Slots in the Characters shop that would normally unlock upon completing Story mode in every Chapter have been changed to
either unlock once all enabled Episodes are unlocked, or once a number of 'All Episodes Token' items have been received.
The unlock condition is controlled by an option in the game yaml.

## What does another world's item look like in Lego Star Wars: The Complete Saga?

All items display as they would in vanilla.

## When the player receives an item, what happens?

The item is immediately added to your unlocked Extras/Characters/Stud count. A text display in-game may show what the
received item was.

Studs are added to your total accumulated Studs rather than your in-level Studs, so the effect of receiving Studs is
not noticeable without returning to the Cantina. The received studs are multiplied by your maximum possible score
multiplier.

## Can I play offline?

No, a connection to the Archipelago server is required to receive items, even in a single-player multiworld.

If the connection to the Archipelago server is lost temporarily, it is possible to continue playing. Any checked
locations while disconnected will be sent once the connection is reestablished.

## Known Issues

### Logic

The logic is quite basic and may have issues. Work is ongoing to rewrite the logic to fix issues and enable more
randomization options, such as individual Minikit logic and different unlock requirements for Chapters.

### Cantina Episode door lights

If you are in the main room of the Cantina when you unlock your first Chapter in an episode, the red lights above the
episode door won't change to green, but the door can still be entered normally. The lights will become green the next
time you enter the main room of the Cantina.

This will happen whenever your starting Chapter is from any Episode other than Episode 1.

#### Episode 1 door in new save files

When starting a new save file and connecting to the Archipelago server, the door to Episode 1 will start, and remain
unlocked until you re-enter the main room of the Cantina.

### Starting Characters

Characters are added to starting inventory to be able to access the starting Chapter. The world's current logic assumes
the player has a Jedi and a Protocol droid because the logic was designed around always starting with 1-1, so if the
starting characters do not include a Jedi and a Protocol Droid, a Jedi and/or a Protocol Droid (usually TC-14) will be
added to the starting characters.

### Player 2 picking locked characters

When loading a save file for the first time, it is possible for Player 2 to load in as Obi-Wan Kenobi or swap to Qui-Gon
Jinn, even if those characters should be locked. Upon entering a Chapter in Free Play, Player 2 will continue using that
character despite the character being locked.

When entering a Chapter in Free Play with only one Character unlocked for that level type (vehicle/non-vehicle), Player
2 will pick a locked Character.

Locked characters should not be used until they are actually unlocked.

### In-game messages

Dying while a received item/checked location message is displayed will cause you to lose studs, but no studs will spawn
to be picked back up.

Collecting studs while an in-game message is displayed will play the sound for collecting Blue/Purple studs, but the
received value of the collected studs will be normal.

In some cases, the Double Score Zone background audio can start playing when in-game messages are displayed.

### 'All Episodes' Character unlocks

Because the AP randomizer changes the unlock condition for the slots in the Characters shop, that would normally unlock
upon completing Story mode in every Chapter, there may be a small delay before the purchase will be allowed, and other
slots in the shop may appear to be unlocked while making the purchase.

### Purchasing already unlocked Characters/Extras

When attempting to purchase a Character/Extra that has already been unlocked, by receiving that Character/Extra from
Archipelago, there may be a small delay before the purchase will be allowed because the client has to temporarily
disable that character to allow the purchase to go through.

### Purple Studs

Receiving a Purple Stud item adds the studs directly to your save data, the stud counter that is visible in the Cantina.

Receiving a Purple Stud while in a level will not add it to your in-level stud count or contribute to True Jedi
progress.

Receiving a Purple Stud while under the effect of a Power Up, or while in a Double Score Zone will not double the
received studs.

## Credits

- maybejess: manual apworld reference
- Roushmore: manual apworld reference