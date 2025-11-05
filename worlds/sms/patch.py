from gclib.gcm import GCM
from gclib.dol import DOL

def patch_sms_gcm(self):
    DOL_OFFSET = 0x578a63
    NEW_BYTES = b'\x38\x00\x00\x64'

    rom_path = "C:\\Users\\Joshark\\Desktop\\Emulators\\Roms\\GC&Wii\\Super Mario Sunshine (USA).iso"

    self.gcm = GCM(rom_path)
    self.dol = DOL()
    self.gcm.read_entire_disc()

    dol_data = self.gcm.read_file_data("sys/main.dol")
    self.dol.read(dol_data)

    self.dol.data.seek(DOL_OFFSET)
    self.dol.data.write(NEW_BYTES)

    self.dol.save_changes()
    self.gcm.changed_files["sys/main.dol"] = self.dol.data

    self.gcm.export_disc_to_iso_with_changed_files("C:\\Users\\Joshark\\Desktop\\Emulators")
    
    