from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .base import BaseModel
from .debate_club import DebateClub
from .enums import GameStatusEnum
from .user import User


class DebateGame(BaseModel):
    class Meta:
        table = "debate_game"

    debate_club: ForeignKeyFieldInstance[DebateClub] = fields.ForeignKeyField(
        "models.DebateClub", related_name="games", on_delete=fields.CASCADE
    )
    telegram_group_message_id = fields.BigIntField(unique=True)

    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    status = fields.CharEnumField(
        GameStatusEnum, default=GameStatusEnum.REGISTRATION, max_length=20
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
