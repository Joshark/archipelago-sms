import dolphin_memory_engine as dme
import addresses
import time
import bit_helper
import sms_engine

testHex = hex(0)
storedShines = []
curShines = []
delaySeconds = 1


def game_start():
    for x in range(0, addresses.SMS_BYTE_COUNT):
        storedShines.append(0x00)
        curShines.append(0x00)
    print(storedShines)
    dme.hook()
    if not dme.is_hooked():
        print("hook unsuccessful")
        quit()


def memory_changed():
    print(str(curShines))
    bit_list = []
    for x in range(0, addresses.SMS_BYTE_COUNT):
        if curShines[x] > storedShines[x]:
            bit_found = bit_helper.extract_bits((curShines[x]), x)
            bit_list.extend(bit_found)
            storedShines[x] = curShines[x]
    parse_bits(bit_list)


def parse_bits(all_bits):
    if len(all_bits) == 0:
        return

    print(all_bits)
    for x in all_bits:
        if x < 120:
            print("Got shine #" + str(x))
            sms_engine.send_location_checks(all_bits)



def get_shine_id(location, value):
    temp = location + value - addresses.SMS_SHINE_OFFSET
    shine_id = int(temp)
    return shine_id


async def location_watcher(watch_running):

    def _sub():
        if not dme.is_hooked():
            quit()

        for x in range(0, addresses.SMS_BYTE_COUNT):
            targ_location = addresses.SMS_SHINE_OFFSET + x
            cache_byte = dme.read_byte(targ_location)
            curShines[x] = cache_byte

        if storedShines != curShines:
            memory_changed()
        return

    while watch_running:
        time.sleep(delaySeconds)
        _sub()
