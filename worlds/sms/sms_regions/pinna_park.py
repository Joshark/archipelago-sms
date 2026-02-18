from .sms_region_helper import *
from .sms_region_helper import SmsRegionName

PINNA_PARK_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.PINNA_ENTRANCE,
    requirements=[Requirements(shines=10), Requirements(skip_forward=True)],
    ticketed="Pinna Park Ticket", parent_region=SmsRegionName.PLAZA)

PINNA_PARK_ONE: SmsRegion = SmsRegion(SmsRegionName.PINNA_ONE,
    shines=[Shine("Mecha-Bowser Appears!", [Requirements([[NozzleType.spray]])], in_game_bit=30),
        Shine("Red Coins of the Pirate Ships", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.PINNA_TWO} - The Beach Cannon's Secret")], in_game_bit=32),
        Shine("The Wilted Sunflowers", [Requirements(ANY_SPLASHER,
            location=f"{SmsRegionName.PINNA_ONE} - Red Coins of the Pirate Ships")], in_game_bit=33),
        Shine("100 Coins", [Requirements([[NozzleType.spray]])], hundred=True, in_game_bit=103)],
    blue_coins=[BlueCoin("Tree Sand Shine", [Requirements(ANY_SPLASHER)], in_game_bit=348),
        BlueCoin("Cannon Sand Shine", [Requirements(ANY_SPLASHER)], in_game_bit=349)],
    parent_region=SmsRegionName.PINNA_ENTRANCE
    )

PINNA_PARK_ONE_THREE_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PINNA_ONE_THREE_FIVE_EIGHT,
    blue_coins=[BlueCoin("Orange Wall M", [Requirements(ANY_SPLASHER)], in_game_bit=320),
        BlueCoin("Sand M", [Requirements(ANY_SPLASHER)], in_game_bit=321),
        BlueCoin("Green Clam", [Requirements(ANY_SPLASHER)], in_game_bit=322),
        BlueCoin("Left O", [Requirements(ANY_SPLASHER)], in_game_bit=323),
        BlueCoin("Entrance Bird", [Requirements([[NozzleType.spray]])], in_game_bit=324),
        BlueCoin("Pineapple Bird", [Requirements([[NozzleType.spray]])], in_game_bit=325),
        BlueCoin("Ship Peak", [Requirements([[NozzleType.hover]])], in_game_bit=326),
        BlueCoin("Cage Platform", [Requirements([[NozzleType.hover]])], in_game_bit=327),
        BlueCoin("Right O", [Requirements(ANY_SPLASHER)], in_game_bit=328),
        BlueCoin("White Wall X", [Requirements([[NozzleType.spray]])], in_game_bit=329),
        BlueCoin("Tree X", [Requirements([[NozzleType.spray]])], in_game_bit=330),
        BlueCoin("Ferris M", [Requirements(ANY_SPLASHER)], in_game_bit=331),
        BlueCoin("Banana Triangle", [Requirements(ANY_SPLASHER)], in_game_bit=332),
        BlueCoin("Ferris Triangle", [Requirements(ANY_SPLASHER)], in_game_bit=333),
        BlueCoin("Stairs", [Requirements([[NozzleType.hover]])], in_game_bit=334),
        BlueCoin("Girder", [Requirements([[NozzleType.hover]])], in_game_bit=336),
        BlueCoin("Coaster Ledge", [Requirements([[NozzleType.hover]])], in_game_bit=337),
        BlueCoin("Cage", [Requirements([[NozzleType.hover]])], in_game_bit=338),
        BlueCoin("Stackin Stus", [Requirements(SPRAY_OR_HOVER)], in_game_bit=339)],
    parent_region=SmsRegionName.PINNA_ENTRANCE)


PINNA_PARK_TWO: SmsRegion = SmsRegion(SmsRegionName.PINNA_TWO,
    requirements=[Requirements(location=f"{SmsRegionName.PINNA_ONE} - Mecha-Bowser Appears!")],
    shines=[Shine("The Beach Cannon's Secret", [Requirements(ANY_SPLASHER)], in_game_bit=31),
        Shine("Red Coins in the Cannon", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.PINNA_TWO} - The Beach Cannon's Secret")], in_game_bit=38)],
    blue_coins=[BlueCoin("Spawn Basket", in_game_bit=340),
        BlueCoin("Flower Basket", in_game_bit=341),
        BlueCoin("Gate Basket", in_game_bit=342),
        BlueCoin("Rock Basket", in_game_bit=345),
        BlueCoin("Middle Basket", in_game_bit=346),
        BlueCoin("Sunflower Basket", in_game_bit=347),
    ], parent_region=SmsRegionName.PINNA_ENTRANCE)

PINNA_PARK_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PINNA_FIVE_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.PINNA_ONE} - Red Coins of the Pirate Ships")],
    shines=[Shine("The Runaway Ferris Wheel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=34),
        Shine("Shadow Mario in the Park", [Requirements([[NozzleType.spray]],
            location=f"{SmsRegionName.PINNA_SIX} - The Yoshi-Go-Round's Secret")], in_game_bit=36),
        Shine("Roller Coaster Balloons", [Requirements([[NozzleType.spray]],
            location=f"{SmsRegionName.PINNA_SIX} - The Yoshi-Go-Round's Secret")], in_game_bit=37)],
    blue_coins=[BlueCoin("Beach Butterfly A", [Requirements([[NozzleType.yoshi]])], in_game_bit=343),
        BlueCoin("Beach Butterfly B", [Requirements([[NozzleType.yoshi]])], in_game_bit=344)
    ], parent_region=SmsRegionName.PINNA_ENTRANCE)

PINNA_PARK_SIX: SmsRegion = SmsRegion(SmsRegionName.PINNA_SIX,
    requirements=[Requirements([[NozzleType.yoshi]], location=f"{SmsRegionName.PINNA_FIVE_EIGHT} - The Runaway Ferris Wheel")],
    shines=[Shine("The Yoshi-Go-Round's Secret", [Requirements([[NozzleType.yoshi]])], in_game_bit=35),
        Shine("Red Coins in the Yoshi-Go-Round", [Requirements(YOSHI_AND_HOVER)], in_game_bit=39)],
    blue_coins=[BlueCoin("Park Butterfly", [Requirements([[NozzleType.yoshi]])], in_game_bit=335)],
    parent_region=SmsRegionName.PINNA_ENTRANCE)