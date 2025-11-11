import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.middlewares.dependencies import DependencyInjectionMiddleware
from bot.middlewares.logging import ConsoleLoggingMiddleware, TelegramLoggingMiddleware
from bot.routers import setup_routers
from config import settings
from db import close_db, init_db

load_dotenv()

bot = Bot(token=settings.bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Setup middlewares
dp.message.middleware(ConsoleLoggingMiddleware())
dp.message.middleware(TelegramLoggingMiddleware(bot))
dp.message.middleware(DependencyInjectionMiddleware())
dp.callback_query.middleware(ConsoleLoggingMiddleware())
dp.callback_query.middleware(TelegramLoggingMiddleware(bot))
dp.callback_query.middleware(DependencyInjectionMiddleware())
dp.chat_member.middleware(DependencyInjectionMiddleware())

dp.include_router(setup_routers())


async def main() -> None:
    try:
        # Initialize database
        await init_db()

        await dp.start_polling(bot)
    finally:
        # Cleanup database connections
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
