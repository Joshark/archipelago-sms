from dataclasses import dataclass


@dataclass
class NozzleItem:
    nozzle_name: str
    ap_item_id: int
    unlock_address: int
    unlock_value: str


NOZZLES: list[NozzleItem] = [
    NozzleItem("Spray Nozzle", 523000, 0, "none"),
    NozzleItem("Hover Nozzle", 523001, 0x80294438, "unknown"),
    NozzleItem("Rocket Nozzle", 523002, 0x8029443C, "38600001"),
    NozzleItem("Turbo Nozzle", 523003, 0x80294440, "4E800020"),
    NozzleItem("Yoshi", 53013, 0, "none")
]


def activate_nozzle(id):
    for nozzles in NOZZLES:
        if id == nozzles.ap_item_id:
            print("Activating " + nozzles.nozzle_name)
    return


def activate_yoshi():
    for nozzles in NOZZLES:
        if id == nozzles.ap_item_id:
            print("Activating " + nozzles.nozzle_name)
    return
