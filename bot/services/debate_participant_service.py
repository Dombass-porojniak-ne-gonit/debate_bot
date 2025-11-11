from bot.repositories import DebateParticipantRepository


class DebateParticipantService:
    def __init__(self, participant_repo: DebateParticipantRepository) -> None:
        self.participant_repo = participant_repo


# TODO: get by game, get by user, is registered, count by role (required for game registration logic)
