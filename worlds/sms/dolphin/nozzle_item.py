nozzle_list = []


class NozzleItem:
    ap_item_id = 0
    nozzle_name = ""
    unlock_address = 0x0
    unlock_value = ""

    def __init__(self, name, ap_id, address, unlocker):
        self.nozzle_name = name
        self.ap_item_id = ap_id
        self.unlock_address = address
        self.unlock_value = unlocker


def add_nozzles():
    hover = NozzleItem.__new__(NozzleItem)
    hover.__init__("Hover Nozzle", 523001, 0x80294438, "unknown")

    rocket = NozzleItem.__new__(NozzleItem)
    rocket.__init__("Rocket Nozzle", 523002, 0x8029443C, "38600001")

    turbo = NozzleItem.__new__(NozzleItem)
    turbo.__init__("Turbo Nozzle", 523003, 0x80294440, "4E800020")

    nozzle_list.append(hover)
    nozzle_list.append(rocket)
    nozzle_list.append(turbo)
