from .sms_region_helper import *

# Pianta Village
PIANTA_VILLAGE_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ENTRANCE,
    requirements=[Requirements([[NozzleType.rocket]], shines=10), Requirements([[NozzleType.rocket]], skip_forward=True)],
    ticketed="Pianta Village Ticket", parent_region=SmsRegionName.PLAZA)

PIANTA_VILLAGE_ANY: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ANY,
    shines=[Shine("Chain Chomplets Unchained", [Requirements(ANY_SPLASHER)], in_game_bit=60),
        Shine("Il Piantissimo's Crazy Climb", [Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomplets Unchained")], in_game_bit=65),  # Req. None
        Shine("The Goopy Inferno", [Requirements([[NozzleType.hover]])], in_game_bit=62),
        Shine("Chain Chomp's Bath", [Requirements(ANY_SPLASHER)], in_game_bit=61),
        Shine("100 Coins", [Requirements(ALL_SPLASHER)], hundred=True, in_game_bit=106)],
    blue_coins=[BlueCoin("Giant M", [Requirements([[NozzleType.spray]])], in_game_bit=430),
        BlueCoin("River End", in_game_bit=432),
        BlueCoin("Grass", in_game_bit=433),
        BlueCoin("Back Tree", [Requirements([[NozzleType.hover]])], in_game_bit=434),
        BlueCoin("River Bridge", in_game_bit=435),
        BlueCoin("Left Tree", [Requirements([[NozzleType.hover]])], in_game_bit=438),
        BlueCoin("Waterfall", [Requirements([[NozzleType.spray]])], in_game_bit=439),
        BlueCoin("Wall Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=443),
        BlueCoin("Hot Tub Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=444),
        BlueCoin("Left M", [Requirements([[NozzleType.spray]])], in_game_bit=445),
        BlueCoin("Right M", [Requirements([[NozzleType.spray]])], in_game_bit=446),
        BlueCoin("Spawn M", [Requirements([[NozzleType.spray]])], in_game_bit=447),
        BlueCoin("Underside M", [Requirements([[NozzleType.spray]])], in_game_bit=448)
    ], ticketed="Pianta Village Ticket", parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_ODD: SmsRegion = SmsRegion(SmsRegionName.PIANTA_ODD,
    blue_coins=[BlueCoin("Moon", [Requirements(ROCKET_AND_SPRAY_AND_HOVER)], in_game_bit=420),
        BlueCoin("Statue's Nose", in_game_bit=429)
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_EVEN: SmsRegion = SmsRegion(SmsRegionName.PIANTA_EVEN, 
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomplets Unchained")],
    blue_coins=[BlueCoin("Sign", [Requirements([[NozzleType.spray]])], in_game_bit=431)],
    parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_THREE: SmsRegion = SmsRegion(SmsRegionName.PIANTA_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Il Piantissimo's Crazy Climb")],
    blue_coins=[BlueCoin("Burning Pianta", [Requirements([[NozzleType.spray]])], in_game_bit=442),
        BlueCoin("FLUDD M", [Requirements([[NozzleType.spray]])], in_game_bit=449)
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_FIVE_ONLY: SmsRegion = SmsRegion(SmsRegionName.PIANTA_FIVE_ONLY,
    requirements=[Requirements(location=f"{SmsRegionName.PIANTA_ANY} - Chain Chomp's Bath")],
    blue_coins=[BlueCoin("Back Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=436),
        BlueCoin("Front Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=437),
        BlueCoin("Butterflies", [Requirements([[NozzleType.yoshi]])], in_game_bit=440)
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_FIVE_BEYOND: SmsRegion = SmsRegion(SmsRegionName.PIANTA_FIVE_BEYOND,
    requirements=[Requirements([[NozzleType.yoshi]])],
    shines=[Shine("Secret of the Village Underside", [Requirements([[NozzleType.yoshi]])], in_game_bit=64),
        Shine("Piantas in Need", [Requirements(ANY_SPLASHER)], in_game_bit=63),
        Shine("Shadow Mario Runs Wild", [Requirements([[NozzleType.spray]], location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Piantas in Need")], in_game_bit=66),
        Shine("Fluff Festival Coin Hunt", [Requirements(ROCKET_OR_HOVER, location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Shadow Mario Runs Wild")], in_game_bit=67),
        Shine("Red Coin Chucksters", [Requirements([[NozzleType.hover]])], in_game_bit=68)
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_SIX: SmsRegion = SmsRegion(SmsRegionName.PIANTA_SIX,
    requirements=[Requirements([[NozzleType.yoshi]], location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Secret of the Village Underside")],
    blue_coins=[BlueCoin("Pianta in Need A", [Requirements([[NozzleType.spray]])], in_game_bit=421),
        BlueCoin("Pianta in Need B", [Requirements([[NozzleType.spray]])], in_game_bit=422),
        BlueCoin("Pianta in Need C", [Requirements([[NozzleType.spray]])], in_game_bit=423),
        BlueCoin("Pianta in Need D", [Requirements([[NozzleType.spray]])], in_game_bit=424),
        BlueCoin("Pianta in Need E", [Requirements([[NozzleType.spray]])], in_game_bit=425),
        BlueCoin("Pianta in Need F", [Requirements([[NozzleType.spray]])], in_game_bit=426),
        BlueCoin("Pianta in Need G", [Requirements([[NozzleType.spray]])], in_game_bit=427),
        BlueCoin("Pianta in Need H", [Requirements([[NozzleType.spray]])], in_game_bit=428)
    ], parent_region=SmsRegionName.PIANTA_ENTRANCE)

PIANTA_VILLAGE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PIANTA_EIGHT,
    requirements=[Requirements([[NozzleType.yoshi]], location=f"{SmsRegionName.PIANTA_FIVE_BEYOND} - Shadow Mario Runs Wild")],
    shines=[Shine("Soak the Sun", [Requirements(SPRAY_AND_HOVER_OR_ROCKET)], in_game_bit=69)],
    blue_coins=[BlueCoin("Bird", [Requirements(SPRAY_AND_HOVER)], in_game_bit=441)],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements([[NozzleType.hover]])], in_game_bit=882)],
    parent_region=SmsRegionName.PIANTA_ENTRANCE)