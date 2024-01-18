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
    print("Shine Count: " + str(local_shine_counter))
    dme.write_double(addresses.SMS_SHINE_COUNTER, local_shine_counter)


def unpack_item(item, ctx):
    refresh_shine_count(ctx)


