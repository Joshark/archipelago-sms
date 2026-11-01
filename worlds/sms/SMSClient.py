import copy
import os
import sys
import asyncio
import time
from dataclasses import dataclass
from typing import Optional

import ModuleUpdate
ModuleUpdate.update() # Handles updated packages on source, does nothing on frozen.

import Utils
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    server_loop
import dolphin_memory_engine as dme
from settings import get_settings

from .constants import *
import addresses
from .bit_helper import bit_flagger
from .regions import ALL_REGIONS
from .items import REGULAR_PROGRESSION_ITEMS, TICKET_ITEMS

TRACKER_LOADED = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext
    TRACKER_LOADED = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext


@dataclass
class Ticket:
    item_name: str
    bit_position: int
    address: int = 0x805789f8
    active: bool = False

def read_string(console_address: int, strlen: int) -> str:
    return dme.read_bytes(console_address, strlen).split(b"\0", 1)[0].decode()


class SmsCommandProcessor(ClientCommandProcessor):
    def _cmd_dolphin(self):
        """Prints the current Dolphin status to the client."""
        if isinstance(self.ctx, SmsContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    # def _cmd_resync(self):
    #     """Manually trigger a resync."""
    #     self.output("Syncing items.")
    #     self.ctx.syncing = True
    #     refresh_collection_counts(self.ctx)

    def _cmd_change_dolphin_process_name(self, process_name: str):
        """Specify the name of the Dolphin process to connect to. "" for system default."""
        self.ctx.hook_name = process_name
        logger.info(f"Changing Dolphin process name to: {process_name if process_name else ""}")
        from . import SuperMarioSunshineSettings
        settings: SuperMarioSunshineSettings = get_settings().sms_options
        settings.dolphin_process_name = SuperMarioSunshineSettings.DolphinProcessName(process_name)
        get_settings().save()
        log_msg: str = f"Dolphin process name set to {process_name or "default"}. You must open a new client for this to take effect."
        logger.info(log_msg)
        Utils.messagebox("Close SMS Client to take effect", log_msg, True)
        Utils.async_start(self.ctx.disconnect())


class SmsContext(SuperContext):
    command_processor = SmsCommandProcessor
    game: str = WORLD_NAME
    items_handling: int = 0b111  # full remote
    corona_message_given: bool = False
    has_send_death: bool = False
    rom_loaded: bool = False
    password_required: bool = False

    send_index: int = 0 # TODO find a place in save ram data to store/read this
    tickets: dict[int, Ticket] = [
        2, Ticket("Bianco Hills Ticket", 5, 0x805789f8),
        3, Ticket("Ricco Harbor Ticket", 6, 0x805789f8),
        4, Ticket("Gelato Beach Ticket", 7, 0x805789f8),
        5, Ticket("Pinna Park Ticket", 1, 0x805789f9),
        9, Ticket("Noki Bay Ticket", 3, 0x805789fd),
        6, Ticket("Sirena Beach Ticket", 3, 0x805789f9),
        8, Ticket("Pianta Village Ticket", 4, 0x805789f9),
        34, Ticket("Corona Mountain Ticket", 6, 0x805789fd)
    ]

    # Current Shine/Blue Coins and Recv Shine/Blue Coin
    curr_shines: int = 0
    req_shine: int = 0
    curr_blue_coins: int = 0
    req_blue_coins: int = 0
    blue_coin_sanity: bool = False
    has_receive_death: bool = False # TODO Do not handle deathlinks while stage is transition / fade to black or during shine get.
    starting_nozzle: int
    ticket_mode: bool

    def __init__(self, server_address, password):
        super(SmsContext, self).__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS

        from . import SuperMarioSunshineSettings
        settings: SuperMarioSunshineSettings = get_settings().sms_options
        if settings.dolphin_process_name:
            os.environ[DME_DOLPHIN_PROCESS_NAME] = settings.dolphin_process_name
        elif DME_DOLPHIN_PROCESS_NAME in os.environ:
            del os.environ[DME_DOLPHIN_PROCESS_NAME]

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """Disconnect from the server, unhook from Dolphin Memory Engine and set flags."""
        await super().disconnect()
        dme.un_hook()
        self.set_dolphin_status(CONNECTION_LOST_STATUS)

    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server. This function will be called as part of the init RoomInfo call
        in CommonClient, however we will exit if the rom is not loaded yet.

        Args:
            password_requested (bool): Whether the server requires a password. Defaults to `False`.
        """
        if not self.rom_loaded:
            logger.info(DOLPHIN_DIDNT_LOAD_ROM_CORRECTLY)
            return

        await super().server_auth(password_requested)

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)

        match cmd:
            # TODO Handle DeathLink

            case "RoomInfo":
                self.password_required = bool(args["password"])

            case "Connected":
                slot_data = args["slot_data"]
                self.req_shine = slot_data["corona_mountain_shines"]
                self.blue_coin_sanity = slot_data["blue_coin_sanity"]
                self.ticket_mode = slot_data["level_access"]
                self.starting_nozzle = slot_data["starting_nozzle"]
                self.req_blue_coins = slot_data["blue_coin_maximum"]
                Utils.async_start(self.update_death_link(bool(slot_data["death_link"])))

    async def dme_loop(self) -> None:
        """Main loop that checks in game values using Dolphin Memory Engine."""
        try:
            # If DME is not already hooked or connected in any way
            if not dme.is_hooked() and not await self.try_hook():
                return

            if not self.dolphin_status == CONNECTION_CONNECTED_STATUS:
                # checks the id of the game as a string
                romgameid: str = dme.read_bytes(0x80000000, 6)
                if not int(romgameid) or romgameid.decode() != GAME_ID:
                    dme.un_hook()
                    self.set_dolphin_status(DOLPHIN_DIDNT_LOAD_ROM_CORRECTLY)
                    await wait_for_next_loop(WAIT_TIMER_LONG_TIMEOUT)
                    return

                if not self.auth:
                    self.auth = dme.read_bytes(addresses.SLOT_NAME_OFF, SMS_PLAYER_NAME_BYTE_LENGTH).decode("utf-8")

                # Inform the player we are ready and waiting for them to connect.
                if not self.rom_loaded:
                    self.set_dolphin_status(CONNECTION_VERIFY_SERVER)
                    self.rom_loaded = True
                    await self.server_auth(self.password_required)

                if not self.slot:
                    await wait_for_next_loop(WAIT_TIMER_LONG_TIMEOUT)
                    return

                self.set_dolphin_status(CONNECTION_CONNECTED_STATUS)

            await self.handle_stages()
            await self.location_watcher()
            await self.sms_give_items()

            if "DeathLink" in self.tags:
                await self.check_death()

            shine_count: int = len([recv_item for recv_item in self.items_received if recv_item.item == 523004])
            if shine_count >= self.req_shine:
                activate_ticket(999999)
                if not self.corona_message_given:
                    logger.info("Corona Mountain requirements reached! Reload Delfino Plaza to unlock.")
                    self.corona_message_given = True
            # TODO always update progression loop, check victory, send finished game
            # if ctx.victory and not ctx.finished_game:
            #     await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            #     ctx.finished_game = True

        except Exception as dmeEx:
            logger.error("Unable to connect to Super Mario Sunshine. Details: " + str(dmeEx))
            await self.disconnect()
            await wait_for_next_loop(WAIT_TIMER_LONG_TIMEOUT)

    async def try_hook(self) -> bool:
        """Try to hook the Dolphin Memory Engine process into dolphin."""
        dme.hook()

        if dme.get_status() == dme.get_status().noEmu or dme.get_status() == dme.get_status().notRunning:
            dme.un_hook()
            self.set_dolphin_status(CONNECTION_INITIAL_STATUS)
            await wait_for_next_loop(WAIT_TIMER_LONG_TIMEOUT)
            return False

        return True

    async def dolphin_loop(self) -> None:
        """Continuously check and communicate with Dolphin until the user disconnects."""
        logger.info("Starting Dolphin connector. Use /dolphin for status information.")
        while not self.exit_event.is_set():
            try:
                await self.dme_loop()
                await wait_for_next_loop(WAIT_TIMER_SHORT_TIMEOUT)

            except Exception as dolphinEx:
                logger.error("Something went wrong when connecting to Dolphin Memory Engine. Details:" + str(dolphinEx))

    def set_dolphin_status(self, status: str) -> None:
        """
        Set the dolphin status and log it to the client.

        Args:
            status (str): The status that should be set and logged.
        """
        self.dolphin_status = status
        logger.info(self.dolphin_status)

    def on_deathlink(self, data: dict):
        super().on_deathlink(data)
        source = data.get('source', 'Unknown')
        cause = data.get('cause', 'No cause specified')
        logger.info(f"DeathLink received! Source: {source}")
        logger.info(f"DeathLink message: {cause}")
        logger.info("Killing Mario now...")
        self.has_receive_death = True
        self.kill_mario()

    def kill_mario(self):
        """Uses the same logic as Gecko code death trigger"""
        if self.slot is not None and dme.is_hooked() and self.dolphin_status == CONNECTION_CONNECTED_STATUS:
            dme.write_bytes(dme.follow_pointers(0x8040E178, [0x4C]),
                (0x4020).to_bytes(2, byteorder="big"))
        return

    def make_gui(self):
        # Performing local import to prevent additional UIs to appear during the patching process.
        # This appears to be occurring if a spawned process does not have a UI element when importing kvui/kivymd.
        from .sms_tab import build_gui, GameManager, MDLabel

        ui: type[GameManager] = super().make_gui()
        class SMSGuiWrapper(ui):
            shine_count: MDLabel
            blue_coins: MDLabel
            tickets: MDLabel
            base_title = "Super Mario Sunshine Client"

            def build(self):
                container = super().build()

                self.base_title += " |  Archipelago"
                build_gui(self)

                return container

            def update_corona_shine_count(self, shine_count: int, shines_required: int):
                self.shine_count.text = f"{shine_count} / {shines_required}"

            def update_blue_coins(self, blue_coins: int, coins_req: int):
                self.blue_coins.text = f"{blue_coins} / {coins_req}"

            def update_ticket_list(self, ticket_list: set[str]):
                self.tickets.text = "; ".join(ticket_list)

        return SMSGuiWrapper

    async def handle_stages(self):
        # Gravi01  change to connection status
        next_stage = dme.read_byte(addresses.SMS_NEXT_STAGE)
        cur_stage = dme.read_byte(addresses.SMS_CURRENT_STAGE)
        current_episode = dme.read_byte(addresses.SMS_CURRENT_EPISODE)
        next_episode = dme.read_byte(addresses.SMS_NEXT_EPISODE)
        if next_stage == 0x01:  # Delfino Plaza
            # If starting Fluddless without ticket mode on, open Bianco Hills
            if self.starting_nozzle == 2 and self.ticket_mode == 0:
                self.open_stage(self.tickets[2])

            # Sets plaza state to 8 if in ticket mode and goal hasn't been reached
            if self.ticket_mode == 1 and next_episode != 0x8 and not self.corona_message_given:
                # Should change this to be flag based, set the flags necessary to load plaza 8 regardless
                dme.write_byte(addresses.SMS_NEXT_EPISODE, 8)

        if cur_stage != next_stage:
            await self.send_map_id(next_stage)
            if self.ticket_mode:
                if not self.tickets[next_stage].active:
                    logger.info("Entering a stage without a ticket! Initiating bootout...")
                    # Byte 1 should correspond to Delfino Plaza
                    dme.write_byte(addresses.SMS_NEXT_STAGE, 1)
                    dme.write_byte(addresses.SMS_CURRENT_STAGE, 1)
                    await self.send_map_id(1)

        if (next_stage < 0x0D and next_stage != 0x07) and (next_episode != current_episode) and (next_episode != 0xFF):
            next_episode = dme.read_byte(addresses.SMS_NEXT_EPISODE)
            if next_stage == 0x01:
                await self.send_episode_id(-1)
            else:
                await self.send_episode_id(next_episode)
        elif next_stage >= 0x0D:
            await self.send_episode_id(-1)

    def open_stage(self, ticket):
        byte_value = bit_flagger(dme.read_byte(ticket.address), ticket.bit_position, True)
        dme.write_byte(ticket.address, byte_value)

    # Checks to see if player changed stages to update map_id for Poptracker
    async def send_map_id(self, map_id):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"sms_map_{self.team}_{self.slot}",
            "default": 0,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": map_id}]
        }])

    async def send_episode_id(self, episode_id):
        await self.send_msgs([{
            "cmd": "Set",
            "key": f"sms_episode_{self.team}_{self.slot}",
            "default": 0,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": episode_id}]
        }])

    async def location_watcher(self):
        shine_byte_list: int = int.from_bytes(dme.read_bytes(dme.follow_pointers(
            addresses.SMS_FLAGS_PTR, [0x0]), addresses.SMS_SHINE_BYTE_COUNT))

        bc_byte_list: int = int.from_bytes(dme.read_bytes(dme.follow_pointers(
            addresses.SMS_FLAGS_PTR, [addresses.BLUECOIN_LOC_OFFSET]), addresses.SMS_BLUECOIN_BYTE_COUNT))

        nb_byte_list: int = int.from_bytes(dme.read_bytes(dme.follow_pointers(
            addresses.SMS_FLAGS_PTR, [addresses.NOZZLE_BOXES_OFFSET]), addresses.NOZZLE_BOXES_BYTE_COUNT))

        local_missing_locs = copy.deepcopy(self.missing_locations)
        for mis_loc_id in local_missing_locs:
            # Get the loc name, then I can get Region name + Shine Name / Blue Coin / Nozzle Box
            loc_full_name = self.location_names.lookup_in_game(mis_loc_id)
            sms_reg = ALL_REGIONS[loc_full_name.split(" - ")[0]]
            loc_name = loc_full_name.split(" - ")[1]

            # If the location is a shine
            if sms_reg.shines and any([shine for shine in sms_reg.shines if loc_name in shine.name]):
                in_game_bit: int = [shine.in_game_bit for shine in sms_reg.shines if loc_name in shine.name][0]
                if (shine_byte_list & (1 << in_game_bit)) > 0:
                    self.locations_checked.add(mis_loc_id)

            # If the location is a blue coin
            elif sms_reg.blue_coins and any([bc for bc in sms_reg.blue_coins if loc_name in bc.name]):
                in_game_bit: int = [bc.in_game_bit for bc in sms_reg.blue_coins if loc_name in bc.name][0]
                if (bc_byte_list & (1 << in_game_bit)) > 0:
                    self.locations_checked.add(mis_loc_id)

            # If the location is a nozzle box
            elif sms_reg.nozzle_boxes and any([nb for nb in sms_reg.nozzle_boxes if loc_name in nb.name]):
                in_game_bit: int = [nb.in_game_bit for nb in sms_reg.nozzle_boxes if loc_name in nb.name][0]
                if (nb_byte_list & (1 << in_game_bit)) > 0:
                    self.locations_checked.add(mis_loc_id)

        # Check corresponds to Shadow Mario Yoshi Egg Chase
        # delfino_yoshi_unlock = dme.read_byte(dme.read_word(addresses.SMS_FLAGS_PTR) + addresses.DELFINO_YOSHI_OFFSET)
        # if (delfino_yoshi_unlock & 0x80) and not ctx.checked_yoshi_egg:
        #     ctx.checked_yoshi_egg = True
        #     memory_changed(ctx, 113, delfino_yoshi_unlock, "Yoshi") # Swapped to self.locations_checked.add()

        await self.check_locations(self.locations_checked)

    async def check_death(self):
        """Check if Mario died by checking if in the 'Mario is dying' game mode, then send DeathLink."""
        game_state = dme.read_byte(addresses.GAME_STATE)

        # Check to see if Mario is dying
        if game_state == 7:

            # Only sends a death link if they are the person dying and have not been sent a death link
            if not self.has_send_death and not self.has_receive_death:
                player_name = self.player_names[self.slot]
                await self.send_death(f"{player_name} died!")
                logger.info(f"Sent DeathLink: Mario died")

            # Set variables to combat niche cases where a death link is sent during an abnormal time
            # i.e. game paused, cutscene, shine get, etc.
            self.has_send_death = True
            self.has_receive_death = False

        # Allows for death links to be sent once respawned
        elif game_state == 4:
            self.has_send_death = False

    def sms_give_items(self):
        #TODO Read the last received index from save ram somewhere around here
        for item_id in self.items_received[self.send_index:]:
            item_name = self.item_names.lookup_in_game(item_id)

            if item_name in REGULAR_PROGRESSION_ITEMS.keys():
                if item_name == "Yoshi":
                    activate_yoshi(ctx)
                else:
                    activate_nozzle(item, ctx)
            elif item_name in TICKET_ITEMS:
                activate_ticket(item)
            elif item_name == "Shine Sprite":
                ...
            elif item_name == "Blue Coin":
                ...
            elif item_name == "1 Up":
                increase_lives(ctx)

    def activate_nozzle(self, id):
        if id == 523000:
            if not ctx.ap_nozzles_received.__contains__(0):
                ctx.ap_nozzles_received.append(0)
        elif id == 523001:
            if not ctx.ap_nozzles_received.__contains__(1):
                ctx.ap_nozzles_received.append(1)
        elif id == 523002:
            if not ctx.ap_nozzles_received.__contains__(2):
                ctx.ap_nozzles_received.append(2)
            # rocket nozzle
        elif id == 523003:
            if not ctx.ap_nozzles_received.__contains__(3):
                ctx.ap_nozzles_received.append(3)
            # turbo nozzle
        return

    def activate_yoshi(self):
        dme.write_byte(0x80417A03, 0x01)
        if not ctx.ap_nozzles_received.__contains__(4):
            ctx.ap_nozzles_received.append(4)
        return

    # Makes filler 1-UP items actually give lives
    # As of now, your life count is increased by 1 if you close the client and reconnect if you already have more than one 1-UP sent
    def increase_lives(self):
        num_1_ups = sum(1 for item in ctx.items_received if ctx.item_names.lookup_in_game(item.item) == "1-UP")
        current_lives = dme.read_word(dme.read_word(addresses.SMS_FLAGS_PTR) + addresses.LIVES_COUNT_OFFSET)

        # Only increase lives a single time when a 1-UP is received
        if ctx.num_1_ups_current != num_1_ups:
            ctx.num_1_ups_current = num_1_ups

            if current_lives < 99 and num_1_ups > 0:
                dme.write_word(dme.read_word(addresses.SMS_FLAGS_PTR) + addresses.LIVES_COUNT_OFFSET, current_lives + 1)
        return

    def send_victory(self):
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
        # logger.info("DoubleDubbel - The Incredible Name For The Randomizer ISO")
        # time.sleep(.05)
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

    async def arbitrary_ram_checks(self):
        while not ctx.exit_event.is_set():
            if not dme.is_hooked() or ctx.slot is None:
                await asyncio.sleep(5)
                continue

            activated_bits = dme.read_byte(addresses.ARB_NOZZLES_ENABLER)

            for noz in ctx.ap_nozzles_received:
                if noz < 4:
                    activated_bits = bit_flagger(activated_bits, noz, True)
                    dme.write_byte(addresses.ARB_FLUDD_ENABLER, 0x1)
                    dme.write_byte(addresses.ARB_NOZZLES_ENABLER, activated_bits)
            await asyncio.sleep(DELAY_SECONDS)


async def wait_for_next_loop(time_to_wait: float) -> None:
    await asyncio.sleep(time_to_wait)

def main(*launch_args: str):
    import colorama
    from .iso_helper.sms_rom import SMSPatch
    server_address: str = ""

    parser = get_base_parser()
    parser.add_argument("apsms_file", default="", type=str, nargs="?", help="Path to a APSMS File")
    args = parser.parse_args(launch_args)

    if args.apsms_file:
        sms_patch = SMSPatch()
        try:
            sms_manifest = sms_patch.read_contents(args.apsms_file)
            server_address = sms_manifest["server"]
            sms_patch.patch(args.apsms_file)
        except Exception as ex:
            logger.error("Unable to patch your Super Mario Sunshine. Additional Details:\n" + str(ex))
            Utils.messagebox("Cannot Patch Super Mario Sunshine", "Unable to patch your Super Mario Sunshine ROM as " +
                "expected. Additional details:\n" + str(ex), True)
            raise ex

    async def _main(connect, password):
        ctx = SmsContext(server_address if server_address else connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        if TRACKER_LOADED:
            ctx.run_generator()
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(ctx.dolphin_loop(), name="SmsDolphinSync")

        #TODO this can probably just be done in the dme_loop.
        arbitrary = asyncio.create_task(arbitrary_ram_checks(ctx), name="SmsArbitraryWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

        if arbitrary:
            await arbitrary

    colorama.just_fix_windows_console()
    asyncio.run(_main(args.connect, args.password))
    colorama.deinit()


if __name__ == "__main__":
    Utils.init_logging("SMSClient", exception_logger="Client")
    main(*sys.argv[1:])