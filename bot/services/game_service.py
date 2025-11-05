from bot.repositories import (
    DebateClubRepository,
    GameRepository,
    ParticipantRepository,
    UserRepository,
)


class GameService:
    def __init__(
        self,
        debate_game_repo: GameRepository,
        debate_club_repo: DebateClubRepository,
        user_repo: UserRepository,
        participant_repo: ParticipantRepository,
    ) -> None:
        self.debate_game_repo = debate_game_repo
        self.debate_club_repo = debate_club_repo
        self.user_repo = user_repo
        self.participant_repo = participant_repo


# TODO: create game, registration, withdrawal, status change
