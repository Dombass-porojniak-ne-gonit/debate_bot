from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="club_router")


@router.message(Command("create_club"))
async def cmd_create_club(message: Message) -> None:
    if message.chat.type == "private":
        await message.answer(
            "Not yet implemented",
        )
        return

    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("club_info"))
async def cmd_club_info(message: Message) -> None:
    if message.chat.type == "private":
        await message.answer(
            "Not yet implemented",
        )
        return

    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("my_clubs"))
async def cmd_my_clubs(message: Message) -> None:
    await message.answer(
        "Not yet implemented",
    )
