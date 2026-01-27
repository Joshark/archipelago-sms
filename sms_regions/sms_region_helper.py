from enum import StrEnum
from typing import Optional, NamedTuple

from BaseClasses import Location, Region


class SmsLocation(Location):
    name: str
    address: Optional[int]
    region: "SmsRegion"

    def __init__(self, player: int, name: str, sms_region: Region):
        self.address = len(sms_region.locations) + 1
        super(SmsLocation, self).__init__(player, name, address=self.address, parent=sms_region)


class SmsRegionName(StrEnum):
    AIRSTRIP = "Delfino Airstrip"
    PLAZA = "Delfino Plaza"
    BOATHOUSE = "Boathouse Traders"
    BIANCO_ENTRANCE = "Bianco Hills"
    BIANCO_ONE = "Bianco Hills 1"
    BIANCO_THREE = "Bianco Hills 3"
    BIANCO_FOUR = "Bianco Hills 4"
    BIANCO_FIVE = "Bianco Hills 5"
    BIANCO_SIX = "Bianco Hills 6"
    BIANCO_SEVEN = "Bianco Hills 7"
    BIANCO_EIGHT = "Bianco Hills 8"
    RICCO_ENTRANCE = "Ricco Harbor"
    RICCO_ONE = "Ricco Harbor 1"
    RICCO_TWO = "Ricco Harbor 2"
    RICCO_THREE = "Ricco Harbor 3"
    RICCO_FOUR_SEVEN = "Ricco Harbor 4-7"
    RICCO_EIGHT = "Ricco Harbor 8"
    GELATO = "Gelato Beach"
    PINNA = "Pinna Park"
    SIRENA = "Sirena Beach"
    NOKI = "Noki Bay"
    PIANTA = "Pianta Village"
    CORONA = "Corona Mountain"


class NozzleType(StrEnum):
    spray = "Spray Nozzle"
    hover = "Hover Nozzle"
    rocket = "Rocket Nozzle"
    turbo = "Turbo Nozzle"
    yoshi = "Yoshi"


class Requirements(NamedTuple):
    nozzles: Optional[list[list[str]]] = None  # conjunctive normal form
    shines: Optional[int] = None  # number of shine sprites needed
    blue_coins: Optional[int] = None
    location: Optional[str] = None
    corona: bool = False  # is corona access needed (configurable)
    skip_forward: bool = None # Only in logic if tickets / fluddless are true


class Shine(NamedTuple):
    name: str
    requirements: list[Optional[Requirements]] = None
    hard: list[Optional[Requirements]] = None
    advanced: list[Optional[Requirements]] = None
    tears: list[Optional[Requirements]] = None
    hundred: bool = False # 100 coin Shines


class BlueCoin(NamedTuple):
    name: str
    requirements: list[Optional[Requirements]] = None
    hard: list[Optional[Requirements]] = None
    advanced: list[Optional[Requirements]] = None
    tears: list[Optional[Requirements]] = None


class OneUp(NamedTuple):
    name: str
    requirements: Requirements = Requirements()


# Yes, I'm going to include Shadow Mario Plaza chases as NozzleBox Locations
class NozzleBox(NamedTuple):
    name: str
    requirements: list[Optional[Requirements]] = None
    hard: list[Optional[Requirements]] = None
    advanced: list[Optional[Requirements]] = None
    tears: list[Optional[Requirements]] = None


class SmsRegion(NamedTuple):
    name: str
    requirements: list[Optional[Requirements]] = None
    shines: Optional[list[Shine]] = []
    blue_coins: Optional[list[BlueCoin]] = []
    nozzle_boxes: Optional[list[NozzleBox]] = []
    ticketed: str = ""
    trade: bool = False
    parent_region: str = None


# Common combinations of Nozzle Types
ANY_SPLASHER: list[list[str]] = [
    [NozzleType.spray],
    [NozzleType.hover],
    [NozzleType.yoshi]]
SPROVER_OR_YOSHI: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover],
    [NozzleType.yoshi]
]
HOVORSHI: list[list[str]] = [
    [NozzleType.hover],
    [NozzleType.yoshi]
]
ROCKET_OR_HOVER_OR_YOSHI: list[list[str]] = [
    [NozzleType.hover],
    [NozzleType.rocket],
    [NozzleType.yoshi],
]
ROCKET_AND_SPLASHER: list[list[str]] = [
    [NozzleType.rocket, NozzleType.spray],
    [NozzleType.rocket, NozzleType.hover],
    [NozzleType.rocket, NozzleType.yoshi]
]
ALL_SPLASHER: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover, NozzleType.yoshi]
]
ROCKET_OR_HOVER_AND_SPRAY: list[list[str]] = [
    [NozzleType.rocket, NozzleType.spray],
    [NozzleType.hover, NozzleType.spray],
]
ROCKET_OR_HOVER: list[list[str]] = [
    [NozzleType.hover],
    [NozzleType.rocket]
]
SPRAY_OR_YOSHI: list[list[str]] = [
    [NozzleType.spray],
    [NozzleType.yoshi]
]
TURSPRAY: list[list[str]] = [
    [NozzleType.spray, NozzleType.turbo]
]
SPRAY_AND_HOVER: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover]
]
SPRAY_AND_ROCKET_OR_HOVER: list[list[str]] = [
    [NozzleType.spray, NozzleType.rocket],
    [NozzleType.hover]
]