from .sms_region_helper import *

BIANCO_HILLS_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_ENTRANCE,
    requirements=[Requirements(ANY_SPLASHER), Requirements(skip_forward=True)],
    ticketed="Bianco Hills Ticket", parent_region=SmsRegionName.PLAZA)

BIANCO_HILLS_ONE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_ONE,
    shines=[Shine("Road to the Big Windmill", [Requirements(ANY_SPLASHER)]),
        Shine("Down with Petey Piranha!", [Requirements([[NozzleType.spray]])]),
        Shine("100 Coins", [Requirements(ALL_SPLASHER)], hundred=True)
    ],
    blue_coins=[BlueCoin("Windmill M", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Windmill Pillar", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Towers House M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Balcony", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Underwater Right"),
        BlueCoin("Wall Side M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Wall Top M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Towers House", [Requirements([[NozzleType.hover]])]), # Could be done with just Spray, easily so I think?
        BlueCoin("Pinwheel", [Requirements(ANY_SPLASHER)]),
        BlueCoin("X Behind Wall", [Requirements(ANY_SPLASHER)]),
        BlueCoin("River End"),
        BlueCoin("X Between Walls", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Sail Platform", [Requirements([[NozzleType.hover]])]),  # Could also be done with just Spray...
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_THREE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_ONE} - Down with Petey Piranha!")],
    shines=[Shine("The Hillside Cave Secret", [Requirements(ROCKET_OR_HOVER)]),
        Shine("Red Coins of the Hillside Cave", [Requirements(ROCKET_OR_HOVER)])],
    blue_coins=[BlueCoin("Treetop", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Tourist", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Windmill Pokey", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Cliff", [Requirements(ROCKET_OR_HOVER)]),
        BlueCoin("Highest Platform", [Requirements(ROCKET_OR_HOVER)]),
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_FOUR: SmsRegion = SmsRegion(SmsRegionName.BIANCO_FOUR,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_THREE} - The Hillside Cave Secret")],
    shines=[Shine("Red Coins of Windmill Village", [Requirements(ROCKET_OR_HOVER)])],
    blue_coins=[BlueCoin("Hillside Pokey", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Bridge Underside")
    ],
    nozzle_boxes=[NozzleBox("Rocket Box")],
    parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_FIVE: SmsRegion = SmsRegion(SmsRegionName.BIANCO_FIVE,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_FOUR} - Red Coins of Windmill Village")],
    shines=[Shine("Petey Piranha Strikes Back", [Requirements(SPRAY_AND_ROCKET_OR_HOVER)])],
    blue_coins=[BlueCoin("Wall Tower Pianta", [Requirements(SPRAY_AND_ROCKET_OR_HOVER)]),
        BlueCoin("Platforms Cross", [Requirements(ROCKET_OR_HOVER)]),
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_SIX: SmsRegion = SmsRegion(SmsRegionName.BIANCO_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_FIVE} - Petey Piranha Strikes Back")],
    shines=[Shine("The Secret of the Dirty Lake", [Requirements(ANY_SPLASHER)]),
        Shine("Red Coins of the Dirty Lake", [Requirements([[NozzleType.hover]])])
    ],
    blue_coins = [BlueCoin("Petey Pillar", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Underwater Left"),
        BlueCoin("Blue Bird", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Chuckster Momma")
    ],
    nozzle_boxes = [NozzleBox("Turbo Box", [Requirements(ANY_SPLASHER)])],
    parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_SEVEN: SmsRegion = SmsRegion(SmsRegionName.BIANCO_SEVEN,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_SIX} - The Secret of the Dirty Lake")],
    shines=[Shine("Shadow Mario on the Loose", [Requirements([[NozzleType.spray]])])],
    blue_coins=[BlueCoin("Towers House O", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Balcony House O", [Requirements(ANY_SPLASHER)])
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)

BIANCO_HILLS_EIGHT: SmsRegion = SmsRegion(SmsRegionName.BIANCO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.BIANCO_SEVEN} - Shadow Mario on the Loose")],
    shines=[Shine("The Red Coins of the Lake", [Requirements(ROCKET_OR_HOVER)])],
    blue_coins=[BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Butterfly", [Requirements([[NozzleType.yoshi]])])
    ], parent_region=SmsRegionName.BIANCO_ENTRANCE)