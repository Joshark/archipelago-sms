import random

from gclib.gcm import GCM
from gclib.dol import DOL, DOLSection

from .Helper_Functions import StringByteFunction as sbf

CUSTOM_CODE_OFFSET_START = 0x3F00A0
SMS_PLAYER_NAME_BYTE_LENGTH = 64

# class SMSTest:

def update_dol_offsets(gcm: GCM, dol: DOL, seed: str, slot_name: str, start_inv: int, level_access: bool,
    coin_shines: bool, blue_rando: int, yoshi_rando: bool) -> (GCM, DOL):

    random.seed(seed)

    dol_data = gcm.read_file_data("sys/main.dol")
    dol.read(dol_data)

    change_nozzle_values = "481ad8a4"
    fmv_values1 = "38600001"
    fmv_values2 = "38600001"
    blue_visual_fix_values = "4e800020"
    skip_blue_save_values = "60000000"
    nozzle_rando_value1 = "481c7ecc"
    nozzle_rando_value2 = "481aeaa4"
    nozzle_rando_value3 = "481aeae0"
    nozzle_rando_value4 = "4814e6cc"
    plaza_darkness1_value = "4800006C"
    plaza_darkness2_value = "4E800020"

    # ChangeNozzle offset to check if we own the nozzles
    change_nozzle_offset = dol.convert_address_to_offset(0x8026a164)

    print(f"Change Nozzle Offset: 0x{change_nozzle_offset:X}")
    dol.data.seek(change_nozzle_offset)
    dol.data.write(bytes.fromhex(change_nozzle_values))

    # FMV Offset patching to skip cutscenes in game
    fmv_offset1 = dol.convert_address_to_offset(0x802B5EF4)
    fmv_offset2 = dol.convert_address_to_offset(0x802B5E8C)
    print(f"FMV1 offset: 0x{fmv_offset1:X}")
    print(f"FMV2 offset: 0x{fmv_offset2:X}")
    dol.data.seek(fmv_offset1)
    dol.data.write(bytes.fromhex(fmv_values1))
    dol.data.seek(fmv_offset2)
    dol.data.write(bytes.fromhex(fmv_values2))

    # Blue Coin Visual Bug Fix (No HUD Glitches upon picking up blue coins)
    blue_visual_fix_offset = dol.convert_address_to_offset(0x8014757c)
    print(f"Blue Visual Fix offset: 0x{blue_visual_fix_offset:X}")
    dol.data.seek(blue_visual_fix_offset)
    dol.data.write(bytes.fromhex(blue_visual_fix_values))

    # Skip Blue Coin Save Prompt
    skip_blue_save_offset = dol.convert_address_to_offset(0x8029A73C)
    print(f"Skip Blue Save offset: 0x{skip_blue_save_offset:X}")
    dol.data.seek(skip_blue_save_offset)
    dol.data.write(bytes.fromhex(skip_blue_save_values))

    # Replace section two with our own custom section, which is about 1000 hex bytes long.
    new_dol_size = 0x1000
    new_dol_sect = DOLSection(CUSTOM_CODE_OFFSET_START, 0x80417800, new_dol_size)
    dol.sections[2] = new_dol_sect

    # Append the extra bytes we expect, to ensure we can write to them in memory.
    dol.data.seek(len(dol.data.getvalue()))
    blank_data = b"\x00" * new_dol_size
    dol.data.write(blank_data)
    
    with open("./worlds/sms/SMS_custom_code.smsco", "rb") as f:
        custom_dol_code = f.read()
    print(f"Custom Code Read: {custom_dol_code[:16]}...")
    dol.data.seek(CUSTOM_CODE_OFFSET_START)
    dol.data.write(custom_dol_code)

    # Fludd Nozzle Rando Codes
    fludd1_offset = dol.convert_address_to_offset(0x8024F934)
    fludd2_offset = dol.convert_address_to_offset(0x80268DD4)
    fludd3_offset = dol.convert_address_to_offset(0x80268E18)
    fludd4_offset = dol.convert_address_to_offset(0x802C924C)

    print(f"Fludd Nozzle Rando Offsets: 0x{fludd1_offset:x}")
    print(f"Fludd Nozzle Rando Offsets: 0x{fludd2_offset:x}")
    print(f"Fludd Nozzle Rando Offsets: 0x{fludd3_offset:x}")
    print(f"Fludd Nozzle Rando Offsets: 0x{fludd4_offset:x}")

    dol.data.seek(fludd1_offset)
    dol.data.write(bytes.fromhex(nozzle_rando_value1))

    dol.data.seek(fludd2_offset)
    dol.data.write(bytes.fromhex(nozzle_rando_value2))

    dol.data.seek(fludd3_offset)
    dol.data.write(bytes.fromhex(nozzle_rando_value3))

    dol.data.seek(fludd4_offset)
    dol.data.write(bytes.fromhex(nozzle_rando_value4))

    # Player Slot Name Writing
    slot_name_offset = dol.convert_address_to_offset(0x80418000)
    print(f"Slot Name Offset: 0x{slot_name_offset:X}")
    dol.data.seek(slot_name_offset)
    dol.data.write(sbf.string_to_bytes(slot_name, SMS_PLAYER_NAME_BYTE_LENGTH))

    # Removes plaza darkness so game won't go full dark mode above 120 shines
    plaza_darkness1_offset = dol.convert_address_to_offset(0x8017D1E0)
    plaza_darkness2_offset = dol.convert_address_to_offset(0x8027C67C)
    print(f"Plaza Darkness1 Offset: 0x{plaza_darkness1_offset:X}")
    print(f"Plaza Darkness2 Offset: 0x{plaza_darkness2_offset:X}")
    dol.data.seek(plaza_darkness1_offset)
    dol.data.write(bytes.fromhex(plaza_darkness1_value))
    dol.data.seek(plaza_darkness2_offset)
    dol.data.write(bytes.fromhex(plaza_darkness2_value))

    for section in dol.sections:
        print(f"Section at 0x{section.offset:X} (0x{section.address:X}) size 0x{section.size:X}")

    dol.save_changes()
    gcm.changed_files["sys/main.dol"] = dol.data

    return gcm, dol
