from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="game_router")


@router.message(Command("create_game"))
async def cmd_create_game(message: Message) -> None:
    # TODO: Implement /create_game command (multi-step)
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("join_game"))
async def cmd_join_game(message: Message) -> None:
    # TODO: Implement /join_game command
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("my_games"))
async def cmd_my_games(message: Message) -> None:
    # TODO: Implement /my_games command
    await message.answer(
        "Not yet implemented",
    )


@router.message(Command("game_status"))
async def cmd_game_status(message: Message) -> None:
    # TODO: Implement /game_status command (most likely will be moved to keyboard button)
    await message.answer(
        "Not yet implemented",
    )
