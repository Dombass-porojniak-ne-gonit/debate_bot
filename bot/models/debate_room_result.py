from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .debate_team import DebateTeam
from .user import User

from .base import BaseModel


class DebateRoomResult(BaseModel):
    class Meta:
        table = "debate_room_result"

    room: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.DebateRoom", related_name="results", on_delete=fields.CASCADE
    )
    winning_team: ForeignKeyFieldInstance[DebateTeam] | None = fields.ForeignKeyField(
        "models.DebateTeam", related_name="wins", null=True
    )
    feedback = fields.TextField(null=True)
    submitted: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="submitted_results"
    )
