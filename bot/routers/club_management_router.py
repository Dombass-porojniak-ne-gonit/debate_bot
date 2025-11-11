"""
Club management router.

Handles club creation, management, and membership operations.
"""

from aiogram import F, Router
from aiogram.filters import JOIN_TRANSITION, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated

router = Router(name="club_management_router")


# TODO: Implement club management commands:
# - /my_clubs - Show user's clubs


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION),
    F.chat.type.in_(["group", "supergroup"]),
)
async def bot_added_to_group(event: ChatMemberUpdated) -> None:
    """Handle bot being added to a group/supergroup."""
    chat = event.chat
    await event.answer(f"👋 Привіт {chat.title}")
