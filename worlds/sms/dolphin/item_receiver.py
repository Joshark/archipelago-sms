import dolphin_memory_engine as dme

def unpack_item(int item)
# this is for testing only, I'll write a real function later, don't arrest me code police
    if(item == 523004)
        shineCountAdd()
    return;

def shineCountAdd()
    value = dme.read_byte(SMS_SHINE_COUNTER)
    value += 1
    dme.write_byte(SMS_SHINE_COUNTER, value)