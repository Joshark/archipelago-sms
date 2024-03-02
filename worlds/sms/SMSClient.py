from __future__ import annotations

import asyncio
import collections
from dataclasses import dataclass

import ModuleUpdate
from .options import SmsOptions
from .bit_helper import change_endian, bit_flagger
from .bit_helper import extract_bits
from .packages import dolphin_memory_engine as dme

ModuleUpdate.update()

import Utils

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

ap_nozzles_received = ["Spray Nozzle"]
in_game_nozzles_avail = ["Spray Nozzle"]
world_flags = {}


class SmsCommandProcessor(ClientCommandProcessor):

    def _cmd_connect(self, address: str = "") -> bool:
        temp = super()._cmd_connect()
        if dme.is_hooked():
            logger.info("Already connected to Dolphin!")
        else:
            logger.info("Please connect to Dolphin (may have issues, default is to start game before opening client).")
        if temp:
            self._cmd_resync()
            return True
        else:
            return False

    def _cmd_resync(self):
        """Manually trigger a resync."""
        if initialize_nozzles():
            logger.info("Connected to Dolphin.")
        self.output(f"Syncing items.")
        self.ctx.syncing = True
        refresh_collection_counts(self.ctx)

    def _cmd_received(self) -> bool:
        for index, item in enumerate(self.ctx.items_received, 1):
            unpack_item(self.ctx.items_received[item.item], self.ctx)
        return super()._cmd_received()


