from .sms_region_helper import *


NOKI_BAY_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.NOKI_ENTRANCE,
    requirements = [Requirements(shines=20), Requirements(skip_forward=True)],
    parent_region = SmsRegionName.PLAZA)


NOKI_BAY_ALL: SmsRegion = SmsRegion(SmsRegionName.NOKI_ALL,
    shines=[Shine("Uncork the Waterfall", [Requirements(SPRAY_AND_HOVER)]),
        Shine("The Boss of Tricky Ruins", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Red Coins in a Bottle", [Requirements(location=f"{SmsRegionName.NOKI_ALL} - The Boss of Tricky Ruins")]), # Underwater Nozzle
        Shine("Eely-Mouth's Dentist", [Requirements(SPRAY_AND_HOVER)]), # Underwater Nozzle
        Shine("Il Piantissimo's Surf Swim", [Requirements(location=f"{SmsRegionName.NOKI_ALL} - Eely-Mouth's Dentist")]),
        Shine("The Shell's Secret", [Requirements([[NozzleType.hover]],
            location=f"{SmsRegionName.NOKI_ALL} - Il Piantissimo's Surf Swim")]),
        Shine("Hold It, Shadow Mario!", [Requirements(SPRAY_AND_HOVER)]),
        Shine("The Red Coin Fish", [Requirements([[NozzleType.hover]], location=f"{SmsRegionName.NOKI_ALL} - Hold It, Shadow Mario!")]), # Underwater Nozzle
        Shine("A Golden Bird", [Requirements([[NozzleType.spray]])]),
        Shine("Red Coins on the Half Shell",
            [Requirements([[NozzleType.hover]], location=f"{SmsRegionName.NOKI_ALL} - The Shell's Secret")]),
        Shine("100 Coins", [Requirements(SPRAY_AND_HOVER)], hundred=True)],
    blue_coins=[BlueCoin("Rocket Alcove", [Requirements(ROCKET_OR_HOVER)]),
        BlueCoin("Bottom Secret Path", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Top Secret Path", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Rocket", [Requirements([[NozzleType.rocket]])]),
        BlueCoin("Bottom Pulley", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Top Pulley", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Tall Alcove", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Turbo Alcove", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Shell Alcove", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Top Right Panel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bottom Left Panel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Top Right Tunnel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bottom Right Tunnel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bottom Right Alcove", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Left Tunnel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bottom Left Alcove", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bird Cliff Panel", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Bird Cliff Alcove", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Spawn", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Coast", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Underwater"),
        BlueCoin("Top Secret Path M", [Requirements(SPRAY_AND_HOVER)])
    ],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(ROCKET_OR_HOVER)])],
    ticketed="Noki Bay Ticket", parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_TWO_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_TWO_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Uncork the Waterfall")],
    blue_coins=[BlueCoin("Right Urn", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Left Urn", [Requirements(ANY_SPLASHER)])
    ], parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Red Coins in a Bottle")],
    blue_coins=[BlueCoin("Deep Sea Front Pillar", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Deep Sea Right Pillar", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Deep Sea Close Left Pillar", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Deep Sea Far Left Pillar", [Requirements([[NozzleType.hover]])])
    ], parent_region=SmsRegionName.NOKI_ENTRANCE)

NOKI_BAY_SIX_EIGHT: SmsRegion = SmsRegion(SmsRegionName.NOKI_SIX_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.NOKI_ALL} - Il Piantissimo's Surf Swim")],
    blue_coins=[BlueCoin("Spawn O", [Requirements(TURSPRAY)]),
        BlueCoin("Boathouse O", [Requirements(TURSPRAY)]),
    ],
    nozzle_boxes=[NozzleBox("Turbo Box", [Requirements([[NozzleType.hover]])])],
    parent_region=SmsRegionName.NOKI_ENTRANCE)