import random
import struct

from gclib.gcm import GCM
from gclib.dol import DOL, DOLSection

CUSTOM_CODE_OFFSET_START = 0x3F00A0
SMS_PLAYER_NAME_BYTE_LENGTH = 64

# class SMSTest:

def update_dol_offsets(gcm: GCM, dol: DOL, seed: str, start_inv: int, level_access: bool,
    coin_shines: bool, blue_rando: int, yoshi_rando: bool) -> (GCM, DOL):

    random.seed(seed)

    dol_data = gcm.read_file_data("sys/main.dol")
    dol.read(dol_data)

    fmv_values1 = [0x38, 0x60, 0x00, 0x01]
    fmv_values2 = [0x38, 0x60, 0x00, 0x01]
    blue_visual_fix_values = [0x4e, 0x80, 0x00, 0x20]
    skip_blue_save_values = "60000000"

    # FMV Offset patching to skip cutscenes in game
    fmv_offset1 = dol.convert_address_to_offset(0x802B5EF4)
    fmv_offset2 = dol.convert_address_to_offset(0x802B5E8C)
    print(f"FMV1 offset: 0x{fmv_offset1:X}")
    print(f"FMV2 offset: 0x{fmv_offset2:X}")
    dol.data.seek(fmv_offset1)
    dol.data.write(struct.pack(">BBBB", *fmv_values1))
    dol.data.seek(fmv_offset2)
    dol.data.write(struct.pack(">BBBB", *fmv_values2))

    # Blue Coin Visual Bug Fix (No HUD Glitches upon picking up blue coins)
    blue_visual_fix_offset = dol.convert_address_to_offset(0x8014757c)
    print(f"Blue Visual Fix offset: 0x{blue_visual_fix_offset:X}")
    dol.data.seek(blue_visual_fix_offset)
    dol.data.write(struct.pack(">BBBB", *blue_visual_fix_values))

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

    with open("SMS_custom_code.smsco", "rb") as f:
        custom_dol_code = f.read()
    print(f"Custom Code Read: {custom_dol_code[:16]}...")
    dol.data.seek(CUSTOM_CODE_OFFSET_START)
    dol.data.write(custom_dol_code)

    # Fludd Nozzle Rando Codes
    fludd1_offset = dol.convert_address_to_offset(0x8024F934)
    fludd2_offset = dol.convert_address_to_offset(0x80268DD4)
    fludd3_offset = dol.convert_address_to_offset(0x80268E18)
    fludd4_offset = dol.convert_address_to_offset(0x802C924C)

    dol.data.seek(fludd1_offset)
    dol.data.write(bytes.fromhex("481c7ecc"))

    dol.data.seek(fludd2_offset)
    dol.data.write(bytes.fromhex("481aeaa4"))

    dol.data.seek(fludd3_offset)
    dol.data.write(bytes.fromhex("481aeae0"))

    dol.data.seek(fludd4_offset)
    dol.data.write(bytes.fromhex("4814e6cc"))

    for section in dol.sections:
        print(f"Section at 0x{section.offset:X} (0x{section.address:X}) size 0x{section.size:X}")

    dol.save_changes()
    gcm.changed_files["sys/main.dol"] = dol.data

    return gcm, dol

# if __name__ == '__main__':
#     unpacked_iso = SMSTest()