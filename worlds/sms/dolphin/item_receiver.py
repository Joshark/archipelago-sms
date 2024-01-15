import dolphin_memory_engine as dme
import addresses

cur_shine_count = 0


def shine_count_add():
    global cur_shine_count
    cur_shine_count += 1
    dme.write_byte(addresses.SMS_SHINE_COUNTER, cur_shine_count)


def unpack_item(item):
    # this is for testing only, I'll write a real function later, don't arrest me code police
    if item == 523004:
        shine_count_add()
    return

