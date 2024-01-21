import dolphin_memory_engine as dme

import worlds.sms.dolphin.addresses as addresses
import worlds.sms.dolphin.bit_helper as bit_helper
import collections
import asyncio

ap_nozzles_received = ["Spray Nozzle"]
in_game_nozzles_avail = ["Spray Nozzle"]


def refresh_item_count(ctx, item_id, targ_address):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    temp = bit_helper.change_endian(counts[item_id])
    dme.write_byte(targ_address, temp)


def refresh_collection_counts(ctx):
    refresh_item_count(ctx, 523004, addresses.SMS_SHINE_COUNTER)


def enable_nozzle(nozzle_name):

    return


async def disable_nozzle(nozzle_name):
    while not ap_nozzles_received.__contains__("Hover Nozzle"):
        if nozzle_name == "Hover Nozzle":
            dme.write_bytes(addresses.SMS_SECONDARY_NOZZLE_ADDRESS, bytes.fromhex(addresses.SMS_SPRAY_NOZZLE_VALUE))
        await asyncio.sleep(0.1)


def initialize_nozzles():
    disable_nozzle("Hover Nozzle")


def unpack_item(item, ctx):
    refresh_collection_counts(ctx)
    if item == 523001:
        ap_nozzles_received.append("Hover Nozzle")
    elif item == 532002:
        ap_nozzles_received.append("Rocket Nozzle")
    elif item == 523003:
        ap_nozzles_received.append("Turbo Nozzle")
    elif item == 523013:
        ap_nozzles_received.append("Yoshi")
    elif item == 523000:
        ap_nozzles_received.append("Spray Nozzle")


def check_in_game_nozzles():
    list.clear(in_game_nozzles_avail)

    primary_nozzle = dme.read_double(addresses.SMS_PRIMARY_NOZZLE_ADDRESS)
    if primary_nozzle == addresses.SMS_SPRAY_NOZZLE_VALUE:
        in_game_nozzles_avail.append("Spray Nozzle")

    secondary_nozzle = dme.read_double(addresses.SMS_SECONDARY_NOZZLE_ADDRESS)
    if secondary_nozzle == addresses.SMS_HOVER_NOZZLE_VALUE:
        in_game_nozzles_avail.append("Hover Nozzle")
    elif secondary_nozzle == addresses.SMS_ROCKET_NOZZLE_VALUE:
        in_game_nozzles_avail.append("Rocket Nozzle")
    elif secondary_nozzle == addresses.SMS_TURBO_NOZZLE_VALUE:
        in_game_nozzles_avail.append("Turbo Nozzle")
    return


def nozzle_assignment():
    primary_nozzle = "None"
    secondary_nozzle = "None"
    if in_game_nozzles_avail.__contains__("Spray Nozzle"):
        if ap_nozzles_received.__contains__("Spray Nozzle"):
            primary_nozzle = "Spray Nozzle"

    if in_game_nozzles_avail.__contains__("Hover Nozzle"):
        if ap_nozzles_received.__contains__("Hover Nozzle"):
            secondary_nozzle = "Hover Nozzle"
        else:
            secondary_nozzle = primary_nozzle

    if in_game_nozzles_avail.__contains__("Rocket Nozzle"):
        if ap_nozzles_received.__contains__("Rocket Nozzle"):
            secondary_nozzle = "Rocket Nozzle"
        elif ap_nozzles_received.__contains__("Hover Nozzle"):
            secondary_nozzle = "Hover Nozzle"
        else:
            secondary_nozzle = primary_nozzle

    if in_game_nozzles_avail.__contains__("Turbo Nozzle"):
        if ap_nozzles_received.__contains__("Turbo Nozzle"):
            secondary_nozzle = "Turbo Nozzle"
        elif ap_nozzles_received.__contains__("Hover Nozzle"):
            secondary_nozzle = "Hover Nozzle"
        else:
            secondary_nozzle = primary_nozzle

    if not ap_nozzles_received.__contains__("Spray Nozzle"):
        primary_nozzle = secondary_nozzle

    return [primary_nozzle, secondary_nozzle]


def set_nozzle_assignment(nozzle_name):
    assign_id = "0"
    if nozzle_name == "Spray Nozzle":
        assign_id = addresses.SMS_SPRAY_NOZZLE_VALUE
    elif nozzle_name == "Hover Nozzle":
        assign_id = addresses.SMS_HOVER_NOZZLE_VALUE
    elif nozzle_name == "Rocket Nozzle":
        assign_id = addresses.SMS_ROCKET_NOZZLE_VALUE
    elif nozzle_name == "Turbo Nozzle":
        assign_id = addresses.SMS_TURBO_NOZZLE_VALUE
    return assign_id


def enforce_nozzles(primary_nozzle, secondary_nozzle):
    primary_id = set_nozzle_assignment(primary_nozzle)
    secondary_id = set_nozzle_assignment(secondary_nozzle)
    dme.write_double(addresses.SMS_PRIMARY_NOZZLE_ADDRESS, primary_id)
    dme.write_double(addresses.SMS_SECONDARY_NOZZLE_ADDRESS, secondary_id)

    return