class SmsContext(CommonContext):
    command_processor: int = SmsCommandProcessor
    game = "Super Mario Sunshine"
    items_handling = 0b111  # full remote

    options = Utils.get_options().get("sms_options", None)

    hook_check = False
    hook_nagged = False

    def __init__(self, server_address, password):
        super(SmsContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(SmsContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    def send_location_checks(self, check_ids):
        self.send_msgs([{"cmd": "LocationChecks", "locations": [check_ids]}])

    def force_resync(self):
        self.syncing = True
        return

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class SmsManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Super Mario Sunshine Client"

        self.ui = SmsManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


class addresses:
    SMS_SHINE_COUNTER = 0x80578A5b
    SMS_BLUECOIN_COUNTER = 0x80578a60

    SMS_SHINE_LOCATION_OFFSET = 0x80578988
    SMS_SHINE_BYTE_COUNT = 15
    SMS_BLUECOIN_LOCATION_OFFSET = 0x80578997
    SMS_BLUECOIN_BYTE_COUNT = 30

    SMS_UNKNOWN_THING = 0x81006D57
    SMS_PRIMARY_NOZZLE_ADDRESS = 0x8026A044
    SMS_SECONDARY_NOZZLE_ADDRESS = 0x80269F50

    SMS_SPRAY_NOZZLE_VALUE = "3BE00000"
    SMS_HOVER_NOZZLE_VALUE = "3BE00002"
    SMS_ROCKET_NOZZLE_VALUE = "3BE00004"
    SMS_TURBO_NOZZLE_VALUE = "3BE00005"
    SMS_NOZZLE_RELEASE = "8BFE1C85"

    SMS_ROCKET_UNLOCK = 0x8029443C
    SMS_ROCKET_UNLOCK_VALUE = "38600001"

    SMS_TURBO_UNLOCK = 0x80294440
    SMS_TURBO_UNLOCK_VALUE = "4E800020"

    SMS_YOSHI_UNLOCK = 0x805789f9

    SMS_SPECIAL_FLAG = 0x80600040

    SMS_NOKI_REQ = 0x802b79e0
    SMS_NOKI_HI = 0x2c030099
    SMS_NOKI_LO = 0x2c030000

    SMS_SHADOW_MARIO_STATE = 0x80578A88

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

async def game_watcher(ctx: SmsContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        victory = False
        # ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        if not ctx.hook_check:
            if not ctx.hook_nagged:
                logger.info("Checking Dolphin hookup...")
            dme.hook()
            if dme.is_hooked():
                logger.info("Hooked to Dolphin!")
                ctx.hook_check = True
            elif not ctx.hook_nagged:
                logger.info(
                    "Please connect to Dolphin (may have issues, default is to start game before opening client).")
                ctx.hook_nagged = True

        if ctx.hook_check and not dme.is_hooked():
            logger.info("Dolphin connection lost!")
            ctx.hook_check = False
            ctx.hook_nagged = False
        await asyncio.sleep(0.1)

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

async def disable_nozzle(nozzle_name):
    while not ap_nozzles_received.__contains__("Hover Nozzle"):
        if nozzle_name == "Hover Nozzle":
            dme.write_bytes(addresses.SMS_SECONDARY_NOZZLE_ADDRESS, bytes.fromhex(addresses.SMS_SPRAY_NOZZLE_VALUE))
        await asyncio.sleep(0.1)
    while not ap_nozzles_received.__contains__("Yoshi"):
        if nozzle_name == "Yoshi":
            temp = dme.read_byte(addresses.SMS_YOSHI_UNLOCK)
            temp = check_world_flags(temp, 7, False)
            dme.write_byte(addresses.SMS_YOSHI_UNLOCK, temp)


def memory_changed(ctx: SmsContext):
    bit_list = []
    for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
        if curShines[x] > storedShines[x]:
            bit_found = extract_bits((curShines[x]), x)
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




def refresh_item_count(ctx, item_id, targ_address):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    temp = change_endian(counts[item_id])
    dme.write_byte(targ_address, temp)


def refresh_all_items(ctx):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    for items in counts:
        if counts[items] > 0:
            unpack_item(items, ctx)
    if counts[523004] > SmsOptions.corona_mountain_shines:
        activate_ticket(999999)


def refresh_collection_counts(ctx):
    refresh_item_count(ctx, 523004, addresses.SMS_SHINE_COUNTER)
    refresh_all_items(ctx)


def check_world_flags(byte_location, byte_pos, bool_setting):
    if world_flags.get(byte_location):
        byte_value = world_flags.get(byte_location)
    else:
        byte_value = dme.read_byte(byte_location)
    byte_value = bit_flagger(byte_value, byte_pos, bool_setting)
    world_flags.update({byte_location: byte_value})
    return byte_value


def enable_nozzle(nozzle_name):
    if nozzle_name == "Hover Nozzle":
        dme.write_bytes(addresses.SMS_SECONDARY_NOZZLE_ADDRESS, bytes.fromhex(addresses.SMS_NOZZLE_RELEASE))
    elif nozzle_name == "Rocket Nozzle":
        dme.write_bytes(addresses.SMS_ROCKET_UNLOCK, bytes.fromhex(addresses.SMS_ROCKET_UNLOCK_VALUE))
    elif nozzle_name == "Turbo Nozzle":
        dme.write_bytes(addresses.SMS_TURBO_UNLOCK, bytes.fromhex(addresses.SMS_TURBO_UNLOCK_VALUE))
    elif nozzle_name == "Yoshi":
        temp = dme.read_byte(addresses.SMS_YOSHI_UNLOCK)
        temp = check_world_flags(temp, 7, True)
        dme.write_byte(addresses.SMS_YOSHI_UNLOCK, temp)




def initialize_nozzles():
    info = False
    if not dme.is_hooked():
        dme.hook()
        info = True
    disable_nozzle("Hover Nozzle")
    disable_nozzle("Yoshi")
    return info


def open_stage(ticket):
    print("Opening stage " + ticket.item_name)
    byte = dme.read_double(ticket.address)
    value = check_world_flags(byte, ticket.bit_position, True)
    print("Write value " + str(value) + " to location " + str(ticket.address))
    dme.write_byte(ticket.address, value)
    return


def special_noki_handling():
    dme.write_double(addresses.SMS_NOKI_REQ, addresses.SMS_NOKI_LO)
    return


def unpack_item(item, ctx):
    if 522999 < item < 523004:
        activate_nozzle(item)
    elif item == 523013:
        activate_yoshi()
    elif 523004 < item < 523011:
        activate_ticket(item)


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


def disable_shadow_mario():
    dme.write_double(addresses.SMS_SHADOW_MARIO_STATE, 0)


def enforce_nozzles(primary_nozzle, secondary_nozzle):
    primary_id = set_nozzle_assignment(primary_nozzle)
    secondary_id = set_nozzle_assignment(secondary_nozzle)
    dme.write_double(addresses.SMS_PRIMARY_NOZZLE_ADDRESS, primary_id)
    dme.write_double(addresses.SMS_SECONDARY_NOZZLE_ADDRESS, secondary_id)
    return




@dataclass
class Ticket:
    item_name: str
    item_id: int
    bit_position: int
    address: int = 0x805789f8
    active: bool = False


TICKETS: list[Ticket] = [
    Ticket("Bianco Hills Ticket", 523005, 5, 0x805789f8),
    Ticket("Ricco Harbor Ticket", 523006, 6, 0x805789f8),
    Ticket("Gelato Beach Ticket", 523007, 7, 0x805789f8),
    Ticket("Pinna Park Ticket", 523008, 1, 0x805789f9),
    Ticket("Noki Bay Ticket", 523009, 3, 0x805789fd),
    Ticket("Sirena Beach Ticket", 523010, 3, 0x805789f9),
    Ticket("Corona Mountain Ticket", 999999, 6, 0x805789fd)
]


def activate_ticket(id: int):
    for tickets in TICKETS:
        if id == tickets.item_id:
            logger.info("Activating " + tickets.item_name)
            tickets.active = True
            handle_ticket(tickets)


def handle_ticket(tick: Ticket):
    if not tick.active:
        return
    if tick.item_name == "Noki Bay Ticket":
        special_noki_handling()
    open_stage(tick)
    return


def refresh_all_tickets():
    for tickets in TICKETS:
        handle_ticket(tickets)


@dataclass
class NozzleItem:
    nozzle_name: str
    ap_item_id: int
    unlock_address: int
    unlock_value: str


NOZZLES: list[NozzleItem] = [
    NozzleItem("Spray Nozzle", 523000, 0, "none"),
    NozzleItem("Hover Nozzle", 523001, 0x80294438, "unknown"),
    NozzleItem("Rocket Nozzle", 523002, 0x8029443C, "38600001"),
    NozzleItem("Turbo Nozzle", 523003, 0x80294440, "4E800020"),
    NozzleItem("Yoshi", 53013, 0, "none")
]


def activate_nozzle(id):
    for nozzles in NOZZLES:
        if id == nozzles.ap_item_id:
            logger.info("Activating " + nozzles.nozzle_name)
    return


def activate_yoshi():
    for nozzles in NOZZLES:
        if id == nozzles.ap_item_id:
            logger.info("Activating " + nozzles.nozzle_name)
    return


def main(connect= None, password= None):
    Utils.init_logging("SMSClient", exception_logger="Client")

    async def _main(connect, password):
        ctx = SmsContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        game_start()
        if dme.is_hooked():
            logger.info("Hooked to Dolphin!")
        loc_watch = asyncio.create_task(location_watcher(ctx))
        item_locker = asyncio.create_task(disable_nozzle("Hover Nozzle"))
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="SmsProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        await loc_watch
        await item_locker
        await progression_watcher

    import colorama
    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="Super Mario Sunshine Client, for text interfacing.")
    args, rest = parser.parse_known_args()
    main(args.connect, args.password)
