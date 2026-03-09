from .sms_region_helper import *

GELATO_BEACH_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ENTRANCE,
    requirements=[Requirements(ANY_SPLASHER, shines=5), Requirements(skip_forward=True)],
    ticketed="Gelato Beach Ticket", parent_region=SmsRegionName.PLAZA)

GELATO_BEACH_ONE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ONE,
    shines=[Shine("Dune Bud Sand Castle Secret", [Requirements(ANY_SPLASHER)], in_game_bit=20),
        Shine("Mirror Madness! Tilt, Slam, Bam!", [Requirements([[NozzleType.spray]])], in_game_bit=21),
        Shine("Wiggler Ahoy! Full Steam Ahead!", [Requirements(ANY_SPLASHER,
            location=f"{SmsRegionName.GELATO_ONE} - Mirror Madness! Tilt, Slam, Bam!")], in_game_bit=22),
        Shine("Red Coins in the Sand Castle", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!")], in_game_bit=28),
        Shine("Sandy Shine Sprite", [Requirements(ANY_SPLASHER)], in_game_bit=29)],
    blue_coins=[BlueCoin("Juicer", in_game_bit=275),
        BlueCoin("Rocket M", [Requirements(ANY_SPLASHER)], in_game_bit=276),
        BlueCoin("Spawn Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=277),
        BlueCoin("Trees Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=278),
        BlueCoin("Left Bird", [Requirements([[NozzleType.spray]])], in_game_bit=280),
        BlueCoin("Right Bird", [Requirements([[NozzleType.spray]])], in_game_bit=281),
        BlueCoin("Highest Rope", [Requirements(ROCKET_OR_HOVER)], in_game_bit=282),
        BlueCoin("Pole", [Requirements(ROCKET_OR_HOVER)], in_game_bit=283),
        BlueCoin("Deck", in_game_bit=288),
        BlueCoin("Swing", [Requirements(ANY_SPLASHER)], in_game_bit=289),
        BlueCoin("Big Tree", in_game_bit=290),
        BlueCoin("Crevice", in_game_bit=291),
        BlueCoin("Sand Cabana Roof", in_game_bit=293),
        BlueCoin("Shack", [Requirements([[NozzleType.rocket]])], in_game_bit=294)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_ONE_TWO_FOUR: SmsRegion = SmsRegion(SmsRegionName.GELATO_ONE_TWO_FOUR,
    blue_coins=[BlueCoin("Red Cataquack", [Requirements(ANY_SPLASHER)], in_game_bit=270)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_NOT_THREE: SmsRegion = SmsRegion(SmsRegionName.GELATO_NOT_THREE,
    blue_coins=[BlueCoin("Sand Shine at Sand Cabana", [Requirements(ANY_SPLASHER)], in_game_bit=271),
        BlueCoin("Sand Shine at Surf Cabana", [Requirements(ANY_SPLASHER)], in_game_bit=272),
        BlueCoin("Middle Sand Shine", [Requirements(ANY_SPLASHER)], in_game_bit=274),
        BlueCoin("Close Underwater", in_game_bit=284),
        BlueCoin("Far Underwater", in_game_bit=285),
        BlueCoin("Blue Fish", [Requirements([[NozzleType.turbo]])], in_game_bit=286),
        BlueCoin("Red Fish", [Requirements([[NozzleType.turbo]])], in_game_bit=287)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_TWO_FOUR_THRU_EIGHT: SmsRegion = SmsRegion(SmsRegionName.GELATO_TWO_FOUR_THRU_EIGHT, 
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_ONE} - Dune Bud Sand Castle Secret")], 
    blue_coins=[BlueCoin("Big Sand Shine", [Requirements(ANY_SPLASHER)], in_game_bit=292)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_FOUR_ONLY: SmsRegion = SmsRegion(SmsRegionName.GELATO_FOUR_ONLY, 
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!")],
    shines=[Shine("The Sand Bird is Born", [Requirements([[NozzleType.hover]])], in_game_bit=23)],
    blue_coins=[BlueCoin("Sand Bird A", [Requirements([[NozzleType.hover]])], in_game_bit=296),
        BlueCoin("Sand Bird B", [Requirements([[NozzleType.hover]])], in_game_bit=297),
        BlueCoin("Sand Bird C", [Requirements([[NozzleType.hover]])], in_game_bit=298),
        BlueCoin("Sand Bird D", [Requirements([[NozzleType.hover]])], in_game_bit=299)],
    nozzle_boxes=[NozzleBox("Turbo Box", in_game_bit=877)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_FIVE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.GELATO_FIVE_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FOUR_ONLY} - The Sand Bird is Born")],
    shines=[Shine("Il Piantissimo's Sand Sprint", [Requirements(TURBO_OR_HOVER)], in_game_bit=24),
        Shine("Red Coins in the Coral Reef", in_game_bit=25),
        Shine("It's Shadow Mario! After Him!", [Requirements([[NozzleType.spray]])], in_game_bit=26),
        Shine("The Watermelon Festival", [Requirements(TURBO_OR_SPLASHER)], in_game_bit=27),
        Shine("100 Coins", [Requirements(YOSHI_AND_SPRAY_OR_YOSHI_AND_HOVER)], hundred=True, in_game_bit=102)],
    blue_coins=[BlueCoin("Blue Cataquack", [Requirements([[NozzleType.spray]])], in_game_bit=273)],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(ROCKET_OR_SPLASHER)], in_game_bit=876)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)

GELATO_BEACH_SIX: SmsRegion = SmsRegion(SmsRegionName.GELATO_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint")],
    blue_coins=[BlueCoin("Yellow Goo Dune Bud", [Requirements([[NozzleType.yoshi]])], in_game_bit=279),
        BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=295)],
    parent_region=SmsRegionName.GELATO_ENTRANCE)