import location_watch
import asyncio
import time


def main():
    async def _main():
        loc_watch = asyncio.create_task(location_watch.location_watcher(True))

        await loc_watch

    location_watch.game_start()
    asyncio.run(_main())
    