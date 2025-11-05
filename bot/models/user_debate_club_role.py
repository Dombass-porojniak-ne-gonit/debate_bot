from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .debate_club import DebateClub
from .user import User

from .base import BaseModel
from .enums import ClubRole


class UserDebateClubRole(BaseModel):
    class Meta:
        table = "user_debate_club_role"
        unique_together = ("user", "debate_club")

    role = fields.IntEnumField(ClubRole, default=ClubRole.MEMBER, max_length=50)
    user: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="debate_club_roles"
    )
    debate_club: ForeignKeyFieldInstance[DebateClub] = fields.ForeignKeyField(
        "models.DebateClub", related_name="members"
    )
