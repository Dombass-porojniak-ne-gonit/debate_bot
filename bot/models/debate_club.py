from tortoise import fields

from .base import BaseModel


class DebateClub(BaseModel):
    class Meta:
        table = "debate_club"

    telegram_id = fields.BigIntField(unique=True)
    telegram_link = fields.CharField(max_length=255)

    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    total_games = fields.IntField(default=0)
