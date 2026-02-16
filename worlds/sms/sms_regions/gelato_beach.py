from .sms_region_helper import *

GELATO_BEACH_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ENTRANCE,
    requirements=[Requirements(ANY_SPLASHER, shines=5), Requirements(skip_forward=True)],
    ticketed="Gelato Beach Ticket", parent_region=SmsRegionName.PLAZA)

GELATO_BEACH_ONE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ONE,
    shines=[Shine("Dune Bud Sand Castle Secret", [Requirements(ANY_SPLASHER)]),
        Shine("Mirror Madness! Tilt, Slam, Bam!", [Requirements([[NozzleType.spray]])]),
        Shine("Wiggler Ahoy! Full Steam Ahead!", [Requirements(ANY_SPLASHER,
            location=f"{SmsRegionName.GELATO_ONE} - Mirror Madness! Tilt, Slam, Bam!")]),
        Shine("Red Coins in the Sand Castle", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!")]),
        Shine("Sandy Shine Sprite", [Requirements(ANY_SPLASHER)])],
    blue_coins=[BlueCoin("Juicer"),
        BlueCoin("Rocket M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Spawn Triangle", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Trees Triangle", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Left Bird", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Right Bird", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Highest Rope", [Requirements(ROCKET_OR_HOVER)]),
        BlueCoin("Pole", [Requirements(ROCKET_OR_HOVER)]),
        BlueCoin("Deck"),
        BlueCoin("Swing", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Big Tree"),
        BlueCoin("Crevice"),
        BlueCoin("Sand Cabana Roof"),
        BlueCoin("Shack", [Requirements([[NozzleType.rocket]])])], 
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_ONE_TWO_FOUR: SmsRegion = SmsRegion(SmsRegionName.GELATO_ONE_TWO_FOUR,
    blue_coins=[BlueCoin("Red Cataquack", [Requirements(ANY_SPLASHER)])], 
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_NOT_THREE: SmsRegion = SmsRegion(SmsRegionName.GELATO_NOT_THREE,
    blue_coins=[BlueCoin("Sand Shine at Sand Cabana", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Sand Shine at Surf Cabana", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Middle Sand Shine", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Close Underwater"),
        BlueCoin("Far Underwater"),
        BlueCoin("Blue Fish", [Requirements([[NozzleType.turbo]])]),
        BlueCoin("Red Fish", [Requirements([[NozzleType.turbo]])])],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_TWO_FOUR_THRU_EIGHT: SmsRegion = SmsRegion(SmsRegionName.GELATO_TWO_FOUR_THRU_EIGHT, 
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_ONE} - Dune Bud Sand Castle Secret")], 
    blue_coins=[BlueCoin("Big Sand Shine", [Requirements(ANY_SPLASHER)])], 
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_FOUR_ONLY: SmsRegion = SmsRegion(SmsRegionName.GELATO_FOUR_ONLY, 
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!")],
    shines=[Shine("The Sand Bird is Born", [Requirements([[NozzleType.hover]])])],
    blue_coins=[BlueCoin("Sand Bird A", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Sand Bird B", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Sand Bird C", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Sand Bird D", [Requirements([[NozzleType.hover]])])],
    nozzle_boxes=[NozzleBox("Turbo Box")], 
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.GELATO_FIVE_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FOUR_ONLY} - The Sand Bird is Born")],
    shines=[Shine("Il Piantissimo's Sand Sprint", [Requirements(TURBO_OR_HOVER)]),
        Shine("Red Coins in the Coral Reef"),
        Shine("It's Shadow Mario! After Him!", [Requirements([[NozzleType.spray]])]),
        Shine("The Watermelon Festival", [Requirements(TURBO_OR_SPLASHER)]),
        Shine("100 Coins", [Requirements(YOSHI_AND_SPRAY_OR_YOSHI_AND_HOVER)], hundred=True)],
    blue_coins=[BlueCoin("Blue Cataquack", [Requirements([[NozzleType.spray]])])],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(ROCKET_OR_SPLASHER)])],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_SIX: SmsRegion = SmsRegion(SmsRegionName.GELATO_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint")],
    blue_coins=[BlueCoin("Yellow Goo Dune Bud", [Requirements([[NozzleType.yoshi]])]),
        BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])])],
    parent_region=SmsRegionName.GELATO_ENTRANCE)