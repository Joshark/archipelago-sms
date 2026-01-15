from enum import StrEnum
from typing import Optional, NamedTuple

class SmsRegionName(StrEnum):
    AIRSTRIP = "Delfino Airstrip"
    PLAZA = "Delfino Plaza"
    BIANCO = "Bianco Hills"
    RICCO = "Ricco Harbor"
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
    id: int
    requirements: list[Optional[Requirements]] = None
    hard: list[Optional[Requirements]] = None
    advanced: list[Optional[Requirements]] = None
    tears: list[Optional[Requirements]] = None
    hundred: bool = False # 100 coin Shines


class BlueCoin(NamedTuple):
    name: str
    id: int
    requirements: list[Optional[Requirements]] = None
    hard: list[Optional[Requirements]] = None
    advanced: list[Optional[Requirements]] = None
    tears: list[Optional[Requirements]] = None


class OneUp(NamedTuple):
    name: str
    id: int
    requirements: Requirements = Requirements()


# Yes, I'm going to include Shadow Mario Plaza chases as NozzleBox Locations
class NozzleBox(NamedTuple):
    name: str
    id: int
    requirements: list[Optional[Requirements]] = None


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
HOVER_AND_SPROSHI: list[list[str]] = [
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