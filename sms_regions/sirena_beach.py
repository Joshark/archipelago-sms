from .sms_region_helper import *

# Non-ticket requires yoshi to clear out the pineapple blocking the pipe. Ticket removes pineapple.
SIRENA_BEACH_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.SIRENA_ENTRANCE,
    requirements=[Requirements([[NozzleType.yoshi]]), Requirements(skip_forward=True)],
    ticketed="Sirena Beach Ticket", parent_region=SmsRegionName.PLAZA)

SIRENA_BEACH_ONE_SIX: SmsRegion = SmsRegion(SmsRegionName.SIRENA_ONE_SIX,
    shines=[Shine("The Manta Storm", [Requirements([[NozzleType.spray]])], in_game_bit=40)],
    blue_coins=[BlueCoin("Ocean", in_game_bit=387),
        BlueCoin("Right Male Noki", [Requirements(ANY_SPLASHER)], in_game_bit=373),
        BlueCoin("Right Female Noki", [Requirements(ANY_SPLASHER)], in_game_bit=374)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_TWO_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_TWO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_ONE_SIX} - The Manta Storm")],
    shines=[Shine("The Hotel Lobby's Secret", [Requirements(SPRAY_OR_HOVER)], in_game_bit=41),
        Shine("Red Coins in Boo's Big Mouth", [Requirements(SPRAY_OR_HOVER)], in_game_bit=48)],
    blue_coins=[BlueCoin("Sign", [Requirements(ANY_SPLASHER)], in_game_bit=370),
        BlueCoin("Cabana Roof", in_game_bit=371),
        BlueCoin("Outside Torch", [Requirements(ANY_SPLASHER)], in_game_bit=372),
        BlueCoin("Hotel Ledge", [Requirements([[NozzleType.hover]])], in_game_bit=375),
        BlueCoin("Flowers", [Requirements(ANY_SPLASHER)], in_game_bit=386),
        BlueCoin("Third Floor Lamp", [Requirements(ANY_SPLASHER)], in_game_bit=392)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_THREE_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_THREE_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_TWO_EIGHT} - The Hotel Lobby's Secret")],
    shines=[Shine("Mysterious Hotel Delfino", [Requirements(SPRAY_AND_HOVER)], in_game_bit=42),
        Shine("The Secret of Casino Delfino", [Requirements(SPRAY_AND_HOVER)], in_game_bit=43),
        # Technically only needs Spray below but then it'll think it's doable without doing the above Shine first...
        Shine("King Boo Down Below", [Requirements(SPRAY_AND_HOVER)], in_game_bit=44),
        Shine("Scrubbing Sirena Beach", [Requirements(SPRAY_AND_HOVER)], in_game_bit=45),
        Shine("Shadow Mario Checks In", [Requirements(SPRAY_AND_HOVER)], in_game_bit=46),
        Shine("Red Coins in the Hotel", [Requirements(SPRAY_AND_HOVER)], in_game_bit=47),
        Shine("Red Coin Winnings in the Casino", [Requirements(SPRAY_AND_HOVER)], in_game_bit=49),
        Shine("100 Coins", [Requirements([[NozzleType.spray]])], hundred=True, in_game_bit=104)],
    blue_coins=[BlueCoin("Big Light", [Requirements([[NozzleType.spray]])], in_game_bit=376),
        BlueCoin("Box Hole", [Requirements([[NozzleType.yoshi]])], in_game_bit=378), # This hard requires Yoshi without Episode rando
        BlueCoin("Glass Hole", in_game_bit=379),
        BlueCoin("White Painting", [Requirements(ANY_SPLASHER)], in_game_bit=380),
        BlueCoin("Dolpic Poster", [Requirements(ANY_SPLASHER)], in_game_bit=381),
        BlueCoin("Bookshelf", [Requirements(ANY_SPLASHER)], in_game_bit=382),
        BlueCoin("Attic", in_game_bit=383)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FOUR_FIVE: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FOUR_FIVE,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_THREE_EIGHT} - Mysterious Hotel Delfino")],
    blue_coins=[BlueCoin("Casino Torch", [Requirements(ANY_SPLASHER)], in_game_bit=398),
        BlueCoin("Slot machine", in_game_bit=399)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FOUR_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FOUR_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_THREE_EIGHT} - Mysterious Hotel Delfino")],
    blue_coins=[BlueCoin("Crate", in_game_bit=377),
        BlueCoin("Attic Boo", in_game_bit=385)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_FIVE_ONLY: SmsRegion = SmsRegion(SmsRegionName.SIRENA_FIVE_ONLY,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_THREE_EIGHT} - The Secret of Casino Delfino")],
    blue_coins=[BlueCoin("Casino M", [Requirements([[NozzleType.spray]])], in_game_bit=391)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_SIX_ONLY: SmsRegion = SmsRegion(SmsRegionName.SIRENA_SIX_ONLY,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_THREE_EIGHT} - King Boo Down Below")],
    blue_coins=[BlueCoin("Left Male Noki", [Requirements(ANY_SPLASHER)], in_game_bit=384),
        BlueCoin("Left Female Noki", [Requirements(ANY_SPLASHER)], in_game_bit=390)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)

SIRENA_BEACH_SEVEN_EIGHT: SmsRegion = SmsRegion(SmsRegionName.SIRENA_SEVEN_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.SIRENA_THREE_EIGHT} - Scrubbing Sirena Beach")],
    blue_coins=[BlueCoin("Outside M", [Requirements(ANY_SPLASHER)], in_game_bit=388),
        BlueCoin("Second Floor M", [Requirements(ANY_SPLASHER)], in_game_bit=389),
        BlueCoin("Ground Floor Triangle", [Requirements(SPRAY_AND_HOVER)], in_game_bit=393),
        BlueCoin("First Floor Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=394),
        BlueCoin("Attic M", [Requirements([[NozzleType.spray]])], in_game_bit=395),
        BlueCoin("Second Floor X", [Requirements([[NozzleType.spray]])], in_game_bit=396),
        BlueCoin("First Floor X", [Requirements(SPRAY_AND_HOVER)], in_game_bit=397)
    ], parent_region=SmsRegionName.SIRENA_ENTRANCE)