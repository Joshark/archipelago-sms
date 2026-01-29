from .sms_region_helper import *

RICCO_HARBOR_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.RICCO_ENTRANCE,
    requirements=[Requirements(ALL_SPLASHER, shines=3), Requirements(ANY_SPLASHER, skip_forward=True)],
    parent_region=SmsRegionName.PLAZA)

RICCO_HARBOR_ONE: SmsRegion = SmsRegion(SmsRegionName.RICCO_ONE, 
        shines=[Shine("Ricco 1 Only - Gooper Blooper Breaks Out", [Requirements([[NozzleType.spray]])]),
        Shine("100 Coins", [Requirements([[NozzleType.hover]])], hundred=True)],
        blue_coins=[BlueCoin("Tower Wall", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Outer Ship M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Spawn Building Top M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Fruit Machine X", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Rooftop M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Far Ledge", [Requirements(ROCKET_OR_HOVER_AND_SPRAY)]),
        BlueCoin("Short Beam", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Tower Platform", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Long Beam", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Off Catwalk", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Crane", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Blooper Open Water", [Requirements([[NozzleType.rocket]])]),
        BlueCoin("Fountain"),
        BlueCoin("Underwater"),
        BlueCoin("Tower X", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Fountain M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Tower Crate"),
        BlueCoin("Tower Rocket", [Requirements([[NozzleType.rocket]])]),
        BlueCoin("Ricco 1 Only - Tower Ground M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Ricco 1 Only - Spawn Building Side M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Ricco 1 Only - Inner Ship M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Ricco 1 Only - Yellow Submarine", [Requirements([[NozzleType.spray]])])
    ], ticketed="Ricco Harbor Ticket", parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_TWO: SmsRegion = SmsRegion(SmsRegionName.RICCO_TWO,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_ONE} - Ricco 1 Only - Gooper Blooper Breaks Out")],
    shines=[Shine("Blooper Surfing Safari"),
        Shine("Blooper-Surfing Sequel")],
    blue_coins=[BlueCoin("Blooper Underground Entrance")],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_THREE: SmsRegion = SmsRegion(SmsRegionName.RICCO_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_TWO} - Blooper Surfing Safari")],
    shines=[Shine("The Caged Shine Sprite", [Requirements(ROCKET_OR_HOVER)])],
    blue_coins=[BlueCoin("Mesh Wall Klamber"),
        BlueCoin("Mesh Ceiling Klamber")],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements([[NozzleType.hover]])])],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_FOUR_SEVEN: SmsRegion = SmsRegion(SmsRegionName.RICCO_FOUR_SEVEN,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_THREE} - The Caged Shine Sprite")],
    shines=[Shine("The Secret of Ricco Tower", [Requirements(ROCKET_OR_HOVER)]),
        Shine("Gooper Blooper Returns", [Requirements([[NozzleType.spray]])]),
        Shine("Red Coins on the Water"),
        Shine("Shadow Mario Revisited", [Requirements([[NozzleType.spray]])]),
        Shine("Red Coins in Ricco Tower")],
    blue_coins=[BlueCoin("Caged Blooper", [Requirements(ROCKET_OR_HOVER)])],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.RICCO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_FOUR_SEVEN} - Shadow Mario Revisited")],
    shines=[Shine("Yoshi's Fruit Adventure", [Requirements([[NozzleType.yoshi]])])],
    blue_coins=[BlueCoin("Butterflies", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Wall Klamber", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("High Platform M", [Requirements(ROCKET_AND_SPLASHER)]),
        BlueCoin("Fish Basket", [Requirements([[NozzleType.spray]])])
    ],
    nozzle_boxes=[NozzleBox("Turbo Box")],
    parent_region=SmsRegionName.RICCO_ENTRANCE)
