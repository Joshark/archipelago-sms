from typing import NamedTuple


class NozzleItem(NamedTuple):
    nozzle_name: str
    ap_item_id: int
    unlock_address: int
    unlock_value: str


NOZZLES: list[NozzleItem] = [
    NozzleItem("Hover Nozzle", 523001, 0x80294438, "unknown"),
    NozzleItem("Rocket Nozzle", 523002, 0x8029443C, "38600001"),
    NozzleItem("Turbo Nozzle", 523003, 0x80294440, "4E800020")
]
