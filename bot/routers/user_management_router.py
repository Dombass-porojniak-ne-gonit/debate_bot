"""
User management router.

Handles general user commands and profile management.
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="user_management_router")


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Handle /help command."""
    await message.answer(
        "📚 Доступні команди:\n\n/start - Старт (Реєстрація)\n/help - Показати це повідомлення"
    )


# TODO: User stats
