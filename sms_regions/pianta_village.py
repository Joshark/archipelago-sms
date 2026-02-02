from .sms_region_helper import *

# Pianta Village
PIANTA_VILLAGE_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ENTRANCE,
    requirements=[Requirements([[NozzleType.rocket]], shines=10), Requirements([[NozzleType.rocket]], skip_forward=True)],
    ticketed="Pianta Village Ticket", parent_region=SmsRegionName.PLAZA)

PIANTA_VILLAGE_ANY: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ANY,
    shines=[Shine("Chain Chomplets Unchained", [Requirements(ALL_SPLASHER)]),
        Shine("Il Piantissimo's Crazy Climb", [Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomplets Unchained")]),  # Req. None
        Shine("The Goopy Inferno", [Requirements([[NozzleType.hover]])]),
        Shine("Chain Chomp's Bath", [Requirements(ALL_SPLASHER)]),
        Shine("100 Coins", [Requirements(ALL_SPLASHER)], hundred=True)],
    blue_coins=[BlueCoin("Giant M", [Requirements([[NozzleType.spray]])]),
        BlueCoin("River End"),
        BlueCoin("Grass"),
        BlueCoin("Back Tree", [Requirements([[NozzleType.hover]])]),
        BlueCoin("River Bridge"),
        BlueCoin("Left Tree", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Waterfall", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Wall Triangle", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Hot Tub Triangle", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Left M", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Right M", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Spawn M", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Underside M", [Requirements([[NozzleType.spray]])])
    ], ticketed="Pianta Village Ticket", parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_ODD: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ODD,
    blue_coins=[BlueCoin("Moon", [Requirements(ROCKET_AND_SPRAY_AND_HOVER)]),
        BlueCoin("Statue's Nose")
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_EVEN: SmsRegion = SmsRegion(SmsRegionName.PIANTA_EVEN, 
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomplets Unchained")],
    blue_coins=[BlueCoin("Sign", [Requirements([[NozzleType.spray]])])], 
    parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_THREE: SmsRegion = SmsRegion(SmsRegionName.PIANTA_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Il Piantissimo's Crazy Climb")],
    blue_coins=[BlueCoin("Burning Pianta", [Requirements([[NozzleType.spray]])]),
        BlueCoin("FLUDD M", [Requirements([[NozzleType.spray]])])
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_FIVE_ONLY: SmsRegion = SmsRegion(SmsRegionName.PIANTA_FIVE_ONLY,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomp's Bath")],
    blue_coins=[BlueCoin("Back Beehive", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Front Beehive", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Butterflies", [Requirements([[NozzleType.yoshi]])])
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_FIVE_BEYOND: SmsRegion = SmsRegion(SmsRegionName.PIANTA_FIVE_BEYOND,
    requirements=[Requirements([[NozzleType.yoshi]])],
    shines=[Shine("Secret of the Village Underside", [Requirements([[NozzleType.yoshi]])]),
        Shine("Piantas in Need", [Requirements(ANY_SPLASHER)]),
        Shine("Shadow Mario Runs Wild", [Requirements([[NozzleType.spray]], location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Piantas in Need")]),
        Shine("Fluff Festival Coin Hunt", [Requirements(ROCKET_OR_HOVER, location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Shadow Mario Runs Wild")]),
        Shine("Red Coin Chucksters", [Requirements([[NozzleType.hover]])])
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_SIX: SmsRegion = SmsRegion(SmsRegionName.PIANTA_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Secret of the Village Underside")],
    blue_coins=[BlueCoin("Pianta in Need A", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need B", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need C", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need D", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need E", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need F", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need G", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pianta in Need H", [Requirements([[NozzleType.spray]])])
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PIANTA_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Shadow Mario Runs Wild")],
    shines=[Shine("Soak the Sun", [Requirements(SPRAY_AND_HOVER_OR_ROCKET)])],
    blue_coins=[BlueCoin("Bird", [Requirements(SPRAY_AND_HOVER)])],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements([[NozzleType.hover]])])],
    parent_region=SmsRegionName.PIANTA_ENTRANCE)