from bot.models import DebateTeam

from .base import BaseRepository


class TeamRepository(BaseRepository[DebateTeam]):
    def __init__(self):
        super().__init__(DebateTeam)


# TODO: get_by_room, is team full, is iron, get participants
