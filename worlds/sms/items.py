from BaseClasses import Item


class SmsItem(Item):
    game: str = "Super Mario Sunshine"


REGULAR_PROGRESSION_ITEMS: dict[str, int] = {
    "Spray Nozzle": 523000,
    "Hover Nozzle": 523001,
    "Rocket Nozzle": 523002,
    "Turbo Nozzle": 523003,
    "Yoshi": 523013,
}

TICKET_ITEMS: dict[str, int] = {
    "Bianco Hills Ticket": 523005,
    "Ricco Harbor Ticket": 523006,
    "Gelato Beach Ticket": 523007,
    "Pinna Park Ticket": 523008,
    "Noki Bay Ticket": 523009,
    "Sirena Beach Ticket": 523010,
    "Pianta Village Ticket": 523011
}

ALL_PROGRESSION_ITEMS: dict[str, int] = {
    "Shine Sprite": 523004,
    "Blue Coin": 523014,
    **REGULAR_PROGRESSION_ITEMS,
    **TICKET_ITEMS,
}

JUNK_ITEMS: dict[str, int] = {
    "1-UP": 523140,
}


ALL_ITEMS_TABLE: dict[str, int] = {
    **ALL_PROGRESSION_ITEMS,
    **JUNK_ITEMS,
}
