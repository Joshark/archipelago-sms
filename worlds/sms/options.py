from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle


class LevelAccess(Choice):
    """If on "vanilla", the main levels are accessed in the way they are in the base game (e.g. Ricco Harbor is accessible after collecting 3 Shine Sprites).
    If on "tickets", each level has a ticket item that must be acquired to access the level."""
    display_name = "Level Access"
    option_vanilla = 0
#    option_tickets = 1


class EnableCoinShines(DefaultOnToggle):
    """Turn off to ignore the 100 coin Shine Sprites, which removes 8 Shine Sprites from the pool.
    You can still collect them, but they don't do anything."""
    display_name = "Enable 100 Coin Shines"


class CoronaMountainShines(Range):
    """How many Shine Sprites are required to access Corona Mountain and the Delfino Airstrip revisit.
    Must be at least one less than the total number of shines, due to the Delfino Airstrip red coins shine."""
    display_name = "Corona Mountain Shines"
    range_start = 0
    range_end = 83
    default = 50


class AmountOfShines(Range):
    """How many Shine Sprites exist."""
    display_name = "Amount of Shines"
    range_start = 0
    range_end = 84
    default = 84


class BlueCoinSanity(Choice):
    """Full shuffle: adds Blue Coins to the pool and makes Blue Coins locations."""
    display_name = "Blue Coinsanity"
    option_no_blue_coins = 0
    option_full_shuffle = 1
#    option_trade_shines_only = 2
    default = 0


class BlueCoinMaximum(Range):
    """How many Blue coins to include in the pool if Blue Coinsanity is on."""
    display_name = "Blue Coin Maximum"
    range_start = 0
    range_end = 240
    default = 240


@dataclass
class SmsOptions(PerGameCommonOptions):
    level_access: LevelAccess
    enable_coin_shines: EnableCoinShines
    corona_mountain_shines: CoronaMountainShines
    amount_of_shines: AmountOfShines
    blue_coin_sanity: BlueCoinSanity
    blue_coin_maximum: BlueCoinMaximum
