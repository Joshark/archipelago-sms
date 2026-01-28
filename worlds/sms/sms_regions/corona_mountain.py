from .sms_region_helper import *

CORONA_MOUNTAIN: SmsRegion = SmsRegion(SmsRegionName.CORONA,
    requirements=[Requirements(SPRAY_AND_HOVER, corona=True)],
    shines=[],
    blue_coins=[BlueCoin("Platform", [Requirements([[NozzleType.hover]])]),
        BlueCoin("Back Right Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Left Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Front Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Front Left Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Front Right Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Back Left Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Far Back Left Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Far Back Right Lava", [Requirements(SPRAY_AND_HOVER)]),
        BlueCoin("Right Lava", [Requirements(SPRAY_AND_HOVER)])],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(SPRAY_AND_HOVER)])],
    parent_region=SmsRegionName.PLAZA)