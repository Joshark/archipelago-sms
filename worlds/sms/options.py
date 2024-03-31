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
    CURRENTLY HARDCODED OFF due to the coin Gecko code issue."""
    display_name = "Enable 100 Coin Shines"


class CoronaMountainShines(Range):
    """How many Shine Sprites are required to access Corona Mountain and the Delfino Airstrip revisit.
    If less than this number of Shines exist in the pool, it will be adjusted to the total Shine count."""
    display_name = "Corona Mountain Shines"
    range_start = 0
    range_end = 360
    default = 50


class BlueCoinSanity(Choice):
    """Full shuffle: adds Blue Coins to the pool and makes Blue Coins locations."""
    display_name = "Blue Coinsanity"
    option_no_blue_coins = 0
    option_full_shuffle = 1
    option_trade_shines_only = 2
    default = 0


class BlueCoinMaximum(Range):
    """How many Blue Coins to include in the pool if Blue Coinsanity is on. Does nothing if Blue Coinsanity is off.
    Corresponding trade shines will be removed from locations.
    Removed Blue Coins will be replaced by extra Shine Sprites."""
    display_name = "Blue Coin Maximum"
    range_start = 0
    range_end = 240
    default = 240


class TradeShineMaximum(Range):
    """The number of Shines from the boathouse trades that will be shuffled. If the Blue Coin Maximum is not enough
    to obtain this amount, it will decrease automatically.
    Keep in mind that if this value is too high, there is a chance you will have to nearly 100% the game."""
    range_start = 0
    range_end = 24
    default = 12

@dataclass
class SmsOptions(PerGameCommonOptions):
    level_access: LevelAccess
    enable_coin_shines: EnableCoinShines
    corona_mountain_shines: CoronaMountainShines
    blue_coin_sanity: BlueCoinSanity
    blue_coin_maximum: BlueCoinMaximum
    trade_shine_maximum: TradeShineMaximum
