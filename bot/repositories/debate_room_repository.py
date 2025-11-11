from bot.models import DebateRoom

from .base_repository import BaseRepository


class DebateRoomRepository(BaseRepository[DebateRoom]):
    def __init__(self):
        super().__init__(DebateRoom)


# TODO: get all rooms for a game
# WARNING: Deleting a room cascades to teams and results due to on_delete=CASCADE
