from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle


class LevelAccess(Choice):
    """If on "vanilla", the main levels are accessed in the way they are in the base game (e.g. Ricco Harbor is accessible after collecting 3 Shine Sprites).
    If on "tickets", each level has a ticket item that must be acquired to access the level.
    CURRENTLY HARDCODED OFF."""
    display_name = "Level Access"
    option_vanilla = 0
#    option_tickets = 1


class EnableCoinShines(Toggle):
    """Turn off to ignore the 100 coin Shine Sprites, which removes 8 Shine Sprites from the pool.
    You can still collect them, but they don't do anything.
    CURRENTLY HARDCODED OFF."""
    display_name = "Enable 100 Coin Shines"


class CoronaMountainShines(Range):
    """How many Shine Sprites are required to access Corona Mountain and the Delfino Airstrip revisit.
    Must be at least one less than the total number of shines, due to the Delfino Airstrip red coins shine."""
    display_name = "Corona Mountain Shines"
    range_start = 0
    range_end = 83
    default = 50


class BlueCoinSanity(DefaultOnToggle):
    """Full shuffle: adds Blue Coins to the pool and makes Blue Coins locations."""
    display_name = "Blue Coinsanity"


@dataclass
class SmsOptions(PerGameCommonOptions):
    level_access: LevelAccess
    enable_coin_shines: EnableCoinShines
    corona_mountain_shines: CoronaMountainShines
    blue_coin_sanity: BlueCoinSanity
