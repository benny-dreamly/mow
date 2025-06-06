# Pokémon Crystal Setup Guide

## Required Software

- [MultiworldGG](https://github.com/MultiworldGG/MultiworldGG/releases)
- An English (UE) Pokémon Crystal v1.0 or v1.1 ROM. The Archipelago community cannot provide this.
- One of the following:
  - [BizHawk](https://tasvideos.org/BizHawk/ReleaseHistory) 2.7 or later. 2.9.1 is recommended.
  - [mGBA](https://mgba.io) 0.10.3 or later.
    - You will also need the [mGBA to Bizhawk Client connector script](https://gist.github.com/Zunawe/d41677500b08694c9985f67f41896cc5).
      You should add it to `data/lua/` in your Archipelago install.

### Configuring BizHawk

Once you have installed BizHawk, open `EmuHawk.exe` and change the following settings:

- On BizHawk 2.8 or earlier, navigate to `Config -> Customize` and click on the Advanced tab. Change the Lua core
  from `NLua+KopiLua` to `Lua+LuaInterface`, then restart EmuHawk. This step is not required on BizHawk 2.9 or later.
- Under Config > Customize > Advanced, make sure the box for AutoSaveRAM is checked, and click the 5s button.
  This reduces the possibility of losing save data in emulator crashes.
- In `Config -> Customize`, enable `Run in background`. This will prevent the game from losing connection to the client
  when tabbed out.
- Open a Gameboy or Gameboy Color game (`.gb` or `.gbc`) and then navigate to `Config -> Controllers...`. This menu may
  not be available if a game is not already open.

### Configuring mGBA

Once you have installed mGBA, open `mGBA`, navigate to Settings/Preferences, and change the following setting:

- In `Game Boy`, under Models, select `Game Boy Color (CGB)` for all models.

## Optional Software

[Pokémon Crystal AP Tracker](https://github.com/palex00/crystal-ap-tracker/releases/latest) for use
with [PopTracker](https://github.com/black-sliver/PopTracker/releases)

## Generating and Patching a Game

1. Add `pokemon_crystal.apworld` to your `custom_worlds` folder in your Archipelago install. It should not be in `lib\worlds`.
2. Create your options file (YAML). You can make one ~~on
   the [Pokémon Crystal options page](../../../games/Pokemon%20Crystal/player-options)~~ by choosing "Generate Template Options"
   from the Archipelago Launcher. From there, you can edit the `.yaml` in any text editor.
4. Follow the general MultiworldGG instructions for [generating a game on your local installation](https://multiworld.gg/tutorial/Archipelago/setup/en#on-your-local-installation).
   This will generate an output file for you. Your patch file will have the `.apcrystal` file extension.
5. Open `MultiworldGGLauncher.exe`
6. Select "Open Patch" on the left side and select your patch file.
7. If this is your first time patching, you will be prompted to locate your vanilla ROM.
8. A patched `.gbc` file will be created in the same place as the patch file.
9. On your first time opening a patch with BizHawk Client, you will also be asked to locate `EmuHawk.exe` in your
   BizHawk install. For mGBA users, you can select `Cancel` and manually open mGBA.

If you're playing a single-player seed and you don't care about autotracking or hints, you can stop here, close the
client, and load the patched ROM in any emulator. However, for multiworlds and other Archipelago features, continue
below using BizHawk or mGBA as your emulator.

## Connecting to a Server

By default, opening a patch file will do steps 1-5 below for you automatically. Even so, keep them in your memory just
in case you have to close and reopen a window mid-game for some reason.

1. Pokémon Crystal uses MultiworldGG's BizHawk Client. If the client isn't still open from when you patched your game,
   you can re-open it from the launcher.
2. Ensure EmuHawk or mGBA is running the patched ROM.
3. In EmuHawk:
   - Go to `Tools > Lua Console`. This window must stay open while playing.
   - In the Lua Console window, go to `Script > Open Script…`.
   - Navigate to your MultiworldGG install folder and open `data/lua/connector_bizhawk_generic.lua`.
4. In mGBA:
   - Go to `Tools > Scripting...`. This window must stay open while playing.
   - Go to `File > Load Script...`.
   - Navigate to your MultiworldGG install folder and open `data/lua/connector_bizhawkclient_mgba.lua`.
5. The emulator and client will eventually connect to each other. The BizHawk Client window should indicate that it
   connected and recognized Pokémon Crystal.
6. To connect the client to the server, enter your room's address and port (e.g. `multiworld.gg:38281`) into the
   top text field of the client and click Connect.

You should now be able to receive and send items. You'll need to do these steps every time you want to reconnect. It is
perfectly safe to make progress offline; everything will re-sync when you reconnect.

## Auto-Tracking

Pokémon Crystal has a fully functional map tracker that supports auto-tracking.

1. Download [Pokémon Crystal AP Tracker](https://github.com/palex00/crystal-ap-tracker/releases/latest) and
   [PopTracker](https://github.com/black-sliver/PopTracker/releases).
2. Put the tracker pack into `packs/` in your PopTracker install.
3. Open PopTracker, and load the Pokémon Crystal pack.
4. For autotracking, click on the "AP" symbol at the top.
5. Enter the Archipelago server address (the one you connected your client to), slot name, and password.
