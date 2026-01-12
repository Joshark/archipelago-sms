from enum import Flag, auto
from typing import Optional, NamedTuple

AIRSTRIP = "Delfino Airstrip"
PLAZA = "Delfino Plaza"
INIT = "Initial Plaza"
STATUE = "Plaza With Statue"
BIANCO = "Bianco Hills"
RICCO = "Ricco Harbor"
GELATO = "Gelato Beach"
PINNA = "Pinna Park"
SIRENA = "Sirena Beach"
NOKI = "Noki Bay"
PIANTA = "Pianta Village"
CORONA = "Corona Mountain"

class NozzleType(Flag):
    none = auto()
    spray = auto()
    hover = auto()
    rocket = auto()
    nobox_rocket = auto()
    turbo = auto()
    nobox_turbo = auto()
    yoshi = auto()
    splasher = auto()  # Customizable generic, for things that are intended for spray but can be hit with others


class Requirements(NamedTuple):
    nozzles: list[NozzleType] = []  # conjunctive normal form
    shines: Optional[int] = None  # number of shine sprites needed
    corona: bool = False  # is corona access needed (configurable)
    blues: int = 0
    location: str = ""
    skip_into: bool = False


class Shine(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()
    hard: Requirements = Requirements()
    advanced: Requirements = Requirements()
    tears: Requirements = Requirements()
    hundred: bool = False
    bandaid: bool = False


class BlueCoin(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()
    hard: Requirements = Requirements()
    advanced: Requirements = Requirements()
    tears: Requirements = Requirements()
    available: [int] = []

class OneUp(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()
    available: [int] = []

# Yes, I'm going to include Shadow Mario Plaza chases as NozzleBox Locations
class NozzleBox(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()
    available: [int] = []


class SmsRegion(NamedTuple):
    name: str
    display: str
    requirements: Requirements = Requirements()
    shines: list[Shine] = []
    blue_coins: list[BlueCoin] = []
    nozzle_boxes: list[NozzleBox] = []
    one_ups: list[OneUp] = []
    ticketed: str = ""
    trade: bool = False
    parent_region: str = "Menu"
    skipped: bool = False


ALL_REGIONS: list[SmsRegion] = [
    # Delfino Airstrip
    SmsRegion(AIRSTRIP, AIRSTRIP, Requirements(), [
        Shine("Delfino Airstrip Dilemma", 523086, Requirements([NozzleType.splasher]))
        ], [], skipped=True),


    # Delfino Plaza
    SmsRegion(INIT, PLAZA, Requirements([NozzleType.splasher], skip_into=True),
    [
        Shine("Shine Sprite in the Sand", 523117, Requirements([NozzleType.hover])),
        Shine("Clean the West Bell", 523096, Requirements([NozzleType.hover | NozzleType.yoshi])),
        Shine("Super Slide", 523090, Requirements([NozzleType.hover | NozzleType.rocket])),
        Shine("The Gold Bird", 523118, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Turbo Dash!", 523116, Requirements([NozzleType.turbo])),
        Shine("Lighthouse Roof", 523093, Requirements([NozzleType.rocket])),
        Shine("Clean the East Bell", 523097, Requirements([NozzleType.rocket, NozzleType.splasher])),
        Shine("Shine Gate", 523099, Requirements([NozzleType.spray, NozzleType.rocket])),
        Shine("Pachinko Game", 523089, Requirements([NozzleType.hover])),
        Shine("Lily Pad Ride", 523091, Requirements([NozzleType.hover, NozzleType.spray, NozzleType.yoshi])),
        Shine("Turbo Track", 523087, Requirements([NozzleType.turbo])),
        Shine("Red Coin Field", 523092,
              Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover]))],
    [
        BlueCoin("Turbo Pillar", 523121, Requirements([NozzleType.turbo])),
        BlueCoin("Burning Pianta", 523124, Requirements([NozzleType.splasher])),
        BlueCoin("Shine Gate M", 523125, Requirements([NozzleType.splasher])),
        BlueCoin("Tower M", 523126, Requirements([NozzleType.splasher])),
        BlueCoin("Chuckster Room M", 523127, Requirements([NozzleType.splasher])),
        BlueCoin("Sea Sewer", 523132),
        BlueCoin("Tower Yellow Goo", 523133, Requirements([NozzleType.yoshi])),
        BlueCoin("Jail Cell", 523134),
        BlueCoin("Police Station Yellow Goo", 523135, Requirements([NozzleType.yoshi])),
        BlueCoin("Shine Gate Sewer", 523136),
        BlueCoin("Canal Sewer", 523137),
        BlueCoin("Blue Bird Near Sirena Pipe", 523138, Requirements([NozzleType.spray | NozzleType.yoshi])),
        BlueCoin("Blue Bird Near Crate Guy", 523139, Requirements([NozzleType.spray | NozzleType.yoshi]))
    ],parent_region=AIRSTRIP),

    SmsRegion(STATUE, PLAZA, Requirements([NozzleType.spray | NozzleType.yoshi], skip_into=True), [
        Shine("Boxing Clever 1", 523094),
        Shine("Boxing Clever 2", 523095),
        Shine("Chuckster", 523098),
        Shine("100 Coins", 523107, Requirements([NozzleType.hover | NozzleType.rocket]), hundred=True)], [
        BlueCoin("Statue X", 523122, Requirements([NozzleType.splasher])),
        BlueCoin("Bell Tower X", 523123, Requirements([NozzleType.splasher])),
        BlueCoin("Pineapple Basket", 523128),
        BlueCoin("Durian Basket", 523129),
        BlueCoin("Banana Basket", 523130),
        BlueCoin("Coconut Basket", 523131, Requirements([NozzleType.splasher]))], [
        # NozzleBox("Shadow Mario Yoshi Egg Chase", 523911, Requirements([NozzleType.spray], location="Pinna Park - The Wilted Sunflowers")),
        # NozzleBox("Shadow Mario Rocket Nozzle Chase", 523870, Requirements([NozzleType.splasher, NozzleType.yoshi], shines=30)),
        # NozzleBox("Shadow Mario Turbo Nozzle Chase", 523871, Requirements([NozzleType.splasher, NozzleType.yoshi], shines=25)),
    ], parent_region=INIT),


    # Bianco Hills
    SmsRegion("Bianco Entrance", BIANCO, Requirements([NozzleType.spray | NozzleType.yoshi], skip_into=True), [
        Shine("Road to the Big Windmill", 523000, Requirements([NozzleType.spray])),
        Shine("Down with Petey Piranha!", 523001,
              Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("100 Coins", 523100, Requirements([NozzleType.yoshi, NozzleType.spray, NozzleType.hover]), hundred=True)], [
        BlueCoin("Windmill M", 523170, Requirements([NozzleType.hover])),
        BlueCoin("Windmill Pillar", 523171, Requirements([NozzleType.splasher])),
        BlueCoin("Towers House M", 523188, Requirements([NozzleType.splasher])),
        BlueCoin("Balcony", 523173, Requirements([NozzleType.hover])),
        BlueCoin("Underwater Right", 523180),
        BlueCoin("Wall Side M", 523186, Requirements([NozzleType.splasher])),
        BlueCoin("Wall Top M", 523187, Requirements([NozzleType.splasher])),
        BlueCoin("Towers House", 523172, Requirements([NozzleType.hover])), # Could be done with just Spray, easily so I think?
        BlueCoin("Pinwheel", 523189, Requirements([NozzleType.splasher])),
        BlueCoin("X Behind Wall", 523190, Requirements([NozzleType.splasher])),
        BlueCoin("River End", 523191),
        BlueCoin("X Between Walls", 523197, Requirements([NozzleType.splasher])),
        BlueCoin("Sail Platform", 523198, Requirements([NozzleType.hover])) # Could also be done with just Spray...
    ], ticketed="Bianco Hills Ticket", parent_region=STATUE),

    SmsRegion("Bianco 3", BIANCO, Requirements(location="Bianco Hills - Down with Petey Piranha!"), [
        Shine("The Hillside Cave Secret", 523002,
              Requirements([NozzleType.hover | NozzleType.rocket])),
        Shine("Red Coins of the Hillside Cave", 523008,
              Requirements([NozzleType.hover | NozzleType.rocket]))], [
        BlueCoin("Treetop", 523174, Requirements([NozzleType.splasher])),
        BlueCoin("Tourist", 523175, Requirements([NozzleType.splasher])),
        BlueCoin("Windmill Pokey", 523184, Requirements([NozzleType.hover])),
        BlueCoin("Cliff", 523192, Requirements([NozzleType.hover | NozzleType.rocket])),
        BlueCoin("Highest Platform", 523199, Requirements([NozzleType.hover | NozzleType.rocket]))
        ], parent_region="Bianco Entrance"),

    SmsRegion("Bianco 4", BIANCO, Requirements(location="Bianco Hills - The Hillside Cave Secret"), [
        Shine("Red Coins of Windmill Village", 523003,
              Requirements([NozzleType.hover | NozzleType.rocket]))], [
        BlueCoin("Hillside Pokey", 523178, Requirements([NozzleType.hover])),
        BlueCoin("Bridge Underside", 523183)
    ], [
        NozzleBox("Rocket Box", 523872)
    ], parent_region="Bianco 3"),

    SmsRegion("Bianco 5", BIANCO, Requirements(location="Bianco Hills - Red Coins of Windmill Village"), [
        Shine("Petey Piranha Strikes Back", 523004,
              Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover])),], [
        BlueCoin("Wall Tower Pianta", 523177, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover])),
        BlueCoin("Platforms Cross", 523185, Requirements([NozzleType.hover | NozzleType.rocket]))
    ], parent_region="Bianco 4"),

    SmsRegion("Bianco 6", BIANCO, Requirements(location="Bianco Hills - Petey Piranha Strikes Back"), [
        Shine("The Secret of the Dirty Lake", 523005,
              Requirements([NozzleType.splasher])),
        Shine("Red Coins of the Dirty Lake", 523009,
              Requirements([NozzleType.hover]))], [
        BlueCoin("Petey Pillar", 523179, Requirements([NozzleType.hover])),
        BlueCoin("Underwater Left", 523181),
        BlueCoin("Blue Bird", 523182, Requirements([NozzleType.spray])),
        BlueCoin("Chuckster Momma", 523193)
    ], [
        NozzleBox("Turbo Box", 523873, Requirements([NozzleType.splasher]))
    ], parent_region="Bianco 5"),

    SmsRegion("Bianco 7", BIANCO, Requirements(location="Bianco Hills - The Secret of the Dirty Lake"), [
        Shine("Shadow Mario on the Loose", 523006,
              Requirements([NozzleType.spray]))], [
        BlueCoin("Towers House O", 523194, Requirements([NozzleType.splasher])),
        BlueCoin("Balcony House O", 523195, Requirements([NozzleType.splasher]))
    ], parent_region="Bianco 6"),

    SmsRegion("Bianco 8", BIANCO, Requirements(location="Bianco Hills - Shadow Mario on the Loose"), [
        Shine("The Red Coins of the Lake", 523007,
              Requirements([NozzleType.hover | NozzleType.rocket]))], [
        BlueCoin("Beehive", 523176, Requirements([NozzleType.yoshi])),
        BlueCoin("Butterfly", 523196, Requirements([NozzleType.yoshi]))
    ], parent_region="Bianco 7"),


    # Ricco Harbor
    SmsRegion("Ricco Entrance", RICCO, Requirements([NozzleType.splasher | NozzleType.yoshi], shines=3), [
        Shine("100 Coins", 523101, Requirements([NozzleType.hover]), hundred=True)],
        [
        BlueCoin("Tower Wall", 523221, Requirements([NozzleType.spray])),
        BlueCoin("Outer Ship M", 523222, Requirements([NozzleType.splasher])),
        BlueCoin("Spawn Building Top M", 523223, Requirements([NozzleType.splasher])),
        BlueCoin("Fruit Machine X", 523224, Requirements([NozzleType.spray])),
        BlueCoin("Rooftop M", 523226, Requirements([NozzleType.splasher])),
        BlueCoin("Far Ledge", 523228, Requirements([NozzleType.hover | NozzleType.spray, NozzleType.rocket])),
        BlueCoin("Short Beam", 523229, Requirements([NozzleType.hover])),
        BlueCoin("Tower Platform", 523230, Requirements([NozzleType.hover])),
        BlueCoin("Long Beam", 523231, Requirements([NozzleType.hover])),
        BlueCoin("Off Catwalk", 523232, Requirements([NozzleType.hover])),
        BlueCoin("Crane", 523234, Requirements([NozzleType.hover])),
        BlueCoin("Blooper Open Water", 523235, Requirements([NozzleType.rocket], location="Ricco Harbor - Gooper Blooper Breaks Out")),
        BlueCoin("Fountain", 523237),
        BlueCoin("Underwater", 523238),
        BlueCoin("Tower X", 523239, Requirements([NozzleType.spray])),
        BlueCoin("Fountain M", 523240, Requirements([NozzleType.splasher])),
        BlueCoin("Tower Crate", 523248),
        BlueCoin("Tower Rocket", 523233, Requirements([NozzleType.rocket]))
    ], ticketed="Ricco Harbor Ticket", parent_region=STATUE),

    SmsRegion("Ricco 1 Only", RICCO, Requirements(), [
        Shine("Gooper Blooper Breaks Out", 523010, Requirements([NozzleType.spray]))], [
        BlueCoin("Tower Ground M", 523227, Requirements([NozzleType.splasher])),
        BlueCoin("Spawn Building Side M", 523241, Requirements([NozzleType.splasher])),
        BlueCoin("Inner Ship M", 523246, Requirements([NozzleType.splasher])),
        BlueCoin("Yellow Submarine", 523249, Requirements([NozzleType.spray]))
    ], parent_region="Ricco Entrance"),

    SmsRegion("Ricco 2 Only", RICCO, Requirements(location="Ricco Harbor - Gooper Blooper Breaks Out"), [
        Shine("Blooper Surfing Safari", 523011),
        Shine("Blooper-Surfing Sequel", 523019)], [
        BlueCoin("Blooper Underground Entrance", 523236)
    ], parent_region="Ricco 1 Only"),

    SmsRegion("Ricco 3", RICCO, Requirements(location="Ricco Harbor - Blooper Surfing Safari"), [
        Shine("The Caged Shine Sprite", 523012, Requirements([NozzleType.hover | NozzleType.rocket]))], [
        BlueCoin("Mesh Wall Klamber", 523243),
        BlueCoin("Mesh Ceiling Klamber", 523244)
    ], [
        NozzleBox("Rocket Box", 523874, Requirements([NozzleType.hover]))
    ], parent_region="Ricco 2 Only"),

    SmsRegion("Ricco 4-7", RICCO, Requirements(location="Ricco Harbor - The Caged Shine Sprite"), [
        Shine("The Secret of Ricco Tower", 523013, Requirements([NozzleType.hover | NozzleType.rocket])),
        Shine("Gooper Blooper Returns", 523014, Requirements([NozzleType.spray])),
        Shine("Red Coins on the Water", 523015, Requirements()),
        Shine("Shadow Mario Revisited", 523016, Requirements([NozzleType.spray])),
        Shine("Red Coins in Ricco Tower", 523018, Requirements())], [
        BlueCoin("Caged Blooper", 523247, Requirements([NozzleType.hover | NozzleType.rocket]))
    ], parent_region="Ricco 3"),

    SmsRegion("Ricco 8", RICCO, Requirements(location="Ricco Harbor - Shadow Mario Revisited"), [
        Shine("Yoshi's Fruit Adventure", 523017, Requirements([NozzleType.yoshi]))], [
        BlueCoin("Butterflies", 523220, Requirements([NozzleType.yoshi])),
        BlueCoin("Wall Klamber", 523225, Requirements([NozzleType.yoshi])),
        BlueCoin("High Platform M", 523242, Requirements([NozzleType.yoshi | NozzleType.rocket, NozzleType.splasher])),
        BlueCoin("Fish Basket", 523245, Requirements([NozzleType.spray]))
    ], [
        NozzleBox("Turbo Box", 523875)
    ], parent_region="Ricco 4-7"),

    # Gelato Beach
    SmsRegion("Gelato Entrance", GELATO, Requirements([NozzleType.splasher | NozzleType.yoshi], shines=5), [
        Shine("Dune Bud Sand Castle Secret", 523020, Requirements([NozzleType.splasher])),
        Shine("Mirror Madness! Tilt, Slam, Bam!", 523021, Requirements([NozzleType.spray])),
        Shine("Wiggler Ahoy! Full Steam Ahead!", 523022, 
            Requirements([NozzleType.splasher], location="Gelato Beach - Mirror Madness! Tilt, Slam, Bam!")),
        Shine("Red Coins in the Sand Castle", 523028, Requirements([NozzleType.hover], location="Gelato Beach - Wiggler Ahoy! Full Steam Ahead!")),
        Shine("Sandy Shine Sprite", 523029, Requirements([NozzleType.splasher]))],
        [
        BlueCoin("Juicer", 523275),
        BlueCoin("Rocket M", 523276, Requirements([NozzleType.splasher])),
        BlueCoin("Spawn Triangle", 523277, Requirements([NozzleType.spray])),
        BlueCoin("Trees Triangle", 523278, Requirements([NozzleType.spray])),
        BlueCoin("Left Bird", 523280, Requirements([NozzleType.spray])),
        BlueCoin("Right Bird", 523281, Requirements([NozzleType.spray])),
        BlueCoin("Highest Rope", 523282, Requirements([NozzleType.hover | NozzleType.rocket])),
        BlueCoin("Pole", 523283, Requirements([NozzleType.hover | NozzleType.rocket])),
        BlueCoin("Deck", 523288),
        BlueCoin("Swing", 523289, Requirements([NozzleType.splasher])),
        BlueCoin("Big Tree", 523290),
        BlueCoin("Crevice", 523291),
        BlueCoin("Sand Cabana Roof", 523293),
        BlueCoin("Shack", 523294, Requirements([NozzleType.rocket]))
    ], ticketed="Gelato Beach Ticket"),

    SmsRegion("Gelato 1/2/4 Only", GELATO, Requirements(), [], [
        BlueCoin("Red Cataquack", 523270, Requirements([NozzleType.splasher]))
    ], parent_region="Gelato Entrance"),

    SmsRegion("Gelato Any Except 3", GELATO, Requirements(), [], [
        BlueCoin("Sand Shine at Sand Cabana", 523271, Requirements([NozzleType.splasher])),
        BlueCoin("Sand Shine at Surf Cabana", 523272, Requirements([NozzleType.splasher])),
        BlueCoin("Middle Sand Shine", 523274, Requirements([NozzleType.splasher])),
        BlueCoin("Close Underwater", 523284),
        BlueCoin("Far Underwater", 523285),
        BlueCoin("Blue Fish", 523286, Requirements([NozzleType.turbo])),
        BlueCoin("Red Fish", 523287, Requirements([NozzleType.turbo]))
    ], parent_region="Gelato Entrance"),

    SmsRegion("Gelato 2 and 4-8", GELATO, Requirements(location="Gelato Beach - Dune Bud Sand Castle Secret"), [], [
        BlueCoin("Big Sand Shine", 523292, Requirements([NozzleType.splasher]))
    ], parent_region="Gelato Entrance"),

    SmsRegion("Gelato 4 Only", GELATO, Requirements([NozzleType.hover],
            location="Gelato Beach - Wiggler Ahoy! Full Steam Ahead!"), [
        Shine("The Sand Bird is Born", 523023, Requirements([NozzleType.hover]))], [
        BlueCoin("Sand Bird A", 523296, Requirements([NozzleType.hover])),
        BlueCoin("Sand Bird B", 523297, Requirements([NozzleType.hover])),
        BlueCoin("Sand Bird C", 523298, Requirements([NozzleType.hover])),
        BlueCoin("Sand Bird D", 523299, Requirements([NozzleType.hover]))
    ], [
        NozzleBox("Turbo Box", 523877)
    ], parent_region="Gelato 2 and 4-8"),

    SmsRegion("Gelato 5-8", GELATO, Requirements(location="Gelato Beach - The Sand Bird is Born"), [
        Shine("Il Piantissimo's Sand Sprint", 523024, Requirements([NozzleType.hover | NozzleType.turbo])),
        Shine("Red Coins in the Coral Reef", 523025),
        Shine("It's Shadow Mario! After Him!", 523026, Requirements([NozzleType.spray])),
        Shine("The Watermelon Festival", 523027, Requirements([NozzleType.splasher | NozzleType.turbo])),
        Shine("100 Coins", 523102, Requirements([NozzleType.yoshi, NozzleType.spray | NozzleType.hover]), hundred=True)], [
        BlueCoin("Blue Cataquack", 523273, Requirements([NozzleType.spray]))
    ], [
        NozzleBox("Rocket Box", 523876, Requirements([NozzleType.splasher | NozzleType.rocket]))
    ], parent_region="Gelato Entrance"),

    SmsRegion("Gelato 6 Only", GELATO, Requirements(location="Gelato Beach - Il Piantissimo's Sand Sprint"),  [], [
        BlueCoin("Yellow Goo Dune Bud", 523279, Requirements([NozzleType.yoshi])),
        BlueCoin("Beehive", 523295, Requirements([NozzleType.yoshi]))
    ], parent_region="Gelato 5-8"),

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

    # Corona Mountain
    SmsRegion("Corona Mountain", "Corona Mountain", Requirements([NozzleType.spray, NozzleType.hover], corona=True),
              [], [
        BlueCoin("Platform", 523540, Requirements([NozzleType.hover])),
        BlueCoin("Back Right Lava", 523541, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Left Lava", 523542, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Front Lava", 523543, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Front Left Lava", 523544, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Front Right Lava", 523545, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Back Left Lava", 523546, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Far Back Left Lava", 523547, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Far Back Right Lava", 523548, Requirements([NozzleType.spray, NozzleType.hover])),
        BlueCoin("Right Lava", 523549, Requirements([NozzleType.spray, NozzleType.hover]))
    ],[
        NozzleBox("Rocket Box", 523886, Requirements([NozzleType.spray, NozzleType.hover]))
    ]),

    SmsRegion("Delfino Airstrip Revisit", "Delfino Airstrip Revisit", Requirements(corona=True), [
        Shine("Red Coin Waterworks", 523088, Requirements([NozzleType.turbo]))], [
        BlueCoin("Ice Cube", 523120, Requirements([NozzleType.turbo, NozzleType.spray]))
    ], parent_region=STATUE),

    # Blue Coin Trades
    SmsRegion("Boathouse Traders", "Boathouse Traders", Requirements(shines=3), [
        Shine("Shine 1", 523070, Requirements(blues=10)),
        Shine("Shine 2", 523071, Requirements(blues=20)),
        Shine("Shine 3", 523072, Requirements(blues=30)),
        Shine("Shine 4", 523073, Requirements(blues=40)),
        Shine("Shine 5", 523074, Requirements(blues=50)),
        Shine("Shine 6", 523075, Requirements(blues=60)),
        Shine("Shine 7", 523076, Requirements(blues=70)),
        Shine("Shine 8", 523077, Requirements(blues=80)),
        Shine("Shine 9", 523078, Requirements(blues=90)),
        Shine("Shine 10", 523079, Requirements(blues=100)),
        Shine("Shine 11", 523080, Requirements(blues=110)),
        Shine("Shine 12", 523081, Requirements(blues=120)),
        Shine("Shine 13", 523082, Requirements(blues=130)),
        Shine("Shine 14", 523083, Requirements(blues=140)),
        Shine("Shine 15", 523084, Requirements(blues=150)),
        Shine("Shine 16", 523085, Requirements(blues=160)),
        Shine("Shine 17", 523108, Requirements(blues=170)),
        Shine("Shine 18", 523109, Requirements(blues=180)),
        Shine("Shine 19", 523110, Requirements(blues=190)),
        Shine("Shine 20", 523111, Requirements(blues=200)),
        Shine("Shine 21", 523112, Requirements(blues=210)),
        Shine("Shine 22", 523113, Requirements(blues=220)),
        Shine("Shine 23", 523114, Requirements(blues=230)),
        Shine("Shine 24", 523115, Requirements(blues=240))
        ], [], trade=True)
]
