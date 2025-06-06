from BaseClasses import Item
from .GameID import jak1_name, jak1_max
from .locs import (OrbLocations as Orbs,
                   CellLocations as Cells,
                   ScoutLocations as Scouts,
                   SpecialLocations as Specials,
                   OrbCacheLocations as Caches)


class JakAndDaxterItem(Item):
    game: str = jak1_name


# Power Cells are generic, fungible, interchangeable items. Every cell is indistinguishable from every other.
cell_item_table = {
    0:  "Power Cell",
}

# Scout flies are interchangeable within their respective sets of 7. Notice the level name after each item.
# Also, notice that their Item ID equals their respective Power Cell's Location ID. This is necessary for
# game<->MultiworldGG communication.
scout_item_table = {
    95: "Scout Fly - Geyser Rock",
    75: "Scout Fly - Sandover Village",
    7:  "Scout Fly - Forbidden Jungle",
    20: "Scout Fly - Sentinel Beach",
    28: "Scout Fly - Misty Island",
    68: "Scout Fly - Fire Canyon",
    76: "Scout Fly - Rock Village",
    57: "Scout Fly - Precursor Basin",
    49: "Scout Fly - Lost Precursor City",
    43: "Scout Fly - Boggy Swamp",
    88: "Scout Fly - Mountain Pass",
    77: "Scout Fly - Volcanic Crater",
    85: "Scout Fly - Spider Cave",
    65: "Scout Fly - Snowy Mountain",
    90: "Scout Fly - Lava Tube",
    91: "Scout Fly - Citadel",  # Had to shorten, it was >32 characters.
}

# Orbs are also generic and interchangeable.
# These items are only used by Orbsanity, and only one of these
# items will be used corresponding to the chosen bundle size.
orb_item_table = {
    1: "1 Precursor Orb",
    2: "2 Precursor Orbs",
    4: "4 Precursor Orbs",
    5: "5 Precursor Orbs",
    8: "8 Precursor Orbs",
    10: "10 Precursor Orbs",
    16: "16 Precursor Orbs",
    20: "20 Precursor Orbs",
    25: "25 Precursor Orbs",
    40: "40 Precursor Orbs",
    50: "50 Precursor Orbs",
    80: "80 Precursor Orbs",
    100: "100 Precursor Orbs",
    125: "125 Precursor Orbs",
    200: "200 Precursor Orbs",
    250: "250 Precursor Orbs",
    400: "400 Precursor Orbs",
    500: "500 Precursor Orbs",
    1000: "1000 Precursor Orbs",
    2000: "2000 Precursor Orbs",
}

# These are special items representing unique unlocks in the world. Notice that their Item ID equals their
# respective Location ID. Like scout flies, this is necessary for game<->MultiworldGG communication.
special_item_table = {
    5: "Fisherman's Boat",              # Unlocks Misty Island
    4: "Jungle Elevator",               # Unlocks the Forbidden Jungle Temple
    2: "Blue Eco Switch",               # Unlocks Blue Eco Vents
    17: "Flut Flut",                    # Unlocks Flut Flut sections in Boggy Swamp and Snowy Mountain
    33: "Warrior's Pontoons",           # Unlocks Boggy Swamp and everything post-Rock Village
    105: "Snowy Mountain Gondola",      # Unlocks Snowy Mountain
    60: "Yellow Eco Switch",            # Unlocks Yellow Eco Vents
    63: "Snowy Fort Gate",              # Unlocks the Snowy Mountain Fort
    71: "Freed The Blue Sage",          # 1 of 3 unlocks for the final staircase in Citadel
    72: "Freed The Red Sage",           # 1 of 3 unlocks for the final staircase in Citadel
    73: "Freed The Yellow Sage",        # 1 of 3 unlocks for the final staircase in Citadel
    70: "Freed The Green Sage",         # Unlocks the final boss elevator in Citadel
}

# These are the move items for move randomizer. Notice that their Item ID equals some of the Orb Cache Location ID's.
# This was 100% arbitrary. There's no reason to tie moves to orb caches except that I need a place to put them. ;_;
move_item_table = {
    10344: "Crouch",
    10369: "Crouch Jump",
    11072: "Crouch Uppercut",
    12634: "Roll",
    12635: "Roll Jump",
    10945: "Double Jump",
    14507: "Jump Dive",
    14838: "Jump Kick",
    23348: "Punch",
    23349: "Punch Uppercut",
    23350: "Kick",
    # 24038: "Orb Cache at End of Blast Furnace",  # Hold onto these ID's for future use.
    # 24039: "Orb Cache at End of Launch Pad Room",
    # 24040: "Orb Cache at Start of Launch Pad Room",
}

# These are trap items. Their Item ID is to be subtracted from the base game ID. They do not have corresponding
# game locations because they are intended to replace other items that have been marked as filler.
trap_item_table = {
    1: "Trip Trap",
    2: "Slippery Trap",
    3: "Gravity Trap",
    4: "Camera Trap",
    5: "Darkness Trap",
    6: "Earthquake Trap",
    7: "Teleport Trap",
    8: "Despair Trap",
    9: "Pacifism Trap",
    10: "Ecoless Trap",
    11: "Health Trap",
    12: "Ledge Trap",
    13: "Zoomer Trap",
    14: "Mirror Trap",
}

# All Items
# While we're here, do all the ID conversions needed.
item_table = {
    **{Cells.to_ap_id(k): cell_item_table[k] for k in cell_item_table},
    **{Scouts.to_ap_id(k): scout_item_table[k] for k in scout_item_table},
    **{Specials.to_ap_id(k): special_item_table[k] for k in special_item_table},
    **{Caches.to_ap_id(k): move_item_table[k] for k in move_item_table},
    **{Orbs.to_ap_id(k): orb_item_table[k] for k in orb_item_table},
    **{jak1_max - k: trap_item_table[k] for k in trap_item_table},
    jak1_max: "Green Eco Pill"  # Filler item.
}
