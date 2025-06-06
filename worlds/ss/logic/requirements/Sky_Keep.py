SKY_KEEP_REQUIREMENTS = {
    "Sky Keep - First Room": {
        "hint_region": "Sky Keep",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Skyview Room": "Nothing",
        },
        "locations": {
            "First Chest": "Nothing",
        },
    },
    "Sky Keep - Skyview Room": {
        "hint_region": "Sky Keep",
        "macros": {
            "Can Pass Sky Keep SV Room": (
                "(Has Beetle | Has Bow) " # Shoot rope
                "& Whip " # Whip hook
                "& Clawshots " # Vines
                "& (Bomb Bag | Has Hook Beetle | Has Bow) " # Kill pyrup
                "& Gust Bellows" # Swinging platform
            ),
        },
        "exits": {
            "Dungeon Exit": "Can Pass Sky Keep SV Room",
            "First Room": "Nothing",
            "Lanayru Mining Facility Room": "Can Pass Sky Keep SV Room",
        },
        "locations": {},
    },
    "Sky Keep - Lanayru Mining Facility Room": {
        "hint_region": "Sky Keep",
        "macros": {
            "Can Pass Sky Keep LMF Room": "Has Bow & Gust Bellows",
        },
        "exits": {
            "Dungeon Exit": "Nothing",
            "Skyview Room": "Nothing",
            "Earth Temple Room": "Can Pass Sky Keep LMF Room",
            "Ancient Cistern Room": "Can Pass Sky Keep LMF Room",
        },
        "locations": {},
    },
    "Sky Keep - Earth Temple Room": {
        "hint_region": "Sky Keep",
        "macros": {
            "Can Pass Sky Keep ET Room": (
                "Has Mogma Mitts & Has Hook Beetle & Bomb Bag & Upgraded Skyward Strike"
            ),
        },
        "exits": {
            "Dungeon Exit": "Nothing",
            "Lanayru Mining Facility Room": "Nothing",
            "Miniboss Room": "Can Pass Sky Keep ET Room",
        },
        "locations": {},
    },
    "Sky Keep - Ancient Cistern Room": {
        "hint_region": "Sky Keep",
        "exits": {
            "Lanayru Mining Facility Room": "Nothing",
            "Fire Sanctuary Room": "Nothing",
        },
        "locations": {
            "Sacred Power of Farore": (
                "Sky Keep Small Key "
                "& Can Defeat Moblins "
                "& Can Defeat Bokoblins "
                "& Can Defeat Stalfos "
                "& Has Bow "
                "& Can Defeat Cursed Bokoblins "
                "& Can Defeat Stalmaster"
            ),
        },
    },
    "Sky Keep - Miniboss Room": {
        "hint_region": "Sky Keep",
        "macros": {
            "Can Beat Dreadfuse": "Clawshots & Has Practice Sword",
        },
        "exits": {
            "Earth Temple Room": "Nothing",
            "Fire Sanctuary Room": "Can Beat Dreadfuse",
        },
        "locations": {
            "Chest after Dreadfuse": "Can Beat Dreadfuse",
        },
    },
    "Sky Keep - Fire Sanctuary Room": {
        "hint_region": "Sky Keep",
        "macros": {
            "Can Pass Sky Keep FS Room": "Has Beetle & Clawshots",
        },
        "exits": {
            "Dungeon Exit": "Nothing",
            "Ancient Cistern Room": "Nothing",
            "Miniboss Room": "Can Pass Sky Keep FS Room",
            "Sandship Room": "Can Pass Sky Keep FS Room",
        },
        "locations": {
            "Rupee in Fire Sanctuary Room in Alcove": "Has Beetle",
            "Sacred Power of Din": "Can Pass Sky Keep FS Room",
        },
    },
    "Sky Keep - Sandship Room": {
        "hint_region": "Sky Keep",
        "exits": {
            "Dungeon Exit": "Nothing",
            "Fire Sanctuary Room": "Nothing",
        },
        "locations": {
            "Sacred Power of Nayru": "Has Bow & Clawshots",
        },
    },
}
