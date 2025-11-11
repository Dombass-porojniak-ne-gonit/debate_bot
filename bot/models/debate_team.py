from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .base import BaseModel
from .debate_room import DebateRoom
from .enums import DebateTeamPositionEnum


class DebateTeam(BaseModel):
    class Meta:
        table = "debate_team"

    room: ForeignKeyFieldInstance[DebateRoom] = fields.ForeignKeyField(
        "models.DebateRoom", related_name="teams", on_delete=fields.CASCADE
    )

    position = fields.IntEnumField(DebateTeamPositionEnum, default=None, null=True)

    rank = fields.IntField(null=True)
