from .sms_region_helper import *

# Still requires yoshi to clear out the pineapple blocking the pipe.
SIRENA_BEACH_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.SIRENA_ENTRANCE,
    requirements=[Requirements([[NozzleType.yoshi]])],
    ticketed="Sirena Beach Ticket", parent_region=SmsRegionName.PLAZA)

SIRENA_BEACH_ONE_SIX: SmsRegion = SmsRegion(SmsRegionName.SIRENA_ONE_SIX,
    shines=[Shine("The Manta Storm", [Requirements([[NozzleType.spray]])])],
    blue_coins=[BlueCoin("Ocean"),
        BlueCoin("Right Male Noki", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Right Female Noki", [Requirements(ANY_SPLASHER)])
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_TWO_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_TWO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_ONE_SIX} - The Manta Storm")],
    shines=[Shine("The Hotel Lobby's Secret", [Requirements(SPRAY_OR_HOVER)]),
        Shine("Red Coins in Boo's Big Mouth", [Requirements(SPRAY_OR_HOVER)])],
    blue_coins=[BlueCoin("Sign", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Cabana Roof"),
        BlueCoin("Outside Torch", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Hotel Ledge", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Flowers", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Third Floor Lamp", [Requirements(ANY_SPLASHER)])
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_THREE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_THREE_EIGHT,
    requirements=[Requirements(nozzles=[[NozzleType.yoshi]], location=f"{SIRENA_BEACH_TWO_EIGHT} - The Hotel Lobby's Secret")],
    shines=[Shine("Mysterious Hotel Delfino", [Requirements(SPRAY_AND_HOVER)]),
        Shine("The Secret of Casino Delfino", [Requirements(SPRAY_AND_HOVER)]),
        # Technically only needs Spray below but then it'll think it's doable without doing the above Shine first...
        Shine("King Boo Down Below", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Scrubbing Sirena Beach", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Shadow Mario Checks In", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Red Coins in the Hotel", [Requirements(SPRAY_AND_HOVER)]),
        Shine("Red Coin Winnings in the Casino", [Requirements(SPRAY_AND_HOVER)]),
        Shine("100 Coins", [Requirements([[NozzleType.spray]])], hundred=True)],
    blue_coins=[BlueCoin("Big Light", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Box Hole"), # This hard requires Yoshi without Episode rando
        BlueCoin("Glass Hole"),
        BlueCoin("White Painting", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Dolpic Poster", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Bookshelf", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Attic")
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FOUR_FIVE: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FOUR_FIVE,
    requirements=[Requirements(location=f"{SIRENA_BEACH_THREE_EIGHT} - Mysterious Hotel Delfino")],
    blue_coins=[BlueCoin("Casino Torch", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Slot machine")
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SIRENA_BEACH_THREE_EIGHT} - Mysterious Hotel Delfino")],
    blue_coins=[BlueCoin("Crate"),
        BlueCoin("Attic Boo")
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FIVE_ONLY: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FIVE_ONLY,
    requirements=[Requirements(location=f"{SIRENA_BEACH_THREE_EIGHT} - The Secret of Casino Delfino")],
    blue_coins=[BlueCoin("Casino M", [Requirements([[NozzleType.spray]])])
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_SIX_ONLY: SmsRegion = SmsRegion(SmsRegionName.SIRENA_SIX_ONLY,
    requirements=[Requirements(location=f"{SIRENA_BEACH_THREE_EIGHT} - King Boo Down Below")],
    blue_coins=[BlueCoin("Left Male Noki", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Left Female Noki", [Requirements(ANY_SPLASHER)])
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_SEVEN_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_SEVEN_EIGHT,
    requirements=[Requirements(location=f"{SIRENA_BEACH_THREE_EIGHT} - Scrubbing Sirena Beach")],
    blue_coins=[BlueCoin("Outside M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Second Floor M", [Requirements(ANY_SPLASHER)]),
        BlueCoin("Ground Floor Triangle", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("First Floor Triangle", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Attic M", [Requirements([[NozzleType.spray]])]),
        BlueCoin("Second Floor X", [Requirements([[NozzleType.spray]])]),
        BlueCoin("First Floor X", [Requirements(SPRAY_AND_HOVER)])
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)