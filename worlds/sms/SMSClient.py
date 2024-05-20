from __future__ import annotations

import asyncio
import collections
import time
from dataclasses import dataclass

import ModuleUpdate
from .options import SmsOptions
from .bit_helper import change_endian, bit_flagger, extract_bits
import dolphin_memory_engine as dme
from . import addresses

ModuleUpdate.update()

import Utils

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

ap_nozzles_received = []
ticket_listing = []
in_game_nozzles_avail = ["Spray Nozzle", "Hover Nozzle", "Rocket Nozzle", "Turbo Nozzle"]
world_flags = {}
debug = False
debug_b = False

game_ver = 0x3a


class SmsCommandProcessor(ClientCommandProcessor):

    def _cmd_connect(self, address: str = "") -> bool:
        temp = super()._cmd_connect()
        if dme.is_hooked():
            logger.info("Already connected to Dolphin!")
            self._cmd_resync()
        else:
            logger.info("Please connect to Dolphin (may have issues, default is to start game before opening client).")
        if temp:
            return True
        else:
            return False

    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True
        refresh_collection_counts(self.ctx)


class SmsContext(CommonContext):
    command_processor: SmsCommandProcessor
    game = "Super Mario Sunshine"
    items_handling = 0b111  # full remote

    options: SmsOptions

    hook_check = False
    hook_nagged = False

    believe_hooked = False

    lives_given = 0
    lives_switch = False

    yoshi_check = False

    goal = 50
    corona_message_given = False
    blue_status = 1
    fludd_start = 0
    yoshi_mode = 0
    ticket_mode = False
    victory = False

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

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            slot_data = args.get("slot_data")
            self.goal = slot_data.get("corona_mountain_shines")
            temp = slot_data.get("blue_coin_sanity")
            if temp:
                self.blue_status = temp
            temp = slot_data.get("starting_nozzle")
            if temp:
                self.fludd_start = temp
            temp = slot_data.get("yoshi_mode")
            if temp:
                self.yoshi_mode = temp
            temp = slot_data.get("ticket_mode")
            if temp:
                self.ticket_mode = temp

    def get_corona_goal(self):
        if self.goal:
            return self.goal
        else:
            return 50


storedShines = []
curShines = []
delaySeconds = .5
location_offset = 523000


def game_start():
    for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
        storedShines.append(0x00)
        curShines.append(0x00)
    dme.hook()
    return dme.is_hooked()


async def game_watcher(ctx: SmsContext):
    while not ctx.exit_event.is_set():

        sync_msg = [{'cmd': 'Sync'}]
        if ctx.locations_checked:
            sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
        await ctx.send_msgs(sync_msg)

        refresh_collection_counts(ctx)
        ctx.lives_switch = True

        if ctx.victory and not ctx.finished_game:
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

        await asyncio.sleep(0.2)
        ctx.lives_switch = False


async def location_watcher(ctx):
    def _sub():
        if not dme.is_hooked():
            return

        for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
            targ_location = addresses.SMS_SHINE_LOCATION_OFFSET + x
            cache_byte = dme.read_byte(targ_location)
            curShines[x] = cache_byte

        if storedShines != curShines:
            memory_changed(ctx)

        return

    while not ctx.exit_event.is_set():
        if not dme.is_hooked():
            dme.hook()
        else:
            _sub()
        await asyncio.sleep(delaySeconds)


async def arbitrary_ram_checks(ctx):
    if not dme.is_hooked():
        return
    for noz in NOZZLES:
        if ap_nozzles_received.__contains__(noz.nozzle_name):
            dme.write_byte(noz.arb_address+0x3, 0x1)


def memory_changed(ctx: SmsContext):
    if debug: logger.info("memory_changed: " + str(curShines))
    bit_list = []
    for x in range(0, addresses.SMS_SHINE_BYTE_COUNT):
        bit_found = extract_bits((curShines[x]), x)
        bit_list.extend(bit_found)
        storedShines[x] = curShines[x]
    if debug: logger.info("bit_list: " + str(bit_list))
    parse_bits(bit_list, ctx)


def send_victory(ctx: SmsContext):
    if ctx.victory:
        return

    ctx.victory = True
    ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
    logger.info("Congratulations on completing your seed!")
    time.sleep(.05)
    logger.info("ARCHIPELAGO SUPER MARIO SUNSHINE CREDITS:")
    time.sleep(.05)
    logger.info("MrsMarinaRose - Client, Modding and Patching")
    time.sleep(.05)
    logger.info("Hatkirby - APworld")
    time.sleep(.05)
    logger.info("ScorelessPine - Original Manual")
    time.sleep(.05)
    logger.info("Fedora - Logic and testing")
    time.sleep(.05)
    logger.info("J2Slow - Logic and testing")
    time.sleep(.05)
    logger.info("Quizzeh - Extra testing")
    time.sleep(.05)
    logger.info("Spicynun - Additional research")
    time.sleep(.05)
    logger.info("JoshuaMKW - Sunshine Toolset")
    time.sleep(.05)
    logger.info("All Archipelago core devs")
    time.sleep(.05)
    logger.info("Nintendo EAD")
    time.sleep(.05)
    logger.info("...and you. Thanks for playing!")
    return


