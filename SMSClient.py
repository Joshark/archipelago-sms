from __future__ import annotations
import os
import sys
import asyncio
import shutil

import typing
import worlds.sms.dolphin.location_watch as location_watch
import worlds.sms.dolphin.item_receiver as item_receiver

import ModuleUpdate
ModuleUpdate.update()

import Utils

if __name__ == "__main__":
    Utils.init_logging("SMSClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop


class SmsCommandProcessor(ClientCommandProcessor):

    def _cmd_connect(self, address: str = "") -> bool:
        temp = super()._cmd_connect()
        if temp:
            self._cmd_resync()
            return True
        else:
            return False

    def _cmd_resync(self):
        """Manually trigger a resync."""
        item_receiver.initialize_nozzles()
        self.output(f"Syncing items.")
        self.ctx.syncing = True
        item_receiver.refresh_collection_counts(self.ctx)

    def _cmd_received(self) -> bool:
        for index, item in enumerate(self.ctx.items_received, 1):
            item_receiver.unpack_item(self.ctx.items_received[item.item], self.ctx)
        return super()._cmd_received()


class SmsContext(CommonContext):
    command_processor: int = SmsCommandProcessor
    game = "Super Mario Sunshine"
    items_handling = 0b111  # full remote

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


async def game_watcher(ctx: SmsContext):
    from worlds.sms.locations import ALL_LOCATIONS_TABLE
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
        await asyncio.sleep(0.1)


if __name__ == '__main__':

    location_watch.game_start()

    async def main(args):
        ctx = SmsContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        loc_watch = asyncio.create_task(location_watch.location_watcher(ctx))
        item_locker = asyncio.create_task(item_receiver.disable_nozzle("Hover Nozzle"))
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="SmsProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await loc_watch
        await item_locker
        await progression_watcher
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Super Mario Sunshine Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
