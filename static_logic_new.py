"""ALL_REGIONS: list[SmsRegion] = [
    # Pinna Park
    SmsRegion("Pinna Entrance", PINNA, Requirements(shines=10), [
        Shine("Mecha-Bowser Appears!", 523030, Requirements([NozzleType.spray])),
        Shine("Red Coins of the Pirate Ships", 523032,Requirements([NozzleType.hover], location="Pinna Park - The Beach Cannon's Secret")),
        Shine("The Wilted Sunflowers", 523033, Requirements([NozzleType.splasher], location="Pinna Park - Red Coins of the Pirate Ships"), bandaid=True),
        Shine("100 Coins", 523103, Requirements([NozzleType.spray]), hundred=True)],
        [
        BlueCoin("Tree Sand Shine", 523348, Requirements([NozzleType.splasher])),
        BlueCoin("Cannon Sand Shine", 523349, Requirements([NozzleType.splasher]))
        ], ticketed="Pinna Park Ticket", parent_region=STATUE),

    SmsRegion("Pinna 1, 3 and 5-8", PINNA, Requirements(), [], [
        BlueCoin("Orange Wall M", 523320, Requirements([NozzleType.splasher])),
        BlueCoin("Sand M", 523321, Requirements([NozzleType.splasher])),
        BlueCoin("Green Clam", 523322, Requirements([NozzleType.splasher])),
        BlueCoin("Left O", 523323, Requirements([NozzleType.splasher])),
        BlueCoin("Entrance Bird", 523324, Requirements([NozzleType.spray])),
        BlueCoin("Pineapple Bird", 523325, Requirements([NozzleType.spray])),
        BlueCoin("Ship Peak", 523326, Requirements([NozzleType.hover])),
        BlueCoin("Cage Platform", 523327, Requirements([NozzleType.hover])),
        BlueCoin("Right O", 523328, Requirements([NozzleType.splasher])),
        BlueCoin("White Wall X", 523329, Requirements([NozzleType.spray])),
        BlueCoin("Tree X", 523330, Requirements([NozzleType.spray])),
        BlueCoin("Ferris M", 523331, Requirements([NozzleType.splasher])),
        BlueCoin("Banana Triangle", 523332, Requirements([NozzleType.splasher])),
        BlueCoin("Ferris Triangle", 523333, Requirements([NozzleType.splasher])),
        BlueCoin("Stairs", 523334, Requirements([NozzleType.hover])),
        BlueCoin("Girder", 523336, Requirements([NozzleType.hover])),
        BlueCoin("Coaster Ledge", 523337, Requirements([NozzleType.hover])),
        BlueCoin("Cage", 523338, Requirements([NozzleType.hover])),
        BlueCoin("Stackin Stus", 523339, Requirements([NozzleType.spray | NozzleType.hover])),
    ], parent_region="Pinna Entrance"),

    SmsRegion("Pinna 2 Only", PINNA, Requirements(location="Pinna Park - Mecha-Bowser Appears!"), [
        Shine("The Beach Cannon's Secret", 523031, Requirements([NozzleType.splasher])),
        Shine("Red Coins in the Cannon", 523038, Requirements([NozzleType.hover], location="Pinna Park - The Beach Cannon's Secret"))], [
        BlueCoin("Spawn Basket", 523340),
        BlueCoin("Flower Basket", 523341),
        BlueCoin("Gate Basket", 523342),
        BlueCoin("Rock Basket", 523345),
        BlueCoin("Middle Basket", 523346),
        BlueCoin("Sunflower Basket", 523347)
    ], parent_region="Pinna Entrance"),

    SmsRegion("Pinna 5-8", PINNA, Requirements(location="Pinna Park - Red Coins of the Pirate Ships"), [
        Shine("The Runaway Ferris Wheel", 523034,
              Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Shadow Mario in the Park", 523036,
              Requirements([NozzleType.spray], location="Pinna Park - The Yoshi-Go-Round's Secret")),
        Shine("Roller Coaster Balloons", 523037,
              Requirements([NozzleType.spray], location="Pinna Park - The Yoshi-Go-Round's Secret"))], [
        BlueCoin("Beach Butterfly A", 523343, Requirements([NozzleType.yoshi])),
        BlueCoin("Beach Butterfly B", 523344, Requirements([NozzleType.yoshi]))
    ], parent_region="Pinna 2 Only"),

    SmsRegion("Pinna 6 Only", PINNA, Requirements(location="Pinna Park - The Runaway Ferris Wheel"), [
        Shine("The Yoshi-Go-Round's Secret", 523035,
              Requirements([NozzleType.yoshi])),
        Shine("Red Coins in the Yoshi-Go-Round", 523039,
              Requirements([NozzleType.yoshi, NozzleType.hover]))], [
        BlueCoin("Park Butterfly", 523335, Requirements([NozzleType.yoshi]))
    ], parent_region="Pinna 5-8"),

    # Sirena Beach
    SmsRegion("Sirena Entrance", SIRENA, Requirements([NozzleType.yoshi]), [
        Shine("The Manta Storm", 523040, Requirements([NozzleType.spray]))], [
        BlueCoin("Ocean", 523387)
    ], ticketed="Sirena Beach Ticket", parent_region=STATUE),

    SmsRegion("Sirena 1 and 6", SIRENA, Requirements(), [], [
        BlueCoin("Right Male Noki", 523373, Requirements([NozzleType.splasher])),
        BlueCoin("Right Female Noki", 523374, Requirements([NozzleType.splasher]))
    ], parent_region="Sirena Entrance"),

    SmsRegion("Sirena 2-8", SIRENA, Requirements(location="Sirena Beach - The Manta Storm"), [
        Shine("The Hotel Lobby's Secret", 523041, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("Red Coins in Boo's Big Mouth", 523048, Requirements([NozzleType.spray | NozzleType.hover]))], [
        BlueCoin("Sign", 523370, Requirements([NozzleType.splasher])),
        BlueCoin("Cabana Roof", 523371),
        BlueCoin("Outside Torch", 523372, Requirements([NozzleType.splasher])),
        BlueCoin("Hotel Ledge", 523375, Requirements([NozzleType.hover])),
        BlueCoin("Flowers", 523386, Requirements([NozzleType.splasher])),
        BlueCoin("Third Floor Lamp", 523392, Requirements([NozzleType.splasher]))
    ], parent_region="Sirena 1 and 6"),

    SmsRegion("Sirena 3-8", SIRENA, Requirements([NozzleType.yoshi], location="Sirena Beach - The Hotel Lobby's Secret"), [
        Shine("Mysterious Hotel Delfino", 523042, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Secret of Casino Delfino", 523043, Requirements([NozzleType.spray, NozzleType.hover])),
        # Technically only needs Spray below but then it'll think it's doable without doing the above Shine first...
        Shine("King Boo Down Below", 523044, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Scrubbing Sirena Beach", 523045, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Shadow Mario Checks In", 523046, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coins in the Hotel", 523047, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coin Winnings in the Casino", 523049, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("100 Coins", 523104, Requirements([NozzleType.spray]), hundred=True)], [
        BlueCoin("Big Light", 523376, Requirements([NozzleType.spray])),
        BlueCoin("Box Hole", 523378), # This hard requires Yoshi without Episode rando
        BlueCoin("Glass Hole", 523379),
        BlueCoin("White Painting", 523380, Requirements([NozzleType.splasher | NozzleType.yoshi])),
        BlueCoin("Dolpic Poster", 523381, Requirements([NozzleType.splasher])),
        BlueCoin("Bookshelf", 523382, Requirements([NozzleType.splasher])),
        BlueCoin("Attic", 523383)
    ], parent_region="Sirena 2-8"),

    SmsRegion("Sirena 4-5", SIRENA, Requirements(location="Sirena Beach - Mysterious Hotel Delfino"), [], [
        BlueCoin("Casino Torch", 523398, Requirements([NozzleType.splasher])),
        BlueCoin("Slot machine", 523399)
    ], parent_region="Sirena 3-8"),

    SmsRegion("Sirena 4-8", SIRENA, Requirements(location="Sirena Beach - Mysterious Hotel Delfino"), [], [
        BlueCoin("Crate", 523377),
        BlueCoin("Attic Boo", 523385)
    ], parent_region="Sirena 3-8"),

    SmsRegion("Sirena 5 Only", SIRENA, Requirements(location="Sirena Beach - The Secret of Casino Delfino"), [], [
        BlueCoin("Casino M", 523391, Requirements([NozzleType.spray]))
    ], parent_region="Sirena 4-8"),

    SmsRegion("Sirena 6 Only", SIRENA, Requirements(location="Sirena Beach - King Boo Down Below"), [], [
        BlueCoin("Left Male Noki", 523384, Requirements([NozzleType.splasher])),
        BlueCoin("Left Female Noki", 523390, Requirements([NozzleType.splasher]))
    ], parent_region="Sirena 5 Only"),

    SmsRegion("Sirena 7-8", SIRENA, Requirements(location="Sirena Beach - Scrubbing Sirena Beach"), [], [
        BlueCoin("Outside M", 523388, Requirements([NozzleType.splasher])),
        BlueCoin("Second Floor M", 523389, Requirements([NozzleType.splasher])),
        BlueCoin("Ground Floor Triangle", 523393, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("First Floor Triangle", 523394, Requirements([NozzleType.spray])),
        BlueCoin("Attic M", 523395, Requirements([NozzleType.spray])),
        BlueCoin("Second Floor X", 523396, Requirements([NozzleType.spray])),
        BlueCoin("First Floor X", 523397, Requirements([NozzleType.spray, NozzleType.hover]))
    ], parent_region="Sirena 6 Only"),


    # Noki Bay
    SmsRegion("Noki Entrance", "Noki Bay", Requirements(shines=20), [
        Shine("Uncork the Waterfall", 523050, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Boss of Tricky Ruins", 523051, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coins in a Bottle", 523052, Requirements(location="Noki Bay - The Boss of Tricky Ruins")), # Underwater Nozzle
        Shine("Eely-Mouth's Dentist", 523053, Requirements([NozzleType.spray, NozzleType.hover])), # Underwater Nozzle
        Shine("Il Piantissimo's Surf Swim", 523054, Requirements(location="Noki Bay - Eely-Mouth's Dentist")),
        Shine("The Shell's Secret", 523055, Requirements([NozzleType.hover], location="Noki Bay - Il Piantissimo's Surf Swim")),
        Shine("Hold It, Shadow Mario!", 523056, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Red Coin Fish", 523057, Requirements([NozzleType.hover], location="Noki Bay - Hold It, Shadow Mario!")), # Underwater Nozzle
        Shine("A Golden Bird", 523059, Requirements([NozzleType.spray])),
        Shine("Red Coins on the Half Shell", 523058, Requirements([NozzleType.hover], location="Noki Bay - The Shell's Secret")),
        Shine("100 Coins", 523105, Requirements([NozzleType.spray, NozzleType.hover]), hundred=True)],
        [],
    [
        NozzleBox("Rocket Box", 523884, Requirements([NozzleType.hover | NozzleType.rocket]))
    ], ticketed="Noki Bay Ticket", parent_region=STATUE),

    SmsRegion("Noki All Except 3", NOKI, Requirements(), [], [
        BlueCoin("Rocket Alcove", 523470, Requirements([NozzleType.hover | NozzleType.rocket])),
        BlueCoin("Bottom Secret Path", 523471, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Top Secret Path", 523472, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Rocket", 523473, Requirements([NozzleType.rocket])),
        BlueCoin("Bottom Pulley", 523474, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Top Pulley", 523475, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Tall Alcove", 523476, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Turbo Alcove", 523477, Requirements([NozzleType.hover])),
        BlueCoin("Shell Alcove", 523478, Requirements([NozzleType.hover])),
        BlueCoin("Top Right Panel", 523479, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bottom Left Panel", 523480, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Top Right Tunnel", 523481, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bottom Right Tunnel", 523482, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bottom Right Alcove", 523483, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Left Tunnel", 523484, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bottom Left Alcove", 523485, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bird Cliff Panel", 523486, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Bird Cliff Alcove", 523487, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Spawn", 523490, Requirements([NozzleType.spray])),
        BlueCoin("Coast", 523491, Requirements([NozzleType.spray])),
        BlueCoin("Underwater", 523492),
        BlueCoin("Top Secret Path M", 523493, Requirements([NozzleType.spray, NozzleType.hover]))
    ], parent_region="Noki Entrance"),

    SmsRegion("Noki 2 and 4-8", NOKI, Requirements(location="Noki Bay - Uncork the Waterfall"), [], [
        BlueCoin("Right Urn", 523488, Requirements([NozzleType.splasher])),
        BlueCoin("Left Urn", 523489, Requirements([NozzleType.splasher]))
    ], parent_region="Noki All Except 3"),

    SmsRegion("Noki 4 and 8", NOKI, Requirements(location="Noki Bay - Red Coins in a Bottle"), [], [
        BlueCoin("Deep Sea Front Pillar", 523495, Requirements([NozzleType.hover])),
        BlueCoin("Deep Sea Right Pillar", 523496, Requirements([NozzleType.hover])),
        BlueCoin("Deep Sea Close Left Pillar", 523497, Requirements([NozzleType.hover])),
        BlueCoin("Deep Sea Far Left Pillar", 523499, Requirements([NozzleType.hover]))
    ], parent_region="Noki 2 and 4-8"),

    SmsRegion("Noki 6-8", NOKI, Requirements(location="Noki Bay - Il Piantissimo's Surf Swim"), [], [
        BlueCoin("Spawn O", 523494, Requirements([NozzleType.spray, NozzleType.turbo])),
        BlueCoin("Boathouse O", 523498, Requirements([NozzleType.spray, NozzleType.turbo])),
    ], [
        NozzleBox("Turbo Box", 523885, Requirements([NozzleType.hover]))
    ], parent_region="Noki 4 and 8"),

    # Pianta Village
    SmsRegion("Pianta Entrance", "Pianta Village", Requirements([NozzleType.rocket], shines=10), [
        Shine("Chain Chomplets Unchained", 523060, Requirements([NozzleType.rocket, NozzleType.splasher])),
        Shine("Il Piantissimo's Crazy Climb", 523065, Requirements([NozzleType.rocket], location="Pianta Village - Chain Chomplets Unchained")), # Req. None
        Shine("The Goopy Inferno", 523062, Requirements([NozzleType.rocket, NozzleType.hover])),
        Shine("Chain Chomp's Bath", 523061, Requirements([NozzleType.rocket, NozzleType.splasher])),
        Shine("100 Coins", 523106, Requirements([NozzleType.rocket, NozzleType.yoshi, NozzleType.spray, NozzleType.hover]), hundred=True)],
        [
        BlueCoin("Giant M", 523430, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("River End", 523432, Requirements([NozzleType.rocket])),
        BlueCoin("Grass", 523433, Requirements([NozzleType.rocket])),
        BlueCoin("Back Tree", 523434, Requirements([NozzleType.rocket, NozzleType.hover])),
        BlueCoin("River Bridge", 523435, Requirements([NozzleType.rocket])),
        BlueCoin("Left Tree", 523438, Requirements([NozzleType.rocket, NozzleType.hover])),
        BlueCoin("Waterfall", 523439, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Wall Triangle", 523443, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Hot Tub Triangle", 523444, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Left M", 523445, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Right M", 523446, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Spawn M", 523447, Requirements([NozzleType.rocket, NozzleType.spray])),
        BlueCoin("Underside M", 523448, Requirements([NozzleType.rocket, NozzleType.spray]))
    ], ticketed="Pianta Village Ticket", parent_region=STATUE),

    SmsRegion("Pianta 1/3/5/7", PIANTA, Requirements(), [], [
        BlueCoin("Moon", 523420, Requirements([NozzleType.rocket, NozzleType.spray, NozzleType.hover])),
        BlueCoin("Statue's Nose", 523429, Requirements([NozzleType.rocket]))
    ], parent_region="Pianta Entrance"),

    SmsRegion("Pianta 2/4/6/8", PIANTA, Requirements(location="Pianta Village - Chain Chomplets Unchained"), [], [
        BlueCoin("Sign", 523431, Requirements([NozzleType.spray]))
    ], parent_region="Pianta 1/3/5/7"),

    SmsRegion("Pianta 3 Only", PIANTA, Requirements(location="Pianta Village - Il Piantissimo's Crazy Climb"), [], [
        BlueCoin("Burning Pianta", 523442, Requirements([NozzleType.spray])),
        BlueCoin("FLUDD M", 523449, Requirements([NozzleType.spray]))
    ], parent_region="Pianta 2/4/6/8"),

    SmsRegion("Pianta 5 Only", PIANTA, Requirements(location="Pianta Village - Chain Chomp's Bath"), [], [
        BlueCoin("Back Beehive", 523436, Requirements([NozzleType.yoshi])),
        BlueCoin("Front Beehive", 523437, Requirements([NozzleType.yoshi])),
        BlueCoin("Butterflies", 523440, Requirements([NozzleType.yoshi]))
    ], parent_region="Pianta 3 Only"),

    SmsRegion("Pianta 5 and Beyond", PIANTA, Requirements([NozzleType.yoshi]), [
        Shine("Secret of the Village Underside", 523064,
              Requirements([NozzleType.yoshi])),
        Shine("Piantas in Need", 523063,
              Requirements([NozzleType.splasher])),
        Shine("Shadow Mario Runs Wild", 523066,
              Requirements([NozzleType.spray], location="Pianta Village - Piantas in Need")),
        Shine("Fluff Festival Coin Hunt", 523067,
              Requirements([NozzleType.hover | NozzleType.rocket], location="Pianta Village - Shadow Mario Runs Wild")),
        Shine("Red Coin Chucksters", 523068,
              Requirements([NozzleType.hover]))], parent_region="Pianta 5 Only"),

    SmsRegion("Pianta 6 Only", PIANTA, Requirements(location="Pianta Village - Secret of the Village Underside"), [], [
        BlueCoin("Pianta in Need A", 523421, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need B", 523422, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need C", 523423, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need D", 523424, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need E", 523425, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need F", 523426, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need G", 523427, Requirements([NozzleType.spray])),
        BlueCoin("Pianta in Need H", 523428, Requirements([NozzleType.spray]))
    ], parent_region="Pianta 5 Only"),

    SmsRegion("Pianta 8 Only", PIANTA, Requirements(location="Pianta Village - Shadow Mario Runs Wild"), [
        Shine("Soak the Sun", 523069, Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket]))],
        [
        BlueCoin("Bird", 523441, Requirements([NozzleType.spray, NozzleType.hover]))
    ], [
        NozzleBox("Rocket Box", 523882, Requirements([NozzleType.hover]))
    ], parent_region="Pianta 6 Only"),
]"""