def parse_bits(all_bits, ctx: SmsContext):
    if debug: logger.info("parse_bits: " + str(all_bits))
    if len(all_bits) == 0:
        return

    for x in all_bits:
        if x <= 119:
            temp = x + location_offset
            ctx.locations_checked.add(temp)
            if debug: logger.info("checks to send: " + str(temp))
        elif 119 < x < 549:
            temp = x + location_offset
            ctx.locations_checked.add(temp)
        if x == 119:
            send_victory(ctx)


def get_shine_id(location, value):
    temp = location + value - addresses.SMS_SHINE_LOCATION_OFFSET
    shine_id = int(temp)
    return shine_id


def refresh_item_count(ctx, item_id, targ_address):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    temp = change_endian(counts[item_id])
    if dme.is_hooked():
        dme.write_byte(targ_address, temp)


def refresh_all_items(ctx: SmsContext):
    counts = collections.Counter(received_item.item for received_item in ctx.items_received)
    for items in counts:
        if counts[items] > 0:
            unpack_item(items, ctx, counts[items])
    if counts[523004] >= ctx.get_corona_goal():
        if counts[523002] > 0:
            activate_ticket(999999)
            if not ctx.corona_message_given:
                logger.info("Corona Mountain requirements reached! Reload Delfino Plaza to unlock.")
                ctx.corona_message_given = True


def refresh_collection_counts(ctx):
    if debug: logger.info("refresh_collection_counts")
    refresh_item_count(ctx, 523004, addresses.SMS_SHINE_COUNTER)
    if ctx.blue_status == 1:
        refresh_item_count(ctx, 523014, addresses.SMS_BLUECOIN_COUNTER)
    refresh_all_items(ctx)


def check_world_flags(byte_location, byte_pos, bool_setting):
    if world_flags.get(byte_location):
        byte_value = world_flags.get(byte_location)
    else:
        byte_value = dme.read_byte(byte_location)
    byte_value = bit_flagger(byte_value, byte_pos, bool_setting)
    world_flags.update({byte_location: byte_value})
    return byte_value


def open_stage(ticket):
    value = check_world_flags(ticket.address, ticket.bit_position, True)
    dme.write_byte(ticket.address, value)
    return


def special_noki_handling():
    dme.write_double(addresses.SMS_NOKI_REQ, addresses.SMS_NOKI_LO)
    return


def unpack_item(item, ctx, amt=0):
    if 522999 < item < 523004:
        activate_nozzle(item)
    elif item == 523013:
        activate_yoshi(ctx)
    elif 523004 < item < 523011:
        activate_ticket(item)


def disable_shadow_mario():
    if dme.is_hooked():
        dme.write_double(addresses.SMS_SHADOW_MARIO_STATE, 0)


@dataclass
class Ticket:
    item_name: str
    item_id: int
    bit_position: int
    course_id: int
    address: int = 0x805789f8
    active: bool = False


TICKETS: list[Ticket] = [
    Ticket("Bianco Hills Ticket", 523005, 5, 2, 0x805789f8),
    Ticket("Ricco Harbor Ticket", 523006, 6, 3, 0x805789f8),
    Ticket("Gelato Beach Ticket", 523007, 7, 4, 0x805789f8),
    Ticket("Pinna Park Ticket", 523008, 1, 5, 0x805789f9),
    Ticket("Noki Bay Ticket", 523009, 3, 9, 0x805789fd),
    Ticket("Sirena Beach Ticket", 523010, 3, 6, 0x805789f9),
    Ticket("Corona Mountain Ticket", 999999, 6, 34, 0x805789fd)
]


def activate_ticket(id: int):
    for tickets in TICKETS:
        if id == tickets.item_id:
            tickets.active = True
            handle_ticket(tickets)
            if not ticket_listing.__contains__(tickets.item_name):
                ticket_listing.append(tickets.item_name)
                logger.info("Current Tickets: " + str(ticket_listing))


def handle_ticket(tick: Ticket):
    if not tick.active:
        return
    if not dme.is_hooked():
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
    arb_address: int


NOZZLES: list[NozzleItem] = [
    NozzleItem("Spray Nozzle", 523000, addresses.ARB_SPRAY_ENABLER),
    NozzleItem("Hover Nozzle", 523001, addresses.ARB_HOVER_ENABLER),
    NozzleItem("Rocket Nozzle", 523002, addresses.ARB_ROCKET_ENABLER),
    NozzleItem("Turbo Nozzle", 523003, addresses.ARB_TURBO_ENABLER),
    NozzleItem("Yoshi", 53013, 0)
]


