from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from .user import User

from .base import BaseModel


class DebateMotion(BaseModel):
    class Meta:
        table = "debate_motions"

    infoslide = fields.CharField(max_length=255, null=True)
    text = fields.TextField()

    created_by: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User", related_name="motions", on_delete=fields.CASCADE
    )
