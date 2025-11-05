import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.routers import setup_routers
from config import settings
from db import close_db, init_db

load_dotenv()

bot = Bot(token=settings.bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(setup_routers())


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    try:
        # Initialize database
        await init_db()

        # Start polling
        await dp.start_polling(bot)
    finally:
        # Cleanup database connections
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
