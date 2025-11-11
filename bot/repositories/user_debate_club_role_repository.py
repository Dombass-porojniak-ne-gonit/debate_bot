from uuid import UUID

from bot.models import UserDebateClubRole
from bot.models.enums import ClubRoleEnum

from .base_repository import BaseRepository


class UserDebateClubRoleRepository(BaseRepository[UserDebateClubRole]):
    def __init__(self):
        super().__init__(UserDebateClubRole)

    async def bulk_create_roles(
        self, user_ids: list[UUID], debate_club_id: UUID, role: ClubRoleEnum
    ) -> list[UserDebateClubRole] | None:
        roles = [
            UserDebateClubRole(
                user_id=user_id, debate_club_id=debate_club_id, role=role
            )
            for user_id in user_ids
        ]
        return await self.model.bulk_create(roles)
