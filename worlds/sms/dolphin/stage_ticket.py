from typing import NamedTuple


class Ticket(NamedTuple):
    item_name: str
    item_id: int
    bit_position: int
    address: int = 0x805789f8
    active: bool = False


TICKETS: list[Ticket] = [
    Ticket("Bianco Hills Ticket", 523005, 5),
    Ticket("Ricco Harbor Ticket", 523006, 6),
    Ticket("Gelato Beach Ticket", 523007, 7),
    Ticket("Pinna Park Ticket", 523008, 1, 0x805789f8),
    #Ticket("Noki Bay Ticket", 523009, 0, 0x805789f8),
    Ticket("Sirena Beach Ticket", 523010, 3, 0x805789f8)
]
