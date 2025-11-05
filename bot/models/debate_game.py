from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .debate_club import DebateClub
from .user import User

from .base import BaseModel
from .enums import GameStatus


class DebateGame(BaseModel):
    class Meta:
        table = "debate_game"

    debate_club: ForeignKeyFieldInstance[DebateClub] = fields.ForeignKeyField(
        "models.DebateClub", related_name="games", on_delete=fields.CASCADE
    )

    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    status = fields.CharEnumField(
        GameStatus, default=GameStatus.REGISTRATION, max_length=20
    )
    date = fields.DateField()
    time = fields.TimeField(null=True)
    registration_deadline = fields.DatetimeField(null=True)
    is_online = fields.BooleanField(default=False)
    location = fields.CharField(max_length=500, null=True)
    meeting_link = fields.CharField(max_length=500, null=True)

    created_by: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="created_games"
    )
