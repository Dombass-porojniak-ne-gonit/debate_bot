import asyncio
import logging
from typing import Any, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

from bot.utils.bot_logging import TelegramLogHandler
from config import settings


class BaseLoggingMiddleware(BaseMiddleware):
    """Base for logging middlewares."""

    _initialized = False

    async def __call__(
        self,
        handler,
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not self._initialized:
            await self._setup_logging()
            self._initialized = True

        try:
            return await handler(event, data)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Unhandled error in handler: {e}", exc_info=True)
            raise

    async def _setup_logging(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass


class ConsoleLoggingMiddleware(BaseLoggingMiddleware):
    """Console logging middleware."""

    async def _setup_logging(self) -> None:
        """Set up console logging."""
        root_logger = logging.getLogger()

        if not any(isinstance(h, logging.StreamHandler) for h in root_logger.handlers):
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
            )
            handler.setLevel(logging.DEBUG)
            root_logger.addHandler(handler)
            root_logger.setLevel(logging.DEBUG)
            print("Console logging enabled.")


class TelegramLoggingMiddleware(BaseLoggingMiddleware):
    """Telegram logging middleware."""

    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot
        self._handler: TelegramLogHandler | None = None

    async def _setup_logging(self) -> None:
        """Set up Telegram logging."""
        if not settings.devel_chat_id:
            print("DEVEL_CHAT_ID not configured. Telegram logging disabled.")
            return

        self._handler = TelegramLogHandler(self.bot, settings.devel_chat_id)
        self._handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s\n%(message)s")
        )
        self._handler.setLevel(logging.WARNING)  # NOTE: Logging level for tg

        root_logger = logging.getLogger()
        root_logger.addHandler(self._handler)
        print("Telegram logging enabled.")

    async def shutdown(self) -> None:
        """Shutdown Telegram handler."""
        if self._handler and hasattr(self._handler, "_task") and self._handler._task:
            self._handler._task.cancel()
            try:
                await self._handler._task
            except asyncio.CancelledError:
                pass
