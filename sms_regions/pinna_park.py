from .sms_region_helper import *
from .sms_region_helper import SmsRegionName

PINNA_PARK_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.PINNA_ENTRANCE,
    requirements=[Requirements(shines=10), Requirements(skip_forward=True)],
    ticketed="Pinna Park Ticket", parent_region=SmsRegionName.PLAZA)

PINNA_PARK_ONE: SmsRegion = SmsRegion(SmsRegionName.PINNA_ONE,
    shines=[Shine("Mecha-Bowser Appears!", [Requirements([[NozzleType.spray]])]),
        Shine("Red Coins of the Pirate Ships", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.PINNA_TWO} - The Beach Cannon's Secret")]),
        Shine("The Wilted Sunflowers", [Requirements(ANY_SPLASHER,
            location=f"{SmsRegionName.PINNA_ONE} - Red Coins of the Pirate Ships")]),
        Shine("100 Coins", [Requirements([[NozzleType.spray]])], hundred=True)],
    blue_coins=[BlueCoin("Tree Sand Shine", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Cannon Sand Shine", [Requirements(ANY_SPLASHER)])],
    parent_region=SmsRegionName.PINNA_ENTRANCE
    )

PINNA_PARK_ONE_THREE_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PINNA_ONE_THREE_FIVE_EIGHT,
    blue_coins=[BlueCoin("Orange Wall M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Sand M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Green Clam", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Left O", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Entrance Bird", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Pineapple Bird", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Ship Peak", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Cage Platform", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Right O", [Requirements(ANY_SPLASHER)]),
        BlueCoin("White Wall X", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Tree X", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Ferris M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Banana Triangle", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Ferris Triangle", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Stairs", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Girder", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Coaster Ledge", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Cage", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Stackin Stus", [Requirements(SPRAY_OR_HOVER)])],
    parent_region=SmsRegionName.PINNA_ENTRANCE)


PINNA_PARK_TWO: SmsRegion = SmsRegion(SmsRegionName.PINNA_TWO,
    requirements=[Requirements(location=f"{SmsRegionName.PINNA_ONE} - Mecha-Bowser Appears!")],
    shines=[Shine("The Beach Cannon's Secret", [Requirements(ANY_SPLASHER)]),
        Shine("Red Coins in the Cannon", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.PINNA_TWO} - The Beach Cannon's Secret")])],
    blue_coins=[BlueCoin("Spawn Basket"),
        BlueCoin("Flower Basket"),
        BlueCoin("Gate Basket"),
        BlueCoin("Rock Basket"),
        BlueCoin("Middle Basket"),
        BlueCoin("Sunflower Basket"),
    ], parent_region=SmsRegionName.PINNA_ENTRANCE)

PINNA_PARK_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.PINNA_FIVE_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.PINNA_ONE} - Red Coins of the Pirate Ships")],
    shines=[Shine("The Runaway Ferris Wheel", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Shadow Mario in the Park", [Requirements([[NozzleType.spray]],
            location=f"{SmsRegionName.PINNA_SIX} - The Yoshi-Go-Round's Secret")]),
        Shine("Roller Coaster Balloons", [Requirements([[NozzleType.spray]],
            location=f"{SmsRegionName.PINNA_SIX} - The Yoshi-Go-Round's Secret")])],
    blue_coins=[BlueCoin("Beach Butterfly A", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Beach Butterfly B", [Requirements([[NozzleType.yoshi]])])
    ], parent_region=SmsRegionName.PINNA_ENTRANCE)

PINNA_PARK_SIX: SmsRegion = SmsRegion(SmsRegionName.PINNA_SIX,
    requirements=[Requirements([[NozzleType.yoshi]], location=f"{SmsRegionName.PINNA_FIVE_EIGHT} - The Runaway Ferris Wheel")],
    shines=[Shine("The Yoshi-Go-Round's Secret", [Requirements([[NozzleType.yoshi]])]),
        Shine("Red Coins in the Yoshi-Go-Round", [Requirements(YOSHI_AND_HOVER)])],
    blue_coins=[BlueCoin("Park Butterfly", [Requirements([[NozzleType.yoshi]])])],
    parent_region=SmsRegionName.PINNA_ENTRANCE)