import typing
import worlds.sms.dolphin.location_watch as location_watch
import asyncio
import worlds.sms.dolphin.item_receiver as item_receiver
from CommonClient import CommonContext, ClientCommandProcessor

global smsComProc


class SmsCommandProcessor(ClientCommandProcessor):
    def _cmd_received(self) -> bool:
        for index, item in enumerate(self.ctx.items_received, 1):
            item_receiver.unpack_item(self.ctx.items_received[item.item])
        return super()._cmd_received()

    def send_location_checks(self, check_ids):
        self.ctx.send_msgs([{"cmd": "LocationChecks", "locations": [check_ids]}])


class SmsContext(CommonContext):
    command_processor: typing.Type[ClientCommandProcessor] = SmsCommandProcessor
    game = "Super Mario Sunshine"


def main():

    async def _main():
        loc_watch = asyncio.create_task(location_watch.location_watcher(True))

        await loc_watch

    location_watch.game_start()
    asyncio.run(_main())



