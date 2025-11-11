from bot.repositories import (
    DebateClubRepository,
    DebateGameRepository,
    DebateParticipantRepository,
    UserRepository,
)


class DebateGameService:
    def __init__(
        self,
        debate_game_repo: DebateGameRepository,
        debate_club_repo: DebateClubRepository,
        user_repo: UserRepository,
        participant_repo: DebateParticipantRepository,
    ) -> None:
        self.debate_game_repo = debate_game_repo
        self.debate_club_repo = debate_club_repo
        self.user_repo = user_repo
        self.participant_repo = participant_repo


# TODO: create game, registration, withdrawal, status change
