from aiogram import Router

from .admin_router import router as admin_router
from .club_management_router import router as club_management_router
from .common_router import router as common_router
from .debate_management_router import router as debate_management_router
from .user_management_router import router as user_management_router
from .user_registration_fsm_router import router as user_registration_fsm_router
from .user_registration_router import router as user_registration_router


def setup_routers() -> Router:
    """Set up all routers organized by functionality."""
    root_router = Router(name="root")

    # Include routers in logical order (most specific first)
    root_router.include_routers(
        # FSM routers (highest priority)
        user_registration_fsm_router,
        # Core routers
        user_registration_router,
        user_management_router,
        debate_management_router,
        club_management_router,
        admin_router,
        # fallback handlers
        common_router,
    )

    return root_router


__all__ = [
    # Setup function
    "setup_routers",
    # Routers
    "user_registration_router",
    "user_registration_fsm_router",
    "user_management_router",
    "debate_management_router",
    "club_management_router",
    "admin_router",
    "common_router",
]

# NOTE: Probably will split routers
