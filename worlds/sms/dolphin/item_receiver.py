import dolphin_memory_engine as dme

import SMSClient
import worlds.sms.dolphin.addresses as addresses
import collections

local_shine_counter = 0
local_bluecoin_counter = 0


def refresh_shine_count(ctx):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    global local_shine_counter
    local_shine_counter = counts[523004]
    temp = local_shine_counter.to_bytes(2, "big")
    temp = int.from_bytes(temp)
    dme.write_byte(addresses.SMS_SHINE_COUNTER, temp)


def unpack_item(item, ctx):
    refresh_shine_count(ctx)


