import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.exceptions import CobaltURLError
from bot.handlers import setup
from bot.cobalt import CobaltAPI
from bot import log



load_dotenv()
storage = MemoryStorage()
bot = Bot(
    token=os.getenv("TOKEN"),
    default=DefaultBotProperties(parse_mode="HTML")
)

def get_bot():
    return bot


async def on_startup():
    cobalt = CobaltAPI()
    if not cobalt.status():
        raise CobaltURLError("Cobalt API not worked")
    log.info("Cobalt API worked")


async def main():
    dp = Dispatcher(storage=storage)
    router = setup()
    await on_startup()
    dp.include_router(router)
    await dp.start_polling(bot)
    try:
        await asyncio.Event().wait()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())