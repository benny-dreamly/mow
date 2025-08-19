import pkgutil
import json

from BaseClasses import ItemClassification

# we can't really tell the difference between quivers and shields without this.
quiver_base_type_array = [
"Serrated Arrow Quiver",
"Fire Arrow Quiver",
"Sharktooth Arrow Quiver",
"Feathered Arrow Quiver",
"Penetrating Arrow Quiver",
"Blunt Arrow Quiver",
"Two-Point Arrow Quiver",
"Spike-Point Arrow Quiver",
"Blazing Arrow Quiver",
"Ornate Quiver",
"Broadhead Arrow Quiver",
"Vile Arrow Quiver",
"Heavy Arrow Quiver",
"Primal Arrow Quiver",
"Artillery Quiver",
]

shield_base_type_array = [
"Splintered Tower Shield",
"Corroded Tower Shield",
"Rawhide Tower Shield",
"Cedar Tower Shield",
"Copper Tower Shield",
"Reinforced Tower Shield",
"Painted Tower Shield",
"Buckskin Tower Shield",
"Mahogany Tower Shield",
"Bronze Tower Shield",
"Magmatic Tower Shield",
"Girded Tower Shield",
"Crested Tower Shield",
"Shagreen Tower Shield",
"Ebony Tower Shield",
"Ezomyte Tower Shield",
"Colossal Tower Shield",
"Heat-attuned Tower Shield",
"Pinnacle Tower Shield",
    
"Goathide Buckler",
"Pine Buckler",
"Painted Buckler",
"Hammered Buckler",
"War Buckler",
"Gilded Buckler",
"Oak Buckler",
"Enameled Buckler",
"Corrugated Buckler",
"Battle Buckler",
"Polar Buckler",
"Golden Buckler",
"Ironwood Buckler",
"Lacquered Buckler",
"Vaal Buckler",
"Crusader Buckler",
"Imperial Buckler",
"Cold-attuned Buckler",
    
"Twig Spirit Shield",
"Yew Spirit Shield",
"Bone Spirit Shield",
"Tarnished Spirit Shield",
"Jingling Spirit Shield",
"Brass Spirit Shield",
"Walnut Spirit Shield",
"Ivory Spirit Shield",
"Ancient Spirit Shield",
"Chiming Spirit Shield",
"Subsuming Spirit Shield",
"Thorium Spirit Shield",
"Lacewood Spirit Shield",
"Fossilised Spirit Shield",
"Vaal Spirit Shield",
"Harmonic Spirit Shield",
"Titanium Spirit Shield",
"Transfer-attuned Spirit Shield",
    
"Rotted Round Shield",
"Fir Round Shield",
"Studded Round Shield",
"Scarlet Round Shield",
"Splendid Round Shield",
"Maple Round Shield",
"Spiked Round Shield",
"Crimson Round Shield",
"Baroque Round Shield",
"Teak Round Shield",
"Spiny Round Shield",
"Cardinal Round Shield",
"Elegant Round Shield",
    
"Plank Kite Shield",
"Linden Kite Shield",
"Reinforced Kite Shield",
"Layered Kite Shield",
"Ceremonial Kite Shield",
"Etched Kite Shield",
"Steel Kite Shield",
"Laminated Kite Shield",
"Angelic Kite Shield",
"Branded Kite Shield",
"Champion Kite Shield",
"Mosaic Kite Shield",
"Archon Kite Shield",
    
"Spiked Bundle",
"Driftwood Spiked Shield",
"Alloyed Spiked Shield",
"Burnished Spiked Shield",
"Ornate Spiked Shield",
"Redwood Spiked Shield",
"Compound Spiked Shield",
"Polished Spiked Shield",
"Sovereign Spiked Shield",
"Alder Spiked Shield",
"Ezomyte Spiked Shield",
"Mirrored Spiked Shield",
"Supreme Spiked Shield",
]

starting_items_table = {
    "Scion": {
        "weapon": "Normal Sword",
        "gem": "Spectral Throw",
        "support": "Prismatic Burst Support"
    },
    "Marauder": {
        "weapon": "Normal Mace",
        "gem": "Heavy Strike",
        "support": "Ruthless Support"
    },
    "Duelist": {
        "weapon": "Normal Sword",
        "gem": "Double Strike",
        "support": "Chance to Bleed Support"
    },
    "Ranger": {
        "weapon": "Normal Bow",
        "gem": "Burning Arrow",
        "support": "Momentum Support"
    },
    "Shadow": {
        "weapon": "Normal Dagger",
        "gem": "Viper Strike",
        "support": "Chance to Poison Support"
    },
    "Witch": {
        "weapon": "Normal Wand",
        "gem": "Fireball",
        "support": "Arcane Surge Support"
    },
    "Templar": {
        "weapon": "Normal Sceptre",
        "gem": "Glacial Hammer",
        "support": "Elemental Proliferation Support"
    },
}


item_array = json.loads(pkgutil.get_data("worlds.poe.data", "Items.json").decode("utf-8"))
item_table = {}
for i, item in enumerate(item_array, start=1):
    item["id"] = i
    item["classification"] = ItemClassification(item.get("classification", ItemClassification.filler))
    item_table[i] = item

data = pkgutil.get_data("worlds.poe.data", "Bosses.json")

if __name__ == "__main__":
    import json
    print(json.dumps(item_table, indent=4))