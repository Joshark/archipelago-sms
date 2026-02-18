from .sms_region_helper import *

RICCO_HARBOR_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.RICCO_ENTRANCE,
    requirements=[Requirements(ANY_SPLASHER, shines=3), Requirements(skip_forward=True)],
    ticketed="Ricco Harbor Ticket", parent_region=SmsRegionName.PLAZA)

RICCO_HARBOR_ONE: SmsRegion = SmsRegion(SmsRegionName.RICCO_ONE, 
    shines=[Shine("Ricco 1 Only - Gooper Blooper Breaks Out", [Requirements(SPRAY_OR_HOVER)], in_game_bit=10),
        Shine("100 Coins", [Requirements([[NozzleType.hover]])], hundred=True, in_game_bit=101)],
    blue_coins=[BlueCoin("Tower Wall", [Requirements([[NozzleType.spray]])], in_game_bit=221),
        BlueCoin("Outer Ship M", [Requirements(ANY_SPLASHER)], in_game_bit=222),
        BlueCoin("Spawn Building Top M", [Requirements(ANY_SPLASHER)], in_game_bit=223),
        BlueCoin("Fruit Machine X", [Requirements([[NozzleType.spray]])], in_game_bit=224),
        BlueCoin("Rooftop M", [Requirements(ANY_SPLASHER)], in_game_bit=226),
        BlueCoin("Far Ledge", [Requirements(ROCKET_OR_HOVER_AND_SPRAY)], in_game_bit=228),
        BlueCoin("Short Beam", [Requirements([[NozzleType.hover]])], in_game_bit=229),
        BlueCoin("Tower Platform", [Requirements([[NozzleType.hover]])], in_game_bit=230),
        BlueCoin("Long Beam", [Requirements([[NozzleType.hover]])], in_game_bit=231),
        BlueCoin("Off Catwalk", [Requirements([[NozzleType.hover]])], in_game_bit=232),
        BlueCoin("Crane", [Requirements([[NozzleType.hover]])], in_game_bit=234),
        BlueCoin("Blooper Open Water", [Requirements([[NozzleType.rocket]],
            location=f"{SmsRegionName.RICCO_ONE} - Ricco 1 Only - Gooper Blooper Breaks Out")], in_game_bit=235),
        BlueCoin("Fountain", in_game_bit=237),
        BlueCoin("Underwater", in_game_bit=238),
        BlueCoin("Tower X", [Requirements([[NozzleType.spray]])], in_game_bit=239),
        BlueCoin("Fountain M", [Requirements(ANY_SPLASHER)], in_game_bit=240),
        BlueCoin("Tower Crate", in_game_bit=248),
        BlueCoin("Tower Rocket", [Requirements([[NozzleType.rocket]])], in_game_bit=233),
        BlueCoin("Ricco 1 Only - Tower Ground M", [Requirements(ANY_SPLASHER)], in_game_bit=227),
        BlueCoin("Ricco 1 Only - Spawn Building Side M", [Requirements(ANY_SPLASHER)], in_game_bit=241),
        BlueCoin("Ricco 1 Only - Inner Ship M", [Requirements(ANY_SPLASHER)], in_game_bit=246),
        BlueCoin("Ricco 1 Only - Yellow Submarine", [Requirements([[NozzleType.spray]])], in_game_bit=249)],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_TWO: SmsRegion = SmsRegion(SmsRegionName.RICCO_TWO,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_ONE} - Ricco 1 Only - Gooper Blooper Breaks Out")],
    shines=[Shine("Blooper Surfing Safari", in_game_bit=11),
        Shine("Blooper-Surfing Sequel", in_game_bit=19)],
    blue_coins=[BlueCoin("Blooper Underground Entrance", in_game_bit=236)],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_THREE: SmsRegion = SmsRegion(SmsRegionName.RICCO_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_TWO} - Blooper Surfing Safari")],
    shines=[Shine("The Caged Shine Sprite", [Requirements(ROCKET_OR_HOVER)], in_game_bit=12)],
    blue_coins=[BlueCoin("Mesh Wall Klamber", in_game_bit=243),
        BlueCoin("Mesh Ceiling Klamber", in_game_bit=244)],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements([[NozzleType.hover]])], in_game_bit=874)],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_FOUR_SEVEN: SmsRegion = SmsRegion(SmsRegionName.RICCO_FOUR_SEVEN,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_THREE} - The Caged Shine Sprite")],
    shines=[Shine("The Secret of Ricco Tower", [Requirements(ROCKET_OR_HOVER)], in_game_bit=13),
        Shine("Gooper Blooper Returns", [Requirements([[NozzleType.spray]])], in_game_bit=14),
        Shine("Red Coins on the Water", in_game_bit=15),
        Shine("Shadow Mario Revisited", [Requirements([[NozzleType.spray]])], in_game_bit=16),
        Shine("Red Coins in Ricco Tower", in_game_bit=18)],
    blue_coins=[BlueCoin("Caged Blooper", [Requirements(ROCKET_OR_HOVER)], in_game_bit=247)],
    parent_region=SmsRegionName.RICCO_ENTRANCE)

RICCO_HARBOR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.RICCO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.RICCO_FOUR_SEVEN} - Shadow Mario Revisited")],
    shines=[Shine("Yoshi's Fruit Adventure", [Requirements([[NozzleType.yoshi]])], in_game_bit=17)],
    blue_coins=[BlueCoin("Butterflies", [Requirements([[NozzleType.yoshi]])], in_game_bit=220),
        BlueCoin("Wall Klamber", [Requirements([[NozzleType.yoshi]])], in_game_bit=225),
        BlueCoin("High Platform M", [Requirements(ROCKET_AND_SPLASHER)], in_game_bit=242),
        BlueCoin("Fish Basket", [Requirements([[NozzleType.spray]])], in_game_bit=245)
    ],
    nozzle_boxes=[NozzleBox("Turbo Box")],
    parent_region=SmsRegionName.RICCO_ENTRANCE)
