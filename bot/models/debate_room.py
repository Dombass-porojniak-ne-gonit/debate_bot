from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .debate_game import DebateGame
from .debate_motion import DebateMotion
from .user import User

from .base import BaseModel


class DebateRoom(BaseModel):
    class Meta:
        table = "debate_room"

    game: ForeignKeyFieldInstance[DebateGame] = fields.ForeignKeyField(
        "models.DebateGame", related_name="rooms", on_delete=fields.CASCADE
    )
    motion: ForeignKeyFieldInstance[DebateMotion] | None = fields.ForeignKeyField(
        "models.DebateMotion", related_name="game_rooms", null=True
    )
    adjudicator: ForeignKeyFieldInstance[User] | None = fields.ForeignKeyField(
        "models.User", related_name="adjudicated_rooms", null=True
    )
