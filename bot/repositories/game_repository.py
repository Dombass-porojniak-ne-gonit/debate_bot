from bot.models import DebateGame

from .base import BaseRepository


class GameRepository(BaseRepository[DebateGame]):
    def __init__(self):
        super().__init__(DebateGame)
