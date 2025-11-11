from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .base import BaseModel
from .debate_club import DebateClub
from .enums import ClubRoleEnum
from .user import User


class UserDebateClubRole(BaseModel):
    class Meta:
        table = "user_debate_club_role"
        unique_together = ("user", "debate_club")

    role = fields.IntEnumField(ClubRoleEnum, default=ClubRoleEnum.MEMBER, max_length=50)
    user: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="debate_club_roles"
    )
    debate_club: ForeignKeyFieldInstance[DebateClub] = fields.ForeignKeyField(
        "models.DebateClub", related_name="members"
    )
