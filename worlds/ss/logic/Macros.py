BASE_MACROS = {
    ## ITEMS
    "Has Practice Sword": "Progressive Sword x1",
    "Has Goddess Sword": "Progressive Sword x2",
    "Has Goddess Longsword": "Progressive Sword x3",
    "Has Goddess White Sword": "Progressive Sword x4",
    "Has Master Sword": "Progressive Sword x5",
    "Has True Master Sword": "Progressive Sword x6",

    "Has Beetle": "Progressive Beetle x1",
    "Has Hook Beetle": "Progressive Beetle x2",
    "Has Quick Beetle": (
        "(Progressive Beetle x3 & option_gondo_upgrades) "
        "| (Can Upgrade to Quick Beetle & not option_gondo_upgrades)"
    ),
    "Has Tough Beetle": (
        "(Progressive Beetle x4 & option_gondo_upgrades) "
        "| (Can Upgrade to Tough Beetle & not option_gondo_upgrades)"
    ),

    "Has Bow": "Progressive Bow x1",
    "Has Slingshot": "Progressive Slingshot x1",
    "Has Bug Net": "Progressive Bug Net x1",
    "Has Digging Mitts": "Progressive Mitts x1",
    "Has Mogma Mitts": "Progressive Mitts x2",
    "Has Pouch": "Progressive Pouch x1",
    "Has Bottle": "Has Pouch & Empty Bottle x1",

    "Has Medium Wallet": "Progressive Wallet x1",
    "Has Big Wallet": "Progressive Wallet x2",
    "Has Giant Wallet": "Progressive Wallet x3",
    "Has Tycoon Wallet": "Progressive Wallet x4",

    "Has Song of the Hero": (
        "Faron Song of the Hero Part "
        "& Eldin Song of the Hero Part "
        "& Lanayru Song of the Hero Part "
    ),
    "Has Completed Triforce": (
        "Triforce of Courage "
        "& Triforce of Power "
        "& Triforce of Wisdom"
    ),

    ## MISC
    "Upgraded Skyward Strike": (
        "Has True Master Sword "
        "| (Has Goddess Sword & option_upgraded_skyward_strike)"
    ),
    "Unlocked Endurance Potion": "Can Raise LMF",
    "Damaging Item": "Has Practice Sword | Has Bow | Bomb Bag",
    "Projectile Item": "Has Slingshot | Has Beetle | Has Bow",
    "Distance Activator": "Projectile Item | Clawshots",
    "Can Cut Trees": "Has Practice Sword | Bomb Bag",
    "Can Unlock Combination Lock": (
        "Has Practice Sword | Has Bow | Whip | Clawshots"
    ),
    "Can Hit Timeshift Stone": (
        "Distance Activator | Has Practice Sword | Whip | Bomb Bag"
    ),
    "Can Farm Ancient Flowers": (
        "Lanayru Mine Ancient Flower Farming "
        "| Lanayru Desert Ancient Flower Farming "
        "| Lanayru Desert Ancient Flower Farming near Main Node "
        "| Lanayru Gorge Ancient Flower Farming "
        "| Pirate Stronghold Ancient Flower Farming"
    ),
    "Can Farm Hornet Larvae": "Deep Woods Hornet Larvae Farming",
    "Can Farm Amber Relics": "Faron Woods Amber Relic Farming",

    "Can Upgrade to Quick Beetle": (
        "Has Hook Beetle "
        "& Can Farm Hornet Larvae "
        "& Can Farm Ancient Flowers "
        "& Clean Cut Minigame"
    ),
    "Can Upgrade to Tough Beetle": (
        "Can Upgrade to Quick Beetle "
        "& Can Farm Amber Relics "
        "& Can Farm Ancient Flowers "
        "& Clean Cut Minigame"
    ),

    ## ENEMIES
    "Can Defeat Bokoblins": "Damaging Item",
    "Can Defeat Moblins": "Damaging Item",
    "Can Defeat Keeses": "Damaging Item | Has Slingshot | Has Beetle | Whip | Clawshots",
    "Can Defeat Lezalfos": "Has Practice Sword | Bomb Bag",
    "Can Defeat Ampilus": "Damaging Item",
    "Can Defeat Moldarachs": "Gust Bellows & Has Practice Sword",
    "Can Defeat Armos": "Gust Bellows & Has Practice Sword",
    "Can Defeat Beamos": "Has Practice Sword | Has Bow",
    "Can Defeat Cursed Bokoblins": "Has Practice Sword | Bomb Bag",
    "Can Defeat Stalfos": "Has Practice Sword",
    "Can Defeat Stalmaster": "Has Practice Sword",

    ## GRATITUDE CRYSTALS
    "Five Gratitude Crystals": "Gratitude Crystal Pack x1 | Gratitude Crystal x5",
    "Ten Gratitude Crystals": (
        "Gratitude Crystal x10 "
        "| (Gratitude Crystal Pack x1 & Gratitude Crystal x5) "
        "| Gratitude Crystal Pack x2"
    ),
    "Thirty Gratitude Crystals": (
        "(Gratitude Crystal x15 & Gratitude Crystal Pack x3) "
        "| (Gratitude Crystal x10 & Gratitude Crystal Pack x4) "
        "| (Gratitude Crystal x5 & Gratitude Crystal Pack x5) "
        "| Gratitude Crystal Pack x6"
    ),
    "Forty Gratitude Crystals": (
        "(Gratitude Crystal x15 & Gratitude Crystal Pack x5) "
        "| (Gratitude Crystal x10 & Gratitude Crystal Pack x6) "
        "| (Gratitude Crystal x5 & Gratitude Crystal Pack x7) "
        "| Gratitude Crystal Pack x8"
    ),
    "Fifty Gratitude Crystals": (
        "(Gratitude Crystal x15 & Gratitude Crystal Pack x7) "
        "| (Gratitude Crystal x10 & Gratitude Crystal Pack x8) "
        "| (Gratitude Crystal x5 & Gratitude Crystal Pack x9) "
        "| Gratitude Crystal Pack x10"
    ),
    "Seventy Gratitude Crystals": (
        "(Gratitude Crystal x15 & Gratitude Crystal Pack x11) "
        "| (Gratitude Crystal x10 & Gratitude Crystal Pack x12) "
        "| (Gratitude Crystal x5 & Gratitude Crystal Pack x13)"
    ),
    "Eighty Gratitude Crystals": (
        "Gratitude Crystal x15 & Gratitude Crystal Pack x13"
    ),
    
    ## RUPEES
    "Can Afford 300 Rupees": "Can Medium Rupee Farm",
    "Can Afford 600 Rupees": (
        "Can High Rupee Farm "
        "& (Has Big Wallet | Extra Wallet x1)"
    ),
    "Can Afford 800 Rupees": (
        "Can High Rupee Farm "
        "& ( Has Big Wallet | (Has Medium Wallet & Extra Wallet x1) | Extra Wallet x2 )"
    ),
    "Can Afford 1000 Rupees": (
        "Can High Rupee Farm "
        "& ( Has Big Wallet | (Has Medium Wallet & Extra Wallet x2) | Extra Wallet x3 )"
    ),
    "Can Afford 1200 Rupees": (
        "Can High Rupee Farm "
        "& ( Has Giant Wallet | (Has Big Wallet & Extra Wallet x1) | Extra Wallet x3 )"
    ),
    "Can Afford 1600 Rupees": (
        "Can High Rupee Farm "
        "& ( Has Giant Wallet | (Has Big Wallet & Extra Wallet x2) )"
    ),

    "Can Medium Rupee Farm": (
        "(Clean Cut Minigame & Can Sell Treasures) "
        "| Can High Rupee Farm"
    ),
    "Can High Rupee Farm": "Fun Fun Minigame | Thrill Digger Minigame",
}
