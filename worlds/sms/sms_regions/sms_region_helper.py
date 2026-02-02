from enum import StrEnum
from typing import Optional, NamedTuple, TYPE_CHECKING

from BaseClasses import Location, Region

if TYPE_CHECKING:
    from worlds.sms import SmsWorld


class SmsLocation(Location):
    name: str
    address: Optional[int]
    region: "SmsRegion"

    def __init__(self, world: "SmsWorld", name: str, sms_region: Region):
        self.address = world.location_name_to_id[name]
        super(SmsLocation, self).__init__(world.player, name, address=self.address, parent=sms_region)


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
    GELATO_ENTRANCE = "Gelato Beach"
    GELATO_ONE = "Gelato Beach 1"
    GELATO_ONE_TWO_FOUR = "Gelato 1/2/4 Only"
    GELATO_NOT_THREE = "Gelato Any Except 3"
    GELATO_TWO_FOUR_THRU_EIGHT = "Gelato 2 and 4-8"
    GELATO_FOUR_ONLY = "Gelato 4 Only"
    GELATO_FIVE_EIGHT = "Gelato 5-8"
    GELATO_SIX = "Gelato 6 Only"
    PINNA_ENTRANCE = "Pinna Park"
    PINNA_ONE = "Pinna Park 1"
    PINNA_ONE_THREE_FIVE_EIGHT = "Pinna 1, 3 and 5-8"
    PINNA_TWO = "Pinna 2 Only"
    PINNA_FIVE_EIGHT = "Pinna 5-8"
    PINNA_SIX = "Pinna 6 Only"
    SIRENA = "Sirena Beach"
    NOKI_ENTRANCE = "Noki Bay"
    NOKI_ALL = "Noki All Except 3"
    NOKI_TWO_FOUR_EIGHT = "Noki 2 and 4-8"
    NOKI_FOUR_EIGHT = "Noki 4 and 8"
    NOKI_SIX_EIGHT = "Noki 6-8"
    SIRENA_ENTRANCE = "Sirena Entrance"
    SIRENA_ONE_SIX = "Sirena 1 and 6"
    SIRENA_TWO_EIGHT = "Sirena 2-8"
    SIRENA_THREE_EIGHT = "Sirena 3-8"
    SIRENA_FOUR_FIVE = "Sirena 4-5"
    SIRENA_FOUR_EIGHT = "Sirena 4-8"
    SIRENA_FIVE_ONLY = "Sirena 5 Only"
    SIRENA_SIX_ONLY = "Sirena 6 Only"
    SIRENA_SEVEN_EIGHT = "Sirena 7-8"
    PIANTA_ENTRANCE = "Pianta Village"
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
    requirements: Optional[list[Requirements]] | None = None
    hard: Optional[list[Requirements]] | None = None
    advanced: Optional[list[Requirements]] | None = None
    tears: Optional[list[Requirements]] | None = None
    hundred: bool = False # 100 coin Shines


class BlueCoin(NamedTuple):
    name: str
    requirements: Optional[list[Requirements]] | None = None
    hard: Optional[list[Requirements]] | None = None
    advanced: Optional[list[Requirements]] | None = None
    tears: Optional[list[Requirements]] | None = None


class OneUp(NamedTuple):
    name: str
    requirements: Requirements = Requirements()


# Yes, I'm going to include Shadow Mario Plaza chases as NozzleBox Locations
class NozzleBox(NamedTuple):
    name: str
    requirements: Optional[list[Requirements]] | None = None
    hard: Optional[list[Requirements]] | None = None
    advanced: Optional[list[Requirements]] | None = None
    tears: Optional[list[Requirements]] | None = None


class SmsRegion(NamedTuple):
    name: str
    requirements: Optional[list[Requirements]] | None = None
    shines: Optional[list[Shine]] | None = []
    blue_coins: Optional[list[BlueCoin]] | None = []
    nozzle_boxes: Optional[list[NozzleBox]] | None = []
    ticketed: str = ""
    trade: bool = False
    parent_region: str = None


# Common combinations of Nozzle Types
ANY_SPLASHER: list[list[str]] = [
    [NozzleType.spray],
    [NozzleType.hover],
    [NozzleType.yoshi]
]
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
YOSHI_AND_HOVER: list[list[str]] = [
    [NozzleType.yoshi, NozzleType.hover]
]
SPRAY_AND_HOVER: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover]
]
SPRAY_OR_HOVER: list[list[str]] = [
    [NozzleType.spray],
    [NozzleType.rocket]
]
SPRAY_AND_ROCKET_OR_HOVER: list[list[str]] = [
    [NozzleType.spray, NozzleType.rocket],
    [NozzleType.hover]
]
TURBO_OR_HOVER: list[list[str]] = [
    [NozzleType.hover],
    [NozzleType.turbo]
]
TURBO_OR_SPLASHER: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover, NozzleType.yoshi],
    [NozzleType.turbo]
]
ROCKET_OR_SPLASHER: list[list[str]] = [
    [NozzleType.spray, NozzleType.hover, NozzleType.yoshi],
    [NozzleType.rocket]
]
YOSHI_AND_SPRAY_OR_YOSHI_AND_HOVER: list[list[str]] = [
    [NozzleType.yoshi, NozzleType.spray],
    [NozzleType.yoshi, NozzleType.hover]
]