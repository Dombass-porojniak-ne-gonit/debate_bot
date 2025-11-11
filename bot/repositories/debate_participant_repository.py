from bot.models import DebateParticipant

from .base_repository import BaseRepository


class DebateParticipantRepository(BaseRepository[DebateParticipant]):
    def __init__(self):
        super().__init__(DebateParticipant)


# TODO: get by game, get by user, is registered, count by role (required for game registration logic)
