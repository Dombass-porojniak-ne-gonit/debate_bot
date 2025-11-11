from bot.models import DebateRoomResult

from .base_repository import BaseRepository


class DebateRoomResultRepository(BaseRepository[DebateRoomResult]):
    def __init__(self):
        super().__init__(DebateRoomResult)


# TODO: get by judge, room, add results for room with uniquness validation
