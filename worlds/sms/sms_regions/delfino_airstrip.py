from .sms_region_helper import *

# Delfino Airstrip
DELFINO_AIRSTRIP: SmsRegion = SmsRegion(SmsRegionName.AIRSTRIP,
    shines=[Shine("Delfino Airstrip Dilemma", [Requirements(ANY_SPLASHER, skip_forward=False)],
        in_game_bit=86),
        Shine("Red Coin Waterworks", [Requirements([[NozzleType.turbo]], corona=True)],
        in_game_bit=88)],
    blue_coins=[BlueCoin("Ice Cube", [Requirements(TURSPRAY, corona=True)], in_game_bit=120)],
    parent_region="Menu"
)