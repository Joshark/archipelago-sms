import dolphin_memory_engine as dme
import addresses


def shine_count_add():
    value = dme.read_byte(addresses.SMS_SHINE_COUNTER)
    value += 1
    dme.write_byte(addresses.SMS_SHINE_COUNTER, value)


def unpack_item(item):
    # this is for testing only, I'll write a real function later, don't arrest me code police
    if item == 523004:
        shine_count_add()
    return

