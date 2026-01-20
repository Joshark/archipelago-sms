from .sms_region_helper import *

# Delfino Airstrip
# TODO Reminder that corona=True means that game must be able to reach Corona mountain
DELFINO_AIRSTRIP: SmsRegion = SmsRegion(SmsRegionName.AIRSTRIP,
    shines=[Shine("Delfino Airstrip Dilemma", 523086, [Requirements(ANY_SPLASHER, skip_forward=False)]),
        Shine("Red Coin Waterworks", 523088, [Requirements([[NozzleType.turbo]], corona=True)])],
    blue_coins=[BlueCoin("Ice Cube", 523120, [Requirements(TURSPRAY, corona=True)])],
    parent_region="Menu"
)