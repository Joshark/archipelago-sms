import location_watch
import asyncio
import time
from .locations import SmsLocation

myContext = new SmsContext()
myComProc = new CommonCommandProcessor()

class SmsContext(CommonContext):
    self.send_msgs()

def main():
    async def _main():
        loc_watch = asyncio.create_task(location_watch.location_watcher(True))

        await loc_watch

    location_watch.game_start()
    asyncio.run(_main())

def send_location_checks(check_ids):
    self.send_msgs([{cmd: "LocationChecks", locations: [check_ids]}])
