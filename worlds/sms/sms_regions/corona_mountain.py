from .sms_region_helper import *

CORONA_MOUNTAIN: SmsRegion = SmsRegion(SmsRegionName.CORONA,
    requirements=[Requirements(SPRAY_AND_HOVER, corona=True)],
    blue_coins=[BlueCoin("Platform"),
        BlueCoin("Back Right Lava"),
        BlueCoin("Left Lava"),
        BlueCoin("Front Lava"),
        BlueCoin("Front Left Lava"),
        BlueCoin("Front Right Lava"),
        BlueCoin("Back Left Lava"),
        BlueCoin("Far Back Left Lava"),
        BlueCoin("Far Back Right Lava"),
        BlueCoin("Right Lava")],
    nozzle_boxes=[NozzleBox("Rocket Box")],
    parent_region=SmsRegionName.PLAZA)