import location_watch
import asyncio
import time
import item_receiver
from .locations import SmsLocation

myContext = new SmsContext()
myComProc = new SmsCommandProcessor()

class SmsContext(CommonContext):
    

class SmsCommandProcessor(CommonCommandProcessor):
    def _cmd_received(self) -> bool:
        for index, item in enumerate(self.ctx.items_received, 1):
            item_receiver.unpack_item(self.ctx.items_received[item.item])
        super()._cmd_received(self)


def main():
    async def _main():
        loc_watch = asyncio.create_task(location_watch.location_watcher(True))

        await loc_watch

    location_watch.game_start()
    asyncio.run(_main())

def send_location_checks(check_ids):
    self.send_msgs([{cmd: "LocationChecks", locations: [check_ids]}])

