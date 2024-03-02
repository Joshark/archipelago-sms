from enum import Flag, auto
from typing import Optional, NamedTuple


class NozzleType(Flag):
    spray = auto()
    hover = auto()
    rocket = auto()
    turbo = auto()


class Requirements(NamedTuple):
    nozzles: list[NozzleType] = []  # conjunctive normal form
    shines: Optional[int] = None  # number of shine sprites needed
    yoshi: bool = False  # is yoshi needed
    corona: bool = False  # is corona access needed (configurable)


class Shine(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()
    hundred: bool = False


class BlueCoin(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()


class SmsRegion(NamedTuple):
    name: str
    requirements: Requirements
    shines: list[Shine]
    ticketed: bool = False


ALL_REGIONS: list[SmsRegion] = [
    SmsRegion("Delfino Airstrip", Requirements(), [
        Shine("Delfino Airstrip Dilemma", 523086, Requirements([NozzleType.spray])),
        Shine("Red Coin Waterworks", 523087, Requirements([NozzleType.turbo], corona=True))]),
    SmsRegion("Delfino Plaza", Requirements([NozzleType.spray]), [
        Shine("Shine Sprite in the Sand", 523117, Requirements([NozzleType.hover])),
        Shine("Boxing Clever 1", 523094),
        Shine("Boxing Clever 2", 523095),
        Shine("Clean the West Bell", 523096, Requirements([NozzleType.hover | NozzleType.rocket], shines=10)),
        Shine("Chuckster", 523098),
        Shine("Super Slide", 523090, Requirements([NozzleType.hover | NozzleType.rocket])),
        Shine("The Gold Bird", 523118, Requirements([NozzleType.spray])),
        Shine("Turbo Dash!", 523116, Requirements([NozzleType.turbo], shines=10)),
        Shine("Lighthouse Roof", 523093, Requirements([NozzleType.rocket], shines=10)),
        Shine("Clean the East Bell", 523097, Requirements([NozzleType.rocket, NozzleType.spray], shines=10)),
        Shine("Shine Gate", 523099, Requirements([NozzleType.rocket], shines=10)),
        Shine("Pachinko Game", 523089, Requirements([NozzleType.hover | NozzleType.rocket], shines=10)),
        Shine("Lily Pad Ride", 523091, Requirements([NozzleType.hover, NozzleType.spray], yoshi=True)),
        Shine("Turbo Track", 523088, Requirements([NozzleType.turbo], shines=10)),
        Shine("Red Coin Field", 523092, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover], shines=10)),
        Shine("100 Coins", 523107, Requirements([NozzleType.hover | NozzleType.rocket]), hundred=True)
    ]),
    SmsRegion("Bianco Hills", Requirements([NozzleType.spray]), [
        Shine("Road to the Big Windmill", 523000, Requirements([NozzleType.spray])),
        Shine("Down with Petey Piranha!", 523001,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("The Hillside Cave Secret", 523002,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("Red Coins of Windmill Village", 52303,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("Petey Piranha Strikes Back", 523004,
              Requirements([NozzleType.spray, NozzleType.rocket])),
        Shine("The Secret of the Dirty Lake", 523005,
              Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket])),
        Shine("Shadow Mario on the Loose", 523006,
              Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket])),
        Shine("The Red Coins of the Lake", 523007,
              Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket])),
        Shine("Red Coins of the Hillside Cave", 523008,
              Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket])),
        Shine("Red Coins of the Dirty Lake", 523009,
              Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket])),
        Shine("100 Coins", 523100, Requirements([NozzleType.spray, NozzleType.hover]), hundred=True)
    ], ticketed=True),
    SmsRegion("Ricco Harbor", Requirements([NozzleType.spray], shines=3), [
        Shine("Gooper Blooper Breaks Out", 523010, Requirements([NozzleType.hover])),
        Shine("Blooper Surfing Safari", 523011, Requirements([NozzleType.hover])),
        Shine("The Caged Shine Sprite", 523012, Requirements([NozzleType.hover])),
        Shine("The Secret of Ricco Tower", 523013, Requirements([NozzleType.hover, NozzleType.rocket])),
        Shine("Gooper Blooper Returns", 523014, Requirements([NozzleType.hover, NozzleType.rocket])),
        Shine("Red Coins on the Water", 523015, Requirements([NozzleType.hover, NozzleType.rocket])),
        Shine("Shadow Mario Revisited", 523016, Requirements([NozzleType.hover, NozzleType.rocket])),
        Shine("Yoshi's Fruit Adventure", 523017, Requirements([NozzleType.hover, NozzleType.rocket], yoshi=True)),
        Shine("Red Coins in Ricco Tower", 523018, Requirements([NozzleType.hover, NozzleType.rocket])),
        Shine("Blooper-Surfing Sequel", 523019, Requirements([NozzleType.hover])),
        Shine("100 Coins", 523101, Requirements([NozzleType.hover]), hundred=True)
    ], ticketed=True),
    SmsRegion("Gelato Beach", Requirements([NozzleType.spray], shines=5), [
        Shine("Dune Bud Sand Castle Secret", 523020, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("Mirror Madness! Tilt, Slam, Bam!", 523021, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Wiggler Ahoy! Full Steam Ahead!", 523022, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Sand Bird is Born", 523023, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Il Piantissimo's Sand Sprint", 523024, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coins in the Coral Reef", 523025, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("It's Shadow Mario! After Him!", 523026, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Watermelon Festival", 523027, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coins in the Sand Castle", 523028, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("Sandy Shine Sprite", 523029, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("100 Coins", 523102, Requirements([NozzleType.spray | NozzleType.hover]), hundred=True)
    ], ticketed=True),
    SmsRegion("Pinna Park", Requirements(shines=10), [
        Shine("Mecha-Bowser Appears!", 523030, Requirements([NozzleType.spray])),
        Shine("The Beach Cannon's Secret", 523031, Requirements([NozzleType.spray])),
        Shine("Red Coins of the Pirate Ships", 523032,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("The Wilted Sunflowers", 523033, Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("The Runaway Ferris Wheel", 523034,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket])),
        Shine("The Yoshi-Go-Round's Secret", 523035,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket], yoshi=True)),
        Shine("Shadow Mario in the Park", 523036,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket], yoshi=True)),
        Shine("Roller Coaster Balloons", 523037,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket], yoshi=True)),
        Shine("Red Coins in the Cannon", 523038, Requirements([NozzleType.spray])),
        Shine("Red Coins in the Yoshi-Go-Round", 523039,
              Requirements([NozzleType.spray, NozzleType.hover | NozzleType.rocket], yoshi=True)),
        Shine("100 Coins", 523103, Requirements([NozzleType.spray]), hundred=True)
    ], ticketed=True),
    SmsRegion("Sirena Beach", Requirements(yoshi=True), [
        Shine("The Manta Storm", 523040, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("The Hotel Lobby's Secret", 523041, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("Mysterious Hotel Delfino", 523042, Requirements([NozzleType.spray | NozzleType.hover], yoshi=True)),
        Shine("The Secret of Casino Delfino", 523043, Requirements([NozzleType.spray], yoshi=True)),
        Shine("King Boo Down Below", 523044, Requirements([NozzleType.spray], yoshi=True)),
        Shine("Scrubbing Sirena Beach", 523045, Requirements([NozzleType.spray], yoshi=True)),
        Shine("Shadow Mario Checks In", 523046, Requirements([NozzleType.spray], yoshi=True)),
        Shine("Red Coins in the Hotel", 523047, Requirements([NozzleType.spray], yoshi=True)),
        Shine("Red Coins in Boo's Big Mouth", 523048, Requirements([NozzleType.spray | NozzleType.hover])),
        Shine("Red Coin Winnings in the Casino", 523049, Requirements([NozzleType.spray], yoshi=True)),
        Shine("100 Coins", 523104, Requirements([NozzleType.spray], yoshi=True), hundred=True)
    ], ticketed=True),
    SmsRegion("Noki Bay", Requirements(shines=20), [
        Shine("Uncork the Waterfall", 523050, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Boss of Tricky Ruins", 523051, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Red Coins in a Bottle", 523052, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Eely-Mouth's Dentist", 523053, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Il Piantissimo's Surf Swim", 523054, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Shell's Secret", 523055, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("Hold It, Shadow Mario!", 523056, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("The Red Coin Fish", 523057, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("A Golden Bird", 523058, Requirements([NozzleType.hover, NozzleType.spray])),
        Shine("Red Coins on the Half Shell", 523059, Requirements([NozzleType.spray, NozzleType.hover])),
        Shine("100 Coins", 523105, Requirements([NozzleType.hover]), hundred=True)
    ], ticketed=False),
    SmsRegion("Pianta Village", Requirements([NozzleType.rocket], shines=10), [
        Shine("Chain Chomplets Unchained", 523060, Requirements([NozzleType.spray])),
        Shine("Il Piantissimo's Crazy Climb", 523061, Requirements([NozzleType.spray])),
        Shine("The Goopy Inferno", 523062, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover])),
        Shine("Chain Chomp's Bath", 523063, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover])),
        Shine("Secret of the Village Underside", 523064,
              Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover], yoshi=True)),
        Shine("Piantas in Need", 523065, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover], yoshi=True)),
        Shine("Shadow Mario Runs Wild", 523066, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover], yoshi=True)),
        Shine("Fluff Festival Coin Hunt", 523067,
              Requirements([NozzleType.spray, NozzleType.rocket], yoshi=True)),
        Shine("Red Coin Chucksters", 523068, Requirements([NozzleType.spray, NozzleType.rocket | NozzleType.hover], yoshi=True)),
        Shine("Soak the Sun", 523069, Requirements([NozzleType.spray, NozzleType.hover], yoshi=True)),
        Shine("100 Coins", 523106, Requirements([NozzleType.spray, NozzleType.hover], yoshi=True), hundred=True)
    ], ticketed=False),
    SmsRegion("Corona Mountain", Requirements([NozzleType.spray, NozzleType.hover, NozzleType.rocket], corona=True), []),
]
