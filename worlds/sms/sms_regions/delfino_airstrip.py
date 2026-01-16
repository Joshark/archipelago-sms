from .sms_region_helper import *

# Delfino Airstrip
DELFINO_AIRSTRIP: SmsRegion = SmsRegion(SmsRegionName.AIRSTRIP,
    shines=[Shine("Delfino Airstrip Dilemma", 523086, [Requirements(ANY_SPLASHER, skip_forward=False)])],
    # TODO Move Revisited to here
)