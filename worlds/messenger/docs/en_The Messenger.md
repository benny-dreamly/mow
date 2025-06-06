# The Messenger

## Quick Links

- [Setup](/tutorial/The%20Messenger/setup/en)
- [Options Page](/games/The%20Messenger/player-options)
- [Courier Github](https://github.com/Brokemia/Courier)
- [The Messenger Randomizer AP Github](https://github.com/alwaysintreble/TheMessengerRandomizerModAP)
- [PopTracker Pack](https://github.com/alwaysintreble/TheMessengerTrackPack)

## What does randomization do in this game?

All items and upgrades that can be picked up by the player in the game are randomized. The player starts in the Tower of
Time HQ with the past section finished, all area portals open, and with the cloud step, and climbing claws already
obtained. You'll be forced to do sections of the game in different ways with your current abilities.

## What items can appear in other players' worlds?

* The player's movement items
* Quest and pedestal items
* Music Box notes
* The Phobekins
* Time shards
* Shop Upgrades
* Power Seals

## Where can I find items?

You can find items wherever items can be picked up in the original game. This includes:

* Shopkeeper dialog where the player originally gains movement items
* Quest Item pickups
* Music Box notes
* Phobekins
* Bosses
* Shop Upgrades, Money Wrench, and Figurine Purchases
* Power seals
* Mega Time Shards

## What are the item name groups?

When you attempt to hint for items in Archipelago you can use either the name for the specific item, or the name of a
group of items. Hinting for a group will choose a random item from the group that you do not currently have and hint
for it.

The groups you can use for The Messenger are:

* Notes - This covers the music notes
* Keys - An alternative name for the music notes
* Crest - The Sun and Moon Crests
* Phobekin - Any of the Phobekins
* Phobe - An alternative name for the Phobekins

## Other changes

* The player can return to the Tower of Time HQ at any point by selecting the button from the options menu
    * This can cause issues if used at specific times. If used in any of these known problematic areas, immediately
      quit to title and reload the save. The currently known areas include:
        * During Boss fights
        * After Courage Note collection (Corrupted Future chase)
* After reaching ninja village a teleport option is added to the menu to reach it quickly
* Toggle Windmill Shuriken button is added to option menu once the item is received
* The mod option menu will also have a hint item button, as well as a release and collect button that are all placed
  when the player fulfills the necessary conditions.
* After running the game with the mod, a config file (APConfig.toml) will be generated in your game folder that can be
  used to modify certain settings such as text size and color. This can also be used to specify a player name that can't
  be entered in game.

## Known issues

* Ruxxtin Coffin cutscene will sometimes not play correctly, but will still reward the item
* If you receive the Magic Firefly while in Quillshroom Marsh, The De-curse Queen cutscene will not play. You can exit
  to Searing Crags and re-enter to get it to play correctly.
* Teleporting back to HQ, then returning to the same level you just left through a Portal can cause Ninja to run left
  and enter a different portal than the one entered by the player or lead to other incorrect inputs, causing a soft lock
* Text entry menus don't accept controller input

## What do I do if I have a problem?

If you believe something happened that isn't intended, please get the `log.txt` from the folder of your game
installation and send a bug report either on GitHub or the [ZSR Discord Server](http://multiworld.gg/discord)

## FAQ

* The tracker says I can get some checks in Howling Grotto, but I can't defeat the Emerald Golem. How do I get there?
    * Due to the way the vanilla game handles bosses and level transitions, if you die to him, the room will be unlocked,
      and you can leave.
* I have the money wrench. Why won't the shopkeeper let me enter the sink?
    * The money wrench is both an item you must find or receive from another player and a location check, which you must
      purchase from the Artificer, as in vanilla.
* How do I unfreeze Manfred? Where is the monk?
    * The monk will only appear near Manfred after you cleanse the Queen of Quills with the fairy (magic firefly).
* I have all the power seals I need to win, but nothing is happening when I open the chest.
    * Due to how the level loading code works, I am currently unable to teleport you out of HQ at will; you must enter the
      shop from within a level.
