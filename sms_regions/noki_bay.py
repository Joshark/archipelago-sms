from .sms_region_helper import *


NOKI_BAY_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.NOKI_ENTRANCE,
    requirements = [Requirements(shines=20), Requirements(skip_forward=True)],
    ticketed="Noki Bay Ticket", parent_region = SmsRegionName.PLAZA)

NOKI_BAY_ALL: SmsRegion = SmsRegion(SmsRegionName.NOKI_ALL,
    shines=[Shine("Uncork the Waterfall", [Requirements(SPRAY_AND_HOVER)], in_game_bit=50),
        Shine("The Boss of Tricky Ruins", [Requirements(SPRAY_AND_HOVER)], in_game_bit=51),
        Shine("Red Coins in a Bottle", [Requirements(location=f"{SmsRegionName.NOKI_ALL} - The Boss of Tricky Ruins")], in_game_bit=52), # Underwater Nozzle
        Shine("Eely-Mouth's Dentist", [Requirements(SPRAY_AND_HOVER)], in_game_bit=53), # Underwater Nozzle
        Shine("Il Piantissimo's Surf Swim", [Requirements(location=f"{SmsRegionName.NOKI_ALL} - Eely-Mouth's Dentist")], in_game_bit=54),
        Shine("The Shell's Secret", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.NOKI_ALL} - Il Piantissimo's Surf Swim")], in_game_bit=55),
        Shine("Hold It, Shadow Mario!", [Requirements(SPRAY_AND_HOVER)], in_game_bit=56),
        Shine("The Red Coin Fish", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.NOKI_ALL} - Hold It, Shadow Mario!")], in_game_bit=57), # Underwater Nozzle
        Shine("A Golden Bird", [Requirements([[NozzleType.spray]])], in_game_bit=59),
        Shine("Red Coins on the Half Shell", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.NOKI_ALL} - The Shell's Secret")], in_game_bit=58),
        Shine("100 Coins", [Requirements(SPRAY_AND_HOVER)], hundred=True, in_game_bit=105)],
    blue_coins=[BlueCoin("Rocket Alcove", [Requirements(ROCKET_OR_HOVER)], in_game_bit=470),
        BlueCoin("Bottom Secret Path", [Requirements(SPRAY_AND_HOVER)], in_game_bit=471),
        BlueCoin("Top Secret Path", [Requirements(SPRAY_AND_HOVER)], in_game_bit=472),
        BlueCoin("Rocket", [Requirements([[NozzleType.rocket]])], in_game_bit=473),
        BlueCoin("Bottom Pulley", [Requirements(SPRAY_AND_HOVER)], in_game_bit=474),
        BlueCoin("Top Pulley", [Requirements(SPRAY_AND_HOVER)], in_game_bit=475),
        BlueCoin("Tall Alcove", [Requirements(SPRAY_AND_HOVER)], in_game_bit=476),
        BlueCoin("Turbo Alcove", [Requirements([[NozzleType.hover]])], in_game_bit=477),
        BlueCoin("Shell Alcove", [Requirements([[NozzleType.hover]])], in_game_bit=478),
        BlueCoin("Top Right Panel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=479),
        BlueCoin("Bottom Left Panel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=480),
        BlueCoin("Top Right Tunnel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=481),
        BlueCoin("Bottom Right Tunnel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=482),
        BlueCoin("Bottom Right Alcove", [Requirements(SPRAY_AND_HOVER)], in_game_bit=483),
        BlueCoin("Left Tunnel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=484),
        BlueCoin("Bottom Left Alcove", [Requirements(SPRAY_AND_HOVER)], in_game_bit=485),
        BlueCoin("Bird Cliff Panel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=486),
        BlueCoin("Bird Cliff Alcove", [Requirements(SPRAY_AND_HOVER)], in_game_bit=487),
        BlueCoin("Spawn", [Requirements([[NozzleType.spray]])], in_game_bit=490),
        BlueCoin("Coast", [Requirements([[NozzleType.spray]])], in_game_bit=491),
        BlueCoin("Underwater", in_game_bit=492),
        BlueCoin("Top Secret Path M", [Requirements(SPRAY_AND_HOVER)], in_game_bit=493)
    ],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(ROCKET_OR_HOVER)], in_game_bit=884)],
    parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_TWO_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_TWO_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Uncork the Waterfall")],
    blue_coins=[BlueCoin("Right Urn", [Requirements(ANY_SPLASHER)], in_game_bit=488),
        BlueCoin("Left Urn", [Requirements(ANY_SPLASHER)], in_game_bit=489)
    ], parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Red Coins in a Bottle")],
    blue_coins=[BlueCoin("Deep Sea Front Pillar", [Requirements([[NozzleType.hover]])], in_game_bit=495),
        BlueCoin("Deep Sea Right Pillar", [Requirements([[NozzleType.hover]])], in_game_bit=496),
        BlueCoin("Deep Sea Close Left Pillar", [Requirements([[NozzleType.hover]])], in_game_bit=497),
        BlueCoin("Deep Sea Far Left Pillar", [Requirements([[NozzleType.hover]])], in_game_bit=499)
    ], parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_SIX_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_SIX_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Il Piantissimo's Surf Swim")],
    blue_coins=[BlueCoin("Spawn O", [Requirements(TURSPRAY)], in_game_bit=494),
        BlueCoin("Boathouse O", [Requirements(TURSPRAY)], in_game_bit=498),
    ],
    nozzle_boxes=[NozzleBox("Turbo Box", [Requirements([[NozzleType.hover]])], in_game_bit=885)],
    parent_region=SmsRegionName.NOKI_ENTRANCE)