SKYVIEW_REQUIREMENTS = {
    "Skyview - First Room": {
        "hint_region": "Skyview",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Second Room": (
                "Can Cut Trees "
                "& ( Water Dragon's Scale "
                "| Bomb Bag "
                "| (Distance Activator & Has Practice Sword) )"
            )
        },
        "locations": {},
    },
    "Skyview - Second Room": {
        "hint_region": "Skyview",
        "exits": {
            "First Room": "Nothing",
            "Main Room": (
                "Skyview Small Key x1 "
                "& (Distance Activator | Has Goddess Sword | Whip)"
            ),
        },
        "locations": {
            "Chest on Tree Branch": "Distance Activator | Has Goddess Sword | Whip",
            "Digging Spot in Crawlspace": (
                "Distance Activator & Water Dragon's Scale & Has Digging Mitts"
            ),
            "Chest behind Two Eyes": (
                "Has Practice Sword & (Clawshots | Distance Activator)"
            ),
        },
    },
    "Skyview - Main Room": {
        "hint_region": "Skyview",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Second Room": "Nothing",
            "Boss Door Area": (
                "Skyview Small Key x2 "
                "& (Has Practice Sword | Bomb Bag) "
                "& (Has Goddess Sword | Has Beetle | Has Bow | Water Dragon's Scale | Bomb Bag) "
                "& (Upgraded Skyward Strike | Has Hook Beetle | Has Bow)"
            ),
        },
        "locations": {
            "Chest after Stalfos Fight": (
                "Distance Activator & (Has Practice Sword | Water Dragon's Scale)"
            ),
            "Item behind Bars": "Has Beetle | Whip",
            "Rupee in Southeast Tunnel": "Has Beetle",
            "Rupee in Southwest Tunnel": "Has Beetle",
            "Rupee in East Tunnel": "Has Beetle",
            "Chest behind Three Eyes": "Has Beetle & Has Practice Sword",
        },
    },
    "Skyview - Boss Door Area": {
        "hint_region": "Skyview",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Main Room": "Nothing",
            "Boss Room": "Skyview Boss Key",
        },
        "locations": {
            "Chest near Boss Door": "Nothing",
            "Boss Key Chest": "Distance Activator | Upgraded Skyward Strike",
        },
    },
    "Skyview - Boss Room": {
        "hint_region": "Skyview",
        "macros": {
            "Can Beat Ghirahim 1": "Has Practice Sword",
        },
        "exits": {
            "Boss Door Area": "Nothing",
            "Skyview Spring": "Can Beat Ghirahim 1",
        },
        "locations": {
            "Heart Container": "Can Beat Ghirahim 1",
        },
    },
    "Skyview - Skyview Spring": {
        "hint_region": "Skyview",
        "macros": {
            "Can Beat Skyview": "Has Goddess Sword",
            "Goddess Cube in Skyview Spring": "Has Goddess Sword",
        },
        "exits": {
            "Boss Room": "Nothing",
            "Strike Crest": "Can Beat Skyview",
        },
        "locations": {
            "Rupee on Spring Pillar": "Has Beetle",
            "Strike Crest": "Can Beat Skyview",
        },
    },
}
