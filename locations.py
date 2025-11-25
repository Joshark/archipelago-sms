from BaseClasses import Location
from .static_logic import ALL_REGIONS
from .options import BlueCoinSanity


class SmsLocation(Location):
    game: str = "Super Mario Sunshine"


ALL_LOCATIONS_TABLE: dict[str, int] = {}

for region in ALL_REGIONS:
    for shine in region.shines:
        ALL_LOCATIONS_TABLE[f"{region.display} - {shine.name}"] = shine.id
    for blue_coin in region.blue_coins:
        ALL_LOCATIONS_TABLE[f"{region.display} - {blue_coin.name} Blue Coin"] = blue_coin.id
    for nozzle_box in region.nozzle_boxes:
        ALL_LOCATIONS_TABLE[f"{region.display} - {nozzle_box.name}"] = nozzle_box.id
    # for one_up in region.one_ups:
    #     ALL_LOCATIONS_TABLE[f"{region.display} - {one_up.name} One Up"] = one_up.id
