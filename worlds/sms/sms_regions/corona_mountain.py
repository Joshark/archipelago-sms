from .sms_region_helper import *

CORONA_MOUNTAIN: SmsRegion = SmsRegion(SmsRegionName.CORONA,
    requirements=[Requirements(SPRAY_AND_HOVER, corona=True)],
    blue_coins=[BlueCoin("Platform", in_game_bit=540),
        BlueCoin("Back Right Lava", in_game_bit=541),
        BlueCoin("Left Lava", in_game_bit=542),
        BlueCoin("Front Lava", in_game_bit=543),
        BlueCoin("Front Left Lava", in_game_bit=544),
        BlueCoin("Front Right Lava", in_game_bit=545),
        BlueCoin("Back Left Lava", in_game_bit=546),
        BlueCoin("Far Back Left Lava", in_game_bit=547),
        BlueCoin("Far Back Right Lava", in_game_bit=548),
        BlueCoin("Right Lava", in_game_bit=549)],
    nozzle_boxes=[NozzleBox("Rocket Box", in_game_bit=886)],
    parent_region=SmsRegionName.PLAZA)