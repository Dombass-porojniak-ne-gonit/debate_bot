from bot.models import DebateClub

from .base_repository import BaseRepository


class DebateClubRepository(BaseRepository[DebateClub]):
    def __init__(self):
        super().__init__(DebateClub)

    async def get_by_telegram_id(self, telegram_id: int) -> DebateClub | None:
        return await self.model.filter(telegram_id=telegram_id).first()

    async def search_by_name(
        self, query: str, limit: int = 10, offset: int = 0
    ) -> list[DebateClub]:
        """case-insensitive"""
        return (
            await self.model.filter(name__icontains=query)
            .limit(limit)
            .offset(offset)
            .all()
        )
