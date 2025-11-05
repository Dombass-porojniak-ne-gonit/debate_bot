from bot.models import DebateRoomResult

from .base import BaseRepository


class ResultRepository(BaseRepository[DebateRoomResult]):
    def __init__(self):
        super().__init__(DebateRoomResult)


# TODO: get by judge, room, add results for room with uniquness validation
