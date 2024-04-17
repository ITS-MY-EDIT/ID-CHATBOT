import asyncio
import importlib

from pyrogram import idle

from SACHINxSANATANI import LOGGER, SACHIN
from SACHINxSANATANI.modules import ALL_MODULES


async def anony_boot():
    try:
        await SACHIN.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("SACHINxSANATANI.modules." + all_module)

    LOGGER.info(f"♥︎ @{SACHIN.username} STARTED.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("♥︎ BOT HAS BEEN STOPED...")
  
