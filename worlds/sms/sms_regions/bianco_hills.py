from .sms_region_helper import *

BIANCO_HILLS_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_ENTRANCE,
    requirements=[Requirements(ANY_SPLASHER), Requirements(skip_forward=True)],
    ticketed="Bianco Hills Ticket", parent_region=SmsRegionName.PLAZA)

BIANCO_HILLS_ONE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_ONE,
    shines=[Shine("Road to the Big Windmill", [Requirements(ANY_SPLASHER)], in_game_bit=0),
        Shine("Down with Petey Piranha!", [Requirements(SPRAY_AND_HOVER)], in_game_bit=1),
        Shine("100 Coins", [Requirements(ALL_SPLASHER)], hundred=True, in_game_bit=100)
    ],
    blue_coins=[BlueCoin("Windmill M", [Requirements([[NozzleType.hover]])], in_game_bit=170),
        BlueCoin("Windmill Pillar", [Requirements(ANY_SPLASHER)], in_game_bit=171),
        BlueCoin("Towers House M", [Requirements(ANY_SPLASHER)], in_game_bit=188),
        BlueCoin("Balcony", [Requirements([[NozzleType.hover]])], in_game_bit=173),
        BlueCoin("Underwater Right", in_game_bit=180),
        BlueCoin("Wall Side M", [Requirements(ANY_SPLASHER)], in_game_bit=186),
        BlueCoin("Wall Top M", [Requirements(ANY_SPLASHER)], in_game_bit=187),
        BlueCoin("Towers House", [Requirements([[NozzleType.hover]])], in_game_bit=172), # Could be done with just Spray, easily so I think?
        BlueCoin("Pinwheel", [Requirements(ANY_SPLASHER)], in_game_bit=189),
        BlueCoin("X Behind Wall", [Requirements(ANY_SPLASHER)], in_game_bit=190),
        BlueCoin("River End", in_game_bit=191),
        BlueCoin("X Between Walls", [Requirements(ANY_SPLASHER)], in_game_bit=197),
        BlueCoin("Sail Platform", [Requirements([[NozzleType.hover]])], in_game_bit=198),  # Could also be done with just Spray...
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_THREE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_ONE} - Down with Petey Piranha!")],
    shines=[Shine("The Hillside Cave Secret", [Requirements(ROCKET_OR_HOVER)], in_game_bit=2),
        Shine("Red Coins of the Hillside Cave", [Requirements(ROCKET_OR_HOVER)], in_game_bit=8)],
    blue_coins=[BlueCoin("Treetop", [Requirements(ANY_SPLASHER)], in_game_bit=174),
        BlueCoin("Tourist", [Requirements(ANY_SPLASHER)], in_game_bit=175),
        BlueCoin("Windmill Pokey", [Requirements([[NozzleType.hover]])], in_game_bit=184),
        BlueCoin("Cliff", [Requirements(ROCKET_OR_HOVER)], in_game_bit=192),
        BlueCoin("Highest Platform", [Requirements(ROCKET_OR_HOVER)], in_game_bit=199),
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_FOUR: SmsRegion = SmsRegion(SmsRegionName.BIANCO_FOUR,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_THREE} - The Hillside Cave Secret")],
    shines=[Shine("Red Coins of Windmill Village", [Requirements(ROCKET_OR_HOVER)], in_game_bit=3)],
    blue_coins=[BlueCoin("Hillside Pokey", [Requirements([[NozzleType.hover]])], in_game_bit=178),
        BlueCoin("Bridge Underside", in_game_bit=183)
    ],
    nozzle_boxes=[NozzleBox("Rocket Box", in_game_bit=872)],
    parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_FIVE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_FIVE,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_FOUR} - Red Coins of Windmill Village")],
    shines=[Shine("Petey Piranha Strikes Back", [Requirements(SPRAY_AND_ROCKET_OR_HOVER)], in_game_bit=4)],
    blue_coins=[BlueCoin("Wall Tower Pianta", [Requirements(SPRAY_AND_ROCKET_OR_HOVER)], in_game_bit=177),
        BlueCoin("Platforms Cross", [Requirements(ROCKET_OR_HOVER)], in_game_bit=185),
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_SIX: SmsRegion = SmsRegion(SmsRegionName.BIANCO_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_FIVE} - Petey Piranha Strikes Back")],
    shines=[Shine("The Secret of the Dirty Lake", [Requirements(ANY_SPLASHER)], in_game_bit=5),
        Shine("Red Coins of the Dirty Lake", [Requirements([[NozzleType.hover]])], in_game_bit=9)
    ],
    blue_coins = [BlueCoin("Petey Pillar", [Requirements([[NozzleType.hover]])], in_game_bit=179),
        BlueCoin("Underwater Left", in_game_bit=181),
        BlueCoin("Blue Bird", [Requirements([[NozzleType.spray]])], in_game_bit=182),
        BlueCoin("Chuckster Momma", in_game_bit=193)
    ],
    nozzle_boxes = [NozzleBox("Turbo Box", [Requirements(ANY_SPLASHER)], in_game_bit=873)],
    parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_SEVEN: SmsRegion = SmsRegion(SmsRegionName.BIANCO_SEVEN,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_SIX} - The Secret of the Dirty Lake")],
    shines=[Shine("Shadow Mario on the Loose", [Requirements([[NozzleType.spray]])], in_game_bit=6)],
    blue_coins=[BlueCoin("Towers House O", [Requirements(ANY_SPLASHER)], in_game_bit=194),
        BlueCoin("Balcony House O", [Requirements(ANY_SPLASHER)], in_game_bit=195)
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_EIGHT: SmsRegion = SmsRegion(SmsRegionName.BIANCO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_SEVEN} - Shadow Mario on the Loose")],
    shines=[Shine("The Red Coins of the Lake", [Requirements(ROCKET_OR_HOVER)], in_game_bit=7)],
    blue_coins=[BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=176),
        BlueCoin("Butterfly", [Requirements([[NozzleType.yoshi]])], in_game_bit=177)
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)