import hashlib
import struct
import os

from pkgutil import get_data

from gclib import fs_helpers as fs
from gclib.gcm import GCM
from gclib.dol import DOL, DOLSection
from gclib.rarc import RARC
from gclib.yaz0_yay0 import Yaz0

class InvalidCleanISOError(Exception): pass

RANDOMIZER_NAME = "Super Mario Sunshine"
CLEAN_MD5 = 0x0c6d2edae9fdf40dfc410ff1623e4119
CUSTOM_CODE_OFFSET_START = 0x3F00A0

class SMSTest:

    def __init__(self):
        self.clean_iso_path = r"C:\Users\Joshark\Desktop\Emulators\Roms\GC&Wii\Super Mario Sunshine (USA).iso"
        self.patched_iso_path = r"C:\Users\Joshark\Desktop\Emulators\Roms\GC&Wii\Super Mario Sunshine (Patched2).iso"

        try:
            if os.path.isfile(self.patched_iso_path):
                temp_file = open(self.patched_iso_path, "r+")  # or "a+", whatever you need
                temp_file.close()
        except IOError:
            raise Exception("'" + self.patched_iso_path + "' is currently in use by another program.")

        self.__verify_supported_version()
        self.gcm = GCM(self.clean_iso_path)
        self.gcm.read_entire_disc()

        dol_data = self.gcm.read_file_data("sys/main.dol")
        self.dol = DOL()
        self.dol.read(dol_data)

        # for section in self.dol.sections:
        #     print(f"Section at 0x{section.offset:X} (0x{section.address:X}) size 0x{section.size:X}")

        fmv_values1 = [0x38, 0x60, 0x00, 0x01]
        fmv_values2 = [0x38, 0x60, 0x00, 0x01]
        blue_visual_fix_values = [0x4e, 0x80, 0x00, 0x20]
        skip_blue_save_values = "60000000"

        # FMV Offset patching to skip cutscenes in game
        fmv_offset1 = self.dol.convert_address_to_offset(0x802B5EF4)
        fmv_offset2 = self.dol.convert_address_to_offset(0x802B5E8C)
        print(f"FMV1 offset: 0x{fmv_offset1:X}")
        print(f"FMV2 offset: 0x{fmv_offset2:X}")
        self.dol.data.seek(fmv_offset1)
        self.dol.data.write(struct.pack(">BBBB", *fmv_values1))
        self.dol.data.seek(fmv_offset2)
        self.dol.data.write(struct.pack(">BBBB", *fmv_values2))

        # Blue Coin Visual Bug Fix (No HUD Glitches upon picking up blue coins)
        blue_visual_fix_offset = self.dol.convert_address_to_offset(0x8014757c)
        print(f"Blue Visual Fix offset: 0x{blue_visual_fix_offset:X}")
        self.dol.data.seek(blue_visual_fix_offset)
        self.dol.data.write(struct.pack(">BBBB", *blue_visual_fix_values))

        # Skip Blue Coin Save Prompt
        skip_blue_save_offset = self.dol.convert_address_to_offset(0x8029A73C)
        print(f"Skip Blue Save offset: 0x{skip_blue_save_offset:X}")
        self.dol.data.seek(skip_blue_save_offset)
        self.dol.data.write(bytes.fromhex(skip_blue_save_values))

        # Replace section two with our own custom section, which is about 1000 hex bytes long.
        new_dol_size = 0x1000
        new_dol_sect = DOLSection(CUSTOM_CODE_OFFSET_START, 0x80417800, new_dol_size)
        self.dol.sections[2] = new_dol_sect

        # Append the extra bytes we expect, to ensure we can write to them in memory.
        self.dol.data.seek(len(self.dol.data.getvalue()))
        blank_data = b"\x00" * new_dol_size
        self.dol.data.write(blank_data)

        with open("SMS_custom_code.smsco", "rb") as f:
            custom_dol_code = f.read()
        # custom_dol_code = open("SMS_custom_code.smsco", "r")
        print(f"Custom Code Read: {custom_dol_code[:16]}...")
        self.dol.data.seek(CUSTOM_CODE_OFFSET_START)
        self.dol.data.write(custom_dol_code)

        # Fludd Nozzle Rando Codes
        fludd1_offset = self.dol.convert_address_to_offset(0x8024F934)
        fludd2_offset = self.dol.convert_address_to_offset(0x80268DD4)
        fludd3_offset = self.dol.convert_address_to_offset(0x80268E18)
        fludd4_offset = self.dol.convert_address_to_offset(0x802C924C)

        self.dol.data.seek(fludd1_offset)
        self.dol.data.write(bytes.fromhex("481c7ecc"))

        self.dol.data.seek(fludd2_offset)
        self.dol.data.write(bytes.fromhex("481aeaa4"))

        self.dol.data.seek(fludd3_offset)
        self.dol.data.write(bytes.fromhex("481aeae0"))

        self.dol.data.seek(fludd4_offset)
        self.dol.data.write(bytes.fromhex("4814e6cc"))

        for section in self.dol.sections:
            print(f"Section at 0x{section.offset:X} (0x{section.address:X}) size 0x{section.size:X}")

        self.dol.save_changes()
        self.gcm.changed_files["sys/main.dol"] = self.dol.data

        print("Patching complete. Saving new ISO to:", self.patched_iso_path)
        
        for _, _ in self.export_files_from_memory():
            continue
        print("New ISO saved!")

    def __verify_supported_version(self):
        with open(self.clean_iso_path, "rb") as f:
            magic = fs.try_read_str(f, 0, 4)
            game_id = fs.try_read_str(f, 0, 6)
        print("Magic: " + str(magic) + "; Game ID: " + str(game_id))
        if magic == "CISO":
            raise InvalidCleanISOError(f"The provided ISO is in CISO format. The {RANDOMIZER_NAME} randomizer " +
                                       "only supports ISOs in ISO format.")
        if game_id != "GMSE01":
            if game_id and game_id.startswith("GLM"):
                raise InvalidCleanISOError(f"Invalid version of {RANDOMIZER_NAME}. " +
                                           "Only the North American version is supported by this randomizer.")
            else:
                raise InvalidCleanISOError("Invalid game given as the vanilla ISO. You must specify a " +
                                           "%s ISO (North American version)." % RANDOMIZER_NAME)
        self.__verify_correct_clean_iso_md5()

    # Verify the MD5 hash matches the expectation of a USA-based ISO.
    # Based on some similar code from (MIT License): https://github.com/LagoLunatic/wwrando
    def __verify_correct_clean_iso_md5(self):
        md5 = hashlib.md5()
        with open(self.clean_iso_path, "rb") as f:
            while True:
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                md5.update(chunk)

        integer_md5 = int(md5.hexdigest(), 16)
        if integer_md5 != CLEAN_MD5:
            raise InvalidCleanISOError(
                f"Invalid vanilla {RANDOMIZER_NAME} ISO. Your ISO may be corrupted.\n" +
                f"Correct ISO MD5 hash: {CLEAN_MD5:x}\nYour ISO's MD5 hash: {integer_md5:x}")

    # Get an ARC / RARC / SZS file from within the ISO / ROM
    def get_arc(self, arc_path):
        arc_path = arc_path.replace("\\", "/")
        data = self.gcm.read_file_data(arc_path)
        arc = RARC(data)  # Automatically decompresses Yaz0
        arc.read()
        return arc
    
    def export_files_from_memory(self):
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.patched_iso_path)

if __name__ == '__main__':
    unpacked_iso = SMSTest()