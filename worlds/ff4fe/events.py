from .locations import LocationData
boss_names = [
     'D. Mist',
     'Officer',
     'Octomamm',
     'Antlion',
     'MomBomb',
     'Fabul Gauntlet',
     'Milon',
     'Milon Z.',
     'Mirror Cecil',
     'Guards',
     'Karate',
     'Baigan',
     'Kainazzo',
     'Dark Elf',
     'Magus Sisters',
     'Valvalis',
     'Calbrena',
     'Golbez',
     'Lugae',
     'Dark Imps',
     'King and Queen',
     'Rubicant',
     'EvilWall',
     'Asura',
     'Leviatan',
     'Odin',
     'Bahamut',
     'Elements',
     'CPU',
     'Pale Dim',
     'Wyvern',
     'Plague',
     'D. Lunars',
     'Ogopogo'
]

boss_event_data = [
     ("Overworld", "MistCave", "D. Mist Slot"),
     ("Overworld", "Kaipo", "Officer Slot"),
     ("Overworld", "WateryPass", "Octomamm Slot"),
     ("Overworld", "AntlionCave", "Antlion Slot"),
     ("Overworld", "MountHobs", "MomBomb Slot"),
     ("Overworld", "Fabul", "Fabul Gauntlet Slot"),
     ("Overworld", "MountOrdeals", "Milon Slot"),
     ("Overworld", "MountOrdeals", "Milon Z. Slot"),
     ("Overworld", "MountOrdeals", "Mirror Cecil Slot"),
     ("Overworld", "BaronWeaponShop", "Karate Slot"),
     ("Overworld", "BaronWeaponShop", "Guards Slot"),
     ("Overworld", "Sewer", "Baigan Slot"),
     ("Overworld", "BaronCastle", "Kainazzo Slot"),
     ("Overworld", "CaveMagnes", "Dark Elf Slot"),
     ("Overworld", "Zot", "Magus Sisters Slot"),
     ("Overworld", "Zot", "Valvalis Slot"),
     ("Underworld", "DwarfCastle", "Calbrena Slot"),
     ("Underworld", "DwarfCastle", "Golbez Slot"),
     ("Overworld", "LowerBabil", "Lugae Slot"),
     ("Overworld", "LowerBabil", "Dark Imp Slot"),
     ("Underworld", "UpperBabil", "King and Queen Slot"),
     ("Underworld", "UpperBabil", "Rubicant Slot"),
     ("Underworld", "SealedCave", "Evilwall Slot"),
     ("Underworld", "Feymarch", "Asura Slot"),
     ("Underworld", "Feymarch", "Leviatan Slot"),
     ("Overworld", "BaronCastle", "Odin Slot"),
     ("Moon", "BahamutCave", "Bahamut Slot"),
     ("Moon", "Giant", "Elements Slot"),
     ("Moon", "Giant", "CPU Slot"),
     ("Moon", "LunarCore", "Pale Dim Slot"),
     ("Moon", "LunarCore", "Wyvern Slot"),
     ("Moon", "LunarCore", "Plague Slot"),
     ("Moon", "LunarCore", "D. Lunars Slot"),
     ("Moon", "LunarCore", "Ogopogo Slot"),
     ("Moon", "LunarCore", "Zeromus")
]

boss_events = []
boss_status_events = {boss: (f"{boss} Defeated") for boss in boss_names}
boss_slots = [(f"{boss} Slot Defeated") for boss in boss_names]

for event in boss_event_data:
    boss_events.append(LocationData(event[2], event[0], event[1], 0xFFFF, True))
