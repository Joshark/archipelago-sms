import dolphin_memory_engine as dme
import addresses
import bit_helper
from SMSClient import SmsContext
import asyncio

storedShines = []
curShines = []
delaySeconds = .25
location_offset = 523000


def game_start():
    for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
        storedShines.append(0x00)
        curShines.append(0x00)
    dme.hook()
    return dme.is_hooked()


def memory_changed(ctx: SmsContext):
    bit_list = []
    for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
        if curShines[x] > storedShines[x]:
            bit_found = bit_helper.extract_bits((curShines[x]), x)
            bit_list.extend(bit_found)
            storedShines[x] = curShines[x]
    parse_bits(bit_list, ctx)


def parse_bits(all_bits, ctx: SmsContext):
    if len(all_bits) == 0:
        return

    for x in all_bits:
        if x < 120:
            temp = x + location_offset
            ctx.locations_checked.add(temp)
            ctx.send_location_checks(temp)


def get_shine_id(location, value):
    temp = location + value - addresses.SMS_SHINE_LOCATION_OFFSET
    shine_id = int(temp)
    return shine_id


async def location_watcher(ctx):
    def _sub():
        for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
            targ_location = addresses.SMS_SHINE_LOCATION_OFFSET + x
            cache_byte = dme.read_byte(targ_location)
            curShines[x] = cache_byte

        if storedShines != curShines:
            memory_changed(ctx)

        SmsContext.force_resync(ctx)
        return

    while not ctx.exit_event.is_set():
        if not dme.is_hooked():
            dme.hook()
        else:
            _sub()
        await asyncio.sleep(delaySeconds)
