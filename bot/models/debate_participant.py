from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .debate_game import DebateGame
from .debate_team import DebateTeam
from .user import User

from .base import BaseModel
from .enums import ParticipantRole


class DebateParticipant(BaseModel):
    class Meta:
        table = "debate_participant"
        unique_together = ("user", "game")

    user: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="debate_participations"
    )
    team: ForeignKeyFieldInstance[DebateTeam] | None = fields.ForeignKeyField(
        "models.DebateTeam", related_name="participants", null=True
    )
    game: ForeignKeyFieldInstance[DebateGame] = fields.ForeignKeyField(
        "models.DebateGame", related_name="players"
    )
    role = fields.IntEnumField(ParticipantRole, default=ParticipantRole.DEBATER)
    speaker_points = fields.IntField(null=True)
