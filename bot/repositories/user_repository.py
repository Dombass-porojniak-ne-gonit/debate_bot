from bot.models import User

from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self) -> None:
        super().__init__(User)

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        return await self.model.filter(telegram_id=telegram_id).first()
