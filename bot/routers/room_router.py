from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="room_router")


@router.message(Command("create_room"))
async def cmd_create_room(message: Message) -> None:
    # TODO: Implement /create_room command (most likely will be moved to keyboard button)
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("list_rooms"))
async def cmd_list_rooms(message: Message) -> None:
    # TODO: Implement /list_rooms command (will be keyboard/message as part of game formatting)
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("room_results"))
async def cmd_room_results(message: Message) -> None:
    # TODO: Implement /room_results command (keyboard)
    await message.answer(
        "Not yet implemented",
    )
