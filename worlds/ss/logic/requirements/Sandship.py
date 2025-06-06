SANDSHIP_REQUIREMENTS = {
    "Sandship - Deck": {
        "hint_region": "Sandship",
        "macros": {
            "Can Change Sandship's Temporality": (
                "Has Bow & (Has Practice Sword | Sandship Small Key x2)"
            ),
        },
        "exits": {
            "Dungeon Exit": "Nothing",
            "Corridor": "Nothing",
            "Boss Key Room": "Can Change Sandship's Temporality & Sandship Small Key x2",
        },
        "locations": {
            "Chest at the Stern": "Can Change Sandship's Temporality & Has Bow & Clawshots",
        },
    },
    "Sandship - Corridor": {
        "hint_region": "Sandship",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Deck": "Nothing",
            "Near Boss Door": (
                "Can Change Sandship's Temporality "
                "| Has Goddess Sword "
                "| Has Bow "
                "| Has Slingshot "
                "| Bomb Bag"
            ),
            "Basement": "Can Change Sandship's Temporality & Has Practice Sword & Has Bow",
            "Bow": "Sandship Small Key x2",
        },
        "locations": {
            "Chest before 4-Door Corridor": "Can Change Sandship's Temporality & Has Bow",
        },
    },
    "Sandship - Near Boss Door": {
        "hint_region": "Sandship",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Corridor": "Nothing",
            "Boss Room": "Can Change Sandship's Temporality & Sandship Boss Key"
        },
        "locations": {
            "Chest behind Combination Lock": (
                "Can Unlock Combination Lock "
                "& (Gust Bellows | Can Change Sandship's Temporality)"
            )
        },
    },
    "Sandship - Basement": {
        "hint_region": "Sandship",
        "exits": {
            "Corridor": "Nothing",
        },
        "locations": {
            "Treasure Room First Chest": "Whip",
            "Treasure Room Second Chest": "Whip",
            "Treasure Room Third Chest": "Whip",
            "Treasure Room Fourth Chest": "Whip",
            "Treasure Room Fifth Chest": "Whip",
            "Robot in Brig's Reward": "Whip",
        },
    },
    "Sandship - Bow": {
        "hint_region": "Sandship",
        "exits": {
            "Corridor": "Nothing",
        },
        "locations": {
            "Chest after Scervo Fight": "Has Practice Sword",
        },
    },
    "Sandship - Boss Key Room": {
        "hint_region": "Sandship",
        "exits": {
            "Deck": "Nothing",
        },
        "locations": {
            "Boss Key Chest": "Has Bow",
        },
    },
    "Sandship - Boss Room": {
        "hint_region": "Sandship",
        "macros": {
            "Can Beat Tentalus": "Has Bow",
            "Can Beat Sandship": "Can Beat Tentalus & Has Goddess Sword",
        },
        "exits": {
            "Near Boss Door": "Nothing",
            "Strike Crest": "Can Beat Sandship",
        },
        "locations": {
            "Heart Container": "Can Beat Tentalus",
            "Nayru's Flame": "Can Beat Sandship",
        },
    },
}
