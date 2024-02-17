from dataclasses import dataclass
import worlds.sms.dolphin.item_receiver as item_receiver


@dataclass
class Ticket:
    item_name: str
    item_id: int
    bit_position: int
    address: int = 0x805789f8
    active: bool = False


TICKETS: list[Ticket] = [
    Ticket("Bianco Hills Ticket", 523005, 5, 0x805789f8),
    Ticket("Ricco Harbor Ticket", 523006, 6, 0x805789f8),
    Ticket("Gelato Beach Ticket", 523007, 7, 0x805789f8),
    Ticket("Pinna Park Ticket", 523008, 1, 0x805789f9),
    Ticket("Noki Bay Ticket", 523009, 3, 0x805789fd),
    Ticket("Sirena Beach Ticket", 523010, 3, 0x805789f9)
]


def activate_ticket(id: int):
    for tickets in TICKETS:
        if id == tickets.item_id:
            print("Activating " + tickets.item_name)
            tickets.active = True
            handle_ticket(tickets)


def handle_ticket(tick: Ticket):
    if not tick.active:
        return
    if tick.item_name == "Noki Bay Ticket":
        item_receiver.special_noki_handling()
    item_receiver.open_stage(tick)
    return


def refresh_all_tickets():
    for tickets in TICKETS:
        handle_ticket(tickets)
