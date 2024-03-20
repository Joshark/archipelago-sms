from BaseClasses import Location
from .static_logic import ALL_REGIONS
from .options import BlueCoinSanity, BlueCoinMaximum


class SmsLocation(Location):
    game: str = "Super Mario Sunshine"


ALL_LOCATIONS_TABLE: dict[str, int] = {}

for region in ALL_REGIONS:
    if region.trade:
        if BlueCoinSanity.option_no_blue_coins:
            continue
        elif region.requirements.blues > BlueCoinMaximum.value:
            continue

    for shine in region.shines:
        ALL_LOCATIONS_TABLE[f"{region.name} - {shine.name}"] = shine.id
    if BlueCoinSanity.option_full_shuffle:
        for blue_coin in region.blue_coins:
            ALL_LOCATIONS_TABLE[f"{region.name} - {blue_coin.name} Blue Coin"] = blue_coin.id
