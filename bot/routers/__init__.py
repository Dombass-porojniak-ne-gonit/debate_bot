from aiogram import Router

from .club_router import router as club_router
from .common_router import router as common_router
from .game_router import router as game_router
from .motion_router import router as motion_router
from .room_router import router as room_router


def setup_routers() -> Router:
    root_router = Router(name="root")

    root_router.include_routers(
        common_router,  # General commands like /start, /help
        club_router,  # Club management
        game_router,  # Debate game management
        room_router,  # Debate room management
        motion_router,  # Motion-related commands
    )

    return root_router


__all__ = [
    "setup_routers",
    "common_router",
    "club_router",
    "game_router",
    "room_router",
    "motion_router",
]

# NOTE: Probably will split routers
