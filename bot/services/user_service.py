import logging

from bot.models import User
from bot.repositories import UserRepository
from bot.utils.exceptions import UserNotFoundException

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def register_user(
        self,
        telegram_id: int,
        first_name: str | None = None,
        last_name: str | None = None,
        username: str | None = None,
        phone_number: str | None = None,
        language: str = "ua",
    ) -> User:
        existing_user = await self.user_repo.get_by_telegram_id(telegram_id)
        if existing_user:
            logger.info(f"New user registered: {telegram_id}")
            return existing_user
        user = await self.user_repo.create(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number,
            language=language,
        )
        if not user:
            raise UserNotFoundException(f"Failed to create user {telegram_id}")

        logger.info(f'New user Id: "{user.id}" registered: {telegram_id}')
        return user
