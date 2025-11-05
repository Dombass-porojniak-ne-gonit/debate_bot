from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="motion_router")


@router.message(Command("create_motion"))
async def cmd_create_motion(message: Message) -> None:
    # TODO: Implement /create_motion command (multi-step)
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("get_my_motions"))
async def cmd_get_my_motions(message: Message) -> None:
    # TODO: Implement /get_my_motions command
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("random_motion"))
async def cmd_random_motion(message: Message) -> None:
    # TODO: Implement /random_motion command
    await message.answer(
        "Not yet implemented",
    )
