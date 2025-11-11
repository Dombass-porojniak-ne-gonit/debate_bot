from bot.models import DebateClub
from bot.repositories import DebateClubRepository, UserRepository


class DebateClubService:
    def __init__(
        self, club_repo: DebateClubRepository, user_repo: UserRepository
    ) -> None:
        self.club_repo = club_repo
        self.user_repo = user_repo

    async def create_club(
        self,
        telegram_id: int,
        name: str,
        description: str,
        telegram_link: str,
        creator_telegram_id: int,
    ) -> DebateClub:
        existing_club = await self.club_repo.get_by_telegram_id(telegram_id)
        if existing_club:
            return existing_club

        new_debate_club = await self.club_repo.create(
            telegram_id=telegram_id,
            name=name,
            description=description,
            telegram_link=telegram_link,
            creator_telegram_id=creator_telegram_id,
        )
        if not new_debate_club:
            raise RuntimeError("Failed to create debate club")
        return new_debate_club


# TODO: update role, add to club, get club members
