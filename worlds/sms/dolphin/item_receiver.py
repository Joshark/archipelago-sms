import dolphin_memory_engine as dme

import worlds.sms.dolphin.addresses as addresses
import worlds.sms.dolphin.bit_helper as bit_helper
import collections
import asyncio

nozzles_available = {"Hover Nozzle": False, "Rocket Nozzle": False, "Turbo Nozzle": False}


def refresh_item_count(ctx, item_id, targ_address):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    temp = bit_helper.change_endian(counts[item_id])
    dme.write_byte(targ_address, temp)


def refresh_collection_counts(ctx):
    refresh_item_count(ctx, 523004, addresses.SMS_SHINE_COUNTER)


def enable_nozzle(nozzle_name):
    if nozzle_name == "Rocket Nozzle":
        dme.write_double(addresses.SMS_ROCKET_UNLOCK, addresses.SMS_ROCKET_UNLOCK_VALUE)
        return
    elif nozzle_name == "Turbo Nozzle":
        dme.write_double(addresses.SMS_TURBO_UNLOCK, addresses.SMS_TURBO_UNLOCK_VALUE)
        return
    elif nozzle_name == "Hover Nozzle":
        dme.write_double(addresses.SMS_NOZZLE_LOCK_ADDRESS, addresses.SMS_NOZZLE_RELEASE)
        return


async def disable_nozzle(nozzle_name):
    while not nozzles_available["Hover Nozzle"]:
        if nozzle_name == "Hover Nozzle":
            dme.hook()
            dme.write_bytes(addresses.SMS_NOZZLE_LOCK_ADDRESS, bytes.fromhex(addresses.SMS_SPRAY_LOCK_VALUE))
        await asyncio.sleep(0.1)


def initialize_nozzles():
    disable_nozzle("Hover Nozzle")


def unpack_item(item, ctx):
    refresh_collection_counts(ctx)
    if item == 523001:
        enable_nozzle("Hover Nozzle")
    elif item == 532002:
        enable_nozzle("Rocket Nozzle")
    elif item == 523003:
        enable_nozzle("Turbo Nozzle")
    elif item == 523013:
        enable_nozzle("Yoshi")
    elif item == 523000:
        enable_nozzle("Spray Nozzle")