def extra_unlocks_needed():
    if not dme.is_hooked():
        return
    dme.write_byte(addresses.SMS_YOSHI_UNLOCK-1, 240)
    val = bit_flagger((dme.read_byte(addresses.SMS_YOSHI_UNLOCK)), 1, True)
    dme.write_byte(addresses.SMS_YOSHI_UNLOCK, val)


def activate_nozzle(id):
    if not dme.is_hooked():
        return
    if id == 523000:
        if not ap_nozzles_received.__contains__("Spray Nozzle"):
            ap_nozzles_received.append("Spray Nozzle")
            logger.info(str(ap_nozzles_received))
    if id == 523001:
        if not ap_nozzles_received.__contains__("Hover Nozzle"):
            ap_nozzles_received.append("Hover Nozzle")
            logger.info(str(ap_nozzles_received))
    if id == 523013:
        temp = dme.read_byte(addresses.SMS_YOSHI_UNLOCK)
        if temp < 2:
            dme.write_byte(addresses.SMS_YOSHI_UNLOCK, 2)
        extra_unlocks_needed()
    if id == 523002:
        if not ap_nozzles_received.__contains__("Rocket Nozzle"):
            ap_nozzles_received.append("Rocket Nozzle")
            logger.info(str(ap_nozzles_received))
        # rocket nozzle
    if id == 523003:

        if not ap_nozzles_received.__contains__("Turbo Nozzle"):
            ap_nozzles_received.append("Turbo Nozzle")
            logger.info(str(ap_nozzles_received))
        # turbo nozzle
    return


def activate_yoshi(ctx):
    if not dme.is_hooked():
        return
    temp = dme.read_byte(addresses.SMS_YOSHI_UNLOCK)
    if temp < 130:
        dme.write_byte(addresses.SMS_YOSHI_UNLOCK, 130)
        # BEGIN YOSHI BANDAID
    if ctx.yoshi_mode:
        flag = dme.read_byte(0x8057898c)
        new_flag = bit_flagger(flag, 1, True)
        dme.write_byte(new_flag, 0x8057898c)
    # END YOSHI BANDAID
    extra_unlocks_needed()

    if not ap_nozzles_received.__contains__("Yoshi"):
        ap_nozzles_received.append("Yoshi")
        logger.info(str(ap_nozzles_received))
    return


def resolve_tickets(stage, ctx):
    for tick in TICKETS:
        if tick.course_id == stage and not tick.active:
            logger.info("Entering a stage without a ticket! Initiating bootout...")
            dme.write_byte(addresses.SMS_NEXT_STAGE, 1)
            dme.write_byte(addresses.SMS_CURRENT_STAGE, 1)
    return


async def handle_stages(ctx):
    while not ctx.exit_event.is_set():
        if dme.is_hooked():
            stage = dme.read_byte(addresses.SMS_NEXT_STAGE)

            if ctx.fludd_start == 2 and stage == 0x00 and ctx.ticket_mode == 0: # Airstrip 1 skip
                open_stage(Ticket("Bianco Hills Ticket", 523005, 5, 2, 0x805789f8))
                dme.write_byte(addresses.SMS_NEXT_STAGE, 0x01)

            if stage == 0x01: # Delfino Plaza
                episode = dme.read_byte(addresses.SMS_NEXT_EPISODE)
                if episode == 0x00 and ctx.ticket_mode == 1:
                    dme.write_byte(addresses.SMS_NEXT_EPISODE, 0x6)
                if not episode == 0x01:
                    dme.write_double(addresses.SMS_SHADOW_MARIO_STATE, 0x0)
                    # BEGIN YOSHI BANDAID
            elif stage == 0x05: # Pinna Park
                if ctx.yoshi_mode:
                    episode = dme.read_byte(addresses.SMS_NEXT_EPISODE)
                    if episode == 0x03:
                        dme.write_byte(addresses.SMS_NEXT_EPISODE, 0x04)
                        dme.write_byte(addresses.SMS_CURRENT_EPISODE, 0x04)
                    # END YOSHI BANDAID
            if ctx.ticket_mode:
                resolve_tickets(stage, ctx)
        await asyncio.sleep(0.1)


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

        arbitrary = asyncio.create_task(arbitrary_ram_checks(ctx))
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="SmsProgressionWatcher")
        loc_watch = asyncio.create_task(location_watcher(ctx))
        stage_watch = asyncio.create_task(handle_stages(ctx))

        await progression_watcher
        await loc_watch
        await stage_watch
        await arbitrary
        await asyncio.sleep(.25)

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        await asyncio.sleep(.5)

    import colorama
    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="Super Mario Sunshine Client, for text interfacing.")
    args, rest = parser.parse_known_args()
    main(args.connect, args.password)
