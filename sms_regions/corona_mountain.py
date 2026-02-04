from .sms_region_helper import *

CORONA_MOUNTAIN: SmsRegion = SmsRegion(SmsRegionName.CORONA,
    requirements=[Requirements(SPRAY_AND_HOVER, corona=True)],
    blue_coins=[BlueCoin("Platform", [Requirements([[NozzleType.hover]], corona=True)]),
        BlueCoin("Back Right Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Left Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Front Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Front Left Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Front Right Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Back Left Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Far Back Left Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Far Back Right Lava", [Requirements(SPRAY_AND_HOVER, corona=True)]),
        BlueCoin("Right Lava", [Requirements(SPRAY_AND_HOVER, corona=True)])],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(SPRAY_AND_HOVER, corona=True)])],
    parent_region=SmsRegionName.PLAZA)