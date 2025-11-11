from bot.models import DebateGame

from .base_repository import BaseRepository


class DebateGameRepository(BaseRepository[DebateGame]):
    def __init__(self):
        super().__init__(DebateGame)
