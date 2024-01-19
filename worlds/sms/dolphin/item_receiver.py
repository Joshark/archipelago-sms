import dolphin_memory_engine as dme

import SMSClient
import worlds.sms.dolphin.addresses as addresses
import collections


def refresh_item_count(ctx, item_id, targ_address):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    temp = counts[item_id]
    temp = temp.to_bytes(2, "big")
    temp = int.from_bytes(temp)
    dme.write_byte(addresses.SMS_SHINE_COUNTER, temp)


def refresh_collection_counts(ctx):
    refresh_item_count(ctx, 523004, addresses.SMS_SHINE_COUNTER)


def enable_nozzle(nozzle_name):
    if nozzle_name == "Rocket Nozzle":
        return
    elif nozzle_name == "Turbo Nozzle":
        return


def disable_nozzle(nozzle_name):
    if nozzle_name == "Hover Nozzle":
        dme.write_double(addresses.SMS_NOZZLE_LOCK_ADDRESS, addresses.SMS_HOVER_LOCK_VALUE)
    return


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

