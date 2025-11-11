from bot.models.debate_motion import DebateMotion

from .base_repository import BaseRepository


class DebateMotionRepository(BaseRepository[DebateMotion]):
    def __init__(self) -> None:
        super().__init__(DebateMotion)

    async def get_by_user(self, user_id: int, limit: int = 50, offset: int = 0):
        return await (
            self.model.filter(created_by_id=user_id)
            .limit(limit)
            .offset(offset)
            .prefetch_related("created_by")
        )
