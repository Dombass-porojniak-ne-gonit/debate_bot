import asyncio
import logging

from aiogram import Bot


class TelegramLogHandler(logging.Handler):
    def __init__(self, bot: Bot, chat_id: str):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id
        self._queue: asyncio.Queue = asyncio.Queue()
        self._task: asyncio.Task | None = None

    def emit(self, record: logging.LogRecord) -> None:
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self._process_queue())

        try:
            self._queue.put_nowait(record)
        except asyncio.QueueFull:
            pass

    async def _process_queue(self) -> None:
        while True:
            try:
                record = await self._queue.get()
                await self._send_log_to_telegram(record)
                self._queue.task_done()
            except asyncio.CancelledError:
                break
            except Exception:
                pass

    async def _send_log_to_telegram(self, record: logging.LogRecord) -> None:
        try:
            message = self.format(record)
            max_length = 4000
            if len(message) > max_length:
                message = message[:max_length] + "\n\n[Message truncated due to length]"

            await self.bot.send_message(
                chat_id=self.chat_id,
                text=f"🤖 <b>Bot Log</b>\n\n{message}",
                parse_mode="HTML",
            )
        except Exception as e:
            # Last resort error handling - don't let logging crash the bot
            print(f"Failed to send log to Telegram: {e}")
